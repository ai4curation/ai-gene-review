# amoA Gene Review Notes

## Colleague Question
**Contact**: nitrogen@whoi.edu
**Key Issue**: Very difficult to distinguish amoA from pmoA by sequence alone

## Key Findings

### The amoA/pmoA Confusion Problem
- **High sequence similarity**: ~40% identity, ~60% similarity
- Both are copper-dependent monooxygenases
- Both have similar membrane topology
- Both oxidize small hydrocarbons
- Functional annotation often wrong

### Distinguishing Features
1. **Active site residues**:
   - amoA: His residues coordinating Cu centers
   - Specific motifs in transmembrane regions
   - Conservation patterns differ subtly

2. **Phylogenetic clustering**:
   - amoA clusters with nitrifiers
   - pmoA clusters with methanotrophs
   - Need robust tree with many sequences

3. **Gene context**:
   - amoA: Found with amoB, amoC genes
   - pmoA: Found with pmoB, pmoC genes
   - Metabolic gene neighborhoods differ

### Functional Differences
- **amoA**: NH₃ + O₂ → NH₂OH (hydroxylamine)
- **pmoA**: CH₄ + O₂ → CH₃OH (methanol)
- Different substrate binding pockets
- Different product release mechanisms

## Environmental Importance
- Nitrosopumilus dominates ocean nitrification
- Critical for nitrogen cycling
- Climate impact (N₂O production)
- Key biomarker for ammonia oxidizers

## GO Annotation Review
- Modified general monooxygenase to specific ammonia monooxygenase
- Added nitrification process
- Confirmed membrane localization
- Specified archaeal-specific annotations

## Practical Tips for Distinction
1. **Never trust BLAST alone** - too similar
2. Check gene synteny (amoB/C presence)
3. Use specialized databases (FunGene)
4. Consider environmental context
5. Look for diagnostic residues

## Key Publications
- [PMID:15574881] - Discovery of archaeal ammonia oxidation
- [PMID:22775980] - Environmental distribution
- [PMID:26923429] - Structure-function relationships
- [PMID:31796959] - Evolution of copper monooxygenases

## Biotechnology Applications
- Wastewater treatment monitoring
- Nitrogen removal systems
- Climate change indicators
- Bioremediation markers

## Remaining Questions
- Can single enzyme oxidize both NH₃ and CH₄?
- What determines substrate specificity?
- How to design specific inhibitors?
- Evolutionary relationship to pmoA?

## Bioinformatics Resources
- FunGene database for functional genes
- Specific amoA primers for PCR
- Curated reference alignments
- Diagnostic HMM profiles

## 2026-10-15: merge of the duplicate D9J262 review (claude-code, claude-opus-5-5)

Two folders reviewed the same UniProt accession D9J262: `genes/NITRP/amoA/`
(DRAFT; MODIFY + 3 NEW) and `genes/NITRP/D9J262/` (COMPLETE; ACCEPT + 2 NEW).
`genes/NITRP/amoA/` is now the single canonical review. `genes/NITRP/D9J262/`
was retired; its Falcon deep research was moved here unchanged as
`amoA-deep-research-falcon.md` (plus `_artifacts/`).

### Identity of D9J262 (corrects both earlier reviews and the deep research)
- D9J262 (D9J262_9ARCH) is a 208-aa **fragment** from environmental clone
  SF_AOA_C12 (UniProt `RC   STRAIN=SF_AOA_C12`), sequenced in a shrimp
  aquaculture biofilter survey [PMID:22775980 "Analysis of bacterial and archaeal
  amoA gene sequences revealed that most ammonia oxidizers were related to
  Nitrosomonas marina and Nitrosopumilus maritimus."]. It is assigned to the
  species-level taxon 338192, not to strain SCM1.
- The deep research equates D9J262 with SCM1 locus Nmar_1500. That is wrong:
  Nmar_1500 is UniProt A9A4U2 (A9A4U2_NITMS, 216 aa; UniProt REST query for
  `Nmar_1500`, 2026-10-15). SCM1 expression/kinetic data in the deep research
  apply to the species, not to this sequence.

### GOA refresh (2026-10-15)
- `just fetch-gene NITRP amoA --force`: UniProt entry version 26 -> 28 removed
  the keyword-mapped `DR GO` lines (GO:0016020 membrane, GO:0004497 monooxygenase
  activity). QuickGO now returns 0 annotations for D9J262 (checked directly).
- The old GO:0004497 IEA row is kept with `retired: true` (precedent:
  `genes/EMENI/fadA`).

### How the conflicting actions were resolved
- **GO:0004497 monooxygenase activity** (amoA: MODIFY; D9J262: ACCEPT) ->
  **MODIFY to GO:0018597 ammonia monooxygenase activity**. True but general
  term; the specific is_a descendant is supported by the Archaeal_AmoA domain
  (PF12942) and family placement. Comparator: bacterial AmoA Q04507
  (AMOA_NITEU) carries GO:0018597 by EXP (PMID:19453274) and GO:0004497 by
  IDA/IMP in QuickGO (2026-10-15). The activity belongs to the complex; the
  catalytic copper site has not been assigned to a subunit
  [PMID:36721060 "no structural studies have been successfully carried out for
  any AMO complex, bacterial or archaeal"].
- **Membrane** (both: NEW GO:0016020) -> **NEW GO:0005886 plasma membrane**
  (ISS). Five Phobius TM helices; AMO subunits are among the most abundant
  membrane-fraction proteins in AOA [PMID:36721060 "AMO subunits (AmoA, AmoB,
  and AmoC) were among the most abundant proteins (22% of iBAQ normalized
  intensity) detected overall in these membrane fractions."]; AOA have one cell
  membrane plus S-layer [PMID:36721060 "rely on a proteinaceous S-layer rather
  than an outer membrane to create a pseudo-periplasmic space"]. Q04507 has
  plasma membrane by EXP.
- **GO:0019329 ammonia oxidation** and **GO:0019409 aerobic respiration, using
  ammonia as electron donor** (amoA: NEW, NAS, no reference) -> **dropped**.
  Comparator check: QuickGO shows 0 annotations to either term for any gene
  product, including the experimentally characterised Q04507, which carries no
  process term at all. GO:0019409's definition ("enzymatic reactions convert
  ammonia to hydrazine, and hydrazine to nitrite") does not describe aerobic
  nitrification. Raised as a suggested question instead.
- **GO:0019331 anaerobic respiration, using ammonium as electron donor**
  (D9J262: NEW, TAS PMID:22775980) -> **dropped**. That term is anammox
  (ammonium + nitrite -> N2 in the absence of oxygen); N. maritimus is an aerobic
  ammonia oxidiser, and PMID:22775980 is an ecological survey that does not
  support any process claim.
- **Proposed term "archaeal ammonia oxidation"** (D9J262) -> **dropped**; GO
  does not split processes by taxon. Replaced by a proposed CC term "ammonia
  monooxygenase complex" (parent GO:1990204 oxidoreductase complex, analogous
  to GO:0015050 methane monooxygenase complex), supported by the AmoABCXYZ
  composition [PMID:36721060 "Besides the known AmoABC subunits and the earlier
  predicted AmoX, two new protein subunits, AmoY and AmoZ, were identified."].

### Citation problems in the earlier notes above
The "Key Publications" list above cites PMIDs that resolve (PubMed esummary,
2026-10-15) to unrelated papers and should not be used:
- PMID:15574881 = "Beta1-integrin orients epithelial polarity via Rac1 and laminin"
- PMID:26923429 = "Enantioselective GC-MS analysis of volatile components from rosemary ..."
- PMID:31796959 = "Anatomical correlates of rapid eye movement sleep-dependent plasticity ..."

Verified replacements cached for this review: PMID:20421470 (Walker 2010,
N. maritimus SCM1 genome), PMID:19794413 (Martens-Habbena 2009, SCM1 kinetics),
PMID:36721060 (Hodgskiss 2023, archaeal AMO complex composition).
