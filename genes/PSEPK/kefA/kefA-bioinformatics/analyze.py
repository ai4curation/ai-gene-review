"""Homology and topology comparison of the dashboard kefA sequence (NZ_LGRH01000055.1_2).

1. Identity of the dashboard sequence to KT2440 PP_5067 (Q88CW3), E. coli MscK (P77338)
   and E. coli MscS (P0C0S1).
2. Map the query's DeepTMHMM segments onto the UniProt topology of E. coli MscK via the
   global alignment.
3. Report which query residues align to E. coli MscK G922 (UniProt mutagenesis
   feature) and W914 (periplasmic tryptophan gate ring, PMID:36371466) and to MscS L105/L109 (pore-lining gate residues).
"""
import argparse
import json

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def aligner(mode):
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = mode
    return a


def stats(aln):
    q, s = aln.target, aln.query
    ident = aligned = 0
    qmap = {}
    for (qs, qe), (ss, se) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(ss, se)):
            aligned += 1
            qmap[i + 1] = j + 1
            if q[i] == s[j]:
                ident += 1
    return ident, aligned, qmap


def topo_from_uniprot(js):
    tms = []
    sig = None
    for f in js["features"]:
        st, en = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if f["type"] == "Transmembrane":
            tms.append((st, en))
        if f["type"] == "Signal":
            sig = (st, en)
    return sig, tms


def overlap(a, b):
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True)
    p.add_argument("--references", required=True)
    p.add_argument("--topology", required=True, help="dashboard_call.json with topology_path")
    p.add_argument("--mscK-json", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()

    q = next(SeqIO.parse(a.query, "fasta"))
    refs = {r.id.split("|")[1]: r for r in SeqIO.parse(a.references, "fasta")}
    out = {"query_id": q.id, "query_len": len(q.seq), "pairs": {}}
    maps = {}
    for acc, r in refs.items():
        mode = "local" if acc == "P0C0S1" else "global"
        aln = aligner(mode).align(str(q.seq), str(r.seq))[0]
        ident, aligned, qmap = stats(aln)
        maps[acc] = qmap
        qcov = sorted(qmap)
        out["pairs"][acc] = {
            "description": r.description,
            "mode": mode,
            "subject_len": len(r.seq),
            "identical": ident,
            "aligned_pairs": aligned,
            "pct_identity_aligned": round(100 * ident / aligned, 1),
            "query_range": [qcov[0], qcov[-1]],
            "subject_range": [min(qmap.values()), max(qmap.values())],
        }

    # Topology: DeepTMHMM path letters (S signal, M membrane, I in, O out)
    dc = json.load(open(a.topology))
    path = dc["topology_path"]
    segs = []
    i = 0
    while i < len(path):
        j = i
        while j < len(path) and path[j] == path[i]:
            j += 1
        if path[i] in "MS":
            segs.append((path[i], i + 1, j))
        i = j
    sig, eco_tms = topo_from_uniprot(json.load(open(a.mscK_json)))
    m = maps["P77338"]
    seg_out = []
    for kind, st, en in segs:
        mapped = [m[k] for k in range(st, en + 1) if k in m]
        rng = (min(mapped), max(mapped)) if mapped else None
        hit = None
        if rng:
            if kind == "S" and sig and overlap(rng, sig):
                hit = f"MscK signal {sig[0]}-{sig[1]}"
            for n, t in enumerate(eco_tms, 1):
                if overlap(rng, t) > 0:
                    hit = f"MscK TM{n} {t[0]}-{t[1]}"
                    break
        seg_out.append({"type": "signal" if kind == "S" else "TM", "query": [st, en],
                        "maps_to_mscK": list(rng) if rng else None, "matches": hit})
    out["deeptmhmm_segments"] = seg_out
    out["n_query_tm"] = sum(1 for s in seg_out if s["type"] == "TM")
    out["n_query_tm_matching_mscK_tm"] = sum(
        1 for s in seg_out if s["type"] == "TM" and s["matches"])
    out["mscK_uniprot_tm_count"] = len(eco_tms)
    out["mscK_uniprot_signal"] = sig

    inv = {v: k for k, v in m.items()}
    rs = str(refs["P77338"].seq)
    out["mscK_positions"] = {}
    # G922: kefA2 mutagenesis site (UniProt); W914: periplasmic gate ring (PMID:36371466)
    for pos in (914, 922):
        g = inv.get(pos)
        out["mscK_positions"][f"{rs[pos-1]}{pos}"] = {
            "query_pos": g, "query_residue": str(q.seq)[g - 1] if g else None}
    inv_s = {v: k for k, v in maps["P0C0S1"].items()}
    ss = str(refs["P0C0S1"].seq)
    out["mscS_gate"] = {}
    for pos in (105, 109):
        g = inv_s.get(pos)
        out["mscS_gate"][f"{ss[pos-1]}{pos}"] = {
            "query_pos": g, "query_residue": str(q.seq)[g - 1] if g else None}
    json.dump(out, open(a.output, "w"), indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
