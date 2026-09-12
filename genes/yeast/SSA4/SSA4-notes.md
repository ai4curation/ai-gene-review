# SSA4 review notes

## 2026-08-22 re-review

- Identity was rechecked as *Saccharomyces cerevisiae* SSA4/YER103W, UniProt
  P22202: the stress-inducible cytosolic Ssa-family Hsp70 paralog. The
  project/workflow citation sentence was removed from the standalone YAML
  description; the Falcon report remains an explicit reference in the review.
- The core function remains one ATP-dependent protein folding chaperone
  activity (GO:0140662) in cytosolic folding/refolding. The broader GO:0044183
  IBA and both GO:0051082 annotations are modified to GO:0140662, while generic
  nucleotide binding is marked over-annotated because ATP binding and ATP
  hydrolysis are already represented. SSA-family Hsp70 is experimentally
  required for folding newly translated cytosolic proteins. [PMID:9789005
  "yeast cytosolic OTC is assisted to its native state by the SSA class of yeast
  cytosolic Hsp70 proteins"]
- The two GO:0006616 annotations retain their existing modification to
  GO:0031204. The IMP rationale is narrowed to the strong rapid effect on
  post-translational ER prepro-alpha-factor import; the paper's separate
  mitochondrial precursor phenotype is recorded but is not encoded by that
  ER-scoped replacement. [PMID:8754838 "The processing of
  prepro-alpha-factor was inhibited within 2 min of the shift to 37 degrees C,
  suggesting a direct effect of the hsp70 defect on translocation."]
- Nuclear localization remains non-core rather than removed because it is an
  experimentally observed, reversible starvation response. [PMID:11279056 "the
  hsp70 Ssa4p concentrates in nuclei upon starvation. Nuclear concentration of
  Ssa4p in starving cells is reversible"]
- The plasma-membrane IBA is removed as a stale PAINT transfer. The pinned 2025
  GOA row points to PTN002500132, but the current local PTHR19375 PAINT snapshot
  carries nucleus and cytosol at that node and no longer carries GO:0005886.
  This is a current-node comparison, not an inference from donor count or the
  composition of WITH/FROM. A targeted OpenScientist run challenged the prior
  KEEP_AS_NON_CORE decision and independently preferred REMOVE because it found
  no SSA4-specific plasma-membrane evidence; the yeast plasma-membrane
  proteomics annotations it identified concern Ssa1/Ssa2/Ssb1, not Ssa4. Its
  live QuickGO absence is consistent with current PAINT, but the report wrongly
  implies that the pinned SSA4 snapshot lacks the 2025 IBA and speculates about
  donor origins. Those claims remain marked DISPUTED and are not used.
  [file:yeast/SSA4/SSA4-hypotheses/existing-go-0005886-keep-as-non-core/openscientist.md
  "The only yeast PM evidence for this family ... covers the paralogs
  Ssa1/Ssa2/Ssb1 ... and excludes Ssa4"]
- The UNFOLDED_PROTEIN_BINDING project row now uses GO:0140662 for SSA4, aligning
  the project decision with the review's ATP-dependent Hsp70 mechanism. All nine
  generic protein-binding IPI rows are now represented separately and modified
  to Hsp70 or heat-shock-protein binding according to the GOA partner; the three
  protein-folding and three unfolded-client IGI rows are likewise retained as
  distinct SSA1/SSA2/SSA3-linked records. No module currently names SSA4.

## 2026-08-27 reviewer follow-up

- The imported SGD/Alliance description was not accepted wholesale: its
  SRP-dependent cotranslational clause conflicts with the primary SSA/Ydj1
  translocation evidence and the review's GO:0031204 replacement. The description
  rubric now explicitly scores and explains that mechanistic error.
- A newly cached primary study directly supports a second conditional nuclear
  localization context. Under cadmium stress, ScSsa4 translocates to the nucleus,
  associates with Pom34, and regulates VHS1 expression in a pathway that reduces
  cadmium accumulation. [PMID:39456809 "ScSSA4 binds to POre Membrane 34 (POM34),
  a key component of nuclear pore complex (NPC), and translocates from the cytoplasm
  to the nucleus, where it regulates the expression of its downstream gene, Viable
  in a Hal3 Sit4 background 1 (VHS1), resulting in reduced Cd accumulation in yeast
  cells."] Both nucleus rows remain KEEP_AS_NON_CORE because starvation and cadmium
  trigger context-specific relocalization rather than defining Ssa4's default
  cytosolic site.
- The redundant synthetic NEW GO:0140662 row was removed. GO:0140662 remains the
  replacement for each broader chaperone/client-binding row and the molecular
  function in `core_functions`; the review therefore contains exactly one record per
  one of the 33 pinned GOA rows. Generic nucleotide binding is now MODIFY to the
  existing specific ATP-binding term GO:0005524.
- The four remaining interactome references now carry manual caveats. Their GOA
  partner identities are retained, but genome-scale co-complex, prediction, paralog-
  heteromer, and affinity-enrichment datasets are not described as targeted proof of
  direct binary contact when the specific edge is absent from the narrative text.
