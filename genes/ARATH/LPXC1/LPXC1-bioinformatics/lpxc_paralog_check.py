"""Compare the five Arabidopsis LpxC paralogs (LPXC1-5) with each other and with
E. coli LpxC (P0A725), and check conservation of E. coli active-site residues.

Inputs: the cached UniProt flat files genes/ARATH/LPXC{1..5}/LPXC*-uniprot.txt
(canonical sequence and VAR_SEQ features) and the E. coli LpxC sequence fetched
from the UniProt REST API (cached to ecoli_P0A725.fasta).
Outputs: results.json and stdout table. Nothing is hardcoded except the list of
E. coli residue positions to inspect (taken from the literature, see README).
"""
import itertools, json, re, sys
from pathlib import Path
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
ARATH = HERE.parent.parent
GENES = ["LPXC1", "LPXC2", "LPXC3", "LPXC4", "LPXC5"]
# E. coli LpxC (P0A725, Met1 numbering) residues of interest:
# Zn(2+) ligands H79, H238, D242 and proton donor H265 (UniProt P0A725 BINDING/ACT_SITE);
# H238, D246, H265 named as critical for activity by Li et al. 2011 (PMID:21709257).
ECOLI_SITES = {79: "H", 238: "H", 242: "D", 246: "D", 265: "H"}


def parse_uniprot(path):
    txt = path.read_text()
    seq = "".join(re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M).group(1).split())
    acc = re.search(r"^AC   (\S+);", txt, re.M).group(1)
    varseqs = []
    for m in re.finditer(r"^FT   VAR_SEQ\s+(\d+)(?:\.\.(\d+))?\n((?:FT {19}.*\n)+)", txt, re.M):
        start, end = int(m.group(1)), int(m.group(2) or m.group(1))
        block = " ".join(l[21:].strip() for l in m.group(3).splitlines())
        note = re.search(r'/note="(.*?)"', block).group(1)
        vid = re.search(r'/id="(.*?)"', block)
        varseqs.append({"start": start, "end": end, "note": note, "id": vid.group(1) if vid else None})
    return acc, seq, varseqs


def apply_varseqs(seq, varseqs):
    """Apply VAR_SEQ edits (from C- to N-terminus) and return the isoform sequence."""
    s = seq
    for v in sorted(varseqs, key=lambda x: -x["start"]):
        if v["note"].startswith("Missing"):
            repl = ""
        else:
            repl = v["note"].split("->")[1].split("(")[0].strip().replace(" ", "")
        s = s[: v["start"] - 1] + repl + s[v["end"]:]
    return s


def ecoli_seq():
    cache = HERE / "ecoli_P0A725.fasta"
    if not cache.exists():
        r = requests.get("https://rest.uniprot.org/uniprotkb/P0A725.fasta", timeout=60)
        r.raise_for_status()
        cache.write_text(r.text)
    return "".join(cache.read_text().splitlines()[1:])


def aligner(mode):
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -10, -0.5
    a.mode = mode
    return a


def identity(aln):
    a, b = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    ident = sum(x == y for x, y in pairs)
    return ident, len(pairs)


def map_positions(aln, query_positions):
    """Map 1-based positions in aln target (seq 0) to residues of seq 1."""
    out = {}
    coords = aln.aligned
    for p in query_positions:
        out[p] = None
        for (ts, te), (qs, qe) in zip(*coords):
            if ts <= p - 1 < te:
                qi = qs + (p - 1 - ts)
                out[p] = (qi + 1, aln.sequences[1][qi])
    return out


def main():
    recs = {}
    for g in GENES:
        acc, seq, vs = parse_uniprot(ARATH / g / f"{g}-uniprot.txt")
        recs[g] = {"acc": acc, "seq": seq, "varseqs": vs}
    eco = ecoli_seq()
    res = {"lengths": {g: len(r["seq"]) for g, r in recs.items()}, "pairwise": {}, "vs_ecoli": {}}
    ga = aligner("global")
    for g1, g2 in itertools.combinations(GENES, 2):
        s1, s2 = recs[g1]["seq"], recs[g2]["seq"]
        aln = ga.align(s1, s2)[0]
        i, n = identity(aln)
        res["pairwise"][f"{g1}-{g2}"] = {"identical_sequence": s1 == s2, "identity_pct": round(100 * i / n, 1)}
    la = aligner("local")
    seqs = {f"{g} ({recs[g]['acc']}) canonical": recs[g]["seq"] for g in GENES}
    for g in GENES:
        # isoforms described by VAR_SEQ features: group by note "(in isoform N)"
        isoforms = {}
        for v in recs[g]["varseqs"]:
            m = re.search(r"in isoform (\w+)", v["note"])
            if m:
                isoforms.setdefault(m.group(1), []).append(v)
        for iso, vs in isoforms.items():
            seqs[f"{g} ({recs[g]['acc']}) isoform {iso}"] = apply_varseqs(recs[g]["seq"], vs)
    for name, s in seqs.items():
        aln = la.align(eco, s)[0]
        i, n = identity(aln)
        mapped = map_positions(aln, ECOLI_SITES)
        sites = {}
        for p, aa in ECOLI_SITES.items():
            m = mapped[p]
            sites[f"{aa}{p}"] = None if m is None else f"{m[1]}{m[0]}"
        conserved = sum(1 for p, aa in ECOLI_SITES.items() if mapped[p] and mapped[p][1] == aa)
        res["vs_ecoli"][name] = {"length": len(s), "identity_pct": round(100 * i / n, 1),
                                 "aligned_cols": n, "sites": sites,
                                 "sites_conserved": f"{conserved}/{len(ECOLI_SITES)}"}
    (HERE / "results.json").write_text(json.dumps(res, indent=2))
    print("Lengths:", res["lengths"])
    print("Pairwise (canonical):")
    for k, v in res["pairwise"].items():
        print(f"  {k}: identical={v['identical_sequence']} identity={v['identity_pct']}%")
    print("Versus E. coli LpxC P0A725 (local alignment):")
    for k, v in res["vs_ecoli"].items():
        print(f"  {k}: len={v['length']} id={v['identity_pct']}% over {v['aligned_cols']} cols; "
              f"sites {v['sites_conserved']}: {v['sites']}")


if __name__ == "__main__":
    sys.exit(main())
