# Curatorial Notes for Human `ACCSL` (`UniProtKB:Q4AC99`)

## 1. Gene & Family Identity
- **HGNC symbol**: `ACCSL` (`HGNC:34391`, *1-aminocyclopropane-1-carboxylate synthase homolog (inactive) like*)
- **UniProtKB**: `Q4AC99` (`1A1L2_HUMAN`, reviewed, 568 aa, sequence version 3; Pharos `Tdark`)
- **Genomic locus**: Human chromosome 11p11.2 (`ENSG00000205126`), located immediately adjacent to its ancestral vertebrate paralog `ACCS` (`Q96QU6`, 50% amino-acid identity), from which `ACCSL` arose via mammalian-specific tandem duplication (`PMID:39876065`).
- **PANTHER classification**: `PANTHER:PTHR43795:SF1` (*INACTIVE 1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 2-RELATED*), a 10-leaf eutherian clade gated by PAINT `IKR` loss at `PANTHER:PTN000202914` (`NOT GO:0016846`).

## 2. Active-Site Sequence Audit (`Q4AC99`, `sv: 3` vs Human `ACCS` `Q96QU6`, `sv: 1`)
Direct inspection of `Q4AC99` (`genes/human/ACCSL/ACCSL-uniprot.txt`, 568 aa, offset `+72` relative to `Q96QU6` across the catalytic core) and Gao et al. 2025 (`PMID:39876065`):
- **Retained PLP-pocket core residues**:
  - `K395` (`Q4AC99:395` = `K`, corresponding to `Q96QU6:323` = `K`): **RETAINED**! Annotated as `MOD_RES 395 N6-(pyridoxal phosphate)lysine` by sequence similarity (`ECO:0000250`), though actual cofactor occupancy has never been experimentally measured on purified `ACCSL`.
  - `D358` (`Q4AC99:358` = `D`, corresponding to `Q96QU6:286` = `D`): **RETAINED** fold-type I pyridinium-stabilizing aspartate.
  - `R403` (`Q96QU6:331` = `R`), `N330` (`Q96QU6:258` = `N`), `Y267` (`Q96QU6:195` = `Y`), `Y204` (`Q96QU6:132` = `Y`), and `W207` (`Q96QU6:135` = `W`): **RETAINED**.
- **Natural active-site substitutions in `hACCSL` (`PMID:39876065`)**:
  1. `C529` (`Q4AC99:529` = `C`, corresponding to substrate alpha-carboxylate-anchoring `R457` in `Q96QU6`): **LOST** in the reference human sequence! Replicating this human-specific substitution in `hACCS` (`R457C`) decreases C-beta-S lyase activity **100-fold** (`PMID:39876065`). Notably, `UniProtKB:Q4AC99` records a natural human coding polymorphism `VAR_060626` (`p.Cys529Arg`, `dbSNP:rs2074051`) that restores `Arg529` (the ancestral residue conserved in non-human mammalian `ACCSL` orthologs such as mouse `Q3UX83` `R551` and rat `D3ZUW2` `R553`).
  2. `Y423` (`Q4AC99:423` = `Y`, corresponding to partner-subunit cationic pocket `R351` in `Q96QU6`): **LOST** across all mammalian `ACCSL` orthologs (`Y445` in mouse `Q3UX83`, `Y447` in rat `D3ZUW2`)! Replicating `R351Y` in `hACCS` decreases C-beta-S lyase activity **~40-fold** (`PMID:39876065`).
  3. `S273` (`Q4AC99:273` = `S`, corresponding to `H201` in `Q96QU6`).
- Based on `C529` and `Y423`, Gao et al. 2025 hypothesized that human `ACCSL` is either a pseudoenzyme or recognizes a completely different class of substrates, explicitly noting that direct in vitro biochemical characterization of `hACCSL` awaits future study [PMID:39876065, "In light of these two “loss-of-function” substitutions (i.e. C529 and Y423) naturally found in hACCSL, we hypothesize that hACCSL is either a pseudoenzyme as predicted, or it possess a totally different function and recognizes substrates different from what we used in this study, a phenomenon known for some psuedokinases.[33] Direct biochemical characterization of hACCSL in vitro would answer this question in the future;"].

## 3. Targeted Literature Search Log
- Systematic PubMed searches conducted on 2026-11-12 for `"ACCSL"`, `"Q4AC99"`, `"ENSG00000205126"`, `"390110"[uid]`, and `"1-aminocyclopropane-1-carboxylate synthase-like protein 2"` returned only `PMID:39876065` (comparative bioinformatics, AlphaFold2 modeling, and surrogate mutagenesis in `hACCS` `R457C`/`R351Y`) and chromosome 11 sequencing (`PMID:16554811`). Zero publications report purification, cofactor-binding measurements, enzymatic assays, subcellular localization, or cellular loss-of-function phenotypes directly on human `ACCSL`.

## 4. Affinage Deep-Research Audit (`ACCSL-deep-research-affinage.md`)
- Affinage returned `n_discoveries: 0`, `citation_count: 0`, `"No mechanistic discoveries found in literature."`
- While this reflects the genuine absence of wet-lab biochemical experiments directly assaying purified `ACCSL`, Affinage missed `PMID:39876065`, which contains a dedicated section (*"Molecular insights for hACCSL function"*) modeling `Q4AC99`, identifying `C529`, `Y423`, and `S273`, and testing the surrogate `R457C` and `R351Y` mutations in `hACCS`.
