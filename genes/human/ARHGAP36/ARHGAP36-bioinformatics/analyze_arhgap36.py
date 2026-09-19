"""Does ARHGAP36 still have the machinery a GTPase activator needs?

ARHGAP36 (Q6ZRI8) carries exactly four GO annotations, none experimental. Three are
IBA from one PAINT node (PTN000973894, seeded by mouse Arhgap6, MGI:1196332); one is
IEA from InterPro's RhoGAP signature. The molecular function among them is
``GO:0005096 GTPase activator activity``. UniProt independently asserts the same
function in its FUNCTION comment, on ``ECO:0000250`` -- by similarity.

The same UniProt entry annotates a "Arginine finger" Site inside the Rho-GAP domain,
by PROSITE ProRule. A RhoGAP works by inserting that arginine into the GTPase active
site to stabilise the transition state, so the residue at that position is the single
most direct sequence-level statement about whether the protein can do the job.

This script measures that, and then tries hard to break its own answer:

Analysis 1 -- what UniProt actually says, read from the API.
  The annotated arginine-finger position, the residue there, the evidence code on the
  Site, and the evidence code on the FUNCTION comment that asserts GAP activity. All
  read from the record; nothing about ARHGAP36 is hardcoded except its accession.

Analysis 2 -- is that Site in register? (reciprocal projection)
  A ProRule Site is placed by profile alignment, so it can be misplaced. Each control's
  OWN annotated arginine finger is projected onto ARHGAP36 by aligning Rho-GAP domain
  to Rho-GAP domain, and the projected position is compared with ARHGAP36's own Site.
  Independent controls converging on the same ARHGAP36 position is what turns "UniProt
  says 258" into "position 258 is where the finger belongs". Each control is also
  projected onto every other control as a method control: a projection that cannot
  recover a known arginine finger is not trusted to place ARHGAP36's.

Analysis 3 -- could the finger simply have moved? (escape test)
  Losing an arginine at one position is only interesting if there is not another one a
  turn away. A window around the projected position is scanned for any arginine and the
  nearest one is reported with its offset. This is the check that would rescue the
  annotation, so it is run and reported whatever it says.

Analysis 4 -- does the sequence record agree with the literature?
  PMID:33999959 calls the equivalent site "Thr227", which is isoform-2 numbering.
  The script applies UniProt's own VSP splice feature for isoform 2 -- read from the
  feature table, not assumed -- and recomputes where canonical 258 lands in that
  isoform. Agreement is a cross-check between two independent records; disagreement
  would mean one of them is about a different residue.

Analysis 5 -- is this a property of ARHGAP36 or of the family?
  The residue is scored the same way for the PAINT donor (mouse Arhgap6) and the human
  paralog in the same PANTHER family, and then for every reviewed human protein
  carrying the PROSITE RhoGAP profile. A loss that the IBD's own seed does not share
  is an argument about the node; a loss the whole family shares would not be.

Analysis 6 -- catalysis versus binding.
  UniProt records an experimental RAC1 interaction via the Rho-GAP domain
  (PubMed:35986704). Losing the catalytic arginine does not by itself remove the
  binding surface, and the two claims need separating. The GAP:GTPase interface is
  computed from PDB 1TX4 (p50RhoGAP:RhoA:GDP:AlF4, a transition-state mimic) and
  projected onto ARHGAP36, counting how much of the surface survives.

What this script deliberately does NOT claim: that a missing arginine finger is
sufficient to call a RhoGAP dead. The sibling review of ARHGAP11B measured the
converse -- a retained arginine finger in a protein that is experimentally GAP-dead --
so residue identity and curated activity are decoupled in both directions in this
family. Analysis 5 re-derives the discrimination rate here so that the weight of the
residue evidence is a number in this report rather than a borrowed claim.

Every number in RESULTS.md comes from a run of this script. Missing input is a hard
error naming the fix, never a silently degraded section.

Usage:
    uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py
    uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import FastMMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import protein_letters_3to1

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "cache"

# --- subjects -------------------------------------------------------------------
QUERY_ACC = "Q6ZRI8"  # ARHGAP36, the subject of the review

# Controls carrying an experimentally or structurally anchored arginine finger.
CONTROLS = {
    "Q07960": "ARHGAP1/p50RhoGAP - arginine finger resolved in the 1TX4 transition state",
    "O54834": "mouse Arhgap6 - the experimental seed (MGI:1196332) of the IBD this review reviews",
    "O43182": "human ARHGAP6 - the PANTHER PTHR12635 paralog of ARHGAP36",
}
# A protein UniProt/the literature treat as binding a RHO GTPase without catalysing
# its hydrolysis. It is the shape ARHGAP36 is being compared against, not a control
# for the alignment.
NEGATIVE_REFERENCE_ACC = "Q01968"  # OCRL
# Retains the arginine and is experimentally GAP-dead: the decoupling control.
DECOUPLING_ACC = "Q3KRB8"  # ARHGAP11B

RHOA_ACC = "P61586"  # the GTPase in the control structure

INTERFACE_PDB = "1TX4"
GAP_CHAIN = "A"
GTPASE_CHAIN = "B"
TS_LIGANDS = {"GDP", "ALF", "MG"}
CONTACT_CUTOFF_A = 4.5

RHOGAP_PROSITE = "PS50238"
ARGININE_FINGER_TEXT = "Arginine finger"
RHOGAP_DOMAIN_NOTE = "Rho-GAP"

# Half-width of the window scanned for a displaced arginine, in residues. One helical
# turn is ~3.6 residues; 10 either side is far wider than any plausible register shift
# and is deliberately generous to the annotation being challenged.
ESCAPE_WINDOW = 10


class AnalysisError(RuntimeError):
    """A hard failure. Never downgraded to a missing section in the report."""


# --- fetching -------------------------------------------------------------------


def _fetch(url: str, dest: Path, binary: bool = False) -> bytes:
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as fh:
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
    # A demerged/deleted accession returns 200 with no sequence, which is otherwise
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


def evidence_codes(feat_or_comment: dict[str, Any]) -> list[str]:
    return sorted({e.get("evidenceCode", "") for e in feat_or_comment.get("evidences", []) if e.get("evidenceCode")})


def site_features(rec: dict[str, Any], text: str | None = None) -> list[dict[str, Any]]:
    """Single-residue Site features, optionally filtered by description text."""
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
        out.append(
            {
                "position": int(start),
                "description": str(feat.get("description", "")),
                "evidence": evidence_codes(feat),
            }
        )
    return sorted(out, key=lambda d: d["position"])


def arginine_finger(rec: dict[str, Any]) -> dict[str, Any] | None:
    hits = site_features(rec, ARGININE_FINGER_TEXT)
    if not hits:
        return None
    if len(hits) > 1:
        raise AnalysisError(f"{name_of(rec)} has {len(hits)} annotated arginine fingers; expected at most 1")
    hit = dict(hits[0])
    hit["residue"] = seq_of(rec)[hit["position"] - 1]
    return hit


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


def rhogap_domain(rec: dict[str, Any]) -> tuple[int, int]:
    spans = domain_spans(rec, RHOGAP_DOMAIN_NOTE)
    if len(spans) != 1:
        raise AnalysisError(f"{name_of(rec)} has {len(spans)} Rho-GAP DOMAIN features; expected exactly 1")
    return spans[0]


def function_comments(rec: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for com in rec.get("comments", []):
        if com.get("commentType") != "FUNCTION":
            continue
        for text in com.get("texts", []):
            out.append({"text": text.get("value", ""), "evidence": evidence_codes(text)})
    return out


def gap_activity_claim(rec: dict[str, Any]) -> dict[str, Any] | None:
    """The FUNCTION sentence, if any, that asserts GTPase-activator activity.

    Anchored on 'GTPase activator' / 'GAP for', NOT on the bare word 'activity': the
    sibling analysis was burned by a substring test that matched ARHGAP36's own phrase
    'converting them to an inactive GDP-bound state', which describes the GTPase's
    nucleotide state and not the protein's catalytic status.
    """
    for com in function_comments(rec):
        low = com["text"].lower()
        if "gtpase activator" in low or "gtpase-activating" in low or re.search(r"\bgap for\b", low):
            return com
    return None


def splice_variants(rec: dict[str, Any]) -> list[dict[str, Any]]:
    """Alternative-sequence features, as (start, end, replacement, id)."""
    out = []
    for feat in rec.get("features", []):
        if feat.get("type") != "Alternative sequence":
            continue
        start = feat["location"]["start"].get("value")
        end = feat["location"]["end"].get("value")
        if start is None or end is None:
            continue
        alt = feat.get("alternativeSequence", {})
        replacement = (alt.get("alternativeSequences") or [""])[0]
        out.append(
            {
                "id": feat.get("featureId", ""),
                "start": int(start),
                "end": int(end),
                "replacement": replacement,
                "description": str(feat.get("description", "")),
            }
        )
    return out


# --- alignment ------------------------------------------------------------------


def make_aligner(mode: str = "global") -> PairwiseAligner:
    aln = PairwiseAligner()
    aln.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln.open_gap_score = -11
    aln.extend_gap_score = -1
    aln.mode = mode
    return aln


def align_map(seq_from: str, seq_to: str, mode: str = "global") -> dict[int, int]:
    """Map 1-based positions of `seq_from` onto 1-based positions of `seq_to`."""
    aln = make_aligner(mode).align(seq_from, seq_to)[0]
    mapping: dict[int, int] = {}
    for (f0, f1), (t0, _t1) in zip(aln.aligned[0], aln.aligned[1]):
        f0, f1, t0 = int(f0), int(f1), int(t0)
        for off in range(f1 - f0):
            mapping[f0 + off + 1] = t0 + off + 1
    return mapping


def project_domain_position(
    src_rec: dict[str, Any],
    src_seq: str,
    dst_rec: dict[str, Any],
    dst_seq: str,
    src_pos: int,
) -> int | None:
    """Project a position in src's Rho-GAP domain onto dst, domain-to-domain.

    Domain-to-domain rather than full-length, because RhoGAP-domain proteins carry the
    domain at wildly different offsets (ARHGAP1 C-terminal behind a CRAL-TRIO domain,
    ARHGAP11A N-terminal of a 1023-residue protein) and a full-length global alignment
    pairs N-terminus with N-terminus and lands the finger hundreds of residues away.
    """
    s0, s1 = rhogap_domain(src_rec)
    d0, d1 = rhogap_domain(dst_rec)
    if not (s0 <= src_pos <= s1):
        raise AnalysisError(f"{name_of(src_rec)} position {src_pos} is outside its Rho-GAP domain {s0}..{s1}")
    mapping = align_map(src_seq[s0 - 1 : s1], dst_seq[d0 - 1 : d1])
    hit = mapping.get(src_pos - s0 + 1)
    return None if hit is None else hit + d0 - 1


# --- analysis 2/3 ---------------------------------------------------------------


def projection_table(query_rec: dict[str, Any], query_seq: str, control_recs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    own = arginine_finger(query_rec)
    rows = []
    for acc, rec in control_recs.items():
        finger = arginine_finger(rec)
        if finger is None:
            raise AnalysisError(f"control {acc} ({name_of(rec)}) has no annotated arginine finger; it cannot anchor a projection")
        if finger["residue"] != "R":
            raise AnalysisError(
                f"control {acc} ({name_of(rec)}) has {finger['residue']} at its own annotated arginine finger "
                f"{finger['position']}; a control that does not hold an arginine cannot anchor this test"
            )
        proj = project_domain_position(rec, seq_of(rec), query_rec, query_seq, finger["position"])
        rows.append(
            {
                "control": acc,
                "control_entry": name_of(rec),
                "control_site": finger["position"],
                "control_residue": finger["residue"],
                "projected_query_position": proj,
                "projected_query_residue": None if proj is None else query_seq[proj - 1],
                "agrees_with_query_site": None if (proj is None or own is None) else (proj == own["position"]),
                "note": CONTROLS.get(acc, ""),
            }
        )
    return rows


def method_control_matrix(control_recs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Project every control's finger onto every other control.

    A projection method that cannot recover a *known* arginine finger has no standing
    to place ARHGAP36's. Every off-diagonal cell must land on the target's own
    annotated site.
    """
    rows = []
    for src_acc, src in control_recs.items():
        for dst_acc, dst in control_recs.items():
            if src_acc == dst_acc:
                continue
            src_f = arginine_finger(src)
            dst_f = arginine_finger(dst)
            assert src_f is not None and dst_f is not None  # guaranteed by projection_table
            proj = project_domain_position(src, seq_of(src), dst, seq_of(dst), src_f["position"])
            rows.append(
                {
                    "from": name_of(src),
                    "to": name_of(dst),
                    "projected": proj,
                    "target_own_site": dst_f["position"],
                    "recovered": proj == dst_f["position"],
                    "projected_residue": None if proj is None else seq_of(dst)[proj - 1],
                }
            )
    return rows


def escape_scan(seq: str, centre: int, half_width: int = ESCAPE_WINDOW) -> dict[str, Any]:
    lo = max(1, centre - half_width)
    hi = min(len(seq), centre + half_width)
    window = seq[lo - 1 : hi]
    args = [lo + i for i, c in enumerate(window) if c == "R"]
    nearest = min(args, key=lambda p: (abs(p - centre), p)) if args else None
    return {
        "centre": centre,
        "centre_residue": seq[centre - 1],
        "window": f"{lo}..{hi}",
        "window_sequence": window,
        "half_width": half_width,
        "arginines_in_window": args,
        "nearest_arginine": nearest,
        "nearest_offset": None if nearest is None else nearest - centre,
    }


# --- analysis 4 -----------------------------------------------------------------


def isoform_position(rec: dict[str, Any], canonical_pos: int, vsp_id: str) -> dict[str, Any]:
    """Where canonical_pos lands after applying one Alternative sequence feature.

    Only defined for a VSP that lies entirely upstream of canonical_pos: that is the
    only case where the shift is a pure offset and needs no alignment.
    """
    variants = {v["id"]: v for v in splice_variants(rec)}
    if vsp_id not in variants:
        raise AnalysisError(
            f"{name_of(rec)} has no Alternative sequence feature {vsp_id}; "
            f"available: {sorted(variants) or '(none)'}"
        )
    v = variants[vsp_id]
    if v["end"] >= canonical_pos:
        raise AnalysisError(
            f"{vsp_id} spans {v['start']}..{v['end']}, which reaches canonical position "
            f"{canonical_pos}; this offset calculation only holds for a variant entirely upstream"
        )
    removed = v["end"] - v["start"] + 1
    added = len(v["replacement"])
    shift = added - removed
    canonical = seq_of(rec)
    isoform_seq = canonical[: v["start"] - 1] + v["replacement"] + canonical[v["end"] :]
    pos = canonical_pos + shift
    return {
        "vsp": vsp_id,
        "vsp_span": f"{v['start']}..{v['end']}",
        "vsp_description": v["description"],
        "residues_removed": removed,
        "residues_added": added,
        "offset": shift,
        "canonical_position": canonical_pos,
        "canonical_residue": canonical[canonical_pos - 1],
        "isoform_position": pos,
        "isoform_residue": isoform_seq[pos - 1],
        "isoform_length": len(isoform_seq),
    }


# The residue the literature names for this site, and the numbering it uses.
# PMID:33999959, Fig 2C legend: "the site that is structurally equivalent to the
# arginine finger (Thr227)". Which isoform that numbering belongs to is NOT assumed --
# it is identified by which UniProt splice variant reproduces it.
PUBLISHED_SITE_POSITION = 227
PUBLISHED_SITE_RESIDUE = "T"


def isoform_crosscheck(rec: dict[str, Any], canonical_pos: int) -> dict[str, Any]:
    """Recompute the site's position under every upstream splice variant.

    No variant is chosen in advance. Each is applied and the resulting position
    reported, and the published number is then looked for among the results. Picking a
    variant first and reporting whether it matched would let a wrong pick masquerade as
    a refutation of the literature.
    """
    upstream = [v for v in splice_variants(rec) if v["end"] < canonical_pos]
    if not upstream:
        raise AnalysisError("no Alternative sequence feature lies upstream of the arginine-finger site")
    rows = [isoform_position(rec, canonical_pos, v["id"]) for v in upstream]
    canonical_row = {
        "vsp": "(canonical)",
        "vsp_span": "—",
        "vsp_description": "isoform 1, displayed sequence",
        "residues_removed": 0,
        "residues_added": 0,
        "offset": 0,
        "canonical_position": canonical_pos,
        "canonical_residue": seq_of(rec)[canonical_pos - 1],
        "isoform_position": canonical_pos,
        "isoform_residue": seq_of(rec)[canonical_pos - 1],
        "isoform_length": len(seq_of(rec)),
    }
    all_rows = [canonical_row] + rows
    matches = [
        r
        for r in all_rows
        if r["isoform_position"] == PUBLISHED_SITE_POSITION and r["isoform_residue"] == PUBLISHED_SITE_RESIDUE
    ]
    return {
        "published_position": PUBLISHED_SITE_POSITION,
        "published_residue": PUBLISHED_SITE_RESIDUE,
        "rows": all_rows,
        "matching_variants": [r["vsp"] for r in matches],
        "reproduced": len(matches) == 1,
        "ambiguous": len(matches) > 1,
    }


# --- analysis 5 -----------------------------------------------------------------


def fetch_rhogap_family() -> list[dict[str, Any]]:
    """Every reviewed human protein carrying the PROSITE RhoGAP profile."""
    query = urllib.parse.quote(f"(xref:prosite-{RHOGAP_PROSITE}) AND (organism_id:9606) AND (reviewed:true)")
    url = (
        f"https://rest.uniprot.org/uniprotkb/search?query={query}"
        "&format=json&size=500&fields=accession,id,protein_name,ft_site,cc_function,sequence"
    )
    raw = _fetch(url, CACHE_DIR / f"family_{RHOGAP_PROSITE}.json")
    payload = json.loads(raw)
    results = payload.get("results", [])
    if not results:
        raise AnalysisError(f"PROSITE {RHOGAP_PROSITE} search returned no reviewed human entries")
    return results


def family_census(members: list[dict[str, Any]], query_acc: str) -> dict[str, Any]:
    rows = []
    for rec in members:
        finger = arginine_finger(rec)
        if finger is None:
            rows.append({"accession": rec["primaryAccession"], "entry": name_of(rec), "site": None, "residue": None})
            continue
        rows.append(
            {
                "accession": rec["primaryAccession"],
                "entry": name_of(rec),
                "site": finger["position"],
                "residue": finger["residue"],
            }
        )
    annotated = [r for r in rows if r["site"] is not None]
    holds_r = [r for r in annotated if r["residue"] == "R"]
    flagged = [r for r in annotated if r["residue"] != "R"]
    if query_acc not in {r["accession"] for r in rows}:
        raise AnalysisError(
            f"the query {query_acc} is absent from the reviewed human {RHOGAP_PROSITE} set; "
            "the census is not about the family the query belongs to"
        )
    return {
        "entries": len(rows),
        "with_annotated_finger": len(annotated),
        "without_annotated_finger": len(rows) - len(annotated),
        "holds_arginine": len(holds_r),
        "does_not_hold_arginine": len(flagged),
        "flagged": sorted(flagged, key=lambda r: r["entry"]),
        "query_flagged": any(r["accession"] == query_acc for r in flagged),
    }


# --- analysis 6 -----------------------------------------------------------------


def fetch_structure(pdb_id: str) -> Any:
    raw = _fetch(f"https://files.rcsb.org/download/{pdb_id.lower()}.cif", CACHE_DIR / f"{pdb_id.lower()}.cif", binary=True)
    path = CACHE_DIR / f"{pdb_id.lower()}.cif"
    if not raw:
        raise AnalysisError(f"empty structure file for {pdb_id}")
    return FastMMCIFParser(QUIET=True).get_structure(pdb_id, str(path))


def chain_observed_sequence(chain: Any) -> tuple[str, list[int]]:
    seq, nums = [], []
    for res in chain:
        if res.id[0] != " ":
            continue
        try:
            seq.append(protein_letters_3to1[res.get_resname()])
        except KeyError:
            continue
        nums.append(res.id[1])
    return "".join(seq), nums


def prove_chain_identity(observed: str, reference: str, label: str, min_identity: float = 0.9) -> float:
    aln = make_aligner("local").align(observed, reference)[0]
    same = sum(
        1
        for (o0, o1), (r0, _r1) in zip(aln.aligned[0], aln.aligned[1])
        for off in range(int(o1) - int(o0))
        if observed[int(o0) + off] == reference[int(r0) + off]
    )
    identity = same / max(1, len(observed))
    if identity < min_identity:
        raise AnalysisError(
            f"{label}: observed chain is only {identity:.1%} identical to the reference sequence; "
            "the chain roles in the structure are not what this analysis assumes"
        )
    return identity


def gap_interface(structure: Any, gap_rec: dict[str, Any]) -> dict[str, Any]:
    model = structure[0]
    gap_chain = model[GAP_CHAIN]
    gtpase_chain = model[GTPASE_CHAIN]

    gap_obs, gap_nums = chain_observed_sequence(gap_chain)
    gtp_obs, _ = chain_observed_sequence(gtpase_chain)
    gap_identity = prove_chain_identity(gap_obs, seq_of(gap_rec), f"{INTERFACE_PDB} chain {GAP_CHAIN}")
    gtp_identity = prove_chain_identity(gtp_obs, seq_of(fetch_uniprot(RHOA_ACC)), f"{INTERFACE_PDB} chain {GTPASE_CHAIN}")

    partner_atoms = [a for r in gtpase_chain for a in r if r.id[0] == " "]
    seen_ligands: set[str] = set()
    for chain in model:
        for res in chain:
            if res.id[0] == " ":
                continue
            resname = res.get_resname().strip()
            if resname in TS_LIGANDS:
                seen_ligands.add(resname)
                partner_atoms.extend(list(res))
    missing = TS_LIGANDS - seen_ligands
    if missing:
        raise AnalysisError(
            f"{INTERFACE_PDB} is missing expected transition-state ligands {sorted(missing)}; "
            "this is not the transition-state mimic the analysis requires"
        )
    ns = NeighborSearch(partner_atoms)

    contacts_pdb = []
    for res in gap_chain:
        if res.id[0] != " ":
            continue
        if any(ns.search(atom.coord, CONTACT_CUTOFF_A) for atom in res):
            contacts_pdb.append(res.id[1])

    # The structure's own residue numbers are the construct's, not UniProt's. Map them
    # onto the UniProt sequence by alignment so that no residue number is *assumed* to
    # be a UniProt number: in 1TX4 the two differ by ~197 and a naive read puts every
    # contact in the wrong part of the protein.
    obs_to_ref = align_map(gap_obs, seq_of(gap_rec))
    num_to_index = {num: i + 1 for i, num in enumerate(gap_nums)}
    contacts = sorted({ref for num in contacts_pdb if (ref := obs_to_ref.get(num_to_index.get(num, -1))) is not None})
    if not contacts:
        raise AnalysisError("interface calculation produced no contacts mappable onto the UniProt sequence")

    finger = arginine_finger(gap_rec)
    if finger is None:
        raise AnalysisError(f"{name_of(gap_rec)} has no annotated arginine finger to sanity-check the geometry")
    if finger["position"] not in contacts:
        raise AnalysisError(
            f"the contact calculation did not recover {name_of(gap_rec)}'s own annotated arginine finger "
            f"({finger['position']}) among its {len(contacts)} contacts; the geometry is wrong"
        )
    return {
        "pdb": INTERFACE_PDB,
        "cutoff_angstrom": CONTACT_CUTOFF_A,
        "gap_chain_identity": round(gap_identity, 4),
        "gtpase_chain_identity": round(gtp_identity, 4),
        "ligands_included": sorted(seen_ligands),
        "contacts_in_pdb_numbering": sorted(contacts_pdb),
        "contacts": contacts,
        "recovered_control_finger": finger["position"],
        "observed_numbering_span": [min(gap_nums), max(gap_nums)] if gap_nums else None,
    }


def project_interface(
    gap_rec: dict[str, Any],
    contacts: list[int],
    query_rec: dict[str, Any],
    query_seq: str,
) -> dict[str, Any]:
    """Project the control's GAP:GTPase contacts onto ARHGAP36, domain to domain.

    Accepted only if the control's own arginine finger lands on ARHGAP36's own
    annotated site; without that reciprocal anchor the whole interface can be placed
    out of register and the retained/lost counts are meaningless.
    """
    c0, c1 = rhogap_domain(gap_rec)
    finger = arginine_finger(gap_rec)
    query_site = arginine_finger(query_rec)
    assert finger is not None and query_site is not None
    anchor = project_domain_position(gap_rec, seq_of(gap_rec), query_rec, query_seq, finger["position"])
    in_register = anchor == query_site["position"]

    rows = []
    for pos in contacts:
        if not (c0 <= pos <= c1):
            rows.append({"control_position": pos, "inside_control_domain": False, "query_position": None, "query_residue": None})
            continue
        proj = project_domain_position(gap_rec, seq_of(gap_rec), query_rec, query_seq, pos)
        rows.append(
            {
                "control_position": pos,
                "control_residue": seq_of(gap_rec)[pos - 1],
                "inside_control_domain": True,
                "query_position": proj,
                "query_residue": None if proj is None else query_seq[proj - 1],
                "identical": None if proj is None else query_seq[proj - 1] == seq_of(gap_rec)[pos - 1],
            }
        )
    mapped = [r for r in rows if r["query_position"] is not None]
    identical = [r for r in mapped if r.get("identical")]
    return {
        "anchor_in_register": in_register,
        "anchor_projected_to": anchor,
        "query_own_site": query_site["position"],
        "control_contacts": len(contacts),
        "inside_control_domain": sum(1 for r in rows if r["inside_control_domain"]),
        "mapped_onto_query": len(mapped),
        "unmapped": sum(1 for r in rows if r["inside_control_domain"] and r["query_position"] is None),
        "identical_residue": len(identical),
        "rows": rows,
    }


# --- driver ---------------------------------------------------------------------


def run(query_seq_override: str | None = None, control_overrides: dict[str, str] | None = None) -> dict[str, Any]:
    query_rec = fetch_uniprot(QUERY_ACC)
    query_seq = query_seq_override if query_seq_override is not None else seq_of(query_rec)
    if len(query_seq) != len(seq_of(query_rec)):
        raise AnalysisError("query sequence override changed the length; positions would no longer be comparable")

    control_recs = {acc: fetch_uniprot(acc) for acc in CONTROLS}
    for acc, replacement in (control_overrides or {}).items():
        rec = control_recs[acc]
        if len(replacement) != len(seq_of(rec)):
            raise AnalysisError("control sequence override changed the length")
        rec["sequence"] = dict(rec["sequence"], value=replacement)

    own = arginine_finger(query_rec)
    if own is None:
        raise AnalysisError(f"{QUERY_ACC} has no annotated arginine finger; this analysis has nothing to test")
    own = dict(own, residue=query_seq[own["position"] - 1])
    claim = gap_activity_claim(query_rec)

    q0, q1 = rhogap_domain(query_rec)
    res: dict[str, Any] = {
        "query": {
            "accession": QUERY_ACC,
            "entry": name_of(query_rec),
            "length": len(query_seq),
            "rho_gap_domain": [q0, q1],
            "arginine_finger_site": own,
            "gap_activity_function_comment": claim,
            "all_sites": site_features(query_rec),
        }
    }

    res["projection"] = projection_table(query_rec, query_seq, control_recs)
    res["method_controls"] = method_control_matrix(control_recs)

    projected = {r["projected_query_position"] for r in res["projection"] if r["projected_query_position"]}
    res["projection_consensus"] = {
        "distinct_projected_positions": sorted(projected),
        "unanimous": len(projected) == 1,
        "agrees_with_uniprot_site": projected == {own["position"]},
    }

    centre = own["position"]
    res["escape"] = escape_scan(query_seq, centre)

    res["isoform_crosscheck"] = isoform_crosscheck(query_rec, centre)

    family = fetch_rhogap_family()
    res["family"] = family_census(family, QUERY_ACC)
    for acc, label in (("O54834", "paint_seed"), ("O43182", "human_paralog")):
        rec = control_recs[acc]
        f = arginine_finger(rec)
        res["family"][label] = {
            "accession": acc,
            "entry": name_of(rec),
            "site": None if f is None else f["position"],
            "residue": None if f is None else f["residue"],
        }
    neg = fetch_uniprot(NEGATIVE_REFERENCE_ACC)
    neg_f = arginine_finger(neg)
    res["family"]["negative_reference"] = {
        "accession": NEGATIVE_REFERENCE_ACC,
        "entry": name_of(neg),
        "site": None if neg_f is None else neg_f["position"],
        "residue": None if neg_f is None else neg_f["residue"],
    }
    dec = fetch_uniprot(DECOUPLING_ACC)
    dec_f = arginine_finger(dec)
    res["family"]["decoupling_control"] = {
        "accession": DECOUPLING_ACC,
        "entry": name_of(dec),
        "site": None if dec_f is None else dec_f["position"],
        "residue": None if dec_f is None else dec_f["residue"],
    }

    gap_rec = control_recs["Q07960"]
    structure = fetch_structure(INTERFACE_PDB)
    res["interface"] = gap_interface(structure, gap_rec)
    res["interface_projection"] = project_interface(gap_rec, res["interface"]["contacts"], query_rec, query_seq)

    # A conservation percentage means nothing without a scale. The same interface is
    # projected onto the PAINT seed -- a family member whose GAP activity is the
    # experimental basis of the IBD under review -- so the query's score can be read
    # against what a working member of this family scores on the same measurement.
    seed_rec = control_recs["O54834"]
    seed_proj = project_interface(gap_rec, res["interface"]["contacts"], seed_rec, seq_of(seed_rec))
    res["interface_projection_baseline"] = {
        "accession": "O54834",
        "entry": name_of(seed_rec),
        "role": "PAINT/IBD seed, experimentally GAP-active",
        **{k: v for k, v in seed_proj.items() if k != "rows"},
    }

    return res


# --- self-test ------------------------------------------------------------------


def _mutate(seq: str, pos: int, new: str, expect: str) -> str:
    if seq[pos - 1] != expect:
        raise AnalysisError(f"self-test anchor drift: position {pos} holds {seq[pos - 1]!r}, expected {expect!r}")
    return seq[: pos - 1] + new + seq[pos:]


def self_test() -> int:
    failures: list[str] = []

    def check(label: str, cond: bool, detail: str = "") -> None:
        if cond:
            print(f"  ok    {label}")
        else:
            failures.append(f"{label}: {detail}")
            print(f"  FAIL  {label}: {detail}")

    print("self-test")
    base = run()
    site = base["query"]["arginine_finger_site"]["position"]
    query_seq = seq_of(fetch_uniprot(QUERY_ACC))

    # 1. Baseline: what the analysis is here to establish.
    check(
        "baseline: the annotated arginine-finger position does not hold an arginine",
        base["query"]["arginine_finger_site"]["residue"] != "R",
        f"residue is {base['query']['arginine_finger_site']['residue']}",
    )
    check(
        "baseline: the projection is unanimous and agrees with UniProt's own site",
        base["projection_consensus"]["unanimous"] and base["projection_consensus"]["agrees_with_uniprot_site"],
        json.dumps(base["projection_consensus"]),
    )
    check(
        "baseline: every method control recovers the target's own arginine finger",
        all(r["recovered"] for r in base["method_controls"]),
        json.dumps([r for r in base["method_controls"] if not r["recovered"]]),
    )

    # 2. Restore the arginine: the verdict must flip, and the escape scan must find it
    #    at offset 0. A test that cannot flip is not measuring anything.
    restored = _mutate(query_seq, site, "R", query_seq[site - 1])
    mut = run(query_seq_override=restored)
    check(
        "mutation: restoring R at the annotated site flips the residue verdict",
        mut["query"]["arginine_finger_site"]["residue"] == "R",
        f"got {mut['query']['arginine_finger_site']['residue']}",
    )
    check(
        "mutation: the escape scan then reports offset 0",
        mut["escape"]["nearest_offset"] == 0,
        f"got {mut['escape']['nearest_offset']}",
    )

    # 3. Negative control: a mutation far from every anchor must change no verdict.
    far = site + 60
    if far >= len(query_seq):
        far = site - 60
    quiet = _mutate(query_seq, far, "A" if query_seq[far - 1] != "A" else "G", query_seq[far - 1])
    quiet_res = run(query_seq_override=quiet)
    check(
        "negative control: a distant substitution leaves the residue verdict unchanged",
        quiet_res["query"]["arginine_finger_site"]["residue"] == base["query"]["arginine_finger_site"]["residue"],
        "a distant substitution changed the verdict",
    )
    check(
        "negative control: a distant substitution leaves the escape scan unchanged",
        quiet_res["escape"]["nearest_arginine"] == base["escape"]["nearest_arginine"],
        f"{quiet_res['escape']['nearest_arginine']} != {base['escape']['nearest_arginine']}",
    )

    # 4. Break a control: a control that has lost its own arginine must be rejected
    #    rather than silently anchoring the projection.
    ctrl_rec = fetch_uniprot("Q07960")
    ctrl_site = arginine_finger(ctrl_rec)["position"]
    broken = _mutate(seq_of(ctrl_rec), ctrl_site, "A", "R")
    try:
        run(control_overrides={"Q07960": broken})
    except AnalysisError as exc:
        check("guard: a control without its own arginine is refused", "cannot anchor this test" in str(exc), str(exc))
    else:
        check("guard: a control without its own arginine is refused", False, "no error raised")

    # 5. The 'inactive' substring trap, regression-tested with the exact sentence that
    #    caused it. ARHGAP36's FUNCTION line contains 'inactive GDP-bound state', which
    #    describes the GTPase, not ARHGAP36.
    claim = base["query"]["gap_activity_function_comment"]
    check(
        "guard: the FUNCTION claim reader anchors on 'GTPase activator', not 'active'",
        claim is not None and "GTPase activator" in claim["text"],
        json.dumps(claim),
    )
    fake = {"comments": [{"commentType": "FUNCTION", "texts": [{"value": "Converts them to an inactive GDP-bound state."}]}]}
    check(
        "guard: an 'inactive GDP-bound state' sentence alone is not read as a GAP claim",
        gap_activity_claim(fake) is None,
        "the substring trap fired",
    )

    # 6. Isoform arithmetic must be refused when the variant overlaps the site.
    iso = base["isoform_crosscheck"]
    a_variant = next(r["vsp"] for r in iso["rows"] if r["vsp"] != "(canonical)")
    try:
        isoform_position(fetch_uniprot(QUERY_ACC), 10, a_variant)
    except AnalysisError as exc:
        check("guard: isoform offset refused when the variant reaches the site", "entirely upstream" in str(exc), str(exc))
    else:
        check("guard: isoform offset refused when the variant reaches the site", False, "no error raised")

    # 7. The isoform cross-check must be able to FAIL. If it reports "reproduced" for a
    #    published number that no variant can produce, it is not a check.
    check(
        "baseline: the published residue is reproduced by exactly one variant",
        iso["reproduced"],
        f"matching variants: {iso['matching_variants']}",
    )
    impossible = isoform_crosscheck(fetch_uniprot(QUERY_ACC), site)
    impossible_positions = {r["isoform_position"] for r in impossible["rows"]}
    bogus = max(impossible_positions) + 1000
    saved = globals()["PUBLISHED_SITE_POSITION"]
    try:
        globals()["PUBLISHED_SITE_POSITION"] = bogus
        flipped = isoform_crosscheck(fetch_uniprot(QUERY_ACC), site)
    finally:
        globals()["PUBLISHED_SITE_POSITION"] = saved
    check(
        "mutation: an unreachable published position is reported as NOT reproduced",
        not flipped["reproduced"] and not flipped["ambiguous"],
        json.dumps({"reproduced": flipped["reproduced"], "matching": flipped["matching_variants"]}),
    )

    print("PASS" if not failures else f"{len(failures)} FAILURE(S)")
    return 0 if not failures else 1


# --- report ---------------------------------------------------------------------


def _yn(v: Any) -> str:
    return "**yes**" if v is True else ("no" if v is False else "—")


def render_markdown(res: dict[str, Any]) -> str:
    q = res["query"]
    site = q["arginine_finger_site"]
    claim = q["gap_activity_function_comment"]
    esc = res["escape"]
    iso = res["isoform_crosscheck"]
    fam = res["family"]
    ip = res["interface_projection"]
    L: list[str] = []
    A = L.append

    A("# ARHGAP36: the arginine finger UniProt annotates, and the residue that is there")
    A("")
    A("Every number below is produced by `analyze_arhgap36.py` in this directory.")
    A("Re-run it to regenerate this file; do not hand-edit.")
    A("")
    A("```")
    A('uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py')
    A('uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py --self-test')
    A("```")
    A("")

    A("## 1. What the UniProt entry says about itself")
    A("")
    A(f"| | |")
    A("|---|---|")
    A(f"| entry | `{q['entry']}` ({q['accession']}), {q['length']} aa |")
    A(f"| Rho-GAP DOMAIN | {q['rho_gap_domain'][0]}..{q['rho_gap_domain'][1]} |")
    A(f"| annotated arginine-finger Site | **{site['position']}** |")
    A(f"| evidence on that Site | `{', '.join(site['evidence']) or '—'}` |")
    A(f"| residue actually at that position | **{site['residue']}** |")
    if claim:
        A(f"| FUNCTION comment asserting GAP activity | \"{claim['text']}\" |")
        A(f"| evidence on that comment | `{', '.join(claim['evidence']) or '—'}` |")
    else:
        A("| FUNCTION comment asserting GAP activity | *(none)* |")
    A("")
    A(
        f"The entry therefore annotates a catalytic arginine at {site['position']} and carries "
        f"{site['residue']} there, while asserting GTPase-activator activity on "
        f"`{', '.join(claim['evidence']) if claim else '—'}`. Both statements are rule- or "
        "similarity-derived; neither is experimental."
    )
    A("")

    A("## 2. Is that Site in register?")
    A("")
    A(
        "A ProRule Site is placed by profile alignment and can be misplaced, so the position is "
        "re-derived from controls that carry their own annotated arginine finger. Each control's "
        "finger is projected onto ARHGAP36 Rho-GAP domain to Rho-GAP domain."
    )
    A("")
    A("| control | entry | its own site | residue | projects onto ARHGAP36 | residue there | same as ARHGAP36's own Site |")
    A("|---|---|---|---|---|---|---|")
    for r in res["projection"]:
        A(
            f"| {r['control']} | `{r['control_entry']}` | {r['control_site']} | {r['control_residue']} | "
            f"**{r['projected_query_position']}** | **{r['projected_query_residue']}** | {_yn(r['agrees_with_query_site'])} |"
        )
    A("")
    cons = res["projection_consensus"]
    A(
        f"Distinct positions the controls project onto: {cons['distinct_projected_positions']}. "
        f"Unanimous: {_yn(cons['unanimous'])}. Agrees with UniProt's own Site: "
        f"{_yn(cons['agrees_with_uniprot_site'])}."
    )
    A("")
    A("Method control — every control projected onto every other control must recover a known arginine finger:")
    A("")
    A("| from | to | projected | target's own site | recovered | residue |")
    A("|---|---|---|---|---|---|")
    for r in res["method_controls"]:
        A(f"| `{r['from']}` | `{r['to']}` | {r['projected']} | {r['target_own_site']} | {_yn(r['recovered'])} | {r['projected_residue']} |")
    A("")

    A("## 3. Could the arginine simply have moved?")
    A("")
    A(
        f"The only result that would rescue the annotation is an arginine displaced by a residue or "
        f"two. A window of ±{esc['half_width']} residues around position {esc['centre']} was scanned."
    )
    A("")
    A(f"| | |")
    A("|---|---|")
    A(f"| window | {esc['window']} |")
    A(f"| sequence | `{esc['window_sequence']}` |")
    A(f"| arginines in window | {esc['arginines_in_window'] or '*(none)*'} |")
    A(f"| nearest arginine | {esc['nearest_arginine'] if esc['nearest_arginine'] else '*(none)*'} |")
    A(f"| offset from the annotated site | {esc['nearest_offset'] if esc['nearest_offset'] is not None else '—'} |")
    A("")

    A("## 4. Does the sequence record agree with the published residue?")
    A("")
    A(
        f"PMID:33999959 names the equivalent position **{iso['published_residue']}{iso['published_position']}**, "
        "in the numbering of whichever isoform that paper worked in. Rather than assume which, the site "
        "is recomputed under the canonical sequence and under every UniProt splice variant lying wholly "
        "upstream of it, and the published number is looked for among the results."
    )
    A("")
    A("| variant | span | description | net offset | position of the site | residue | isoform length |")
    A("|---|---|---|---|---|---|---|")
    for r in iso["rows"]:
        hit = r["isoform_position"] == iso["published_position"] and r["isoform_residue"] == iso["published_residue"]
        mark = " ←" if hit else ""
        A(
            f"| `{r['vsp']}` | {r['vsp_span']} | {r['vsp_description']} | {r['offset']:+d} | "
            f"**{r['isoform_position']}**{mark} | **{r['isoform_residue']}** | {r['isoform_length']} aa |"
        )
    A("")
    if iso["reproduced"]:
        A(
            f"Exactly one variant reproduces `{iso['published_residue']}{iso['published_position']}`: "
            f"`{iso['matching_variants'][0]}`. So the published residue and the UniProt Site are the same "
            "residue, reached by two independent routes — a profile-based annotation rule and a "
            "mutagenesis paper's own construct numbering — and the threonine call does not depend on "
            "either one alone."
        )
    elif iso["ambiguous"]:
        A(
            f"More than one variant reproduces the published number ({iso['matching_variants']}), so this "
            "cross-check does not identify a unique isoform and cannot corroborate the residue."
        )
    else:
        A(
            f"No canonical or upstream-variant numbering reproduces "
            f"`{iso['published_residue']}{iso['published_position']}`. The published residue and the "
            "UniProt Site have **not** been shown to be the same residue by this check."
        )
    A("")

    A("## 5. Is the loss ARHGAP36's, or the family's?")
    A("")
    A("| role | accession | entry | annotated site | residue |")
    A("|---|---|---|---|---|")
    for key, label in (
        ("paint_seed", "PAINT/IBD seed (MGI:1196332)"),
        ("human_paralog", "human paralog, same PANTHER family"),
        ("negative_reference", "binds a RHO GTPase without catalysing (reference)"),
        ("decoupling_control", "retains R but is experimentally GAP-dead"),
    ):
        r = fam[key]
        A(f"| {label} | {r['accession']} | `{r['entry']}` | {r['site']} | **{r['residue']}** |")
    A(f"| **query** | {q['accession']} | `{q['entry']}` | {site['position']} | **{site['residue']}** |")
    A("")
    A(f"Across all reviewed human proteins carrying the PROSITE RhoGAP profile {RHOGAP_PROSITE}:")
    A("")
    A("| | count |")
    A("|---|---|")
    A(f"| entries | {fam['entries']} |")
    A(f"| with an annotated arginine finger | {fam['with_annotated_finger']} |")
    A(f"| that position holds R | {fam['holds_arginine']} |")
    A(f"| that position does not hold R | {fam['does_not_hold_arginine']} |")
    A("")
    A("Entries whose annotated arginine-finger position does not hold an arginine:")
    A("")
    A("| entry | residue |")
    A("|---|---|")
    for r in fam["flagged"]:
        A(f"| `{r['entry']}` | {r['residue']} |")
    A("")
    A(
        f"The query is among them: {_yn(fam['query_flagged'])}. The decoupling control "
        f"(`{fam['decoupling_control']['entry']}`) is **not** — it keeps its arginine and is "
        "nonetheless experimentally GAP-dead, so a retained arginine is not evidence of activity. "
        "The inference this report supports runs only in the other direction."
    )
    A("")

    A("## 6. Catalysis versus binding")
    A("")
    A(
        f"UniProt records an experimental RAC1 interaction via ARHGAP36's Rho-GAP domain. Losing the "
        f"catalytic arginine does not by itself remove the binding surface, so the two are counted "
        f"separately. The GAP:GTPase interface is taken from PDB {res['interface']['pdb']} "
        f"(p50RhoGAP:RhoA:GDP:AlF4), as every GAP residue with an atom within "
        f"{res['interface']['cutoff_angstrom']} A of the GTPase or of the nucleotide/metal/fluoride."
    )
    A("")
    A(
        f"Chain roles are proved, not assumed: chain {GAP_CHAIN} is "
        f"{res['interface']['gap_chain_identity']:.1%} identical to Q07960 and chain {GTPASE_CHAIN} is "
        f"{res['interface']['gtpase_chain_identity']:.1%} identical to {RHOA_ACC}. The calculation "
        f"recovers the control's own annotated arginine finger ({res['interface']['recovered_control_finger']}) "
        "among its contacts, as it must."
    )
    A("")
    A("| | count |")
    A("|---|---|")
    A(f"| control GAP:GTPase contacts | {ip['control_contacts']} |")
    A(f"| inside the control's Rho-GAP domain | {ip['inside_control_domain']} |")
    A(f"| projected onto ARHGAP36 | {ip['mapped_onto_query']} |")
    A(f"| unmapped (aligned to a gap) | {ip['unmapped']} |")
    A(f"| identical residue in ARHGAP36 | {ip['identical_residue']} |")
    A("")
    A(
        f"Projection in register (control's finger lands on ARHGAP36's own Site "
        f"{ip['query_own_site']}): {_yn(ip['anchor_in_register'])}."
    )
    A("")
    A("| control pos | control res | ARHGAP36 pos | ARHGAP36 res | identical |")
    A("|---|---|---|---|---|")
    for r in ip["rows"]:
        if not r["inside_control_domain"]:
            continue
        A(
            f"| {r['control_position']} | {r['control_residue']} | {r['query_position']} | "
            f"{r['query_residue']} | {_yn(r.get('identical'))} |"
        )
    A("")
    base = res["interface_projection_baseline"]
    frac = ip["identical_residue"] / ip["mapped_onto_query"] if ip["mapped_onto_query"] else 0.0
    base_frac = base["identical_residue"] / base["mapped_onto_query"] if base["mapped_onto_query"] else 0.0
    A(
        f"{ip['identical_residue']} of {ip['mapped_onto_query']} projected interface positions "
        f"({frac:.0%}) are identical in ARHGAP36. A percentage alone has no scale, so the same interface "
        f"was projected onto `{base['entry']}` ({base['accession']}), the {base['role']} — the member of "
        f"this family whose experiments are the basis of the IBD under review. It scores "
        f"{base['identical_residue']}/{base['mapped_onto_query']} ({base_frac:.0%})."
    )
    A("")
    A(
        "So the GTPase-contacting surface is conserved in ARHGAP36 to a degree "
        + ("comparable to" if abs(frac - base_frac) < 0.10 else ("below" if frac < base_frac else "above"))
        + " the family member that does catalyse, while the one residue that performs the catalysis is "
        "not conserved. That is the configuration in which a domain can still engage a GTPase without "
        "accelerating its hydrolysis — the shape `OCRL_HUMAN` is documented to have. This is a statement "
        "about what the structure permits, not a measurement of binding: the binding claim rests on the "
        "curated experiment, not on this table."
    )
    A("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true", help="break the inputs on purpose and assert each check notices")
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
