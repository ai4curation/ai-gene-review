# AKTIP focused report incorporation, 2026-09-21

The ready OpenScientist report `noncatalytic-k63-ubiquitination-and-lesion-bypass`
was read in full, including its evidence matrix, limitations and citation index.
Both supplied artifacts (`final_report.html`, `final_report.pdf`, 14 pages) were
text-extracted and checked as renderings of the same report. They contain no
executed alignment code, saved alignment or raw IntAct results with which to
reproduce the report's approximate identity and interaction-count claims.

## Actual ancestral placement

The live PANTHER v19 `geneinfo` service maps Q9H8T0 to **PTHR24068**, whereas the
newer local UniProt record and PAINT slice use **PTHR24067**. An initial v19
PTHR24067 tree lookup could therefore not locate the target. This version
difference was resolved through the accession query, not interpreted as loss.

The v19 PTHR24068 tree gives the following ordered key nodes:

`PTN002514495` (root, catalytic IBD) → `PTN000630262` (both process IBDs) →
`PTN000630263` → `PTN000630283` → `PTN001529378` → `PTN001176003` →
`PTN000630284` → `PTN000630285` → `PTN001529379` → `PTN008392917` →
`PTN009079467` → `PTN004661315` (AKTIP subfamily) → `PTN004661317` →
`PTN004661318` → `PTN004661320` → `PTN004661321` → `PTN004661322` →
`PTN004661323` → `PTN004661324` → `PTN002545715` (human Q9H8T0).

The corresponding local PAINT rows place GO:0070534 and GO:0006301 at
PTN000630262. Their experimentally annotated descendants include UBE2N/P61088;
these are not assertions shown to originate in an exclusively UBE2V1/UBE2V2
clade, as the report implies. The process-specific NOT/IKR rows on PTN000630296
and transferase NOT/IRD on PTN000630367 are **not on the AKTIP target path**.
The compact response provenance and complete target path are saved in
`AKTIP-paint-lineage.json`. A dedicated AKTIP subfamily does not erase descent
from the deeper IBD. Pairwise sequence identity is not a test of that descent.

## Primary experiments and their limits

- **PMID:26110528**, full text checked, Figures 5–7 and Methods. Purified-protein
  experiments support TRF interactions. Figure 6F instead uses a GST pull-down
  from 293T extracts: “AKTIP precipitates both PCNA and RPA70”. This is physical
  association, not proof that each contact is a purified binary interaction.
  PCNA recruitment and S-phase/BrdU experiments establish replication-associated
  function. Figure 7 tests TRF1 ChIP and BrdU incorporation in synchronized HeLa
  cells; the authors caution that the result is not complete failure of telomere
  replication and suggest impaired TRF1 association during replication. These
  readouts do not measure bypass of a defined DNA lesion or K63-linked PCNA
  modification. Conversely, they do not show that such additional capacity is
  absent. The source explicitly identifies a UBC domain “lacking the catalytic cysteine
  that mediates ubiquitin transfer.” This catalytic-apparatus distinction
  challenges intrinsic E2 transfer chemistry. Its separate Asp106 numbering
  statement is not adopted: the cached canonical 292-aa UniProt sequence has
  W106, also consistent with the W106/F107 Hook-binding mutant in PMID:18799622.
  Exact residue numbering needs isoform/alignment reconciliation; the primary
  studies agree on the absence of the catalytic cysteine.
- **PMID:18799622**, newly fetched full text checked. Figure 1/2 interaction and
  mutational studies establish FTS–Hook binding and endogenous FHF assembly;
  endosomal EGF transit assays include an RNAi-resistant rescue and a
  Hook-binding-defective FTS mutant. The introduction explicitly distinguishes
  catalytically inactive UEVs from their noncatalytic roles, including the
  characterized MMS2–UBC13 complex. The observed FHF function does not constitute
  a negative assay of all other complexes. The paper's missing endogenous AKT
  interaction under its conditions is likewise not a universal exclusion.
- **PMID:36516775**, full Figure 3/S5 results, perturbations and limitations
  checked. In MCF7 and MDA-MB-361 cells AKTIP depletion reduces ERα
  polyubiquitination and increases stability. CAND1 depletion reverses the
  ubiquitination/stability effect. AKTIP–CAND1 binding, increased CAND1–CUL2
  association and reduced CUL2–ERα association provide a noncatalytic context;
  Hook depletion does not reproduce the proposed mechanism. The study does not
  establish **K63 linkage**, and no particular other linkage is inferred here
  merely from proteasomal turnover. The authors explicitly state: “The mechanism
  underpinning these altered protein interactions remains to be elucidated.”
  Their proposed reduced CUL2 ligase activity requires validation. Thus this
  source supports a ubiquitination-related role without proving the disputed
  exact process, direct catalytic activity, or a fully resolved ternary scaffold.
- **PMID:18284681**, newly fetched full text checked, human HeLa/293T and mouse
  embryonic-stem-cell experiments. PCNA ubiquitin laddering persists after
  MMS2 loss or combined MMS2/UEV1A depletion, whereas UBC13/RAD18 depletion
  reduces it. The authors identify redundancy without identifying the
  compensating protein. This is not an AKTIP assay. The report's use of this
  paper to define an exclusive UBE2V1/2 mechanism overlooks the main result.
  **PMID:24674630** and **PMID:18757916** remain abstract-only after official
  fetch; their yeast Rad5 mechanisms are background and are not used as
  evidence that human AKTIP lacks either process.

## Decision and remaining question

The live QuickGO definition of GO:0061631 requires thioester-linked ubiquitin
transfer through cysteine sulfhydryls. Retain **REMOVE** for that intrinsic E2
activity and retain the existing NOT transferase assertion. The two process
definitions do not require that every participating subunit itself catalyze
the transfer.

Restore **KEEP_AS_NON_CORE** for GO:0070534 and GO:0006301 on the verified
positive ancestral descent, with no target-specific process-loss evidence.
These remain phylogenetic assertions, not newly demonstrated human mechanisms.
The report itself concedes: “Absence of interactome coverage cannot fully exclude
a transient/condition-specific scaffold role.” Its refutation is therefore not
adopted. Human K63-complex contribution and lesion-bypass participation remain
specific experimental follow-up questions: linkage-resolved chain assembly,
PCNA modification after defined damage, and lesion-bypass assays with suitable
separation-of-function rescue. No new annotation or duplicate report is added.

Sources: [PAINT local slice](../../../interpro/panther/PTHR24067/PTHR24067-paint.tsv),
[live gene mapping](https://www.pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList=Q9H8T0&organism=9606),
[live v19 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR24068),
[DNA damage tolerance definition](https://www.ebi.ac.uk/QuickGO/term/GO:0006301),
[K63 process definition](https://www.ebi.ac.uk/QuickGO/term/GO:0070534),
[E2 activity definition](https://www.ebi.ac.uk/QuickGO/term/GO:0061631).
