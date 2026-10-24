# ALDOB (P05062) review notes

Human fructose-bisphosphate aldolase B (liver-type aldolase). Deep research (falcon)
did not materialize within the 8-min poll window; review grounded in the UniProt record
(`ALDOB-uniprot.txt`), the seeded GOA (`ALDOB-goa.tsv`), cached `publications/PMID_*.md`,
and the HFI disorders KB (`~/repos/dismech/kb/disorders/Hereditary_Fructose_Intolerance.yaml`).

## Core biology

- Class I (Schiff-base) fructose-1,6-bisphosphate aldolase, EC 4.1.2.13; homotetramer;
  active-site Lys230 forms the Schiff-base intermediate, Asp188 is proton acceptor
  (UniProt FT ACT_SITE 188, 230).
- Two catalytic activities in one active site:
  - **Fructose-bisphosphate aldolase (GO:0004332)**: F1,6BP <-> DHAP + G3P (glycolysis/
    gluconeogenesis). Rhea:14729, EC 4.1.2.13.
  - **Fructose-1-phosphate aldolase (GO:0061609)**: F1P -> DHAP + D-glyceraldehyde
    (fructolysis). Rhea:30851. ALDOB has comparatively high F1P activity vs ALDOA/ALDOC.
  - UniProt kinetics: KM ~1 uM for F1,6BP, ~0.7-2.3 mM for F1P (PMID:10970798, PMID:20848650).
- Cytosolic (GO:0005829). Also reported at cytoskeleton/MTOC/centriolar satellite
  (PMID:18000879) and binds actin cytoskeleton (PMID:9244396) — moonlighting/peripheral.
- Tissue expression: liver, kidney, intestine (HPA "Group enriched (intestine, kidney, liver)").

## Disease

- **Hereditary fructose intolerance (HFI, MONDO:0009249, MIM:229600)** — autosomal
  recessive aldolase B deficiency. Fructose ingestion -> F1P accumulation, ATP/Pi
  depletion, hypoglycemia, hepatic/renal toxicity. Common alleles A150P, A175D, N335K
  (UniProt VARIANT). Many HFI variants characterized functionally in the cited papers
  (PMID:3383242, 10625657, 10970798, 12205126, 20848650).

## Moonlighting / non-canonical

- **Tumor suppressor scaffold (PMID:35122041, abstract-only)**: Aldob directly binds and
  inhibits G6PD, potentiating p53-mediated inhibition of G6PD in an Aldob-G6PD-p53
  ternary complex; scaffolding effect independent of enzymatic activity. Basis for GOA
  IDA molecular_adaptor_activity (GO:0060090), IMP negative regulation of PPP shunt
  (GO:1905856), and IPI protein binding to TP53/G6PD. Mutagenesis (K147A, R149A, K230A)
  impairs G6PD interaction (UniProt MUTAGEN).
- **V-ATPase assembly (PMID:17576770, abstract-only)**: aldolase physically associates
  with the B subunit of vacuolar H+-ATPase; binding (not catalysis) required for V-ATPase
  assembly/activity. Basis for GOA IMP GO:0070072 and IDA GO:0051117 ATPase binding.
  Note: the abstract describes "aldolase" generically; curator (BHF-UCL) attributed to ALDOB.
- **BBS protein interactions (PMID:18000879, abstract-only)**: Y2H + coIP + colocalization
  with BBS1/2/4/7; basis for centriolar satellite / MTOC localization and protein binding IPIs.
- Cytoskeleton binding (PMID:9244396): aldolase B binds liver cytoskeleton (actin);
  basis for GO:0008092 cytoskeletal protein binding IDA.

## Curation decisions summary

- Core MF: GO:0004332 and GO:0061609 (both heavily EXP/IDA supported) -> ACCEPT.
- Core BP: fructolysis/fructose catabolism (GO:0006001), glycolysis (GO:0006096),
  gluconeogenesis (GO:0006094), F1,6BP metabolic process (GO:0030388), fructose
  metabolic process (GO:0006000) -> ACCEPT/KEEP.
- Bare `protein binding` (GO:0005515) IPIs: uninformative -> MARK_AS_OVER_ANNOTATED
  (per policy, not REMOVE). The ALDOA IPIs (P04075) are large-scale interactome hits
  reflecting the homo/heterotetramer / co-purification.
- Moonlighting scaffold functions (G6PD/p53, V-ATPase, BBS, cytoskeleton, MTOC/centriolar
  satellite) -> KEEP_AS_NON_CORE; real but peripheral to the canonical aldolase function.
- extracellular exosome (GO:0070062, HDA prostatic-secretion exosome proteomics) ->
  KEEP_AS_NON_CORE (mass-spec bystander).
- Reactome cytosol TAS duplicates -> ACCEPT (cytosol) / KEEP_AS_NON_CORE where redundant.

## Verification note on PMID:6696436

GOA line 25: EXP GO:0004332 with original_reference_id PMID:6696436, assigned by Reactome.
The cached abstract (PMID:6696436) is "Human skeletal-muscle aldolase: N-terminal sequence
analysis..." — a sequencing paper on muscle (ALDOA) aldolase, not an activity assay on ALDOB.
Per policy (do not REMOVE experimental annotations whose full text I can't verify, and the
paper is clearly about the aldolase family EC 4.1.2.13), marked UNDECIDED: the EC 4.1.2.13
family activity is correct for aldolases but this specific reference does not appear to
establish ALDOB fructose-bisphosphate aldolase activity; other strong EXP/IDA lines already
support GO:0004332.

## 2026-09-27 substantive ClinGen re-review

This entry supersedes the earlier decision summary and its source-access assumptions; the historical notes above are retained. HGNC:417 approves ALDOB (UniProt P05062). HGNC lists no alias, while the preserved UniProt record also uses ALDB. Canonical and ALDB open-PR searches were empty; no alias directory was found. All five starting files matched parent-verified main `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc` byte for byte.

The fresh default Falcon attempt and perplexity-lite fallback both failed before provider contact with PyPI DNS errors (exit 2); no provider report was produced or authored. Log: `/tmp/ALDOB-fresh-research.log`. Concurrent normal GOA publication caching found all 14 original PMIDs already cached. Subsequent normal fetches failed for four newly required publications and two Reactome events, listed below. The work therefore remains DRAFT despite completing every annotation judgment.

### Source-specific decisions

All 53 original source objects, including qualifiers, reference identities and any isoform flags, are preserved. Final actions are 37 ACCEPT, 8 KEEP_AS_NON_CORE, 5 REMOVE, 1 MODIFY and 2 UNDECIDED, with no NEW. Fifteen propagation reviews trace the actual ancestral nodes or electronic sources. Two catalytic cores replace the prior three: the same F1,6BP reaction serves both glycolysis and gluconeogenesis; F1P cleavage is the distinct substrate-specific second core.

- **Fructose versus fructose phosphate.** The current [GO:0070061 definition](https://amigo.geneontology.org/amigo/term/GO:0070061) identifies the unphosphorylated ketohexose. The complete original PMID:10625657 paper, independently read by annotation_aars1 and checked at its Methods/Results here, measures F1P/F1,6BP cleavage, phosphate-substrate affinity elution and DHAP/glyceraldehyde condensation. Its mutant-binding discussion does not demonstrate free-fructose binding. Both the experimental and ARBA free-fructose assertions are removed at the ligand-scope level, without asserting biochemical impossibility. The ARBA predicates remain uninspected; no causal claim about how that rule acquired the term is made. A binding-to-catalysis replacement would change functional category and duplicate already-present enzyme terms, so none is proposed. [Original JBC PDF](https://genetyca-icm.com/wp-content/uploads/2018/03/Expression-purification-and-characterization-of-natural-mutants-of-human-aldolase-B.-Role-of-quaternary-structure-in-catalysis..pdf), p.1146: “Aldolase cleavage activity toward the substrates fructose 1-phosphate and fructose 1,6-bisphosphate was assayed”. Local cache remains abstract-only.
- **Protein interactions.** Generic protein-binding records for BBS proteins and ALDOA are removed as uninformative, without denying interaction. ALDOA/P04075 is a different protein, so these pair records do not establish ALDOB homotetramers or functional heterotetramers. The independent self-partner/biophysical PMID:10625657 record does support functional homotetramerization. The G6PD/TP53 generic IPI is instead refined to the already-seeded molecular-adaptor activity on positive ternary-scaffold evidence.
- **Hepatic scaffold.** PMID:35122041 reports G6PD inhibition potentiated by an ALDOB-G6PD-p53 complex independently of aldolase catalysis. The primary abstract is explicit; individual activity/localization panels and the complete mechanistic body remain unread. Those IDAs are retained by curator deference plus independent enzyme/location support. The scaffold and PPP regulatory activity remain non-core in the reported hepatic/HCC context, not because catalytic proteins cannot have adaptor activity. The actual [2025 correction, PMID:41188550](https://www.nature.com/articles/s43018-025-01075-1.pdf), published 4 November 2025, replaces the fourth panel of Extended Data Fig.4d (Aldob-null plus Aldob AAV) and associated source data. It does not retract the paper or announce withdrawal of the scaffold conclusion.
- **V-ATPase.** The [original full PMID:17576770 article](https://www.researchgate.net/publication/6259929_Physical_Interaction_between_Aldolase_and_Vacuolar_H-ATPase_Is_Essential_for_the_Assembly_and_Activity_of_the_Proton_Pump) actually tests human ALDOB A318E/R303W constructs in yeast, alongside yeast aldolase mutants. Thus the human gene assignment is experimentally grounded, not inferred from a generic abstract. Binding-dependent assembly is direct structural/cofactor participation; ALDOB does not perform proton pumping. Exogenous ATP in the pump assay limits conclusions about physiological energy supply. Keep the specific ATPase-binding and assembly annotations non-core with this context.
- **BBS/centrosome.** The [full PMID:18000879 author article](https://www.researchgate.net/publication/5845874_Novel_interaction_partners_of_Bardet-Biedl_syndrome_proteins) uses human fetal-kidney library fragments, full-length Y2H confirmations, fragment coIP and transfected-HeLa localization. ALDOB is adjacent to gamma-tubulin rather than overlapping it; the authors qualify the satellite/MTOC interpretation. Retain the existing compartment assertions as non-core without manufacturing an endogenous hepatocyte ciliogenesis role.
- **Cytoskeleton and exosomes.** PMID:9244396 explicitly gives positive ALDOB liver-cytoskeleton binding, whereas detailed mutant/competition/fibroblast-contraction experiments in its abstract concern ALDOA. The broad binding term is retained without transferring those additional mechanisms. PMID:23533145 verifies the EPS-urine exosome-enriched screen; its individual supplementary ALDOB peptide entry remains unrecovered. The target-specific HDA is therefore UNDECIDED, deferring to the curator without asserting an error. The older notes' “bystander” wording is unsupported and is superseded; neither contamination nor extracellular enzyme function is asserted.
- **Remaining citation uncertainty.** PMID:6696436 remains UNDECIDED because the source-specific ALDOB experiment has not been recovered from the full skeletal-muscle sequencing paper; the old MISCITED/wrong-paralog interpretation is withdrawn. PMID:12205126 is metadata-only locally, although an original introductory excerpt identifies the Spanish HFI study. Its exact functional assays remain unverified; the two established enzyme activities are retained through curator deference and independent purified-human measurements. No fabricated supporting quote is supplied.

### Propagation, corrections and source availability

The cached PTHR11627 PAINT IBD has PTN002614886 for F1P activity with human P05062 and mouse MGI:87995 descendants. Four older seeded rows name PTN000179343, while the current export uses PTN004279385 for their terms. The historical correspondence was not reconstructed; this is an UNRESOLVED source-version issue, not evidence for target loss or bad node placement. Human descendant evidence is valid ancestral grounding. ARBA predicates and current InterPro mapping internals were not inspected and are marked accordingly rather than described as fully audited.

Mouse Q91Y97/ENSMUSP00000029987 donor provenance was traced through the [MGI Aldob comparative graph](https://www.informatics.jax.org/homology/GOGraph/Aldob), generated 2023-03-10. Activity evidence includes [PMID:25637246] (primary knockout abstract read). Fructose-catabolism evidence is PMID:29533924 IMP and PMID:4343087 IDA. The [full JCI PMID:29533924 study](https://www.jci.org/articles/view/94427) tests Aldob-deficient mice and upstream Khk interventions, with fructose-phosphate/ATP phenotypes; the KHK assay is not an ALDOB assay. [PubMed PMID:4343087](https://pubmed.ncbi.nlm.nih.gov/4343087/) confirms the older mouse study identity and explicitly has no abstract; its original biochemical attribution remains unresolved. Human purified-enzyme measurements independently establish the accepted target functions.

The liver-interactome [erratum PMID:29254952](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740501/) is already genuinely cached; it corrects author Juncheng Wei's name, not interaction data. Local `full_text_unavailable` flags reflect actual cache metadata. The BioPlex PMID:33961781 cache contains partial full sections but omits pair-level supplements; its true availability flag does not imply all experimental evidence was inspected. All original reference titles and IDs are preserved.

The live Reactome events [R-HSA-5656438](https://reactome.org/content/detail/R-HSA-5656438) and [R-HSA-70342](https://reactome.org/content/detail/R-HSA-70342) were read and explicitly specify human cytosol. The former is a mutant-loss event and is not used as a positive WT activity assay. Cached R-HSA-71495/71496 establish the opposite directions of the common aldol reaction; their isozyme-equivalence prose is not extended to F1P specificity.

No NEW assertion is proposed: the two established reaction activities, their seeded pathways, cytosol and homomeric assembly already cover core chemistry. The specific adaptor, ATPase-binding and assembly assertions also already exist. A `gocams/index.tsv` lookup found no P05062 activity entry; this is not used to infer a missed process. The live adaptor definition supports a coordinated ternary scaffold; the free-fructose definition was checked separately. No new ontology identifier was invented.

### Required cache recovery and checks

Missing publication records after normal fetch: **PMID:25637246, PMID:29533924, PMID:4343087, PMID:41188550**. Logs `/tmp/ALDOB-additional-fetch.log` (terminal 1/3 because PMID:29254952 was already cached; two DNS failures) and `/tmp/ALDOB-mouse-source-fetch.log` (terminal 0/2, DNS failures). Missing events: **Reactome:R-HSA-5656438 and Reactome:R-HSA-70342**, both terminal False/DNS in `/tmp/ALDOB-fetch-reactome.log`. All six are required draft gates; no standard cache was hand-authored or altered. PMID:4343087's provisional title typography must be compared with the genuine fetched metadata on recovery.

The quote check is case-sensitive after whitespace normalization. The single external Methods excerpt above has a retained manual provenance receipt, distinct from a publication cache. Original source-field/isoform/reference preservation, immutable GOA/UniProt hashes, no-alias YAML, trailing whitespace, targeted validation, history validation and rendering are checked before the final manifest. The parent independently reviews the final biological draft before publication.

Final targeted validation passed with two warning groups: four missing PMID caches, and the intentional source-specific ACCEPT/UNDECIDED split for GO:0004332 (unresolved PMID:6696436 attribution versus independently supported enzyme records). The two missing Reactome records are separately tracked draft gates even though that validator did not report them. History validation and rendering passed. No NEW rows, source-object edits, cache edits or Git mutations were made.

Parent independent review accepted the full biological draft and requested that the unrecovered ALDOB exosome hit remain UNDECIDED. That source-specific change was applied without changing the seeded assertion. All 53 decisions, the two cores, reference assessments and correction scopes received independent parent review; the final one-row delta was returned for publication inspection.

## 2026-09-27 source6 recovery and PR #3279 follow-up

All five canonical gene files matched the current published head
`74cbc1ede513e7f16dfd053df2a63a64ccd1aa5d` before editing. Formal review
5329496575 and detailed comment 5854101760 were read in full. This follow-up
preserves every original source assertion, all 53 actions, both catalytic cores
and the existing experimental uncertainties.

The six source6 records were imported by the parent as exact normal-fetcher
bytes after archive, source, identity, fresh-main absence and no-overwrite checks.
Source run 36297910960, head `41e41a94fb65b65ddc78627208d955fa1e7eb1c7`, and
`tmp/source6-canonical-import-receipt.json` identify the recovery. The preceding
six missing-cache gates are now closed; source availability is still limited:

- PMID:25637246 and PMID:29533924 contain research abstracts, not full bodies.
  Their mouse knockout and upstream KHK intervention results corroborate the
  donor physiology already assessed. They do not replace direct human enzyme
  measurements or assign KHK catalysis to ALDOB. Exact abstract excerpts are now
  attached to their findings.
- PMID:4343087 and PMID:41188550 are bibliographic-only despite their Abstract
  headings. The older mouse paper's exact gene/assay attribution remains
  UNVERIFIED; its provisional title is replaced by the actual machine-fetched
  isotope typography. The correction's previously inspected publisher notice
  still supplies the bounded image-replacement assessment; the recovered record
  alone does not reveal that notice body.
- Reactome:R-HSA-5656438 and Reactome:R-HSA-70342 contain human event summaries.
  The first is defective-enzyme context; the second directly states cytosolic
  tetrameric ALDOB and F1P cleavage. The existing positive compartment decision
  and two substrate-specific cores are retained. No additional bibliography
  entry merely mentioned by a Reactome summary is promoted to an independent
  supporting source without inspecting it.

The original full BBS paper and V-ATPase paper were recovered again at the author
URLs above. Figure 3 and adjacent Results in PMID:18000879 distinguish peripheral
MTOC association from overlap with the gamma-tubulin marker. The three
compartment rows now attach a short exact Figure 3 excerpt using
`supporting_text_fulltext`, replacing the uninformative coIP abstract quote.
Methods/Results and Figures 2, 3 and 6 of PMID:17576770 establish human A318E and
R303W constructs in yeast and the binding-versus-catalysis distinction. The two
contextual assembly/binding rows now attach short exact external excerpts.
Manual access receipts reside in `tmp/ALDOB-source6-followup/external-evidence.json`;
the normal caches are untouched and remain marked full-text unavailable. The
prior full JBC Methods/Results read for PMID:10625657 was complete for the
substrate assays, not an inference from an abstract or a partial-paper absence.

The local ALDOA and PFKM review reasons were inspected read-only. Several accept
free-fructose binding using F1,6BP/F6P evidence; PFKM calls F6P binding more
specific, although it lies on the carbohydrate-derivative branch rather than
under the free monosaccharide term. A suggested question now flags these
source-specific judgments and the shared ARBA00092505 rule for a separate
primary-evidence review. Neither other gene was edited or automatically judged
incorrect from corpus agreement/disagreement.

The local `rules/arba/rules_data.json` summary is now inspected: ARBA00092505
lists one condition set, taxon/FunFam condition types, aldolase FunFam
3.20.20.70:FF:000021 and GO:0070061. ARBA00043337 and ARBA00087539 also have
summaries, while ARBA00035055 is absent. These summaries lack the complete
grouped taxon predicates and training annotations, so they do not resolve every
source-status uncertainty as the reviewer suggested. The propagation comments
now distinguish inspected summary fields from unresolved exact derivation.

The generic G6PD/TP53 IPI row still recommends MODIFY to the already-supported
adaptor MF because this is positive functional refinement of an existing source
assertion. The separately seeded adaptor row is IDA, so the source tuples are
not identical; no extra row or NEW coverage is manufactured. The exosome HDA
remains UNDECIDED because its target-specific supplementary hit is unrecovered.
Other genes' majority actions cannot supply this missing evidence or justify a
contamination claim. The two catalytic/process rows cited to PMID:9244396 retain
their independent human enzyme support and no longer attach its unrelated
cytoskeleton-preference quotation.

The recursive authored-source census still contains 19 required PMIDs and six
Reactome records, all now present. No provider report or hidden provider-only
bibliography exists for this gene. Original PDF/author URLs are mapped to their
already cited primary records; no novel DOI-only citation or new fetch request
is introduced. DRAFT is retained while the intentional GO:0004332
source-specific ACCEPT/UNDECIDED validation advisory remains. Current-head
review and required CI are separate from local cache closure.


## 2026-09-27 — public full-text excerpt representation

This field-scope correction is based on exact PR #3279 head `b2e55f8b282aa52332b17cb5f20b68a20e155137`, with all five canonical files independently matched before editing. It supersedes the earlier use of `supporting_text_fulltext` for six public-article excerpt occurrences. That schema field is reserved for full text that cannot be publicly shared, not for a public article whose normal local cache is abstract-only. The unchanged excerpts below are attributed source-access receipts; these notes are **not an independent study** and do not turn an external read into a full publication cache.

- [PMID:18000879], [original author article](https://www.researchgate.net/publication/5845874_Novel_interaction_partners_of_Bardet-Biedl_syndrome_proteins), Figure 3 caption, read with the adjacent Results and Discussion: “ALDOB and EXOC7 associate peripherally with the MTOC”. The original human full-length constructs were expressed in HeLa cells; peripheral centrosomal association and the qualified satellite interpretation are distinct from an endogenous hepatocyte function. This same excerpt supports the three existing compartment judgments and is not counted as three independent experiments.
- [PMID:17576770], [original author article](https://www.researchgate.net/publication/6259929_Physical_Interaction_between_Aldolase_and_Vacuolar_H-ATPase_Is_Essential_for_the_Assembly_and_Activity_of_the_Proton_Pump), Results around Figure 2: “wild-type human aldolase B restored V-ATPase assembly”. Figure 3A caption: “yeast cells were transformed with the pYES3/CT plasmid harboring the human aldolase B mutant, A318E.” These are human ALDOB constructs in a yeast host, with binding and catalytic controls; ALDOB is not assigned proton-pumping chemistry. The two unchanged excerpts retain the previously reviewed assembly/binding context.
- [PMID:10625657], [original JBC PDF](https://genetyca-icm.com/wp-content/uploads/2018/03/Expression-purification-and-characterization-of-natural-mutants-of-human-aldolase-B.-Role-of-quaternary-structure-in-catalysis..pdf), journal page 1146, Methods: “Aldolase cleavage activity toward the substrates fructose 1-phosphate and fructose 1,6-bisphosphate was assayed”. The original human wild-type/variant enzymes were expressed in E. coli; these phosphate-substrate assays are not a free-fructose binding assay. The previously reviewed substrate judgment is unchanged.

The original PMID identities, all 53 immutable source assertions and all review judgments, actions, core functions and alternative-product data remain unchanged. Existing ordinary cache excerpts stay attached to their PMIDs. The six public excerpts now use ordinary `supporting_text` against this explicitly attributed notes receipt; the original articles remain the primary evidence. Full-text availability for the normal publication caches is unchanged. The notes-file reference describes its documentary role and is not a replacement publication or additional independent experiment. No source cache, provider output or published history was edited, and no new source was introduced. Validation, history, rendering and exact preservation checks accompany the four-file manifest.


## 2026-09-27 direct primary attribution

The public excerpts documented above remain external-reading receipts with original page/figure locations and retrieval URLs. The evidence objects now name the original PMIDs directly: [PMID:18000879] on the three compartment rows, and the already present [PMID:17576770] and [PMID:10625657] entries on the other three. Exact excerpts available in the unmodified machine caches remain attached. The notes are no longer used as a proxy for automatic primary-quote verification. This supersedes the preceding representation; it does not remove or independently corroborate the public readings. No full-paper sharing or copyright conclusion is inferred from public accessibility. The specialized full-text field is left unused here; the access limitation is recorded explicitly.

The description now says cytoskeleton without the unsupported actin-specific modifier. The source's liver-cytoskeleton preference remains the supported scope; ALDOA actin experiments are not transferred. All 53 annotation decisions and both catalytic cores are unchanged. The existing source-specific GO:0004332 advisory remains intentional, so the review YAML remains DRAFT with all required records cached.

## 2026-09-27 reference-assessment wording correction

At exact PR #3279 head `0b767b1afd247d58bbc7d72a17fddc6ab3ba80ee`, two reference assessments still described the earlier excerpt representation. The [PMID:18000879] assessment now accurately states that the three compartment rows cite the primary PMID directly with an explicit local full-text limitation; the public Figure 3 receipt remains separately documented above. The [PMID:17576770] assessment now distinguishes the exact cached abstract quotations attached to the assembly and ATPase-binding rows from the public full-text excerpts and figure locators retained in these notes. Both normal publication caches remain abstract-only. This corrects attribution prose without changing the previously reviewed experiments or claiming new full-text retrieval.

All 53 complete annotation objects, both core functions, reference identities and source bytes are unchanged. No citation or evidence attachment is added or removed, and the existing source-specific GO:0004332 advisory remains intentional. The earlier frozen manifest and published histories remain unchanged; the new history and follow-up manifest record focused validation and rendering.

Focused schema, reference, best-practices and GOA validation passed with only that existing advisory. Exact comparison against the published head confirms the two reference prose fields are the only YAML changes and all 25 required publication/Reactome records remain byte-identical. Ontology validation was not repeated because no term object changed. Rendering and the new history record were checked separately.
