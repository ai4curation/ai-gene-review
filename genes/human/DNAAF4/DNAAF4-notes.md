# DNAAF4 curation notes

## 2026-10-17 — source-based review

Reviewed all 42 imported GO annotations and preserved their source dictionaries. The [source guide](DNAAF4-source-guide.md) records the actual species, constructs, assays, original-section locators and access limits. The current proposal contains 9 ACCEPT, 16 MODIFY, 16 KEEP_AS_NON_CORE and one REMOVE, with no NEW annotations.

The core is one dynein preassembly unit covering outer and inner arms in cytosol and DynAPs. Molecular function is omitted because neither assembly-factor membership nor chaperone co-immunoprecipitation establishes an autonomous folding or motor activity. Ciliary movement, fluid flow and laterality remain positive physiological contexts. The sole removal corrects a process-to-extracellular-location inference.

Nuclear and neuronal observations remain positive in their reported contexts. The estrogen-receptor work supports specific binding and directional regulation, retained as secondary biology rather than a second defining core. Rat neurite proximity, human cellular co-immunoprecipitation, proposed protein cleavage and natural splice products are kept distinct. The obsolete estrogen-receptor-binding source IDs remain intact, with current nuclear receptor binding proposed in the reviews.

Seven binding rows receive supported partner-class refinements. DNAAF2, DNAAF6 and ZMYND10 associations remain non-core where no more informative molecular-function class is established. This applies the [project instruction](https://github.com/ai4curation/ai-gene-review/blob/062f1cb52a5dc375c70af95599c74317bccd775c/projects/CLINGEN_MENDELIAN.md#curation-instructions), without inventing a catalytic or physiological pathway role from association.

All three official products are retained. The 2018 isoform labels correspond to official products by length/domain organization, not complete recovered plasmid sequences; interaction efficiencies do not establish identical assembly activity. Source caches and availability flags remain unchanged. Automated research failed and manual original-source review supplied the assessment; no provider output was fabricated.


## Follow-up: chaperone binding and the unresolved assembly mechanism

This entry supersedes the earlier reason for omitting a molecular function. [GO:0051087](https://www.ebi.ac.uk/QuickGO/term/GO:0051087) concerns the chaperone partner; it does not require DNAAF4 to fold proteins autonomously. The single assembly core now records protein-folding chaperone binding, supported by human DYX1C1–HSP70/HSP90 LUMIER associations in [PMID:29844425](https://doi.org/10.1038/s41467-018-04431-1), Results/Figure 4b and LUMIER Methods. The low, controlled co-IP efficiencies are association measurements, not affinities or purified-contact proof. The new ten-word source anchor occurs once in the YAML core.

The [PMID:23872636](https://doi.org/10.1038/ng.2707) chaperone interactome provides separate ortholog evidence. Results describe mouse trachea and confirm HSP70/HSP90/CCT associations, while the immunoprecipitation Methods specify mouse brain lysates. These contexts remain distinguished from the human DNAAF2 assays. The DNAAF2, DNAAF6 and ZMYND10 source pairs stay positive and non-core: their assembly/co-chaperone roles do not automatically establish that each partner recognizes nascent or unfolded clients. No source partner is replaced by an HSP from a different experiment.

The core now records a residual biological knowledge gap and a matching experiment: how these contacts contribute to client recognition, chaperone cycling and productive dynein assembly. No folding, ATPase-regulatory or motor activity is asserted. The 2018 R2SP client experiments belong to PIH1D2 and do not close this DNAAF4-specific gap. DynAP wording explicitly identifies tagged Xenopus ortholog evidence, without changing the existing location annotations.

All 42 imported source objects, all actions, three products and source files are unchanged. The original four quotations remain intact; only the ten-word PMID:29844425 anchor is added. The guide remains a locator and is not primary support. Separately recovered original sections for the three abstract-only caches remain distinguished from those caches in their reference assessments. Rat neuronal perturbation and mouse knockout observations retain their different contexts; no universal finding reversal is asserted.


## Follow-up: explicit chaperone-binding annotation

The existing assembly core is now matched by one proposed GO:0051087 annotation (IPI, PMID:29844425), based on the controlled human HEK293 LUMIER experiments described above. This supersedes the earlier no-NEW statement: the 42 imported source objects and their decisions are unchanged, with one authored binding assertion appended. Co-immunoprecipitation supports specific association without establishing a purified direct interface or an autonomous folding reaction. No HSP accession or natural-isoform assignment is invented. The core, products and residual mechanistic gap are unchanged. The ten-word source anchor now occurs in the new row and the existing core, totaling 20 quoted words from this paper.

The three supported generic-binding rows remain KEEP_AS_NON_CORE under the [explicit user instruction for this ClinGen project](https://github.com/ai4curation/ai-gene-review/blob/892df26b8431488c000fcd9c85197d0d8644622e/projects/CLINGEN_MENDELIAN.md#curation-instructions). This task-specific instruction takes precedence over the general informational-exclusion recommendation; it neither changes repository-wide policy nor treats uninspected evidence as verified. Their positive source evidence and partner-specific limitations remain the reasons for retention. Replacing them with REMOVE solely to silence a policy advisory would conflict with that instruction.

The preceding canonical normal and CI checks passed with four warnings. Three concerned this intentional generic-binding treatment; the remaining warning concerned the core function lacking an annotation, which this addition addresses. These were warnings rather than validation errors. The successor still requires the publisher's ordinary checks; this note does not claim they have already run.
