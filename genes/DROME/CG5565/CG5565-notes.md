# CG5565 evidence notes

## Identity and evidence

Q9VQ04 is the single 240-residue CG5565-PA product in the current FlyBase record. The complete HAD-family architecture is compatible with the manually transferred PUDP activity; it is not a truncated native isoform.

[PMID:20722631](https://pubmed.ncbi.nlm.nih.gov/20722631/) characterized human HDHD1/PUDP Q08623: purified enzyme hydrolyzed pseudouridine 5′-phosphate with Km 0.3 μM and at least 1000-fold greater catalytic efficiency than the other tested phosphate esters. GOA specifically records manual ortholog transfer from that experimentally characterized protein. The proposed core function is a qualified inference rather than a direct fly assay.

The current PTHR18901 PAINT export places pseudouridine 5′-phosphatase activity at PTN000431252, seeded by human PUDP and corroborated through the UniProt cross-reference for yeast YKL033W-A, while the broad GO:0016791 phosphatase IBA in the CG5565 GOA snapshot cites PTN000431251. Re-fetching PTHR18901 with Q9VQ04 explicitly included did not put PTN000431251 into the local slice, so the slice is insufficient to call that GOA source stale. The GOA seed union is instead consistent with a legitimate broad phosphatase placement above the plant GPP and human/yeast PUDP branches. The broad IBA remains less granular than the existing FlyBase ISS to human PUDP, but direct Drosophila kinetics and PAINT descent from PTN000431252 remain unestablished.

The ProtNLM structural donor Q9V1B3 is a Pyrococcus protein; its glyceraldehyde-3-phosphate statement is itself by similarity to Q58832. Shared structure does not determine substrate specificity. Conversely the existence of a better-supported physiological substrate cannot refute the explicitly in vitro side-activity claim, which remains UNC. The source is a function paragraph only, with no original GO predictions.

## Research assessment and sequence check

The Falcon report was inspected. Its discussion of HAD substrate ambiguity is relevant, but its “no specific reaction without biochemical testing” recommendation misses the current FlyBase PUDP ortholog transfer to experimentally characterized human Q08623. A full-length comparison with that human protein retains both catalytic Asp positions and covers 226 of 228 human residues; the original archaeal structural donor is substantially less similar in sequence. This supports accepting the qualified PUDP transfer while keeping the separate in vitro substrate claim unresolved. The comparison alone does not establish orthology or prove a particular substrate. Inputs, script, alignments, controls and [RESULTS.md](CG5565-bioinformatics/RESULTS.md) are retained.
