# Acbd6 (rat, UniProtKB:Q5RJK8) Curation Notes

## Identity and Domain Architecture
- **Gene / Protein**: Rat `Acbd6` (`UniProtKB:Q5RJK8`, sequence version 1, 282 aa; `RGD:1305030`; `NCBITaxon:10116`).
- **PANTHER Subfamily**: `PANTHER:PTHR24119:SF0` (*ACYL-COA-BINDING DOMAIN-CONTAINING PROTEIN 6*).
- **Orthology & Sequence Conservation**: 1:1 mammalian ortholog of human `ACBD6` (`UniProtKB:Q9BR61`, 282 aa) and mouse `Acbd6` (`UniProtKB:Q9D061`, 282 aa). Soluble monomeric intracellular protein lacking transmembrane helices:
  - **N-terminal ACB domain** (residues 42–127; `InterPro:IPR000582`): preserves `Phe46`, CoA-headgroup triad `Tyr69`/`Lys73`/`Lys95`, regulatory loop `Ser106`/`Ser108`, and essential acyl-CoA cavity `Tyr114`. Multi-organ rat phosphoproteomics (`PMID:22673903`) directly detected endogenous phosphorylation at `Ser41` immediately preceding helix `αH1` of the ACB domain.
  - **C-terminal ANK-repeat domain** (`ANK1` residues 191–220, `ANK2` residues 224–253; `InterPro:IPR002110`): conserved NMT1/NMT2 interaction module.

## Species-Specific Literature Distinction (`circAcbd6` vs Protein-Coding `Acbd6`)
- Aside from quantitative multi-tissue phosphoproteomics detecting endogenous `Acbd6` `Ser41` phosphorylation across rat organs (`PMID:22673903`), the only rat-specific publication naming `Acbd6` is `PMID:35305988`, which characterizes a back-spliced **circular RNA** (`circAcbd6`) enriched in hippocampal exosomes that acts as a cytoplasmic `miR-320-5p` sponge to upregulate `Osbpl2` and promote neural stem cell differentiation into cholinergic neurons.
- That miRNA-sponge activity belongs strictly to the non-coding `circAcbd6` transcript, **not** to the 282-aa `Q5RJK8` protein product reviewed here, and must not be annotated onto `UniProtKB:Q5RJK8`.

## Annotation Audit Summary
- **Retained Core**: `GO:0000062` (`fatty-acyl-CoA binding`, 4 rows: `IBA`, `IEA`, `ISO`, `ISS`), `GO:0008047` (`enzyme activator activity`, 2 rows: `IBA`, `ISO`), `GO:0005829` (`cytosol`, 2 rows: `IEA`, `ISO`).
- **Non-Core**: `GO:0005634` (`nucleus`, 3 rows: `IEA`, `ISO`, `ISS`) — conserved secondary vertebrate pool transferred from human `ACBD6`.
- **Refined (`MODIFY`)**: `GO:0008289` (`lipid binding`, 3 rows -> `GO:0000062` `fatty-acyl-CoA binding`); `GO:0005737` (`cytoplasm`, 3 rows -> `GO:0005829` `cytosol`).
- **Removed (`REMOVE` + `source_defects`)**: `GO:0005783` (`endoplasmic reticulum`, `IBA`) and `GO:0005886` (`plasma membrane`, `IBA`) — false PAINT `PTN001191022` over-propagation from transmembrane *Arabidopsis* `ACBP1`/`ACBP2` (`PMID:12650615`).
