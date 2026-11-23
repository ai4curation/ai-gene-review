# tusA curation notes

## Target selection

PP_2116/Q88L21 is the relay-relevant TusA paralog. The OpenScientist analysis
reports 57.5% identity to *E. coli* TusA and the specific IPR022931
`Sulphur_carrier_TusA` signature; PP_1233 has only the broader TusA-like
signature and remains outside this module. [file:projects/P_PUTIDA/deep-research/PSEPK__bacterial-mnma-trna-wobble-uridine-thiolation-sulfur-relay__ppu04122-deep-research-openscientist.md
"it uniquely carries the specific InterPro **IPR022931
(Sulphur_carrier_TusA)**"]

## Evidence boundary

The specific KT2440 assignment is based on family discrimination and conserved
sequence, while the mechanistic evidence comes from *E. coli*. The reconstituted
system directly transfers persulfide sulfur from IscS to TusA.
[PMID:16387657 "IscS transfers the persulfide sulfur to TusA."] TusA can also
serve broader physiological roles, so the review does not claim exclusivity to
this relay. [PMID:33526615 "TusA, however, is a versatile protein that is also
involved in numerous other cellular pathways."]


## 2026-11-07 — complete source-aware review

All original rows and historical NEW proposals are retained in their original order and source payload. The review now distinguishes target-specific family/curated-site inference from E. coli experiments; no KT2440 assay is invented. The soluble location is inferred from the conserved reaction/complex context, not ARBA-only annotation. Broad true rows are refined where ontology ancestry supports it; covalent sulfur-carrier and sulfurtransferase terms are not treated as a false hierarchy.

Conserved cysteine-dependent sulfur carriage from IscS into the Tus relay, inferred for KT2440 without excluding other sulfur acceptor pathways.

Evidence and exact source/access limits are in [the consultation](../../../analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/evidence.md). A reproducible frozen-sequence alignment independently checks conserved sites rather than quoting generated provider claims. Existing OpenScientist material is discovery provenance. A normal Falcon attempt for this gene failed HTTP403 authentication; the actual log is retained at `analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/falcon-tusA.log`. No provider report was fabricated.

The earlier notes are preserved as historical text. Where they describe C5 modification as obligatorily downstream, assert a directly established KT2440 reaction or operon expression, or equate carrier with a catalytic GO descendant, this append and the current review supersede that wording. No NEW annotation was added to fill a core-coverage warning.
