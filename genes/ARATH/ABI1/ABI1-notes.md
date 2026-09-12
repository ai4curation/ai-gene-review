# ABI1 re-review, 2026-09-11

Reviewed all 56 existing annotation rows against the cached publications, UniProt and existing Falcon research. PubMed and full-text searches were used for ambiguous claims. Publication caching recovered 41/41 existing references. New Falcon research with perplexity-lite fallback was launched; provider status is recorded below when complete.

The phosphatase/ABA mechanism is grounded in direct literature rather than synthetic descriptions of research or PANTHER files. [PMID:8898906, "Mg2+ or Mn2+ dependence"] [PMID:19924127, "the SnRK2 kinases are kept inactive by the PP2Cs through physical interaction and dephosphorylation."] SnRK1 and MAPKKK18 extend the signaling substrate scope [PMID:24179127; PMID:26443375].

The REMOVE decision for PMID:17267444 was withdrawn: an abstract about SCAR/WAVE does not establish a gene-name mapping error. Search results point to divergent ABI/ABIL naming, but assay construct identity remains unverified. The row is UNDECIDED. This also applies to interaction-map rows whose specific interaction tables were unavailable.

The 1991 cold study reports "Cold-regulated expression of all three cor genes, however, was nearly the same in wild-type and abi1 mutant plants." [PMID:1834244]. Its row is UNDECIDED pending full context; the independent 1995 cold-response result remains non-core [PMID:12228349].

Early calcium-binding assertions were sequence predictions [PMID:7910981; PMID:8197457]. Later experiments question physiological EF-hand regulation [PMID:8898906]. The calcium annotations remain over-annotated with an evidence-based rationale. Broad cation binding is retained non-core because magnesium/manganese dependence is experimentally established. The broad PAINT signaling-regulation annotation is accepted; target-specific ABA evidence does not invalidate an ancestral broad function.

Specific citations and snippets were added only where the accessible text supports the assertion. IEA mappings use cited rationale without mandatory snippets. Several abstracts do not expose the ABI1-specific assays; those rows retain explicit uncertainty rather than invented supporting quotations.

Falcon research refresh completed successfully and generated an updated report plus provider artifacts. Its synthesis confirms the PP2C/SnRK2 mechanism and flags kinase-side osmotic regulation as context; no unverified new experimental annotations were added from that synthesis. The refresh of PMID:24179127 recovered full text confirming ABI1-SnRK1.1 interaction and phosphatase activity. Proposed replacement GO identifiers were checked with QuickGO and match current labels. Removed the obsolete failure-classification block from the now-accepted PAINT annotation instead of retaining an unsupported evolutionary defect claim.
