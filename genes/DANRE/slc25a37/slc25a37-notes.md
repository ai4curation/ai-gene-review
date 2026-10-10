# Notes for DANRE slc25a37

## 2026-05-09 review notes

- Core function is mitochondrial inner-membrane ferrous iron transport/import for erythroid heme biosynthesis [file:DANRE/slc25a37/slc25a37-uniprot.txt "Mitochondrial iron transporter that specifically mediates iron uptake"].
- Broad iron-transporter/transmembrane-transport annotations were modified to ferrous iron transporter activity and iron import into mitochondrion [file:DANRE/slc25a37/slc25a37-uniprot.txt "Reaction=Fe(2+)(in) = Fe(2+)(out)"].
- Erythrocyte development, maturation, and embryonic hemopoiesis are retained as non-core phenotypes downstream of impaired mitochondrial iron uptake [PMID:16511496 "profound hypochromic anaemia and erythroid maturation arrest"].

## Re-review 2026-09-29

Full re-review of all 13 annotation rows against the cached literature; the templated
review blocks were replaced with evidence-specific summaries and reasons.

- GOA remapping: current QuickGO attaches ZFIN's experimental (IDA/IMP) rows for this gene
  to newer TrEMBL accessions of the same gene, so the 11 ZFIN rows (PMID:16511496,
  PMID:9007251, PMID:21627978, PMID:25957689) are absent from a fresh Q287T7 download.
  They were restored into slc25a37-goa.tsv by the orchestrator and are reviewed here on
  their merits; the yaml rows are legitimate and must be kept.
- Core activity: ferrous iron transmembrane transport across the mitochondrial inner
  membrane, feeding heme synthesis in erythroblasts. IBA GO:0015093 and the ZFIN
  IMP/IBA GO:0048250 rows are ACCEPT [PMID:16511496 "Our data show that mfrn functions as
  the principal mitochondrial iron importer essential for haem biosynthesis in vertebrate
  erythroblasts."] [file:DANRE/slc25a37/slc25a37-uniprot.txt "Reaction=Fe(2+)(in) =
  Fe(2+)(out); Xref=Rhea:RHEA:28486"].
- GO:0005381 (IEA ARBA and ZFIN IMP) and GO:0055085 (IEA InterPro) are MODIFY to the
  specific children GO:0015093 / GO:0048250; these are granularity refinements, not
  challenges to the curator (the Shaw 2006 cache is abstract only, full text unseen).
- GO:0005739 mitochondrion IDA is ACCEPT as stated rather than refined to inner
  membrane: the inner-membrane placement is a UniProt inference (ECO:0000305) from the
  same paper and is already carried by the SubCell IEA row.
- Developmental IMP rows (erythrocyte development PMID:25957689, embryonic hemopoiesis
  PMID:21627978 and PMID:9007251, erythrocyte maturation PMID:16511496) are
  KEEP_AS_NON_CORE: each records a genuine mutant phenotype, but the program that fails
  is downstream of the iron-supply step mitoferrin-1 performs [PMID:25957689 "ALA
  supplementation specifically rescued anemia in ALAS2 mutant (sauternes, (Brownlie et
  al., 1998)) embryos, but not anemia in mitochondrial iron transporter mutants
  (frascati, (Shaw et al., 2006))"] [PMID:21627978 "normal human MFRN1 cDNA was able to
  fully complement the anemia in mutant embryos"] [PMID:9007251 "Mutations in five genes,
  chablis, frascati, merlot, retsina, thunderbird and two possibly unique mutations cause
  a progressive decrease in the number of blood cells during the first 5 days of
  development."].
- reference_review added to all four PMIDs (all VERIFIED against cached titles);
  description rewritten as standalone biology; core_functions carries the single
  Fe2+-import activity. Validation: zero errors, zero warnings (the deep-research
  file is cited only as secondary support for the inner-membrane localization row; all
  functional claims rest on cached primary literature and UniProt). Status set to
  COMPLETE.
