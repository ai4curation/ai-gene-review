# LNX1 review notes

## Setup and source provenance

- Current human identity: HGNC **LNX1**, reviewed UniProt **Q8TBB1**.
- Falcon deep research failed with HTTP 402; the required Perplexity-lite fallback
  failed with HTTP 401/quota. No provider-named deep-research file was fabricated.
  This review instead uses cached primary literature, UniProt, QuickGO, and the
  independently reconstructed source provenance.
- Live QuickGO contains 922 raw annotations. They normalize to 33 review objects.
  All 922 rows target canonical Q8TBB1, with no NOT annotations or extensions.
  Ordered tuples and all ordered WITH/FROM unions were independently compared:
  31 normalized objects carry 934 supporting-entity identifiers, with zero mismatch.
- The large count is driven by interaction maps: the 15 generic protein-binding
  objects contain hundreds of partners from Y2H, fragment, and perturbation screens.
  These are real source observations but should not define LNX1 function.

## Product architecture and isoform boundary

Canonical Q8TBB1-1/LNX1p80 is a soluble modular E3 ligase. It contains an
N-terminal RING-type zinc-finger region (UniProt 41–79), a NUMB-binding NPXY motif
(181–184), a MAGEB18-interaction region (186–244), and four C-terminal PDZ domains
(274–359, 381–464, 507–593, and 638–724). Structural work identifies a wider
Zn–RING–Zn catalytic module and a dimeric Ubc13/UBE2V2-bound mechanism
[PMID:29496391, "The RING domain of LNX1 is embedded between two zinc-finger
motifs (Zn-RING-Zn), both of which are crucial for its ubiquitination activity."].

Q8TBB1-2/LNX1p70 replaces residues 1–127 and therefore lacks the entire RING and
flanking catalytic zinc module. Intrinsic GO:0061630 ubiquitin protein ligase
activity must not be transferred to p70. The shorter product retains the NPXY
motif and four PDZ domains and can act as a multivalent scaffold. Human HEK293T
experiments show that p70 can still promote lower-level ubiquitination of selected
ligands, plausibly by recruiting other E3s [PMID:29121065, "On this basis we
propose a model whereby LNX1p70, despite lacking a catalytic RING domain, may
function as a scaffold to promote ubiquitination of its ligands through recruitment
of other E3-ligases."].

## Direct functional evidence

### Canonical E3 ligase

The strongest molecular-function model is isoform-1-specific, PDZ-directed
ubiquitination. The founding study used mouse Lnx constructs and demonstrates
RING-dependent NUMB ubiquitination and proteasomal degradation, so it is strong
orthology evidence rather than direct human-product evidence [PMID:11782429,
"The isolated RING finger domain was able to function as an E2-dependent, E3
ubiquitin ligase in vitro and mutation of a conserved cysteine residue within the
RING domain abolished its activity"]. Direct human structural biochemistry defines
the catalytic Zn–RING–Zn/Ubc13–UBE2V2 module and dimeric transfer mechanism
[PMID:29496391].

Human SRC is a directly demonstrated PDZ-recruited substrate: its C-terminal ligand
binds an LNX1 PDZ domain, SRC phosphorylates LNX1, and LNX1 ubiquitinates SRC
[PMID:17936276, "Moreover, c-Src itself is ubiquitinated by LNX1, suggesting an
interdependent regulation of c-Src and LNX1."]. Human-cell proteomics further
identifies PPFIA1, KLHL11, KIF7, and ERC2 as LNX1 ubiquitination substrates
[PMID:29121065, "We show that PPFIA1 (liprin-α1), KLHL11, KIF7 and ERC2 are
substrates for ubiquitination by LNX1."]. Substrate outcomes are not uniformly
degradative: SRC, NUMB, PBK, and SUFU studies support degradation in particular
contexts, whereas RHOC monoubiquitination is regulatory and activating. Therefore
the core process is protein ubiquitination, with ubiquitin-dependent proteolysis as
an important but substrate-specific branch.

### PDZ-dependent scaffolding

PMID:16002321 reports that human LNX binds Ski-interacting protein/SNW1 through
PDZ domains and co-immunoprecipitates with "SKIP" in HEK293 cells [PMID:16002321,
"The co-immunoprecipitation results suggested that LNX interacted with SKIP in
HEK293 cells."]. GOA/IntAct instead maps that row to Q9BT40/INPP5K, a different
protein also aliased SKIP; the homonym discrepancy remains unresolved. The paper's
`cytoplasm` wording comes
from in-situ hybridization and describes transcript signal, not protein localization.
Mouse-derived UniProt evidence assigns p70 an endocytic JAM4 scaffold role. This
supports a bounded p70 scaffold function, but not intrinsic E3 activity or a stable
named complex.

### Interaction screens

The proteome-scale Y2H, HuRI, edgotyping, fragmentomics, and disease-network papers
provide valid pair-level provenance but little physiological context. Generic
GO:0005515 `protein binding` is marked over-annotated throughout. One direct exception
is PMID:17936276: the source row is refined to GO:1990782 protein tyrosine kinase
binding because SRC is the explicitly validated partner class. MAGEB18 binding is
directly mapped to LNX1 residues 186–244 [PMID:20864041], but no stable physiological
MAGE–LNX1 complex or MAGE-dependent substrate is established.

## Localization and organism boundaries

Human protein localization evidence is limited. HPA supplies direct cytosol and
cell-junction observations, while UniProt cytoplasmic and synaptic statements are
largely mouse-orthology transfers. The hippocampal mossy-fiber/CA3, postsynaptic,
and synapse-maturation rows are retained as non-core inferred biology and must not
be presented as direct human neuronal function. LNX1 has no transmembrane segment or
signal peptide and is not assigned to a stable complex.

## Existing-annotation synthesis

- Refine broad GO:0004842 transferase rows to GO:0061630 ubiquitin protein ligase
  activity, explicitly restricted to the RING-containing product in synthesis.
- Retain GO:0016567 protein ubiquitination as the central process. Keep broad
  ubiquitin-dependent catabolism, but do not imply every substrate is degraded.
- Refine metal-ion binding to GO:0008270 zinc ion binding based on the structurally
  defined Zn–RING–Zn module.
- Refine direct SRC generic binding to GO:1990782.
- Reframe mouse-transferred GO:0030165 PDZ domain binding as GO:0140378 protein
  complex scaffold activity: LNX1 supplies PDZ domains and binds ligands, rather
  than merely binding somebody else's PDZ domain.
- Treat hundreds of generic binding rows as over-annotated and self-association as
  a mechanistic non-core property.

## Core model and gaps

1. **LNX1p80:** dimeric Zn–RING–Zn ubiquitin protein ligase whose PDZ domains recruit
   selected substrates for degradative or regulatory ubiquitination.
2. **LNX1p70:** RING-less PDZ scaffold that organizes endocytic/signalling partners
   and can recruit other E3 ligases; evidence is narrower and partly orthology-based.

Open questions include the endogenous human substrate hierarchy, tissue-specific
expression of p80 versus p70, whether p70's recruited E3s are necessary in vivo,
and which of the many screen partners survive endogenous topology- and abundance-aware
validation.

## Suggested experiments

1. Use isoform-specific endogenous tags and quantitative proteomics to map p80 and p70
   expression, localization, and partner occupancy across epithelial and neuronal cells.
2. Compare isogenic p80-only, p70-only, RING-mutant, PDZ-mutant, and dimer-interface
   mutants using ubiquitin-remnant proteomics and protein-stability measurements.
3. Reconstitute human Zn–RING–Zn LNX1 with alternative E2s and defined PDZ-recruited
   substrates to resolve linkage type, mono/polyubiquitination, and degradation coupling.
4. Validate prioritized screen partners at endogenous abundance with reciprocal
   co-immunoprecipitation, proximity labeling, compartment controls, and functional rescue.
