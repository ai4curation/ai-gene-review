"""Check conservation of E. coli DdlB (P07862) catalytic / Mg-binding residues
in each of the two Ddl modules of Arabidopsis At3g08840 (A0A1I9LPE3).

Residue positions are taken at run time from the UniProt feature table of
P07862 (ACT_SITE and single-residue BINDING features); nothing is hardcoded
except the accessions and the module split point search.

Usage: uv run python catalytic_residues.py > results.txt
"""
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF = "P07862"   # E. coli DdlB
REF2 = "P0A6J8"  # E. coli DdlA
TARGETS = ["A0A1I9LPE3", "Q3LHI3"]  # Arabidopsis At3g08840; moss Pp-DDL (genetically shown to act as Ddl, PMID:27325639)


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url) as fh:
        import json
        return json.load(fh)


def residues_of_interest(entry):
    out = []
    for f in entry.get("features", []):
        if f["type"] not in ("Active site", "Binding site"):
            continue
        s = f["location"]["start"]["value"]
        e = f["location"]["end"]["value"]
        if s != e:
            continue
        lig = f.get("ligand", {}).get("name", "")
        out.append((s, f["type"], lig))
    return sorted(set(out))


def align(ref_seq, tgt_seq):
    al = Align.PairwiseAligner()
    al.mode = "local"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    return al.align(ref_seq, tgt_seq)[0]


def map_positions(aln):
    """Return dict ref_pos(1-based) -> tgt_pos(1-based) for aligned residues."""
    m = {}
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            m[rs + i + 1] = ts + i + 1
    return m


def identity(aln):
    ident = n = 0
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            n += 1
            ident += aln.target[rs + i] == aln.query[ts + i]
    return ident, n


def prosite_regex(acc):
    """Fetch a PROSITE pattern and convert it to a Python regex."""
    import re
    url = f"https://prosite.expasy.org/{acc}.txt"
    with urllib.request.urlopen(url) as fh:
        txt = fh.read().decode()
    pa = "".join(l[5:].strip() for l in txt.splitlines() if l.startswith("PA   "))
    pa = pa.rstrip(".")
    rx = ""
    for el in pa.split("-"):
        rep = ""
        m = re.match(r"(.+?)\((\d+(?:,\d+)?)\)$", el)
        if m:
            el, rep = m.group(1), "{" + m.group(2) + "}"
        if el == "x":
            el = "."
        elif el.startswith("{"):
            el = "[^" + el[1:-1] + "]"
        rx += el + rep
    return pa, rx


def main():
    for t in TARGETS:
        report(t)


def report(TARGET):
    import re
    tgt = fetch(TARGET)["sequence"]["value"]
    print(f"\n# ===== target {TARGET} length {len(tgt)}")
    for ps in ("PS00843", "PS00844"):
        pa, rx = prosite_regex(ps)
        hits = [(m.start() + 1, m.group()) for m in re.finditer(rx, tgt)]
        print(f"# PROSITE {ps} {pa}: {hits if hits else 'no match'}")
    for ref_acc in (REF, REF2):
        ref_entry = fetch(ref_acc)
        ref = ref_entry["sequence"]["value"]
        feats = residues_of_interest(ref_entry)
        print(f"\n## reference {ref_acc} length {len(ref)}; "
              f"{len(feats)} single-residue active/binding-site features")
        # module 1: best local alignment over whole target; module 2: best local
        # alignment to the region C-terminal of module 1's end.
        aln1 = align(ref, tgt)
        t_end1 = aln1.aligned[1][-1][1]
        t_start1 = aln1.aligned[1][0][0]
        rest_off = t_end1
        aln2 = align(ref, tgt[rest_off:])
        modules = [("module_1", aln1, 0), ("module_2", aln2, rest_off)]
        # if module 1 hit the C-terminal copy, search N-terminal of it instead
        if t_start1 > len(tgt) // 2:
            aln2 = align(ref, tgt[:t_start1])
            modules = [("module_N", aln2, 0), ("module_C", aln1, 0)]
        for name, aln, off in modules:
            m = map_positions(aln)
            ident, n = identity(aln)
            ts = aln.aligned[1][0][0] + off + 1
            te = aln.aligned[1][-1][1] + off
            print(f"### {name}: target {ts}-{te}, score {aln.score:.1f}, "
                  f"identity {ident}/{n} ({100*ident/max(n,1):.1f}%)")
            print("ref_pos\tref_aa\tfeature\tligand\ttarget_pos\ttarget_aa\tconserved\tref_window\ttarget_window")
            for pos, ftype, lig in feats:
                raa = ref[pos - 1]
                tp = m.get(pos)
                if tp is None:
                    print(f"{pos}\t{raa}\t{ftype}\t{lig}\tgap\t-\tno")
                    continue
                taa = tgt[tp - 1 + off]
                tw = tgt[max(0, tp + off - 4):tp + off + 3]
                rw = ref[max(0, pos - 4):pos + 3]
                print(f"{pos}\t{raa}\t{ftype}\t{lig}\t{tp+off}\t{taa}\t"
                      f"{'yes' if taa == raa else 'no'}\t{rw}\t{tw}")


if __name__ == "__main__":
    sys.exit(main())
