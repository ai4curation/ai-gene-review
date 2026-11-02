# FUL (FRUITFULL, AGL8, At5g60910; UniProt Q38876) curation notes

## 2026-10-05 — initial review (floral_meristem_identity module)

- Identity: UniProt primary gene name is AGL8 (synonym FUL); fetched by accession
  (`just fetch-gene ARATH Q38876 --alias FUL`) and gene_symbol set to the standard TAIR symbol FUL.
- Falcon deep research attempted; the provider failed (exit code 1). Notes are from cached publications.

### Floral transition and meristem identity

- AGL8 is expressed in the inflorescence meristem, stem and cauline leaves, excluded from floral primordia, partly by AP1
  [PMID:8535133 "The lack of AGL8 RNA in floral meristems is due in part to the action of another MADS box gene, APETALA1, because AGL8 RNA does accumulate in apetala1 mutant flower primordia."]
- Rapid induction at the apex during photoinduction [PMID:9367440 "Extension of an 8-hour day by either continuous red- or far-red-enriched light induced LEAFY and AGAMOUS-LIKE8 expression within 4 hours."]
- ap1 cal ful non-flowering phenotype; LFY not up-regulated, TFL1 ectopic [PMID:10648231].
- FT-dependent accumulation [PMID:16155177 "FUL, SEP3, and APETALA1 accumulation in the meristem is associated with and contributes to the transition to flowering."]
- SPLs (age pathway) directly activate flower-promoting MADS-box genes [PMID:19703399 "with SPLs directly activating flower-promoting MADS box genes"].
- FUL redundantly with SOC1 promotes flowering; heterodimer model
  [PMID:24465009 "A model is proposed where the sequential formation of FUL-SVP and FUL-SOC1 heterodimers may mediate the vegetative and meristem identity transitions"].
- soc1 ful double mutants: perennial-like phenotypes, meristem determinacy [PMID:18997783 "We found that the MADS box proteins SUPPRESSOR OF OVEREXPRESSION OF CONSTANS 1 (SOC1) and FRUITFULL (FUL) not only control flowering time, but also affect determinacy of all meristems."]

### Fruit and other roles

- Fruit: [PMID:9502732 "The primary defect of ful-1 fruits is within the valves, whose cells fail to elongate and differentiate."]
- Stem/branch growth via SAUR10 [PMID:28586421].
- End of flowering (global proliferative arrest) via direct AP2 repression [PMID:29422669 "FUL directly and negatively regulates APETALA2 expression in the shoot apical meristem"].

### Decisions

- Core MF GO:0000981; core BPs GO:0010228 (vegetative to reproductive phase transition of meristem; supported by Balanza 2014 and Hempel 1997, not in GOA), GO:0009911 (existing), GO:0010154 fruit development (existing IMP).
- All protein binding IPI rows (SEP3, SOC1, AGL24 partners) -> MODIFY to GO:0046982.
- GO:0010077 IGI with BOP1/2 (abstract-only paper) -> KEEP_AS_NON_CORE, deferring to the curator; same decision used for the SOC1 row from the same paper.
- GO:0060560 (SAUR10 / branch growth) and the Y1H nitrogen network row -> KEEP_AS_NON_CORE.
