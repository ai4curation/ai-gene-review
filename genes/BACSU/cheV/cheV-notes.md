

## 2026-11-06 Bacillus comparative chemotaxis review

Identity: P37599, primary gene cheV, UniProt BACSU, strain 168, taxon 224308. Current primary names were checked explicitly because historical cheA/cheC/cheD aliases can refer to fliZ/fliP/fliY.

The reviewed accession is the strain 168 reference. The receptor and CheD mechanistic studies explicitly use OI1085-derived chemotactic laboratory strains; these are not relabeled as literal strain 168 assays. Conserved gene identity and curated strain 168 records support the functional synthesis, with no claim of a sequence-verified identical assay construct. PMID25313396 instead uses predominantly strain 3610; these experiments are identified as such.

CheV is a two-domain chemotaxis coupling and adaptation protein in Bacillus subtilis. Its N-terminal CheW-like domain couples receptors to the CheA kinase, partly overlapping the function of CheW. Its C-terminal receiver domain accepts phosphate from CheA on a conserved aspartate, and this phosphorylation is required for normal adaptation to asparagine even when basal receptor-kinase coupling remains functional.

- [PMID:11553614 Phosphorylation of the response regulator CheV is required for adaptation to attractants during Bacillus subtilis chemotaxis.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:8169224 Chemotaxis in Bacillus subtilis requires either of two functionally redundant CheW homologs.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.

The pristine review text, complete original non-review annotation payloads, inherited proposals and raw SHA-256 hashes are recorded in `.cache/module-audit-logs/chemotaxis-20261106/bacillus-baseline.json`. Every machine annotation is preserved. No raw UniProt or GOA file was edited. The normal default Falcon attempt returned HTTP 403 authorization failure; manual notes are used and no provider report was fabricated.

No NEW biological-process annotation was inferred from necessity alone. New proposals, if any, identify missing experimentally grounded molecular activities. PAINT loss checks were run for all genes carrying IBA and found no lineage loss; donor count and target self-inclusion were not used as weaknesses.

Integration refinement: the newly authored adaptor MF is GO:0030159 signaling receptor complex adaptor activity. PMID8169224 and PMID11553614 explicitly place CheW/CheV coupling between chemoreceptors and CheA, meeting the physical-support definition for a receptor signaling complex. This refines the earlier authored GO:0035591 proposal; there was no machine-seeded adaptor MF to modify. CheV receiver adaptation remains a distinct function.
