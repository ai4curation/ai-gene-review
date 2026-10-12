# elg1 (Q86BP6) curation notes

- Ortholog of yeast Elg1 / human ATAD5; AAA+ large subunit of the Elg1 RFC-like complex (PCNA unloader).
- Complex: [PMID:27198229 "identified peptides from all components of the Elg1 PCNA-unloader complex: Elg1, Rfc4, Rfc38, CG8142, and Rfc3"].
- Function in flies: [PMID:27198229 "knocking down elg1 using dsRNAs did not affect total PCNA levels but resulted in increases in the levels of both chromatin-bound PCNA and monoubiquitinated PCNA"]. Enok complex binds via Br140 and inhibits unloading to promote G1/S.
- Germline: [PMID:24531791 "elg1 is required for grk transcript localization and nurse cell endoreplication"]; [PMID:27198229 "knocking down enok partially rescued the defective nurse cell endoreplication observed in the Elg1-depleted germline"].
- NAS row for DNA strand elongation cites PMID:24204884 (Elongin/Corto), which does not mention Elg1; MODIFY to GO:0006261 since Elg1 acts after elongation (unloading).
- GO:0061860 IBA (donor ATAD5) accepted; core function recorded as contributes_to with GO:0031391.
- Round-2 rule applied: generic parents (DNA replication, ATP-dependent activity acting on DNA, protein-containing complex) changed from KEEP_AS_NON_CORE to MODIFY toward the specific term the gene already carries; subunit-level binding/ATPase terms stay KEEP_AS_NON_CORE.
- Falcon deep research (arrived late) gives an accurate orthology-based picture (Elg1-RFC/ATAD5-RFC unloader structures, Xenopus Atad5-RLC as main unloader) but overlooked PMID:27198229, so it understates direct fly evidence.
