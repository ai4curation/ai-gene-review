# xis (P04889) — Curation Notes

## Overview
- **Gene symbol**: `xis`
- **UniProt ID**: `P04889` (`VXIS_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Excisionase (116 AA)

## Sequence & Domain Architecture
- **Length**: 116 AA (`file:genes/BPP22/xis/xis-uniprot.txt`)
- **Domains**:
  - `InterPro:IPR041657` (`HTH_17`), `Pfam:PF12728` (`HTH_17`) — excisionase helix-turn-helix DNA-binding domain.
  - Monomeric in solution (`Mr` ~ 12.9 kDa), oligomerizing cooperatively upon binding the four repeated subsite motifs (`X1`–`X4`) on `attR` / `attP` DNA ([PMID:18502866]).

## Biological Function
- **Architectural DNA-binding recombination directionality factor (excisionase) required for prophage excision**:
  - P22 Xis is an architectural DNA-binding protein essential, together with P22 integrase (Int) and host IHF, for site-specific excisive recombination (`attL` x `attR`) that excises the P22 prophage from the host *Salmonella* chromosome ([PMID:3491212], [PMID:18502866], `file:genes/BPP22/xis/xis-uniprot.txt`).
  - Mattis et al. ([PMID:18502866]) purified P22 Xis and demonstrated by EMSA, footprinting, cross-linking, and circular permutation DNA-bending assays that P22 Xis binds a region on the `P` arm of `attR` containing three direct 6-bp `TTTGCA` repeats (`X1`, `X2`, `X3`) and one imperfect repeat `TTTCGA` (`X4`), inducing a sharp DNA bend of approximately 137 degrees to promote assembly of the excisive intasome while inhibiting integrative recombination.

## Key Literature & Verbatim Evidence
- **[PMID:18502866]** (Mattis et al., 2008, *J Bacteriol*):
  > "We purified P22 Xis and studied the protein in vitro by means of electrophoretic mobility shift assays and footprinting, cross-linking, gel filtration stoichiometry, and DNA bending assays. We identified one protected site that is bent approximately 137 degrees when bound by P22 Xis."
  > "Inspection of the protected DNA sequence revealed a 6-bp “TTTGCA” motif that is directly repeated three times (X1, X2, and X3) and imperfectly repeated once as “TTTCGA” (X4)"
- **[PMID:3491212]** (Leong et al., 1986, *J Mol Biol*):
  > "In this study, we have identified and sequenced the int and xis genes of phi 80 and P22. phi 80 int and xis were identified using a plasmid recombination assay in vivo, and the P22 genes were mapped using Tn1 insertion mutations. In all three phage, the site-specific recombination genes are located directly adjacent to the phage attachment site."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`) -> `ACCEPT` (directly binds and bends `X1`–`X4` repeats in `attR` DNA, [PMID:18502866]).
  2. `GO:0006310` (`DNA recombination`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0032359` (`provirus excision`), which is already present on the record and captures the specific recombination process mediated by Xis.
  3. `GO:0032359` (`provirus excision`, IEA, `GO_REF:0000043`) -> `ACCEPT` (core biological process of Xis).
- **Proposed `NEW` annotations**:
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
