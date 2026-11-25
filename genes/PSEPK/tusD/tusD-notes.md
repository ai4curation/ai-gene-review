# tusD curation notes

## Functional assignment

PP_3993/Q88FT9 is the TusD-family catalytic sulfur-bearing subunit in the
contiguous `tusD-tusC-tusB-tusE` locus. The target retains the
Cys78-equivalent residue identified by the OpenScientist sequence analysis.
[file:projects/P_PUTIDA/deep-research/PSEPK__bacterial-mnma-trna-wobble-uridine-thiolation-sulfur-relay__ppu04122-deep-research-openscientist.md
"**Catalytic Cys78-equivalent conserved**"]

The orthologous *E. coli* structure establishes TusBCD as a heterohexamer and
mutagenesis identifies TusD Cys78 as the sulfur-transfer residue.
[PMID:16472754 "In vivo mutant analyses revealed that only Cys78, in the TusD
subunit, participates in sulfur transfer during the s2U modification process."]
Accordingly, broad sulfurtransferase activity is retained as non-core rather
than rejected; sulfur carrier activity is the more specific molecular-function
summary.

No direct biochemical characterization of KT2440 TusD was identified, so the
species assignment remains a conservative family-, residue-, and locus-based
transfer from the enterobacterial mechanism. [PMID:16387657 "TusE binds TusBCD
complex and stimulates sulfur transfer from TusA to TusD."]


## 2026-11-07 — complete source-aware review

All original rows and historical NEW proposals are retained in their original order and source payload. The review now distinguishes target-specific family/curated-site inference from E. coli experiments; no KT2440 assay is invented. The soluble location is inferred from the conserved reaction/complex context, not ARBA-only annotation. Broad true rows are refined where ontology ancestry supports it; covalent sulfur-carrier and sulfurtransferase terms are not treated as a false hierarchy.

Covalent sulfur carriage by the TusD subunit within the inferred KT2440 TusBCD assembly, supported by the homologous active site and complex-mediated transfer.

Evidence and exact source/access limits are in [the consultation](../../../analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/evidence.md). A reproducible frozen-sequence alignment independently checks conserved sites rather than quoting generated provider claims. Existing OpenScientist material is discovery provenance. A normal Falcon attempt for this gene failed HTTP403 authentication; the actual log is retained at `analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/falcon-tusD.log`. No provider report was fabricated.

The earlier notes are preserved as historical text. Where they describe C5 modification as obligatorily downstream, assert a directly established KT2440 reaction or operon expression, or equate carrier with a catalytic GO descendant, this append and the current review supersede that wording. No NEW annotation was added to fill a core-coverage warning.
