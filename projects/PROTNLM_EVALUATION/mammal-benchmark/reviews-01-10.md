---
species: [HORSE, human]
---

# Paired reviews 01–10

The initial pass assesses all 688 existing GOA rows across these ten human–horse pairs, with no PENDING actions. All ten human genes have completed Falcon research reports; GHSR also has a horse-specific report because direct horse literature warranted it. Primary sources are cached separately, and each horse target has a reproducible alignment with mapped human sequence features. Gene reviews remain IN_PROGRESS where assay, phylogenetic or protein-model questions are unresolved.

| Gene | Human / horse GOA rows | External prediction assessment | Main finding |
|---|---:|---|---|
| VAPA | 182 / 3 | PLI, function paragraph | ER membrane adaptor with an MSP domain does not acquire nematode sperm-crawling function. |
| CAPSL | 3 / 1 | NPI, function paragraph | Venom-secretion narrative conflicts with intracellular family biology; human endothelial studies and emerging mammalian ciliary evidence inform function. |
| MYL10 | 12 / 5 | NPI, function paragraph | Venom narrative is unsupported for the conserved EF-hand light-chain protein. |
| KRIT1 | 51 / 5 | NPI, function paragraph | Rap1-associated CCM junctional scaffold is assigned a piRNA/germ-granule narrative. |
| CTDSP2 | 20 / 0 | UNC, GO:0016301 kinase activity | The selected 174-residue horse model lacks the canonical phosphatase catalytic region. A gene-name-based phosphatase/kinase contradiction would overstate exact-sequence evidence. |
| PEA15 | 21 / 4 | UNC, GO:0008643 carbohydrate transport | Direct human experiments establish regulation of glucose-transporter recruitment and uptake; whether the exact transport-process term is appropriate remains unresolved. |
| ALDH7A1 | 42 / 10 | UNC, GO:0043878 substrate-specific dehydrogenase | Broad aldehyde activity does not establish glyceraldehyde-3-phosphate oxidation; an internal 18-residue horse deletion adds uncertainty. |
| GHSR | 90 / 33 | PLI, function paragraph | Ghrelin receptor is assigned oxytocin-receptor function. A separate GHRH-receptor GO error propagates from human to horse and is corrected in both reviews. |
| ALG5 | 19 / 2 | PLI, function paragraph | ALG5-family UDP-glucose chemistry is confused with GDP-mannose/DPM synthesis; the selected horse protein has an internal 30-residue deletion. |
| HSPD1 | 178 / 7 | PLI, function paragraph | Mitochondrial type I Hsp60 is assigned type II CCT/TRiC and its clients. A concordant horse electronic CCT-complex annotation is removed. A 32-residue deletion limits exact Hsp60 activity transfer. |

The three GO predictions have standard prediction-review YAMLs. The seven original function paragraphs are preserved verbatim in gene-specific `GENE-protnlm-function-review.md` reports and assessed as atomic claims. Paragraph assessments describe the principal biological assertion; shared generic clauses are separately identified and do not rescue an incorrect specific complex, substrate or physiological context. Training-set membership is unknown.

Human GHSR and horse GHSR receive particular attention to the distinction between ghrelin and growth-hormone-releasing hormone. [PMID:10604470](https://pubmed.ncbi.nlm.nih.gov/10604470/) explicitly separates the pathways. Horse-specific [PMID:42426797](https://pubmed.ncbi.nlm.nih.gov/42426797/) supports sequence-confirmed receptor transcript in pituitary and adrenal medulla; [PMID:29526750](https://pubmed.ncbi.nlm.nih.gov/29526750/) studies receptor-associated ghrelin responses in equine chondrocytes. Tissue expression, pharmacology and exact-accession binding competence remain distinct evidence claims.

Validation: all 20 main gene YAMLs pass individual validation, all three prediction YAMLs pass schema and evidence validation, all seven original paragraphs match the frozen source CSV, and all 20 HTML pages render. Matching history records were scaffolded and validated for each curated gene. Warnings about omitted core functions for unresolved horse models and uninspected details of particular IBA placements remain explicit; no unsupported function was added merely to silence an advisory.
