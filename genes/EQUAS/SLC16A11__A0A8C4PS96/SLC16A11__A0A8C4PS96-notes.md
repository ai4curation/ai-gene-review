# SLC16A11 (donkey, A0A8C4PS96) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Folder `SLC16A11__A0A8C4PS96` because `genes/EQUAS/SLC16A11` is keyed to another transcript model of the same Ensembl gene (A0A9L0JV53). Created with `just fetch-gene EQUAS A0A8C4PS96 --alias SLC16A11__A0A8C4PS96`; 6 GOA rows, all electronic (SubCell, TreeGrafter, InterPro2GO).

### Deep research
`just deep-research-falcon EQUAS SLC16A11__A0A8C4PS96 --fallback perplexity-lite` failed: falcon "Failed to authenticate", perplexity-lite HTTP 401 (quota). No deep-research file exists. The review uses the cached full-text human papers PMID:24390345 and PMID:28666119 and the human UniProt record (Q8NCK7, in `genes/human/SLC16A11/`).

### Evidence status in donkey
There is no experimental work on donkey (or any equid) SLC16A11. UniProt PE 3 (inferred from homology); its FUNCTION, CATALYTIC ACTIVITY, SUBUNIT and SUBCELLULAR LOCATION comments are all ARBA rules, so they are not used as support. Everything functional below is inferred from human MCT11.

### Evolutionary grounding
- Same PANTHER subfamily as human Q8NCK7: PTHR11360:SF80 MONOCARBOXYLATE TRANSPORTER 11 (both UniProt records). Same CDD (cd17423 MFS_MCT11_13) and InterPro MFS_MCT_13 signature.
- PAINT: PTHR11360 node PTN000888455 carries GO:0008028 by IBD at taxon:6072 (Eumetazoa), with human Q8NCK7 among the donors; PTN002260587 carries GO:0005886 and GO:0022857. PAINT did NOT propagate the human-specific pyruvate terms (GO:0050833) from any node; I treat that as deliberate and do not add a pyruvate-specific annotation to donkey.
- Alignment (`SLC16A11__A0A8C4PS96-bioinformatics/RESULTS.md`): all 447 human residues align, 90.6% identity; donkey Met74 = human Met1, so residues 1-73 are an N-terminal extension that is probably a gene-model artefact (human cDNAs with "Erroneous initiation; Extended N-terminus" are flagged on Q8NCK7). All 12 human TM segments are 81-95% identical in donkey.

### Human literature (the reference for transfer)
- PMID:24390345 (SIGMA 2014): T2D risk haplotype; V5-tagged SLC16A11 in HeLa localises to ER [PMID:24390345 "SLC16A11-V5 co-localizes with the endoplasmic reticulum membrane protein Calnexin, but shows minimal overlap with plasma membrane, Golgi apparatus and mitochondria"]; overexpression raises TAG [PMID:24390345 "Expression of SLC16A11 resulted in substantial increases in triacylglycerol (TAG) levels"]. The lipid change is an overexpression readout, not evidence that the transporter participates in lipid metabolism.
- PMID:28666119 (Rusu 2017): H+-coupled pyruvate transport in HEK293T [PMID:28666119 "In summary, bioinformatic analyses and transport assays together establish SLC16A11 as a H+-coupled monocarboxylate transporter belonging to category I."]; ~5% at plasma membrane; BSG interaction needed for cell-surface localisation [PMID:28666119 "We found that BSG knockout significantly reduces localization of SLC16A11REF to the plasma membrane by ~80% (Figure 5G)."]. Only pyruvate was tested as substrate.

### Decisions
- PM: ACCEPT (site of transport). ER membrane: KEEP_AS_NON_CORE (steady-state pool of overexpressed tagged protein).
- GO:0008028: ACCEPT, as precise as the donkey evidence supports (PAINT node level; substrate range untested beyond pyruvate in human).
- GO:0015718: ACCEPT.
- GO:0022857: MODIFY -> GO:0008028. GO:0055085: MODIFY -> GO:1905039 carboxylic acid transmembrane transport (verified is_a descendant via OLS ancestors of GO:1901475).
- No NEW annotations; lipid metabolic process not added (overexpression phenotype only, and human IDA row is not in donkey GOA).
