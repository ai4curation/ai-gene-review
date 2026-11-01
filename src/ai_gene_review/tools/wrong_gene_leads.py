#!/usr/bin/env python3
"""Find literature-based annotations whose cited paper may be about a different gene.

UniProt lists the papers it used for each entry (``RX   PubMed=`` lines). When an
experimental or author-statement GOA row (EXP, IDA, IPI, IMP, IGI, IEP, TAS, NAS)
cites a paper that the annotated protein's own entry does not cite, but another
reviewed UniProt entry does, the paper may have studied that
other protein: a paralog, a protein sharing a gene symbol, or a different gene
altogether. ``genes/human/CSGALNACT1`` is the motivating case: ten rows cite
PMID:11514575, which cloned chondroitin synthase CHSY1 (Q86X52), and only CHSY1's
entry cites it.

The output is a ranked lead list for review, never a verdict. UniProt does not cite
every relevant paper, and a paper can study several genes. Two confounders are
removed or penalised:

- An entry for the *same gene* in the same species (an unreviewed or secondary entry
  annotated while the reviewed one cites the paper) is not a different gene, so such
  citing entries are dropped.
- A paper that names the annotated gene in its cached title or abstract probably did
  study it (papers on several paralogs are common), so the lead is penalised.

Leads rank higher for a paralog in the same species, another gene in the same
species, the same-named gene in another species (an annotation transferred across
species with a direct evidence code), few citing entries, and an abstract that does
not name the annotated gene. Papers cited by many reviewed entries are treated as
large-scale and skipped, as are bare protein-binding rows.

>>> own = GeneRecord("P1", "9606", frozenset({"PTHR1"}), frozenset({"ABC1"}), frozenset())
>>> other = CitingEntry("P2", "ABC2", "9606", frozenset({"PTHR1"}))
>>> score_lead(own, [other], named_in_abstract=False)
(6, 'same_taxon_paralog;few_citing_entries;gene_not_named_in_abstract')
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import urllib.parse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from ai_gene_review.tools.function_requirements import REPO_ROOT, _get, _write_tsv

PUBLICATIONS_DIR = REPO_ROOT / "publications"

REPORT_DIR = REPO_ROOT / "reports" / "wrong-gene-leads"
CACHE_DIR = REPO_ROOT / ".cache" / "wrong-gene-leads"
UNIPROT_STREAM = "https://rest.uniprot.org/uniprotkb/stream"

# Low-throughput experimental codes, plus author statements (TAS, NAS) that cite a
# paper: both are curated from a specific publication, so both can be attached to
# the wrong gene. High-throughput papers are skipped.
LITERATURE_CODES = frozenset({"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "TAS", "NAS"})
# A paper cited by more reviewed entries than this is treated as large-scale.
MAX_CITING_ENTRIES = 20
BATCH_SIZE = 40
# Bare protein binding is removed by policy regardless of gene, so it is skipped.
SKIPPED_TERMS = frozenset({"GO:0005515"})


@dataclass(frozen=True)
class GeneRecord:
    """What the annotated protein's own UniProt entry says about it."""

    accession: str
    taxon: str
    panther_families: frozenset[str]
    gene_names: frozenset[str]
    cited_pmids: frozenset[str]
    protein_names: frozenset[str] = frozenset()


@dataclass(frozen=True)
class CitingEntry:
    """A reviewed UniProt entry that cites a given paper."""

    accession: str
    gene: str
    taxon: str
    panther_families: frozenset[str]


def parse_uniprot_flatfile(text: str) -> GeneRecord:
    """Read accession, taxon, PANTHER families, gene names and cited PMIDs.

    >>> r = parse_uniprot_flatfile(
    ...     "AC   Q8TDX6; Q8N1A2;\\nGN   Name=CSGALNACT1; Synonyms=CSGALNACT;\\n"
    ...     "OX   NCBI_TaxID=9606;\\nRX   PubMed=11788602;\\n"
    ...     "DR   PANTHER; PTHR12369:SF11; X; 1.\\nDR   PANTHER; PTHR12369; Y; 1.\\n")
    >>> r.accession, r.taxon, sorted(r.gene_names), sorted(r.panther_families), sorted(r.cited_pmids)
    ('Q8TDX6', '9606', ['CSGALNACT', 'CSGALNACT1'], ['PTHR12369'], ['11788602'])
    """
    accession = ""
    taxon = ""
    families: set[str] = set()
    gn_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("AC   ") and not accession:
            accession = line[5:].split(";")[0].strip()
        elif line.startswith("OX   ") and not taxon:
            m = re.search(r"NCBI_TaxID=(\d+)", line)
            taxon = m.group(1) if m else ""
        elif line.startswith("GN   "):
            gn_lines.append(line[5:])
        elif line.startswith("DR   PANTHER; "):
            families.add(line.split(";")[1].strip().split(":")[0])
    # GN entries wrap across lines (a synonym list can continue on the next line),
    # so parse the joined block with evidence braces removed.
    gn = re.sub(r"\{[^}]*\}", "", " ".join(gn_lines))
    names: set[str] = set()
    for m in re.finditer(r"(?:Name|Synonyms|OrderedLocusNames|ORFNames)=([^;]+)", gn):
        names.update(n.strip() for n in m.group(1).split(","))
    pmids = frozenset(re.findall(r"PubMed=(\d+)", text))
    return GeneRecord(
        accession,
        taxon,
        frozenset(families),
        frozenset(n for n in names if n),
        pmids,
        parse_protein_names(text),
    )


def parse_protein_names(text: str) -> frozenset[str]:
    """Recommended, alternative and submitted protein names from ``DE`` lines.

    >>> sorted(parse_protein_names(
    ...     "DE   RecName: Full=Aurora kinase C;\\nDE            EC=2.7.11.1;\\n"
    ...     "DE   AltName: Full=Aurora 3 {ECO:0000303};\\nDE            Short=ARK-3;\\n"))
    ['ARK-3', 'Aurora 3', 'Aurora kinase C']
    """
    names = set()
    for line in text.splitlines():
        if line.startswith("DE   "):
            for m in re.finditer(r"(?:Full|Short)=([^;{]+)", line):
                names.add(m.group(1).strip())
    return frozenset(n for n in names if n and "uncharacterized" not in n.lower())


def _norm(token: str) -> str:
    """Upper-case and strip non-alphanumerics, so ``GDI/D4`` matches ``GDID4``."""
    return re.sub(r"[^A-Z0-9]", "", token.upper())


def _phrase(text: str) -> str:
    """Lower-case and turn punctuation into spaces, so "Filamin-C" reads "filamin c"."""
    return " " + " ".join(re.sub(r"[^a-z0-9,]+", " ", text.lower()).split()) + " "


def _names_protein(text: str, name: str) -> bool:
    """Whether a protein name occurs in phrase-normalised text.

    A name whose last word is a short qualifier ("Aurora kinase C") also matches an
    enumeration of the family ("aurora kinases A, B, and C").

    >>> t = _phrase("The aurora kinases A, B, and C are serine/threonine kinases.")
    >>> _names_protein(t, "Aurora kinase C"), _names_protein(t, "Aurora kinase D")
    (True, False)
    >>> _names_protein(_phrase("expression of Filamin C in muscle"), "Filamin-C")
    True
    """
    words = _phrase(name).replace(",", " ").split()
    if len(" ".join(words)) < 6:
        return False
    if " " + " ".join(words) + " " in text.replace(",", " ").replace("  ", " "):
        return True
    if len(words) >= 2 and len(words[-1]) <= 2:
        stem = r"\s+".join(re.escape(w) for w in words[:-1])
        # _phrase leaves single spaces between words and keeps commas attached,
        # so each listed item is a whole 1-2 character word, e.g. "a, b, and c".
        item = r"[a-z0-9]{1,2},? (?:(?:and|or) )?"
        pattern = rf" {stem}s? (?:{item})*{re.escape(words[-1])},? "
        return re.search(pattern, text) is not None
    return False


def named_in_abstract(
    pmid: str,
    names: Iterable[str],
    publications_dir: Path = PUBLICATIONS_DIR,
    protein_names: Iterable[str] = (),
) -> bool | None:
    """Whether the cached title or abstract names the gene or its protein.

    Returns None when the paper is not cached. Gene names are matched per
    whitespace token after normalisation (names shorter than three characters are
    ignored); protein names are matched as phrases.

    >>> import tempfile
    >>> d = Path(tempfile.mkdtemp())
    >>> _ = (d / "PMID_1.md").write_text("title: X\\n## Abstract\\nGFP-tagged GDI/D4 was diffuse; aurora kinases A, B, and C.\\n## Full Text\\nCSGALNACT1")
    >>> named_in_abstract("1", ["GDID4"], d), named_in_abstract("1", ["CSGALNACT1"], d), named_in_abstract("2", ["X"], d)
    (True, False, None)
    >>> named_in_abstract("1", ["AURKC"], d, ["Aurora kinase C"])
    True
    """
    path = publications_dir / f"PMID_{pmid}.md"
    if not path.exists():
        return None
    text = path.read_text(errors="replace").split("\n## Full Text", 1)[0]
    tokens = {_norm(tok) for tok in text.split()}
    wanted = {_norm(n) for n in names}
    if {w for w in wanted if len(w) >= 3} & tokens:
        return True
    phrased = _phrase(text)
    return any(_names_protein(phrased, n) for n in protein_names)


def score_lead(
    own: GeneRecord, citing: list[CitingEntry], named_in_abstract: bool | None
) -> tuple[int, str]:
    """Score how likely the cited paper is about one of the citing entries instead.

    A paralog in the same species +3, another gene in the same species +2, the
    same-named gene in another species +2, three or fewer citing entries +1, and an
    abstract that does not name the annotated gene +2 (or -3 if it does).
    """
    reasons = []
    score = 0
    same_taxon = [c for c in citing if c.taxon == own.taxon]
    if any(c.panther_families & own.panther_families for c in same_taxon):
        score += 3
        reasons.append("same_taxon_paralog")
    elif same_taxon:
        score += 2
        reasons.append("same_taxon_other_gene")
    if any(c.taxon != own.taxon and c.gene in own.gene_names for c in citing):
        score += 2
        reasons.append("same_gene_other_species")
    if len(citing) <= 3:
        score += 1
        reasons.append("few_citing_entries")
    if named_in_abstract is False:
        score += 2
        reasons.append("gene_not_named_in_abstract")
    elif named_in_abstract:
        score -= 3
        reasons.append("gene_named_in_abstract")
    return score, ";".join(reasons)


def candidate_rows(gene_dir: Path) -> tuple[GeneRecord, list[dict[str, str]]] | None:
    """Literature-based GOA rows citing a PMID that the gene's own UniProt entry does not."""
    uniprot = list(gene_dir.glob("*-uniprot.txt"))
    goa = list(gene_dir.glob("*-goa.tsv"))
    if not uniprot or not goa:
        return None
    own = parse_uniprot_flatfile(uniprot[0].read_text(errors="replace"))
    rows = []
    with goa[0].open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ref = row.get("REFERENCE") or ""
            if (
                row.get("GO EVIDENCE CODE") in LITERATURE_CODES
                and ref.startswith("PMID:")
                and ref[5:] not in own.cited_pmids
                and row.get("GO TERM") not in SKIPPED_TERMS
                and not (row.get("QUALIFIER") or "").startswith("NOT")
            ):
                rows.append(row)
    return own, rows


def parse_citing_tsv(text: str, pmids: Iterable[str]) -> dict[str, list[CitingEntry]]:
    """Map each queried PMID to the entries in a UniProt TSV result that cite it.

    >>> tsv = ("Entry\\tGene Names (primary)\\tOrganism (ID)\\tPubMed ID\\tPANTHER\\n"
    ...        "Q86X52\\tCHSY1\\t9606\\t11514575; 10231032\\tPTHR12369:SF42;PTHR12369;\\n")
    >>> out = parse_citing_tsv(tsv, ["11514575", "9113980"])
    >>> [c.accession for c in out["11514575"]], out["9113980"]
    (['Q86X52'], [])
    """
    wanted = set(pmids)
    out: dict[str, list[CitingEntry]] = {p: [] for p in wanted}
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        families = frozenset(f.split(":")[0] for f in row["PANTHER"].split(";") if f)
        entry = CitingEntry(
            row["Entry"], row["Gene Names (primary)"], row["Organism (ID)"], families
        )
        for pmid in {p.strip() for p in row["PubMed ID"].split(";")} & wanted:
            out[pmid].append(entry)
    return out


def fetch_citing_entries(
    pmids: Iterable[str], cache_dir: Path = CACHE_DIR
) -> dict[str, list[CitingEntry]]:
    """Reviewed UniProt entries citing each PMID, fetched in batches and cached."""
    cache = cache_dir / "citing-entries.json"
    stored: dict[str, list[dict[str, Any]]] = (
        json.loads(cache.read_text()) if cache.exists() else {}
    )
    need = sorted(set(pmids) - set(stored))
    fields = "accession,gene_primary,organism_id,lit_pubmed_id,xref_panther"
    for i in range(0, len(need), BATCH_SIZE):
        batch = need[i : i + BATCH_SIZE]
        query = (
            "reviewed:true AND (" + " OR ".join(f"lit_pubmed:{p}" for p in batch) + ")"
        )
        params = urllib.parse.urlencode(
            {"query": query, "fields": fields, "format": "tsv"}
        )
        for pmid, entries in parse_citing_tsv(
            _get(f"{UNIPROT_STREAM}?{params}", "text/plain"), batch
        ).items():
            stored[pmid] = [
                {
                    "accession": e.accession,
                    "gene": e.gene,
                    "taxon": e.taxon,
                    "panther": sorted(e.panther_families),
                }
                for e in entries
            ]
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(stored))
    return {
        p: [
            CitingEntry(e["accession"], e["gene"], e["taxon"], frozenset(e["panther"]))
            for e in v
        ]
        for p, v in stored.items()
    }


def _review_index(gene_dir: Path) -> dict[tuple[str, str, str], tuple[str, bool]]:
    """Map (term, evidence, reference) to (review action, has WRONG_GENE_PRODUCT defect)."""
    paths = list(gene_dir.glob("*-ai-review.yaml"))
    if not paths:
        return {}
    review = (
        yaml.load(
            paths[0].read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)
        )
        or {}
    )
    index = {}
    for a in review.get("existing_annotations") or []:
        r = a.get("review") or {}
        key = (
            str((a.get("term") or {}).get("id")),
            str(a.get("evidence_type")),
            str(a.get("original_reference_id")),
        )
        wrong_gene = any(
            d.get("defect_type") == "WRONG_GENE_PRODUCT"
            for d in r.get("source_defects") or []
        )
        index[key] = (str(r.get("action") or ""), wrong_gene)
    return index


def find_leads(
    gene_dirs: Iterable[Path],
    citing: dict[str, list[CitingEntry]] | None = None,
    cache_dir: Path = CACHE_DIR,
    publications_dir: Path = PUBLICATIONS_DIR,
) -> list[dict[str, Any]]:
    """Ranked wrong-gene leads for the GOA rows in the given gene folders.

    ``citing`` maps PMIDs to the entries citing them; when omitted it is fetched
    from UniProt for every candidate PMID.
    """
    candidates = [
        (d, c) for d in sorted(gene_dirs) if (c := candidate_rows(d)) and c[1]
    ]
    if citing is None:
        citing = fetch_citing_entries(
            {r["REFERENCE"][5:] for _, (_, rows) in candidates for r in rows}, cache_dir
        )
    leads: list[dict[str, Any]] = []
    for gene_dir, (own, rows) in candidates:
        index: dict[tuple[str, str, str], tuple[str, bool]] | None = None
        for row in rows:
            # Drop the gene itself: the same accession, or the same-named gene in
            # the same species (a secondary entry for one gene is not a wrong gene).
            others = [
                c
                for c in citing.get(row["REFERENCE"][5:], [])
                if c.accession != own.accession
                and not (c.taxon == own.taxon and c.gene in own.gene_names)
            ]
            if not others or len(others) > MAX_CITING_ENTRIES:
                continue
            if index is None:
                index = _review_index(gene_dir)
            action, wrong_gene = index.get(
                (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"]), ("", False)
            )
            score, reasons = score_lead(
                own,
                others,
                named_in_abstract(
                    row["REFERENCE"][5:],
                    own.gene_names,
                    publications_dir,
                    own.protein_names,
                ),
            )
            leads.append(
                {
                    "gene": f"{gene_dir.parent.name}/{gene_dir.name}",
                    "accession": own.accession,
                    "go_id": row["GO TERM"],
                    "go_label": row["GO NAME"],
                    "evidence": row["GO EVIDENCE CODE"],
                    "reference": row["REFERENCE"],
                    "assigned_by": row["ASSIGNED BY"],
                    "score": score,
                    "reasons": reasons,
                    "citing_entries": ";".join(
                        f"{c.accession}:{c.gene}" for c in others
                    ),
                    "review_action": action,
                    "wrong_gene_defect": wrong_gene,
                }
            )
    leads.sort(key=lambda r: (-r["score"], r["gene"], r["go_id"]))
    return leads


def main(argv: list[str] | None = None) -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--genes-root", type=Path, default=REPO_ROOT / "genes")
    parser.add_argument("--out-dir", type=Path, default=REPORT_DIR)
    args = parser.parse_args(argv)
    leads = find_leads(args.genes_root.glob("*/*"))
    _write_tsv(args.out_dir / "leads.tsv", leads)
    reviewed = [r for r in leads if r["review_action"]]
    agreed = [
        r for r in reviewed if r["wrong_gene_defect"] or r["review_action"] == "REMOVE"
    ]
    print(f"{len(leads)} leads in {len({r['gene'] for r in leads})} genes")
    print(
        f"{len(reviewed)} on reviewed rows; {len(agreed)} already REMOVE or WRONG_GENE_PRODUCT"
    )
    for score, n in sorted(Counter(r["score"] for r in leads).items(), reverse=True):
        print(f"score {score}: {n}")


if __name__ == "__main__":
    main()
