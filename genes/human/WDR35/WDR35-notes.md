# WDR35 (IFT121) notes

## Summary
- IFT-A peripheral subunit [PMID:27932497 "a peripheral subcomplex, composed of IFT43/IFT121/IFT139, where IFT139 is most distally located"]
- Ciliogenesis/localization: [PMID:21473986 "We show that endogenous WDR35 localizes to cilia and centrosomes throughout the developing embryo and that human and mouse fibroblasts lacking the protein fail to produce cilia."]
- COPI-like fold: [PMID:21473986 "WDR35 has strong homology to the COPI coatamers involved in vesicular trafficking"]
- Membrane-protein entry: [PMID:27806291 "Wdr35 is essential for entry of many membrane proteins into the cilium through robust interactions with cargoes and other IFT-A subunits"]; additional roles [PMID:27806291 "Beyond its role in retrograde transport, we show that Wdr35 functions in fusion of Rab8 vesicles at the nascent cilium, protein exit from the cilium, and centriolar satellite organization."]
- Disease: SRTD7, CED2 (UniProt).

## Curation decisions
- 4 protein binding IPI rows (IFT43/IFT122): REMOVE (uninformative; captured by part_of IFT-A).
- All other rows (IFT-A, cilium/axoneme/tip/basal body/centrosome, anterograde and retrograde IFT, cilium assembly, protein localization to cilium, protein carrier contributes_to) ACCEPT.
- Anterograde transport IDA from 40472089: accepted, deferring to curator (same caveat as IFT122).

## HPA cilium atlas vs module role
- HPA v25: WDR35 is not in HPA (no antibody-based localization), so the atlas neither supports nor contradicts the module.
- Module: IFT-A subunit; retrograde IFT; IFT cargo adaptor; non-motile cilium.
- Assessment: consistent with the literature. core_functions = contributes to IFT-A cargo carrier activity (membrane-protein import), retrograde IFT, cilium assembly. Fu et al. show WDR35 is most prominently needed for membrane-protein entry, which supports the module's "cargo adaptor" label more than retrograde transport alone.

## Deep research
See below.
Falcon deep research succeeded (WDR35-deep-research-falcon.md). Points used:
- [file:human/WDR35/WDR35-deep-research-falcon.md "Reintroducing wild-type WDR35 rescued IFT88 retrograde transport and ARL13B entry."]
- WDR35-dependent periciliary vesicle coat (Quidwai et al. 2021, mouse; not cached): the IFT139-IFT121-IFT43 trimer binds phosphatidic acid. This supports the COPI-like-coat question in suggested_questions; no annotation proposed.
