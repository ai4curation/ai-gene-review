# CycA review notes

The selected 490 aa PC protein differs from 491 aa PA by one N-terminal residue; the cyclin domain is unchanged. Broad cell-cycle and CDK-regulator transfer is supported by fly genetics and biochemical work. All three original GOA rows are accepted and one molecular-function annotation is proposed NEW; the two original GO predictions are CNN. The annotation-overlap categories do not establish training-data novelty. No exact PC degradation kinetics are claimed.

## Provider research assessment

The completed Falcon synthesis was inspected. It supports CycA as the regulatory, noncatalytic partner of Cdk1 and places the G2/M role in established fly cell-cycle biology. Its additional centromere, cortical spindle-orientation, ER-remodeling and endocycle discussions concern particular tissues or perturbations, not direct characterization of the exact PC isoform. These findings do not alter the supported broad CDK-regulator and mitotic-transition assessments. Original GOA sparsity does not make those known functions novel; both predictions and the narrative are CNN, while actual training-set membership is unknown. The local sequence comparison provides the explicit PC-to-PA connection that the provider report does not independently resolve.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** M9NFR3 is "Cyclin A, isoform C" (FlyBase CycA-PC, FBgn0000404), 490 aa, an unreviewed TrEMBL entry. The reviewed canonical product of the same gene is P14785 (CCNA_DROME, isoform A, 491 aa; UniProt also lists a short isoform B lacking residues 1-146). The existing local alignment (CycA-bioinformatics/RESULTS.md) shows that PC lacks only Gln66 of PA and keeps the cyclin N-terminal domain (PA 206-332 maps to PC 205-331); SMART also places both cyclin-box folds in PC (240-324, 337-419) and the Cyclin_C domain (333-450). Nothing functional is missing. M9NFR3 is therefore a full-length alternative isoform, and gene-level CycA evidence transfers to it. P14785 has no review in the repo (searched genes/*/* for P14785; none found), so the next relative is the same-gene canonical product, which would go in genes/DROME/CycA__P14785.

**Evolutionary placement.** PANTHER 19.0 places P14785 in PTHR10177:SF593 "G2/MITOTIC-SPECIFIC CYCLIN-A". Human CCNA2 (P20248) is SF444 and CCNA1 (P78396) is SF254, so the cyclin A orthologs fall in separate, lineage-split SFs; this review transfers no SF-specific function from them. FBgn0000404 is itself one of the PAINT IBD donors at the family-root node PTN000019791 for GO:0016538 (CDK regulator activity), GO:0005634, GO:0005737 and GO:0000082 (interpro/panther/PTHR10177/PTHR10177-paint.tsv), so the core MF is grounded at the base of the family and also experimentally in fly. PTN000020367 (GO:0097124 cyclin A2-CDK2 complex, taxon:33213) has only mammalian donors (MGI:108069, P20248). Fly CycA is reported to complex only with Cdk1 [PMID:9210381 "In Drosophila , however, cyclin A only complexes with cdc2"], so that IBA on P14785 looks like an over-propagation into the fly lineage. I recorded it as a suggested question and did not transfer it.

**PANTHER family review.** interpro/panther/PTHR10177/PTHR10177-review.yaml lists M9NFR3 under "Benchmark members without resolved subfamily placement". The UniProt record for P14785 and the PANTHER member file place CycA in SF593, so that subfamily placement can now be considered resolved. The review.md describes fly CycA under the "S-phase / G1-S cyclins (cyclin A and cyclin E class)" grouping. This is a broad-class description, but it under-weights CycA's established G2/M role (PMID:8428595), and fly CycA is closer to the A/B mitotic cyclin class than to cyclin E. I did not edit the family review.

**Literature (new citations cached).** PMID:2139805 (cyclin A-deficient cells do not enter mitosis); PMID:8428595 (CycA acts synergistically with CycB at G2-M, and double mutants arrest in G2 before mitosis 15); PMID:15203007 (CycA is cytoplasmic in interphase through LMB-sensitive export, nuclear accumulation is dispensable for mitosis, and the essential mitotic function is CycA-kinase-dependent inhibition of Fzr/APC-C); PMID:9210381 (ectopic CycA drives G1/S, and CycA partners only cdc2).

**Changes to annotations.**
- GO:0000278 mitotic cell cycle: ACCEPT → MODIFY to GO:0000086 G2/M transition of mitotic cell cycle (an is_a descendant, checked in OLS). CycA is the regulatory subunit of the kinase that performs the transition, so this is participation, not just necessity. I did not propose G1/S, because the S-phase activity rests on overexpression.
- GO:0005634 nucleus: ACCEPT → KEEP_AS_NON_CORE. Nuclear only from prophase, and nuclear accumulation is not required for function (PMID:15203007).
- GO:0051301 cell division: ACCEPT (retained).
- GO:0016538 CDK regulator activity: kept as NEW (core MF), with support added from PMID:9210381, the P14785 curated SUBUNIT line, and the PAINT donor observation.
- NEW GO:0005737 cytoplasm: the main interphase location, supported by PMID:15203007 and PMID:2564316.
- NEW GO:0000307 cyclin-dependent protein kinase holoenzyme complex: CycA-Cdk1, from the P14785 SUBUNIT line and PMID:9210381. GO:0097124 was deliberately not used.
- Description rewritten as a biological summary, and status set to COMPLETE.

**Not proposed.** Centromere, spindle-orientation, ER and endocycle-suppression roles from the Falcon report concern particular tissues or perturbations. Negative regulation of APC/C-Fzr is mechanistically attractive, but whether Fzr is a direct substrate is not established (see suggested_questions).

**Modules.** No module lists CycA as a part. Related modules are modules/g2_m_transition.yaml, modules/cell_cycle_progression.yaml, modules/metaphase_anaphase_transition_and_mitotic_exit.yaml (mitotic cyclins A/B as APC/C substrates) and modules/g1_s_transition.yaml.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0016538, GO:0005737) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/DROME/CycA__P14785/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn, following the rule applied across the
ProtNLM2 re-review cohorts (first raised in the review of PR #5303). The gene-level function is unchanged.
