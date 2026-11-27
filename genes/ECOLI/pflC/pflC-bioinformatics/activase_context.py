"""Genome context and sequence comparison of E. coli K-12 GRE activase paralogs.

Fetches (live, nothing hardcoded):
  * the NCBI feature table of E. coli K-12 MG1655 (NC_000913.3),
  * UniProt sequences of the activases and glycyl radical enzymes (GREs),
  * NCBIfam/InterPro family descriptions for the activase families.

Reports, for each activase gene: its neighbours (strand, coordinates, intergenic
gap), whether it is co-directional and adjacent to a GRE gene, pairwise global
identities among activases and among GREs, and the NCBIfam family text.

Usage: uv run python activase_context.py > activase_context.out
"""
import re
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

FT_URL = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
          "?db=nuccore&id=NC_000913.3&rettype=ft&retmode=text")
ACTIVASES = {"pflA": "P0A9N4", "nrdG": "P0A9N8", "pflC": "P32675",
             "ybiY": "P75794", "yjjW": "P39409"}
GRES = {"pflB": "P09373", "tdcE": "P42632", "nrdD": "P28903",
        "pflD": "P32674", "ybiW": "P75793", "yjjI": "P37342"}
FAMILIES = ["TIGR02493", "TIGR02491", "TIGR02494", "TIGR04041", "NF007483"]
FLANK = 6


def parse_feature_table(text):
    genes = []
    cur = None
    for line in text.splitlines():
        m = re.match(r"^<?(\d+)\t>?(\d+)\t(\w+)$", line)
        if m:
            start, end, kind = int(m.group(1)), int(m.group(2)), m.group(3)
            if kind == "gene":
                cur = {"start": min(start, end), "end": max(start, end),
                       "strand": "+" if end >= start else "-",
                       "gene": None, "locus": None, "product": None}
                genes.append(cur)
            elif kind in ("CDS", "ncRNA", "tRNA", "rRNA") and cur is not None:
                cur["_in_product_feature"] = True
            else:
                cur = None if kind == "gene" else cur
            continue
        fields = line.strip().split("\t")
        if cur is None or len(fields) != 2:
            continue
        key, val = fields
        if key == "gene" and cur["gene"] is None:
            cur["gene"] = val
        elif key == "locus_tag" and cur["locus"] is None:
            cur["locus"] = val
        elif key == "product" and cur.get("_in_product_feature") and cur["product"] is None:
            cur["product"] = val
    genes.sort(key=lambda g: g["start"])
    return genes


def uniprot_seq(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a, b, aligner):
    aln = aligner.align(a, b)[0]
    ident = aligned_cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned_cols += 1
            ident += a[i] == b[j]
    return 100.0 * ident / min(len(a), len(b)), aligned_cols


def main():
    out = sys.stdout
    text = requests.get(FT_URL, timeout=120).text
    genes = parse_feature_table(text)
    by_name = {g["gene"]: i for i, g in enumerate(genes) if g["gene"]}
    gre_names = set(GRES)
    out.write(f"# Parsed {len(genes)} gene features from NC_000913.3\n\n")
    out.write("## Genome neighbourhoods of activase genes\n")
    for name in ACTIVASES:
        i = by_name.get(name)
        if i is None:
            out.write(f"\n{name}: NOT FOUND\n")
            continue
        g = genes[i]
        out.write(f"\n### {name} ({g['locus']}) {g['start']}-{g['end']} strand {g['strand']}\n")
        for j in range(max(0, i - FLANK), min(len(genes), i + FLANK + 1)):
            n = genes[j]
            mark = "*" if j == i else ("G" if n["gene"] in gre_names else " ")
            out.write(f"{mark} {n['gene'] or '-':8s} {n['locus'] or '-':7s} {n['start']:>8d}-{n['end']:<8d} "
                      f"{n['strand']} {n['product'] or ''}\n")
        for j in (i - 1, i + 1):
            if 0 <= j < len(genes) and genes[j]["gene"] in gre_names:
                n = genes[j]
                gap = (g["start"] - n["end"] - 1) if j < i else (n["start"] - g["end"] - 1)
                same = n["strand"] == g["strand"]
                out.write(f"  -> adjacent GRE gene {n['gene']}: intergenic gap {gap} bp, "
                          f"{'same strand' if same else 'opposite strand'}\n")

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    for title, group in (("activases", ACTIVASES), ("GREs", GRES)):
        seqs = {k: uniprot_seq(v) for k, v in group.items()}
        names = list(seqs)
        out.write(f"\n## Pairwise global identity among {title} (% of shorter sequence)\n")
        out.write("        " + "".join(f"{n:>8s}" for n in names) + "\n")
        for a in names:
            row = []
            for b in names:
                row.append("     -  " if a == b else f"{identity(seqs[a], seqs[b], aligner)[0]:8.1f}")
            out.write(f"{a:8s}" + "".join(row) + f"   (len {len(seqs[a])})\n")

    out.write("\n## Glycine-loop heptamer of each GRE (pattern RV.GY within the last 80 residues)\n")
    for name, acc in GRES.items():
        seq = uniprot_seq(acc)
        off = len(seq) - 80
        hits = [(m.start() + off + 1, seq[m.start() + off:m.start() + off + 7])
                for m in re.finditer(r"RV[A-Z]G[YF]", seq[off:])]
        out.write(f"{name:6s} {acc}  len {len(seq):4d}  " +
                  ("; ".join(f"{h} at {pos}-{pos + 6} (Gly {pos + 3})" for pos, h in hits) or "no match") + "\n")

    out.write("\n## NCBIfam family descriptions (InterPro API)\n")
    for fam in FAMILIES:
        r = requests.get(f"https://www.ebi.ac.uk/interpro/api/entry/ncbifam/{fam}", timeout=60)
        if r.status_code != 200:
            out.write(f"\n{fam}: HTTP {r.status_code}\n")
            continue
        md = r.json()["metadata"]
        desc = " ".join(re.sub(r"<[^>]+>", "", d["text"]) for d in (md.get("description") or []))
        out.write(f"\n{fam} | {md['name']['name']}\n{desc.strip() or '(no description)'}\n")


if __name__ == "__main__":
    main()
