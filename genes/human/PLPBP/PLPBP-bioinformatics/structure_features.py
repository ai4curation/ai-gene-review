"""Per-residue structural features of a query protein from its AlphaFold model,
with the PLP cofactor transplanted from PLP-bound homolog crystal structures.

For each query residue: pLDDT, relative side-chain-inclusive SASA, minimum
heavy-atom distance to PLP (per template, after CA superposition on aligned
residues), template secondary structure (HELIX/SHEET records), aligned
template residue, and family conservation (star alignment on the query).

Usage: structure_features.py --query-fasta F --model AF.pdb --family-fasta fam.fasta
        --template 1CT5.pdb:A --template 1W8G.pdb:A --out features.tsv --summary summary.json
"""
import argparse
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import PDBParser, ShrakeRupley, Superimposer
from Bio.PDB.Polypeptide import protein_letters_3to1

# Tien et al. 2013 theoretical max ASA
MAX_ASA = dict(A=129, R=274, N=195, D=193, C=167, E=223, Q=225, G=104, H=224, I=197, L=201,
               K=236, M=224, F=240, P=159, S=155, T=172, W=285, Y=263, V=174)
NONSTD = {"MSE": "M", "LLP": "K"}


def aligner() -> PairwiseAligner:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "global"
    al.end_gap_score = 0.0
    return al


def colmap(q: str, t: str) -> dict[int, int]:
    """0-based query index -> 0-based target index for aligned (ungapped) columns."""
    aln = aligner().align(q, t)[0]
    m = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for k in range(qe - qs):
            m[qs + k] = ts + k
    return m


def chain_seq(chain):
    res, seq = [], []
    for r in chain:
        name = r.get_resname().strip()
        if r.id[0] == " " or name in NONSTD:
            one = NONSTD.get(name) or protein_letters_3to1.get(name)
            if one and "CA" in r:
                res.append(r)
                seq.append(one)
    return res, "".join(seq)


def sec_struct(pdb_path: str, chain_id: str) -> dict[int, str]:
    ss = {}
    for line in open(pdb_path):
        if line.startswith("HELIX") and line[19] == chain_id:
            for i in range(int(line[21:25]), int(line[33:37]) + 1):
                ss[i] = "H"
        elif line.startswith("SHEET") and line[21] == chain_id:
            for i in range(int(line[22:26]), int(line[33:37]) + 1):
                ss[i] = "E"
    return ss


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query-fasta", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--family-fasta", required=True)
    ap.add_argument("--template", action="append", default=[], help="file.pdb:CHAIN")
    ap.add_argument("--ligand", default="PLP")
    ap.add_argument("--out", required=True)
    ap.add_argument("--summary", required=True)
    a = ap.parse_args()

    qrec = next(SeqIO.parse(a.query_fasta, "fasta"))
    q = str(qrec.seq)
    parser = PDBParser(QUIET=True)
    model = parser.get_structure("af", a.model)[0]
    mchain = next(iter(model))
    mres, mseq = chain_seq(mchain)
    if mseq != q:
        raise SystemExit("AlphaFold model sequence differs from the query FASTA")
    ShrakeRupley().compute(model, level="R")
    plddt = [r["CA"].get_bfactor() for r in mres]
    rsa = [min(1.5, r.sasa / MAX_ASA[s]) for r, s in zip(mres, q)]

    # conservation
    fam = [r for r in SeqIO.parse(a.family_fasta, "fasta")]
    cols = [Counter() for _ in q]
    nseq = 0
    for r in fam:
        s = str(r.seq)
        if s == q:
            continue
        nseq += 1
        m = colmap(q, s)
        for i in range(len(q)):
            cols[i][s[m[i]] if i in m else "-"] += 1
    ident, ent = [], []
    for i, c in enumerate(cols):
        ident.append(c[q[i]] / nseq)
        tot = sum(c.values())
        ent.append(-sum(v / tot * math.log2(v / tot) for v in c.values()))

    summary = {"query": qrec.id, "length": len(q), "n_family_sequences": nseq,
               "mean_plddt": float(np.mean(plddt)), "templates": {}}
    tcols = {}
    for spec in a.template:
        path, ch = spec.rsplit(":", 1)
        name = Path(path).stem
        ts = parser.get_structure(name, path)[0]
        tchain = ts[ch]
        tres, tseq = chain_seq(tchain)
        lig = [at for r in tchain if r.get_resname().strip() == a.ligand for at in r]
        if not lig:
            raise SystemExit(f"{name}: no {a.ligand} in chain {ch}")
        m = colmap(q, tseq)
        pairs = [(i, j) for i, j in m.items() if plddt[i] >= 70]
        sup = Superimposer()
        fixed = [mres[i]["CA"] for i, _ in pairs]
        moving = [tres[j]["CA"] for _, j in pairs]
        sup.set_atoms(fixed, moving)
        # iterative outlier rejection (2 rounds, 3 A)
        for _ in range(2):
            rot, tran = sup.rotran
            d = [np.linalg.norm(f.coord - (mv.coord @ rot + tran)) for f, mv in zip(fixed, moving)]
            keep = [k for k, x in enumerate(d) if x < 3.0]
            fixed = [fixed[k] for k in keep]
            moving = [moving[k] for k in keep]
            sup.set_atoms(fixed, moving)
        rot, tran = sup.rotran
        lig_xyz = np.array([at.coord @ rot + tran for at in lig])
        lig_names = [at.get_id() for at in lig]
        dist, near = [], []
        for r in mres:
            xyz = np.array([at.coord for at in r if at.element != "H"])
            dm = np.linalg.norm(xyz[:, None, :] - lig_xyz[None, :, :], axis=2)
            k = np.unravel_index(dm.argmin(), dm.shape)
            dist.append(float(dm.min()))
            near.append(lig_names[k[1]])
        ss = sec_struct(path, ch)
        ident_pairs = sum(q[i] == tseq[j] for i, j in m.items())
        # Schiff-base lysine: template residue whose NZ is within 1.8 A of PLP C4A
        c4a = next((at for at in lig if at.get_id() == "C4A"), None)
        schiff = None
        for j, r in enumerate(tres):
            if r.get_resname() == "LYS" and "NZ" in r and c4a is not None and (r["NZ"] - c4a) < 1.8:
                inv = {v: k for k, v in m.items()}
                schiff = {"template_residue": f"K{r.id[1]}",
                          "query_residue": (f"{q[inv[j]]}{inv[j] + 1}" if j in inv else None)}
        summary["templates"][name] = {
            "chain": ch, "aligned_columns": len(m), "identity_over_aligned": ident_pairs / len(m),
            "ca_pairs_used": len(fixed), "ca_rmsd": float(sup.rms), "schiff_base_lysine": schiff,
            "query_residues_within_4A_of_ligand": [f"{q[i]}{i + 1}" for i in range(len(q)) if dist[i] <= 4.0],
        }
        tcols[name] = (m, tres, tseq, dist, near, ss)

    with open(a.out, "w") as fh:
        hdr = ["pos", "aa", "plddt", "rsa", "family_identity", "family_entropy"]
        for n in tcols:
            hdr += [f"{n}_res", f"{n}_ss", f"{n}_dist_{a.ligand}", f"{n}_nearest_{a.ligand}_atom"]
        fh.write("\t".join(hdr) + "\n")
        for i, aa in enumerate(q):
            row = [i + 1, aa, f"{plddt[i]:.1f}", f"{rsa[i]:.2f}", f"{ident[i]:.2f}", f"{ent[i]:.2f}"]
            for n, (m, tres, tseq, dist, near, ss) in tcols.items():
                if i in m:
                    tr = tres[m[i]]
                    row += [f"{tseq[m[i]]}{tr.id[1]}", ss.get(tr.id[1], "-")]
                else:
                    row += ["-", "-"]
                row += [f"{dist[i]:.1f}", near[i]]
            fh.write("\t".join(map(str, row)) + "\n")
    Path(a.summary).write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
