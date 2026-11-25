"""Domain / CAZy family placement of DVU_1219 (Q72CR4) and test of the GH13 catalytic triad.

1. hmmscan (pyhmmer) of the query against the full dbCAN HMM library (CAZy families, dbCAN v5.2.9)
   and the full Pfam-A library, reporting every domain with independent E-value <= 10 (no gathering
   threshold), so that weak, sub-threshold GH13 or other CAZy signals are visible.
2. GH13 catalytic residues. The Pfam Alpha-amylase (PF00128) and dbCAN GH13 profiles are aligned to
   characterized GH13 references whose catalytic residues are annotated in UniProt (ACT_SITE/SITE
   features are fetched live), to find the HMM match states of the nucleophile Asp, acid/base Glu and
   transition-state Asp. The query is then forced onto the same profiles (E <= 1000) and the residue it
   places at each of those states is reported (HMMER acceleration filters off, so a forced alignment
   is always produced; its E-value says whether it is meaningful). The dbCAN GH13_33 subfamily profile,
   the query's best CAZy hit, is used the same way.

Usage: python3 -I domains.py --query FASTA --dbcan dbCAN.hmm --pfam Pfam-A.hmm --output results.json
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path

import pyhmmer

REFS = {  # characterized GH13 enzymes; catalytic residues are taken from their UniProt ACT_SITE/SITE features
    "P15067": "E. coli GlgX",
    "P0C1B3": "A. oryzae TAKA-amylase A",
    "P04746": "human pancreatic alpha-amylase",
    "Q9ZEU2": "N. polysaccharea amylosucrase",
}


def read_fasta(text: str) -> list[tuple[str, str]]:
    recs, name, buf = [], None, []
    for line in text.splitlines():
        if line.startswith(">"):
            if name:
                recs.append((name, "".join(buf)))
            name, buf = line[1:].split()[0], []
        elif line.strip():
            buf.append(line.strip())
    if name:
        recs.append((name, "".join(buf)))
    return recs


def uniprot(acc: str) -> tuple[str, str, list[dict]]:
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).read().decode()
    de = re.search(r"^DE   RecName: Full=([^;{]+)", txt, re.M)
    seq = re.sub(r"[^A-Z]", "", txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0])
    feats = []
    for m in re.finditer(r"^FT   (ACT_SITE|SITE)\s+(\d+)\n((?:FT {19}.*\n)*)", txt, re.M):
        note = re.search(r'/note="([^"]+)"', m.group(3))
        feats.append({"type": m.group(1), "pos": int(m.group(2)), "note": note.group(1) if note else ""})
    return (de.group(1).strip() if de else ""), seq, feats


def state_map(dom) -> dict[int, int]:
    """sequence position (1-based) -> HMM match state for one domain alignment."""
    ali = dom.alignment
    qpos, hpos, m = ali.target_from, ali.hmm_from, {}
    for hc, tc in zip(ali.hmm_sequence, ali.target_sequence):
        if hc != "." and tc != "-":
            m[qpos] = hpos
        if hc != ".":
            hpos += 1
        if tc != "-":
            qpos += 1
    return m


def scan(hmm_path: Path, seq, E: float = 10.0) -> list[dict]:
    out = []
    with pyhmmer.plan7.HMMFile(hmm_path) as fh:
        for hits in pyhmmer.hmmscan([seq], fh, E=E, domE=E, cpus=4):
            for hit in hits:
                for d in hit.domains:
                    if d.i_evalue > E:
                        continue
                    nm = hit.name.decode() if isinstance(hit.name, bytes) else hit.name
                    acc = hit.accession.decode() if isinstance(hit.accession, bytes) else (hit.accession or "")
                    out.append({"model": nm, "accession": acc, "seq_from": d.env_from, "seq_to": d.env_to,
                                "hmm_from": d.alignment.hmm_from, "hmm_to": d.alignment.hmm_to,
                                "hmm_len": hit.length if hasattr(hit, "length") else None,
                                "score": round(d.score, 1), "i_evalue": float(f"{d.i_evalue:.3g}"),
                                "full_seq_evalue": float(f"{hit.evalue:.3g}")})
    return sorted(out, key=lambda r: r["i_evalue"])


def get_hmm(path: Path, pattern: str):
    with pyhmmer.plan7.HMMFile(path) as fh:
        for h in fh:
            nm = h.name.decode() if isinstance(h.name, bytes) else h.name
            acc = (h.accession.decode() if isinstance(h.accession, bytes) else h.accession) or ""
            if re.fullmatch(pattern, nm) or re.fullmatch(pattern, acc.split(".")[0]):
                return h
    raise SystemExit(f"HMM {pattern} not found in {path}")


def best_dom(hmm, seq, E=1000.0):
    hits = next(iter(pyhmmer.hmmsearch([hmm], [seq], E=E, domE=E, incE=E, incdomE=E, F1=1.0, F2=1.0, F3=1.0, bias_filter=False)))
    doms = [d for h in hits for d in h.domains]
    return max(doms, key=lambda d: d.score) if doms else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", type=Path, required=True)
    ap.add_argument("--dbcan", type=Path, required=True)
    ap.add_argument("--pfam", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--positions", type=int, nargs="*", default=[],
                    help="query positions to report GH13_33 match state, consensus and top emissions for")
    a = ap.parse_args()
    alpha = pyhmmer.easel.Alphabet.amino()
    qname, qseq = read_fasta(a.query.read_text())[0]
    q = pyhmmer.easel.TextSequence(name=qname.encode(), sequence=qseq).digitize(alpha)
    res = {"query": qname, "length": len(qseq)}
    res["dbcan_hits_E10"] = scan(a.dbcan, q)
    res["pfam_hits_E10"] = scan(a.pfam, q)
    print("dbCAN hits (i-E <= 10):")
    for r in res["dbcan_hits_E10"][:20]:
        print("  ", r)
    print("Pfam hits (i-E <= 10):")
    for r in res["pfam_hits_E10"][:20]:
        print("  ", r)

    refs = {}
    for acc, label in REFS.items():
        try:
            name, s, feats = uniprot(acc)
        except Exception as e:  # noqa: BLE001
            print("skip", acc, e)
            continue
        if feats:
            refs[acc] = {"label": label, "uniprot_name": name, "seq": s, "features": feats}
    tri = {}
    for prof_name, path, pat in (("Pfam PF00128 Alpha-amylase", a.pfam, r"PF00128"), ("dbCAN GH13", a.dbcan, r"GH13(\.hmm)?"),
                                 ("dbCAN GH13_33", a.dbcan, r"GH13_33(\.hmm)?")):
        hmm = get_hmm(path, pat)
        qd = best_dom(hmm, q)
        entry = {"profile_length": hmm.M}
        if qd is None:
            entry["query"] = None
        else:
            qmap = state_map(qd)
            entry["query"] = {"seq_from": qd.alignment.target_from, "seq_to": qd.alignment.target_to,
                              "hmm_from": qd.alignment.hmm_from, "hmm_to": qd.alignment.hmm_to,
                              "score": round(qd.score, 1), "i_evalue": float(f"{qd.i_evalue:.3g}")}
            inv = {v: k for k, v in qmap.items()}
        refrows = []
        for acc, r in refs.items():
            rs = pyhmmer.easel.TextSequence(name=acc.encode(), sequence=r["seq"]).digitize(alpha)
            rd = best_dom(hmm, rs)
            if rd is None:
                continue
            rmap = state_map(rd)
            for f in r["features"]:
                st = rmap.get(f["pos"])
                row = {"ref": acc, "ref_name": r["uniprot_name"], "feature": f["type"], "note": f["note"],
                       "ref_pos": f["pos"], "ref_res": r["seq"][f["pos"] - 1], "hmm_state": st,
                       "ref_i_evalue": float(f"{rd.i_evalue:.3g}")}
                if qd is not None and st is not None and st in inv:
                    row["query_pos"] = inv[st]
                    row["query_res"] = qseq[inv[st] - 1]
                    row["query_window"] = qseq[max(0, inv[st] - 6): inv[st] + 5]
                else:
                    row["query_pos"] = None
                    row["query_res"] = None
                refrows.append(row)
        entry["catalytic_state_mapping"] = refrows
        tri[prof_name] = entry
        print(f"\n{prof_name} (M={hmm.M}); query best domain: {entry['query']}")
        for r in refrows:
            print(f"   {r['ref']} {r['note']:<30} {r['ref_res']}{r['ref_pos']} state {r['hmm_state']} -> query "
                  f"{r['query_res']}{r['query_pos']} {r.get('query_window', '')}")
    res["gh13_catalytic_mapping"] = tri
    # GH13_33 profile at chosen query positions (e.g. those structurally equivalent to GH13 catalytic residues)
    h33 = get_hmm(a.dbcan, r"GH13_33(\.hmm)?")
    d33 = best_dom(h33, q)
    m33 = state_map(d33)
    cons = h33.consensus
    syms = alpha.symbols
    pos_rows = []
    for p in a.positions:
        st = m33.get(p)
        row = {"query_pos": p, "query_res": qseq[p - 1], "gh13_33_state": st}
        if st is not None:
            em = list(h33.match_emissions[st])[:20]
            top = sorted(zip(syms[:20], em), key=lambda x: -x[1])[:3]
            row["consensus"] = cons[st - 1]
            row["top_emissions"] = [(aa, round(pr, 3)) for aa, pr in top]
            row["p_query_res"] = round(em[syms.index(qseq[p - 1])], 3)
            row["p_D"], row["p_E"] = round(em[syms.index("D")], 3), round(em[syms.index("E")], 3)
        pos_rows.append(row)
        print("GH13_33 at query", row)
    res["gh13_33_positions"] = pos_rows
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
