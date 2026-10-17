# DDX11 evidence access guide

Access checked 2026-10-17. This guide records where the review's evidence was read; an abstract-only repository cache does not imply that an original was unavailable elsewhere. Conversely, a successful HTTP response containing a challenge page is not a recovered paper. Zero-based row numbers below are locators only; the GO term, evidence code and original reference identify each immutable source assertion.

| Source | Actual access and scope |
| --- | --- |
| [Hirota and Lahti, 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC102573/) · PMID 10648783 | Separately recovered original; recombinant constructs, ATPase and unwinding Methods/Results, polarity assays and limitations read. Normal cache remains abstract-only. |
| [Parish et al., 2006, JCS](https://journals.biologists.com/jcs/article/119/23/4857/29186/The-DNA-helicase-ChlR1-is-required-for-sister) · PMID 17105772 | Publisher-indexed original Methods, localization figures, co-immunoprecipitation, cohesion measurements and Discussion read. Cache is abstract-only. |
| [Parish et al., 2006, Molecular Cell](https://doi.org/10.1016/j.molcel.2006.11.005) · PMID 17189189 | Abstract and bibliographic metadata only. Publisher PDF failed; Birmingham repository returned metadata/abstract with no original download. Row 23 remains undecided; independent evidence supports the general locations. |
| [Farina et al., 2008](https://doi.org/10.1074/jbc.M802696200) · PMID 18499658 | Separately recovered PMC original Methods and Results, especially Figs. 6–8. Cache remains abstract-only. Distinguishes recombinant PCNA added to lysate, RFC-subunit co-purification and isolated FEN1 binding. |
| [Kang et al., 2008](https://doi.org/10.1021/pr800225z) · PMID 18570454 | Abstract only; the DDX11 protein-level supplementary record was not recovered. Failed/empty exploratory responses are not evidence. Row 78 remains undecided. |
| [Leman et al., 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2823575/) · PMID 20124417 | Genuine original, interaction and fractionation Methods/Results and cohesion experiments read. |
| [Wu et al., 2012](https://doi.org/10.1074/jbc.M111.276022) · PMID 22102414 | Separately recovered PMC original, construct/purification, ATP binding versus turnover, defined-substrate Methods/Results and Discussion read. Cache remains abstract-only. |
| [Shah et al., 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3752303/) · PMID 23797032 | Full original text in the normal cache; depletion, damage/repair and replication-recovery experiments read, including the authors' causal limitation. |
| [Sun et al., 2015](https://doi.org/10.1093/hmg/ddv213) · PMID 26089203 | Original article text, including Methods, read through the [author-uploaded indexed full text](https://www.researchgate.net/publication/280846002_The_Warsaw_breakage_syndrome-related_protein_DDX11_is_required_for_ribosomal_RNA_synthesis_and_embryonic_development). Publisher/raw mirror retrieval failed; normal cache remains abstract-only. Evidence includes human-cell localization, rDNA assays and co-immunoprecipitation. |
| [Calì et al., 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4737141/) · PMID 26503245 | Full original in cache: purified-protein substrate/binding assays, TIMELESS interaction and hydroxyurea DNA-fiber experiments read. |
| [Marchese et al., 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5893147/) · PMID 27477908 | Full cached text plus genuine NCBI BioC original. CONCR capture/RIP, chromatin fractionation/ChIP-seq, rescue and ATPase passages read. A separate attempted HTML response was a challenge, not evidence. |
| [Huttlin et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165030/) · PMID 33961781 | Genuine original previously recovered in the shared evidence packet; AP-MS, clone and gene-aggregation Methods read. Literal IntAct FUZ–DDX11 record was independently inspected. |
| [Qin et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9053732/) · PMID 34819669 | Genuine original and AP-MS/image-integration Methods read. Supplementary Table 1 was not recovered; the exact second FUZ–DDX11 record remains unresolved (row 33). |
| [Frank and Werner, 1996](https://doi.org/10.1074/jbc.271.40.24337) · PMID 8798685 | Indexed original cloning Methods/Results and Discussion read. Its helicase statement was a sequence-based prediction, not an activity assay. |
| [Amann et al., 1997](https://doi.org/10.1074/jbc.272.6.3823) · PMID 9013641 | Indexed original DNA-cellulose experiments, antibody Methods and localization passages read. Historical antibody limitations are considered with the later evidence. |

The source paths in the private audit packet retain the raw responses, source identifiers, retrieval receipts, exact selected passages and hashes. Those paths are provenance aids, not additional literature citations. Public claims can be checked through the links above. No uncached full-text passage is inserted as a `supporting_text` quote.

| Structured evidence | What was inspected |
| --- | --- |
| [UniProt Q96FC9](https://www.uniprot.org/uniprotkb/Q96FC9/entry) and [HGNC:2736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2736) | Official identity, historical aliases, locations, catalytic mappings and all five alternative sequences. |
| [InterPro target matches](https://www.ebi.ac.uk/interpro/protein/UniProt/Q96FC9/) | Seven actual target matches, five annotation-bearing domain/family mappings and target coordinates. Generic family labels were not used as evidence of a wrong paralog. |
| [PANTHER PTHR11472](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR11472) | Saved PAINT IBD rows, complete tree path to target PTN002479319, donor descendants and alignment. The target aligned sequence equals the current 970-residue displayed product. The yeast donor's [experimental source abstract](https://pubmed.ncbi.nlm.nih.gov/23334284/) was read; no new yeast annotation is proposed. |
| [Human Protein Atlas DDX11](https://www.proteinatlas.org/ENSG00000013573-DDX11/subcellular) | HPA v25 XML: nucleoplasm/nucleoli, cell lines, HPA065197 and antigen sequence. Image metadata was read; no independent microscopic image reanalysis is claimed. |
| [Reactome expression event](https://reactome.org/content/detail/R-HSA-1791116) | Typed output R-HSA-535492 → reference Q96FC9 → nucleoplasm. An expression product was not treated as the catalyst of the expression event. |
| [Rhea 13065](https://www.rhea-db.org/rhea/13065) and [EC 5.6.2.3](https://enzyme.expasy.org/EC/5.6.2.3) | Official reaction and directional-helicase definitions, compared with the frozen UniProt record. |
| [QuickGO](https://www.ebi.ac.uk/QuickGO/) | Current definitions and typed `is_a` paths for proposed replacements, including [D-loop DNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0062037), [RNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003723) and [ATP hydrolysis activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016887). |
| [IntAct](https://www.ebi.ac.uk/intact/) and official partner UniProt records | Exact FUZ bait/DDX11 prey source record for PMID 33961781; partner identity/function checks for RAD21, SMC3, TIMELESS, POLR1A, UBTF and E2. Co-purification is not represented as purified binary binding. |

No NEW annotation is proposed. The three source-specific undecided assertions are explicit evidence limits, not removal decisions. The source dictionaries, NOT flag and alternative products remain intact.


## 2026-10-17 follow-up source locators

The current annotation reasons supersede earlier coupled-activity retention based on ATPase synonyms. GO:0008094 requires ATP-driven DNA modification; GO:0008186 requires RNA-dependent ATP hydrolysis that drives another reaction. The measured turnover therefore maps to GO:0016887. GO:0033677 expressly covers DNA/RNA-hybrid unwinding; no NEW annotation is needed.

| Original source | Locator and scope |
| --- | --- |
| [PMID:10648783](https://pubmed.ncbi.nlm.nih.gov/10648783/) | Helicase Methods, Fig.5B and substrate-specificity Results. The hybrid assay's labeling limitation is retained in the review; no native R-loop role is inferred. |
| [PMID:18499658](https://pubmed.ncbi.nlm.nih.gov/18499658/) | Directionality and Substrate Specificity; Fig.4. DNA loading-strand directionality; the additional hybrid observation is explicitly data not shown. |
| [PMID:26089203](https://pubmed.ncbi.nlm.nih.gov/26089203/) | Fig.7B–C; ATPase Methods. Human FLAG-DDX11 from HEK293 cells; rDNA fragment −410 to +81; turnover and mutant comparison. |
| [PMID:27477908](https://pubmed.ncbi.nlm.nih.gov/27477908/) | Figs.5–6 and associated Results. CONCR association and ATP turnover; wild-type/K50R cohesion rescue is a separate cellular experiment. |
| [PMID:26503245](https://pubmed.ncbi.nlm.nih.gov/26503245/) | DNA-fiber Methods; Fig.7A–C. HU treatment/removal and fork restart in depleted HeLa cells. |
| [PMID:20124417](https://pubmed.ncbi.nlm.nih.gov/20124417/) | Fig.5A–D; plasmid and RNAi Methods. Human ChlR1 association, depletion and partial cohesion rescue. |

The one nuclear helicase core includes already represented GO:0031297 and GO:0034085; G4 substrate capacity alone does not establish a second evolved core. Original product, antibody, access and interaction limitations remain applicable. The table adds locators, not publication quotations.
