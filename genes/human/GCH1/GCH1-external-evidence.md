# GCH1 original-reading scope

The review distinguishes the normal publication cache from independently accessible original text. The following locators describe what was inspected; they do not imply inspection of all figures or supplements. Exact current quotations occur only in the review YAML.

| Source | Inspected scope and limits |
| --- | --- |
| [33229582, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC7750480/) | Selected Methods, Results and Discussion; engineered human GCH1 42–250 and GFRP 1–84. Structural and activity evidence are distinct from the proposed residence-time mechanism. |
| [8068008, author reprint](https://www.researchgate.net/publication/15131256_Human_GTP_cyclohydrolase_I_only_one_out_of_three_cDNA_isoforms_gives_rise_to_the_active_enzyme) | Indexed original construct descriptions, Results narrative and Discussion, plus authenticated abstract. No independent complete historical sequence alignment, figure pixels or table-rate columns. |
| [11087827](https://pubmed.ncbi.nlm.nih.gov/11087827/) | Selected original Methods and Results after direct PMC recovery. Human engineered deletion and bacterial mutagenesis have separate scopes. |
| [16696853, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2239266/) | Selected original Methods/Results; human GCH1, human AHSA1 and rat GFRP retain separate scopes. |
| [21988832](https://pubmed.ncbi.nlm.nih.gov/21988832/) | Original corrected Table S2 row 782 and Methods identify GCH1–YWHAZ. The author-name correction does not alter that row; clone sequence and physiological consequence remain distinct questions. |
| [32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | Six retained original PSI records cover the two transportin partners. Yeast screen/product labels are retained; no individual orthogonal-assay or import mechanism claim. |
| [15604419, indexed original](https://citeseerx.ist.psu.edu/document?doi=53cf4f3bede38a20f506d8d93e15c60610615889&repid=rep1&type=pdf) | Original selected endothelial Methods/Results include a stated negative LPS result. Publisher access was restricted and direct mirror retrieval returned HTML; the readable indexed original, not that failed file, supports the interpretation. |
| [19666465](https://pubmed.ncbi.nlm.nih.gov/19666465/) | Indexed original selected Methods/Results/Discussion distinguish human GCH1 transgene in murine NIH3T3 cells from endogenous murine endothelial knockdown. The methotrexate antioxidant-capacity experiment is a separate intervention. |
| [17717598, original](https://www.jci.org/articles/view/31093) | Selected original Results, Discussion and Methods: human associations and a UTR reporter do not directly measure NOS catalytic activity or natural GCH1 protein isoforms. |
| [25557619](https://pubmed.ncbi.nlm.nih.gov/25557619/) | Selected original Doppler, treatment and developmental Results/Discussion/Figure 4 text. Global-null mouse bradycardia and partial survival rescue do not establish a demonstrated heart-rate rescue. |
| [17057711](https://pubmed.ncbi.nlm.nih.gov/17057711/) | Authentic abstract and publisher abstract only; rat pain interventions and separate human haplotypes are distinguished. Full experimental controls were not independently read. |
| [11087823, original](https://www.pnas.org/doi/10.1073/pnas.240398797) | Complete original main text concerns PAX6 cis-regulation, not GCH1 complex activity. This supports MISCITED; nearby PMID 11087827 is not guessed to be the intended identifier. |

The [Human Protein Atlas GCH1 page](https://www.proteinatlas.org/ENSG00000131979-GCH1/subcellular) was inspected as target-specific text/table evidence: nucleoplasm in A-431, U-251MG and U2OS, cytosol in U-251MG/U2OS, and nuclear membrane in U2OS. Antibody images were not independently interpreted.

The official Reactome graph was checked through every relevant component edge. R-HSA-1474146 uses catalyst 1474128, human decamer 1474144, dimer 1474143 and GCH1 entity 1474127, resolving to P30793 residues 1–250 in cytosol. R-HSA-1474158 contains the same target in input/output complexes. Its inhibitory catalyst 9959889 instead resolves through 1474155/1474159 to P30047 GCHFR. These are model-supported locations, not newly inspected microscopy experiments.

The exact PANTHER19.0 source URLs, target path and sequence hashes are in [the evidence inventory](GCH1-source-evidence.yaml). The unqualified inherited review is preserved unchanged through [the historical archive](GCH1-context-archive.json); its absent qualifiers remain unknown.

## LPS endpoints and complex specificity

[PMID:7678411, indexed original](https://pdfs.semanticscholar.org/4ce7/a625a2788a854c08778b200a06d1e4f9774e.pdf?skipShowableCheck=true) Methods/Results describe HUVEC passages 3–8, 24-hour enzyme/pterin measurements and increased activity after LPS. Indexed dose typography is ambiguous; no figure pixels were inspected. The separate [PMID:15604419 Results](https://doi.org/10.1161/01.RES.0000153669.24827.DF) report absent protein induction, with data not shown. Endpoint differences do not explain the discrepancy. UniProt's collective induction bibliography does not override either experiment.

[GO:0034615 GCH1 complex](https://www.ebi.ac.uk/QuickGO/term/GO:0034615) represents the catalytic assembly, with verified is_a paths to protein-containing complex through catalytic complex and intracellular protein-containing complex. Human homodecamer structures support this refinement; GFRP binding does not require inventing another complex term.

[PMID:17704208](https://pubmed.ncbi.nlm.nih.gov/17704208/) is available here as an authentic abstract: it distinguishes laminar from oscillatory shear and CK2 alpha-prime from the separate astrocyte alpha-subunit pair. Its phosphorylation endpoint is not an additional direct interaction assay for P68400. Full Methods were not inspected.
