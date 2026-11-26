# XBP1 (human, P17861) review notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable).
Review based on cached GOA-cited publications and the UniProt entry.

## Key findings
- Spliced XBP1 is the active UPR transcription factor
  [PMID:11779464 "only the spliced form of XBP1 can activate the UPR efficiently"]
- bZIP DNA binding/transactivation of CRE-like elements [PMID:8657566]; c-Fos heterodimer [PMID:1903538].
- XBP1u is a negative feedback regulator [PMID:16461360 "pXBP1(U) is a negative feedback regulator of pXBP1(S)"], has a type II TMD cleaved by SPP [PMID:25239945].
- ATF6-XBP1 heterodimers induce ERAD components [PMID:17765680].
- Required for plasma cell differentiation [PMID:11460154].

## Curation decisions
- Many ISS transfers from mouse (metabolism, development, physiology) kept as non-core.
- bZIP array protein binding -> MODIFY to heterodimerization; identical protein binding -> homodimerization.
- ERAD quality control pathway -> MODIFY to GO:1904294 positive regulation of ERAD pathway.
- `positive regulation of T cell differentiation` (PMID:11460154, abstract only) -> UNDECIDED.
- NEW: GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (MF refinement).
