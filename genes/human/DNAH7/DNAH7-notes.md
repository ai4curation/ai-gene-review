# DNAH7 notes

## Identity and structure
- UniProt Q8WXX0, 4024 aa, full dynein heavy chain architecture (stem 1..1289, AAA1-AAA6, stalk 2572..2873) [file:human/DNAH7/DNAH7-uniprot.txt].
- Cryo-EM of human respiratory DMTs: "IDAb and IDAe are both DNAH7" [PMID:37258679 "we have now confirmed those HC assignments40 and also discovered that IDAa is DNAH12, IDAc is DNAH3, and IDAb and IDAe are both DNAH7"].
- IDAb/IDAe motor domains modelled as copies of IDAg, "the other centrin-containing IDA" [PMID:37258679].

## Localization
- Airway cilia, induced during ciliogenesis [PMID:11877439 "DNAH7 was induced during ciliated cell differentiation, and immunohistochemistry demonstrated the presence of DNAH7 in normal cilia"].
- Along entire respiratory axoneme; absent in CCDC39/CCDC40 ruler mutants [PMID:39056782 "In healthy control subjects, DNAH7 is localized throughout the entire length of ciliary axonemes"].
- Reduced in sperm lacking radial spoke 1 (IQUB) [PMID:39849482 "DNAH7 and DNAH12, the components of IDA, were significantly reduced both in the spermatozoa of IQUB842del patient and Iqub−/− mice"].

## Disease (CILD50 / male infertility)
- [PMID:34476482 "The spermatozoa from the patients with DNAH7 bi-allelic mutations showed specific losses in the inner dynein arms."]
- [PMID:35543642 "DNAH7 disruption in humans results in male infertility, which was characterised by multiple morphological abnormalities of sperm flagella"]; mitochondrial sheath defects.
- [PMID:40810911 "immunofluorescent staining revealed a marked reduction of DNAH7 and other IDA-associated proteins, such as DNAH3 and DNAH6, in the patients' spermatozoa"]; ODA proteins unaffected.
- The 2002 PCD case (PMID:11877439) lacked IDAs but DNAH7 was synthesised; the primary lesion was not shown to be in DNAH7.

## Curation decisions
- Core MF: minus-end-directed microtubule motor activity (IBA; full motor domain). Core CC: inner dynein arm. Core BP: cilium movement; IDA assembly (structural subunit).
- Calcium ion binding (InterPro EF-hand hit, no UniProt EF-hand): MARK_AS_OVER_ANNOTATED.
- Dynein intermediate chain binding: UNDECIDED; PAINT IBD at PTN000743491 seeded only by dictyBase:DDB_G0276355 (cytoplasmic dynein) (interpro/panther/PTHR10676/PTHR10676-paint.tsv).
- HPA sperm annulus: UNDECIDED (annulus is not axonemal).

## PANTHER / IBA check
- Human DNAH7 (Q8WXX0) and mouse Dnah7a (E9Q0T8) / Dnah7c (A0A087WR13) receive the same 8 IBAs in QuickGO (incl. GO:0036156, GO:0036159, GO:0120316); no human/mouse family split as seen for DNAH12. DNAH7 itself seeds the PTN008503981 inner dynein arm IBD and PTN008951089 IDA assembly IBD.

## Deep research
- Falcon deep research failed (Edison API authentication 503 errors on repeated attempts); review based on direct reading of cached literature.
