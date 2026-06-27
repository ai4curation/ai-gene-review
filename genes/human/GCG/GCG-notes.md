# GCG (Proglucagon) — review notes

UniProt: P01275 (GLUC_HUMAN), 180 aa precursor. HGNC:4191. Taxon 9606.

## Core framing: one gene, many chains

GCG is the textbook example (alongside POMC) of a **polyprotein precursor** whose
biology lives in its **cleavage products**, not the precursor. Proglucagon is
processed **tissue-specifically** by prohormone convertases:

- **Pancreatic α-cells (islets of Langerhans):** PCSK2/PC2 liberates **glucagon**
  as the major bioactive hormone.
- **Intestinal L-cells and selected brain neurons:** PCSK1/PC1 liberates
  **GLP-1, GLP-2, glicentin and oxyntomodulin**.

[UniProt:P01275 PTM, "Proglucagon is post-translationally processed in a tissue-specific manner in pancreatic A cells and intestinal L cells. In pancreatic A cells, the major bioactive hormone is glucagon cleaved by PCSK2/PC2. In the intestinal L cells PCSK1/PC1 liberates GLP-1, GLP-2, glicentin and oxyntomodulin."]

### The chains (UniProt feature table, PRO IDs)

| Chain | Residues | PRO id | Receptor | Core role |
|-------|----------|--------|----------|-----------|
| Glicentin | 21-89 | PRO_0000011253 | (unclear) | gastric acid / mucosal growth (weak) |
| GRPP (glicentin-related polypeptide) | 21-50 | PRO_0000011254 | — | unknown |
| Oxyntomodulin | 53-89 | PRO_0000011255 | GCGR/GLP1R (dual, weak) | reduces food intake, inhibits gastric emptying |
| **Glucagon** | 53-81 | PRO_0000011256 | **GCGR** | raises blood glucose (gluconeogenesis↑, glycolysis↓); counter-regulatory to insulin |
| **GLP-1** (and 7-37 / 7-36) | 92-128 / 98-128 / 98-127 | PRO_0000011258/9/60 | **GLP1R** | incretin: glucose-dependent insulin secretion; satiety; β-cell survival |
| **GLP-2** | 146-178 | PRO_0000011262 | **GLP2R** | intestinotrophic: villus growth, crypt proliferation, ↓enterocyte apoptosis |

Critical consequence for GO curation: GO annotations are attached to the **precursor
P01275** with **no chain/PRO qualifier**, so functions belonging to *different
peptides with different receptors* are conflated at the gene level. Ideally each
function would carry the PRO id of the responsible peptide. I capture this with the
`functional_isoforms` block (CLEAVAGE_PRODUCT, mapped to PRO ids) and attribute each
function in `core_functions`.

## Per-chain function evidence (from UniProt FUNCTION blocks + literature)

### Glucagon
- "Plays a key role in glucose metabolism and homeostasis. Regulates blood glucose
  by increasing gluconeogenesis and decreasing glycolysis. A counterregulatory hormone
  of insulin... Binds to and activates the glucagon receptor GCGR, which couples to
  the G(s) G protein and elevates intracellular cAMP" [UniProt:P01275 FUNCTION Glucagon; ECO:0000269|PubMed:32193322].
- Receptor binding: GO:0031769 glucagon receptor binding (IBA) is the specific MF.
- Glucagon is an **IDE substrate** [PMID:17051221, structure of IDE with glucagon as one of four substrates: "structures of human IDE in complex with four substrates (insulin B chain, amyloid-beta peptide (1-40), amylin and glucagon)"] — clearance, not a core function.
- Glucagon **self-assembles into amyloid fibrils** in vitro [PMID:22212535 "The 29-residue peptide hormone glucagon forms many different morphological types of amyloid-like fibrils"] — basis of GO:0042802 identical protein binding (IPI). In vitro / pharmaceutical-formulation behavior, not a physiological function.

### GLP-1 (incretin)
- "Potent stimulator of glucose-dependent insulin release" [UniProt:P01275 FUNCTION GLP-1; ECO:0000269|PubMed:22037645, PubMed:40446798]. Also gastric motility, suppression of glucagon, satiety, islet mass / β-cell proliferation, **inhibits beta cell apoptosis**.
- IL-6 increases GLP-1 production from α-cells via ↑proglucagon + PC1/3 [PMID:22037645 "IL-6 increased GLP-1 production from alpha cells through increased proglucagon (which is encoded by GCG) and prohormone convertase 1/3 expression"].
- Central satiety: ICV GLP-1 inhibits feeding; "central GLP-1 is a new physiological mediator of satiety" [PMID:8538742]. Basis of GO:0007631 feeding behavior (TAS).
- GLP-1 is a **DPP4** substrate (Reactome R-HSA-9023632/3) and a slow **FAP** substrate [PMID:21314817 "FAP slowly hydrolysed other hormone peptides, such as the incretins glucagon-like peptide-1 and glucose-dependent insulinotropic peptide"] — degradation/clearance, not core.

### GLP-2 (intestinotrophic)
- "GLP-2 stimulates intestinal growth and up-regulates villus height in the small
  intestine, concomitant with increased crypt cell proliferation and decreased
  enterocyte apoptosis" [PMID:9990065]. Acts through its own receptor GLP-2R:
  "GLP-2, like glucagon and GLP-1, exerts its actions through a distinct and specific
  novel receptor" [PMID:9990065]. Basis of GO:0005102 signaling receptor binding (TAS) and GO:0007186 GPCR signaling (TAS) from this paper.

### Oxyntomodulin / Glicentin
- Oxyntomodulin: "Significantly reduces food intake. Inhibits gastric emptying"
  [UniProt:P01275 FUNCTION Oxyntomodulin]. Glicentin: gastric acid / mucosal growth (weak, ECO:0000303).

## Annotation-by-annotation reasoning highlights

- **Hormone activity GO:0005179 (IBA/IEA), receptor ligand activity GO:0048018, glucagon
  receptor binding GO:0031769, signaling receptor binding GO:0005102**: all correct, core
  MF. These are the right way to describe the peptides' molecular function (agonist/ligand).
- **GPCR / adenylate cyclase-activating signaling (GO:0007188, GO:0007189, GO:0007186)**:
  all chains act through class B GPCRs (GCGR, GLP1R, GLP2R) → Gs → adenylyl cyclase → cAMP.
  Correct.
- **Insulin secretion terms (GO:0035774, GO:0032024, GO:0050796)**: GLP-1 incretin effect.
  Correct, specific GO:0035774 (positive regulation of insulin secretion involved in
  cellular response to glucose stimulus) is the best term and captures glucose-dependence.
- **Gluconeogenesis GO:0045722, glucose homeostasis GO:0042593**: glucagon. Correct, core.
- **GO:0001678 intracellular glucose homeostasis (IBA)**: questionable term choice —
  glucagon regulates *systemic/blood* glucose, not intracellular glucose homeostasis
  (cell-autonomous). The PANTHER family IBA propagated a sibling term; GO:0042593
  glucose homeostasis is the better fit. MODIFY.
- **GO:0005737 cytoplasm located_in (IEA, Ensembl)**: wrong for a secreted peptide hormone;
  proglucagon only transits cytoplasm-bounded compartments (ER → granule). Misleading.
  REMOVE.
- **GO:0005886 plasma membrane is_active_in (IEA, Ensembl)**: the secreted ligand engages a
  PM receptor from the extracellular side; the peptide is not *active in* the PM. Over-annotation.
- **GO:0071377 cellular response to glucagon stimulus involved_in (IEA)**: semantically
  backwards — GCG is the *source* of the glucagon stimulus, not a cell *responding to* it.
  This is the response program of glucagon TARGET cells. Over-propagated IEA. MARK_AS_OVER_ANNOTATED.
- **GO:0070374 positive regulation of ERK1/2 cascade, GO:0090280 positive regulation of
  calcium ion import, GO:0043066 negative regulation of apoptotic process (all IEA Ensembl)**:
  real downstream effects of GLP-1/glucagon signaling in target cells but indirect, several
  steps removed from the hormone's molecular function; keep as non-core at most.
- **GO:0014823 response to activity (IEA/ISS)**: ortholog-transferred, weak/contextual; keep non-core.
- **GO:0005515 protein binding (IPI ×3) + GO:0042802 identical protein binding (IPI)**:
  real binary interactions (IDE substrate, FAP substrate, GIPR co-structure, self-fibrillation)
  but uninformative / non-physiological; KEEP_AS_NON_CORE (per guidance avoid "protein binding"
  as a core MF).
- **Locations**: extracellular region GO:0005576 (secreted) = core; ER lumen GO:0005788 and
  secretory granule lumen GO:0034774 = correct biosynthetic/storage transit locations (ACCEPT).

## References checked
All 9 PMIDs read at abstract level (only PMID:22037645 has full text in cache). Reference
correctness judgments recorded in `reference_review`. PMID:7929237 (type I adenylyl cyclase)
and PMID:17715056 (GIP receptor ECD) are tool/structure papers that use a GCG product or a
paralogous incretin peripherally — flagged LOW relevance.
