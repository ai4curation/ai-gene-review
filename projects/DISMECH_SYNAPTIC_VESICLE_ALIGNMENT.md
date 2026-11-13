---
title: dismech synaptic vesicle disorders aligned with ai-gene-review
maturity: IN_PROGRESS
description: Coordinated review of dismech disorders of synaptic vesicle dysfunction and the gene reviews, PANTHER families, orthologs, modules and GO-CAMs behind their causal genes
tags: [BIOLOGY_DOMAIN]
species: [human, worm, rat]
genes: [STXBP1, UNC13A, SYN1, SYT1, SNAP25, VAMP2, STX1B, CPLX1, DNM1, ATP6V0C, TBC1D24, TSPOAP1, CACNA2D4]
---

# dismech synaptic vesicle disorders aligned with ai-gene-review

dismech models how a disease arises; ai-gene-review records what each gene product normally
does. For a monogenic disorder the two should tell one story: the lesion at the head of the
disease pathograph should be a loss or change of exactly the function the gene review calls
core. This page tracks that agreement for disorders of the synaptic vesicle cycle.

## Scope

The disorders are the 14 dismech entries that declare `conforms_to` on the dismech
`synaptic_vesicle_cycle` mechanism module (`scope.yaml` in the `DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/`
directory beside this page). Ten of them are members of the dismech
`Synaptic_Vesicle_Cycle_Disorders` grouping; the other four (ATP6V0C, TBC1D24, TSPOAP1 and
CACNA2D4 disease) conform to the module without being members.

The genes are the 13 causal genes of those entries. For each gene the review covers the human
gene review, the PANTHER family it belongs to, the ortholog reviews already in this repository,
the vesicle-cycle modules that name it, and the GO-CAM models that use it or an ortholog.

## Method

The comparison is the one built for
[DISMECH_METABOLIC_ALIGNMENT](DISMECH_METABOLIC_ALIGNMENT.md), run over this scope with the same
script (`projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py`). For each gene bound in an
entry's `genetic` records it takes the GO molecular functions and biological processes on the
pathophysiology nodes that name that gene and tests each against the gene review's core
functions, counting a pair as aligned when either term is an is_a/part_of ancestor of the other.
That page sets out why this is a weak test, and the caveats apply here unchanged: the relation is
symmetric and unbounded in distance, node terms are read per node and not per gene, and module
membership is not module coverage.

The table below is generated from the committed report by `make_table.py` in the project
directory. Flag meanings are listed on the metabolic alignment page.

## Baseline, before the review

Run `2026-11-13T00:09:13Z`; dismech `0669e13e5`; ai-gene-review `ba3c1b4ad` (baseline before the coordinated review); GO `2026-07-26`.

| dismech entry | Gene | Relationship | Origin | Nodes naming gene | Review | Aligned node terms | Unmatched node terms | Modules | Flags |
|---|---|---|---|---|---|---|---|---|---|
| STXBP1_Encephalopathy | STXBP1 | - | GERMLINE | 0 | none | - | - | - | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| UNC13A_Congenital_NDD_with_Epilepsy | UNC13A | - | GERMLINE | 0 | none | - | - | - | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| UNC13A_NDD_with_Seizures_and_Movement_Disorder | UNC13A | - | DE_NOVO | 0 | none | - | - | - | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| SYN1-Related_Disorder | SYN1 | CAUSATIVE | GERMLINE | 1 | COMPLETE | `GO:0099504` | `GO:0140090`, `GO:7770062` | synaptic_vesicle_cycle | `PARTIAL_ALIGNMENT` |
| SYT1_Baker-Gordon_Syndrome | SYT1 | CAUSATIVE | DE_NOVO | 1 | none | - | - | - | `NO_AIGR_REVIEW` |
| SNAP25_Encephalopathy | SNAP25 | CAUSATIVE | GERMLINE | 0 | none | - | - | - | `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| VAMP2-Related_Disorder | VAMP2 | - | GERMLINE | 0 | none | - | - | - | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| STX1B-Related_Epilepsy | STX1B | - | GERMLINE | 0 | none | - | - | - | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| CPLX1-Related_DEE | CPLX1 | CAUSATIVE | GERMLINE | 1 | none | - | - | - | `NO_AIGR_REVIEW` |
| DNM1_Encephalopathy | DNM1 | - | GERMLINE | 0 | DRAFT | - | - | synaptic_vesicle_cycle, synaptic_vesicle_endocytosis | `UNTYPED`, `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `AIGR_NOT_COMPLETE` |
| ATP6V0C-Related_Epilepsy | ATP6V0C | CAUSATIVE | GERMLINE | 1 | COMPLETE | `GO:0046961` | - | vacuolar_atpase_acidification | ok |
| Developmental_And_Epileptic_Encephalopathy_16 | TBC1D24 | CAUSATIVE | GERMLINE | 0 | none | - | - | - | `GENE_ON_NO_NODE`, `NO_GO_ON_GENE_NODES`, `NO_AIGR_REVIEW` |
| Dystonia_22_Juvenile_Onset | TSPOAP1 | CAUSATIVE | - | 1 | none | - | - | - | `NO_ORIGIN`, `NO_AIGR_REVIEW` |
| CACNA2D4-related_Retinopathy | CACNA2D4 | CAUSATIVE | GERMLINE | 1 | COMPLETE | `GO:0005246` | - | - | `NO_MODULE_MEMBERSHIP` |

What the baseline shows:

- **Eight of the 14 entries name their causal gene on no pathophysiology node**
  (`GENE_ON_NO_NODE`). The gene is bound in `genetic`, and the node text describes its protein,
  but no node carries a `genes` descriptor, so the pathograph does not link gene to mechanism and
  there is nothing to compare against a gene review.
- **Six genetic records carry no `relationship_type`** (`UNTYPED`), and one carries no
  `variant_origin` (`NO_ORIGIN`).
- **Ten of the 13 genes had no finished human review** when the audit ran: nine had none
  (`NO_AIGR_REVIEW`) and DNM1 was a draft.
- Of the three entries that could be compared, ATP6V0C and CACNA2D4 align on their core
  molecular function. SYN1 aligns on the synaptic vesicle cycle process, while two molecular
  functions on its dismech node, `GO:0140090` membrane curvature sensor activity and `GO:7770062`
  vesicle membrane tethering activity, match nothing in the SYN1 review's core functions.
- ATP6V0C sits in the `vacuolar_atpase_acidification` module but not in
  `synaptic_vesicle_neurotransmitter_loading`, which represents the vesicle proton pump by its
  catalytic A subunit alone. CACNA2D4 is in no module.

## Coverage of the genes beyond their reviews

PANTHER families. Names are PANTHER's own, from `interpro/panther/panther.obo`.

| Gene | UniProt | Family | Subfamily | PAINT slice cached | Family review |
|---|---|---|---|---|---|
| STXBP1 | P61764 | `PTHR11679` VESICLE PROTEIN SORTING-ASSOCIATED | - | no | none |
| UNC13A | Q9UPW8 | `PTHR10480` PROTEIN UNC-13 HOMOLOG | `SF1` PROTEIN UNC-13 HOMOLOG A | no | none |
| SYN1 | P17600 | `PTHR10841` SYNAPSIN | `SF24` SYNAPSIN-1 | no | none |
| SYT1 | P21579 | `PTHR10024` SYNAPTOTAGMIN | `SF239` SYNAPTOTAGMIN-1 | no | none |
| SNAP25 | P60880 | `PTHR19305` SYNAPTOSOMAL ASSOCIATED PROTEIN | `SF5` SYNAPTOSOMAL-ASSOCIATED PROTEIN 25 | no | none |
| VAMP2 | P63027 | `PTHR45701` SYNAPTOBREVIN FAMILY MEMBER | - | no | none |
| STX1B | P61266 | `PTHR19957` SYNTAXIN | `SF334` SYNTAXIN-1B | yes | none |
| CPLX1 | O14810 | `PTHR16705` COMPLEXIN | `SF6` COMPLEXIN-1 | yes | none |
| DNM1 | Q05193 | `PTHR11566` DYNAMIN | `SF32` DYNAMIN-1 | yes | none |
| ATP6V0C | P27449 | `PTHR10263` V-TYPE PROTON ATPASE PROTEOLIPID SUBUNIT | - | yes | none |
| TBC1D24 | Q9ULP9 | `PTHR23354` NUCLEOLAR PROTEIN 7/ESTROGEN RECEPTOR COACTIVATOR-RELATED | `SF122` GTPASE-ACTIVATING PROTEIN SKYWALKER | not cached | none |
| TSPOAP1 | O95153 | `PTHR14234` RIM BINDING PROTEIN-RELATED | `SF20` PERIPHERAL-TYPE BENZODIAZEPINE RECEPTOR-ASSOCIATED PROTEIN 1 | yes | none |
| CACNA2D4 | Q7Z3S7 | `PTHR10166` VOLTAGE-DEPENDENT CALCIUM CHANNEL SUBUNIT ALPHA-2/DELTA-RELATED | `SF59` VOLTAGE-DEPENDENT CALCIUM CHANNEL SUBUNIT ALPHA-2_DELTA-4 | no | none |

Ortholog reviews already in the repository:

| Human gene | Worm | Rat | Other |
|---|---|---|---|
| STXBP1 | unc-18 | Stxbp1 | - |
| UNC13A | unc-13 | - | - |
| SYN1 | snn-1 | - | human SYN2 (paralog) |
| SYT1 | snt-1 | Syt1 | - |
| SNAP25 | ric-4 | - | - |
| VAMP2 | snb-1 | - | - |
| STX1B | unc-64 | - | - |
| CPLX1 | cpx-1 | - | squid cpx (`DORPE`) |
| DNM1 | dyn-1 | - | human DNM2 (paralog, draft) |
| ATP6V0C | vha-1 | - | human ATP6V0B (paralog) |
| TBC1D24 | - | - | - |
| TSPOAP1 | rimb-1 | - | human RIMBP2 (paralog) |
| CACNA2D4 | - | - | human CACNA2D1 (paralog) |

There are no fly or mouse reviews for any of these genes.

Modules. The umbrella `synaptic_vesicle_cycle` module and its three stage modules
(`synaptic_vesicle_neurotransmitter_loading`, `synaptic_vesicle_exocytosis`,
`synaptic_vesicle_endocytosis`) are all drafts. Of the 13 genes they name STXBP1, UNC13A, SYN1,
SYT1, SNAP25, VAMP2, CPLX1 and DNM1 as participants. STX1B is represented by its paralog STX1A,
TSPOAP1 by its paralog RIMBP2, and ATP6V0C, TBC1D24 and CACNA2D4 are absent.

GO-CAM models that use one of the genes or an ortholog (`gocams/index.tsv`); none has a review yet:

| Model | Species | Title | In-scope activities |
|---|---|---|---|
| `69729a3800000783` | rat | Stxbp1 SNARE assembly | Stxbp1, Unc13a, Vamp2 |
| `682fbcd000006614` | rat | Syp vesicle fusion | Vamp2 (with Syp) |
| `682fbcd000002630` | rat | Syt1 vesicle organization | Syt1 (with Csnk1a1, Sv2a) |
| `69729a3800000567` | rat | dense core granule exocytosis | Unc13a, Snap25 (with Cadps) |
| `62f58d8800006739` | mouse | Negative regulation of insulin secretion 2 | Snap25 |
| `5b528b1100000489` | worm | XBP-1 is a cell-nonautonomous regulator of stress resistance and longevity | unc-13 |

## Open

- Human gene reviews for the nine unreviewed genes, and completion of DNM1.
- Family reviews for the 13 families.
- Reviews of the six GO-CAM models.
- dismech: gene descriptors on the lesion nodes, typed genetic records, and review of each entry.
- A second audit run once both sides have changed.
