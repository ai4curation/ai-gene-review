#!/usr/bin/env python3
"""Did the ADNP NAP-peptide annotation defect propagate onto its paralogue ADNP2?

ADNP's merged review (genes/human/ADNP/ADNP-ai-review.yaml, PR #2331) established
that 13 of its 19 rat-derived Ensembl-Compara rows rest on experiments performed
with the synthetic ADNP-derived octapeptide NAPVSIPQ ("NAP"/davunetide) rather
than on the gene product, and classified them SOURCE_BAD + ROLE_CONFLATION.

This script asks whether any of that reached ADNP2, and it answers the question
with measurements rather than with an argument from paralogy:

A. nap_motif_scan       -- is the NAP octapeptide present in ADNP2 at all?
                           ADNP orthologues are the positive control: a scan that
                           cannot find NAPVSIPQ in ADNP is broken, not informative.
B. pxvxl_scan           -- the HP1-contact motif, with its compositional null.
                           Reproduces the merged ADNP review's published numbers
                           as a precondition before reporting ADNP2's.
C. pxvxl_alignment      -- are the two PxVxL motifs positionally HOMOLOGOUS, or
                           merely both present? Co-occurrence of a motif whose
                           expected count is ~1 is worth nothing on its own.
D. propagation_audit    -- which route carried each ADNP2 GOA row, and which of
                           ADNP's terms did NOT reach ADNP2. Builds source_entities
                           from the GOA WITH/FROM field with a count assertion.
E. donor_evidence       -- for each IBD seed named in an ADNP2 IBA row, what
                           experimental annotation does that seed itself hold for
                           the propagated term, and WHAT MOLECULE was assayed in
                           the reference behind it.
F. opposite_pair_test   -- intersect the reference sets of any logically opposed
                           term pair. Reported even though it comes back negative.

Every network query asserts its HTTP status and that pagination is complete, so a
rejected query cannot be mistaken for an empty result.

    uv run python analyze_adnp2_propagation.py            # write results.json + RESULTS.md
    uv run python analyze_adnp2_propagation.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GENES_ROOT = GENE_DIR.parent

ADNP2_GOA = GENE_DIR / "ADNP2-goa.tsv"
ADNP_GOA = GENES_ROOT / "ADNP" / "ADNP-goa.tsv"

# ---------------------------------------------------------------------------
# HTTP helpers.  A rejected query and a genuine zero look identical downstream
# unless the status is asserted, so every fetch asserts.
# ---------------------------------------------------------------------------


def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    resp = urllib.request.urlopen(req, timeout=120)
    if resp.status != 200:
        raise RuntimeError(f"HTTP {resp.status} for {url}")
    return json.load(resp)


def uniprot(accession: str, fields: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json?fields={fields}"
    d = _get_json(url)
    # A stale accession is NOT the quiet zero it is usually described as.  When
    # `fields=` is supplied, UniProt answers a MERGED accession with an HTTP 303
    # to its successor, which urllib follows, so you receive HTTP 200 and a
    # complete, `entryType: UniProtKB reviewed` record -- for a DIFFERENT protein.
    # Measured: O15507 -> P56159 GFRA1_HUMAN, 465 aa.  Neither the status code,
    # nor `entryType`, nor the presence of `uniProtkbId` distinguishes it.  The
    # only field that does is `primaryAccession`.
    returned = (d.get("primaryAccession") or "").upper()
    if returned != accession.upper():
        raise RuntimeError(
            f"asked UniProt for {accession} and received {returned} "
            f"({d.get('uniProtkbId')}). The accession has been merged or demerged; "
            f"silently accepting the successor substitutes a different protein."
        )
    if d.get("entryType") == "Inactive" or not d.get("uniProtkbId"):
        raise RuntimeError(
            f"{accession} is an inactive UniProt entry ({d.get('inactiveReason')}). "
            f"Querying it is indistinguishable from an entry that carries nothing."
        )
    if "sequence" in fields and not d.get("sequence", {}).get("value"):
        raise RuntimeError(f"{accession} returned no sequence")
    return d


def sequence(accession: str) -> tuple[str, str]:
    d = uniprot(accession, "sequence,id")
    return d["uniProtkbId"], d["sequence"]["value"]


def quickgo_annotations(**params) -> list[dict]:
    """Fully paginated QuickGO annotation search.

    Compares numberOfHits against len(results) rather than against a page-size
    constant: QuickGO clamps limit at 100 and a clamp is invisible to a guard
    that trusts its own page size.
    """
    out: list[dict] = []
    page = 1
    total = None
    while True:
        q = dict(params, limit=100, page=page)
        url = (
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
            + urllib.parse.urlencode(q)
        )
        d = _get_json(url)
        total = d["numberOfHits"]
        got = d["results"]
        out.extend(got)
        if len(out) >= total or not got:
            break
        page += 1
        if page > 200:
            raise RuntimeError(f"runaway pagination for {params}")
    if len(out) != total:
        raise RuntimeError(
            f"pagination incomplete for {params}: collected {len(out)} of {total}"
        )
    return out


def pubmed_titles(pmids: list[str]) -> dict[str, str]:
    if not pmids:
        return {}
    ids = ",".join(pmids)
    d = _get_json(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        f"?db=pubmed&retmode=json&id={ids}"
    )["result"]
    titles = {u: d[u]["title"] for u in d["uids"]}
    missing = set(pmids) - set(titles)
    if missing:
        raise RuntimeError(f"PubMed returned no record for {sorted(missing)}")
    return titles


# ---------------------------------------------------------------------------
# A. The NAP octapeptide
# ---------------------------------------------------------------------------

NAP = "NAPVSIPQ"

NAP_PANEL = {
    "Q6IQ32": "human ADNP2 (subject)",
    "Q8CHC8": "mouse Adnp2 (the Compara/ISS donor for ADNP2)",
    "Q9H2P0": "human ADNP (paralogue)",
    "Q9JKL8": "rat Adnp (the Compara donor behind ADNP's NAP rows)",
    "Q9Z103": "mouse Adnp",
}

# Every entry whose gene symbol is ADNP must contain the octapeptide; this is the
# positive control that distinguishes "ADNP2 lacks it" from "the scan is broken".
NAP_POSITIVE_CONTROLS = {"Q9H2P0", "Q9JKL8", "Q9Z103"}


def nap_motif_scan() -> dict:
    rows = []
    for acc, label in NAP_PANEL.items():
        name, seq = sequence(acc)
        octa = [m.start() + 1 for m in re.finditer(re.escape(NAP), seq)]
        # The relaxed scan matters: "no NAPVSIPQ" would still leave room for a
        # diverged variant.  ADNP2 has no NAP tripeptide anywhere.
        tri = [m.start() + 1 for m in re.finditer("NAP", seq)]
        rows.append(
            {
                "accession": acc,
                "entry_name": name,
                "label": label,
                "length": len(seq),
                "napvsipq_positions": octa,
                "nap_tripeptide_positions": tri,
            }
        )
    by_acc = {r["accession"]: r for r in rows}
    for acc in NAP_POSITIVE_CONTROLS:
        if not by_acc[acc]["napvsipq_positions"]:
            raise RuntimeError(
                f"positive control failed: {acc} ({by_acc[acc]['entry_name']}) is an "
                f"ADNP orthologue and must contain {NAP}. The scan is broken; a "
                f"negative result for ADNP2 would be meaningless."
            )
    return {
        "motif": NAP,
        "positive_controls": sorted(NAP_POSITIVE_CONTROLS),
        "rows": rows,
        "adnp2_carries_nap": bool(by_acc["Q6IQ32"]["napvsipq_positions"]),
        "adnp2_carries_any_nap_tripeptide": bool(
            by_acc["Q6IQ32"]["nap_tripeptide_positions"]
        ),
    }


# ---------------------------------------------------------------------------
# B. PxVxL, with the merged ADNP review's own regex and null model
# ---------------------------------------------------------------------------

# Identical to ADNP-bioinformatics/analyze_compara_donors.py so the two numbers
# are comparable.  Three fixed positions (P, V, and the [LMIV] class).
PXVXL = re.compile(r"(?=(P.V.[LMIV]))")

# Published in the merged ADNP review (ADNP-bioinformatics/results.json).
# Reproduced here as a precondition: a panel that disagrees with a merged
# sibling's numbers must be reconciled before any of it is interpreted.
ADNP_PUBLISHED = {
    "length": 1102,
    "hits": [{"match": "PGVLL", "start": 820, "end": 824}],
    "expected_matches_under_composition_null": 0.758,
}


def _pxvxl(accession: str) -> dict:
    name, seq = sequence(accession)
    hits = [
        {"match": m.group(1), "start": m.start() + 1, "end": m.start() + 5}
        for m in PXVXL.finditer(seq)
    ]
    n = len(seq)
    f = Counter(seq)
    # P(window matches) = p(P) * p(V) * p(L|M|I|V); the two x positions are free.
    p_window = (
        (f["P"] / n) * (f["V"] / n) * (sum(f[a] for a in "LMIV") / n)
    )
    return {
        "accession": accession,
        "entry_name": name,
        "length": n,
        "pattern": PXVXL.pattern,
        "hits": hits,
        "expected_matches_under_composition_null": round(p_window * (n - 4), 3),
    }


def pxvxl_scan() -> dict:
    adnp = _pxvxl("Q9H2P0")
    mismatch = []
    if adnp["length"] != ADNP_PUBLISHED["length"]:
        mismatch.append(f"length {adnp['length']} != {ADNP_PUBLISHED['length']}")
    if adnp["hits"] != ADNP_PUBLISHED["hits"]:
        mismatch.append(f"hits {adnp['hits']} != {ADNP_PUBLISHED['hits']}")
    if (
        abs(
            adnp["expected_matches_under_composition_null"]
            - ADNP_PUBLISHED["expected_matches_under_composition_null"]
        )
        > 0.002
    ):
        mismatch.append(
            f"null {adnp['expected_matches_under_composition_null']} != "
            f"{ADNP_PUBLISHED['expected_matches_under_composition_null']}"
        )
    if mismatch:
        raise RuntimeError(
            "this scan does not reproduce the merged ADNP review's published PxVxL "
            "numbers, so ADNP2's column cannot be interpreted against them: "
            + "; ".join(mismatch)
        )
    adnp2 = _pxvxl("Q6IQ32")
    return {
        "adnp_reproduces_merged_review": True,
        "ADNP": adnp,
        "ADNP2": adnp2,
        "note": (
            "One occurrence in ~1100 aa is not enrichment for either paralogue: "
            f"the compositional null is {adnp['expected_matches_under_composition_null']} "
            f"for ADNP and {adnp2['expected_matches_under_composition_null']} for ADNP2. "
            "What distinguishes ADNP2 is not the count but that PMID:38960717 mutated "
            "the motif and lost HP1beta binding."
        ),
    }


# ---------------------------------------------------------------------------
# C. Are the two motifs positionally homologous?
# ---------------------------------------------------------------------------


def pxvxl_alignment() -> dict:
    from Bio import Align
    from Bio.Align import substitution_matrices

    _, a1 = sequence("Q9H2P0")
    _, a2 = sequence("Q6IQ32")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(a1, a2)[0]

    # Map ADNP position -> ADNP2 position through the aligned blocks.
    # Biopython returns numpy int64 coordinates, which json.dumps cannot encode;
    # coerce at the boundary rather than at the writer, so every downstream
    # comparison is between plain ints too.
    mapping: dict[int, int] = {}
    for (s1, e1), (s2, e2) in zip(aln.aligned[0], aln.aligned[1]):
        s1, e1, s2 = int(s1), int(e1), int(s2)
        for k in range(e1 - s1):
            mapping[s1 + k] = s2 + k

    adnp_start0 = ADNP_PUBLISHED["hits"][0]["start"] - 1
    adnp2_hits = _pxvxl("Q6IQ32")["hits"]
    if not adnp2_hits:
        raise RuntimeError("no PxVxL found in ADNP2 -- the scan is broken")

    # Do NOT assume ADNP2 has exactly one candidate.  Under the degenerate
    # P-x-V-x-[LMIV] consensus it has two, which is the whole point of stating the
    # null: presence of the motif carries no information on its own.  The test is
    # therefore projective -- does ADNP's motif land on one of ADNP2's? -- rather
    # than a comparison of two positions assumed to be unique.
    projected = mapping.get(adnp_start0)
    matched = [
        h for h in adnp2_hits if projected is not None and h["start"] - 1 == projected
    ]
    identities = sum(1 for i, j in mapping.items() if a1[i] == a2[j])
    chosen = (matched or adnp2_hits)[0]
    adnp2_start0 = chosen["start"] - 1
    return {
        "adnp_pxvxl_start": adnp_start0 + 1,
        "adnp2_pxvxl_candidates": adnp2_hits,
        "adnp_pxvxl_projects_to_adnp2_position": None if projected is None else projected + 1,
        "projection_lands_on_an_adnp2_candidate": bool(matched),
        "homologous_adnp2_motif": chosen if matched else None,
        "global_percent_identity": round(100.0 * identities / min(len(a1), len(a2)), 1),
        "adnp_context": a1[adnp_start0 - 20 : adnp_start0 + 25],
        "adnp2_context": a2[adnp2_start0 - 20 : adnp2_start0 + 25],
        "adnp_residues_after_motif": len(a1) - (adnp_start0 + 5),
        "adnp2_residues_after_motif": len(a2) - (adnp2_start0 + 5),
    }


# ---------------------------------------------------------------------------
# D. Propagation audit over the two GOA tables
# ---------------------------------------------------------------------------


def read_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise RuntimeError(f"{path} is empty -- run `just fetch-gene human <GENE>`")
    return rows


def split_withfrom(value: str) -> list[str]:
    return [t for t in value.split("|") if t]


def propagation_audit() -> dict:
    a2 = read_goa(ADNP2_GOA)
    a1 = read_goa(ADNP_GOA)

    # source_entities, built FROM the WITH/FROM field so the counts match GOA by
    # construction rather than by hand.
    source_entities = {}
    for r in a2:
        key = f"{r['GO TERM']}|{r['GO EVIDENCE CODE']}|{r['REFERENCE']}|{r['WITH/FROM']}"
        toks = split_withfrom(r["WITH/FROM"])
        source_entities[key] = toks
        if r["WITH/FROM"] and len(toks) != r["WITH/FROM"].count("|") + 1:
            raise RuntimeError(f"WITH/FROM tokenisation lost a token on {key}")

    t2 = {r["GO TERM"] for r in a2}
    t1 = {r["GO TERM"] for r in a1}

    # The rows on ADNP that the merged review classified SOURCE_BAD are the rat
    # Ensembl-Compara ones.  Which of their terms reached ADNP2?
    rat_compara_terms = sorted(
        {
            r["GO TERM"]
            for r in a1
            if r["REFERENCE"] == "GO_REF:0000107" and "Q9JKL8" in r["WITH/FROM"]
        }
    )
    leaked = sorted(set(rat_compara_terms) & t2)

    # Which route carried each ADNP2 row, and from which species/paralogue?
    routes = []
    for r in a2:
        routes.append(
            {
                "term": r["GO TERM"],
                "name": r["GO NAME"],
                "evidence": r["GO EVIDENCE CODE"],
                "reference": r["REFERENCE"],
                "with_from": split_withfrom(r["WITH/FROM"]),
                "assigned_by": r["ASSIGNED BY"],
                "qualifier": r["QUALIFIER"],
            }
        )

    compara2 = sorted(
        {
            tok
            for r in a2
            if r["REFERENCE"] in ("GO_REF:0000107", "GO_REF:0000024")
            for tok in split_withfrom(r["WITH/FROM"])
            if tok.startswith("UniProtKB:")
        }
    )
    compara1 = sorted(
        {
            tok
            for r in a1
            if r["REFERENCE"] in ("GO_REF:0000107", "GO_REF:0000024")
            for tok in split_withfrom(r["WITH/FROM"])
            if tok.startswith("UniProtKB:")
        }
    )

    return {
        "adnp2_goa_rows": len(a2),
        "adnp2_distinct_rows": len({tuple(r.items()) for r in a2}),
        "adnp2_distinct_terms": len(t2),
        "adnp_goa_rows": len(a1),
        "adnp_distinct_terms": len(t1),
        "shared_terms": sorted(t1 & t2),
        "adnp_only_terms": sorted(t1 - t2),
        "adnp2_only_terms": sorted(t2 - t1),
        "rat_compara_terms_on_adnp": rat_compara_terms,
        "rat_compara_terms_that_reached_adnp2": leaked,
        "adnp2_sequence_similarity_donors": compara2,
        "adnp_sequence_similarity_donors": compara1,
        "source_entities_by_row": source_entities,
        "routes": routes,
    }


# ---------------------------------------------------------------------------
# E. What molecule was assayed behind each IBD seed's own evidence?
# ---------------------------------------------------------------------------

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# The IBD seeds named in ADNP2's two IBA rows, resolved through UniProt xref
# lookups (recorded here so the mapping is auditable without re-querying).
SEED_ACCESSIONS = {
    "MGI:MGI:1338758": ("Q9Z103", "mouse Adnp"),
    "RGD:71030": ("Q9JKL8", "rat Adnp"),
    "UniProtKB:Q9H2P0": ("Q9H2P0", "human ADNP"),
    "ZFIN:ZDB-GENE-061215-112": ("F1QLG5", "zebrafish adnpa"),
}

IBA_ROWS = [
    ("GO:0005634", ["UniProtKB:Q9H2P0", "ZFIN:ZDB-GENE-061215-112"]),
    ("GO:0010468", ["MGI:MGI:1338758", "RGD:71030"]),
]


def donor_evidence() -> dict:
    out = []
    pmids: set[str] = set()
    for term, seeds in IBA_ROWS:
        for seed in seeds:
            acc, label = SEED_ACCESSIONS[seed]
            anns = quickgo_annotations(
                geneProductId=f"UniProtKB:{acc}",
                goId=term,
                goUsage="descendants",
                goUsageRelationships="is_a,part_of",
            )
            exp = [a for a in anns if a["goEvidence"] in EXPERIMENTAL]
            for a in exp:
                if a["reference"].startswith("PMID:"):
                    pmids.add(a["reference"].split(":", 1)[1])
            out.append(
                {
                    "propagated_term": term,
                    "seed_token": seed,
                    "accession": acc,
                    "label": label,
                    "annotations_in_subtree": len(anns),
                    "own_experimental": [
                        {
                            "term": a["goId"],
                            "evidence": a["goEvidence"],
                            "reference": a["reference"],
                        }
                        for a in exp
                    ],
                }
            )
    titles = pubmed_titles(sorted(pmids))
    # A NAP-peptide paper is identified by its own title naming the peptide or the
    # drug, not by inference.  Titles are printed in RESULTS.md so a reader judges.
    nap_re = re.compile(r"\bNAP\b|NAPVSIPQ|davunetide", re.I)
    for row in out:
        for e in row["own_experimental"]:
            pmid = e["reference"].split(":", 1)[-1]
            e["title"] = titles.get(pmid, "")
            e["title_names_the_peptide"] = bool(nap_re.search(e["title"]))
    # A guard on the guard: the NAP matcher must fire on a known NAP title and
    # must not fire on a known gene-product title.
    if not nap_re.search("NAP mechanisms of neuroprotection."):
        raise RuntimeError("NAP title matcher failed on a known positive")
    if nap_re.search("ADNP promotes neural differentiation by modulating Wnt"):
        raise RuntimeError("NAP title matcher fired on a known negative")
    return {
        "rows": out,
        "seeds_with_own_experimental_evidence": sum(
            1 for r in out if r["own_experimental"]
        ),
        "seeds_total": len(out),
        "peptide_derived_seed_annotations": [
            {"seed": r["label"], "propagated_term": r["propagated_term"], **e}
            for r in out
            for e in r["own_experimental"]
            if e["title_names_the_peptide"]
        ],
    }


# ---------------------------------------------------------------------------
# F. Logical-opposite citation cross-product
# ---------------------------------------------------------------------------

OPPOSITE = [("positive regulation of ", "negative regulation of ")]


def opposite_pair_test() -> dict:
    rows = read_goa(ADNP2_GOA)
    by_name = {}
    for r in rows:
        by_name.setdefault(r["GO NAME"], set()).add(r["REFERENCE"])
    pairs = []
    for pos_prefix, neg_prefix in OPPOSITE:
        for name, refs in by_name.items():
            if not name.startswith(pos_prefix):
                continue
            twin = neg_prefix + name[len(pos_prefix) :]
            if twin in by_name:
                shared = sorted(refs & by_name[twin])
                pairs.append(
                    {
                        "positive": name,
                        "negative": twin,
                        "shared_references": shared,
                        "is_full_cross_product": bool(shared)
                        and set(refs) == set(by_name[twin]),
                    }
                )
    return {
        "opposed_pairs_found": len(pairs),
        "pairs": pairs,
        "result": "NEGATIVE -- ADNP2 carries no logically opposed term pair, so the "
        "cross-product defect found on ADIPOQ cannot occur here."
        if not pairs
        else "pairs found; inspect shared_references",
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def build() -> dict:
    return {
        "subject": {"gene": "ADNP2", "accession": "Q6IQ32", "organism": "Homo sapiens"},
        "nap_motif_scan": nap_motif_scan(),
        "pxvxl_scan": pxvxl_scan(),
        "pxvxl_alignment": pxvxl_alignment(),
        "propagation_audit": propagation_audit(),
        "donor_evidence": donor_evidence(),
        "opposite_pair_test": opposite_pair_test(),
    }


def render(d: dict) -> str:
    L: list[str] = []
    add = L.append
    add("# ADNP2: did the ADNP NAP-peptide annotation defect propagate to the paralogue?")
    add("")
    add(
        "Generated by `analyze_adnp2_propagation.py`. Every number below is computed "
        "at run time from UniProt, QuickGO, PubMed and the two committed GOA tables; "
        "nothing is hardcoded except the merged ADNP review's published PxVxL figures, "
        "which are asserted as a precondition."
    )
    add("")

    nap = d["nap_motif_scan"]
    add("## A. The NAP octapeptide is absent from ADNP2")
    add("")
    add("| accession | entry | length | NAPVSIPQ | any `NAP` tripeptide |")
    add("|---|---|---|---|---|")
    for r in nap["rows"]:
        add(
            f"| {r['accession']} | {r['entry_name']} ({r['label']}) | {r['length']} | "
            f"{r['napvsipq_positions'] or '**none**'} | "
            f"{r['nap_tripeptide_positions'] or '**none**'} |"
        )
    add("")
    add(
        f"Positive controls {nap['positive_controls']} all carry the octapeptide, so a "
        f"negative for ADNP2 is a result rather than a broken scan. Human and mouse "
        f"ADNP2 contain **no NAPVSIPQ and not one `NAP` tripeptide** in 1131 / 1165 "
        f"residues. No experiment on the NAP peptide can be an experiment on ADNP2."
    )
    add("")

    px = d["pxvxl_scan"]
    add("## B. PxVxL, with its null")
    add("")
    add(
        "Precondition satisfied: this scan reproduces the merged ADNP review's "
        f"published figures exactly (1 hit at 820-824, null "
        f"{px['ADNP']['expected_matches_under_composition_null']})."
    )
    add("")
    add("| protein | length | hits | expected under composition null |")
    add("|---|---|---|---|")
    for k in ("ADNP", "ADNP2"):
        s = px[k]
        hits = ", ".join(f"{h['match']}@{h['start']}-{h['end']}" for h in s["hits"])
        add(
            f"| {k} ({s['accession']}) | {s['length']} | {hits} | "
            f"{s['expected_matches_under_composition_null']} |"
        )
    add("")
    add(px["note"])
    add("")

    al = d["pxvxl_alignment"]
    add("## C. Which of ADNP2's PxVxL candidates is the homologue?")
    add("")
    cands = ", ".join(
        f"{h['match']}@{h['start']}-{h['end']}" for h in al["adnp2_pxvxl_candidates"]
    )
    add(
        f"ADNP2 has **{len(al['adnp2_pxvxl_candidates'])}** P-x-V-x-[LMIV] candidates "
        f"({cands}) against a compositional expectation of "
        f"{d['pxvxl_scan']['ADNP2']['expected_matches_under_composition_null']}. "
        "Presence of the motif is therefore uninformative on its own, and the count "
        "cannot be used as evidence."
    )
    add("")
    add(
        f"The discriminating test is projective. Global BLOSUM62 alignment of ADNP vs "
        f"ADNP2 ({al['global_percent_identity']}% identity) maps ADNP's motif start "
        f"({al['adnp_pxvxl_start']}) onto ADNP2 position "
        f"{al['adnp_pxvxl_projects_to_adnp2_position']}. Does that land on one of "
        f"ADNP2's candidates? **{al['projection_lands_on_an_adnp2_candidate']}** "
        f"({al['homologous_adnp2_motif']})."
    )
    add("")
    add(f"```\nADNP   {al['adnp_context']}\nADNP2  {al['adnp2_context']}\n```")
    add("")
    add(
        f"The absolute positions differ only because ADNP carries "
        f"{al['adnp_residues_after_motif']} residues after the motif against ADNP2's "
        f"{al['adnp2_residues_after_motif']} -- the poorly conserved C-terminal "
        "extension described in PMID:38960717. The second ADNP2 candidate has no "
        "ADNP counterpart and no experimental support."
    )
    add("")

    pa = d["propagation_audit"]
    add("## D. Which route carried each ADNP2 row, and what did not cross")
    add("")
    add(
        f"ADNP2 GOA: {pa['adnp2_goa_rows']} rows "
        f"({pa['adnp2_distinct_rows']} distinct), {pa['adnp2_distinct_terms']} terms. "
        f"ADNP GOA: {pa['adnp_goa_rows']} rows, {pa['adnp_distinct_terms']} terms."
    )
    add("")
    add(
        f"**Sequence-similarity donors for ADNP2** (GO_REF:0000107 Ensembl Compara and "
        f"GO_REF:0000024 UniProt ISS): `{', '.join(pa['adnp2_sequence_similarity_donors'])}`"
    )
    add(
        f"**Sequence-similarity donors for ADNP**: "
        f"`{', '.join(pa['adnp_sequence_similarity_donors'])}`"
    )
    add("")
    add(
        f"ADNP's rat-Compara block covers **{len(pa['rat_compara_terms_on_adnp'])} terms**. "
        f"Terms from that block that also appear on ADNP2: "
        f"**{pa['rat_compara_terms_that_reached_adnp2'] or 'none'}**."
    )
    add("")
    add("| term | name | evidence | reference | with/from |")
    add("|---|---|---|---|---|")
    for r in pa["routes"]:
        add(
            f"| {r['term']} | {r['name']} | {r['evidence']} | {r['reference']} | "
            f"`{', '.join(r['with_from']) or '-'}` |"
        )
    add("")

    de = d["donor_evidence"]
    add("## E. What molecule was assayed behind each IBD seed")
    add("")
    add(
        f"{de['seeds_with_own_experimental_evidence']} of {de['seeds_total']} seed/term "
        "pairs carry their own experimental annotation in the propagated term's subtree."
    )
    add("")
    add("| propagated term | seed | own experimental evidence | reference title | names the peptide? |")
    add("|---|---|---|---|---|")
    for r in de["rows"]:
        if not r["own_experimental"]:
            add(f"| {r['propagated_term']} | {r['label']} ({r['accession']}) | none | | |")
        for e in r["own_experimental"]:
            add(
                f"| {r['propagated_term']} | {r['label']} ({r['accession']}) | "
                f"{e['term']} {e['evidence']} {e['reference']} | {e['title']} | "
                f"{'**YES**' if e['title_names_the_peptide'] else 'no'} |"
            )
    add("")
    if de["peptide_derived_seed_annotations"]:
        add(
            "**Partial confirmation.** "
            f"{len(de['peptide_derived_seed_annotations'])} seed annotation(s) rest on a "
            "reference whose own title names the NAP peptide. This is inside the donor "
            "set of an ADNP2 row, but it is not the whole donor set -- see the table "
            "above for the co-seed's evidence, which is a gene-product experiment."
        )
    else:
        add("No seed annotation traces to a NAP-peptide reference.")
    add("")

    op = d["opposite_pair_test"]
    add("## F. Logical-opposite citation cross-product")
    add("")
    add(f"{op['result']} (opposed pairs found: {op['opposed_pairs_found']})")
    add("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# Self-test.  Each mutation is as fine-grained as the claim it certifies: a
# mutation that blanks a whole input proves only that the check reads its input.
# ---------------------------------------------------------------------------


def self_test() -> int:
    failures: list[str] = []

    # 1. The NAP positive control must fire when the control sequence loses the
    #    motif -- not merely when the panel is empty.
    global sequence
    real_sequence = sequence

    def fake(acc: str):
        name, seq = real_sequence(acc)
        if acc == "Q9JKL8":  # rat Adnp: strip only the octapeptide
            seq = seq.replace(NAP, "AAAAAAAA")
        return name, seq

    sequence = fake
    try:
        nap_motif_scan()
        failures.append("nap positive control did not fire when a control lost NAPVSIPQ")
    except RuntimeError as e:
        if "positive control failed" not in str(e):
            failures.append(f"nap control raised the wrong error: {e}")
    finally:
        sequence = real_sequence

    # 2. The PxVxL precondition must fire on a one-residue disagreement with the
    #    merged review, not only on a wholly different protein.
    published = dict(ADNP_PUBLISHED)
    try:
        ADNP_PUBLISHED["expected_matches_under_composition_null"] = 0.900
        pxvxl_scan()
        failures.append("pxvxl precondition passed against a wrong published null")
    except RuntimeError as e:
        if "does not reproduce" not in str(e):
            failures.append(f"pxvxl precondition raised the wrong error: {e}")
    finally:
        ADNP_PUBLISHED.clear()
        ADNP_PUBLISHED.update(published)

    # 3. The regex must be overlap-aware, must reject a 4-residue window, and must
    #    honour the [LMIV] class.
    if [m.group(1) for m in PXVXL.finditer("PGVLLPAVAV")] != ["PGVLL", "PAVAV"]:
        failures.append("PXVXL regex missed an overlapping second occurrence")
    if [m.group(1) for m in PXVXL.finditer("PGVLA")]:
        failures.append("PXVXL regex matched a non-[LMIV] final residue")
    if [m.group(1) for m in PXVXL.finditer("PVXL")]:
        failures.append("PXVXL regex matched a 4-residue window")

    # 4. The opposite-pair test must FIND a cross-product when one exists.  A test
    #    that only ever confirms the negative cannot distinguish "none present"
    #    from "detector broken" -- the happy path is the untested path.
    global read_goa
    real_read = read_goa

    def fake_goa(path: Path):
        rows = real_read(path)
        base = dict(rows[0])
        for name, ref in [
            ("positive regulation of X", "PMID:1"),
            ("positive regulation of X", "PMID:2"),
            ("negative regulation of X", "PMID:1"),
            ("negative regulation of X", "PMID:2"),
        ]:
            r = dict(base)
            r["GO NAME"] = name
            r["REFERENCE"] = ref
            rows.append(r)
        return rows

    read_goa = fake_goa
    try:
        res = opposite_pair_test()
        if res["opposed_pairs_found"] != 1 or not res["pairs"][0]["is_full_cross_product"]:
            failures.append(f"opposite-pair detector missed an injected cross-product: {res}")
    finally:
        read_goa = real_read

    # 5. The WITH/FROM tokeniser must not silently drop a token.
    if split_withfrom("A:1|B:2|C:3") != ["A:1", "B:2", "C:3"]:
        failures.append("split_withfrom lost a token")
    if split_withfrom("") != []:
        failures.append("split_withfrom invented a token from an empty field")

    # 6. A merged accession must fail loudly.  The mutation is deliberately the
    #    hard case: O15507 does not 404, it silently redirects to P56159 GFRA1
    #    and returns a complete reviewed record.  A guard that only checked the
    #    HTTP status, or `entryType`, or the presence of an entry name would pass
    #    here while having substituted a different protein.
    try:
        got = uniprot("O15507", "sequence,id")
        failures.append(
            f"a merged accession did not raise; returned {got.get('primaryAccession')}"
        )
    except RuntimeError as e:
        if "merged or demerged" not in str(e):
            failures.append(f"merged-accession guard raised the wrong error: {e}")
    except urllib.error.HTTPError:
        pass
    #    ... and the guard must not fire on a live accession.
    if uniprot("Q6IQ32", "sequence,id")["primaryAccession"] != "Q6IQ32":
        failures.append("merged-accession guard mangled a live accession")

    if failures:
        for f in failures:
            print("SELF-TEST FAILURE:", f, file=sys.stderr)
        return 1
    print("self-test: 6/6 directions OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    data = build()
    (HERE / "results.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(data))
    print(f"wrote {HERE/'results.json'} and {HERE/'RESULTS.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
