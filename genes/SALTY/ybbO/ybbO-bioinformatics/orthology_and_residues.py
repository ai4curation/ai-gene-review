"""Orthology (1:1?) and residue-level analysis for Salmonella YbbO (STM0505, Q7CR11).

Questions addressed:
1. Is Q7CR11 the 1:1 orthologue of E. coli YbbO (P0AFP4)?  Reciprocal best hit
   between the full LT2 and K-12 reference proteomes, plus the nearest Salmonella
   paralogues, plus conservation of the gene neighbourhood (synteny).
2. Which residues are conserved?  SDR catalytic tetrad and cofactor motifs; the
   positions that differ between Salmonella and E. coli YbbO; whether those
   differences fall in an approximate active-site pocket (AlphaFold model); and
   per-position conservation across Enterobacterales YbbO orthologues compared
   with vertebrate SDR9C relatives (hydroxysteroid/retinol dehydrogenases).

All data are fetched from UniProt and AlphaFold DB at run time (proteomes are
cached under data/). Nothing is hard-coded except accessions and parameters.
Run:  uv run python orthology_and_residues.py
"""

import json
import time
import urllib.error
from io import StringIO
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices
from Bio.PDB import PDBParser

HERE = Path(__file__).parent
DATA = HERE / "data"
QUERY = "Q7CR11"  # Salmonella Typhimurium LT2 YbbO
ECOLI = "P0AFP4"  # E. coli K-12 YbbO
PROTEOMES = {"SALTY_LT2": "UP000001014", "ECOLI_K12": "UP000000625"}
# Vertebrate SDR9C relatives from the PTN000672121 IBA WITH/FROM list
SDR9C_RELATIVES = {
    "O14756": "HSD17B6 human",
    "O75452": "RDH16 human",
    "Q9BPW9": "DHRS9 human",
    "Q92781": "RDH5 human",
}
POCKET_RADIUS = 10.0  # angstrom, from centroid of catalytic Ser OG / Tyr OH


def fetch_text(url, tries=4):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url) as r:
                return r.read().decode()
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == tries - 1:
                raise
            time.sleep(2 ** (attempt + 1))


def clean(seq):
    """Map residues outside the BLOSUM62 alphabet (U, O, J) to X."""
    return "".join(c if c in "ARNDCQEGHILKMFPSTWYVBZX" else "X" for c in seq)


def fetch_seq(acc):
    fasta = fetch_text(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(l for l in fasta.splitlines() if not l.startswith(">"))


def proteome(name, upid):
    DATA.mkdir(exist_ok=True)
    path = DATA / f"{name}.fasta"
    if not path.exists():
        url = ("https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
               + urllib.parse.quote(f"proteome:{upid}"))
        path.write_text(fetch_text(url))
    return {r.id.split("|")[1]: (r.description, clean(str(r.seq)))
            for r in SeqIO.parse(path, "fasta")}


def aligner(mode):
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -11, -1
    a.mode = mode
    return a


LOCAL, GLOBAL = aligner("local"), aligner("global")


def identity(a, b):
    """Percent identity over aligned columns of the best local alignment, and coverage of a."""
    aln = LOCAL.align(a, b)[0]
    cols = [(x, y) for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-"]
    ident = sum(x == y for x, y in cols)
    return 100 * ident / max(len(cols), 1), 100 * len(cols) / len(a)


def rank(query_seq, prot, top=5):
    scores = [(LOCAL.score(query_seq, s), acc) for acc, (_, s) in prot.items()]
    scores.sort(reverse=True)
    out = []
    for sc, acc in scores[:top]:
        pid, cov = identity(query_seq, prot[acc][1])
        out.append((acc, sc, pid, cov, prot[acc][0].split(" OS=")[0].split(" ", 1)[1]))
    return out


def mapping(ref, other):
    """Map ref positions (1-based) to residues of other via global alignment."""
    aln = GLOBAL.align(ref, other)[0]
    m = {}
    for (rs, re), (os_, oe) in zip(*aln.aligned):
        for i in range(re - rs):
            m[rs + i + 1] = other[os_ + i]
    return m


def neighbours(locus_tags, taxid):
    q = "(" + " OR ".join(locus_tags) + f") AND organism_id:{taxid}"
    url = ("https://rest.uniprot.org/uniprotkb/search?format=tsv&fields=gene_oln,gene_primary&query="
           + urllib.parse.quote(q))
    rows = [l.split("\t") for l in fetch_text(url).splitlines()[1:]]
    tag2name = {}
    for oln, name in rows:
        for t in oln.split():
            tag2name[t] = name
    return [(t, tag2name.get(t, "?")) for t in locus_tags]


def main():
    q = fetch_seq(QUERY)
    eco = fetch_seq(ECOLI)
    sal_prot = proteome("SALTY_LT2", PROTEOMES["SALTY_LT2"])
    eco_prot = proteome("ECOLI_K12", PROTEOMES["ECOLI_K12"])

    print("## 1. Orthology\n")
    print(f"Proteome sizes: LT2 {len(sal_prot)}, K-12 {len(eco_prot)}\n")
    print(f"### Forward: {QUERY} vs E. coli K-12 proteome (top 5, local SW, BLOSUM62)")
    fwd = rank(q, eco_prot)
    for acc, sc, pid, cov, name in fwd:
        print(f"  {acc}\tscore {sc:.0f}\tid {pid:.1f}%\tcov {cov:.0f}%\t{name}")
    print(f"\n### Reverse: {ECOLI} vs Salmonella LT2 proteome (top 5)")
    rev = rank(eco, sal_prot)
    for acc, sc, pid, cov, name in rev:
        print(f"  {acc}\tscore {sc:.0f}\tid {pid:.1f}%\tcov {cov:.0f}%\t{name}")
    rbh = fwd[0][0] == ECOLI and rev[0][0] == QUERY
    print(f"\nReciprocal best hit {QUERY} <-> {ECOLI}: {rbh}")
    print(f"Score gap forward (best / 2nd): {fwd[0][1]:.0f} / {fwd[1][1]:.0f}; "
          f"reverse: {rev[0][1]:.0f} / {rev[1][1]:.0f}")
    print(f"\n### Nearest Salmonella paralogues of {QUERY} (top 5 excluding self)")
    para = [h for h in rank(q, sal_prot, top=6) if h[0] != QUERY][:5]
    for acc, sc, pid, cov, name in para:
        print(f"  {acc}\tscore {sc:.0f}\tid {pid:.1f}%\tcov {cov:.0f}%\t{name}")

    print("\n### Gene neighbourhood (UniProt ordered locus names)")
    for label, tags, tax in [("LT2", [f"STM{n:04d}" for n in range(503, 508)], 99287),
                             ("K-12", [f"b{n:04d}" for n in range(491, 496)], 83333)]:
        print(f"  {label}: " + "  ".join(f"{t}={n}" for t, n in neighbours(tags, tax)))

    print("\n## 2. Residues\n")
    # Classical SDR (Filling et al. 2002, 3alpha/20beta-HSD numbering): catalytic
    # tetrad N111-S138-Y151-K155, i.e. Ser 13 upstream of the YxxxK Tyr and the
    # alpha-E helix Asn ~27 upstream of the Ser; NNAG (N86) and TGxxxGxG are
    # structural / cofactor motifs.
    tyr = next(i + 1 for i in range(len(q) - 4) if q[i] == "Y" and q[i + 4] == "K" and i > 100)
    lys, ser = tyr + 4, tyr - 13
    asn = next(p for p in range(ser - 24, ser - 31, -1) if q[p - 1] == "N")
    nnag = q.find("NNAG") + 1
    tg = q.find("TG") + 1
    print(f"Cofactor motif at {tg}: {q[tg - 1:tg + 7]}; structural NNAG motif at {nnag}")
    print(f"Catalytic tetrad: N{asn}({q[asn - 1]}) S{ser}({q[ser - 1]}) "
          f"Y{tyr}({q[tyr - 1]}) K{lys}({q[lys - 1]})")
    tetrad = {asn, ser, tyr, lys}

    # AlphaFold model -> approximate pocket around catalytic Ser OG / Tyr OH
    meta = json.loads(fetch_text(f"https://alphafold.ebi.ac.uk/api/prediction/{QUERY}"))[0]
    pdb_path = DATA / f"AF-{QUERY}.pdb"
    if not pdb_path.exists():
        pdb_path.write_text(fetch_text(meta["pdbUrl"]))
    chain = next(PDBParser(QUIET=True).get_structure("af", pdb_path)[0].get_chains())
    centre = (chain[ser]["OG"].coord + chain[tyr]["OH"].coord) / 2
    pocket = set()
    for res in chain:
        side = [a for a in res if a.get_id() not in ("N", "C", "O")]
        if any(np.linalg.norm(a.coord - centre) <= POCKET_RADIUS for a in side):
            pocket.add(res.id[1])
    plddt = {res.id[1]: res["CA"].get_bfactor() for res in chain}
    print(f"\nAlphaFold model {meta['entryId']} (mean pLDDT {np.mean(list(plddt.values())):.1f}); "
          f"approximate pocket = residues with a side-chain atom within {POCKET_RADIUS} A "
          f"of the S{ser} OG / Y{tyr} OH midpoint: {len(pocket)} residues")
    print("  " + " ".join(f"{q[p - 1]}{p}" for p in sorted(pocket)))

    # Salmonella vs E. coli substitutions
    m_eco = mapping(q, eco)
    subs = [p for p in range(1, len(q) + 1) if m_eco.get(p) and m_eco[p] != q[p - 1]]
    print(f"\n### {QUERY} vs {ECOLI}: {len(subs)} substituted positions")
    print("  " + " ".join(f"{q[p - 1]}{p}{m_eco[p]}" for p in subs))
    in_pocket = [p for p in subs if p in pocket]
    print(f"  in approximate pocket: {len(in_pocket)} "
          + (" ".join(f"{q[p - 1]}{p}{m_eco[p]}" for p in in_pocket) or "(none)"))
    print(f"  tetrad residues substituted: {sorted(set(subs) & tetrad) or 'none'}")

    # Conservation across Enterobacterales YbbO orthologues vs SDR9C relatives
    url = ("https://rest.uniprot.org/uniprotkb/search?format=fasta&size=200&query="
           + urllib.parse.quote("gene_exact:ybbO AND taxonomy_id:91347 AND keyword:KW-1185"))
    orth = {r.id.split("|")[1]: clean(str(r.seq)) for r in SeqIO.parse(StringIO(fetch_text(url)), "fasta")}
    orth.pop(QUERY, None)
    maps = [mapping(q, s) for s in orth.values()]
    cons = {p: sum(m.get(p) == q[p - 1] for m in maps) / len(maps) for p in range(1, len(q) + 1)}
    rel_maps = {acc: mapping(q, fetch_seq(acc)) for acc in SDR9C_RELATIVES}
    print(f"\n### Conservation across {len(orth)} Enterobacterales YbbO orthologues "
          "(UniProt gene_exact:ybbO, reference proteomes)")
    pids = [identity(q, s)[0] for s in orth.values()]
    print(f"  identity to {QUERY}: min {min(pids):.1f}%, median {np.median(pids):.1f}%, max {max(pids):.1f}%")
    print(f"  tetrad conservation: " + ", ".join(f"{q[p - 1]}{p} {100 * cons[p]:.0f}%" for p in sorted(tetrad)))
    inv_pocket = [p for p in sorted(pocket) if cons[p] == 1.0]
    print(f"  pocket residues invariant in all orthologues: {len(inv_pocket)}/{len(pocket)}")
    print("\n  Pocket residues: query, % identical in YbbO orthologues, residue in SDR9C relatives "
          + "(" + ", ".join(SDR9C_RELATIVES.values()) + "); * = invariant in YbbO and differs from all relatives")
    spec = []
    for p in sorted(pocket):
        rel = [rel_maps[a].get(p, "-") for a in SDR9C_RELATIVES]
        flag = cons[p] == 1.0 and all(r != q[p - 1] for r in rel)
        if flag:
            spec.append(p)
        print(f"  {q[p - 1]}{p}\t{100 * cons[p]:.0f}%\t{' '.join(rel)}\t{'*' if flag else ''}\tpLDDT {plddt[p]:.0f}")
    # Rank Salmonella -> E. coli substitutions by likely functional impact
    blosum = substitution_matrices.load("BLOSUM62")
    dist = {}
    for res in chain:
        side = [a for a in res if a.get_id() not in ("N", "C", "O")]
        dist[res.id[1]] = min(float(np.linalg.norm(a.coord - centre)) for a in side)
    print(f"\n### Substitutions {QUERY} -> {ECOLI}, sorted by distance to the catalytic centre")
    print("  sub\tdist_A\tpLDDT\tBLOSUM62\t%orth_query_res\t#orth_with_ecoli_res\tother residues at position")
    for p in sorted(subs, key=lambda x: dist[x]):
        e = m_eco[p]
        n_e = sum(m.get(p) == e for m in maps)
        others = sorted({m.get(p) for m in maps if m.get(p)} - {q[p - 1], e})
        print(f"  {q[p - 1]}{p}{e}\t{dist[p]:.1f}\t{plddt[p]:.0f}\t{blosum[q[p - 1]][e]:.0f}\t"
              f"{100 * cons[p]:.0f}%\t{n_e}/{len(maps)}\t{''.join(others) or '-'}")
    print(f"\nCandidate YbbO-specific pocket residues (invariant in YbbO orthologues, differ from all "
          f"four vertebrate SDR9C relatives): {' '.join(f'{q[p - 1]}{p}' for p in spec) or 'none'}")


if __name__ == "__main__":
    main()
