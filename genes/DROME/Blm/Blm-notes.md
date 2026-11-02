# Blm (DROME, Q9VGI8) review notes

## Session 2026-10-28

- Fetched with `just fetch-gene DROME Blm`; accession Q9VGI8 (Swiss-Prot BLM_DROME,
  FlyBase FBgn0002906, GeneID 41366) confirmed. 49 GOA rows.
- No deep-research provider available; manual synthesis in `Blm-deep-research-manual.md`.
- Extra papers cached for biochemistry: PMID:16849422 (Blm+Top3alpha dHJ
  dissolution), PMID:22511792 (Top3alpha C-terminus binds Blm), PMID:20389284
  (N-terminal strand exchange, abstract only), PMID:24392087.

### Key decisions
- Core MF: 3'-5' DNA helicase activity (IDA PMID:17272294
  "has 3'-->5' DNA helicase activity"), plus DNA-dependent ATP hydrolysis,
  Y-form DNA binding and DNA/DNA annealing (all IDA).
- Core BP: SDSA (GO:0045003) and HR (GO:0000724); generic DNA repair / DSB
  repair / DNA damage response / DNA recombination rows MODIFIED to GO:0000724.
- NHEJ (PMID:15184650, IGI, abstract only) marked over-annotated: RNAi epistasis
  with Ku, not evidence that Blm performs NHEJ.
- DNA synthesis involved in DNA repair (PMID:12522255) marked over-annotated:
  Blm promotes repair synthesis indirectly (D-loop processing); the polymerase
  performs the synthesis.
- Nucleus IDA PMID:31772289: full text shows imaging of transfected **human** BLM in
  S2 cells (`hBLM localized to the DAPI-stained nucleus`). Term is still true
  (other rows), recorded a PROBABLE source defect for FlyBase.
- PMID:8608940 originally (wrongly) mapped mus309 to Ku70/IRBP; PMID:11283371
  showed mus309 = Blm. FlyBase attaches the DSB repair phenotype to Blm, which is
  correct for the alleles used.
- Cytoplasm IBA marked over-annotated (seeds include E. coli RecQ, RECQL5; no fly
  evidence).
- RTR complex (ISS from Sgs1): accepted; Drosophila Blm cooperates with Top3alpha
  biochemically (PMID:16849422) and binds it (PMID:22511792); flies apparently
  lack Rmi1 per PMID:22511792.
- No NEW terms proposed. A double Holliday junction dissolution process term does not
  exist in GO (OLS search empty); noted as a suggested question rather than a NEW row.
