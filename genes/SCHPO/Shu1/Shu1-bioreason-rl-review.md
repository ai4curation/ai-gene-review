# BioReason-Pro RL Review: Shu1 (S. pombe)

Source: Shu1-deep-research-bioreason-rl.md

- **Correctness**: 1/5
- **Completeness**: 1/5

## Functional Summary Review

The BioReason functional summary is fundamentally wrong:

> A cytoplasmic ubiquitin ligase in fission yeast that uses a HECT catalytic core to form a transient thioester with ubiquitin and transfer it onto target proteins. By assembling mono- and polyubiquitin on substrates, it modulates proteostasis and signaling pathways that govern protein turnover and pathway routing.

Shu1 is a **GPI-anchored cell surface heme receptor** that enables high-affinity heme acquisition as an iron source during iron starvation. It has nothing to do with ubiquitin ligation, HECT domains, or proteostasis. The curated review, supported by multiple experimental papers (PMID:25733668, PMID:28193844, PMID:29549126), establishes:

- Shu1 binds hemin with micromolar affinity (KD ~2.2 uM) through a cysteine-rich partial CFEM-like motif
- It localizes to the **external side of the plasma membrane** (GPI-anchored), not the cytoplasm
- It undergoes ligand-induced endocytosis to deliver heme to the vacuole
- It works with vacuolar ABC transporter Abc3 for heme assimilation
- Expression is regulated by iron availability through the Fep1 repressor

BioReason assigns a completely incorrect domain (HECT-type zinc finger, InterPro_2001048) that does not match the curated InterPro annotations for Shu1. The sequence provided to BioReason appears to be correct for Shu1 (Q92340), so the domain recognition failure is a BioReason error. The functional summary is entirely disconnected from the actual biology.

The localization is also wrong: BioReason places the protein in the cytoplasm and on internal membranes, while the actual protein is GPI-anchored on the external cell surface and traffics to the vacuolar membrane upon heme binding.

Comparison with interpro2go:

There are no interpro2go (GO_REF:0000002) annotations in the curated review for Shu1. The IEA annotations come from other automated sources (GO_REF:0000043, GO_REF:0000044, GO_REF:0000108, GO_REF:0000120), which correctly identify plasma membrane, vacuole, and membrane localization. BioReason's summary is worse than any of the automated annotations, which at least get some localization aspects right.

## Notes on thinking trace

The thinking trace assigns a "HECT-type zinc finger" domain (InterPro_2001048) to Shu1, which appears to be a domain recognition error. The actual protein is a small GPI-anchored receptor with a cysteine-rich region. The entire downstream reasoning chain collapses because of this initial misidentification.
