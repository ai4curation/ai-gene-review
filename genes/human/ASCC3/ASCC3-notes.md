# ASCC3 review notes

## Summary

Automated deep research status: `just deep-research-falcon human ASCC3 --fallback perplexity-lite` was run for this review. Falcon timed out after 600 seconds, and the configured `perplexity-lite` fallback failed with an API quota 401. No provider deep-research artifact was produced, so this review uses the cached UniProt, GOA, Reactome, and primary publication files plus the manual notes below.

ASCC3 is a large ATP-dependent SF2 helicase with two well-supported functional contexts. In the nucleus, it is the catalytic helicase subunit of the ASCC-ALKBH3 DNA dealkylation repair complex. Dango et al. show that ASCC3 unwinds DNA to provide the single-stranded substrate used by ALKBH3 for repair [PMID:22055184 "ASCC3 unwinds DNA to generate the single-stranded substrate needed for ALKBH3-mediated DNA repair"]. Brickner et al. further show alkylation-specific recruitment of ASCC3 to nuclear repair foci [PMID:29144457 "Endogenous ASCC3 formed nuclear foci upon treatment of U2OS cells with the alkylating agent"].

In the cytosol, ASCC3 is the hRQT/RQT2 ATPase subunit of the ribosome quality control trigger complex. Hashimoto et al. define hRQT as ASCC3, ASCC2, and TRIP4 [PMID:32099016 "The hRQT complex is composed of ASCC3, ASCC2, and TRIP4"], and Juszkiewicz et al. show that ASCC acts on ubiquitinated collided ribosomes to disassemble the lead ribosome [PMID:32579943 "ASCC acts on ubiquitinated collided ribosomes to selectively disassemble the lead ribosome"]. Narita et al. refine this as K63-uS10-dependent hRQT-mediated subunit dissociation [PMID:36302773 "the trimeric hRQT complex-mediated subunit dissociation"].

## PN projection

The PN workbook places ASCC3 under `Translation > Cytosolic translation > Ribosome-associated QC > Ribosomal rescue` with UniProt ID Q8N3C0 and synonym RQT2. The local projection report maps this path to two GO targets: `GO:0072344 rescue of stalled cytosolic ribosome`, which is already in GOA, and the broader `GO:0006515 protein quality control for misfolded or incompletely synthesized proteins`, listed as new to GOA.

Conservative decision: retain the exact ribosome-rescue/RQC annotations and do not add a new ASCC3 annotation to `GO:0006515`. ASCC3 has direct evidence for splitting K63-ubiquitinated collided ribosomes and thereby initiating RQC, but the existing GOA already captures this more specifically with `GO:0072344`, `GO:0032790`, and `GO:1990116`. The broad PN projection is biologically compatible as an ancestor/context term but would be redundant and less informative as a new gene-level assertion.

## Annotation decisions

- Accept the DNA repair core: `GO:0043138 3'-5' DNA helicase activity`, `GO:0006307 DNA alkylation repair`, nuclear/nucleoplasm/nuclear-speckle locations, and `GO:1990391 DNA repair complex`.
- Accept the RQC core: `GO:0180022 RQC-trigger complex`, `GO:0016887 ATP hydrolysis activity`, `GO:0022626 cytosolic ribosome`, `GO:0032790 ribosome disassembly`, `GO:0072344 rescue of stalled cytosolic ribosome`, and `GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process`.
- Treat generic binding annotations conservatively. `protein binding` rows are interaction evidence but not informative molecular-function curation. Broad nucleic-acid/helicase terms should defer to the specific DNA helicase/ATPase/RQT annotations.
- Remove the `DNA replication` annotation: the cited ASCC1/ASCC damage-response paper supports alkylation repair-complex regulation, not a general DNA replication process for ASCC3.
- Remove the high-throughput `membrane` localization: ASCC3 is a soluble nuclear/cytosolic protein with no transmembrane-domain basis, and stronger curated evidence places it in ASCC/hRQT contexts.
