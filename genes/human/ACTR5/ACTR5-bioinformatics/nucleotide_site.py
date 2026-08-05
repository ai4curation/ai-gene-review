#!/usr/bin/env python3
"""Is human ARP5 (ACTR5, Q9H9F9) a nucleotide-binding actin-fold protein, and
could it polymerise?

Why this is worth computing.  ACTR5's GO record contains no nucleotide-binding
annotation of any kind, while every actin-family paralog reviewed alongside it
(ACTR1A, ACTR1B, ACTR10) now carries one, justified from a ligand resolved in a
cryo-EM structure of its complex.  Meanwhile UniProt calls ACTR5 a member of
"the actin family, ARP5 subfamily" and CDD annotates it `ASKHA_NBD_Arp5`, so a
nucleotide site is *asserted* by fold assignment but nowhere tested.

Method.  Every number below is computed; nothing is hardcoded from prose.

1.  For each PDB entry UniProt lists for Q9H9F9, resolve which chain is ARP5
    from the PDBe SIFTS UniProt mapping.  A missing Q9H9F9 mapping is a hard
    error, never a silent zero.
2.  Enumerate all non-polymer ligands and their chain.  Report nucleotides that
    sit in the ARP5 chain, with the ARP5 residues within `CONTACT_CUTOFF`.
3.  Reciprocal site test.  Take conventional beta-actin's own ATP contacts from
    PDB 2BTF, align ACTR5 to beta-actin, and ask whether ARP5's *observed*
    nucleotide contacts fall on positions that align to beta-actin's own ATP
    contacts.  Finding a ligand is not enough; it has to be the same site.
4.  ATP-hydrolysis trigger.  Check the five literature-defined actin catalytic
    positions (Asp11, Gln137, Asp154, Val159, His161 in ACTB numbering) in
    ACTR5 and in a benchmark panel.  The script asserts these positions carry
    the expected residue in ACTB before mapping anything, and cross-checks its
    ACTR5 answer against the independently committed
    ACTL7A-bioinformatics/results.json.
5.  Opposite direction: the F-actin protomer-protomer interface (PDB 8A2S, the
    same entry the ACTL7A review used) mapped onto ACTR5, with a benchmark
    panel of conventional actins, the filament-forming Arp1, other nuclear
    ARPs, and the ARP5 orthologs that donate ACTR5's IBA annotations.  Repeated
    under a second substitution matrix and gap model for robustness.

Writes results.json.  RESULTS.md is generated from that file by
write_results.py so the report cannot drift from the computation.
"""

from __future__ import annotations

import gzip
import json
from collections import Counter
from pathlib import Path

import gemmi
import numpy as np
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
CIF_DIR = HERE / "structures"

ACTR5_ACC = "Q9H9F9"
ACTB_ACC = "P60709"  # human beta-actin: the numbering frame for every site below

ARP5_ENTRIES = ["6hts", "7zi4", "9gcg", "9ge5", "9gev", "9gfb"]
G_ACTIN_ENTRY = "2btf"  # profilin-beta-actin + ATP (as used by the ACTL8 review)
F_ACTIN_ENTRY = "8a2s"  # cryo-EM F-actin, 5 protomers (as used by the ACTL7A review)

NUCLEOTIDES = {"ATP", "ADP", "AMP", "ANP", "ADX", "AGS", "ACP", "GTP", "GDP"}
IONS = {"MG", "ZN", "CA", "MN", "BEF", "ALF", "AF3", "PO4", "POP"}
# Groups that turn a bound ADP into an ATP/transition-state mimic. Whether one of
# these sits in the SAME chain as the ADP decides whether the ligand is plain ADP
# or ADP-BeF3, which is the difference between "ADP is what is bound" and "an ATP
# analogue is what is bound". Raised by the PR review of #2291.
ATP_MIMICS = {"BEF", "ALF", "AF3", "VO4", "PO4"}

CONTACT_CUTOFF = 4.0
INTERFACE_CUTOFF = 4.5
PROTOMER_FRACTION = 0.5

# Literature-defined actin ATP-hydrolysis positions, ACTB numbering. Identical
# set to genes/human/ACTL7A/ACTL7A-bioinformatics (kept deliberately in sync so
# the two reviews' numbers are comparable).
CATALYTIC_RESIDUES: dict[int, str] = {11: "D", 137: "Q", 154: "D", 159: "V", 161: "H"}

CONSERVATIVE_GROUPS = [
    set("AGSTP"), set("ILVMC"), set("FYW"), set("KRH"), set("DE"), set("NQ"),
]

# Benchmark panel. group labels are used only for grouping in the report.
PANEL: dict[str, tuple[str, str]] = {
    "ACTB_HUMAN": ("P60709", "conventional_actin"),
    "ACTA1_HUMAN": ("P68133", "conventional_actin"),
    "ARP1_ACTR1A_HUMAN": ("P61163", "filament_forming_arp"),
    "ARP3_ACTR3_HUMAN": ("P61158", "nucleotide_binding_arp"),
    "ARP11_ACTR10_HUMAN": ("Q9NZ32", "divergent_arp"),
    "ARP4_ACTL6A_HUMAN": ("O96019", "nuclear_arp"),
    "ARP6_ACTR6_HUMAN": ("Q9GZN1", "nuclear_arp"),
    "ARP8_ACTR8_HUMAN": ("Q9H981", "nuclear_arp"),
    "ARP5_HUMAN": ("Q9H9F9", "query"),
    "ARP5_DROME": ("Q9VEC3", "arp5_ortholog_iba_donor"),
    "ARP5_YEAST": ("P53946", "arp5_ortholog_iba_donor"),
    "ARP5_SCHPO": ("Q9Y7X8", "arp5_ortholog_iba_donor"),
    "ARP5_ARATH": ("Q940Z2", "arp5_ortholog_iba_donor"),
}


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def fetch_json(url: str) -> dict:
    r = requests.get(url, headers={"Accept": "application/json"}, timeout=180)
    if r.status_code != 200:
        die(f"{url} returned HTTP {r.status_code}")
    return r.json()


def fetch_cif(pdb_id: str) -> Path:
    CIF_DIR.mkdir(exist_ok=True)
    path = CIF_DIR / f"{pdb_id}.cif.gz"
    if not path.exists():
        r = requests.get(
            f"https://www.ebi.ac.uk/pdbe/entry-files/download/{pdb_id}.cif", timeout=900
        )
        if r.status_code != 200:
            die(f"could not download mmCIF for {pdb_id} (HTTP {r.status_code})")
        path.write_bytes(gzip.compress(r.content))
    return path


_SEQ_CACHE: dict[str, str] = {}


def uniprot_sequence(acc: str) -> str:
    if acc in _SEQ_CACHE:
        return _SEQ_CACHE[acc]
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=180)
    if r.status_code != 200:
        die(f"UniProt {acc} returned HTTP {r.status_code}")
    d = r.json()
    # the only reliable liveness guard: the entry actually returned is the one asked for
    if d.get("primaryAccession") != acc:
        die(f"UniProt returned {d.get('primaryAccession')!r} for requested {acc}")
    seq = d["sequence"]["value"]
    if not seq:
        die(f"UniProt {acc} returned an empty sequence (dead or deleted entry?)")
    _SEQ_CACHE[acc] = seq
    return seq


def sifts_chains(pdb_id: str) -> dict[str, dict]:
    """auth-or-label chain id -> {accession, name, offset} from PDBe SIFTS.

    `offset` converts the residue numbering PDBe reports (`residue_number`,
    i.e. label_seq) into UniProt numbering for that accession.
    """
    d = fetch_json(f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id}")
    out: dict[str, dict] = {}
    for acc, v in d.get(pdb_id, {}).get("UniProt", {}).items():
        for m in v.get("mappings", []):
            ch = m["chain_id"]
            offset = m["unp_start"] - m["start"]["residue_number"]
            auth_start = m["start"].get("author_residue_number")
            out.setdefault(
                ch,
                {
                    "accession": acc,
                    "name": v.get("name"),
                    "label_to_unp_offset": offset,
                    "auth_start": auth_start,
                    "auth_to_unp_offset": (
                        m["unp_start"] - auth_start if auth_start is not None else None
                    ),
                },
            )
    return out


def entry_resolution(pdb_id: str) -> float | None:
    """PDBe-reported resolution, so the report never hardcodes a number."""
    d = fetch_json(f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/experiment/{pdb_id}")
    for exp in d.get(pdb_id, []):
        r = exp.get("resolution")
        if r is not None:
            return float(r)
    return None


def load_model(pdb_id: str) -> gemmi.Structure:
    st = gemmi.read_structure(str(fetch_cif(pdb_id)))
    st.setup_entities()
    st.remove_alternative_conformations()
    st.remove_hydrogens()
    return st


def is_aa(res: gemmi.Residue) -> bool:
    info = gemmi.find_tabulated_residue(res.name)
    return info is not None and info.is_amino_acid()


def one_letter(res: gemmi.Residue) -> str:
    return gemmi.find_tabulated_residue(res.name).one_letter_code.upper()


def chain_of(st: gemmi.Structure, name: str) -> gemmi.Chain:
    for chain in st[0]:
        if chain.name == name:
            return chain
    die(f"chain {name} absent from {st.name}")


def unp_number(res: gemmi.Residue, info: dict) -> int | None:
    """UniProt position for a residue, using whichever numbering SIFTS anchored."""
    if info["auth_to_unp_offset"] is not None:
        return res.seqid.num + info["auth_to_unp_offset"]
    if res.label_seq is None:
        return None
    return res.label_seq + info["label_to_unp_offset"]


def all_ligands(st: gemmi.Structure) -> list[dict]:
    out = []
    for chain in st[0]:
        for res in chain:
            info = gemmi.find_tabulated_residue(res.name)
            if info is not None and (info.is_amino_acid() or info.is_nucleic_acid()):
                continue
            if res.name in ("HOH", "DOD"):
                continue
            out.append({"chain": chain.name, "comp": res.name, "seqid": res.seqid.num})
    return out


def coords(res: gemmi.Residue) -> np.ndarray:
    return np.array([[a.pos.x, a.pos.y, a.pos.z] for a in res])


def ligand_contacts(
    st: gemmi.Structure, lig_chain: str, lig_comp: str, lig_seqid: int,
    prot_chain: str, chain_info: dict, cutoff: float,
) -> list[dict]:
    lig = None
    for res in chain_of(st, lig_chain):
        if res.name == lig_comp and res.seqid.num == lig_seqid:
            lig = coords(res)
    if lig is None or len(lig) == 0:
        die(f"ligand {lig_comp} {lig_chain}/{lig_seqid} not found in {st.name}")
    hits = []
    for res in chain_of(st, prot_chain):
        if not is_aa(res):
            continue
        c = coords(res)
        if len(c) == 0:
            continue
        d = float(np.linalg.norm(c[:, None, :] - lig[None, :, :], axis=2).min())
        if d <= cutoff:
            pos = unp_number(res, chain_info)
            hits.append(
                {"unp_pos": pos, "resname": res.name, "aa": one_letter(res),
                 "min_dist": round(d, 2)}
            )
    return sorted(hits, key=lambda h: (h["unp_pos"] is None, h["unp_pos"]))


def protomer_interface(
    st: gemmi.Structure, chains: list[str], chain_info: dict[str, dict], cutoff: float
) -> dict:
    """UniProt positions contacting a *different* protomer, per protomer."""
    residues = {}
    for ch in chains:
        rs = []
        for res in chain_of(st, ch):
            if is_aa(res):
                c = coords(res)
                if len(c):
                    rs.append((unp_number(res, chain_info[ch]), c))
        residues[ch] = rs

    per_chain: dict[str, set[int]] = {ch: set() for ch in chains}
    for i, ci in enumerate(chains):
        for cj in chains[i + 1:]:
            for pi, xi in residues[ci]:
                for pj, xj in residues[cj]:
                    if np.linalg.norm(xi.mean(0) - xj.mean(0)) > 25.0:
                        continue
                    d = np.linalg.norm(xi[:, None, :] - xj[None, :, :], axis=2).min()
                    if d <= cutoff:
                        if pi is not None:
                            per_chain[ci].add(pi)
                        if pj is not None:
                            per_chain[cj].add(pj)
    n_with = sum(1 for ch in chains if per_chain[ch])
    if n_with == 0:
        die(f"{st.name}: no inter-protomer contacts found")
    counts = Counter(p for ch in chains for p in per_chain[ch])
    consensus = sorted(p for p, n in counts.items() if n >= PROTOMER_FRACTION * n_with)
    return {"per_chain_counts": {ch: len(per_chain[ch]) for ch in chains},
            "n_protomers_with_contacts": n_with, "positions": consensus}


def align(query: str, ref: str, matrix: str = "BLOSUM62",
          open_gap: float = -11, extend_gap: float = -1):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load(matrix)
    aligner.open_gap_score = open_gap
    aligner.extend_gap_score = extend_gap
    aligner.mode = "global"
    aln = aligner.align(query, ref)[0]
    a_q, a_r = str(aln[0]), str(aln[1])
    ref_to_query: dict[int, int | None] = {}
    qi = ri = n_ident = n_aln = 0
    for cq, cr in zip(a_q, a_r):
        if cq != "-":
            qi += 1
        if cr != "-":
            ri += 1
            ref_to_query[ri] = qi if cq != "-" else None
        if cq != "-" and cr != "-":
            n_aln += 1
            n_ident += cq == cr
    return ref_to_query, {
        "aligned_columns": n_aln, "identities": n_ident,
        "percent_identity": round(100.0 * n_ident / n_aln, 1) if n_aln else 0.0,
        "matrix": matrix, "gap_open": open_gap, "gap_extend": extend_gap,
    }


def classify(q: str | None, r: str) -> str:
    if q is None:
        return "deleted"
    if q == r:
        return "identical"
    for grp in CONSERVATIVE_GROUPS:
        if q in grp and r in grp:
            return "conservative"
    return "non_conservative"


def transfer(site_positions: list[int], actb_seq: str, query_seq: str,
             ref_to_query: dict[int, int | None]) -> dict:
    rows = []
    for p in site_positions:
        if p is None or p > len(actb_seq):
            continue
        qp = ref_to_query.get(p)
        qa = query_seq[qp - 1] if qp else None
        rows.append({"actb_pos": p, "actb_aa": actb_seq[p - 1],
                     "query_pos": qp, "query_aa": qa,
                     "class": classify(qa, actb_seq[p - 1])})
    summary = Counter(r["class"] for r in rows)
    n = len(rows)
    return {"n_positions": n, "rows": rows, "summary": dict(summary),
            "percent_identical": round(100.0 * summary["identical"] / n, 1) if n else 0.0}


def main() -> None:
    res: dict = {
        "parameters": {
            "ligand_contact_cutoff_angstrom": CONTACT_CUTOFF,
            "interface_contact_cutoff_angstrom": INTERFACE_CUTOFF,
            "protomer_fraction": PROTOMER_FRACTION,
            "numbering_frame": f"human beta-actin {ACTB_ACC} UniProt numbering",
            "catalytic_residues": CATALYTIC_RESIDUES,
        }
    }

    actb_seq = uniprot_sequence(ACTB_ACC)
    actr5_seq = uniprot_sequence(ACTR5_ACC)
    # hard check: the catalytic positions must carry the expected residue in ACTB
    for pos, expected in CATALYTIC_RESIDUES.items():
        if actb_seq[pos - 1] != expected:
            die(f"ACTB {ACTB_ACC} position {pos} is {actb_seq[pos-1]}, expected {expected}; "
                "CATALYTIC_RESIDUES is not in this numbering frame")

    # ---------- 1-2: nucleotides in the ARP5 chain ----------
    entries = []
    for pdb_id in ARP5_ENTRIES:
        chains = sifts_chains(pdb_id)
        arp5 = sorted(c for c, v in chains.items() if v["accession"] == ACTR5_ACC)
        if not arp5:
            die(f"{pdb_id}: SIFTS has no {ACTR5_ACC} chain — refusing to report a silent zero")
        st = load_model(pdb_id)
        ligs = all_ligands(st)
        by_comp: dict[str, list[str]] = {}
        for L in ligs:
            by_comp.setdefault(L["comp"], []).append(L["chain"])
        e = {
            "pdb_id": pdb_id.upper(),
            "resolution_angstrom": entry_resolution(pdb_id),
            "arp5_chains": arp5,
            "chain_to_protein": {c: chains[c]["name"] for c in sorted(chains)},
            "ligand_inventory": {k: sorted(v) for k, v in sorted(by_comp.items())},
            "arp5_nucleotides": [],
            "arp5_ions": sorted({L["comp"] for L in ligs
                                 if L["chain"] in arp5 and L["comp"] in IONS}),
        }
        for L in ligs:
            if L["chain"] in arp5 and L["comp"] in NUCLEOTIDES:
                cont = ligand_contacts(st, L["chain"], L["comp"], L["seqid"],
                                       L["chain"], chains[L["chain"]], CONTACT_CUTOFF)
                mimics_same_chain = sorted(
                    {x["comp"] for x in ligs
                     if x["chain"] == L["chain"] and x["comp"] in ATP_MIMICS}
                )
                mimics_elsewhere = sorted(
                    {(x["comp"], x["chain"]) for x in ligs
                     if x["comp"] in ATP_MIMICS and x["chain"] != L["chain"]}
                )
                e["arp5_nucleotides"].append(
                    {"comp": L["comp"], "seqid": L["seqid"],
                     "n_contacts": len(cont), "contacts": cont,
                     "atp_mimic_in_same_chain": mimics_same_chain,
                     "atp_mimic_elsewhere_in_entry": [list(x) for x in mimics_elsewhere],
                     "ligand_is_plain_adp": not mimics_same_chain}
                )
        entries.append(e)
    res["arp5_structures"] = entries
    res["arp5_structures_with_nucleotide"] = [
        e["pdb_id"] for e in entries if e["arp5_nucleotides"]
    ]

    # ---------- 3: beta-actin's own ATP site (2BTF) ----------
    chains = sifts_chains(G_ACTIN_ENTRY)
    actin_ch = sorted(c for c, v in chains.items()
                      if (v.get("name") or "").upper().startswith("ACT"))
    if not actin_ch:
        die(f"{G_ACTIN_ENTRY}: no actin chain in SIFTS ({sorted(chains)})")
    ch = actin_ch[0]
    struct_acc = chains[ch]["accession"]
    struct_seq = uniprot_sequence(struct_acc)
    _, id_to_human = align(struct_seq, actb_seq)
    if id_to_human["percent_identity"] < 95.0:
        die(f"{G_ACTIN_ENTRY} actin {struct_acc} is only "
            f"{id_to_human['percent_identity']}% identical to human ACTB")
    st = load_model(G_ACTIN_ENTRY)
    nts = [L for L in all_ligands(st) if L["chain"] == ch and L["comp"] in NUCLEOTIDES]
    if not nts:
        die(f"{G_ACTIN_ENTRY} chain {ch}: no nucleotide found")
    g_contacts = ligand_contacts(st, ch, nts[0]["comp"], nts[0]["seqid"],
                                 ch, chains[ch], CONTACT_CUTOFF)
    g_site = sorted(c["unp_pos"] for c in g_contacts if c["unp_pos"])
    res["g_actin_pocket"] = {
        "pdb_id": G_ACTIN_ENTRY.upper(), "chain": ch,
        "structure_accession": struct_acc,
        "structure_entry_name": chains[ch]["name"],
        "identity_to_human_ACTB": id_to_human,
        "ligand": nts[0]["comp"], "n_positions": len(g_site),
        "positions": g_site,
        "residues": ["%s%d" % (c["aa"], c["unp_pos"]) for c in g_contacts if c["unp_pos"]],
    }

    # ---------- 5a: F-actin protomer interface (8A2S) ----------
    fchains_info = sifts_chains(F_ACTIN_ENTRY)
    fchains = sorted(c for c, v in fchains_info.items()
                     if (v.get("name") or "").upper().startswith("ACT"))
    if len(fchains) < 3:
        die(f"{F_ACTIN_ENTRY}: expected >=3 actin protomers, got {fchains}")
    fst = load_model(F_ACTIN_ENTRY)
    iface = protomer_interface(fst, fchains, fchains_info, INTERFACE_CUTOFF)
    f_acc = fchains_info[fchains[0]]["accession"]
    f_seq = uniprot_sequence(f_acc)
    f_to_human, f_id = align(f_seq, actb_seq)
    if f_id["percent_identity"] < 85.0:
        die(f"{F_ACTIN_ENTRY} actin {f_acc} only {f_id['percent_identity']}% identical to ACTB")
    # positions are in f_acc numbering -> convert to ACTB numbering
    human_to_f = {v: k for k, v in f_to_human.items() if v is not None}
    f_site = sorted({human_to_f[p] for p in
                     [hp for hp, fp in human_to_f.items() if fp in set(iface["positions"])]}
                    ) if False else sorted(
        {hp for hp, fp in human_to_f.items() if fp in set(iface["positions"])})
    res["f_actin_interface_site"] = {
        "pdb_id": F_ACTIN_ENTRY.upper(),
        "structure_accession": f_acc,
        "structure_entry_name": fchains_info[fchains[0]]["name"],
        "identity_to_human_ACTB": f_id,
        "chains": fchains,
        "per_chain_counts": iface["per_chain_counts"],
        "n_positions_structure_numbering": len(iface["positions"]),
        "n_positions": len(f_site),
        "positions": f_site,
    }

    # ---------- 3/4/5b: transfer both sites and the catalytic set onto the panel ----------
    panel: dict[str, dict] = {}
    for label, (acc, group) in PANEL.items():
        qseq = uniprot_sequence(acc)
        r2q, stats = align(qseq, actb_seq)
        cat = "".join(
            (qseq[r2q[p] - 1] if r2q.get(p) else "-") for p in sorted(CATALYTIC_RESIDUES)
        )
        n_cat = sum(c == CATALYTIC_RESIDUES[p]
                    for c, p in zip(cat, sorted(CATALYTIC_RESIDUES)))
        g_tr = transfer(g_site, actb_seq, qseq, r2q)
        f_tr = transfer(f_site, actb_seq, qseq, r2q)
        # Per-position rows are kept only for the query and for the two controls
        # that the argument rests on (conventional beta-actin and the
        # filament-forming Arp1). For the rest of the panel only the counts are
        # kept, so results.json stays comparable in size to the sibling reviews'
        # audits; nothing the report cites is dropped.
        if group not in ("query", "conventional_actin", "filament_forming_arp"):
            g_tr = {k: v for k, v in g_tr.items() if k != "rows"}
            f_tr = {k: v for k, v in f_tr.items() if k != "rows"}
        panel[label] = {
            "accession": acc, "group": group, "length": len(qseq),
            "alignment_to_ACTB": stats,
            "catalytic_residues": cat,
            "n_catalytic_conserved": n_cat,
            "g_pocket": g_tr,
            "f_interface": f_tr,
        }
        # robustness under a second matrix/gap model
        r2q2, stats2 = align(qseq, actb_seq, "BLOSUM45", -14, -2)
        panel[label]["second_model"] = {
            "alignment_to_ACTB": stats2,
            "catalytic_residues": "".join(
                (qseq[r2q2[p] - 1] if r2q2.get(p) else "-")
                for p in sorted(CATALYTIC_RESIDUES)
            ),
            "g_pocket_percent_identical": transfer(g_site, actb_seq, qseq, r2q2)["percent_identical"],
            "f_interface_percent_identical": transfer(f_site, actb_seq, qseq, r2q2)["percent_identical"],
        }
    res["panel"] = panel

    # ---------- 3 (continued): reciprocal check on ACTR5's observed contacts ----------
    r2q_actr5, _ = align(actr5_seq, actb_seq)
    actr5_positions_at_actin_pocket = sorted(
        {r2q_actr5[p] for p in g_site if r2q_actr5.get(p)}
    )
    recip = []
    for e in entries:
        for nt in e["arp5_nucleotides"]:
            obs = sorted({c["unp_pos"] for c in nt["contacts"] if c["unp_pos"]})
            shared = sorted(set(obs) & set(actr5_positions_at_actin_pocket))
            recip.append({
                "pdb_id": e["pdb_id"], "ligand": nt["comp"],
                "n_observed_contacts": len(obs),
                "n_on_aligned_actin_pocket": len(shared),
                "fraction_on_aligned_actin_pocket":
                    round(len(shared) / len(obs), 2) if obs else None,
                "observed_contacts": obs,
                "shared_with_actin_pocket": shared,
                "outside_actin_pocket": sorted(set(obs) - set(shared)),
            })
    res["reciprocal_site_check"] = recip
    res["actr5_positions_aligned_to_actin_pocket"] = actr5_positions_at_actin_pocket
    union_obs = sorted({p for r in recip for p in r["observed_contacts"]})
    res["actr5_observed_contact_union"] = {
        "positions": union_obs,
        "n": len(union_obs),
        "n_on_aligned_actin_pocket": len(set(union_obs) & set(actr5_positions_at_actin_pocket)),
    }

    # ---------- cross-check against the already-merged ACTL7A audit ----------
    actl7a = HERE.parents[1] / "ACTL7A" / "ACTL7A-bioinformatics" / "results.json"
    if actl7a.exists():
        other = json.loads(actl7a.read_text())
        theirs = other["catalytic_residues"]["per_sequence"].get("ARP5_HUMAN")
        mine = panel["ARP5_HUMAN"]["catalytic_residues"]
        res["crosscheck_ACTL7A_audit"] = {
            "file": str(actl7a.relative_to(HERE.parents[2])),
            "their_ARP5_HUMAN_catalytic_residues": theirs["residues"] if theirs else None,
            "our_ARP5_HUMAN_catalytic_residues": mine,
            "agree": bool(theirs and theirs["residues"] == mine),
        }
        if theirs and theirs["residues"] != mine:
            die("catalytic-residue string for ARP5_HUMAN disagrees with the committed "
                f"ACTL7A audit: ours={mine} theirs={theirs['residues']}")
    else:
        die(f"expected sibling audit at {actl7a} for cross-checking; not found")

    res["provenance"] = {"gemmi": gemmi.__version__, "script": Path(__file__).name}
    (HERE / "results.json").write_text(json.dumps(res, indent=2))
    print("ARP5 chains with a nucleotide:", res["arp5_structures_with_nucleotide"])
    print("reciprocal:", [(r["pdb_id"], r["ligand"], r["n_observed_contacts"],
                           r["n_on_aligned_actin_pocket"]) for r in recip])
    print("catalytic ARP5_HUMAN:", panel["ARP5_HUMAN"]["catalytic_residues"],
          panel["ARP5_HUMAN"]["n_catalytic_conserved"], "/", len(CATALYTIC_RESIDUES))
    print("crosscheck:", res["crosscheck_ACTL7A_audit"])
    print("g_pocket n=", res["g_actin_pocket"]["n_positions"],
          "f_interface n=", res["f_actin_interface_site"]["n_positions"])
    for k, v in panel.items():
        print("  %-24s %-24s cat=%s %d/5  pocket=%5.1f%%  iface=%5.1f%%  id=%4.1f%%" % (
            k, v["group"], v["catalytic_residues"], v["n_catalytic_conserved"],
            v["g_pocket"]["percent_identical"], v["f_interface"]["percent_identical"],
            v["alignment_to_ACTB"]["percent_identity"]))
    print("wrote", HERE / "results.json")


if __name__ == "__main__":
    main()
