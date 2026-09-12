# ADAM10 notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene-pmids human ADAM10` completed successfully; all 44 PMID-backed publication caches were present after refresh.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human ADAM10 --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes rely on cached UniProt, GOA, and publication files.
- `just validate human ADAM10` passes cleanly.

## Functional synthesis

ADAM10 is a type I membrane zinc metalloprotease and broad ectodomain sheddase. A tetraspanin-regulation study gives the cleanest high-level statement of the core function: [PMID:26686862 "ADAM10 mediates the ectodomain shedding of more than 40 transmembrane proteins"] It also captures two central substrate axes: APP [PMID:26686862 "ADAM10-mediated cleavage of the amyloid precursor protein (APP) prevents the formation of the amyloid peptide Aβ"] and Notch [PMID:26686862 "ADAM10 is also the main protease for the cleavage of Notch receptors at a site called S2 following ligand binding"].

ADAM10 alpha-secretase biology is directly relevant to Alzheimer mechanisms. A full-text cached paper states [PMID:33731436 "ADAM10 cleaves APP to generate neuroprotective soluble APPα (sAPPα), which precludes the generation of Aβ"] and frames reduced ADAM10 activity as a shift toward beta-secretase processing. Synaptic trafficking work adds that ADAM10 resides in postsynaptic compartments and that its surface removal affects activity: [PMID:23676497 "ADAM10 removal from the plasma membrane was mediated by clathrin-dependent endocytosis"].

ADAM10's substrate range is much broader than APP. L1 processing supports cell-surface/Golgi/vesicle cleavage: [PMID:12475894 "ADAM10 is involved in L1 cleavage, which occurs at the cell surface and in the Golgi apparatus"] Fractalkine/CX3CL1 processing supports constitutive shedding: [PMID:12714508 "ADAM10 contributes to the constitutive shedding of CX3CL1 in unstimulated cells"] TREM2 shedding, TNF-family and FasL processing, cadherin/junction substrates, and tetraspanin-dependent substrate selectivity were retained as substrate-specific consequences of the same sheddase function rather than separate core functions.

The S. aureus alpha-toxin pore annotations are biologically supported as pathogen exploitation of junctional ADAM10, not normal evolved host function: [PMID:30463011 "Junctionally clustered ADAM10 supports the efficient formation of stable toxin pores."] These were retained as non-core.

## Annotation decisions

- Accepted metalloendopeptidase, metallopeptidase, endopeptidase, proteolysis, membrane-protein ectodomain proteolysis, constitutive ectodomain proteolysis, signaling receptor ligand precursor processing, APP catabolic processing, negative amyloid-beta formation regulation, Notch signaling, EGFR-ligand maturation, and core membrane/Golgi/synaptic/tetraspanin-domain locations.
- Modified `negative regulation of amyloid precursor protein biosynthetic process` to APP catabolic processing and negative regulation of amyloid-beta formation; ADAM10 cleaves APP rather than regulating APP biosynthesis.
- Removed `metallodipeptidase activity` because ADAM10 is an endopeptidase/sheddase, not a dipeptidase.
- Marked generic `protein binding` annotations as over-annotated.
- Kept immune, adhesion, chemokine, TNF, FasL, TREM2, synaptic-organization, developmental, granule, exosome, and S. aureus alpha-toxin pore annotations as non-core substrate/context outputs.

Final action distribution: 88 ACCEPT, 42 KEEP_AS_NON_CORE, 19 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 1 REMOVE.

## Knowledge gaps and experiments

- The major curation challenge is representing ADAM10 substrate specificity without turning every downstream substrate phenotype into a core function.
- Useful experiments would combine endogenous ADAM10 variant knock-ins with substrate-specific reporters for APP, Notch, cadherins, TREM2, CX3CL1, and TNF-family substrates across defined tetraspanin backgrounds.
- For Alzheimer biology, the highest-value assay is compartment-resolved measurement of ADAM10 maturation, synaptic/cell-surface retention, APP alpha-cleavage, and amyloid-beta suppression in human neurons.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls. No annotation actions were
changed. The single REMOVE call remains appropriate for GO:0070573
metallodipeptidase activity, because ADAM10 is a membrane
metalloendopeptidase/sheddase and not a dipeptidase.

The YAML now records `reference_review` metadata for the main evidence anchors:
PMID:26686862 for broad ectodomain shedding, APP cleavage, Notch S2 cleavage,
and tetraspanin compartmentalization; PMID:33731436 for APP alpha-secretase
cleavage; PMID:23676497 for synaptic ADAM10 endocytosis; PMID:12475894 for L1
cleavage at cell-surface/Golgi-vesicle contexts; and PMID:30463011 for
S. aureus alpha-toxin exploitation of junctional ADAM10.

The core review remains substrate-aware but conservative: ADAM10's evolved core
function is regulated membrane-protein ectodomain shedding. Substrate-specific
outputs should be retained when directly supported, but broad downstream
developmental, immune, synaptic, pathogen, or cancer phenotypes should not be
promoted above that sheddase mechanism.
