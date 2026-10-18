---
title: DPM1 source and assay guide
gene: DPM1
annotation_scope:
  imported_annotations: 43
  new_annotations: 0
---

# DPM1 source and assay guide

DPM1 supplies the catalytic component of Dol-P-Man synthesis at the ER membrane. The single core distinguishes that reaction from production of its Dol-P substrate, downstream glycosylation and the separate flipping step. All 43 historical source assertions remain intact; current raw provenance contains 44 contexts because one term/evidence/reference assertion has two provider/date contexts. Newly fetched metadata is retained separately from the historical source dictionaries.

## Catalysis, anchoring and products

| Source | Actual evidence and limits |
|---|---|
| [PMID:9535917](https://pubmed.ncbi.nlm.nih.gov/9535917/) — [indexed author original](https://www.researchgate.net/publication/51328247_A_Homologue_of_Saccharomyces_cerevisiae_Dpm1p_Is_Not_Sufficient_for_Synthesis_of_Dolichol-Phosphate-Mannose_in_Mammalian_Cells) | Human and mouse DPM1 constructs rescue mouse class E cells but fail in hamster Lec15 cells under the reported conditions. Microsomal GDP-mannose/Dol-P assays measure Dol-P-Man, and human GST-DPM1 membrane fractionation is described. Original Methods, Results and Discussion were read; the normal cache remains abstract-only. Its O-linked-glycan example explicitly concerns yeast. |
| [PMID:9724629](https://pubmed.ncbi.nlm.nih.gov/9724629/) — [indexed author original](https://www.researchgate.net/publication/13560298_DPM2_regulates_biosynthesis_of_dolichol_phosphate-mannose_in_mammalian_cells_correct_subcellular_localization_and_stabilization_of_DPM1_and_binding_of_dolichol_phosphate) | Human DPM1 and rat DPM2 in hamster-host co-immunoprecipitation/fractionation are distinguished from the engineered human DPM1–rat microsomal ALDH anchor. The fusion forms Dol-P-Man without DPM2. DPM3 was not removed, and this was not purified unanchored human DPM1. The continuation around Figure 9 describes lipid association without proving zero DPM1 substrate binding. |
| [PMID:10835346, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC212771/) | Human DPM1-containing complexes purified from JY25 cells were reconstituted in PC/PE liposomes; GDP-[3H]mannose incorporation and lipid TLC establish product formation. The synthase assay was performed without exogenous Dol-P. Separate hamster Lec15 experiments used human DPM1/DPM3 and rat DPM2. DPM3 overexpression permits activity without DPM2, with lower specific activity. Results, Methods and figure captions were read; image pixels were not independently scored. |
| [PMID:10944123, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC302040/) | Controlled human tagged DPM1–DPM3 co-immunoprecipitation supports their association. The separate GPI-GnT association is specific to DPM2, not DPM1 or DPM3. |
| [PMID:16280320](https://pubmed.ncbi.nlm.nih.gov/16280320/) | The complete abstract positively reports DPM3-mediated anchoring, DPM1 degradation without DPM3 and association of free DPM1 with CHIP. Full-body access attempts were unsuccessful; exact CHIP construct/tag/panel details are not claimed. The current IntAct participant record is human DPM1 with hamster DPM3, not a STUB1 record. |
| [PMID:23856421, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3800268/) | Human WT/G152V DPM1–DPM3 co-immunoprecipitation includes expression controls. Reduced binding and patient-membrane synthase activity are positive findings, not proof of complete binding loss. Muscle glycoepitope changes support human O-mannosylation context. Patient-cell labels vary within the paper; the activity preparation is described conservatively as patient membranes. |
| [PMID:28743912, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC5526996/) | Purified Pyrococcus furiosus Q8U4M3 expressed in E. coli provides substrate/product structures, metal dependence and biochemical activity. The high-temperature assay and membrane topology are not human measurements. This directly grounds the archaeal ISS donor rather than a human structural claim. |

The [official human O60762 record](https://www.uniprot.org/uniprotkb/O60762/entry) and FASTA establish one 260-residue primary sequence without an alternative-products block. Initiator-methionine removal produces the annotated chain 2–260, PRO_0000059170, with acetylated Ala2. Processing does not create a separate splice product or establish another function.

The core uses [GO:0004582](https://www.ebi.ac.uk/QuickGO/term/GO:0004582) as a catalytic contribution to the physiological complex while preserving all imported source qualifiers, including `enables`. DPM1 remains the catalytic subunit. This conservative complex context does not claim DPM2 is indispensable for all activity. [GO:0180047](https://www.ebi.ac.uk/QuickGO/term/GO:0180047) describes Dol-P-Man formation; [GO:0043048](https://www.ebi.ac.uk/QuickGO/term/GO:0043048) describes Dol-P formation and is not the measured DPM1 reaction. The replacement is a chemistry correction, not an asserted ontology ancestor relation.

## Binding identity and assay specificity

The [portable interaction audit](DPM1-bioinformatics/interaction-audit/RESULTS.md) includes exact raw query bytes, public URLs and hashes, all 42 MITAB fields, participant-sequence calculations and executed outputs. Ten selected records represent repeated source/assay contexts for DPM3, TDO2 and a MEOX2 clone, not ten independent partners. Source records absent from that snapshot are assessed from their original experiments.

| Source | Target evidence |
|---|---|
| [PMID:25416956, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC4266588/) | Three DPM1–TDO2 records include validated two-hybrid retesting. Original Methods describe fresh-colony quadruplicate tests, at least three positive attempts and confirmed identities. Dataset-level orthogonal tests are not assigned to the DPM1 pair without pair-specific evidence. |
| [PMID:25910212, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC4441215/) | Three DPM1–TDO2 records retain variant features and repeat-assay contexts. Original Methods distinguish Y2H from separately used LUMIER assays. Normal cached text omits some operative Methods that were read in the indexed original. |
| [PMID:32296183, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) | Three DPM1–Q6FHY5 records include validated two-hybrid retesting. HuRI reports quadruplicate retests and sequence confirmation; the earlier 2014 three-of-four threshold is not transferred. Q6FHY5 reproduces its recorded checksum. It differs from canonical MEOX2 P50222 by one glutamine within positions 81–84, outside the homeobox. The repeated sequence prevents assigning a unique deletion position. |

[TDO2 P48775](https://www.uniprot.org/uniprotkb/P48775/entry) is an enzyme, supporting [GO:0019899 enzyme binding](https://www.ebi.ac.uk/QuickGO/term/GO:0019899). [MEOX2 P50222](https://www.uniprot.org/uniprotkb/P50222/entry) has curated DNA-dependent transcriptional activity, supporting [GO:0140297](https://www.ebi.ac.uk/QuickGO/term/GO:0140297) for the verified clone. The positive CHIP association supports [GO:0031625 ubiquitin protein ligase binding](https://www.ebi.ac.uk/QuickGO/term/GO:0031625). These are partner-class statements, not assertions that DPM1 catalyzes TDO2 chemistry, regulates transcription or performs ubiquitination.

[DPM3 Q9P2X0](https://www.uniprot.org/uniprotkb/Q9P2X0/entry) is an anchoring/stabilizing subunit, not an independently demonstrated enzyme. Its supported contacts remain non-core protein binding under the [ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/c8e8122a09c0722c9b56ef378ec0ffd8646ff3c0/projects/CLINGEN_MENDELIAN.md#curation-instructions). Controlled association does not automatically establish a purified interface or an additional native pathway, and lack of the latter does not invalidate a literal binding class.

## Localization and context

[PMID:21630459](https://pubmed.ncbi.nlm.nih.gov/21630459/) is supplemented by the author's [public thesis](https://diposit.ub.edu/server/api/core/bitstreams/748602ae-3122-4398-88b1-5043df608fcb/content). Table 8.1, physical PDF page 194 (printed page 193), lists DPM1/O60762 with 13.1% sequence coverage and two peptides. The inspected Methods cover CTAB/digitonin nuclear isolation and MS identification with false-discovery filtering and a minimum of two peptides including one unique peptide. This is positive fraction-level localization without a demonstrated nuclear catalytic role. No claim that the source microscopy images were independently scored is made. ER tethering alone does not prove contamination.

[PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) describes the YTS membrane-proteome survey. The particular DPM1 table row remained unverified, so ER-membrane refinement is grounded in the independent DPM1 fractionation/anchoring studies, not represented as organelle resolution by that survey. [HPA's downloadable target XML](https://www.proteinatlas.org/ENSG00000000419.xml) contains tissue staining but no target ICC/IF subcellular-assay records in the inspected snapshot. It is not used as direct ER imaging.

## Propagation and pathway entities

The [PANTHER family PTHR43398](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR43398) tree contains the exact human O60762 leaf PTN002535381. Its ungapped alignment matches all 260 residues. The 22-node ancestor path joins the literal PAINT IBDs: PTN000092441 for ER membrane, PTN000092440 for dolichol-linked oligosaccharide biosynthesis and PTN002459128 for mannosyltransferase activity. Human target evidence among descendant sources is legitimate, not circular. The broader oligosaccharide process is retained as non-core donor-supply context rather than denied solely because its direct polymerization is performed downstream.

The normal Reactome chain is [pathway R-HSA-162699](https://reactome.org/content/detail/R-HSA-162699) → [reaction R-HSA-162721](https://reactome.org/content/detail/R-HSA-162721) → [catalyst 162705](https://reactome.org/ContentService/data/query/162705) → [complex 162692](https://reactome.org/ContentService/data/query/162692) → [DPM1 entity 162865](https://reactome.org/ContentService/data/query/162865) → [O60762 reference 53836](https://reactome.org/ContentService/data/query/53836). The target chain is residues 2–260 in ER membrane. The separate [flipping reaction R-HSA-162715](https://reactome.org/content/detail/R-HSA-162715) is not assigned to DPM1.

Disease contexts are separately resolved: [DPM1 failed reaction R-HSA-4717406](https://reactome.org/content/detail/R-HSA-4717406) uses [catalyst 9631868](https://reactome.org/ContentService/data/query/9631868), [complex 9631831](https://reactome.org/ContentService/data/query/9631831) and [variant set 4717364](https://reactome.org/ContentService/data/query/4717364); [DPM3 failed reaction R-HSA-4719354](https://reactome.org/content/detail/R-HSA-4719354) uses [catalyst 9631797](https://reactome.org/ContentService/data/query/9631797) and [complex 9631746](https://reactome.org/ContentService/data/query/9631746), retaining normal DPM1 with DPM3 L85S; [DPM2 failed reaction R-HSA-4719375](https://reactome.org/content/detail/R-HSA-4719375) uses [catalyst 9631985](https://reactome.org/ContentService/data/query/9631985) and [complex 9631812](https://reactome.org/ContentService/data/query/9631812), retaining normal DPM1 with DPM2 Y23C. These records do not establish normal activity for every pathogenic variant.

The inspected GO-CAM target index has no O60762 activity. The cached dolichol-phosphate sugar-donor module supplies pathway context, not evidence for a new annotation. No absence-based process expansion is made.

## Access and preservation

| PMID | Effective normal cache | Actual read scope |
|---|---|---|
| 9535917 | Abstract only | Indexed author original Methods, functional rescue, fractionation and Discussion. |
| 9724629 | Abstract only | Indexed author original Methods/Results and fusion/lipid-association continuation. |
| 10835346 | Abstract only | Indexed PMC original Results, Discussion, Methods and relevant captions. |
| 10944123 | Abstract only | Separately recovered original target co-immunoprecipitation, GPI-GnT results and Methods. |
| 16280320 | Abstract only | Complete abstract; original-body attempts failed. |
| 19946888 | Abstract only | Complete abstract; target identification table not recovered. |
| 21630459 | Abstract only | Complete abstract plus authenticated author-thesis target table and isolation/MS Methods. |
| 23856421 | Abstract only | Separately recovered PMC original target assays, controls and Methods. |
| 25416956 | Full text | Authenticated original retesting Methods and exact target pair records. |
| 25910212 | Full-text flag, partial Methods | Indexed original repeat-assay/sequence Methods and exact target records. |
| 32296183 | Full text | Original platform/retesting Methods and exact target records. |
| 28743912 | New genuine full XML cache | Archaeal Methods, substrate/product structures and activity Results. |

Existing source/cache bytes and flags, provider files and historical notes are preserved. Failed routes, challenge pages and superseded parsing attempts are not treated as biological evidence. Existing excerpts remain legacy content; this reassessment adds no quoted source text. The public audit is a reproducible analysis of machine-source records, not an independent primary experiment.
