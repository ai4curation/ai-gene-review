# statA evidence notes

## 2026-09-20 focused OpenScientist report incorporation

Read all findings, evidence matrix, limitations and leads in `statA-hypotheses/proliferation-and-defense-response/openscientist.md`. The report resolves the STATb proliferation source and acknowledges: "**Vegetative growth rate of statA-null** — Not directly quantified in the retrieved literature." Its defense assessment similarly states: "**statA in bacterial killing / S-cell function** — Untested."

The report does not establish STATa-specific loss of either function. Metazoan source leaves, a distinct TirA defense pathway and direct STATb growth evidence are not exclusion tests. Retain GO:0042127 and GO:0006952 as non-core ancestral inferences from PTN000927860. Differentiation is not itself proliferation evidence, and osmotic stress is not defense evidence. The report is DISPUTED for its donor-composition and absence-of-assay rejection rationale. No duplicate report requested.


## Recovery PR evidence follow-up (2026-09-22)

Anchor the retained STAT defense inference to the actual PAINT IBD row, or remove the unsupported negative ACG/SDF-1 assertion from supporting evidence; keep the report assessment in the reason.

## Literature review integration (2026-10-04)

- Liongue & Ward 2013 (PMID:24058787) and Wang & Levy 2012 (PMID:24058748) added to the GO:0007259 -> GO:0097696 MODIFY.
  JAK is a metazoan innovation [PMID:24058787 "The first bona fide JAK-like protein is represented in the basal metazoan porifera lineage"],
  and the pathway was assembled in bilateria [PMID:24058787 "the interaction of these proteins to form an active pathway, which occurred in bilateria"].
  Dictyostelium STAT signaling lies outside the Metazoa [PMID:24058748 "The discovery of STAT signaling in Dictyostelium extended this intercellular phosphotyrosine pathway beyond the Metazoa"].
- Implication for PAINT: the GO:0007259 IBD sits at PTN000927860, which includes the Dictyostelium STATs.
  On Liongue's timeline the JAK-dependent pathway arose in bilateria, so that IBD is placed deeper than the
  pathway's origin. The node placement is the root cause, not just term scoping. The propagation_review
  root_cause (TERM_SCOPING_PROBLEM) was left unchanged.
- Slime mold STATs lack the transactivation and N-terminal domains [PMID:24058748 "However, they lack the N-terminal and transactivation domains characteristic of STAT proteins from higher organisms"].
- Kawata 2011 (PMID:21534947, abstract only) added to both GO:0031154 culmination IMP rows and to the culmination core function [PMID:21534947 "The Dd-STATa null mutant displays delayed aggregation, no phototaxis and fails culmination."].
- The description's phrase "canonical STAT domain architecture" is in tension with these reviews, because Dd-STATa lacks the N-terminal and transactivation domains. The description was not edited.
- No actions changed.

Cross-gene briefing for GO editors and PAINT curators: https://claude.ai/artifact/4MLfbbbWWnLchDvspwdPuM
