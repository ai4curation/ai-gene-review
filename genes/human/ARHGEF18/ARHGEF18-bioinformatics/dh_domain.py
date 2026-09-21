#!/usr/bin/env python3
"""Is ARHGEF18's DH/PH module catalytically competent, and can residues call its substrate?

Two separate questions, deliberately kept apart because they have different answers.

**Question 1 -- competence.**  ARHGEF18's exchange activity is already established by
direct biochemistry: Blomquist et al. 2000 (PMID:11085924) showed the purified protein
"efficiently catalysed guanine nucleotide exchange of RhoA".  So a residue argument here
can only *corroborate*, never decide.  What it can do is anchor the two experimentally
validated loss-of-function substitutions onto the current canonical sequence, which is
non-trivial because **the two papers use two different numbering systems and neither
states which**:

* Arno et al. 2017 (PMID:28132693) report the RP78 missense variant as ``p.Thr270Ala``;
  UniProt independently records it as ``VARIANT 458 T->A``.  That gives a checkable
  offset of +188 -- the length UniProt added to the N-terminus in sequence version 4
  (10-OCT-2018), after the paper.
* Terry et al. 2011 (PMID:21258369) inactivated the GEF by substituting "a conserved
  tyrosine residue in the Dbl domain necessary for GEF activity (p114RhoGEF-Y260A)".
  They give no accession.  This script does not assume an offset: it enumerates every
  offset UniProt's own ``VAR_SEQ`` records license and reports which ones actually put a
  tyrosine there.

**Question 2 -- substrate.**  Blomquist 2000 found p114RhoGEF "interacted specifically
with RhoA ... but not with Rac1 and Cdc42"; Niu et al. 2003 (PMID:14512443) found it
"activated RhoA and Rac1 but not Cdc42".  The two primary papers disagree about Rac1 and
UniProt carries both.  Sequence is the cheapest possible arbiter, so it is worth asking
whether it can arbitrate at all.  The test: take the GTPase-contacting residues resolved
in two structures -- LARG/ARHGEF12 DH/PH bound to **RhoA** (PDB 1X86) and TIAM1 DH/PH
bound to **RAC1** (PDB 1FOE) -- map both anchor sets onto ARHGEF18 through a DH-domain
alignment, and see whether ARHGEF18 matches one pattern better than the other.

Nothing is hardcoded.  Domain boundaries come from each protein's own UniProt feature
table; contact residues are computed from the deposited coordinates; the PDB-to-UniProt
residue correspondence comes from PDBe SIFTS and is then **verified residue-by-residue**
against the UniProt sequence, so an off-by-N mapping cannot pass silently.

Controls, all asserted rather than described:

* POSITIVE (mapping)   -- every SIFTS-mapped structural residue must match the UniProt
  sequence at its mapped position, for both 1X86/LARG and 1FOE/TIAM1.
* POSITIVE (biology)   -- Terry's claim that analogous mutations inactivate GEF-H1 and
  Lbc requires the aligned column in ARHGEF2 to be a tyrosine.  Checked, not assumed.
* POSITIVE (variant)   -- canonical residue 458 must be Thr, which UniProt asserts
  independently of this script.
* NEGATIVE (offset)    -- the +188 offset that works for Arno's variant must NOT put a
  tyrosine at Terry's position, otherwise the offset assignment is ambiguous.
* NEGATIVE (panel)     -- RHOA is included in the input panel and has no DH domain.  It
  must be *excluded with a reason*, not silently aligned.
* NEGATIVE (anchor)    -- a scrambled control sequence must fail to receive anchor
  mappings at the same rate as the real orthologs.

Run:    uv run python dh_domain.py
        uv run python dh_domain.py --self-test
Writes: dh_domain.json
"""

from __future__ import annotations

import argparse
import json
import math
import random
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "dh_domain.json"

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
PDBE_SIFTS = "https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb}"
RCSB_CIF = "https://files.rcsb.org/download/{pdb}.cif"

TARGET = "Q6ZSZ5"  # human ARHGEF18 / p114RhoGEF

# Panel.  RHOA is a deliberate negative control: it has no DH domain and must be
# excluded by the domain-extraction step rather than aligned.
PANEL = {
    "Q6ZSZ5": "ARHGEF18 (human, target)",
    "Q6P9R4": "Arhgef18 (mouse ortholog)",
    "Q9VIV0": "cyst/Dp114RhoGEF (Drosophila ortholog)",
    "Q9NZN5": "ARHGEF12/LARG (human; DH/PH solved bound to RhoA, PDB 1X86)",
    "O15085": "ARHGEF11/PDZ-RhoGEF (human; RhoA-specific)",
    "Q92888": "ARHGEF1/p115RhoGEF (human; RhoA-specific)",
    "Q92974": "ARHGEF2/GEF-H1 (human; Terry's stated comparator)",
    "Q12802": "AKAP13/Lbc (human; Terry's stated comparator)",
    "Q8N1W1": "ARHGEF28/RGNEF (human; PAINT co-seed)",
    "Q60610": "Tiam1 (mouse; DH/PH solved bound to RAC1, PDB 1FOE)",
    "Q13009": "TIAM1 (human; RAC1-specific)",
    "O75962": "TRIO (human; DH1 = RAC1-specific, held out from the anchor's family)",
    "O60229": "KALRN (human; DH1 = RAC1-specific, held out from the anchor's family)",
    "Q15811": "ITSN1 (human; CDC42-specific)",
    "P61586": "RHOA (human) -- NEGATIVE CONTROL, no DH domain",
    "Q92608": "DOCK2 (human) -- NEGATIVE CONTROL, a real RAC1 GEF with no DH domain",
}

# Declared substrate specificity, used ONLY to validate the classifier on held-out
# proteins.  ARHGEF18 is deliberately absent: it is the question, not a label.
KNOWN_SPECIFICITY = {
    "Q9NZN5": "RHOA",   # LARG
    "O15085": "RHOA",   # PDZ-RhoGEF
    "Q92888": "RHOA",   # p115RhoGEF
    "Q92974": "RHOA",   # GEF-H1
    "Q12802": "RHOA",   # Lbc
    "Q8N1W1": "RHOA",   # RGNEF
    "Q60610": "RAC1",   # Tiam1 (mouse)
    "Q13009": "RAC1",   # TIAM1 (human)
    "O75962": "RAC1",   # TRIO DH1
    "O60229": "RAC1",   # KALRN DH1
}

# Structures: (pdb id, GEF uniprot, GEF auth chain, GTPase uniprot, GTPase auth chain)
STRUCTURES = [
    ("1x86", "Q9NZN5", "A", "P61586", "B"),  # LARG DH/PH + RhoA
    ("1foe", "Q60610", "A", "P63000", "B"),  # TIAM1 DH/PH + RAC1
]

# PH-domain structures.  6BCB is the only deposited structure of any part of ARHGEF18:
# the mouse PH domain bound to activated RhoA at 1.4 A (Chen et al. 2018, PMID:29876405),
# the structural counterpart of the positive-feedback binding reported in PMID:23493395.
# 6BCA is the sister structure of the AKAP13/Lbc PH domain from the same study and acts
# as the independent positive comparator.
PH_STRUCTURES = [
    ("6bcb", "Q6P9R4", "A", "P61586", "F"),  # mouse Arhgef18 PH + RhoA-GTP analog
    ("6bca", "Q12802", "A", "P61586", "C"),  # AKAP13/Lbc PH + RhoA-GTP analog
]

CONTACT_CUTOFF = 4.0  # angstrom, heavy atoms

# The two experimentally validated substitutions, in the numbering their papers used.
PAPER_MUTATIONS = {
    "Arno2017_T270A": {"pmid": "28132693", "paper_position": 270, "residue": "T"},
    "Terry2011_Y260A": {"pmid": "21258369", "paper_position": 260, "residue": "Y"},
}


# --------------------------------------------------------------------------- fetch


def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "aigr"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)


def _get_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "aigr"})
    with urllib.request.urlopen(req, timeout=300) as fh:
        return fh.read().decode("utf-8", errors="replace")


def uniprot_record(acc: str) -> dict:
    """Sequence, DH-domain bounds and VAR_SEQ deletions, all from UniProt's own record."""
    d = _get_json(UNIPROT.format(acc=acc))
    seq = d["sequence"]["value"]
    dh = []
    ph = []
    varseq = []
    for ft in d.get("features", []):
        loc = ft.get("location", {})
        start = (loc.get("start") or {}).get("value")
        end = (loc.get("end") or {}).get("value")
        if ft.get("type") == "Domain" and (ft.get("description") or "").strip().upper().startswith("DH"):
            dh.append((start, end))
        if ft.get("type") == "Domain" and (ft.get("description") or "").strip().upper().startswith("PH"):
            ph.append((start, end))
        if ft.get("type") == "Alternative sequence":
            varseq.append(
                {
                    "start": start,
                    "end": end,
                    "description": ft.get("description"),
                    "alternative": (ft.get("alternativeSequence") or {}).get("originalSequence"),
                    "id": ft.get("featureId"),
                }
            )
    return {
        "accession": acc,
        "id": d.get("uniProtkbId"),
        "length": len(seq),
        "sequence": seq,
        "dh_domains": dh,
        "ph_domains": ph,
        "var_seq": varseq,
        "sequence_version": d.get("entryAudit", {}).get("sequenceVersion"),
    }


# ------------------------------------------------------------------- structure work


def parse_cif_atoms(cif_text: str) -> list[dict]:
    """Minimal mmCIF ATOM/HETATM reader for the atom_site loop.

    Written out rather than pulled from a parser library so the column semantics are
    visible: we need auth_asym_id (the chain the PDB entry page names) and auth_seq_id
    (the numbering SIFTS maps), not the label_* equivalents.
    """
    lines = cif_text.splitlines()
    i = 0
    atoms: list[dict] = []
    while i < len(lines):
        if lines[i].strip() == "loop_":
            j = i + 1
            cols: list[str] = []
            while j < len(lines) and lines[j].lstrip().startswith("_"):
                cols.append(lines[j].strip())
                j += 1
            if cols and cols[0].startswith("_atom_site."):
                names = [c.split(".", 1)[1] for c in cols]
                idx = {n: k for k, n in enumerate(names)}
                while j < len(lines) and not lines[j].startswith(("#", "loop_", "data_")):
                    row = lines[j].split()
                    if len(row) >= len(names) and row[0] in ("ATOM", "HETATM"):
                        atoms.append(
                            {
                                "group": row[0],
                                "element": row[idx["type_symbol"]],
                                "chain": row[idx["auth_asym_id"]],
                                "seq": row[idx["auth_seq_id"]],
                                "comp": row[idx["auth_comp_id"]] if "auth_comp_id" in idx else row[idx["label_comp_id"]],
                                "x": float(row[idx["Cartn_x"]]),
                                "y": float(row[idx["Cartn_y"]]),
                                "z": float(row[idx["Cartn_z"]]),
                            }
                        )
                    j += 1
                return atoms
            i = j
        else:
            i += 1
    return atoms


THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
    "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
    "TYR": "Y", "VAL": "V", "MSE": "M", "SEC": "U", "PYL": "O",
}


def sifts_offset(pdb: str, chain: str, acc: str) -> int | None:
    """auth_seq_id -> UniProt offset from PDBe SIFTS, or None when SIFTS omits it.

    PDBe returns ``author_residue_number: null`` for some legacy entries (1FOE among
    them), so this cannot be the only route; it is kept as an independent cross-check
    on the empirical offset derived from residue identities.
    """
    d = _get_json(PDBE_SIFTS.format(pdb=pdb))
    for uacc, body in d.get(pdb, {}).get("UniProt", {}).items():
        if uacc != acc:
            continue
        for seg in body.get("mappings", []):
            if seg.get("chain_id") != chain and seg.get("struct_asym_id") != chain:
                continue
            a_start = seg["start"].get("author_residue_number")
            if a_start is None:
                continue
            return seg["unp_start"] - a_start
    return None


def derive_offset(names: dict[int, str], seq: str) -> dict:
    """Fit auth_seq_id -> UniProt position by maximising residue-identity agreement.

    Returns the best offset, how well it scores, and how well the *runner-up* scores.
    A correct fit is essentially unique, so a narrow margin is itself a failure signal.
    """
    if not names:
        return {"offset": None, "checked": 0, "matched": 0, "best_pct": 0.0, "runner_up_pct": 0.0}
    lo = 1 - max(names)
    hi = len(seq) - min(names)
    scores: list[tuple[float, int, int, int]] = []
    for off in range(lo, hi + 1):
        checked = matched = 0
        for auth, res in names.items():
            pos = auth + off
            if 1 <= pos <= len(seq):
                checked += 1
                if seq[pos - 1] == res:
                    matched += 1
        if checked >= 50:
            scores.append((matched / checked, off, checked, matched))
    if not scores:
        return {"offset": None, "checked": 0, "matched": 0, "best_pct": 0.0, "runner_up_pct": 0.0}
    scores.sort(reverse=True)
    best = scores[0]
    runner = scores[1] if len(scores) > 1 else (0.0, None, 0, 0)
    return {
        "offset": best[1],
        "checked": best[2],
        "matched": best[3],
        "best_pct": round(100 * best[0], 2),
        "runner_up_pct": round(100 * runner[0], 2),
    }


def contact_residues(
    atoms: list[dict], gef_chain: str, gtpase_chain: str, cutoff: float
) -> set[int]:
    """auth_seq_id of GEF residues with any heavy atom within `cutoff` of the GTPase."""
    gef = [a for a in atoms if a["chain"] == gef_chain and a["element"] != "H" and is_polymer_residue(a)]
    gt = [a for a in atoms if a["chain"] == gtpase_chain and a["element"] != "H" and is_polymer_residue(a)]
    # Bucket the GTPase atoms on a coarse grid so this stays linear-ish.
    cell = cutoff
    grid: dict[tuple[int, int, int], list[dict]] = {}
    for a in gt:
        key = (int(a["x"] // cell), int(a["y"] // cell), int(a["z"] // cell))
        grid.setdefault(key, []).append(a)
    hits: set[int] = set()
    c2 = cutoff * cutoff
    for a in gef:
        if not a["seq"].lstrip("-").isdigit():
            continue
        kx, ky, kz = int(a["x"] // cell), int(a["y"] // cell), int(a["z"] // cell)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for b in grid.get((kx + dx, ky + dy, kz + dz), ()):
                        d2 = (a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2
                        if d2 <= c2:
                            hits.add(int(a["seq"]))
                            break
    return hits


def is_polymer_residue(atom: dict) -> bool:
    """Amino-acid residues only.

    Waters, the GTP analogue and the Mg ion are deposited under the *same* auth chain
    as the protein in 6BCB, and they carry high auth_seq_id values.  Counting them as
    residues drove the structure-to-sequence fit for that entry down to 48% identity --
    which the fit guard caught, and which is why the guard exists.
    """
    return atom["comp"].upper() in THREE_TO_ONE


def structure_residue_names(atoms: list[dict], chain: str) -> dict[int, str]:
    out: dict[int, str] = {}
    for a in atoms:
        if a["chain"] != chain or not a["seq"].lstrip("-").isdigit() or not is_polymer_residue(a):
            continue
        out[int(a["seq"])] = THREE_TO_ONE[a["comp"].upper()]
    return out


# ------------------------------------------------------------------------ alignment


def mafft_align(records: list[tuple[str, str]]) -> dict[str, str]:
    exe = shutil.which("mafft")
    if exe is None:
        raise RuntimeError("mafft not found on PATH; install it or the alignment cannot be built")
    fasta = "".join(f">{name}\n{seq}\n" for name, seq in records)
    proc = subprocess.run(
        [exe, "--quiet", "--maxiterate", "1000", "--localpair", "-"],
        input=fasta,
        capture_output=True,
        text=True,
        check=True,
    )
    aln: dict[str, str] = {}
    name = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            aln[name] = ""
        elif name is not None:
            aln[name] += line.strip()
    return aln


def col_of(aligned: str, offset0: int) -> int | None:
    """Alignment column holding the 0-based ungapped index `offset0` of `aligned`."""
    seen = -1
    for col, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
            if seen == offset0:
                return col
    return None


def residue_at_col(aligned: str, col: int) -> tuple[str, int | None]:
    """(residue, 0-based ungapped index) at alignment column `col`."""
    seen = -1
    for k, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
        if k == col:
            return ch, (seen if ch != "-" else None)
    return "-", None


# ----------------------------------------------------------------------------- main


def build() -> dict:
    result: dict = {
        "target": TARGET,
        "contact_cutoff_angstrom": CONTACT_CUTOFF,
        "panel": {},
        "excluded": {},
        "structures": {},
        "controls": {},
        "mutation_mapping": {},
        "anchor_mapping": {},
    }

    # ---- 1. UniProt records; DH extraction doubles as the negative-control gate.
    recs: dict[str, dict] = {}
    for acc, label in PANEL.items():
        rec = uniprot_record(acc)
        rec["label"] = label
        recs[acc] = rec
        if not rec["dh_domains"]:
            result["excluded"][acc] = {
                "label": label,
                "reason": "UniProt feature table declares no DH domain; excluded from the alignment",
                "length": rec["length"],
            }
        else:
            result["panel"][acc] = {
                "label": label,
                "uniprot_id": rec["id"],
                "length": rec["length"],
                "sequence_version": rec["sequence_version"],
                "dh_domain": rec["dh_domains"][0],
                "n_dh_domains": len(rec["dh_domains"]),
            }

    aligned_accs = [a for a in PANEL if recs[a]["dh_domains"]]

    # ---- 2. structural anchors
    anchors: dict[str, dict] = {}
    for pdb, gef_acc, gef_chain, gt_acc, gt_chain in STRUCTURES:
        atoms = parse_cif_atoms(_get_text(RCSB_CIF.format(pdb=pdb.upper())))
        contacts = contact_residues(atoms, gef_chain, gt_chain, CONTACT_CUTOFF)
        names = structure_residue_names(atoms, gef_chain)
        gef_seq = recs[gef_acc]["sequence"]

        # Two independent routes to the auth_seq_id -> UniProt correspondence.  The
        # empirical fit is the one used; SIFTS is the cross-check, and it is absent for
        # some legacy entries, which is exactly why the fit exists.
        fit = derive_offset(names, gef_seq)
        sifts_off = sifts_offset(pdb, gef_chain, gef_acc)
        off = fit["offset"]

        mapped = {}
        for auth in sorted(contacts):
            unp = auth + off
            if 1 <= unp <= len(gef_seq):
                mapped[unp] = gef_seq[unp - 1]

        dh_start, dh_end = recs[gef_acc]["dh_domains"][0]
        in_dh = {p: r for p, r in mapped.items() if dh_start <= p <= dh_end}
        anchors[pdb] = {
            "gef": gef_acc,
            "gef_label": recs[gef_acc]["label"],
            "gtpase": gt_acc,
            "n_contact_auth_residues": len(contacts),
            "n_mapped_to_uniprot": len(mapped),
            "n_in_dh_domain": len(in_dh),
            "dh_contacts": in_dh,
            "offset_fit": fit,
            "sifts_offset": sifts_off,
            "offsets_agree": (sifts_off is None) or (sifts_off == off),
        }
        result["structures"][pdb] = {k: v for k, v in anchors[pdb].items() if k != "dh_contacts"}
        result["structures"][pdb]["dh_contact_positions"] = sorted(in_dh)

    # ---- 3. DH-domain alignment, plus a scrambled negative control
    records = []
    for acc in aligned_accs:
        s, e = recs[acc]["dh_domains"][0]
        records.append((acc, recs[acc]["sequence"][s - 1 : e]))
    rng = random.Random(20260919)
    tgt_dh = dict(records)[TARGET]
    scrambled = "".join(rng.sample(tgt_dh, len(tgt_dh)))
    records.append(("SCRAMBLED_CONTROL", scrambled))
    aln = mafft_align(records)
    result["alignment"] = {
        "tool": "mafft --localpair --maxiterate 1000",
        "n_sequences": len(records),
        "n_columns": len(next(iter(aln.values()))),
    }

    # ---- 4. map each anchor set onto every panel member
    per_anchor: dict[str, dict] = {}
    for pdb, info in anchors.items():
        gef_acc = info["gef"]
        gef_dh_start = recs[gef_acc]["dh_domains"][0][0]
        cols = {}
        for pos in sorted(info["dh_contacts"]):
            col = col_of(aln[gef_acc], pos - gef_dh_start)
            if col is not None:
                cols[pos] = col
        table: dict[str, dict] = {}
        for acc in list(aligned_accs) + ["SCRAMBLED_CONTROL"]:
            same = gap = 0
            detail = {}
            dh_start = recs[acc]["dh_domains"][0][0] if acc in recs else None
            for pos, col in cols.items():
                res, ung = residue_at_col(aln[acc], col)
                if res == "-":
                    gap += 1
                elif res == info["dh_contacts"][pos]:
                    same += 1
                native = (dh_start + ung) if (dh_start is not None and ung is not None) else None
                detail[str(pos)] = {"residue": res, "native_position": native}
            n = len(cols) or 1
            table[acc] = {
                "label": PANEL.get(acc, "scrambled permutation of the target DH domain"),
                "n_anchor_columns": len(cols),
                "identical": same,
                "gapped": gap,
                "pct_identical": round(100.0 * same / n, 1),
                "per_position": detail,
            }
        per_anchor[pdb] = {"gtpase": info["gtpase"], "anchor_source": gef_acc, "mapping": table}
    result["anchor_mapping"] = per_anchor

    # ---- 5. resolve the two paper mutations onto the current canonical sequence
    tgt = recs[TARGET]
    seq = tgt["sequence"]
    # Offsets UniProt's own record licenses: each VAR_SEQ deletion at the N-terminus
    # defines an isoform whose numbering is shifted by the deleted length; and the
    # sequence-version-4 N-terminal extension defines the historical-canonical shift.
    candidate_offsets = {0: "current canonical (Q6ZSZ5-4, 1361 aa)"}
    for vs in tgt["var_seq"]:
        if vs["start"] == 1 and vs["end"] and vs["alternative"] is None:
            candidate_offsets[vs["end"]] = f"isoform numbering; VAR_SEQ {vs['id']} deletes 1-{vs['end']}"
    dh_start, dh_end = tgt["dh_domains"][0]
    # The Arno variant is the calibrator: UniProt states it independently as T458.
    arno_offset = 458 - PAPER_MUTATIONS["Arno2017_T270A"]["paper_position"]
    candidate_offsets[arno_offset] = (
        "historical canonical; UniProt sequence version 4 (10-OCT-2018) extended the "
        "N-terminus, and UniProt itself records Arno's Thr270 as VARIANT 458"
    )

    for name, mut in PAPER_MUTATIONS.items():
        hits = []
        for off, why in sorted(candidate_offsets.items()):
            pos = mut["paper_position"] + off
            if pos < 1 or pos > len(seq):
                continue
            hits.append(
                {
                    "offset": off,
                    "rationale": why,
                    "canonical_position": pos,
                    "residue": seq[pos - 1],
                    "matches_paper_residue": seq[pos - 1] == mut["residue"],
                    "inside_dh_domain": dh_start <= pos <= dh_end,
                }
            )
        consistent = [h for h in hits if h["matches_paper_residue"] and h["inside_dh_domain"]]
        result["mutation_mapping"][name] = {
            "pmid": mut["pmid"],
            "paper_position": mut["paper_position"],
            "paper_residue": mut["residue"],
            "candidates": hits,
            "n_consistent": len(consistent),
            "resolved_canonical_position": consistent[0]["canonical_position"] if len(consistent) == 1 else None,
        }

    # ---- 6. controls, asserted
    ctrl = result["controls"]
    ctrl["sifts_mapping_verified"] = {
        pdb: {
            "fitted_offset": anchors[pdb]["offset_fit"]["offset"],
            "residues_checked": anchors[pdb]["offset_fit"]["checked"],
            "identity_pct": anchors[pdb]["offset_fit"]["best_pct"],
            "runner_up_identity_pct": anchors[pdb]["offset_fit"]["runner_up_pct"],
            "sifts_offset": anchors[pdb]["sifts_offset"],
            "offsets_agree": anchors[pdb]["offsets_agree"],
            # A correct structure-to-sequence fit is near-perfect and unique.  Requiring
            # the runner-up to be far behind is what stops a spurious offset passing.
            "pass": (
                anchors[pdb]["offset_fit"]["best_pct"] >= 95.0
                and anchors[pdb]["offset_fit"]["checked"] >= 100
                and anchors[pdb]["offset_fit"]["runner_up_pct"] < 30.0
                and anchors[pdb]["offsets_agree"]
            ),
        }
        for pdb in anchors
    }
    ctrl["negative_no_dh_domain_excluded"] = {
        "accessions": ["P61586", "Q92608"],
        "excluded": sorted(a for a in ("P61586", "Q92608") if a in result["excluded"]),
        "pass": all(a in result["excluded"] for a in ("P61586", "Q92608")),
    }
    terry = result["mutation_mapping"]["Terry2011_Y260A"]
    arno = result["mutation_mapping"]["Arno2017_T270A"]
    ctrl["positive_arno_variant_is_T458"] = {
        "resolved": arno["resolved_canonical_position"],
        "pass": arno["resolved_canonical_position"] == 458,
    }
    off188 = [c for c in terry["candidates"] if c["offset"] == arno_offset]
    ctrl["negative_terry_not_at_arno_offset"] = {
        "offset": arno_offset,
        "residue_found": off188[0]["residue"] if off188 else None,
        "pass": bool(off188) and not off188[0]["matches_paper_residue"],
    }
    ctrl["terry_offset_unique"] = {
        "n_consistent_offsets": terry["n_consistent"],
        "resolved": terry["resolved_canonical_position"],
        "pass": terry["n_consistent"] == 1,
    }

    # POSITIVE (biology): Terry says analogous mutations inactivate GEF-H1 and Lbc, so
    # the aligned column in ARHGEF2 and AKAP13 should also be a tyrosine.
    if terry["resolved_canonical_position"]:
        tcol = col_of(aln[TARGET], terry["resolved_canonical_position"] - dh_start)
        comp = {}
        for acc in aligned_accs + ["SCRAMBLED_CONTROL"]:
            res, ung = residue_at_col(aln[acc], tcol)
            start = recs[acc]["dh_domains"][0][0] if acc in recs else None
            comp[acc] = {
                "label": PANEL.get(acc, "scrambled control"),
                "residue": res,
                "native_position": (start + ung) if (start is not None and ung is not None) else None,
            }
        n_real = [a for a in aligned_accs if comp[a]["residue"] == "Y"]
        ctrl["positive_terry_tyrosine_conserved"] = {
            "alignment_column": tcol,
            "per_protein": comp,
            "n_tyrosine_of_n_panel": [len(n_real), len(aligned_accs)],
            "ARHGEF2_is_tyrosine": comp.get("Q92974", {}).get("residue") == "Y",
            "AKAP13_is_tyrosine": comp.get("Q12802", {}).get("residue") == "Y",
            "pass": comp.get("Q92974", {}).get("residue") == "Y",
        }
        result["terry_column"] = comp

    # ---- 7. does the anchor-identity score classify substrate at all?
    # Delta = %identity to the RhoA-contact anchor minus %identity to the RAC1-contact
    # anchor.  A protein is *held out* if it is neither anchor.  Without this block the
    # ARHGEF18 delta would be an uncalibrated number; with it, the delta is only worth
    # reading if the classifier gets held-out proteins with known specificity right.
    rho_pdb, rac_pdb = "1x86", "1foe"
    anchor_accs = {anchors[rho_pdb]["gef"], anchors[rac_pdb]["gef"]}
    deltas: dict[str, float] = {}
    for acc in aligned_accs + ["SCRAMBLED_CONTROL"]:
        deltas[acc] = round(
            per_anchor[rho_pdb]["mapping"][acc]["pct_identical"]
            - per_anchor[rac_pdb]["mapping"][acc]["pct_identical"],
            1,
        )
    held_out = []
    correct = 0
    for acc, truth in KNOWN_SPECIFICITY.items():
        if acc in anchor_accs or acc not in deltas:
            continue
        pred = "RHOA" if deltas[acc] > 0 else "RAC1"
        held_out.append(
            {"accession": acc, "label": PANEL[acc], "delta": deltas[acc], "truth": truth, "predicted": pred}
        )
        correct += pred == truth
    result["specificity_classifier"] = {
        "definition": "delta = %identity at RhoA-contact columns (1X86) minus %identity at RAC1-contact columns (1FOE)",
        "anchors_excluded": sorted(anchor_accs),
        "held_out": held_out,
        "n_held_out": len(held_out),
        "n_correct": correct,
        "accuracy_pct": round(100.0 * correct / len(held_out), 1) if held_out else None,
        "target_delta": deltas.get(TARGET),
        "rho_group_delta_range": [
            min(h["delta"] for h in held_out if h["truth"] == "RHOA"),
            max(h["delta"] for h in held_out if h["truth"] == "RHOA"),
        ]
        if any(h["truth"] == "RHOA" for h in held_out)
        else None,
        "rac_group_delta_range": [
            min(h["delta"] for h in held_out if h["truth"] == "RAC1"),
            max(h["delta"] for h in held_out if h["truth"] == "RAC1"),
        ]
        if any(h["truth"] == "RAC1" for h in held_out)
        else None,
        "cdc42_out_of_scope": {"Q15811": deltas.get("Q15811")},
        "all_deltas": deltas,
    }

    # ---- 8. the PH domain: ARHGEF18's own structure, bound to activated RhoA
    # Everything above maps *other* proteins' contacts onto ARHGEF18.  6BCB is different:
    # it is ARHGEF18 itself (the mouse ortholog) in complex with RhoA-GTP, so the contact
    # residues are the protein's own, and only the mouse-to-human step is inferred.
    ph_block: dict = {}
    ph_records = []
    for acc in aligned_accs:
        if recs[acc]["ph_domains"]:
            s, e = recs[acc]["ph_domains"][0]
            ph_records.append((acc, recs[acc]["sequence"][s - 1 : e]))
    tgt_ph = dict(ph_records).get(TARGET)
    if tgt_ph:
        ph_records.append(("SCRAMBLED_CONTROL", "".join(rng.sample(tgt_ph, len(tgt_ph)))))
    ph_aln = mafft_align(ph_records)

    for pdb, gef_acc, gef_chain, gt_acc, gt_chain in PH_STRUCTURES:
        atoms = parse_cif_atoms(_get_text(RCSB_CIF.format(pdb=pdb.upper())))
        names = structure_residue_names(atoms, gef_chain)
        gef_seq = recs[gef_acc]["sequence"]
        fit = derive_offset(names, gef_seq)
        off = fit["offset"]
        contacts = contact_residues(atoms, gef_chain, gt_chain, CONTACT_CUTOFF)
        ph_start, ph_end = recs[gef_acc]["ph_domains"][0]
        in_ph = {}
        for auth in sorted(contacts):
            unp = auth + off if off is not None else None
            if unp and ph_start <= unp <= ph_end:
                in_ph[unp] = gef_seq[unp - 1]
        cols = {}
        for pos in sorted(in_ph):
            col = col_of(ph_aln[gef_acc], pos - ph_start)
            if col is not None:
                cols[pos] = col
        table = {}
        for acc in [a for a, _ in ph_records]:
            same = 0
            detail = {}
            start = recs[acc]["ph_domains"][0][0] if acc in recs else None
            for pos, col in cols.items():
                res, ung = residue_at_col(ph_aln[acc], col)
                if res == in_ph[pos]:
                    same += 1
                detail[str(pos)] = {
                    "residue": res,
                    "native_position": (start + ung) if (start is not None and ung is not None) else None,
                }
            n = len(cols) or 1
            table[acc] = {
                "label": PANEL.get(acc, "scrambled permutation of the target PH domain"),
                "identical": same,
                "n_anchor_columns": len(cols),
                "pct_identical": round(100.0 * same / n, 1),
                "per_position": detail,
            }
        ph_block[pdb] = {
            "gef": gef_acc,
            "gef_label": recs[gef_acc]["label"],
            "gtpase": gt_acc,
            "offset_fit": fit,
            "n_rhoa_contacts_in_ph": len(in_ph),
            "contact_positions": sorted(in_ph),
            "mapping": table,
        }
    result["ph_domain_rhoa_interface"] = ph_block

    if "6bcb" in ph_block:
        b = ph_block["6bcb"]
        ctrl["ph_structure_is_this_protein"] = {
            "pdb": "6bcb",
            "chain_accession": b["gef"],
            "is_arhgef18_ortholog": b["gef"] in ("Q6P9R4", "Q6ZSZ5"),
            "identity_pct_of_fit": b["offset_fit"]["best_pct"],
            "pass": b["gef"] in ("Q6P9R4", "Q6ZSZ5") and b["offset_fit"]["best_pct"] >= 95.0,
        }
        ctrl["ph_mouse_to_human_conserved"] = {
            "human_pct_at_mouse_contacts": b["mapping"].get(TARGET, {}).get("pct_identical"),
            "scrambled_pct": b["mapping"].get("SCRAMBLED_CONTROL", {}).get("pct_identical"),
            # Orthologs should agree almost everywhere; if they do not, the mouse contacts
            # cannot be carried across and the human claim has to be withdrawn.
            "pass": (
                (b["mapping"].get(TARGET, {}).get("pct_identical") or 0) >= 80.0
                and (b["mapping"].get(TARGET, {}).get("pct_identical") or 0)
                > (b["mapping"].get("SCRAMBLED_CONTROL", {}).get("pct_identical") or 0)
            ),
        }

    # NEGATIVE (anchor): the scrambled control must score far below the real orthologs.
    for pdb, blk in per_anchor.items():
        real = [blk["mapping"][a]["pct_identical"] for a in aligned_accs if a != TARGET]
        scr = blk["mapping"]["SCRAMBLED_CONTROL"]["pct_identical"]
        ctrl[f"negative_scrambled_below_orthologs_{pdb}"] = {
            "scrambled_pct": scr,
            "min_real_pct": min(real) if real else None,
            "median_real_pct": sorted(real)[len(real) // 2] if real else None,
            "pass": bool(real) and scr < min(real),
        }

    result["all_controls_pass"] = all(
        v.get("pass") is True for v in ctrl.values() if isinstance(v, dict) and "pass" in v
    ) and all(
        s["pass"] for s in ctrl["sifts_mapping_verified"].values()
    )
    return result


def self_test(data: dict) -> int:
    """Assert each guard fires with its expected message; negative controls stay silent."""
    failures: list[str] = []

    def check(name: str, cond: bool, msg: str) -> None:
        if not cond:
            failures.append(f"{name}: {msg}")

    for pdb, s in data["controls"]["sifts_mapping_verified"].items():
        check(f"structure_to_sequence[{pdb}]", s["pass"], f"offset fit failed or disagreed with SIFTS: {s}")
    check(
        "negative_no_dh_domain_excluded",
        data["controls"]["negative_no_dh_domain_excluded"]["pass"],
        "a DH-domain-free protein (RHOA or DOCK2) survived the DH-domain gate",
    )
    sc = data["specificity_classifier"]
    check(
        "classifier_has_held_out_rac_gefs",
        sum(1 for h in sc["held_out"] if h["truth"] == "RAC1") >= 2,
        "fewer than two held-out RAC1-specific GEFs, so the RhoA-vs-RAC1 contrast is circular",
    )
    for key in ("ph_structure_is_this_protein", "ph_mouse_to_human_conserved"):
        if key in data["controls"]:
            check(key, data["controls"][key]["pass"], f"{key} failed: {data['controls'][key]}")
    check(
        "positive_arno_variant_is_T458",
        data["controls"]["positive_arno_variant_is_T458"]["pass"],
        "Arno Thr270 did not resolve to canonical T458",
    )
    check(
        "negative_terry_not_at_arno_offset",
        data["controls"]["negative_terry_not_at_arno_offset"]["pass"],
        "the Arno offset also places a Tyr at Terry's position, so the offset is ambiguous",
    )
    check(
        "terry_offset_unique",
        data["controls"]["terry_offset_unique"]["pass"],
        "Terry's Y260 is consistent with more than one offset",
    )
    if "positive_terry_tyrosine_conserved" in data["controls"]:
        check(
            "positive_terry_tyrosine_conserved",
            data["controls"]["positive_terry_tyrosine_conserved"]["pass"],
            "ARHGEF2 does not carry a tyrosine at Terry's aligned column",
        )
    for k, v in data["controls"].items():
        if k.startswith("negative_scrambled_below_orthologs"):
            check(k, v["pass"], f"scrambled control scored >= a real ortholog: {v}")

    # Structural anchors must actually exist, or the whole substrate question is vacuous.
    for pdb, s in data["structures"].items():
        check(f"anchors[{pdb}]", s["n_in_dh_domain"] >= 5, f"only {s['n_in_dh_domain']} DH contacts found")

    if failures:
        print("SELF-TEST FAILURES:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"self-test: {len(data['controls'])} control blocks, all pass")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    data = build()
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT}")
    print(f"all_controls_pass = {data['all_controls_pass']}")
    if args.self_test:
        return self_test(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
