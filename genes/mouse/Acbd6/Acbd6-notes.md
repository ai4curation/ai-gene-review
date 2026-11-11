# Acbd6 (mouse, UniProtKB:Q9D061) Curation Notes

## Identity and Domain Architecture
- **Gene / Protein**: Mouse `Acbd6` (`UniProtKB:Q9D061`, sequence version 2, 282 aa; `MGI:1919987`; `NCBITaxon:10090`).
- **PANTHER Subfamily**: `PANTHER:PTHR24119:SF0` (*ACYL-COA-BINDING DOMAIN-CONTAINING PROTEIN 6*).
- **Orthology & Sequence Conservation**: 1:1 mammalian ortholog of human `ACBD6` (`UniProtKB:Q9BR61`, 282 aa; ~93% sequence identity). Retains the soluble monomeric architecture with no transmembrane helices:
  - **N-terminal ACB domain** (residues 42–127; `InterPro:IPR000582`): 100% conservation of the human acyl-CoA binding pocket residues `Phe46`, `Tyr69`, `Lys73`, `Lys95`, regulatory phosphorylation serines `Ser106` and `Ser108`, and helix-`αH4` pocket `Tyr114`.
  - **C-terminal ANK-repeat domain** (`ANK1` residues 191–220, `ANK2` residues 224–253; `InterPro:IPR002110`): conserved NMT1/NMT2-binding module.
- **Alternative Splicing Isoforms (`UniProtKB:Q9D061`)**:
  - `Q9D061-1` (canonical, 282 aa): full-length protein containing both the N-terminal ACB domain and C-terminal ANK repeats.
  - `Q9D061-2` (137 aa; `VSP_018003`, `VSP_018004`) and `Q9D061-3` (139 aa; `VSP_018002`, `VSP_018005`): C-terminally truncated splice variants that retain the intact N-terminal ACB domain (residues 42–127) and `Tyr114` pocket—consistent with human `ACBD6-ΔC` retaining acyl-CoA binding (`PMID:18268358`)—but lack both C-terminal ANK repeats required for `NMT1`/`NMT2` binding and competitive protection (`PMID:32108178`). Whether `Q9D061-2` or `Q9D061-3` accumulate as stable endogenous proteins in vivo has not been tested.

## Literature Search Log and ND Policy Assessment
- **Literature search log (2026-11-11)**: Targeted queries of PubMed, Europe PMC, and the local publication cache for `("Acbd6" OR "2610019F03Rik" OR "Q9D061") AND ("mouse" OR "murine" OR "Mus musculus")` identified **0 primary experimental publications** assaying endogenous or recombinant mouse `Acbd6` molecular activity or biological process phenotypes in *Mus musculus*.
- `PMID:37951597` reports adult mouse brain single-cell RNA-seq expression (`Acbd6 is expressed in nearly all regions of the adult mouse brain profiled by single-cell RNA sequencing`), which establishes regional transcript expression rather than a GO molecular function or biological process. UniProt (`UniProtKB:Q9D061`) also annotates similarity-transferred `Phosphoserine` modifications at `Ser41` and `Ser106` without mouse-specific functional perturbation.
- **ND Annotations (`GO:0003674` MF `ND` and `GO:0008150` BP `ND`, `GO_REF:0000015`)**:
  - Because no species-specific experimental literature in *Mus musculus* establishes a molecular function or biological process for mouse `Acbd6`, both MGI `ND` annotations strictly follow `GORULE:0000011`/`GORULE:0000054` and `projects/NO_DATA.md`: both are **ACCEPTED** (`action: ACCEPT`) with **`nd_case: INFERABLE`** (Case N2: not assayed in mouse, while core functions in fatty-acyl-CoA binding `GO:0000062`, NMT enzyme activation `GO:0008047`, protein N-myristoylation regulation, and `LPCAT`-mediated phosphatidylcholine acyl-chain remodeling `GO:0036151` are firmly established in the 93%-identical human ortholog `Q9BR61` and vertebrate `acbd6` models).

## Annotation Audit Summary
- **Retained Core**: `GO:0000062` (`fatty-acyl-CoA binding`, 4 rows: `IBA`, `IEA`, `ISO`, `ISS`), `GO:0008047` (`enzyme activator activity`, 1 `IBA` row), `GO:0005829` (`cytosol`, 2 rows: `IEA`, `ISO`).
- **Accepted ND**: `GO:0003674` (`ND`, `INFERABLE`) and `GO:0008150` (`ND`, `INFERABLE`).
- **Non-Core**: `GO:0005634` (`nucleus`, 3 rows: `IEA`, `ISO`, `ISS`) — genuine secondary localization transferred from human `ACBD6` (`PMID:25604091`, `PMID:37951597`), with core acyl-CoA delivery/NMT activation occurring in the cytosol.
- **Refined (`MODIFY`)**: `GO:0008289` (`lipid binding`, 3 rows -> `GO:0000062` `fatty-acyl-CoA binding`); `GO:0005737` (`cytoplasm`, 3 rows -> `GO:0005829` `cytosol`).
- **Removed (`REMOVE` + `source_defects`)**: `GO:0005783` (`endoplasmic reticulum`, `IBA`) and `GO:0005886` (`plasma membrane`, `IBA`) — false PAINT `PTN001191022` over-propagation from transmembrane *Arabidopsis* `ACBP1`/`ACBP2` (`PMID:12650615`).
