# SSA3 review notes

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: wording was adjusted from `cytosol/nucleus proteostasis network` to avoid confusion with project-specific Proteostasis Network terminology.

## 2026-08-22 re-review

- Identity was rechecked as *Saccharomyces cerevisiae* SSA3/YBL075C, UniProt
  P09435: the stress-inducible cytosolic Ssa-family Hsp70 paralog. SSA3 is
  normally expressed at very low levels but can provide essential Ssa function
  when expressed constitutively. [PMID:3302682 "an intact copy of SSA3 regulated
  by the constitutive SSA2 promoter was capable of rescuing a ssa1 ssa2 ssa4
  strain"]
- The core function is consolidated as ATP-dependent protein folding chaperone
  activity (GO:0140662) in cytosolic folding/refolding. The broader
  GO:0044183 IBA is modified to that mechanistically precise child term, and
  generic nucleotide binding is marked over-annotated because ATP binding and
  ATP hydrolysis are already represented. SSA-family Hsp70 is experimentally
  required for folding newly translated cytosolic proteins. [PMID:9789005
  "yeast cytosolic OTC is assisted to its native state by the SSA class of yeast
  cytosolic Hsp70 proteins"]
- The two GO:0006616 annotations are modified rather than simply retained as
  non-core. Becker et al. tested precursor import into the ER and mitochondria,
  supporting post-translational translocation (GO:0006620), not the existing
  SRP-dependent cotranslational label. [PMID:8754838 "These results are
  consistent with SSA proteins and Ydj1p acting together in the translocation
  process."]
- The plasma-membrane IBA is removed as a compartment-mismatched family
  propagation. UniProt and the SSA3-focused literature consistently identify
  Ssa3 as cytosolic; no target-specific plasma-membrane evidence was found. A
  targeted OpenScientist hypothesis run independently preferred `REMOVE`: it
  traced the family signal to plasma-membrane proteomics evidence for Ssa1/Ssa2,
  found no current GO_Central GO:0005886 annotation for P09435, and characterized
  `KEEP_AS_NON_CORE` only as a conservative fallback. [file:yeast/SSA3/SSA3-hypotheses/existing-go-0005886-keep-as-non-core/openscientist.md
  "**Primary lead — REMOVE** the plasma-membrane IBA for SSA3."]
- The PMID:10745074 cached abstract is not treated as a direct SSA3 localization
  experiment: it describes cytoplasmic Ssa-family Hsp70s but reports the detailed
  transport/localization results for Ssa1/2. The cytosol annotation remains
  accepted because that location is independently established and the curator
  had access to more evidence than the cached abstract.
- The UNFOLDED_PROTEIN_BINDING project row now uses GO:0140662 for SSA3, aligning
  the project decision with the review's ATP-dependent Hsp70 mechanism.
