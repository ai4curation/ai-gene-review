# BLTP1: initial evidence review

This is a provisional research record; annotation decisions are not finalized.

BLTP1 (Q2LD37; formerly KIAA1109/FSA/TWEEK) is a 5,005-residue member of the bridge-like lipid-transfer protein family. The normal seed contains 20 source assertions and six alternative products. The products slot is absent. Yeast Csf1 (Q12150), the source of several ISS annotations, must not be confused with the human cytokine CSF1.

## Direct human evidence

[PMID:30906834, Endosomal trafficking defects in patient cells with KIAA1109 biallelic variants](https://pubmed.ncbi.nlm.nih.gov/30906834/) compares primary fibroblasts from one affected child with a healthy donor. Selected full-text Results describe reduced KIAA1109 transcript abundance, altered endosomal marker distributions and dextran pulse-chase trafficking. The study supports the existing endosomal-transport and recycling annotations. It does not establish a catalytic lipid-transfer mechanism, direct localization of BLTP1 to every affected compartment, or a causal rescue in the sections inspected. A useful short supporting phrase is: “with an accumulation of dextran in the patient cells”. These findings should be distinguished from direct localization and from a claim that BLTP1 catalyses every downstream process affected by lipid imbalance.

[PMID:31540829, Systematic Identification of Host Cell Regulators of Legionella pneumophila Pathogenesis Using a Genome-wide CRISPR Screen](https://pubmed.ncbi.nlm.nih.gov/31540829/) validates impaired uptake of nonpathogenic delta-dotA Legionella with two independent KIAA1109 sgRNAs in human U937 cells. The selected Results identify the relevant phenotype: “knockouts of the uncharacterized genes C1orf43 and KIAA1109 significantly impaired phagocytosis of L. pneumophila”. The subsequent experiments with diverse substrates, mouse macrophages and complementation principally test C1orf43. They must not be silently attributed to BLTP1. The existing phagocytosis assertion has direct human perturbation support, while its placement in the core functional synthesis needs to distinguish lipid supply from the wider cellular uptake phenotype.

[PMID:17190194, Molecular cloning and preliminary analysis of a fragile site associated gene](https://pubmed.ncbi.nlm.nih.gov/17190194/) is available as an abstract-only normal cache. It describes CHO genomic cloning, a full-length human FSA cDNA, and immunohistochemistry in differentiated epithelial tissues. The authors conclude a role in epithelial growth and differentiation. The abstract does not resolve nuclear localization or establish a detailed regulatory mechanism. Do not reject the underlying NAS assertions on the basis of this incomplete text; obtain full-text evidence or retain explicit uncertainty.

[PMID:16632497, G8: a novel domain associated with polycystic kidney disease and non-syndromic hearing loss](https://pubmed.ncbi.nlm.nih.gov/16632497/) is also abstract-only. It is a historical domain analysis, not direct experimental BLTP1 membrane localization. Modern BLTP-family evidence and the normal UniProt record provide separate context for membrane association.

## Additional mechanistic and disease references

Four references are requested through the normal publication fetcher; the local attempt failed DNS resolution for all four and created no caches. They are not yet formal cached references in the review.

- [PMID:35015055](https://pubmed.ncbi.nlm.nih.gov/35015055/), DOI 10.1083/jcb.202111095, PMCID PMC8757616: yeast Csf1 and orthologs support availability of phosphatidylethanolamine for GPI-anchor synthesis. The PubMed abstract and figure captions distinguish the yeast mechanism from human HEK-293 KIAA1109 knockdown and reduced surface CD55. A transporter supplying substrate should not automatically receive a NEW GPI-synthesis annotation; the participation and comparator checks remain necessary.
- [PMID:35491307](https://pubmed.ncbi.nlm.nih.gov/35491307/), DOI 10.1016/j.tcb.2022.03.011, PMCID PMC9588498: a review proposing the repeating beta-groove superfamily. This supplies structural synthesis, not a new experimental human BLTP1 assay.
- [PMID:40269155](https://pubmed.ncbi.nlm.nih.gov/40269155/), DOI 10.1038/s41586-025-08918-y, PMCID PMC13533485: the cryo-EM structure is the native worm LPD-3 complex. Selected external Results also report that knockdown of human BLTP1 or C1orf43 in HeLa cells reduces GFP-MAPPER-labelled ER–plasma-membrane junctions. C1orf43 localization was tested separately. These observations support a conserved role in contact-site formation or maintenance; they do not turn the worm structure into a directly measured human structure or establish direct human BLTP1 localization by that assay alone.
- [PMID:29290337](https://pubmed.ncbi.nlm.nih.gov/29290337/), DOI 10.1016/j.ajhg.2017.12.002, PMCID PMC5777449: human biallelic variants in Alkuraya-Kucinskas syndrome; useful for disease context without equating developmental consequences with core molecular activity.

## Scope and remaining checks

The IBA synaptic-vesicle-endocytosis assertion carries a fly descendant and PTN000781310. Its donor count is not evidence of weakness; no PAINT-node reassessment has yet been performed. The beta-catenin IPI row also requires its source-specific interaction context before any functional refinement. No NEW annotation is proposed here. The local GO-CAM index search returned no BLTP1/Q2LD37/KIAA1109 entry.

Reading scope: all 20 seeded assertion objects, selected normal UniProt sections, four seeded publication abstracts, and selected Results text from PMID30906834 and PMID31540829. No whole-paper, figure-image or supplement audit is claimed. External PMC direct page opens were challenged; indexed primary-source passages were usable. The automated Perplexity research invocation failed because the required deep-research-client version could not be resolved in the established offline environment. No provider-labelled research output was authored manually.


## Independent evidence check — 2026-10-01

The first consultation assessed all 20 source assertions and agreed with retaining eight as core-compatible, eight as non-core and three as unresolved historical claims, with one partner-specific binding refinement. The six normal alternative products remain unchanged; no isoform-specific function is inferred from historical interaction-fragment coordinates. No new annotation is proposed.

### Beta-catenin interaction

[PMID:20195357](https://pubmed.ncbi.nlm.nih.gov/20195357/) used human cDNA-fragment mRNA display to map interactions. The [author-attributed Table S5 mirror](https://www.researchgate.net/publication/293849155_Table_S5) contains CTNNB1–KIAA1109 entries IR_350 and IR_353, with historical regions 1200–1214 and 2190–2199. These match the partner named in GOA and normal UniProt. The mirror rows do not display pair-specific reciprocal validation results; neither a native full-length complex nor two independent studies is established. Original XLS bytes and supplement images were unavailable, and historical coordinates were not remapped to current isoforms.

The existing IPI assertion is refined to [GO:0008013 beta-catenin binding](https://amigo.geneontology.org/amigo/term/GO:0008013). This preserves the physical interaction while giving the partner class. It does not establish Wnt signaling, transcriptional regulation or a core lipid-transfer function for this interaction.

### Lipid specificity and location

The specific phosphatidylethanolamine-transfer annotation is retained as a curated similarity inference, with uncertainty stated. [PMID:35015055](https://pmc.ncbi.nlm.nih.gov/articles/PMC8757616/) explicitly permits alternative explanations involving another lipid or Mcd4 regulation. [PMID:40269155](https://pmc.ncbi.nlm.nih.gov/articles/PMC13533485/) did not chemically resolve the lipid densities in the native worm complex. Thus, the authored core uses [GO:0120014 phospholipid transfer activity](https://amigo.geneontology.org/amigo/term/GO:0120014), together with the existing intermembrane-transfer process and ER–plasma-membrane contact-site location. No purified human substrate-selectivity measurement is claimed.

The mitochondrial annotations retain their yeast-donor boundary: contact-site proximity is distinct from demonstrated human mitochondrial targeting or membrane insertion. Apical membrane localization retains its worm-based provenance. Human BLTP1 depletion affecting MAPPER-marked junctions supports contact maintenance but does not substitute for direct BLTP1 localization. These limits also motivate the proposed experiments.

### Phylogenetic and process boundaries

The [FlyBase tweek record](https://flybase.org/reports/FBgn0261671) provides experimental context for the conserved synaptic-vesicle-endocytosis assertion and the named PAINT node. The complete IBD tree and alignment were not inspected. The inference is retained without using donor count as a measure of quality or claiming a target-specific loss. Its logically inferred presynaptic location is retained consistently as non-core.

The direct human phagocytosis and endosomal/recycling assertions remain supported cellular contexts. The review does not infer additional localization from marker changes, transfer C1orf43-only experiments to BLTP1, or convert disease phenotypes into developmental process annotations. It also does not propose GPI-anchor biosynthesis merely because lipid supply is necessary for anchor production.

Reading scope was extended to the two displayed interaction rows, official GO definitions, the selected lipid-specificity passages and the independent consultation. This is not a whole-paper, original-spreadsheet, figure-image or complete phylogeny audit. Formal source recovery, final reference checks and canonical validation remain pending at this draft stage.


## Final evidence synthesis — 2026-10-01

The reference archive has now been recovered through the normal fetcher and authenticated. All four requested papers include XML full text. Complete abstracts, body boundaries and selected Results/discussion passages were read; this is not a whole-paper or supplement audit. The references are included in the final candidate with exact fetched titles, and their canonical import is checked separately before final validation.

The selected cached text confirms that the human GPI-surface assay used HEK-293 cells and two KIAA1109 shRNAs. The yeast discussion explicitly leaves substrate specificity and indirect Mcd4 regulation open. The 2025 worm structure contains lipid densities modeled with a phosphoethanolamine head group, but their chemical identities were not resolved. Human BLTP1 depletion reduced MAPPER-marked contacts; C1orf43 localization was a separate assay. These observations support a broad phospholipid-transfer core with the existing similarity-derived PE annotation retained at its original evidence level.

All 20 original assertions and six alternative products are preserved: eight ACCEPT, eight KEEP_AS_NON_CORE, three UNDECIDED and one MODIFY to beta-catenin binding. No NEW annotations, isoform functions or extra products were added. The three unresolved claims concern the abstract-only FSA study. The final core contains phospholipid transfer, intermembrane lipid transfer and ER–plasma-membrane contact-site context. Disease phenotypes and downstream membrane-trafficking consequences are not additional molecular activities.

Earlier entries retain the reading scope and workflow state at the time they were written. This entry supersedes their statements that reference recovery and the interaction consultation are pending. Canonical validation, final independent review and publication will be recorded after they occur.


## Canonical validation — 2026-10-01

The final independent annotation and core-function review passed. All four recovered reference caches were imported and checked against the authenticated archive before applying the reviewed candidate. Canonical schema, term, reference and GOA validation passed; the new history record and HTML rendering also passed. The rendered embedded YAML equals the review. One advisory notes that the broad core term GO:0120014 is absent from the source annotations. It is intentionally retained as the broader supported core activity while the existing PE-specific ISS assertion preserves its curator provenance and explicit uncertainty. No redundant NEW ancestor annotation was added. All 20 source assertions, six alternative products, and fetched UniProt/GOA and publication bytes remain unchanged. Publication and remote checks are separate subsequent steps.
