---
title: "Spatial cell-cell communication: curated ligand modules meet spatial omics"
maturity: SCOPING
tags: [PIPELINE]
description: Audit ligand-receptor databases against GO and curated modules, and evaluate two-cell signaling modules on spatial omics data.
species: [human]
autolink_gene_symbols: false
index_group: CROSS_CUTTING
---

# Spatial cell-cell communication

**Status: scoping.** Nothing has been run yet. This page sets out the plan, what
already exists in the repository to build on, and the open decisions.

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

**Validation.** Pick modules whose spatial pattern is known independently of
expression, so that the result is a derivation rather than a restatement. Candidates
to choose from in the first run:

- Chemokine gradients and their receptor-bearing immune cells in lymph node or tonsil
  (the chemokine module).
- The liver lobule, which the gluconeogenesis work already oriented. A human liver
  spatial atlas (GEO GSE239480) is noted there as the open validation target.
- Notch lateral signaling, where sender and receiver are adjacent by definition.

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

1. Decide the open questions below.
2. Track A, first pass: fetch CellPhoneDB v5 and the OmniPath intercellular
   collection, map to UniProt, and run the four questions over the human pairs. Write
   the result to `projects/SPATIAL_CELL_COMMUNICATION/results/` with a generated
   `RESULTS.md`.
3. Triage the *GO gap* and *Contradicted* categories for the pathways that already
   have modules. Route gene-level fixes to gene-review PRs.
4. Track B: add the sender/receiver split and adjacency to `module_logic.py`, with
   doctests on a two-step module (MIF), before touching real data.
5. Build one spatial oracle on the chosen dataset and run the ligand modules over it,
   with a threshold sweep and the LIANA or CellPhoneDB comparison.
6. Module export, once the module set used in steps 3 to 5 is stable.

## Open questions

- **Which spatial dataset first?** It needs to be public, human, with a stable
  download and a known spatial pattern for at least two of our modules. Spot-based
  (Visium) data needs deconvolution, while imaging-based single-cell data (Xenium,
  MERFISH, CosMx) has small gene panels that may miss module members.
- **Which resource is the primary comparator?** CellPhoneDB is complex-aware and
  curated. The OmniPath intercellular collection is broader and already aggregates
  several resources, including CellPhoneDB.
- **Small-molecule ligands.** CellPhoneDB v5 added about 1,000 interactions mediated
  by nonpeptidic ligands [PMID:40133495]. Our modules represent a small-molecule
  ligand by its biosynthetic enzymes, if at all. Should Track B treat the synthesising
  enzyme as the sender atom? This overlaps with the X category of the ligand gap check.
- **Species scope.** The modules are pan-species and the resources are mainly human
  and mouse. Start with human only.
- **Where does sender/receiver assignment live?** An inferred split from the ligand MF
  may be enough. Otherwise each signaling module would need an explicit side on each
  part, which is a schema question.

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
