# Curation Notes for Caenorhabditis elegans abhd-11.1 (UniProtKB:O62202)

## 1. Identity, Subfamily Placement, and Active-Site Conservation (`PANTHER:PTHR46118:SF3`)
- **Gene / UniProtKB**: `abhd-11.1` (`F32B4.6` / `WBGene00018007` / `UniProtKB:O62202`, unreviewed TrEMBL entry, 297 aa, `sv=1`).
- **MOD gene description check**: `mod_description_deep_research worm abhd-11.1` confirmed that WormBase provides no hand-written `MOD_provided_gene_description` for `abhd-11.1`.
- **Nematode-specific subfamily `PANTHER:PTHR46118:SF3` (`file:human/ABHD11/ABHD11-bioinformatics/RESULTS.md`)**:
  - `abhd-11.1` (`O62202`) belongs to `PANTHER:PTHR46118:SF3` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`, clade `PANTHER:PTN002251067`), arising from a *Caenorhabditis*-specific gene duplication (`PANTHER:PTN002251066`) sister to `abhd-11.2` (`UniProtKB:O45707`, `PTHR46118:SF4`).
  - Although Pfam `PF00561` only matches the N-terminal half (`FT DOMAIN 37..140`) in `abhd-11.1-uniprot.txt`, full-length family alignment (`RESULTS.md`) shows that `O62202` retains the canonical oxyanion-hole motif `44-HGLGG-48` and the complete Ser-Asp-His catalytic triad across the full protein: `Ser114` (`110-LIGHSMGGK-118`), `Asp140` (`136-IVAVDISPA-144`), and `His267` (`263-PKCGHWIHS-271`).

## 2. Literature Search and Organelle Granularity (`projects/ORGANELLES.md`)
- Targeted PubMed and cached-corpus queries for `("abhd-11.1" OR "F32B4.6" OR "O62202" OR "WBGene00018007") AND ("Caenorhabditis" OR "elegans")` identified **zero** primary experimental studies assaying `abhd-11.1` in *C. elegans*.
- **Organelle granularity check (`GO:0005739` mitochondrion)**:
  - The PAINT `IBA` (`GO_REF:0000033`) from Unikont node `PANTHER:PTN000106239` soundly supports `GO:0005739` (`ACCEPT`).
  - Per `projects/ORGANELLES.md` and `PTHR46118-review.yaml` (where `GO:0005759` `mitochondrial matrix` is `SUBFAMILY_ONLY` restricted to `PANTHER:PTHR46118:SF4`), we stay at root `GO:0005739` and do **not** add `GO:0005759` because `abhd-11.1` (`SF3`) is a lineage-specific nematode duplicate with a shorter N-terminus (`44-HGLGG-48` vs `54-HGLGG-58` in `abhd-11.2`) and zero experimental sub-organelle or transit-peptide cleavage data.

## 3. Annotation Review Decisions
- `GO:0005739` (`mitochondrion`, `IBA`, `GO_REF:0000033`): `ACCEPT` (stay at root organelle per `projects/ORGANELLES.md`).
- `GO:0006629` (`lipid metabolic process`, `IBA`, `GO_REF:0000033`): `MARK_AS_OVER_ANNOTATED` (weak single-seed yeast `IMO32` overexpression TAG shift over-propagated across `Eukaryota`).
- `GO:0052689` (`carboxylic ester hydrolase activity`, `IBA`, `GO_REF:0000033`): `ACCEPT` (intact `44-HGLGG-48` oxyanion loop and `Ser114-Asp140-His267` catalytic triad).
