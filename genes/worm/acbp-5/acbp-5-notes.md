# acbp-5 (worm, UniProtKB:Q9XVJ0) Curation Notes

## Identity and Domain Architecture
- **Gene / Protein**: *Caenorhabditis elegans* `acbp-5` (`UniProtKB:Q9XVJ0`, sequence version 2, 274 aa; WormBase `WB:WBGene00011731`, sequence/cosmid name `T12D8.3`; `NCBITaxon:6239`).
- **PANTHER Subfamily**: `PANTHER:PTHR24119:SF0` (*ACYL-COA-BINDING DOMAIN-CONTAINING PROTEIN 6*).
- **Domain Architecture & Verified Pocket Residues (`Q9XVJ0`, SV=2)**:
  - Soluble 274-aa nematode ankyrin-repeat acyl-CoA-binding protein (`CeACBP-5`) lacking transmembrane helices or signal peptides; one of three multidomain ACBP-domain paralogs alongside four basal cytosolic ACBPs in *C. elegans* (`PMID:21539519`).
  - **N-terminal ACB domain** (residues 28–114; `InterPro:IPR000582`): conserves CoA headgroup triad `Tyr56`/`Lys60`/`Lys82` (aligning to human `Q9BR61` `Tyr69`/`Lys73`/`Lys95`) and helix-`αH4` acyl-chain pocket `Tyr101` (aligning to human `Tyr114`).
  - **C-terminal ANK-repeat domain** (UniProt `FT REPEAT` 222–254 within the C-terminal two-ankyrin-repeat module; `InterPro:IPR002110`): tandem ankyrin repeats homologous to the NMT-binding module of human `ACBD6` (*C. elegans* encodes cytosolic N-myristoyltransferase `nmt-1`, `WBGene00003771`).

## Experimental Biology in *C. elegans* (`PMID:21539519`, `PMID:36551154`)
- Elle et al. (`PMID:21539519`) analyzed all seven *C. elegans* ACBP paralogs (`acbp-1` through `acbp-7`) and demonstrated that each paralog—including `acbp-5`—functionally complements the growth defect of `ACB1`-deficient *Saccharomyces cerevisiae* cells, establishing in vivo fatty-acyl-CoA binding/carrier activity.
- `ACBP-5` exhibits tissue-restricted expression in the adult pharynx and intestine (highest in the anterior intestine), and functional disruption/downregulation of `acbp-5` elevates intestinal lipid droplet abundance (~1.4-fold over wild type; noted in WormBase `WB:WBGene00011731` and contrasted with human `ACBD6.KO` cells in `PMID:36551154`).

## External MOD Description Audit (`acbp-5-deep-research-wormbase.md`)
- WormBase's hand-written `MOD_provided_gene_description` (`WB:WBGene00011731`, uncited and undated) states:
  `"acbp-5 encodes a highly conserved protein containing a functional acyl-CoA-binding binding domain required for protein stability and ligand binding; contains two ankyrin repeats which may mediate interactions with other proteins; Disruption of ACBP-5 function results in 1.4 times more lipid droplets than in wildtype; ACBP-5 localizes in adult pharynx and intestine with highest expression in anterior part of the intestine."`
- **Audit Verdict (`VERIFIED`, `relevance: HIGH`)**:
  - Biological claims match `PMID:21539519` (Elle et al. 2011; cached abstract-only in `publications/PMID_21539519.md`, with the ~40% lipid-droplet increase upon `CeACBP-5` downregulation independently corroborated in full-text `PMID:36551154` citing Elle et al.).
  - Recorded `source_defects` (`resource: WORMBASE`, `record: WB:WBGene00011731`, `slot: MOD_provided_gene_description`, `defect_type: MISSING_STATEMENT`, `requested_change: ADD`, `asserted_value: WB:WBGene00011731`, `confidence: PROBABLE`): the WormBase summary omits the key functional rescue experiment in `PMID:21539519` showing that `acbp-5` complements the growth defect of ACBP-deficient yeast cells, and also contains a minor duplicated-word typo (`"acyl-CoA-binding binding domain"`).

## Annotation Audit Summary
- **Retained Core**: `GO:0000062` (`fatty-acyl-CoA binding`, 2 rows: `IBA`, `IEA`).
- **Retained Non-Core**: `GO:0008047` (`enzyme activator activity`, 1 `IBA` row) — conserved soluble `ACB + ANK` architecture and presence of *C. elegans* `nmt-1`, kept as `KEEP_AS_NON_CORE` pending direct biochemical testing of `ACBP-5`–`NMT-1` activation in nematodes.
- **Removed (`REMOVE` + `source_defects`)**: `GO:0005783` (`endoplasmic reticulum`, `IBA`) and `GO:0005886` (`plasma membrane`, `IBA`) — false PAINT `PTN001191022` over-propagation from transmembrane *Arabidopsis* `ACBP1`/`ACBP2` (`PMID:12650615`).
