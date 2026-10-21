# EREG (O14944) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein and localization

Epiregulin is made as proepiregulin, a type I single-pass membrane precursor (signal
1-29, chain 30-169, transmembrane 120-140) whose EGF-like domain (64-104) lies in the
extracellular segment; the mature chain 63-108 is shed as a soluble growth factor.
[PMID:9337852 "The human epiregulin gene encoded a 163-residue putative transmembrane precursor containing an EGF-like domain in the internal segment"]
[PMID:9337852 "Recombinant expression in mammalian cells also showed that human epiregulin was secreted as a soluble form"]
UniProt records both locations, by molecule.
[file:human/EREG/EREG-uniprot.txt "SUBCELLULAR LOCATION: [Epiregulin]: Secreted, extracellular space"]
[file:human/EREG/EREG-uniprot.txt "SUBCELLULAR LOCATION: [Proepiregulin]: Cell membrane"]

Localization conclusion: secreted/extracellular for the mature ligand (the dominant,
core location, 89 annotation rows), plus plasma membrane for the uncleaved precursor
with the EGF domain extracellular. The clathrin-coated-vesicle rows reflect ligand being
carried in with the internalising receptor and are kept as non-core.

## Function

[PMID:9419975 "Epiregulin binds to epidermal growth factor receptor and ErbB-4 and induces tyrosine phosphorylation of epidermal growth factor receptor, ErbB-2, ErbB-3 and ErbB-4."]
[PMID:28988771 "Using crystallography and other approaches, we show how the EGFR ligands epiregulin (EREG) and epigen (EPGN) stabilize different dimeric conformations of the EGFR extracellular region."]
[PMID:9556621 "Activation of ErbB4 by the bifunctional epidermal growth factor family hormone epiregulin is regulated by ErbB2."]
[PMID:10681561 "Epiregulin stimulated human keratinocyte proliferation under both subconfluent and confluent culture conditions in the absence of exogenous EGF family growth factors."]
[PMID:9990076 "Epiregulin is a potent vascular smooth muscle cell-derived mitogen induced by angiotensin II, endothelin-1, and thrombin."]
[PMID:12898511 "Epiregulin is more potent than EGF or TGFalpha in promoting in vitro wound closure due to enhanced ERK/MAPK activation."]

## Review decisions of note

- `GO:0009299 mRNA transcription` (IDA) and `GO:0045892 negative regulation of
  DNA-templated transcription` (IDA) were marked as over-annotations: a secreted ligand
  does not perform nuclear transcription, and the underlying observations are
  transcriptional responses downstream of receptor activation.
- `GO:0019221 cytokine-mediated signaling pathway` was modified to the EGFR signaling
  pathway, which is what the cited experiments show.
- The two `positive regulation of phosphorylation` rows were refined to positive
  regulation of peptidyl-tyrosine phosphorylation.
- Bare protein-binding rows: EGFR rows modified to EGFR binding, the ERBB4 row to
  receptor ligand activity (GO has no ERBB4-binding term), and four high-throughput
  interactome hits (CXCL9, MS4A13, OLFM4, NINJ2) removed.
- Ovarian, immune and cell-type-specific proliferation rows, and the DNA-replication and
  mitotic-division readouts, were kept as non-core.
