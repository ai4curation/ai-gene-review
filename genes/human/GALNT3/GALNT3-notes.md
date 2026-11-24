# GALNT3 review notes (2026-10-10)

Deep research: `just deep-research-falcon human GALNT3` failed (falcon timeout); literature work was done manually from
the GOA-cited papers cached in `publications/`.

## Function
- Initiating GalNAc-transferase of mucin-type O-glycosylation; recombinant enzyme active with distinct
  specificity [PMID:8663203]; "GalNAc-T1 and -T3 showed strict donor substrate specificities for UDP-GalNAc"
  [PMID:9295285].
- Key physiological substrate FGF23: "GalNAc-T3 selectively directs O-glycosylation in a subtilisin-like
  proprotein convertase recognition sequence motif, which blocks processing of FGF23" [PMID:16638743];
  "GalNAc-T3 specifically glycosylates FGF23 at Thr178 in its subtilisin-like proprotein convertase (PC) site"
  [PMID:31932717].
- Type II Golgi membrane enzyme with "Golgi lumen located catalytic, GT-A fold domain" [PMID:31932717].

## Disease (HFTC1 / HHS)
- "Both patients had low levels of the full-length FGF23 with markedly augmented amounts of the inactive
  fragments" [PMID:17129170].

## Curation decisions
- All activity rows ACCEPT; core MF GO:0004653, BP GO:0016266, location Golgi membrane.
- FGFR signaling (Reactome TAS) -> MARK_AS_OVER_ANNOTATED: GALNT3 makes the ligand, it does not signal.
- Cytoplasm (is_active_in, IEA) -> MARK_AS_OVER_ANNOTATED.
- Calcium ion binding IDA -> UNDECIDED (abstract only; cofactor is Mn2+).
- Alignment with dismech `Hyperphosphatemic_Familial_Tumoral_Calcinosis`: the GALNT3 node uses GO:0004653
  (LOSS_OF_FUNCTION) and the downstream node protein O-linked glycosylation DECREASED - consistent.


## 2026-11-02 source-based reassessment

The current synthesis is supported by direct human GALNT3 peptide glycosylation, purified-enzyme and FGF23 cell experiments (PMID:8663203, PMID:9295285, PMID:16638743, PMID:17129170, PMID:31932717). A single Golgi glycosyltransferase core describes O-GalNAc initiation. Human enzyme and cell evidence is distinguished from the zebra finch crystal complexes in PMID:31932717, and from engineered soluble constructs rather than natural splice products. The 633- and 192-residue products are both preserved; equivalent activity of the short product is not established.

The later FGF23 study refines the inherited secretion account: the short pulse assay did not show a marked secretion-rate increase, while greater intact hormone accumulation at the later endpoint was mainly attributed to stability after secretion (PMID:31932717). The GALNT3–FGF23 chemistry remains direct, but membership in Reactome 190372 does not establish execution of the receptor-triggered signals defined by GO:0008543. That annotation is marked over-annotated without calling the pathway source wrong or adding a replacement process.

The calcium-binding annotation remains UNDECIDED. The original human enzyme experiment found no turnover when calcium or magnesium replaced manganese, but that is not a direct demonstration of absent calcium binding (PMID:9295285). The ocular perinuclear annotation also remains UNDECIDED because the target-specific panel was not recovered; the abstract's GALNT2 observation does not prove a GALNT3 curator error (PMID:12506059). Independently established human Golgi localization remains accepted (PMID:9394011; HPA).

The original exosome Table 2 target row is now resolved: historical GI1617312 maps to human GALNT3, with one matched peptide in fraction 3 (PMID:18570454). This supports a limited non-core vesicle-fraction association with the neural-stem-cell context. It establishes neither membrane orientation nor a role in vesicle biogenesis. The prior uncertainty and every original quote/claim remain preserved in the inherited archive.

Four broad O-glycosylation contexts are refined to O-GalNAc glycosylation through the verified is_a relation. Broad membrane and cytoplasm contexts are refined to Golgi membrane and Golgi apparatus using verified is_a and part_of relations. Cytoplasm includes organelles, so the earlier cytosol-based rejection is not retained. Actual PAINT origins and the human target alignment support all three inherited placements; self-donor evidence is legitimate. Reactome failed-mutant events are separated from normal catalytic records, with genuine GALNT3 membership preserved.

The [source guide](GALNT3-source-guide.md) gives original-source URLs, selected-reading limits, the portable EV row, product/construct distinctions and typed relation paths. All 35 incoming contexts and three extension atoms are preserved, with no NEW annotation. The whole prior review and all 48 quote occurrences, prior journal, provider and history artifacts remain historical evidence. The four initial quote-routing mismatches were resolved against the correct immutable UniProt source without changing the archive. Current excerpts are short exact source substrings and are not repeated in these notes.

Native acquisition and reconciliation now establish 35 exact contexts, both products and all 24 sources. The inherited review was not reseeded, and all 19 existing source bytes remain unchanged. The three literal extension atoms omitted by the native parser are restored from their original contexts. [Compact source provenance](GALNT3-source-evidence.yaml) retains the lossless current fields and immutable prior-review/journal/provider/history locators. The full old-review and expanded evidence archives remain private. A native EDIT record documents this update. Default validation and strict GOA matching pass for all 35 contexts; the computed review status remains DRAFT because two judgments are UNDECIDED. Structured term-scope metadata records the valid PAINT transfer, and a reference-only support pointer links the direct human O-GalNAc process without repeating excerpts. The remaining advisory concerns the preserved, unused falcon artifact; it is not cited as scientific evidence. History validation and private rendering also pass.

## 2026-11-04 source-specific review follow-up

This entry supersedes the earlier non-core manganese and undecided perinuclear judgments while preserving the dated journal above. Manganese binding is accepted as a property of the existing catalytic core: purified human GALNT3 supports manganese-dependent transfer, whereas calcium or magnesium did not replace it in the tested assay (PMID:9295285). This does not establish that calcium cannot bind. Calcium binding remains UNDECIDED, and transferred zebra-finch residue assignments are not described as direct human structural measurements.

The ocular study used GALNT3-specific antibodies and reported positive human target distribution (PMID:12506059). Together with independent Golgi localization (PMID:9394011), this supports a non-core perinuclear assignment while deferring to the curator; the exact original GALNT3 panel was not independently recovered. No GALNT2 observation is relabeled as a GALNT3 result.

The extracellular-vesicle evidence is stronger than a solitary unvalidated spectrum. Original Table 2 identifies GALNT3 in fraction 3; TEM and size fractionation characterize the vesicles, and the authors required Mascot scores above 50 plus repeated detection across three shotgun analyses for single-peptide identifications (PMID:18570454, Tables 1–2 and Results p3480). This supports non-core fraction membership, without claiming purity, membrane orientation, extracellular enzyme activity, biological replication or vesicle biogenesis. The [source guide](GALNT3-source-guide.md) gives the public original-source links and selected-reading limits.

The current tally is 25 ACCEPT, 6 MODIFY, 2 KEEP_AS_NON_CORE, 1 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED. All 35 original contexts, three extension atoms, two products, the catalytic core, six current excerpts and all historical evidence remain unchanged. No new quote or source is added.

Default validation and strict GOA matching passed for all 35 contexts; the computed status is DRAFT with one UNDECIDED judgment. The retained, unused historical falcon artifact remains the sole advisory. Status audit, native EDIT validation and private rendering passed. All 24 source files, the compact source-evidence YAML and ontology cache remain unchanged.

## Citation and portable-evidence follow-up, 2026-11-04

The biological judgments remain unchanged. Each of the 35 reviews now links its relevant sources explicitly. Short exact anchors make the human catalytic, manganese-cofactor, FGF23-glycosylation and ocular-distribution evidence visible; reference-only links share that evidence without duplicating quotations. The 2006 processing result remains interpreted alongside the later secretion-rate/stability distinction. Calcium binding stays UNDECIDED, and the exact ocular perinuclear panel remains uninspected.

The [portable original-source evidence](GALNT3-external-evidence.md) reproduces the selected vesicle-table target line and links its official accession mapping. It records the original methods/table locators and the limits of a repeated single-peptide identification. The normal publication cache remains abstract-only. Reactome R-HSA-5083625 is now explicitly cited as disease provenance on the two R-HSA-5096537 contexts, separately from normal wild-type catalytic evidence. The [source guide](GALNT3-source-guide.md) describes the reading scope and excerpt budgets.

All 35 machine contexts, three extension atoms, two products, the catalytic core and the six prior current excerpts remain exact. All 48 historical quotation associations remain available through their immutable prior-review locators. Default validation and strict GOA matching passed for all 35 contexts. The status audit confirms DRAFT, with calcium binding remaining UNDECIDED; the retained unused falcon artifact is the sole annotation advisory. Native EDIT validation and private rendering passed. All 24 normal source files, prior history and the ontology cache remain unchanged.
