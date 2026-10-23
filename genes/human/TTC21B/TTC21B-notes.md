# TTC21B (IFT139/THM1) notes

## Summary
- Distal IFT-A subunit, dispensable for assembly, essential for retrograde IFT: [PMID:27932497 "IFT139 is dispensable for IFT-A assembly but essential for retrograde trafficking of IFT-A, IFT-B, and GPCRs"]; [PMID:27932497 "IFT139-KO cells showed the accumulation of IFT-A, IFT-B, and GPCRs, including Smoothened and GPR161, at the bulged ciliary tips"]
- Attachment: [PMID:27932497 "IFT122 interacted robustly with the IFT43–IFT121 dimer (lane 5), through which it indirectly interacted with IFT139 (lane 8)."]
- Hedgehog: negative modulator (UniProt, by similarity to mouse alien/Thm1).
- Disease: SRTD4, NPHP12; modifier allele across ciliopathies (UniProt).

## Curation decisions
- chromatin binding (IEA from mouse): REMOVE, no biological basis.
- protein binding with IFT122 isoform: REMOVE.
- regulation of transcription by RNA pol II (IMP, PMID:22302990, BBS/RNF2 paper; abstract-only): UNDECIDED — cannot see how TTC21B was assayed; any effect would be indirect.
- regulation of gene expression (ARBA): MARK_AS_OVER_ANNOTATED.
- cilium assembly NAS: KEEP_AS_NON_CORE (IFT139 KO cells still form cilia, with bulged tips).
- regulation of intraciliary retrograde transport (IMP): MODIFY to intraciliary retrograde transport (IFT139 is part of the machinery, not a regulator of it).

## HPA cilium atlas vs module role
- HPA v25: Primary cilium (Approved), Basal body (Approved), Centriolar satellite (Approved).
- Module: IFT-A subunit; retrograde IFT; cargo adaptor; non-motile cilium.
- Assessment: consistent. The ciliary and basal-body calls fit an IFT-A subunit. The centriolar-satellite call is not explained by known function; satellites may act as a staging pool (WDR35 loss affects centriolar satellite organization, PMID:27806291). core_functions focus on retrograde IFT, which matches the module. For TTC21B, the "cargo adaptor" label fits less well than for the IFT-A core, because TULP3 docks on the IFT122/IFT140/IFT144 core rather than on IFT139.

## Deep research
See below.
Falcon deep research succeeded (TTC21B-deep-research-falcon.md). Points used:
- [file:human/TTC21B/TTC21B-deep-research-falcon.md "IFT-A can still be purified without IFT139"]. This is consistent with Hirano 2017.
- The deep research reports that TULP3 contacts IFT-A through IFT122/IFT140 and that IFT139 is not required for that interface. This supports treating TTC21B as a retrograde/train-organizing subunit rather than a direct cargo adaptor.
