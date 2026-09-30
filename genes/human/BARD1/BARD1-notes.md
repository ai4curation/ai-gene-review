# BARD1 review notes

## 2026-09-30 — human BARD1

Human BARD1 is UniProt Q99728, HGNC:952, NCBI Gene580. The source record has four alternative products; their identifiers, names and sequence-difference descriptors are preserved. The full-length protein and engineered experimental fragments must not be treated as functional measurements of every alternative product.

### Chromatin recognition and ubiquitination

[PMID:34321665](https://pubmed.ncbi.nlm.nih.gov/34321665/) provides structural, binding and ubiquitination evidence using recombinant human sequences. BARD1's ankyrin/BRCT region recognizes histones, DNA and N-terminal H2A ubiquitin marks, while its RING region helps position the ligase on the nucleosome. BRCA1 provides the observed E2 interface. Keep recognition of RNF168-generated H2AK13/K15 ubiquitin distinct from the heterodimer's modification of C-terminal H2A K125/K127/K129. Constructs include engineered fusions and isolated domains as well as a near-full-length BARD1 construct. The publisher's author correction adds a citation and related sentence; it does not retract the assays.

The first core function combines the demonstrated ubiquitin-modified histone reader activity with a contribution to histone H2A ubiquitin ligase activity. The existing K127/K129 assertions remain in their original source rows. H4K20me0 recognition is described without adding redundant broad and narrow reader annotations. The BRCA1–BARD1 complex belongs in `in_complex`; nucleus is the anatomical location.

[PMID:12890688](https://pubmed.ncbi.nlm.nih.gov/12890688/) supports K6-linked autoubiquitination in the tested heterodimer system. [PMID:17873885](https://pubmed.ncbi.nlm.nih.gov/17873885/) shows E2-dependent differences in output, so K6 is not asserted as the exclusive linkage for every substrate. [PMID:15184379](https://pubmed.ncbi.nlm.nih.gov/15184379/) reports NPM1 stabilization after ubiquitination; ubiquitination is not equated universally with degradation.

### Direct assistance of DNA repair

[PMID:28976962](https://pubmed.ncbi.nlm.nih.gov/28976962/) shows that purified BRCA1–BARD1 binds DNA and RAD51 and promotes synaptic complex formation and D-loop formation. BARD1 RAD51-contact mutations impair stimulation while retaining DNA binding, and complementary BRCA1 mutants also compromise activity. This supports a complex-contributed recombinase activator function, distinct from RAD51's strand-exchange catalysis and BRCA2-like presynaptic loading. The independent annotation consultation agrees with one new molecular-function assertion for this activity; no new biological-process assertion is needed because homologous recombination is already represented.

[PMID:39261729](https://pubmed.ncbi.nlm.nih.gov/39261729/) separately reconstitutes stimulation of DNA-end resection machinery. EXO1 and DNA2 perform nuclease reactions, and BLM/WRN supply helicase activity. The BRCA1–BARD1 contribution is not grounds for assigning those catalytic activities to BARD1. The source's DSB-end resection assays do not establish the narrower replication-fork resection assertion in GO:0110025.

### Context and unresolved assertions

The original XIST paper [PMID:12419249](https://pubmed.ncbi.nlm.nih.gov/12419249/) includes anti-BARD1 precipitation experiments despite its BRCA1-focused title. The available original Results support association without resolving direct RNA binding. Later disagreement about BRCA1-dependent XIST localization does not automatically refute that BARD1 association. Retain the curated RNA-binding observation as non-core.

[PMID:10477523](https://pubmed.ncbi.nlm.nih.gov/10477523/) reports CstF-50 binding and inhibition of polyadenylation; [PMID:15905410](https://pubmed.ncbi.nlm.nih.gov/15905410/) links the heterodimer to damage-dependent RNAP II ubiquitination/degradation and reduced 3′ processing. These provide specific regulatory contributions, without making BARD1 the RNA-cleavage or polyadenylation enzyme. The apoptosis and cell-cycle experiments are context-dependent; the proapoptotic p53/Ku70 mechanism and antiapoptotic BRCA1 nuclear-retention experiment need not have the same outcome.

Two original assertions remain UNDECIDED. For PMID:35512704, the exact BARD1–AKT1 wild-type/variant constructs were not resolved from the inspected material. For PMID:29709199, selected MRN-review passages do not establish BARD1-specific replication-fork resection. Neither uncertainty is framed as evidence that the curator cited the wrong gene or that the original experiment did not exist.

All 53 Reactome-derived annotations are nucleoplasm locations. Event titles describing phosphorylation, nucleolysis or another repair reaction are contextual information, not evidence that BARD1 executes every reaction. Disease-event wording is not a NOT qualifier. The original PAINT node assertions are retained; a short donor list or BARD1 itself among donors is not circular evidence. No complete family phylogeny was available, and the unreviewed family prose was not used as biological proof. No BARD1/Q99728 entry was found in the local GO-CAM index.

### Research and validation boundaries

The standard Falcon/perplexity-lite invocation failed before either provider started because its pinned client dependency was unavailable offline. No provider report was manufactured. The review uses the normal source caches and explicitly bounded primary-paper readings. Full text flags were checked against actual content: several records remain abstract-only, and no complete supplementary-data or figure-image audit is claimed. Exact source and alternative-product objects are preserved; only authored curation fields are changed.

The integrated review preserves 161 source assertions and four alternative products, and adds one complex-contributed molecular function. The decisions are 96 ACCEPT, 50 KEEP_AS_NON_CORE, 13 MODIFY, two UNDECIDED and one NEW. The two additional papers were recovered as exact normal records after the ordinary cache command failed with DNS errors; both canonical records were verified equal to the authenticated staging bytes before application. No downloaded source text was edited.

Focused validation passed on 2026-09-30 with 33 advisories for supported generic interactions retained as non-core under the supplied ActionEnum. Rendering passed, and a matching Codex history record was scaffolded with `just new-history`. The two unresolved annotations remain explicit. This is a focused-gene result; the earlier repository-wide reference check remains incomplete because of an unrelated Crossref DNS failure.
