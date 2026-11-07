# PP_3995 curation notes

## Functional assignment

PP_3995/Q88FT7 is assigned as the structural TusB-family subunit of TusBCD by
the specific IPR007215 and TIGR03011 family records and its position in the
contiguous PP_3993-PP_3996 `tusD-tusC-tusB-tusE` locus.
[file:PSEPK/PP_3995/PP_3995-uniprot.txt "DR   InterPro; IPR007215;
Sulphur_relay_TusB/DsrH."] The machine-generated UniProt recommended name is
not used as the evidentiary anchor.

The complex-level assignment is transferred from the *E. coli* TusBCD
structure; no direct KT2440 complex study was identified. [PMID:16472754 "Here,
we solved the 2.15 angstroms crystal structure of the E. coli TusBCD complex, a
sulfur transfer mediator, forming a heterohexamer composed of a dimer of the
heterotrimer."] The complete *E. coli* relay was also reconstituted with TusBCD.
[PMID:16387657 "Efficient 2-thiouridine formation in vitro was reconstituted
with recombinant TusA, a TusBCD complex, TusE, and previously identified IscS
and MnmA."]


## 2026-11-07 — complete source-aware review

All original rows and historical NEW proposals are retained in their original order and source payload. The review now distinguishes target-specific family/curated-site inference from E. coli experiments; no KT2440 assay is invented. The soluble location is inferred from the conserved reaction/complex context, not ARBA-only annotation. Broad true rows are refined where ontology ancestry supports it; covalent sulfur-carrier and sulfurtransferase terms are not treated as a false hierarchy.

TusB-family structural participant in the inferred KT2440 TusBCD complex that supports sulfur delivery to the tRNA U34 thiolation pathway.

Evidence and exact source/access limits are in [the consultation](../../../analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/evidence.md). A reproducible frozen-sequence alignment independently checks conserved sites rather than quoting generated provider claims. Existing OpenScientist material is discovery provenance. A normal Falcon attempt for this gene failed HTTP403 authentication; the actual log is retained at `analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/falcon-PP_3995.log`. No provider report was fabricated.

The earlier notes are preserved as historical text. Where they describe C5 modification as obligatorily downstream, assert a directly established KT2440 reaction or operon expression, or equate carrier with a catalytic GO descendant, this append and the current review supersede that wording. No NEW annotation was added to fill a core-coverage warning.
