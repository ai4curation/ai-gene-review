---
title: DOLK source and assay guide
gene: DOLK
annotation_scope:
  imported_annotations: 25
  new_annotations: 0
---

# DOLK source and assay guide

DOLK directly phosphorylates dolichol to Dol-P. The review retains 25 historical imported assertions, whose triples encompass all 45 current GOA contexts. One inherited authored proposal remains visible but retired. It is not a retired curator assertion. The single catalytic core separates production of the lipid carrier from glycosyl-chain assembly by downstream enzymes.

## Chemistry and product identity

| Source | Operative evidence and limits |
|---|---|
| [PMID:12213788](https://pubmed.ncbi.nlm.nih.gov/12213788/) | Human brain cDNA expressed in yeast and Sf9 cells supports dolichol kinase activity and complementation. Crude microsomal activity is distinguished from DAG kinase. Complete abstract read; original full Methods remained inaccessible. |
| [PMID:16923818](https://pubmed.ncbi.nlm.nih.gov/16923818/) | Human protein expressed in CHO cells is described as an ER membrane protein with luminal N terminus, cytoplasmic C terminus and a cytoplasm-facing CTP-binding region. Complete abstract read; detailed original Methods remained inaccessible. |
| [PMID:17273964, Methods and Figure 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC1821118/) | Crude human fibroblast extracts are assayed with radiolabeled CTP and dolichol, with a no-dolichol background and lipid-product extraction. Patient variants reduce activity; WT human DOLK rescues temperature-sensitive yeast. LLO abundance and downstream glycosylation are separate endpoints. |
| [PMID:22242004](https://pubmed.ncbi.nlm.nih.gov/22242004/) | Patient/control biochemical assays use dolichol-19 and radiolabeled CTP to measure Dol-P. Human WT/mutant ORFs are sequence-verified before yeast complementation. These experiments substantiate cellular kinase activity, not purified-protein kinetics. |
| [PMID:26871637, Figure 6D and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC4882190/) | Historical DOLK_1 rescues restrictive-temperature yeast growth and binds KCNA3; DOLK_2 does not rescue and binds UBQLN1 splice constructs. The actual figure was inspected. Clone-sequence supplements were inaccessible, so the clone names are not mapped to new official products. |

The [official human record Q9UPQ8](https://www.uniprot.org/uniprotkb/Q9UPQ8/entry) and its FASTA agree on one 538-residue protein, without an alternative-products block. Historical splice-clone observations are retained without inventing isoform IDs or declaring that a clone failing one yeast rescue assay is universally inactive.

## Binding pairs and assay context

The [portable source audit](DOLK-bioinformatics/interaction-audit/RESULTS.md) contains exact query bytes, public URLs, hashes, a standard-library Python script and executed outputs. It joins target, partner and PMID; preserves all 42 MITAB fields; recomputes participant ROGIDs; and keeps assay regions and tagged-bait direction separate from sequence identity.

| Source | Target evidence and source-specific boundary |
|---|---|
| [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | Three DOLK–EDA records include validated two-hybrid retesting. Original Methods specify quadruplicate retests, at least three positive attempts and confirmed sequence identity. EDA is a TNF-family cytokine; the binding class does not identify the processed-ligand contact or imply receptor agonism. |
| [PMID:26871637](https://pmc.ncbi.nlm.nih.gov/articles/PMC4882190/) | Three records identify KCNA3 residues 53–575, including validated retesting. Main Methods describe the study's own repeat-screen and sequence-confirmation procedure. Binding to this channel region does not demonstrate modulation of gating. |
| [PMID:28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/) | Two AP-MS records identify tagged KCNA6 and LRRC4C baits recovering DOLK. Platform Methods describe human ORF expression, anti-tag purification and background filtering; a direct interface is not inferred. |
| [PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) | Nineteen current partner contexts join 63 records, with one validated two-hybrid record per partner. Quadruplicate retesting and sequence confirmation are described; the earlier study's three-of-four threshold is not transferred. Sampled orthogonal validation is not asserted for each pair. |
| [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | Three AP-MS records recover DOLK with KCNA6 or LRRC4C in the source platform contexts. Human ORF, tag, purification and background Methods were independently read. Repeated recoveries are not three independent mechanistic demonstrations. |

The exact current definitions of [cytokine binding, GO:0019955](https://www.ebi.ac.uk/QuickGO/term/GO:0019955) and [transmembrane transporter binding, GO:0044325](https://www.ebi.ac.uk/QuickGO/term/GO:0044325) support the two homogeneous-pair refinements. Potassium-channel regulator activity would additionally require modulation, which these assays do not establish. The three heterogeneous historical aggregates remain non-core; applying one subclass would discard other supported partners. Repeated-partner action differences are explained in the audit. The [project's generic-binding instruction](https://github.com/ai4curation/ai-gene-review/blob/c5687cdb1d1c624585433576d6e6fbc2981914be/projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported associations when a finer activity is not established.

## Localization and curated pathway roles

The [HPA target record](https://www.proteinatlas.org/ENSG00000175283-DOLK/subcellular) and [downloadable XML](https://www.proteinatlas.org/ENSG00000175283.xml) report supported nucleolar staining. Approved ICC/IF records include antibodies HPA066767 and HPA068706; the latter reports nucleoli in HaCaT, MCF-7 and U2OS. This contextual observation is retained, without a claim to have independently scored image pixels or genetic specificity controls. ER topology alone does not invalidate it. The active kinase core remains at the experimentally characterized ER membrane.

The normal Reactome path is [R-HSA-446199](https://reactome.org/content/detail/R-HSA-446199) → [reaction R-HSA-446195](https://reactome.org/content/detail/R-HSA-446195) → [catalyst 449273](https://reactome.org/ContentService/data/query/449273) → [human target entity 449274](https://reactome.org/ContentService/data/query/449274) → [Q9UPQ8 reference entity 67698](https://reactome.org/ContentService/data/query/67698). The target is residues 1–538 in ER membrane. The disease [failed reaction R-HSA-4755600](https://reactome.org/content/detail/R-HSA-4755600) separately uses [catalyst 9631897](https://reactome.org/ContentService/data/query/9631897) and [variant set 4755544](https://reactome.org/ContentService/data/query/4755544), with a normalReaction link back to R-HSA-446195. This does not establish normal activity in every mutant.

The target activity in [GO-CAM 66c7d41500000080](https://noctua.geneontology.org/editor/graph/gomodel:66c7d41500000080) is enabled by Q9UPQ8, with GO:0004168, GO:0043048 and GO:0005789. PAINT's literal IBDs for the same function/process/location lie at PTN000324722 on the target PTN002491113 lineage; the aligned target sequence matches all 538 residues. The descendant sources include yeast SEC59 and human DOLK, with other term-specific donors. Target self-evidence is legitimate experimental grounding, not circular propagation.

## The historical additional process proposal

[GO:0006488](https://www.ebi.ac.uk/QuickGO/term/GO:0006488) describes glycosyl-chain assembly on the lipid carrier. DOLK performs carrier phosphorylation. Downstream glycosylation rescue does not identify a glycosyl-addition step performed by DOLK. Current same-role comparators are mixed: SRD5A3 carries GO:0006488, while the checked DHDDS, DOLPP1 and SEC59 records do not. The review therefore does not claim a universal exclusion convention, nor treat absence as a missing-annotation gap. It conservatively withdraws the inherited authored expansion while retaining the directly supported Dol-P synthesis process.

## Access and preservation

| PMID | Existing normal cache | Actual read scope |
|---|---|---|
| 12213788 | Abstract only | Complete abstract; original access attempts unsuccessful. |
| 16923818 | Abstract only | Complete abstract and official target curation; detailed original Methods inaccessible. |
| 17273964 | Full-text flag, partial body | Separately recovered PMC original Methods, biochemical Results and Figure 4 caption. |
| 22242004 | Full text | Operative human assays, variant effects, yeast rescue and Methods. |
| 25416956 | Full text | Separately authenticated original retesting Methods plus exact target pair records. |
| 26871637 | Full-text flag, partial body | Genuine PMC original Methods/Results and actual Figure 6D pixels; clone-sequence supplement unavailable. |
| 28514442 | Full text | Platform Methods and exact target AP-MS records. |
| 32296183 | Full text | Genuine original platform/retesting Methods and all target pair records. |
| 33961781 | Full-text flag, partial body | Separately recovered original AP-MS Methods and target pair records. |

Existing publication bytes and flags, imported source dictionaries and prior notes are preserved. Failed XML, supplement and challenge responses are not treated as article evidence. The public audit provides reproducible machine-source evidence; it is not an independent primary experiment. Remaining biological questions concern the nuclear species, historical splice-clone sequences, native binding contexts and de novo versus recycling contributions.
