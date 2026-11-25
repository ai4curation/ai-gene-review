# Paralog comparison: VC_2283 (AatX, Q9KPS9) vs VC_1669 (Q9KRH3)

Run: `analyze.py` via `just all` (Biopython global alignment, BLOSUM62, gap open -10 /
extend -0.5). Recorded as BERIL run `20261030T213758Z-vc2283-vc1669-nss-paralog-comparison`.
All numbers below are from `results.json`. This analysis is shared by
`genes/VIBCH/VC_2283/` (VC_2283) and `genes/VIBCH/VC_1669/`.

## Question

The dashboard called both *V. cholerae* NSS (PF00209) paralogs tryptophan transporters.
Only VC2283 is named in the literature (aatX, PMID:36130487). Which paralog does the
tryptophan evidence belong to?

## 1. Pairwise identity (identity over aligned pairs)

| pair | identity | aligned pairs |
|---|---|---|
| VC_2283 (Q9KPS9) vs VC_1669 (Q9KRH3) | 55.5% | 445 |
| dashboard NZ_NMTP01000136.1_1 vs Q9KPS9 | 100.0% | 451 |
| dashboard NZ_JADNQR010000211.1_1 vs Q9KRH3 | 98.2% | 447 |
| dashboard NZ_JADNQR010000211.1_1 vs Q9KPS9 (AatX) | 54.8% | 445 |
| Q9KPS9 vs MhsT (Q9KDT3, B. halodurans) | 41.1% | 428 |
| Q9KRH3 vs MhsT | 40.6% | 429 |
| Q9KPS9 vs TnaT (Q67SB6, S. thermophilum) | 34.7% | 421 |
| Q9KRH3 vs TnaT | 32.1% | 405 |
| Q9KPS9 vs LeuT (O67854, A. aeolicus) | 35.1% | 413 |
| Q9KRH3 vs LeuT | 33.7% | 424 |
| Q9KPS9 vs SO_4339 (Q8E9E5, S. oneidensis) | 45.2% | 449 |
| Q9KRH3 vs SO_4339 | 48.1% | 439 |
| Q9KPS9 vs YocR (O34383, B. subtilis) | 41.2% | 422 |
| Q9KRH3 vs YocR | 40.8% | 419 |

The two paralogs are 55.5% identical to each other and equally distant (32-48%) from
every characterized bacterial NSS. Identity therefore does not place either one closer to
the Trp-specific TnaT or the Trp-binding MhsT than the other.

## 2. TrpR operator scan

Best match (both strands) to the *E. coli* trpEDCBA operator 20-mer `CGAACTAGTTAACTAGTACG`
within 300 bp upstream of each CDS start, over all 3,585 CDS on both chromosomes.

| gene | best site | mismatches | fraction of all CDS with <= this many mismatches |
|---|---|---|---|
| trp leader / trpE (VC1176/VC1174), positive control | `CGCACTAGTTAACTAGTACG` | 1 | 0.0008 |
| **VC2283 (aatX)** | `TGTACTAGTTAACTAGTGTG` | 3 | 0.0011 |
| trpR (VC0701) | `TGTATCACTTAACGAGTACA` | 7 | 0.0625 |
| **VC1669** | `TGAACTGATTTACTTGCCAT` | 9 | 0.7782 |

Genome-wide, only four CDS have a site with three or fewer mismatches: trpE, the trp
leader peptide and the divergent rnm gene (all sharing the trp operon promoter region),
and VC2283. VC2283 is the only gene outside the trp operon with a near-consensus TrpR
operator. VC1669 has no TrpR-like site (9 mismatches, the genome median).

## 3. Genomic neighbourhood (chromosome I)

- VC2283 (minus strand): VC2282 succinylglutamate desuccinylase/aspartoacylase (+),
  VC2285 diguanylate cyclase (-). No tryptophan-metabolism genes.
- VC1669 (minus strand): VC1668 TIGR01621 pseudouridine synthase (-), VC1670 cls
  cardiolipin synthase (+). No amino-acid-metabolism genes.

## Conclusion

The tryptophan evidence belongs to VC2283. It carries a near-consensus TrpR operator,
which fits the RegPrecise TrpR-regulon prediction and the TrpR repression measured in
PMID:36130487. VC1669 has no TrpR site, no tryptophan-related neighbours and no
experimental data beyond being a CarR ChIP-seq target (PMID:35676416). Its substrate is
unknown. Calling VC1669 a tryptophan transporter transfers the AatX annotation to a
55%-identical paralog in the same genome. Two paralogs in one genome usually differ in
substrate or regulation, and here they demonstrably differ in regulation.

Caveats:
- The operator scan uses the *E. coli* operator, not a *Vibrio*-trained TrpR matrix.
- Neither protein has been assayed for transport. AatX's tryptophan role rests on
  regulation plus a double-mutant consumption phenotype.

## Genome files (not committed)

The TrpR-operator scan reads the N16961 chromosome sequences and feature tables from `data/`. They are too large to commit. To fetch them:

```bash
for c in NC_002505.1 NC_002506.1; do
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$c&rettype=fasta" > data/$c.fasta
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$c&rettype=ft" > data/$c.ft
done
```
