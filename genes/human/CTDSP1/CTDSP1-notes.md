# CTDSP1 (human, Q9GZU7) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: CTDSP1 was reviewed as the closest experimentally characterised relative of
the ProtNLM2 benchmark gene human CTDSP2 (O14595). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human CTDSP1 --fallback perplexity-lite` failed: Falcon
(Edison API) returned "Failed to authenticate", and the perplexity-lite fallback
returned HTTP 401 "insufficient_quota". No deep-research file exists. Literature was
gathered instead by a PubMed E-utilities search (`CTDSP1[tiab] OR (SCP1[tiab] AND
phosphatase[tiab])`, 77 hits) and caching the key primary papers with `just fetch-pmid`.

### Evolutionary placement

- PANTHER 19 gene-info service (pantherdb.org/services/oai/pantherdb/geneinfo,
  queried 2026-10-20): CTDSP1 Q9GZU7 = PTHR12210:SF139; CTDSP2 O14595 = PTHR12210:SF187;
  CTDSPL O15194 = PTHR12210:SF43. All three are SCP-clade members of PTHR12210.
- PAINT (interpro/panther/PTHR12210/PTHR12210-paint.tsv): the IBD for GO:0008420 sits
  at PTN000954535, seeded by Q9GZU7 and O14595 only. CTDSP1 also seeds the deeper
  GO:0004721 node PTN000258719. PAINT propagated no BP or CC terms from the SCP node,
  and I treat that as a deliberate decision. GO:0030514 is proposed as a gene-level NEW
  on human experimental evidence and is not transferred.
- Catalytic residues are intact: UniProt ACT_SITE 96 ("4-aspartylphosphate
  intermediate", ECO:0000269 PMID:15304220, PMID:17157258) and 98 (proton donor).

### What is experimentally established in human CTDSP1 (the reference for transfer)

- CTD Ser5 phosphatase (GO:0008420). Recombinant human SCP1 assays [PMID:12721286 "This study describes a family of small CTD phosphatases (SCPs) that preferentially catalyze the dephosphorylation of Ser5 within the consensus repeat."]; crystal structures with phospho-CTD peptides [PMID:17157258]; Asp96 phosphoaspartate mechanism [PMID:15304220; PMID:20222012].
- Repression of Pol II transcription [PMID:12721286 "Expression of SCP1 inhibits activated transcription from a number of promoters, whereas a phosphatase-inactive mutant of SCP1 enhances transcription."]; REST recruitment to RE-1 genes [PMID:15681389 "We show that REST/NRSF recruits SCPs to neuronal genes that contain RE-1 elements, leading to neuronal gene silencing in non-neuronal cells."].
- Smad1 C-terminal phosphatase / BMP attenuation [PMID:16882717 "In human cells, RNAi-mediated depletion of SCP1 and SCP2 increases the extent and duration of Smad1 phosphorylation in response to BMP"]; corroborated in myoblasts [PMID:21239611].
- Smad2/3 linker phosphatase [PMID:17035229]. Not annotated: the downstream consequence (enhanced TGF-beta response) is indirect, so I left it out to be conservative.
- REST degron dephosphorylation and REST stabilization, from two labs [PMID:25197063; PMID:30217818]; PML S518 stabilization [PMID:25293974]. Proposed NEW GO:0050821 protein stabilization.
- Destabilizing dephosphorylation of Twist1 Ser68 [PMID:26975371] and c-Myc Ser62 [PMID:25893300]. Not annotated as a process: the effect depends on the substrate.
- Location: nucleus (IDA, PMID:12721286), nucleoplasm (HPA). One study reports palmitoylated, epitope-tagged SCP1 at the plasma membrane dephosphorylating AKT S473, with more angiogenesis in Ctdsp1-knockout mice [PMID:28440748]. That rests on overexpressed tagged protein in a single study, so it is not annotated and is raised as a question.

### What is NOT established (do not transfer)

- Developmental "anti-neural" phenotypes (chick spinal cord, P19 differentiation;
  PMID:17403776, PMID:15681389) are downstream organismal or cellular outcomes of REST
  co-repression. They are not annotated as neuron differentiation process terms.
- Exosome (HDA, PMID:23533145): a single proteomic detection, marked over-annotated.
- 41 bare protein-binding IPI rows: 40 removed under the GO:0005515 policy. The SMAD1 row
  was modified to GO:0004722 because it is an enzyme-substrate pair.

### Actions summary

ACCEPT: GO:0008420 (IBA, IDA, IEA), GO:0004722 (EXP x2, IEA), GO:0006470 (IDA),
nucleus x3, nucleoplasm. MODIFY: GO:0006357 -> GO:0000122; GO:0016791 -> GO:0008420 +
GO:0004722; SMAD1 protein binding -> GO:0004722. MARK_AS_OVER_ANNOTATED: extracellular
exosome. REMOVE: 40 bare protein-binding rows. NEW: GO:0030514 (comparator MTMR4 carries
it, IMP PMID:23150675; PPM1A carries the TGF-beta analogue GO:0030512) and GO:0050821.
