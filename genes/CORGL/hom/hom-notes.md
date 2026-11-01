# CORGL hom research notes

## 2026-11-01 — NADPH chemistry, feedback and strain boundaries

P08499 is the reviewed ATCC13032 standalone homoserine dehydrogenase (taxon196627; PTHR43331 HOMOSERINE DEHYDROGENASE, SF1 same). The sequence record integrates historical corynebacterial work from other strains. In particular, PMID:2835591 hom-thrB operon sequencing is assigned by UniProt to ATCC13059. Its abstract says the genes encode two separate polypeptides, supporting standalone architecture rather than an aspartokinase/Hom fusion.

PMID:1743520 abstract reports wild-type C.glutamicum threonine inhibition (Ki0.16mM) and an engineered frameshift/deletion mutant with markedly reduced inhibition. The full ScienceDirect endpoint returned403. The abstract neither identifies ATCC13032 nor resolves cofactor preference. PMID:1902466, also abstract-only despite the PMC landing URL, documents a different feedback-resistant mutation G378E. Neither mutant is the unmodified native enzyme. The recovered PMID:4394351 paper is B.flavum No2247, not ATCC13032. Its full primary J-STAGE PDF establishes NADPH chemistry, substrate/product inhibition and threonine feedback using a partially purified preparation; it explicitly notes small amounts of other enzyme activities remaining in FractionIII. It does not demonstrate NADH use. See `hom-source-analysis.md` for canonical paper/manifestation mapping and exact boundary evidence.

QuickGO GO:0004412 currently defines L-homoserine + NADP+ = L-aspartate4-semialdehyde + NADPH +H+. GO:0004022 explicitly uses NAD+, and GO:0070403 is NAD+ binding. The raw UniProt record asserts both NAD- and NADP-linked reactions while citing1743520/4394351. The latter recovered paper supports NADPH only; the former abstract cannot settle NAD specificity. Therefore GO:0004022 and GO:0070403 remain UNDECIDED. They are not removed based on inaccessible text and are not mechanically changed to GO:0004412, which would silently change the cofactor. A purified wild-type ATCC13032 NADPH/NADH comparison is the outstanding question.

The four GO:0004412 rows, including the two experimental rows, are consistently accepted: family identity, corynebacterial enzyme activity/regulation and comparative primary chemistry establish the function. The absence of a full1743520 paper does not erase a clearly corroborated Hom function. Strain-specific source limitations are explicit, not an allegation of wrong-gene experimental curation. NADP binding and threonine/methionine biosynthesis are supported. Broad redox and amino-acid metabolism terms are refined. The conservative native module uses NADPH for Hom and should not present an equally established NADH alternative. All12 seeded rows adjudicated; no NEW.

## Source acquisition and scope

Normal `just fetch-gene` generated the UniProt record, GOA export and seeded review. The 41 original rows across this five-gene panel and all ten raw files were snapshotted before curation. An initial folder-code misunderstanding was corrected to canonical CORGL; the five new folders were moved without changing raw bytes or machine annotation payloads. The original and migrated baselines and an explicit migration record are retained in `.cache/module-audit-logs/bacterial-threonine-corgl-20261101/`.

A normal Falcon research request failed with HTTP403 authentication failure. This is a provider failure, not a research report; no provider-named report was fabricated. The shared authentication failure was not repeatedly retried for the other four genes. The nonhuman MOD-description command was run for all five under canonical CORGL and reported no configured MOD provider. Research below is manual synthesis of immutable primary caches and the reviewed UniProt record.

No raw annotation was removed or rewritten. Ordinary relationship qualifiers played no part in the judgment. No NEW annotation was proposed: the original set and supported refinements already cover the supported biosynthetic functions. No unverified universal bacterial architecture or native production flux is inferred from recombinant protein or engineered production strains.


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

The review suggestion that both cited experimental papers in fact assay NADPH is established only for the recovered1970 full text. The1991 abstract cannot support that conclusion. One structured `source_defects` entry therefore uses `WRONG_REFERENCE`, `confidence: SUSPECTED`, and `requested_change: CHECK` for the RHEA:15757 experimental evidence attachment. It has no corrected_value and is NOT_REPORTED. This is an exportable curator query about attribution, not a confirmed correction, a request to delete the NAD reaction, or an unsupported reassignment of both papers to NADPH-only chemistry. PMID4394351's strain and alternate-PDF identity remain documented in hom-source-analysis.md.
