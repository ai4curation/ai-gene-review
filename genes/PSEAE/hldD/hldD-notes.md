# hldD research notes

## 2026-10-25 — complete annotation and evidence audit

Applied the review and annotation-reviewer instructions to every seeded row. Source fields were preserved and a JSON comparison checked that only annotation review blocks changed. Correct broad terms were refined with MODIFY, not treated as false or excessive claims. No new process annotations were added.

Research provenance: the actual `just deep-research-falcon ECOLI hldE --fallback perplexity-lite` run was launched concurrently with publication caching. Falcon/Edison returned HTTP 403 authentication failure; the Perplexity fallback returned HTTP 401 insufficient_quota. This session-wide provider outage applies to this four-gene audit; these notes are manual primary-source research, not a provider-generated report. Existing and additional publication caches were fetched with supported commands; no publication cache was hand-edited.

`just fetch-fitness PSEAE hldD` was attempted and failed because no local FEBA data or reachable data source was available; no fitness artifact was written. PSEAE additionally lacks an organism mapping in the fetcher. No fitness phenotype is inferred from that failure.

Identity verified directly from UniProt: Q9HYQ8, PA3337, hldD/rfaD, Pseudomonas aeruginosa PAO1, NCBITaxon208964. Seeded with `just fetch-gene PSEAE hldD`; all 7 rows reviewed. Exact epimerase, NADP binding and ADP-L,D-heptose/LPS core pathway claims are retained; generic carbohydrate metabolism is refined to the specific pathways.

A direct purified PA3337 biochemical experiment was not located. The review therefore explicitly grounds target activity in HldD-specific HAMAP MF01601, InterPro IPR011912, conserved active-site/NADP-binding features and PAINT inference, rather than relabelling an E. coli or generic HldD paper as a Pseudomonas experiment. PANTHER placement verified from UniProt: PTHR43103:SF3, ADP-L-GLYCERO-D-MANNO-HEPTOSE-6-EPIMERASE.

Curated UniProt function quote: “Catalyzes the interconversion between ADP-D-glycero-beta-D-manno-heptose and ADP-L-glycero-beta-D-manno-heptose via an epimerization at carbon 6 of the heptose.” This is HAMAP-supported conservation, not ARBA or a protein-name/EC restatement. PMID15264802 and PMID17455913 establish family mechanism using isotope and substrate analog experiments, but are abstract-only in the cache and do not identify PA3337 as an assayed target. PMID17455913 states: “An initial oxidation at C-6'' gives a 6''-keto intermediate, and a subsequent reduction on the opposite face of the carbonyl group generates the epimeric product.” NADP is tightly bound and recycled, not a net substrate.

The reaction changes the **glycero C6** stereochemistry from D,D to L,D while retaining the beta anomeric nucleotide linkage. Thus the product of HldE is ADP-D,D-heptose and the product needed for the conventional Pseudomonas LPS inner core is ADP-L,D-heptose. HldD does not establish ADP-D,D biosynthesis alone and its role must remain distinct from pathways terminating at D,D or from GDP-alpha-heptose routes.
