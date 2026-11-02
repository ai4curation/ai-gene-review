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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 9 GOA rows, the description and core functions. ProtNLM2 output was not consulted.

Deep research: `just deep-research EQUAS ATG4C --provider falcon` failed (Edison API "Failed to authenticate",
HTTP 403); no deep-research file was produced. Review rests on the cached publications (PMID:21177865,
PMID:29458288, PMID:33773106, all abstract-only), the human Swiss-Prot record Q96DT6 and the existing
donkey-human comparison in `ATG4C-bioinformatics/`.

Identity: A0A9L0IIU3 is the full-length donkey ATG4C product, not a fragment or isoform. It is 458 aa, the
same length as human Q96DT6, with full-length pairing at 94.98% identity
[file:EQUAS/ATG4C/ATG4C-bioinformatics/RESULTS.md "with 94.98% identity across 458 paired residues"], no
unpaired segments, catalytic Cys111/Asp345/His347 conserved, and Peptidase_C54 plus ATG4_LIR (PF20166)
domains present. Five RefSeq models map to the same Ensembl gene.

Evolutionary grounding: UniProt places the donkey protein in PANTHER PTHR22624:SF38 (CYSTEINE PROTEASE ATG4C),
the same subfamily as human Q96DT6, mouse Q811C2 and Xenopus Q5XH30/Q68EP9
(interpro/panther/PTHR22624/PTHR22624-entries.csv). The TreeGrafter rows all come from PTN009050878, which
also gives human ATG4C its IBA rows for the same terms, so the transfer is from a family-wide PAINT node;
subfamily-specific features (weak priming, weak/no mitophagy role) come from human ATG4C itself, which is
in the same subfamily. No PANTHER family review YAML exists under interpro/panther/PTHR22624/ (entries and
metadata only), so there is no subfamily-placement disagreement to report.

Changes from the earlier review:
- GO:0008234 cysteine-type peptidase activity: ACCEPT -> MODIFY to GO:0004197 (already carried), since the
  earlier reason itself said a more specific term is supported.
- GO:0005737 cytoplasm: reason corrected; human record says cytoplasm by similarity to mouse Q8BGE6, which
  is ATG4B (SF39), not the mouse ortholog.
- GO:0034727 piecemeal microautophagy of the nucleus: kept MARK_AS_OVER_ANNOTATED, reasoning tied to the
  family-wide PAINT node and the yeast-specific nucleus-vacuole junction.
- NEW GO:0051697 protein delipidation (ISS from human ATG4C): ATG4C is the enzyme performing the step,
  human has direct delipidation assays [PMID:29458288 "all 4 ATG4 proteases can be activated to similar
  enzymatic activities on lipid-attached substrates"]; added to core_functions.
- Unchanged: autophagosome assembly, cysteine-type endopeptidase activity, protein processing,
  protein-PE deconjugating activity (ACCEPT); mitophagy (MARK_AS_OVER_ANNOTATED, human ATG4C weakly or not
  involved in mitophagic phagophore growth); aggrephagy (KEEP_AS_NON_CORE).

Relative to review next: human ATG4C (Q96DT6), ortholog in the same PANTHER subfamily SF38; no review
exists in genes/human/. Module: modules/metazoan_autophagosome_biogenesis.yaml (ATG4 priming part,
PANTHER:PTHR22624).
