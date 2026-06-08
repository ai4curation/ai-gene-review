# HSPB2 (HspB2 / MKBP) research notes

## Identity
- UniProt Q16082 (HSPB2_HUMAN), 182 aa. HGNC:5247. AltName: DMPK-binding protein (MKBP). Small heat-shock protein (HSP20/alpha-crystallin) family; sHSP/ACD domain 55-163.
- Gene head-to-head with CRYAB (alphaB-crystallin) on chr11. Expressed preferentially in skeletal muscle and heart (not lens).

## Function
- ATP-independent small HSP (holdase-type chaperone). Identified as MKBP, binds and activates myotonic dystrophy protein kinase (DMPK) and protects it from heat-induced inactivation.
  [PMID:9490724 "In vitro, MKBP enhances the kinase activity of DMPK and protects it from heat-induced inactivation."]
  [UniProt FUNCTION "May regulate the kinase DMPK." SUBUNIT "Interacts with DMPK; may enhance its kinase activity."]
- Forms its own oligomeric complex in muscle cytosol, separate from the alphaB-crystallin/HSP27 complex; not heat-inducible but redistributes to insoluble fraction under stress.
  [PMID:9490724 "In muscle cytosol, MKBP exists as an oligomeric complex separate from the complex formed by alphaB-crystallin and HSP27." / "The expression of MKBP is not induced by heat shock"]
- Localizes to the Z-membrane of myofibrils and the neuromuscular junction (where DMPK concentrates).
- Cardiac overexpression is cardioprotective in ischemia (reduced infarct size, maintained ATP); has a mitochondrial-leaning "cardiac interactome"; validated client GAPDH via chaperone assays.
  [PMID:26465331 "exhibited ischemic cardioprotection in transgenic overexpressing mice including reduced infarct size and maintenance of ATP levels" / "validated as a potential client protein of HspB2 through chaperone assays"]

## Localization
- Cytoplasm and nucleus (nuclear foci) (IDA, PMID:19464326). HPA nucleoplasm IDA. TAS cytosol (PMID:9490724).

## Interactions
- DMPK (functional, PMID:9490724). CRYAB/alphaB-crystallin (P02511; PMID:23188086, 26465331) — sHSP hetero-association. HSPB8/HSP22 (Q9UJY1; PMID:14594798) — sHSP interaction. BAG3 (O95817; PMID:32296183/33961781) — co-chaperone of sHSP/autophagy. APP (P05067; PMID:32814053). Many HuRI binary hits (PMID:32296183) — mostly uninformative.
- Orchestrator note mentions HSPB3 partner; HSPB2-HSPB3 form a known sHSP complex in muscle (literature), though HSPB3 is not among the cached GOA partners here.

## GO annotation review reasoning
- unfolded protein binding (IBA, GO:0051082) — ACCEPT; core sHSP holdase MF (binds non-native proteins to prevent aggregation). Confirmed by GAPDH client chaperone assay.
- enzyme activator activity (TAS, GO:0008047, PMID:9490724) — ACCEPT/core; specifically enhances DMPK kinase activity (kinase activator).
- protein refolding (IBA, GO:0042026) — sHSPs are holdases, not foldases; they hold substrates for downstream ATP-dependent refolding by HSP70. KEEP_AS_NON_CORE (mislabels mechanism but reflects downstream outcome).
- response to heat (IBA, GO:0009408) — KEEP_AS_NON_CORE; note HSPB2 is NOT heat-inducible, but participates in stress response; family-level term.
- response to unfolded protein (NAS, GO:0006986, PMID:9344664) — ACCEPT/KEEP; stress-response role.
- negative regulation of apoptotic process (IBA, GO:0043066) — KEEP_AS_NON_CORE; sHSP cytoprotective family role; cardioprotection consistent.
- structural constituent of eye lens (IEA InterPro, GO:0005212) — REMOVE/MARK_AS_OVER_ANNOTATED; HSPB2 is explicitly NOT expressed in lens; transferred from alpha-crystallin family.
- nucleus / cytoplasm / cytosol / nucleoplasm — ACCEPT (well supported by IDA).
- protein binding (IPI) — the CRYAB and HSPB8 sHSP interactions could MODIFY to heat shock protein binding (GO:0031072); BAG3 etc; bare Y2H -> KEEP_AS_NON_CORE.

## Core functions
1. ATP-independent holdase chaperone (unfolded protein binding) — sHSP preventing aggregation of client proteins (e.g. GAPDH).
2. DMPK kinase activator / enzyme activator activity — binds and activates DMPK, protecting from heat inactivation.
