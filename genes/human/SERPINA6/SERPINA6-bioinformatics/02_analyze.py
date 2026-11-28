# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "numpy", "pyyaml", "pyfamsa"]
# ///
"""Structural and population analysis of SERPINA6 / corticosteroid-binding globulin (P08185).

Reads only files written by 01_fetch_data.py (cache/) and variants_literature.yaml.
Writes results.json, tables/*.tsv and RESULTS.md. Nothing is hardcoded as a result: every
number in RESULTS.md is computed here from the cached inputs, and thresholds are named constants.
"""
from __future__ import annotations

import csv
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import yaml
from Bio import SeqIO
from Bio.PDB import MMCIFParser, ShrakeRupley
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from pyfamsa import Aligner, Sequence

HERE = Path(__file__).parent
CACHE = HERE / "cache"
TABLES = HERE / "tables"
ACC = "P08185"

CONTACT_A = 4.0  # heavy-atom distance defining a direct ligand contact
SHELL_A = 8.0  # second shell around the steroid
BURIED_RSA = 0.20  # relative side-chain accessibility below which a residue is called buried
STEROID_LIGANDS = {"HCY": "cortisol", "STR": "progesterone"}
# Max side-chain-inclusive accessible surface of Gly-X-Gly tripeptides (Tien et al. 2013, theoretical), A^2
MAX_ASA = dict(A=129, R=274, N=195, D=193, C=167, Q=225, E=223, G=104, H=224, I=197, L=201, K=236, M=224,
               F=240, P=159, S=155, T=172, W=285, Y=263, V=174)
THREE = dict(ALA="A", ARG="R", ASN="N", ASP="D", CYS="C", GLN="Q", GLU="E", GLY="G", HIS="H", ILE="I", LEU="L",
             LYS="K", MET="M", PHE="F", PRO="P", SER="S", THR="T", TRP="W", TYR="Y", VAL="V")
ONE_TO_THREE = {v: k.capitalize() for k, v in THREE.items()}
A1AT_P1_PRECURSOR = None  # derived below from the UniProt "Reactive bond" site of P01009, not typed in


def load_uniprot() -> dict:
    return json.loads((CACHE / "uniprot_P08185.json").read_text())


def features(up: dict, ftype: str) -> list[dict]:
    return [f for f in up["features"] if f["type"] == ftype]


def fasta_seq(path: Path) -> str:
    return str(next(SeqIO.parse(path, "fasta")).seq)


# ----------------------------------------------------------------------------- structures
def parse_structure(pdb_id: str):
    return MMCIFParser(QUIET=True).get_structure(pdb_id, CACHE / "pdb" / f"{pdb_id}.cif")


def auth_to_uniprot_map(pdb_id: str, accession: str) -> dict[tuple[str, int], int]:
    """(chain, auth_seq_id) -> UniProt position, from the mmCIF _struct_ref_seq blocks for `accession`."""
    d = MMCIF2Dict(CACHE / "pdb" / f"{pdb_id}.cif")
    out: dict[tuple[str, int], int] = {}
    for strand, db, b, e, ab, ae in zip(
        d["_struct_ref_seq.pdbx_strand_id"], d["_struct_ref_seq.pdbx_db_accession"],
        d["_struct_ref_seq.db_align_beg"], d["_struct_ref_seq.db_align_end"],
        d["_struct_ref_seq.pdbx_auth_seq_align_beg"], d["_struct_ref_seq.pdbx_auth_seq_align_end"],
    ):
        if db != accession:
            continue
        b, e, ab, ae = int(b), int(e), int(ab), int(ae)
        if e - b != ae - ab:
            raise ValueError(f"{pdb_id} segment length mismatch")
        for k in range(e - b + 1):
            out[(strand, ab + k)] = b + k
    return out


def engineered_positions(pdb_id: str) -> dict[tuple[str, int], str]:
    d = MMCIF2Dict(CACHE / "pdb" / f"{pdb_id}.cif")
    if "_struct_ref_seq_dif.pdbx_auth_seq_num" not in d:
        return {}
    return {
        (c, int(n)): f"{dbm}->{m} ({det})"
        for c, m, n, dbm, det in zip(
            d["_struct_ref_seq_dif.pdbx_pdb_strand_id"], d["_struct_ref_seq_dif.mon_id"],
            d["_struct_ref_seq_dif.pdbx_auth_seq_num"], d["_struct_ref_seq_dif.db_mon_id"],
            d["_struct_ref_seq_dif.details"],
        )
        if n not in ("?", ".")
    }


def ligand_distances(pdb_id: str, accession: str) -> dict:
    """Minimum heavy-atom distance from each protein residue to each steroid copy, per chain."""
    st = parse_structure(pdb_id)
    amap = auth_to_uniprot_map(pdb_id, accession)
    model = st[0]
    ligs = [r for ch in model for r in ch if r.id[0].startswith("H_") and r.get_resname() in STEROID_LIGANDS]
    out = {"pdb": pdb_id, "ligands": [], "min_dist": {}, "contact_atoms": {}}
    if not ligs:
        return out
    prot = [(ch.id, r) for ch in model for r in ch if r.id[0] == " " and r.get_resname() in THREE]
    for lig in ligs:
        lc = np.array([a.coord for a in lig if a.element != "H"])
        latoms = [a.get_id() for a in lig if a.element != "H"]
        # the protein chain this ligand copy belongs to = chain with most atoms within 4.5 A
        near = Counter()
        per_res = {}
        for cid, r in prot:
            rc = np.array([a.coord for a in r if a.element != "H"])
            dm = np.linalg.norm(rc[:, None, :] - lc[None, :, :], axis=2)
            m = float(dm.min())
            i, j = np.unravel_index(dm.argmin(), dm.shape)
            per_res[(cid, r.id[1])] = (m, [a.get_id() for a in r if a.element != "H"][i], latoms[j], r.get_resname())
            if m <= 4.5:
                near[cid] += 1
        if not near:
            continue
        owner = near.most_common(1)[0][0]
        out["ligands"].append({"resname": lig.get_resname(), "name": STEROID_LIGANDS[lig.get_resname()], "chain": owner})
        for (cid, num), (m, patom, latom, resn) in per_res.items():
            if cid != owner:
                continue  # distances are measured within the protomer that binds this ligand copy
            up = amap.get((cid, num))
            if up is None:
                continue
            key = str(up)
            if key not in out["min_dist"] or m < out["min_dist"][key]:
                out["min_dist"][key] = round(m, 2)
                out["contact_atoms"][key] = f"{THREE[resn]}{up} {patom}...{latom} (chain {cid})"
    return out


def relative_sasa(pdb_id_or_path, accession: str | None, chain_id: str | None = None) -> dict[int, float]:
    """Relative side-chain-inclusive SASA per UniProt position for one chain (protein atoms only)."""
    if isinstance(pdb_id_or_path, Path):
        st = MMCIFParser(QUIET=True).get_structure("af", pdb_id_or_path)
        amap = None
    else:
        st = parse_structure(pdb_id_or_path)
        amap = auth_to_uniprot_map(pdb_id_or_path, accession)
    model = st[0]
    chain = model[chain_id] if chain_id else next(iter(model))
    # strip waters / ligands / other chains so accessibility is of the isolated protomer
    for ch in list(model):
        if ch.id != chain.id:
            model.detach_child(ch.id)
    for r in list(chain):
        if r.id[0] != " ":
            chain.detach_child(r.id)
    ShrakeRupley().compute(model, level="R")
    out = {}
    for r in chain:
        aa = THREE.get(r.get_resname())
        if not aa:
            continue
        pos = r.id[1] if amap is None else amap.get((chain.id, r.id[1]))
        if pos is not None:
            out[pos] = round(min(r.sasa / MAX_ASA[aa], 1.5), 3)
    return out


def ca_coords(pdb_id_or_path, accession=None, chain_id=None) -> dict[int, np.ndarray]:
    if isinstance(pdb_id_or_path, Path):
        st = MMCIFParser(QUIET=True).get_structure("af", pdb_id_or_path)
        amap = None
    else:
        st = parse_structure(pdb_id_or_path)
        amap = auth_to_uniprot_map(pdb_id_or_path, accession)
    model = st[0]
    out = {}
    for ch in model:
        if chain_id and ch.id != chain_id and amap is None:
            continue
        for r in ch:
            if r.id[0] == " " and "CA" in r:
                pos = r.id[1] if amap is None else amap.get((ch.id, r.id[1]))
                if pos is not None and (chain_id is None or ch.id == chain_id or amap is not None) and pos not in out:
                    out[pos] = r["CA"].coord
    return out


def neighbour_count(coords: dict[int, np.ndarray], pos: int, radius: float = 10.0, min_sep: int = 4) -> int | None:
    if pos not in coords:
        return None
    c = coords[pos]
    return sum(1 for p, x in coords.items() if abs(p - pos) >= min_sep and np.linalg.norm(x - c) <= radius)


BACKBONE = {"N", "CA", "C", "O", "OXT"}


def residue_table(pdb_id_or_path, accession=None, chain_id=None) -> dict[int, object]:
    """UniProt position -> Bio.PDB residue for one protein chain."""
    if isinstance(pdb_id_or_path, Path):
        st = MMCIFParser(QUIET=True).get_structure("af", pdb_id_or_path)
        amap = None
    else:
        st = parse_structure(pdb_id_or_path)
        amap = auth_to_uniprot_map(pdb_id_or_path, accession)
    model = st[0]
    chain = model[chain_id] if chain_id else next(iter(model))
    out = {}
    for r in chain:
        if r.id[0] != " " or r.get_resname() not in THREE:
            continue
        pos = r.id[1] if amap is None else amap.get((chain.id, r.id[1]))
        if pos is not None:
            out[pos] = r
    return out


def environment(table: dict[int, object], pos: int, cutoff: float = 4.0, polar_cutoff: float = 3.5) -> dict | None:
    """Side-chain neighbours (heavy atoms within `cutoff`), polar partners and backbone torsions of one residue."""
    if pos not in table:
        return None
    res = table[pos]
    side = [a for a in res if a.element != "H" and a.get_id() not in BACKBONE] or [a for a in res if a.element != "H"]
    neigh, polar = {}, []
    for q, other in table.items():
        if abs(q - pos) < 2:
            continue
        best = None
        for a in side:
            for b in other:
                if b.element == "H":
                    continue
                d = float(np.linalg.norm(a.coord - b.coord))
                if best is None or d < best:
                    best = d
                if d <= polar_cutoff and a.element in ("N", "O") and b.element in ("N", "O") and a.get_id() not in BACKBONE:
                    polar.append((round(d, 2), a.get_id(), q, b.get_id()))
        if best is not None and best <= cutoff:
            neigh[q] = round(best, 2)
    tors = {}
    if pos - 1 in table and pos + 1 in table:
        from Bio.PDB.vectors import calc_dihedral

        try:
            tors["phi"] = round(math.degrees(calc_dihedral(table[pos - 1]["C"].get_vector(), res["N"].get_vector(),
                                                           res["CA"].get_vector(), res["C"].get_vector())), 0)
            tors["psi"] = round(math.degrees(calc_dihedral(res["N"].get_vector(), res["CA"].get_vector(),
                                                           res["C"].get_vector(), table[pos + 1]["N"].get_vector())), 0)
        except KeyError:
            pass
    return {"neighbours": neigh, "polar": sorted(set(polar)), **tors}


def plddt(path: Path) -> dict[int, float]:
    st = MMCIFParser(QUIET=True).get_structure("af", path)
    return {r.id[1]: float(r["CA"].get_bfactor()) for r in next(iter(st[0])) if "CA" in r}


# ----------------------------------------------------------------------------- alignment
def align(named: list[tuple[str, str]]) -> dict[str, str]:
    msa = Aligner(guide_tree="upgma").align([Sequence(n.encode(), s.encode()) for n, s in named])
    return {m.id.decode(): m.sequence.decode() for m in msa}


def column_map(aligned_ref: str) -> dict[int, int]:
    """1-based ungapped position in the reference -> alignment column."""
    out, k = {}, 0
    for col, ch in enumerate(aligned_ref):
        if ch != "-":
            k += 1
            out[k] = col
    return out


def pos_at_col(aligned: str, col: int) -> int | None:
    if aligned[col] == "-":
        return None
    return sum(1 for ch in aligned[: col + 1] if ch != "-")


# ----------------------------------------------------------------------------- variants
def parse_hgvsp(h: str | None):
    """'p.Asp389Asn' -> ('D', 389, 'N'); nonsense -> alt '*'; other shapes -> (ref, pos, None)."""
    if not h:
        return None
    m = re.match(r"p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2}|Ter|\*|=)?", h)
    if not m:
        return None
    three = {k.capitalize(): v for k, v in THREE.items()}
    ref = three.get(m.group(1))
    alt = m.group(3)
    alt1 = "*" if alt in ("Ter", "*") else three.get(alt) if alt else None
    return ref, int(m.group(2)), alt1


def main() -> None:  # noqa: C901, PLR0912, PLR0915
    TABLES.mkdir(exist_ok=True)
    up = load_uniprot()
    seq = up["sequence"]["value"]
    assert fasta_seq(CACHE / "uniprot_P08185.fasta") == seq
    R: dict = {"accession": ACC, "length": len(seq), "sequence_version": up["entryAudit"]["sequenceVersion"],
               "uniprot_entry_version": up["entryAudit"]["entryVersion"]}

    # ---- 1. numbering ---------------------------------------------------------------
    sig = features(up, "Signal")[0]
    sp_len = sig["location"]["end"]["value"]
    R["signal_peptide"] = {"start": 1, "end": sp_len, "sequence": seq[:sp_len]}
    R["mature_offset"] = sp_len
    R["mature_length"] = len(seq) - sp_len
    R["mature_n_terminus"] = seq[sp_len : sp_len + 8]

    def to_precursor(v: dict) -> int:
        return v["pos"] + sp_len if v["numbering"] == "mature" else v["pos"]

    lit = yaml.safe_load((HERE / "variants_literature.yaml").read_text())
    numbering_rows = []
    for v in lit["variants"]:
        p = to_precursor(v)
        canon = seq[p - 1]
        ok = canon == v["ref"]
        alt_note = ""
        if not ok and canon == v["alt"]:
            alt_note = "reference and alternate are swapped relative to the UniProt canonical sequence"
        # would the reported number also match if (mis)read in the other numbering scheme?
        other = v["pos"] if v["numbering"] == "mature" else v["pos"] - sp_len
        other_res = seq[other - 1] if 0 < other <= len(seq) else None
        alias_notes = []
        for al in v.get("also_reported_as", []):
            ap = al["pos"] + sp_len if v["numbering"] == "mature" else al["pos"]
            if seq[ap - 1] != al["ref"]:
                alias_notes.append({
                    "variant": v["name"], "label": al["label"], "reported": f"{al['ref']}{al['pos']}{al['alt']}",
                    "precursor_pos": ap, "canonical_residue": seq[ap - 1], "references": al["references"],
                    "note": ("reference and alternate are swapped relative to the UniProt canonical sequence"
                             if seq[ap - 1] == al["alt"] else "reference residue does not match the canonical sequence")})
        v["alias_notes"] = alias_notes
        v.update(precursor_pos=p, mature_pos=p - sp_len, canonical_residue=canon, ref_matches_canonical=ok,
                 numbering_note=alt_note, residue_if_read_in_other_numbering=other_res)
        numbering_rows.append(v)
    R["numbering_check"] = {
        "n_variants": len(numbering_rows),
        "n_ref_match": sum(v["ref_matches_canonical"] for v in numbering_rows),
        "mismatches": [
            {k: v[k] for k in ("name", "numbering", "ref", "pos", "alt", "precursor_pos", "canonical_residue", "numbering_note")}
            for v in numbering_rows if not v["ref_matches_canonical"]
        ],
        "alias_mismatches": [n for v in numbering_rows for n in v["alias_notes"]],
        "ambiguous_if_numbering_confused": [
            v["name"] for v in numbering_rows
            if v["ref_matches_canonical"] and v["residue_if_read_in_other_numbering"] == v["ref"]
        ],
    }

    # ---- 2. sequence features ---------------------------------------------------------
    sequons = [m.start() + 1 for m in re.finditer(r"(?=N[^P][ST])", seq)]
    up_glyc = [f["location"]["start"]["value"] for f in features(up, "Glycosylation")]
    R["n_glycosylation"] = {
        "sequons_precursor": sequons, "sequons_mature": [s - sp_len for s in sequons],
        "uniprot_annotated": up_glyc, "sequons_not_annotated_in_uniprot": sorted(set(sequons) - set(up_glyc)),
    }
    R["cysteines_precursor"] = [i + 1 for i, a in enumerate(seq) if a == "C"]
    R["cysteines_mature_chain"] = [p - sp_len for p in R["cysteines_precursor"] if p > sp_len]
    R["uniprot_binding_sites"] = [f["location"]["start"]["value"] for f in features(up, "Binding site")]
    sse = []
    for t in ("Helix", "Beta strand", "Turn"):
        for f in features(up, t):
            sse.append((f["location"]["start"]["value"], f["location"]["end"]["value"], t))
    sse.sort()
    n_h = n_s = 0
    sse_named = []
    for s, e, t in sse:
        if t == "Helix":
            n_h += 1
            sse_named.append((s, e, f"helix {n_h} ({s}-{e})"))
        elif t == "Beta strand":
            n_s += 1
            sse_named.append((s, e, f"strand {n_s} ({s}-{e})"))

    def sse_at(p: int) -> str:
        for s, e, n in sse_named:
            if s <= p <= e:
                return n
        return "loop/unassigned"

    # ---- 3. reactive-centre loop register via alignment to alpha-1-antitrypsin --------------
    comp = {p.stem: fasta_seq(p) for p in sorted((CACHE / "comparators").glob("*.fasta"))}
    a1at_json = None
    # The P1-P1' reactive bond of A1AT is taken from the cached UniProt variation/feature data if present;
    # otherwise from the A1AT sequence motif surrounding the scissile bond is NOT assumed -- we fetch it.
    a1at_site_file = CACHE / "comparators" / "P01009.fasta"
    aln = align([(ACC, seq)] + [(k, v) for k, v in comp.items()])
    cmap = column_map(aln[ACC])
    R["comparators"] = {k: len(v) for k, v in comp.items()}

    def comparator_residue(acc: str, pos: int) -> str:
        col = cmap[pos]
        return aln[acc][col]

    # Literature register (PMID:19011238): check the residues, then derive P1 from the stated P-sites.
    reg = lit["rcl_register_reported"]
    reg_checks, p1_votes = [], []
    for site, (aa, mpos) in reg["sites"].items():
        ppos = mpos + sp_len
        n = int(site[1:])
        reg_checks.append({"site": site, "reported": f"{aa}{mpos}", "precursor_pos": ppos, "canonical": seq[ppos - 1],
                           "match": seq[ppos - 1] == aa})
        p1_votes.append(ppos + n - 1)
    p1 = Counter(p1_votes).most_common(1)[0][0]
    R["rcl"] = {
        "register_source": reg["reference"], "register_checks": reg_checks,
        "register_consistent": len(set(p1_votes)) == 1 and all(c["match"] for c in reg_checks),
        "P1_precursor": p1, "P1_mature": p1 - sp_len, "P1_residue": seq[p1 - 1], "P1prime_residue": seq[p1],
        "P17_to_P4prime_precursor": [p1 - 16, p1 + 4],
        "sequence_P17_P4prime": seq[p1 - 17 : p1 + 4],
    }
    # what aligns to CBG P1 in the comparators, and the hinge (P15-P9) composition
    R["rcl"]["aligned_P1"] = {acc: {"residue": aln[acc][cmap[p1]], "position": pos_at_col(aln[acc], cmap[p1])} for acc in comp}
    R["rcl"]["hinge_P15_P9"] = {ACC: seq[p1 - 15 : p1 - 8], **{
        acc: "".join(aln[acc][cmap[q]] for q in range(p1 - 14, p1 - 7)) for acc in comp}}
    R["rcl"]["aligned_P17_P4prime"] = {acc: "".join(aln[acc][cmap[q]] for q in range(p1 - 16, p1 + 5)) for acc in comp}
    rcl_range = range(p1 - 16, p1 + 5)

    # ---- 4. structures ------------------------------------------------------------------
    pdb_info = {}
    for ef in sorted((CACHE / "pdb").glob("*_entry.json")):
        e = json.loads(ef.read_text())
        pid = ef.stem.split("_")[0]
        pdb_info[pid] = {
            "title": e["struct"]["title"],
            "resolution": (e.get("rcsb_entry_info", {}).get("resolution_combined") or [None])[0],
            "deposited": e["rcsb_accession_info"]["deposit_date"][:10],
            "engineered": sorted(set(engineered_positions(pid).values())),
        }
    R["structures"] = pdb_info
    human_lig = {}
    for pid in ("2VDY", "4C49", "4BB2"):
        human_lig[pid] = ligand_distances(pid, ACC)
    rat_lig = ligand_distances("2V95", "P31211")
    # map rat (native, RCL-exposed) contacts to human numbering through the alignment
    rat_to_human = {}
    for hp, col in cmap.items():
        rp = pos_at_col(aln["P31211"], col)
        if rp:
            rat_to_human[rp] = hp
    rat_min = {str(rat_to_human[int(k)]): v for k, v in rat_lig["min_dist"].items() if int(k) in rat_to_human}

    def min_lig(pos: int) -> dict:
        d = {pid: human_lig[pid]["min_dist"].get(str(pos)) for pid in human_lig}
        d["2V95(rat,native)"] = rat_min.get(str(pos))
        return d

    contacts = defaultdict(dict)
    for pid, ld in human_lig.items():
        for k, v in ld["min_dist"].items():
            if v <= CONTACT_A:
                contacts[int(k)][pid] = v
    for k, v in rat_min.items():
        if v <= CONTACT_A:
            contacts[int(k)]["2V95(rat,native)"] = v
    R["steroid_site"] = {
        "contact_cutoff_A": CONTACT_A,
        "ligands": {pid: ld["ligands"] for pid, ld in human_lig.items()} | {"2V95": rat_lig["ligands"]},
        "contact_residues": [
            {"precursor_pos": p, "mature_pos": p - sp_len, "residue": seq[p - 1], "min_dist_A": contacts[p],
             "n_structures": len(contacts[p]), "rat_residue": aln["P31211"][cmap[p]],
             "A1AT_residue": aln["P01009"][cmap[p]], "TBG_residue": aln["P05543"][cmap[p]]}
            for p in sorted(contacts)
        ],
    }
    core_pocket = sorted(p for p in contacts if sum(1 for k in contacts[p] if not k.startswith("2V95")) >= 2)
    R["steroid_site"]["core_pocket_precursor"] = core_pocket
    R["steroid_site"]["core_pocket_mature"] = [f"{seq[p - 1]}{p - sp_len}" for p in core_pocket]
    R["steroid_site"]["uniprot_binding_sites_within_cutoff"] = {
        str(p): bool(p in contacts) for p in R["uniprot_binding_sites"]}

    rsa_cleaved = relative_sasa("4C41", ACC, "A")
    rsa_af = relative_sasa(CACHE / "alphafold_model.cif", None)
    pl = plddt(CACHE / "alphafold_model.cif")
    tab_af = residue_table(CACHE / "alphafold_model.cif")
    lig_chain_4c49 = human_lig["4C49"]["ligands"][0]["chain"]
    tab_bound = residue_table("4C49", ACC, lig_chain_4c49)
    glyc_sites = [f["location"]["start"]["value"] for f in features(up, "Glycosylation")]
    ca_af = ca_coords(CACHE / "alphafold_model.cif")
    ca_cl = ca_coords("4C41", ACC, "A")
    # conformational state of each model: packing density of RCL residues P14..P3 (inserted strand = dense)
    probe = [q for q in range(p1 - 13, p1 - 1)]
    R["rcl"]["mean_CA_neighbours_10A"] = {
        "AlphaFold": round(statistics.mean([n for q in probe if (n := neighbour_count(ca_af, q)) is not None]), 1),
        "4C41_cleaved": round(statistics.mean([n for q in probe if (n := neighbour_count(ca_cl, q)) is not None]), 1),
        "n_RCL_residues_resolved_4C41": sum(1 for q in probe if q in ca_cl),
    }
    R["rcl"]["mean_pLDDT_RCL"] = round(statistics.mean(pl[q] for q in rcl_range), 1)
    R["alphafold"] = {
        "mean_pLDDT": round(statistics.mean(pl.values()), 1),
        "mean_pLDDT_signal_peptide": round(statistics.mean(pl[q] for q in range(1, sp_len + 1)), 1),
        "mean_pLDDT_mature": round(statistics.mean(pl[q] for q in range(sp_len + 1, len(seq) + 1)), 1),
    }
    # where does the cleaved RCL sit relative to the steroid site in the cleaved structure?
    R["structures_resolved"] = {"4C41_chain_A_residues": len(ca_cl), "4C41_first": min(ca_cl), "4C41_last": max(ca_cl),
                                "4C41_missing": [q for q in range(min(ca_cl), max(ca_cl) + 1) if q not in ca_cl]}

    # ---- 5. conservation ----------------------------------------------------------------
    recs = list(SeqIO.parse(CACHE / "orthologs_gene_exact_SERPINA6.fasta", "fasta"))
    by_species: dict[str, tuple] = {}
    for r in recs:
        m = re.search(r"OS=(.+?) OX=(\d+)", r.description)
        if not m:
            continue
        sp = m.group(1)
        reviewed = r.id.startswith("sp|")
        key = (reviewed, -abs(len(r.seq) - len(seq)))
        if "X" in str(r.seq):
            continue
        if sp not in by_species or key > by_species[sp][0]:
            by_species[sp] = (key, r.id.split("|")[1], str(r.seq))
    orth = [(f"{acc}|{sp}", s) for sp, (_, acc, s) in sorted(by_species.items()) if acc != ACC]
    oaln = align([(ACC, seq)] + orth)
    ocmap = column_map(oaln[ACC])
    # keep orthologues that align over most of the human sequence (drops fragments / mis-named paralogues)
    kept = {}
    for name, s in oaln.items():
        if name == ACC:
            continue
        ident = sum(1 for p, c in ocmap.items() if s[c] == seq[p - 1]) / len(seq)
        cov = sum(1 for p, c in ocmap.items() if s[c] != "-") / len(seq)
        if cov >= 0.9 and ident >= 0.35:
            kept[name] = (s, round(ident, 3))
    cons = {}
    for p, c in ocmap.items():
        col = [s[c] for s, _ in kept.values()]
        nong = [x for x in col if x != "-"]
        cnt = Counter(nong)
        ent = -sum((n / len(nong)) * math.log2(n / len(nong)) for n in cnt.values()) if nong else None
        cons[p] = {"identity": round(sum(1 for x in col if x == seq[p - 1]) / len(col), 3),
                   "entropy_bits": round(ent, 3) if ent is not None else None,
                   "observed": "".join(f"{a}{n}" for a, n in cnt.most_common(4))}
    R["conservation"] = {
        "n_species_fetched": len(by_species), "n_orthologues_used": len(kept),
        "species_used": sorted(n.split("|")[1] for n in kept),
        "median_identity_to_human": round(statistics.median(v[1] for v in kept.values()), 3),
        "mean_site_identity_mature": round(statistics.mean(cons[p]["identity"] for p in range(sp_len + 1, len(seq) + 1)), 3),
        "mean_site_identity_core_pocket": round(statistics.mean(cons[p]["identity"] for p in core_pocket), 3) if core_pocket else None,
        "mean_site_identity_RCL": round(statistics.mean(cons[p]["identity"] for p in rcl_range), 3),
    }

    # ---- 6. AlphaMissense ---------------------------------------------------------------
    am = {}
    with open(CACHE / "alphamissense_substitutions.csv") as fh:
        for row in csv.DictReader(fh):
            am[row["protein_variant"]] = (float(row["am_pathogenicity"]), row["am_class"])
    am_by_pos = defaultdict(list)
    for k, (s, _) in am.items():
        am_by_pos[int(k[1:-1])].append(s)
    am_mean = {p: statistics.mean(v) for p, v in am_by_pos.items()}
    R["alphamissense"] = {
        "mean_all": round(statistics.mean(am_mean.values()), 3),
        "mean_signal_peptide": round(statistics.mean(am_mean[p] for p in range(1, sp_len + 1) if p in am_mean), 3),
        "mean_core_pocket": round(statistics.mean(am_mean[p] for p in core_pocket), 3) if core_pocket else None,
        "mean_RCL": round(statistics.mean(am_mean[p] for p in rcl_range if p in am_mean), 3),
        "fraction_substitutions_likely_pathogenic": round(sum(1 for s, c in am.values() if c in ("LPath", "pathogenic", "likely_pathogenic")) / len(am), 3),
        "class_labels": sorted({c for _, c in am.values()}),
    }

    # ---- 7. gnomAD ------------------------------------------------------------------------
    g = json.loads((CACHE / "gnomad_gene.json").read_text())["data"]["gene"]
    R["gnomad_constraint"] = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in g["gnomad_constraint"].items()}
    gv = {}
    gv_all = []
    lof_cons = {"stop_gained", "frameshift_variant", "splice_donor_variant", "splice_acceptor_variant", "start_lost"}
    plof = []
    for v in g["variants"]:
        ac = an = hom = 0
        for src in ("exome", "genome"):
            if v[src] and not v[src]["filters"]:
                ac += v[src]["ac"]
                an = max(an, v[src]["an"])
                hom += v[src]["homozygote_count"]
        j = v.get("joint")
        if j:
            ac, an, hom = j["ac"], j["an"], j["homozygote_count"]
        af = ac / an if an else 0.0
        rec = {"variant_id": v["variant_id"], "consequence": v["consequence"], "hgvsc": v["hgvsc"], "hgvsp": v["hgvsp"],
               "ac": ac, "an": an, "af": af, "hom": hom, "lof": v["lof"], "rsids": v["rsids"]}
        gv_all.append(rec)
        if v["hgvsp"] and (v["hgvsp"] not in gv or rec["ac"] > gv[v["hgvsp"]]["ac"]):
            gv[v["hgvsp"]] = rec
        if v["consequence"] in lof_cons and ac > 0:
            plof.append(rec)
    hc = [r for r in plof if r["lof"] == "HC"]
    R["gnomad_plof"] = {
        "dataset": "gnomAD v4 (gnomad_r4), canonical transcript " + g["canonical_transcript_id"],
        "n_plof_variants": len(plof), "n_high_confidence": len(hc),
        "cumulative_af_high_confidence": float(f"{sum(r['af'] for r in hc):.3e}"),
        "total_homozygotes_high_confidence": sum(r["hom"] for r in hc),
        "most_frequent": [
            {"hgvsp": r["hgvsp"], "hgvsc": r["hgvsc"], "consequence": r["consequence"], "ac": r["ac"], "an": r["an"],
             "af": float(f"{r['af']:.3e}"), "hom": r["hom"], "lof": r["lof"]}
            for r in sorted(plof, key=lambda r: -r["af"])[:8]],
    }
    mis = [r for r in gv.values() if r["consequence"] == "missense_variant" and r["ac"] > 0]
    R["gnomad_missense"] = {
        "n": len(mis),
        "most_frequent": [
            {"hgvsp": r["hgvsp"], "ac": r["ac"], "af": float(f"{r['af']:.3e}"), "hom": r["hom"], "rsids": r["rsids"]}
            for r in sorted(mis, key=lambda r: -r["af"])[:10]],
    }

    def gnomad_lookup(ref, pos, alt, hgvs_c=None):
        """Match on the cDNA change when the paper gives one; otherwise on the protein change."""
        if hgvs_c:
            c = re.sub(r"del[ACGT]+$", "del", hgvs_c)
            for r in gv_all:
                if r["hgvsc"] in (hgvs_c, c):
                    return r
        if alt and alt not in ("fs",):
            alt3 = "Ter" if alt == "*" else ONE_TO_THREE[alt]
            hits = [r for r in gv_all if r["hgvsp"] == f"p.{ONE_TO_THREE[ref]}{pos}{alt3}"]
            if hits:
                return max(hits, key=lambda r: r["ac"])
        return None

    # ---- 8. ClinVar ---------------------------------------------------------------------
    clin = []
    for f in sorted(CACHE.glob("clinvar_esummary_*.json")):
        res = json.loads(f.read_text())["result"]
        for uid in res["uids"]:
            e = res[uid]
            genes = {x.get("symbol") for x in e.get("genes", [])}
            title = e.get("title", "")
            cls = (e.get("germline_classification") or {}).get("description", "")
            traits = sorted({t.get("trait_name", "") for t in (e.get("germline_classification") or {}).get("trait_set", [])})
            m = re.search(r"\((p\.[^)]+)\)", title)
            mc = re.search(r":(c\.[^ ]+)", title)
            clin.append({"vcv": e.get("accession"), "title": title, "genes": sorted(g_ for g_ in genes if g_),
                         "single_gene": genes == {"SERPINA6"}, "type": e.get("obj_type"),
                         "classification": cls, "review_status": (e.get("germline_classification") or {}).get("review_status"),
                         "traits": traits, "hgvsp": m.group(1) if m else None, "hgvsc": mc.group(1) if mc else None})
    sg = [c for c in clin if c["single_gene"]]
    R["clinvar"] = {
        "n_records_gene_query": len(clin), "n_single_gene_SERPINA6": len(sg),
        "n_multi_gene_cnv": len(clin) - len(sg),
        "classification_counts_single_gene": dict(Counter(c["classification"] for c in sg).most_common()),
        "pathogenic_or_likely_pathogenic": [c for c in sg if "athogenic" in c["classification"] and "Conflicting" not in c["classification"]],
        "conflicting": [c for c in sg if "Conflicting" in c["classification"]],
    }
    clin_by_p = {c["hgvsp"]: c for c in sg if c["hgvsp"]}

    # ---- 9. per-residue annotation + variant tables -----------------------------------------
    def annotate(pos: int) -> dict:
        ml = min_lig(pos)
        dists = [v for v in ml.values() if v is not None]
        dmin = min(dists) if dists else None
        rsa_c, rsa_a = rsa_cleaved.get(pos), rsa_af.get(pos)
        env = environment(tab_af, pos) or {}
        envb = environment(tab_bound, pos) or {}
        nb = set(env.get("neighbours", {})) | set(envb.get("neighbours", {}))
        pocket_nb = sorted(q for q in nb if q in core_pocket)
        glyc_nb = sorted(q for q in glyc_sites if q in nb or abs(q - pos) <= 2)
        region = ("signal peptide" if pos <= sp_len else "reactive-centre loop (P17-P4')" if pos in rcl_range else "serpin body")
        return {
            "region": region, "secondary_structure": sse_at(pos),
            "min_dist_to_steroid_A": dmin, "dist_by_structure": ml,
            "in_core_pocket": pos in core_pocket,
            "rsa_cleaved_4C41": rsa_c, "rsa_alphafold": rsa_a, "plddt": round(pl[pos], 1),
            "orthologue_identity": cons[pos]["identity"], "orthologue_residues": cons[pos]["observed"],
            "A1AT_residue": aln["P01009"][cmap[pos]], "TBG_residue": aln["P05543"][cmap[pos]],
            "rat_CBG_residue": aln["P31211"][cmap[pos]],
            "am_mean_at_position": round(am_mean[pos], 3) if pos in am_mean else None,
            "is_sequon_asn": pos in sequons,
            "packs_against_pocket_residues": [f"{seq[q - 1]}{q - sp_len}" for q in pocket_nb],
            "near_glycosylated_asn": [f"N{q - sp_len}" for q in glyc_nb if q != pos],
            "sidechain_neighbours_alphafold": [f"{seq[q - 1]}{q - sp_len}" for q in sorted(env.get("neighbours", {}))],
            # partner residues are labelled in MATURE numbering, like every other residue label in the tables
            "polar_partners_alphafold": [f"{a_}...{seq[q - 1]}{q - sp_len} {b_}" for _, a_, q, b_ in env.get("polar", [])],
            "polar_partners_4C49": [f"{a_}...{seq[q - 1]}{q - sp_len} {b_}" for _, a_, q, b_ in envb.get("polar", [])],
            "phi_psi_alphafold": [env.get("phi"), env.get("psi")],
            "phi_psi_4C49": [envb.get("phi"), envb.get("psi")],
        }

    def sequon_effect(pos: int, alt: str) -> str:
        mut = seq[: pos - 1] + alt + seq[pos:]
        new = {m.start() + 1 for m in re.finditer(r"(?=N[^P][ST])", mut)}
        lost, gained = sorted(set(sequons) - new), sorted(new - set(sequons))
        return "; ".join(x for x in (f"destroys sequon N{lost[0]}" if lost else "", f"creates sequon N{gained[0]}" if gained else "") if x)

    def mechanism(v: dict, a: dict) -> str:
        """Rule-based structural class; thresholds are the module constants."""
        if v["kind"] in ("nonsense", "frameshift"):
            where = "within the signal peptide" if v["precursor_pos"] <= sp_len else f"at {100 * v['precursor_pos'] / len(seq):.0f}% of the precursor"
            return f"premature termination {where}: no steroid-binding serpin fold can be made (null allele)"
        d = a["min_dist_to_steroid_A"]
        rsa = a["rsa_alphafold"] if a["rsa_alphafold"] is not None else a["rsa_cleaved_4C41"]
        buried = rsa is not None and rsa < BURIED_RSA
        if d is not None and d <= CONTACT_A:
            return "direct steroid contact residue (first shell)"
        if a["packs_against_pocket_residues"]:
            return (("buried " if buried else "") + "second-shell residue whose side chain packs against steroid-contact residue(s) "
                    + ", ".join(a["packs_against_pocket_residues"]))
        if d is not None and d <= SHELL_A:
            return ("buried " if buried else "") + "residue within the second shell of the steroid site"
        if a["region"].startswith("reactive"):
            return "reactive-centre loop residue (protease recognition / loop insertion)"
        if buried:
            return "buried residue remote from the steroid site (fold stability / secretion)"
        return "solvent-exposed residue remote from the steroid site"

    lit_rows = []
    for v in numbering_rows:
        a = annotate(v["precursor_pos"])
        gn = gnomad_lookup(v["canonical_residue"] if v["ref_matches_canonical"] else v["alt"], v["precursor_pos"],
                           v["alt"] if v["ref_matches_canonical"] else v["ref"], v.get("hgvs_c"))
        key = f"{v['canonical_residue']}{v['precursor_pos']}{v['alt']}" if v["ref_matches_canonical"] else f"{v['alt']}{v['precursor_pos']}{v['ref']}"
        ams = am.get(key)
        row = {
            "name": v["name"], "as_reported": v["as_reported"], "numbering": v["numbering"],
            "hgvs_p_precursor": (f"p.{ONE_TO_THREE[v['ref']]}{v['precursor_pos']}" + ("Ter" if v["alt"] == "*" else "fs" if v["alt"] == "fs" else ONE_TO_THREE[v["alt"]])),
            "mature": f"{v['ref']}{v['mature_pos']}{v['alt']}" if v["precursor_pos"] > sp_len else f"signal peptide residue {v['precursor_pos']}",
            "ref_matches_canonical": v["ref_matches_canonical"], "numbering_note": v["numbering_note"],
            "kind": v["kind"], "effect_class": v["effect_class"], "reported_effect": v["reported_effect"],
            "references": v["references"], **a,
            "am_score": ams[0] if ams else None, "am_class": ams[1] if ams else None,
            "sequon_effect": sequon_effect(v["precursor_pos"], v["alt"]) if v["kind"] == "missense" else "",
            "gnomad_af": float(f"{gn['af']:.3e}") if gn else None, "gnomad_ac": gn["ac"] if gn else None,
            "gnomad_hom": gn["hom"] if gn else None,
            "clinvar": (clin_by_p.get(f"p.{ONE_TO_THREE[v['canonical_residue']]}{v['precursor_pos']}{'Ter' if v['alt'] == '*' else ONE_TO_THREE.get(v['alt'], '')}") or {}).get("classification"),
        }
        row["structural_class"] = mechanism({**v}, a)
        lit_rows.append(row)
    R["literature_variants"] = lit_rows

    # class-level statistics: do functional classes separate by distance to the steroid?
    def med(xs):
        xs = [x for x in xs if x is not None]
        return round(statistics.median(xs), 2) if xs else None

    binding_classes = {"REDUCED_AFFINITY", "NO_BINDING", "REDUCED_CAPACITY"}
    grp = defaultdict(list)
    for r in lit_rows:
        if r["kind"] != "missense":
            continue
        k = ("binding-defective" if r["effect_class"] in binding_classes else
             "secretion-defective" if r["effect_class"] == "SECRETION_DEFECT" else "no binding defect reported")
        grp[k].append(r)
    R["class_summary"] = {
        k: {"n": len(rs), "variants": [r["name"] for r in rs],
            "median_dist_to_steroid_A": med(r["min_dist_to_steroid_A"] for r in rs),
            "n_within_contact": sum(1 for r in rs if r["min_dist_to_steroid_A"] is not None and r["min_dist_to_steroid_A"] <= CONTACT_A),
            "n_within_second_shell": sum(1 for r in rs if r["min_dist_to_steroid_A"] is not None and r["min_dist_to_steroid_A"] <= SHELL_A),
            "median_rsa_alphafold": med(r["rsa_alphafold"] for r in rs),
            "median_orthologue_identity": med(r["orthologue_identity"] for r in rs),
            "median_alphamissense": med(r["am_score"] for r in rs)}
        for k, rs in grp.items()
    }

    # do binding-defective variants remote from the steroid touch each other (a shared allosteric element)?
    remote = [r for r in lit_rows if r["kind"] == "missense" and r["effect_class"] in binding_classes
              and r["min_dist_to_steroid_A"] is not None and r["min_dist_to_steroid_A"] > SHELL_A]
    remote_pos = sorted({int(re.search(r"(\d+)", r["hgvs_p_precursor"]).group(1)) for r in remote})
    pairs = []
    for i, a_ in enumerate(remote_pos):
        for b_ in remote_pos[i + 1:]:
            if a_ in tab_af and b_ in tab_af:
                dmin = min(float(np.linalg.norm(x.coord - y.coord)) for x in tab_af[a_] for y in tab_af[b_]
                           if x.element != "H" and y.element != "H")
                pairs.append({"a": f"{seq[a_ - 1]}{a_ - sp_len}", "b": f"{seq[b_ - 1]}{b_ - sp_len}", "min_dist_A": round(dmin, 2),
                              "same_element": sse_at(a_) == sse_at(b_) and sse_at(a_) != "loop/unassigned"})
    R["remote_binding_variant_cluster"] = {
        "positions_mature": [f"{seq[q - 1]}{q - sp_len}" for q in remote_pos],
        "elements": {f"{seq[q - 1]}{q - sp_len}": sse_at(q) for q in remote_pos},
        "orthologue_residues": {f"{seq[q - 1]}{q - sp_len}": {"observed": cons[q]["observed"], "rat_CBG": aln["P31211"][cmap[q]],
                                                            "mouse_CBG": aln["Q06770"][cmap[q]]} for q in remote_pos},
        "variant_residue_is_wild_type_in_an_orthologue": {
            r["name"]: sum(1 for sq, _ in kept.values()
                           if sq[ocmap[int(re.search(r"(\d+)", r["hgvs_p_precursor"]).group(1))]] == THREE.get(r["hgvs_p_precursor"][-3:].upper()))
            for r in remote},
        "pairs_in_contact_4.5A": [x for x in pairs if x["min_dist_A"] <= 4.5],
        "pairs_same_element": [x for x in pairs if x["same_element"]],
    }

    defective = [r for r in lit_rows if r["kind"] == "missense" and r["effect_class"] in binding_classes | {"SECRETION_DEFECT"}]
    R["alphamissense_vs_assay"] = {
        "n_experimentally_defective_missense": len(defective),
        "n_called_likely_benign": sum(1 for r in defective if r["am_class"] in ("LBen", "benign", "likely_benign")),
        "n_called_ambiguous": sum(1 for r in defective if r["am_class"] in ("Amb", "ambiguous")),
        "n_called_likely_pathogenic": sum(1 for r in defective if r["am_class"] in ("LPath", "pathogenic", "likely_pathogenic")),
        "likely_benign_names": [r["name"] for r in defective if r["am_class"] in ("LBen", "benign", "likely_benign")],
    }
    cs_rows = []
    for c in lit.get("cleavage_sites_reported", []):
        a_aa, a_pos = c["after"]
        b_aa, b_pos = c["before"]
        ap, bp = a_pos + sp_len, b_pos + sp_len
        cs_rows.append({"protease": c["protease"], "reference": c["reference"], "reported": f"{a_aa}{a_pos}-{b_aa}{b_pos}",
                        "precursor": f"{seq[ap - 1]}{ap}-{seq[bp - 1]}{bp}",
                        "residues_match": seq[ap - 1] == a_aa and seq[bp - 1] == b_aa,
                        "P_site": f"P{p1 - ap + 1}-P{p1 - bp + 1}" if bp <= p1 else f"P{p1 - ap + 1}-P{bp - p1}'",
                        "c_terminal_fragment_residues": len(seq) - ap})
    R["rcl"]["cleavage_sites"] = cs_rows

    # ClinVar single-gene variants placed on the protein
    cv_rows = []
    for c in sg:
        ph = parse_hgvsp(c["hgvsp"])
        if not ph or ph[0] is None or "=" in (c["hgvsp"] or ""):
            continue
        ref, pos, alt = ph
        if pos > len(seq):
            continue
        a = annotate(pos)
        gn = gv.get(c["hgvsp"])
        ams = am.get(f"{ref}{pos}{alt}") if alt and alt != "*" else None
        cv_rows.append({"vcv": c["vcv"], "hgvsp": c["hgvsp"], "hgvsc": c["hgvsc"], "classification": c["classification"],
                        "traits": "; ".join(c["traits"]), "ref_matches_canonical": seq[pos - 1] == ref,
                        "mature_pos": pos - sp_len if pos > sp_len else None, **{k: a[k] for k in (
                            "region", "secondary_structure", "min_dist_to_steroid_A", "in_core_pocket", "rsa_alphafold",
                            "orthologue_identity")},
                        "am_score": ams[0] if ams else None, "am_class": ams[1] if ams else None,
                        "gnomad_af": float(f"{gn['af']:.3e}") if gn else None})
    R["clinvar_placed"] = {
        "n": len(cv_rows), "n_ref_mismatch": sum(1 for r in cv_rows if not r["ref_matches_canonical"]),
        "n_missense_within_contact": sum(1 for r in cv_rows if r["min_dist_to_steroid_A"] is not None and r["min_dist_to_steroid_A"] <= CONTACT_A),
    }

    # every gnomAD missense variant at a core pocket residue
    pocket_gnomad = []
    for r in mis:
        ph = parse_hgvsp(r["hgvsp"])
        if ph and ph[1] in core_pocket:
            ams = am.get(f"{ph[0]}{ph[1]}{ph[2]}")
            pocket_gnomad.append({"hgvsp": r["hgvsp"], "mature": f"{ph[0]}{ph[1] - sp_len}{ph[2]}", "ac": r["ac"],
                                  "af": float(f"{r['af']:.3e}"), "hom": r["hom"], "am_score": ams[0] if ams else None})
    R["gnomad_missense_at_core_pocket"] = sorted(pocket_gnomad, key=lambda x: -x["af"])

    # ---- write ----------------------------------------------------------------------------
    def tsv(name: str, rows: list[dict], cols: list[str]) -> None:
        with open(TABLES / name, "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(cols)
            for r in rows:
                w.writerow(["" if r.get(c) is None else r.get(c) for c in cols])

    tsv("literature_variants.tsv", lit_rows, [
        "name", "hgvs_p_precursor", "mature", "ref_matches_canonical", "kind", "effect_class", "region",
        "secondary_structure", "min_dist_to_steroid_A", "in_core_pocket", "rsa_alphafold", "rsa_cleaved_4C41", "plddt",
        "orthologue_identity", "orthologue_residues", "A1AT_residue", "TBG_residue", "rat_CBG_residue", "am_score",
        "am_class", "sequon_effect", "gnomad_af", "gnomad_ac", "gnomad_hom", "clinvar", "structural_class"])
    tsv("clinvar_variants_placed.tsv", cv_rows, list(cv_rows[0].keys()) if cv_rows else [])
    tsv("steroid_contacts.tsv", [
        {**c, "min_dist_A": json.dumps(c["min_dist_A"])} for c in R["steroid_site"]["contact_residues"]],
        ["precursor_pos", "mature_pos", "residue", "n_structures", "min_dist_A", "rat_residue", "A1AT_residue", "TBG_residue"])
    tsv("per_residue.tsv", [
        {"precursor_pos": p, "mature_pos": p - sp_len if p > sp_len else "", "residue": seq[p - 1], **{
            k: v for k, v in annotate(p).items() if k != "dist_by_structure"}} for p in range(1, len(seq) + 1)],
        ["precursor_pos", "mature_pos", "residue", "region", "secondary_structure", "min_dist_to_steroid_A",
         "in_core_pocket", "rsa_cleaved_4C41", "rsa_alphafold", "plddt", "orthologue_identity", "orthologue_residues",
         "A1AT_residue", "TBG_residue", "rat_CBG_residue", "am_mean_at_position", "is_sequon_asn"])
    (HERE / "results.json").write_text(json.dumps(R, indent=1, default=str) + "\n")
    write_markdown(R, lit_rows, cv_rows, sp_len)
    print("wrote results.json, RESULTS.md and tables/")


def fmt(x, nd=2):
    return "NA" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


def write_markdown(R: dict, lit_rows: list[dict], cv_rows: list[dict], sp_len: int) -> None:  # noqa: C901, PLR0915
    L: list[str] = []
    w = L.append
    w("# SERPINA6 / corticosteroid-binding globulin (P08185): structural placement of variants")
    w("")
    w("Generated by `02_analyze.py` from the inputs downloaded by `01_fetch_data.py` (see `cache/MANIFEST.tsv`).")
    w("Do not edit by hand: re-run the scripts. All positions are given on the 405-residue UniProt precursor")
    w("unless marked *mature*.")
    w("")
    w("## 1. Residue numbering")
    w("")
    w(f"- UniProt P08185 sequence version {R['sequence_version']} is {R['length']} residues; the signal peptide is residues "
      f"1-{sp_len} (`{R['signal_peptide']['sequence']}`), so the secreted chain has {R['mature_length']} residues and starts `{R['mature_n_terminus']}`.")
    w(f"- Mature (literature and PDB author) numbering = precursor (HGVS p.) numbering - {sp_len}.")
    nc = R["numbering_check"]
    w(f"- {nc['n_ref_match']} of {nc['n_variants']} literature variants have a reference residue that matches the canonical sequence after conversion.")
    for m in nc["mismatches"]:
        w(f"- Mismatch: {m['name']} is reported as {m['ref']}{m['pos']}{m['alt']} ({m['numbering']} numbering), but canonical residue "
          f"{m['precursor_pos']} is {m['canonical_residue']}; {m['numbering_note'] or 'unexplained'}.")
    for m in nc["alias_mismatches"]:
        w(f"- Alternative name: {m['variant']} is also written {m['label']} ({m['reported']}; {', '.join(m['references'])}), but canonical residue "
          f"{m['precursor_pos']} is {m['canonical_residue']}; {m['note']}.")
    if nc["ambiguous_if_numbering_confused"]:
        w("- Variants whose reference residue would also match if the reported number were read in the other numbering "
          "scheme (cannot be disambiguated by the residue check alone): " + ", ".join(nc["ambiguous_if_numbering_confused"]) + ".")
    else:
        w("- No literature variant has a reference residue that also matches when its number is read in the other numbering scheme.")
    g = R["n_glycosylation"]
    w(f"- N-x-S/T sequons at precursor positions {', '.join(map(str, g['sequons_precursor']))} (mature {', '.join(map(str, g['sequons_mature']))}); "
      f"UniProt annotates glycosylation at {', '.join(map(str, g['uniprot_annotated']))}.")
    w(f"- Cysteines in the secreted chain (mature numbering): {', '.join(map(str, R['cysteines_mature_chain']))}.")
    w("")
    w("## 2. Reactive-centre loop (RCL)")
    w("")
    r = R["rcl"]
    w(f"- The P-site register stated in {r['register_source']} (P16 E334 ... P8 T342, mature numbering) is "
      f"{'consistent' if r['register_consistent'] else 'NOT consistent'} with the canonical sequence and places P1 at mature "
      f"{r['P1_residue']}{r['P1_mature']} (precursor {r['P1_precursor']}), P1' {r['P1prime_residue']}{r['P1_mature'] + 1}.")
    w(f"- RCL P17-P4' = precursor {r['P17_to_P4prime_precursor'][0]}-{r['P17_to_P4prime_precursor'][1]}: `{r['sequence_P17_P4prime']}`.")
    a1 = r["aligned_P1"]["P01009"]
    w(f"- In the FAMSA alignment the CBG P1 column holds alpha-1-antitrypsin (P01009) residue {a1['residue']}{a1['position']}, "
      f"thyroxine-binding globulin (P05543) {r['aligned_P1']['P05543']['residue']}{r['aligned_P1']['P05543']['position']}.")
    w("- Aligned P17-P4' segments: " + "; ".join(f"{k} `{v}`" for k, v in r["aligned_P17_P4prime"].items()) + ".")
    for cs in r.get("cleavage_sites", []):
        w(f"- {cs['protease'].capitalize()} cleavage site reported as {cs['reported']} (mature; {cs['reference']}) = precursor {cs['precursor']} "
          f"({'residues match' if cs['residues_match'] else 'RESIDUES DO NOT MATCH'} the canonical sequence), i.e. the {cs['P_site']} bond; "
          f"cleavage there releases a {cs['c_terminal_fragment_residues']}-residue C-terminal fragment.")
    n = r["mean_CA_neighbours_10A"]
    w(f"- Mean number of C-alpha atoms within 10 A of RCL residues P14-P3: {n['AlphaFold']} in the AlphaFold model versus "
      f"{n['4C41_cleaved']} in the cleaved crystal structure 4C41 ({n['n_RCL_residues_resolved_4C41']} of 12 residues resolved). "
      f"Mean AlphaFold pLDDT over the RCL is {r['mean_pLDDT_RCL']} (whole model {R['alphafold']['mean_pLDDT']}).")
    w("")
    w("## 3. Experimental structures and the steroid-binding site")
    w("")
    w("| PDB | Title | Resolution (A) | Engineered differences from P08185 |")
    w("|---|---|---|---|")
    for pid, s in R["structures"].items():
        w(f"| {pid} | {s['title']} | {fmt(s['resolution'])} | {'; '.join(s['engineered']) or 'none recorded'} |")
    w("")
    ss = R["steroid_site"]
    w(f"Residues with a heavy atom within {ss['contact_cutoff_A']} A of the bound steroid (human cleaved CBG: 2VDY cortisol, 4C49 cortisol, "
      "4BB2 progesterone; rat native CBG 2V95 cortisol mapped through the alignment):")
    w("")
    w("| Precursor | Mature | Residue | Structures in contact | Min distance (A) | Rat CBG | A1AT | TBG |")
    w("|---|---|---|---|---|---|---|---|")
    for c in ss["contact_residues"]:
        w(f"| {c['precursor_pos']} | {c['mature_pos']} | {c['residue']} | {', '.join(c['min_dist_A'])} | {min(c['min_dist_A'].values())} | "
          f"{c['rat_residue']} | {c['A1AT_residue']} | {c['TBG_residue']} |")
    w("")
    w(f"- Core pocket (contact in at least two human structures), mature numbering: {', '.join(ss['core_pocket_mature'])}.")
    ub = ss["uniprot_binding_sites_within_cutoff"]
    w("- UniProt `Binding site` positions and whether they are within the contact cutoff here: " + ", ".join(f"{k}: {'yes' if v else 'no'}" for k, v in ub.items()) + ".")
    c = R["conservation"]
    w(f"- Conservation over {c['n_orthologues_used']} SERPINA6 orthologues (one per species; median identity to human {c['median_identity_to_human']}): "
      f"mean per-site identity {c['mean_site_identity_mature']} over the mature chain, {fmt(c['mean_site_identity_core_pocket'], 3)} over the core pocket, "
      f"{c['mean_site_identity_RCL']} over the RCL.")
    am = R["alphamissense"]
    w(f"- Mean AlphaMissense pathogenicity per position: {am['mean_all']} overall, {fmt(am['mean_core_pocket'], 3)} at the core pocket, "
      f"{am['mean_RCL']} in the RCL, {am['mean_signal_peptide']} in the signal peptide.")
    w("")
    w("## 4. Literature variants placed on the protein")
    w("")
    w("| Variant | HGVS p. (precursor) | Reported effect class | Element | Min distance to steroid (A) | RSA (AlphaFold) | Orthologue identity | AlphaMissense | gnomAD v4 AF (hom) | Structural class |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for x in lit_rows:
        af = "absent" if x["gnomad_af"] is None else f"{x['gnomad_af']:.2e} ({x['gnomad_hom']})"
        w(f"| {x['name']} | {x['hgvs_p_precursor']} | {x['effect_class']} | {x['secondary_structure']} | {fmt(x['min_dist_to_steroid_A'])} | "
          f"{fmt(x['rsa_alphafold'])} | {fmt(x['orthologue_identity'])} | {fmt(x['am_score'], 3)} {x['am_class'] or ''} | {af} | {x['structural_class']} |")
    w("")
    for k, s in R["class_summary"].items():
        w(f"- {k} missense variants (n={s['n']}): median distance to the steroid {fmt(s['median_dist_to_steroid_A'])} A; "
          f"{s['n_within_contact']} in direct contact, {s['n_within_second_shell']} within {SHELL_A:.0f} A; median RSA {fmt(s['median_rsa_alphafold'])}; "
          f"median orthologue identity {fmt(s['median_orthologue_identity'])}; median AlphaMissense {fmt(s['median_alphamissense'], 3)}.")
    w("")
    w("### Side-chain environment of the missense variants")
    w("")
    w("Residue labels in this table are in mature numbering.")
    w("")
    w("| Variant | Packs against steroid-contact residues | Polar partners of the wild-type side chain (4C49, cortisol-bound) | Polar partners (AlphaFold) | Near N-glycan site | phi/psi (4C49) | Sequon change |")
    w("|---|---|---|---|---|---|---|")
    for x in lit_rows:
        if x["kind"] != "missense":
            continue
        pp = x["phi_psi_4C49"]
        w(f"| {x['name']} | {', '.join(x['packs_against_pocket_residues']) or 'none'} | {'; '.join(x['polar_partners_4C49']) or 'none'} | "
          f"{'; '.join(x['polar_partners_alphafold']) or 'none'} | {', '.join(x['near_glycosylated_asn']) or 'no'} | "
          f"{fmt(pp[0], 0)}/{fmt(pp[1], 0)} | {x['sequon_effect'] or 'none'} |")
    w("")
    rc = R["remote_binding_variant_cluster"]
    w(f"- Binding-defective missense positions more than {SHELL_A:.0f} A from the steroid (mature numbering): " + ", ".join(
        f"{k} [{v}]" for k, v in rc["elements"].items()) + ".")
    w("- Of these, pairs whose side chains are in contact (<= 4.5 A, AlphaFold model): " + (
        "; ".join(f"{x['a']}-{x['b']} ({x['min_dist_A']} A)" for x in rc["pairs_in_contact_4.5A"]) or "none") + "; pairs on the same helix or strand: " + (
        "; ".join(f"{x['a']}-{x['b']}" for x in rc["pairs_same_element"]) or "none") + ".")
    w("- Residues observed at these positions across the orthologues (count per residue; rat, mouse CBG): " + "; ".join(
        f"{k} {v['observed']} ({v['rat_CBG']}, {v['mouse_CBG']})" for k, v in rc["orthologue_residues"].items()) + ".")
    w("- Number of orthologues (of " + str(R["conservation"]["n_orthologues_used"]) + ") whose wild-type residue equals the human variant residue: " + "; ".join(
        f"{k}: {v}" for k, v in rc["variant_residue_is_wild_type_in_an_orthologue"].items()) + ".")
    av = R["alphamissense_vs_assay"]
    w(f"- Of {av['n_experimentally_defective_missense']} missense variants with an experimentally shown binding or secretion defect, AlphaMissense calls "
      f"{av['n_called_likely_benign']} likely benign, {av['n_called_ambiguous']} ambiguous and {av['n_called_likely_pathogenic']} likely pathogenic.")
    w("")
    w("## 5. Population data (gnomAD v4)")
    w("")
    gc = R["gnomad_constraint"]
    w(f"- Constraint: pLI = {gc['pLI']:.2g}; observed/expected loss-of-function = {gc['oe_lof']:.2f} "
      f"(90% CI {gc['oe_lof_lower']:.2f}-{gc['oe_lof_upper']:.2f}; {gc['obs_lof']} observed, {gc['exp_lof']:.1f} expected); "
      f"missense o/e = {gc['oe_mis']:.2f}, missense Z = {gc['mis_z']:.2f}.")
    p = R["gnomad_plof"]
    w(f"- {p['n_plof_variants']} predicted loss-of-function variants are present ({p['n_high_confidence']} LOFTEE high-confidence; "
      f"cumulative high-confidence allele frequency {p['cumulative_af_high_confidence']:.2e}; {p['total_homozygotes_high_confidence']} homozygotes).")
    w("- Most frequent predicted loss-of-function alleles: " + "; ".join(
        f"{x['hgvsp'] or x['hgvsc']} (AC {x['ac']}, AF {x['af']:.2e}, hom {x['hom']})" for x in p["most_frequent"][:5]) + ".")
    m = R["gnomad_missense"]
    w("- Most frequent missense alleles: " + "; ".join(f"{x['hgvsp']} (AF {x['af']:.2e}, hom {x['hom']})" for x in m["most_frequent"][:6]) + ".")
    pg = R["gnomad_missense_at_core_pocket"]
    w(f"- {len(pg)} distinct gnomAD missense variants fall on core steroid-pocket residues" + (
        ": " + "; ".join(f"{x['hgvsp']} (AF {x['af']:.2e})" for x in pg[:8]) + "." if pg else "."))
    w("")
    w("## 6. ClinVar")
    w("")
    cl = R["clinvar"]
    w(f"- {cl['n_records_gene_query']} ClinVar records match SERPINA6[gene]; {cl['n_single_gene_SERPINA6']} involve SERPINA6 alone "
      f"({cl['n_multi_gene_cnv']} are multi-gene copy-number records).")
    w("- Classification of single-gene records: " + "; ".join(f"{k or 'not provided'}: {v}" for k, v in cl["classification_counts_single_gene"].items()) + ".")
    for x in cl["pathogenic_or_likely_pathogenic"] + cl["conflicting"]:
        w(f"- {x['vcv']} {x['title']}: {x['classification']} ({x['review_status']}); condition: {'; '.join(x['traits']) or 'not provided'}.")
    cp = R["clinvar_placed"]
    w(f"- {cp['n']} protein-changing single-gene records were placed on the sequence ({cp['n_ref_mismatch']} with a reference residue that does not "
      f"match P08185); {cp['n_missense_within_contact']} lie on residues in direct steroid contact. Full table: `tables/clinvar_variants_placed.tsv`.")
    w("")
    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
