# ATG4C (donkey, A0A9L0IIU3) notes

DONKEY40 cohort review. Evidence: donkey UniProt TrEMBL record (PE 3; RuleBase/ARBA-derived function text),
donkey GOA (9 IEA rows, 7 from TreeGrafter), human Swiss-Prot Q96DT6 fetched into `ATG4C-bioinformatics/`,
cached publications PMID:21177865, PMID:29458288 and PMID:33773106 (abstract-only), the human ATG4D review
for family conventions, and a donkey-human comparison. No deep-research provider call was made.

## Sequence

- 458 aa vs human 458 aa, 94.98% identity, full-length [file:EQUAS/ATG4C/ATG4C-bioinformatics/RESULTS.md "with 94.98% identity across 458 paired residues"].
- Catalytic triad conserved [file:EQUAS/ATG4C/ATG4C-bioinformatics/RESULTS.md "ACT_SITE (Nucleophile): human [111] C -> donkey [111] C."; also D345, H347].
- Peptidase C54 catalytic domain and C-terminal ATG4 LIR (Pfam PF20166) present; PANTHER PTHR22624:SF38.

## Function

- Cysteine protease priming and delipidating ATG8 proteins [file:EQUAS/ATG4C/ATG4C-bioinformatics/human_Q96DT6-uniprot.txt "Cysteine protease that plays a key role in
  autophagy by mediating both proteolytic activation and delipidation of ATG8 family proteins"].
- Weak priming, stronger delipidation than ATG4B [file:EQUAS/ATG4C/ATG4C-bioinformatics/human_Q96DT6-uniprot.txt "shows weaker ability to cleave the C-terminal amino acid
  of ATG8 proteins, while it displays stronger delipidation activity"]; kinetics show minimal ATG4C priming
  activity [PMID:21177865 "whereas Atg4C and Atg4D had minimal activities as did the catalytic mutant of Atg4B
  (C74S)"]; all four ATG4s delipidate membrane-anchored ATG8s [PMID:29458288 "all 4 ATG4 proteases can be
  activated to similar enzymatic activities on lipid-attached substrates"].
- Mitophagy: ATG4C weakly or not involved in phagophore growth during mitophagy [file:EQUAS/ATG4C/ATG4C-bioinformatics/human_Q96DT6-uniprot.txt "In contrast to other members
  of the family, weakly or not involved in phagophore growth during mitophagy"].
- Piecemeal microautophagy of the nucleus is a yeast nucleus-vacuole junction process with no mammalian
  counterpart demonstrated.

## Decisions

ACCEPT: cysteine-type endopeptidase activity, protein-PE deconjugating activity, autophagosome assembly,
protein processing, cytoplasm, cysteine-type peptidase activity (InterPro parent). KEEP_AS_NON_CORE: aggrephagy.
MARK_AS_OVER_ANNOTATED: mitophagy (human evidence that ATG4C is the family member least involved), piecemeal
microautophagy of the nucleus (yeast-specific process).

## ProtNLM2 GO predictions

GO:0006508 proteolysis: LSP (protein processing and cysteine-type endopeptidase activity in GOA).
GO:0051697 protein delipidation: COR (human IDA; donkey GOA has the MF only).
GO:0006914 autophagy: LSP (autophagosome assembly, aggrephagy in GOA).
