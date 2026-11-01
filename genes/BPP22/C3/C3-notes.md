# C3 (P14110) — Curation Notes

## Overview
- **Gene symbol**: `C3` (`c3`)
- **UniProt ID**: `P14110` (`RPC3_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein C3 (52 AA), the homolog and functional analog of phage lambda cIII.

## Sequence & Domain Architecture
- **Length**: 52 AA (`file:genes/BPP22/C3/C3-uniprot.txt`)
- **Domains & Classification**:
  - `MEROPS:I75.001` (Bacteriophage lambda CIII peptidase inhibitor family)
  - `InterPro:IPR013056` (`Phage_lambda_CIII`), `Pfam:PF02061` (`Lambda_CIII`), `PROSITE:PS00553` (`LAMBDA_PHAGE_CIII`)

## Biological Function
- **Endopeptidase inhibitor that stabilizes the C1 (cII-like) transcriptional activator to promote lysogeny**:
  - Semerjian et al. ([PMID:2738922]) sequenced the P22 `PL` operon and demonstrated that P22 `c3` is both sequence-homologous and functionally analogous to coliphage lambda `cIII`.
  - Like lambda cIII (`MEROPS:I75.001`), P22 C3 acts as a competitive inhibitor of the host ATP-dependent metalloprotease FtsH (HflB), protecting the unstable phage transcriptional activator C1 (the P22 homolog of lambda cII) from rapid proteolytic degradation (`file:genes/BPP22/C3/C3-uniprot.txt`, [PMID:2738922]).
  - Stabilization of C1 enables activation of the `PRE` and `Pa23` promoters, driving `c2` repressor expression and promoting the establishment of lysogeny (`file:genes/BPP22/C3/C3-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:2738922]** (Semerjian et al., 1989, *Gene*):
  > "In addition, three new genes have been identified: ral, kil and arf. Genes ral and c3 are homologous, as well as functionally analogous, to lambda ral and cIII, respectively."
- **`file:genes/BPP22/C3/C3-uniprot.txt`**:
  > `CC   -!- FUNCTION: Presence of the CIII protein in the cell results in the stabilization of the CII transcriptional activator (a very unstable protein), CII activates CI, the gene for repressor, and thus promotes the establishment of lysogeny.`
  > `DR   MEROPS; I75.001; -.`
  > `DR   InterPro; IPR013056; Phage_lambda_CIII.`

## GO Annotation Decisions
- **Existing GOA**: Empty (`[]`).
- **Proposed `NEW` annotations**:
  - `GO:0004866` (`endopeptidase inhibitor activity`, `enables`) — C3 belongs to the MEROPS I75 peptidase inhibitor family (`MEROPS:I75.001`, `InterPro:IPR013056`) and inhibits proteolytic degradation of the C1 (cII) activator.
  - `GO:0046782` (`regulation of viral transcription`, `involved_in`) — by stabilizing the C1 transcriptional activator against proteolysis, C3 promotes C1-dependent viral transcription and establishment of lysogeny.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell.
