# DNAH8 notes

## Deep research
- `just deep-research-falcon human DNAH8` failed twice (Edison/FutureHouse API: "Failed to authenticate"). No deep-research file exists; literature was gathered directly from PubMed E-utilities (`DNAH8[tiab]`, 49 hits) and cached with `just fetch-pmid`.

## Identity and structure
- Gamma-type outer dynein arm (ODA) heavy chain; sperm paralog of DNAH5. 4490 aa; six AAA domains, stalk between AAA4 and AAA5, ATP P-loop at 1846-1853 [file:human/DNAH8/DNAH8-uniprot.txt "FT   BINDING         1846..1853"].
- Whitfield et al. classify DNAH8 as gamma-type [PMID:31178125 "γ-type: DNAH5 and DNAH8 and β-type: DNAH9, DNAH11, and DNAH17"]. Mouse Dnahc8 likewise [PMID:16054618 "Dnahc8, an axonemal gamma-type dynein heavy chain (gammaDHC) gene"]. (UniProt's AltName "Axonemal beta dynein heavy chain 8" is a legacy name.)

## Localization
- Sperm axoneme, not respiratory cilia [PMID:31178125 "We show that DNAH17 and DNAH8, but not DNAH5, DNAH9, or DNAH11, colocalize with α-tubulin along the sperm axoneme, whereas the reverse picture is observed in respiratory cilia"].
- Mouse: principal piece [PMID:16054618 "Interestingly, DNAHC8 is confined to the principal piece of the sperm tail."]; cytoplasm of primary spermatocytes (UniProt, by similarity to Q91XQ0) = preassembly stage.

## Disease / phenotype
- SPGF46, MMAF [PMID:32619401 "Dnah8-knockout male mice also presented typical MMAF phenotypes and sterility."]; independent: PMID:32681648, PMID:33704367, PMID:33611675, PMID:36308074.
- DNAH8 and DNAH17 are interdependent: DNAH17 lost in DNAH8-mutant sperm [PMID:32619401; PMID:36308074 "In addition, expression of DNAH17, a DNAH8-associated protein, was significantly reduced in the sperm flagella of the patients with the DNAH8 mutation."], and DNAH8 lost in DNAH17-mutant sperm [PMID:31178125; PMID:41549443].
- Non-axonemal reports (low confidence): AR regulator in prostate cancer [PMID:27363033 "we identified Dynein Axonemal Heavy Chain 8 (DNAH8) as an AR regulator"]; fetal testosterone/hypospadias in KO mice [PMID:41463044]. Not annotated.

## Annotation review decisions
- Core: minus-end-directed microtubule motor activity (IBA, accepted); outer dynein arm; sperm flagellum/axoneme.
- REMOVE dynein light intermediate chain binding (IBA + IEA): seeded only by cytoplasmic dynein 1 heavy chains; the ODA has no light intermediate chain, and DNALI1 (IDA subunit) is retained in DNAH17/DNAH8-null sperm [PMID:31178125].
- MODIFY generic dynein complex IEA -> outer dynein arm; NAS cilium-dependent cell motility -> flagellated sperm motility.
- NEW: flagellated sperm motility (GO:0030317). Comparator check: mouse Dnah1, Dnah7a/b/c, Dnah11 carry GO:0030317 in GOA.

## PANTHER / IBA
- GOA IBAs come from PTHR10676 nodes (PTN000743491 root; PTN002472868 gamma ODA HC; PTN008503977 sperm flagellum). UniProt's PANTHER xref places DNAH8 in PTHR46532:SF11 (named "DYNEIN AXONEMAL HEAVY CHAIN 12"), the same subfamily the DNAH12 review flagged. Despite this, human DNAH8 and mouse Dnah8 (Q91XQ0) receive the same 7 IBAs in QuickGO (checked 2026-10-14), so there is no human/mouse IBA gap for DNAH8.
