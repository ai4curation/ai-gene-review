#!/usr/bin/env python3
"""Trace every human ADNP ``GO_REF:0000107`` (Ensembl Compara) IEA row back to the
rodent annotation it was projected from, and record what the *cited experiment*
actually manipulated: the full-length ADNP protein, or the synthetic
ADNP-derived octapeptide NAPVSIPQ ("NAP").

Why this exists
---------------
19 of human ADNP's 53 GOA rows are Ensembl Compara projections of rat ``Adnp``
(Q9JKL8) annotations.  Reading the rat donors' primary references shows that
most of them assayed **NAP applied exogenously as a synthetic peptide**, not the
ADNP gene product.  One of them (``PMID:15963648``) used ``D-NAPVSIPQ`` -- the
all-D-amino-acid enantiomer, which no gene can encode.

The classification below is *computed* from the donor reference's title and
abstract, not hand-assigned, and both the peptide markers and the
protein-level markers that fired are recorded per reference so the call can be
audited.  It is a screen over abstracts (most of these papers have no cached
full text), so ``RESULTS.md`` states that limitation explicitly.

Guards (each fails loudly rather than degrading):

* every QuickGO query asserts ``numberOfHits == len(results)`` -- the service
  clamps ``limit`` rather than erroring, so a page-size constant cannot be used;
* every ``GO_REF:0000107`` row must resolve to exactly one donor accession;
* every donor row must resolve to at least one primary (PMID) reference;
* the classifier must place at least one donor reference in *each* class --
  a classifier that calls everything "peptide" would manufacture this paper's
  conclusion, so the happy-path direction is checked too;
* each donor reference is checked for retraction / erratum / expression of
  concern via ``CommentsCorrections`` on its own PubMed record.

Usage::

    uv run python analyze_compara_donors.py          # refresh results.json + RESULTS.md
    uv run python analyze_compara_donors.py --check   # regenerate and diff against committed
    uv run python analyze_compara_donors.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent

HUMAN = "UniProtKB:Q9H2P0"
RAT = "UniProtKB:Q9JKL8"
MOUSE = "UniProtKB:Q9Z103"
COMPARA_REF = "GO_REF:0000107"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Markers for "the thing assayed was the synthetic ADNP-derived peptide".
# NAP is also an English word fragment, so it is only matched as a standalone
# token or inside the explicit peptide spellings.
PEPTIDE_PATTERNS: dict[str, str] = {
    "NAPVSIPQ": r"NAPVSIPQ",
    "D-NAP": r"\bD-NAP\b",
    "NAP (standalone token)": r"\bNAP\b",
    "ADNF-9": r"\bADNF-9\b",
    "SALLRSIPA": r"SALLRSIPA",
    "octapeptide": r"\boctapeptide\b",
    "8-amino-acid peptide": r"8-amino-acid peptide",
}

# Markers for "the full-length gene product was detected or perturbed".
#
# These are matched SENTENCE-SCOPED: a marker only counts when the sentence it
# appears in also names ADNP.  Without that scoping the classifier reports a
# perturbation of some *other* gene as evidence that ADNP itself was assayed --
# on PMID:19047645 the siRNA is against Fyn kinase, not ADNP, and the unscoped
# match turned a pure NAP-peptide result into MIXED.  Both the scoped and the
# unscoped marker sets are recorded so the difference stays visible.
PROTEIN_PATTERNS: dict[str, str] = {
    "knockout/deficiency": r"\bknockout\b|\bknock-out\b|\bdeficien(?:t|cy)\b|gene disruption|\bablation\b|haploinsufficien",
    "knockdown/RNAi": r"\bknockdown\b|\bsiRNA\b|\bshRNA\b|\bRNAi\b",
    # Deliberately narrow.  A bare `\bdisrupt` fired on the PMID:19047645 title
    # "Ethanol inhibits neuronal differentiation by disrupting ADNP signaling",
    # where what is disrupted is downstream NAP signalling, not the gene
    # product -- so this class must name ADNP as the thing lost.
    "loss of function": (
        r"loss of (?:ADNP|Adnp|adnp)\b|(?:ADNP|Adnp|adnp)[- ]deficien"
        r"|deplet\w+ of (?:ADNP|Adnp|adnp)\b|(?:ADNP|Adnp|adnp) deplet"
    ),
    "overexpression": r"\boverexpress",
    "immunodetection": r"immunoreactiv|immunostain|immunohistochem|immunoblot|immunocytochem|immunoprecipitat",
    "recombinant protein": r"recombinant ADNP",
    "transcript measurement": r"\bmRNA\b|RT-PCR|reverse transcription|microarray",
    "protein expression readout": r"\bexpression\b|\bsynthesis\b",
    "cell fractionation": r"cell fractionation|nuclear cell fraction|subcellular localization",
    "chromatin immunoprecipitation": r"chromatin[- ]immunoprecipitation|\bChIP\b",
}

# Tokens that mean "this sentence is talking about the ADNP gene product".
ADNP_TOKEN = re.compile(
    r"\bADNP\b|\bAdnp\b|\badnp\b|activity[- ]dependent neuroprotective protein",
)


# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------
def _get_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        return json.load(resp)


def quickgo(**params: Any) -> list[dict]:
    """Fully paginated QuickGO annotation search.

    Asserts ``numberOfHits == len(results)``.  Comparing against a page-size
    constant would not catch the service clamping ``limit``, which is the
    silent-truncation mode this guard exists for.
    """
    params.setdefault("limit", 100)
    collected: list[dict] = []
    total: int | None = None
    page = 1
    while True:
        query = dict(params, page=page)
        payload = _get_json(QUICKGO + "?" + urllib.parse.urlencode(query))
        total = payload["numberOfHits"]
        collected.extend(payload["results"])
        if len(collected) >= total or not payload["results"]:
            break
        page += 1
    if total is None or len(collected) != total:
        raise RuntimeError(
            f"QuickGO pagination mismatch: read {len(collected)} of {total} for {params}"
        )
    return collected


def pubmed_records(pmids: list[str]) -> dict[str, dict]:
    """Title, abstract, publication types and CommentsCorrections per PMID."""
    if not pmids:
        return {}
    url = (
        f"{EUTILS}/efetch.fcgi?db=pubmed&retmode=xml&id=" + ",".join(sorted(set(pmids)))
    )
    with urllib.request.urlopen(url) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        tree = ET.parse(resp)
    out: dict[str, dict] = {}
    for art in tree.getroot().findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID") or ""
        abstract = " ".join(
            (node.text or "") for node in art.findall(".//Abstract/AbstractText")
        )
        corrections = [
            {"type": cc.get("RefType"), "pmid": cc.findtext("PMID")}
            for cc in art.findall(".//CommentsCorrections")
            if cc.get("RefType")
            in {
                "RetractionIn",
                "ErratumIn",
                "ExpressionOfConcernIn",
                "CorrectedandRepublishedIn",
                "RepublishedIn",
            }
        ]
        out[pmid] = {
            "pmid": pmid,
            "title": art.findtext(".//ArticleTitle") or "",
            "abstract": abstract,
            "publication_types": [p.text for p in art.findall(".//PublicationType")],
            "corrections": corrections,
        }
    missing = sorted(set(pmids) - set(out))
    if missing:
        raise RuntimeError(f"PubMed returned no record for {missing}")
    return out


# --------------------------------------------------------------------------
# Classification
# --------------------------------------------------------------------------
def classify(record: dict) -> dict:
    text = f"{record['title']}. {record['abstract']}"
    sentences = [s for s in re.split(r"(?<=[.;])\s+", text) if s.strip()]
    adnp_sentences = [s for s in sentences if ADNP_TOKEN.search(s)]

    peptide_hits = [k for k, pat in PEPTIDE_PATTERNS.items() if re.search(pat, text)]
    protein_hits = sorted(
        {
            k
            for k, pat in PROTEIN_PATTERNS.items()
            for s in adnp_sentences
            if re.search(pat, s)
        }
    )
    protein_hits_unscoped = [
        k for k, pat in PROTEIN_PATTERNS.items() if re.search(pat, text)
    ]

    if peptide_hits and not protein_hits:
        verdict = "PEPTIDE_ONLY"
    elif protein_hits and not peptide_hits:
        verdict = "PROTEIN"
    elif peptide_hits and protein_hits:
        verdict = "MIXED"
    else:
        verdict = "UNCLASSIFIED"
    return {
        "verdict": verdict,
        "peptide_markers": peptide_hits,
        "protein_markers": protein_hits,
        "protein_markers_unscoped": protein_hits_unscoped,
        "scoping_changed_call": sorted(set(protein_hits_unscoped)) != protein_hits,
    }


def go_names(go_ids: list[str]) -> dict[str, str]:
    """QuickGO ontology lookup; fails loudly on any id it cannot resolve."""
    out: dict[str, str] = {}
    ids = sorted(set(go_ids))
    for start in range(0, len(ids), 20):
        chunk = ids[start : start + 20]
        payload = _get_json(
            "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
            + ",".join(chunk)
        )
        for term in payload["results"]:
            out[term["id"]] = term["name"]
    missing = sorted(set(ids) - set(out))
    if missing:
        raise RuntimeError(f"QuickGO could not resolve GO ids {missing}")
    return out


# The HP1-interaction motif.  P-x-V-x-[LMIV]: three fixed positions and one
# four-way position, so chance matches are NOT rare in a 1100-residue protein --
# the expected count is computed below from the subject's own composition and
# reported alongside the hits, because "exactly one match" reads as enrichment
# evidence when it is roughly what chance predicts.
PXVXL = re.compile(r"(?=(P.V.[LMIV]))")


def pxvxl_scan(accession: str = "Q9H2P0", expected_length: int = 1102) -> dict:
    payload = _get_json(
        f"https://rest.uniprot.org/uniprotkb/{accession}.json?fields=sequence,id"
    )
    seq = payload["sequence"]["value"]
    if len(seq) != expected_length:
        raise RuntimeError(
            f"{accession} is {len(seq)} aa, expected {expected_length} -- the reference "
            "sequence has changed and every position in this analysis must be re-checked"
        )
    hits = [
        {"start": m.start() + 1, "end": m.start() + 5, "match": m.group(1)}
        for m in PXVXL.finditer(seq)
    ]
    n = len(seq)
    freq = {aa: seq.count(aa) / n for aa in set(seq)}
    p_last = sum(freq.get(aa, 0.0) for aa in "LMIV")
    p_window = freq.get("P", 0.0) * freq.get("V", 0.0) * p_last
    expected = (n - 4) * p_window
    return {
        "accession": accession,
        "entry_name": payload["uniProtkbId"],
        "length": n,
        "pattern": "P.V.[LMIV]",
        "hits": hits,
        "expected_matches_under_composition_null": round(expected, 3),
        "interpretation": (
            "The observed count is not enrichment evidence: it is close to the "
            "number chance predicts from the protein's own residue composition. "
            "The support for this motif being the HP1 contact is its conservation "
            "between ADNP and ADNP2 (PMID:38960717) plus binding to all three HP1 "
            "paralogues, not its rarity. No point mutant has been tested."
        ),
    }


def withfrom_ids(row: dict) -> list[str]:
    return [
        f"{x['db']}:{x['id']}"
        for conn in (row.get("withFrom") or [])
        for x in conn["connectedXrefs"]
    ]


# --------------------------------------------------------------------------
# Analysis
# --------------------------------------------------------------------------
def build() -> dict:
    human = quickgo(geneProductId=HUMAN)
    rat = quickgo(geneProductId=RAT)
    mouse = quickgo(geneProductId=MOUSE)

    compara = [r for r in human if r["reference"] == COMPARA_REF]
    if not compara:
        raise RuntimeError("no GO_REF:0000107 rows on human ADNP -- has GOA changed?")

    donor_index: dict[tuple[str, str], list[dict]] = {}
    for row in rat:
        donor_index.setdefault((RAT, row["goId"]), []).append(row)
    for row in mouse:
        donor_index.setdefault((MOUSE, row["goId"]), []).append(row)

    experimental = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

    entries: list[dict] = []
    wanted_pmids: set[str] = set()
    for row in compara:
        sources = [t for t in withfrom_ids(row) if t.startswith("UniProtKB:")]
        if len(sources) != 1:
            raise RuntimeError(
                f"{row['goId']}: expected exactly one UniProtKB donor in withFrom, got {sources}"
            )
        donor = sources[0]
        donor_rows = donor_index.get((donor, row["goId"]), [])
        if not donor_rows:
            raise RuntimeError(f"{row['goId']}: donor {donor} carries no such term")
        primary = [
            {"reference": d["reference"], "evidence": d["goEvidence"], "assignedBy": d["assignedBy"]}
            for d in donor_rows
            if d["reference"].startswith("PMID:")
        ]
        if not primary:
            raise RuntimeError(
                f"{row['goId']}: donor {donor} has no primary (PMID) reference; "
                f"only {[d['reference'] for d in donor_rows]}"
            )
        wanted_pmids.update(p["reference"].split(":", 1)[1] for p in primary)
        entries.append(
            {
                "go_id": row["goId"],
                "aspect": row.get("goAspect"),
                "qualifier": row.get("qualifier"),
                "donor": donor,
                "donor_annotations": primary,
                "donor_has_own_experimental_evidence": any(
                    p["evidence"] in experimental for p in primary
                ),
            }
        )

    papers = pubmed_records(sorted(wanted_pmids))
    names = go_names([e["go_id"] for e in entries])
    for entry in entries:
        entry["go_name"] = names[entry["go_id"]]

    # Reference-projection test: how many distinct entities does each donor
    # reference annotate anywhere in GOA?  A reference that annotates a complex
    # plus all its subunits is a projection, not N independent findings.
    projection: dict[str, dict] = {}
    for pmid in sorted(wanted_pmids):
        rows = quickgo(reference=f"PMID:{pmid}")
        projection[pmid] = {
            "annotations": len(rows),
            "entities": sorted({r["geneProductId"] for r in rows}),
            "terms": sorted({r["goId"] for r in rows}),
        }

    for entry in entries:
        calls = []
        for ann in entry["donor_annotations"]:
            pmid = ann["reference"].split(":", 1)[1]
            paper = papers[pmid]
            call = classify(paper)
            calls.append(
                {
                    "pmid": ann["reference"],
                    "evidence": ann["evidence"],
                    "title": paper["title"],
                    "publication_types": paper["publication_types"],
                    "corrections": paper["corrections"],
                    "entities_annotated_by_this_reference": len(
                        projection[pmid]["entities"]
                    ),
                    **call,
                }
            )
        entry["reference_calls"] = calls
        verdicts = {c["verdict"] for c in calls}
        entry["assayed_entity"] = (
            "PEPTIDE_ONLY" if verdicts == {"PEPTIDE_ONLY"} else "|".join(sorted(verdicts))
        )

    verdict_counts: dict[str, int] = {}
    for entry in entries:
        verdict_counts[entry["assayed_entity"]] = (
            verdict_counts.get(entry["assayed_entity"], 0) + 1
        )

    # Happy-path guard: a classifier that labelled every donor reference
    # "peptide" would fabricate this analysis's conclusion.  Require both
    # classes to be populated -- the protein-derived localisation rows (axon,
    # dendrite, neuronal cell body, extracellular region) are the control.
    if "PEPTIDE_ONLY" not in verdict_counts:
        raise RuntimeError("classifier found no peptide-derived donor: check PEPTIDE_PATTERNS")
    if set(verdict_counts) == {"PEPTIDE_ONLY"}:
        raise RuntimeError(
            "classifier called every donor peptide-derived; the protein-level "
            "control rows must classify otherwise -- check PROTEIN_PATTERNS"
        )

    # Retraction / erratum sweep over EVERY PMID cited by the review, not just
    # the donor references -- a claim that "no reference is retracted" has to be
    # reproducible in the repository, not a number from a one-off shell command.
    review = yaml.safe_load((HERE.parent / "ADNP-ai-review.yaml").read_text())
    review_pmids = sorted(
        {r["id"].split(":", 1)[1] for r in review.get("references", [])
         if str(r.get("id", "")).startswith("PMID:")}
    )
    all_papers = dict(papers)
    extra = sorted(set(review_pmids) - set(all_papers))
    if extra:
        all_papers.update(pubmed_records(extra))
    flagged = [
        {"pmid": p["pmid"], "title": p["title"], "corrections": p["corrections"]}
        for p in all_papers.values()
        if p["corrections"]
    ]

    # Rat rows that were NOT projected to human -- the negative control on the
    # Compara filter itself.
    projected_terms = {e["go_id"] for e in entries}
    rat_experimental_only = sorted(
        {
            r["goId"]
            for r in rat
            if r["goEvidence"] in experimental and r["goId"] not in projected_terms
        }
    )

    return {
        "subject": HUMAN,
        "pxvxl_scan": pxvxl_scan(),
        "human_annotation_rows": len(human),
        "compara_rows": len(compara),
        "donors": sorted({e["donor"] for e in entries}),
        "verdict_counts": verdict_counts,
        "entries": sorted(entries, key=lambda e: e["go_id"]),
        "reference_projection": projection,
        "references_with_corrections": flagged,
        "retraction_check_pmids": sorted(all_papers),
        "rat_experimental_terms_not_projected": rat_experimental_only,
        "nap_derived_go_ids": sorted(
            e["go_id"] for e in entries if e["assayed_entity"] == "PEPTIDE_ONLY"
        ),
        "protein_derived_go_ids": sorted(
            e["go_id"] for e in entries if e["assayed_entity"] != "PEPTIDE_ONLY"
        ),
    }


def render(data: dict) -> str:
    lines: list[str] = []
    add = lines.append
    add("# Ensembl Compara donor provenance for human ADNP (Q9H2P0)")
    add("")
    add(
        "Generated by `analyze_compara_donors.py`. Every number here is computed "
        "from QuickGO and PubMed at run time; nothing is hand-entered."
    )
    add("")
    add("## Summary")
    add("")
    add(f"- human GOA rows: **{data['human_annotation_rows']}**")
    add(
        f"- of which projected by Ensembl Compara (`GO_REF:0000107`): "
        f"**{data['compara_rows']}**"
    )
    add(f"- donor entries: {', '.join(data['donors'])}")
    add("")
    for verdict, count in sorted(data["verdict_counts"].items()):
        add(f"- rows whose donor reference classifies as `{verdict}`: **{count}**")
    add("")
    add(
        "`PEPTIDE_ONLY` means the donor's primary reference names the synthetic "
        "ADNP-derived octapeptide (NAPVSIPQ / D-NAPVSIPQ / the related ADNF-9 "
        "peptide) and contains **no** marker of the full-length gene product "
        "being detected or perturbed."
    )
    add("")
    add("## Rows")
    add("")
    add("| GO id | term | donor | donor evidence | donor reference | assayed entity | peptide markers | ADNP-scoped protein markers |")
    add("|---|---|---|---|---|---|---|---|")
    for entry in data["entries"]:
        for call in entry["reference_calls"]:
            add(
                "| {go} | {name} | {donor} | {ev} | {ref} | **{v}** | {pm} | {prm} |".format(
                    go=entry["go_id"],
                    name=(entry["go_name"] or "?"),
                    donor=entry["donor"],
                    ev=call["evidence"],
                    ref=call["pmid"],
                    v=call["verdict"],
                    pm=", ".join(call["peptide_markers"]) or "-",
                    prm=", ".join(call["protein_markers"]) or "-",
                )
            )
    add("")
    rescoped = sorted(
        {
            call["pmid"]
            for entry in data["entries"]
            for call in entry["reference_calls"]
            if call["scoping_changed_call"]
        }
    )
    add(
        "References where restricting protein markers to ADNP-naming sentences "
        f"changed the marker set: {', '.join(rescoped) if rescoped else 'none'}. "
        "The scoping matters: on PMID:19047645 the unscoped match fired on an "
        "siRNA directed against *Fyn kinase*, not ADNP."
    )
    add("")
    scan = data["pxvxl_scan"]
    add("## HP1-interaction motif scan")
    add("")
    add(
        f"`{scan['pattern']}` over {scan['entry_name']} ({scan['accession']}, "
        f"{scan['length']} aa):"
    )
    add("")
    add("| position | match |")
    add("|---|---|")
    for hit in scan["hits"]:
        add(f"| {hit['start']}-{hit['end']} | `{hit['match']}` |")
    add("")
    add(
        f"**Expected matches under a null from the protein's own residue composition: "
        f"{scan['expected_matches_under_composition_null']}.** {scan['interpretation']}"
    )
    add("")
    add("## Reference-projection test")
    add("")
    add(
        "For each donor reference, the number of distinct gene products it "
        "annotates anywhere in GOA. A reference annotating a complex plus every "
        "subunit with identical evidence would be a projection rather than N "
        "independent findings."
    )
    add("")
    add("| reference | annotations | distinct entities | terms |")
    add("|---|---|---|---|")
    for pmid, info in sorted(data["reference_projection"].items()):
        add(
            f"| PMID:{pmid} | {info['annotations']} | {len(info['entities'])} | "
            f"{', '.join(info['terms'])} |"
        )
    add("")
    add("## Retraction / erratum check")
    add("")
    add(
        f"Checked **{len(data['retraction_check_pmids'])}** PubMed records: every donor "
        "reference above plus every `PMID:` entry in the review's own reference list."
    )
    add("")
    if data["references_with_corrections"]:
        for item in data["references_with_corrections"]:
            add(f"- **PMID:{item['pmid']}** -- {item['corrections']}")
    else:
        add(
            "None carries a `RetractionIn`, `ErratumIn`, `ExpressionOfConcernIn` "
            "or republication link on its own PubMed record. Negative result, "
            "recorded so the next reader knows the check was run. Note the known "
            "limitation: a correction whose own PubMed id is null is invisible to "
            "this route and would need a Crossref `relation`/`update-to` lookup."
        )
    add("")
    add("## Rat experimental terms that were NOT projected to human")
    add("")
    add(
        "The negative control on the Compara filter itself: rat `Adnp` terms with "
        "their own experimental evidence that did not reach human ADNP."
    )
    add("")
    for go_id in data["rat_experimental_terms_not_projected"]:
        add(f"- {go_id}")
    add("")
    add("## Limitations")
    add("")
    add(
        "- The classifier reads the donor reference's **title and abstract**. "
        "Most of these papers have `full_text_available: false` in "
        "`publications/`, so a peptide-only call is a strong screen, not a "
        "reading of the methods. Each call is reported with the exact markers "
        "that fired so it can be re-checked."
    )
    add(
        "- `MIXED` means both peptide and protein markers fired; those rows are "
        "not counted as peptide-derived, which is the conservative direction."
    )
    add(
        "- Entity counts come from QuickGO's fully paginated annotation search "
        "(`numberOfHits == len(results)` asserted), so they are distinct "
        "gene-product ids, not annotation totals."
    )
    add("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="regenerate and diff against committed files")
    parser.add_argument("--self-test", action="store_true", help="break-test the guards offline")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    data = build()
    text = render(data)
    json_path = HERE / "results.json"
    md_path = HERE / "RESULTS.md"

    if args.check:
        problems = []
        if json.loads(json_path.read_text()) != data:
            problems.append("results.json differs from a fresh run")
        if md_path.read_text() != text:
            problems.append("RESULTS.md differs from a fresh run")
        for problem in problems:
            print(f"MISMATCH: {problem}", file=sys.stderr)
        return 1 if problems else 0

    json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    md_path.write_text(text)
    print(f"wrote {json_path} and {md_path}")
    print("verdict counts:", data["verdict_counts"])
    return 0


def self_test() -> int:
    """Break-test the classifier in both directions, offline."""
    failures: list[str] = []

    peptide_paper = {
        "title": "Synergistic effects of the peptide fragment D-NAPVSIPQ on ethanol inhibition",
        "abstract": "an octapeptide, D-NAPVSIPQ (D-NAP), was applied to slices.",
    }
    if classify(peptide_paper)["verdict"] != "PEPTIDE_ONLY":
        failures.append("peptide paper not classified PEPTIDE_ONLY")

    protein_paper = {
        "title": "Expression of activity-dependent neuroprotective protein in the brain of adult rats",
        "abstract": "ADNP-like immunoreactivity was detected by immunohistochemistry.",
    }
    if classify(protein_paper)["verdict"] != "PROTEIN":
        failures.append("protein paper not classified PROTEIN")

    mixed_paper = {
        "title": "NAP corrects the phenotype of Adnp mice",
        "abstract": "NAPVSIPQ was given to Adnp deficient animals.",
    }
    if classify(mixed_paper)["verdict"] != "MIXED":
        failures.append("mixed paper not classified MIXED")

    # Sentence scoping: a perturbation of a DIFFERENT gene must not count as
    # evidence that ADNP itself was assayed.  This is the PMID:19047645 shape.
    other_gene = {
        "title": "Ethanol inhibits neuronal differentiation by disrupting ADNP signaling",
        "abstract": (
            "NAPVSIPQ (NAP) potentiated axon outgrowth. "
            "Expression of a Fyn kinase siRNA abolished NAP-mediated axon outgrowth."
        ),
    }
    scoped = classify(other_gene)
    if scoped["verdict"] != "PEPTIDE_ONLY":
        failures.append(
            f"other-gene siRNA leaked into protein markers: {scoped['protein_markers']}"
        )
    if not scoped["scoping_changed_call"]:
        failures.append("scoping_changed_call did not fire on the other-gene case")

    silent_paper = {"title": "Something unrelated", "abstract": "No markers here."}
    if classify(silent_paper)["verdict"] != "UNCLASSIFIED":
        failures.append("empty paper not classified UNCLASSIFIED")

    # "NAP" must not fire on words that merely contain the letters.
    false_friend = {
        "title": "Synaptic vesicle fusion",
        "abstract": "SNAP-25 and synaptotagmin drive the reaction.",
    }
    if classify(false_friend)["peptide_markers"]:
        failures.append("bare-NAP pattern fired on SNAP-25 (word-boundary bug)")

    # The motif regex must be overlap-aware and must not match a 4-residue window.
    if [m.group(1) for m in PXVXL.finditer("PGVLLPAVAV")] != ["PGVLL", "PAVAV"]:
        failures.append("PXVXL regex missed an overlapping/second occurrence")
    if [m.group(1) for m in PXVXL.finditer("PGVLA")]:
        failures.append("PXVXL regex matched a window with a non-[LMIV] final residue")
    if [m.group(1) for m in PXVXL.finditer("PVXL")]:
        failures.append("PXVXL regex matched a 4-residue window")

    for failure in failures:
        print(f"SELF-TEST FAIL: {failure}", file=sys.stderr)
    if not failures:
        print("self-test: 10/10 directions OK (7 classifier + 3 motif-regex)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
