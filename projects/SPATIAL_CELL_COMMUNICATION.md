---
title: "Spatial cell-cell communication: curated ligand modules meet spatial omics"
maturity: IN_PROGRESS
tags: [PIPELINE]
description: Audit ligand-receptor databases against GO and curated modules, and evaluate two-cell signaling modules on spatial omics data.
species: [human]
autolink_gene_symbols: false
index_group: CROSS_CUTTING
---

# Spatial cell-cell communication

**Status: in progress.** The first pass of the resource audit (Track A) is done,
the two lymph-node modules are curated, and GO-CAM coverage has been checked; see
[Results so far](#results-so-far). Track B has not started. The
[design decisions](#decisions-2026-11-23) were taken before work began.

**Bottom line:** cell-cell communication (CCC) tools such as CellPhoneDB, CellChat,
NicheNet and LIANA infer signaling between cell types or spots by asking whether a
ligand is expressed in one place and its receptor in a neighbouring one. Underneath each
tool is a ligand-receptor resource. The repository already holds a curated,
evidence-backed version of part of such a resource: the ligand-first signaling modules
from [LIGANDS_IN_SIGNALING](LIGANDS_IN_SIGNALING.md), plus gene reviews of the ligands
and receptors. It also holds an engine that evaluates a module as a boolean circuit
against expression data, from
[PATHWAY_SATISFIABILITY](PATHWAY_SATISFIABILITY.md). This project joins the two
in two tracks:

- **Track A, resource audit.** Compare the pairs in the CCC resources with GO
  annotations, our gene reviews and our modules. The comparison should surface missing
  GO annotations, and also resource pairs that rest only on binding with no signaling
  evidence.
- **Track B, two-cell satisfiability.** Extend `module_logic.py` so that a signaling
  module is satisfied only when its ligand step holds in a sender location and its
  receptor-side steps hold in an adjacent receiver location. Then evaluate it on a
  public spatial transcriptomics dataset.

A third, smaller deliverable follows from both: export the curated modules in a
format CCC tools can consume, keeping complex subunits and alternative ligands or
receptors intact.

## Results so far

### Track A: CellPhoneDB audit, first pass (2026-11-23)

Script: [scripts/ccc_resource_audit.py](SPATIAL_CELL_COMMUNICATION/scripts/ccc_resource_audit.py);
inputs fetched by [scripts/fetch_data.sh](SPATIAL_CELL_COMMUNICATION/scripts/fetch_data.sh).
Full generated output:
[results/RESULTS.md](SPATIAL_CELL_COMMUNICATION/results/RESULTS.md), with per-pair
tables in `results/`. Inputs: CellPhoneDB data v5.0.0, OmniPath (retrieved
2026-11-23), goa_human.gaf generated 2026-05-21, GO release 2026-07-26, and the
repository's modules, gene reviews and production GO-CAMs.

CellPhoneDB v5.0.0 has 2,911 interactions. The audit covers its 1,475 protein
ligand-receptor interactions. It skips 1,033 non-protein ones, where CellPhoneDB
stands a small molecule in by its biosynthetic enzymes (decision 4).

| Category | Interactions | Meaning |
|---|---:|---|
| concordant | 64 | In a curated module, and GOA has the ligand activity and a shared pathway |
| go_gap | 29 | In a module, but GOA lacks the ligand activity or a shared pathway |
| go_supported | 858 | No module, but GOA supports the pair (module candidates) |
| partial_go | 256 | No module, and GOA supports only one of the two |
| resource_only | 266 | No module and no GOA support |
| review_flag | 2 | The ligand's gene review removes its ligand-activity rows and keeps none |

Findings:

- **The go_gap list reproduces the LIGANDS_IN_SIGNALING gaps from an independent
  source.** KITLG-KIT, NTN1 with DCC and the UNC5 receptors, IL21, IL22, IL34-CSF1R,
  EFNB1, SLIT1-ROBO1, GALP, CRH, UCN, AVP and EDN3 all fall here. Each lacks either
  the ligand-activity MF or a pathway term shared with its receptor in GOA.
- **177 interactions have a ligand with only a receptor-binding MF.** The commonest
  terms are generic *signaling receptor binding* (76 interactions), *ephrin receptor
  binding* (34), *integrin binding* (30) and *neurexin family protein binding* (22).
  This is the binding-term problem of LIGANDS_IN_SIGNALING (its next step 3), now
  with a pair list attached.
- **The two review_flag rows are C5 with C5AR1 and C5AR2.** The C5 review rightly
  removes the TAS row for *chemokine activity*, since C5a is not a chemokine. But it
  keeps C5's core function as *G protein-coupled receptor binding*, not a
  ligand-activity term, so C5a's anaphylatoxin activity is not captured as ligand
  activity. This belongs in the binding-term MODIFY batch, and the pair itself is not
  in doubt.
- **CellPhoneDB lacks some well-established curated pairs.** These ligands are absent
  from CellPhoneDB altogether: MIF and DDT (with the CD74-CD44 receptor complex), the
  collagens with DDR1 and DDR2, NTN3 and SLIT3 (`results/module_only_pairs.tsv`).
  They are candidates to report to CellPhoneDB.
- **OmniPath is broader.** It has 5,072 ligand-receptor protein pairs, of which 1,237
  are also CellPhoneDB pairs (1,484 once complexes are split into subunit pairs). Of
  the 3,835 OmniPath-only pairs, 707 have GOA support for both the ligand activity and
  a shared pathway.

### GO-CAM check

Production GO-CAMs (`gocams/`) were checked for every audited pair. A pair counts as
linked when a model has a direct causal edge from the ligand's activity to the
receptor's. Complex subunits are included, and mouse models are matched through MGI
human-mouse homology.

- **227 of the 1,475 interactions are linked** in at least one model, and 38 more
  co-occur in a model without a direct edge. In 221 of the 227, the ligand's MF on
  the edge is receptor ligand activity or a child, mostly *cytokine activity*,
  *hormone activity*, *growth factor activity* and *chemokine activity*. The
  exceptions are AGRP and ASIP (*receptor antagonist activity*, which GO does not
  place under ligand activity), TF-TFRC, THBS1-CD36 and F2-F2RL2.
- **GO-CAM coverage is uneven by pathway.** Linked interactions per CellPhoneDB
  class: interleukins 21 of 45, BMP 21 of 52, chemokines 14 of 93, ephrins 4 of 55,
  and none for Wnt (355), Notch (26) or FGF (26). The only production Wnt and Notch
  ligand-receptor models are for fly and zebrafish.
- **No production GO-CAM contains CCL19, CCL21, CCR7, CXCL13 or CXCR5.** Both module
  curators queried the GO-CAM index and the cached model files by UniProt and MGI
  ids, symbols and GO term ids. The same queries return CXCL8 and CXCR2, and other
  CC chemokine pairs (CCL2-CCR2, CCL17/CCL22-CCR4, CCL1-CCR8) are modelled, so the
  absence is a GO-CAM curation gap, not a convention. The two new modules record it
  in their notes.
- 704 of the 858 go_supported interactions have no GO-CAM link. Together with the
  module-only pairs, this is a ranked list of candidates for GO-CAM models.

### Lymph-node modules (plan step 4)

Both modules are drafts, and their GO-CAM checks are described above.

- [`modules/ccr7_chemokine_signaling.yaml`](../modules/ccr7_chemokine_signaling.yaml):
  CCL19 or CCL21 (a variant set) acting on CCR7. Ligands carry *chemokine activity*;
  CCR7 carries *C-C chemokine receptor activity*. The pathway is GO:0038118 *C-C
  chemokine receptor CCR7 signaling pathway*, with the ligand-specific children
  GO:0038119 and GO:0038120 on the variants. Scope is Euteleostomi, from the CCR7
  PAINT node PTN002573880.
- [`modules/cxcr5_chemokine_signaling.yaml`](../modules/cxcr5_chemokine_signaling.yaml):
  CXCL13 acting on CXCR5. GO has no CXCL13- or CXCR5-specific pathway term, so the
  module uses *chemokine-mediated signaling pathway* and proposes a new child term,
  "chemokine (C-X-C motif) ligand 13 signaling pathway". The sender (follicular
  dendritic cell) and receiver (B cell) are recorded in `cell_types` (decision 6).
  Scope is Mammalia.
- **Both pairs are now concordant in the audit.** CCL19-CCR7, CCL21-CCR7 and
  CXCL13-CXCR5 moved from go_supported once the modules existed. The pairs with
  the atypical receptors ACKR4 and CCRL2 stay go_supported, because the modules
  include only the signaling receptors.
- **Follow-ups the curators found:**
  - No gene reviews exist yet for CCL19, CCL21, CCR7, CXCL13 or CXCR5.
  - PAINT node PTN001628461 propagates *C-C chemokine receptor activity* and *C-C
    chemokine binding* to the CXC receptor CXCR5 by IBA, which looks like
    over-propagation. It is noted for a future PTHR10489 family review.
  - The PTHR10489 family review has no entry for the receptor-activity terms both
    modules use, so the module validator warns.

## Why this is worth doing

1. **The resources disagree, and their prior knowledge drives the results.** LIANA's
   systematic comparison of 16 CCC resources and 7 methods found "few unique
   interactions, a varying degree of overlap, and an uneven coverage of specific
   pathways and tissue-enriched proteins", and showed that the choice of method and
   resource both "strongly influence the predicted intercellular interactions"
   [PMID:35680885]. A curated, citable reference for a subset of pathways is a way to
   score those resources rather than just compare them with each other.
2. **Subunit and alternative structure matters, and modules already encode it.**
   CellPhoneDB was built to take "into account the subunit architecture of both ligands
   and receptors, representing heteromeric complexes accurately" [PMID:32103204]. Our
   modules represent the same thing more generally: an AND over required parts (the
   MIF module's receptor step is the CD74-CD44 complex, since neither subunit signals
   alone), and an OR over interchangeable variants (MIF or DDT as ligand).
   `module_logic.py` already compiles that structure into a circuit.
3. **The GO side has known holes that a CCC resource could locate.** The ligand gap
   check in LIGANDS_IN_SIGNALING found receptor-initiated pathway terms with no
   annotated ligand in every organism checked (78 of 237 pathway terms in human), and
   820 annotation rows that give a ligand only a receptor-specific binding term rather
   than receptor ligand activity. A CCC resource names candidate ligands for many of
   those pathways. That makes it a source of leads; it is not evidence on its own.
4. **Spatial data is the natural home for the two-cell question.** CellPhoneDB v5 now
   uses "tissue microenvironments derived from spatial transcriptomics technologies" to
   prioritise interactions [PMID:40133495]. The satisfiability engine has already
   resolved a one-cell pathway (gluconeogenesis) per tissue in GTEx and per lobule
   layer in mouse liver zonation data. The two-cell case is the next step.

## What exists to build on

| Asset | Where | Use here |
|---|---|---|
| Ligand-first signaling modules (netrin, Slit-Robo, MIF, IL34, IL21, IL22, chemokine, C5a, TSH, endothelin, galanin, opioid, collagen-DDR, Kit, ephrin, death receptor, bombesin, fly Toll-6/7 neurotrophin) | `modules/` | Curated ligand and receptor steps for Track A, circuits for Track B |
| Other modules with ligand-receptor steps (Notch, Wnt, Hedgehog, IL-1, KNDy, plant CLV-WUS and stomatal lineage) | `modules/` | More circuits; about 49 modules mention a ligand-activity term |
| Ligand and receptor gene reviews (about 30 from LIGANDS_IN_SIGNALING alone) | `genes/` | Reviewed MF/BP status per gene for the audit |
| Ligand gap check, triage, `expected_ligands.yaml` | `projects/LIGANDS_IN_SIGNALING/` | GO-only baseline; candidate ligands per pathway term |
| Module circuit compiler, route enumeration, gap report | `src/ai_gene_review/module_logic.py` | Engine for Track B |
| Context oracles (GTEx, mouse zonation) and lobule figures | `modules/experimental/gluconeogenesis-context/` | Pattern for a spatial oracle |
| GO-CAM activity index | `gocams/index.tsv` | Whether a curated model links a ligand to its receptor |
| `ModuleContext.cell_types` / `anatomical_locations` | `src/ai_gene_review/schema/gene_review.yaml` | Where sender and receiver cell types can be recorded on a module node or annoton |

## Track A: resource audit

**Inputs.** CellPhoneDB v5 [PMID:40133495] (curated repository, with heteromeric
complexes) and the OmniPath intercellular collection [PMID:41251164], which LIANA
uses for its consensus resource [PMID:35680885]. CellChatDB [PMID:33597522] is a
candidate third input. Fetch each from its released files, pin the version, and keep
only a derived pair table in the repository; the raw downloads are re-fetched on
demand, as for the zonation oracle.

**Mapping.** Resolve every ligand, receptor and complex subunit to a UniProtKB
accession. Use each resource's own complex definitions rather than splitting
complexes into pairwise edges.

**Questions asked of each pair:**

1. Does the ligand carry `GO:0048018` receptor ligand activity or a descendant
   (directly, or as a module core function)? If it carries only a receptor-specific
   binding term, flag it for the binding-term MODIFY batch in LIGANDS_IN_SIGNALING.
2. Are ligand and receptor annotated `involved_in` the same signaling pathway term, or
   one is an ancestor of the other's?
3. Does a GO-CAM model in `gocams/index.tsv` contain both genes? Does a curated module
   contain both, in the ligand and receptor roles?
4. Has the ligand or receptor been reviewed here, and what did the review conclude
   about the relevant rows?

**Output categories** (a sketch, to settle on the first run):

- *Concordant:* the pair is in a module, and GO has both genes on the pathway with the
  right MFs.
- *GO gap:* the resource and a module agree, but GOA lacks the ligand-activity MF or
  the pathway BP. These feed the gene-review queue, and each needs its own literature
  evidence before any `NEW` row.
- *Resource-only:* no module, no GO pathway link. These are candidates for new modules,
  or binding-only pairs that the resource should label as such.
- *Module-only:* a curated ligand-receptor step that the resource lacks, reported back
  to the resource.
- *Contradicted:* the resource lists a pair our reviews argue against, for example a
  receptor-side protein or a non-ligand binder in the ligand slot.

**Guardrail.** A pair in a CCC resource is never on its own the basis for a GO
annotation. It is a lead to check against the literature it cites, under the
participation and comparator rules in `CLAUDE.md`.

## Track B: two-cell satisfiability on spatial data

**Engine change.** A signaling module splits into a sender side and a receiver side.
The first version infers the split from the circuit: atoms whose molecular function is
`GO:0048018` or a descendant form the sender side, and everything else forms the
receiver side. Where a module already records `cell_types` on a node, that wins. The
module is satisfied for an ordered pair of locations (s, r) when the sender
sub-circuit holds at s, the receiver sub-circuit holds at r, and s and r are adjacent
under a stated neighbourhood (same spot, or within k spots). The existing gap report
then says which step fails, on which side.

**Oracle.** Per-spot (or per-cell-type, after deconvolution) expression with an
explicit threshold, built from a public dataset with a documented download. Following
the satisfiability project, report results across a threshold sweep rather than at
one cut-off.

**Validation.** Use modules whose spatial pattern is known independently of their
own genes' expression, so that the result is a derivation rather than a
restatement. The first run uses lymph node (decision 1): the CCR7 module should be
satisfied in the T-cell zone, the CXCR5 module in the follicles, and modules for
signals the tissue does not use should fail. The liver lobule is second. Notch
signaling between neighbouring cells is a later case, since sender and receiver are
adjacent by definition.

**Comparison.** Run LIANA or CellPhoneDB on the same data, restricted to the pairs
the modules cover, and compare the calls. Expect differences where a module requires a
co-receptor or a full receptor complex that a pairwise resource does not, and where a
widely expressed paralog satisfies a naive pair but not the curated step (the G6PC3
trap in the gluconeogenesis results is the one-cell version).

## Module export

Write the ligand and receptor steps of each signaling module as a CellPhoneDB-style
interaction table plus complex table, or the OmniPath/LIANA equivalent. Carry the
module id, PANTHER family or PTN, and evidence references in extra columns, so that a
CCC result can be traced back to the curation. This is a derived product: generate it
from the module YAML, do not commit hand-edited tables.

## Plan

1. ~~Decide the open questions.~~ Done; see [Decisions](#decisions-2026-11-23).
2. ~~Track A, first pass.~~ Done 2026-11-23; see
   [Results so far](#results-so-far).
3. Triage the go_gap and review_flag categories for the pathways that already have
   modules, and the binding-only ligands with LIGANDS_IN_SIGNALING step 3. Route
   gene-level fixes to gene-review PRs. Also review CCL19, CCL21, CCR7, CXCL13 and
   CXCR5.
4. ~~Curate the CCL19/CCL21-CCR7 and CXCL13-CXCR5 modules.~~ Done 2026-11-23 (drafts).
5. Track B: add the sender/receiver split and spot adjacency to `module_logic.py`,
   with doctests on a two-step module (MIF), before touching real data.
6. Build the Visium lymph node oracle. Outline the T-cell zone and the follicles
   from marker genes that are not module members. Run the two homing modules, the
   other ligand modules, and modules not expected in lymph node as negative
   controls (for example TSH and galanin), with a threshold sweep and the
   CellPhoneDB comparison on the same pairs.
7. Module export, once the module set used in steps 3 to 6 is stable.

## Decisions (2026-11-23)

Taken by the agent at C. Mungall's request ("you decide"). Each can be reopened, and
the reason is given so that it is clear what would change it.

1. **First spatial dataset: the 10x Genomics Visium human lymph node sample
   (`V1_Human_Lymph_Node`, Space Ranger 1.1.0 public dataset).** Reasons:
   - It is public, human, and downloads directly from the 10x CDN. The download
     was checked from this environment on 2026-11-23.
   - It is a whole-transcriptome assay, so no module member is missing from a
     gene panel, as it could be on Xenium, MERFISH or CosMx.
   - Lymph node has two well-known compartments, each organised by one
     chemokine-receptor pair: the T-cell zone (CCL19 and CCL21 from stromal
     reticular cells, CCR7 on T cells and dendritic cells) and the B-cell follicles
     (CXCL13 from follicular dendritic cells, CXCR5 on B cells). The zones can be
     outlined from cell-type marker genes that are not module members, so a
     module result can be checked against them without circularity. This is the
     same safeguard as orienting the liver lobule with landmark genes in the
     gluconeogenesis work.
   - It is widely used as a benchmark for spot deconvolution, so other methods'
     results on it can be compared.

   The cost is that the repository's chemokine module covers CXCL8 with
   CXCR1/CXCR2 and CCR5, not the homing chemokines. So Track B needs two new
   ligand-first modules, CCL19/CCL21-CCR7 and CXCL13-CXCR5. CCL19 signaling
   is already in the LIGANDS_IN_SIGNALING queue, so that curation is useful on
   its own. The human liver atlas (GSE239480) remains the second dataset, once
   a zonation pipeline exists for it.
2. **Spots, not deconvolved cell types, for version 1.** The engine evaluates
   modules on normalised per-spot expression, with a threshold sweep. Neighbours
   are the spot itself plus its first ring of adjacent spots on the hexagonal grid.
   Visium spots are 55 µm across, so one spot already mixes several cells, and the
   same-spot case cannot tell autocrine signaling from neighbour signaling. The
   page will state that limit and not claim cell-level resolution. Deconvolution
   is a later refinement, added only if spot-level results are too noisy to read.
3. **Primary comparator: CellPhoneDB v5.** It is curated and complex-aware, and it
   matches the module model best (heteromeric receptors as AND, alternative
   ligands as separate interactions). The OmniPath intercellular collection is
   used in Track A only, as a breadth check: pairs it has and CellPhoneDB lacks
   are reported as a separate group. Both sources were reachable from this
   environment on 2026-11-23: CellPhoneDB data via `raw.githubusercontent.com`
   (the GitHub API for that repository is not enabled here) and OmniPath via its
   web service.
4. **Small-molecule ligands are out of scope for version 1.** Track A counts
   CellPhoneDB's nonpeptidic interactions [PMID:40133495] but does not audit them,
   and Track B does not model them. Treating a biosynthetic enzyme as the sender
   would put a metabolic route inside the sender side. That is a separate
   design, and it overlaps the X category of the ligand gap check, which deals
   with pathways that have no protein ligand.
5. **Human only.** The resources are human-first and the dataset is human. The
   modules stay pan-species. A mouse run would map the human modules to mouse
   orthologs and state that it does so, as the zonation run did.
6. **Ligand and receptor sides are inferred, with no schema change.** The sender
   side is the annotons whose molecular function is `GO:0048018` or a descendant;
   everything else is the receiver side. A module can override this with the
   existing `ModuleContext.cell_types` slot. The run reports every module where
   inference gives an empty side, or puts the same annoton on both sides.
   Bidirectional ephrin signaling and membrane-bound Notch ligands are the
   expected cases. If more than a handful of modules need overrides, an explicit
   side field becomes a schema proposal in a separate PR.

## References

- [PMID:32103204] Efremova et al. 2020, CellPhoneDB: inferring cell-cell communication
  from combined expression of multi-subunit ligand-receptor complexes. *Nat Protoc*.
- [PMID:40133495] Troulé et al. 2025, CellPhoneDB v5: inferring cell-cell
  communication from single-cell multiomics data. *Nat Protoc*.
- [PMID:35680885] Dimitrov et al. 2022, Comparison of methods and resources for
  cell-cell communication inference from single-cell RNA-Seq data. *Nat Commun*
  (LIANA).
- [PMID:41251164] Türei et al. 2026, OmniPath: integrated knowledgebase for multi-omics
  analysis. *Nucleic Acids Res*.
- [PMID:33597522] Jin et al. 2021, Inference and analysis of cell-cell communication
  using CellChat. *Nat Commun*.
- [PMID:31819264] Browaeys et al. 2020, NicheNet: modeling intercellular communication
  by linking ligands to target genes. *Nat Methods*.
- [PMID:28166538] Halpern et al. 2017, the liver zonation atlas used as the spatial
  oracle in PATHWAY_SATISFIABILITY.

## Related projects

- [LIGANDS_IN_SIGNALING](LIGANDS_IN_SIGNALING.md): ligand gap check and ligand-first
  modules. Track A extends its gap check to external resources.
- [PATHWAY_SATISFIABILITY](PATHWAY_SATISFIABILITY.md): the module-logic engine and
  context oracles. Track B extends it to two cells.
- [IEP](IEP.md) and [OMICS_EVIDENCE](OMICS_EVIDENCE.md): limits on what expression
  evidence can support in GO annotation.
- [ARATH_SINGLE_CELL_FUNGAL](ARATH_SINGLE_CELL_FUNGAL.md): a single-cell atlas used as a
  source of review targets, with the same caution about expression evidence.
