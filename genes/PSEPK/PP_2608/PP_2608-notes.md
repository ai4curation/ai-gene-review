# PP_2608 (Q88JP1, RifI2) — curation notes

## Why this file exists

The batch's OpenScientist deep-research job for PP_2608 was still `RUNNING` when the
review was written, so unlike its siblings in this batch there is no
`PP_2608-deep-research-asta.md`. This file records the provenance actually used, so
the review is self-documenting if that job lands late.

## Sources used

1. `genes/PSEPK/PP_2608/PP_2608-goa.tsv` — 5 annotations, all IEA
   (`GO_REF:0000118` TreeGrafter, `GO_REF:0000120` combined IEA). No experimental
   GO annotation exists for this protein.
2. `genes/PSEPK/PP_2608/PP_2608-uniprot.txt` — the UniProt record, including the
   PDB:4K28 structure cross-reference and its ligand features.
3. `publications/PMID_23142411.md` — the primary characterization paper. **Note:
   `full_text_available: false`; this is the abstract only.**

## Key evidence

The protein is RifI2, a divergent member of the shikimate dehydrogenase (SDH)
structural family, kinetically distinct from the canonical biosynthetic AroE:

- [PMID:23142411 "RifI2 exhibits much lower activity using shikimate as a substrate
  than AroE, and a strong preference for NAD(+) instead of NADP(+) as a cofactor."]
- [PMID:23142411 "Moreover, the enzyme has only trace activity using quinate, unlike
  YdiB."] — so it is not the quinate-catabolic family member either.
- [PMID:23142411 "Here, we have determined the crystal structure of an SDH homolog
  belonging to the RifI class, a group of enzymes with proposed roles in antibiotic
  biosynthesis."]
- [file:PSEPK/PP_2608/PP_2608-uniprot.txt "X-RAY CRYSTALLOGRAPHY (2.15 ANGSTROMS) IN
  COMPLEX WITH MN(2+) AND NAD(+)."] — PDB:4K28.

## Curation reasoning

- **Cofactor corrected, not removed.** `GO:0004764` shikimate 3-dehydrogenase (NADP+)
  is MODIFY → `GO:0052734` (NAD+): the shikimate substrate component is measured, the
  NADP-specific cofactor is contradicted by the kinetics and by the NAD(+)-bound
  structure.
- **`GO:0009423` chorismate biosynthetic process → REMOVE.** The paper establishes no
  physiological pathway role, and KT2440 separately encodes canonical AroE-family
  candidates (PP_0074, PP_2406, PP_3002, PP_3768), so the pathway assignment is a
  paralog-level inference.
- **`GO:0019632` shikimate metabolic process → MARK_AS_OVER_ANNOTATED, not REMOVE.**
  Revised on review feedback. `GO:0019632` is defined direction-neutrally ("The
  chemical reactions and pathways involving shikimate", verified in GO via OLS) and
  carries none of the biosynthetic commitment that makes the `GO:0009423` removal
  correct. Removing it while accepting `GO:0052734` as the core molecular function
  would be internally inconsistent — accepting "acts on shikimate" as the MF and
  denying it as a process. `MARK_AS_OVER_ANNOTATED` records the real problem instead:
  the only measured turnover is low-efficiency and in vitro, and the physiological
  direction is unresolved.

## Open questions

- Physiological substrate is unknown — low shikimate, trace quinate activity.
- Whether the three Mn(2+) sites in 4K28 (`FT BINDING` 34/155/166,
  `ECO:0007829|PDB:4K28`) are a functional metal site or crystallization-derived. The
  cached abstract does not mention metal, SDH-family dehydrogenases are not classically
  metal-dependent, and GOA carries no metal-binding annotation — so no metal-binding
  term is proposed here. Raised as a `suggested_question` instead.
