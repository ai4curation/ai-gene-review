# ASB11 notes

- Substrate receptor of CRL5(ASB11) [PMID:31387940 "These findings are consistent with the adaptor role of ASB11 in recruiting BIK to the CRL5 complex."].
- Substrates: Ribophorin 1 (PMID:24337577), BIK (PMID:31387940; K48 chains), DIRAS2 (PMID:38574733), PAICS (PMID:37848033; K6 chains), ERLIN1 (PMID:41668292).
- The GO:0070979 K11 row (PMID:38574733) cannot be checked: the cached record is abstract-only and contains no linkage term. Kept as non-core, deferring to the curator.
- GO:0035556 (InterPro SOCS box) is removed. The SOCS box here is an Elongin BC/Cul5-binding module, and the signalling term comes from cytokine-signalling SOCS proteins.
- Zebrafish Asb11 (DeltaA ubiquitination, Notch, progenitor maintenance; PMID:18776899, PMID:16893969, PMID:22512762) appears in the description only. No NEW process is added, because human ASB11 has not been tested.
- The five Reactome cytosol files do not name ASB11 (grep, 2026-10-04).
- Recall check: PubMed tiab search for ASB11 (2026-10-04) found no mechanistic paper beyond the affinage set.

## 2026-11-04 ORGANELLES ER batch 1 (endoplasmic reticulum rows)

- Rows: GO:0005783 IDA (PMID:24337577) and IEA (GO_REF:0000044, SL-0095). No ER sub-compartment rows.
- The IEA keyword rests on the curated UniProt line "SUBCELLULAR LOCATION: Endoplasmic reticulum {ECO:0000269|PubMed:24337577}" [file:human/ASB11/ASB11-uniprot.txt].
- PMID:24337577 is abstract-only in the cache; PubMed MCP for PMC3900953 returned no full text. Abstract: [PMID:24337577 "We also demonstrated that ASB11 is a novel endoplasmic reticulum-associated ubiquitin ligase"]. PMID:31387940: "Similar to BIK, ASB11 is an ER-residing protein (Andresen et al."
- Sub-compartment: UniProt has no TRANSMEM feature; the only membrane line is my reading of the hydrophobic N-terminal stretch (~residues 13-41, IFITMFATFFFFKLLIKVFLALLTHFYIV; replaced in isoform 3). One unassayed line, so stay at root (rule 4).
- Outcome: both rows stay ACCEPT (core: ER-membrane substrates Ribophorin 1 and BIK, ER stress role); dated ORGANELLES sentence added to each reason.
