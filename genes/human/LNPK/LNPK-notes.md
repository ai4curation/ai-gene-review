# LNPK review notes

## Setup and provenance

- Current human identity: HGNC symbol **LNPK**, reviewed UniProt **Q9C0E8**.
- Deep-research provider attempts failed: Falcon returned HTTP 402 and Perplexity-lite
  returned HTTP 401/quota. Literature was therefore reviewed from the repository's
  cached PubMed records, UniProt, QuickGO, and primary full text where cached.
- Live QuickGO returned 32 raw rows. These normalize to 24 review objects: eight HuRI
  rows collapse to one isoform-2 IPI object and two identical PMID:24223779 ER-membrane
  rows collapse to one. Ordered tuples, qualifiers, evidence codes, references,
  isoforms, and WITH/FROM unions were independently checked against the live export.
- No source annotation is negated and no live row carries an extension.

## Protein architecture and product boundaries

LNPK is a 428-aa, N-myristoylated, double-pass integral ER membrane protein. UniProt
places the two transmembrane segments at residues 46–66 and 78–98, leaving both the
N terminus and the long C-terminal region cytosolic. The C-terminal region contains
coiled-coil and C4 zinc-finger features needed for self-association and junction
targeting. Human-cell topology experiments directly support the double-spanning,
cytosolic-termini model [PMID:24223779, "Analysis of tumor necrosis factor-fusion
proteins with each of the two putative transmembrane domains and their flanking
regions of protein Lunapark revealed that transmembrane domain 1 and 2 functioned as
type II signal anchor sequence and stop transfer sequence, respectively, and together
generated a double-spanning integral membrane protein with an N-/C-terminal
cytoplasmic orientation."]

UniProt lists four splice products. Isoform 2 replaces the first nine residues and was
the construct used in the HuRI source rows; that identifies the tested product but does
not establish isoform-specific interactions. Isoform 3 lacks residues 1–123, including
the membrane-targeting N terminus and both transmembrane segments, so its localization
and function cannot be inferred from canonical LNPK. Isoform 4 contains a 31-aa
insertion at residue 235. No separate physiological function is established for any
alternative product.

## Evidence hierarchy

1. **Direct human causal mechanism.** U2OS CRISPR knockout reduces peripheral ER
   tubules and three-way junctions in favor of sheets; low-level wild-type rescue
   restores the network and localizes to junctions [PMID:27619977, "Cells lacking Lnp
   exhibited a proliferation of peripheral sheets and a reduction of tubules and
   junctions"]. The same study links zinc-finger-containing sequences to LNPK–LNPK
   interaction and junction targeting.
2. **Human topology and lipidation.** HEK293T/COS-1 experiments establish an
   N-myristoylated, double-pass integral ER protein; overexpression reshapes peripheral
   ER, with the expected overexpression caveat [PMID:24223779].
3. **Mammalian junction dynamics.** Nascent junctions that acquire LNPK persist, while
   those that do not rapidly close [PMID:25548161, "Newly formed junctions that acquire
   mLnp1 remain stable within the ER network, whereas nascent junctions that fail to
   acquire mLnp1 undergo rapid ring closure."]. The cache is abstract-only, so exact
   construct provenance is not overinterpreted.
4. **Curvature/junction mechanism.** Modeling plus mammalian experiments frame LNPK as
   an S-type curvature stabilizer at concave junction edges [PMID:25404289]. Reciprocal
   regulation with atlastin further supports LNPK as a junction stabilizer rather than
   a membrane-fusion catalyst [PMID:30498943, "Junctions are formed through atlastin
   (ATL)-mediated membrane fusion and stabilized by lunapark (Lnp)."].
5. **Human disease physiology.** Biallelic loss-of-function causes a severe
   neurodevelopmental syndrome; affected cells lack full-length LNPK and have abnormal
   ER structures, and all three reported individuals had corpus-callosum hypoplasia
   [PMID:30032983].

## Existing-annotation decisions

- Accept the specific ER tubular-network, ER-membrane, three-way-junction-network,
  homodimerization, ER-organization, and ER-maintenance annotations.
- Replace the two `positive regulation of endoplasmic reticulum tubular network
  organization` annotations with direct executor terms: GO:0071788 for the maintenance
  experiment and GO:0071786 for the overexpression/morphology experiment.
- Replace broad `membrane` with GO:0005789 ER membrane.
- Mark generic protein-binding screen rows as over-annotated. The BioPlex SYNPR and
  isoform-2 HuRI edges have no demonstrated LNPK mechanism or stable-complex role.
- Mark limb development as over-annotated: PMID:12732147 reports shared expression in a
  regulatory landscape, not a causal developmental function.

## Synthesis

The core function is architectural: LNPK is active in the ER tubular network and
stabilizes newly created three-way junctions. Its membrane topology, N-myristoylation,
self-association, and zinc-finger/coiled-coil regions position it at junctions and help
maintain the balance between tubules, junctions, and sheets. LNPK is not assigned a
stable stoichiometric complex because reported partners are either screen hits or
dynamic ER-shaping proteins.

Two downstream human roles are retained outside the core architectural unit:

- Biallelic loss-of-function supports GO:0022038 corpus callosum development
  [PMID:30032983, "Together, our results implicate the ER junction stabilizer lunapark
  in establishing the corpus callosum."].
- Human-cell knockout/depletion supports a spatially restricted contribution to
  secretome-mRNA initiation at lysosome-proximal LNPK-marked ER junctions
  [PMID:41193816, "Loss of LNPK selectively reduces ribosome occupancy and translation
  efficiency of secretome mRNAs at these junctions by impairing eIF2-dependent
  initiation, an effect that can be rescued by the integrated stress response (ISR)
  inhibitor ISRIB."].

## Unresolved findings and boundaries

- PMID:27387505 reports intrinsic and associated in-vitro ubiquitin-ligase activity for
  mammalian LNPK. The cache is abstract-only, current UniProt/GOA do not adopt this
  catalytic activity, and independent replication is lacking. It is therefore a
  knowledge gap, not a NEW or core molecular function.
- Direct zinc binding has not been measured even though the conserved C4 zinc-finger is
  functionally required. Do not upgrade the current inferred zinc-binding feature to an
  experimental annotation.
- The curvature-stabilizer model does not establish membrane curvature sensor activity
  or direct membrane bending in a purified human assay.
- It remains unclear how the structural ER-junction role produces selective translation
  initiation effects and why loss preferentially disrupts corpus-callosum development.
- The eight isoform-2 HuRI partners and the SYNPR BioPlex association need endogenous,
  topology-aware validation before any specific interaction function is inferred.

## Questions and experiments

1. Does purified human LNPK have intrinsic ubiquitin-ligase activity after eliminating
   copurifying E3 enzymes? Reconstitute wild-type and N-terminal mutants with defined
   E1/E2/ubiquitin components and orthogonal mass-spectrometric product detection.
2. Which LNPK architecture features distinguish junction stabilization from the
   translation phenotype? Rescue LNPK-null human cells with myristoylation-, coiled-coil-,
   zinc-finger-, and oligomerization-defective variants while measuring both ER topology
   and spatial ribosome occupancy.
3. Are alternative products membrane-localized and functional? Express endogenous-level,
   isoform-specific tagged products and test junction localization, topology, and rescue.
4. What neural cell type makes corpus-callosum development most sensitive to LNPK loss?
   Use isogenic human neural organoids with lineage-restricted rescue and quantitative ER
   ultrastructure, axon-extension, and secretome-translation readouts.
