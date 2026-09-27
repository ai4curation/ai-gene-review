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

Mouse Q91Y97/ENSMUSP00000029987 donor provenance was traced through the [MGI Aldob comparative graph](https://www.informatics.jax.org/homology/GOGraph/Aldob), generated 2023-03-10. Activity evidence includes [PMID:25637246](https://pubmed.ncbi.nlm.nih.gov/25637246/) (primary knockout abstract read). Fructose-catabolism evidence is PMID:29533924 IMP and PMID:4343087 IDA. The [full JCI PMID:29533924 study](https://www.jci.org/articles/view/94427) tests Aldob-deficient mice and upstream Khk interventions, with fructose-phosphate/ATP phenotypes; the KHK assay is not an ALDOB assay. [PubMed PMID:4343087](https://pubmed.ncbi.nlm.nih.gov/4343087/) confirms the older mouse study identity and explicitly has no abstract; its original biochemical attribution remains unresolved. Human purified-enzyme measurements independently establish the accepted target functions.

The liver-interactome [erratum PMID:29254952](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740501/) is already genuinely cached; it corrects author Juncheng Wei's name, not interaction data. Local `full_text_unavailable` flags reflect actual cache metadata. The BioPlex PMID:33961781 cache contains partial full sections but omits pair-level supplements; its true availability flag does not imply all experimental evidence was inspected. All original reference titles and IDs are preserved.

The live Reactome events [R-HSA-5656438](https://reactome.org/content/detail/R-HSA-5656438) and [R-HSA-70342](https://reactome.org/content/detail/R-HSA-70342) were read and explicitly specify human cytosol. The former is a mutant-loss event and is not used as a positive WT activity assay. Cached R-HSA-71495/71496 establish the opposite directions of the common aldol reaction; their isozyme-equivalence prose is not extended to F1P specificity.

No NEW assertion is proposed: the two established reaction activities, their seeded pathways, cytosol and homomeric assembly already cover core chemistry. The specific adaptor, ATPase-binding and assembly assertions also already exist. A `gocams/index.tsv` lookup found no P05062 activity entry; this is not used to infer a missed process. The live adaptor definition supports a coordinated ternary scaffold; the free-fructose definition was checked separately. No new ontology identifier was invented.

### Required cache recovery and checks

Missing publication records after normal fetch: **PMID:25637246, PMID:29533924, PMID:4343087, PMID:41188550**. Logs `/tmp/ALDOB-additional-fetch.log` (terminal 1/3 because PMID:29254952 was already cached; two DNS failures) and `/tmp/ALDOB-mouse-source-fetch.log` (terminal 0/2, DNS failures). Missing events: **Reactome:R-HSA-5656438 and Reactome:R-HSA-70342**, both terminal False/DNS in `/tmp/ALDOB-fetch-reactome.log`. All six are required draft gates; no standard cache was hand-authored or altered. PMID:4343087's provisional title typography must be compared with the genuine fetched metadata on recovery.

The quote check is case-sensitive after whitespace normalization. The single external Methods excerpt above has a retained manual provenance receipt, distinct from a publication cache. Original source-field/isoform/reference preservation, immutable GOA/UniProt hashes, no-alias YAML, trailing whitespace, targeted validation, history validation and rendering are checked before the final manifest. The parent independently reviews the final biological draft before publication.

Final targeted validation passed with two warning groups: four missing PMID caches, and the intentional source-specific ACCEPT/UNDECIDED split for GO:0004332 (unresolved PMID:6696436 attribution versus independently supported enzyme records). The two missing Reactome records are separately tracked draft gates even though that validator did not report them. History validation and rendering passed. No NEW rows, source-object edits, cache edits or Git mutations were made.

Parent independent review accepted the full biological draft and requested that the unrecovered ALDOB exosome hit remain UNDECIDED. That source-specific change was applied without changing the seeded assertion. All 53 decisions, the two cores, reference assessments and correction scopes received independent parent review; the final one-row delta was returned for publication inspection.
