# IRF9 (donkey, A0A9L0I7X9) notes

DONKEY40 cohort review. Evidence: donkey UniProt TrEMBL record (PE 3; ARBA-derived function text), donkey GOA
(11 IEA rows: 4 TreeGrafter, ARBA, UniRule, combined), human Swiss-Prot Q00978 fetched into
`IRF9-bioinformatics/`, a donkey-human global comparison (`RESULTS.md`) and a DNA-binding-domain check
(`dbd_check.md`). No cached publications exist for donkey IRF9. No deep-research provider call was made.

## Sequence

- Donkey 421 aa vs human 393 aa: 80.41% identity over 388 paired residues; donkey has a 33-residue C-terminal
  extension (389-421) [file:EQUAS/IRF9/IRF9-bioinformatics/RESULTS.md "with 80.41% identity across 388 paired residues"].
- DNA-binding domain highly conserved; all five pentad tryptophans retained [file:EQUAS/IRF9/IRF9-bioinformatics/dbd_check.md "98 of 108 residues identical
  in donkey A0A9L0I7X9."]. Most divergence is in the disordered linker (114-197).
- IRF-3/IAD domain (Pfam PF10401, SMAD/FHA fold) present, which in IRF9 mediates STAT2 binding.
- The donkey record's CAUTION about lacking conserved residues comes from a PROSITE ProRule; the human
  Swiss-Prot entry has no such caution, and the pentad tryptophans are all conserved here.

## Function (human, transferred)

- ISGF3 DNA-binding subunit in type I IFN signalling [file:EQUAS/IRF9/IRF9-bioinformatics/human_Q00978-uniprot.txt "IRF9/ISGF3G associates with the phosphorylated
  STAT1:STAT2 dimer to form a complex termed ISGF3 transcription factor, that enters the nucleus."].
- ISRE binding and ISG activation [file:EQUAS/IRF9/IRF9-bioinformatics/human_Q00978-uniprot.txt "ISGF3 binds to the IFN stimulated response element (ISRE) to activate
  the transcription of interferon stimulated genes"].
- Human IRF9 deficiency causes immunodeficiency 65 with impaired type I IFN response.

## Decisions

ACCEPT: RNA pol II cis-regulatory sequence-specific DNA binding, RNA pol II-specific DNA-binding TF activity,
transcription cis-regulatory region binding, DNA-binding TF activity, nucleus, regulation of DNA-templated
transcription, regulation of transcription by RNA pol II, positive regulation of transcription by RNA pol II.
TOO_GENERAL: DNA binding (UniRule). MODIFY: immune system process -> type I interferon-mediated signaling
pathway (GO:0060337). MARK_AS_OVER_ANNOTATED: DNA-templated transcription (a transcription factor regulates,
rather than performs, transcription). NEW: ISGF3 complex (GO:0070721).

## ProtNLM2 GO predictions

GO:0045944, GO:0000976, GO:0003700: all CNN (exact terms already in donkey GOA).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used for this section.

### Identity

- A0A9L0I7X9 is the full-length donkey IRF9 product (421 aa, Ensembl ENSEASP00005036572.1, RefSeq
  XP_014724060.1), not a fragment. Relative to human Q00978 (393 aa) it carries a 33-residue C-terminal
  extension (donkey 389-421) and lacks 5 human residues (193-197) in the disordered linker
  [file:EQUAS/IRF9/IRF9-bioinformatics/RESULTS.md "with 80.41% identity across 388 paired residues"].
  Both the IRF tryptophan-pentad DNA-binding domain and the IRF-3/IAD (STAT2-binding) domain are present;
  all five pentad tryptophans are conserved [file:EQUAS/IRF9/IRF9-bioinformatics/dbd_check.md "human W80 -> donkey W80"].
  The record's PROSITE ProRule CAUTION about missing conserved residues does not correspond to any loss of
  the pentad tryptophans; it is not taken as evidence of a pseudogene or divergent model.

### Evolutionary grounding

- UniProt PANTHER cross-references place donkey IRF9 in PTHR11949:SF26 "INTERFERON REGULATORY FACTOR 9"
  [file:EQUAS/IRF9/IRF9-uniprot.txt "PTHR11949:SF26; INTERFERON REGULATORY FACTOR 9"], the same subfamily as
  human Q00978 and mouse Q61179 (interpro/panther/PTHR11949/PTHR11949-entries.csv). The GOA TreeGrafter rows
  come from PTN008986835. Function transfer from human IRF9 is therefore within-subfamily orthology, not a
  best-hit transfer. No PANTHER family review (ai-review) exists under interpro/panther/PTHR11949/ (only
  entries + metadata), so there is no subfamily-placement disagreement to report.

### Literature (cached this session)

- PMID:1630447 (Veals 1992, abstract): ISGF3-gamma is the DNA-recognition subunit of ISGF3 and binds DNA
  sequence-specifically ["ISGF3 gamma serves as the DNA recognition subunit"].
- PMID:30143481 (Hernandez 2018, full text): IRF9-deficient human cells form GAF but not ISGF3, lose ISRE
  binding by EMSA and ISRE-reporter activity; rescued by wild-type IRF9 ["These phenotypes are rescued by wild-type IRF9"].
- PMID:11846981 (Reich 2002 review): IRF9 is regulated by nucleocytoplasmic redistribution.
- PMID:30826365 (second IRF9-deficient family): no abstract text in cache; listed but not used as support.
- Deep research: `just deep-research-falcon EQUAS IRF9 --fallback perplexity-lite` failed on 2026-10-21
  (falcon "Failed to authenticate"; perplexity 401 insufficient_quota). No deep-research file exists.

### Changes vs previous review

- Supporting quotes of human DR GO lines (which restate annotations) replaced by quotes from PMID:1630447
  and PMID:30143481, plus PANTHER subfamily membership.
- GO:0000976, GO:0003700, GO:0006355, GO:0006357: ACCEPT -> TOO_GENERAL. Each previous reason argued that a
  more specific term was also annotated; OLS confirms GO:0000978 is_a GO:0000976, GO:0000981 is_a GO:0003700,
  and GO:0045944 is a descendant of GO:0006355 and GO:0006357.
- Unchanged: ACCEPT GO:0000978, GO:0000981, GO:0005634, GO:0045944; TOO_GENERAL GO:0003677;
  MARK_AS_OVER_ANNOTATED GO:0006351; MODIFY GO:0002376 -> GO:0060337; NEW GO:0070721 ISGF3 complex.
  IRF9 is a structural subunit of ISGF3 and performs its DNA-recognition step, so the complex and the
  type I IFN signalling term are participation, not downstream phenotype.
- Cytoplasm (human IDA/TAS) was considered as NEW but not added: the donkey GOA lacks it, and the
  nucleus is where the core activity is executed.

### Relative

- Closest characterised relative by phylogeny: human IRF9 (Q00978), same PANTHER subfamily SF26. No review
  exists in genes/human/IRF9 (nor mouse Irf9), so it needs review.
- Modules: modules/type_i_interferon_signaling.yaml (IRF9 DNA-binding partner, UniProtKB:Q00978),
  modules/jak_stat_signaling.yaml (ISGF3 mentioned in prose).
