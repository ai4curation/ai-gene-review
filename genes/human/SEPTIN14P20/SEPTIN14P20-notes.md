# SEPTIN14P20 (C0HM01, RBRP) review notes

## 2026-10-08 - MICROPROTEINS Tier 2 review (claude-code)

**Identity / existence.** 71-aa "putative RNA-binding regulatory peptide". UniProt PE5
(Uncertain) with CAUTION "Could be the product of a pseudogene". HGNC: `pseudogene`
(septin 14 pseudogene 20; prev. symbols LINC00266-1, C20orf69, NCRNA00266). 20q13.33.
It has its own HGNC symbol, so the standard folder convention applies.

**Bioinformatics** (SEPTIN14P20-bioinformatics/RESULTS.md): RBRP 1-47 is 47/47 identical to
SEPTIN14 383-429; only residues 48-71 are unique. The IGF2BP1-binding residue Gly-19 is septin
sequence (SEPTIN14 Gly-401). This contradicts the paper's statement
[PMID:32245947 "Sequence comparisons did not identify homologs of LINC00266-1 or the RBRP peptide in any other species, and there were no matching proteins and known domains/motifs in RBRP, indicating that RBRP is an uncharacterized peptide."]
The endogenous MS used a custom database
[PMID:32245947 "For the identification of exogenous and endogenous RBRP peptide, protein identification was performed using the Mascot (version 2.6.2) program against our generated RBRP protein database with the default parameters."]
so SEPTIN14-shared peptides cannot be excluded; the antibody epitope (TDTKKDKHPDPY) is
8/12 SEPTIN14-shared.

**Literature.** PubMed search for RBRP / LINC00266-1 / SEPTIN14P20 finds only PMID:32245947
(functional) and PMID:32709857 (LINC00266-1 as a ceRNA lncRNA in osteosarcoma; RNA-level,
not about the peptide; not cited in the review). One-paper peptide.

Key claims, PMID:32245947 (full text, PMC7125119):
- RNase-resistant IGF2BP1 binding via KH3-4; G19A abolishes it.
- Recombinant RBRP increases recombinant IGF2BP1 binding to m6A RNA
  [PMID:32245947 "Collectively, RBRP enhances the m6A recognition by IGF2BP1 on RNAs."]
- MYC mRNA stabilisation, IGF2BP1/METTL14/m6A-site dependent; rescue by WT but not G19A
  [PMID:32245947 "Thus, RBRP strengthens the recruitment of the RNA stabilizers HuR, MATR3, and PABPC1 to m6A-c-Myc CRD RNAs, to promote the stability of c-Myc mRNA and upregulate the c-Myc levels."]

**Decisions.** 3 rows. protein binding (IPI, IGF2BP1) -> MODIFY to GO:0140677 molecular
function activator activity (supported by recombinant in vitro data). mRNA stabilization and
positive regulation of mRNA binding (IDA) -> ACCEPT: locus-specific, full-text experimental
evidence, so the Tier 3 doubtful-existence rule (aimed at inherited rows) does not force
removal; caveats (PE5, pseudogene, single lab, SEPTIN14 identity) recorded on the reference
(DISPUTED) and a finding_review. No NEW terms.
