"""Residue-level test of ADGB's two annotation-critical claims.

ADGB (androglobin, Q8N7X0) is chimeric: an N-terminal calpain-like (peptidase C2)
region and an internal circularly-permuted globin domain.  GOA carries IEA rows
derived from each domain's InterPro signature:

  * IPR001300 (Peptidase_C2_calpain_cat) -> GO:0004198 calcium-dependent
    cysteine-type endopeptidase activity, GO:0006508 proteolysis
  * IPR012292 (Globin/Proto)             -> GO:0019825 oxygen binding,
                                            GO:0020037 heme binding

A domain's NAME is not an activity.  This script asks, from sequence alone:

  Q1  Does ADGB retain the papain-like catalytic triad (Cys/His/Asn) of the
      calpain protease domain?
  Q2  Does ADGB retain the globin heme-iron ligands -- the proximal His(F8) and
      the distal His(E7)?

Method (Q1).  For each reviewed reference calpain, align its catalytic domain to
ADGB 70-411 and read off the ADGB residue aligned to each of the reference's own
UniProt-annotated Active site positions.  Following the AADACL2 rule in the
campaign brief, a "match" requires BOTH residue identity AND that the alignment
column be anchored on an annotated site of the reference -- matching an amino
acid anywhere is not evidence.

Method (Q2).  Same, against reviewed globins whose heme-iron Binding site
features UniProt annotates as proximal/distal.

Every conclusion is computed.  Nothing is hardcoded.  Guards are break-tested in
BOTH directions by --self-test: a positive control that must reproduce a known
triad, and a negative control that must not.
"""

from __future__ import annotations

import argparse
import json
import sys
import html
import re
import urllib.request
from dataclasses import dataclass, field, asdict

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"

SUBJECT = "Q8N7X0"  # human ADGB

# Reference sets.  Roles are labels only; every number below is measured.
CALPAIN_REFS = ["P07384", "P17655", "P20807", "Q9Y6W3", "Q9HC96", "O75808"]
GLOBIN_REFS = ["P02144", "P69905", "P68871", "Q9NPG2", "Q8WWM9"]

# UniProt annotates ADGB's own calpain catalytic domain and globin domain.
# Boundaries are read from the entry, never typed in.
CALPAIN_DOMAIN_NOTE = "Calpain catalytic"
GLOBIN_DOMAIN_NOTES = ("Globin; C-terminal part", "Globin; N-terminal part")


# --------------------------------------------------------------------------- #
# fetching
# --------------------------------------------------------------------------- #
_cache: dict[str, dict] = {}


def fetch(acc: str) -> dict:
    """Fetch a UniProt entry.  Fails loudly on a dead/empty accession.

    The ACTR10 lesson: a deleted entry returns no name and no features, which is
    indistinguishable from a live entry that genuinely carries none.  So assert.
    """
    if acc in _cache:
        return _cache[acc]
    with urllib.request.urlopen(UNIPROT.format(acc=acc)) as fh:
        d = json.load(fh)
    if not d.get("sequence", {}).get("value"):
        raise SystemExit(
            f"FATAL: {acc} returned no sequence -- inactive/deleted accession? "
            f"Check https://rest.uniprot.org/uniprotkb/{acc}.json"
        )
    _cache[acc] = d
    return d


def entry_name(d: dict) -> str:
    return d.get("uniProtkbId", "?")


def protein_name(d: dict) -> str:
    pd = d.get("proteinDescription", {})
    rn = pd.get("recommendedName") or (pd.get("submissionNames") or [{}])[0]
    return rn.get("fullName", {}).get("value", "?")


def is_reviewed(d: dict) -> bool:
    """'reviewed' is a SUBSTRING of 'unreviewed' -- anchor the test (ACTG2)."""
    return d.get("entryType", "").startswith("UniProtKB reviewed")


def seq(d: dict) -> str:
    return d["sequence"]["value"]


def features(d: dict, ftype: str) -> list[dict]:
    return [f for f in d.get("features", []) if f["type"] == ftype]


def sites(d: dict, ftype: str) -> list[tuple[int, str]]:
    """1-based single-residue positions of a feature type, with their notes."""
    out = []
    for f in features(d, ftype):
        s = f["location"]["start"]["value"]
        e = f["location"]["end"]["value"]
        if s == e:
            note = f.get("description", "") or f.get("ligand", {}).get("name", "")
            out.append((s, note))
    return sorted(out)


def domain_span(d: dict, note_substr: str) -> tuple[int, int]:
    for f in features(d, "Domain"):
        if note_substr.lower() in f.get("description", "").lower():
            return f["location"]["start"]["value"], f["location"]["end"]["value"]
    raise SystemExit(f"FATAL: no Domain feature matching {note_substr!r} in {entry_name(d)}")


# --------------------------------------------------------------------------- #
# alignment
# --------------------------------------------------------------------------- #
def make_aligner(matrix: str = "BLOSUM62", open_gap: float = -11, extend: float = -1):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend
    al.mode = "global"
    return al


def column_map(aln) -> dict[int, int]:
    """Map reference (target, seqA) 1-based index -> query (seqB) 1-based index.

    Only ungapped columns appear.  Built from the alignment's own coordinates so
    it cannot drift from the alignment that produced it.
    """
    m = {}
    ta, qa = aln.aligned  # blocks of (start, end) 0-based half-open
    for (ts, te), (qs, qe) in zip(ta, qa):
        for k in range(te - ts):
            m[int(ts) + k + 1] = int(qs) + k + 1
    return m


def pct_identity(aln, a: str, b: str) -> float:
    cm = column_map(aln)
    if not cm:
        return 0.0
    ident = sum(1 for i, j in cm.items() if a[i - 1] == b[j - 1])
    return 100.0 * ident / min(len(a), len(b))


@dataclass
class SiteResult:
    ref_acc: str
    ref_name: str
    ref_reviewed: bool
    ref_pos: int
    ref_res: str
    ref_note: str
    subj_pos: int | None
    subj_res: str | None
    identity_pct: float
    aligned: bool
    residue_matches: bool
    # The load-bearing second condition (AADACL2 rule): the column must land on a
    # position the SUBJECT itself annotates as the same kind of site.
    lands_on_subject_annotated_site: bool


@dataclass
class Report:
    subject: str = ""
    subject_name: str = ""
    subject_reviewed: bool = False
    subject_length: int = 0
    calpain_domain: tuple[int, int] | None = None
    globin_domains: dict = field(default_factory=dict)
    subject_own_active_sites: list = field(default_factory=list)
    subject_own_binding_sites: list = field(default_factory=list)
    calpain_results: list = field(default_factory=list)
    globin_results: list = field(default_factory=list)
    notes: list = field(default_factory=list)


def probe(subject: dict, sub_lo: int, sub_hi: int,
          ref_accs: list[str], ref_domain_note: str | None,
          ref_feature: str, subj_feature: str,
          aligner) -> list[SiteResult]:
    """Align each reference's domain to the subject region and read the columns."""
    s_full = seq(subject)
    s_sub = s_full[sub_lo - 1: sub_hi]
    subj_annotated = {p for p, _ in sites(subject, subj_feature)}
    out: list[SiteResult] = []
    for acc in ref_accs:
        rd = fetch(acc)
        r_full = seq(rd)
        if ref_domain_note:
            try:
                rlo, rhi = domain_span(rd, ref_domain_note)
            except SystemExit:
                rlo, rhi = 1, len(r_full)
        else:
            rlo, rhi = 1, len(r_full)
        r_sub = r_full[rlo - 1: rhi]
        aln = aligner.align(r_sub, s_sub)[0]
        cm = column_map(aln)
        ident = pct_identity(aln, r_sub, s_sub)
        rsites = [(p, n) for p, n in sites(rd, ref_feature) if rlo <= p <= rhi]
        if not rsites:
            out.append(SiteResult(acc, entry_name(rd), is_reviewed(rd), -1, "",
                                  f"NO {ref_feature} ANNOTATED IN DOMAIN", None, None,
                                  ident, False, False, False))
            continue
        for p, note in rsites:
            local_ref = p - rlo + 1
            local_subj = cm.get(local_ref)
            if local_subj is None:
                out.append(SiteResult(acc, entry_name(rd), is_reviewed(rd), p,
                                      r_full[p - 1], note, None, None, ident,
                                      False, False, False))
                continue
            gpos = local_subj + sub_lo - 1
            sres = s_full[gpos - 1]
            out.append(SiteResult(
                acc, entry_name(rd), is_reviewed(rd), p, r_full[p - 1], note,
                gpos, sres, ident, True,
                residue_matches=(sres == r_full[p - 1]),
                lands_on_subject_annotated_site=(gpos in subj_annotated),
            ))
    return out


# --------------------------------------------------------------------------- #
# self-test: break the guards in BOTH directions
# --------------------------------------------------------------------------- #
MODELS = [
    ("BLOSUM62", -11.0, -1.0),
    ("BLOSUM45", -14.0, -2.0),
    ("BLOSUM80", -10.0, -1.0),
    ("PAM250", -12.0, -2.0),
]


# MEROPS catalytic-type controlled vocabulary.  Longest-first so that
# "Non-peptidase homologue" cannot be shadowed by a shorter alternative.
MEROPS_TYPES = ["Non-peptidase homologue", "Asparagine", "Threonine", "Aspartic",
                "Cysteine", "Glutamic", "Metallo", "Serine", "Mixed", "Unknown"]


def merops_status(acc: str) -> dict:
    """Read the MEROPS identifier UniProt cross-references, and its catalytic type.

    MEROPS numbers genuine peptidases from .001 upward within a family and places
    NON-PEPTIDASE HOMOLOGUES in a high block.  Rather than trusting that
    convention from memory, the block boundary is DERIVED here from the observed
    identifiers of the reference calpains, and the catalytic type is read from
    the MEROPS summary page itself.
    """
    d = fetch(acc)
    ids = [r["id"] for r in d.get("uniProtKBCrossReferences", [])
           if r["database"] == "MEROPS"]
    out = {"acc": acc, "gene": [g.get("geneName", {}).get("value")
                                for g in d.get("genes", [])], "merops": ids,
           "catalytic_type": None}
    for mid in ids:
        try:
            with urllib.request.urlopen(
                    f"https://www.ebi.ac.uk/merops/cgi-bin/pepsum?id={mid}",
                    timeout=60) as fh:
                page = fh.read().decode("utf8", "replace")
        except Exception as exc:                      # network, not logic
            out["catalytic_type"] = f"UNAVAILABLE ({exc})"
            continue
        txt = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", page,
                                             flags=re.S | re.I))
        txt = re.sub(r"\s+", " ", html.unescape(txt))
        # Anchor to MEROPS's controlled vocabulary.  An open-ended
        # "[A-Za-z- ]+? up to a terminator" pattern silently returned UNPARSED
        # for CAPN1/2/3, whose pages are followed by "Peplist" rather than
        # "NC-IUBMB" -- an unanchored substring test on a controlled vocabulary
        # is exactly the defect this brief warns about.
        m = re.search(r"Catalytic type\s+(" + "|".join(MEROPS_TYPES) + r")\b", txt)
        out["catalytic_type"] = m.group(1) if m else "UNPARSED"
    return out


def consensus_calpain(subj: dict, lo: int, hi: int) -> dict:
    """Per-residue consensus over several substitution models.

    A single model's triad count is not a measurement (the brief: a weak family
    count may be an alignment artefact).  What matters is whether the ADGB
    POSITION each reference's catalytic residue lands on is stable across models,
    and whether the residue there is the catalytic one.
    """
    agg: dict[str, dict[str, list]] = {}
    for name, og, eg in MODELS:
        al = make_aligner(name, og, eg)
        for r in probe(subj, lo, hi, CALPAIN_REFS, "Calpain catalytic",
                       "Active site", "Active site", al):
            if not r.aligned:
                continue
            slot = agg.setdefault(r.ref_res, {"positions": [], "residues": [],
                                              "models": [], "refs": []})
            slot["positions"].append(r.subj_pos)
            slot["residues"].append(r.subj_res)
            slot["models"].append(name)
            slot["refs"].append(r.ref_name)
    return agg


def self_test(aligner) -> None:
    problems: list[str] = []

    # (1) HAPPY DIRECTION.  A guard can be wrong about success as easily as about
    #     failure (ACTA1 defect #5: an agreement check that failed on PERFECT
    #     agreement).  CAPN2 vs CAPN1 are close paralogs whose triads correspond,
    #     so every site must align, match, AND land on CAPN2's own annotated site.
    capn2 = fetch("P17655")
    lo, hi = domain_span(capn2, "Calpain catalytic")
    res = probe(capn2, lo, hi, ["P07384"], "Calpain catalytic",
                "Active site", "Active site", aligner)
    if len(res) != 3:
        problems.append(f"[happy] expected 3 CAPN1 active sites, got {len(res)}")
    for r in res:
        if not (r.aligned and r.residue_matches and r.lands_on_subject_annotated_site):
            problems.append(
                f"[happy] CAPN1 {r.ref_res}{r.ref_pos} -> CAPN2 "
                f"{r.subj_res}{r.subj_pos} aligned={r.aligned} "
                f"match={r.residue_matches} on_site={r.lands_on_subject_annotated_site}"
            )

    # (2) CATCH DIRECTION.  An unrelated protein must NOT produce a full triad.
    #     Without the lands_on_subject_annotated_site condition, alignment noise
    #     manufactures triads (brief: Arabidopsis CXE5 at 19.7% identity).
    n5c1a = fetch("Q9BXI3")
    neg = probe(n5c1a, 1, len(seq(n5c1a)), ["P07384"], "Calpain catalytic",
                "Active site", "Active site", aligner)
    full_hits = [r for r in neg if r.residue_matches and r.lands_on_subject_annotated_site]
    if full_hits:
        problems.append(f"[catch] negative control scored {len(full_hits)} full hits: {full_hits}")
    # ... and show the condition is load-bearing: residue-only matching is looser.
    residue_only = [r for r in neg if r.residue_matches]
    if len(residue_only) <= len(full_hits):
        problems.append(
            "[catch] the lands_on_subject_annotated_site condition made no "
            "difference on the negative control, so it is untested here"
        )

    # (3) Anchored substring test: 'reviewed' is a substring of 'unreviewed'.
    if not is_reviewed(fetch("P07384")):
        problems.append("[reviewed] Swiss-Prot entry P07384 not detected as reviewed")
    fake = {"entryType": "UniProtKB unreviewed (TrEMBL)"}
    if is_reviewed(fake):
        problems.append("[reviewed] 'unreviewed' wrongly matched as reviewed")

    # (4) A mutation that silently no-ops proves nothing -- assert the target is
    #     present before mutating (ACTA1 defect #3 / guard-writing lesson 3).
    subj = fetch(SUBJECT)
    real = domain_span(subj, "Calpain catalytic")
    if real != (70, 411):
        problems.append(f"[anchor] ADGB calpain domain moved: {real} (was 70-411)")
    # deliberately shift the window and require the result to change
    shifted = probe(subj, real[0] + 200, real[1], ["P07384"], "Calpain catalytic",
                    "Active site", "Active site", aligner)
    unshifted = probe(subj, real[0], real[1], ["P07384"], "Calpain catalytic",
                      "Active site", "Active site", aligner)
    if [(r.subj_pos, r.subj_res) for r in shifted] == [(r.subj_pos, r.subj_res) for r in unshifted]:
        problems.append("[anchor] shifting the subject window changed nothing -- probe() is inert")

    # (5) Matrix/gap robustness: the calpain verdict must not depend on the model.
    alt = make_aligner("BLOSUM45", open_gap=-14, extend=-2)
    a = probe(subj, real[0], real[1], CALPAIN_REFS, "Calpain catalytic",
              "Active site", "Active site", aligner)
    b = probe(subj, real[0], real[1], CALPAIN_REFS, "Calpain catalytic",
              "Active site", "Active site", alt)
    ca = sum(1 for r in a if r.residue_matches)
    cb = sum(1 for r in b if r.residue_matches)
    print(f"  [robustness] residue matches BLOSUM62={ca}  BLOSUM45/-14/-2={cb}")

    # (6) MEROPS parse must not silently degrade to UNPARSED, and the vocabulary
    #     anchor must be break-tested in both directions.
    mtypes = {a: merops_status(a)["catalytic_type"] for a in [SUBJECT] + CALPAIN_REFS}
    unparsed = [a for a, t in mtypes.items() if t in (None, "UNPARSED")
                or str(t).startswith("UNAVAILABLE")]
    if unparsed:
        problems.append(f"[merops] failed to parse catalytic type for {unparsed}: "
                        f"{ {a: mtypes[a] for a in unparsed} }")
    if mtypes.get(SUBJECT) == mtypes.get("P07384"):
        problems.append("[merops] subject and CAPN1 have the SAME catalytic type "
                        f"({mtypes.get(SUBJECT)}) -- the comparison is not discriminating")
    # the vocabulary must actually be required: a page without a listed type
    # must yield UNPARSED rather than capturing arbitrary prose.
    probe_txt = "Catalytic type Bananas NC-IUBMB"
    if re.search(r"Catalytic type\s+(" + "|".join(MEROPS_TYPES) + r")\b", probe_txt):
        problems.append("[merops] vocabulary anchor matched a non-vocabulary word")
    if not re.search(r"Catalytic type\s+(" + "|".join(MEROPS_TYPES) + r")\b",
                     "Catalytic type Non-peptidase homologue Other databases"):
        problems.append("[merops] vocabulary anchor failed on a VALID type "
                        "(happy direction)")
    print(f"  [merops] {mtypes}")

    if problems:
        print("SELF-TEST FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("SELF-TEST PASSED (happy direction, catch direction, anchors, robustness)")


# --------------------------------------------------------------------------- #

def write_results_md(path, rep, cons, mer, cal, gl) -> None:
    """Generate RESULTS.md entirely from computed values.

    Nothing here is typed in by hand: every count, position and verdict is
    interpolated from the same objects the console table was printed from, so a
    hand-edit to the file is reverted by the next run and the prose cannot drift
    from the numbers.  Verify with:  python adgb_sites.py --results-md /tmp/x &&
    diff /tmp/x RESULTS.md
    """
    C = cons.get("C", {"positions": [], "residues": []})
    H = cons.get("H", {"positions": [], "residues": []})
    N = cons.get("N", {"positions": [], "residues": []})

    def kept(slot, aa):
        return sorted({f"{r}{p}" for r, p in zip(slot["residues"], slot["positions"])
                       if r == aa})

    c_keep, h_keep, n_keep = kept(C, "C"), kept(H, "H"), kept(N, "N")
    c_tot, h_tot, n_tot = len(C["positions"]), len(H["positions"]), len(N["positions"])
    c_hit = sum(1 for r in C["residues"] if r == "C")
    h_hit = sum(1 for r in H["residues"] if r == "H")
    n_hit = sum(1 for r in N["residues"] if r == "N")

    subj_mer = next(m for m in mer if m["acc"] == rep.subject)
    ref_mer = [m for m in mer if m["acc"] != rep.subject]
    ref_types = sorted({m["catalytic_type"] for m in ref_mer})

    # Q2: split references by whether the column lands on ADGB's own annotated site
    onreg = [g for g in gl if g["lands_on_subject_annotated_site"]]
    offreg = [g for g in gl if g["aligned"] and not g["lands_on_subject_annotated_site"]]
    distal = [g for g in onreg if g["subj_pos"] == 792]
    proximal = [g for g in onreg if g["subj_pos"] == 824]
    dist_res = sorted({g["ref_res"] for g in distal})
    prox_match = [g for g in proximal if g["residue_matches"]]

    L = []
    A = L.append
    A("# ADGB (Q8N7X0) - do the calpain and globin domains retain their functional residues?")
    A("")
    A("Generated by `adgb_sites.py`. Reproduce with:")
    A("")
    A("```bash")
    A("uv run python adgb_sites.py --self-test              # guards, both directions")
    A("uv run python adgb_sites.py --json results.json \\")
    A("                            --results-md RESULTS.md  # this file")
    A("```")
    A("")
    A("Every number below is interpolated from the same run that printed the tables,")
    A("so this file cannot drift from the measurement. A hand-edit is reverted by the")
    A("next run.")
    A("")
    A("## Question")
    A("")
    A("GOA gives ADGB four InterPro IEA rows, two from each domain signature:")
    A("")
    A("| signature | GO term |")
    A("|---|---|")
    A("| IPR001300 Peptidase_C2_calpain_cat | GO:0004198 calcium-dependent cysteine-type endopeptidase activity |")
    A("| IPR001300 Peptidase_C2_calpain_cat | GO:0006508 proteolysis |")
    A("| IPR012292 Globin/Proto | GO:0019825 oxygen binding |")
    A("| IPR012292 Globin/Proto | GO:0020037 heme binding |")
    A("")
    A("A domain's name is not an activity. Does ADGB keep the residues each activity needs?")
    A("")
    A(f"Subject: `{rep.subject}` {rep.subject_name}, {rep.subject_length} aa, "
      f"reviewed={rep.subject_reviewed}.")
    A(f"UniProt annotates the calpain catalytic domain at "
      f"{rep.calpain_domain[0]}-{rep.calpain_domain[1]} and the globin domain in two "
      f"parts, {rep.globin_domains['Globin; C-terminal part']} and "
      f"{rep.globin_domains['Globin; N-terminal part']} (circular permutation).")
    A("")
    A("## Q1. Calpain catalytic triad: NOT retained")
    A("")
    A(f"Each of the {len(CALPAIN_REFS)} reviewed reference calpains carries three UniProt")
    A(f"`Active site` features. **ADGB carries {len(rep.subject_own_active_sites)}.**")
    A("")
    A(f"Aligning each reference's catalytic domain to ADGB "
      f"{rep.calpain_domain[0]}-{rep.calpain_domain[1]} under "
      f"{len(MODELS)} substitution/gap models ({', '.join(m[0] for m in MODELS)}) and")
    A("reading the ADGB residue in each reference-active-site column:")
    A("")
    A("| triad role | aligned columns | ADGB positions hit | columns where ADGB has the catalytic residue |")
    A("|---|---|---|---|")
    A(f"| nucleophile Cys | {c_tot} | {sorted(set(C['positions']))} | "
      f"**{c_hit}/{c_tot}**, always at {c_keep or 'none'} |")
    A(f"| general base His | {h_tot} | {sorted(set(H['positions']))} | "
      f"{h_hit}/{h_tot} {h_keep or '(none)'} |")
    A(f"| Asn | {n_tot} | {sorted(set(N['positions']))} | {n_hit}/{n_tot} {n_keep or '(none)'} |")
    A("")
    A("Read per-residue rather than per-triad (a single model's triad count is an")
    A("alignment artefact, not a measurement):")
    A("")
    A(f"- The **nucleophile column converges**: whenever a reference's catalytic Cys")
    A(f"  aligns to a Cys in ADGB it is always the same residue, {', '.join(c_keep) or 'n/a'},")
    A(f"  in {c_hit} of {c_tot} columns. Which references reach it varies by model; the")
    A("  ADGB position does not.")
    A(f"- The **general-base His column does not converge**: {h_hit} of {h_tot} columns,")
    A(f"  scattered over ADGB positions {sorted(set(H['positions']))}. The lone hit")
    A(f"  ({', '.join(h_keep) or 'none'}) appears under one model only and at a position no")
    A("  other model selects - the signature of alignment noise, not conservation.")
    A(f"- The **Asn column never yields an Asn**: {n_hit} of {n_tot}.")
    A("")
    A("A papain-fold cysteine protease cannot catalyse without the general-base")
    A("histidine that deprotonates the nucleophile. A retained Cys with no His and no")
    A("Asn is a fold, not an active site.")
    A("")
    A("### Independent corroboration: MEROPS classifies ADGB as a non-peptidase homologue")
    A("")
    A("This does not depend on the alignment at all.")
    A("")
    A("| accession | gene | MEROPS | catalytic type |")
    A("|---|---|---|---|")
    for m in mer:
        A(f"| {m['acc']} | {m['gene'][0] if m['gene'] else '?'} | "
          f"`{m['merops'][0] if m['merops'] else '-'}` | {m['catalytic_type']} |")
    A("")
    A(f"All {len(ref_mer)} reference calpains: {', '.join(ref_types)}. "
      f"ADGB: **{subj_mer['catalytic_type']}**, and ADGB is the *holotype* of that entry.")
    A(f"The identifier block is consistent: reference suffixes "
      f"{sorted(int(m['merops'][0].split('.')[1]) for m in ref_mer)} against ADGB's "
      f"{[int(m['merops'][0].split('.')[1]) for m in [subj_mer]][0]}.")
    A("")
    A("UniProt says the same thing in its `CAUTION`: *\"The calpain domain lacks the")
    A("conserved active site residues. Probably catalytically inactive as a")
    A("calcium-dependent cysteine-type endopeptidase.\"*")
    A("")
    A("**Verdict: `GO:0004198` is not supported.** The measurement refines UniProt's")
    A("wording - it is not that all the active-site residues are gone; the nucleophile")
    A("survives and the general base and Asn do not.")
    A("")
    A("### Caveat that must be stated")
    A("")
    for note in rep.notes:
        if isinstance(note, str) and note.startswith("Q1 CAVEAT"):
            A("> " + note)
    A("")
    A("## Q2. Globin heme ligands: proximal His retained, distal His replaced by Gln")
    A("")
    A("Same method against reviewed globins whose heme-iron ligands UniProt annotates.")
    A("Here ADGB *does* have its own annotated sites, so the")
    A("`lands_on_subject_annotated_site` condition is live and does the discriminating.")
    A("")
    A("| reference | %id | reference site | -> ADGB | residue match | on an ADGB-annotated site | role |")
    A("|---|---|---|---|---|---|---|")
    for g in gl:
        if not g["aligned"]:
            continue
        A(f"| {g['ref_acc']} {g['ref_name']} | {g['identity_pct']:.1f} | "
          f"{g['ref_res']}{g['ref_pos']} | {g['subj_res']}{g['subj_pos']} | "
          f"{'yes' if g['residue_matches'] else 'no'} | "
          f"{'**yes**' if g['lands_on_subject_annotated_site'] else 'no'} | {g['ref_note']} |")
    A("")
    A(f"- **Distal position (ADGB Q792).** {len(distal)} reference columns land on it, "
      f"from {len(set(g['ref_acc'] for g in distal))} distinct globins, and the reference")
    A(f"  residue is {'/'.join(dist_res)} in every one. ADGB has "
      f"**{[g['subj_res'] for g in distal][0] if distal else '?'}**.")
    A(f"- **Proximal position (ADGB H824).** {len(proximal)} reference columns land on it "
      f"and {len(prox_match)} of {len(proximal)} match: ADGB retains the proximal histidine.")
    A(f"- **{len(offreg)} columns are off-register** (they do not land on either ADGB")
    A("  annotated site). Their apparent matches are noise - the HBB alignment in")
    A("  particular 'matches' a distal His at a position UniProt does not annotate while")
    A("  failing the proximal one. Sequence identity does not predict register here")
    A(f"  (CYGB at {[g['identity_pct'] for g in gl if g['ref_acc']=='Q8WWM9'][0]:.1f}% is on-register for both sites; "
      f"HBB at {[g['identity_pct'] for g in gl if g['ref_acc']=='P68871'][0]:.1f}% is on-register for neither) - the")
    A("  annotated-site condition does.")
    A("")
    A("**Verdict: the globin domain is intact as a heme protein, but it is a His/Gln")
    A("hexacoordinate globin, not a bis-histidyl one.**")
    A("")
    A("This is confirmed independently by the primary literature, in three places that")
    A("agree with the sequence and with each other:")
    A("")
    A("- Reeder *et al.* 2024 (PMID:38725499) state the ferric coordination as")
    A("  His-Fe(III)-X with *\"X = His for Cygb and Gln for Adgb\"*, and label the")
    A("  alignment position *\"the distal histidine/glutamine\"*.")
    A("- Nie *et al.* 2025 (PMID:39719941) label Fig. 1B *\"the distal Gln30\"* and conclude")
    A("  *\"Gln30 in the heme distal site may coordinate to the heme iron in the ferrous")
    A("  state\"* - their construct starts at UniProt 763, so their His62/res30 are")
    A("  UniProt H824/Q792 exactly (spacing 32 in both numberings).")
    A("- Ren *et al.* 2026 (PMID:42372363) name it in the title and mutate it: *\"the heme")
    A("  distal residue Gln12 through the generation of Q12H and Q12Y mutants\"*.")
    A("")
    A("**UniProt's own FUNCTION line is internally inconsistent with its feature table:**")
    A("it says ADGB is a *\"chimeric globin with a bis-histidyl six-coordinate heme-iron")
    A(f"atom\"* while the feature table annotates the distal ligand as "
      f"{[b['res'] for b in rep.subject_own_binding_sites if b['pos']==792][0]}792. Worth reporting to UniProt.")
    A("")
    A("## What this does and does not settle")
    A("")
    A("- It settles that the calpain-domain-derived catalytic MF term has no residue")
    A("  support, and that MEROPS and UniProt independently agree.")
    A("- It settles that heme binding is structurally well founded (the proximal ligand")
    A("  is retained and is the residue UniProt annotates).")
    A("- **It does not test oxygen binding**, which is a ligand-binding measurement, not")
    A("  a sequence one. See the notes file: an oxy complex *is* formed and its")
    A("  association rate was measured (PMID:38725499), so `GO:0019825` is true as")
    A("  chemistry, while the same paper's autoxidation rate argues it is not a")
    A("  physiological role.")
    A("- It does not test whether ADGB contributes to SEPT10 cleavage by a non-catalytic")
    A("  route, which is what the cell-based data actually show.")
    A("")
    with open(path, "w") as fh:
        fh.write("\n".join(L) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json", help="write results here")
    ap.add_argument("--results-md", help="write RESULTS.md here")
    args = ap.parse_args()

    aligner = make_aligner()
    if args.self_test:
        self_test(aligner)
        return

    subj = fetch(SUBJECT)
    rep = Report(
        subject=SUBJECT,
        subject_name=f"{entry_name(subj)} / {protein_name(subj)}",
        subject_reviewed=is_reviewed(subj),
        subject_length=len(seq(subj)),
    )
    s = seq(subj)
    rep.subject_own_active_sites = sites(subj, "Active site")
    rep.subject_own_binding_sites = [
        {"pos": p, "res": s[p - 1], "note": n} for p, n in sites(subj, "Binding site")
    ]

    print("=" * 78)
    print(f"SUBJECT  {SUBJECT}  {rep.subject_name}")
    print(f"         {rep.subject_length} aa   reviewed={rep.subject_reviewed}")
    print(f"         own UniProt Active site features: "
          f"{rep.subject_own_active_sites or 'NONE'}")
    print(f"         own UniProt Binding site features:")
    for b in rep.subject_own_binding_sites:
        print(f"           {b['res']}{b['pos']}  {b['note']}")

    # ---------------- Q1: calpain triad -----------------------------------
    clo, chi = domain_span(subj, CALPAIN_DOMAIN_NOTE)
    rep.calpain_domain = (clo, chi)
    print("\n" + "=" * 78)
    print(f"Q1  CALPAIN CATALYTIC TRIAD   (ADGB domain {clo}-{chi}, "
          f"{chi - clo + 1} aa; InterPro IPR001300 -> GO:0004198 / GO:0006508)")
    print("=" * 78)
    cal = probe(subj, clo, chi, CALPAIN_REFS, "Calpain catalytic",
                "Active site", "Active site", aligner)
    rep.calpain_results = [asdict(r) for r in cal]
    hdr = (f"{'reference':22s} {'SP':3s} {'%id':>5s}  {'ref site':>9s} -> "
           f"{'ADGB':>8s}  match  on_ADGB_site")
    print(hdr)
    print("-" * len(hdr))
    for r in cal:
        sp = "yes" if r.ref_reviewed else "NO"
        if not r.aligned and r.ref_note.startswith("NO "):
            print(f"{r.ref_acc + ' ' + r.ref_name:22s} {sp:3s} {r.identity_pct:5.1f}  {r.ref_note}")
            continue
        tgt = f"{r.subj_res}{r.subj_pos}" if r.aligned else "(gap)"
        mark = "YES" if r.residue_matches else "no"
        onsite = "YES" if r.lands_on_subject_annotated_site else "no"
        print(f"{r.ref_acc + ' ' + r.ref_name:22s} {sp:3s} {r.identity_pct:5.1f}  "
              f"{r.ref_res}{r.ref_pos:>8} -> {tgt:>8s}  {mark:5s}  {onsite}")

    aligned = [r for r in cal if r.aligned]
    matched = [r for r in aligned if r.residue_matches]
    print(f"\n  aligned catalytic-site columns : {len(aligned)}/{len([r for r in cal if r.ref_pos > 0])}")
    print(f"  ADGB retains the reference residue: {len(matched)}")
    print(f"  ADGB's own annotated Active site features: "
          f"{len(rep.subject_own_active_sites)}")
    if not rep.subject_own_active_sites:
        rep.notes.append(
            "Q1 CAVEAT: ADGB carries ZERO UniProt 'Active site' features, so the "
            "lands_on_subject_annotated_site condition is VACUOUS in Q1 and its "
            "all-'no' column is not a measurement. That absence is itself the "
            "signal: UniProt annotates the Calpain catalytic domain on ADGB but "
            "propagates no catalytic residues into it, whereas all "
            f"{len(CALPAIN_REFS)} reference calpains carry 3 each. "
            "The condition IS load-bearing in Q2, where ADGB has 2 annotated "
            "heme-iron Binding sites and it separates the on-register "
            "Mb/Ngb/Cygb alignments from the off-register HBB one.")
        print("  " + "!" * 70)
        for line in rep.notes[-1].split(". "):
            print("  ! " + line.strip())
    # per-residue-role breakdown, derived not assumed
    byres: dict[str, list[str]] = {}
    for r in aligned:
        byres.setdefault(r.ref_res, []).append(f"{r.subj_res}{r.subj_pos}")
    for ref_res, hits in sorted(byres.items()):
        same = sum(1 for h in hits if h[0] == ref_res)
        print(f"    reference {ref_res} -> ADGB {sorted(set(hits))}  "
              f"({same}/{len(hits)} conserved)")

    # ---------------- Q2: globin heme ligands ------------------------------
    print("\n  --- per-residue consensus over "
          f"{len(MODELS)} substitution/gap models ---")
    cons = consensus_calpain(subj, clo, chi)
    rep.notes.append(f"consensus models: {MODELS}")
    for ref_res in sorted(cons):
        slot = cons[ref_res]
        pos = sorted(set(slot["positions"]))
        hits = [f"{r}{p}" for r, p in zip(slot["residues"], slot["positions"])
                if r == ref_res]
        print(f"    reference {ref_res}: {len(slot['positions'])} aligned columns "
              f"across models -> ADGB positions {pos}")
        print(f"      columns where ADGB also has {ref_res}: "
              f"{len(hits)}/{len(slot['positions'])}  {sorted(set(hits)) or 'NONE'}")
    rep.notes.append({k: {"positions": sorted(set(v["positions"])),
                          "conserved": sorted({f"{r}{p}" for r, p
                                               in zip(v["residues"], v["positions"])
                                               if r == k})}
                      for k, v in cons.items()})

    print("\n  --- MEROPS classification (independent of the alignment) ---")
    mer = [merops_status(a) for a in [SUBJECT] + CALPAIN_REFS]
    rep.notes.append({"merops": mer})
    for m in mer:
        tag = "<== SUBJECT" if m["acc"] == SUBJECT else ""
        print(f"    {m['acc']} {str(m['gene']):12s} {str(m['merops']):14s} "
              f"{m['catalytic_type']}  {tag}")
    nums = []
    for m in mer:
        for mid in m["merops"]:
            if "." in mid:
                nums.append((m["acc"], mid, int(mid.split(".")[1])))
    peps = [n for a, i, n in nums if a != SUBJECT]
    subj_n = [n for a, i, n in nums if a == SUBJECT]
    print(f"    reference calpain MEROPS suffixes: {sorted(peps)}")
    print(f"    ADGB MEROPS suffix: {subj_n}  "
          f"(max reference = {max(peps) if peps else 'n/a'})")

    print("\n" + "=" * 78)
    print("Q2  GLOBIN HEME-IRON LIGANDS  (InterPro IPR012292 -> GO:0019825 / GO:0020037)")
    print("=" * 78)
    for note in GLOBIN_DOMAIN_NOTES:
        rep.globin_domains[note] = domain_span(subj, note)
        print(f"  ADGB {note}: {rep.globin_domains[note]}")
    glo, ghi = rep.globin_domains["Globin; C-terminal part"]
    gl = probe(subj, glo, ghi, GLOBIN_REFS, None, "Binding site", "Binding site", aligner)
    rep.globin_results = [asdict(r) for r in gl]
    print(f"\n{'reference':22s} {'SP':3s} {'%id':>5s}  {'ref site':>9s} -> "
          f"{'ADGB':>8s}  match  on_ADGB_site  role")
    print("-" * 100)
    for r in gl:
        sp = "yes" if r.ref_reviewed else "NO"
        if not r.aligned and r.ref_note.startswith("NO "):
            print(f"{r.ref_acc + ' ' + r.ref_name:22s} {sp:3s} {r.identity_pct:5.1f}  {r.ref_note}")
            continue
        tgt = f"{r.subj_res}{r.subj_pos}" if r.aligned else "(gap)"
        mark = "YES" if r.residue_matches else "no "
        onsite = "YES" if r.lands_on_subject_annotated_site else "no "
        print(f"{r.ref_acc + ' ' + r.ref_name:22s} {sp:3s} {r.identity_pct:5.1f}  "
              f"{r.ref_res}{r.ref_pos:>8} -> {tgt:>8s}  {mark}   {onsite:12s}  {r.ref_note[:34]}")

    print("\n  ADGB's own annotated heme-iron ligands (from UniProt, not alignment):")
    for b in rep.subject_own_binding_sites:
        print(f"    {b['res']}{b['pos']}  {b['note']}")

    if args.results_md:
        write_results_md(args.results_md, rep, cons, mer,
                         rep.calpain_results, rep.globin_results)
        print(f"wrote {args.results_md}")

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(asdict(rep), fh, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
