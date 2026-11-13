---
title: "MCR alpha-subunit active sites across clades: results"
autolink_gene_symbols: false
---

# MCR alpha-subunit active sites across clades: results

Script: `compare_active_sites.py` (this folder). Output: `RESULTS.tsv`.
Run from the repository root with the project environment:
`python projects/ARCHAEA/mcrA-across-clades/compare_active_sites.py`.

## Method

The reference is the *Methanothermobacter marburgensis* MCR I alpha subunit
(P11558, MCRA_METTM). Its 12 positions carrying a UniProt BINDING or MOD_RES
feature were read from the cached UniProt flat file
(`genes/METTM/mcrA/mcrA-uniprot.txt`). One further position, Gln332, has no
UniProt feature but is singled out by the ANME-2d MCR structures
(PMID:40913044); it is listed as an input in the script (`EXTRA_POSITIONS`). Each other sequence, read from its own
cached UniProt file, was aligned globally to P11558 (Biopython
PairwiseAligner, BLOSUM62, gap open -10, gap extend -0.5). The script reports
the residue aligned to each reference position and the target's own UniProt
feature there, if it has one. A pairwise alignment to one reference is
adequate for this conserved core. It is not a phylogeny.

## Summary of the run (2026-11-13, 13 positions)

| Accession | Clade | Identity to P11558 | Reference positions not conserved |
|---|---|---|---|
| P11558 | Methanobacteriales | 100.0% | none |
| O27232 | Methanobacteriales | 99.3% | none |
| Q58256 | Methanococcales | 71.9% | none |
| Q49605 | Methanopyrales | 72.9% | none |
| P07962 | Methanosarcinales | 66.5% | Y444->F464 |
| Q8THH1 | Methanosarcinales | 66.6% | Y444->F464 |
| A0A284VQI9 | ANME-2d (Ca. Methanoperedentaceae) | 60.3% | Q332->M347 |
| A0A7R9R780 | GoM-Arc1 (Ca. Methanoperedentaceae) | 47.6% | Q147->M181, R225->A259, Q332->N375, C452->Q497 |

Reference positions examined: Q147 (coenzyme F430 nickel axial ligand),
R225, K256, H257, R270 (coenzyme B), R271 (5-methylarginine), Q332 (next to
the coenzyme M tyrosine; literature position), Y333, Y444 (coenzyme M), Q400
(2-methylglutamine), G445 (thioglycine), D450 (didehydroaspartate), C452
(S-methylcysteine). H257 is both a coenzyme B contact and a methylhistidine.

## Findings

1. All six methanogen McrA sequences, from four orders, keep the
   F430 axial glutamine, the coenzyme B and coenzyme M contacts, and the
   residues that carry the core modifications. The one substitution is
   Tyr444 to Phe in both *Methanosarcina* sequences (P07962 F464, Q8THH1
   F464). UniProt still annotates that position as a coenzyme M contact in
   P07962.
2. The ANME-2d McrA (A0A284VQI9, *Ca.* Methanoperedens) keeps the F430
   axial glutamine, all coenzyme B and coenzyme M contacts and the residue
   at every modification site, consistent with a methane-activating enzyme
   that uses the same chemistry as methanogenic MCR. A conserved residue does
   not mean a conserved modification: the ANME-2d structures lack the
   methylglutamine (PMID:40913044). Its one change is Met347 at the
   position of P11558 Gln332, which matches the methionine the ANME-2d MCR
   structures report beside the coenzyme M-coordinating tyrosine
   (PMID:40913044).
3. The ethyl-coenzyme M reductase (ECR) alpha subunit of *Ca.* Ethanoperedens
   thermophilum (A0A7R9R780) is the most divergent sequence (47.6%
   identity). It has Met181 at the position of the F430 axial glutamine,
   Ala259 at the position of the coenzyme B contact Arg225, Asn375 at the
   Gln332 position, and Gln497 at the S-methylcysteine position. The coenzyme B contacts K290 and R304
   are conserved, and UniProt annotates both from the 7B1S/7B2C structures.
   The Met181 substitution is the nickel-ligand change described from the
   crystal structure (PMID:34210888).
4. Gln400, the 2-methylglutamine site of P11558, is conserved in every
   sequence. Only P11558 carries a MOD_RES feature there; P07962 has no
   modification at Q420.

## ANME-2d strain check

`compare_anme2d_strains.py` aligns A0A284VQI9 with RefSeq WP_097300250.1, the
McrA of *Ca.* Methanoperedens sp. BLZ2, whose MCR structure was solved
(PMID:40913044). The BLZ2 protein maps only to deleted UniProt entries, so the
script fetches it from NCBI. Result (2026-11-13): 89.7% identity over aligned
positions, so the BLZ2 structure is evidence from a close same-genus ortholog,
not from this entry.

These are sequence observations. Whether a substitution changes substrate
specificity is a question for the structural and biochemical literature
cited in each gene review.
