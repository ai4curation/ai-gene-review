# AK1 (P00568) bioinformatics: where the adenylate kinase deficiency variants sit and what they break

All numbers below are produced by the scripts in this folder (`just all`); the
machine-readable outputs are in `results/`. Inputs are the committed UniProt flat
file, NM_000476.3 (NCBI), PDB 1Z83, 2C95, 7X7S, 8X1G and 7DE3, the AlphaFold DB
model and AlphaMissense scores for P00568, UniProtKB (orthologues, family panel,
unreviewed human entries) and the gnomAD v4 GraphQL API (variants, constraint and
the ClinVar records it mirrors). Downloads are cached in `data/`, which is not
committed. Run date 2026-11-26.

## 1. Numbering check (`01_variant_consequences.py`)

The NM_000476.3 coding sequence is 585 nt and its translation is identical to the 194-residue UniProt P00568 canonical sequence, so cDNA and protein numbering agree with no offset.
Every reported substitution names the reference base that is really at that position.
All fourteen published cDNA changes reproduce the protein consequence the papers give; the one consequence the cached record did not state, c.518T>G, computes to p.Val173Gly.
The in-frame deletion c.418_420del removes one of two adjacent aspartates (Asp140 or Asp141); the two descriptions are the same protein, and HGVS 3' rule names it p.Asp141del while UniProt lists position 140.
The legacy name "delG138" is c.138del (ClinVar writes it c.139del, the same allele in a run of two G) and gives p.Val47SerfsTer45, a stop at codon 91 as the paper reported.

| Truncating allele | Native residues kept | New stop codon | Predicted NMD (stop more than 55 nt upstream of the last exon junction at c.516) |
|---|---|---|---|
| c.138del p.Val47SerfsTer45 | 46 | 91 | yes |
| c.166A>T p.Lys56Ter (ClinVar only) | 55 | 56 | yes |
| c.223dup p.Met75AsnfsTer19 | 74 | 93 | yes |
| c.319C>T p.Arg107Ter | 106 | 107 | yes |
| c.464del p.Lys155ArgfsTer39 | 154 | 193 | no (stop in the last exon) |

Four of the five truncating alleles are predicted to be degraded by nonsense-mediated decay and, if translated at all, would lack the LID domain and the Arg132, Arg138 and Arg149 phosphate-binding residues.
The c.464del allele escapes the NMD rule and would make a 192-residue protein whose last 38 residues are out of frame, replacing the C-terminal half of the CORE domain including the Gly177 ATP-binding position.

## 2. Structure mapping (`02_structure_mapping.py`)

1Z83 (human AK1 with the bisubstrate inhibitor Ap5A, 1.90 A) and 2C95 (with Ap4A, 1.71 A) are numbered exactly as UniProt; both crystallised constructs differ from the canonical sequence only at Lys9 (Asn) and the C-terminal residue.
7X7S (apo wild type, NMR) is numbered with a five-residue tag offset (author label minus UniProt position = 5), so residues were mapped by sequence alignment and not by label.
The adenosine of Ap5A nearest the P-loop (residues 18-23) was taken as the ATP-site nucleotide and the other as the AMP-site nucleotide.

Full per-variant table: `results/variant_table.md`. Summary:

| Variant | Domain | Distance to Ap5A in 1Z83 (A) | What the wild-type side chain does (computed contacts) | rSASA |
|---|---|---|---|---|
| Gln24Arg | CORE, helix 21-32 behind the P-loop | 5.15 (phosphate) | side chain hydrogen-bonds the backbone of Val179 and Phe183 | 0.04 |
| Gly40Arg | NMP | 3.53 (phosphate) | no side chain; invariant glycine at the AMP phosphate | 0.19 |
| Gly64Arg | NMP | 4.42 (AMP ribose) | no side chain; glycine in the Gly64-Gln65 AMP-binding turn | 0.10 |
| Arg97Trp | CORE, AMP site | 3.51 (AMP adenine) | guanidinium bonds Thr157; packs on Tyr95, Tyr153, Ala156 | 0.23 |
| Gln101Lys | CORE, AMP site | 3.06 (AMP adenine) | side chain hydrogen-bonds N1 and N6 of the AMP adenine | 0.04 |
| Arg128Trp | CORE, ATP site | 3.38 (ATP adenine) | bonds the backbone of Gly18 and Ser19 (P-loop) and Ala175, and N6 of the ATP adenine | 0.29 |
| Arg132His | LID | 2.83 (phosphate) | bonds two phosphates, Asp141 and Arg138 | 0.28 |
| Arg138His | LID | 3.15 (phosphate) | bonds four phosphate oxygens, Asp140, Arg132, Arg149 and Arg44 | 0.28 |
| Asp141del | LID, helix 139-141 | 5.06 (phosphate) | carboxylate bridges Arg132 and Arg149 | 0.05 |
| Tyr164Cys | CORE, helix 158-167 | 11.80 | buried; hydroxyl bonds Glu106 | 0.01 |
| Val173Gly | CORE, strand 170-174 | 9.91 | fully buried in the central beta-sheet | 0.00 |

Eight of the eleven non-truncating variants (Gly40Arg, Gly64Arg, Arg97Trp, Gln101Lys, Arg128Trp, Arg132His, Arg138His and Asp141del) change a residue within 5.1 A of the bound bisubstrate inhibitor, in the AMP site, the ATP site or the phosphate-clamping arginine network of the LID.
The three remaining missense variants (Gln24Arg, Tyr164Cys and Val173Gly) change residues that are buried (relative solvent accessibility 0.04 or less) and 5 to 12 A from the nucleotide, the pattern expected of folding or stability defects rather than loss of a ligand contact.
No disease variant lies on the protein surface away from the active site.

### Experimental structures of two variants

| Entry | State | NMP-CORE (A) | LID-CORE (A) | NMP-LID (A) |
|---|---|---|---|---|
| 1Z83 | wild type + Ap5A, closed | 18.76 | 21.53 | 15.69 |
| 2C95 | wild type + Ap4A, closed | 18.64 | 21.65 | 15.58 |
| 7X7S | wild type, apo, NMR (20 models) | 17.71 +/- 0.28 | 23.19 +/- 0.40 | 18.87 +/- 0.96 |
| 8X1G | Arg97Trp, apo, NMR (20 models) | 19.36 +/- 0.39 | 24.28 +/- 0.51 | 23.42 +/- 0.98 |
| 7DE3 | Arg128Trp, crystal, no nucleotide | 22.41 | 24.44 | 30.46 |

Distances are between CA centroids of the NMP domain (38-67), the LID (131-141) and the remaining CORE residues.
In the apo NMR ensembles the NMP-to-LID distance is 18.87 A in wild type and 23.42 A in Arg97Trp, a difference of about 4.6 A that is several times the ensemble spread: the variant is more open.
In apo wild type Arg97 contacts Tyr153, Ala156, Thr157 and Val160; in the Arg97Trp ensemble Trp97 contacts Leu66, Leu69 and Tyr95 instead, so the side chain has left the helix 153-160 surface and packs against the base of the NMP domain.
In the Arg128Trp crystal structure Trp128 has lost the contacts Arg128 makes with Gly18, Ser19 and Ala175 or Gly177, and LID residues 133-141 are not modelled (disordered).
7DE3 has no deposited publication (the PDB record gives "to be published") and no nucleotide, so its very open geometry mixes the effect of the substitution with crystal packing and the apo state; it is reported as observed and not interpreted further.

### AlphaFold and AlphaMissense

The AlphaFold model has a mean pLDDT of 95.88 and adds nothing the crystal structures do not already show.
AlphaMissense calls every disease missense variant likely pathogenic (scores 0.76 to 1.00) and the three common homozygous population variants likely benign (Glu123Gln 0.09, Ala162Thr 0.08, Ser58Leu 0.19).

## 3. Conservation (`03_conservation.py`)

Orthologue panel: the seven reviewed, non-fragment vertebrate AK1 entries other than human (rat, mouse, cow, rabbit, pig, chicken, carp; 73 to 97 percent identical to human).
Family panel: human AK2, AK3, AK4, AK5, CMPK1, yeast ADK1, E. coli Adk and B. subtilis Adk (30 to 58 percent identical).

Gly40, Arg97, Arg128, Asp141 and Tyr164 are identical in all seven vertebrate orthologues and all eight family-panel sequences.
Gly64, Gln101, Arg132 and Arg138 are identical in all orthologues and in seven of eight family sequences, and Gln24 in six of eight.
Val173 is the least conserved disease position (five of seven orthologues, two of eight family sequences, where it is replaced by Ile, Phe or Ala); the position tolerates larger hydrophobic side chains, and the variant removes the side chain altogether.
The common polymorphism Glu123Gln, the classical AK1*2 electrophoretic allele position, is surface exposed (rSASA 0.41) and 9.9 A from the nucleotide.

## 4. Population data (`04_population.py`)

gnomAD v4 constraint for AK1: pLI 0.009, loss-of-function observed/expected 0.54 (90 percent interval 0.35 to 0.86), missense Z 1.10.
AK1 is therefore not constrained against heterozygous loss of function, which fits a recessive disorder with healthy carriers.
gnomAD holds 39 high-confidence predicted loss-of-function variants on the MANE transcript with 98 alleles in total and no homozygote.
None of the reported disease variants is homozygous in gnomAD; the most frequent is Arg97Trp (40 alleles in 1,461,858), then Arg132His (23) and Arg138His (10).
Two published indels are in gnomAD under their 3'-shifted names and are matched by protein consequence: Asp141del as c.421_423del (6 alleles) and Val47SerfsTer45 as c.139del (1 allele).
Published variants absent from gnomAD v4 are Gln24Arg, Met75AsnfsTer19, Lys155ArgfsTer39 and Val173Gly.
The missense variants that do occur homozygous are Glu123Gln (1,477 homozygotes, allele frequency 0.038), Ala162Thr (74), Ser58Leu (17), Ala162Val (2), Ser51Leu (1) and Leu5Pro (1).
ClinVar (as mirrored by gnomAD) lists eleven pathogenic or likely pathogenic AK1 records: the published variants Gly40Arg, Gly64Arg, Gln101Lys, Arg107Ter, Arg128Trp, Asp141del, Tyr164Cys and Val47SerfsTer45, plus Arg132His, Lys56Ter and a splice-acceptor deletion-insertion (c.44-5_48delinsC) for which no publication was found in PubMed.
Most ClinVar assertions carry no or one review star, and 45 AK1 records are of uncertain significance.

## 5. The AK1beta isoform (`06_ak1beta_isoform.py`)

The reviewed entry P00568 lists no alternative products.
Among the 18 human UniProtKB entries with gene name AK1, one unreviewed entry, Q5T9B7 (210 residues; RefSeq NP_001305051.1; Ensembl ENST00000223836), carries canonical residues 3-194 behind an alternative 18-residue N-terminus, MGCCSSSDPRREDDLRAR.
That N-terminus matches the N-myristoylation consensus (Gly2, Ser6) and has cysteines at positions 3 and 4.
Residue numbers in this isoform are the canonical number plus 16.

## Interpretation

1. The disease alleles are loss-of-function alleles of three kinds: truncations that remove the protein, substitutions of residues that bind AMP, ATP or the transferred phosphates, and substitutions of buried residues that hold the CORE fold together.
2. Nothing in the data suggests a gain of function or a dominant-negative effect: the enzyme is a monomer, the gene tolerates heterozygous loss-of-function variants in the population, and there is no surface or interface cluster.
3. The analysis cannot say how much residual activity each allele leaves in a red cell; that needs the enzyme assays reported in the literature.
4. The analysis does not address why red cells are the tissue affected, or whether AK1 loss alone is sufficient for haemolysis; those are questions about erythrocyte metabolism, not about the protein.
