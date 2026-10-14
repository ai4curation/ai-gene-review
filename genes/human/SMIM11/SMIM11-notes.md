# SMIM11 (P58511) review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt P58511 SIM11_HUMAN, 58 aa, PE1; aliases C21orf51, FAM165B, SMIM11A (HGNC:1293).
  Chromosome 21. N-terminal predicted helical TM segment (10-32) followed by a lysine-rich
  coiled-coil (29-58). Membrane / single-pass is curator inference (ECO:0000305).
- Family: Pfam PF14981 FAM165, InterPro IPR042125, PANTHER PTHR35975 (family name "SMALL INTEGRAL
  MEMBRANE PROTEIN 11A"). No characterized member.
- Expression: UniProt "Expressed in heart, spleen, liver, stomach, muscle, lung, testis, skin, PBL
  and bone marrow." HPA "Low tissue specificity". HPA antibody IF (proteinatlas.org JSON, fetched
  2026-10-03): "Focal adhesion sites". That is an unusual location for a single-pass peptide; it is not in GOA
  and not used.

### Literature search
- PubMed `SMIM11[tiab] OR C21orf51[tiab] OR FAM165B[tiab] OR SMIM11A[tiab]` -> 2 hits.
  - PMID:11707072 (Genomics 2001; abstract only): confirmation of C21orf51 as a bona fide transcript in a
    revision of the chromosome 21 transcription map [PMID:11707072 "Here we report
    the characterization and expression pattern of the putative transcripts C21orf7,
    C21orf11, C21orf15, C21orf18, C21orf19, C21orf22, C21orf42, C21orf50, C21orf51,"]. Gene
    existence only.
  - PMID:34113558 (sporamin-treated LoVo cells): lists "SMIM11A" among down-regulated "TFs". SMIM11 is
    not a transcription factor; this is a list-level mislabel and is not cited.

### GOA rows
- 3 x protein binding (IPI), all HuRI [PMID:32296183]: ASPH isoform (Q12797-6), CERS4 (Q9HA82;
  ER-membrane ceramide synthase), UBQLN2 (Q9UHD9; cytosolic TMD chaperone
  [PMID:27345149 "We show that Ubiquilin family proteins bind transmembrane domains in the cytosol"]).
  CERS4 is a multi-pass ER-membrane enzyme; single Y2H hits between TM peptides and membrane proteins
  carry no functional information without follow-up. -> REMOVE all three.
- membrane (IEA) -> ACCEPT.

### Conclusion
No function known. No core function, no NEW terms.
