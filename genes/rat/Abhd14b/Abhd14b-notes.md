# Abhd14b (rat) — review notes

Family-coordinated review of rat `Abhd14b` (`UniProtKB:Q6DGG1`, `RGD:1359649`, `PANTHER:PTHR46197:SF2`, 210 aa).

## 1. Orthology and sequence conservation

Rat ABHD14B (`Q6DGG1`, 210 aa, `sequence_version: 1`) is a strict 1:1 mammalian ortholog of human `ABHD14B` (`Q96IU4`, 210 aa) and mouse `Abhd14b` (`Q8VCR7`, 210 aa) in `PANTHER:PTHR46197:SF2` (`PROTEIN-LYSINE DEACYLASE ABHD14B-RELATED`). It preserves the exact 210-residue soluble domain architecture without any transmembrane segment and retains all three catalytic triad residues at identical positions: `Ser111` (`SPSLSGMY`, 109–116), `Asp162` (`VYGDQDPM`, 157–164), and `His188` (`GAGHPCYL`, 185–192).

No rat-specific biochemical or genetic study has been published; all 21 GOA annotations derive from orthology projection (`IBA`, `ISO` by RGD, `ISS` by UniProt, `IEA` by Ensembl/UniProt/RHEA).

## 2. Review of the 21 existing GOA rows

- **`GO:0061733` (`protein-lysine-acetyltransferase activity`, `IEA` `GO_REF:0000116` via `RHEA:45948` and `ISS` `GO_REF:0000024` from `UniProtKB:Q96IU4`) -> `REMOVE` (with `source_defects`)**:
  - Same RHEA2GO / UniProt directionality inversion as on human `Q96IU4` and mouse `Q8VCR7`: UniProt records `RHEA:45948` with `PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:45950` (CoA-dependent deacetylation of acetyl-lysine, generating acetyl-CoA), whereas `GO:0061733` asserts the reverse lysine acetyltransferase (KAT) reaction contradicted by `PMID:31478652`.
- **`GO:0016787` (`hydrolase activity`, `IBA` `PTN002920773`, `IEA` `GO_REF:0000107`, `ISO` `GO_REF:0000121`) -> `MARK_AS_OVER_ANNOTATED`**:
  - Projected from human `Q96IU4` in vitro surrogate *p*-nitrophenyl ester hydrolysis (`PMID:14672934`, `PMID:31478652`); physiological catalysis transfers acetyl groups to CoA (`RHEA:45950`) rather than hydrolyzing water.
- **`GO:0045944` (`positive regulation of transcription by RNA polymerase II`, `IBA`, `IEA`, `ISO`) -> `KEEP_AS_NON_CORE`**:
  - Orthologous projection from human CIB reporter assays (`PMID:14672934`); retained as non-core consistent with human and mouse orthologs.
- **Subcellular localization**:
  - `GO:0005829` (`cytosol`, `IEA`, `ISO`) -> `ACCEPT`
  - `GO:0005634` (`nucleus`, `IEA`, `ISO`, `ISS`) -> `ACCEPT`
  - `GO:0005654` (`nucleoplasm`, `IEA`, `ISO`) -> `ACCEPT`
  - `GO:0005730` (`nucleolus`, `IEA`, `ISO`) -> `KEEP_AS_NON_CORE`
  - `GO:0005737` (`cytoplasm`, `IBA`, `IEA`, `ISO`, `ISS`) -> `TOO_GENERAL` (entailed by accepted `GO:0005829` `cytosol`).
- **`NEW` annotations**:
  - `GO:0016407` (`acetyltransferase activity`) and `GO:0035601` (`protein deacylation`) inferred from strict 1:1 orthology and intact `Ser111-Asp162-His188` active site (`Q96IU4`, `PMID:31478652`), accompanied by `proposed_new_terms` for `CoA-dependent protein-lysine deacetylase activity` (`RHEA:45950`).
