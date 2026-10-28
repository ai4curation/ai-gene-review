# FLNB annotation review notes

## 2026-10-28 — initial review

All37 genuine seeded source contexts and nine natural products are preserved. The final decisions are13 ACCEPT,6 KEEP_AS_NON_CORE,8 MODIFY,3 TOO_GENERAL and7 UNDECIDED. One core describes the characterized full-length actin-binding scaffold and its contribution to actin-cytoskeleton organization. See [the source evidence guide](FLNB-source-evidence.yaml) for exact normal-source hashes, primary access, ontology checks and product provenance.

The explicit campaign instructions require reference-only support without new publication quotations and retain supported generic binding as non-core when no specific evidence-backed refinement is established. These instructions take precedence over the local skills’ quotation/default generic-removal recommendations; they are not a legacy-record exception. Default validators remain unchanged. No NEW annotations are introduced. Provider authentication/quota failures were already established in this campaign; manual primary-source research is used without further retries or a fabricated provider report.

Nineteen existing normal dependencies were hydrated exactly from qualified main before genuine fetch. Four qualified absent publications were fetched normally. All23 source files remain immutable after acquisition. The existing PTHR38537 family slice is preserved; no incoming IBA exists, so no phylogenetic propagation assertion is invented.

## Biological and source boundaries

- Human FLNB fragment and full-length observations support the actin scaffold core. Historical PMID:8327473 is a195-residue TABP clone lacking the actin-binding domain; later evidence supports the retained gene-level functions. [PMID:19505475](https://pubmed.ncbi.nlm.nih.gov/19505475/), [PMID:11807098](https://pubmed.ncbi.nlm.nih.gov/11807098/), [PMID:9651345](https://pubmed.ncbi.nlm.nih.gov/9651345/).
- PMID:10676904 is a verified bovine embryo-culture article and remains MISCITED for the imported integrin claim. Its original identifier is preserved and is not used as positive binding support. Independent human construct experiments and the explicit FLNB abstract support integrin-binding refinement; wild-type yeast versus GST pull-down outcomes and enhanced variant binding remain distinct. [PMID:11807098](https://pubmed.ncbi.nlm.nih.gov/11807098/), [PMID:16076904](https://pubmed.ncbi.nlm.nih.gov/16076904/).
- The GRB2 SH2-bait complex in PMID:12577067 remains generic non-core association. Separate FLNB peptide/GRB2 and NCK1 SH3-domain arrays in PMID:17474147 support their own specific refinements and do not identify the SH2-complex interface. [PMID:12577067](https://pubmed.ncbi.nlm.nih.gov/12577067/), [PMID:17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/).
- Actual covalent ISG15 conjugation is established, while a separate noncovalent binding activity remains unresolved. The imported MAP3K4/Q9Y6R4 partner is preserved despite the inspected primary assay naming MKK4; uninspected supplemental experiments are not declared absent. RAC1 and MEKK1 associations support specific partner-class binding, not GEF/GAP or kinase activity by FLNB. [PMID:19270716](https://pubmed.ncbi.nlm.nih.gov/19270716/).
- Human FLNB constructs in mouse hosts, endogenous mouse protein, human HFF1 proteomics and human NT2 associations are kept separate. Historical var-1 sequence boundaries differ from current UniProt by one residue; natural products and engineered constructs are not equated without sequence reconciliation. [PMID:11807098](https://pubmed.ncbi.nlm.nih.gov/11807098/), [PMID:12393796](https://pubmed.ncbi.nlm.nih.gov/12393796/), [PMID:21423176](https://pubmed.ncbi.nlm.nih.gov/21423176/).
- Brush-border Supplement2 TableS1 has a positive mouse FilaminB row (14peptides/8.3% coverage), supporting contextual donor localization. Phagosomal target data remain inaccessible. Cadherin proximity labeling does not resolve the unrecovered FLNB binding entry. [PMID:22114352](https://pubmed.ncbi.nlm.nih.gov/22114352/), [PMID:19144319](https://pubmed.ncbi.nlm.nih.gov/19144319/), [PMID:25468996](https://pubmed.ncbi.nlm.nih.gov/25468996/).

## Individual decisions

Raw indices below refer to the retained official source intake; the stored-order projection is independently checked.

| Raw | Source term | Action | Assessment |
| --- | --- | --- | --- |
| 0 | GO:0003723 RNA binding | UNDECIDED | PMID:22681889 describes photoreactive-nucleotide UV crosslinking, oligo(dT) purification and quantitative proteomics in human embryonic kidney cells. |
| 1 | GO:0003779 actin binding | ACCEPT | Actin binding is a defining FLNB activity, independently corroborated by purified human wild-type FLNB actin-binding-domain co-sedimentation with F-actin in the PMID:19505475 abstract. |
| 2 | GO:0005515 protein binding | UNDECIDED | The exact FLNB-DVL1 experiment in PMID:10644691 could not be recovered. |
| 3 | GO:0005515 protein binding | UNDECIDED | The exact FLNB-DVL2 experiment in PMID:10644691 could not be recovered. |
| 4 | GO:0005515 protein binding | MODIFY | Human FLNB constructs bind beta1-integrin tails with splice-variant and assay dependence. |
| 5 | GO:0005515 protein binding | MODIFY | Human FLNB associates with FLNA through assayed filamin fragments and in NT2 cells. |
| 6 | GO:0005515 protein binding | KEEP_AS_NON_CORE | FLNB is recovered in a GRB2 SH2-bait complex without a resolved pairwise interface. |
| 7 | GO:0005515 protein binding | MODIFY | The cited study explicitly includes FLNB binding to FATZ1/MYOZ1. |
| 8 | GO:0005515 protein binding | MODIFY | The cited study explicitly includes FLNB binding to the cytoskeletal Z-disc protein myotilin. |
| 9 | GO:0005515 protein binding | MODIFY | An FLNB peptide binds three assayed human NCK1 SH3 domains. |
| 10 | GO:0005515 protein binding | MODIFY | An FLNB peptide binds an assayed human GRB2 SH3 domain. |
| 11 | GO:0005515 protein binding | UNDECIDED | Covalent FLNB ISGylation is established; independent noncovalent ISG15 binding remains unresolved. |
| 12 | GO:0005515 protein binding | MODIFY | FLNB associates with RAC1 in the assayed interferon-responsive scaffold. |
| 13 | GO:0005515 protein binding | MODIFY | FLNB associates with the MEKK1 serine/threonine kinase in the assayed signaling scaffold. |
| 14 | GO:0005515 protein binding | UNDECIDED | The imported partner Q9Y6R4 is MAP3K4/MEKK4. |
| 15 | GO:0042802 identical protein binding | ACCEPT | Human FLNB carboxy-terminal fragment self-association is supported by the original PMID:12393796 experiments, with separate fragment crosslinking in PMID:11807098 supporting dimerization. |
| 16 | GO:0045296 cadherin binding | UNDECIDED | Selected original PMID:25468996 Results, Methods and Discussion describe E-cadherin-BirA* proximity labeling in human MKN28 cells with parental controls and replicate proteomics. |
| 17 | GO:0051015 actin filament binding | ACCEPT | The actual InterPro IPR044801 mapping to actin filament binding agrees with independent human FLNB actin-binding-domain co-sedimentation reported in PMID:19505475. |
| 18 | GO:0007165 signal transduction | KEEP_AS_NON_CORE | PMID:19270716 directly supports regulated FLNB scaffold participation in IFN-responsive RAC1/MEKK1 signaling, distinct from the kinases and conjugating enzymes acting on the scaffold. |
| 19 | GO:0030036 actin cytoskeleton organization | ACCEPT | InterPro IPR044801 maps to actin cytoskeleton organization. |
| 20 | GO:0030036 actin cytoskeleton organization | ACCEPT | Actin cytoskeleton organization is independently supported by later human FLNB construct and structural evidence in PMID:11807098, full-length architecture in PMID:9651345, and the actin-binding assay summarized in PMID:19505475. |
| 21 | GO:0001725 stress fiber | ACCEPT | PMID:11807098 directly observes stress-fiber association of human FLNB constructs expressed in mouse fibroblast/myoblast hosts, with endogenous mouse protein examined separately. |
| 22 | GO:0005737 cytoplasm | TOO_GENERAL | The broad cytoplasm location is entailed by independently supported cytosol and cortex localization. |
| 23 | GO:0005829 cytosol | ACCEPT | The actual Human Protein Atlas subcellular report supports FLNB cytosol localization with antibody and cell-line scope. |
| 24 | GO:0005829 cytosol | ACCEPT | The exact Reactome:R-HSA-1169398 summary places FLNB scaffold ISGylation in the cytosol, consistent with actual human-cell experiments in PMID:19270716 and the Human Protein Atlas cytosol report. |
| 25 | GO:0005856 cytoskeleton | TOO_GENERAL | Actin cytoskeleton is an independently supported, more specific descendant of cytoskeleton, confirmed by official QuickGO ancestry. |
| 26 | GO:0005886 plasma membrane | ACCEPT | The actual Human Protein Atlas subcellular report supports plasma-membrane localization in its antibody and cell-line contexts. |
| 27 | GO:0005903 brush border | KEEP_AS_NON_CORE | The actual mouse donor Q80X90 carries IDA PMID:22114352. |
| 28 | GO:0005925 focal adhesion | ACCEPT | Original PMID:11807098 shows focal-contact enrichment of human FLNB constructs in mouse hosts, particularly the combined var-1/hinge-1 deletion; it is not a universal full-length localization result. |
| 29 | GO:0005925 focal adhesion | ACCEPT | Original PMID:21423176 Results explicitly identify filamin B in isolated focal adhesions from human HFF1 fibroblasts and report reduced abundance after myosin-II inhibition. |
| 30 | GO:0005938 cell cortex | ACCEPT | Cell-cortex localization agrees with the membrane-associated actin scaffold role and original PMID:12393796 human NT2 cell-periphery colocalization. |
| 31 | GO:0015629 actin cytoskeleton | ACCEPT | The full-length human beta-filamin architecture described in PMID:9651345 agrees with actin-cytoskeleton localization, independently supported by the actual human FLNB construct experiments in PMID:11807098. |
| 32 | GO:0016020 membrane | TOO_GENERAL | Supported plasma-membrane localization is more specific than this broad membrane term, with official QuickGO ancestry confirming the relation. |
| 33 | GO:0030018 Z disc | KEEP_AS_NON_CORE | PMID:11807098 observes GFP-tagged human filamin B aligned with Z-lines and M-bands in some well-differentiated mouse myotubes. |
| 34 | GO:0045335 phagocytic vesicle | UNDECIDED | Official mouse GOA traces donor Q80X90 to IDA PMID:19144319. |
| 35 | GO:0070062 extracellular exosome | KEEP_AS_NON_CORE | The original authors' urinary-exosome database explicitly lists FLNB/NP_001448 with one peptide and links the entry to PMID:19056867. |
| 36 | GO:0070062 extracellular exosome | KEEP_AS_NON_CORE | The original PMID:23533145 main text describes urinary/prostatic vesicle preparations, but its exact supplementary FLNB target row was not recovered. |

## Natural products

All nine official product records are preserved in their original order. Sequence reconstruction matches individual official FASTAs:1/2602aa,2/2578,3/2561,7/2422,4/2150,5/2146,6/2537,8/2633,9/2591. Truncated products do not inherit blanket full-length dimerization or structural-contact claims. The source guide records the exact variant features and sequence hashes.

## Validation and provenance

A scaffolded Codex history record accompanies this review. Targeted schema/term/reference checks, exact GOA conservation, status reporting, history validation, private HTML rendering, source/context conservation and product replay are recorded in the final review packet. No default validator is relaxed to accommodate the explicit campaign policy.
