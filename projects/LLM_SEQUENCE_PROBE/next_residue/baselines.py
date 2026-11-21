"""No-model baselines for the next-residue probe on all 3,340 cuts. Usage: baselines.py CLONE

Checks whether trivial order heuristics already show a real-versus-shuffled gap (they do not).
"""
import collections, csv, random, sys, zlib
def shuffled(seq, acc):
    r = list(seq); random.Random(zlib.crc32(acc.encode())).shuffle(r); return "".join(r)
rows = list(csv.DictReader(open(f"{sys.argv[1]}/data/confirm_sequences.tsv"), delimiter="\t"))
top = lambda s: collections.Counter(s).most_common(1)[0][0]
H = {"repeat last residue": lambda p: p[-1], "most common in prefix": top, "most common in last 20": lambda p: top(p[-20:]),
     "bigram within prefix": lambda p: top([p[i + 1] for i in range(len(p) - 1) if p[i] == p[-1]] or p)}
for name, h in H.items():
    res = {}
    for cond in ("real", "shuffled", "reversed"):
        ok = n = 0
        for r in rows:
            s = {"real": r["sequence"], "shuffled": shuffled(r["sequence"], r["accession"]), "reversed": r["sequence"][::-1]}[cond]
            for c in map(int, r["cuts"].split(",")): ok += h(s[:c]) == s[c]; n += 1
        res[cond] = 100 * ok / n
    print(f"{name:24s} real {res['real']:.1f}  shuffled {res['shuffled']:.1f}  reversed {res['reversed']:.1f}  (n={n})")
