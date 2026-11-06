# betA (E. coli K-12, P17444) notes

## Sources read (2026-11-03)
- Cached abstracts: PMID:3512525, PMID:3512526, PMID:8626294, PMID:1956285, PMID:3065456, PMID:39510372 (fetched this session).
- Deep research: `just deep-research-falcon` failed (403, API key rejected); `just deep-research-openscientist ECOLI P17444 --alias betA` succeeded and produced `betA-deep-research-openscientist.md`. Its key new lead, PMID:39510372, was fetched and checked.

## Findings
- Crude membranes: "A membrane-bound, O2-dependent, and electron transfer-linked dehydrogenase was found which oxidized choline to glycine betaine aldehyde and aldehyde to glycine betaine at nearly the same rate." [PMID:3512525]
- The NAD-dependent aldehyde oxidation is a separate soluble enzyme (BetB): "Also, a soluble, NAD-dependent dehydrogenase oxidized glycine betaine aldehyde." [PMID:3512525]
- Purified enzyme: "highly pure E. coli CHDH could only oxidize choline to betaine aldehyde but failed to further oxidize betaine aldehyde to betaine" [PMID:39510372]
- Mutants: "Mutants blocked at the level of choline dehydrogenase were isolated by selection of strains which did not grow at elevated osmotic strength in the presence of choline but grew when supplemented with glycine betaine." [PMID:3512526]

## Decisions
- GO:0008812 is the core function; plasma membrane (peripheral) is the location; GO:0031456 is added as NEW (IMP, PMID:3512526).
- GO:0008802 (NAD+ betaine-aldehyde dehydrogenase) IEA is REMOVED. It is NAD-specific, BetA's acceptor is respiratory, and purified BetA lacks the activity. UniProt P17444 attributes BetB's NAD kinetics to BetA; recorded as source_defects. The same call is applied to P. putida BetA (Q88CW6), which gets the same HAMAP MF_00750 propagation.
- Generic rows (membrane, GO:0016614) are MODIFIED to the specific terms the gene carries.
- Osmotic-stress IEP/IMP rows are non-core.


## 2026-11-06 comparative choline/betaine module audit

Retained choline dehydrogenase and rejection of the electronic NAD-specific aldehyde reaction. The original source explicitly separates membrane electron-transfer activity from soluble NAD-dependent aldehyde oxidation. The 2024 purified Ecoli preparation failed to oxidize aldehyde under the tested conditions; its accessible abstract does not establish exact strain/accession or all assay conditions. The 2022 Acinetobacter full publisher article uses PMS, not NAD. Removed the categorical FAD/no-NAD inference; retained source-defect flags and the inherited glycine-betaine process proposal.

Existing genuine OpenScientist research was inspected and preserved; no replacement provider report was authored.

All original machine row fields and raw UniProt/GOA files were preserved, with inherited NEW assertions tracked separately from this audit (zero added rows). The six-target baseline has 55 rows, three inherited NEW, twelve raw-file hashes and four provider-report hashes. Reusable check: `.cache/module-audit-logs/choline-betaine-20261106/check-original-six.py`; report `original-six-preservation.json`. Focused gene validation passed with no curation warnings. Ecoli BetT/BetA/BetB PAINT loss checks found no IRD/IKR. Status remains COMPLETE because review decisions are complete; unresolved biological/source claims are explicitly qualified.

Normal force-fetches of PMIDs39510372,34431198,3512525,3512526,2194570,17322201,27718375,26913973 did not recover full text; the first fetch of PMID18156257 also remained abstract-only. PMID34431198 full publisher text was read externally (https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.15741), including assay methods and preparation purity. Source distinctions: A. baumannii ATCC19606 HMPREF0010_01460 with a recombinant His tag; PMS serves as primary acceptor and oxygen measures its reoxidation. These data are comparative, not assays of either original BetA target. No publication cache was manually edited.

## PR6108 round1 evidence and ontology follow-up

The PMID3512525 finding now states the older crude-membrane dual-substrate observation rather than omitting its second reaction. A finding_review marks attribution of that second reaction to BetA DISPUTED and links PMID39510372 purified-enzyme evidence. OVERTURNED would exceed the accessible strain/assay comparison; the original observation and separate soluble BetB NAD kinetics remain distinct. Added the missing ontology question for hypothetical acceptor-linked betaine-aldehyde oxidation, without asserting this unresolved BetA capability.

All original machine and authored annotation payloads remain unchanged. Exact primary excerpts and source provenance are in BACSU/gbsB/gbsB-source-analysis/round1-primary-excerpts.txt; official term checks are in modules/bacterial_choline_to_glycine_betaine_biosynthesis-source-analysis/round1-ontology-evidence.yaml.
