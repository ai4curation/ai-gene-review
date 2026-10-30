# FKRP source evidence, context coverage and experimental boundaries

The curated model is a Golgi-associated second ribitol-phosphate transfer step on alpha-dystroglycan. Evidence access and biological scope are kept separate: a trusted curated localization can remain valid when its exact original experiment is not recoverable, provided independent target evidence supports it. The source TSV and all non-review seed fields remain unchanged. No new publication quotations are authored.

## Primary evidence

| Source | Evidence actually available | Interpretation and limit |
| --- | --- | --- |
| [PMID:26923585](https://pubmed.ncbi.nlm.nih.gov/26923585/) | Verified primary abstract in exact-main cache | Sequential FKTN/FKRP RboP transfer using CDP-ribitol. Full original Methods and specific localization assay were not inspected. |
| [PMID:27194101](https://pmc.ncbi.nlm.nih.gov/articles/PMC4873967/) | Full Results and construct Methods | Radiolabeled ribitol and phosphate transfer with heat/acceptor-omission controls; reported exclusion of FKTN contamination. Mouse enzymes and rabbit dystroglycan fragments in human host cells. The exact attachment site and second-step specificity require complementary studies. |
| [PMID:31949166](https://pmc.ncbi.nlm.nih.gov/articles/PMC6965139/) | Full primary XML/normal cache, Results and Methods | Human soluble 45–495 FKRP and separate Asn33-start assay constructs. Protomer pairs recognize distinct phosphate groups; acceptor O-Man6-phosphate is required in the tested reaction. Tetramer observed in crystal/SEC-SAXS, physiological significance unresolved. Terminal acceptor ribitol lacked resolved density. Mg/Mn support activity in vitro; cellular metal unestablished, structural zinc distinct. |
| [PMID:29884773](https://pmc.ncbi.nlm.nih.gov/articles/PMC6078450/) | Abstract-only normal cache plus separately recovered official full HTML | Soluble Myc-tagged enzyme assays support sequential acceptor specificity and lower-efficiency glycerol-phosphate transfer/CDP-glycerol inhibition in vitro. Construct origins refer to the earlier paper; not every insert species independently reconstructed. This study supports the donor-specificity boundary in the accepted phosphotransferase reason and a dedicated question. No new physiological regulation or extracellular-catalysis annotation follows. |
| [PMID:25279699](https://elifesciences.org/articles/03941) | Full Results, Table 1/Fig 1 caption and cloning Methods | Human patient fibroblasts retain DGFc340 phosphorylation but fail LARGE bypass. Localization uses mouse Fkrp pTW323 in HEK293T; human FKTN is pTW322. Human host is not evidence of human insert species. |
| [PMID:27601598](https://pmc.ncbi.nlm.nih.gov/articles/PMC5098040/) | Abstract-only normal cache; separate full HTML and Figures 6–7 read in independent consultation | Human tagged-protein co-IP in HEK293T supports association. HCT116 knockout glycoforms are separate: two RboP residues can occupy two core M3 sites, and extended tandem RboP was detected in HEK293T rather than WT HCT116. Alternative donor/assembly models are hypotheses. Reporter species not independently established. |
| [PMID:29477842](https://pubmed.ncbi.nlm.nih.gov/29477842/) | Verified abstract plus [author-deposited doctoral summary](https://da.lib.kobe-u.ac.jp/da/kernel/D1007246/D1007246y.pdf), not journal full text | Tagged triple co-IP and GM130 colocalization; expressed TMEM5 recovers FKTN/FKRP activities. Endogenous FKRP protein was not independently detected in the summary immunoblot. Exact insert species, full Methods, stoichiometry and channeling unestablished. |
| [PMID:21886772](https://pmc.ncbi.nlm.nih.gov/articles/PMC3160285/) | Full original text | Endogenous control human rectus femoris double-immunogold localization, two peptide antibodies, MG160 overlap. PDI and beta-dystroglycan patterns differ in this specimen. Separate human tagged COS7/BHK21 and truncation experiments support oligomerization. No universal exclusion of other pools. |
| [PMID:15213246](https://pubmed.ncbi.nlm.nih.gov/15213246/) | Abstract-only normal cache; [original scanned article](https://mhlw-grants.niph.go.jp/system/files/2004/043141/200400741B/200400741B0016.pdf), journal pages 709–712, PDF pages 7–10 visually read | Endogenous differentiated human myotubes, mouse C2C12 and normal human muscle biopsy support rough ER with calnexin/BiP patterns. COS myc construct is separate antibody validation. Partial Golgi overlap and sample differences prohibit absolute localization claims. |
| [PMID:17554798](https://pubmed.ncbi.nlm.nih.gov/17554798/) | Verified abstract; original full Methods unavailable | Explicitly normal human/mouse Golgi localization and mutant ER retention. Exact tags and endogenous-versus-expressed preparations not fully established. |
| [PMID:19900540](https://pubmed.ncbi.nlm.nih.gov/19900540/) | Verified abstract; original full Methods unavailable | CHO-medium secretion and mutation-dependent differences. Exact species/tags and endogenous tissue secretion unresolved. E310X is a pathogenic truncation, not a natural alternative product. |
| [PMID:17452335](https://pubmed.ncbi.nlm.nih.gov/17452335/) | Abstract-only normal cache plus [original author manuscript](http://www.physiology.uiowa.edu/campbell/Publications/pdf/363%20beedle.pdf) | Endogenous mouse surface localization with two epitope antibodies, peptide competition and no-primary control; no Fkrp-null specificity control. Recombinant mouse constructs and native DGC co-enrichment corroborate association, not direct binary contact or surface catalysis. |

## Curated and ontology evidence

The four exact-main Reactome records R-HSA-9940735, R-HSA-9940756, R-HSA-9940805 and R-HSA-9948070 were read for the FKRP Golgi context. Their FKTN, FKRP, RXYLT1 and assembly events are distinct. A partner reaction or modeled assembly dependency is not assigned to FKRP. The source GO_REF:0000052 HPA IDA is trusted corroboration; no independent HPA image or antibody audit was performed. The broad cytoplasm donor Q8CG64 is mouse Fkrp; its original donor experiment was not replayed. Cytoplasm includes organelles and is not synonymous with soluble cytosol. Fresh official GO paths establish Golgi membrane part_of Golgi apparatus part_of cytoplasm. Both cytoplasm rows are therefore TOO_GENERAL beside accepted target Golgi annotations; this judges term precision without rejecting either source or excluding additional intracellular pools.

Official QuickGO confirms the substituted-phosphate scope of GO:0016780 and the later-extension scope of GO:0035269. GO:0047356 is not substituted on the strength of its ribitol-containing name; the polymer-reaction interpretation is left as a question. For all three IBAs, the original IBD node PTN001007059 lies on the actual Q9H9S5 lineage in the complete 102-node PTHR13627 topology. Human experimental seeds are legitimate. Separate retrieval dates are preserved rather than claiming that topology, IBD and QuickGO are a single synchronized release.

## Every original context

Stored review indices below are zero-based. There are 35 stored decisions (25 ACCEPT, 8 KEEP_AS_NON_CORE, 2 TOO_GENERAL), covering 36 original contexts (26 ACCEPT, 8 KEEP_AS_NON_CORE, 2 TOO_GENERAL). The one pair shares all seed-represented fields and is not manually duplicated. The immutable 36-row TSV retains both assigned-by values.

| QuickGO context | Assigned by | Stored index | Term / evidence / original source | Decision |
| --- | --- | --- | --- | --- |
| UniProtKB:Q9H9S5!357933252 | UniProt | 11 | GO:0005515 / IPI / PMID:27601598 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933253 | UniProt | 12 | GO:0005515 / IPI / PMID:29477842 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933254 | GO_Central | 23 | GO:0016780 / IBA / GO_REF:0000033 | ACCEPT |
| UniProtKB:Q9H9S5!357933255 | UniProt | 24 | GO:0016780 / IDA / PMID:26923585 | ACCEPT |
| UniProtKB:Q9H9S5!357933256 | UniProt | 25 | GO:0016780 / IDA / PMID:27194101 | ACCEPT |
| UniProtKB:Q9H9S5!357933257 | UniProt | 26 | GO:0016780 / IDA / PMID:29477842 | ACCEPT |
| UniProtKB:Q9H9S5!357933258 | UniProt | 27 | GO:0016780 / IDA / PMID:31949166 | ACCEPT |
| UniProtKB:Q9H9S5!357933259 | IntAct | 32 | GO:0042802 / IPI / PMID:31949166 | ACCEPT |
| UniProtKB:Q9H9S5!357933260 | GO_Central | 28 | GO:0035269 / IBA / GO_REF:0000033 | ACCEPT |
| UniProtKB:Q9H9S5!357933261 | UniProt | 30 | GO:0035269 / IMP / PMID:25279699 | ACCEPT |
| UniProtKB:Q9H9S5!357933262 | ComplexPortal | 29 | GO:0035269 / IDA / PMID:29477842 | ACCEPT |
| UniProtKB:Q9H9S5!357933263 | UniProt | 33 | GO:0051262 / IDA / PMID:31949166 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933264 | GO_Central | 3 | GO:0000139 / IBA / GO_REF:0000033 | ACCEPT |
| UniProtKB:Q9H9S5!357933265 | UniProt | 6 | GO:0000139 / IEA / GO_REF:0000044 | ACCEPT |
| UniProtKB:Q9H9S5!357933266 | UniProt | 0 | GO:0000139 / EXP / PMID:17554798 | ACCEPT |
| UniProtKB:Q9H9S5!357933267 | UniProt | 1 | GO:0000139 / EXP / PMID:21886772 | ACCEPT |
| UniProtKB:Q9H9S5!357933268 | UniProt | 2 | GO:0000139 / EXP / PMID:25279699 | ACCEPT |
| UniProtKB:Q9H9S5!357933269 | UniProt | 4 | GO:0000139 / IDA / PMID:26923585 | ACCEPT |
| UniProtKB:Q9H9S5!357933270 | UniProt | 5 | GO:0000139 / IDA / PMID:29477842 | ACCEPT |
| UniProtKB:Q9H9S5!357933271 | ComplexPortal | 5 | GO:0000139 / IDA / PMID:29477842 | ACCEPT |
| UniProtKB:Q9H9S5!357933272 | Reactome | 7 | GO:0000139 / TAS / Reactome:R-HSA-9940735 | ACCEPT |
| UniProtKB:Q9H9S5!357933273 | Reactome | 8 | GO:0000139 / TAS / Reactome:R-HSA-9940756 | ACCEPT |
| UniProtKB:Q9H9S5!357933274 | Reactome | 9 | GO:0000139 / TAS / Reactome:R-HSA-9940805 | ACCEPT |
| UniProtKB:Q9H9S5!357933275 | Reactome | 10 | GO:0000139 / TAS / Reactome:R-HSA-9948070 | ACCEPT |
| UniProtKB:Q9H9S5!357933276 | UniProt | 14 | GO:0005576 / IEA / GO_REF:0000044 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933277 | UniProt | 13 | GO:0005576 / IDA / PMID:19900540 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933278 | UniProt | 16 | GO:0005737 / ISS / GO_REF:0000024 | TOO_GENERAL |
| UniProtKB:Q9H9S5!357933279 | UniProt | 15 | GO:0005737 / IEA / GO_REF:0000044 | TOO_GENERAL |
| UniProtKB:Q9H9S5!357933280 | UniProt | 18 | GO:0005791 / IEA / GO_REF:0000044 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933281 | UniProt | 17 | GO:0005791 / IDA / PMID:15213246 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933282 | HPA | 19 | GO:0005794 / IDA / GO_REF:0000052 | ACCEPT |
| UniProtKB:Q9H9S5!357933283 | UniProt | 20 | GO:0005794 / IDA / PMID:19900540 | ACCEPT |
| UniProtKB:Q9H9S5!357933284 | UniProt | 21 | GO:0005794 / IDA / PMID:25279699 | ACCEPT |
| UniProtKB:Q9H9S5!357933285 | UniProt | 22 | GO:0005794 / IDA / PMID:29477842 | ACCEPT |
| UniProtKB:Q9H9S5!357933286 | UniProt | 31 | GO:0042383 / IEA / GO_REF:0000044 | KEEP_AS_NON_CORE |
| UniProtKB:Q9H9S5!357933287 | ComplexPortal | 34 | GO:1902494 / IDA / PMID:29477842 | ACCEPT |

## Review follow-up

The two cytoplasm actions were refined after PR review using the official part_of path, with no change to their source contexts. The existing metal question now explicitly records why no GO:0000287 annotation is proposed: Mg and Mn support activity in vitro, while the physiological catalytic metal remains unresolved and structural zinc is distinct. The accepted broad Golgi locations and ontology-specificity question are retained; no speculative subcompartment annotation or new term is added.
