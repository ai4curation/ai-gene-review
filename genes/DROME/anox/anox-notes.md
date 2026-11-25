# anox / Acbp-Ank (DROME, UniProtKB:Q9VRG6) Curation Notes

## Identity, Nomenclature, and Dicistronic Locus Architecture
- **Gene / Protein**: *Drosophila melanogaster* `anox` (`UniProtKB:Q9VRG6`, sequence version 2, 243 aa; FlyBase `FBgn0064116`, current FlyBase symbol `Acbp-Ank`, annotation ID `CG33713`; `NCBITaxon:7227`).
- **PANTHER Subfamily**: `PANTHER:PTHR24119:SF0` (*ACYL-COA-BINDING DOMAIN-CONTAINING PROTEIN 6*).
- **MOD Description Check**: `mod-description-deep-research DROME anox` returned `no_curated: 1` (FlyBase provides no hand-written `MOD_provided_gene_description` for `FBgn0064116`).
- **Dicistronic Locus Provenance (`PMID:18773904`, `PMID:21917925`)**:
  - Originally identified via P-element insertion `GS1189` in the dicistronic transcription unit `CG33071` (`anorexia` / `Anox`), which altered larval sugar/fatty-acid food preference (`PMID:18773904`) and severely reduced larval feeding activity (`PMID:21917925`).
  - The dicistronic `CG33071` mRNA contains two non-overlapping open reading frames subsequently split by FlyBase into `CG33714` (5' ORF encoding an RRM domain protein) and `CG33713` / `FBgn0064116` (`Acbp-Ank`, 3' ORF encoding the 243-aa ACBP-ANK protein `UniProtKB:Q9VRG6`).
  - Crucially, Ryuda et al. (`PMID:21917925`) raised antibodies against both predicted ORFs and showed by immunoblotting of larval extracts a clear band reacting with anti-ACBP-ANK IgG and **no** band reacting with anti-RRM antibody, demonstrating that `Q9VRG6` (`ACBP-ANK`) is the translated endogenous protein product acting in normal larvae.

## Domain Architecture & Sequence-Verified Pocket Residues (`Q9VRG6`, SV=2)
- Soluble 243-aa intracellular protein lacking any transmembrane domain or signal peptide.
- **N-terminal ACB domain** (residues 9–94; `InterPro:IPR000582`): conserves CoA headgroup triad `Tyr36`/`Lys40`/`Lys62` (aligning to human `Q9BR61` `Tyr69`/`Lys73`/`Lys95`) and helix-`αH4` acyl-chain pocket `Tyr81` (aligning to human `Tyr114`), as well as serines `Ser73` and `Ser75` at the positions aligning to human regulatory loop `Ser106` and `Ser108` (insect phosphorylation not yet assayed).
- **C-terminal ANK-repeat domain** (`ANK1` residues 148–180, `ANK2` residues 181–213; `InterPro:IPR002110`): two tandem ankyrin repeats homologous to the NMT-binding ANK module of human `ACBD6`. *Drosophila* encodes a single essential cytosolic N-myristoyltransferase (`Nmt`, `FBgn0002942`), making NMT interaction/activation plausible though not yet directly assayed in fly.

## Physiological Biology (`PMID:18773904`, `PMID:21917925`)
- Expressed in cephalic chemosensory organs (gustatory/olfactory sensilla) and central nervous system (CNS) neurons of larvae and adults (`PMID:21917925`).
- `Anox` loss-of-function mutants abolish larval feeding and mouth-hook contraction rates and reduce adult post-starvation meal intake; CNS-specific overexpression and RNAi knockdown of `Anox` respectively elevate and repress expression of the *Drosophila* insulin receptor gene (`dInR` / `InR`), modulating feeding behavior downstream of neuronal lipid/acyl-CoA sensing (`PMID:21917925`).

## Annotation Audit Summary
- **Retained Core**: `GO:0000062` (`fatty-acyl-CoA binding`, 3 rows: `IBA`, `IEA`, `ISM` `PMID:21917925`).
- **Retained Non-Core**:
  - `GO:0008047` (`enzyme activator activity`, 1 `IBA` row): phylogenetically supported via the conserved soluble `ACB + ANK` architecture and presence of cytosolic *Drosophila* `Nmt`, kept as `KEEP_AS_NON_CORE` consistent with `PTHR24119-review.yaml` because direct `Acbp-Ank`–`Nmt` enzymatic stimulation has not yet been biochemically assayed in insects.
  - `GO:0007631` (`feeding behavior`, 1 `IMP` row with `acts_upstream_of`, `PMID:21917925`): organism-level behavioral output downstream of neuronal `dInR` regulation rather than the direct molecular reaction of the acyl-CoA carrier.
- **Removed (`REMOVE` + `source_defects`)**: `GO:0005783` (`endoplasmic reticulum`, `IBA`) and `GO:0005886` (`plasma membrane`, `IBA`) — false PAINT `PTN001191022` over-propagation from transmembrane *Arabidopsis* `ACBP1`/`ACBP2` (`PMID:12650615`).
