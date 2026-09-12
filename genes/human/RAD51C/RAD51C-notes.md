# RAD51C (O43502) — review notes

Human RAD51C / RAD51L2 / R51H3 / FANCO. RAD51 paralog. 376 aa, chr17q. RecA family, RAD51 subfamily (UniProt SIMILARITY).

## Core biology / provenance

- Only paralog shared by BOTH complexes: BCDX2 (RAD51B-RAD51C-RAD51D-XRCC2) and CX3 (RAD51C-XRCC3).
  [PMID:11751635 "the five paralogs exist in two distinct complexes in human cells: one contains RAD51B, RAD51C, RAD51D, and XRCC2 (defined as BCDX2), whereas the other consists of RAD51C with XRCC3"]
  [PMID:12966089 "These RAD51-like proteins form two different complexes, but only the RAD51L2 (RAD51C) protein is a part of both complexes."]

- BCDX2 binds ssDNA, ss gaps, nicks (early pre-RAD51 role):
  [PMID:11751635 "BCDX2 binds single-stranded DNA and single-stranded gaps in duplex DNA, in accord with the proposal that the paralogs play an early (pre-RAD51) role in recombinational repair. Moreover, BCDX2 complex binds specifically to nicks in duplex DNA."]

- Both complexes bind Holliday junctions and replication forks with high specificity; ring-shaped (four-way junction DNA binding; located at forks/junctions):
  [PMID:20207730 "We show that both complexes bind with exceptionally high specificity to the DNA junctions with little binding observed elsewhere on the DNAs."]
  [PMID:20207730 "revealed a multimeric ring structure whose subunits are arranged into a flat disc around a central channel"]

- BCDX2 = RAD51-filament mediator via coupled ATPases (cryo-EM, single molecule); RAD51 filament = supramolecular fiber:
  [PMID:37344587 "BCDX2 stimulates the nucleation and extension of RAD51 filaments-which are essential for recombinational DNA repair-in reactions that depend on the coupled ATPase activities of RAD51B and RAD51C"]
  [PMID:37344587 "BCDX2 promotes RAD51 filament nucleation and extension, in events dependent upon BCDX2′s high-affinity ssDNA binding state induced by the coupled RAD51B and RAD51C ATPases."]

- BCDX2 vs CX3 act at different HR stages:
  [PMID:23149936 "In response to DNA damage, the BCDX2 complex acts downstream of BRCA2 recruitment but upstream of Rad51 recruitment. In contrast, the CX3 complex acts downstream of Rad51 recruitment"]

- HJ processing / branch migration & resolution (RAD51C/CX3, late HR). NOTE: RAD51C itself has no nuclease domain; the resolvase activity lost on RAD51C depletion is now attributed to GEN1 — RAD51C contributes to processing but is not itself an endonuclease:
  [PMID:14716019 "extracts from cells carrying mutations in the recombination/repair genes RAD51C or XRCC3 have reduced levels of HJ resolvase activity ... depletion of RAD51C ... caused a loss of branch migration and resolution activity"]
  [PMID:23108668 "XRCC3 functions jointly with GEN1 later in the pathway at the stage of Holliday junction resolution."]

- Early + late function; recruitment requires ATM/NBS1/RPA; required for CHK2 activation (checkpoint signaling):
  [PMID:19451272 "RAD51C recruitment depends on ataxia telangiectasia mutated, NBS1, and replication protein A, indicating it functions after DNA end resection but before RAD51 assembly."]
  [PMID:19451272 "RAD51C is required for activation of the checkpoint kinase CHK2 and cell cycle arrest in response to DNA damage"]

- Gene conversion / HR-mediated DSB repair; nuclear localization; ATP-binding domain required:
  [PMID:12966089 "non-conservative mutation of the putative ATP-binding domain severely reduces its function"]
  [PMID:12966089 "a RAD51L2-deficient cell line was found to have significantly reduced homology-directed repair of a DNA double-strand break by gene conversion"]
  [PMID:12966089 "the protein is localized to the nucleus ... provisionally identify a C-terminal domain that acts as a nuclear localization signal"]

- Replication fork protection & restart (ATP-hydrolysis dependent); FANCO/BROVCA patient mutations fail to protect forks:
  [PMID:26354865 "RAD51C and XRCC3 promote the restart of stalled replication in an ATP hydrolysis dependent manner by disengaging RAD51 and other RAD51 paralogs from the halted forks"]
  [PMID:26354865 "RAD51 paralogs prevent degradation of stalled forks and promote the restart of halted replication to avoid replication fork collapse"]

- Mitochondrial genome maintenance (Rad51/Rad51C/Xrcc3 in mitochondria; mtDNA copy number):
  [PMID:20413593 "Rad51 and the related HR proteins Rad51C and Xrcc3 exist in human mitochondria ... Depletion of Rad51, Rad51C, or Xrcc3 results in a dramatic decrease in mtDNA copy number"]

- Regulates Rad51 stability (cytoplasmic/perinuclear pools; ubiquitin-mediated proteolysis of Rad51):
  [PMID:16215984 "we are able to detect endogenous Rad51C and Xrcc3 in human cells ... Rad51C plays an important role in regulating this [Rad51 ubiquitin-proteasome degradation] process"]

- Mitotic protection: RAD51B/RAD51C depletion → G2/M arrest; paralogs protect against mitotic defects/aneuploidy:
  [PMID:23108668 "inhibition of RAD51B or RAD51C induces G2/M cell cycle arrest in HeLa cells"]

- PALB2-scaffolded HR complex (PALB2-BRCA2-RAD51C-RAD51):
  [PMID:24141787 "RAD51C is part of a novel protein complex that contains PALB2 and BRCA2"]

- SWSAP1 interaction (HR repair):
  [PMID:21965664 "hSWS1·SWSAP1 is an evolutionarily conserved complex required for efficient homologous recombination repair"]

## Disease (UniProt)
- FANCO (Fanconi anemia complementation group O), biallelic; MIM:613390. His-258 variant characterized [PMID:20400963, PMID:24141787].
- BROVCA3 (familial breast-ovarian cancer 3), monoallelic; MIM:613399 [PMID:20400964, PMID:21990120, PMID:24141787].

## Structure/features (UniProt)
- ATP BINDING 125..132 (Walker A). MUTAGEN K131A abolishes function/HJ resolution. Phospho-Ser20. NLS motif 366..370.
- 7 cryo-EM structures (BCDX2). RecA_ATP-bd IPR020588; Rad51_C IPR013632; PANTHER PTHR46239 RAD51C.

## Curation decisions summary
- protein binding (GO:0005515, IPI ×15): MARK_AS_OVER_ANNOTATED (uninformative per guidelines; real interactors captured in complexes/core functions).
- crossover junction DNA endonuclease activity (GO:0008821, contributes_to, IBA+IMP): MARK_AS_OVER_ANNOTATED — RAD51C is a RecA-fold ATPase mediator, not a nuclease; resolvase activity reassigned to GEN1.
- Meiotic terms (GO:0000707, GO:0007131), telomere (GO:0000722), sister chromatid cohesion (GO:0007062), G2/M (GO:0010971), mitochondrion, perinuclear: KEEP_AS_NON_CORE.
- Core: HR mediator / RAD51 filament assembly (BCDX2), fork protection/restart, junction binding + late HR (CX3).
