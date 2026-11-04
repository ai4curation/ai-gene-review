# GAN evidence and source guide

Gigaxonin recognizes substrates within CUL3–RBX1 ubiquitin ligase complexes. The review retains 32 original annotation contexts: 16 ACCEPT, three cytoplasm-to-cytosol refinements and 13 removals of uninformative generic protein binding. Removal preserves the positive interaction evidence. No new annotation is proposed.

The [review](GAN-ai-review.yaml) carries the biological judgments and manual reference assessments. The [compact evidence file](GAN-source-evidence.yaml) preserves the original records and their mapping. The [journal](GAN-notes.md) explains the synthesis and source limitations. This guide accompanies the actual native review: all 32 joins, 38 normal sources and six excerpt occurrences have been reconciled.

## Original records and products

`original_contexts.columns` and each corresponding row reconstruct all 32 original QuickGO objects, including null values, literal donor order, dates, assignment and qualifiers. The joins identify the original record, TSV row and offline parser forecast; an actual native index will be recorded only after fetch. There are no negated records or annotation-extension atoms. No inherited GAN review or journal was present at the inspected main.

The official human record is Q9H2C0, a 597-residue displayed sequence; no alternative product is declared. Partner isoform suffixes in interaction annotations identify the reported partner, not a GAN isoform. Engineered fragments and tags are not treated as natural products. In PMID:19818708, the selected original describes a GAN 1–258 construct, whereas the UniProt bibliography gives 1–254; the discrepancy is retained. PMID:37903270's reagent table identifies purchased human GST-gigaxonin but does not establish exact construct boundaries.

## Phylogenetic evidence

The current UniProt classification is PTHR45632:SF17. The incoming PAINT assertions instead resolve through the actual [PANTHER19 PTHR24412 book](https://data.pantherdb.org/PANTHER19.0/books/PTHR24412/tree.tree), its alignment and AN/PTN mapping. Human GAN is AN1997/PTN002521105 with an exact 597-residue sequence. All four assertions originate at AN25/PTN001561260 on its ancestry; the literal IBDs, donor sets and donor mappings are preserved. No target-path negative assertion was found in the retained data. The assertion node's species/age is not inferred. Target self-evidence is legitimate experimental descendant grounding.

The source projection keeps the two family versions distinct. The complete large family book remains private; the portable projection contains the target route and four actual assertions. The normal source plan retains the existing current-family machine files unchanged.

## Primary mechanisms and their limits

- [PMID:37903270](https://pmc.ncbi.nlm.nih.gov/articles/PMC10636361/) supplies the central adaptor mechanism. ROOT read original main Results/Methods and selected supplementary reagent-table material. Reconstitution includes E1, E2, neddylated CUL3–RBX1, human GST-gigaxonin and defined substrates. NEFL, INA, TPM1, TAGLN and CNN2 occur in the purified assay; TPM2's broader cellular evidence is not relabeled as that purified experiment. Modeling, variant effects and binding are distinguished. No autonomous GAN ubiquitin-transfer enzyme is inferred.
- [PMID:12147674](https://pmc.ncbi.nlm.nih.gov/articles/PMC2173828/) was read through extracted original Methods, Results and textual captions. The MAP1B light-chain interaction and neuronal localization are positive. GAN's microtubule association in this study is indirect through MAP1B. PMID:16227972 and PMID:16303566 provide authentic abstract-level MAP1B/TBCB degradation evidence; complete original Methods were not read.
- PMID:15983046 explicitly includes GAN1 in a CUL3-dependent ubiquitination study. Modification of GAN alone is not participation in substrate ubiquitination. The latter claim is independently supported by the reconstitution above. Keap1-specific stress responses are not transferred to GAN.
- PMID:19424503's actual original Discussion reports cytoplasmic GAN-1, with the observation described as data not shown. The ENC1 title does not invalidate that target observation. Cytosol precision also has independent GAN localization and exact Reactome entity support.
- [PMID:26460568](https://pubmed.ncbi.nlm.nih.gov/26460568/) and [PMID:37043392](https://pubmed.ncbi.nlm.nih.gov/37043392/) were read as extracted original main prose, Methods and textual captions, without images or videos. Intermediate-filament association, soluble oligomer accumulation and transport phenotypes inform cytoskeletal homeostasis. They do not establish GAN as a kinesin motor or the proposed unidentified motor adaptor.
- ROOT's selected original reading of PMID:31944090 and PMID:40749357 distinguishes regulation of GAN by glycosylation and NUDCD3 association from a GAN glycosyltransferase or chaperone activity. PMID:27000625 was read as the abstract and figure captions; mouse DRG consequences are not direct human mitochondrial-transport activity.

The manual assessment on each reference records its own reading scope. An available full-text cache does not mean every section or image was inspected. All 38 required normal sources are now present. Actual header flags and extraction methods are retained separately from the selected reading scopes.

## Interaction evidence

The actual original BioPlex 2.0 and 3.0 GAN–NUDCD3 rows and the NDEx U2OS AP-MS target edge are preserved in `interaction_table_rows`, with source hashes and locators. These are positive cellular associations, not purified binding constants. Exact IntAct records separately identify the E1, TBCB, LUMIER, Haenig and 14-3-3 target pairs and assay methods. Original partner identifiers and experimental scope are retained.

The initially missing PMID:15778465 target table was recovered in the [author-uploaded original](https://www.researchgate.net/publication/7957504_Targeted_Proteomic_Analysis_of_14-3-3_a_p53_Effector_Commonly_Silenced_in_Cancer). ROOT read selected Methods, opening Results and the Table I GAN row/caption/footnote. The sequence-coverage percentages support detection; they are not binding magnitudes. Duplicate EGF-condition columns do not represent five independent conditions. This resolved the earlier source uncertainty and supports removing the bare binding term while preserving the positive association.

PMID:25036637's normal cache has a partial extraction despite its full-text flag. Selected recovered original prose and the exact IntAct LUMIER pair are available. Two retained files with spreadsheet names are HTML responses; no spreadsheet-cell verification is claimed. For Haenig and PMID:36931259, curated target records and the authentic abstracts were inspected; complete original target panels/construct sequences were not.

## Reactome and ontology

Five actual event-to-component chains end at human GAN entity [976014](https://reactome.org/content/detail/R-HSA-976014), whose reference is Q9H2C0 and compartment is cytosol. The intermediate sets and relations are retained. Membership supports the compartment; it does not assign GAN the catalytic work of neddylation, deneddylation or CAND1 exchange. Broad pathway bibliography entries do not generate new process annotations.

The sole replacement term is cytosol, with the directly inspected `GO:0005829 part_of GO:0005737` relation. The core describes substrate recognition within the CUL3 complex and its role in proteasomal turnover. Broader accepted cytoskeletal annotations remain visible without being repeated as redundant core entries.

## Current excerpts and native work

Six short primary excerpts anchor distinct claims; they are not duplicated in this guide or the journal. All six excerpts now match genuine normal-cache bytes; four native linebreak adaptations preserve the same words. Genuine native seeding produced all 32 original contexts, matching every one of the 16 export columns and the exact 597-residue sequence. The 38-source inventory contains 20 unchanged main objects and 18 missing-only acquisitions. The initial projected PTHR45632 PAINT filename was absent and is excluded; existing family entries/metadata and the actual PTHR24412 IBA evidence remain separate. One title was reconciled to native typography. Target validation passed with zero annotation advisories; strict GOA matching passed for all 32 original contexts, and computed status is COMPLETE. Genuine CREATE history and private render/link checks accompany the review.

Native acquisition supplied the original PMID:23585478 text. Selected Results and IP/ubiquitination Methods were read: filament clearance is supported, while vimentin ubiquitination was not detected and TBCB levels were unchanged in those particular assays. This does not contradict later purified reconstitution with other selected substrates. The newly full PMID:27000625 cache does not expand the earlier abstract/caption reading. Original tables and external selected readings remain distinct from normal-cache availability.
