# DGAT1 / TAG1 (diacylglycerol O-acyltransferase 1) — Arabidopsis thaliana — review notes

UniProt: Q9SLD2 · At2g19450 · EC 2.3.1.20 · Taxon 3702
Relevance: terminal committed step of seed-oil (TAG) assembly — a premier DOE/BER
oilseed yield-engineering target.

## Core function
- **Acyl-CoA:diacylglycerol acyltransferase 1**: catalyzes the terminal, committed step
  of the acyl-CoA-dependent (Kennedy) pathway of TAG assembly — transfer of an acyl group
  from acyl-CoA to the sn-3 position of diacylglycerol (DAG) to form triacylglycerol (TAG).
  [file:ARATH/DGAT1/DGAT1-deep-research-falcon.md; PMID:10386579; PMID:11171171]
- Multi-pass ER membrane protein of the **MBOAT** family (~8-10 TM segments).
  [file:ARATH/DGAT1/DGAT1-deep-research-falcon.md]
- Major microsomal DGAT in seeds/pollen; tag1/dgat1 mutants lose most microsomal DGAT
  activity (WT ~116-201 vs tag1 ~2-8 nmol/mg/min) and have reduced seed oil (dgat1-1 ~75%,
  dgat1-2 ~55% of WT). Functionally redundant with PDAT1 (acyl-CoA-independent route);
  dgat1 + PDAT1 knockdown drops TAG ~70-80%. [PMID:10601854; PMID:10571850;
  file:ARATH/DGAT1/DGAT1-deep-research-falcon.md]

## Localization
- **Endoplasmic reticulum membrane** (microsomal), the functional site of TAG synthesis;
  also lipid-droplet associated (ER-LD interface). [IBA; EXP/IDA; PMID:24663078]
- Spurious / non-functional localizations to address:
  - GO:0005634 nucleus (ISM, AtSubP) -> REMOVE (sequence-model artifact; same as FAE1/FAD2)
  - GO:0031969 chloroplast membrane (IEA, UniProt SL mapping) -> REMOVE (electronic
    propagation of a contested localization; no functional support)
  - GO:0009941 chloroplast envelope (IDA, PMID:12177474) -> MARK_AS_OVER_ANNOTATED:
    detected in a chloroplast-envelope proteomics survey, almost certainly co-purifying
    ER contamination; DGAT1 is functionally an ER enzyme.

## Pleiotropy (KEEP_AS_NON_CORE)
A single mutant-phenotype study (PMID:12114588) generated many indirect BP annotations via
`acts_upstream_of_or_within`: carbohydrate metabolic process, response to cold/salt/ABA/
glucose, embryo development ending in seed dormancy. These reflect the downstream
physiological consequences of disrupting seed oil storage / carbon partitioning, not
DGAT1's molecular activity -> KEEP_AS_NON_CORE. Likewise seed-germination and embryonic-
development regulation (PMID:10580283, PMID:11402213) are pleiotropic -> KEEP_AS_NON_CORE.
GO:0005515 protein binding (IPI) is uninformative per curation guidance -> KEEP_AS_NON_CORE.

## Annotation review summary
- GO:0004144 diacylglycerol O-acyltransferase activity (EXP/IDA/IMP/ISS/IEA, x8) -> ACCEPT (core MF)
- GO:0019432 triglyceride biosynthetic process (IDA/IMP/TAS/IEA, x5) -> ACCEPT (core BP)
- GO:0005789 ER membrane (IBA/IEA) -> ACCEPT (core location)
- GO:0016020 membrane (IDA/TAS) -> ACCEPT (general location)
- GO:0005811 lipid droplet (IDA) -> KEEP_AS_NON_CORE
- chloroplast membrane (IEA) -> REMOVE; chloroplast envelope (IDA) -> MARK_AS_OVER_ANNOTATED
- nucleus (ISM) -> REMOVE
- seed-germination / embryonic-development / stress-response / carbohydrate BPs -> KEEP_AS_NON_CORE
- protein binding (IPI) -> KEEP_AS_NON_CORE

## DOE/BER relevance
DGAT1 overexpression raises DGAT activity (~10-70%), seed weight, and oil content — a
direct lever for boosting oilseed yield in bioenergy feedstocks; acyl preference of DGAT
variants can tailor oil composition.
