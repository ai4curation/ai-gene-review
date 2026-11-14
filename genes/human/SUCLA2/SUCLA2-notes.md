# SUCLA2 notes

Literature review was done manually from cached PubMed records; the falcon deep-research report (SUCLA2-deep-research-falcon.md) completed afterwards and was skimmed for consistency with the review decisions; no conflicts were found.

- SUCLA2 is the ATP-forming beta subunit of the Krebs cycle succinyl-CoA ligase [PMID:17287286 "The SUCLA2 gene encodes the ATP-forming beta subunit of the Krebs cycle enzyme succinyl-CoA ligase."].
- Disease mechanism hypotheses: NDPK association / dNTP salvage [PMID:15877282 "Succinyl-CoA synthetase is invariably in a complex with mitochondrial nucleotide diphosphate kinase"], and succinyl-CoA accumulation explaining MMA [PMID:17287286].
- Promiscuous malyl-CoA formation by TCA enzymes, repaired by CLYBL [PMID:40108300]; 'toxic metabolite repair' was therefore marked as over-annotation for SUCLA2 (changed to UNDECIDED on 2026-11-12, see below).
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

- Affinage record fetched (trust gates clear) and added as a reference with correctness DISPUTED (changed to LOW_QUALITY on 2026-11-12, with the dispute moved to the grounding finding): the checkable narrative claims hold (for example ALAS2 binding [PMID:22740690 "Wild type ALAS2 bound strongly to a SUCLA2 affinity column, but the adjacent XLSA mutant enzymes and the truncated mutant did not bind."]), but its GO grounding with transferase activity and molecular function regulator activity presents indirect effects on protein succinylation as activities of SUCLA2. No annotation imported; one suggested question added.
- GO:0042709 succinate-CoA ligase complex IBA changed from ACCEPT to TOO_GENERAL so that it matches SUCLG2, LSC2 and S. pombe SPCC1620.08: each carries a nucleotide-specific child complex term, and the family root correctly carries the parent.

## Retrospective audit corrections (2026-11-12)

A retrospective audit of the succinyl-CoA synthetase reviews found errors in this review. Each was checked against the source before it was changed.

- GO:0110052 toxic metabolite repair (IDA, PMID:40108300): MARK_AS_OVER_ANNOTATED changed to UNDECIDED, the same as SUCLG1. Only the abstract of the published paper is cached and the published full text is not open. The abstract and the bioRxiv preprint (doi 10.1101/2024.09.25.614871, version 1) present succinyl-CoA synthetase as a source of malyl-CoA and CLYBL as the repair enzyme, which argues for over-annotation. The preprint also names succinyl-CoA synthetase with AUH and CLYBL as an enzyme of itaconate catabolism, so the curator may have annotated the activating step of a disposal route. The experimental row is not overruled on an unread paper. A suggested question records what would settle it.
- GO:0046872 metal ion binding (IEA): KEEP_AS_NON_CORE changed to MODIFY with replacement GO:0000287 magnesium ion binding, which SUCLA2 already carries. A correct but general term is a MODIFY, not a non-core keep.
- core_functions: GO:0004775 moved from molecular_function to contributes_to_molecular_function. The enzyme is an obligate heterodimer, with the phosphohistidine and CoA site on the alpha subunit and the nucleotide and succinate site on the beta subunit. SUCLG1 and SUCLG2 already used contributes_to.
- Itaconate. The description said the enzyme forms itaconyl-CoA. One study found no conversion [PMID:34492704 "neither ATP- nor GTP-specific SCS is able to use itaconate under the same conditions as succinate in vitro"]; the preprint of PMID:40108300 reports a catalytic efficiency 30-fold lower than with succinate for the ADP-forming enzyme. The description now says the activity is reported but contested, and the negative result is a DISPUTED finding of PMID:34492704. The GO:0004775 EXP row from that paper stays ACCEPT and now quotes the result that recombinant SCS-A converted succinate.
- GO:0016878 acid-thiol ligase (IDA, contributes_to): action unchanged, reason rewritten as in SUCLG1. Malyl-CoA formation is covered by GO:0050074 on this gene; the row is retained only because itaconate-CoA ligase activity has no GO term.
- GO:0004775 EXP row from PMID:40108300: the CLYBL abstract sentence was replaced by the curated UniProt reaction, because the sentence says nothing about succinate-CoA ligase activity.
- GO:0006104 rows: the reason now says why the term is kept beside its child GO:1901289. The child is defined by breakdown of succinyl-CoA, so it names only the direction that consumes succinyl-CoA (the forward direction of the TCA cycle).
- Status changed from COMPLETE to DRAFT. The GO:0110052 row is UNDECIDED until the published text of PMID:40108300 is read, as in SUCLG1 and SUCLG2.
- Affinage record. The note listed PMID:33991485 and PMID:39482887 as not verified because they were not cached. Both are cached and support the claims [PMID:33991485 "at S79 dissociates from GLS, resulting in enhanced GLS K311 succinylation"]; they were moved to the verified list. Correctness changed from DISPUTED to LOW_QUALITY, with the DISPUTED status moved to the GO grounding finding. Its one supporting quote on the GO:0004775 IBA row was kept beside the primary paper it was verified against. (Removed later on 2026-11-12: a record rated LOW_QUALITY should not support an annotation row; the row keeps its primary support. The validator's advisory warning that no annotation cites the deep research file is accepted.)
- Cross-file consistency pass (2026-11-12). GO:0003824 catalytic activity (IEA) stays TOO_GENERAL; its reason is now worded the same way in all eleven subunit reviews of the family.
