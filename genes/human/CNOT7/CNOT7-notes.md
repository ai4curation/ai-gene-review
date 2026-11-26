# CNOT7 review notes

PANTHER places human CNOT7 and CNOT8 in the CAF1/POP2 DEDD-family deadenylase family PTHR10797.
The cached PAINT slice asserts four root gains at PTN000084083: P-body, CCR4-NOT core complex,
poly(A)-specific ribonuclease activity, and nuclear-transcribed mRNA catabolic process,
deadenylation-dependent decay. The nuclease and core-complex claims fit CNOT7 directly; the P-body
claim is peripheral for human CNOT7 because its direct human localization support in the GOA set is
nuclear and cytoplasmic granule evidence, while the P-body transfer comes from mouse, budding yeast
and worm CAF1/Pop2 orthologs.

Key CNOT7 sources used here:

- [PMID:15769875] identified conserved human CAF1-family deadenylase activity and directly tested
  CNOT7 and CNOT8.
- [PMID:19276069] solved the Tob-hCAF1 interaction and showed CNOT7 poly(A)-specific nuclease
  activity in vitro.
- [PMID:19558367] isolated human CCR4-NOT complexes with alternative CNOT7/CNOT8 and CNOT6/CNOT6L
  catalytic subunits.
- [PMID:20065043] connected CCR4-NOT deadenylation to human miRISC-associated mRNAs.
- [PMID:21278420] showed that CNOT1 recruits CAF1/CNOT7 to tristetraprolin targets for mRNA decay.
- [PMID:21336257] showed TOB-mediated CNOT7 recruitment to a CPEB3 target for deadenylation.
- [PMID:21981923] and [PMID:21984185] show that GW182/TNRC6 recruits CCR4-NOT during
  miRNA-mediated deadenylation.
- [PMID:23386060] supports a STAT1-binding, interferon-signaling role for CNOT7 that is mechanistic
  but outside the core mRNA deadenylation activity.
- [PMID:31320642] reconstituted recombinant human CCR4-NOT and connected the CNOT1 MIF4G scaffold,
  the CAF1 nuclease module, and other noncatalytic modules to coordinated deadenylation.
- [PMID:31439799] placed CNOT7 poly(A)-specific ribonuclease activity in CAPRIN1/FMRP condensates.

Rows judged over-annotated:

- The mouse-derived `piRNA binding`, `piRNA-mediated gene silencing by mRNA destabilization`, and
  broad regulatory ncRNA-mediated silencing IEA/ISS transfers rest on a germline Nanos2/piRNA
  context. Human CNOT7 has direct evidence for miRNA-associated mRNA deadenylation, but no direct
  piRNA-binding or piRNA-pathway role in the fetched GOA references.
- The NK-cell membrane HDA row has no supporting topology or trafficking mechanism for a soluble
  CCR4-NOT deadenylase.
- BTG/TOB experiments show that CNOT7 mediates target mRNA deadenylation recruited by those adaptors;
  the downstream positive or negative cell-proliferation readouts are not the direct molecular work
  performed by CNOT7.

## 2026-11-26: upstream ORF `c8riboseqorf15` (microprotein project)

- The TransCODE consortium lists a 39 aa upstream ORF in CNOT7's first exon, `c8riboseqorf15`,
  as a Tier 1A "peptidein" [PMID:42092140 "codify the new conceptual model of 'peptideins' as microproteins that have indeterminate potential as functional proteins"].
- Ji & Salzberg (bioRxiv preprint, DOI:10.64898/2026.11.19.767917, not cached, not peer
  reviewed) instead read it as the first coding exon of an unannotated CNOT7 isoform. The same
  start codon splices past exon 2 into exon 3, in frame, giving a protein like canonical CNOT7
  with a different N-terminus. Their earlier uORF study is
  [PMID:39565752 "541 out of 2,199 upstream ORFs have strong evidence that they can form protein coding exons that are part of an existing gene"].
- Neither reading affects any GO row in this review: every annotation concerns the canonical
  CCR4-NOT deadenylase. If UniProt later adds this ORF as a separate entry, or adds the
  isoform to Q9UIV1, revisit it. Context: `projects/MICROPROTEINS.md`, section "Contested
  Ribo-seq ORF evidence".
