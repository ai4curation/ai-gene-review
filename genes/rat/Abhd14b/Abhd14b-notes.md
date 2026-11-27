# Abhd14b (rat) — review notes

Family-coordinated review of rat `Abhd14b` (`UniProtKB:Q6DGG1`, `RGD:1359649`, `PANTHER:PTHR46197:SF2`, 210 aa).

## 1. Orthology and sequence conservation

Rat ABHD14B (`Q6DGG1`, 210 aa, `sequence_version: 1`) is a strict 1:1 mammalian ortholog of human `ABHD14B` (`Q96IU4`, 210 aa) and mouse `Abhd14b` (`Q8VCR7`, 210 aa) in `PANTHER:PTHR46197:SF2` (`PROTEIN-LYSINE DEACYLASE ABHD14B-RELATED`). It preserves the exact 210-residue soluble domain architecture without any transmembrane segment and retains all three catalytic triad residues at identical positions: `Ser111` (`SPSLSGMY`, 109–116), `Asp162` (`VYGDQDPM`, 157–164), and `His188` (`GAGHPCYL`, 185–192).

No rat-specific biochemical or genetic study has been published; all 21 GOA annotations derive from orthology projection (`IBA`, `ISO` by RGD, `ISS` by UniProt, `IEA` by Ensembl/UniProt/RHEA).

## 2. Review of the 21 existing GOA rows

- **`GO:0061733` (`protein-lysine-acetyltransferase activity`)**:
  - `IEA` (`GO_REF:0000116` via `RHEA:45948`) -> `REMOVE` (with `source_defects` `DELETE_ROW`): undirected `RHEA:45948` mapping ignores UniProt's `PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:45950` (CoA-dependent lysine deacetylation, not KAT).
  - `ISS` (`GO_REF:0000024` from `UniProtKB:Q96IU4`) -> `MODIFY` to `GO:0016407` (`acetyltransferase activity`, with `source_defects` `REPOINT`): preserves the valid `Q96IU4` orthologous catalytic transfer while correcting the inverted KAT term to `GO:0016407` pending creation of a dedicated dual-parented `CoA-dependent protein-lysine deacetylase activity` (`RHEA:45950`) term under `GO:0160215` (`deacylase activity`) and `GO:0016407`.
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
- **`NEW` annotation & `knowledge_gaps`**:
  - `GO:0010906` (`regulation of glucose metabolic process`, `ISS` from mouse `Q8VCR7`, `acts_upstream_of_or_within`, `PMID:35700823`) captures conserved mammalian upstream regulation of fasting glucose metabolism (`directly_involved_in` omitted on `core_functions[0]`).
  - `knowledge_gaps` (`MF_DARK`, `BIOLOGY`, `status: NARROWING`) records the absence of direct rat biochemical/genetic studies and unmapped endogenous mammalian acetyl-lysine substrates alongside UniProtKB's `Putative protein-lysine deacylase` similarity caution.
