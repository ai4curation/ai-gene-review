# B6SNH0 (ZmbZIP60) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene MAIZE B6SNH0`; UniProt id is B6SNH0 (no accession switch).
  GeneID 100280864 = Zm00001d046718 = GRMZM2G025812 ("bZIP transcription factor 60" in NCBI
  Gene), the ZmbZIP60 locus [PMID:30008724 "ZmbZIP60 (Zm00001d046718)"].
- B6SNH0 (300 aa) is the unspliced precursor [PMID:22417282 "The unspliced mRNA is predicted
  to encode a type II membrane protein of 300 AA with a single transmembrane domain (TMD)"].
  The active nuclear TF is the 258-aa product of IRE1-type spliced mRNA, which has no UniProt
  record; recorded as a functional isoform plus a MISSING_ISOFORM source defect.
- GOA has 5 IEA rows only. No experimental GO annotations exist for this gene.
- Key evidence: Li et al. 2012 (full text, splicing; protein localization is predicted, not
  shown), Wang et al. 2012 (abstract only; GFP-deltaC nuclear, yeast transactivation,
  complementation of Arabidopsis bzip60 BiP3 induction), Li et al. 2020 Plant Cell (abstract
  only; bzip60-2 mutant, HSFTF13 promoter target in protoplasts).
- Decisions:
  - GO:0003700 ACCEPT (core).
  - GO:0043565 ACCEPT (bZIP basic region; part of core TF activity).
  - GO:0005634 ACCEPT (spliced form; GFP-deltaC nuclear).
  - GO:0005789 KEEP_AS_NON_CORE (precursor anchoring; TMD shown by sequence analysis, ER
    membrane shown for Arabidopsis bZIP60 by IDA, not for the maize protein).
  - GO:0006355 MODIFY -> GO:0045893 positive regulation of DNA-templated transcription
    (transactivation in yeast; mutant loses target upregulation). OAK confirms is_a.
  - NEW GO:0030968 endoplasmic reticulum unfolded protein response (IC). Comparator check:
    AtbZIP60 carries GO:0030968; XBP1 (functional analog) carries UPR terms. bZIP60 does work
    in the process: it is the transcription factor output of the IRE1 branch. Not used the
    more specific GO:0036498 because the maize IRE1 has not been shown to perform the splicing.
  - Heat response / HSR link not added as a NEW term: it rests on a knock-down phenotype and an
    abstract-only paper (NEW bar).
