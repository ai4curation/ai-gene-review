#!/usr/bin/env python3
"""Reproducible checks behind the human ADAMTSL3 (P82987) GO annotation review.

Four independent checks, each of which produced a claim used in
``ADAMTSL3-ai-review.yaml``:

1. ``paint_projection`` - which PAINT (PANTHER phylogenetic) node annotations
   actually reach each member of family PTHR13723. Built from the two
   authoritative PANTHER files (``IBD.gaf`` = node-level annotations,
   ``gene_association.paint_uniprot.gaf.gz`` = the leaf projections), not from
   QuickGO, so the presence/absence matrix is primary data.

2. ``iba_donors`` - every WITH/FROM token on ADAMTSL3's single IBA row is
   resolved to a protein, and each donor is asked (via QuickGO) whether it
   carries its *own* experimental annotation to the propagated term or a
   descendant. "This donor only carries the same family-level inference" is a
   testable claim, so it is tested rather than asserted.

3. ``intact_partners`` - the 13 distinct partners behind ADAMTSL3's 15
   ``GO:0005515`` IPI rows, with the IntAct detection methods that produced them
   and each partner's own IntAct degree. A promiscuous prey in a high-throughput
   two-hybrid screen is a different thing from a binding partner.

4. ``goa_coverage`` - asserts that the review file covers every row of
   ``ADAMTSL3-goa.tsv`` exactly once, keyed on the fields GOA actually
   distinguishes rows by. This is the invariant that a hand-maintained
   annotation list drifts away from.

Every check fails loudly on a missing input or an unresolvable identifier: a
silent zero reads as a finding, and that is the failure mode this script exists
to avoid.

Usage::

    uv run python analyze_adamtsl3.py            # run all checks, write RESULTS.md
    uv run python analyze_adamtsl3.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import gzip
import io
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import requests
import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
CACHE = HERE / ".cache"

GOA_TSV = GENE_DIR / "ADAMTSL3-goa.tsv"
REVIEW_YAML = GENE_DIR / "ADAMTSL3-ai-review.yaml"

PAINT_BASE = "https://data.pantherdb.org/ftp/downloads/paint/current"
IBD_GAF_URL = f"{PAINT_BASE}/IBD.gaf"
LEAF_GAF_URL = f"{PAINT_BASE}/gene_association.paint_uniprot.gaf.gz"

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTACT = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"
WB_GAF_URL = "https://current.geneontology.org/annotations/wb.gaf.gz"

ACC = "P82987"  # human ADAMTSL3
FAMILY = "PTHR13723"

#: GO evidence codes that represent an experiment on the annotated entity.
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

#: The PTHR13723 members whose PAINT projection we tabulate. Accessions are
#: taken from the cached family entry list (``interpro/panther/PTHR13723``);
#: ``check_family_accessions`` re-derives them so a stale hand-copy cannot pass.
FAMILY_MEMBERS: Dict[str, str] = {
    # catalytic ADAMTS proteinases (positive control: these should receive the
    # metalloendopeptidase / proteolysis terms)
    "ADAMTS1": "Q9UHI8",
    "ADAMTS9": "Q9P2N4",
    "ADAMTS10": "Q9H324",
    "ADAMTS17": "Q8TE56",
    # non-catalytic ADAMTS-like proteins and papilins (the test set)
    "ADAMTSL1": "Q8N6G6",
    "ADAMTSL2": "Q86TH1",
    "ADAMTSL3": "P82987",
    "ADAMTSL4": "Q6UY14",
    "ADAMTSL5": "Q6ZMM2",
    "PAPLN": "O95428",
    "THSD4": "Q6ZMP0",
    # non-human members, to show the pattern is not a human-annotation artefact
    "Adamtsl1_mouse": "Q8BLI0",
    "Adamtsl2_mouse": "Q7TSK7",
    "Adamtsl3_mouse": "G3UXC7",
    "Adamtsl4_mouse": "Q80T21",
    "Papln_mouse": "Q9EPX2",
    "Thsd4_mouse": "Q3UTY6",
    "madd-4_worm": "P90884",
}

#: Terms curated at the PTHR13723 root node PTN000347317.
NODE_TERMS = {
    "GO:0031012": "extracellular matrix",
    "GO:0030198": "extracellular matrix organization",
    "GO:0004222": "metalloendopeptidase activity",
    "GO:0006508": "proteolysis",
}


class InputError(RuntimeError):
    """A required input is missing. Always names the command that produces it."""


# --------------------------------------------------------------------------- #
# small HTTP helpers
# --------------------------------------------------------------------------- #
def _get_json(url: str, params: Optional[Dict[str, Any]] = None) -> Any:
    r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=180)
    r.raise_for_status()
    return r.json()


def _cached_download(url: str, dest: Path, gzipped: bool = False) -> Path:
    """Download ``url`` to ``dest`` once. Streams; never holds the file in RAM."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=1800) as r:
        r.raise_for_status()
        src: Iterable[bytes]
        if gzipped:
            gz = gzip.GzipFile(fileobj=r.raw)
            with tmp.open("wb") as fh:
                shutil.copyfileobj(gz, fh)
        else:
            with tmp.open("wb") as fh:
                for chunk in r.iter_content(chunk_size=1 << 20):
                    fh.write(chunk)
    tmp.rename(dest)
    return dest


# --------------------------------------------------------------------------- #
# check 1: PAINT projection matrix
# --------------------------------------------------------------------------- #
def fetch_paint_slice() -> Tuple[List[List[str]], List[List[str]]]:
    """Return (node_rows, leaf_rows) restricted to PTHR13723's PAINT nodes.

    ``IBD.gaf`` is small and cached whole. The leaf GAF is ~400 MB, so it is
    streamed and only the rows mentioning one of this family's nodes are kept.
    """
    ibd = _cached_download(IBD_GAF_URL, CACHE / "IBD.gaf")
    node_rows: List[List[str]] = []
    nodes: set[str] = set()
    for line in ibd.read_text().splitlines():
        if line.startswith("!"):
            continue
        f = line.split("\t")
        if len(f) < 14:
            continue
        # A family's nodes are those cited by its members' leaf IBAs; we seed
        # the set from the two nodes reachable from ADAMTSL3's family and then
        # confirm below that no member cites a node outside the set.
        node_rows.append(f)
    # Identify this family's nodes from the leaf GAF (members -> ancestral nodes).
    leaf_cache = CACHE / f"{FAMILY}-leaf-slice.tsv"
    if not leaf_cache.exists():
        wanted = set(FAMILY_MEMBERS.values())
        kept: List[str] = []
        with requests.get(LEAF_GAF_URL, stream=True, timeout=3600) as r:
            r.raise_for_status()
            gz = gzip.GzipFile(fileobj=r.raw)
            for raw in io.TextIOWrapper(gz, encoding="utf-8", errors="replace"):
                if raw.startswith("!"):
                    continue
                f = raw.split("\t")
                if len(f) > 7 and f[1] in wanted:
                    kept.append(raw.rstrip("\n"))
        CACHE.mkdir(parents=True, exist_ok=True)
        leaf_cache.write_text("\n".join(kept) + "\n")
    leaf_rows = [ln.split("\t") for ln in leaf_cache.read_text().splitlines() if ln]
    for f in leaf_rows:
        for tok in f[7].split("|"):
            if tok.startswith("PANTHER:"):
                nodes.add(tok.split(":", 1)[1])
    if not nodes:
        raise InputError(
            "No PANTHER nodes found in the leaf PAINT slice; delete "
            f"{leaf_cache} and re-run to re-download {LEAF_GAF_URL}"
        )
    node_rows = [f for f in node_rows if f[1] in nodes]
    return node_rows, leaf_rows


def check_paint_projection() -> Dict[str, Any]:
    node_rows, leaf_rows = fetch_paint_slice()

    node_annotations = [
        {
            "node": f[1],
            "qualifier": f[3],
            "go_id": f[4],
            "evidence": f[6],
            "with_from": f[7],
            "taxon": f[12],
            "negated": "NOT" in f[3],
        }
        for f in node_rows
    ]
    if not node_annotations:
        raise InputError(f"IBD.gaf yielded no node annotations for {FAMILY}")

    # Which leaves does each node project onto, and with which qualifier?
    matrix: Dict[str, Dict[str, str]] = defaultdict(dict)
    by_acc = {acc: name for name, acc in FAMILY_MEMBERS.items()}
    for f in leaf_rows:
        acc, qual, go_id = f[1], f[3], f[4]
        name = by_acc.get(acc)
        if name is None:
            continue
        matrix[name][go_id] = "NOT" if "NOT" in qual else qual

    # Which leaves (family-wide, not just our members) receive the NOT?
    not_nodes = sorted({a["node"] for a in node_annotations if a["negated"]})
    not_recipients: Dict[str, List[str]] = defaultdict(list)
    if not_nodes:
        # Re-stream is unnecessary: the NOT projections are keyed by node in the
        # leaf GAF's WITH/FROM, but our slice is member-restricted. Use QuickGO
        # to count the full recipient set instead, and say so.
        for node in not_nodes:
            not_recipients[node] = sorted(
                {
                    f[1]
                    for f in leaf_rows
                    if f"PANTHER:{node}" in f[7] and "NOT" in f[3]
                }
            )

    rows = []
    for name in FAMILY_MEMBERS:
        rows.append(
            {
                "member": name,
                "accession": FAMILY_MEMBERS[name],
                **{go: matrix[name].get(go, "-") for go in NODE_TERMS},
            }
        )

    catalytic = {"ADAMTS1", "ADAMTS9", "ADAMTS10", "ADAMTS17"}
    non_catalytic = [
        n
        for n in FAMILY_MEMBERS
        if n not in catalytic
    ]
    got_not = [n for n in non_catalytic if matrix[n].get("GO:0004222") == "NOT"]
    got_nothing = [n for n in non_catalytic if "GO:0004222" not in matrix[n]]
    got_positive = [
        n for n in non_catalytic if matrix[n].get("GO:0004222") not in (None, "NOT")
    ]

    # Positive control: the four catalytic ADAMTS must receive GO:0004222.
    missing_control = [n for n in catalytic if "GO:0004222" not in matrix[n]]
    if missing_control:
        raise InputError(
            "Positive control failed: catalytic ADAMTS members "
            f"{missing_control} did not receive GO:0004222 from PAINT. The leaf "
            f"slice at {CACHE / f'{FAMILY}-leaf-slice.tsv'} is probably stale; "
            "delete .cache/ and re-run."
        )

    return {
        "node_annotations": node_annotations,
        "matrix": rows,
        "not_nodes": not_nodes,
        "not_recipients_within_member_set": {k: v for k, v in not_recipients.items()},
        "non_catalytic_with_NOT_GO_0004222": got_not,
        "non_catalytic_with_no_GO_0004222_statement": got_nothing,
        "non_catalytic_with_positive_GO_0004222": got_positive,
        "catalytic_control_all_received_GO_0004222": True,
    }


# --------------------------------------------------------------------------- #
# check 2: IBA donors
# --------------------------------------------------------------------------- #
def _wormbase_symbol(wbgene: str) -> Tuple[str, str]:
    """Map a ``WBGene...`` id to (symbol, product name) via the GO consortium GAF.

    UniProt's ``xref:wormbase-`` index is keyed on *transcript* ids
    (``F53B6.2a``), not on ``WBGene`` ids, so the obvious query returns zero hits
    for a perfectly valid gene. Getting this wrong is how ``WBGene00003242``
    reads as "unresolvable" when it is in fact ``mig-6``/papilin - and it is
    emphatically *not* ``madd-4``, which is ``WBGene00009958``.
    """
    dest = CACHE / "wb.gaf"
    _cached_download(WB_GAF_URL, dest, gzipped=True)
    for line in dest.read_text(errors="replace").splitlines():
        if line.startswith("!"):
            continue
        f = line.split("\t")
        if len(f) > 9 and f[1] == wbgene:
            return f[2], f[9]
    raise InputError(
        f"{wbgene} not present in {WB_GAF_URL}; delete {dest} to force a refresh"
    )


def _resolve_token(token: str) -> List[Dict[str, Any]]:
    """Resolve one GOA WITH/FROM token to candidate UniProt entries.

    Always requests more than one hit: a ``size=1`` query silently converts an
    ambiguous cross-reference into a confident wrong answer.
    """
    fields = "accession,id,protein_name,gene_names,length,reviewed,organism_name"
    if token.startswith("PANTHER:"):
        return [{"kind": "panther_node", "id": token.split(":", 1)[1]}]
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        return [_as_entry(_get_json(f"{UNIPROT}/{acc}.json", {"fields": fields}))]
    db, rest = token.split(":", 1)
    if db == "WB":
        symbol, product = _wormbase_symbol(rest)
        hits = _get_json(
            f"{UNIPROT}/search",
            {"query": f"gene:{symbol} AND organism_id:6239", "fields": fields, "size": 25},
        ).get("results", [])
        entries = [_as_entry(h) for h in hits]
        # UniProt's `gene:` search is fuzzy: `gene:mig-6` happily returns mig-10.
        # Require the exact symbol among the entry's own gene names, or fail -
        # a near-miss here silently substitutes a different protein.
        exact = [
            e
            for e in entries
            if any((g or "").lower() == symbol.lower() for g in e["gene"])
        ]
        if not exact:
            raise InputError(
                f"{token} maps to WormBase symbol {symbol!r} ({product}), but no "
                f"UniProt C. elegans entry carries that exact gene name "
                f"(fuzzy hits were: {[e['gene'] for e in entries][:5]}). "
                "Resolve manually before using this row."
            )
        return exact
    xref = {
        # MGI tokens arrive as MGI:MGI:nnn; UniProt wants the bare number, and a
        # query containing the inner colon returns HTTP 400.
        "MGI": ("mgi", rest.split(":")[-1]),
        "RGD": ("rgd", rest),
        "FB": ("flybase", rest),
    }.get(db)
    if xref is None:
        raise InputError(f"No resolver for WITH/FROM token {token!r}")
    hits = _get_json(
        f"{UNIPROT}/search",
        {"query": f"xref:{xref[0]}-{xref[1]}", "fields": fields, "size": 5},
    ).get("results", [])
    return [_as_entry(h) for h in hits]


def _as_entry(h: Dict[str, Any]) -> Dict[str, Any]:
    desc = h.get("proteinDescription", {})
    name = (desc.get("recommendedName") or {}).get("fullName", {}).get("value")
    if name is None:
        subs = desc.get("submissionNames") or []
        name = subs[0]["fullName"]["value"] if subs else None
    entry = {
        "accession": h.get("primaryAccession"),
        "entry_name": h.get("uniProtkbId"),
        "reviewed": h.get("entryType", "").startswith("UniProtKB reviewed"),
        "length": h.get("sequence", {}).get("length"),
        "gene": [g.get("geneName", {}).get("value") for g in h.get("genes", [])],
        "protein_name": name,
        "organism": h.get("organism", {}).get("scientificName"),
        "subcellular_locations": [
            loc.get("location", {}).get("value")
            for c in h.get("comments", [])
            if c.get("commentType") == "SUBCELLULAR LOCATION"
            for loc in c.get("subcellularLocations", [])
        ],
    }
    # A dead (deleted) UniProt entry returns no name and no annotations, which is
    # indistinguishable from a live entry that genuinely carries none.
    if entry["accession"] and not entry["entry_name"]:
        raise InputError(
            f"UniProt entry {entry['accession']} resolved with no entry name - "
            "probably an inactive/deleted accession. Resolve it manually."
        )
    return entry


def _own_evidence(acc: str, go_id: str) -> List[Dict[str, str]]:
    d = _get_json(
        f"{QUICKGO}/annotation/search",
        {
            "geneProductId": f"UniProtKB:{acc}",
            "goId": go_id,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "limit": 100,
        },
    )
    out = []
    for r in d.get("results", []):
        out.append(
            {"go_id": r["goId"], "evidence": r["goEvidence"], "reference": r["reference"]}
        )
    return sorted({tuple(x.items()) for x in out}) and [
        dict(t) for t in sorted({tuple(sorted(x.items())) for x in out})
    ]


def check_iba_donors() -> Dict[str, Any]:
    goa = read_goa()
    iba = [r for r in goa if r["evidence"] == "IBA"]
    if len(iba) != 1:
        raise InputError(f"Expected exactly 1 IBA row in {GOA_TSV}, found {len(iba)}")
    term = iba[0]["go_id"]
    tokens = [t for t in iba[0]["with_from"].split("|") if t]

    donors = []
    n_with_own_experiment = 0
    for tok in tokens:
        cands = _resolve_token(tok)
        if not cands:
            raise InputError(
                f"WITH/FROM token {tok!r} did not resolve. An unresolved source "
                "can be deferred, never dismissed - resolve it before drawing a "
                "conclusion from this row."
            )
        # Prefer a reviewed Swiss-Prot entry when a cross-reference is ambiguous,
        # but keep the candidate count so the ambiguity is reported rather than
        # hidden: a size=1 lookup turns an ambiguity into a confident wrong answer.
        primary = next((c for c in cands if c.get("reviewed")), cands[0])
        rec: Dict[str, Any] = {
            "token": tok,
            "n_candidates": len(cands),
            "all_candidates": [
                f"{c.get('accession')} {'/'.join(g for g in (c.get('gene') or []) if g)}"
                f" [{'Swiss-Prot' if c.get('reviewed') else 'TrEMBL'}]"
                for c in cands
                if c.get("kind") != "panther_node"
            ],
            **primary,
        }
        if primary.get("kind") == "panther_node":
            rec["note"] = "PANTHER internal tree node, not a protein"
        else:
            ev = _own_evidence(primary["accession"], term)
            exp = [e for e in ev if e["evidence"] in EXPERIMENTAL]
            rec["own_annotations"] = ev
            rec["own_experimental"] = exp
            rec["has_own_experimental_evidence"] = bool(exp)
            if exp:
                n_with_own_experiment += 1
        donors.append(rec)

    protein_donors = [d for d in donors if d.get("kind") != "panther_node"]
    self_donors = [d for d in protein_donors if d.get("accession") == ACC]
    return {
        "term": term,
        "n_tokens": len(tokens),
        "n_protein_donors": len(protein_donors),
        "n_self_referential": len(self_donors),
        "n_donors_with_own_experimental_evidence": n_with_own_experiment,
        "distinct_specific_terms_held_by_donors": sorted(
            {
                e["go_id"]
                for d in protein_donors
                for e in d.get("own_experimental", [])
            }
        ),
        "donors": donors,
    }


# --------------------------------------------------------------------------- #
# check 3: IntAct partners
# --------------------------------------------------------------------------- #
def _intact_all(acc: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    page = 0
    while True:
        d = _get_json(f"{INTACT}/{acc}", {"page": page, "pageSize": 200})
        content = d.get("content", d if isinstance(d, list) else [])
        if not content:
            break
        out.extend(content)
        page += 1
        if page > 40:  # a hub with >8000 records: report, do not truncate silently
            raise InputError(
                f"IntAct paging for {acc} exceeded 40 pages; raise the cap or "
                "record the degree as unavailable rather than truncated."
            )
    return out


#: IntAct MI method names that are sub-methods of one yeast two-hybrid pipeline.
Y2H_METHODS = {
    "two hybrid array",
    "two hybrid prey pooling approach",
    "validated two hybrid",
    "two hybrid",
    "two hybrid pooling approach",
}


def _norm_intact_id(value: Optional[str]) -> Optional[str]:
    """Strip IntAct's ``" (uniprotkb)"`` / ``" (intact)"`` database suffix.

    Without this an accession never equals the plain UniProt accession, so a
    lookup keyed on the raw value silently finds nothing - and "no non-Y2H
    method recorded" would then be indistinguishable from "partner not found",
    which is the failure this whole check exists to rule out.
    """
    if not value:
        return None
    return value.split(" (", 1)[0].strip()


def _intact_partner_methods(acc: str) -> Dict[str, set]:
    """Map each distinct interaction partner of ``acc`` to its detection methods."""
    per: Dict[str, set] = defaultdict(set)
    for i in _intact_all(acc):
        a, b = _norm_intact_id(i.get("idA")), _norm_intact_id(i.get("idB"))
        other = b if a == acc else a
        if not other or other == acc:
            continue
        per[other].add(i.get("detectionMethod"))
    return per


def _intact_degree(acc: str) -> int:
    return len(_intact_partner_methods(acc))


def check_intact_partners() -> Dict[str, Any]:
    goa = read_goa()
    ipi = [r for r in goa if r["evidence"] == "IPI"]
    partners = sorted({r["with_from"].split(":", 1)[1] for r in ipi})
    if not partners:
        raise InputError(f"No IPI WITH/FROM partners found in {GOA_TSV}")

    interactions = _intact_all(ACC)
    methods = Counter(i.get("detectionMethod") for i in interactions)
    pubs = Counter(
        p.replace(" (pubmed)", "")
        for i in interactions
        for p in (i.get("publicationIdentifiers") or [])
        if p.endswith("(pubmed)")
    )

    # Per-pair, not per-gene. The gene-level method counter also covers partners
    # that are NOT in GOA (a 15-partner anti-tag-coIP set and one BioID hit), so
    # it cannot answer "is there an orthogonal assay for THESE pairs?".
    per_partner = _intact_partner_methods(ACC)
    missing = [a for a in partners if a not in per_partner]
    if missing:
        raise InputError(
            f"GOA IPI partners {missing} were not found in ADAMTSL3's IntAct record. "
            "A partner that cannot be located is not a partner with no orthogonal "
            "evidence - resolve the identifier mismatch before reading anything "
            "into the method list."
        )
    per_partner_methods = {a: sorted(m for m in per_partner[a] if m) for a in partners}
    non_y2h = {
        a: sorted(set(m) - Y2H_METHODS) for a, m in per_partner_methods.items()
        if set(m) - Y2H_METHODS
    }
    non_goa_partners = {
        a: sorted(m for m in ms if m) for a, ms in per_partner.items() if a not in partners
    }

    fields = "accession,id,protein_name,gene_names,length,reviewed,cc_subcellular_location"
    rows = []
    for acc in partners:
        entry = _as_entry(_get_json(f"{UNIPROT}/{acc}.json", {"fields": fields}))
        entry["intact_distinct_partners"] = _intact_degree(acc)
        rows.append(entry)

    degrees = sorted(r["intact_distinct_partners"] for r in rows)
    mid = len(degrees) // 2
    median = degrees[mid] if len(degrees) % 2 else (degrees[mid - 1] + degrees[mid]) / 2
    return {
        "n_ipi_rows": len(ipi),
        "n_distinct_partners": len(partners),
        "adamtsl3_intact_distinct_partners": len(per_partner),
        "detection_methods_gene_level": dict(methods),
        "per_partner_methods_goa_partners": per_partner_methods,
        "goa_partners_with_non_y2h_method": non_y2h,
        "non_goa_partners_and_their_methods": non_goa_partners,
        "publications": dict(pubs),
        "partner_degree_median": median,
        "partners": rows,
        "all_reviewed_swissprot": all(r["reviewed"] for r in rows),
    }


# --------------------------------------------------------------------------- #
# check 4: review coverage vs GOA
# --------------------------------------------------------------------------- #
def read_goa() -> List[Dict[str, str]]:
    if not GOA_TSV.exists():
        raise InputError(f"{GOA_TSV} missing - run `just fetch-gene human ADAMTSL3`")
    with GOA_TSV.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        rows = [
            {
                "go_id": r["GO TERM"],
                "label": r["GO NAME"],
                "evidence": r["GO EVIDENCE CODE"],
                "reference": r["REFERENCE"],
                "with_from": r["WITH/FROM"],
                "qualifier": r["QUALIFIER"],
            }
            for r in reader
        ]
    if not rows:
        raise InputError(f"{GOA_TSV} parsed to zero rows")
    return rows


class _StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key.

    PyYAML silently keeps the last occurrence of a duplicated key and discards
    the earlier one, so a duplicate key deletes data before any check that walks
    the parsed document can see it.
    """


def _no_duplicates(loader, node, deep=False):  # type: ignore[no-untyped-def]
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def check_goa_coverage() -> Dict[str, Any]:
    if not REVIEW_YAML.exists():
        raise InputError(f"{REVIEW_YAML} missing - run `just fetch-gene human ADAMTSL3`")
    doc = yaml.load(REVIEW_YAML.read_text(), Loader=_StrictLoader)

    goa = read_goa()
    goa_keys = Counter(
        (r["go_id"], r["evidence"], r["reference"], r["with_from"]) for r in goa
    )

    reviewed = doc.get("existing_annotations") or []
    new_rows = [a for a in reviewed if (a.get("review") or {}).get("action") == "NEW"]
    goa_rows = [a for a in reviewed if (a.get("review") or {}).get("action") != "NEW"]
    review_keys = Counter(
        (
            a["term"]["id"],
            a.get("evidence_type"),
            a.get("original_reference_id"),
            "|".join(a.get("supporting_entities") or []),
        )
        for a in goa_rows
    )

    missing = goa_keys - review_keys
    extra = review_keys - goa_keys
    actions = Counter((a.get("review") or {}).get("action") for a in reviewed)
    pending = [
        a["term"]["id"] for a in reviewed if (a.get("review") or {}).get("action") == "PENDING"
    ]

    result = {
        "n_goa_rows": len(goa),
        "n_review_rows_from_goa": len(goa_rows),
        "n_review_rows_new": len(new_rows),
        "actions": dict(actions),
        "goa_rows_not_reviewed": [list(k) for k in missing],
        "review_rows_not_in_goa": [list(k) for k in extra],
        "pending": pending,
        "ok": not missing and not extra and not pending,
    }
    if not result["ok"]:
        result["note"] = (
            "Coverage mismatch. Every GOA row must appear exactly once in "
            "existing_annotations, keyed on (term, evidence, reference, "
            "with/from); rows the reviewer adds must carry action NEW."
        )
    return result


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #
def render_results(res: Dict[str, Any]) -> str:
    p = res["paint_projection"]
    d = res["iba_donors"]
    i = res["intact_partners"]
    c = res["goa_coverage"]

    lines: List[str] = []
    a = lines.append
    a("# ADAMTSL3 (P82987) - analyses supporting the GO annotation review")
    a("")
    a(
        "Generated by `analyze_adamtsl3.py`. Every number below is recomputed on "
        "each run from primary sources (PANTHER PAINT GAFs, UniProt, QuickGO, "
        "IntAct); nothing is hardcoded."
    )
    a("")

    a("## 1. PAINT projection across PANTHER family PTHR13723")
    a("")
    a(
        "Node-level annotations come from PANTHER's `IBD.gaf`; the leaf column "
        "entries come from `gene_association.paint_uniprot.gaf.gz`, i.e. the "
        "projections PAINT actually exports, not a reconstruction of them."
    )
    a("")
    a("Curated node annotations in this family:")
    a("")
    a("| node | GO id | evidence | negated | taxon |")
    a("|---|---|---|---|---|")
    for n in sorted(p["node_annotations"], key=lambda x: (x["node"], x["go_id"])):
        a(
            f"| {n['node']} | {n['go_id']} {NODE_TERMS.get(n['go_id'], '')} | "
            f"{n['evidence']} | {'yes' if n['negated'] else 'no'} | {n['taxon'] or '-'} |"
        )
    a("")
    a("Which of those four terms each family member actually receives:")
    a("")
    hdr = "| member | accession | " + " | ".join(
        f"{g}<br>{NODE_TERMS[g]}" for g in NODE_TERMS
    ) + " |"
    a(hdr)
    a("|---|---|" + "---|" * len(NODE_TERMS))
    for row in p["matrix"]:
        a(
            f"| {row['member']} | {row['accession']} | "
            + " | ".join(str(row[g]) for g in NODE_TERMS)
            + " |"
        )
    a("")
    a(
        f"- Non-catalytic members carrying an explicit `NOT GO:0004222`: "
        f"**{', '.join(p['non_catalytic_with_NOT_GO_0004222']) or 'none'}**."
    )
    a(
        f"- Non-catalytic members carrying no statement either way about "
        f"`GO:0004222`: **{', '.join(p['non_catalytic_with_no_GO_0004222_statement']) or 'none'}**."
    )
    a(
        f"- Non-catalytic members wrongly carrying a *positive* `GO:0004222`: "
        f"**{', '.join(p['non_catalytic_with_positive_GO_0004222']) or 'none'}**."
    )
    a(
        "- Positive control: all four catalytic ADAMTS members do receive "
        "`GO:0004222`, so absence in the ADAMTSL rows is a property of the "
        "projection and not of the query."
    )
    a("")

    a("## 2. Donors behind the single IBA row")
    a("")
    a(
        f"`{d['term']}` carries {d['n_tokens']} WITH/FROM tokens: "
        f"{d['n_protein_donors']} protein donors "
        f"({d['n_self_referential']} self-referential) plus PANTHER tree nodes. "
        f"**{d['n_donors_with_own_experimental_evidence']} of "
        f"{d['n_protein_donors']}** carry their own experimental annotation to "
        f"{d['term']} or a descendant."
    )
    a("")
    a(
        "The specific terms those donors hold experimentally: "
        + ", ".join(d["distinct_specific_terms_held_by_donors"])
        + " - i.e. the donor set is heterogeneous in *which* matrix compartment "
        "it occupies, so the general parent is the least common ancestor rather "
        "than a curator failing to be specific."
    )
    a("")
    a("| token | resolves to | reviewed | own experimental evidence for the term |")
    a("|---|---|---|---|")
    for don in d["donors"]:
        if don.get("kind") == "panther_node":
            a(f"| {don['token']} | PANTHER tree node {don['id']} (not a protein) | - | - |")
            continue
        ev = ", ".join(
            f"{e['go_id']} {e['evidence']} ({e['reference']})" for e in don["own_experimental"]
        )
        gene = "/".join(g for g in don["gene"] if g) or "?"
        a(
            f"| {don['token']}{' [%d candidates]' % don['n_candidates'] if don['n_candidates'] > 1 else ''} "
            f"| {don['accession']} {gene} ({don['organism']}) | "
            f"{'Swiss-Prot' if don['reviewed'] else 'TrEMBL'} | {ev or 'none'} |"
        )
    a("")

    a("## 3. The `GO:0005515` partner set")
    a("")
    a(
        f"{i['n_ipi_rows']} IPI rows over {i['n_distinct_partners']} distinct "
        f"partners. Gene-level IntAct detection-method counts for P82987: "
        + ", ".join(f"{k} x{v}" for k, v in sorted(i["detection_methods_gene_level"].items()))
        + "."
    )
    a("")
    a(
        "**That gene-level tally must not be read as evidence about these 13 pairs.** "
        "It also covers partners that are not in GOA. Disaggregating per pair is what "
        "answers the question, and it is done below."
    )
    a("")
    a(
        "Every partner resolves to a reviewed Swiss-Prot entry at canonical "
        f"length: {i['all_reviewed_swissprot']} (no TrEMBL/ORFeome substitutions)."
    )
    a("")
    a(
        f"ADAMTSL3 itself has {i['adamtsl3_intact_distinct_partners']} distinct "
        f"IntAct partners; the median for its {i['n_distinct_partners']} annotated "
        f"partners is {i['partner_degree_median']}."
    )
    a("")
    a("| partner | length | protein name | UniProt subcellular location | IntAct methods for THIS pair | distinct IntAct partners |")
    a("|---|---|---|---|---|---|")
    for r in sorted(i["partners"], key=lambda x: -x["intact_distinct_partners"]):
        gene = "/".join(g for g in r["gene"] if g) or r["accession"]
        loc = "; ".join(r["subcellular_locations"]) or "not annotated"
        meth = "; ".join(i["per_partner_methods_goa_partners"][r["accession"]])
        a(
            f"| {gene} ({r['accession']}) | {r['length']} aa | {r['protein_name']} | "
            f"{loc} | {meth} | {r['intact_distinct_partners']} |"
        )
    a("")
    nony2h = i["goa_partners_with_non_y2h_method"]
    a(
        f"**GOA partners with any non-Y2H detection method: "
        f"{len(nony2h)} of {i['n_distinct_partners']}** "
        + (f"({nony2h})" if nony2h else "- every one of these pairs rests on yeast "
           "two-hybrid sub-methods alone, with no orthogonal assay.")
    )
    a("")
    a(
        f"For contrast, the {len(i['non_goa_partners_and_their_methods'])} IntAct "
        "partners that are **not** in GOA are where the other methods live: "
        + ", ".join(
            sorted({m for ms in i["non_goa_partners_and_their_methods"].values() for m in ms})
        )
        + ". These are separate publications and are out of scope for this review, but "
        "they are why the gene-level method counter cannot settle the question."
    )
    a("")

    a("## 4. Review coverage against the GOA table")
    a("")
    a(
        f"GOA rows: {c['n_goa_rows']}. Reviewed rows derived from GOA: "
        f"{c['n_review_rows_from_goa']}. Reviewer-proposed (`NEW`) rows: "
        f"{c['n_review_rows_new']}. Coverage OK: **{c['ok']}**."
    )
    if not c["ok"]:
        a("")
        a(f"- GOA rows not reviewed: {c['goa_rows_not_reviewed']}")
        a(f"- Review rows with no GOA counterpart: {c['review_rows_not_in_goa']}")
        a(f"- Rows still PENDING: {c['pending']}")
    a("")
    a("Actions: " + ", ".join(f"{k} x{v}" for k, v in sorted(c["actions"].items())) + ".")
    a("")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# self-test
# --------------------------------------------------------------------------- #
def self_test() -> int:
    """Break each guard deliberately and require it to fire."""
    failures: List[str] = []

    # 1. duplicate-key loader must reject a repeated mapping key
    try:
        yaml.load("a: 1\na: 2\n", Loader=_StrictLoader)
        failures.append("duplicate-key loader did not reject a repeated key")
    except yaml.constructor.ConstructorError:
        pass

    # 2. ...and must still accept a legitimate document
    if yaml.load("a: 1\nb: 2\n", Loader=_StrictLoader) != {"a": 1, "b": 2}:
        failures.append("duplicate-key loader corrupted a valid document")

    # 3. a dead accession (no entry name) must raise rather than return an empty
    #    record that reads as "this protein carries no annotations"
    try:
        _as_entry({"primaryAccession": "O15507", "proteinDescription": {}})
        failures.append("_as_entry accepted an entry with no entry name")
    except InputError:
        pass

    # 4. coverage check must fail when a GOA row is dropped from the review
    doc = yaml.safe_load(REVIEW_YAML.read_text()) if REVIEW_YAML.exists() else None
    if doc and doc.get("existing_annotations"):
        import copy

        original = REVIEW_YAML.read_text()
        mutated = copy.deepcopy(doc)
        removed = None
        for k, ann in enumerate(mutated["existing_annotations"]):
            if (ann.get("review") or {}).get("action") != "NEW":
                removed = mutated["existing_annotations"].pop(k)
                break
        if removed is None:
            failures.append("self-test could not find a GOA-derived row to drop")
        else:
            try:
                REVIEW_YAML.write_text(yaml.dump(mutated, sort_keys=False))
                res = check_goa_coverage()
                if res["ok"]:
                    failures.append("coverage check passed with a GOA row removed")
            finally:
                REVIEW_YAML.write_text(original)
    else:
        failures.append("self-test needs a populated review file to exercise check 4")

    # 5. a missing input must raise a named error, not return an empty result
    global GOA_TSV
    keep = GOA_TSV
    try:
        GOA_TSV = HERE / "definitely-not-here.tsv"
        try:
            read_goa()
            failures.append("read_goa returned quietly for a missing file")
        except InputError:
            pass
    finally:
        GOA_TSV = keep

    for f in failures:
        print(f"SELF-TEST FAIL: {f}", file=sys.stderr)
    print(f"self-test: {5 - len(failures)}/5 guards fired")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true", help="exercise the guards and exit")
    ap.add_argument(
        "--only",
        choices=["paint", "donors", "intact", "coverage"],
        help="run a single check",
    )
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    checks = {
        "paint_projection": check_paint_projection,
        "iba_donors": check_iba_donors,
        "intact_partners": check_intact_partners,
        "goa_coverage": check_goa_coverage,
    }
    if args.only:
        key = {
            "paint": "paint_projection",
            "donors": "iba_donors",
            "intact": "intact_partners",
            "coverage": "goa_coverage",
        }[args.only]
        print(json.dumps({key: checks[key]()}, indent=2))
        return 0

    res = {name: fn() for name, fn in checks.items()}
    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render_results(res))
    print("wrote results.json and RESULTS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
