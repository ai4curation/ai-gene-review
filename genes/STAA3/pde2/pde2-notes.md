# pde2 functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: A0A0H2XFX6, Staphylococcus aureus subsp. aureus USA300. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon STAA3 pde2` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:27834680 New Insights into the Cyclic Di-adenosine Monophosphate (c-di-AMP) Degradation Pathway and the Requirement of the Cyclic Dinucleotide for Acid Stress Resistance in Staphylococcus aureus.] Cached full text examined; locus SAUSA300_1650 establishes identity independently of the uncharacterized UniProt name. Native mutant and purified-protein data support pApA clearance, while physiological direct c-di-AMP hydrolysis remains uncertain.

Pde2 pApA clearance is kept separate from weak direct c-di-AMP turnover. The canonical pApA hydrolase proposal states only chemistry; feedback relief is its biological justification. The DHH domain alone does not establish a distinct RNA-binding role.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `pde2_activity`.

## 2026-11-05 — PR #5997 evidence follow-up

The hydrolysis evidence supports the catalytic assignment: [PMID:27834680 "Although capable of hydrolyzing c-di-AMP, Pde2 preferentially converts linear 5'-phosphadenylyl-adenosine (pApA) to AMP."]

Removed the hydrolysis quotation from the nucleic-acid-binding over-annotation judgment. The judgment assesses unsupported extension from DHHA1-domain membership; it is not a negative RNA-binding assay. The catalytic evidence remains on the catalytic assertion and core function.

Existing-term check used the [QuickGO term service](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004532,GO:0000175,GO:0004534,GO:0008441,GO:0008081,GO:0034611,GO:0106409). GO:0034611 is obsolete because it corresponded to an assay. GO:0004532 and its directional subclasses GO:0000175/GO:0004534 describe sequential RNA exonuclease reactions; the pApA assay establishes cleavage of one phosphodiester, not a sequential mode or direction. GO:0008441 describes pAp dephosphorylation (AMP plus phosphate), not pApA cleavage (two AMP). The related Bacillus NrnA entry [UniProtKB:O34600](https://www.uniprot.org/uniprotkb/O34600/entry) carries GO:0008441, which does not warrant transferring PAP-phosphatase activity to S. aureus Pde2 or changing the demonstrated pApA reaction. GO:0008081 remains a compatible broad parent. The pApA proposal name, definition and parent are unchanged; its justification now records these comparisons explicitly.
