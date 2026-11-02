# ptk1 (O74962, SPBC4B4.01c) notes

Role: type II pantothenate kinase (EC 2.7.1.33); module `coenzyme_a_biosynthesis`.
Fetch: `just fetch-gene SCHPO ptk1` FAILED (no UniProt gene name: "PomBase; SPBC4B4.01c; -."); refetched with `-u O74962`.
Naming trap: S. cerevisiae PTK1 (YKL198C) is an unrelated polyamine-transport protein kinase; the budding-yeast ortholog of S. pombe ptk1 is CAB1.

## Evidence
- [PMID:23091701 "For comparison, the genes for SPBC4B4.01c/Ptk1 (designated Ptk1, PANK)"]; no direct activity assay in S. pombe.
- [UniProt:O74962 "SIMILARITY: Belongs to the type II pantothenate kinase family."]
- Localisation whole cell [PMID:23091701 "The GFP signals of both Ppc1 and Ptk1 were observed in the whole cell (figure 4e), whereas Acs1 was enriched in the nuclear chromatin."]
- PANTHER: UniProt assigns PTHR12280:SF20 whose name is "4'-PHOSPHOPANTETHEINE PHOSPHATASE" (PANK4-type name); S. cerevisiae CAB1 is in the same subfamily, and ptk1 (403 aa) lacks the PANK4 C-terminal DUF89 phosphatase domain, so this is a subfamily-naming quirk, not evidence of phosphatase function.

## Decisions
- Nucleus (HDA/IBA/IDA/IEA) and ATP binding non-core; everything else accepted.
- Core: GO:0004594 / GO:0015937 / GO:0005829 — matches S. cerevisiae CAB1 review and both PomBase GO-CAMs.
