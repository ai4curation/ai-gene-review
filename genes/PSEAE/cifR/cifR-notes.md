# cifR (PA2931, Q9HZR6) notes

## Identity

- CifR, 196 aa TetR-family (TFR) transcriptional repressor, divergently
  transcribed from the morB-cfrX-cif operon. UniProt TrEMBL entry
  (Q9HZR6_PSEAE, SubName "CifR"), PE 1 (evidence at protein level) on the
  strength of three crystal structures (PDB 6NSM, 6NSN, 6NSR).
- Domains: HTH tetR-type 9..69 with the H-T-H motif at 32..51
  (PROSITE PS50977, PRU00335); TetR_N (PF00440) plus TetR_C_13 (PF16925)
  ligand-binding domain. PANTHER PTHR47506 / PTHR47506:SF1.
- UniProt records Cys107 modified as cysteine sulfenic and sulfinic acid from
  the 6NSN structure (ECO:0007829), matching the epoxide/oxidant-sensing
  cysteine of the 2024 study.

## Function

- CifR was identified as the repressor of cif, the secreted epoxide hydrolase
  virulence factor that reduces apical CFTR
  [PMID:18458065 "We show that the predicted TetR family transcriptional repressor encoded by the PA2931 gene, which is immediately adjacent to and divergently transcribed from the cif-containing, three-gene operon, negatively regulates cif gene expression by binding to the promoter region immediately upstream of the cif-containing operon."]
  and the DNA complex is released by the epoxide epibromohydrin
  [PMID:18458065 "Furthermore, this protein-DNA interaction is disrupted by the epoxide EBH in vitro, suggesting that the binding of EBH by the PA2931 protein product drives the disassociation from its DNA-binding site."]
- Two operators in the cifR-morB intergenic region, mapped by EMSA and
  chromosomal mutagenesis, controlling both divergent transcripts
  [PMID:22843844 "We identified two sites of CifR binding in the intergenic space between cifR and morB, the first gene in the operon containing the cif gene."]
  [PMID:22843844 "Mutagenesis of these binding sites resulted in a loss of DNA binding in vitro, and mutation of one of these sites in vivo resulted in an increase in transcription of both the cif and cifR genes."]
  So CifR represses its own gene as well as the cif operon
  [PMID:22843844 "Mutagenesis of the operator proximal to morB resulted in an increase in expression of both the cif and cifR transcripts, suggesting that both sites are required for complete repression of each of these genes."]
- Structures of CifR alone and bound to operator DNA, with Cys107 as the
  epoxide-sensing residue
  [PMID:39413156 "We present here the first molecular structures of CifR alone and in complex with operator DNA, resolved in a single crystal lattice."]
  [PMID:39413156 "We also determined that cysteine residue Cys107 is critical for epoxide sensing and DNA release."]
  [PMID:39413156 "Despite the length of the operator sequence, the overall structure turned out to involve a single CifR dimer binding per operator site, with unusual protein:DNA contacts at the periphery."]
  [PMID:39413156 "Furthermore, EBH disrupts CifR binding to the intergenic promoter region, permitting transcription of cifR and the three divergently transcribed genes including cif ( 16 , 18 ) (Figure 1; bottom row)."]
- CifR is described as the first epoxide-sensing bacterial transcription factor
  [PMID:39413156 "CifR represents the first reported epoxide-sensing bacterial transcriptional regulator, but neither its interaction with cognate operator sequences nor the mechanism of activation has been investigated."]
- See genes/PSEAE/cif (reviewed separately) for the regulated target.

## PAINT node PTN002934616

- PTHR47506 ("transcriptional regulatory protein"; subfamily SF1 "HTH-type
  transcriptional regulator YjdC"). The repository family folder has no
  PAINT file, so the node content was read from QuickGO: 25 leaf IBAs of
  GO:0045892 in 9 taxa (E. coli yjdC, Shewanella mexR and SO_1578/SO_3393,
  Bradyrhizobium bll/blr genes, Streptomyces SCO genes, Vibrio VC_A genes,
  Xanthomonas XCC0044, Gloeobacter gll1420, Rhodopirellula RB genes, and
  P. aeruginosa cifR and PA2484).
- The only IBD at the node is GO:0045892, and cifR is the sole seed. The
  supporting annotations are all experimental and all on CifR itself:
  CollecTF EXP and IEP from PMID:22843844 and PseudoCAP IMP from
  PMID:18458065. Only the IMP is a PseudoCAP row.
- The leaves are TetR/MarR-type HTH regulators, for which repression is the
  usual mode; the term is a cautious, aspect-appropriate family-level claim,
  not a transfer of the epoxide-sensing specialisation. CollecTF's finer MF/CC
  rows (GO:0001217, GO:0000976, GO:0032993) were not propagated, which is the
  right choice since operator identity is gene-specific.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002934616 | GO:0045892 negative regulation of DNA-templated transcription | 1 (sole seed) | 25 (9 taxa) | GO:0045892, IMP, PMID:18458065 (PseudoCAP); same term EXP and IEP, PMID:22843844 (CollecTF) | SOUND | The seed is the gene's own direct activity, not a downstream phenotype: purified CifR binds two mapped operators in the cifR-morB intergenic region, chromosomal operator mutations raise cif and cifR transcription, and the epoxide EBH releases CifR from DNA; the 2024 structures show a CifR dimer on its operator. A sole seed is not weak support (the IBD rests on a well-characterised repressor), and cifR appearing in its own With/From marks the experimental grounding on the target. The node term is a broad, sign-correct generalisation for a clade of TetR/MarR-type HTH repressors, and the gene-specific operator and epoxide-sensing claims were correctly not propagated. |

The other PseudoCAP row types for this gene: there is only one PseudoCAP
annotation in the GOA file (the GO:0045892 IMP above). PA2931 has no other
PseudoCAP seeding, so no further seeds need assessment.

## Decisions summary

- ACCEPT: negative regulation of DNA-templated transcription (IMP, EXP, IEP,
  IBA), DNA-binding transcription repressor activity, transcription
  cis-regulatory region binding, protein-DNA complex.
- MODIFY: DNA binding (IEA) -> transcription cis-regulatory region binding;
  regulation of DNA-templated transcription (ARBA IEA) -> negative regulation
  of DNA-templated transcription.
- No REMOVE; no source defects found.
