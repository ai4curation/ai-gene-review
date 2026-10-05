# vas2 evidence notes

Vas2 (Aps1) is the sigma subunit of the heterotetrameric AP-1 clathrin adaptor complex. It associates with the gamma subunit Apl4 and contributes to assembly and membrane recruitment of AP-1 at the Golgi and endosomal system. The complex sorts membrane-protein cargo into intracellular transport carriers and supports exit of cargo such as the v-SNARE Syb1 from endosomes.

## Identity and prediction provenance

PomBase primary symbol vas2, locus SPAP27G11.06c, current UniProt Q9P7N2. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."
- [PMID:19624755 Deletion mutants of AP-1 adaptin subunits display distinct phenotypes in fission yeast.] "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4, and Apl4 binds Aps1 even in the absence of Apm1 and Apl2. Consistently, the deletion of any subunit generally caused the disassociation of the heterotetrameric complex from endosomes, although some subunits weakly localized to endosomes. In addition, the deletion of individual subunits caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1. Altogether, results suggest that the four subunits are all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from endosomes."

## Evidence limits and adjudication

- GO:0005634 (KEEP_AS_NON_CORE): Retain the reported nuclear signal from the tagged-protein screen as an ancillary localization. It does not establish a nuclear AP-1 cargo-sorting mechanism and is not the principal functional location supported by endosomal trafficking experiments.
- GO:0010496 (REMOVE): GO:0010496 means movement between cells, as verified in QuickGO. The experimentally established Vas2/AP-1 pathway sorts cargo between compartments inside a cell. This ARBA assertion conflates intercellular and intracellular transport and lacks an independent intercellular mechanism.
- GO:0030276 (KEEP_AS_NON_CORE): Retain the curator-mediated orthology transfer for clathrin association in the AP-1 context. The decisive target evidence establishes adaptor-complex assembly; it does not demonstrate that isolated sigma subunit is the principal direct clathrin-binding interface.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

The full original function paragraph and all atomic claims are assessed in [vas2-protnlm-function-review.md](vas2-protnlm-function-review.md).

## Provider report appraisal

The late Falcon report was inspected after the wrapper timeout. It misses the target Aps1 pull-down and deletion experiments in PMID:19624755, so its statement that direct Vas2-binding evidence was not found is incomplete. Target Apl4-Aps1 association and AP-1 exit-transport evidence are prioritized over pathway-only Apm1 observations.
