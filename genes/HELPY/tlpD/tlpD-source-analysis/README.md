# TlpD source and sequence audit

## Provenance and reproducibility

Retrieved 2026-11-06 through the public UniProt REST service:

- `SS1-A0A1U9IUC7-record.json`: https://rest.uniprot.org/uniprotkb/A0A1U9IUC7.json
- `UPI000980CA3C.json`: https://rest.uniprot.org/uniparc/UPI000980CA3C.json

These are unmodified downloaded JSON responses. The first record is inactive because it is no longer part of a reference proteome, and explicitly links the archived sequence UPI000980CA3C. This database retirement does not mean that the SS1 protein is biologically absent. PMID:31465435 names A0A1U9IUC7 as the SS1 TlpD sequence used for recombinant experiments.

Run `python3 genes/HELPY/tlpD/tlpD-source-analysis/compare_records.py` from the repository root. The script reads the frozen target UniProt flat file and archived sequence, reports every positional difference and writes `sequence-comparison.json`. No remote retrieval or external package is required. Both sequences are 433 residues, with 426 identical positions (98.383%). H315, C340, H368 and H372 are conserved. Seven substitutions are explicitly listed. These are closely related strain orthologs, not identical sequences; HOCl-sensing biochemistry is transferred to 26695 by inference.

## Primary-source attribution

- PMID:31465435, full cached text: recombinant TlpD is from SS1, CheW from SS1, and CheA from G27, expressed with N-terminal His tags in E. coli. Native HOCl attraction was assayed in G27 and PMSS1. HOCl oxidizes the conserved C340 zinc ligand, inhibiting CheA stimulation; the in vitro assay did not support direct zinc, pH, hydrogen peroxide or superoxide sensing. These facts do not exclude indirect responses to other stress conditions in vivo.
- PMID:21725005, normal fetch abstract-only; publisher full text inspected at https://journals.asm.org/doi/10.1128/jb.05140-11 (Materials and Methods, Protein sequence analysis; Cloning and mutagenesis). The sequence-analysis target is explicitly strain 26695 locus HP0599, also called hlyB/hylB. Recombinant zinc-binding experiments use SS1/J99, not 26695. Thus the legacy HylB name is an alias of the chemoreceptor, not evidence for hemolysin secretion.
- PMID:18245281, normal fetch abstract-only; publisher full text inspected at https://journals.asm.org/doi/full/10.1128/jb.01940-07 (Construction of chemotaxis sensor mutants; Construction of a tlpD-V5 shuttle plasmid). HP0599 DNA was cloned from KE26695. A KE26695-derived TlpD-V5 fusion was expressed in trans in an N6 tlpD mutant; it rescued behavior. This supports receptor function of a 26695-derived construct without making the experiment a native untagged 26695 assay. Localization included cytoplasmic and peripheral pools. The energy-dependent behavioral phenotype does not by itself identify the molecule sensed directly.
- PMID:27002127 remains abstract-only after a normal forced fetch. The abstract explicitly reports membrane association dependent on other chemotaxis proteins, autonomous polar signaling by TlpD, and oxidative-stress responses. Its assertion of membrane association is compatible with a cytoplasmic receptor that lacks transmembrane segments.
- PMID:41660828, full text: experiments use G27 and tagged ectopic constructs. Loss of the last 45 residues disrupts polar localization and signaling. Its discussion labels AcxC with HP0599, a locus mismatch: HP0599 is TlpD. That sentence is not used as identity or interaction evidence here.
- PMID:41648481 is a 2026 preprint, not an established peer-reviewed target assay. Its structural protein is from J99. It is contextual evidence only; neither a direct 26695 structure nor a new ligand assay is claimed.

## Interpretation

O25321/HP_0599 is TlpD, a cytoplasmic chemoreceptor with MCP signaling and CZB domains. The raw UniProt name “Hemolysin secretion protein (HylB)” is inconsistent with the locus-resolved literature. Preserve the source file and report its name as a source defect. TlpD's physiological signaling can occur in polar, peripheral membrane-associated complexes; lack of a transmembrane helix does not negate membrane association. The full-text review PMID:38048436 reports that H. pylori lacks the canonical CheR/CheB methylation adaptation pair, so the historical domain label “methyl-accepting” does not establish receptor methylation in this organism.
