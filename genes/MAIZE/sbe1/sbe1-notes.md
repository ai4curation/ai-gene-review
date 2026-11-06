# sbe1 (Q41740) review notes

- Fetched by accession (`just fetch-gene MAIZE Q41740 --alias sbe1`) because fetching by symbol resolves Q08047 (SBEIIb, GeneID 542238).
  Confirmed Q41740 = GeneID 542315, gene name sbe1, 12 GOA rows (all IBA/IEA, none experimental).
- Literature work in `sbe1-deep-research-manual.md` (no API deep research available).
- PMID:11864975 was cached during a search but is a Phaseolus vulgaris paper, not relevant; not cited.

## Annotation decisions (summary)
- GO:0003844 branching enzyme activity (IBA, IEA): ACCEPT - direct biochemistry on native and recombinant maize BEI
  [PMID:12231902 "BEI had the highest activity in branching amylose"].
- GO:0003824 catalytic activity: MODIFY -> GO:0003844.
- GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds (InterPro2GO from IPR004193, CBM48 N-terminal domain): REMOVE;
  BE is a transglycosylase (EC 2.4.1.18), no hydrolytic activity reported for maize BEI. Source defect recorded.
- GO:0043169 cation binding (IPR006048): MARK_AS_OVER_ANNOTATED; no cation requirement established for BEI.
- GO:0005737 cytoplasm (IBA): MODIFY -> GO:0009501 amyloplast (plastid protein; cytoplasm is true by GO part_of but uninformative).
- GO:0005975 carbohydrate metabolic process (IBA, IEA) and GO:0044042 glucan metabolic process: MODIFY -> GO:0019252 starch biosynthetic process.
- GO:0005978 glycogen biosynthetic process (IEA InterPro2GO from IPR037439): REMOVE; plants do not make glycogen; taxon-unaware mapping.
- GO:0019252 starch biosynthetic process, GO:0009501 amyloplast: ACCEPT.
- No NEW process terms: germination/coleoptile phenotype (PMID:21599988) is downstream of starch structure and does not meet the NEW bar.
  Possible NEW starch grain (GO:0043036) not added: BEI is only a trace granule component in wild type; noted as a question.
