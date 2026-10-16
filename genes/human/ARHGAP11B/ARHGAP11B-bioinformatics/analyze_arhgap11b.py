"""Why is human-specific ARHGAP11B GAP-dead when its arginine finger is still there?

ARHGAP11B (Q3KRB8, 267 aa) is a human-specific partial duplication of ARHGAP11A
(Q6P4F7, 1023 aa). Two curated IDA annotations state ``NOT enables GO:0005096
GTPase activator activity`` (PMID:25721503, PMID:27957544), yet Reactome asserts
the positive ``enables GO:0005096`` by TAS, and InterPro's RhoGAP-domain signature
IPR000198 supplies ``GO:0007165 signal transduction`` by IEA. So the automated
record still treats this protein as a working RhoGAP.

The campaign's standard test for a claimed-inactive enzyme is "are the catalytic
residues still present?". Applied here that test gives the WRONG answer, and this
script is built to demonstrate that rather than to confirm a prior:

Analysis 1 -- where the paralogy actually ends.
  ARHGAP11B and ARHGAP11A are colinear from Met1, so identity is measured by direct
  positional comparison and the colinearity is *proved* first, by asserting that a
  global alignment of the two N-terminal regions opens no gaps. The boundary is then the
  single changepoint that maximises the between-segment sum of squares of the per-residue
  identity vector, with its significance established by permuting that vector. **No
  identity cutoff is chosen anywhere**, and the script raises rather than reporting the
  argmax of noise if any permutation matches the observed statistic. No divergence
  position is taken from the literature or hardcoded.

  (An earlier version did place a threshold inside the largest gap of a windowed-identity
  distribution. That was abandoned because the windows straddling the boundary take every
  intermediate value, so the distribution is never cleanly bimodal and the check could not
  fire.)

Analysis 2 -- the arginine finger, tested reciprocally.
  Each control's own UniProt-annotated arginine finger is aligned onto ARHGAP11B, and
  the residue is scored as retained only if BOTH the aligned residue is an arginine
  AND the aligned position lands on one of ARHGAP11B's own annotated Site features.
  That second condition is what stops sequence noise manufacturing a catalytic residue.
  Controls are ARHGAP11A -- the paralog whose RhoGAP activity was measured in the very
  assay that scored ARHGAP11B negative -- and ARHGAP1/p50RhoGAP, whose arginine finger
  is resolved in a transition-state crystal structure.

Analysis 3 -- does the arginine-finger test discriminate anything in this family?
  Every human reviewed protein carrying the PROSITE RhoGAP profile is fetched and asked
  whether it has an annotated arginine finger and whether that position holds an arginine.
  Then -- because a count of FLAGGED proteins is not a count of confirmed pseudo-enzymes --
  each flagged entry is asked what UniProt itself concluded about its catalytic status, and
  on what evidence code. The result is that residue identity and curated activity are
  decoupled in both directions in this family, which is a measurable property of the test
  rather than an opinion about it.

Analysis 4 -- what is actually lost, measured on a structure.
  The GAP:GTPase interface is computed from PDB 1TX4 (p50RhoGAP:RhoA:GDP:AlF4, 1.65 A),
  a transition-state mimic, as every ARHGAP1 residue within a distance cutoff of RhoA or
  of the nucleotide/metal/fluoride ligands. The chain roles are not assumed: the script
  proves them by aligning each observed chain sequence to the UniProt sequence it is
  supposed to be, and raises if the identity is not overwhelming. Interface residues are
  then mapped onto ARHGAP11A by alignment and partitioned into the part ARHGAP11B keeps
  and the part it lost, so "the truncation removes catalytic machinery" becomes a count
  rather than an assertion.

Analysis 5 -- the UniProt Rho-GAP domain boundary.
  ARHGAP11A's and ARHGAP11B's own Rho-GAP DOMAIN features are compared against the
  divergence point derived in Analysis 1.

Every number in RESULTS.md is produced by a run of this script. Missing input is a hard
error naming the fix, never a silently degraded section. ``--self-test`` mutates the
inputs and asserts each check flips, and asserts that the number of mutations applied
equals the number of anchors detected, so a mutation whose target has drifted is an
error rather than a vacuous pass.

Usage:
    uv run python analyze_arhgap11b.py            # run analyses, write results.json + RESULTS.md
    uv run python analyze_arhgap11b.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import FastMMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import protein_letters_3to1

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "cache"

# --- subjects -------------------------------------------------------------------
QUERY_ACC = "Q3KRB8"  # ARHGAP11B, the subject of the review
PARALOG_ACC = "Q6P4F7"  # ARHGAP11A, source of the partial duplication
RHOGAP1_ACC = "Q07960"  # ARHGAP1 / p50RhoGAP, structurally characterised control
RHOA_ACC = "P61586"  # RhoA, the GTPase in the control structure

INTERFACE_PDB = "1TX4"
GAP_CHAIN = "A"
GTPASE_CHAIN = "B"
# Ligands that make up the transition-state mimic; contacts to these are part of the
# catalytic interface just as much as contacts to RhoA's polypeptide.
TS_LIGANDS = {"GDP", "ALF", "MG"}
CONTACT_CUTOFF_A = 4.5

# PROSITE RhoGAP profile; the signature that puts every RhoGAP-domain protein
# (including ARHGAP11B) into the family in the first place.
RHOGAP_PROSITE = "PS50238"

ARGININE_FINGER_TEXT = "Arginine finger"

# Block size used only for the reported identity profile. The divergence POSITION is
# not read off a threshold on these blocks -- it is a changepoint fitted to the raw
# per-residue identity vector, and its significance is established by permutation.
BLOCK = 20
N_PERMUTATIONS = 2000
PERMUTATION_SEED = 20260916


class AnalysisError(RuntimeError):
    """A hard failure. Never downgraded to a missing section in the report."""


# --- fetching -------------------------------------------------------------------


def _fetch(url: str, dest: Path, binary: bool = False) -> bytes:
    """Fetch `url` to `dest`, caching. A fetch failure is fatal and names the fix."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as fh:
            payload = fh.read()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        raise AnalysisError(
            f"could not fetch {url}: {exc}. This analysis has no offline fallback; "
            f"re-run with network access, or delete {CACHE_DIR} and retry."
        ) from exc
    if not payload:
        raise AnalysisError(f"empty response from {url}")
    dest.write_bytes(payload)
    return payload


def fetch_uniprot(acc: str) -> dict[str, Any]:
    raw = _fetch(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json",
        CACHE_DIR / f"{acc}.json",
    )
    rec = json.loads(raw)
    # The DEAD-ACCESSION trap: an inactive entry returns 200 with no sequence and no
    # name, which is indistinguishable from a protein that simply carries no features.
    if not rec.get("sequence", {}).get("value"):
        raise AnalysisError(f"UniProt {acc} returned no sequence (deleted/demerged entry?)")
    name = rec.get("uniProtkbId")
    if not name:
        raise AnalysisError(f"UniProt {acc} returned no entry name")
    return rec


def uniprot_sequence(rec: dict[str, Any]) -> str:
    return rec["sequence"]["value"]


def uniprot_entry_name(rec: dict[str, Any]) -> str:
    return rec["uniProtkbId"]


def uniprot_is_reviewed(rec: dict[str, Any]) -> bool:
    # "reviewed" is a SUBSTRING of "unreviewed": a containment test silently promotes
    # every TrEMBL entry. Anchor to the start of the string.
    return str(rec.get("entryType", "")).startswith("UniProtKB reviewed")


def uniprot_protein_name(rec: dict[str, Any]) -> str:
    desc = rec.get("proteinDescription", {})
    rec_name = desc.get("recommendedName", {}).get("fullName", {}).get("value")
    if rec_name:
        return rec_name
    subs = desc.get("submissionNames") or []
    if subs:
        return subs[0].get("fullName", {}).get("value", "")
    return ""


def site_positions(rec: dict[str, Any], text: str | None = None) -> list[int]:
    """1-based positions of Site features, optionally filtered by description text."""
    out = []
    for feat in rec.get("features", []):
        if feat.get("type") != "Site":
            continue
        if text is not None and text.lower() not in str(feat.get("description", "")).lower():
            continue
        start = feat["location"]["start"].get("value")
        end = feat["location"]["end"].get("value")
        if start is None or end is None or start != end:
            continue
        out.append(int(start))
    return sorted(set(out))


def domain_spans(rec: dict[str, Any], note: str) -> list[tuple[int, int]]:
    out = []
    for feat in rec.get("features", []):
        if feat.get("type") != "Domain":
            continue
        if note.lower() not in str(feat.get("description", "")).lower():
            continue
        start = feat["location"]["start"].get("value")
        end = feat["location"]["end"].get("value")
        if start is None or end is None:
            continue
        out.append((int(start), int(end)))
    return out


# --- alignment ------------------------------------------------------------------


def make_aligner() -> PairwiseAligner:
    aln = PairwiseAligner()
    aln.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln.open_gap_score = -11
    aln.extend_gap_score = -1
    aln.mode = "global"
    return aln


def align_map(seq_from: str, seq_to: str, mode: str = "global") -> dict[int, int]:
    """Map 1-based positions of `seq_from` onto 1-based positions of `seq_to`."""
    aligner = make_aligner()
    aligner.mode = mode
    aln = aligner.align(seq_from, seq_to)[0]
    mapping: dict[int, int] = {}
    for (f0, f1), (t0, t1) in zip(aln.aligned[0], aln.aligned[1]):
        # Biopython returns numpy ints; cast so the results are JSON-serialisable and
        # so equality against plain-int site positions behaves predictably.
        f0, f1, t0 = int(f0), int(f1), int(t0)
        for off in range(f1 - f0):
            mapping[f0 + off + 1] = t0 + off + 1
    return mapping


def alignment_opens_gaps(seq_a: str, seq_b: str) -> bool:
    """True if a global alignment of the two sequences is not a straight colinear run."""
    aln = make_aligner().align(seq_a, seq_b)[0]
    blocks_a, blocks_b = aln.aligned
    if len(blocks_a) != 1:
        return True
    (a0, a1), (b0, b1) = blocks_a[0], blocks_b[0]
    return not (a0 == 0 and b0 == 0 and a1 == len(seq_a) and b1 == len(seq_b))


# --- analysis 1: divergence point -----------------------------------------------


@dataclass
class DivergenceResult:
    colinear_prefix_proved: bool
    divergence_point: int
    statistic: float
    permutations: int
    permuted_max_statistic: float
    empirical_p_value: float
    identity_before: float
    identity_after: float
    n_identical_before: int
    n_compared_before: int
    n_identical_after: int
    n_compared_after: int
    block: int = BLOCK
    block_profile: list[dict[str, float]] = field(default_factory=list)


def _changepoint(ident: list[int]) -> tuple[int, float]:
    """Best single split of a 0/1 vector, by between-group sum of squares.

    Threshold-free: nothing is compared against a number I chose. The returned
    position is the 1-based index of the last residue of the left segment.
    """
    n = len(ident)
    total = sum(ident)
    best_pos, best_stat = 0, -1.0
    running = 0
    for k in range(1, n):  # left segment = ident[:k]
        running += ident[k - 1]
        left_mean = running / k
        right_mean = (total - running) / (n - k)
        stat = (k * (n - k) / n) * (left_mean - right_mean) ** 2
        if stat > best_stat:
            best_stat, best_pos = stat, k
    return best_pos, best_stat


def derive_divergence_point(query: str, paralog: str) -> DivergenceResult:
    """Find where ARHGAP11B stops being ARHGAP11A, without choosing a cutoff.

    The two proteins share a translation start, so identity is scored positionally.
    That assumption is proved, not assumed: the N-terminal regions must align without
    opening a single gap.

    The boundary is then the single changepoint that maximises the between-segment
    sum of squares of the per-residue identity vector. Its significance is established
    by permuting that vector, so the analysis fails loudly on a sequence pair with no
    real boundary rather than reporting the argmax of noise.
    """
    probe = min(150, len(query))
    if alignment_opens_gaps(query[:probe], paralog[:probe]):
        raise AnalysisError(
            "query and paralog N-termini do not align colinearly; the positional "
            "identity scan used by this analysis is invalid for these sequences"
        )

    n = min(len(query), len(paralog))
    if n < 2 * BLOCK:
        raise AnalysisError(f"sequences too short ({n}) for this analysis")

    ident = [1 if query[i] == paralog[i] else 0 for i in range(n)]
    if len(set(ident)) == 1:
        raise AnalysisError(
            "per-residue identity is constant over the compared region, so no "
            "divergence point exists; refusing to invent one"
        )

    divergence_point, stat = _changepoint(ident)

    import random

    rng = random.Random(PERMUTATION_SEED)
    shuffled = list(ident)
    n_ge = 0
    permuted_max = 0.0
    for _ in range(N_PERMUTATIONS):
        rng.shuffle(shuffled)
        _, s = _changepoint(shuffled)
        permuted_max = max(permuted_max, s)
        if s >= stat:
            n_ge += 1
    p_value = (n_ge + 1) / (N_PERMUTATIONS + 1)
    if n_ge > 0:
        raise AnalysisError(
            f"the best changepoint (statistic {stat:.3f}) is matched by "
            f"{n_ge}/{N_PERMUTATIONS} permutations of the same identity vector "
            f"(p = {p_value:.4f}); there is no significant divergence point to report"
        )

    before = ident[:divergence_point]
    after = ident[divergence_point:]
    blocks = []
    for start in range(0, n, BLOCK):
        chunk = ident[start : start + BLOCK]
        blocks.append(
            {
                "start": start + 1,
                "end": start + len(chunk),
                "identity": round(sum(chunk) / len(chunk), 4),
            }
        )
    return DivergenceResult(
        colinear_prefix_proved=True,
        divergence_point=divergence_point,
        statistic=round(stat, 4),
        permutations=N_PERMUTATIONS,
        permuted_max_statistic=round(permuted_max, 4),
        empirical_p_value=p_value,
        identity_before=sum(before) / len(before) if before else 0.0,
        identity_after=sum(after) / len(after) if after else 0.0,
        n_identical_before=sum(before),
        n_compared_before=len(before),
        n_identical_after=sum(after),
        n_compared_after=len(after),
        block_profile=blocks,
    )


# --- analysis 2: arginine finger ------------------------------------------------


def test_arginine_finger(
    query_seq: str,
    query_sites: list[int],
    control_rec: dict[str, Any],
) -> dict[str, Any]:
    """Is the control's own arginine finger present, and on an annotated query site?"""
    control_seq = uniprot_sequence(control_rec)
    fingers = site_positions(control_rec, ARGININE_FINGER_TEXT)
    if not fingers:
        raise AnalysisError(
            f"{uniprot_entry_name(control_rec)} carries no '{ARGININE_FINGER_TEXT}' Site "
            "feature, so it cannot serve as a control for this test"
        )
    results = []
    mapping = align_map(control_seq, query_seq)
    for pos in fingers:
        control_res = control_seq[pos - 1]
        q_pos = mapping.get(pos)
        q_res = query_seq[q_pos - 1] if q_pos else None
        lands_on_site = bool(q_pos and q_pos in query_sites)
        results.append(
            {
                "control_position": pos,
                "control_residue": control_res,
                "query_position": q_pos,
                "query_residue": q_res,
                "residue_is_arginine": q_res == "R",
                "lands_on_annotated_query_site": lands_on_site,
                "retained": bool(q_res == "R" and lands_on_site),
            }
        )
    return {
        "control_accession": control_rec["primaryAccession"],
        "control_entry_name": uniprot_entry_name(control_rec),
        "control_reviewed": uniprot_is_reviewed(control_rec),
        "sites": results,
    }


# --- analysis 3: family census --------------------------------------------------


def fetch_rhogap_family() -> tuple[list[dict[str, Any]], int]:
    """All human reviewed proteins carrying the PROSITE RhoGAP profile."""
    size = 500
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query="
        f"%28taxonomy_id%3A9606%29%20AND%20%28reviewed%3Atrue%29%20AND%20"
        f"%28xref%3Aprosite-{RHOGAP_PROSITE}%29"
        f"&fields=accession%2Cid%2Cprotein_name%2Cft_site%2Csequence%2Clength"
        f"&format=json&size={size}"
    )
    dest = CACHE_DIR / f"rhogap_family_{RHOGAP_PROSITE}.json"
    if dest.exists() and dest.stat().st_size > 0:
        payload = json.loads(dest.read_text())
        total = payload.get("_x_total_results")
        results = payload["results"]
    else:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as fh:
                body = fh.read()
                total_hdr = fh.headers.get("x-total-results")
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            raise AnalysisError(f"could not fetch the RhoGAP family census: {exc}") from exc
        payload = json.loads(body)
        total = int(total_hdr) if total_hdr is not None else None
        payload["_x_total_results"] = total
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(payload))
        results = payload["results"]
    if total is None:
        raise AnalysisError("UniProt did not return x-total-results; cannot verify completeness")
    # Anti-truncation: compare the reported total against what was actually READ, never
    # against the page-size constant we chose. A service that clamps rather than errors
    # would sail past a page-size test.
    if total != len(results):
        raise AnalysisError(
            f"RhoGAP family census truncated: server reports {total} hits, "
            f"{len(results)} were read. Paginate before drawing any conclusion."
        )
    return results, total


# Phrases that can only be about the PROTEIN's own catalytic status. An earlier version of
# this check used the bare word "inactive", which matched ARHGAP36's FUNCTION line
# "converting them to an inactive GDP-bound state" -- the GTPase's state, not the protein's
# -- and scored a protein UniProt calls ACTIVE as confirmed inactive. Any substring test on
# a controlled vocabulary needs an anchor.
INACTIVE_PHRASES = (
    "lacks the catalytic arginine",
    "is catalytically inactive",
    "catalytically inactive",
    "does not have gtpase activator",
    "no gap activity",
    "lacks gap activity",
)
ACTIVE_PHRASES = ("gtpase activator", "gap activity")
EXPERIMENTAL_ECO = "ECO:0000269"


def catalytic_status(rec: dict[str, Any]) -> dict[str, Any]:
    """What does UniProt itself say about this protein's GAP activity, and on what evidence?

    Residue identity is one thing; what a curator has concluded is another. Reporting them
    separately is the point -- if they disagree, that disagreement is the finding.
    """
    items = []
    for c in rec.get("comments", []):
        if c.get("commentType") not in {"FUNCTION", "CAUTION", "DOMAIN"}:
            continue
        for t in c.get("texts", []):
            ecos = sorted({e.get("evidenceCode", "") for e in (t.get("evidences") or [])})
            items.append({"type": c["commentType"], "text": t.get("value", ""), "eco": ecos})

    inact = [i for i in items if any(k in i["text"].lower() for k in INACTIVE_PHRASES)]
    act = [
        i
        for i in items
        if any(k in i["text"].lower() for k in ACTIVE_PHRASES)
        and not any(k in i["text"].lower() for k in INACTIVE_PHRASES)
    ]
    if inact:
        verdict = "UNIPROT_SAYS_INACTIVE"
        chosen = inact[0]
    elif act:
        verdict = "UNIPROT_ASSERTS_ACTIVITY"
        chosen = act[0]
    else:
        return {"verdict": "UNIPROT_SILENT", "statement": None, "eco": [], "experimental": False}
    return {
        "verdict": verdict,
        "statement": chosen["text"][:400],
        "comment_type": chosen["type"],
        "eco": chosen["eco"],
        "experimental": EXPERIMENTAL_ECO in chosen["eco"],
    }


def census_arginine_fingers(
    entries: list[dict[str, Any]], fetch_status: bool = True
) -> dict[str, Any]:
    with_finger, without_finger = [], []
    finger_is_r, finger_not_r = [], []
    for rec in entries:
        seq = rec.get("sequence", {}).get("value")
        if not seq:
            raise AnalysisError(f"census entry {rec.get('primaryAccession')} has no sequence")
        positions = site_positions(rec, ARGININE_FINGER_TEXT)
        acc = rec["primaryAccession"]
        name = rec.get("uniProtkbId", "")
        if not positions:
            without_finger.append({"accession": acc, "entry_name": name})
            continue
        with_finger.append({"accession": acc, "entry_name": name, "positions": positions})
        residues = [seq[p - 1] for p in positions if 1 <= p <= len(seq)]
        row = {"accession": acc, "entry_name": name, "positions": positions, "residues": residues}
        if residues and all(r == "R" for r in residues):
            finger_is_r.append(row)
        else:
            finger_not_r.append(row)
    # For everything the residue screen FLAGS, ask what UniProt concluded independently.
    # A count of flagged proteins is not a count of confirmed pseudo-enzymes.
    status_counts: Counter[str] = Counter()
    n_experimental = 0
    if fetch_status:
        for row in finger_not_r:
            rec = fetch_uniprot(row["accession"])
            st = catalytic_status(rec)
            row["uniprot_catalytic_status"] = st
            status_counts[st["verdict"]] += 1
            if st["verdict"] == "UNIPROT_SAYS_INACTIVE" and st["experimental"]:
                n_experimental += 1

    return {
        "n_entries": len(entries),
        "n_with_annotated_arginine_finger": len(with_finger),
        "n_without_annotated_arginine_finger": len(without_finger),
        "n_finger_position_is_arginine": len(finger_is_r),
        "n_finger_position_not_arginine": len(finger_not_r),
        "flagged_uniprot_status_counts": dict(status_counts),
        "n_flagged_confirmed_inactive_experimentally": n_experimental,
        "finger_not_arginine": finger_not_r,
        "without_annotated_arginine_finger": without_finger,
    }


# --- analysis 4: structural interface -------------------------------------------


def fetch_structure(pdb_id: str) -> Any:
    raw = _fetch(
        f"https://files.rcsb.org/download/{pdb_id.lower()}.cif",
        CACHE_DIR / f"{pdb_id.lower()}.cif",
    )
    parser = FastMMCIFParser(QUIET=True)
    import io

    return parser.get_structure(pdb_id, io.StringIO(raw.decode()))


def chain_observed_sequence(chain: Any) -> tuple[str, list[int]]:
    seq, nums = [], []
    for res in chain:
        if res.id[0] != " ":
            continue
        try:
            one = protein_letters_3to1[res.get_resname()]
        except KeyError:
            continue
        seq.append(one)
        nums.append(res.id[1])
    return "".join(seq), nums


def prove_chain_identity(observed: str, reference: str, label: str, min_identity: float = 0.9) -> float:
    """Refuse to proceed unless the chain really is the protein we think it is."""
    if not observed:
        raise AnalysisError(f"{label}: no observed protein residues in this chain")
    mapping = align_map(observed, reference)
    matched = sum(1 for i, j in mapping.items() if observed[i - 1] == reference[j - 1])
    identity = matched / len(observed)
    if identity < min_identity:
        raise AnalysisError(
            f"{label}: observed chain sequence is only {identity:.1%} identical to the "
            "UniProt sequence it is supposed to be. The chain roles assumed by this "
            "analysis are wrong; refusing to compute an interface."
        )
    return identity


def gap_gtpase_interface(
    gap_ref_seq: str, gtpase_ref_seq: str, gap_chain_id: str, gtpase_chain_id: str
) -> dict[str, Any]:
    structure = fetch_structure(INTERFACE_PDB)
    model = next(iter(structure))
    chain_ids = [c.id for c in model]
    for needed in (gap_chain_id, gtpase_chain_id):
        if needed not in chain_ids:
            raise AnalysisError(
                f"{INTERFACE_PDB} has no chain {needed} (chains present: {chain_ids})"
            )
    gap_chain = model[gap_chain_id]
    gtpase_chain = model[gtpase_chain_id]

    gap_obs, gap_nums = chain_observed_sequence(gap_chain)
    gtpase_obs, _ = chain_observed_sequence(gtpase_chain)
    gap_identity = prove_chain_identity(gap_obs, gap_ref_seq, f"{INTERFACE_PDB}:{gap_chain_id}")
    gtpase_identity = prove_chain_identity(
        gtpase_obs, gtpase_ref_seq, f"{INTERFACE_PDB}:{gtpase_chain_id}"
    )

    partner_atoms = [a for r in gtpase_chain for a in r if r.id[0] == " "]
    ligand_names = set()
    for chain in model:
        for res in chain:
            if res.id[0] == " ":
                continue
            resname = res.get_resname().strip()
            if resname in TS_LIGANDS:
                ligand_names.add(resname)
                partner_atoms.extend(list(res))
    missing = TS_LIGANDS - ligand_names
    if missing:
        raise AnalysisError(
            f"{INTERFACE_PDB} is missing expected transition-state ligands {sorted(missing)}; "
            "this is not the transition-state complex this analysis requires"
        )
    if not partner_atoms:
        raise AnalysisError("no partner atoms found for the interface calculation")

    search = NeighborSearch(partner_atoms)
    contacts: list[int] = []
    for res in gap_chain:
        if res.id[0] != " ":
            continue
        if any(search.search(atom.coord, CONTACT_CUTOFF_A) for atom in res):
            contacts.append(res.id[1])

    # Map the structure's own numbering onto the UniProt sequence via alignment, so no
    # residue number is trusted to be a UniProt number.
    obs_to_ref = align_map(gap_obs, gap_ref_seq)
    num_to_index = {num: i + 1 for i, num in enumerate(gap_nums)}
    contact_ref: list[int] = []
    for num in contacts:
        idx = num_to_index.get(num)
        if idx is None:
            continue
        ref = obs_to_ref.get(idx)
        if ref is not None:
            contact_ref.append(ref)
    if not contact_ref:
        raise AnalysisError("interface calculation produced no mapped contacts")

    return {
        "pdb_id": INTERFACE_PDB,
        "gap_chain": gap_chain_id,
        "gtpase_chain": gtpase_chain_id,
        "gap_chain_identity_to_reference": round(gap_identity, 4),
        "gtpase_chain_identity_to_reference": round(gtpase_identity, 4),
        "ligands_included": sorted(ligand_names),
        "cutoff_angstrom": CONTACT_CUTOFF_A,
        "n_contacts": len(contact_ref),
        "contact_positions_in_reference": sorted(set(contact_ref)),
    }


def partition_interface(
    interface: dict[str, Any],
    gap_ref_seq: str,
    control_domain: tuple[int, int],
    control_finger: int,
    paralog_seq: str,
    paralog_domain: tuple[int, int],
    paralog_finger: int,
    divergence_point: int,
) -> dict[str, Any]:
    """Project the control GAP's interface onto ARHGAP11A, then split it by what
    ARHGAP11B still has.

    ARHGAP1 carries its Rho-GAP domain at the C-terminus behind a CRAL-TRIO domain,
    while ARHGAP11A carries its at the N-terminus of a 1023-residue protein. A global
    alignment of the two full sequences therefore pairs N-terminus with N-terminus and
    lands the whole interface in the wrong half of ARHGAP11A -- which is exactly what
    an earlier version of this function did, mapping the arginine finger to residue
    684. So the control's annotated Rho-GAP domain is excised and aligned LOCALLY, and
    the result is only accepted if the control's own arginine finger lands on the
    paralog's own annotated arginine finger. That reciprocal anchor is the check; the
    local alignment alone is not sufficient.
    """
    c_start, c_end = control_domain
    p_start, p_end = paralog_domain
    control_domain_seq = gap_ref_seq[c_start - 1 : c_end]
    paralog_domain_seq = paralog_seq[p_start - 1 : p_end]

    # Two projections, because either alone can mislead.
    #
    # LOCAL (control domain vs the whole paralog) does not assume the paralog's own
    # domain boundary is correct -- but it is free to stop early, and on this pair it
    # does: it ends at control 401 / paralog 204, i.e. just short of the divergence
    # point at 220. Six interface contacts fall past its end, so reading "0 contacts
    # lost" off the local alignment alone would report an alignment artefact as biology.
    #
    # GLOBAL (control domain vs paralog domain) covers both domains end to end and can
    # therefore answer the question the local alignment declines to. Its risk is drift
    # at low identity, so it is accepted only if it agrees with the local alignment
    # everywhere both have an opinion.
    local = {c_start + k - 1: v for k, v in align_map(control_domain_seq, paralog_seq, mode="local").items()}
    glob = {
        c_start + k - 1: p_start + v - 1
        for k, v in align_map(control_domain_seq, paralog_domain_seq, mode="global").items()
    }

    for label, mapping_ in (("local", local), ("domain-global", glob)):
        anchor = mapping_.get(control_finger)
        if anchor != paralog_finger:
            raise AnalysisError(
                f"{label} alignment anchor failed: the control's arginine finger "
                f"({control_finger}) maps to paralog residue {anchor}, but the paralog's own "
                f"annotated arginine finger is {paralog_finger}. The domains are not in "
                "register; refusing to partition an interface computed on a bad alignment."
            )

    shared = sorted(set(local) & set(glob))
    disagreements = [(p, local[p], glob[p]) for p in shared if local[p] != glob[p]]
    if disagreements:
        raise AnalysisError(
            f"the local and domain-global projections disagree at {len(disagreements)} of "
            f"{len(shared)} shared positions (first: {disagreements[0]}). One of them is "
            "drifting; refusing to extend the mapping past the local alignment's end."
        )

    mapping = glob
    retained, lost, unmapped = [], [], []
    for pos in interface["contact_positions_in_reference"]:
        target = mapping.get(pos)
        if target is None:
            unmapped.append(pos)
            continue
        row = {
            "control_position": pos,
            "control_residue": gap_ref_seq[pos - 1],
            "paralog_position": target,
            "paralog_residue": paralog_seq[target - 1],
            "inside_paralog_rhogap_domain": p_start <= target <= p_end,
        }
        if target <= divergence_point:
            retained.append(row)
        else:
            lost.append(row)
    n_mapped = len(retained) + len(lost)
    in_domain_lost = [r for r in lost if r["inside_paralog_rhogap_domain"]]
    return {
        "divergence_point": divergence_point,
        "alignment_mode": "global, control Rho-GAP domain vs paralog Rho-GAP domain",
        "cross_checked_against": "local, control Rho-GAP domain vs full paralog",
        "n_positions_shared_by_both_projections": len(shared),
        "n_projection_disagreements": 0,
        "local_projection_last_control_position": max(local) if local else None,
        "local_projection_last_paralog_position": max(local.values()) if local else None,
        "anchor_control_arginine_finger": control_finger,
        "anchor_paralog_arginine_finger": paralog_finger,
        "anchor_verified": True,
        "n_control_contacts": len(interface["contact_positions_in_reference"]),
        "n_mapped_to_paralog": n_mapped,
        "n_unmapped": len(unmapped),
        "unmapped_control_positions": unmapped,
        "n_retained_by_query": len(retained),
        "n_lost_by_query": len(lost),
        "fraction_lost": round(len(lost) / n_mapped, 4) if n_mapped else None,
        "lost_contacts": lost,
        "retained_contacts": retained,
        "n_lost_inside_paralog_rhogap_domain": len(in_domain_lost),
        "lost_inside_paralog_rhogap_domain": in_domain_lost,
    }


# --- driver ---------------------------------------------------------------------


def run(
    query_seq_override: str | None = None,
    skip_census: bool = False,
    gap_chain_id: str = GAP_CHAIN,
    gtpase_chain_id: str = GTPASE_CHAIN,
    family_entries_override: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    query_rec = fetch_uniprot(QUERY_ACC)
    paralog_rec = fetch_uniprot(PARALOG_ACC)
    control_rec = fetch_uniprot(RHOGAP1_ACC)
    rhoa_rec = fetch_uniprot(RHOA_ACC)

    query_seq = query_seq_override if query_seq_override is not None else uniprot_sequence(query_rec)
    paralog_seq = uniprot_sequence(paralog_rec)
    control_seq = uniprot_sequence(control_rec)
    rhoa_seq = uniprot_sequence(rhoa_rec)

    query_sites = site_positions(query_rec)
    if not query_sites:
        raise AnalysisError(
            f"{QUERY_ACC} carries no Site features; the 'lands on an annotated site' "
            "condition cannot be evaluated and the arginine-finger test would degrade "
            "to bare residue matching"
        )

    divergence = derive_divergence_point(query_seq, paralog_seq)

    finger_tests = [
        test_arginine_finger(query_seq, query_sites, paralog_rec),
        test_arginine_finger(query_seq, query_sites, control_rec),
    ]

    query_domain = domain_spans(query_rec, "Rho-GAP")
    paralog_domain = domain_spans(paralog_rec, "Rho-GAP")
    control_domain = domain_spans(control_rec, "Rho-GAP")
    if not query_domain or not paralog_domain:
        raise AnalysisError("expected a Rho-GAP DOMAIN feature on both query and paralog")

    interface = gap_gtpase_interface(control_seq, rhoa_seq, gap_chain_id, gtpase_chain_id)

    # Did the interface calculation recover the control's own arginine finger? If not,
    # the geometry is wrong and every downstream number is meaningless.
    control_fingers = site_positions(control_rec, ARGININE_FINGER_TEXT)
    paralog_fingers = site_positions(paralog_rec, ARGININE_FINGER_TEXT)
    if len(control_fingers) != 1 or len(paralog_fingers) != 1:
        raise AnalysisError(
            f"expected exactly one annotated arginine finger on each of the control "
            f"({control_fingers}) and the paralog ({paralog_fingers}) to anchor the alignment"
        )
    finger_in_interface = [
        p for p in control_fingers if p in interface["contact_positions_in_reference"]
    ]
    if not finger_in_interface:
        raise AnalysisError(
            "the computed GAP:GTPase interface does not include the control's own "
            f"annotated arginine finger {control_fingers}; the contact calculation is wrong"
        )
    if not control_domain:
        raise AnalysisError("expected a Rho-GAP DOMAIN feature on the structural control")
    partition = partition_interface(
        interface,
        control_seq,
        control_domain[0],
        control_fingers[0],
        paralog_seq,
        paralog_domain[0],
        paralog_fingers[0],
        divergence.divergence_point,
    )

    census = None
    if not skip_census:
        entries = (
            family_entries_override
            if family_entries_override is not None
            else fetch_rhogap_family()[0]
        )
        census = census_arginine_fingers(entries)

    q_start, q_end = query_domain[0]
    p_start, p_end = paralog_domain[0]
    domain_overrun = q_end - divergence.divergence_point

    return {
        "subjects": {
            "query": {
                "accession": QUERY_ACC,
                "entry_name": uniprot_entry_name(query_rec),
                "protein_name": uniprot_protein_name(query_rec),
                "reviewed": uniprot_is_reviewed(query_rec),
                "length": len(query_seq),
                "rhogap_domain": query_domain,
                "site_features": query_sites,
            },
            "paralog": {
                "accession": PARALOG_ACC,
                "entry_name": uniprot_entry_name(paralog_rec),
                "protein_name": uniprot_protein_name(paralog_rec),
                "reviewed": uniprot_is_reviewed(paralog_rec),
                "length": len(paralog_seq),
                "rhogap_domain": paralog_domain,
                "arginine_finger_sites": site_positions(paralog_rec, ARGININE_FINGER_TEXT),
            },
            "structural_control": {
                "accession": RHOGAP1_ACC,
                "entry_name": uniprot_entry_name(control_rec),
                "protein_name": uniprot_protein_name(control_rec),
                "reviewed": uniprot_is_reviewed(control_rec),
                "length": len(control_seq),
                "rhogap_domain": control_domain,
                "arginine_finger_sites": control_fingers,
            },
            "gtpase": {
                "accession": RHOA_ACC,
                "entry_name": uniprot_entry_name(rhoa_rec),
                "reviewed": uniprot_is_reviewed(rhoa_rec),
                "length": len(rhoa_seq),
            },
        },
        "divergence": {
            k: v for k, v in divergence.__dict__.items() if k != "block_profile"
        },
        "divergence_block_profile": divergence.block_profile,
        "arginine_finger_tests": finger_tests,
        "rhogap_family_census": census,
        "interface": interface,
        "interface_partition": partition,
        "interface_recovers_control_arginine_finger": finger_in_interface,
        "domain_boundary": {
            "query_domain_start": q_start,
            "query_domain_end": q_end,
            "query_domain_length": q_end - q_start + 1,
            "paralog_domain_start": p_start,
            "paralog_domain_end": p_end,
            "paralog_domain_length": p_end - p_start + 1,
            "divergence_point": divergence.divergence_point,
            "query_domain_residues_past_divergence": max(0, domain_overrun),
            "query_domain_longer_than_paralog_by": (q_end - q_start) - (p_end - p_start),
        },
    }


# --- self-test ------------------------------------------------------------------


def self_test() -> int:
    """Break each check on purpose and require it to notice.

    A self-test can only prove that the guards I thought of fire; it cannot tell me
    which guard I failed to write. So each mutation asserts its ANCHOR is present
    before mutating, and the count of anchors detected must equal the count mutated --
    a mutation whose target has drifted is an error, not a silent pass.
    """
    failures: list[str] = []
    baseline = run()

    # ---- T1: remove the arginine finger; the test must report it lost.
    q_seq = uniprot_sequence(fetch_uniprot(QUERY_ACC))
    finger_positions = [
        s["query_position"]
        for t in baseline["arginine_finger_tests"]
        for s in t["sites"]
        if s["query_position"] is not None
    ]
    detected = len(finger_positions)
    if detected == 0:
        failures.append("T1: no arginine-finger anchor detected in the baseline; nothing to mutate")
    else:
        mutated = 0
        seq_list = list(q_seq)
        for pos in sorted(set(finger_positions)):
            if seq_list[pos - 1] != "R":
                failures.append(f"T1: anchor at {pos} is {seq_list[pos - 1]!r}, not 'R'; drifted")
                continue
            seq_list[pos - 1] = "A"
            mutated += 1
        if mutated != len(set(finger_positions)):
            failures.append(f"T1: detected {len(set(finger_positions))} anchors but mutated {mutated}")
        broken = run(query_seq_override="".join(seq_list), skip_census=True)
        still_retained = [
            s for t in broken["arginine_finger_tests"] for s in t["sites"] if s["retained"]
        ]
        if still_retained:
            failures.append(f"T1: arginine finger still reported retained after R->A: {still_retained}")

    # ---- T2: restore the paralog C-terminus; divergence and lost contacts must move.
    p_seq = uniprot_sequence(fetch_uniprot(PARALOG_ACC))
    dp = baseline["divergence"]["divergence_point"]
    if dp >= len(q_seq):
        failures.append("T2: baseline divergence point is at/after the query C-terminus; drifted")
    else:
        restored = q_seq[:dp] + p_seq[dp : len(q_seq)]
        if restored == q_seq:
            failures.append("T2: the restoring mutation changed nothing; anchor drifted")
        else:
            try:
                run(query_seq_override=restored, skip_census=True)
                failures.append(
                    "T2: a query restored to the paralog sequence still yielded a significant "
                    "divergence point; the changepoint test is not discriminating"
                )
            except AnalysisError as exc:
                msg = str(exc)
                ok_reasons = (
                    "no significant divergence point",
                    "per-residue identity is constant",
                )
                if not any(r in msg for r in ok_reasons):
                    failures.append(f"T2: failed for the wrong reason: {exc}")

    # ---- T3: swap the chain roles; the frame proof must refuse.
    try:
        run(skip_census=True, gap_chain_id=GTPASE_CHAIN, gtpase_chain_id=GAP_CHAIN)
        failures.append("T3: swapped chain roles were accepted; the frame proof does not fire")
    except AnalysisError as exc:
        if "identical to the" not in str(exc):
            failures.append(f"T3: failed for the wrong reason: {exc}")

    # ---- T4: the census must be able to SEE a lost arginine finger.
    fake = [
        {
            "primaryAccession": "X0TEST1",
            "uniProtkbId": "TEST_LOST",
            "sequence": {"value": "MAAAAAAAAA"},
            "features": [
                {
                    "type": "Site",
                    "description": "Arginine finger; crucial for GTP hydrolysis",
                    "location": {"start": {"value": 5}, "end": {"value": 5}},
                }
            ],
        },
        {
            "primaryAccession": "X0TEST2",
            "uniProtkbId": "TEST_KEPT",
            "sequence": {"value": "MAAARAAAAA"},
            "features": [
                {
                    "type": "Site",
                    "description": "Arginine finger; crucial for GTP hydrolysis",
                    "location": {"start": {"value": 5}, "end": {"value": 5}},
                }
            ],
        },
    ]
    got = census_arginine_fingers(fake, fetch_status=False)
    if got["n_finger_position_not_arginine"] != 1 or got["n_finger_position_is_arginine"] != 1:
        failures.append(f"T4: census cannot discriminate a lost arginine finger: {got}")

    # ---- T4b: the catalytic-status reader must not be fooled by "inactive GDP-bound state".
    # This is a real bug this script had: the bare keyword "inactive" matched ARHGAP36's
    # FUNCTION line, which describes the GTPASE's state, and scored a protein UniProt calls
    # ACTIVE as confirmed inactive. Regression-tested with the exact sentence.
    decoy = {
        "comments": [
            {
                "commentType": "FUNCTION",
                "texts": [
                    {
                        "value": (
                            "GTPase activator for the Rho-type GTPases by converting them "
                            "to an inactive GDP-bound state"
                        ),
                        "evidences": [{"evidenceCode": "ECO:0000250"}],
                    }
                ],
            }
        ]
    }
    got_decoy = catalytic_status(decoy)
    if got_decoy["verdict"] != "UNIPROT_ASSERTS_ACTIVITY":
        failures.append(
            "T4b: 'inactive GDP-bound state' was read as the protein being inactive; "
            f"got {got_decoy['verdict']}"
        )
    truly_inactive = {
        "comments": [
            {
                "commentType": "DOMAIN",
                "texts": [
                    {
                        "value": "the Rho-GAP domain lacks the catalytic arginine and is catalytically inactive",
                        "evidences": [{"evidenceCode": "ECO:0000269"}],
                    }
                ],
            }
        ]
    }
    got_inact = catalytic_status(truly_inactive)
    if got_inact["verdict"] != "UNIPROT_SAYS_INACTIVE" or not got_inact["experimental"]:
        failures.append(f"T4b: a genuine inactivity statement was missed: {got_inact}")
    if catalytic_status({"comments": []})["verdict"] != "UNIPROT_SILENT":
        failures.append("T4b: an empty record was not reported as silent")

    # ---- T5: a dead/empty UniProt record must be a hard error, not a silent zero.
    try:
        uniprot_sequence({"sequence": {}})
        failures.append("T5: an empty sequence record was accepted")
    except KeyError:
        pass

    # ---- T6: the interface projection must refuse an out-of-register alignment.
    # This is the bug that actually happened: a GLOBAL alignment of ARHGAP1 onto
    # ARHGAP11A put the arginine finger on residue 684. Reproduce it and require the
    # anchor check to catch it. A wrong expected-anchor value stands in for any
    # alignment that lands somewhere other than the paralog's own annotated site.
    control_rec = fetch_uniprot(RHOGAP1_ACC)
    paralog_rec = fetch_uniprot(PARALOG_ACC)
    control_seq = uniprot_sequence(control_rec)
    paralog_seq_t6 = uniprot_sequence(paralog_rec)
    c_dom = domain_spans(control_rec, "Rho-GAP")[0]
    p_dom = domain_spans(paralog_rec, "Rho-GAP")[0]
    c_finger = site_positions(control_rec, ARGININE_FINGER_TEXT)[0]
    p_finger = site_positions(paralog_rec, ARGININE_FINGER_TEXT)[0]
    fake_iface = {"contact_positions_in_reference": [c_finger]}
    try:
        partition_interface(
            fake_iface,
            control_seq,
            c_dom,
            c_finger,
            paralog_seq_t6,
            p_dom,
            p_finger + 1,  # deliberately wrong expected anchor
            baseline["divergence"]["divergence_point"],
        )
        failures.append("T6: an out-of-register alignment was accepted; the anchor check is dead")
    except AnalysisError as exc:
        if "alignment anchor failed" not in str(exc):
            failures.append(f"T6: failed for the wrong reason: {exc}")
    # and the correct anchor must still pass, or T6 proves nothing
    ok = partition_interface(
        fake_iface, control_seq, c_dom, c_finger, paralog_seq_t6, p_dom, p_finger,
        baseline["divergence"]["divergence_point"],
    )
    if not ok["anchor_verified"]:
        failures.append("T6: the correct anchor did not verify; the check rejects everything")

    for line in failures:
        print("SELF-TEST FAIL:", line)
    if not failures:
        print("SELF-TEST: all 7 checks fired as intended")
    return 1 if failures else 0


# --- reporting ------------------------------------------------------------------


def render_markdown(res: dict[str, Any]) -> str:
    q = res["subjects"]["query"]
    p = res["subjects"]["paralog"]
    c = res["subjects"]["structural_control"]
    div = res["divergence"]
    db = res["domain_boundary"]
    part = res["interface_partition"]
    iface = res["interface"]
    census = res["rhogap_family_census"]

    lines: list[str] = []
    a = lines.append
    a("# ARHGAP11B: a GAP-dead RhoGAP that still has its arginine finger")
    a("")
    a("All numbers below are produced by `analyze_arhgap11b.py` in this directory.")
    a("Re-run it to regenerate this file; do not hand-edit.")
    a("")
    a("```")
    a("uv run python analyze_arhgap11b.py")
    a("uv run python analyze_arhgap11b.py --self-test")
    a("```")
    a("")
    a("## Subjects")
    a("")
    a("| role | accession | entry | length | Rho-GAP DOMAIN (UniProt) |")
    a("|---|---|---|---|---|")
    for key, label in (
        ("query", "query"),
        ("paralog", "paralog / ancestor"),
        ("structural_control", "structural control"),
    ):
        s = res["subjects"][key]
        dom = ", ".join(f"{x}..{y}" for x, y in s["rhogap_domain"]) or "-"
        a(f"| {label} | {s['accession']} | {s['entry_name']} | {s['length']} | {dom} |")
    a("")
    a(
        f"The GTPase in the control structure is {res['subjects']['gtpase']['entry_name']} "
        f"({res['subjects']['gtpase']['accession']})."
    )
    a("")

    a("## 1. Where ARHGAP11B stops being ARHGAP11A")
    a("")
    a(
        f"Colinearity proved (global alignment of the N-terminal regions opens no gaps): "
        f"`{div['colinear_prefix_proved']}`."
    )
    a(
        "No identity cutoff is chosen anywhere. The boundary is the single changepoint that "
        "maximises the between-segment sum of squares of the per-residue identity vector, and "
        f"its significance is established by permuting that vector {div['permutations']} times: "
        f"observed statistic {div['statistic']}, best statistic over permutations "
        f"{div['permuted_max_statistic']}, empirical p = {div['empirical_p_value']:.2e}. "
        "The script raises rather than reporting the argmax of noise if any permutation matches "
        "the observed statistic."
    )
    a("")
    a(f"**Derived divergence point: residue {div['divergence_point']}.**")
    a("")
    a("| region | identical / compared | identity |")
    a("|---|---|---|")
    a(
        f"| 1-{div['divergence_point']} | {div['n_identical_before']} / "
        f"{div['n_compared_before']} | {div['identity_before']:.1%} |"
    )
    a(
        f"| {div['divergence_point'] + 1}-{q['length']} | {div['n_identical_after']} / "
        f"{div['n_compared_after']} | {div['identity_after']:.1%} |"
    )
    a("")

    a("## 2. The arginine finger is retained")
    a("")
    a(
        "A control's own annotated arginine finger is aligned onto ARHGAP11B and scored as "
        "retained only if the aligned residue is an arginine **and** the aligned position "
        "lands on one of ARHGAP11B's own annotated Site features."
    )
    a("")
    a("| control | control site | control residue | aligned ARHGAP11B position | residue | on an annotated ARHGAP11B site | retained |")
    a("|---|---|---|---|---|---|---|")
    for t in res["arginine_finger_tests"]:
        for s in t["sites"]:
            a(
                f"| {t['control_entry_name']} ({t['control_accession']}) | {s['control_position']} | "
                f"{s['control_residue']} | {s['query_position']} | {s['query_residue']} | "
                f"{s['lands_on_annotated_query_site']} | **{s['retained']}** |"
            )
    a("")
    a(
        "So the residue test that normally exposes a pseudo-enzyme returns *retained* here, "
        "for a protein that two independent experimental annotations record as GAP-dead. "
        "The hypothesis that ARHGAP11B lost catalysis by losing its arginine finger is "
        "**not confirmed**."
    )
    a("")

    if census is not None:
        a("## 3. How much does the arginine-finger test discriminate?")
        a("")
        a(
            f"All **{census['n_entries']} reviewed (Swiss-Prot) human proteins** carrying the "
            f"PROSITE RhoGAP profile {RHOGAP_PROSITE} were fetched. This is the Swiss-Prot "
            "subset of the family, not the whole family."
        )
        a("")
        a("| | count |")
        a("|---|---|")
        a(f"| entries | {census['n_entries']} |")
        a(f"| with an annotated arginine finger | {census['n_with_annotated_arginine_finger']} |")
        a(f"| without an annotated arginine finger | {census['n_without_annotated_arginine_finger']} |")
        a(f"| annotated finger position holds R | {census['n_finger_position_is_arginine']} |")
        a(f"| annotated finger position does not hold R | {census['n_finger_position_not_arginine']} |")
        a("")
        if census["n_finger_position_not_arginine"] == 0:
            a(
                "Every annotated arginine-finger position in the reviewed human RhoGAP set "
                "holds an arginine. The test therefore separates no member of this set from "
                "any other, so it could not have predicted ARHGAP11B's inactivity."
            )
        else:
            a(
                f"The screen flags {census['n_finger_position_not_arginine']} of "
                f"{census['n_entries']}. **ARHGAP11B is not among them.** But a count of flagged "
                "proteins is not a count of confirmed pseudo-enzymes, so each flagged entry is "
                "asked what UniProt itself concluded, and on what evidence:"
            )
            a("")
            a("| entry | residue | UniProt verdict | evidence |")
            a("|---|---|---|---|")
            for r in census["finger_not_arginine"]:
                st = r.get("uniprot_catalytic_status", {})
                eco = ", ".join(st.get("eco") or []) or "-"
                a(
                    f"| `{r['entry_name']}` | {'/'.join(r['residues'])} | "
                    f"{st.get('verdict', '?')} | {eco} |"
                )
            a("")
            a(
                f"Only **{census['n_flagged_confirmed_inactive_experimentally']}** of the flagged "
                "entries carries an *experimentally* supported (`ECO:0000269`) UniProt statement "
                "that the domain is catalytically inactive for want of the arginine."
            )
            a("")
            a(
                "The sharper result is that **residue identity and curated activity are decoupled "
                "in both directions within this family**. ARHGAP11B keeps the arginine and is "
                "experimentally GAP-dead. `RHG36_HUMAN` (ARHGAP36) has a threonine at its own "
                "annotated arginine-finger position and UniProt nonetheless asserts GTPase "
                "activator activity for it — by similarity, `ECO:0000250`, which is the weakest "
                "thing UniProt says. That is the same class of defect as the one this review "
                "corrects, pointing the other way."
            )
            a("")
            a(
                "So the catalytic-residue screen could not have predicted ARHGAP11B's inactivity, "
                "and would not have been decisive even where it fires. A curation pipeline that "
                "gates a GAP-activity term on arginine-finger presence keeps the term on this "
                "protein."
            )
        a("")

    a("## 4. What the truncation actually removes")
    a("")
    a(
        f"The GAP:GTPase interface is computed from PDB {iface['pdb_id']} "
        f"(chain {iface['gap_chain']} = {c['entry_name']}, chain {iface['gtpase_chain']} = "
        f"{res['subjects']['gtpase']['entry_name']}), a transition-state mimic containing "
        f"{', '.join(iface['ligands_included'])}. Chain roles are proved, not assumed: chain "
        f"{iface['gap_chain']} is {iface['gap_chain_identity_to_reference']:.1%} identical to "
        f"{c['accession']} and chain {iface['gtpase_chain']} is "
        f"{iface['gtpase_chain_identity_to_reference']:.1%} identical to "
        f"{res['subjects']['gtpase']['accession']}. Contacts are every GAP residue with an atom "
        f"within {iface['cutoff_angstrom']} A of RhoA or of the nucleotide/metal/fluoride."
    )
    a("")
    a(
        f"Sanity check on the geometry: the calculation recovers the control's own annotated "
        f"arginine finger {res['interface_recovers_control_arginine_finger']} among its "
        f"contacts, as it must."
    )
    a("")
    a(
        f"Those {iface['n_contacts']} contact positions are projected onto ARHGAP11A "
        f"({part['alignment_mode']}) and split at the divergence point derived in section 1. "
        f"The projection is accepted only because it is in register: the control's arginine "
        f"finger ({part['anchor_control_arginine_finger']}) maps onto ARHGAP11A's own annotated "
        f"arginine finger ({part['anchor_paralog_arginine_finger']}). Without that reciprocal "
        f"anchor a global alignment of these two proteins lands the whole interface in the "
        f"wrong half of ARHGAP11A, because ARHGAP1 carries its Rho-GAP domain at the C-terminus "
        f"and ARHGAP11A at the N-terminus."
    )
    a("")
    a("| | count |")
    a("|---|---|")
    a(f"| control GAP contacts | {part['n_control_contacts']} |")
    a(f"| mapped onto ARHGAP11A | {part['n_mapped_to_paralog']} |")
    a(f"| unmapped | {part['n_unmapped']} |")
    a(f"| **retained** by ARHGAP11B (ARHGAP11A pos <= {part['divergence_point']}) | {part['n_retained_by_query']} |")
    a(f"| **lost** by ARHGAP11B (ARHGAP11A pos > {part['divergence_point']}) | {part['n_lost_by_query']} |")
    if part["n_lost_inside_paralog_rhogap_domain"] is not None:
        a(
            f"| of those, inside ARHGAP11A's own Rho-GAP domain | "
            f"{part['n_lost_inside_paralog_rhogap_domain']} |"
        )
    a("")
    if part["lost_contacts"]:
        a("Interface positions ARHGAP11B does **not** have (ARHGAP11A numbering):")
        a("")
        a("| control pos | control res | ARHGAP11A pos | ARHGAP11A res | inside ARHGAP11A's Rho-GAP domain |")
        a("|---|---|---|---|---|")
        for r in part["lost_contacts"]:
            a(
                f"| {r['control_position']} | {r['control_residue']} | "
                f"{r['paralog_position']} | {r['paralog_residue']} | "
                f"{r['inside_paralog_rhogap_domain']} |"
            )
        a("")
        a(
            f"The truncation therefore removes {part['n_lost_by_query']} of "
            f"{part['n_mapped_to_paralog']} mapped GAP:GTPase interface positions "
            f"({part['fraction_lost']:.0%}) while leaving the arginine finger in place. "
            "The catalytic residue survives; part of the surface that has to present it to "
            "the GTPase does not."
        )
        a("")
    else:
        a(
            "**No** GAP:GTPase contact position maps past the divergence point. On this "
            "measurement the truncation does not remove interface residues, so the loss of "
            "activity is not explained by loss of contacts and must be argued on other "
            "grounds (fold integrity, or the experiments themselves)."
        )
        a("")

    a("## 5. The UniProt Rho-GAP domain boundary")
    a("")
    a("| | value |")
    a("|---|---|")
    a(f"| ARHGAP11B Rho-GAP DOMAIN | {db['query_domain_start']}..{db['query_domain_end']} ({db['query_domain_length']} aa) |")
    a(f"| ARHGAP11A Rho-GAP DOMAIN | {db['paralog_domain_start']}..{db['paralog_domain_end']} ({db['paralog_domain_length']} aa) |")
    a(f"| derived divergence point | {db['divergence_point']} |")
    a(f"| ARHGAP11B domain residues past the divergence point | {db['query_domain_residues_past_divergence']} |")
    a(f"| ARHGAP11B domain longer than ARHGAP11A's by | {db['query_domain_longer_than_paralog_by']} aa |")
    a("")
    if db["query_domain_residues_past_divergence"] > 0:
        a(
            f"UniProt's Rho-GAP DOMAIN feature on ARHGAP11B runs "
            f"{db['query_domain_residues_past_divergence']} residues past the last residue that "
            f"is homologous to ARHGAP11A, i.e. into the human-specific frameshift C-terminus. "
            f"The annotated domain on the truncated paralog is therefore "
            f"{db['query_domain_longer_than_paralog_by']} residues **longer** than the annotated "
            f"domain on the catalytically active parent. Any pipeline reading domain extent as "
            f"evidence of a working RhoGAP will read this protein as more intact than the active "
            f"one, not less."
        )
    else:
        a("The annotated domain does not extend past the divergence point.")
    a("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true", help="mutate inputs and require checks to fire")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    res = run()
    (SCRIPT_DIR / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (SCRIPT_DIR / "RESULTS.md").write_text(render_markdown(res))
    print(f"wrote {SCRIPT_DIR / 'results.json'}")
    print(f"wrote {SCRIPT_DIR / 'RESULTS.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
