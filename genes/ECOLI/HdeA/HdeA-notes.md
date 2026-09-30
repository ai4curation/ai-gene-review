# HdeA qualifier-aware annotation re-review — 2026-08-29

## Coverage and provenance

- Reconciled all 14 current physical GOA signatures exactly once: 6 `enables`, 4 `located_in`, 3 `involved_in`, and 1 `acts_upstream_of_or_within`.
- Evidence distribution is 4 IEA, 5 IDA, 2 EXP, 1 IPI, 1 IMP, and 1 RCA, totaling 14 physical rows. There are no IBA rows and therefore no PTN/WITH-FROM propagation claim to audit.
- All six GOA PMID sources are abstract-only in the repository cache. Experimental rows were retained or refined only where their cached abstracts directly support the interpretation; none was removed for lack of full text.

## Holdase and ontology decision

HdeA is an ATP-independent, acid-activated in-situ holdase. At neutral pH it is an inactive folded dimer; below pH 3 it becomes a disordered client-binding monomer. [PMID:15911614 “it possesses an ordered conformation that is unable to bind denatured substrate proteins under normal physiological conditions (i.e. at neutral pH) and transforms into a globally disordered conformation that is able to bind substrate proteins under stress conditions (i.e. at a pH below 3)”]

No cached study demonstrates escort to a defined acceptor molecule or destination. HdeA binds clients within the periplasm, prevents aggregation, then releases them when pH is neutralized. Therefore carrier-specific GO:0140309 does not fit. The physical GO:0051082 IDA row is retained as an interim annotation but `MODIFY` now points machine-readably to `NTR` holdase chaperone activity, following the CRYAA/project convention. [file:projects/UNFOLDED_PROTEIN_BINDING.md]

GO:0050821 protein stabilization is added as a NEW BP because aggregation suppression is direct: “Functional studies demonstrate that HDEA is activated by a dimer-to-monomer transition at acidic pH, leading to suppression of aggregation by acid-denatured proteins.” [PMID:10623550]

## Refolding decision

GO:0042026 protein refolding is retained as the replacement for the broad physical GO:0006457 protein folding row. The BP does not imply that HdeA catalyzes folding chemistry. PMID:20080625 directly states that HdeA “is capable of independently facilitating the refolding of acid-denatured proteins” and explains that slow release keeps aggregation-sensitive intermediates below their aggregation threshold. This supports involvement in refolding through an environmentally regulated binding-release cycle.

The three experimental GO:0044183 protein folding chaperone rows are retained. Although HdeA is mechanistically a holdase, the direct evidence shows that its binding-release cycle assists the folding process. The core-function prose now separates this refolding assistance from the primary in-situ aggregation-prevention activity.

## Other annotation decisions

- GO:0042802 identical protein binding remains `MARK_AS_OVER_ANNOTATED` because the specific physical GO:0042803 homodimerization activity is present and experimentally supported.
- Broad and specific periplasm/local acid-response rows remain accepted; their exact GOA qualifiers are now explicit in YAML.
- The standalone description remains biological and project-independent, covering compartment, pH-dependent activation, aggregation prevention, controlled release, and cooperation with HdeB/DegP/SurA.

## PR #2740 follow-up — 2026-08-29

- Revised the GO:0006457 `MODIFY` rationale to describe the parent term as too general and uninformative about HdeA's demonstrated pH-triggered refolding mechanism, while retaining GO:0042026 and the distinction between process involvement and folding catalysis.
- Narrowed the PMID:9298646 and PMID:9731767 reference-review notes to claims visible in their abstract-only caches. `correctness: VERIFIED` remains appropriate for verified citation identity and the explicitly available abstract claims; it does not assert verification of inaccessible full-text assay details.

## PR #2741 follow-up — 2026-08-29

- Anchored the PMID:9298646 signal-peptide claim to the UniProt record's `PROTEIN SEQUENCE OF 22-33` attribution and `SIGNAL 1..21` feature, while keeping the abstract's limited subcellular-location wording separate and not treating it as HdeA-specific compartment proof.
- Recorded that the cached PMID:9731767 entry contains no result-bearing abstract, whereas UniProt explicitly attributes 2.2-A crystallography and the Cys39-Cys87 disulfide to that PMID.
- Simplified the GO:0006457 BP rationale to the specificity argument: the parent is too general, GO:0042026 captures the demonstrated neutralization-triggered refolding process, and this does not imply that HdeA catalyzes folding chemistry.
