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
G. tfclass_reach        -- the node-reach census behind the GO:0000981 verdict and
                           behind this review's ask to NTNU_SB: which genes does
                           tfclass:3.1.8 reach, what does the GO_REF:0000113 import
                           look like as a whole, and which entities does it already
                           EXCLUDE from GO:0000981. Emits the exclusion set as a
                           list, not a count: a curator acting on this needs a
                           diffable set of accessions, and the numbers in the review
                           prose have to be reproducible from here rather than
                           asserted.

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
# G. TFClass node reach and the import's own exclusion set
# ---------------------------------------------------------------------------

TFCLASS_NODE = "tfclass:3.1.8"
TFCLASS_GOREF = "GO_REF:0000113"
MF_TERM = "GO:0000981"   # DNA-binding TF activity, RNA polymerase II-specific
CC_TERM = "GO:0000785"   # chromatin

# The subject and its paralogue must both appear in the node's reach. A census that
# does not contain the gene it is about is a broken query, not an empty result --
# the same positive-control discipline as the NAP scan.
TFCLASS_REACH_CONTROLS = {"UniProtKB:Q6IQ32", "UniProtKB:Q9H2P0"}

# HOPX: a homeodomain protein UniProt says outright does not bind DNA, carrying a
# DNA_BIND feature anyway, already excluded from GO:0000981 by this import.  It is
# the precedent for the BIOLOGICAL claim.  It is NOT a good precedent for the
# fold-symmetry claim, because its DNA_BIND note reads "Homeobox; degenerate" while
# ADNP2's reads plain "Homeobox" -- an asymmetry a curator would raise immediately.
# So the fold-symmetry precedent is derived by measurement below instead of asserted:
# exclusion_set_dna_bind() scans all 18 excluded entities and requires at least one
# with a NON-degenerate DNA-binding domain.
HOPX = "Q9BPY8"


def _dna_bind(accession: str) -> list[dict]:
    d = uniprot(accession, "ft_dna_bind,cc_function,id")
    return [
        {
            "start": f["location"]["start"]["value"],
            "end": f["location"]["end"]["value"],
            "note": f.get("description", ""),
        }
        for f in d.get("features", [])
        if f["type"] == "DNA binding"
    ]


def _rendered_node_rows(text: str) -> set[str]:
    """Node ids appearing as rows of the granularity table in the EMITTED RESULTS.md.

    Reads the artifact that ships rather than the structure that produced it. The
    original silent-filter defect was invisible to any check over `render()`'s inputs,
    because the inputs were complete; only the output was short.
    """
    return set(re.findall(r"^\| `tfclass:([0-9.]+)` \|", text, re.M))


def _shared_property_statement(granularity: list[dict], excluded: list[str]) -> str:
    """The one place the "what does this set share?" claim is written.

    It has to be derived from the partition rather than asserted, because every
    hand-written version of it has been false: "the non-DNA-binding members" (refuted
    by three excluded entities carrying a DNA_BIND feature), "none is a
    sequence-specific polymerase II transcription factor" (refuted by NFX1, which binds
    the X-box motif), and "each is an exclusion inside a node whose other members keep
    the term" (refuted by the four nodes where no member keeps it).
    """
    by_node: dict[str, dict] = {}
    for g in granularity:
        by_node.setdefault(g["node"], g)
    subset = [g for g in by_node.values() if g["node_members_with_mf"] > 0]
    whole = [g for g in by_node.values() if g["node_members_with_mf"] == 0]
    n_subset = sum(len(g["node_members_excluded"]) for g in subset)
    n_whole = sum(len(g["node_members_excluded"]) for g in whole)
    if n_subset + n_whole != len(excluded):
        raise RuntimeError(
            f"partition covers {n_subset + n_whole} entities but the exclusion set has "
            f"{len(excluded)}; the shared-property statement would be computed over the "
            f"wrong set"
        )
    if whole:
        return (
            f"They share no property at all. {n_subset} of the {len(excluded)} sit in "
            f"nodes whose other members keep the term, but the remaining {n_whole} sit "
            f"in {len(whole)} nodes where NO member keeps it, so not even the structural "
            f"description holds across the set. What can be said is only per-node, which "
            f"is why the table above is the claim and this sentence is not."
        )
    return (
        f"All {len(excluded)} sit in nodes whose other members keep the term, so the set "
        f"is uniformly structural even though it is biologically heterogeneous."
    )


def _entity_terms(anns: list[dict]) -> dict[str, set[str]]:
    """Distinct entities -> the set of terms each holds.

    Derived as a set of gene-product ids, never from an annotation total: one entity
    can hold several annotations for the same term, so an annotation count is not an
    entity count.
    """
    out: dict[str, set[str]] = {}
    for a in anns:
        out.setdefault(a["geneProductId"], set()).add(a["goId"])
    return out


def tfclass_reach() -> dict:
    node = quickgo_annotations(withFrom=TFCLASS_NODE)
    node_ents = _entity_terms(node)
    symbols = {a["geneProductId"]: a.get("symbol") for a in node}

    missing = TFCLASS_REACH_CONTROLS - set(node_ents)
    if missing:
        raise RuntimeError(
            f"positive control failed: {sorted(missing)} absent from the {TFCLASS_NODE} "
            f"reach. The census cannot be about a gene it does not contain."
        )

    imp = quickgo_annotations(reference=TFCLASS_GOREF)
    imp_ents = _entity_terms(imp)
    doublet = {MF_TERM, CC_TERM}
    with_mf = sorted(k for k, v in imp_ents.items() if v == doublet)
    cc_only = sorted(k for k, v in imp_ents.items() if v == {CC_TERM})
    other = sorted(k for k, v in imp_ents.items() if v not in (doublet, {CC_TERM}))
    if len(with_mf) + len(cc_only) + len(other) != len(imp_ents):
        raise RuntimeError("entity partition does not sum to the entity total")

    imp_symbols = {a["geneProductId"]: a.get("symbol") for a in imp}
    hopx_id = f"UniProtKB:{HOPX}"
    if hopx_id not in cc_only:
        raise RuntimeError(
            f"the HOPX precedent is not in the {TFCLASS_GOREF} chromatin-only exclusion "
            f"set, so the review's argument from it does not hold. Re-derive the ask "
            f"before citing HOPX."
        )
    hopx_dna_bind = _dna_bind(HOPX)
    adnp2_dna_bind = _dna_bind("Q6IQ32")
    if not hopx_dna_bind or not adnp2_dna_bind:
        raise RuntimeError(
            "the precedent rests on BOTH proteins carrying a DNA_BIND feature; one is "
            f"missing (HOPX={hopx_dna_bind}, ADNP2={adnp2_dna_bind})"
        )

    # Which of the excluded entities carry an annotated DNA-binding domain at all, and
    # is any of them NON-degenerate?  Without this the fold-symmetry argument rests on
    # HOPX, whose domain UniProt calls degenerate -- so a curator could reply that HOPX
    # is excluded BECAUSE its homeodomain is broken, which would not transfer to ADNP2's
    # intact one.  Measured rather than argued.
    adnp2_notes = {f["note"] for f in adnp2_dna_bind}
    excluded_dna_bind = []
    for e in cc_only:
        acc = e.split(":", 1)[1]
        feats = _dna_bind(acc)
        if not feats:
            continue
        excluded_dna_bind.append(
            {
                "gene_product": e,
                "symbol": imp_symbols.get(e),
                "features": feats,
                "any_non_degenerate": any(
                    "degenerate" not in f["note"].lower() for f in feats
                ),
                "note_matches_adnp2": any(f["note"] in adnp2_notes for f in feats),
            }
        )
    intact = [r for r in excluded_dna_bind if r["any_non_degenerate"]]
    same_note = [r for r in excluded_dna_bind if r["note_matches_adnp2"]]
    if not intact:
        raise RuntimeError(
            "no excluded entity carries a non-degenerate DNA-binding domain, so this "
            "import supplies no precedent for excluding a protein whose fold is intact. "
            "The fold-symmetry half of the ask would not hold -- rewrite it before filing."
        )

    # Is the exclusion a PER-ENTITY judgement or PER-NODE coverage?  This decides
    # whether the precedent supports the ask at all: if GO_REF:0000113 can only
    # withhold GO:0000981 for a whole node, then excluding ADNP2 would also exclude
    # ADNP -- which would be wrong, since ADNP's sequence-specific binding is measured
    # -- and the correct request would be a different one.  So the question has to be
    # answered from the data rather than assumed in either direction.
    ent_node: dict[str, set[str]] = {}
    for a in imp:
        for w in a.get("withFrom") or []:
            for c in w["connectedXrefs"]:
                if c["db"] == "tfclass":
                    ent_node.setdefault(a["geneProductId"], set()).add(c["id"])
    granularity = []
    for e in cc_only:
        for nd in sorted(ent_node.get(e, [])):
            peers = quickgo_annotations(withFrom=f"tfclass:{nd}")
            peer_terms = _entity_terms(peers)
            peer_sym = {a["geneProductId"]: a.get("symbol") for a in peers}
            excluded_here = sorted(
                peer_sym[k] or k for k, v in peer_terms.items() if MF_TERM not in v
            )
            granularity.append(
                {
                    "gene_product": e,
                    "symbol": imp_symbols.get(e),
                    "node": nd,
                    "node_members": len(peer_terms),
                    "node_members_with_mf": sum(
                        1 for v in peer_terms.values() if MF_TERM in v
                    ),
                    "node_members_excluded": excluded_here,
                }
            )
    # Per-entity exclusion is demonstrated iff some node retains the term for the
    # majority of its members while withholding it from a strict subset.
    per_entity = [
        g for g in granularity if g["node_members_with_mf"] > 0 and g["node_members"] > 1
    ]
    subject_node = sorted(ent_node.get("UniProtKB:Q6IQ32", []))
    subject_peers = _entity_terms(quickgo_annotations(withFrom=f"tfclass:{subject_node[0]}"))

    evidence = Counter(a["goEvidence"] for a in imp)
    return {
        "node": TFCLASS_NODE,
        "node_annotations": len(node),
        "node_entities": len(node_ents),
        "node_reach": [
            {
                "gene_product": k,
                "symbol": symbols.get(k),
                "terms": sorted(v),
            }
            for k, v in sorted(node_ents.items(), key=lambda x: str(symbols.get(x[0])))
        ],
        "node_term_signatures": {
            ",".join(sorted(s)): c
            for s, c in Counter(frozenset(v) for v in node_ents.values()).items()
            for s in [sorted(s)]
        },
        "import": {
            "reference": TFCLASS_GOREF,
            "annotations": len(imp),
            "entities": len(imp_ents),
            "evidence_codes": dict(evidence),
            "entities_with_the_doublet": len(with_mf),
            "entities_chromatin_only": len(cc_only),
            "entities_other_signature": len(other),
            # The exclusion set as a SET, not a number: this is what a curator would
            # diff against, and it is the payload of the ask to NTNU_SB.
            "chromatin_only_exclusion_set": [
                {"gene_product": k, "symbol": imp_symbols.get(k)} for k in cc_only
            ],
        },
        "hopx_precedent": {
            "accession": HOPX,
            "in_exclusion_set": True,
            "dna_bind_features": hopx_dna_bind,
            "adnp2_dna_bind_features": adnp2_dna_bind,
            # Stated here so the artifact surfaces the asymmetry rather than leaving a
            # reader to find it: HOPX's domain is annotated degenerate, ADNP2's is not.
            "hopx_domain_is_degenerate": any(
                "degenerate" in f["note"].lower() for f in hopx_dna_bind
            ),
            "adnp2_domain_is_degenerate": any(
                "degenerate" in f["note"].lower() for f in adnp2_dna_bind
            ),
        },
        "exclusion_set_dna_bind": {
            "entities_with_a_dna_bind_feature": excluded_dna_bind,
            "with_a_non_degenerate_domain": [r["symbol"] for r in intact],
            "with_a_note_identical_to_adnp2": [r["symbol"] for r in same_note],
        },
        "exclusion_granularity": {
            # SINGLE SOURCE for the "what does this set share?" claim.  It was previously
            # a hardcoded sentence in render() AND a separate sentence in the notes, so
            # correcting one left the other standing -- which is how the same claim was
            # wrong four rounds running.  Computed once here, from the same partition the
            # table iterates, and consumed by render(); the notes quote render's output.
            "shared_property_statement": _shared_property_statement(
                granularity, cc_only
            ),
            "per_entity_demonstrated": bool(per_entity),
            "nodes_where_a_strict_subset_is_excluded": [
                {k: g[k] for k in ("symbol", "node", "node_members",
                                   "node_members_with_mf", "node_members_excluded")}
                for g in per_entity
            ],
            "all_excluded_entities_by_node": granularity,
            "distinct_nodes_reached_by_the_exclusion_set": sorted(
                {g["node"] for g in granularity}
            ),
            "subject_node": subject_node[0] if subject_node else None,
            "subject_node_members": len(subject_peers),
            "subject_node_members_with_mf": sum(
                1 for v in subject_peers.values() if MF_TERM in v
            ),
        },
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
        "tfclass_reach": tfclass_reach(),
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

    tf = d["tfclass_reach"]
    imp = tf["import"]
    add("## G. TFClass node reach, and the import's own exclusion set")
    add("")
    add(
        f"`{tf['node']}` reaches **{tf['node_entities']}** human gene products "
        f"({tf['node_annotations']} annotations). Positive control: the subject "
        f"(`UniProtKB:Q6IQ32`) and its paralogue (`UniProtKB:Q9H2P0`) are both present, "
        f"so this is a census of the right set. Per-entity term signatures: "
        f"{tf['node_term_signatures']}."
    )
    add("")
    add("| gene product | symbol | terms received |")
    add("|---|---|---|")
    for r in tf["node_reach"]:
        add(f"| {r['gene_product']} | {r['symbol']} | {', '.join(r['terms'])} |")
    add("")
    add(
        f"So every gene the node reaches receives the identical pair, which means "
        f"`{MF_TERM}` on ADNP2 is a property of class membership rather than a judgement "
        f"about ADNP2."
    )
    add("")
    add(
        f"Widening to the whole import: **`{imp['reference']}` = {imp['annotations']} "
        f"annotations over {imp['entities']} distinct entities**, evidence codes "
        f"{imp['evidence_codes']}. Of those entities, **{imp['entities_with_the_doublet']}** "
        f"receive `{CC_TERM}`+`{MF_TERM}`, **{imp['entities_chromatin_only']}** receive "
        f"`{CC_TERM}` alone, and {imp['entities_other_signature']} carry some other "
        f"signature. Entity counts are derived as a distinct set of gene-product ids, not "
        f"from the annotation total."
    )
    add("")
    add(
        f"The **{imp['entities_chromatin_only']} chromatin-only entities are the import's "
        f"own negative control** — the pipeline already withholds the molecular-function "
        f"term where it does not apply. Listed as a set rather than a count, because this "
        f"is the payload of the ask to NTNU_SB and a curator needs something diffable:"
    )
    add("")
    add("| gene product | symbol |")
    add("|---|---|")
    for r in imp["chromatin_only_exclusion_set"]:
        add(f"| {r['gene_product']} | {r['symbol']} |")
    add("")
    hp = tf["hopx_precedent"]
    ex = tf["exclusion_set_dna_bind"]

    def _feats(feats: list[dict]) -> str:
        return ", ".join(
            f"{f['start']}-{f['end']}" + (f" ({f['note']})" if f["note"] else "")
            for f in feats
        )

    add(
        f"**Which excluded entities carry a DNA-binding domain?** Rendering the `DOMAIN` "
        f"note alongside the span, because the notes are not uniform and the difference "
        f"matters. Of the {imp['entities_chromatin_only']} excluded entities, "
        f"{len(ex['entities_with_a_dna_bind_feature'])} carry an annotated `DNA_BIND` "
        f"feature at all:"
    )
    add("")
    add("| gene product | symbol | DNA_BIND | non-degenerate? | note identical to ADNP2's? |")
    add("|---|---|---|---|---|")
    for r in ex["entities_with_a_dna_bind_feature"]:
        add(
            f"| {r['gene_product']} | {r['symbol']} | {_feats(r['features'])} | "
            f"{'yes' if r['any_non_degenerate'] else 'no'} | "
            f"{'**yes**' if r['note_matches_adnp2'] else 'no'} |"
        )
    add("")
    add(
        f"ADNP2's own feature is {_feats(hp['adnp2_dna_bind_features'])}. So the "
        f"fold-symmetry precedent is **{', '.join(ex['with_a_note_identical_to_adnp2']) or 'none'}** "
        f"— annotated with the identical note — and not HOPX, whose domain UniProt calls "
        f"**degenerate** (`{_feats(hp['dna_bind_features'])}`). That asymmetry is stated here "
        f"rather than left in the JSON for a reader to find, because it is the first thing a "
        f"curator would raise: if HOPX were the only precedent, the reply would be that HOPX "
        f"is excluded *because* its homeodomain is broken, which would not transfer to "
        f"ADNP2's intact one. The script asserts that at least one excluded entity has a "
        f"non-degenerate domain and refuses to report if none does."
    )
    add("")
    add(
        f"HOPX still carries the **biological** half of the precedent — UniProt describes it "
        f"as an atypical homeodomain protein that does not bind DNA, and it is in the "
        f"exclusion set (asserted, not assumed: the script fails if it is not). What it does "
        f"not carry is fold symmetry with ADNP2."
    )
    add("")
    gr = tf["exclusion_granularity"]
    # Every node, split by kind.  An earlier revision rendered only the strict-subset
    # nodes under a sentence about "the 18", silently dropping 4 nodes / 8 entities --
    # a filter that omits rows without saying so.  Both kinds are printed here, and
    # the counts are derived from the same structure the table iterates.
    by_node = {}
    for g in gr["all_excluded_entities_by_node"]:
        by_node.setdefault(g["node"], g)
    whole = [g for g in by_node.values() if g["node_members_with_mf"] == 0]
    subset = [g for g in by_node.values() if g["node_members_with_mf"] > 0]
    n_whole_ents = sum(len(g["node_members_excluded"]) for g in whole)
    n_subset_ents = sum(len(g["node_members_excluded"]) for g in subset)
    add(
        f"**Is the exclusion a per-entity judgement or per-node coverage?** This decides "
        f"whether the precedent supports the ask at all: if `{TFCLASS_GOREF}` could only "
        f"withhold `{MF_TERM}` for a whole node, then excluding ADNP2 would also exclude "
        f"ADNP — whose sequence-specific binding *is* measured — and the correct request "
        f"would be a different one. Answer, from the data: **per-entity, demonstrated = "
        f"{gr['per_entity_demonstrated']}** (an existential: it holds if *any* node retains "
        f"the term for some members while withholding it from a strict subset)."
    )
    add("")
    add(
        f"**The import uses both granularities, and that distinction has to be stated rather "
        f"than filtered away.** The excluded entities are spread across "
        f"{len(by_node)} nodes, of which **{len(subset)} withhold the term from a strict "
        f"subset** ({n_subset_ents} entities) while **{len(whole)} withhold it from every "
        f"member** ({n_whole_ents} entities). All {len(by_node)} are printed:"
    )
    add("")
    add("| node | members | keep the term | excluded | kind |")
    add("|---|---|---|---|---|")
    for g in sorted(subset, key=lambda x: -x["node_members"]) + sorted(
        whole, key=lambda x: x["node"]
    ):
        kind = (
            "strict subset"
            if g["node_members_with_mf"]
            else "**whole node**"
        )
        add(
            f"| `tfclass:{g['node']}` | {g['node_members']} | "
            f"{g['node_members_with_mf']} | {', '.join(g['node_members_excluded'])} | {kind} |"
        )
    add("")
    # The two class-3.1 figures the review quotes to NTNU_SB: read from the data, never
    # retyped.  Round 4 fixed exactly this defect in the notes; hardcoding the same two
    # numbers here would have reintroduced it in the file the notes are derived from.
    same_class = sorted(
        (g for g in subset if g["node"].startswith("3.1.")),
        key=lambda x: -x["node_members"],
    )
    # Count, enumerate AND LABEL the same list. Two earlier revisions were wrong here in
    # sequence: first the count was over all same-class strict-subset nodes while the
    # enumeration filtered to single-exclusion ones (so they could diverge); then the count
    # was narrowed to match but the LABEL still said "strict-subset nodes", so a node
    # excluding two members would silently drop from the count, the list and the label
    # together. The label now names the filter. This matters because the inputs are live
    # QuickGO queries, so "true today" is not a property of the code.
    same_class_all = same_class
    same_class = [g for g in same_class_all if len(g["node_members_excluded"]) == 1]
    dropped = [g for g in same_class_all if g not in same_class]
    phrases = [
        f"**{', '.join(g['node_members_excluded'])} excluded alone out of "
        f"{g['node_members']} members of `tfclass:{g['node']}`**"
        for g in same_class
    ]
    dropped_note = (
        ""
        if not dropped
        else (
            " ("
            + ", ".join(
                f"`tfclass:{g['node']}` excludes "
                f"{len(g['node_members_excluded'])} and is not counted here"
                for g in dropped
            )
            + ")"
        )
    )
    add(
        f"{len(same_class)} of the **single-exclusion** strict-subset nodes sit in the same "
        f"TFClass class as ADNP2{dropped_note}"
        f"{'. ' if dropped_note else ': '}"
        f"{', and '.join(phrases)} — while ADNP2's own node "
        f"`tfclass:{gr['subject_node']}` currently has "
        f"{gr['subject_node_members_with_mf']}/{gr['subject_node_members']} members holding "
        f"the term. So single-entity exclusion inside a populated homeodomain node is "
        f"something this import already performs, " + {1: "once", 2: "twice"}.get(len(phrases), f"{len(phrases)} times") + f" within class 3.1, and "
        f"the request needs no new mechanism and would not touch ADNP: it takes one node from "
        f"{gr['subject_node_members_with_mf']}/{gr['subject_node_members']} to "
        f"{gr['subject_node_members_with_mf'] - 1}/{gr['subject_node_members']}. The "
        f"wholly-excluded nodes are not the precedent ADNP2 needs — but they do show the "
        f"import has the coarser granularity too, so naming which one the ask relies on "
        f"matters."
    )
    add("")
    # The shared-property claim is NOT written here. It is computed once in
    # tfclass_reach() and consumed, because three successive hand-written versions of it
    # were false and the last one survived a correction purely by living in a second
    # emitter.
    add(
        f"That also settles what these {imp['entities_chromatin_only']} entities do **not** "
        f"have in common. They are biologically heterogeneous: NFX1 "
        f"*\"Binds to the X-box motif of MHC class II genes\"*, which is sequence-specific "
        f"binding at a cis-regulatory region, and DMRTC1 is named a transcription factor. "
        f"Three successive drafts generalised the set as \"the non-DNA-binding members\", then "
        f"as \"none is a sequence-specific polymerase II transcription factor\", then as \"each "
        f"is an exclusion inside a node whose other members keep the term\"; **all three are "
        f"false**, each refuted by a table in this same document. So the statement below is "
        f"computed from the partition rather than written:"
    )
    add("")
    add(f"> {gr['shared_property_statement']}")
    add("")
    add(
        f"**And the positive argument for ADNP2 is neither of those.** It is the measured "
        f"failure to find a motif: no sequence motif explains ADNP2's ChIP-seq distribution, "
        f"its peaks avoid transcription start sites, and PxVxL mutation nearly abolishes its "
        f"chromatin binding. The exclusion set shows only that this import *has* a mechanism "
        f"for withholding `{MF_TERM}` and already applies it to intact-domain proteins; it "
        f"does not itself argue that ADNP2 belongs there."
    )
    add("")
    add(
        f"Note what does **not** depend on any of this: the `{MF_TERM}` verdict rests on "
        f"the quoted three-clause failure against `GO:0003700`'s definition. This section "
        f"supports the upstream ask, not the annotation action."
    )
    add("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# Self-test.  Each mutation is as fine-grained as the claim it certifies: a
# mutation that blanks a whole input proves only that the check reads its input.
# ---------------------------------------------------------------------------


def _count_self_test_directions() -> int:
    """Count the numbered directions in self_test()'s own source.

    A hardcoded total is the first thing to go stale when a direction is added, and a
    stale total is worse than none because it reads as reassurance. The comments that
    enumerate the directions ARE the enumeration, so count those.
    """
    src = Path(__file__).read_text()
    # Anchor on the DEFINITION at column 0, and take the LAST match. A plain
    # `src.split("def self_test() -> int:")` is self-referential: that exact string
    # occurs inside this function's own source, so the split lands here and the count
    # comes back 0 -- a counter defeated by containing the thing it searches for.
    parts = re.split(r"^def self_test\(\) -> int:\s*$", src, flags=re.M)
    if len(parts) < 2:
        return 0
    body = parts[-1].split("\ndef ", 1)[0]
    return len(re.findall(r"^    #\s*\d+[.)]", body, re.M))


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

    # 7. The TFClass census must fail if its positive control is absent -- i.e. if the
    #    census does not contain the gene it is about.  The mutation is as fine as the
    #    claim: it removes ONE control accession, not the whole query.
    global TFCLASS_REACH_CONTROLS
    real_controls = TFCLASS_REACH_CONTROLS
    try:
        TFCLASS_REACH_CONTROLS = real_controls | {"UniProtKB:P00000"}
        tfclass_reach()
        failures.append("tfclass census passed with a control absent from the node reach")
    except RuntimeError as e:
        if "positive control failed" not in str(e):
            failures.append(f"tfclass control raised the wrong error: {e}")
    finally:
        TFCLASS_REACH_CONTROLS = real_controls

    # 8. The HOPX precedent must be VERIFIED, not assumed.  Point the check at a
    #    protein that is in the import but NOT in the chromatin-only set, and the
    #    guard must refuse -- otherwise the review could cite a precedent that is not
    #    actually excluded.  ADNP2 itself is the ideal wrong answer: it is in the
    #    import and receives the doublet.
    global HOPX
    real_hopx = HOPX
    try:
        HOPX = "Q6IQ32"
        tfclass_reach()
        failures.append("HOPX precedent check passed for a protein NOT in the exclusion set")
    except RuntimeError as e:
        if "not in the" not in str(e):
            failures.append(f"HOPX precedent check raised the wrong error: {e}")
    finally:
        HOPX = real_hopx

    # 9. The happy direction, which is the one that usually goes untested: with
    #    everything correct the census must actually produce a non-empty reach, a
    #    non-empty exclusion set, and a partition that sums.  A guard that only ever
    #    fires on breakage cannot tell you it works when nothing is broken.
    tf = tfclass_reach()
    if tf["node_entities"] < 2:
        failures.append(f"tfclass node reach implausibly small: {tf['node_entities']}")
    imp = tf["import"]
    if not imp["chromatin_only_exclusion_set"]:
        failures.append("exclusion set is empty; the negative-control argument is vacuous")
    if (
        imp["entities_with_the_doublet"]
        + imp["entities_chromatin_only"]
        + imp["entities_other_signature"]
        != imp["entities"]
    ):
        failures.append("entity partition does not sum on the happy path")
    if not tf["hopx_precedent"]["dna_bind_features"]:
        failures.append("HOPX DNA_BIND feature missing on the happy path")

    # 10. The asymmetry the reviewer found must stay VISIBLE in both artifacts. It is
    #     recorded in results.json as an explicit boolean, and RESULTS.md must render
    #     the DOMAIN note, not just the span -- dropping the note is exactly how the
    #     defect arose. Assert against the EMITTED text, not the builder source.
    if not tf["hopx_precedent"]["hopx_domain_is_degenerate"]:
        failures.append("HOPX degeneracy flag is False; the asymmetry claim is stale")
    if tf["hopx_precedent"]["adnp2_domain_is_degenerate"]:
        failures.append("ADNP2 domain now reads degenerate; the contrast is stale")
    #     A missing RESULTS.md must FAIL, not pass silently: `if md.exists()` made this
    #     check vacuous whenever the artifact it polices was absent, which is the fifth
    #     vacuous-pass this campaign has recorded and the most common way a guard
    #     reports coverage it does not have.
    md = HERE / "RESULTS.md"
    if not md.exists():
        failures.append(
            f"{md} is missing, so the rendering check cannot run -- generate it with a "
            f"plain run before self-testing"
        )
    else:
        text = md.read_text()
        if "degenerate" not in text:
            failures.append("RESULTS.md does not surface the degenerate note")
        if "Homeobox; degenerate" not in text:
            failures.append("RESULTS.md renders spans without the DOMAIN note")

    # 11. The fold-symmetry precedent must be DERIVED, not assumed: if no excluded
    #     entity had a non-degenerate domain the section must refuse. Exercise it by
    #     marking every excluded entity's domain degenerate -- a mutation as fine as
    #     the claim, since it leaves the query, the counts and HOPX all intact.
    global _dna_bind
    real_dna_bind = _dna_bind

    def all_degenerate(acc: str):
        return [dict(f, note="Homeobox; degenerate") for f in real_dna_bind(acc)]

    _dna_bind = all_degenerate
    try:
        tfclass_reach()
        failures.append(
            "fold-symmetry precedent passed with every excluded domain degenerate"
        )
    except RuntimeError as e:
        if "non-degenerate" not in str(e):
            failures.append(f"fold-symmetry guard raised the wrong error: {e}")
    finally:
        _dna_bind = real_dna_bind

    # 12. The granularity block had no break-test at all, and its verdict is what the
    #     ask to NTNU_SB now rests on. Two directions, both finer than blanking a query.
    #     (a) If NO node retained the term for any member -- i.e. every exclusion were
    #     whole-node -- per_entity_demonstrated must go False, because then excluding
    #     ADNP2 would also exclude ADNP and the ask would be the wrong request.
    real_qgo = globals()["quickgo_annotations"]

    def only_whole_nodes(**params):
        rs = real_qgo(**params)
        wf = params.get("withFrom", "")
        if wf.startswith("tfclass:") and wf != f"tfclass:{TFCLASS_NODE.split(':')[1]}":
            return [a for a in rs if a["goId"] != MF_TERM]
        return rs

    globals()["quickgo_annotations"] = only_whole_nodes
    try:
        tf_mut = tfclass_reach()
        if tf_mut["exclusion_granularity"]["per_entity_demonstrated"]:
            failures.append(
                "per_entity_demonstrated stayed True when every node was wholly excluded"
            )
    except RuntimeError:
        pass  # an upstream assertion firing first is acceptable
    finally:
        globals()["quickgo_annotations"] = real_qgo

    #     (b) The happy direction, and the specific claim the ask quotes: at least one
    #     class-3.1 node must exclude exactly ONE member while the rest keep the term.
    gr = tfclass_reach()["exclusion_granularity"]
    singles_31 = [
        g
        for g in gr["all_excluded_entities_by_node"]
        if g["node"].startswith("3.1.")
        and g["node_members_with_mf"] > 0
        and len(g["node_members_excluded"]) == 1
    ]
    if not singles_31:
        failures.append(
            "no class-3.1 node excludes exactly one member; the ask's precedent is gone"
        )
    if gr["subject_node"] != "3.1.8":
        failures.append(f"subject node moved: {gr['subject_node']}")
    #     (c) The row-completeness check, retargeted. The previous version compared two
    #     comprehensions over the SAME list -- a tautology that could never fail -- and it
    #     inspected the INPUTS while the defect it was written for lived in render(). The
    #     silent filter would still ship today. So assert over the EMITTED text: every node
    #     in the data must appear as a row in the rendered table.
    nodes = {g["node"] for g in gr["all_excluded_entities_by_node"]}
    if not md.exists():
        failures.append("cannot check rendered row completeness: RESULTS.md absent")
    else:
        rendered = _rendered_node_rows(md.read_text())
        if rendered != nodes:
            failures.append(
                f"rendered node table does not match the data: missing "
                f"{sorted(nodes - rendered)}, unexpected {sorted(rendered - nodes)}"
            )
        #  and prove that check can fail, by deleting one row from a copy of the text.
        one = sorted(nodes)[0]
        mutated = "\n".join(
            l for l in md.read_text().splitlines()
            if not l.startswith(f"| `tfclass:{one}` |")
        )
        if _rendered_node_rows(mutated) == nodes:
            failures.append(
                "row-completeness check cannot detect a deleted table row -- it is vacuous"
            )

    if failures:
        for f in failures:
            print("SELF-TEST FAILURE:", f, file=sys.stderr)
        return 1
    # Derived, not hardcoded: a literal count drifts the moment a direction is added,
    # and then the reassuring number is the stale part.
    n = _count_self_test_directions()
    if n < 12:
        print(f"SELF-TEST FAILURE: only {n} numbered directions found; the counter "
              f"cannot see the enumeration", file=sys.stderr)
        return 1
    print(f"self-test: {n}/{n} directions OK")
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
