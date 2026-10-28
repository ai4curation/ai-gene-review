# FKTN source guide

This guide records the evidence access used for the FKTN review. Normal publication, UniProt, QuickGO, Reactome and family files were obtained through their standard routes and were not hand-edited. Separately recovered originals remain distinct from abstract-only normal caches.

## Original sources and independent readings

- [PMID26923585 original Kobe PDF](https://da.lib.kobe-u.ac.jp/da/kernel/90003339/90003339.pdf): original Results/Discussion and enzyme Methods read in the independent ROOT consultation; selected pages 8,12,13 visually inspected there. SHA256: 811ef34a76ad1513e6d267b08b0bbb66462316a68f8c85a4cd0586e0dc69102c. NMR establishes GalNAc-C3 attachment; separate pNp acceptors lack mannose phosphate. Insert species and uninspected supplement boundaries remain explicit.
- [PMID27194101 full primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4873967/): mouse enzymes, rabbit dystroglycan and human host cells distinguished; donor transfer and rescue do not independently resolve every linkage.
- [PMID25279699 publisher full text](https://elifesciences.org/articles/03941): human FKTN pTW322 versus mouse Fkrp pTW323; human patient fibroblasts are separate experiments.
- [PMID27601598 full primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC5098040/): selected Methods/Results and Figures 6–7 in the association consultation. Co-recovery and HCT116/HEK293T glycoforms remain distinct; alternative donor models are hypotheses.
- [PMID29477842 abstract](https://pubmed.ncbi.nlm.nih.gov/29477842/) plus [author-deposited doctoral summary](https://da.lib.kobe-u.ac.jp/da/kernel/D1007246/D1007246y.pdf): the summary is supplementary primary evidence, not journal full Methods. Tagged triple co-IP, GM130 localization, activities and FKTN product MS were described; endogenous FKTN was detected, endogenous FKRP was not independently visualized.
- [PMID29884773 full primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC6078450/): FKTN/FKRP donor competition and soluble enzyme assays. FKTN kinetic parameters are not reassigned to FKRP; no physiological glycerol-regulation annotation is manufactured.
- [PMID18808525 full primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC2613979/) and [PMID34830034 full primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8622492/): actual selected Methods/Results/Discussion read, preserving cancer-cell identity, doses, timepoints, controls and unresolved mechanistic differences. No figure-pixel or supplement audit is claimed for these readings.
- [PMID17034757](https://pubmed.ncbi.nlm.nih.gov/17034757/) and [official IntAct](https://www.ebi.ac.uk/intact/search?query=pubid%3A17034757): full publisher Methods unavailable; abstract and curated assay records support association/localization with stated limits. Exact human pair O75072/Q8WZA1, tagged COS-7 and one C2C12 colocalization context were recovered.
- [PMID15213246](https://pubmed.ncbi.nlm.nih.gov/15213246/): the normal cache is abstract-only; original scanned pages 709–712 were independently read in the localization consultation. FKTN is the transfected myc cis-Golgi comparator; FKRP endogenous rough-ER observations are not evidence for FKTN ER localization.
- [PMID9690476](https://pubmed.ncbi.nlm.nih.gov/9690476/): original abstract and metadata support historical disease/secretion contexts. Detailed construct and endogenous secretion assays remain unavailable.
- BioPlex [PMID28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/) and [PMID33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/): curated interaction contexts plus independent targeted corroboration. Exact supplemental edge, bait direction, cell-line allocation and spectra were not replayed; the 33961781 normal full-text flag does not imply Methods access.

## Ontology and phylogeny

[GO:0016780](https://www.ebi.ac.uk/QuickGO/term/GO:0016780) covers substituted-phosphate transfer. [GO:0047356](https://www.ebi.ac.uk/QuickGO/term/GO:0047356) describes ribitol-phosphate-polymer extension; the name does not by itself justify replacement for mammalian glycopeptide transfer, and no hard bacterial taxon restriction is asserted. [GO:0035269](https://www.ebi.ac.uk/QuickGO/term/GO:0035269) includes later extension of an O-mannose glycan. [GO:1902494](https://www.ebi.ac.uk/QuickGO/term/GO:1902494) requires a catalytically active complex; membership here integrates recovery with activity evidence.

[Official GO path](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139/paths/GO:0005737?relations=is_a,part_of) confirms GO:0000139 part_of GO:0005794 part_of GO:0005737. The exact 188-byte response SHA256: a37f7f3aea05c7f1900929078d604158bfee3b1262ea57e4830c75d7fddede42 supports the two TOO_GENERAL cytoplasm decisions. This is a precision judgment, not a false-location claim.

The original PAINT IBD assertions at PTN001034988 and PTN000395622 were matched to the human FKTN target path in the complete 115-node PTHR15407 topology. Original IBD, official family topology, normal family cache and incoming QuickGO provenance were distinguished. Human FKTN among experimental seed evidence is not circular; fungal descendants do not negate an ancestral glycan-biosynthesis assertion. The normal PTHR15407 entries, metadata and paint files were preserved byte-for-byte, without bulk leaf-GAF download.

Private reproducible PAINT proof SHA256: 2c31a1b9925e962049d9bf0b6dfac012bd114f685d58809c5992e16d0e33e0d4. Original QuickGO 44-context response SHA256: 20d79b929cc5a3938ba01fc88c3d11f0d89890fdd739401bcabd374e62ef2c74. The complete context mapping is described in [source evidence](FKTN-source-evidence.md).

## Normal-source conservation

Direct source receipts for the independent replay: [complete PTHR15407 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR15407), retrieved 2026-10-28T16:09:58Z, SHA256: 602c3a4e8bc859c0ba859c3b6373257213b7b9bfbc0b7e68e11c5613dea91a30; [original IBD.gaf](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf), retrieved 2026-10-28T05:21:02Z, last-modified 2026-08-28, SHA256: 0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569; [original 44-context QuickGO response](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:O75072&limit=200&page=1), retrieved 2026-10-28T15:25:45Z, SHA256: 20d79b929cc5a3938ba01fc88c3d11f0d89890fdd739401bcabd374e62ef2c74. Separate retrieval provenance does not assert whole-release synchronization.

The [original scanned PMID15213246 article](https://mhlw-grants.niph.go.jp/system/files/2004/043141/200400741B/200400741B0016.pdf) has SHA256: 65d858e4d7683851fca71242c712a0814c7600699d7d3bdc36b0ecef3ab7fd0e; journal pages 709–712 correspond to PDF pages 7–10. The independent localization consultation read those pages visually. This does not imply that figure pixels or supplements from other sources were inspected.

Seventeen sources were present on qualified main d50d8c566c7a9ddc56c56e226483608c0717faef and were hydrated/verified before fetch. Four absent sources (PMID9690476,17034757,18808525,34830034) were acquired normally. All 21 final normal-source identities are below; no provider-generated research text was authored.

| Normal path | Bytes | SHA256 | Disposition |
| --- | --- | --- | --- |
| interpro/panther/PTHR15407/PTHR15407-entries.csv | 3198 | 398b9360549edaf4d6d59f1abd6628663069d12a3a2e40c7a229734bd63ecb75 | EXACT_MAIN_REUSE |
| interpro/panther/PTHR15407/PTHR15407-metadata.yaml | 906 | 6f7ad632ede6abeed9efe53eb8c0fb272256a658466fee41e68ad00ed2d96f2f | EXACT_MAIN_REUSE |
| interpro/panther/PTHR15407/PTHR15407-paint.tsv | 325 | 612da5a2b5ff948094ee14762297744121383753d53fb8bd294c73f1b79a863d | EXACT_MAIN_REUSE |
| publications/PMID_15213246.md | 1938 | 335497422820a021613aa6df7bb1021045c066beffcfb84384a1d5c8da371f9f | EXACT_MAIN_REUSE |
| publications/PMID_17034757.md | 2856 | 63ca257caefe206974447d9952b356bd39683456beeb88d3de381ddef355f0b5 | ABSENT_UNOWNED |
| publications/PMID_18808525.md | 3002 | e8aedac9ba2ef373248db379a1d9f504bbc129854cf0f7336d250490c851ea3d | ABSENT_UNOWNED |
| publications/PMID_25279699.md | 253307 | 34c07f13885884962bc334a1f8bdd35cfcfecacf2921fb903137d557e2ef7676 | EXACT_MAIN_REUSE |
| publications/PMID_26923585.md | 4201 | 0c708a3abeaba668bef8ef077f4f61a0720a1f697828c8777cff0ac49280c701 | EXACT_MAIN_REUSE |
| publications/PMID_27194101.md | 174338 | 9c8897c543f57ae34a8fe6027b31ebcc60d433820c86ac9820205c268ee58f7d | EXACT_MAIN_REUSE |
| publications/PMID_27601598.md | 4412 | 8b7dad80b4b9187081d1e58e526b63514eab5a4fe0e0798081cb13e9ef80a4c1 | EXACT_MAIN_REUSE |
| publications/PMID_28514442.md | 142186 | 41cf18a7c776a7c6f513c9e222ddfdc2946291ccbd589a8d1317d94a3e69d9f4 | EXACT_MAIN_REUSE |
| publications/PMID_29477842.md | 3256 | 11b3ac279d881dac4f8b55c7d7bf7af12d904d98b28c05db61c2a2a536f9793f | EXACT_MAIN_REUSE |
| publications/PMID_29884773.md | 3953 | b6f56d0342f7aef9899bd4d56af78b495051f1a1a426db38a8b7610f40e80907 | EXACT_MAIN_REUSE |
| publications/PMID_33961781.md | 10060 | 4763a1c8018e1b047fc1c2bf3d0e72c837e4b4c3dffbed428befa479e1c92286 | EXACT_MAIN_REUSE |
| publications/PMID_34830034.md | 79804 | 10a7270155a2073fc0be4f394bd02a87149a0efccf3e10700f2c9c5481e5d7d9 | ABSENT_UNOWNED |
| publications/PMID_9690476.md | 2949 | 0c32dc6ad3c120f5984af680bfdc4e14fd4f8f84a94d75f6497d52c3794e72d2 | ABSENT_UNOWNED |
| reactome/R-HSA-8931838.md | 3620 | d22d4d7f158cd412f189be8cfa6b7cef9799d4091ac4ebd9cfc2f48ba656ff5f | EXACT_MAIN_REUSE |
| reactome/R-HSA-9940735.md | 2320 | ed847f91e74afe76a75b0644d29818d51c7e7e159883d8e653142b585ebf1f29 | EXACT_MAIN_REUSE |
| reactome/R-HSA-9940756.md | 1480 | 33fb8995db2bf276324cb0bd172c7c49515fa4f8aea6dae833f0758342096774 | EXACT_MAIN_REUSE |
| reactome/R-HSA-9940805.md | 1136 | b2ba57384b3b3abd79d16a1e692359a916ca77a34edc0ca8efdb57ca09fdfdac | EXACT_MAIN_REUSE |
| reactome/R-HSA-9948070.md | 676 | a15701f23331367961579645658262669c2afde74108e332c2fd94950a5b9d01 | EXACT_MAIN_REUSE |
