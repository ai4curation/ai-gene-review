# ACTN1 curation notes

## 2026-11-25 — evidence and scope

ACTN1 (HGNC:163; UniProt P12814) encodes alpha-actinin-1, an actin-filament crosslinker and adhesion-associated structural protein. Native acquisition yielded 136 GOA rows and 128 distinct seeded annotation contexts; eight rows collapse under the deterministic seeder's complete source key. The review retains the original term, evidence, reference, partner and negation fields. In particular, the two native NOT annotations remain identifiable.

The [source guide](ACTN1-source-guide.md) records the primary experiments, access limits and isoform distinctions. Actin crosslinking is a direct biochemical activity. Platelet size and proplatelet-tip organization are physiological consequences of that structural activity; the disease studies do not establish that normal ACTN1 universally prevents platelet activation or aggregation. The experiments also do not show that every disease variant abolishes calcium regulation or increases actin association to the same degree.

ACTN1 splice variants have different calcium-binding properties. The isolated-domain affinities in PMID:26020004 and PMID:27272015 are not intracellular activation thresholds. Manuscript names and residue numbering are retained in the evidence discussion without silently mapping them onto every current UniProt isoform.

The postsynaptic study PMID:29429936 directly tests alpha-actinin-1, including purified-protein interactions and rescue with PSD-95-binding mutants after combined alpha-actinin-1/-2/-4 depletion. It supports a structural anchoring function in that experimental setting; it does not establish ACTN1 as the only neuronal alpha-actinin. Likewise, articles centered on ACTN4, ACTN2 or another interacting protein are not grounds for rejecting an ACTN1 annotation without checking their experiments.

Supported generic protein-binding annotations follow the standing ClinGen instruction: retain correct interaction evidence as non-core when a more specific molecular activity has not been established. Complex copurification does not prove direct binary binding. When an independent study verifies the same interaction, retain the supported claim while recording the original source-access limit separately; otherwise leave unadjudicated interactions unresolved. Broad terms are refined only when the original row's own evidence supports the refinement.

Falcon deep research failed authentication and the Perplexity-lite fallback reported insufficient quota. Research therefore continued through primary articles, cached publications and manual source inspection. No manual text is labelled as provider-generated output.

The native publication cache was materialized from Git before seeding, preserving existing evidence. A bounded native full-text retrieval subsequently expanded PMID:11101506, PMID:20120020 and PMID:22351778; their previous versions are recoverable under `refs/recovery/clingen-actn1-20261125/pre-warm-four-v1`. The cache's full-text flag is not treated as proof that all Methods, Results or supplementary tables are present. PMID:21266579 requires particular care because its cached extraction omits key experimental sections.

The PANTHER 19.0 family tree places P12814 at PTN002539723. All eight native IBA term/node combinations match the retained PAINT IBD assertions and lie on this lineage. No IRD, IKR or NOT assertion was found on the lineage. This is an audit of the retained PAINT snapshot, not a new phylogenetic analysis. An ACTN1 descendant appearing among the supporting sources is legitimate experimental grounding, not circularity. The GO-CAM index at the review base has no P12814 entry; that absence is not evidence for adding a process annotation.

The existing registered sparse Orca checkout and retained runtime are reused. ROOT is the only writer of curated files; three read-only helpers propose reviews for disjoint annotation ranges. There is no copied checkout or per-gene environment. Validation uses project code from this checkout without synchronizing the retained environment. The retained Python and dependency versions differ from the current lock, so local checks and the PR's current-environment CI are reported separately.

ACTN1 receives no campaign completion credit until its own review, validation and delivery are verified.

Cross-review distinguishes an uninspected original experiment from an unresolved biological claim. The exact ACTN1–C14orf119 pair is independently supported by HuRI and is retained without claiming inspection of its OpenCell experiment. Verified PAINT ancestry supports non-core Z-disc and enclosing sarcomere locations; the inspected Reactome ACTN1 entity supports non-core alpha-granule-lumen cargo localization. Original assay and peptide-table access limits remain explicit. No source-defect or wrong-paralog finding is inferred from those limits.
