# Curation Notes for Schizosaccharomyces pombe SPAC22H12.03 (UniProtKB:O94437)

## 1. Identity, Active-Site Conservation, and Organelle Localization (`PANTHER:PTHR46118:SF4`)
- **Gene / UniProtKB**: `SPAC22H12.03` (`UniProtKB:O94437`, reviewed Swiss-Prot entry `YFI3_SCHPO`, 270 aa, `sv=1`).
- **Active-site alignment (`file:human/ABHD11/ABHD11-bioinformatics/RESULTS.md`)**:
  - `SPAC22H12.03` (`O94437`) is the sole *Schizosaccharomyces pombe* member of `PANTHER:PTHR46118:SF4` (`FT DOMAIN 21..257`), conserving the canonical oxyanion-hole loop `28-HGLGG-32` and the complete charge-relay catalytic triad: `Ser95` (`91-LVGHSMGGK-99`), beta-6 `Asp119` (`115-LIAIDISPV-123`), and loop `His250` (`246-PKAGHYIHA-254`). (Note that Swiss-Prot `FT ACT_SITE 190` is an automated beta-7 projection from `Q6DRD9`, whereas structural alignment to *E. coli* YbfF `PDB:3BF7` `PMID:18215690` and yeast Eat1 `FT ACT_SITE 139` identifies beta-6 `Asp119` as the conserved triad acid.)
- **Mitochondrial localization (`projects/ORGANELLES.md`)**:
  - Direct proteome-wide YFP-tagging microscopy in *S. pombe* (`PMID:16823372`) localized `SPAC22H12.03` to the mitochondrion (`GO:0005739`, `HDA`), reinforced by PAINT `IBA` (`GO_REF:0000033` from `PTN000106239`) and UniProt SubCell `IEA` (`GO_REF:0000044`).
  - Per `projects/ORGANELLES.md`, all three `GO:0005739` rows are `ACCEPT`, and we stay at root `GO:0005739` without proposing `NEW` `GO:0005759` (`mitochondrial matrix`) because `O94437` is a compact 270-aa sequence lacking a mapped cleavable N-terminal transit peptide (`FT CHAIN 1..270` in `SPAC22H12.03-uniprot.txt`) and has no sub-mitochondrial fractionation or matrix enzyme-complex assay in *S. pombe* (only whole-organelle YFP fluorescence).

## 2. Trans-Kingdom ISS Audit (`GO:0006631` from *E. coli* `ybfF` `UniProtKB:P75736`)
- PomBase carries `GO:0006631` (`fatty acid metabolic process`, `ISS`, `GO_REF:0000024`, `supporting_entities: [UniProtKB:P75736]`), projected from bacterial *Escherichia coli* K-12 `ybfF` (`PMID:18215690`), which hydrolyzed palmitoyl-CoA and malonyl-CoA in vitro.
- However:
  1. Even in *E. coli*, `ybfF` was characterized structurally and biochemically in vitro (`PMID:18215690`) without genetic evidence establishing an in vivo fatty-acid metabolic pathway role.
  2. Eukaryotic mitochondrial `PTHR46118:SF4` homologs diverge sharply in substrate specificity across kingdoms: human `ABHD11` explicitly does **not** hydrolyze long-chain acyl-CoAs (`oleoyl-CoA` or `arachidonoyl-CoA`, `PMID:27544863`) and instead deglutarylates lipoylated OGDHc (`PMID:40664791`), while budding yeast `Eat1` catalyzes mitochondrial ethanol O-acetyltransfer (`PMID:28356220`).
- Therefore, both `GO:0006631` (`fatty acid metabolic process`, `ISS` from `P75736`) and `GO:0006629` (`lipid metabolic process`, `IBA` from yeast `IMO32` overexpression TAG shifts) are `MARK_AS_OVER_ANNOTATED`, while `GO:0052689` (`carboxylic ester hydrolase activity`, `IBA`) is `ACCEPT`.
