# Manual research synthesis: NCU07379 (V5IQW8)

This report was researched manually on 2026-09-09 after provider failure. It is not a Falcon or Perplexity report. Sources inspected include the complete current UniProt sequence/features, the seeded GO annotations, the preserved prediction/donor records where applicable, and the primary publications cited below.

## Biological synthesis

NCU07379 encodes an AP-1-like bZIP transcription factor related to fungal Yap1 proteins. Conserved family placement supports binding to transcriptional regulatory DNA and activation of RNA polymerase II transcription in the nucleus. Its physiological target genes and regulatory inputs in Neurospora crassa remain incompletely characterized.

## Direct and comparative evidence

- file:NEUCR/NCU07379/NCU07379-uniprot.txt: “DR   PANTHER; PTHR40621:SF6; AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED; 1.”
- PMID:2542125: “Disruption of the YAP1 gene demonstrates this gene is not essential but is required for AP-1 recognition element-dependent transcriptional activation.”

## Subfamily inference and limits

The sequence-based PANTHER assignment PTHR40621:SF6 is AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED and InterPro identifies AP-1-like/bZIP. PMID:2542125 establishes element-dependent transcriptional activation by fungal Yap1. This supports the conserved molecular property in combination with the PAINT assertion, not a direct assay on NCU07379. Search by exact NCU locus recovered no decisive target-specific DNA-binding or localization experiment. A polysaccharide transcriptome study (DOI:10.1111/mmi.12459) lists NCU07379 among mostly putative TFs; expression in a cluster alone does not establish an essential pectin-response function. No nap-1 synonym or oxidative-stress pathway is assigned without verified mapping.

## Annotation implications

- GO:0000976: ACCEPT. The target is placed in the fungal AP-1/Yap1-related bZIP subfamily. Characterized yeast Yap1 binds a cis-regulatory sequence and is required for element-dependent transcriptional activation; the curated PAINT inference supports conservation of this regulatory activity without specifying the Neurospora target genes.
- GO:0001228: ACCEPT. The target is placed in the fungal AP-1/Yap1-related bZIP subfamily. Characterized yeast Yap1 binds a cis-regulatory sequence and is required for element-dependent transcriptional activation; the curated PAINT inference supports conservation of this regulatory activity without specifying the Neurospora target genes.
- GO:0003700: ACCEPT. The target is placed in the fungal AP-1/Yap1-related bZIP subfamily. Characterized yeast Yap1 binds a cis-regulatory sequence and is required for element-dependent transcriptional activation; the curated PAINT inference supports conservation of this regulatory activity without specifying the Neurospora target genes.
- GO:0006355: ACCEPT. The target is placed in the fungal AP-1/Yap1-related bZIP subfamily. Characterized yeast Yap1 binds a cis-regulatory sequence and is required for element-dependent transcriptional activation; the curated PAINT inference supports conservation of this regulatory activity without specifying the Neurospora target genes.
- GO:0045944: ACCEPT. The target is placed in the fungal AP-1/Yap1-related bZIP subfamily. Characterized yeast Yap1 binds a cis-regulatory sequence and is required for element-dependent transcriptional activation; the curated PAINT inference supports conservation of this regulatory activity without specifying the Neurospora target genes.
- GO:0005634: ACCEPT. A nuclear site of action follows from the supported DNA-binding transcription factor function and bZIP-family placement. Constitutive nuclear accumulation or the stimulus-dependent import/export mechanism is not established.
- GO:0090575: ACCEPT. A DNA-binding bZIP transcription activator acts in a transcription regulator assembly, and PAINT supports inheritance of this complex association. The annotation does not identify a specific heterodimer partner or imply membership in core RNA polymerase II.
