# BRCA1 Gene Review Notes

## 2025-01-14 - Term Label Update

**Issue**: Validation failure due to 1 GO term having an outdated label.

**Root Cause**: GO:0006301 had the label "DNA damage tolerance" but the current ontology uses "postreplication repair".

**Action Taken**: Updated the term label from "DNA damage tolerance" to "postreplication repair" to match the current GO ontology.

**Validation Status**: After fixing the term label, the gene now passes validation with only warnings about PENDING annotations.

**Note**: This represents a routine ontology term label update. BRCA1 is a critical DNA repair protein associated with hereditary breast and ovarian cancer, and the term "postreplication repair" more accurately describes one of its DNA repair functions.

## 2026-07-22 - QA re-review pass

Conservative QA pass over the complete review (275 existing annotations). Changes made:

1. **GO:0045944 (positive regulation of transcription by RNA polymerase II) — action consistency.**
   The four annotations to this term disagreed: IBA, IEA, IDA were `KEEP_AS_NON_CORE` but
   the IMP annotation (PMID:20820192) was `ACCEPT`. Set the IMP annotation to
   `KEEP_AS_NON_CORE` so all four agree. The whole review consistently treats BRCA1
   transcriptional coactivation as peripheral to its core DNA-repair / E3-ligase roles, so
   non-core is the biologically correct choice. This IMP entry also had an **erroneous
   copy-paste summary/reason** ("BRCA1 nucleoplasm localization from Reactome pathway" /
   "Nucleoplasm localization is essential") that described a nucleoplasm CC annotation, not a
   transcription BP term — rewrote both to describe the actual transcriptional-coactivator
   function. supporting_text left unchanged.

2. **GO:0005737 (cytoplasm) — action consistency.**
   The IEA annotation was `ACCEPT` while the IDA annotation (PMID:20160719) was
   `KEEP_AS_NON_CORE`. BRCA1 is predominantly nuclear; cytoplasm is a minor, non-core pool
   (the IEA entry's own reason describes it as splice-variant / context-specific). Set the
   IEA annotation to `KEEP_AS_NON_CORE` to match.

Checked but deliberately left unchanged:
- All 70 `protein binding` (GO:0005515) annotations are already `REMOVE` — none were
  `ACCEPT`/`MODIFY`, so nothing to fix for the "avoid protein binding" guideline. (The
  aggressive blanket-REMOVE of experimental IPI annotations is the prior reviewer's
  consistent choice; not second-guessed here per the "don't overrule curators" guideline.)
- core_functions ids (GO:0004842, GO:0003684, GO:0002039) are all correctly in the
  molecular_function branch.
- No remaining terms have inconsistent actions across evidence types.

Validation after edits: `✓ Valid` (no warnings/errors).