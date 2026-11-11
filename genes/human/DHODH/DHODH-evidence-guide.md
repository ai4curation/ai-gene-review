# DHODH source evidence and assay-scope guide

The review retains 23 imported source annotations and the three historical proposal positions. All 23 imported source dictionaries are unchanged. The ferroptosis proposal remains retired UNDECIDED as a genuinely withdrawn, uncertain assertion. The historical quinone-binding proposal is refined in place to active NEW GO:0048039 with direct human substrate evidence; its prior term/evidence/reference is preserved in appended notes and history. No annotation row is added. One catalytic unit combines quinone-dependent dihydroorotate oxidation, de novo UMP and UDP pathway participation, and mitochondrial inner-membrane location. The official human record is [Q02127](https://www.uniprot.org/uniprotkb/Q02127/entry), 395 residues with no listed alternative products. The targeting segment is not annotated as cleaved; precise topology features carry homology evidence.

## Catalysis, binding and localization

| Source | Access actually used | Scope and consequence |
|---|---|---|
| [8925840](https://pubmed.ncbi.nlm.nih.gov/8925840/) | Primary abstract; full original not recovered | Purified recombinant human fragment expressed through baculovirus, positive FMN analysis and kinetics with ubiquinone-50/decylubiquinone. Positive IDA evidence is retained; unknown fragment endpoints are not invented. |
| [10673429](https://doi.org/10.1016/S0969-2126(00)00077-0) | Genuine author-posted original Methods/Results, independently read; repository cache remains abstract-only | Human engineered Met30–Arg396 construct with an uncleaved N-terminal ten-His tag, expressed in E. coli. FMN, orotate and inhibitors are resolved; a quinone pose is modeled. The historical numbering does not create another natural product. |
| [10727948](https://doi.org/10.1046/j.1432-1327.2000.01213.x) | Genuine publisher original Methods/Results; repository cache remains abstract-only | Endogenous rat protease protection and carbonate extraction establish membrane integration and exposure to the intermembrane space. Human, rat and fly constructs import into isolated yeast mitochondria without detected size change. The human construct has an incomplete extreme N terminus and C-terminal enterokinase/eight-His extension. Rat deletions and energy tests are not direct human topology assays. |
| [Human Protein Atlas](https://www.proteinatlas.org/ENSG00000102967-DHODH/subcellular) | Actual official subcellular summary and antibody/cell-line table; image pixels not re-evaluated | Mitochondrial main location is enhanced; nucleoplasm and cytosol are also reported. HPA010123 reports mitochondria in MCF7/U2OS; HPA011942 in A549/MCF7. Keep mitochondrion resolution without excluding other pools or inventing isoform resolution. |
| [34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) | Full cached original Methods and genuine published [Table S1 workbook](https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx) | Q02127/DHODH is protein group 5570, Table S1(A) row 301 and S1(B) row 274. MitoCoP inclusion and subtractive/spatial/importomics classifications are positive. Human HEK293 fractionation, HeLa import perturbation and carbonate extraction support mitochondrial/membrane localization, not exact inner-membrane sidedness or multiple official products. |
| [Reactome 73569](https://reactome.org/content/detail/R-HSA-73569) and [9708759](https://reactome.org/content/detail/R-HSA-9708759) | Protected cached summaries plus fresh typed entity records | Catalyst 73535 resolves to complex 73534, whose protein component 73523 is Q02127 residues 1–395 at the inner membrane. The inhibitor reaction shares this entity. Metabolite cytosol annotations do not move the enzyme to cytosol. |

The structure and independent substrate kinetics support refinement of historical quinone binding to [ubiquinone binding](https://www.ebi.ac.uk/QuickGO/term/GO:0048039). FMN and quinone interactions are parts of one catalytic mechanism. Neither a separate binding core nor another parent/child NEW assertion is needed.

## Binary interactions and partner classes

The [HuRI original](https://pubmed.ncbi.nlm.nih.gov/32296183/) full Methods describe three assay versions, pairwise quadruplicate retesting and sequence confirmation. Dataset MAPPIT/GPCA benchmarks are not pair-specific validation. Exact [IntAct](https://www.ebi.ac.uk/intact/search?query=Q02127) human records were checked against official sequence-derived ROGIDs:

| Partner | Exact pair accessions, validated / array / pool | Interpretation |
|---|---|---|
| TTPA, P49638, 278 residues | EBI-24684579 / EBI-24005256 / EBI-23712419 | Supported association with a lipid-transfer protein; no native vitamin-transfer mechanism or more specific supported binding class is inferred. Retain non-core. |
| RNF19B, Q6ZMZ0, 732-residue canonical sequence | EBI-24739527 / EBI-24098718 / EBI-23806696 | The record states a sufficient-binding region at 185–732, not a full native interaction assay. The established E3 ligase partner class permits GO:0031625 binding refinement; DHODH is not assigned ligase activity or substrate status. |

RNF19B class is supported by the full original [27485036](https://pubmed.ncbi.nlm.nih.gov/27485036/): human V5-tagged constructs and immunoprecipitated coupled-translation products were tested with E1, E2, ubiquitin and ATP; WT and RING/cysteine mutants differ. This is independent partner evidence, not a DHODH experiment. Physiological colocalization, affinity and stoichiometry of either HuRI pair remain unestablished. Supported generic TTPA binding follows the project's [explicit instruction](https://github.com/ai4curation/ai-gene-review/blob/d77f71b566bd5ee0e87e410083f71e5b6f27036b/projects/CLINGEN_MENDELIAN.md#curation-instructions).

## Propagation and term scope

The actual PTHR48109 tree places human PTN002535636 beneath PTN000234184 (activity/process) and PTN000234186 (inner membrane), outside the alternative class-1 branch PTN002466504. The protected IBD table and complete current donor annotation queries were read. Human target evidence in an IBD donor set is legitimate. Q08210, P0A7E1, G5EB61 and Q5E9W3 were mapped to actual descendant paths; a donor's presence or count is not used as a substitute for phylogenetic reasoning. This review does not claim all donor original papers were recovered.

Actual target matches include IPR005719 (39–394), IPR005720 (77–377), IPR001295 conserved regions and IPR013785. ARBA00047233's inspected conjunction of IPR001295/IPR005720/IPR013785 is met. Broad mappings are refined on target chemistry/location rather than rejected from a broad family name. Combined mapping sources retain their source-specific limitations.

The GO definitions and typed ancestry were inspected. Cytoplasm includes mitochondria and differs from cytosol; the inner-membrane path reaches mitochondrion and cytoplasm. Specific quinone-dependent oxidation descends from the general dehydrogenase and CH-CH oxidoreductase classes. De novo UMP biosynthesis supplies the specific replacement for broad nucleotide-process assertions.

Historical GO:0004151 is now REMOVE. Its hydrolytic ring reaction differs from the demonstrated FMN/quinone oxidation and class-2 DHODH domain/structure. The official [human CAD record](https://www.uniprot.org/uniprotkb/P27708/entry) assigns EC 3.5.2.3 to DHOase-family machinery with zinc cofactors, supporting the distinct enzyme chemistry. The absence of this assertion from the complete mouse O35435 snapshot (2026-10-17 12:34:11 UTC) is corroborating provenance; the exact historical donor cause remains unknown. No name-confusion or wrong-paralog mechanism is inferred.

For UDP biosynthesis, that mouse snapshot contains experimental annotations citing [30449682](https://pubmed.ncbi.nlm.nih.gov/30449682/) and [6249586](https://pubmed.ncbi.nlm.nih.gov/6249586/). The former full original uses mouse 4T1/B16 knockout and mouse-cDNA rescue, with DHODH activity, orotate and labelled UMP readouts (Results Figures 4–5; Methods on DHODH reconstitution, enzyme activity and glutamine-to-UMP flux). The latter is accessible only as a positive tumour-cell inhibitor/rescue abstract. GO:0006225 includes pathways; DHODH performs the upstream orotate-producing catalytic step. Both existing UDP and UMP process assertions are represented in the same core, preserving the UMP assay endpoint and excluding any DHODH kinase claim. Neither process is an ontology ancestor of the other; UMP is not treated as a narrower UDP descendant.

## Ferroptosis: preserve the dispute and access limits

The [2021 study, 33981038](https://doi.org/10.1038/s41586-021-03539-7), was read as abstract and extended-data captions, not full main Methods/Results. Captions include knockout, reconstitution, uridine and CoQ-related experiments; genetic evidence is therefore present. Its universal mechanistic interpretation is not treated as settled.

The published [2023 Matters Arising, 37407687](https://doi.org/10.1038/s41586-023-06269-0), was recovered as the original article reproduced in author Toshitaka Nakamura's institutional thesis, PDF pages 109–118. Main text and selected Methods on pages 109, 111 and 112 were read. High-dose brequinar inhibits FSP1; sensitization can remain after DHODH loss and disappear after FSP1 loss. Genetic DHODH effects were modest and context-dependent. The study includes human and mouse cellular systems and recombinant enzyme assays; it does not refute established DHODH quinone chemistry.

The [reply, 37407682](https://doi.org/10.1038/s41586-023-06270-7), was accessible as introductory text and extended captions only. Its complete argument and figure pixels were not assessed, so this review does not declare the dispute resolved. The [34341547 correction](https://pubmed.ncbi.nlm.nih.gov/34341547/) adds funding acknowledgment only. The inherited ferroptosis proposal is UNDECIDED, outside the core, with a DISPUTED reference assessment. This retains the distinction between drug specificity, context-dependent genetics and unverified breadth raised in the earlier [human review](https://github.com/ai4curation/ai-gene-review/issues/821).

## Provenance

The earlier PR 827 formal approval and PR 1990 human-authorized merge are retained in the audit record. Existing notes remain a byte-identical prefix, followed by a dated superseding assessment. Existing publication caches, UniProt, GOA, Falcon and Reactome files are unchanged. Newly fetched caches accurately retain their own access flags; separately recovered originals never turn an abstract-only cache into an invented full text. The [19915526 original](https://pubmed.ncbi.nlm.nih.gov/19915526/) supplies the cited Miller syndrome genetics, not an additional enzyme function. Short verbatim anchors occur once in the YAML and are reused by reference; repeated quotation is not repeated evidence.

## 2026-10-17 review follow-up

The protected historical `DHODH-goa.tsv` contains 23 rows. An independent complete [QuickGO API query for Q02127](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB%3AQ02127&limit=200&page=1), captured on 2026-10-17 at 12:25:19 UTC, returned 21 rows on one page. This is an observation at that time, not a statement that the historical cache was refreshed.

| Term/evidence/reference/qualifier key | Historical TSV | Separate timestamped API snapshot |
|---|---|---|
| GO:0004151 / IEA / GO_REF:0000107 / enables | Present | Absent |
| GO:0006221 / IEA / GO_REF:0000043 / involved_in | Present | Absent |
| GO:0016491 / IEA / GO_REF:0000043 / enables | Present | Absent |
| GO:0044210 / IEA / GO_REF:0000107 / involved_in | Absent | Present |

GO:0044210 is de novo CTP biosynthesis. No CTP annotation is added, and this key-level comparison does not assert full WITH/FROM equality. The protected TSV, historical source dictionaries and prior notes are unchanged.

The active ubiquinone-binding proposal uses PMID:8925840 for direct positive human kinetics with ubiquinone-50/decylubiquinone; the verified abstract explicitly provides those findings even though the full original was unavailable. PMID:10673429 remains structural context with a modeled quinone position. The broad historical proposal is refined within its existing position, so there is no duplicate quinone-parent/ubiquinone-child assertion. The ferroptosis proposal is separately withdrawn and uncertain; its retired flag is appropriate under the schema's retirement-or-replacement definition and intentionally excludes it from positive function coverage. Its public reason and dispute remain visible.

No new quotation is introduced. Existing short anchors are reused by reference. The inherited notes contain 26 quoted words from PMID:8925840 and remain byte-identical; zero words are added from that source.
