# Ckmt2 review notes

## Evidence summary
- [UniProtKB:P09605] UniProt describes Ckmt2 as reversibly transferring phosphate between ATP and creatine/phosphocreatine for energy transduction.
- [PMID:3972849] The fetched GOA file uses this publication for cardiolipin binding, which is kept as non-core membrane-context support rather than the defining function.
- [PMID:8086475] The fetched GOA file uses expression evidence for heart and skeletal muscle development terms; these are marked over-annotated because expression/developmental context is not the enzyme core function.

## Curation decisions
- Core function: mitochondrial creatine kinase S-type (creatine kinase activity, GO:0004111).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-04

**GOA changes.** None in substance: the refreshed GOA has the same 14 rows (3 IBA, 8 IEA, 1 IDA cardiolipin binding from PMID:3972849, 2 IEP developmental rows from PMID:8086475). No PENDING, no retired rows.

**Row audit.** No action changed (5 ACCEPT, 3 KEEP_AS_NON_CORE, 4 MODIFY of generic catalytic/kinase/transferase parents to GO:0004111 creatine kinase activity, 3 MARK_AS_OVER_ANNOTATED developmental rows). The developmental rows rest on expression timing only [PMID:8086475 "sMtCK mRNA in heart is undetectable prenatally but is dramatically upregulated by 28 d postnatally."]; that is not participation in tissue development, so MARK_AS_OVER_ANNOTATED stands.

**Stale quotes fixed.** The refreshed UniProt record no longer has `DR GO` lines, so ten `supporting_text` quotes of the form "GO; GO:0004111; F:creatine kinase activity; IBA:GO_Central." no longer matched the source. They now quote the record's CATALYTIC ACTIVITY ("Reaction=creatine + ATP = N-phosphocreatine + ADP + H(+);"), SUBCELLULAR LOCATION, TISSUE SPECIFICITY and MISCELLANEOUS ("Mitochondrial creatine kinase binds cardiolipin.") lines. The cardiolipin-binding IDA row also cites its own paper [PMID:3972849 "mt-CK was bound by liposomes but only if they contained cardiolipin."]. The IEA skeletal-muscle-development row now cites the expression data it derives from.

**Description.** Rewritten as standalone biology; removed "The review accepts ... marks ... as non-core or over-annotated".

**Open questions.** None new.
