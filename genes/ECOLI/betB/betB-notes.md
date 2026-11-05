# betB (E. coli K-12, P17445) notes

## Sources read (2026-11-03)
- Cached abstracts: PMID:2194570, PMID:3512525, PMID:3512526, PMID:3065456, PMID:27718375, PMID:39510372; PMID:18304323 (full text, per-protein table not included).
- Deep research: falcon failed (403, key rejected); `just deep-research-openscientist ECOLI P17445 --alias betB` produced `betB-deep-research-openscientist.md`, which agrees with the review (soluble cytoplasmic, K+-dependent homotetramer) and is cited on the cytosol row.

## Findings
- "The dehydrogenase was found to be a tetramer with identical 55 kDa subunits." "The dehydrogenase was highly specific for betaine aldehyde." [PMID:2194570]
- Soluble, NAD-dependent aldehyde oxidation, separate from the membrane choline dehydrogenase [PMID:3512525].
- Purified BetA cannot oxidize betaine aldehyde [PMID:39510372], so BetB is the dedicated second-step enzyme.
- PANTHER: PTHR11699:SF228 (4-TRIMETHYLAMINOBUTYRALDEHYDE DEHYDROGENASE), shared with vertebrate ALDH9A1.

## Decisions
- Core: GO:0008802, GO:0031456, cytosol.
- Generic oxidoreductase and metal ion binding rows are MODIFIED (to GO:0008802 and GO:0030955 potassium ion binding).
- Tetramer rows non-core; osmotic-stress IEP rows non-core; X-ray screen hit over-annotated.
