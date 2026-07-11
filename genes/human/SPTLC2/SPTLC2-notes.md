# SPTLC2 (O15270) review notes

## Summary of function

SPTLC2 (serine palmitoyltransferase long chain base subunit 2, EC 2.3.1.50) is the
PLP-binding catalytic subunit of serine palmitoyltransferase (SPT). With SPTLC1 it forms
the catalytic heterodimeric core of the SPT complex, which also contains a small subunit
(SPTSSA or SPTSSB, substrate specificity) and negative regulators (ORMDL1/2/3). SPT
catalyzes the first, committed, and rate-limiting step of de novo sphingolipid
biosynthesis: PLP-dependent condensation of L-serine with palmitoyl-CoA (C16-CoA) to form
3-oxosphinganine (3-ketodihydrosphingosine) + CO2 + CoA, at the cytoplasmic side of the ER
membrane [UniProt O15270; PMID:9363775; PMID:19416851].

- Catalytic lysine K379 forms the Schiff base with the PLP cofactor (N6-(pyridoxal
  phosphate)lysine; UniProt MOD_RES 379; MUTAGEN K379A abolishes activity, PMID:33558762).
- Belongs to class-II PLP-dependent aminotransferase family (AOS synthase class-II).
- Localizes to ER membrane, single-pass membrane protein (By similarity to mouse P97363);
  active on the cytoplasmic side [PMID:19416851 basis of GO:0098554 by curator].

## SPT complex composition and substrate specificity (PMID:19416851)

- SPTLC1 + SPTLC2/SPTLC3 = catalytic core; SPTSSA/SPTSSB confer substrate specificity.
- SPTLC1-SPTLC2-SPTSSA prefers C16-CoA; SPTLC1-SPTLC2-SPTSSB prefers C18-CoA.
- Structures (PMID:33558761, PMID:33558762, PMID:37308477): dimer of heterodimers; ORMDL3
  blocks the substrate tunnel (ceramide-dependent negative feedback).

## Disease

Dominant SPTLC2 missense variants (A182P, R183W, V359M, G382V, I504F) cause hereditary
sensory and autonomic neuropathy type 1C (HSAN1C, MIM:613640). Mechanism: shifted substrate
specificity toward L-alanine/L-glycine, producing neurotoxic 1-deoxysphingolipids
[PMID:20920666; PMID:26573920; PMID:23658386].

## Annotation review decisions

Core MF term present in GOA and current: **GO:0004758 serine C-palmitoyltransferase activity**
(confirmed via OLS; label unchanged). Used verbatim in core_functions.

- All catalytic (GO:0004758), sphingolipid/ceramide/sphingosine biosynthesis, SPT complex,
  and ER membrane annotations ACCEPTED (strongly supported experimentally + IBA + structures).
- `enables` vs `contributes_to` for GO:0004758: catalysis requires the SPTLC1/SPTLC2
  heterodimer, so `contributes_to` (per-molecule contribution to a complex activity) is
  the strictly correct qualifier; both are retained/ACCEPTED as they describe the same
  well-supported catalytic role.
- Three IPI GO:0005515 "protein binding" (all with SPTLC1/O15269) -> MARK_AS_OVER_ANNOTATED
  (bare protein binding is uninformative; the informative capture is part_of SPT complex
  GO:0017059, which is separately annotated). Per policy, not REMOVE.
- GO:0016740 transferase activity (IEA/InterPro) -> too general; MODIFY -> GO:0004758.
- GO:0006665 sphingolipid metabolic process (IEA/UniPathway) -> parent of biosynthetic;
  KEEP_AS_NON_CORE (biosynthetic child is the informative core term, already present).
- GO:0060612 adipose tissue development (ISS/IEA from mouse P97363) -> KEEP_AS_NON_CORE;
  peripheral, By-similarity from mouse, not a core molecular role.
- GO:1904504 positive regulation of lipophagy (IDA, PMID:25332431) -> mouse-liver
  overexpression study; downstream/indirect consequence of elevated de novo sphingolipid
  synthesis, not a direct SPTLC2 function -> KEEP_AS_NON_CORE.
- GO:0006686 sphingomyelin biosynthetic process (IDA, PMID:30242129): that paper is about
  SMS1-GCS complex; SM synthesis is downstream of SPT (SPT makes the ceramide precursor).
  Keep as non-core downstream pathway contribution -> KEEP_AS_NON_CORE.
- GO:0006688 glycosphingolipid biosynthetic process (IDA, PMID:19416851) -> downstream of
  SPT-generated long-chain bases -> KEEP_AS_NON_CORE.
</content>
</invoke>
