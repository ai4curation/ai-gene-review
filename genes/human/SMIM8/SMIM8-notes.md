# SMIM8 (Q96KF7) review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt Q96KF7 SMIM8_HUMAN, 97 aa, PE1; aliases C6orf162, DC18. Disordered, basic/acidic
  N-terminal region (1-24), single predicted helical TM segment (48-70), short C-terminal tail.
  Membrane / single-pass is curator inference (ECO:0000305).
- Family: "Belongs to the SMIM8 family"; Pfam PF14937 DUF4500, InterPro IPR026686 UPF0708,
  PANTHER PTHR14274. No characterized member.
- Expression: HPA "Low tissue specificity" in human (UniProt DR line). In mouse, Smim8 was chosen as a
  testis-enriched gene [PMID:34290169]. HPA antibody IF (proteinatlas.org JSON, fetched 2026-10-03):
  "Vesicles". Not in GOA, not used.

### Literature search
- PubMed `SMIM8[tiab] OR C6orf162[tiab]` -> 3 hits.
  - PMID:34290169 (Asian J Androl 2022): CRISPR knockout of 12 testis-enriched mouse genes including
    Smim8. All were dispensable for male fertility [PMID:34290169 "Here, we deleted 12 mouse genes that
    are predicted to be expressed predominantly in the testis with the CRISPR/Cas9 system and revealed
    that all 12 genes were dispensable for male fertility."]. The Smim8 line was mated under a different
    caging scheme [PMID:34290169 "(except for Smim8)"]. The paper also notes
    [PMID:34290169 "Smim8 and Smim9 each containing one transmembrane domain"].
  - PMID:29986096 (NAR 2018): SMIM8 skeletal muscle mRNA is among 16 "CORE-IS" genes positively
    correlated with improvement in insulin sensitivity [PMID:29986096 "These 16 genes segregated into two
    clusters, one positively (DHTKD1, SLC43A1, PCYT2, MCCC1, SGCG, ECHDC3, ALDH6A1, SMIM8 and OARD1)"].
    Correlative only. Most of the co-clustering genes are mitochondrial enzymes, which is at least
    consistent with the MitoCoP localization, but this is not evidence of function.
  - PMID:38658807 (pig myofiber ceRNA network node): expression-network mention only; not cached.

### GOA rows
- mitochondrion (HTP, PMID:34800366 MitoCoP): SMIM8 is in the high-confidence mitochondrial proteome
  defined by quantitative proteomics of purified mitochondria. The only experimental localization in
  GOA. Sub-mitochondrial location unknown. -> ACCEPT.
- membrane (IEA) -> ACCEPT.

### Conclusion
Mitochondrial single-pass membrane protein of unknown function. Knockout mice are fertile. No MF/BP,
no NEW terms. core_functions left empty because there is no function to describe; location-only
"core function" would be padding.
