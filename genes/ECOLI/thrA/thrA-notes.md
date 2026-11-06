# thrA annotation-review notes

## 2026-10-26 complete native-function review

All 21 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

ThrA has two activities on one polypeptide: aspartate kinase and homoserine dehydrogenase (PMID:4364333 genetic cistrons are historical functional subdivisions, not two separate modern gene products). PMID:11368768 assays pathway enzyme kinetics; normal cache is abstract-only. PMID:204643 directly measures a concentration-dependent dimer/tetramer equilibrium in threonine and reports both forms retain dehydrogenase activity; the inactive monomer was produced by chaotropic treatment. Retain specific self-binding and tetramer assembly as non-core rather than general protein-binding removal.

The current QuickGO definition of GO0004412 names NADP+ specifically, whereas GO0004022 is alcohol oxidation with NAD+. The normally fetched UniProt record separately curates NADP(H) and NAD(H) reactions by similarity to Arabidopsis Q9SA18. Retain the original NAD-dependent alcohol-dehydrogenase and NAD-binding rows as non-core inferred cofactor usage; do not replace them with the NADP-specific term and lose the NAD claim, and do not infer ethanol turnover. No direct target comparison establishing equal physiological NAD/NADP use was recovered. Only kinase and NADP-homoserine chemistry are highlighted as cores. Generic oxidoreductase refinement includes both existing specific activities.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-thrA-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## PR #5569 source-specific corrective review (2026-10-26)

Live QuickGO definitions checked on 2026-10-26: GO:0004022 explicitly uses NAD+; GO:0004412 explicitly uses NADP+. Homoserine is a primary alcohol, so its NAD-dependent oxidation fits GO:0004022 without implying ethanol metabolism or substrate promiscuity. Both can refine their common broad oxidoreductase ancestor. Retain the NAD-dependent catalytic capacity as core across all four enzymes, while distinguishing directly measured yeast kinetics from conserved inference in other targets. Missing native cofactor comparisons limit claims about physiological preference, not the biological centrality of the supported homoserine reaction. Earlier fungal MODIFY to GO:0004412 erased the cofactor distinction and is superseded. Sources: https://www.ebi.ac.uk/QuickGO/term/GO:0004022 and https://www.ebi.ac.uk/QuickGO/term/GO:0004412 .

Action changes: the existing NAD-dependent alcohol-dehydrogenase and NAD+ binding assertions change from KEEP_AS_NON_CORE to ACCEPT, because both describe integral catalytic properties of the homoserine reaction. Evidence limitations are recorded separately from core status.

All 21 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

The N-terminal ATP-dependent kinase and C-terminal homoserine dehydrogenase are distinguished. PMID:11368768 provides integrated E. coli pathway kinetics; PMID:204643 measures a dimer–tetramer equilibrium with active forms, not a mandatory single oligomer. NAD-dependent GO:0004022 remains ACCEPT and is not replaced by the NADP-specific sibling. Plant donor chemistry does not transfer chloroplast localization or allosteric regulation.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged.


## 2026-11-01 bacterial aspartate-to-threonine audit follow-up

Re-read the existing COMPLETE review and every annotation decision for the narrower bacterial route audit. Retained all annotation actions, machine-sourced payloads, standalone description, core functions and raw records. Added manual assessments and verbatim findings to existing references, distinguishing native experiments from comparative synthesis, bibliographic-only records and inference. No new annotation rows were proposed.

ThrA retains separate N-terminal aspartate-kinase and C-terminal homoserine-dehydrogenase functions. The intervening Asd step remains required: the fusion neither bypasses aspartyl-phosphate reduction nor establishes channeling. PMID:4364333 identifies two functions within one polypeptide. The module may reuse that protein for steps 1 and 3, with Asd at step 2.

PMID:204643 directly reports: "Both the dimeric and tetrameric forms of the enzyme possess dehydrogenase activity." This is condition-dependent assembly, not an invariant tetramer. Both domain activities are threonine-regulated. The NAD(H) reaction and NAD+ binding remain accepted as curated conserved catalytic capacity, supported by UniProt orthology to Q9SA18 rather than a native NAD/NADP preference assay. NADP-specific GO:0004412 is not a replacement for NAD-specific GO:0004022; no equal cofactor use is asserted.

Acquisition and evidence limits: `just mod-description-deep-research ECOLI thrA metL lysC asd thrB thrC` completed with all six skipped because no MOD provider is configured for ECOLI. A fresh normal Falcon request for ECOLI thrA failed with the shared Edison authentication/access 403; the same failed service was not retried for the other five. Earlier actual provider attempts remain documented above. No provider report was fabricated or rewritten. Manual review used existing primary-publication and curated UniProt caches. Logs are in the ignored `.cache/module-audit-logs/bacterial-threonine-ecoli/` directory.

PMID:11368768 supports the native route, but its nominal full-text HTML cache contains a duplicated abstract and PDF link rather than the full paper. The coordinating agent's normal PDF retrieval also returned an HTML interstitial. No unseen kinetic measurements or exact strain details are attributed to that abstract. Native proteomics annotations retain the caveat that individual target supplement rows were not independently reconstructed. Raw UniProt PANTHER membership and the official `interpro/panther/panther.obo` label were checked for module selectors; membership alone does not establish every family's substrate or regulatory specificity.


## PR #5858 round 1 — cofactor definition and cross-gene evidence

Live QuickGO was rechecked at 2026-11-01T21:55:53.814183+00:00:

> Catalysis of the reaction: L-homoserine + NADP+ = L-aspartate-4-semialdehyde + NADPH + H+.

Source: [QuickGO GO:0004412](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004412). The same definition is committed in [the module audit GO terms](../../../analysis/module_audits/bacterial_aspartate_to_threonine_biosynthesis/go-terms.yaml); the fresh response is saved in the ignored `pr5858-hom-cofactor-followup/GO_0004412-live.json` log. GO's definition here is NADP+, not NAD(P)+. The broader EC 1.1.1.3 grouping does not override this explicit GO reaction definition.

The three GO:0004022 decisions reflect different inspected evidence, not different interpretations of that definition:

| Target | Evidence behind its NAD-linked RHEA:15757 reaction | Decision and limit |
| --- | --- | --- |
| ECOLI ThrA P00561 | Curated ECO:0000250 transfer from Q9SA18 | ACCEPT conserved NAD-linked capacity; no matched native cofactor preference assay. ECO:0000250 is sequence-similarity evidence and does not itself prove strict orthology. |
| CORGL Hom P08499 | ECO:0000269 attached to PMID:1743520 and PMID:4394351; citation/strain/cofactor scope only partly inspectable | UNDECIDED; recovered4394351 demonstrates NADPH chemistry in B.flavum No2247, while1743520 is abstract-only and cannot exclude or establish NADH use. |
| PSEPK Hom Q88MU8 | NAD reaction supported only by ARBA:ARBA00049031; independent RuleBase/PROSITE/PIRSR support Hom with NADP/NADPH contacts | MODIFY to GO:0004412 is an explicit target-specific cofactor correction, not a claim that this term preserves NAD chemistry or that native NAD use was disproved. |

These decisions are cross-referenced in the respective review reasons. The evidence code alone does not dictate the outcome: the reaction provenance, inspected source content, independent family/cofactor features and remaining uncertainty do. No native purified NADH/NADPH preference measurements are invented.
