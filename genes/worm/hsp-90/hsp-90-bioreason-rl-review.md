# BioReason-Pro RL Review: hsp-90 (C. elegans)

Source: hsp-90-deep-research-bioreason-rl.md

- **Correctness**: 5/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason functional summary states:

> A cytoplasmic ATP-dependent molecular chaperone that uses an N-terminal nucleotide-binding module and a dimerizing C-terminus to drive conformational cycles that fold and stabilize labile client proteins. By coupling ATP binding and hydrolysis to transient recognition of non-native polypeptides, it promotes proteostasis and stress-adaptive signaling in the cytosol, coordinating with co-chaperones to assemble and remodel multiprotein complexes.

This is an accurate and well-constructed summary. All core assertions are supported by the curated review:

- ATP-dependent molecular chaperone: matches GO:0140662 (ATP-dependent protein folding chaperone) and GO:0016887 (ATP hydrolysis activity)
- N-terminal nucleotide-binding module driving conformational cycles: correctly describes the HSP90 N-terminal ATPase domain
- Dimerizing C-terminus: accurate for HSP90 architecture
- Folding and stabilizing labile client proteins: matches GO:0006457 (protein folding)
- Cytoplasmic/cytosolic localization: correct
- Coordination with co-chaperones: the curated review explicitly mentions STI-1/Hop, CDC-37, AHA-1, and PPH-5

The thinking trace even correctly hypothesizes interactions with "Hsp70 and its adaptors," "CDC37-like adaptor," and "p23- and Aha1-like co-chaperones" -- all confirmed by the curated review.

Missing aspects for completeness:

- HSP-90 is also known as DAF-21 in C. elegans
- Specific client proteins: kinases, guanylyl cyclases, steroid hormone receptors
- Essential for larval development, chemosensory behavior, dauer formation, germline development
- Role in transcellular chaperone signaling (protection of distant tissues)
- Predominantly expressed in germline under normal conditions, induced body-wide under heat stress via PQM-1

Comparison with interpro2go:

The interpro2go annotations (GO_REF:0000002) assign GO:0006457 (protein folding), GO:0016887 (ATP hydrolysis activity), GO:0051082 (unfolded protein binding, proposed for obsoletion), and GO:0140662 (ATP-dependent protein folding chaperone). BioReason's summary accurately captures all of these in mechanistic prose. For HSP-90, the domain architecture is sufficiently diagnostic that interpro2go and BioReason converge on an accurate description. BioReason adds value by integrating the tripartite domain organization into a coherent mechanistic narrative.

## Notes on thinking trace

The trace provides an excellent structural dissection of the HSP90 N-terminal ATPase, middle domain, and C-terminal dimerization platform. The co-chaperone hypotheses (Hsp70, CDC37, p23/Aha1) are particularly well-calibrated. This is a case where domain architecture is highly diagnostic and the system performs well.
