# ASNS research notes

## 2026-09-28: source and evidence boundaries

The normal seed contains 24 source assertions and three alternative products. The original GOA, UniProt and source caches are preserved. Seed16 auxiliary recovery supplied six missing abstract-only PMID records and the normal human Reactome70599 record. Four existing publication copies were retained even where recovered alternatives differed; both family exports remain quarantined. The exact seven-file import is documented in `tmp/seed16-auxiliary-import-receipt.json`.

One configured Falcon/fallback research attempt failed without a report; raw provider diagnostics were discarded. The ordinary publication-cache command completed with no additional outputs. `tmp/ASNS-initial/research-closure.json` records both actual outcomes and preservation of all 14 starting files. This is a manual research journal, not a provider-generated report.

All ten original complete cached abstracts and the entire normal Reactome70599 summary were read. The 2014, 2019 and 2020 interaction records have full-text extractions, but availability does not mean that every supplementary target-pair record was read. The 1999 cache's Full Text section repeats its abstract and remains explicitly abstract-only.

## Coupled catalysis and substrate modes

Human ASNS directly catalyzes glutamine-dependent asparagine production. PMID2564390 reports active human recombinant enzyme expressed in bacteria, including ammonia- and glutamine-fed activity. PMID2573597 distinguishes the N-terminal cysteine requirement for the glutamine-dependent route from retained ammonia-dependent synthesis in a human construct expressed in yeast. PMID16023613 reports active, correctly processed C-terminally tagged human enzyme purified after baculovirus-based expression. PMID2886907 uses human fibroblast cDNA in Jensen rat sarcoma recipients; the species of the cDNA and recipient must remain distinct. Detailed original assay Methods for these four papers were not read.

The original ts11 paper PMID2569668 identifies human ASNS by complementation of the BHK G1 defect and by asparagine bypass. Its complete abstract describes G1-associated expression in human, mouse and hamster cells. It supports the enzyme identity and a contextual cell-cycle consequence, but does not by itself specify a dedicated checkpoint mechanism. Its exact IDA assay details remain deferred to the original curator.

Current official AmiGO definitions and parents were read for [GO:0004066](https://amigo.geneontology.org/amigo/term/GO:0004066), [GO:0004071](https://amigo.geneontology.org/amigo/term/GO:0004071), [GO:0004359](https://amigo.geneontology.org/amigo/term/GO:0004359) and [GO:0070981](https://amigo.geneontology.org/amigo/term/GO:0070981). The glutamine-fed and ammonia-fed ligase terms are distinct reaction terms, not an ancestor/descendant pair. Glutaminase activity describes the hydrolytic first reaction; accepting that existing annotation does not assert an autonomous glutamine-catabolic role. The proposed single core uses the complete coupled activity and asparagine biosynthesis, with its internal glutaminase step described in prose.

Additional human primary PMID39627226, DOI10.1038/s41467-024-54912-9, PMCPMC11615228, was verified against official records. The complete abstract, original publisher Results through the start of the simulation analysis, indexed Table1 and the targeted kinetic Methods paragraph were read. Human wild-type ASNS expressed in Sf9 cells formed a head-to-head apo dimer. The kinetic table separates glutamine and free-ammonia conditions and measures PPi production as the assay readout. No full supplement, isolated glutaminase assay or ligand-bound human structure is claimed. A single ordinary normal-cache attempt failed in 32.384 seconds with exit1 and no output; independent identity assessment is saved and fixed Source57 recovery is pending. No hand-written cache is used.

The earlier human-structure paper PMID31552298 and its correction PMID31799439 were inspected only as background: official abstract/metadata plus correction text. The correction concerns author affiliation/funding, not the experimental findings. Neither is currently proposed as an additional normal reference.

## Location and process context

The current [HPA ASNS subcellular page](https://www.proteinatlas.org/ENSG00000070669-ASNS/subcellular) reports Cytosol, Supported. Displayed antibody/cell-line records include HPA004924 in A431/U251MG/U2OS and HPA064737 in MCF7/SK-MEL-30/U2OS. The historical images were not independently rescored. Cytosolic localization is not asserted to be exclusive. The complete normal [Reactome70599](https://reactome.org/content/detail/R-HSA-70599) summary explicitly identifies the cytosolic ASNS-catalyzed reaction.

PMID10085239 directly reports glucose-dependent ASNS transcription in human HepG2/MOLT4 cells, with other cell contexts separately named. Current [GO:0042149](https://amigo.geneontology.org/amigo/term/GO:0042149) includes gene-expression changes in its response definition. Retaining that existing response annotation does not identify ASNS as a glucose sensor.

For PMID17409444, beyond the complete cached abstract, the original author-upload paper was accessed at [ResearchGate](https://www.researchgate.net/publication/6413396_Enhanced_Expression_of_Asparagine_Synthetase_under_Glucose-Deprived_Conditions_Protects_Pancreatic_Cancer_Cells_from_Apoptosis_Induced_by_Glucose_Deprivation_and_Cisplatin). Targeted apoptosis Methods, human ASNS siRNA/transfection Methods and Results/Fig2–3 were read. MiaPaCa2 knockdown and overexpression altered apoptosis under glucose deprivation/cisplatin; annexin-V/propidium-iodide and Hoechst readouts support the endpoint. This is a conditional survival observation, not a direct ASNS JNK activity or universal apoptosis suppression. The canonical cache remains abstract-only; external target reading is recorded separately. Current GO0043066 and GO0045931 definitions were checked through official AmiGO/MGI records.

The local GO-CAM index has no human P08243/ASNS activity entry. The textual ASNSYNB reaction matches in that index are yeast ASN1/ASN2, not human ASNS. No new process annotation is proposed.

## Interaction provenance

The immutable human UniProt aggregation names WDR27/A2RRH5, TRIM69/Q86WT6 and TRIM69/Q86WT6-2. It does not by itself establish that every pair occurred in each cited publication.

The exact human ASNS-bait/WDR27-prey two-hybrid record was independently read in [BioGRID interaction1037059](https://thebiogrid.org/interaction/1037059/asns-wdr27.html). Its publication link resolves to the Rolland2014 record and explicitly PMID25416956. This curated source-specific pair supports non-core retention, with the original supplementary constructs/raw reporter data unread. It does not establish a specialized WDR27 molecular function or endogenous complex.

The 2014 abbreviated extraction, 2019 variant-screen abstract/targeted Results and 2020 HuRI abstract/screen overview were read. Exact ASNS–TRIM69 source-specific tables, variant conditions and the TRIM69-2 construct remained unexposed. The current primary HuRI TRIM69 page returned an empty interaction table; search nonmatches are not contradictory experiments. These three source-specific assertions remain prospective UNDECIDED. No vendor aggregation is used to close them, and no ligase-binding function is inferred from a name alone.

The explicit user ActionEnum governs disposition of valid broad interactions: NONCORE can preserve a demonstrated association; unread target evidence warrants UNDECIDED. Genericity alone is not grounds to assert that binding is false. The biological rationales will state the individual evidence rather than repeat this policy discussion.

## 2026-09-28: completed normal Source57 closure and final decisions

The exact normal PMID39627226 XML record is now present, imported without overwriting any prior source. Its title is “3D variability analysis reveals a hidden conformational change controlling ammonia transport in human asparagine synthetase.” DOI10.1038/s41467-024-54912-9 and PMC11615228 match the independently checked identity. The earlier journal spelling “PMCPMC11615228” was a transcription error; the correct identifier is PMC11615228. The earlier pending-recovery paragraph is historical and is superseded by this closure.

The complete actual cached abstract/frontmatter, human dimer/domain Results and Fig1–2 captions, steady-state Results/Table1 and adjacent interpretation, expression/purification Methods and kinetic Methods were read. These are human proteins expressed in Sf9 insect cells. The structure supports a head-to-head homodimer; it does not establish a second physiological core. Under glutamine conditions the R142I/R142A variants have reduced turnover, while ammonia-fed parameters are broadly maintained. The continuous EnzChek assay measures PPi, and the paper invokes bacterial-homolog analogy for its 1:1 relationship to asparagine. It is not a direct asparagine-product assay in this experiment. Measurements were in duplicate. Free-ammonia-dependent synthesis remains an in-vitro alternative; physiological use was not established. No full supplement, raw movie/map or figure-pixel audit is claimed. The two domains and intramolecular nitrogen transfer are synthesized with the older human mutagenesis and catalytic evidence, without asserting a separately measured autonomous glutaminase process.

The final review retains all 24 original source assertions and three alternative products: 16 ACCEPT, five KEEP_AS_NON_CORE and three source-specific UNDECIDED decisions. There are no NEW assertions. One core describes the complete coupled cytosolic asparagine-synthesis reaction. The three unresolved TRIM69 source/construct questions remain open; the demonstrated WDR27 association is retained as non-core. All original source and provider files remain unchanged. The earlier prospective language records the deliberation; these are now the final authored decisions. Independent prospective and preliminary authored consultation found no requested biological changes. Final source attachments are checked against the actual normal cache before final independent consultation.


## 2026-09-28 glutaminase feedback

The N-terminal glutamine-hydrolysis step remains ACCEPT because it performs an integral part of glutamine-dependent asparagine synthesis. Human N-terminal cysteine mutagenesis distinguishes glutamine-fed from ammonia-fed synthesis (PMID:2573597), while human domain/tunnel and coupled-reaction evidence (PMID:39627226) supports the integrated mechanism. The single core describes the complete coupled GO:0004066 reaction. RHEA:15889 is curator-inferred in the shipped UniProt record; this provenance does not make its chemistry biologically peripheral and does not establish an independently measured autonomous glutaminase assay. No second core or contributes_to relation is added.

This bounded follow-up changes only the glutaminase rationale, leaving all original assertion fields, actions, three alternative products and the core unchanged. The WDR27 binding policy question remains pending; its positive pair evidence is not reclassified as incorrect. Counts remain 16 ACCEPT, 5 KEEP_AS_NON_CORE and 3 UNDECIDED.


## 2026-10-01 UTC — Binding-policy clarification

The [review of PR #3438](https://github.com/ai4curation/ai-gene-review/pull/3438) at `2e917ec2d` correctly distinguishes exclusion of an uninformative term from rejection of a reported interaction. The repository default can exclude GO:0005515 even when the interaction is real. The earlier notes should not be read as claiming that the default requires biological falsity or that a touched annotation falls within a legacy exception.

For this task, the explicit instruction is not to remove generic binding solely for informativeness and to preserve UNDECIDED when the relevant experiment cannot be adjudicated. The existing decisions are a scoped application of those instructions. This is a documented departure from the default binding policy, not a global policy change or a claim that its advisory warnings have disappeared.

The retained WDR27 association rests on the previously inspected, source-specific BioGRID pair record. That is not a claim that the original supplementary constructs or raw reporter data were read, nor evidence of an endogenous regulatory complex or a more specific ASNS binding function. The three other unadjudicated interaction rows remain UNDECIDED. The coupled asparagine-synthesis core and its integral glutamine-hydrolysis step are unchanged; retaining the association does not add a second catalytic core.

This addendum adds no primary-source reading, assay verification or quotation. All existing actions, source assertions, products, reference findings and core claims remain unchanged.
