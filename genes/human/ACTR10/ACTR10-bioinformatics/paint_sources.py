"""Resolve the PAINT (IBA) WITH/FROM sources on ACTR10 and ask what each one knows.

Every IBA row in ``ACTR10-goa.tsv`` carries a ``WITH/FROM`` list of the tree
members whose annotations PAINT propagated to human ACTR10. Two questions decide
whether the propagation is sound, and neither can be answered from the GOA file:

1. **Who is the source?**  An ortholog transfer is legitimate; a transfer from a
   different actin-fold subfamily (a paralog such as a nuclear chromatin-remodelling
   Arp) is not. Resolution uses ``size=5`` and reports *every* hit, because a
   cross-reference that maps to several accessions is data, not an error --- and a
   ``size=1`` query would silently pick one and hide the ambiguity.
2. **Does the source itself carry experimental evidence for the propagated term?**
   QuickGO is asked directly. "The sources only carry the same family-level guess"
   is a testable claim, and IBA WITH/FROM lists experimentally-annotated members by
   construction, so it is usually false.

Swiss-Prot vs TrEMBL status is printed next to every name: an unreviewed entry's
protein *name* is an automatic by-similarity label and is not evidence of function,
even when that same entry carries real curated experimental GO annotations.

The source list is built FROM the GOA file, never by hand, and the per-row token
count is asserted against the file.
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

GOA_TSV = Path(__file__).resolve().parent.parent / "ACTR10-goa.tsv"

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}

# UniProt xref database token for each GOA WITH/FROM prefix. WormBase entries for
# this family have no reviewed record and are not indexed under xref:wormbase-*,
# so that prefix is resolved by free-text search over the gene id instead.
XREF_DB = {
    "MGI": "mgi",
    "SGD": "sgd",
    "CGD": "cgd",
    "RGD": "rgd",
    "ZFIN": "zfin",
    "dictyBase": "dictybase",
    "FB": "flybase",
    "TAIR": "araport",
}


def http_json(url: str, tries: int = 4) -> dict:
    """GET JSON, retrying on transient failure. A persistent failure is fatal."""
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url}") from last


@dataclass
class Candidate:
    accession: str
    reviewed: bool
    organism: str
    genes: list[str]
    name: str

    @property
    def status(self) -> str:
        return "Swiss-Prot" if self.reviewed else "TrEMBL"

    def render(self) -> str:
        gene = "/".join(self.genes) if self.genes else "-"
        return f"{self.accession} ({self.status}) {self.organism} {gene} :: {self.name}"


@dataclass
class Source:
    token: str
    kind: str  # "protein" | "tree-node"
    candidates: list[Candidate] = field(default_factory=list)
    note: str = ""
    # accession -> list of goEvidence codes QuickGO reports for the propagated term
    evidence: dict[str, list[str]] = field(default_factory=dict)

    @property
    def has_experimental(self) -> bool:
        return any(
            code in EXPERIMENTAL_CODES
            for codes in self.evidence.values()
            for code in codes
        )


def parse_entry(entry: dict) -> Candidate:
    desc = entry.get("proteinDescription", {})
    name = (
        desc.get("recommendedName", {}).get("fullName", {}).get("value")
        or "; ".join(
            s.get("fullName", {}).get("value", "") for s in desc.get("submissionNames", [])
        )
        or "(no name)"
    )
    return Candidate(
        accession=entry["primaryAccession"],
        reviewed=entry.get("entryType", "").endswith("(Swiss-Prot)"),
        organism=entry.get("organism", {}).get("scientificName", "?"),
        genes=[
            g["geneName"]["value"]
            for g in entry.get("genes", [])
            if g.get("geneName")
        ],
        name=name,
    )


FIELDS = "id,protein_name,gene_names,organism_name"


def uniprot_by_accession(acc: str) -> list[Candidate]:
    """Resolve one accession, flagging a redirect rather than aborting.

    A merged accession makes UniProt return the merge target's record, so the reply looks
    healthy while describing a different protein. Here the accession comes from the GOA
    WITH/FROM field rather than from a hand-written list, so a redirect is informative data
    about a stale GOA reference, not a code defect - it is reported, not raised.
    """
    entry = http_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields={FIELDS}")
    cand = parse_entry(entry)
    if cand.accession != acc:
        cand.name = (
            f"{cand.name} [WARNING: requested {acc}, UniProt returned {cand.accession} - "
            "accession has been merged or demerged]"
        )
    return [cand]


def uniprot_search(query: str) -> list[Candidate]:
    url = (
        "https://rest.uniprot.org/uniprotkb/search?"
        + urllib.parse.urlencode({"query": query, "fields": FIELDS, "size": 5})
    )
    return [parse_entry(e) for e in http_json(url).get("results", [])]


def resolve(token: str) -> Source:
    """Resolve one GOA WITH/FROM token to the protein(s) it denotes."""
    prefix, _, local = token.partition(":")
    if prefix == "PANTHER":
        return Source(
            token,
            "tree-node",
            note=(
                "internal PANTHER tree node, not a protein; records the ancestral "
                "node PAINT annotated, so it carries no independent evidence"
            ),
        )
    if prefix == "UniProtKB":
        return Source(token, "protein", candidates=uniprot_by_accession(local))
    if prefix == "MGI":
        # tokens arrive as MGI:MGI:1891654; xref lookup needs the bare number,
        # because a query containing the inner colon returns HTTP 400.
        local = local.split(":")[-1]
    if prefix == "WB":
        cands = uniprot_search(local)
        return Source(
            token,
            "protein",
            candidates=cands,
            note="resolved by free-text id search; not indexed under xref:wormbase-*",
        )
    db = XREF_DB.get(prefix)
    if db is None:
        return Source(token, "protein", note=f"no UniProt xref database known for prefix {prefix!r}")
    cands = uniprot_search(f"xref:{db}-{local}")
    note = "" if cands else "no UniProt entry found for this cross-reference; cannot be dismissed, only deferred"
    return Source(token, "protein", candidates=cands, note=note)


def quickgo_evidence(accession: str, go_id: str) -> list[str]:
    """Evidence codes QuickGO reports for `accession` on `go_id` or its descendants."""
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
        + urllib.parse.urlencode(
            {
                "geneProductId": f"UniProtKB:{accession}",
                "goId": go_id,
                "goUsage": "descendants",
                "goUsageRelationships": "is_a,part_of",
                "limit": 100,
            }
        )
    )
    payload = http_json(url)
    hits, got = payload.get("numberOfHits"), len(payload.get("results", []))
    if hits is not None and hits > got:
        raise SystemExit(
            f"truncated result: QuickGO reports {hits} hits but only {got} were returned "
            f"for {url} - raise the limit or paginate before trusting the evidence set."
        )
    return sorted({r["goEvidence"] for r in payload.get("results", [])})


@dataclass
class Row:
    go_id: str
    go_label: str
    aspect: str
    qualifier: str
    evidence_code: str
    tokens: list[str]
    sources: list[Source] = field(default_factory=list)


def load_ipi_rows(rows: list[dict]) -> list[tuple[str, str, list[Candidate]]]:
    """(reference, token, resolved partner) for every IPI protein-binding row."""
    out = []
    for r in rows:
        if r["GO EVIDENCE CODE"] != "IPI":
            continue
        for token in r["WITH/FROM"].split("|"):
            if not token:
                continue
            out.append((r["REFERENCE"], token, resolve(token).candidates))
    return out


def main() -> str:
    if not GOA_TSV.exists():
        raise SystemExit(
            f"missing input: {GOA_TSV}\nRegenerate it with:  just fetch-gene human ACTR10"
        )
    with GOA_TSV.open() as fh:
        goa = list(csv.DictReader(fh, delimiter="\t"))

    rows: list[Row] = []
    for r in goa:
        if r["GO EVIDENCE CODE"] not in {"IBA", "ISS", "ISO", "ISA", "ISM"}:
            continue
        tokens = [t for t in r["WITH/FROM"].split("|") if t]
        assert len(tokens) == r["WITH/FROM"].count("|") + 1, (
            f"token count drifted from GOA for {r['GO TERM']}"
        )
        rows.append(
            Row(
                go_id=r["GO TERM"],
                go_label=r["GO NAME"],
                aspect=r["GO ASPECT"],
                qualifier=r["QUALIFIER"],
                evidence_code=r["GO EVIDENCE CODE"],
                tokens=tokens,
            )
        )

    for row in rows:
        for token in row.tokens:
            src = resolve(token)
            for cand in src.candidates:
                src.evidence[cand.accession] = quickgo_evidence(cand.accession, row.go_id)
            row.sources.append(src)
        assert len(row.sources) == len(row.tokens), "source list drifted from GOA WITH/FROM"

    ipi = load_ipi_rows(goa)

    lines: list[str] = []
    out = lines.append
    out("## PAINT (IBA) source resolution and source-side evidence")
    out("")
    out(
        "Built directly from `ACTR10-goa.tsv` column `WITH/FROM`; token counts are "
        "asserted against the file. `own evidence` is what QuickGO reports for that "
        "source protein on the propagated term or its `is_a`/`part_of` descendants. "
        "Experimental codes counted: " + ", ".join(sorted(EXPERIMENTAL_CODES)) + "."
    )
    out("")
    for row in rows:
        out(f"### {row.go_id} {row.go_label} ({row.aspect}, {row.qualifier}, {row.evidence_code})")
        out("")
        out(f"{len(row.tokens)} WITH/FROM tokens.")
        out("")
        out("| WITH/FROM token | resolves to | own evidence for this term |")
        out("|---|---|---|")
        for src in row.sources:
            if src.kind == "tree-node":
                out(f"| `{src.token}` | _{src.note}_ | n/a |")
                continue
            if not src.candidates:
                out(f"| `{src.token}` | **unresolved** — _{src.note}_ | not queried |")
                continue
            rendered = "<br>".join(c.render() for c in src.candidates)
            if len(src.candidates) > 1:
                rendered = f"**{len(src.candidates)} hits (ambiguous cross-reference)**<br>" + rendered
            ev = "<br>".join(
                f"{acc}: {', '.join(codes) if codes else 'none'}"
                for acc, codes in src.evidence.items()
            )
            out(f"| `{src.token}` | {rendered} | {ev} |")
        out("")
        prot = [s for s in row.sources if s.kind == "protein"]
        with_exp = [s for s in prot if s.has_experimental]
        reviewed = [
            s for s in prot if any(c.reviewed for c in s.candidates)
        ]
        out(
            f"- protein sources: {len(prot)}; with own experimental evidence for this "
            f"term: {len(with_exp)}; with a reviewed (Swiss-Prot) record: {len(reviewed)}"
        )
        out("")

    out("## IPI (`GO:0005515 protein binding`) partners")
    out("")
    out("| reference | WITH/FROM | partner |")
    out("|---|---|---|")
    for ref, token, cands in ipi:
        out(f"| {ref} | `{token}` | " + "<br>".join(c.render() for c in cands) + " |")
    out("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.stdout.write(main())
