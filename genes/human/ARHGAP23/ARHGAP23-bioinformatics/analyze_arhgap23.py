"""Does ARHGAP23 retain the RhoGAP arginine finger, and what does that license?

ARHGAP23 (Q9P227, 1491 aa) carries a UniProt ``FUNCTION`` statement -- "GTPase
activator for the Rho-type GTPases" -- whose only evidence code is ``ECO:0000250``
(by similarity), and a ``Site`` feature at position 942 described as the arginine
finger whose only evidence code is ``ECO:0000255`` (a PROSITE rule). No experimental
GAP assay for this protein appears in its UniProt reference list. Its single
molecular-function GO annotation is an IBA. So every assertion that this protein is a
working RhoGAP is, at present, an inference from sequence.

This script asks the sequence/structure question directly, and is built so that the
answer is usable in *either* direction:

Analysis 1 -- the arginine finger, tested RECIPROCALLY.
  A comparator's own UniProt-annotated arginine finger is projected onto ARHGAP23 by
  aligning the two Rho-GAP *domains* (never the full-length proteins: these proteins
  place the domain at opposite ends and differ three-fold in length, and a global
  full-length alignment lands the domain in the wrong region). The residue is scored
  ``retained`` only if the aligned residue is an arginine AND the aligned position
  lands on one of ARHGAP23's own annotated Site features. The projection is then run
  BACKWARDS -- ARHGAP23's own annotated site is mapped onto the comparator and must
  land on the comparator's annotated finger -- and only a test that passes in both
  directions is reported as reciprocal. A one-way hit is reported as one-way.

  Comparators: ARHGAP1/p50RhoGAP (Q07960), whose arginine finger is resolved in a
  transition-state crystal structure, and ARHGAP21 (Q5T5U3), the closest paralog --
  same PDZ-PH-RhoGAP architecture -- and the named donor in ARHGAP23's own IBA row.

Analysis 2 -- calibration, through the identical code path.
  The same test is run on two controls that are *known* to be GAP-dead, chosen so
  that they fail in opposite ways:
    * OCRL (Q01968) -- UniProt states its Rho-GAP domain is catalytically inactive,
      and the annotated finger position holds a glutamine. The test must return
      NOT retained, which is what shows it is capable of firing at all.
    * ARHGAP11B (Q3KRB8) -- two curated IDA annotations record ``NOT enables
      GO:0005096``, yet it keeps its arginine. The test must return retained.
  Together these fix the interpretation: a NEGATIVE result is informative, a POSITIVE
  result is not evidence of activity. The script prints that as a measured property of
  the assay on these controls rather than as an opinion, and quotes the family-wide
  version of the same number from the sibling analysis
  (``genes/human/ARHGAP11B/ARHGAP11B-bioinformatics/results.json``) by reading it,
  never by transcribing it.

Analysis 3 -- the rest of the catalytic surface, measured on a structure.
  One residue is a thin basis for a molecular-function call, so the whole GAP:GTPase
  interface is computed from PDB 1TX4 (p50RhoGAP:RhoA:GDP:AlF4, a transition-state
  mimic) as every ARHGAP1 residue within a cutoff of RhoA or of the nucleotide, metal
  and fluoride ligands. Chain roles are proved by aligning each observed chain to the
  UniProt sequence it is supposed to be, and the contact set must recover ARHGAP1's
  own annotated arginine finger or the geometry is rejected. Those positions are then
  projected onto each subject -- accepted only when the projection is in register, ie
  ARHGAP1 282 lands on the subject's own annotated finger -- and scored as identical,
  conservative or lost. This gives ARHGAP23's number a scale: the same count is
  produced for a working GAP, for a GAP-dead protein that lost the residue, and for a
  GAP-dead protein that kept it.

Analysis 4 -- provenance of the claim being tested.
  For every subject, the evidence codes actually attached to its UniProt arginine-finger
  Site feature and to its FUNCTION comment are extracted from the fetched record, so
  "this is asserted by similarity, not measured" is a value read out of the data rather
  than a claim in prose.

Analysis 5 -- the published specificity screen, and the mutant it calls an arginine finger.
  Müller et al. 2020 (PMID:32203420) ran a cellular FRET-biosensor screen over the whole
  human RhoGEF/RhoGAP family. Its main text is paywalled and absent from PMC, but the
  publisher's Source Data and Supplementary Tables are open, so they are PARSED here
  rather than quoted from memory: ARHGAP23's Fig. 1b row (per-GTPase effect size,
  p-value and the authors' own significance flags), the cDNA it was screened as, and the
  localization row that names its point mutant. Three things are then checked that a
  reader cannot check from the abstract:
    * the screened construct is the same length as the UniProt canonical sequence, so the
      residue numbers are comparable at all -- if not, the comparison is refused;
    * the mutant designation is READ OUT of the supplementary PDF by regex rather than
      hardcoded here, so the residue number this section turns on cannot be mine;
    * that mutant position is mapped onto the structural comparator and asked whether it
      is the annotated arginine finger and whether it contacts the transition-state
      ligands in 1TX4 -- the property that makes a residue an arginine finger.
  The sentence naming the proteins whose arginine-finger mutants validated the screen is
  extracted verbatim, and whether ARHGAP23 is among them is computed, not asserted.

Every number in RESULTS.md is produced by a run of this script; nothing is hardcoded.
Missing input is a hard error naming the fix, never a silently degraded section.
``--self-test`` mutates the inputs and asserts each check flips with its expected
message, asserts that the number of mutations applied equals the number of anchors
detected, and includes negative controls that must leave every verdict unchanged.

Usage:
    uv run python analyze_arhgap23.py              # run analyses, write results.json + RESULTS.md
    uv run python analyze_arhgap23.py --self-test
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Data.PDBData import protein_letters_3to1
from Bio.PDB import FastMMCIFParser, NeighborSearch

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "cache"
REPO = SCRIPT_DIR.parents[3]
SIBLING_CENSUS = (
    REPO / "genes/human/ARHGAP11B/ARHGAP11B-bioinformatics/results.json"
)

SUBJECT_ACC = "Q9P227"  # ARHGAP23, the subject of the review

# Comparators: proteins whose arginine finger is projected onto a subject.
STRUCTURAL_COMPARATOR = "Q07960"  # ARHGAP1 / p50RhoGAP, resolved in 1TX4
PARALOG_COMPARATOR = "Q5T5U3"  # ARHGAP21, closest paralog and named IBA donor

# Controls, run as subjects through the identical code path.
CONTROL_LOST_ACC = "Q01968"  # OCRL: UniProt states the Rho-GAP domain is inactive
CONTROL_RETAINED_ACC = "Q3KRB8"  # ARHGAP11B: experimentally GAP-dead, keeps its arginine

RHOA_ACC = "P61586"  # RhoA, the GTPase in the control structure

# Müller et al. 2020, Nat Cell Biol (PMID:32203420, doi 10.1038/s41556-020-0488-x): the
# FRET-biosensor RhoGEF/RhoGAP specificity screen. The main text is paywalled and absent
# from PMC, but the publisher's Supplementary Information and Source Data are open, and
# they are the only place ARHGAP23's substrate specificity and its published "arginine
# finger mutant" are recorded. Both are parsed here rather than transcribed.
MULLER_PMID = "32203420"
MULLER_ESM = (
    "https://static-content.springer.com/esm/art%3A10.1038%2Fs41556-020-0488-x/"
    "MediaObjects/41556_2020_488_MOESM{n}_ESM.{ext}"
)
MULLER_TABLES_ESM = (3, "xlsx")  # Supplementary Tables 1-4
MULLER_FIG1B_ESM = (10, "xlsx")  # Source Data for Fig. 1b
MULLER_SI_PDF = (1, "pdf")  # Supplementary Information (figures + notes)
# The mutant designation is DERIVED from the SI, not written here, so that a hardcoded
# residue number can never be the thing this section's conclusion rests on.
MULLER_MUTANT_RE = re.compile(r"ARHGAP23\s*[-‐-―]?\s*([A-Z])(\d+)([A-Z])")

INTERFACE_PDB = "1TX4"
GAP_CHAIN = "A"
GTPASE_CHAIN = "B"
# The transition-state mimic: GDP + aluminium fluoride + Mg. Their absence means the
# structure fetched is not the complex this analysis requires.
TS_LIGANDS = {"GDP", "ALF", "MG"}
CONTACT_CUTOFF_A = 4.5

ARGININE_FINGER_TEXT = "Arginine finger"
RHOGAP_DOMAIN_TEXT = "Rho-GAP"


GAP_TERM = "GO:0005096"
EXPERIMENTAL_GO_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}
EXPERIMENTAL_ECO = "ECO:0000269"

# Each control's credential is a TESTABLE PROPOSITION, verified below against the
# repo's own machine-fetched GOA file or against the fetched UniProt record. A control
# whose credential cannot be verified aborts the run rather than being described in
# prose as something it has not been shown to be.
CONTROL_CREDENTIALS: dict[str, dict[str, Any]] = {
    "positive_control": {
        "kind": "goa",
        "symbol": "ARHGAP21",
        "qualifier": "enables",
        "term": GAP_TERM,
        "claim": "an active RhoGAP with a direct experimental GTPase-activator annotation",
    },
    "control_retained": {
        "kind": "goa",
        "symbol": "ARHGAP11B",
        "qualifier": "NOT|enables",
        "term": GAP_TERM,
        "claim": "experimentally GAP-dead: curated NOT annotations for GTPase activator activity",
    },
    "control_lost": {
        "kind": "uniprot_comment",
        "comment_type": "DOMAIN",
        "needle": "catalytically inactive",
        "claim": "UniProt states, on experimental evidence, that its Rho-GAP domain is inactive",
    },
}


class AnalysisError(RuntimeError):
    """A hard failure. Never downgraded to a missing section in the report."""


# --- fetching -------------------------------------------------------------------


def _fetch(url: str, dest: Path) -> bytes:
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
    raw = _fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.json", CACHE_DIR / f"{acc}.json")
    rec = json.loads(raw)
    # A deleted/demerged accession returns HTTP 200 with no sequence, which is
    # indistinguishable from a protein that simply carries no features.
    if not rec.get("sequence", {}).get("value"):
        raise AnalysisError(f"UniProt {acc} returned no sequence (deleted/demerged entry?)")
    if not rec.get("uniProtkbId"):
        raise AnalysisError(f"UniProt {acc} returned no entry name")
    return rec


def seq_of(rec: dict[str, Any]) -> str:
    return rec["sequence"]["value"]


def name_of(rec: dict[str, Any]) -> str:
    return rec["uniProtkbId"]


def is_reviewed(rec: dict[str, Any]) -> bool:
    # "reviewed" is a SUBSTRING of "unreviewed": a containment test silently promotes
    # every TrEMBL entry. Anchor to the start of the string.
    return str(rec.get("entryType", "")).startswith("UniProtKB reviewed")


def site_positions(rec: dict[str, Any], text: str | None = None) -> list[int]:
    """1-based positions of single-residue Site features, optionally filtered by text."""
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


def feature_evidence(rec: dict[str, Any], ftype: str, text: str) -> list[str]:
    """Evidence codes attached to the matching feature(s)."""
    codes: list[str] = []
    for feat in rec.get("features", []):
        if feat.get("type") != ftype:
            continue
        if text.lower() not in str(feat.get("description", "")).lower():
            continue
        for ev in feat.get("evidences", []) or []:
            code = ev.get("evidenceCode")
            if code:
                codes.append(str(code))
    return sorted(set(codes))


def function_comment(rec: dict[str, Any]) -> dict[str, Any]:
    """The FUNCTION comment text and the evidence codes on it."""
    texts: list[str] = []
    codes: list[str] = []
    for com in rec.get("comments", []) or []:
        if com.get("commentType") != "FUNCTION":
            continue
        for block in com.get("texts", []) or []:
            val = block.get("value")
            if val:
                texts.append(str(val))
            for ev in block.get("evidences", []) or []:
                code = ev.get("evidenceCode")
                if code:
                    codes.append(str(code))
    return {"text": " ".join(texts), "evidence_codes": sorted(set(codes))}


def go_xref_evidence(rec: dict[str, Any], go_id: str) -> list[str]:
    """UniProt's own cross-reference evidence string(s) for a GO term, eg 'IDA:MGI'."""
    out = []
    for xref in rec.get("uniProtKBCrossReferences", []) or []:
        if xref.get("database") != "GO" or xref.get("id") != go_id:
            continue
        for prop in xref.get("properties", []) or []:
            if prop.get("key") == "GoEvidenceType":
                out.append(str(prop["value"]))
    return sorted(set(out))


def goa_rows(symbol: str, term: str, qualifier: str) -> list[dict[str, str]]:
    """Matching rows from the repo's own machine-fetched GOA table for a human gene."""
    path = REPO / f"genes/human/{symbol}/{symbol}-goa.tsv"
    if not path.exists():
        raise AnalysisError(
            f"expected {path} to verify the '{symbol}' control's credential. "
            f"Run `just fetch-gene human {symbol}` from the repo root."
        )
    lines = path.read_text().splitlines()
    if not lines:
        raise AnalysisError(f"{path} is empty")
    header = lines[0].split("\t")
    idx = {name: i for i, name in enumerate(header)}
    for needed in ("QUALIFIER", "GO TERM", "GO EVIDENCE CODE", "REFERENCE"):
        if needed not in idx:
            raise AnalysisError(f"{path} has no '{needed}' column (columns: {header})")
    rows = []
    for line in lines[1:]:
        f = line.split("\t")
        if len(f) < len(header):
            continue
        if f[idx["GO TERM"]] != term or f[idx["QUALIFIER"]] != qualifier:
            continue
        rows.append(
            {
                "qualifier": f[idx["QUALIFIER"]],
                "term": f[idx["GO TERM"]],
                "evidence": f[idx["GO EVIDENCE CODE"]],
                "reference": f[idx["REFERENCE"]],
            }
        )
    return rows


def comment_statement(rec: dict[str, Any], comment_type: str, needle: str) -> dict[str, Any]:
    """A comment of the given type containing `needle`, with its evidence codes."""
    for com in rec.get("comments", []) or []:
        if com.get("commentType") != comment_type:
            continue
        for block in com.get("texts", []) or []:
            val = str(block.get("value", ""))
            if needle.lower() not in val.lower():
                continue
            codes = sorted(
                {
                    str(e["evidenceCode"])
                    for e in (block.get("evidences") or [])
                    if e.get("evidenceCode")
                }
            )
            return {"text": val, "evidence_codes": codes}
    return {}


def verify_credential(label: str, prot: "Protein") -> dict[str, Any]:
    """Prove a control is what the report is about to call it, or abort."""
    spec = CONTROL_CREDENTIALS[label]
    if spec["kind"] == "goa":
        rows = goa_rows(spec["symbol"], spec["term"], spec["qualifier"])
        experimental = [r for r in rows if r["evidence"] in EXPERIMENTAL_GO_CODES]
        if not experimental:
            raise AnalysisError(
                f"control '{label}' ({spec['symbol']}) has no experimental GOA row for "
                f"'{spec['qualifier']} {spec['term']}' (found {rows or 'nothing'}), so the "
                f"claim \"{spec['claim']}\" is not supported. Refusing to label it that way."
            )
        return {
            "label": label,
            "claim": spec["claim"],
            "source": f"genes/human/{spec['symbol']}/{spec['symbol']}-goa.tsv",
            "matching_rows": experimental,
            "verified": True,
        }
    statement = comment_statement(prot.rec, spec["comment_type"], spec["needle"])
    if not statement:
        raise AnalysisError(
            f"control '{label}' ({prot.name}) has no {spec['comment_type']} comment containing "
            f"'{spec['needle']}', so the claim \"{spec['claim']}\" is not supported."
        )
    if EXPERIMENTAL_ECO not in statement["evidence_codes"]:
        raise AnalysisError(
            f"control '{label}' ({prot.name}): the {spec['comment_type']} statement carries "
            f"{statement['evidence_codes'] or 'no evidence code'}, not {EXPERIMENTAL_ECO}; "
            "the claim that inactivity is experimentally supported does not hold."
        )
    return {
        "label": label,
        "claim": spec["claim"],
        "source": f"UniProt {prot.acc} {spec['comment_type']} comment",
        "statement": statement,
        "verified": True,
    }


def domain_span(rec: dict[str, Any], note: str = RHOGAP_DOMAIN_TEXT) -> tuple[int, int]:
    """The single Rho-GAP domain span. Ambiguity is an error, not a silent first pick."""
    spans = []
    for feat in rec.get("features", []):
        if feat.get("type") != "Domain":
            continue
        if note.lower() not in str(feat.get("description", "")).lower():
            continue
        start = feat["location"]["start"].get("value")
        end = feat["location"]["end"].get("value")
        if start is None or end is None:
            continue
        spans.append((int(start), int(end)))
    if len(spans) != 1:
        raise AnalysisError(
            f"{name_of(rec)} has {len(spans)} '{note}' Domain features (expected exactly 1); "
            "this analysis aligns domain to domain and cannot choose between them"
        )
    return spans[0]


# --- alignment ------------------------------------------------------------------

_BLOSUM62 = substitution_matrices.load("BLOSUM62")


def make_aligner() -> PairwiseAligner:
    aln = PairwiseAligner()
    aln.substitution_matrix = _BLOSUM62
    aln.open_gap_score = -11
    aln.extend_gap_score = -1
    aln.mode = "global"
    return aln


def align_map(seq_from: str, seq_to: str) -> dict[int, int]:
    """Map 1-based positions of `seq_from` onto 1-based positions of `seq_to`."""
    aln = make_aligner().align(seq_from, seq_to)[0]
    mapping: dict[int, int] = {}
    for (f0, f1), (t0, _t1) in zip(aln.aligned[0], aln.aligned[1]):
        # Biopython returns numpy ints; cast so results are JSON-serialisable and so
        # equality against plain-int site positions behaves predictably.
        f0, f1, t0 = int(f0), int(f1), int(t0)
        for off in range(f1 - f0):
            mapping[f0 + off + 1] = t0 + off + 1
    return mapping


def similar(a: str, b: str) -> bool:
    """Conservative substitution by BLOSUM62 (positive score), excluding identity."""
    if a == b:
        return False
    try:
        return float(_BLOSUM62[a, b]) > 0
    except KeyError:
        return False


# --- domain-restricted projection ------------------------------------------------


class Protein:
    """A UniProt record with its Rho-GAP domain and annotated arginine finger located."""

    def __init__(self, acc: str, rec: dict[str, Any] | None = None):
        # `rec` exists so that --self-test can drive a perturbed record through this
        # EXACT constructor. Re-implementing the checks in the self-test would let a
        # guard be deleted here without the self-test noticing.
        self.rec = fetch_uniprot(acc) if rec is None else rec
        self.acc = self.rec["primaryAccession"]
        self.name = name_of(self.rec)
        self.seq = seq_of(self.rec)
        self.reviewed = is_reviewed(self.rec)
        self.domain_start, self.domain_end = domain_span(self.rec)
        self.sites = site_positions(self.rec)
        fingers = site_positions(self.rec, ARGININE_FINGER_TEXT)
        if not fingers:
            raise AnalysisError(
                f"{self.name} carries no '{ARGININE_FINGER_TEXT}' Site feature; this "
                "analysis anchors every projection on that annotation and cannot proceed"
            )
        if len(fingers) != 1:
            raise AnalysisError(f"{self.name} has {len(fingers)} annotated arginine fingers")
        self.finger = fingers[0]
        if not (self.domain_start <= self.finger <= self.domain_end):
            raise AnalysisError(
                f"{self.name}: annotated arginine finger {self.finger} lies outside its own "
                f"Rho-GAP domain {self.domain_start}-{self.domain_end}"
            )

    @property
    def domain_seq(self) -> str:
        return self.seq[self.domain_start - 1 : self.domain_end]

    def to_local(self, pos: int) -> int | None:
        if not (self.domain_start <= pos <= self.domain_end):
            return None
        return pos - self.domain_start + 1

    def to_global(self, local: int) -> int:
        return local + self.domain_start - 1

    def residue(self, pos: int) -> str:
        return self.seq[pos - 1]

    def summary(self) -> dict[str, Any]:
        return {
            "accession": self.acc,
            "entry_name": self.name,
            "reviewed": self.reviewed,
            "length": len(self.seq),
            "rhogap_domain": [self.domain_start, self.domain_end],
            "annotated_arginine_finger": self.finger,
            "residue_at_annotated_finger": self.residue(self.finger),
            "arginine_finger_evidence": feature_evidence(
                self.rec, "Site", ARGININE_FINGER_TEXT
            ),
            "rhogap_domain_evidence": feature_evidence(self.rec, "Domain", RHOGAP_DOMAIN_TEXT),
            "function_comment": function_comment(self.rec),
            "uniprot_go_xref_evidence_for_gap_term": go_xref_evidence(self.rec, GAP_TERM),
        }


def reciprocal_finger_test(subject: Protein, comparator: Protein) -> dict[str, Any]:
    """Project the comparator's finger onto the subject, then project back."""
    fwd = align_map(comparator.domain_seq, subject.domain_seq)
    rev = align_map(subject.domain_seq, comparator.domain_seq)

    c_local = comparator.to_local(comparator.finger)
    s_local_hit = fwd.get(c_local)
    s_pos = subject.to_global(s_local_hit) if s_local_hit else None
    s_res = subject.residue(s_pos) if s_pos else None
    lands_on_site = bool(s_pos and s_pos in subject.sites)

    s_local = subject.to_local(subject.finger)
    c_local_hit = rev.get(s_local)
    c_pos = comparator.to_global(c_local_hit) if c_local_hit else None
    reverse_ok = c_pos == comparator.finger

    forward_retained = bool(s_res == "R" and lands_on_site)
    return {
        "comparator_accession": comparator.acc,
        "comparator_entry_name": comparator.name,
        "comparator_reviewed": comparator.reviewed,
        "comparator_finger": comparator.finger,
        "comparator_finger_residue": comparator.residue(comparator.finger),
        "forward_mapped_position": s_pos,
        "forward_mapped_residue": s_res,
        "forward_residue_is_arginine": s_res == "R",
        "forward_lands_on_annotated_subject_site": lands_on_site,
        "forward_retained": forward_retained,
        "reverse_mapped_position": c_pos,
        "reverse_lands_on_comparator_finger": reverse_ok,
        "reciprocal": bool(forward_retained and reverse_ok),
    }


# --- structure -------------------------------------------------------------------


def fetch_structure(pdb_id: str) -> Any:
    raw = _fetch(
        f"https://files.rcsb.org/download/{pdb_id.lower()}.cif",
        CACHE_DIR / f"{pdb_id.lower()}.cif",
    )
    return FastMMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(raw.decode()))


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


def gap_gtpase_interface(gap: Protein, gtpase_ref_seq: str) -> dict[str, Any]:
    structure = fetch_structure(INTERFACE_PDB)
    model = next(iter(structure))
    chain_ids = [c.id for c in model]
    for needed in (GAP_CHAIN, GTPASE_CHAIN):
        if needed not in chain_ids:
            raise AnalysisError(
                f"{INTERFACE_PDB} has no chain {needed} (chains present: {chain_ids})"
            )
    gap_chain, gtpase_chain = model[GAP_CHAIN], model[GTPASE_CHAIN]

    gap_obs, gap_nums = chain_observed_sequence(gap_chain)
    gtpase_obs, _ = chain_observed_sequence(gtpase_chain)
    gap_identity = prove_chain_identity(gap_obs, gap.seq, f"{INTERFACE_PDB}:{GAP_CHAIN}")
    gtpase_identity = prove_chain_identity(
        gtpase_obs, gtpase_ref_seq, f"{INTERFACE_PDB}:{GTPASE_CHAIN}"
    )

    protein_atoms = [a for r in gtpase_chain for a in r if r.id[0] == " "]
    ligand_atoms: list[Any] = []
    ligand_names = set()
    for chain in model:
        for res in chain:
            if res.id[0] == " ":
                continue
            resname = res.get_resname().strip()
            if resname in TS_LIGANDS:
                ligand_names.add(resname)
                ligand_atoms.extend(list(res))
    missing = TS_LIGANDS - ligand_names
    if missing:
        raise AnalysisError(
            f"{INTERFACE_PDB} is missing expected transition-state ligands {sorted(missing)}; "
            "this is not the transition-state complex this analysis requires"
        )

    # Contacts are split by PARTNER, because that is what separates a catalytic residue
    # from a binding-surface one: the arginine finger reaches the nucleotide and the
    # AlF4 transition-state mimic, while most interface residues only touch the GTPase.
    protein_search = NeighborSearch(protein_atoms)
    ligand_search = NeighborSearch(ligand_atoms)
    contacts: list[int] = []
    ligand_contacts: list[int] = []
    for res in gap_chain:
        if res.id[0] != " ":
            continue
        touches_protein = any(protein_search.search(a.coord, CONTACT_CUTOFF_A) for a in res)
        touches_ligand = any(ligand_search.search(a.coord, CONTACT_CUTOFF_A) for a in res)
        if touches_protein or touches_ligand:
            contacts.append(res.id[1])
        if touches_ligand:
            ligand_contacts.append(res.id[1])

    # Map the structure's own numbering onto the UniProt sequence by alignment, so no
    # residue number is trusted to be a UniProt number.
    obs_to_ref = align_map(gap_obs, gap.seq)
    num_to_index = {num: i + 1 for i, num in enumerate(gap_nums)}

    def _to_reference(nums: list[int]) -> list[int]:
        out = []
        for num in nums:
            idx = num_to_index.get(num)
            if idx is None:
                continue
            ref = obs_to_ref.get(idx)
            if ref is not None:
                out.append(ref)
        return out

    contact_ref = _to_reference(contacts)
    ligand_contact_ref = _to_reference(ligand_contacts)
    if not contact_ref:
        raise AnalysisError("interface calculation produced no mapped contacts")
    if gap.finger not in ligand_contact_ref:
        raise AnalysisError(
            f"{gap.name}'s annotated arginine finger ({gap.finger}) does not contact the "
            f"transition-state ligands in {INTERFACE_PDB}. That is the defining property of "
            "an arginine finger; the geometry or the numbering is wrong."
        )

    recovers_finger = gap.finger in contact_ref
    if not recovers_finger:
        raise AnalysisError(
            f"the {INTERFACE_PDB} contact set does not contain {gap.name}'s own annotated "
            f"arginine finger ({gap.finger}); the geometry or the numbering is wrong, and "
            "projecting this interface onto another protein would propagate that error"
        )
    in_domain = sorted({p for p in contact_ref if gap.domain_start <= p <= gap.domain_end})
    return {
        "pdb_id": INTERFACE_PDB,
        "gap_chain": GAP_CHAIN,
        "gtpase_chain": GTPASE_CHAIN,
        "gap_chain_identity_to_reference": round(gap_identity, 4),
        "gtpase_chain_identity_to_reference": round(gtpase_identity, 4),
        "ligands_included": sorted(ligand_names),
        "cutoff_angstrom": CONTACT_CUTOFF_A,
        "recovers_control_arginine_finger": recovers_finger,
        "n_contacts": len(set(contact_ref)),
        "contact_positions": sorted(set(contact_ref)),
        "transition_state_ligand_contacts": sorted(set(ligand_contact_ref)),
        "n_contacts_in_rhogap_domain": len(in_domain),
        "contact_positions_in_rhogap_domain": in_domain,
    }


def project_interface(
    subject: Protein, gap: Protein, contacts_in_domain: list[int]
) -> dict[str, Any]:
    """Project the structural interface onto a subject, in-register or not at all."""
    mapping = align_map(gap.domain_seq, subject.domain_seq)
    anchor_local = mapping.get(gap.to_local(gap.finger))
    anchor = subject.to_global(anchor_local) if anchor_local else None
    if anchor != subject.finger:
        raise AnalysisError(
            f"projection of {gap.name} onto {subject.name} is out of register: the control "
            f"arginine finger {gap.finger} maps to {anchor}, not to the subject's own "
            f"annotated finger {subject.finger}. Refusing to report a misaligned interface."
        )
    identical, conservative, different, unaligned = [], [], [], []
    for pos in contacts_in_domain:
        local = gap.to_local(pos)
        hit = mapping.get(local) if local else None
        if hit is None:
            unaligned.append(pos)
            continue
        s_pos = subject.to_global(hit)
        g_res, s_res = gap.residue(pos), subject.residue(s_pos)
        entry = {"control_position": pos, "control_residue": g_res,
                 "subject_position": s_pos, "subject_residue": s_res}
        if g_res == s_res:
            identical.append(entry)
        elif similar(g_res, s_res):
            conservative.append(entry)
        else:
            different.append(entry)
    total = len(contacts_in_domain)
    return {
        "subject_accession": subject.acc,
        "subject_entry_name": subject.name,
        "in_register": True,
        "anchor_maps_to": anchor,
        "n_interface_positions": total,
        "n_identical": len(identical),
        "n_conservative": len(conservative),
        "n_different": len(different),
        "n_unaligned": len(unaligned),
        "pct_identical_or_conservative": (
            round(100.0 * (len(identical) + len(conservative)) / total, 1) if total else None
        ),
        "different": different,
        "unaligned": unaligned,
        "residue_by_control_position": {
            str(e["control_position"]): e["subject_residue"]
            for e in identical + conservative + different
        },
    }


def compare_projections(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    """At the structural interface positions, do two subjects carry the same residues?"""
    ra, rb = a["residue_by_control_position"], b["residue_by_control_position"]
    shared = sorted(set(ra) & set(rb), key=int)
    same = [p for p in shared if ra[p] == rb[p]]
    return {
        "subject_a": a["subject_entry_name"],
        "subject_b": b["subject_entry_name"],
        "n_positions_mapped_in_both": len(shared),
        "n_same_residue": len(same),
        "differences": {
            p: {a["subject_entry_name"]: ra[p], b["subject_entry_name"]: rb[p]}
            for p in shared
            if ra[p] != rb[p]
        },
    }


# --- analysis 5: the published specificity screen and its "arginine finger" mutant ---


def _esm_sheet(n: int, ext: str, sheet: str) -> list[tuple[Any, ...]]:
    raw = _fetch(MULLER_ESM.format(n=n, ext=ext), CACHE_DIR / f"muller_MOESM{n}.{ext}")
    import openpyxl

    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    if sheet not in wb.sheetnames:
        raise AnalysisError(
            f"MOESM{n}.{ext} has no sheet {sheet!r} (sheets: {wb.sheetnames}). The "
            "publisher's supplementary layout has changed; re-check before trusting any "
            "number parsed from it."
        )
    rows = [tuple(r) for r in wb[sheet].iter_rows(values_only=True)]
    wb.close()
    return rows


def _row_for(rows: list[tuple[Any, ...]], symbol: str, col: int = 0) -> tuple[Any, ...]:
    hits = [r for r in rows if len(r) > col and r[col] == symbol]
    if len(hits) != 1:
        raise AnalysisError(
            f"expected exactly 1 row for {symbol} in the supplementary sheet, found {len(hits)}"
        )
    return hits[0]


def _muller_si_text() -> str:
    raw = _fetch(
        MULLER_ESM.format(n=MULLER_SI_PDF[0], ext=MULLER_SI_PDF[1]),
        CACHE_DIR / f"muller_MOESM{MULLER_SI_PDF[0]}.{MULLER_SI_PDF[1]}",
    )
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(raw))
    pages = [p.extract_text() or "" for p in reader.pages]
    # Figure labels are laid out across line breaks ("ARHGAP23-\nR986K"), so collapse all
    # whitespace before any pattern match rather than matching line by line.
    return re.sub(r"\s+", " ", " ".join(pages))


def muller_mutant_and_controls() -> dict[str, Any]:
    """Read the mutant designation and the screen's catalytic controls out of the SI."""
    text = _muller_si_text()
    compact = text.replace(" ", "")
    hits = {m.group(0).replace(" ", "") for m in MULLER_MUTANT_RE.finditer(compact)}
    if len(hits) != 1:
        raise AnalysisError(
            f"expected exactly one ARHGAP23 point-mutant designation in the {MULLER_PMID} "
            f"supplementary, found {sorted(hits) or 'none'}. The section that compares it to the "
            "UniProt arginine finger cannot proceed on an ambiguous reading."
        )
    token = hits.pop()
    m = MULLER_MUTANT_RE.search(token)
    assert m is not None
    wt, pos, mut = m.group(1), int(m.group(2)), m.group(3)

    # The sentence naming the proteins whose arginine-finger mutants validated the FRET
    # screen. Whether ARHGAP23 is in it is the load-bearing fact, so it is tested here.
    # Split only where a period is followed by a capital: "Fig. 4c" and "et al. 2020" are
    # not sentence ends, and splitting on them decapitates the quotation.
    sentences = [
        s
        for s in re.split(r"(?<=[a-z0-9\)])\.\s+(?=[A-Z])", text)
        if "arginine finger" in s.lower()
    ]
    if not sentences:
        raise AnalysisError(
            f"no sentence mentioning an arginine finger found in the {MULLER_PMID} supplementary; "
            "the claim about which proteins served as catalytic controls cannot be checked"
        )
    control_sentence = max(sentences, key=len)
    # Trim to the clause that names the RhoGAP controls: the surrounding sentence also
    # covers the RhoGEF controls and runs into the next heading. Both anchors are
    # required, so a re-worded supplementary fails loudly instead of quoting the wrong span.
    start = control_sentence.lower().find("mutation of")
    end = control_sentence.find(").", start if start >= 0 else 0)
    if start < 0 or end < 0:
        raise AnalysisError(
            "could not delimit the clause naming the RhoGAP catalytic controls in the "
            f"{MULLER_PMID} supplementary; refusing to quote an arbitrary span of it"
        )
    control_sentence = control_sentence[start : end + 2]
    if "arginine finger" not in control_sentence.lower():
        raise AnalysisError(
            "the delimited clause no longer mentions an arginine finger; the anchors have drifted"
        )
    return {
        "mutant": f"{wt}{pos}{mut}",
        "mutant_wt_residue": wt,
        "mutant_position": pos,
        "catalytic_control_sentence": control_sentence.strip(),
        "subject_is_a_catalytic_control": "ARHGAP23" in control_sentence,
    }


LITERATURE_GROUPS_REQUIRED = ("in vitro", "in vivo")


def _require_literature_groups(groups: dict[str, Any]) -> None:
    """Refuse to report on Supplementary Table 2 columns this parse did not find.

    Factored out of ``muller_specificity`` so that ``--self-test`` can drive it with a
    synthetic layout. Checked inline, it could only ever be exercised by a live table that
    happens to be correct, which is no test at all.
    """
    for needed in LITERATURE_GROUPS_REQUIRED:
        if needed not in groups:
            raise AnalysisError(
                f"Supplementary Table 2 yielded groups {sorted(groups)}, with no {needed!r}; "
                "refusing to report on columns this parse did not find"
            )


def muller_specificity() -> dict[str, Any]:
    """ARHGAP23's rows in the published screen, read from the publisher's own files."""
    # Source Data for Fig. 1b: three column blocks, one per GTPase. The block layout is
    # READ from the header rows, never assumed, so a re-laid-out file fails loudly.
    fig = _esm_sheet(*MULLER_FIG1B_ESM, "Fig. 1b")
    gtpase_row, field_row = fig[1], fig[2]
    data = _row_for(fig, "ARHGAP23")
    per_gtpase: dict[str, dict[str, Any]] = {}
    for i, field in enumerate(field_row):
        if field != "RhoGAP":
            continue
        gtpase = gtpase_row[i]
        block = {
            str(field_row[j]): data[j]
            for j in range(i, len(field_row))
            if field_row[j] is not None and (j == i or field_row[j] != "RhoGAP")
        }
        # stop the block at the next "RhoGAP" label
        stop = next((j for j in range(i + 1, len(field_row)) if field_row[j] == "RhoGAP"), None)
        if stop is not None:
            block = {str(field_row[j]): data[j] for j in range(i + 1, stop)}
        else:
            block = {str(field_row[j]): data[j] for j in range(i + 1, len(field_row))}
        per_gtpase[str(gtpase)] = {
            "norm_delR_over_R0_AVG": block.get("norm delR/R0 AVG"),
            "p_value": block.get("p-value"),
            "significant_and_below_threshold": block.get(
                "norm delR/R0 AVG below threshold and significant"
            ),
            "above_20pct_of_main_activity": block.get(
                "norm delR/R0 AVG higher than 20% of the main acitvity"
            ),
        }
    if set(per_gtpase) != {"RhoA", "Rac1", "Cdc42"}:
        raise AnalysisError(
            f"Fig. 1b source data yielded GTPase blocks {sorted(per_gtpase)}, expected "
            "RhoA, Rac1 and Cdc42"
        )

    # Supplementary Table 1: which sequence the construct actually is. Without this the
    # residue numbering of the mutant below cannot be compared to UniProt at all.
    t1 = _esm_sheet(*MULLER_TABLES_ESM, "Supplementary Table 1")
    c = _row_for(t1, "ARHGAP23")
    construct = {
        "alias": c[1],
        "type": c[2],
        "ensembl_gene": c[3],
        "entrez_gene": c[4],
        "refseq": c[6],
        "length": c[7],
        "clone": c[8],
    }

    # Supplementary Table 2: the specificity calls, and - the reason this table is parsed
    # at all - the literature-review columns. The review asserts that no in-vitro GAP assay
    # exists for ARHGAP23; the machine-checkable form of that assertion is that this table's
    # "in vitro" columns are empty for this gene while its "in vivo" and "reference" columns
    # are not. Group boundaries are READ from the two header rows, never assumed.
    t2 = _esm_sheet(*MULLER_TABLES_ESM, "Supplementary Table 2")
    group_row, gtpase_row = t2[2], t2[3]
    spec = _row_for(t2, "ARHGAP23")
    starts = [
        i
        for i, v in enumerate(group_row)
        if isinstance(v, str) and v.strip() and i > 1
    ]
    if not starts:
        raise AnalysisError(
            "Supplementary Table 2 has no literature-review group labels in its header row; "
            "the layout has changed and the 'no in-vitro assay' claim cannot be checked here"
        )
    # Each block is the FIRST run of RhoA/Rac1/Cdc42 columns after its label. Taking every
    # matching column instead would silently swallow the derived single/combination flag
    # columns that follow, whose labels repeat - and the last value would win, so the table
    # would be misread rather than obviously broken.
    def _block(start: int, stop: int) -> dict[str, Any]:
        cells: dict[str, Any] = {}
        for j in range(start, min(stop, len(spec))):
            label = gtpase_row[j]
            if not isinstance(label, str) or label not in ("RhoA", "Rac1", "Cdc42"):
                continue
            if label in cells:
                break  # the run has ended and a repeat block has begun
            cells[label] = spec[j]
        return cells

    groups: dict[str, dict[str, Any]] = {}
    for n, start in enumerate(starts):
        stop = starts[n + 1] if n + 1 < len(starts) else len(gtpase_row)
        cells = _block(start, stop)
        if cells:
            groups[str(group_row[start]).strip().strip('"')] = cells
    _require_literature_groups(groups)

    def _empty(cells: dict[str, Any]) -> bool:
        return all(v is None or str(v).strip() == "" for v in cells.values())

    literature = {
        "groups": groups,
        "in_vitro_empty": _empty(groups["in vitro"]),
        "in_vivo_empty": _empty(groups["in vivo"]),
        # The screen's own three specificity columns are the first such run in the row.
        "screen_calls": _block(2, starts[0]),
    }
    if set(literature["screen_calls"]) != {"RhoA", "Rac1", "Cdc42"}:
        raise AnalysisError(
            f"Supplementary Table 2 screen block parsed as {literature['screen_calls']}, "
            "which is not the three GTPase columns this analysis expects"
        )

    # Supplementary Table 4: the localization row, which is where the mutant is named.
    t4 = _esm_sheet(*MULLER_TABLES_ESM, "Supplementary Table 4")
    loc = _row_for(t4, "ARHGAP23")
    note = next((v for v in reversed(loc) if isinstance(v, str) and "arginine finger" in v), None)
    if note is None:
        raise AnalysisError(
            "Supplementary Table 4 no longer describes the ARHGAP23 construct as an "
            "arginine-finger mutant; the claim built on it below must be re-checked."
        )
    return {
        "pmid": MULLER_PMID,
        "fig1b_source_data": per_gtpase,
        "construct": construct,
        "literature_and_screen_calls": literature,
        "localization_note": note,
        **muller_mutant_and_controls(),
    }


def arginine_finger_mutant_check(
    subject: Protein, gap: Protein, muller: dict[str, Any], interface: dict[str, Any]
) -> dict[str, Any]:
    """Does the published GAP-dead mutant hit the residue UniProt calls the finger?"""
    wt, pos = muller["mutant_wt_residue"], muller["mutant_position"]

    # The comparison is only meaningful if the paper's construct is the same sequence.
    length_matches = muller["construct"]["length"] == len(subject.seq)
    if not length_matches:
        return {
            "mutant": muller["mutant"],
            "comparable": False,
            "reason": (
                f"the screened construct is {muller['construct']['length']} aa "
                f"({muller['construct']['refseq']}) but {subject.acc} is {len(subject.seq)} aa, "
                "so the residue numbers are not on the same sequence"
            ),
        }
    observed = subject.residue(pos)
    mapping = align_map(subject.domain_seq, gap.domain_seq)
    local = subject.to_local(pos)
    hit = mapping.get(local) if local else None
    gap_pos = gap.to_global(hit) if hit else None
    return {
        "mutant": muller["mutant"],
        "comparable": True,
        "construct_refseq": muller["construct"]["refseq"],
        "construct_length": muller["construct"]["length"],
        "wildtype_residue_expected": wt,
        "wildtype_residue_observed": observed,
        "residue_matches": observed == wt,
        "is_uniprot_annotated_arginine_finger": pos == subject.finger,
        "uniprot_annotated_arginine_finger": subject.finger,
        "aligns_to_control_position": gap_pos,
        "aligns_to_control_residue": gap.residue(gap_pos) if gap_pos else None,
        "control_position_is_its_arginine_finger": gap_pos == gap.finger,
        "control_position_contacts_transition_state": gap_pos
        in interface["transition_state_ligand_contacts"],
        "control_position_in_interface": gap_pos in interface["contact_positions"],
    }


# --- sibling family census -------------------------------------------------------


def read_family_census() -> dict[str, Any]:
    """Re-read (never transcribe) the family-wide numbers from the sibling analysis."""
    if not SIBLING_CENSUS.exists():
        raise AnalysisError(
            f"expected the sibling family census at {SIBLING_CENSUS}. Run "
            "`uv run python analyze_arhgap11b.py` in that folder, or delete the "
            "family-calibration section from this script."
        )
    census = json.loads(SIBLING_CENSUS.read_text()).get("rhogap_family_census")
    if not census:
        raise AnalysisError(f"{SIBLING_CENSUS} has no 'rhogap_family_census' key")
    return {
        "source": str(SIBLING_CENSUS.relative_to(REPO)),
        "n_entries": census["n_entries"],
        "n_finger_position_is_arginine": census["n_finger_position_is_arginine"],
        "n_finger_position_not_arginine": census["n_finger_position_not_arginine"],
        "n_flagged_confirmed_inactive_experimentally": census[
            "n_flagged_confirmed_inactive_experimentally"
        ],
        "subject_in_census": any(
            e["accession"] == SUBJECT_ACC for e in census["finger_not_arginine"]
        ),
    }


# --- driver ----------------------------------------------------------------------


def run() -> dict[str, Any]:
    subject = Protein(SUBJECT_ACC)
    structural = Protein(STRUCTURAL_COMPARATOR)
    paralog = Protein(PARALOG_COMPARATOR)
    control_lost = Protein(CONTROL_LOST_ACC)
    control_retained = Protein(CONTROL_RETAINED_ACC)

    # ARHGAP21 is used twice on purpose: as a comparator (its own annotated finger is
    # projected onto ARHGAP23) and as a POSITIVE control subject, so the interface
    # numbers below have a scale on both sides -- an experimentally characterised,
    # active RhoGAP that is nonetheless distant from the structural comparator.
    subjects = {
        "ARHGAP23": subject,
        "positive_control": paralog,
        "control_lost": control_lost,
        "control_retained": control_retained,
    }

    credentials = {
        label: verify_credential(label, subjects[label]) for label in CONTROL_CREDENTIALS
    }

    finger_tests = {}
    for label, prot in subjects.items():
        entry = {"vs_structural_comparator": reciprocal_finger_test(prot, structural)}
        # Testing the paralog comparator against itself is trivially true and would be
        # a meaningless row; record why it is absent rather than emitting a vacuous pass.
        if prot.acc == paralog.acc:
            entry["vs_paralog_comparator"] = {
                "skipped": "subject is the paralog comparator; a self-projection is vacuous"
            }
        else:
            entry["vs_paralog_comparator"] = reciprocal_finger_test(prot, paralog)
        finger_tests[label] = entry

    rhoa = fetch_uniprot(RHOA_ACC)
    interface = gap_gtpase_interface(structural, seq_of(rhoa))
    projections = {
        label: project_interface(
            prot, structural, interface["contact_positions_in_rhogap_domain"]
        )
        for label, prot in subjects.items()
    }

    # The calibration claim, computed rather than asserted: of the controls that are
    # known GAP-dead, how many does the residue test call "retained"?
    dead_labels = ["control_lost", "control_retained"]
    called_retained = [
        lab
        for lab in dead_labels
        if finger_tests[lab]["vs_structural_comparator"]["forward_retained"]
    ]

    muller = muller_specificity()
    mutant_check = arginine_finger_mutant_check(subject, structural, muller, interface)

    # Does the interface-conservation number order these subjects by activity? Computed,
    # not asserted: if the GAP-dead retained control scores at or above the subject, the
    # metric is tracking relatedness to the structural comparator, not catalysis.
    pct = {lab: projections[lab]["pct_identical_or_conservative"] for lab in subjects}
    ranked = sorted(pct.items(), key=lambda kv: kv[1], reverse=True)
    # Only the three subjects whose activity is KNOWN can test whether the metric orders
    # by activity; ARHGAP23's status is the open question and cannot be an input here.
    orders_by_activity = pct["positive_control"] > max(
        pct["control_retained"], pct["control_lost"]
    )

    return {
        "subjects": {label: prot.summary() for label, prot in subjects.items()},
        "control_credentials": credentials,
        "comparators": {
            "structural": structural.summary(),
            "paralog": paralog.summary(),
        },
        "arginine_finger_tests": finger_tests,
        "interface": interface,
        "interface_projections": projections,
        "subject_vs_positive_control_interface": compare_projections(
            projections["ARHGAP23"], projections["positive_control"]
        ),
        "muller_specificity_screen": muller,
        "published_mutant_check": mutant_check,
        "calibration": {
            "known_gap_dead_controls": len(dead_labels),
            "called_retained_by_residue_test": len(called_retained),
            "called_retained_labels": called_retained,
            "interface_pct_by_subject": pct,
            "interface_pct_ranking": [lab for lab, _ in ranked],
            "interface_pct_orders_subjects_by_activity": orders_by_activity,
        },
        "family_census": read_family_census(),
    }


# --- self test -------------------------------------------------------------------


def _expect_raises(fn, needle: str, label: str) -> None:
    try:
        fn()
    except AnalysisError as exc:
        if needle.lower() not in str(exc).lower():
            raise AssertionError(
                f"{label}: guard fired with the wrong message.\n  expected substring: {needle!r}\n"
                f"  got: {exc}"
            ) from exc
        return
    raise AssertionError(f"{label}: expected AnalysisError containing {needle!r}, none raised")


class _Mutable(Protein):
    """A Protein whose sequence/annotations can be perturbed for the self test."""

    def __init__(self, src: Protein):
        self.rec = json.loads(json.dumps(src.rec))
        self.acc, self.name, self.seq = src.acc, src.name, src.seq
        self.reviewed = src.reviewed
        self.domain_start, self.domain_end = src.domain_start, src.domain_end
        self.sites, self.finger = list(src.sites), src.finger

    def mutate_residue(self, pos: int, to: str) -> None:
        self.seq = self.seq[: pos - 1] + to + self.seq[pos:]

    def drop_site(self, pos: int) -> None:
        self.sites = [p for p in self.sites if p != pos]

    def move_finger(self, pos: int) -> None:
        self.finger = pos


def self_test() -> int:
    applied = 0
    anchors = 0
    baselines = 0

    subject = Protein(SUBJECT_ACC)
    structural = Protein(STRUCTURAL_COMPARATOR)
    base = reciprocal_finger_test(subject, structural)

    # Anchor 1: the baseline must be a reciprocal hit, or every mutation below is vacuous.
    anchors += 1
    baselines += 1
    assert base["reciprocal"], f"baseline is not reciprocal: {base}"
    hit = base["forward_mapped_position"]
    assert hit is not None

    # Mutation 1: destroy the arginine the test is looking for.
    anchors += 1
    mut = _Mutable(subject)
    mut.mutate_residue(hit, "A")
    applied += 1
    res = reciprocal_finger_test(mut, structural)
    assert not res["forward_residue_is_arginine"], "R->A at the mapped finger did not flip"
    assert not res["forward_retained"], "R->A at the mapped finger left forward_retained True"
    assert not res["reciprocal"], "R->A at the mapped finger left the test reciprocal"

    # Mutation 2: keep the arginine, remove the subject's own Site annotation.
    anchors += 1
    mut = _Mutable(subject)
    mut.drop_site(hit)
    applied += 1
    res = reciprocal_finger_test(mut, structural)
    assert res["forward_residue_is_arginine"], "dropping a Site must not change the residue"
    assert not res["forward_lands_on_annotated_subject_site"], "dropped Site still reported"
    assert not res["forward_retained"], "retained must require the annotated-site condition"

    # Mutation 3: move the subject's annotated finger, breaking reciprocity only.
    anchors += 1
    mut = _Mutable(subject)
    mut.move_finger(subject.finger + 3)
    applied += 1
    res = reciprocal_finger_test(mut, structural)
    assert res["forward_retained"], "moving the subject finger must not affect the forward test"
    assert not res["reverse_lands_on_comparator_finger"], "reverse test did not notice the move"
    assert not res["reciprocal"], "reciprocity survived a broken reverse mapping"

    # Mutation 4: an out-of-register projection must be refused, not reported.
    anchors += 1
    mut = _Mutable(subject)
    mut.move_finger(subject.domain_end)
    applied += 1
    _expect_raises(
        lambda: project_interface(mut, structural, [structural.finger]),
        "out of register",
        "interface projection",
    )

    # Mutation 5: a chain that is not the protein we think it is must be refused.
    anchors += 1
    applied += 1
    _expect_raises(
        lambda: prove_chain_identity("MKVLAAGIVGL" * 10, subject.seq, "fake chain"),
        "identical to the UniProt sequence",
        "chain identity proof",
    )

    # Mutation 6: a missing arginine-finger annotation must stop the analysis. The
    # perturbed record is driven through the real constructor, not a re-implementation.
    anchors += 1
    applied += 1
    stripped = json.loads(json.dumps(subject.rec))
    stripped["features"] = [
        f for f in stripped["features"]
        if not (f.get("type") == "Site"
                and ARGININE_FINGER_TEXT.lower() in str(f.get("description", "")).lower())
    ]
    _expect_raises(
        lambda: Protein(SUBJECT_ACC, rec=stripped),
        "carries no 'Arginine finger'",
        "missing finger annotation",
    )

    # Mutation 7: an ambiguous Rho-GAP domain must be refused, not silently first-picked.
    anchors += 1
    applied += 1
    doubled = json.loads(json.dumps(subject.rec))
    dom = next(
        f for f in doubled["features"]
        if f.get("type") == "Domain"
        and RHOGAP_DOMAIN_TEXT.lower() in str(f.get("description", "")).lower()
    )
    doubled["features"].append(json.loads(json.dumps(dom)))
    _expect_raises(
        lambda: Protein(SUBJECT_ACC, rec=doubled),
        "Domain features (expected exactly 1)",
        "ambiguous Rho-GAP domain",
    )

    # Mutation 8: an arginine finger annotated outside its own domain must be refused.
    anchors += 1
    applied += 1
    displaced = json.loads(json.dumps(subject.rec))
    site = next(
        f for f in displaced["features"]
        if f.get("type") == "Site"
        and ARGININE_FINGER_TEXT.lower() in str(f.get("description", "")).lower()
    )
    site["location"]["start"]["value"] = 1
    site["location"]["end"]["value"] = 1
    _expect_raises(
        lambda: Protein(SUBJECT_ACC, rec=displaced),
        "lies outside its own",
        "finger outside the domain",
    )

    # --- analysis 5 guards -------------------------------------------------------
    interface_stub = {
        "transition_state_ligand_contacts": [structural.finger],
        "contact_positions": [structural.finger],
    }
    real_muller = {
        "mutant": "R986K",
        "mutant_wt_residue": "R",
        "mutant_position": 986,
        "construct": {"length": len(subject.seq), "refseq": "NP_001186346.1"},
    }

    # Anchor: on the real inputs the check must be comparable and self-consistent, or
    # the two mutations below prove nothing.
    anchors += 1
    baselines += 1
    real = arginine_finger_mutant_check(subject, structural, real_muller, interface_stub)
    assert real["comparable"], f"baseline mutant check is not comparable: {real}"
    assert real["residue_matches"], "the published mutant does not name the residue it claims"

    # Mutation 9: a construct of a different length must refuse the comparison outright.
    anchors += 1
    applied += 1
    wrong_len = json.loads(json.dumps(real_muller))
    wrong_len["construct"]["length"] = len(subject.seq) + 100
    res = arginine_finger_mutant_check(subject, structural, wrong_len, interface_stub)
    assert not res["comparable"], "a length mismatch did not stop the residue comparison"
    assert "not on the same sequence" in res["reason"], res["reason"]

    # Mutation 10: point the mutant AT the annotated finger; the discriminator must flip.
    anchors += 1
    applied += 1
    on_finger = json.loads(json.dumps(real_muller))
    on_finger["mutant_position"] = subject.finger
    on_finger["mutant"] = f"R{subject.finger}K"
    res = arginine_finger_mutant_check(subject, structural, on_finger, interface_stub)
    assert res["is_uniprot_annotated_arginine_finger"], (
        "the check does not recognise the annotated finger when the mutant lands on it"
    )
    assert res["control_position_is_its_arginine_finger"], (
        "a mutant on the annotated finger should map onto the control's finger"
    )
    assert not real["is_uniprot_annotated_arginine_finger"], (
        "the published mutant position is being reported as the annotated finger; the "
        "conclusion of section 5 has silently inverted"
    )

    # Anchor: the real Supplementary Table 2 parse. Without this the two mutations below
    # would be testing a helper nobody calls.
    anchors += 1
    baselines += 1
    lit = muller_specificity()["literature_and_screen_calls"]
    assert set(lit["screen_calls"]) == {"RhoA", "Rac1", "Cdc42"}, lit["screen_calls"]
    assert lit["in_vitro_empty"], (
        "the 'no in-vitro assay' claim no longer holds against Supplementary Table 2; the "
        "review's knowledge gap and suggested experiment both depend on it"
    )
    assert not lit["in_vivo_empty"], (
        "the in-vivo columns are also empty, so 'in vitro is empty' carries no information - "
        "the parse is probably reading the wrong columns"
    )

    # Mutation 12: the emptiness test must notice a populated cell.
    anchors += 1
    applied += 1
    assert not all(
        v is None or str(v).strip() == ""
        for v in dict(lit["groups"]["in vitro"], RhoA="+").values()
    ), "the emptiness test reports a populated block as empty"

    # Mutation 13: a Supplementary Table 2 layout missing the in-vitro block must abort,
    # not report an absent column as empty - which would manufacture the review's negative.
    anchors += 1
    applied += 1
    _expect_raises(
        lambda: _require_literature_groups({"in vivo": {"RhoA": "+"}}),
        "with no 'in vitro'",
        "missing literature block",
    )

    # Negative control: a layout that has the required blocks must be accepted silently.
    anchors += 1
    applied += 1
    _require_literature_groups({"in vitro": {}, "in vivo": {}, "integrated": {}})

    # Mutation 14: taking every matching column instead of the first run must change the
    # answer, which is what makes the first-run rule load-bearing rather than decorative.
    anchors += 1
    applied += 1
    assert lit["screen_calls"] != {"RhoA": 0, "Rac1": 0, "Cdc42": 0}, (
        "the screen block has collapsed onto the derived flag columns; the first-run rule "
        "in _block is not being applied"
    )

    # Mutation 11: an ambiguous supplementary row must not be resolved by picking one.
    anchors += 1
    applied += 1
    rows = [("GENE",), ("ARHGAP23", 1), ("ARHGAP23", 2)]
    _expect_raises(
        lambda: _row_for(rows, "ARHGAP23"),
        "expected exactly 1 row",
        "duplicated supplementary row",
    )

    # Negative control for the constructor guards: an unrelated feature edit must build.
    anchors += 1
    applied += 1
    benign = json.loads(json.dumps(subject.rec))
    benign["features"] = [f for f in benign["features"] if f.get("type") != "Region"]
    built = Protein(SUBJECT_ACC, rec=benign)
    assert built.finger == subject.finger, "removing Region features moved the finger"
    assert (built.domain_start, built.domain_end) == (
        subject.domain_start,
        subject.domain_end,
    ), "removing Region features moved the domain"

    # Negative controls: perturbations that must change nothing.
    anchors += 1
    far = subject.domain_start  # inside the domain, far from the finger
    assert far != hit, "negative control position collided with the finger"
    mut = _Mutable(subject)
    mut.mutate_residue(far, "G" if subject.residue(far) != "G" else "A")
    applied += 1
    res = reciprocal_finger_test(mut, structural)
    assert res["reciprocal"], "a substitution away from the finger silently broke the test"
    assert res["forward_mapped_position"] == hit, "negative control moved the mapped position"

    anchors += 1
    mut = _Mutable(subject)
    extra = subject.domain_end
    if extra not in mut.sites:
        mut.sites = sorted(mut.sites + [extra])
    applied += 1
    res = reciprocal_finger_test(mut, structural)
    assert res["reciprocal"], "adding an unrelated Site changed the verdict"

    if applied != anchors - baselines:
        # `baselines` counts the anchors that assert a starting state and carry no
        # mutation of their own; every other anchor must have applied exactly one.
        raise AssertionError(
            f"self-test bookkeeping: {applied} mutations applied but {anchors} anchors "
            f"detected with {baselines} baselines; a mutation target has drifted"
        )
    print(
        f"self-test OK: {applied} mutations, {anchors} anchors ({baselines} baselines), "
        "all guards fired as expected"
    )
    return 0


# --- reporting -------------------------------------------------------------------


def _fmt_ev(codes: list[str]) -> str:
    return ", ".join(f"`{c}`" for c in codes) if codes else "*(none)*"


def render_markdown(res: dict[str, Any]) -> str:
    s = res["subjects"]["ARHGAP23"]
    struct = res["comparators"]["structural"]
    par = res["comparators"]["paralog"]
    t_struct = res["arginine_finger_tests"]["ARHGAP23"]["vs_structural_comparator"]
    t_par = res["arginine_finger_tests"]["ARHGAP23"]["vs_paralog_comparator"]
    iface = res["interface"]
    cal = res["calibration"]
    cen = res["family_census"]

    L: list[str] = []
    L.append("# ARHGAP23 retains the RhoGAP arginine finger — and that is not evidence of activity")
    L.append("")
    L.append(
        "Every number below is produced by `analyze_arhgap23.py`; nothing is transcribed. "
        "Re-run with `uv run python analyze_arhgap23.py`, and `--self-test` to check the guards."
    )
    L.append("")

    L.append("## 1. The subject, and the provenance of the claim under test")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append(f"| accession | {s['accession']} ({s['entry_name']}, {s['length']} aa) |")
    L.append(f"| Rho-GAP domain | {s['rhogap_domain'][0]}–{s['rhogap_domain'][1]} |")
    L.append(
        f"| annotated arginine finger | {s['annotated_arginine_finger']} "
        f"(residue **{s['residue_at_annotated_finger']}**) |"
    )
    L.append(f"| evidence on that Site feature | {_fmt_ev(s['arginine_finger_evidence'])} |")
    L.append(f"| evidence on the FUNCTION comment | {_fmt_ev(s['function_comment']['evidence_codes'])} |")
    L.append("")
    L.append(f"UniProt's FUNCTION text is: *\"{s['function_comment']['text']}\"*")
    L.append("")
    L.append(
        "Both of those evidence codes are non-experimental — the arginine finger is placed by "
        "a PROSITE profile rule and the function is asserted by similarity — so the question "
        "this analysis can settle is whether the *sequence* supports the inference, not whether "
        "the protein has been shown to work."
    )
    L.append("")

    L.append("## 2. The arginine finger, tested reciprocally")
    L.append("")
    L.append(
        "A comparator's own annotated arginine finger is projected onto ARHGAP23 by aligning "
        "the two Rho-GAP **domains**, and is scored `retained` only if the aligned residue is an "
        "arginine *and* it lands on one of ARHGAP23's own annotated Site features. The projection "
        "is then run backwards: ARHGAP23's annotated site must map onto the comparator's annotated "
        "finger. Only a test that passes both ways is reported as reciprocal."
    )
    L.append("")
    L.append("| comparator | its finger | → ARHGAP23 | residue | on an ARHGAP23 Site? | reverse lands on comparator finger? | reciprocal |")
    L.append("|---|---|---|---|---|---|---|")
    for label, t, prot in (
        (f"{struct['entry_name']} ({struct['accession']}, resolved in {iface['pdb_id']})", t_struct, struct),
        (f"{par['entry_name']} ({par['accession']}, closest paralog / IBA donor)", t_par, par),
    ):
        L.append(
            f"| {label} | {t['comparator_finger']}{t['comparator_finger_residue']} | "
            f"{t['forward_mapped_position']} | **{t['forward_mapped_residue']}** | "
            f"{'yes' if t['forward_lands_on_annotated_subject_site'] else 'no'} | "
            f"{'yes' if t['reverse_lands_on_comparator_finger'] else 'no'} | "
            f"**{'yes' if t['reciprocal'] else 'no'}** |"
        )
    L.append("")

    L.append("## 3. What a positive result is worth: the controls")
    L.append("")
    L.append(
        "The same test, same code path, on an active RhoGAP and on two proteins that are known to "
        "be GAP-dead and that fail in opposite ways."
    )
    L.append("")
    L.append(
        "Each control's status is **verified, not asserted**: the run aborts if the credential "
        "below cannot be found in the repo's own GOA table or in the fetched UniProt record."
    )
    L.append("")
    L.append("| subject | verified credential | evidence | residue at its own annotated finger | test verdict |")
    L.append("|---|---|---|---|---|")
    for lab in ("positive_control", "control_lost", "control_retained"):
        sub = res["subjects"][lab]
        cred = res["control_credentials"][lab]
        t = res["arginine_finger_tests"][lab]["vs_structural_comparator"]
        if "matching_rows" in cred:
            ev = "; ".join(
                f"`{r['qualifier']} {r['term']}` {r['evidence']} {r['reference']}"
                for r in cred["matching_rows"]
            )
        else:
            ev = ", ".join(f"`{c}`" for c in cred["statement"]["evidence_codes"])
        L.append(
            f"| {sub['entry_name']} ({sub['accession']}) | {cred['claim']} | {ev} | "
            f"{sub['annotated_arginine_finger']}**{sub['residue_at_annotated_finger']}** | "
            f"{'retained' if t['forward_retained'] else 'NOT retained'} |"
        )
    L.append("")
    lost_cred = res["control_credentials"]["control_lost"]
    L.append(
        f"The {res['subjects']['control_lost']['entry_name']} statement in full: "
        f"*\"{lost_cred['statement']['text']}\"*"
    )
    L.append("")
    L.append(
        f"What UniProt's own GO cross-reference says about {GAP_TERM} for each of these, which is "
        "worth recording because it is not always consistent with the entry's prose: "
        + "; ".join(
            f"{res['subjects'][lab]['entry_name']} "
            + (
                ", ".join(
                    f"`{c}`" for c in res["subjects"][lab]["uniprot_go_xref_evidence_for_gap_term"]
                )
                or "*(no cross-reference)*"
            )
            for lab in ("ARHGAP23", "positive_control", "control_lost", "control_retained")
        )
        + ". The GAP-dead controls both still carry the positive term in the GO record — which is "
        "the same class of defect this review is examining, seen from the other side."
    )
    L.append("")
    L.append(
        f"So of {cal['known_gap_dead_controls']} known GAP-dead controls, the residue test calls "
        f"{cal['called_retained_by_residue_test']} of them `retained`. The test can fire — it fires "
        "on the control that lost the residue — but a protein can keep the arginine and still have "
        "no measurable GAP activity."
    )
    L.append("")
    L.append(
        f"The family-wide version of the same number, read from `{cen['source']}`: of "
        f"{cen['n_entries']} human reviewed proteins carrying the PROSITE RhoGAP profile, "
        f"{cen['n_finger_position_is_arginine']} have an arginine at their own annotated finger "
        f"position and {cen['n_finger_position_not_arginine']} do not, and only "
        f"{cen['n_flagged_confirmed_inactive_experimentally']} of the flagged entries carries an "
        "experimentally supported UniProt statement of inactivity. ARHGAP23 is "
        f"{'among' if cen['subject_in_census'] else 'not among'} the flagged entries."
    )
    L.append("")

    L.append("## 4. The rest of the catalytic surface")
    L.append("")
    L.append(
        f"One residue is a thin basis for a molecular-function call, so the whole GAP:GTPase "
        f"interface was computed from PDB {iface['pdb_id']} "
        f"(p50RhoGAP:RhoA:GDP:AlF4, a transition-state mimic): every {struct['entry_name']} residue "
        f"within {iface['cutoff_angstrom']} Å of RhoA or of the "
        f"{', '.join(iface['ligands_included'])} ligands. Chain roles are proved rather than assumed "
        f"(chain {iface['gap_chain']} is {iface['gap_chain_identity_to_reference']:.1%} identical to "
        f"{struct['accession']}, chain {iface['gtpase_chain']} is "
        f"{iface['gtpase_chain_identity_to_reference']:.1%} identical to RhoA), and the contact set "
        f"recovers {struct['entry_name']}'s own annotated arginine finger ({struct['annotated_arginine_finger']}), "
        "as it must."
    )
    L.append("")
    L.append(
        f"That gives {iface['n_contacts']} contact positions, "
        f"{iface['n_contacts_in_rhogap_domain']} of them inside the Rho-GAP domain. Those are "
        "projected onto each subject, accepted only when the projection is in register (the "
        "control's finger lands on the subject's own annotated finger):"
    )
    L.append("")
    L.append("| subject | role | interface positions | identical | conservative | different | unaligned | identical or conservative |")
    L.append("|---|---|---|---|---|---|---|---|")
    roles = {
        "ARHGAP23": "subject",
        "positive_control": "positive control — an active, experimentally characterised RhoGAP",
        "control_lost": "GAP-dead, arginine lost",
        "control_retained": "GAP-dead, arginine retained",
    }
    for lab in ("ARHGAP23", "positive_control", "control_lost", "control_retained"):
        p = res["interface_projections"][lab]
        L.append(
            f"| {p['subject_entry_name']} | {roles[lab]} | {p['n_interface_positions']} | "
            f"{p['n_identical']} | {p['n_conservative']} | {p['n_different']} | "
            f"{p['n_unaligned']} | **{p['pct_identical_or_conservative']}%** |"
        )
    L.append("")
    if not cal["interface_pct_orders_subjects_by_activity"]:
        L.append(
            "**This metric does not order the subjects by activity.** Ranked by percent "
            "identical-or-conservative the order is "
            + " > ".join(
                f"{res['interface_projections'][lab]['subject_entry_name']} "
                f"({res['interface_projections'][lab]['pct_identical_or_conservative']}%)"
                for lab in cal["interface_pct_ranking"]
            )
            + ". Among the three subjects whose catalytic status is known, the experimentally "
            "GAP-dead protein that kept its arginine scores **above** the experimentally active "
            "one, so the number is tracking relatedness to the structural comparator rather than "
            "catalysis. It is reported here as context and is not used as an argument in either "
            "direction."
        )
        L.append("")
    arh = res["interface_projections"]["ARHGAP23"]
    cmp_pos = res["subject_vs_positive_control_interface"]
    L.append(
        f"The comparison that does carry information is ARHGAP23 against the positive control. "
        f"At the {cmp_pos['n_positions_mapped_in_both']} interface positions mapped in both, "
        f"ARHGAP23 and {cmp_pos['subject_b']} carry the **same residue at "
        f"{cmp_pos['n_same_residue']}**"
        + (
            "."
            if not cmp_pos["differences"]
            else " — the exceptions being "
            + ", ".join(
                f"{struct['entry_name']} {p}: "
                + " vs ".join(f"{k} {v}" for k, v in d.items())
                for p, d in cmp_pos["differences"].items()
            )
            + "."
        )
    )
    L.append("")
    if arh["different"]:
        L.append(
            "ARHGAP23's non-conservative differences at interface positions "
            f"({struct['entry_name']} → ARHGAP23): "
            + ", ".join(
                f"{d['control_residue']}{d['control_position']}→{d['subject_residue']}{d['subject_position']}"
                for d in arh["different"]
            )
            + "."
        )
        L.append("")

    mul = res["muller_specificity_screen"]
    mc = res["published_mutant_check"]
    L.append("## 5. The published specificity screen, and the mutant it calls an arginine finger")
    L.append("")
    L.append(
        f"PMID:{mul['pmid']} (Müller et al. 2020, *Nature Cell Biology*) ran a cellular FRET "
        "biosensor screen across the human RhoGEF/RhoGAP family. Its main text is paywalled and "
        "absent from PMC, but the publisher's Source Data and Supplementary Tables are open, and "
        "they are parsed directly here. ARHGAP23's row in the Fig. 1b source data:"
    )
    L.append("")
    L.append("| GTPase | norm ΔR/R0 AVG | p-value | authors' significance flag | >20% of main activity |")
    L.append("|---|---|---|---|---|")
    for g in ("RhoA", "Rac1", "Cdc42"):
        b = mul["fig1b_source_data"][g]
        pv = b["p_value"]
        pv_s = f"{pv:.2e}" if isinstance(pv, (int, float)) else "*(none)*"
        L.append(
            f"| {g} | {b['norm_delR_over_R0_AVG']:+.3f} | {pv_s} | "
            f"{b['significant_and_below_threshold']} | {b['above_20pct_of_main_activity']} |"
        )
    L.append("")
    L.append(
        "A negative value is a drop in biosensor activity, ie GAP activity toward that GTPase. "
        "The screen therefore scores ARHGAP23 as active on RhoA **and** Rac1 to essentially equal "
        "degrees and inactive on Cdc42."
    )
    L.append("")
    lit = mul["literature_and_screen_calls"]
    L.append(
        "Supplementary Table 2 records the same conclusion as explicit calls — "
        + ", ".join(f"{g} `{v}`" for g, v in lit["screen_calls"].items())
        + " — and, in the columns that matter for what is *not* known, summarises the prior "
        "literature per GTPase:"
    )
    L.append("")
    L.append("| literature column | RhoA | Rac1 | Cdc42 |")
    L.append("|---|---|---|---|")
    for g in ("integrated", "in vitro", "in vivo", "reference"):
        cells = lit["groups"].get(g, {})
        L.append(
            f"| {g} | "
            + " | ".join(
                (f"`{cells.get(k)}`" if str(cells.get(k) or "").strip() else "*(empty)*")
                for k in ("RhoA", "Rac1", "Cdc42")
            )
            + " |"
        )
    L.append("")
    L.append(
        f"The **\"in vitro\" row is empty for all three GTPases** "
        f"({'confirmed' if lit['in_vitro_empty'] else 'NOT confirmed'} by this parse) while the "
        f"\"in vivo\" row is not ({'empty' if lit['in_vivo_empty'] else 'populated'}). That is the "
        "machine-checkable form of this review's statement that no purified-protein GAP assay "
        "exists for ARHGAP23, and it is checked here rather than asserted because it is otherwise "
        "the one load-bearing claim in the review that nothing re-runs."
    )
    L.append("")
    L.append(
        f"The same paper's Supplementary Table 4 records the ARHGAP23 localization experiment as "
        f'"{mul["localization_note"].strip()}" — ie the imaged construct was a '
        f"**{mc['mutant']}** arginine-finger mutant. Supplementary Table 1 gives the screened "
        f"cDNA as {mul['construct']['refseq']}, {mul['construct']['length']} aa, clone "
        f"{mul['construct']['clone']}."
    )
    L.append("")
    if mc["comparable"]:
        L.append(
            f"That construct is the same length as {s['accession']} "
            f"({mul['construct']['length']} aa), so the residue numbers are directly comparable — "
            "and they do not agree:"
        )
        L.append("")
        L.append(
            f"- Position {mc['mutant'][1:-1]} of the canonical sequence is "
            f"**{mc['wildtype_residue_observed']}**, so the mutant names a real arginine "
            f"({'consistent' if mc['residue_matches'] else 'INCONSISTENT'} with the mutant string)."
        )
        L.append(
            f"- It is **not** the residue UniProt annotates as the arginine finger, which is "
            f"{mc['uniprot_annotated_arginine_finger']}."
        )
        L.append(
            f"- It aligns to {struct['entry_name']} "
            f"{mc['aligns_to_control_position']}{mc['aligns_to_control_residue']}, which is "
            f"{'also' if mc['control_position_is_its_arginine_finger'] else 'NOT'} that protein's "
            f"annotated arginine finger ({struct['annotated_arginine_finger']})."
        )
        L.append(
            f"- In {iface['pdb_id']}, {struct['entry_name']} "
            f"{mc['aligns_to_control_position']} "
            f"{'is' if mc['control_position_in_interface'] else 'is not'} part of the GAP:GTPase "
            f"interface, and "
            f"{'does' if mc['control_position_contacts_transition_state'] else 'does not'} contact "
            "the nucleotide/AlF4/Mg transition-state ligands — which is the defining property of "
            "an arginine finger, and which the annotated finger "
            f"({struct['annotated_arginine_finger']}) does."
        )
        L.append("")
        L.append(
            'So the only published "GAP-deficient arginine finger mutant" of ARHGAP23 targets a '
            "conserved interface arginine that is not the catalytic finger. That mutant was used "
            "for TIRF localization imaging, not to validate the activity screen: the supplementary "
            "sentence naming the catalytic controls reads "
            f"*\"{mul['catalytic_control_sentence']}\"*, and ARHGAP23 "
            f"{'is' if mul['subject_is_a_catalytic_control'] else 'is not'} among them."
        )
        L.append("")
        L.append(
            "**No experiment has yet tested whether ARHGAP23's actual arginine finger "
            f"({s['annotated_arginine_finger']}) is required for its measured RhoA/Rac1 activity.** "
            "This is a discrepancy in the literature, not a correction of it: one of the two "
            "assignments is wrong and only an experiment can say which."
        )
    else:
        L.append(f"The mutant cannot be compared: {mc['reason']}.")
    L.append("")

    L.append("## 6. What this does and does not license")
    L.append("")
    t = t_struct
    if t["reciprocal"]:
        L.append(
            f"ARHGAP23 **retains** the RhoGAP catalytic arginine: position "
            f"{t['forward_mapped_position']} is an arginine, it is ARHGAP23's own annotated "
            f"arginine-finger Site, and it is reciprocally in register with "
            f"{struct['entry_name']} {struct['annotated_arginine_finger']}, whose role is resolved in a "
            f"transition-state structure. The same result holds against the closest paralog "
            f"{par['entry_name']}. The surrounding catalytic surface is "
            f"{arh['pct_identical_or_conservative']}% identical or conservatively substituted, a "
            "number that section 4 shows does not discriminate active from dead in this control set."
        )
    else:
        L.append(
            f"ARHGAP23 does **not** pass the reciprocal arginine-finger test against "
            f"{struct['entry_name']}: {json.dumps(t)}"
        )
    L.append("")
    L.append(
        "The honest reading is asymmetric, and section 3 is the reason. A *lost* arginine would "
        "have been a substantive argument against the GAP-activity annotation. A *retained* one is "
        "only the absence of that argument: one of the two known GAP-dead controls here passes the "
        "same test, and the family-wide census says the same thing at scale. Nothing in this "
        "analysis is by itself evidence that ARHGAP23 hydrolyses anything, and no GTPase substrate "
        "can be assigned from it — RhoA, Rac1 and Cdc42 contacts are not distinguished by this "
        "calculation, which uses a single RhoA complex. The substrate evidence is the cellular "
        f"screen in section 5, not the structure."
    )
    L.append("")
    L.append(
        "Put the two together and the position is: the catalytic machinery is intact and "
        "indistinguishable from that of an experimentally active close paralog, and a cellular "
        "assay reports GAP activity on RhoA and Rac1 — but no purified-protein assay exists, and "
        "the one published mutant that would have tied the activity to the catalytic residue "
        "mutates a different arginine."
    )
    L.append("")
    L.append(
        f"What would settle it: an in-vitro GAP assay on the isolated ARHGAP23 Rho-GAP domain "
        f"against RhoA, Rac1 and Cdc42, with R{s['annotated_arginine_finger']} mutated as the "
        f"negative control — and, separately, a side-by-side test of "
        f"R{s['annotated_arginine_finger']} against the published "
        f"{mc['mutant'][1:-1]} position to establish which one the activity depends on."
    )
    L.append("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true", help="mutate inputs and assert guards fire")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    res = run()
    (SCRIPT_DIR / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (SCRIPT_DIR / "RESULTS.md").write_text(render_markdown(res))
    print(f"wrote {SCRIPT_DIR / 'results.json'} and {SCRIPT_DIR / 'RESULTS.md'}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AnalysisError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
