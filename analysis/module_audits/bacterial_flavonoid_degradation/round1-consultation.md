# PR #6140 annotation-reviewer consultation

The two requested action/reason corrections are addressed, and the same participation criterion has been applied across every inherited process proposal in the 21-member panel.

1. **Hsero_1012 EC mapping:** GO:0003978 is current and correctly maps EC:5.1.3.2. The defect is the unvetted, substrate-specific EC assertion on the protein. Restored the PROBABLE WRONG_TERM/DELETE_VALUE report. MARK_AS_OVER_ANNOTATED is used rather than REMOVE because neither a negative enzyme assay nor an evolutionary contradiction establishes absence; the available fold and competing KO classification establish over-specificity. This implements the reviewer's explicitly offered qualified alternative.
2. **PP_3198 process proposal:** withdrawn from the active set with retired:true and a current MAOA judgment, preserving source payload and position. The supported cluster-binding core remains; the unsupported process core is removed.
3. **ORS285 provenance:** the PMID entry stays within the cached abstract and a separate file evidence entry traces the previously accessed Results/Figure 8 through module notes.
4. **FdeB consistency:** Hsero_1004, PP_3195 and bll6428 now consistently flag peptide claims as MAOA and leave ester specificity UNDECIDED. Reviewed UniProt Q93NG6 provides an independent experimentally supported C-C hydrolase within IPR050261; official snapshots are preserved. The PTHR22946 narrative is aligned without changing scopes, PAINT assessments or supporting quotes. R13077 remains an explicitly hypothetical reaction-role class in the module, not a demonstrated representative activity.
5. **Core synthesis:** remove uninformative bll6422/bll6428 placeholders and unsupported specific or process-only cores for the reassessed candidates, retaining uncertainty in knowledge gaps.
6. **Description:** bll6428 now uses biological prose rather than annotation commentary. The two other FdeB descriptions reflect the same unresolved physiology.
7. **Shared project journal:** untouched by this consultation per coordinator instruction. Root should fix the review's spacing glitches and regenerate its page.

## Complete proposal audit

Nine inherited process rows are explicitly retired: Hsero_1004, PP_3195, PP_3198, Hsero_1010, PP_3204, Hsero_1011, PP_3205, Hsero_1012 and PP_3206. These depend on untested B/D/H/I/J assignments or similarity to unassayed counterparts, not an experimentally grounded individual step. Four FdeE/FdeC process proposals remain, grounded by HERSS experiments or qualified PSEPK donor transfer; three FdeC reaction-class MF proposals also remain. No new row is introduced.

This is **curator withdrawal**, not an upstream GOA disappearance. The schema's retired field preserves the historic assertion while excluding it from active matching. Simply replacing NEW with MAOA fails GOA validation because the row never came from GOA; explicit retirement records the intended state without modifying the validator or fabricating a GOA record. All 46 annotation source payloads and original positions remain; all 16 inherited proposal rows remain present, with seven active NEW rows after reassessment. The proof records all nine retirement flags separately from unchanged source fields.

## Validation

Eleven changed gene reviews pass `just validate`; two reference batches cover all eleven files with zero issues. All thirteen generated history records validate. Gene and module rendering passes. Module schema and semantics pass with twenty documented conformance advisories; 44 candidate-coverage cases and four mechanism mutations pass, as does Ruff. These checks do not prove native complete catabolism. Eighty-five scoped publication/raw/provider artifacts remain byte-identical. No shared tracker, source snapshot, test, validator or schema was modified. Renewed full validation and remote publication remain root responsibilities.
