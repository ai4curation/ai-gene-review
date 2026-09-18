# sen15 evidence notes

Sen15 is a small, conserved noncatalytic subunit of the heterotetrameric tRNA-splicing endonuclease complex. Together with Sen2, Sen34 and Sen54 it supports recognition and excision of introns from precursor tRNAs before the cleaved exons are ligated. The catalytic splice-site cleavage centers reside in Sen2 and Sen34. Nuclear and cytosolic pools have been reported in fission yeast localization screens.

## Identity and prediction provenance

PomBase primary symbol sen15, locus SPAC959.10, current UniProt Q7LKV3. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:9200603 The yeast tRNA splicing endonuclease: a tetrameric enzyme with two active site subunits homologous to the archaeal tRNA endonucleases.] "Our results demonstrate that the eucaryal tRNA splicing endonuclease contains two functionally independent active sites for cleavage of the 5' and 3' splice sites, encoded by SEN2 and SEN34, respectively."
- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."

## Evidence limits and adjudication

- GO:0003676 (UNDECIDED): The Sen15 subunit supports an RNA-processing complex, but specific RNA contacts by the target or conserved contacts in a characterized Sen15 ortholog have not been established in the primary evidence inspected here. Complex membership alone does not resolve whether this particular subunit binds nucleic acid. Binding within an assembled complex would be sufficient; an isolated-subunit assay is not required.
- GO:0005634 (KEEP_AS_NON_CORE): Retain the PomBase localization observation from the fission yeast tagged-ORFeome screen. The accessible abstract documents the assay but not the individual localization image; the screen is not sufficient to identify which detected pool executes tRNA cleavage.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

## Provider report appraisal

The Falcon report supports a noncatalytic architecture and highlights human TSEN15 structures lacking detectable direct RNA contacts. Its generic claim that no target localization data exist is incomplete because PomBase retains tagged-ORFeome observations. No compartment was inferred from budding-yeast mitochondrial localization.
