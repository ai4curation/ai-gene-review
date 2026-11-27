# SUR1 (At2g20610, Q9SIV0) review notes

## Summary of biology
- PLP-dependent C-S lyase of core glucosinolate biosynthesis [PMID:14871316 "We report characterization of SUPERROOT1 (SUR1) as the C-S lyase in glucosinolate biosynthesis."]; sur1 "is completely devoid of aliphatic and indole glucosinolates"; recombinant enzyme active on djenkolic acid.
- High-auxin superroot phenotype is indirect: [PMID:14871316 "the \"high-auxin\" phenotype of sur1 is caused by accumulation of endogenous C-S lyase substrates as well as aldoximes, including indole-3-acetaldoxime (IAOx) that is channeled into the main auxin indole-3-acetic acid (IAA)"]. Original mutant: [PMID:8589625 "increased levels of both free and conjugated indole-3-acetic acid"].
- 2026 update: sur1 still makes significant indolic GLs, so an additional C-S lyase exists; auxin excess in sur1 depends on MYB34 [PMID:41819465].
- Family: PTHR45744 (tyrosine aminotransferase), subfamily SF15 (SUR1). SUR1-like Taraxacum C-S lyase lacks TyrAT activity but has AlaAT activity [PMID:23073363 "we detected no in vitro tyrosine aminotransferase (TyrAT) activity"].

## Decisions
- S-alkylthiohydroximate lyase (IMP), C-S lyase (IDA), glucosinolate biosynthesis (IMP), cytosol, cytoplasm, PLP binding -> ACCEPT.
- IAA biosynthesis (IMP), adventitious root development (TAS), regulation of cell growth by extracellular stimulus (IMP) -> MARK_AS_OVER_ANNOTATED: indirect consequences of IAOx shunting; SUR1 performs no step in these processes. Not REMOVE because experimental/abstract-only.
- TAT activity IBA -> MARK_AS_OVER_ANNOTATED; L-tyrosine catabolic process IBA -> REMOVE (neofunctionalized subfamily, no Tyr-catabolism phenotype). propagation_review: PROPAGATION_BAD / FUNCTIONAL_DIVERGENCE.
- transaminase activity IEA -> MODIFY to GO:0080108. amino acid metabolic process IEA -> MARK_AS_OVER_ANNOTATED.
- protein binding IPI -> REMOVE (uninformative).
- mitochondrion HDA -> MARK_AS_OVER_ANNOTATED.
- defense response to fungus IDA (PMID:32213638) -> UNDECIDED: cited paper is about ODR1/bHLH57 seed dormancy; abstract-only, no full text retrievable from Europe PMC; cannot verify.
- No NEW terms.

## 2026-10-15 journal: defense response to fungus row resolved (PR #5026 follow-up)

Supersedes the "-> UNDECIDED ... abstract-only, no full text retrievable" line above.

- Full text now cached: `ai-gene-review fetch-pmid PMID:32213638 --force` on 2026-10-15 retrieved PMC7268807 (publisher restricts the PMC XML; the pipeline's HTML fallback succeeded; `full_text_available: true`, `full_text_extraction_method: html`).
- A search of the cached full text for SUR1, SUPERROOT, At2g20610, glucosinol, fung and pathogen returns no hits. The Accession Numbers section lists every gene studied: ODR1, ABI3, bHLH57, NCED2/3/5/6/9, CYP707A1-4, ABI4, DREB2C, TTG1, MYB5, DOG1, RDO5 and PP2A; At2g20610 is absent.
- Query (re-run 2026-10-15): QuickGO REST, `https://www.ebi.ac.uk/QuickGO/services/annotation/search?reference=PMID:32213638&limit=200` returned 1 annotation: SUR1 (Q9SIV0) GO:0050832 IDA acts_upstream_of_or_within, assigned by TAIR; nothing for ODR1 or bHLH57.
- Action: GO:0050832 IDA is REMOVE (unsupported by its reference; likely a mis-keyed reference in the TAIR record). Supporting quote from the accession list added to the row; the reference is now marked MISCITED, and a suggested question asks TAIR which paper was intended. This does not deny an indirect role of SUR1-derived indole glucosinolates in antifungal defense.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (17) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

PMID14871316 combines in vivo feeding/intermediate accumulation with recombinant djenkolic-acid cleavage, not a demonstrated purified native Cys-Gly assay. GGP1-to-SUR1 handoff is qualified using21712415. PMID41819465 reports significant residual indolic glucosinolates, so neither description nor core asserts universal sole-enzyme necessity. Tyrosine-catabolism removal was too confident about target-specific evolutionary loss; now over-annotated, without treating Taraxacum lack of TyrAT activity as proof for Arabidopsis. The C-S lyase class term is refined to the existing specific activity.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.
