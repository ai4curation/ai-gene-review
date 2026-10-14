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
