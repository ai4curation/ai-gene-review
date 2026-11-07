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
