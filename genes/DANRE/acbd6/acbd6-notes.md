# acbd6 (DANRE, UniProtKB:Q4V8X4) Curation Notes

## Identity and Domain Architecture
- **Gene / Protein**: Zebrafish *Danio rerio* `acbd6` (`UniProtKB:Q4V8X4`, sequence version 1, 300 aa; `ZFIN:ZDB-GENE-030131-2810`; `NCBITaxon:7955`).
- **PANTHER Subfamily**: `PANTHER:PTHR24119:SF0` (*ACYL-COA-BINDING DOMAIN-CONTAINING PROTEIN 6*).
- **Domain Architecture & Verified Pocket Residues (`Q4V8X4`, SV=1)**:
  - Soluble 300-aa vertebrate ACBD6 ortholog lacking transmembrane helices or peroxisomal signals; carries an 18-residue N-terminal extension relative to mammalian `ACBD6`.
  - **N-terminal ACB domain** (residues 60–145; `InterPro:IPR000582`): conserves `Phe64` (aligning to human `Phe46`), CoA headgroup triad `Tyr87`/`Lys91`/`Lys113` (human `Tyr69`/`Lys73`/`Lys95`), regulatory loop `Ser124` (human `Ser106`, whereas the human `Ser108`-equivalent position carries `Glu126`, a proposed structural phosphomimic shared across most ACBD family proteins; `PMID:30642881`), and helix-`αH4` pocket `Tyr132` (human `Tyr114`).
  - **C-terminal ANK-repeat domain** (`ANK1` residues 209–238, `ANK2` residues 242–271; `InterPro:IPR002110`): conserved NMT interaction module; human pathogenic ANK-domain missense equivalent `p.Asp201Gly` introduced into zebrafish `acbd6` cDNA fails to rescue `acbd6` knockout microphthalmia (`PMID:37951597`).

## Experimental Biology in *Danio rerio* (`PMID:37951597`)
- Whole-mount in situ hybridization shows maternal and zygotic `acbd6` expression in early embryos becoming prominent in the developing central nervous system, optic tectum, eye, and head structures by 24–72 hpf (`PMID:37951597`).
- CRISPR/Cas9 F0 and germline `acbd6` loss-of-function zebrafish exhibit reduced eye size (microphthalmia), microcephaly/altered head morphology, movement defects, and progressive developmental delay (`PMID:37951597`).
- Co-injection of wild-type human `ACBD6` mRNA rescues these phenotypes, demonstrating functional conservation between human and zebrafish `ACBD6`, whereas introducing human pathogenic alleles (`p.Glu63Ter` truncating the ACB domain or `p.Asp201Gly` in the ANK repeat) into `acbd6` cDNA abolishes rescue (`PMID:37951597`).
- Click-chemistry proteomics (`YnMyr` labeling) in `acbd6`-deficient zebrafish larvae demonstrated global remodeling of the N-myristoylome: overall `YnMyr`-labeled protein abundance increased while a specific subset of N-myristoylated proteins required for eye, neuron, and muscle development (including `Fus`, `Marcks`, and `Chchd`-family proteins) was significantly reduced (`PMID:37951597`).

## Annotation Audit Summary
- **Retained Core**: `GO:0000062` (`fatty-acyl-CoA binding`, 3 rows: `IBA`—where `ZFIN:ZDB-GENE-030131-2810` is itself a PAINT seed—, `IEA`, and `IMP` `PMID:37951597`) and `GO:0008047` (`enzyme activator activity`, 1 `IBA` row).
- **Non-Core**: `GO:0005634` (`nucleus`, 2 rows: `IEA`, `ISS` from human `Q9BR61`).
- **Refined (`MODIFY`)**: `GO:0008289` (`lipid binding`, `IMP` `PMID:37951597` -> `GO:0000062` `fatty-acyl-CoA binding`); `GO:0005737` (`cytoplasm`, 2 rows: `IEA`, `ISS` -> `GO:0005829` `cytosol`).
- **Removed (`REMOVE` + `source_defects`)**: `GO:0005783` (`endoplasmic reticulum`, `IBA`) and `GO:0005886` (`plasma membrane`, `IBA`) — false PAINT `PTN001191022` over-propagation from transmembrane *Arabidopsis* `ACBP1`/`ACBP2` (`PMID:12650615`).
