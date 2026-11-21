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

## 2026-11-04: DeepTMHMM2 S20 topology audit

Source: [DeepTMHMM2 v1](https://doi.org/10.64898/2026.08.24.746435), supplied workbook `media-1.xlsx`, S20 row 17, O15270. Author evidence category: **Element**. These are the authors' predictions, with one-based inclusive coordinates:

`Cytoplasmic(1-71); interfacial(72-87); Cytoplasmic(88-562)`

**Assessment: Correct topology from human structure.** The human SPT structure (PMID:33558761) describes an amphipathic SPTLC2 helix and ssSPTa-mediated anchoring and says SPTLC2 appears to lack transmembrane regions. Replace the single-pass description, retain ER membrane and cytoplasmic-face annotations, and record the conflicting inherited UniProt description as a source defect. The earlier local benchmark reproduces S20 IF72-87; it corroborates the mechanism but does not supply the experimental evidence.

The complete source row, workbook hash and cross-gene decisions are retained in [the audit](../../../projects/DEEPTMHMM2.md). Membrane-contact geometry is considered separately from organelle localization and molecular function; no new function/process annotation is derived from this prediction.

## 2026-11-05: expanded local DeepTMHMM2 panel

SPTLC2 was rerun with 30 other human proteins, including its membrane-spanning
partner SPTLC1. Both API repeats and the unmodified CLI reproduce SPTLC2 IF72–87,
with no transmembrane segment or membrane-type assignment. SPTLC1 is assigned
one TM segment and ER membrane, although its predicted segment is short (26–36).
The expanded run confirms reproducibility, not independent biological evidence;
the curated SPTLC2 interpretation remains grounded in the human structure.
See [the panel report](SPTLC2-bioinformatics/deeptmhmm2-benchmark/panel-2026-11-05/RESULTS.md)
for all 31 outputs, CPU costs and the API/CLI precision diagnostic.
