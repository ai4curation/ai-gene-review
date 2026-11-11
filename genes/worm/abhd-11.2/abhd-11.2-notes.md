# Curation Notes for Caenorhabditis elegans abhd-11.2 (UniProtKB:O45707)

## 1. Identity, Subfamily Placement, and Active-Site Conservation (`PANTHER:PTHR46118:SF4`)
- **Gene / UniProtKB**: `abhd-11.2` (`R05D7.4` / `WBGene00019896` / `UniProtKB:O45707`, unreviewed TrEMBL entry, 299 aa, `sv=2`).
- **MOD gene description check**: `mod_description_deep_research worm abhd-11.2` confirmed that WormBase provides no hand-written `MOD_provided_gene_description` for `abhd-11.2`.
- **Nematode paralogy and subfamily (`file:human/ABHD11/ABHD11-bioinformatics/RESULTS.md`)**:
  - *Caenorhabditis* underwent a lineage-specific duplication (`PANTHER:PTN002251066`) yielding `abhd-11.2` (`UniProtKB:O45707`, assigned to core subfamily `PANTHER:PTHR46118:SF4`) and `abhd-11.1` (`UniProtKB:O62202`, assigned to sister subfamily `PANTHER:PTHR46118:SF3`, clade `PANTHER:PTN002251067`).
  - `abhd-11.2` (`O45707`) conserves the complete alpha/beta-hydrolase catalytic core (`FT DOMAIN 47..286`), including the canonical oxyanion-hole motif `54-HGLGG-58` and the charge-relay triad `Ser124` (`120-LIGHSMGGK-128`), `Asp150` (`146-VVAVDISPA-154`), and `His279` (`275-PDAGHWVHA-283`), aligning 1:1 with human `ABHD11` (`Q8NFV4` `sv=2`) `Ser132`, `Asp156`, and `His287`.

## 2. Literature Search and Organelle Granularity (`projects/ORGANELLES.md`)
- Targeted PubMed and cached-corpus queries for `("abhd-11.2" OR "R05D7.4" OR "O45707" OR "WBGene00019896") AND ("Caenorhabditis" OR "elegans")` identified **zero** primary experimental studies assaying `abhd-11.2` in *C. elegans*.
- **Organelle granularity check (`GO:0005739` mitochondrion)**:
  - The PAINT `IBA` (`GO_REF:0000033`) from Unikont node `PANTHER:PTN000106239` (backed by experimental mouse `Abhd11`, human `ABHD11`, and yeast `Imo32` mitochondrial localization) soundly supports `GO:0005739` (`ACCEPT`).
  - Per `projects/ORGANELLES.md`, we do **not** add `GO:0005759` (`mitochondrial matrix`) as `NEW` because `O45707` is an experimentally uncharacterized TrEMBL sequence with neither a verified cleavable N-terminal presequence (`FT TRANSIT` absent) nor a sub-organelle localization or matrix enzyme-complex assay in *C. elegans* (fewer than two independent lines of sub-compartment evidence).

## 3. Annotation Review Decisions
- `GO:0005739` (`mitochondrion`, `IBA`, `GO_REF:0000033`): `ACCEPT` (stay at root organelle per `projects/ORGANELLES.md`).
- `GO:0006629` (`lipid metabolic process`, `IBA`, `GO_REF:0000033`): `MARK_AS_OVER_ANNOTATED` (propagated from single-seed yeast `IMO32` high-copy overexpression TAG changes; mammalian `ABHD11` acts on lipoylated OGDHc rather than cellular glycerolipids, and `abhd-11.2` is unassayed in *C. elegans*).
- `GO:0052689` (`carboxylic ester hydrolase activity`, `IBA`, `GO_REF:0000033`): `ACCEPT` (conserved `54-HGLGG-58` oxyanion loop and `Ser124-Asp150-His279` catalytic triad).
