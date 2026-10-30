# yxcA (Q9CDI2) bioinformatics: relationship to characterized plasmalogen synthases

Script: `analyze_plsA.py` (`uv run python analyze_plsA.py`). It fetches the
sequences live (UniProt, UniParc, NCBI protein), writes them to
`sequences.fasta`, and writes every number below to `results.json`. Nothing
here is hard-coded.

## Questions

1. How close is Q9CDI2 to the PlsA proteins whose plasmalogen-forming activity
   was shown experimentally?
2. Does Q9CDI2 carry the full PlsAR domain set (Act1, Act2, Red1, Red2), or
   only the activator half implied by its name ("2-hydroxyglutaryl-CoA
   dehydratase"; KBase/eggNOG "hgdC")?

## Methods

- Global (Needleman-Wunsch) alignment, BLOSUM62, gap open -11 / extend -1
  (Biopython `PairwiseAligner`), against single-chain homologs; local
  (Smith-Waterman) alignment against the two separate *C. perfringens*
  proteins. Identity = identical columns / all alignment columns, gaps
  included.
- Pfam HMMs PF01869 (BcrAD_BadFG), PF09989 (DUF2229) and PF06050 (HGD-D),
  downloaded from the InterPro API and searched with pyhmmer (E <= 10, so
  that weak hits are reported) against the full chain, against residues
  901-1436 alone, and against controls.

## Results

### Sequence identity of Q9CDI2

| Comparator | What it is | Identity | Q9CDI2 span |
|---|---|---|---|
| UPI00072AC48C (1441 aa) | KBase NZ_VXKC01000008.1_19 / WP_081041604 | 98.3% | 1-1436 |
| ABJ73971.1 (1436 aa) | *L. cremoris* ATCC BAA-493 LACR_2543, the PlsA expressed in PMID:41427725 | 96.6% | 1-1436 |
| A2RP33 (1436 aa) | *L. cremoris* MG1363 llmg_2516 | 96.7% | 1-1436 |
| AAO81118.1 (1415 aa) | *E. faecalis* EF1327 PlsA (PMID:33350306) | 67.3% | 1-1436 |
| BAB80901.1 (1004 aa) | *C. perfringens* CPE1195 PlsA (Act1-Act2-Red1) | 51.1% | 1-989 |
| BAB80900.1 (420 aa) | *C. perfringens* CPE1194 PlsR (Red2) | 41.3% | 1011-1411 |

PMID:41427725 names the BAA-493 gene "plsABAA493 (4,311 bp)" and lists its
locus tag as LACR_2543. 4,311 bp is 1,436 codons plus a stop codon, which
matches ABJ73971.1.

### Domain coverage

- Pfam on the full chain: BcrAD_BadFG at 7-257 (i-E 1.3e-24) and 322-576
  (i-E 1.5e-40), so Act1 and Act2 are present. DUF2229 is present at 676-897
  (i-E 4e-80; Red1).
- C-terminal region: PF06050 (HGD-D) gives no hit on Q9CDI2, either on the
  full chain or on residues 901-1436 alone. A weak partial DUF2229 match
  (HMM 17-63, i-E ~1e-6) lies at 1023-1089. *C. perfringens* PlsR, the
  experimentally required Red2 subunit, behaves the same way: it also gives
  only weak, partial DUF2229 matches (i-E 1.2e-7 for HMM 14-66). In EF1327,
  HGD-D gives only fragmentary hits (best i-E 2.6e-4).
- The local alignment of Q9CDI2 residues 1011-1411 to PlsR (41.3% identity
  over 402 columns) is the direct evidence that the C-terminal ~430 residues
  are the Red2 domain, fused in one chain as in EF1327. The Pfam HGD-D model
  is too divergent to detect this domain.

### Act-domain cysteines

Of the nine cysteines in Q9CDI2 residues 1-620, eight align to cysteine in
both EF1327 and *C. perfringens* PlsA (C126, C165, C445, C449, C484, C606,
C609, C613). C572 is Ala in EF1327. PMID:33350306 reports that Act1 and Act2
share conserved cysteines for iron-sulfur cluster ligation with HAD and BCR
activators. This analysis shows only that the cysteines are conserved among
PlsA proteins. It does not map them onto HgdC cluster ligands.

## Conclusions

- Q9CDI2 is a full-length, single-chain plasmalogen synthase (PlsA/PlsAR
  architecture Act1-Act2-Red1-Red2). It is essentially the same protein
  (96.6% identity) as the *L. cremoris* PlsA shown to confer plasmalogen
  synthesis on *E. coli*.
- The ProtNLM name "2-hydroxyglutaryl-CoA dehydratase" and the eggNOG name
  "hgdC" describe only one family relationship. Neither describes this
  protein's function.
- Limits: identity is not proof of identical activity. No *L. lactis* subsp.
  *lactis* knockout or in vitro enzyme assay exists. Cysteine conservation is
  not cluster-ligand assignment.
