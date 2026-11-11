# Elovl7 review notes

## Evidence summary
- [UniProtKB:D4ADY9] UniProt describes Elovl7 as an ER-bound condensing enzyme that adds two carbons per cycle during long-chain fatty acid elongation.
- [UniProtKB:D4ADY9] The entry records fatty acid elongase activity and ER membrane localization mostly from HAMAP/by-similarity evidence; no rat PMID was present in the fetched GOA references.

## Curation decisions
- Core function: very-long-chain fatty acid elongase 7 (fatty acid elongase activity, GO:0009922).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-10

GOA changes: two new IBA rows from the ELO family node PTN000125390 (GO:0009922 fatty acid elongase activity; GO:0042761 very long-chain fatty acid biosynthetic process). One row retired: GO:0008610 lipid biosynthetic process (IEA, GO_REF:0000117), review kept with a retirement note. 25 rows total; no rat-specific primary literature in GOA (all evidence is IBA/ISO/IEA, the ISO donor being human ELOVL7, UniProtKB:A1L3X0).

- PENDING resolved: IBA fatty acid elongase activity ACCEPT (core, conserved ELO-family activity); IBA VLCFA biosynthetic process KEEP_AS_NON_CORE, matching the IEA/ISO rows for that term.
- GO:0005789 endoplasmic reticulum membrane (IBA, IEA, ISO): KEEP_AS_NON_CORE -> ACCEPT. The ER membrane is where the condensing step happens [UniProtKB:D4ADY9 "This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle."]; added as the core-function location.
- VLCFA biosynthetic process rows: kept non-core with an explicit rationale. GO defines VLCFA as more than 22 carbons, and ELOVL7 has [UniProtKB:D4ADY9 "Little or no activity toward C22:0-, C24:0-, or C26:0-CoAs."].
- Sphingolipid biosynthetic process (IBA): kept MARK_AS_OVER_ANNOTATED (target-specific divergence: C18-preferring substrate range); replaced its stale `DR GO` quote with the UniProt substrate-range line.
- Replaced all circular or stale `DR GO;` supporting quotes (3 stale, about 15 circular) with UniProt FUNCTION/SUBCELLULAR LOCATION/PATHWAY lines and deep-research quotes; rewrote boilerplate reasons into term-specific ones.
- Description rewritten as standalone biology; core function now lists ER membrane location and the monounsaturated elongation process. Status COMPLETE.

Open question: no rat-specific biochemistry exists; substrate specificity is inferred from human ELOVL7 (Naganuma et al. 2011, per deep research).
