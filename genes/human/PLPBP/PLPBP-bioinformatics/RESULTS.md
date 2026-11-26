# PLPBP (O94903) structure and variant analysis: results

Inputs fetched 2026-11-26: AlphaFold model AF-O94903-F1 v6, PDB 1CT5 and 1B54
(S. cerevisiae YBL036C with PLP), 1W8G (E. coli YggS with PLP), 5NM8
(Synechococcus PipY with PLP), RefSeq NM_007198.4 CDS, ClinVar, gnomAD v4.
All numbers below come from the files in `results/`.

## Checklist

- [x] No script hardcodes inputs or outputs (all paths and identifiers are arguments)
- [x] Scripts tested on a second input (`just control`: mouse Q9Z2Y8 gives the same Schiff-base lysine, K47)
- [x] Analyses completed as expected
- [x] Direct results are in `results/`
- [x] Provenance and justification are given below
- [ ] An experimental structure of the human protein was used (none exists; PDBe `best_structures` returns no entry for O94903, so the human coordinates are an AlphaFold model)
- [ ] Stability (ddG) prediction was run (not run; no stability predictor is used here, so "destabilising" below is a structural argument, not a computed energy)
- [ ] A mitochondrial-targeting predictor (TargetP, MitoFates) was run (not run; only sequence descriptors are reported)

## 1. Numbering check

- The NM_007198.4 CDS (828 nt) translates exactly to the 275-residue UniProt canonical sequence (`variant_summary.json`, `cds_translation_equals_uniprot_canonical: true`).
- All 24 literature variants that carry a protein change reproduce that change when their c. change is applied to the CDS (`n_p_consistent: 24`, no inconsistencies). The other four are two splice-donor variants, one splice-acceptor variant and c.596dup, whose paper gives no protein change in the abstract; the CDS gives p.Leu200Alafs*11 for c.596dup.
- No gnomAD missense variant disagrees with the canonical reference residue.

Residue numbers in the literature for this gene therefore refer to the canonical O94903 sequence.

## 2. Fold and PLP site

- The AlphaFold model is confident for the barrel (mean pLDDT 89.3); residues 1-11 and 250-275 have pLDDT below 70 and are treated as unmodelled tails.
- The model superposes on the four PLP-bound homologs with CA RMSD 0.82-0.91 Å over 130-156 residue pairs (38-45% sequence identity).
- In all four templates the lysine whose NZ is covalently linked to PLP C4A aligns with human **Lys47** (yeast K49, E. coli K36, PipY K26). This agrees with the mass-spectrometric identification of K47 in the human protein (PMID:31825581).
- Human residues within 4.5 Å of the transplanted PLP: V45, K47, N68, I94, M181, I183, M225, S226, A227, R241, I242, G243, S244, R250.
  - Phosphate contacts: S226 (1.7 Å from a phosphate oxygen), G243, S244, I242 backbone region.
  - Pyridine ring contacts: R241 (2.9 Å from N1), N68 (2.5 Å from O3), V45, I94, M181, I183, M225.
- E. coli Lys137, reported as the key RNA-binding residue (PMID:39604152), aligns with human Lys153 (family identity 0.76), 9.7 Å from PLP.

## 3. Reported patient variants

Columns are in `results/literature_variants.tsv`. Distances are to the transplanted PLP; RSA is relative solvent accessibility in the monomer model; identity is the fraction of 29 reviewed family members with the human residue.

### Truncating and splice variants

| Variant | Native residues kept | PLP-site residues lost |
|---|---|---|
| p.Cys15Ter | 14 | all, including K47 |
| c.207+1G>A, c.207+1G>T (donor of the exon ending at codon 69) | not computed (splice) | not computed |
| p.Gln71Ter | 70 | I94 onwards (11 of 14) |
| p.Ser78Ter | 77 | I94 onwards |
| p.Ser84Cysfs*21 | 83 | I94 onwards |
| c.320-2A>G (acceptor) | not computed (splice) | not computed |
| p.Asp124Lysfs*2 | 123 | M181 onwards (10 of 14) |
| p.Leu200Alafs*11 (c.596dup) | 199 | M225, S226, A227, R241-S244, R250 |

Every truncating variant removes the phosphate-binding residues S226 and G243/S244 and the ring-contacting R241, and removes at least one third of the barrel strands. None can produce a PLP-binding barrel. Where measured, the transcript and protein are lost (p.Ser78Ter: UniProt VAR_078005, PMID:27912044).

### Missense variants at the PLP site (≤ 4.5 Å)

- **p.Val45Asp** (3.7 Å, RSA 0.07, identity 0.83): buried strand residue two positions before K47; places a carboxylate against the pyridine ring face and next to the Schiff-base lysine.
- **p.Ile94Phe** (3.1 Å, RSA 0.07, identity 0.86): packs on the PLP methyl (C2A); +23 Å3 in a closed pocket.
- **p.Arg241Gln** (2.7 Å, RSA 0.05, identity 1.00): the guanidinium sits 2.9 Å from the pyridine N1 and is hydrogen-bonded to the T182, S222 and M223 backbone. Loss of this arginine fits the experimental loss of PLP from the purified mutant (PMID:29689137) and failure to complement E. coli ΔyggS (PMID:27912044).

### Second shell and barrel core (buried, RSA < 0.2)

- **p.Glu67Lys** (6.8 Å, RSA 0.00, identity 1.00): the carboxylate is bonded to the K47 backbone N, S46 OG and K76 NZ; charge reversal in a buried position beside the Schiff-base strand.
- **p.His92Arg** (8.5 Å, RSA 0.00, identity 1.00): buried; contacts R41, T64, F65, M113 and E115.
- **p.Thr116Ile** (5.9 Å, RSA 0.00, identity 0.59): buried; side chain hydroxyl bonded to the G95 backbone, next to I94 and M181 of the pocket.
- **p.Gly224Ala** (5.2 Å, RSA 0.03, identity 1.00): invariant glycine immediately before M225-S226 of the phosphate loop.
- **p.Ala232Val** (10.4 Å, RSA 0.00, identity 0.97): helix packing against F198, M223 and G224; +51 Å3.
- **p.Val235Gly** (15.0 Å, RSA 0.12, identity 0.10): same helix as A232; −80 Å3 cavity. Poorly conserved and the most frequent patient missense allele in gnomAD (allele count 335, no homozygotes).
- **p.Leu175Pro** (18.6 Å, RSA 0.00, identity 0.90): proline in a buried strand/helix element far from the cofactor. Matches the gross misfolding of the recombinant mutant (PMID:29689137) and undetectable protein in fibroblasts (PMID:27912044).
- **p.Arg205Gln** (18.0 Å, RSA 0.10, identity 0.31) and **p.Met113Thr** (11.2 Å, RSA 0.01, identity 0.07) and **p.Pro40Leu** (13.3 Å, RSA 0.05, identity 0.10): buried, poorly conserved positions; R205Q and P40L showed reduced thermal stability experimentally (PMID:29689137).

### Solvent-exposed positions

- **p.Arg41Gln / p.Arg41Trp** (10.3 Å, RSA 0.24, identity 0.24): in the model the guanidinium forms a salt bridge with E220 and a hydrogen bond with N239, tying the first strand to the segment that carries the phosphate loop (G224-S226) and R241.
- **p.Tyr69Cys** (7.4 Å, RSA 0.28, identity 0.62): exposed position after N68; consistent with the reported intermolecular disulfide dimers and reduced PLP content (PMID:29689137).
- **p.Pro87Leu** (22.2 Å, RSA 0.50, identity 0.24) and **p.Ala107Thr** (19.8 Å, RSA 0.46, identity 0.34): exposed, poorly conserved, far from the cofactor. The model gives no structural reason for loss of function. P87L lowered solubility and yield of recombinant protein but the purified protein was folded (PMID:29689137).
- **p.His275Asp** (C-terminal residue, pLDDT 44, identity 0.10): in the disordered tail, 57 Å from PLP in the model. The structure gives no support for pathogenicity.

## 4. Patient versus population missense variants

Restricted to residues with pLDDT ≥ 70, patient missense variants (n = 18) differ from other gnomAD missense variants (n = 301) (permutation tests, 20,000 shuffles, seed 1; `spatial_tests.json`):

| Feature | Patient mean | gnomAD mean | p (two-sided) |
|---|---|---|---|
| Family identity | 0.58 | 0.39 | 0.003 |
| Relative SASA | 0.12 | 0.25 | 0.019 |
| Distance to PLP (Å) | 10.7 | 14.5 | 0.006 |

- The 14 patient positions outside the PLP site have a mean pairwise CA distance of 17.8 Å against a null of 22.6 Å for random well-modelled positions (p = 0.005). This null does not control for burial, and buried residues are closer together by construction, so this is weak evidence of a second functional surface.
- Close pairs among patient positions: R41-P40, H92-M113 (4.7 Å), E67-H92 (6.4 Å), E67-Y69, G224-A232, A232-V235. R41, H92 and M113 are in mutual side-chain contact.
- gnomAD homozygous missense variants on modelled residues are p.Val24Met (41 homozygotes) and p.Leu202Val (5 homozygotes), both at poorly conserved positions (identity 0.24 and 0.14) more than 10 Å from PLP.

## 5. Constraint and carrier frequency

- gnomAD v4 constraint: pLI 0.00002, LOEUF 0.97 (observed/expected LoF 0.67), missense Z 1.05. The gene tolerates heterozygous loss.
- 63 high-confidence predicted loss-of-function alleles, total allele count 307, no homozygotes. The most frequent are c.370_373del (108), c.207+1G>A (74), c.28G>T p.Glu10Ter (31), c.320-2A>G (13) and c.249_252del (11); four of these five are established patient alleles.

## 6. N-terminal descriptors

Residues 1-30 (`MWRAGSMSAELGVGCALRAVNERVQQAVAR`): net charge +2, two acidic residues, four basic residues, maximum 18-residue hydrophobic moment 0.46 at 100°, mean pLDDT 77. UniProt annotates no transit peptide. These descriptors do not establish or exclude a cleavable presequence.

## Interpretation

1. PLPBP is a single-domain fold-type III (alanine racemase N-terminal-like) barrel with PLP held as a Schiff base on K47, the phosphate by S226 and G243-S244, and the ring by R241 and N68. This is the only molecular function the structure supports directly; the barrel lacks the second domain that fold-type III enzymes use to complete an active site.
2. Disease is loss of function. Truncating alleles delete the phosphate and ring-binding residues; most missense alleles are at buried, conserved positions, at the cofactor or in its second shell, or are core substitutions with experimentally shown misfolding or instability. Heterozygous loss is tolerated in the population, as expected for a recessive disorder, and there is no clustering pattern that suggests gain of function or a dominant-negative effect.
3. Two classes remain unexplained by fold or cofactor contacts: the exposed variants P87L and A107T, and the C-terminal H275D. The model cannot say whether they affect an interaction surface, expression or splicing, or whether (for H275D in particular) the variant is causal.
4. R41, H92 and M113 form a contact cluster about 10 Å from PLP that links strand 1 to the C-terminal phosphate-binding segment. Variants there are expected to act through the cofactor site rather than a separate surface.
