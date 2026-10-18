# SIGNOR pathway exports

Verbatim snapshots of SIGNOR (SIGnaling Network Open Resource, PMID:36243968)
pathway relation exports, used as a **signed-interaction source** for calibrating
curated signalling modules. SIGNOR is not a Boolean model, but its causal
relations (`up-regulates` / `down-regulates`, with mechanism, residue, cell/tissue
context, PMID and a `direct` flag) are exactly the edge vocabulary a Boolean
regulatory graph is built from, and SIGNOR's own Boolean-model pipeline (SIGNOR
→ CaSQ → SBML-qual, PMID:32403123) makes the same reduction.

- **Fetched from**: `https://signor.uniroma2.it/getPathwayData.php?pathway=SIGNOR-EGF&relations=only`
  on 2026-09-26 (`SIGNOR-EGF.tsv`, 102 relation rows, md5 `d3f40370e822a7a6a983214ec17198ae`).
  The pathway list is at `getPathwayData.php?list`.
- **Licence**: SIGNOR data are released under Creative Commons Attribution 4.0
  International (CC BY 4.0), as stated on the SIGNOR API page.
- **Columns of interest**: `entitya`/`ida`/`databasea` (regulator, with a UniProt
  accession or a SIGNOR protein-family/complex/phenotype id), `entityb`/`idb`,
  `effect`, `mechanism`, `residue`, `tax_id`, `pmid`, `direct`, `sentence`.
- **Caveats**: relations are pooled across taxa (human, mouse, rat, cell lines);
  SIGNOR protein-family nodes (`ERK1/2` = SIGNOR-PF1, `MEK1/2` = SIGNOR-PF25,
  `AKT` = SIGNOR-PF24) and phenotype nodes (`Proliferation` = SIGNOR-PH4) sit
  alongside single proteins.

`SIGNOR-EGF.mapping_to_modules.yaml` is the reviewed bridge from SIGNOR entity
names to the same shared symbols used by `../bbm-070-mapk-cancer-cell-fate/`; see
`models/boolean/README.md` for the format.

To refresh or extend:

```bash
curl -sS "https://signor.uniroma2.it/getPathwayData.php?pathway=SIGNOR-P38&relations=only" \
  -o models/boolean/signor/SIGNOR-P38.tsv
```
