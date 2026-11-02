# hom curation notes

Current UniProt assigns EC 1.1.1.3 and marks RHEA:15759 as the physiological
direction, reducing aspartate 4-semialdehyde with NADH. However, its predicted
binding features and GOA specify NADP(H), an unresolved record-level cofactor
inconsistency. Q88MU8 has a C-terminal ACT domain, not an aspartate kinase
catalytic domain. Its pathway contribution is shared with methionine.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. A normal Falcon attempt returned HTTP 403 Failed to authenticate; no fabricated report was written. Manual literature and curated-source review supplied the fallback.

The earlier NADH-only description and replacement of NADP binding were unjustified. The raw NAD-linked reaction is supported only by ARBA; independent RuleBase homoserine-dehydrogenase family membership, PS01042 and PIRSR000098-2 NADP contacts (9–16) and NADPH contact (103) support the current NADPH-capable functional inference. Live QuickGO confirms GO:0004412 itself is NADP-linked and GO:0050661 includes NADP+ or NADPH. Neither the binding term nor the inferred activity claims exclusive donor preference. NADH remains possible; its native kinetic contribution is unresolved.

PMID:4391829 is comparative pseudomonad/coliform work: “either nicotinamide adenine dinucleotide (NAD) or nicotinamide adenine dinucleotide phosphate can serve as a cofactor for this enzyme”, with widely varying relative activities. That is a warning against universal donor or regulatory transfer, not an exact KT2440 paralog assay. PMID:5441405 is bibliographic only; 1970 strain/locus remain unresolved. PMID:29636528 studies Sulfolobus tokodaii, not KT2440, and is not transferred as native cofactor kinetics.

PMID:40236303 native Hom overproduction did not increase threonine in the tested engineered context. The supplement hom_nhe_R primer encodes terminal RVEQLN of Q88MU8, not Q88Q34. The supplementary 46.2-kDa size is consistent with the long Hom construct. This establishes which paralog was cloned, not native allostery or purified catalysis. The ACT domain supports regulatory potential, not a measured threonine feedback mechanism.

The inherited authored GO:0071266 NEW row is archived in full at hom-source-analysis/retired-new-annotations.yaml and retired from the active review. Live QuickGO defines this process as forming methionine from simpler components including aspartate or homoserine; shared precursor enzymes can therefore participate. The issue is insufficient independent support for this particular extra native assertion, not exclusion by definition. Its parents include amino-acid biosynthesis (GO:0008652), sulfur amino-acid biosynthesis and methionine biosynthesis. Existing annotations/cores were checked for overlapping methionine terms. Exact-term QuickGO comparator queries on E. coli ThrA P00561 and MetL P00562 returned zero; this is a convention warning, not proof of false biology. No cached GO-CAM index hit was found for these three targets. Shared methionine precursor biology remains in prose; no replacement NEW ancestor/descendant is proposed. Query responses are preserved in the ignored audit logs.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.

Direct DOI full-text access was attempted for the relevant historical 1970 papers and the 1992 P. aeruginosa paper using the web tool on 2026-11-01; the URLs were inaccessible. No unavailable experimental detail was invented.


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
