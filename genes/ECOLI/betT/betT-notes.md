# betT (E. coli K-12, P0ABC9) notes

## Sources read (2026-11-03)
- Cached abstracts: PMID:1956285, PMID:17322201 (fetched), PMID:3512526, PMID:15919996, PMID:11967071.
- Deep research: falcon failed (403); `just deep-research-openscientist ECOLI P0ABC9 --alias betT` produced `betT-deep-research-openscientist.md`, consistent with the review (proton-driven, high-affinity, osmo-activated choline carrier); cited on the MF row.

## Findings
- "betT encoding a proton-motive-force-driven, high-affinity transport system for choline" [PMID:1956285]
- 12 TM segments, cytoplasmic termini; osmotic upshock raises activity tenfold; the C-terminal domain is needed for activation [PMID:17322201].

## Decisions
- Core: GO:0015220 choline transmembrane transporter activity, GO:0015871 choline transport, plasma membrane.
- BCCT-family generic rows (GO:0022857, GO:0055085, GO:0016020) are MODIFIED to the specific terms. GO:0055085 -> GO:0015871 is lateral, because GO has no choline transmembrane transport term.
- The DNA damage response IEP (mitomycin microarray) is over-annotated.
- PANTHER PTHR30047:SF7 is not choline-specific (it also holds BetP, OpuD, BetL, EctP, TmaT), so neither the family nor that subfamily can define a choline-uptake selector.


## 2026-11-06 comparative choline/betaine module audit

Accepted the true transmembrane-transport process alongside choline transport; no lateral replacement drops the membrane-crossing claim. Recovered the full published PMID11967071 article and verified Table1 b0314/betT in MMC-induced cluster U2. GO0006974 explicitly includes expression responses, so retained this existing IEP claim as non-core context rather than labeling the observed response a by-product. This does not imply DNA-repair activity. Clarified that the global topology study target supplement was not inspected, while BetT-specific topology corroborates its location.

Existing genuine OpenScientist research was inspected and preserved; no replacement provider report was authored.

All original machine row fields and raw UniProt/GOA files were preserved, with inherited NEW assertions tracked separately from this audit (zero added rows). The six-target baseline has 55 rows, three inherited NEW, twelve raw-file hashes and four provider-report hashes. Reusable check: `.cache/module-audit-logs/choline-betaine-20261106/check-original-six.py`; report `original-six-preservation.json`. Focused gene validation passed with no curation warnings. Ecoli BetT/BetA/BetB PAINT loss checks found no IRD/IKR. Status remains COMPLETE because review decisions are complete; unresolved biological/source claims are explicitly qualified.

Normal force-fetches of PMIDs39510372,34431198,3512525,3512526,2194570,17322201,27718375,26913973 did not recover full text; the first fetch of PMID18156257 also remained abstract-only. PMID34431198 full publisher text was read externally (https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.15741), including assay methods and preparation purity. Source distinctions: A. baumannii ATCC19606 HMPREF0010_01460 with a recombinant His tag; PMS serves as primary acceptor and oxygen measures its reoxidation. These data are comparative, not assays of either original BetA target. No publication cache was manually edited.

The committed source artifact is the verbatim betT table-row excerpt and retrieval provenance. The complete retrieved PDF and text are retained in the local audit cache; the curation decision and original annotation payload are unchanged.

## PR6108 round1 evidence and ontology follow-up

Current QuickGO ancestry confirms the existing ACCEPT decision for GO0055085. Choline transport is a separate cargo process, and the search found no appropriate choline-specific transmembrane-transport BP descendant. GO0015220 remains the specific MF. OpuB reviews are brought into the same interpretation.

All original machine and authored annotation payloads remain unchanged. Exact primary excerpts and source provenance are in BACSU/gbsB/gbsB-source-analysis/round1-primary-excerpts.txt; official term checks are in analysis/module_audits/bacterial_choline_to_glycine_betaine_biosynthesis/round1-ontology-evidence.yaml.
