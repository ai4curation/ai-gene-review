# GCSH (Glycine cleavage system H protein, mitochondrial) — review notes

UniProt: P23434 (GCSH_HUMAN), 173 aa precursor, HGNC:4208, chr16.

## Core biology

GCSH is the **H-protein of the mitochondrial glycine cleavage system (GCS)**. It is a small,
**non-catalytic lipoyl-carrier protein**: it bears a covalently attached lipoyl group on a
specific lysine (N6-lipoyllysine at Lys107 in the mature/precursor numbering) that acts as a
**swinging arm** shuttling the reaction intermediate between the other GCS components.

- FT MOD_RES 107 = N6-lipoyllysine; DOMAIN 66..148 = Lipoyl-binding (PROSITE PS50968 BIOTINYL_LIPOYL, PS00189 LIPOYL).
- COFACTOR: Binds 1 (R)-lipoate cofactor covalently [ECO:0000269|PubMed:1671321].
- AltName "Lipoic acid-containing protein"; KW Lipoyl.

### GCS reaction cycle (P/H/T/L proteins)
From [PMID:36190515]:
"Glycine is decarboxylated to carbon dioxide and the resulting aminomethyl-group transferred to
lipoyl-H-protein as aminomethyl-lipoate. The T-protein releases ammonia while transferring the
methyl-group to tetrahydrofolate. The L-protein reoxidizes the reduced lipoyl-group."
- P-protein = GLDC (glycine dehydrogenase, decarboxylating)
- T-protein = AMT/GCST (aminomethyltransferase)
- L-protein = DLD (dihydrolipoyl dehydrogenase)
- H-protein = GCSH itself: "the H-protein itself is the lipoate carrier of this enzyme complex."
- "Variants could also affect the reaction of the swinging lipoyl-arm to protect the amino-methyl group, for which Ser67 is important" [PMID:36190515].

### Moonlighting: lipoate biogenesis / donor
GCSH also acts in **lipoate biosynthesis and transfer** to other 2-keto-acid dehydrogenases
(DLAT/PDH E2, DLST/2-KGDH E2): apo-H → octanoyl-H (LIPT2) → lipoyl-H (LIAS) → lipoyl donated by
LIPT1 to DLAT/DLST. [PMID:36190515]: "The H-protein is pivotal in the biosynthesis and transfer of
the cofactor lipoate to several critical cellular energetics enzymes." UniProt FUNCTION: "Has a
pivotal role in the lipoylation of enzymes involved in cellular energetics." This underlies the
`protein maturation` (GO:0051604) and `generation of precursor metabolites and energy` (GO:0006091)
TAS annotations from PMID:36190515 — legitimate but non-core moonlighting roles.

## Localization
Mitochondrion / mitochondrial matrix. TRANSIT 1..48 = mitochondrial targeting.
- EXP [PMID:36190515]: colocalization of GCSH (green) with mitochondrial marker cytochrome C (red)
  in COS7 cells.
- HTP [PMID:34800366]: MitoCoP high-confidence mitochondrial proteome (>1,100 proteins).
- Reactome TAS: mitochondrial matrix (GCS + lipoylation reactions occur in matrix).

## Disease
Biallelic GCSH variants → variant/combined nonketotic hyperglycinemia (NKH) + lipoate deficiency;
"Multiple mitochondrial dysfunctions syndrome 7" (MMDS7, MIM:620423). [PMID:36190515, PMID:33890291].
NKH = glycine encephalopathy (accumulation of glycine, elevated CSF/plasma ratio, epileptic
encephalopathy). GCSH accounts for <1% of NKH.

## Annotation strategy
- MF: GOA only gives `protein binding` (GO:0005515) IPIs from large-scale Y2H interactome maps
  (PMID:16189514, PMID:32296183) whose interactors (NMI, MAGEA6/11, MED11, MIS18A, RHBDD2, CIDEB)
  are NOT GCS partners and don't inform function → MARK_AS_OVER_ANNOTATED (bare protein binding,
  uninformative; experimental IPI so not REMOVE).
- The informative MF for a lipoyl carrier is **lipoic acid binding (GO:0031405)** — captures the
  covalent lipoyl cofactor (PROSITE lipoyl domain + N6-lipoyllysine K107 + (R)-lipoate cofactor).
  Add as NEW MF and use as the core_function molecular_function.
- BP core: glycine decarboxylation via glycine cleavage system (GO:0019464) / glycine catabolic
  process (GO:0006546).
- CC core: glycine cleavage complex (GO:0005960); located in mitochondrial matrix (GO:0005759).
- Verified candidate MF `GO:0031405 lipoic acid binding` is current (molecular_function, not obsolete).

## References status
All cited PMIDs and Reactome entries are cached. PMID:1671321 and PMID:3348809 are abstract-only
(full_text_available: false) — abstracts confirm H-protein/GCS identity and lipoylation/cofactor.
PMID:36190515 full text available (the key functional paper).
