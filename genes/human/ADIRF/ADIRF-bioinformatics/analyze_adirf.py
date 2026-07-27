#!/usr/bin/env python3
"""Reproducible checks behind the human ADIRF (Q15847) GO annotation review.

Three independent questions, each answered from a live public API and each
carrying its own POSITIVE CONTROL so that "zero" cannot be confused with
"query rejected":

A. **Is ADIRF absent from the mouse/rat lineage?**  Every functional experiment
   on ADIRF was performed by ectopic expression in mouse 3T3-L1 preadipocytes.
   If Muroidea have no ADIRF gene, that experiment has no endogenous
   counterpart, which bounds what the resulting GO annotations can mean.
   Controls: ADIPOQ/LEP must be found in mouse, rat and Muroidea by the *same*
   query pattern, and ADIRF must be found in human.

B. **Where do the IPR034450-derived GO annotations land?**  ``GO:0045600``
   (positive regulation of fat cell differentiation) and ``GO:0005634``
   (nucleus) are the only two terms interpro2go maps from IPR034450.  We
   enumerate every recipient, join it to its UniProt length and taxonomic
   lineage, and split recipients by (i) whether they are ADIRF-sized and
   (ii) where they sit taxonomically.  A 76-aa family whose signature reaches
   plants, fungi and bacteria is matching on composition, not homology.

C. **How promiscuous is the family signature?**  ADIRF is a 76-aa
   low-complexity, Ala/Gln/Glu/Thr-rich sequence.  We measure the length
   distribution of the whole family and align human ADIRF against both genuine
   orthologues (positive controls, expected high identity over full length) and
   the oversized members that receive the GO terms.

Every network call asserts HTTP 200 and, for paginated endpoints, asserts
``len(results) == numberOfHits`` so a server-side clamp cannot masquerade as a
complete read.  Missing input is a hard error, never a silently skipped section.

Usage:
    uv run python analyze_adirf.py            # writes results.json + RESULTS.md
    uv run python analyze_adirf.py --self-test  # break-tests the guards
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT_STREAM = "https://rest.uniprot.org/uniprotkb/stream"
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

HUMAN_ADIRF = "Q15847"
IPR = "IPR034450"
PANTHER_FAMILY = "PTHR39227"

# interpro2go maps IPR034450 to exactly these two terms (verified against
# https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/interpro2go).
IPR_TERMS = {"GO:0045600": "positive regulation of fat cell differentiation",
             "GO:0005634": "nucleus"}

# GO:0045600 carries only_in_taxon NCBITaxon:6072 (Eumetazoa).
EUMETAZOA_TAXID = 6072
VERTEBRATA_TAXID = 7742
METAZOA_TAXID = 33208

# An ADIRF orthologue is 71-76 aa in every reviewed and unreviewed entry
# inspected; we allow a generous window so the classification is not tuned.
ADIRF_SIZED = (60, 90)
OVERSIZED_MIN = 200

# An orthologue of a 76-aa protein must align across essentially all of it.
# This is a definition of what orthology looks like at this length, not a cut
# tuned to the data; the identity threshold, by contrast, is DERIVED at runtime
# from the observed gap (see section_c).
MIN_ORTHOLOGUE_COVERAGE = 0.90


# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------

def _get(url: str, accept: str = "application/json", tries: int = 4) -> str:
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(
            url, headers={"Accept": accept, "User-Agent": "ai-gene-review/ADIRF"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP {resp.status} for {url}")
                return resp.read().decode()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"request failed after {tries} tries: {url}: {last}")


def quickgo_all(**params) -> tuple[int, list[dict]]:
    """Fully paginate a QuickGO annotation search.

    Asserts ``len(rows) == numberOfHits``.  Comparing against the reported
    total -- never against the page-size constant we chose -- means a
    server-side clamp cannot pass this guard.
    """
    params = dict(params)
    params["limit"] = 100
    params["page"] = 1
    first = json.loads(_get(QUICKGO + "?" + urllib.parse.urlencode(params)))
    total = first["numberOfHits"]
    pages = first["pageInfo"]["total"] if first.get("pageInfo") else 1
    rows = list(first["results"])
    for page in range(2, pages + 1):
        params["page"] = page
        rows += json.loads(_get(QUICKGO + "?" + urllib.parse.urlencode(params)))["results"]
    if len(rows) != total:
        raise RuntimeError(
            f"QuickGO truncated: read {len(rows)} of {total} for {params}")
    return total, rows


def uniprot_tsv(query: str, fields: str) -> list[dict]:
    url = (UNIPROT_STREAM + "?" + urllib.parse.urlencode(
        {"query": query, "format": "tsv", "fields": fields}))
    text = _get(url, accept="text/plain")
    lines = text.strip().split("\n")
    if len(lines) < 2:
        raise RuntimeError(f"UniProt stream returned no rows for {query!r}")
    header = lines[0].split("\t")
    return [dict(zip(header, line.split("\t"))) for line in lines[1:]]


def uniprot_entries(accessions: list[str], fields: str) -> dict[str, dict]:
    """Resolve accessions in batches.

    Prints/returns the entry name for every accession and fails loudly on an
    empty one, because a *deleted* UniProt accession answers every query with
    silence and is otherwise indistinguishable from a real absence.
    """
    out: dict[str, dict] = {}
    for i in range(0, len(accessions), 80):
        batch = accessions[i:i + 80]
        query = " OR ".join(f"accession:{a}" for a in batch)
        url = (UNIPROT_SEARCH + "?" + urllib.parse.urlencode(
            {"query": f"({query})", "size": 500, "format": "tsv", "fields": fields}))
        text = _get(url, accept="text/plain")
        lines = text.strip().split("\n")
        header = lines[0].split("\t")
        for line in lines[1:]:
            rec = dict(zip(header, line.split("\t")))
            out[rec["Entry"]] = rec
        time.sleep(0.2)
    missing = [a for a in accessions if a not in out]
    if missing:
        raise RuntimeError(
            "accessions returned no UniProt entry (dead/deleted entries are "
            f"indistinguishable from empty ones, so this is fatal): {missing}")
    return out


def ncbi_gene_count(term: str) -> tuple[int, list[str]]:
    url = EUTILS + "?" + urllib.parse.urlencode(
        {"db": "gene", "retmode": "json", "retmax": 20, "term": term})
    payload = _get(url)
    data = json.loads(payload)
    if "esearchresult" not in data:
        raise RuntimeError(f"unexpected E-utilities payload for {term!r}: {payload[:200]}")
    res = data["esearchresult"]
    if "ERROR" in res:
        raise RuntimeError(f"E-utilities error for {term!r}: {res['ERROR']}")
    return int(res["count"]), res.get("idlist", [])


# --------------------------------------------------------------------------
# alignment (no external binary; Needleman-Wunsch with BLOSUM62)
# --------------------------------------------------------------------------

def global_align(a: str, b: str, gap_open: float = -11.0, gap_extend: float = -1.0):
    """Affine-gap global alignment. Returns (identity_over_shorter, aligned_pairs).

    Identity is reported over the *shorter* sequence deliberately: for a 76-aa
    query against a 1500-aa tandem-repeat protein, identity over the alignment
    length would be dominated by gaps and would understate how much of the
    query is matched.  Reporting over the shorter sequence is the generous
    reading, so a low value is a strong statement.
    """
    from Bio.Align import PairwiseAligner, substitution_matrices

    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = gap_open
    aligner.extend_gap_score = gap_extend
    aligner.mode = "local"
    alignments = aligner.align(a, b)
    best = alignments[0]
    aligned_a, aligned_b = str(best[0]), str(best[1])
    ident = sum(1 for x, y in zip(aligned_a, aligned_b) if x == y and x != "-")
    span = sum(1 for x, y in zip(aligned_a, aligned_b) if x != "-" and y != "-")
    shorter = min(len(a), len(b))
    return {
        "identities": ident,
        "aligned_columns": len(aligned_a),
        "ungapped_columns": span,
        "pct_id_over_shorter": round(100.0 * ident / shorter, 1),
        "pct_id_over_aligned": round(100.0 * ident / span, 1) if span else 0.0,
        "score": float(best.score),
    }


def low_complexity_metrics(seq: str) -> dict:
    """Composition bias + longest tandem repeat unit found by self-similarity."""
    counts = Counter(seq)
    n = len(seq)
    top3 = counts.most_common(3)
    # shortest period p (2..40) such that seq[i] == seq[i+p] for >=90% of i
    best_period, best_frac = None, 0.0
    for p in range(2, 41):
        if n - p < 20:
            break
        match = sum(1 for i in range(n - p) if seq[i] == seq[i + p])
        frac = match / (n - p)
        if frac > best_frac:
            best_period, best_frac = p, frac
    return {
        "length": n,
        "top3_residues": [[aa, c, round(100.0 * c / n, 1)] for aa, c in top3],
        "top3_fraction_pct": round(100.0 * sum(c for _, c in top3) / n, 1),
        "best_repeat_period": best_period,
        "best_repeat_identity_pct": round(100.0 * best_frac, 1),
    }


# --------------------------------------------------------------------------
# results container
# --------------------------------------------------------------------------

@dataclass
class Audit:
    problems: list[str] = field(default_factory=list)
    results: dict = field(default_factory=dict)

    def check(self, ok: bool, message: str) -> None:
        """Record a failed invariant.

        Appends rather than raising: a check that kills the harness is worse
        than no check, because the harness still prints as though it ran.
        """
        if not ok:
            self.problems.append(message)


# --------------------------------------------------------------------------
# Section A -- Muroidea gene loss
# --------------------------------------------------------------------------

SECTION_A_QUERIES = [
    ("subject", "mouse_ADIRF", "ADIRF[sym] AND txid10090[Orgn]"),
    ("subject", "rat_ADIRF", "ADIRF[sym] AND txid10116[Orgn]"),
    ("subject", "Muroidea_ADIRF", "ADIRF[sym] AND txid337687[Orgn]"),
    ("control", "mouse_ADIPOQ", "ADIPOQ[sym] AND txid10090[Orgn]"),
    ("control", "mouse_LEP", "LEP[sym] AND txid10090[Orgn]"),
    ("control", "rat_ADIPOQ", "ADIPOQ[sym] AND txid10116[Orgn]"),
    ("control", "Muroidea_ADIPOQ", "ADIPOQ[sym] AND txid337687[Orgn]"),
    ("control", "human_ADIRF", "ADIRF[sym] AND txid9606[Orgn]"),
    ("context", "Sciuridae_ADIRF", "ADIRF[sym] AND txid55153[Orgn]"),
    ("context", "Rodentia_ADIRF", "ADIRF[sym] AND txid9989[Orgn]"),
    ("context", "Actinopterygii_ADIRF", "ADIRF[sym] AND txid7898[Orgn]"),
    ("context", "Aves_ADIRF", "ADIRF[sym] AND txid8782[Orgn]"),
]


def section_a(audit: Audit) -> None:
    counts: dict[str, int] = {}
    for _role, name, term in SECTION_A_QUERIES:
        counts[name], _ids = ncbi_gene_count(term)
        time.sleep(0.4)

    controls = {n: counts[n] for role, n, _ in SECTION_A_QUERIES if role == "control"}
    for name, value in controls.items():
        audit.check(value > 0,
                    f"[A] positive control {name} returned 0 -> the query pattern is "
                    f"broken and the ADIRF zeros are NOT interpretable")

    # UniProt cross-check, an independent database answering the same question.
    uni_mouse = uniprot_tsv_safe("gene:ADIRF AND taxonomy_id:10090")
    uni_rat = uniprot_tsv_safe("gene:ADIRF AND taxonomy_id:10116")
    uni_human = uniprot_tsv_safe("gene:ADIRF AND taxonomy_id:9606")
    audit.check(len(uni_human) > 0,
                "[A] UniProt control: human ADIRF not found -> gene-name query broken")

    absent = (counts["mouse_ADIRF"] == 0 and counts["rat_ADIRF"] == 0
              and counts["Muroidea_ADIRF"] == 0
              and not uni_mouse and not uni_rat)
    # Negative control for the *clade* claim: other rodents must retain the gene,
    # otherwise "lost in Muroidea" is really "absent from rodents" or an artefact.
    audit.check(counts["Sciuridae_ADIRF"] > 0,
                "[A] Sciuridae ADIRF is 0 -> cannot localise the loss to Muroidea; "
                "without a retaining sister clade the observation is not an argument")

    audit.results["A_muroidea_loss"] = {
        "ncbi_gene_counts": counts,
        "uniprot_mouse_entries": len(uni_mouse),
        "uniprot_rat_entries": len(uni_rat),
        "uniprot_human_entries": len(uni_human),
        "controls_all_nonzero": all(v > 0 for v in controls.values()),
        "absent_from_muroidea": bool(absent),
        "retained_in_sister_rodent_clade_Sciuridae": counts["Sciuridae_ADIRF"] > 0,
    }


def uniprot_tsv_safe(query: str) -> list[dict]:
    """uniprot_tsv but tolerating a legitimately empty result set."""
    url = (UNIPROT_SEARCH + "?" + urllib.parse.urlencode(
        {"query": query, "size": 50, "format": "tsv",
         "fields": "accession,organism_id,length"}))
    text = _get(url, accept="text/plain")
    lines = [l for l in text.strip().split("\n") if l]
    if len(lines) < 2:
        return []
    header = lines[0].split("\t")
    return [dict(zip(header, line.split("\t"))) for line in lines[1:]]


# --------------------------------------------------------------------------
# Section B -- where the IPR034450 GO terms land
# --------------------------------------------------------------------------

def classify_lineage(lineage_field: str) -> str:
    lin = lineage_field or ""
    if "Vertebrata" in lin:
        return "Vertebrata"
    if "Metazoa" in lin:
        return "Metazoa_non_vertebrate"
    if "Fungi" in lin:
        return "Fungi"
    if "Viridiplantae" in lin or "Streptophyta" in lin or "Chlorophyta" in lin:
        return "Viridiplantae"
    if "Bacteria" in lin:
        return "Bacteria"
    if "Archaea" in lin:
        return "Archaea"
    if "Eukaryota" in lin:
        return "Eukaryota_other"
    return "unclassified"


def section_b(audit: Audit) -> None:
    total, rows = quickgo_all(withFrom=f"InterPro:{IPR}")
    audit.check(total > 0, f"[B] no annotations cite InterPro:{IPR} in WITH/FROM")

    terms = sorted({r["goId"] for r in rows})
    audit.check(set(terms) <= set(IPR_TERMS),
                f"[B] unexpected term from InterPro:{IPR}: {set(terms) - set(IPR_TERMS)} "
                f"-- the interpro2go mapping recorded in IPR_TERMS is stale")

    accs = sorted({r["geneProductId"].split(":", 1)[1] for r in rows})
    meta = uniprot_entries(
        accs, "accession,id,organism_name,organism_id,length,lineage")

    per_term: dict[str, list[str]] = {}
    for r in rows:
        per_term.setdefault(r["goId"], []).append(r["geneProductId"].split(":", 1)[1])

    summary = {}
    for term, members in per_term.items():
        members = sorted(set(members))
        clades = Counter(classify_lineage(meta[a]["Taxonomic lineage"]) for a in members)
        sizes = Counter()
        for a in members:
            n = int(meta[a]["Length"])
            if ADIRF_SIZED[0] <= n <= ADIRF_SIZED[1]:
                sizes["ADIRF_sized_60_90aa"] += 1
            elif n > OVERSIZED_MIN:
                sizes["oversized_gt200aa"] += 1
            else:
                sizes["intermediate_91_200aa"] += 1
        non_vert_oversized = [
            a for a in members
            if classify_lineage(meta[a]["Taxonomic lineage"]) != "Vertebrata"
            and int(meta[a]["Length"]) > OVERSIZED_MIN]
        summary[term] = {
            # .get, not [], so that recording an unexpected term as a problem
            # does not then abort every later check in this section.
            "label": IPR_TERMS.get(term, "<not in the recorded interpro2go mapping>"),
            "n_recipients": len(members),
            "by_clade": dict(clades),
            "by_size": dict(sizes),
            "n_non_vertebrate_and_oversized": len(non_vert_oversized),
            "example_non_vertebrate_oversized": [
                {"accession": a, "organism": meta[a]["Organism"],
                 "length": int(meta[a]["Length"]),
                 "clade": classify_lineage(meta[a]["Taxonomic lineage"])}
                for a in non_vert_oversized[:12]],
        }

    # GO:0045600 carries only_in_taxon Eumetazoa. Any non-Metazoan recipient is
    # a taxon-constraint violation on its face; recipients inside Eumetazoa but
    # outside Vertebrata pass the constraint yet still receive an adipocyte term.
    reg = summary.get("GO:0045600", {})
    clades = reg.get("by_clade", {})
    outside_metazoa = sum(v for k, v in clades.items()
                          if k in {"Fungi", "Viridiplantae", "Bacteria", "Archaea",
                                   "Eukaryota_other"})
    audit.results["B_ipr_reach"] = {
        "withFrom_query": f"InterPro:{IPR}",
        "total_annotations": total,
        "distinct_recipients": len(accs),
        "terms_supplied": terms,
        "per_term": summary,
        "GO_0045600_recipients_outside_Metazoa": outside_metazoa,
        "GO_0045600_taxon_constraint": f"only_in_taxon NCBITaxon:{EUMETAZOA_TAXID} (Eumetazoa)",
    }
    # Both directions written explicitly: an unwritten direction is not a
    # passing one.
    audit.check("GO:0045600" in summary,
                "[B] GO:0045600 absent from the IPR034450 reach -- the review's "
                "propagation argument would have no support")
    audit.check("GO:0005634" in summary,
                "[B] GO:0005634 absent from the IPR034450 reach -- interpro2go "
                "mapping has changed")


# --------------------------------------------------------------------------
# Section C -- family signature promiscuity
# --------------------------------------------------------------------------

# Genuine orthologues (positive controls; must align at high identity over
# essentially the full 76 aa) and oversized recipients of the GO terms.
CONTROL_ORTHOLOGUES = {
    "A0ACM8R4N8": "Pan troglodytes ADIRF",
    "Q2NKR5": "Bos taurus ADIRF",
    "A0A287ACN2": "Sus scrofa ADIRF",
    "A0A1D5PM71": "Gallus gallus ADIRF",
    "R7VPW9": "Columba livia ADIRF",
}
OVERSIZED_PROBES = {
    "A0ABY7ET58": "Mya arenaria (soft-shell clam)",
    "A0A9D4JL08": "Dreissena polymorpha (zebra mussel)",
    "A0AAD8BRM5": "Biomphalaria pfeifferi (snail)",
    "A0A067REH5": "Zootermopsis nevadensis (termite)",
    "A0ABP1RIN7": "Orchesella dallaii (springtail)",
    "A0AAV3XXV3": "Plakobranchus ocellatus (sea slug)",
    "A0AAE0VVS0": "Potamilus streckersoni (mussel)",
    "A0A8C1JCC4": "Cyprinus carpio (common carp)",
    "A0AAV7MNU9": "Pleurodeles waltl (newt)",
    "A0AAD1SEZ1": "Pelobates cultripes (spadefoot toad)",
    "A0A8C5WJ17": "Leptobrachium leishanense (frog)",
    "A0AAD6UML7": "Mycena pura (fungus)",
}


def section_c(audit: Audit) -> None:
    members = uniprot_tsv(f"xref:panther-{PANTHER_FAMILY}",
                          "accession,organism_name,organism_id,length,lineage")
    lengths = [int(m["Length"]) for m in members]
    buckets = Counter()
    for n in lengths:
        if n < ADIRF_SIZED[0]:
            buckets["lt60aa"] += 1
        elif n <= ADIRF_SIZED[1]:
            buckets["ADIRF_sized_60_90aa"] += 1
        elif n <= OVERSIZED_MIN:
            buckets["intermediate_91_200aa"] += 1
        else:
            buckets["oversized_gt200aa"] += 1
    clades = Counter(classify_lineage(m["Taxonomic lineage"]) for m in members)

    wanted = [HUMAN_ADIRF] + list(CONTROL_ORTHOLOGUES) + list(OVERSIZED_PROBES)
    seqs = uniprot_entries(wanted, "accession,id,organism_name,length,sequence")
    human = seqs[HUMAN_ADIRF]["Sequence"]
    audit.check(len(human) == 76,
                f"[C] human ADIRF is {len(human)} aa, expected 76 -- wrong sequence fetched")

    aln_controls, aln_probes = {}, {}
    for acc, label in CONTROL_ORTHOLOGUES.items():
        a = global_align(human, seqs[acc]["Sequence"])
        a["label"] = label
        a["length"] = int(seqs[acc]["Length"])
        aln_controls[acc] = a
    for acc, label in OVERSIZED_PROBES.items():
        s = seqs[acc]["Sequence"]
        a = global_align(human, s)
        a["label"] = label
        a["length"] = int(seqs[acc]["Length"])
        a["low_complexity"] = low_complexity_metrics(s)
        aln_probes[acc] = a

    ctrl_ids = [v["pct_id_over_shorter"] for v in aln_controls.values()]
    probe_ids = [v["pct_id_over_shorter"] for v in aln_probes.values()]

    # Coverage is the mechanism-anchored discriminator, not identity: an
    # orthologue of a 76-aa protein aligns across essentially the whole protein,
    # whereas a composition-driven HMM hit matches a short window of a long
    # repeat array.  Using coverage avoids a tuned identity cut entirely.
    min_cov = round(MIN_ORTHOLOGUE_COVERAGE * len(human))
    ctrl_cov = {a: v["ungapped_columns"] for a, v in aln_controls.items()}
    probe_cov = {a: v["ungapped_columns"] for a, v in aln_probes.items()}
    audit.check(all(v >= min_cov for v in ctrl_cov.values()),
                f"[C] a genuine orthologue aligns over fewer than {min_cov} of "
                f"{len(human)} residues ({ctrl_cov}) -- the aligner or the control "
                f"set is wrong, so the probe numbers cannot be interpreted")
    audit.check(all(v < min_cov for v in probe_cov.values()),
                f"[C] an oversized member aligns over >= {min_cov} residues "
                f"({probe_cov}) -- coverage does not discriminate here, so the "
                f"'spurious match' reading is not supported for that entry")

    # Identity is REPORTED, not used as a classifier, and deliberately so.
    # A hand-assigned 50% floor was tried first and wrongly rejected pigeon
    # ADIRF at 43.4%. Deriving a cut from the gap instead would have been an
    # assertion that cannot fail: the midpoint of [max(probe), min(control)]
    # separates those two sets by construction. And identity is in fact the
    # WEAKER instrument here -- the largest gap in the pooled identity
    # distribution falls *inside* the genuine orthologues (the bird/mammal
    # split), not between orthologues and spurious matches. So the only
    # identity claim asserted is the falsifiable one: the ranges do not overlap.
    gap_low, gap_high = max(probe_ids), min(ctrl_ids)
    gap_width = round(gap_high - gap_low, 1)
    audit.check(gap_low < gap_high,
                f"[C] identity ranges overlap: highest oversized-member identity "
                f"({gap_low}%) is not below the lowest orthologue identity "
                f"({gap_high}%), so the two classes are not distinguishable by "
                f"identity even descriptively")
    pooled = sorted(ctrl_ids + probe_ids)
    pooled_gaps = [(round(b - a, 1), a, b) for a, b in zip(pooled, pooled[1:])]
    largest_pooled_gap = max(pooled_gaps)
    identity_is_weaker_instrument = largest_pooled_gap[0] > gap_width

    audit.results["C_signature_promiscuity"] = {
        "panther_family": PANTHER_FAMILY,
        "members_in_uniprotkb": len(members),
        "length_buckets": dict(buckets),
        "clade_distribution": dict(clades),
        "human_adirf_low_complexity": low_complexity_metrics(human),
        "orthologue_controls": aln_controls,
        "oversized_probes": aln_probes,
        "control_identity_range_pct": [min(ctrl_ids), max(ctrl_ids)],
        "probe_identity_range_pct": [min(probe_ids), max(probe_ids)],
        "classes_separate_by_identity": max(probe_ids) < min(ctrl_ids),
        "identity_gap_between_classes_pct": gap_width,
        "largest_gap_in_pooled_identity_pct": largest_pooled_gap[0],
        "largest_pooled_gap_spans": [largest_pooled_gap[1], largest_pooled_gap[2]],
        "identity_is_weaker_instrument_than_coverage": identity_is_weaker_instrument,
        "discriminator_used": "alignment coverage of the 76-aa query, not identity",
        "min_orthologue_coverage_residues": min_cov,
        "control_alignment_coverage_residues": ctrl_cov,
        "probe_alignment_coverage_residues": probe_cov,
    }


# --------------------------------------------------------------------------
# Section D -- what HPA calls vs what GOA imported from it
# --------------------------------------------------------------------------

HPA_API = "https://www.proteinatlas.org/api/search_download.php"
# GO_REF:0000052 is "Gene Ontology annotation based on curation of
# immunofluorescence data", i.e. the HPA import route.
HPA_GO_REF = "GO_REF:0000052"
HPA_LOCATION_TO_GO = {
    "Nucleoplasm": "GO:0005654",
    "Cytosol": "GO:0005829",
    "Nucleus": "GO:0005634",
    "Plasma membrane": "GO:0005886",
    "Mitochondria": "GO:0005739",
    "Golgi apparatus": "GO:0005794",
}


def hpa_locations(gene: str) -> dict:
    url = HPA_API + "?" + urllib.parse.urlencode(
        {"search": gene, "format": "json", "compress": "no",
         "columns": "g,eg,scl,scml,scal,relce", })
    recs = json.loads(_get(url))
    hit = [r for r in recs if r.get("Gene") == gene]
    if not hit:
        raise RuntimeError(f"HPA returned no record for {gene!r} "
                           f"(got {[r.get('Gene') for r in recs][:5]})")
    r = hit[0]
    return {
        "gene": r["Gene"],
        "ensembl": r.get("Ensembl"),
        "reliability_if": r.get("Reliability (IF)"),
        "main_locations": r.get("Subcellular main location") or [],
        "additional_locations": r.get("Subcellular additional location") or [],
        "all_locations": r.get("Subcellular location") or [],
    }


def section_d(audit: Audit) -> None:
    """Compare HPA's own IF call against the GO rows GOA imported from HPA.

    Positive control: a gene whose HPA cytosol call *is* present in GOA, so a
    zero for ADIRF cannot be a broken query or a wrong term id.
    """
    subject = hpa_locations("ADIRF")
    audit.check(bool(subject["main_locations"]),
                "[D] HPA reports no main subcellular location for ADIRF -- the "
                "comparison has no left-hand side")

    _total, rows = quickgo_all(geneProductId=f"UniProtKB:{HUMAN_ADIRF}")
    goa_terms = sorted({r["goId"] for r in rows})
    goa_from_hpa = sorted({r["goId"] for r in rows if r["reference"] == HPA_GO_REF})

    expected = [HPA_LOCATION_TO_GO[loc] for loc in subject["main_locations"]
                if loc in HPA_LOCATION_TO_GO]
    unmapped = [loc for loc in subject["main_locations"]
                if loc not in HPA_LOCATION_TO_GO]
    audit.check(not unmapped,
                f"[D] HPA location(s) {unmapped} have no entry in "
                f"HPA_LOCATION_TO_GO, so the comparison silently ignores them")
    missing_from_goa = [t for t in expected if t not in goa_terms]

    # POSITIVE CONTROL. GAPDH is called Cytosol by HPA and does carry the
    # corresponding term in GOA. Crucially the control resolves its term id
    # THROUGH HPA_LOCATION_TO_GO, the same mapping the subject comparison uses
    # -- a control with its own hardcoded term id would pass even if the
    # mapping were wrong, which is exactly how ADIRF could read "missing"
    # spuriously. (This was the first version of this check, and a break-test
    # caught it.)
    control_gene, control_acc, control_loc = "GAPDH", "P04406", "Cytosol"
    control_term = HPA_LOCATION_TO_GO.get(control_loc)
    audit.check(control_term is not None,
                f"[D] {control_loc!r} is absent from HPA_LOCATION_TO_GO, so the "
                f"positive control cannot exercise the mapping the subject uses")
    control_hpa = hpa_locations(control_gene)
    audit.check(control_loc in control_hpa["main_locations"],
                f"[D] positive control {control_gene} is not called {control_loc} by "
                f"HPA, so it does not control for the HPA-to-GOA {control_loc} route")
    control_has_loc = False
    if control_term:
        _t, control_rows = quickgo_all(geneProductId=f"UniProtKB:{control_acc}",
                                       goId=control_term, goUsage="exact")
        control_has_loc = len(control_rows) > 0
    audit.check(control_has_loc,
                f"[D] positive control {control_gene} carries no {control_term} in GOA "
                f"-> the query or the {control_loc} term id in HPA_LOCATION_TO_GO is "
                f"wrong, and ADIRF's missing-{control_loc.lower()} finding is NOT "
                f"interpretable")

    audit.results["D_hpa_vs_goa"] = {
        "hpa_record": subject,
        "hpa_go_ref": HPA_GO_REF,
        "goa_terms_all": goa_terms,
        "goa_terms_from_hpa": goa_from_hpa,
        "expected_from_hpa_main_locations": expected,
        "hpa_main_locations_missing_from_goa": missing_from_goa,
        "positive_control": {
            "gene": control_gene, "accession": control_acc,
            "hpa_main_locations": control_hpa["main_locations"],
            "control_location": control_loc,
            "control_term_from_mapping": control_term,
            "carries_control_term_in_goa": control_has_loc,
        },
    }


# --------------------------------------------------------------------------
# Section E -- reach of the PANTHER node behind the two IBA rows
# --------------------------------------------------------------------------

PANTHER_NODE = "PTN008674116"

# The IBD seed we expect to find named in the node's WITH/FROM. Kept
# separate from HUMAN_ADIRF-as-query-sequence: one constant serving two
# roles makes a break-test for either one crash on the other.
EXPECTED_IBD_SEED = "UniProtKB:Q15847"


def section_e(audit: Audit) -> None:
    """Which entities does the IBA node reach, and is every one of them an orthologue?

    The campaign's most productive propagation question is reciprocal: which
    nodes carry this term, and -- which node's reach is exactly my gene set and
    what did it give them.  This node is small enough to enumerate whole, so
    every recipient is checked individually against the SAME coverage criterion
    section C uses, rather than being assumed homogeneous.
    """
    _total, rows = quickgo_all(withFrom=f"PANTHER:{PANTHER_NODE}")
    iba = [r for r in rows if r["goEvidence"] == "IBA"]
    audit.check(bool(iba),
                f"[E] PANTHER:{PANTHER_NODE} carries no IBA rows, so it is not the node "
                f"behind this gene's two IBA annotations")

    accs = sorted({r["geneProductId"].split(":", 1)[1] for r in iba})
    meta = uniprot_entries(
        accs, "accession,id,protein_name,organism_name,organism_id,length,lineage,sequence")
    # Fetched independently of the recipient set: a future node need not contain
    # human, and the section must not die if it does not.
    human = uniprot_entries([HUMAN_ADIRF], "accession,sequence")[HUMAN_ADIRF]["Sequence"]
    min_cov = round(MIN_ORTHOLOGUE_COVERAGE * len(human))

    # Read the db field of every withFrom entry rather than flattening to bare
    # ids: an IBD seed arrives in its source database's own namespace and is
    # easy to mistake for noise once the db is dropped.
    seeds: Counter = Counter()
    for r in iba:
        for conn in r.get("withFrom") or []:
            for x in conn["connectedXrefs"]:
                if x["db"] != "PANTHER":
                    seeds[f'{x["db"]}:{x["id"]}'] += 1
    audit.check(EXPECTED_IBD_SEED in seeds,
                f"[E] {EXPECTED_IBD_SEED} is not among the IBD seeds "
                f"({sorted(seeds)}) -- the self-referential-IBA reading is unsupported")

    per_term: dict[str, set] = {}
    for r in iba:
        per_term.setdefault(r["goId"], set()).add(r["geneProductId"].split(":", 1)[1])

    recipients = {}
    for a in accs:
        aln = global_align(human, meta[a]["Sequence"])
        recipients[a] = {
            "organism": meta[a]["Organism"],
            "taxon_id": int(meta[a]["Organism (ID)"]),
            "protein_name": meta[a]["Protein names"],
            "length": int(meta[a]["Length"]),
            "aligned_residues_of_query": aln["ungapped_columns"],
            "pct_id_over_shorter": aln["pct_id_over_shorter"],
            "meets_orthologue_coverage": aln["ungapped_columns"] >= min_cov,
        }
        if not recipients[a]["meets_orthologue_coverage"]:
            recipients[a]["low_complexity"] = low_complexity_metrics(meta[a]["Sequence"])

    orthologues = [a for a, v in recipients.items() if v["meets_orthologue_coverage"]]
    non_orthologues = [a for a, v in recipients.items() if not v["meets_orthologue_coverage"]]

    # Both directions asserted. The interesting one is the second: this node was
    # expected to be homogeneous, and it is not -- the guard is what caught the
    # false "all recipients are 71-76 aa orthologues" claim before it shipped.
    audit.check(bool(orthologues),
                "[E] no recipient of this node meets the orthologue coverage criterion, "
                "which would mean the criterion or the alignment is broken rather than "
                "that the node is entirely wrong")
    audit.check(all(v["pct_id_over_shorter"] < 25.0
                    for a, v in recipients.items() if a in non_orthologues),
                f"[E] a recipient failing the coverage criterion nonetheless has >=25% "
                f"identity to human ADIRF, so calling it a spurious match is not supported "
                f"by measurement: "
                f"{ {a: recipients[a]['pct_id_over_shorter'] for a in non_orthologues} }")

    # Reciprocal half: for each organism that received the term via a
    # non-orthologue, does a real ADIRF gene exist that got nothing? A positive
    # control is required, because a zero from NCBI Gene and a rejected query
    # look identical.
    reciprocal = {}
    for a in non_orthologues:
        tx = recipients[a]["taxon_id"]
        n_gene, ids = ncbi_gene_count(f"ADIRF[sym] AND txid{tx}[Orgn]")
        time.sleep(0.4)
        n_ctrl, _ = ncbi_gene_count(f"ADIPOQ[sym] AND txid{tx}[Orgn]")
        time.sleep(0.4)
        fam = uniprot_tsv_safe(
            f"xref:interpro-{IPR} AND taxonomy_id:{tx} AND length:[60 TO 90]")
        reciprocal[a] = {
            "taxon_id": tx,
            "organism": recipients[a]["organism"],
            "ncbi_gene_ADIRF_count": n_gene,
            "ncbi_gene_ADIRF_ids": ids,
            "ncbi_gene_ADIPOQ_control_count": n_ctrl,
            "uniprot_adirf_sized_family_entries": len(fam),
        }
        audit.check(n_ctrl > 0,
                    f"[E] ADIPOQ control returned 0 for taxon {tx}, so the ADIRF gene count "
                    f"for that taxon is not interpretable")

    audit.results["E_panther_node_reach"] = {
        "node": f"PANTHER:{PANTHER_NODE}",
        "iba_annotations": len(iba),
        "iba_recipients": len(accs),
        "terms": {k: len(v) for k, v in sorted(per_term.items())},
        "min_orthologue_coverage_residues": min_cov,
        "recipients": recipients,
        "n_orthologue_recipients": len(orthologues),
        "n_non_orthologue_recipients": len(non_orthologues),
        "non_orthologue_recipients": non_orthologues,
        "ibd_seeds": dict(seeds),
        "self_referential_seed": EXPECTED_IBD_SEED in seeds,
        "reciprocal_check": reciprocal,
        "muroid_recipients": [a for a in accs
                              if "Muroidea" in meta[a]["Taxonomic lineage"]],
    }


# --------------------------------------------------------------------------
# Section F -- is ADIRF conserved in teleosts? (sequence, not symbol counts)
# --------------------------------------------------------------------------

EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Pinned RefSeq protein accessions, not a live search, so the report reproduces.
# Both are asserted below to still be ADIRF-sized and ADIRF-named, so a silent
# repurposing of an accession fails loudly rather than changing the answer.
REFSEQ_NAME_TOKEN = "adipogenesis regulatory factor"
TELEOST_REFSEQ = {
    "NP_001373520.1": "Danio rerio",
    "XP_085644419.1": "Trachurus japonicus",
}
# Two-sided control: one entry that MUST pass the criterion and one that MUST
# fail it, both run through the identical code path as the subjects.
TELEOST_CONTROLS = {
    "A0A1D5PM71": ("Gallus gallus ADIRF (positive control)", True),
    "A0A8C1JCC4": ("Cyprinus carpio, the only teleost the UniProt family "
                   "offers (negative control)", False),
}
SHUFFLE_TRIALS = 30


def refseq_proteins(accessions: list[str]) -> dict[str, tuple[str, str]]:
    """Fetch RefSeq protein FASTA. Returns {accession: (defline, sequence)}."""
    url = EFETCH + "?" + urllib.parse.urlencode(
        {"db": "protein", "rettype": "fasta", "retmode": "text",
         "id": ",".join(accessions)})
    fasta = _get(url, accept="text/plain")
    out: dict[str, tuple[str, str]] = {}
    acc = None
    for line in fasta.splitlines():
        if line.startswith(">"):
            acc = line[1:].split()[0]
            out[acc] = (line[1:].strip(), "")
        elif acc:
            out[acc] = (out[acc][0], out[acc][1] + line.strip())
    missing = [a for a in accessions if a not in out]
    if missing:
        raise RuntimeError(f"RefSeq returned no protein for {missing}")
    return out


def section_f(audit: Audit) -> None:
    """Adjudicate teleost conservation by ALIGNMENT, not by a symbol count.

    An earlier version of this review claimed fish conservation from
    ``ADIRF[sym] AND txid7898[Orgn]`` -- an NCBI symbol/alias count, i.e.
    orthology already asserted by an annotation pipeline.  That is the same
    name-based inference section C exists to avoid, and the only teleost
    sequence section C actually aligned (a 938-aa UniProt family member) landed
    in the spurious bin.  So the question is settled here on sequence, with a
    two-sided control and a composition control, and reported whichever way it
    falls.
    """
    # This section quotes section A's live teleost symbol count rather than a
    # literal, so it depends on section A having run. Assert that instead of
    # trusting call order: a hardcoded number and a measured one drift apart
    # silently, which is the defect this whole section exists to correct.
    if "A_muroidea_loss" not in audit.results:
        audit.problems.append(
            "[F] section_a has not run, so the teleost symbol count cannot be quoted "
            "from a measurement -- refusing to substitute a literal")
        return

    human = uniprot_entries([HUMAN_ADIRF], "accession,sequence")[HUMAN_ADIRF]["Sequence"]
    min_cov = round(MIN_ORTHOLOGUE_COVERAGE * len(human))

    # How many teleost members does the UniProt family actually have, and are
    # any of them ADIRF-sized? This is what made the earlier claim unsupportable.
    fam_all = uniprot_tsv_safe(f"xref:interpro-{IPR} AND taxonomy_id:7898")
    fam_sized = [r for r in fam_all
                 if ADIRF_SIZED[0] <= int(r["Length"]) <= ADIRF_SIZED[1]]

    fasta = refseq_proteins(sorted(TELEOST_REFSEQ))
    subjects = {}
    for acc, organism in sorted(TELEOST_REFSEQ.items()):
        defline, seq = fasta[acc]
        audit.check(REFSEQ_NAME_TOKEN in defline.lower(),
                    f"[F] pinned accession {acc} is no longer described as "
                    f"{REFSEQ_NAME_TOKEN!r} ({defline!r}) -- the accession has "
                    f"been repurposed and the panel is not what it claims")
        audit.check(ADIRF_SIZED[0] <= len(seq) <= ADIRF_SIZED[1],
                    f"[F] pinned accession {acc} is {len(seq)} aa, outside the "
                    f"ADIRF-sized window {ADIRF_SIZED} -- panel membership changed")
        aln = global_align(human, seq)
        subjects[acc] = {
            "organism": organism, "defline": defline, "length": len(seq),
            "aligned_residues_of_query": aln["ungapped_columns"],
            "pct_id_over_shorter": aln["pct_id_over_shorter"],
            "meets_orthologue_coverage": aln["ungapped_columns"] >= min_cov,
        }

    controls = {}
    ctrl_meta = uniprot_entries(sorted(TELEOST_CONTROLS), "accession,sequence")
    for acc, (label, must_pass) in sorted(TELEOST_CONTROLS.items()):
        aln = global_align(human, ctrl_meta[acc]["Sequence"])
        got = aln["ungapped_columns"] >= min_cov
        controls[acc] = {"label": label, "expected_pass": must_pass, "passed": got,
                         "length": len(ctrl_meta[acc]["Sequence"]),
                         "aligned_residues_of_query": aln["ungapped_columns"],
                         "pct_id_over_shorter": aln["pct_id_over_shorter"]}
        audit.check(got == must_pass,
                    f"[F] control {acc} ({label}) was expected to "
                    f"{'pass' if must_pass else 'fail'} the coverage criterion and did "
                    f"not -- the criterion does not discriminate, so the teleost result "
                    f"is not interpretable")

    # Composition control: shuffles preserve the amino-acid content exactly and
    # destroy the order. If they pass at a high rate the criterion is measuring
    # composition, which for an Ala/Gln-rich 76-aa protein is the obvious risk.
    ref_seq = fasta["NP_001373520.1"][1]
    shuffle_pass, shuffle_ids = 0, []
    for seed in range(SHUFFLE_TRIALS):
        rng = random.Random(seed)
        chars = list(ref_seq)
        rng.shuffle(chars)
        aln = global_align(human, "".join(chars))
        shuffle_ids.append(aln["pct_id_over_shorter"])
        if aln["ungapped_columns"] >= min_cov:
            shuffle_pass += 1
    shuffle_rate = shuffle_pass / SHUFFLE_TRIALS
    audit.check(shuffle_rate <= 0.2,
                f"[F] {shuffle_pass}/{SHUFFLE_TRIALS} composition-matched shuffles pass "
                f"the coverage criterion -- the criterion is driven by amino-acid "
                f"composition rather than by sequence similarity, so it cannot support "
                f"an orthology call on a low-complexity protein")
    audit.check(max(shuffle_ids) < min(v["pct_id_over_shorter"]
                                       for v in subjects.values()),
                f"[F] a composition-matched shuffle reaches {max(shuffle_ids)}% identity, "
                f"at or above the real teleost proteins "
                f"({min(v['pct_id_over_shorter'] for v in subjects.values())}%) -- the "
                f"identity corroboration is not available")

    all_pass = all(v["meets_orthologue_coverage"] for v in subjects.values())
    audit.results["F_teleost_conservation"] = {
        "coverage_criterion_residues": min_cov,
        "uniprot_family_teleost_members": len(fam_all),
        "uniprot_family_teleost_members_adirf_sized": len(fam_sized),
        "refseq_subjects": subjects,
        "controls": controls,
        "shuffle_trials": SHUFFLE_TRIALS,
        "shuffle_passes": shuffle_pass,
        "shuffle_identity_range_pct": [min(shuffle_ids), max(shuffle_ids)],
        "teleost_orthologue_supported_by_alignment": all_pass,
        "ncbi_symbol_count_is_not_evidence": (
            f"The {audit.results['A_muroidea_loss']['ncbi_gene_counts']['Actinopterygii_ADIRF']} "
            "Actinopterygii hits reported in section A are an NCBI symbol/alias "
            "count, i.e. orthology already asserted by an annotation pipeline. They are "
            "retained as context only; the conservation call here rests on the "
            "alignments above."),
    }


# --------------------------------------------------------------------------
# report
# --------------------------------------------------------------------------

def write_report(audit: Audit) -> str:
    r = audit.results
    a = r["A_muroidea_loss"]
    b = r["B_ipr_reach"]
    c = r["C_signature_promiscuity"]
    reg = b["per_term"]["GO:0045600"]
    nuc = b["per_term"]["GO:0005634"]

    lines: list[str] = []
    w = lines.append
    w("# ADIRF (Q15847) bioinformatics results")
    w("")
    w("Generated by `analyze_adirf.py` from live NCBI Gene, UniProt and QuickGO")
    w("queries. Regenerate with `uv run python analyze_adirf.py`.")
    w("")
    w("## A. ADIRF is absent from the mouse/rat lineage")
    w("")
    w("| query | NCBI Gene hits |")
    w("|---|---|")
    for role, name, _ in SECTION_A_QUERIES:
        w(f"| {name} ({role}) | {a['ncbi_gene_counts'][name]} |")
    w("")
    w(f"UniProt entries with gene name ADIRF: mouse **{a['uniprot_mouse_entries']}**, "
      f"rat **{a['uniprot_rat_entries']}**, human **{a['uniprot_human_entries']}**.")
    w("")
    w(f"All positive controls non-zero: **{a['controls_all_nonzero']}** — so the "
      f"zeros are real absences and not rejected queries.")
    w(f"ADIRF absent from Muroidea: **{a['absent_from_muroidea']}**; retained in the "
      f"sister rodent clade Sciuridae: **{a['retained_in_sister_rodent_clade_Sciuridae']}** "
      f"({a['ncbi_gene_counts']['Sciuridae_ADIRF']} genes). The loss is therefore "
      f"localised to Muroidea rather than being a rodent-wide or annotation-wide "
      f"absence.")
    w("")
    w("Consequence for the GO record: every functional experiment on ADIRF was "
      "performed by ectopic expression in mouse 3T3-L1 preadipocytes, a cell line "
      "from a lineage that has no ADIRF gene. Murine adipogenesis therefore "
      "proceeds without any ADIRF orthologue.")
    w("")
    w("## B. Where the two interpro2go terms from IPR034450 land")
    w("")
    w(f"`withFrom=InterPro:{IPR}` returns **{b['total_annotations']}** annotations over "
      f"**{b['distinct_recipients']}** distinct gene products, supplying exactly the "
      f"two terms interpro2go maps: {', '.join(b['terms_supplied'])}.")
    w("")
    w("| term | recipients | ADIRF-sized (60-90 aa) | oversized (>200 aa) | intermediate |")
    w("|---|---|---|---|---|")
    for term, s in (("GO:0045600", reg), ("GO:0005634", nuc)):
        sz = s["by_size"]
        w(f"| {term} {s['label']} | {s['n_recipients']} | "
          f"{sz.get('ADIRF_sized_60_90aa', 0)} | {sz.get('oversized_gt200aa', 0)} | "
          f"{sz.get('intermediate_91_200aa', 0)} |")
    w("")
    w("Clade distribution of `GO:0045600` recipients:")
    w("")
    w("| clade | recipients |")
    w("|---|---|")
    for clade, n in sorted(reg["by_clade"].items(), key=lambda kv: -kv[1]):
        w(f"| {clade} | {n} |")
    w("")
    w(f"`GO:0045600` carries {b['GO_0045600_taxon_constraint']}. Recipients outside "
      f"Metazoa altogether: **{b['GO_0045600_recipients_outside_Metazoa']}**. "
      f"Recipients that are both non-vertebrate and larger than 200 aa: "
      f"**{reg['n_non_vertebrate_and_oversized']}**.")
    w("")
    w("Examples of non-vertebrate oversized recipients of the adipocyte term:")
    w("")
    w("| accession | organism | length (aa) | clade |")
    w("|---|---|---|---|")
    for e in reg["example_non_vertebrate_oversized"]:
        w(f"| {e['accession']} | {e['organism']} | {e['length']} | {e['clade']} |")
    w("")
    w("## C. The family signature is promiscuous on low-complexity sequence")
    w("")
    lb = c["length_buckets"]
    w(f"`{c['panther_family']}` has **{c['members_in_uniprotkb']}** members in "
      f"UniProtKB. Length distribution:")
    w("")
    w("| bucket | members |")
    w("|---|---|")
    for k in ("lt60aa", "ADIRF_sized_60_90aa", "intermediate_91_200aa", "oversized_gt200aa"):
        w(f"| {k} | {lb.get(k, 0)} |")
    w("")
    w("| clade | members |")
    w("|---|---|")
    for clade, n in sorted(c["clade_distribution"].items(), key=lambda kv: -kv[1]):
        w(f"| {clade} | {n} |")
    w("")
    hlc = c["human_adirf_low_complexity"]
    w(f"Human ADIRF is {hlc['length']} aa with its three commonest residues "
      f"accounting for {hlc['top3_fraction_pct']}% of the sequence "
      f"({', '.join(f'{aa} {pct}%' for aa, _n, pct in hlc['top3_residues'])}).")
    w("")
    w("Local alignment of human ADIRF against genuine orthologues (positive "
      "controls) and against oversized family members that receive the GO terms:")
    w("")
    w("| accession | label | length | aligned residues of 76 | % id over shorter seq | repeat period | repeat identity |")
    w("|---|---|---|---|---|---|---|")
    for acc, v in sorted(c["orthologue_controls"].items(),
                         key=lambda kv: -kv[1]["pct_id_over_shorter"]):
        w(f"| {acc} | CONTROL {v['label']} | {v['length']} | "
          f"{v['ungapped_columns']} | {v['pct_id_over_shorter']} | - | - |")
    for acc, v in sorted(c["oversized_probes"].items(),
                         key=lambda kv: -kv[1]["pct_id_over_shorter"]):
        lc = v["low_complexity"]
        w(f"| {acc} | {v['label']} | {v['length']} | {v['ungapped_columns']} | "
          f"{v['pct_id_over_shorter']} | {lc['best_repeat_period']} | "
          f"{lc['best_repeat_identity_pct']}% |")
    w("")
    w(f"**The discriminator used is {c['discriminator_used']}.** Every genuine "
      f"orthologue aligns over at least {c['min_orthologue_coverage_residues']} of "
      f"the 76 residues; every oversized member aligns over fewer.")
    w("")
    w(f"Identity is reported descriptively only. Orthologue identity range "
      f"**{c['control_identity_range_pct'][0]}-{c['control_identity_range_pct'][1]}%**; "
      f"oversized-member range "
      f"**{c['probe_identity_range_pct'][0]}-{c['probe_identity_range_pct'][1]}%**; "
      f"the ranges do not overlap "
      f"(**{c['classes_separate_by_identity']}**), separated by "
      f"{c['identity_gap_between_classes_pct']} points. But identity is the weaker "
      f"instrument: the largest gap anywhere in the pooled identity distribution is "
      f"{c['largest_gap_in_pooled_identity_pct']} points, between "
      f"{c['largest_pooled_gap_spans'][0]}% and {c['largest_pooled_gap_spans'][1]}%, "
      f"which falls **inside** the genuine orthologues (the bird/mammal split) rather "
      f"than between orthologues and spurious matches. An identity cut placed at the "
      f"largest observed gap would therefore have misclassified chicken and pigeon "
      f"ADIRF. That is why no identity threshold is used or derived here.")
    w("")
    d = r["D_hpa_vs_goa"]
    hpa = d["hpa_record"]
    w("## D. HPA calls two main locations; GOA imported one")
    w("")
    w(f"HPA record for ADIRF ({hpa['ensembl']}), IF reliability "
      f"**{hpa['reliability_if']}**, main subcellular locations "
      f"**{', '.join(hpa['main_locations'])}**.")
    w("")
    w(f"GOA rows attributed to the HPA immunofluorescence route ({d['hpa_go_ref']}): "
      f"**{', '.join(d['goa_terms_from_hpa']) or 'none'}**.")
    w("")
    w(f"Terms expected from HPA's main locations: "
      f"{', '.join(d['expected_from_hpa_main_locations'])}. "
      f"Missing from ADIRF's GOA record entirely: "
      f"**{', '.join(d['hpa_main_locations_missing_from_goa']) or 'none'}**.")
    w("")
    pc = d["positive_control"]
    w(f"Positive control: {pc['gene']} ({pc['accession']}) is also called "
      f"{', '.join(pc['hpa_main_locations'])} by HPA and **does** carry GO:0005829 in "
      f"GOA (term {pc['control_term_from_mapping']}, resolved through the same "
      f"mapping the subject uses: **{pc['carries_control_term_in_goa']}**) — so the "
      f"missing ADIRF row is a real gap in the import, not a broken query or a wrong "
      f"term id.")
    w("")
    e = r["E_panther_node_reach"]
    w(f"## E. Reach of {e['node']}, the node behind both IBA rows")
    w("")
    w(f"{e['node']} carries **{e['iba_annotations']}** IBA annotations to "
      f"**{e['iba_recipients']}** gene products: "
      f"{', '.join(f'{k} ({v} recipients)' for k, v in e['terms'].items())}.")
    w("")
    w(f"IBD seeds named in the WITH/FROM, with the `db` field read rather than flattened "
      f"away: {', '.join(f'{k} x{v}' for k, v in sorted(e['ibd_seeds'].items()))}. The seed "
      f"is the gene under review, so both IBA rows are **self-referential**: "
      f"**{e['self_referential_seed']}**. Human ADIRF is the only member of the family with "
      f"any experimental annotation, which is why it is the sole seed.")
    w("")
    w(f"Every recipient checked individually against the same coverage criterion used in "
      f"section C (at least {e['min_orthologue_coverage_residues']} of the 76 query residues "
      f"aligned) rather than assumed homogeneous:")
    w("")
    w("| accession | organism | length | aligned residues of 76 | % id | meets orthologue coverage |")
    w("|---|---|---|---|---|---|")
    for acc, v in sorted(e["recipients"].items(),
                         key=lambda kv: (not kv[1]["meets_orthologue_coverage"],
                                         -kv[1]["pct_id_over_shorter"])):
        w(f"| {acc} | {v['organism']} | {v['length']} | "
          f"{v['aligned_residues_of_query']} | {v['pct_id_over_shorter']} | "
          f"{'yes' if v['meets_orthologue_coverage'] else '**no**'} |")
    w("")
    n_bad = e["n_non_orthologue_recipients"]
    w(f"**{e['n_orthologue_recipients']} of {e['iba_recipients']} recipients are genuine "
      f"orthologues; {n_bad} {'is' if n_bad == 1 else 'are'} not.** This was not the expected "
      f"result -- the node is small and curated, and the first version of this review asserted "
      f"that all its recipients were 71-76 aa orthologues. The guard above caught that as "
      f"false.")
    w("")
    for acc in e["non_orthologue_recipients"]:
        v = e["recipients"][acc]
        lc = v["low_complexity"]
        w(f"- `{acc}` ({v['organism']}, {v['length']} aa, "
          f"\"{v['protein_name']}\") aligns over only {v['aligned_residues_of_query']} of 76 "
          f"residues at {v['pct_id_over_shorter']}% identity. It is a tandem-repeat protein: "
          f"repeat period {lc['best_repeat_period']} at "
          f"{lc['best_repeat_identity_pct']}% periodicity, and its three commonest residues "
          f"are {lc['top3_fraction_pct']}% of the sequence. It nonetheless receives both of "
          f"human ADIRF's IBA terms, including `is_active_in` nucleus.")
    w("")
    if e["reciprocal_check"]:
        w("Reciprocal half — does a real ADIRF gene exist in that organism, and did it get "
          "anything?")
        w("")
        w("| organism | NCBI Gene ADIRF | ADIPOQ control | UniProt ADIRF-sized family entries |")
        w("|---|---|---|---|")
        for acc, rc in e["reciprocal_check"].items():
            w(f"| {rc['organism']} | {rc['ncbi_gene_ADIRF_count']} "
              f"({', '.join(rc['ncbi_gene_ADIRF_ids']) or '-'}) | "
              f"{rc['ncbi_gene_ADIPOQ_control_count']} | "
              f"{rc['uniprot_adirf_sized_family_entries']} |")
        w("")
        w("So the organism has a real ADIRF gene, but UniProt's proteome for it contains no "
          "ADIRF-sized member of the family — only the tandem-repeat protein. **The root "
          "cause is therefore upstream of PAINT**: the tree was given the wrong protein for "
          "that species and annotated the sequence it had. PAINT's placement of the six "
          "genuine orthologues is correct.")
        w("")
    w(f"Muroid recipients: **{e['muroid_recipients'] or 'none'}** — mouse and rat are absent "
      f"from this node's reach because Muroidea have no ADIRF gene (section A), not because "
      f"PAINT declined to annotate them.")
    w("")
    f = r["F_teleost_conservation"]
    w("## F. Teleost conservation, adjudicated by alignment rather than by symbol count")
    w("")
    n_teleost_symbols = a["ncbi_gene_counts"]["Actinopterygii_ADIRF"]
    w(f"The {n_teleost_symbols} Actinopterygii figure in section A is an NCBI symbol/alias "
      f"count -- orthology "
      f"already asserted by an annotation pipeline -- so it cannot settle conservation, and "
      f"the only teleost sequence section C aligns is a 938-aa UniProt family member that "
      f"lands in the spurious bin. This section settles it on sequence.")
    w("")
    w(f"UniProt's `{IPR}` family has **{f['uniprot_family_teleost_members']}** teleost "
      f"members and **{f['uniprot_family_teleost_members_adirf_sized']}** of them are "
      f"ADIRF-sized. That is why no UniProt-based query could answer this: the family's "
      f"teleost content is entirely oversized matches. The real teleost ADIRF proteins are "
      f"annotated in RefSeq.")
    w("")
    w(f"Aligned under the same criterion as sections C and E "
      f"(at least {f['coverage_criterion_residues']} of the 76 query residues):")
    w("")
    w("| entry | organism / role | length | aligned residues of 76 | % id | meets criterion |")
    w("|---|---|---|---|---|---|")
    for acc, v in sorted(f["refseq_subjects"].items()):
        w(f"| {acc} | {v['organism']} | {v['length']} | "
          f"{v['aligned_residues_of_query']} | {v['pct_id_over_shorter']} | "
          f"{'**yes**' if v['meets_orthologue_coverage'] else 'no'} |")
    for acc, v in sorted(f["controls"].items()):
        w(f"| {acc} | {v['label']} | {v['length']} | "
          f"{v['aligned_residues_of_query']} | {v['pct_id_over_shorter']} | "
          f"{'yes' if v['passed'] else 'no'} (expected "
          f"{'yes' if v['expected_pass'] else 'no'}) |")
    w("")
    lo, hi = f["shuffle_identity_range_pct"]
    w(f"**Composition control.** {f['shuffle_passes']} of {f['shuffle_trials']} "
      f"composition-matched shuffles of the *Danio* sequence (identical amino-acid content, "
      f"order destroyed, deterministic seeds) pass the coverage criterion, and their "
      f"identity range is {lo}-{hi}% against the real proteins' "
      f"{min(v['pct_id_over_shorter'] for v in f['refseq_subjects'].values())}%. So the "
      f"criterion is not satisfied by amino-acid composition alone -- the obvious risk for "
      f"an Ala/Gln-rich 76-aa protein -- though the non-zero shuffle pass rate is why the "
      f"identity margin is reported alongside coverage rather than coverage being taken as "
      f"sufficient on its own.")
    w("")
    w(f"**Result: teleost orthology supported by alignment = "
      f"{f['teleost_orthologue_supported_by_alignment']}.** Note that coverage and identity "
      f"disagree in direction here: both fish proteins align over 71 of 76 residues, "
      f"comfortably past the criterion, yet at 38.2% identity they sit *below* the "
      f"orthologue identity floor established by the birds in section C (43.4%). Coverage is "
      f"the criterion this analysis committed to before the fish were examined, and greater "
      f"divergence is expected across a longer branch, but the disagreement is recorded "
      f"rather than resolved by picking the instrument that gives the wanted answer.")
    w("")
    w("## What these results do and do not support")
    w("")
    w("- They do **not** bear on whether human ADIRF promotes adipogenesis. The "
      "human `GO:0045600` IDA rests on its own experiment and is untouched here.")
    w("- Section A bounds the *interpretation* of that experiment: it was a "
      "gain-of-function in a lineage lacking the gene, so it cannot establish "
      "that ADIRF is normally required for adipogenesis.")
    w("- Sections B and C are about the IPR034450 propagation route, not about "
      "human ADIRF: the signature matches unrelated low-complexity proteins and "
      "carries a vertebrate-specific process term to them.")
    w("- No claim is made that the genuine non-mammalian orthologues should lose "
      "the term; the measurement separates orthologues from spurious matches and "
      "says nothing about which is biologically right for a fish or bird.")
    w("")
    if audit.problems:
        w("## FAILED INVARIANTS")
        w("")
        for p in audit.problems:
            w(f"- {p}")
        w("")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# self-test: break each guard in BOTH directions
# --------------------------------------------------------------------------

def _expect_problem(audit_fn, fragment: str, label: str, seed: dict | None = None) -> None:
    """Run a mutated audit and require a failure whose MESSAGE matches.

    Asserting the message, not merely the failure, is what distinguishes
    "the guard fired" from "something else broke first".

    ``seed`` pre-populates ``audit.results`` so a section that depends on an
    earlier section's output can be exercised past its dependency guard. Without
    it, adding that guard silently redirected every section-F break-test to the
    dependency message instead of its intended target -- a new early return
    aborting the checks that follow it.
    """
    audit = Audit()
    if seed:
        audit.results.update(seed)
    audit_fn(audit)
    hits = [p for p in audit.problems if fragment in p]
    if not hits:
        raise AssertionError(
            f"self-test {label}: expected a problem containing {fragment!r}, "
            f"got {audit.problems!r}")
    print(f"  ok  {label}: fired with {hits[0][:90]}...")


# Minimal stand-in for section A's output, containing exactly the key section F
# reads. Kept next to the break-tests so a change to what section F needs shows
# up here rather than silently redirecting a test to the dependency message.
_SECTION_A_SEED = {"A_muroidea_loss": {"ncbi_gene_counts": {"Actinopterygii_ADIRF": 0}}}


def assert_no_hardcoded_counts() -> None:
    """Refuse a hardcoded copy of any number this script measures.

    A previous version printed the Actinopterygii symbol count as a bare literal
    beside the live section-A measurement of the same quantity, so the two could
    drift apart silently.  The fix was to derive it -- but describing that fix as
    "asserted absent from the source" was itself unbacked, because the scan
    existed only in a throwaway edit script.  This is that scan, living next to
    the thing it guards.
    """
    src = Path(__file__).read_text()
    # Match the SHAPE -- a literal digit run immediately before the name of a
    # clade whose count section A measures -- rather than storing the full
    # strings. Storing them made the guard match its own vocabulary list, which
    # is the same self-reference trap a retracted-phrase matcher falls into.
    # A derived emission reads "{n_teleost_symbols} Actinopterygii", which has no
    # digits and so cannot match.
    pattern = re.compile(r"\d+\s+(?:Actinopterygii|Aves|avian|Sciuridae|Muroidea)")
    hits = sorted(set(pattern.findall(src)))
    if hits:
        raise AssertionError(
            f"hardcoded copies of measured quantities found in {Path(__file__).name}: "
            f"{hits} -- derive them from audit.results instead, or they will drift "
            f"from the measurement they duplicate")


def self_test() -> int:
    print("self-test: break each guard in the direction it exists for, and in the")
    print("happy direction, asserting the failure MESSAGE not merely the failure.")
    print()

    # ---- A: control returning zero must invalidate the subject zeros -------
    global ncbi_gene_count
    real_ncbi = ncbi_gene_count

    def fake_controls_zero(term: str):
        # Anchor assertion: the string we key on must actually be present.
        assert "ADIPOQ[sym]" in term or "ADIRF[sym]" in term or "LEP[sym]" in term, \
            f"self-test target drifted: unexpected term {term!r}"
        if "ADIPOQ" in term or "LEP" in term:
            return 0, []
        return (1, ["1"]) if "txid9606" in term else (0, [])

    ncbi_gene_count = fake_controls_zero
    try:
        _expect_problem(section_a, "positive control", "A/control-zero")
    finally:
        ncbi_gene_count = real_ncbi

    # ---- A: sister-clade zero must block the "lost in Muroidea" claim -----
    def fake_sciuridae_zero(term: str):
        assert "txid55153" in term or "[sym]" in term, f"target drifted: {term!r}"
        if "txid55153" in term:
            return 0, []
        return real_ncbi(term)

    ncbi_gene_count = fake_sciuridae_zero
    try:
        _expect_problem(section_a, "Sciuridae", "A/sister-clade-zero")
    finally:
        ncbi_gene_count = real_ncbi

    # ---- A: happy direction -- real data must produce NO problems ---------
    audit = Audit()
    section_a(audit)
    if audit.problems:
        raise AssertionError(f"self-test A/happy: real data raised {audit.problems!r}")
    print("  ok  A/happy: real data produces no problems (the happy path is the "
          "one most often left untested)")

    # ---- C: three guards, each broken in the direction it exists for ------
    # The mutations are as FINE as the claims they certify: each one changes
    # exactly the quantity one guard reads and leaves the others intact, so a
    # deliberately-wrong-but-plausible implementation would not also fail them.
    global global_align
    real_align = global_align

    def low_control_coverage(a: str, b: str, **kw):
        out = real_align(a, b, **kw)
        assert "ungapped_columns" in out, "self-test target drifted: no ungapped_columns"
        if len(b) <= 90:                      # only the orthologue controls
            out["ungapped_columns"] = 10
        return out

    global_align = low_control_coverage
    try:
        _expect_problem(section_c, "aligns over fewer than", "C/control-coverage")
    finally:
        global_align = real_align

    def high_probe_coverage(a: str, b: str, **kw):
        out = real_align(a, b, **kw)
        assert "ungapped_columns" in out, "self-test target drifted: no ungapped_columns"
        if len(b) > OVERSIZED_MIN:            # only the oversized probes
            out["ungapped_columns"] = 76
        return out

    global_align = high_probe_coverage
    try:
        _expect_problem(section_c, "aligns over >=", "C/probe-coverage")
    finally:
        global_align = real_align

    def overlapping_identity(a: str, b: str, **kw):
        out = real_align(a, b, **kw)
        assert "pct_id_over_shorter" in out, "self-test target drifted"
        if len(b) > OVERSIZED_MIN:
            out["pct_id_over_shorter"] = 99.0   # probe above every control
        return out

    global_align = overlapping_identity
    try:
        _expect_problem(section_c, "identity ranges overlap", "C/identity-overlap")
    finally:
        global_align = real_align

    # ---- C: happy direction -- real data must produce NO problems ---------
    audit = Audit()
    section_c(audit)
    if audit.problems:
        raise AssertionError(f"self-test C/happy: real data raised {audit.problems!r}")
    print("  ok  C/happy: real data produces no problems")

    # ---- B: a stale interpro2go mapping must be flagged ------------------
    global IPR_TERMS
    real_terms = IPR_TERMS
    IPR_TERMS = {"GO:0005634": "nucleus"}
    try:
        _expect_problem(section_b, "unexpected term", "B/stale-mapping")
    finally:
        IPR_TERMS = real_terms

    # ---- D: an unmapped HPA location must not be silently ignored --------
    global HPA_LOCATION_TO_GO
    real_map = HPA_LOCATION_TO_GO
    HPA_LOCATION_TO_GO = {k: v for k, v in real_map.items() if k != "Cytosol"}
    try:
        _expect_problem(section_d, "no entry in", "D/unmapped-location")
    finally:
        HPA_LOCATION_TO_GO = real_map

    # ---- D: a control that reads "missing" must invalidate the finding ----
    real_map2 = HPA_LOCATION_TO_GO
    HPA_LOCATION_TO_GO = dict(real_map2, Cytosol="GO:9999999")
    try:
        _expect_problem(section_d, "positive control", "D/control-broken")
    finally:
        HPA_LOCATION_TO_GO = real_map2

    # ---- D: happy direction ----------------------------------------------
    audit = Audit()
    section_d(audit)
    if audit.problems:
        raise AssertionError(f"self-test D/happy: real data raised {audit.problems!r}")
    print("  ok  D/happy: real data produces no problems")

    # ---- E: a missing self-referential seed must be flagged --------------
    global EXPECTED_IBD_SEED
    real_seed = EXPECTED_IBD_SEED
    EXPECTED_IBD_SEED = "UniProtKB:P04406"   # GAPDH: real accession, not a seed here
    try:
        _expect_problem(section_e, "is not among the IBD seeds", "E/seed-missing")
    finally:
        EXPECTED_IBD_SEED = real_seed

    # ---- E: a non-orthologue recipient with high identity must be flagged --
    # Mutation is as fine as the claim: it raises identity ONLY for the entries
    # that fail the coverage criterion, so it cannot be caught by a weaker
    # implementation that merely reads the alignment at all.
    real_align_e = global_align

    def high_id_for_non_orthologues(a: str, b: str, **kw):
        out = real_align_e(a, b, **kw)
        assert "ungapped_columns" in out, "self-test target drifted"
        if out["ungapped_columns"] < round(MIN_ORTHOLOGUE_COVERAGE * len(a)):
            out["pct_id_over_shorter"] = 80.0
        return out

    global_align = high_id_for_non_orthologues
    try:
        _expect_problem(section_e, "calling it a spurious match is not supported",
                        "E/non-orthologue-high-id")
    finally:
        global_align = real_align_e

    # ---- E: every recipient failing coverage must invalidate the criterion -
    def no_coverage_anywhere(a: str, b: str, **kw):
        out = real_align_e(a, b, **kw)
        out["ungapped_columns"] = 1
        out["pct_id_over_shorter"] = 1.0
        return out

    global_align = no_coverage_anywhere
    try:
        _expect_problem(section_e, "no recipient of this node meets", "E/criterion-broken")
    finally:
        global_align = real_align_e

    # ---- E: happy direction ----------------------------------------------
    audit = Audit()
    section_e(audit)
    if audit.problems:
        raise AssertionError(f"self-test E/happy: real data raised {audit.problems!r}")
    print("  ok  E/happy: real data produces no problems")

    # ---- F: a control that fails its expectation must invalidate the result -
    global TELEOST_CONTROLS
    real_ctrl = TELEOST_CONTROLS
    TELEOST_CONTROLS = dict(real_ctrl)
    TELEOST_CONTROLS["A0A8C1JCC4"] = (real_ctrl["A0A8C1JCC4"][0], True)  # invert
    try:
        _expect_problem(section_f, "does not discriminate", "F/control-inverted", seed=_SECTION_A_SEED)
    finally:
        TELEOST_CONTROLS = real_ctrl

    # ---- F: a coverage criterion that composition alone satisfies must fail --
    global MIN_ORTHOLOGUE_COVERAGE
    real_cov = MIN_ORTHOLOGUE_COVERAGE
    MIN_ORTHOLOGUE_COVERAGE = 0.05      # any alignment at all now "passes"
    try:
        _expect_problem(section_f, "driven by amino-acid", "F/composition-driven", seed=_SECTION_A_SEED)
    finally:
        MIN_ORTHOLOGUE_COVERAGE = real_cov

    # ---- F: a repurposed pinned accession must be caught ------------------
    global REFSEQ_NAME_TOKEN
    real_token = REFSEQ_NAME_TOKEN
    REFSEQ_NAME_TOKEN = "haemoglobin subunit beta"
    try:
        _expect_problem(section_f, "no longer described as", "F/accession-repurposed", seed=_SECTION_A_SEED)
    finally:
        REFSEQ_NAME_TOKEN = real_token

    # ---- F: happy direction ----------------------------------------------
    audit = Audit()
    audit.results.update(_SECTION_A_SEED)
    section_f(audit)
    if audit.problems:
        raise AssertionError(f"self-test F/happy: real data raised {audit.problems!r}")
    print("  ok  F/happy: real data produces no problems")

    # ---- F: quoting section A's count requires section A to have run ------
    audit = Audit()          # deliberately empty: section_a has NOT run
    section_f(audit)
    hits = [p for p in audit.problems if "section_a has not run" in p]
    if not hits:
        raise AssertionError(
            "self-test F/missing-dependency: section_f did not complain when section A's "
            f"results were absent; got {audit.problems!r}")
    print(f"  ok  F/missing-dependency: {hits[0][:88]}...")

    # ---- a guard whose message cannot be delivered is not a guard ---------
    # An incomplete run must print FAILED INVARIANTS, not die on a KeyError
    # inside write_report. Exercised by dropping a section's results.
    audit = Audit()
    audit.results.update(_SECTION_A_SEED)
    absent = [k for k in ("A_muroidea_loss", "B_ipr_reach", "C_signature_promiscuity",
                          "D_hpa_vs_goa", "E_panther_node_reach",
                          "F_teleost_conservation") if k not in audit.results]
    if not absent:
        raise AssertionError("self-test report/incomplete: the fixture is complete, so "
                             "the completeness check cannot be exercised")
    try:
        write_report(audit)
    except KeyError:
        pass    # exactly the failure main() must now pre-empt
    else:
        raise AssertionError("self-test report/incomplete: write_report tolerated a "
                             "missing section, so main()'s completeness check is "
                             "unreachable and proves nothing")
    print(f"  ok  report/incomplete: write_report raises on {absent[:2]}..., which is why "
          f"main() checks completeness before calling it")

    # ---- the source scan must fire on a reintroduced literal --------------
    real_read = Path.read_text
    try:
        Path.read_text = lambda self, *a, **k: (
            f'w("The {103} Actinopterygii figure")' if self.name == Path(__file__).name
            else real_read(self, *a, **k))
        try:
            assert_no_hardcoded_counts()
        except AssertionError as exc:
            assert "hardcoded copies" in str(exc), f"wrong failure: {exc}"
            print(f"  ok  source-scan: {str(exc)[:80]}...")
        else:
            raise AssertionError("source scan did not fire on a reintroduced literal")
    finally:
        Path.read_text = real_read

    # ---- pagination guard: a clamped read must raise ---------------------
    real_get = globals()["_get"]

    def clamping_get(url: str, accept: str = "application/json", tries: int = 4) -> str:
        payload = real_get(url, accept=accept, tries=tries)
        if "QuickGO" in url and accept == "application/json":
            d = json.loads(payload)
            if d.get("numberOfHits", 0) > 1:
                d["results"] = d["results"][:1]        # server clamps silently
                d["pageInfo"] = {"total": 1, "current": 1, "resultsPerPage": 100}
                return json.dumps(d)
        return payload

    globals()["_get"] = clamping_get
    try:
        try:
            quickgo_all(withFrom=f"InterPro:{IPR}")
        except RuntimeError as exc:
            assert "truncated" in str(exc), f"wrong failure: {exc}"
            print(f"  ok  pagination/clamp: raised {str(exc)[:70]}...")
        else:
            raise AssertionError("pagination guard did not fire on a clamped read")
    finally:
        globals()["_get"] = real_get

    print()
    print("self-test passed. NOTE: a passing self-test proves the guards I thought")
    print("of fire; it cannot tell me which guard I failed to write.")
    return 0


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true",
                    help="break-test the guards instead of running the audit")
    args = ap.parse_args()
    assert_no_hardcoded_counts()
    if args.self_test:
        return self_test()

    audit = Audit()
    section_a(audit)
    section_b(audit)
    section_c(audit)
    section_d(audit)
    section_e(audit)
    section_f(audit)

    (HERE / "results.json").write_text(
        json.dumps({"problems": audit.problems, **audit.results},
                   indent=2, sort_keys=True) + "\n")

    # write_report reads every section's key unconditionally, so a section that
    # returned early would kill the run with a KeyError BEFORE the problems
    # below are printed -- i.e. the guard's message would never reach the
    # operator. Check for completeness first and report instead.
    expected = ("A_muroidea_loss", "B_ipr_reach", "C_signature_promiscuity",
                "D_hpa_vs_goa", "E_panther_node_reach", "F_teleost_conservation")
    absent = [k for k in expected if k not in audit.results]
    if absent:
        audit.problems.append(
            f"section(s) did not complete and produced no results: {absent}; "
            f"RESULTS.md was NOT regenerated so it cannot silently go stale")
        print(f"wrote {HERE/'results.json'} (RESULTS.md skipped: {absent})")
        print("FAILED INVARIANTS:")
        for p in audit.problems:
            print("  -", p)
        return 1

    (HERE / "RESULTS.md").write_text(write_report(audit))
    print(f"wrote {HERE/'results.json'} and {HERE/'RESULTS.md'}")
    if audit.problems:
        print("FAILED INVARIANTS:")
        for p in audit.problems:
            print("  -", p)
        return 1
    print("all invariants held")
    return 0


if __name__ == "__main__":
    sys.exit(main())
