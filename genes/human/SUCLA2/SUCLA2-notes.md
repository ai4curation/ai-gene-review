# SUCLA2 notes

Literature review was done manually from cached PubMed records; the falcon deep-research report (SUCLA2-deep-research-falcon.md) completed afterwards and was skimmed for consistency with the review decisions; no conflicts were found.

- SUCLA2 is the ATP-forming beta subunit of the Krebs cycle succinyl-CoA ligase [PMID:17287286 "The SUCLA2 gene encodes the ATP-forming beta subunit of the Krebs cycle enzyme succinyl-CoA ligase."].
- Disease mechanism hypotheses: NDPK association / dNTP salvage [PMID:15877282 "Succinyl-CoA synthetase is invariably in a complex with mitochondrial nucleotide diphosphate kinase"], and succinyl-CoA accumulation explaining MMA [PMID:17287286].
- Promiscuous malyl-CoA formation by TCA enzymes, repaired by CLYBL [PMID:40108300]; 'toxic metabolite repair' therefore marked as over-annotation for SUCLA2.
- 'succinyl-CoA pathway' (heme) rests on the speculative ALAS2 interaction [PMID:10727444]; marked as over-annotation.

## The organelle-level localization rows

The ten `GO:0005739` mitochondrion rows are `ACCEPT`, and that is a decision rather than an
oversight. SUCLA2 is a matrix enzyme and `GO:0005759` is accepted here on two rows and is the core
location, so a reader applying the "correct but general terms are MODIFY" rule mechanically, or
re-running an ancestor-based scan, will stop on these ten. They are not reached by that rule: none
of the ten reasons says the term is less specific than the evidence supports — they give the
localization and proteome evidence and the gene's function. Each does describe SUCLA2 as a matrix
TCA-cycle enzyme, which names a narrower compartment than the row annotates; that is background on
the protein rather than an argument that the row's term should be refined, which is the distinction
the rule turns on. Nothing else in this file refines a mitochondrial-location ancestor, so the file
does not treat one argument two ways. Whether GOA's
organelle-level rows should be refined wherever a compartment row exists is a real question, and it
is a slice-wide one rather than anything specific to this gene.

## 2026-11-11 Affinage added; one action harmonised

- Affinage record fetched (trust gates clear) and added as a reference with correctness DISPUTED: the checkable narrative claims hold (for example ALAS2 binding [PMID:22740690 "Wild type ALAS2 bound strongly to a SUCLA2 affinity column, but the adjacent XLSA mutant enzymes and the truncated mutant did not bind."]), but its GO grounding with transferase activity and molecular function regulator activity presents indirect effects on protein succinylation as activities of SUCLA2. No annotation imported; one suggested question added.
- GO:0042709 succinate-CoA ligase complex IBA changed from ACCEPT to TOO_GENERAL so that it matches SUCLG2, LSC2 and S. pombe SPCC1620.08: each carries a nucleotide-specific child complex term, and the family root correctly carries the parent.
