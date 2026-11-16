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


## 2026-11-06 comparative choline/betaine module audit

Retained NAD-dependent aldehyde oxidation, cytosolic location and the biosynthetic core. NADP use is measured, but NAD is preferred; this is not a reason to transfer NAD chemistry to BetA. Potassium-binding refinement rests on the curated HAMAP assignment rather than high-K salt tolerance alone. Changed the X-ray response row to UNDECIDED: the abstract names betB among radiation-sensitive mutants but does not resolve its individual UV/X-ray result or controls, and full target-level evidence remained unavailable.

Existing genuine OpenScientist research was inspected and preserved; no replacement provider report was authored.

All original machine row fields and raw UniProt/GOA files were preserved, with inherited NEW assertions tracked separately from this audit (zero added rows). The six-target baseline has 55 rows, three inherited NEW, twelve raw-file hashes and four provider-report hashes. Reusable check: `.cache/module-audit-logs/choline-betaine-20261106/check-original-six.py`; report `original-six-preservation.json`. Focused gene validation passed with no curation warnings. Ecoli BetT/BetA/BetB PAINT loss checks found no IRD/IKR. Status remains COMPLETE because review decisions are complete; unresolved biological/source claims are explicitly qualified.

Normal force-fetches of PMIDs39510372,34431198,3512525,3512526,2194570,17322201,27718375,26913973 did not recover full text; the first fetch of PMID18156257 also remained abstract-only. PMID34431198 full publisher text was read externally (https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.15741), including assay methods and preparation purity. Source distinctions: A. baumannii ATCC19606 HMPREF0010_01460 with a recombinant His tag; PMS serves as primary acceptor and oxygen measures its reoxidation. These data are comparative, not assays of either original BetA target. No publication cache was manually edited.
