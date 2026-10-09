# CD70 evidence and annotation review — 2026-10-09

The verified human P32970 seed contains 40 annotations, two alternative-product records and 19 references. All original annotation attributes, interaction partners, qualifiers, product objects and reference identifiers are preserved. The candidate uses existing workspace copies of already present caches and exact recovered archive bytes for missing sources. Source selection and hashes were retained in the working evidence packet. No NEW assertion is proposed.

The annotation-reviewer and core-function-synthesizer skills were applied with the ClinGen project's standing generic-binding override. A genuine isolated Falcon research attempt timed out at 600 seconds; its explicit Perplexity-lite fallback then failed after request retries. No provider report was generated. This document is manual research, not a provider-produced report. The failed attempt produced no research report.

## Molecular activity and physiological context

CD70 is a cell-surface TNF-family ligand for CD27. Expression-cloning studies identify the ligand and its T-cell costimulatory action [PMID:8387892; PMID:8120384]. Human deficiency, receptor binding and rescue studies show that CD70 on presenting B cells supports CD27-dependent T-cell activation and expansion [PMID:28011863; PMID:28011864]. This activity is summarized as receptor ligand activity at the plasma membrane in the CD27 signaling pathway. The inspected production GO-CAM `666b894f00000352` already represents P32970 in that role, separate from the CD27 receptor and intracellular effector nodes. No intracellular kinase/adaptor activity is assigned to the ligand.

The broad InterPro TNF-signaling annotation is refined to CD27 signaling: the current GO definitions distinguish the TNF ligand from CD70/CD27. T-cell and broad lymphocyte proliferation inferences are refined to positive regulation of T-cell proliferation. This describes the ligand's costimulatory role; T-cell division occurs in the responding cell. Source labels and identifiers are retained under `term`, with refinements confined to `review`.

The two seeded products P32970-1 and P32970-2 are preserved exactly. The VSP_056416 sequence note alone does not establish an isoform-specific functional distinction, and none is invented.

## Source-specific decisions

For PMID:28011863, full targeted Results, Methods and legends were read, including CD70 knockout/restoration and CD27-dependence experiments. Generic stimulation and antigen-specific costimulation are distinguished. For PMID:28011864, full relevant Results, Methods and Discussion were read. Reduced memory compartments, humoral defects and impaired EBV immunity support existing broader physiological annotations, but the paper expressly leaves the humoral mechanism uncertain. Row22 (1-based), B-cell proliferation, remains UNDECIDED: its accessible division assays are T-cell assays, and a specific direct B-cell division experiment was not identified. Neither malignancy nor altered population counts is treated as a demonstration of CD70 doing the work of division. This is not a claim that the experimental GOA annotation names the wrong gene.

Five generic binding rows name CD27. They are refined to the independently established receptor-ligand activity using cloning and functional rescue evidence. The exact BioPlex CD27–CD70 pairs were inspected in IntAct: EBI-21555258 for PMID:28514442 and EBI-54533983 for PMID:33961781. Both are HEK293T anti-tag coimmunoprecipitation associations with spoke expansion; neither alone establishes agonism. The exact source-specific supplementary entries for PMID:32822567 and PMID:35922511 were not retrieved. Their identifiers and study methods were checked, but their uninspected target rows are not described as newly verified. The functional refinement rests on independent primary evidence.

The HuRI CD70–ELOVL4 pair from PMID:32296183 is directly represented by three inspected IntAct records from the same study, with validated, array and pooled-prey yeast two-hybrid methods. It remains supported generic binding NC under the project rule, with no inferred fatty-acid-elongation role. These records and UniProt's interaction listing represent overlapping evidence, not independent physiological replication. The interaction record identifiers above identify the inspected source-linked pairs.

The exosome annotation is retained NC. The cached PMID:20458337 abstract describes exosome proteomics; its linked Vesiclepedia CD70 entry identifies target protein detection in human B-cell preparations. The original supplementary mass-spectrometry row was not independently inspected. Study-wide western-blot methodology does not prove a CD70-specific western result, and localization is not equated with exosome biogenesis.

PMID:9177220 has only an abstract in the canonical cache. Its official PubMed Figure1 legend explicitly describes CD70-versus-mock transfectant experiments, including fixed-cell ligand presentation, with apoptotic responses in lymphocyte systems. This supports contextual NC retention of extrinsic apoptotic signaling; the title's focus on CD27/Siva is not a citation error. Full primary body retrieval failed. The distinct activating and death-associated contexts are not conflated into a universal CD70 outcome.

## Access and provenance

All 13 PMID identities and titles were independently checked against official Europe PMC MED records. The cached abstracts and targeted primary sections described above were inspected, distinguishing full target experiments, interaction-database records and inaccessible supplements. The 2024 correction to the immune wiring paper was read: it changes other figure details and references without identifying an altered CD70 result. Retrieval challenge/error responses were not counted as full text. Original caches are unchanged.

Only one short exact anchor appears in the review YAML, and notes contain no verbatim excerpts. The quotation check counted repeated occurrences across the review and these notes. PAINT assertions are considered ancestral-node judgments; target self-evidence is not circular and donor count is not used as a weakness criterion.

Primary links: [human ligand rescue](https://pmc.ncbi.nlm.nih.gov/articles/PMC5206497/), [human deficiency and binding mutants](https://pmc.ncbi.nlm.nih.gov/articles/PMC5206499/), [cloning](https://pubmed.ncbi.nlm.nih.gov/8387892/), [apoptosis figure legend](https://pubmed.ncbi.nlm.nih.gov/9177220/), [immune wiring correction](https://doi.org/10.1038/s41586-024-07928-6).
