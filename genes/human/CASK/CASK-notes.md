# CASK research and annotation notes

## 2026-10-04 — primary-source review, preliminary checkpoint

This checkpoint covers the normal human CASK source seed. It is a working scientific record, not a final sign-off. The four additional disease/mechanism caches are being obtained through the normal publication workflow; the final review will integrate their actual recovered contents. No source cache or canonical annotation was changed by this authoring step.

### Identity and source preservation

The reviewed human protein is **CASK, UniProt O14936 / CSKP_HUMAN**, HGNC:1497, NCBI Gene 8573. The canonical displayed sequence is 926 residues. Q5JS79 is a different, unreviewed entry and was not substituted. All six normal products, including their exact VSP sequence notes, are preserved. Legacy constructs and transcript labels are not automatically mapped onto those products. In particular, the 921-residue human construct discussed in PMID:9660868 is not a reason to rewrite the current displayed sequence.

The normal GOA file contains 120 raw assertions and the ordinary seed has 118 source objects. Two pairs differ only in assigning group/date, fields omitted from the normal seed projection: GO:0061045 and GO:0090288, both IMP/PMID:18664494. Every source qualifier, partner, evidence code, original reference, isoform/negation field and term is retained. This is documented in the authenticated source projection, not an author-created biological deduplication. No new assertion or guessed family identifier is introduced.

### Two distinct biochemical roles

The active N-terminal protein kinase must be separated from the C-terminal guanylate-kinase-like scaffold region. The full experimental account in [PMID:18423203](https://pubmed.ncbi.nlm.nih.gov/18423203/) supports ATP-dependent phosphotransfer and identifies neurexin-tail serine phosphorylation. Recruitment by full-length CASK improves substrate phosphorylation. Hypomorphic S24D/V26L experiments, neuronal manipulations and the biochemical assays provide complementary evidence; the rat and mouse cellular experiments are not described as patient enzymology. Calcium/calmodulin dependence is not established by the gene name. A single protein-serine-kinase core summarizes the demonstrated chemistry without creating a second overlapping kinase core.

By contrast, the complete historical [PMID:9660868](https://pubmed.ncbi.nlm.nih.gov/9660868/) states that GUK activity had not been tested. The later [PMID:12482754](https://pubmed.ncbi.nlm.nih.gov/12482754/) reports no detectable GMP binding or GMP-kinase activity for CASK-SH3GK, with yeast GK as a positive control. Its complete normal abstract and actual publisher-indexed Results/Table I/Figure 1/Discussion were inspected in the independent mechanism consultation. Full Methods, assayed CASK species and figure pixels were not resolved; PSD95-specific folding/binding controls are not relabeled as CASK controls. These observations support rejecting the four GMP-kinase/GMP-metabolism/GDP-metabolism assertions while retaining the independently demonstrated protein kinase. The original GOA source objects remain intact.

The requested later normal references, PMID:20424264 and PMID:36137748, will refine context. The first concerns engineered ATP-pocket substitutions, not additional native chemistry. The second distinguishes ATP binding and liprin-dependent condensate regulation from direct phosphorylation of liprin by CASK. Neither should be used to erase the 2008 neurexin experiments or to claim a newly established physiological substrate without the appropriate assay.

### Scaffold mechanism and selected binding evidence

The molecular-adaptor core reflects coordination of partner assemblies, not the mere presence of a list of interactors. In [PMID:16688213](https://pubmed.ncbi.nlm.nih.gov/16688213/), the first and second L27 regions are distinguished experimentally. Human CASK bait, canine MDCK complexes, and worm receptor-localization experiments are separate evidence contexts. The curated [LIN7/CASK/APBA1 event](https://reactome.org/content/detail/R-HSA-5336443) and [neurexin/CASK/protein-4.1 assembly](https://reactome.org/content/detail/R-HSA-6797568) corroborate the conserved organizing role; their summaries are not newly performed localization experiments.

The full human-domain study [PMID:21763699](https://pubmed.ncbi.nlm.nih.gov/21763699/) demonstrates CASKIN1 docking and tests APBA1 and TIAM1 motif peptides. A peptide interaction does not establish a physiological kinase substrate or all functions of a full-length complex. [PMID:22117215](https://pubmed.ncbi.nlm.nih.gov/22117215/) specifically tests phosphorylated whirlin peptide binding to CASK SH3-GK; the much more extensive DLG experiments are not transferred wholesale to CASK. The source-specific whirlin row is refined to phosphoprotein binding. The neurexin row is refined to the existing neurexin-family-binding term.

Human GPCR interactome Results and Methods in [PMID:26617989](https://pubmed.ncbi.nlm.nih.gov/26617989/) explicitly describe CASK copurification with MAS1, CYSLTR2 and ADRA1D. These are retained as qualified non-core physical associations. Detailed SCRIB/syntrophin pharmacology cannot be attributed to CASK, and a direct receptor-CASK interface is not inferred from tandem-affinity proteomics.

The full [PMID:39009827](https://pubmed.ncbi.nlm.nih.gov/39009827/) text reports APC W2658L effects in the peptide-selection dataset, supporting bounded APC motif binding. Its CASK–mutant-MAPT example is a different pair and did not validate as a full-length cellular neoassociation. Similarly, the SLC43A2 experiments in [PMID:40355756](https://pubmed.ncbi.nlm.nih.gov/40355756/) cannot stand in for the source row naming SLC16A3.

### Fragmentomics: provenance remains decisive

The 23 source assertions from [PMID:36115835](https://pubmed.ncbi.nlm.nih.gov/36115835/) remain **UNDECIDED** at this checkpoint. The complete relevant Methods and Results distinguish isolated PDZ–motif affinity measurements from cell-extract AP-MS capture. In particular, CASK can copurify with viral motifs despite the lack of detectable isolated-PDZ affinity; the authors propose complex-mediated capture through L27 partners. They also explicitly caution that a subthreshold affinity is not evidence of physical impossibility.

The independent bounded consultation joined all 23 partners to 29 motif records in the paper-linked ProfAff SQL repository. That SQL snapshot was uploaded in July 2021, before the 2022 publication, and has **not** been authenticated as the final supplementary workbook. Its zero composite values and subthreshold DAPF measurements therefore neither confirm 23 direct binding positives nor justify removing the curated experimental assertions. Exact AP-MS versus holdup versus benchmark provenance remains unresolved. Domain-map residues 489–564 do not authenticate cloned construct endpoints. The final workbook, IntAct record and assay controls are the actionable next evidence; no source field was edited.

The official [2022 correction](https://doi.org/10.1038/s41467-022-35177-6) repairs figure labels and panel presentation. The read notice does not announce withdrawal of the supplementary affinity data. Any future visual assignment should use the corrected figures.

### Epithelial localization and process scope

The normal cache for [PMID:18664494](https://journals.biologists.com/jcs/article/121/16/2705/30173/The-MAGUK-family-protein-CASK-is-targeted-to) is abstract-only, but the complete official publisher scientific prose, Methods and captions were read separately. Human keratinocyte perturbation supports contextual effects on adhesion, proliferation and growth-factor responsiveness. Nuclear, nucleolar and extraction-resistant pools are retained without inventing transcriptional or RNA-processing functions.

The basement-membrane rows remain unresolved and have different relations: source row 67 says `colocalizes_with`, whereas row 68 says `part_of`. Spatial coincidence near an extracellular boundary does not require a secreted matrix constituent, and is weaker than membership in the matrix. Figure pixels and the curator's precise interpretation were not independently established. The wound-healing claim is broader than the measured perturbation endpoints and is provisionally marked over-annotated; tissue repair itself was not measured after CASK manipulation. The distinct review will reassess these two boundaries before final sealing.

### Phylogenetic and source-access limits

PAINT rows remain node-based evolutionary judgments. Donor count is not a quality score, and human CASK among its own supporting descendants is expected rather than circular. Conserved receptor binding, membrane/junction localization, partner positioning and sign-neutral neurotransmitter regulation are retained where coherent with the experimentally grounded scaffold. No new PAINT tree reconstruction is claimed.

Specialized donor compartments—ciliary membrane, vesicle and Schaffer collateral–CA1 synapse—need the actual donor experiments. The direct QuickGO donor queries were inaccessible; that technical result does not establish biological absence. The HPA nucleoplasm record and focal-adhesion proteomics also need their exact antibody/image or target-enrichment evidence. A knockdown effect on focal adhesions is not localization of CASK itself.

For unresolved high-throughput interactions, the required next item is the target-level source row with construct, assay and control information, not another broad review abstract. Complete source headers and available abstracts were checked at intake. Missing target evidence does not justify wrong-gene, wrong-paralog, retraction or miscitation claims. The project permits supported non-core protein binding; it does not require declaring every interaction unsupported simply because it is broad, and it does not waive genuine evidence-access limits.

### Mendelian context and corrections

The official disease reports identify the microcephaly/pontocerebellar-hypoplasia and familial intellectual-disability/nystagmus spectrum. Their normal caches are pending at this checkpoint. The [Najm correction](https://doi.org/10.1038/ng1108-1384b) specifies **CINAP/TSPYL2**, not TAF9. The [Hackett correction](https://doi.org/10.1038/ejhg.2010.24) changes the family-123 nucleotide notation to **c.2755T>C**, with p.W919R retained in that publication's coordinate system. Neither historical coordinate nor study transcript labels are silently mapped onto the current six UniProt products. Disease necessity is not used to manufacture new developmental-process annotations.

### Checkpoint boundaries

This preliminary candidate has 118 decisions, 42 references, six unchanged products, two core activities and no NEW annotations. Normal final validation, exact source/preimage audit, completed cache integration and a distinct whole-science review remain required before sealing. Supporting quotations have not been added in this preliminary draft.


## 2026-10-04 — final source integration and bounded synthesis

The four requested references are now present as immutable publication caches. PMID:19165920 and PMID:20029458 remain abstract-only; PMID:20424264 and PMID:36137748 provide XML-derived full text. Complete unique Results and Discussion were read for both mechanistic papers, and the available Methods and captions were read for the 2022 study. The 2010 supplementary Methods and original figure pixels were not reanalysed. These access statements supersede the pending-cache boundary above.

The 2010 experiments convert CASK to an engineered Mg-stimulated kinase with four ATP-pocket substitutions. That construct does not establish native Mg dependence. Full-length native and engineered CASK produce similar steady-state neurexin phosphorylation in the tested cells; the kinase-domain truncation is a distinct control. The kinase core retains the 2008 direct chemistry and adds the later corroborating source, without adding an overlapping activity.

The 2022 study tests human variants in HEK293T cells and cultured embryonic rat hippocampal neurons. Coassociation, Liprin W981A and CASK E115K perturbations connect the CASK–Liprin interaction to condensate behavior. CASK coexpression reduces Liprin S87 phosphorylation, and S87 substitutions fail to recapitulate the condensation phenotype. These results support a separable interaction mechanism, not a newly established Liprin substrate or a proven disease mechanism. TV3 and TV5 constructs remain unmapped to current UniProt product identifiers.

The two clinical papers support the standalone disease summary. Their official corrections were read and are described above; no obsolete partner name or unqualified historical variant coordinate is imported. Clinical necessity does not manufacture a developmental GO assertion.

Three precision points were resolved after the preliminary read. Adhesion is described as CASK-directed depletion, without claiming that both siRNAs independently replicated that particular assay. PMID:15694377 compares Id1 splice variants, not CASK products. The protein-transport row now records the selected L27-paper Introduction and Methods that became available; the actual complete transport evidence remains unresolved. The wound-healing rationale concerns the direction of a repair mechanism, without requiring a wound-closure assay as the only possible evidence. The independent epithelial consultation supports that distinction and the separate basement-membrane relations.

All 118 actions remain 27 ACCEPT, 26 KEEP_AS_NON_CORE, 3 MODIFY, 4 REMOVE, 57 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED. The six products and all machine assertion fields remain exact. The review contains 46 references, two core activities and no NEW assertions. Two short verbatim anchors support the adaptor and kinase cores; all other supporting citations remain reference-only. DRAFT records unresolved biological or evidence-access questions, not the validator advisories. Nine supported generic-binding advisories follow the project policy; the cytosol advisory reflects broad electronic localization versus contextual Reactome pools, as explained in the row reasons.

One ordinary isolated deep-research attempt with Falcon and its configured Perplexity-lite fallback failed with connection errors. No provider report was produced or fabricated. This is a manual primary-source review with explicit access limits. Final schema/term/reference/GOA checks, status agreement, rendering and the distinct whole-review receipt are recorded in the sealed handoff; the review makes no claim to have resolved inaccessible target tables or donor experiments.
