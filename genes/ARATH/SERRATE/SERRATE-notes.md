# SERRATE (SE, At2g27100, UniProt Q9ZVD0) - curation notes

## 2026-10-19 - initial review (claude-code)

No deep-research provider was available in this environment, so these notes are
based on the cached publications (publications/PMID_*.md), PubMed searches, and the
UniProt record. Abstract-only papers are flagged.

### Identity and family

- 720-aa nuclear protein, ARS2 family (PANTHER PTHR13165:SF0; Pfam PF04959 ARS2,
  PF12066 SERRATE_Ars2_N), single C2H2-type zinc finger at 498-523 (UniProt FT),
  extensive disordered N- and C-terminal regions (MobiDB-lite).
- Metazoan ortholog is ARS2/SRRT [PMID:30152752 "SE and its metazoan ortholog
  ARSENITE RESISTANCE2 (ARS2) form complexes with DICER proteins and are required for
  efficient, precise primary-miRNA processing"]. No human SRRT review exists in this
  repo yet. Human SRRT carries IDA protein-macromolecule adaptor activity and mRNA
  cap binding complex binding (QuickGO, PMID:28297668), consistent with a
  family-level "CBC-associated adaptor" framing.

### Original cloning and development (abstract-only papers)

- se mutant: defects in organ initiation/elaboration; zinc finger protein
  [PMID:11402159 "Cloning the SE gene revealed that it encodes a protein with a single,
  C(2)H(2)-type, zinc finger related to genes in other eukaryotes"]. That paper
  speculated on chromatin modification [PMID:11402159 "suggests a role for the SE gene
  product in regulating changes in gene expression via chromatin modification"] - this
  is the source of the ISS DNA binding / TF / transcription regulation annotations. No
  study has shown sequence-specific DNA binding.
- Phase length / juvenile leaves [PMID:10607301].
- Leaf polarity and meristem via miR165/166-PHB and KNOX competence
  [PMID:16222298 "SERRATE acts in a microRNA (miRNA) gene-silencing pathway to regulate
  expression of the HD-Zip III gene PHABULOSA (PHB)"].

### miRNA biogenesis (core)

- General role in pri-miRNA processing, interacts with HYL1 [PMID:16889646 "SE is
  critical for the accumulation of multiple miRNAs and the trans-acting small
  interfering RNA (ta-siRNA), but is not required for sense post-transcriptional gene
  silencing"]; [PMID:16977334 "We show that SE is a general regulator of miRNA levels
  affecting the processing of primary miRNA to miRNA."]
- In vitro reconstitution: SE stimulates DCL1 [PMID:18632569 "We show that recombinant
  HYL1 and SE proteins accelerate the rate of DCL1-mediated cleavage of pre- and
  pri-miR167b substrates and promote accurate processing."] SE alone gave a ~6-fold
  stimulation of miR167b release (full text).
- Domain dissection [PMID:23921632 "SE uses its N-terminal domain to bind to RNA and
  requires both N-terminal and ZnF domains to bind to DCL1."]; [PMID:23921632 "the
  interaction with the ZnF domain of SE becomes indispensible and stimulates the
  activity of DCL1 without requiring SE binding to RNA"]. This is the best direct
  evidence for ribonuclease activator activity (GO:0170054), which the
  plant_mirna_biogenesis module already asserts for SE.
- Crystal structure of SE core 194-543 (PDB 3AX1) [PMID:21685453 "SE core provides the
  platform for HYL1 and DCL1 binding"]. NOTE: this paper carries a 2021 Expression of
  Concern (Nucleic Acids Res 49:3002); used only as corroborating evidence.
- D-bodies: [PMID:17442570 "bimolecular fluorescence complementation (BiFC) shows that
  DCL1, HYL1, and SE interact in D-bodies"]; SE is mostly in speckles and only
  transiently in D-bodies [PMID:17442570 "SE predominantly localizes to nuclear
  speckles"].
- Phase separation (abstract only) [PMID:33288888 "SE forms droplets and drives DCL1,
  HYL1 and pri/pre-miRNAs into the droplets in vitro, and mutation of SE abrogates the
  formation of D-bodies in vivo"]. Supports molecular condensate scaffold activity
  (GO:0140693) as a NEW MF.
- Scaffold role: [PMID:23141542 "In the miRNA processing complex, SE functions as a
  scaffold to mediate CPL1 interaction with HYL1"] (abstract only).
- CHR2/BRM remodels pri-miRNAs via SE [PMID:29769717 "We conclude that CHR2 accesses
  pri-miRNAs through SE and remodels their secondary structures"].
- SE recruits NEXT for pri-miRNA decay [PMID:32449937 "SE regulates miRNA biogenesis
  through its double contribution in promoting miRNA processing but also pri-miRNA
  degradation through the recruitment of the NEXT complex"].
- Other partners: HOS5, RS40, RS41 in speckles [PMID:26227967]; SMA1 [PMID:29982637];
  SEAP1 [PMID:34449907]; PAG1/20S proteasome turnover of SE [PMID:32690892].

### Splicing / CBC

- [PMID:18550839 "Whole-genome tiling array analyses reveal that se, abh1/cbp80, and
  cbp20 mutants also share similar splicing defects"] (abstract only).
- [PMID:24137006 "using Bimolecular Fluorescence Complementation (BiFC), pull-down and
  co-immunoprecipitation experiments, we show that both subunits of AtCBC, AtCBP20 and
  AtCBP80 interact with AtSE."] and SE affects 5' splice site choice of first introns.
- GOA has SE part_of nuclear cap binding complex (GO:0005846). GO defines that complex
  as the CBP20/CBP80 heterodimer; SE is an interacting partner (CBC-SE, cf. human
  CBC-ARS2). Proposed MODIFY to mRNA cap binding complex binding (GO:0140262), matching
  human SRRT IDA.

### Transcription

- [PMID:30152752 "Chromatin-bound SE liaised with paused and elongating polymerase II
  complexes and promoted their association with intronless target genes."] This is
  Pol II association, not DNA binding; supports positive regulation of Pol II
  transcription as a non-core role.

### Decisions summary

- REMOVE: DNA binding (ISS), DNA-binding TF activity (ISS): no evidence; zinc finger
  is a non-canonical protein/RNA-interaction module.
- MODIFY protein binding rows where the paper shows a scaffolding role (CPL1-HYL1,
  CHR2, NEXT) to protein-macromolecule adaptor activity; other bare protein binding
  rows REMOVE (policy).
- NEW: ribonuclease activator activity (GO:0170054) - SE stimulates DCL1; molecular
  condensate scaffold activity (GO:0140693).
- Upstream report candidates: GO:0005846 part_of -> GO:0140262; ISS DNA binding/TF
  rows from 2000-2001 sequence-based speculation.

## 2026-10-20: ported fixes from the parallel review branch

- The SE-DCL1/SMA1 GO:0005515 row (PMID:29982637, full text cached) changed from REMOVE to MODIFY to GO:0030674 protein-macromolecule adaptor activity, as for the SE-HYL1/CPL1 rows from PMID:23141542 [PMID:29982637 "After IP, both DCL1 and SE were detected in the GFP-SMA1 precipitates but not in the GFP precipitates"].
- Source defects recorded for the TAIR ISS rows GO:0003700 (PMID:11118137) and GO:0003677 (PMID:11402159), both without With/From, and for part_of GO:0005846 nuclear cap binding complex (PMID:24137006), which should be enables GO:0140262.
