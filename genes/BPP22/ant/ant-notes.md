# ant (P03037) — Curation Notes

## Overview
- **Gene symbol**: `ant`
- **UniProt ID**: `P03037` (`RANT_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Antirepressor protein Ant (300 AA)

## Sequence & Domain Architecture
- **Length**: 300 AA (`file:genes/BPP22/ant/ant-uniprot.txt`, [PMID:6350606])
- **Domains**:
  - **N-terminal domain**: `InterPro:IPR018875` (`Antirepressor_Ant_N`), `Pfam:PF10547` (`P22_AR_N`)
  - **C-terminal domain**: `InterPro:IPR018876` (`Phage_P22_antirepressor_C`), `Pfam:PF10548` (`P22_AR_C`)
  - Family signature: `PRINTS:PR01994` (`ANTIREPRESSR`)

## Biological Function
- **Transcription regulator inhibitor (antirepressor) of P22 C2 and related lambdoid phage repressors**:
  - Ant is encoded in the unique `immI` region of phage P22 and transcribed from the `Pant` promoter under the negative control of Mnt and Arc ([PMID:6350606], [PMID:11053393]).
  - Ant binds directly and non-covalently to the P22 C2 immunity repressor (as well as the cI repressors of related lambdoid phages such as lambda and 434), preventing the repressor from binding its operator DNA sites (`OL` and `OR`) without proteolytically cleaving it (`file:genes/BPP22/ant/ant-uniprot.txt`, [PMID:6350606], [PMID:11053393]).
  - By inhibiting C2 repressor activity, Ant derepresses viral transcription from `PL` and `PR` and can induce resident prophages (release from viral latency).

## Key Literature & Verbatim Evidence
- **[PMID:6350606]** (Sauer et al., 1983, *Biochemistry*):
  > "This region includes the ant gene, which encodes the P22 antirepressor protein, and the mnt and arc genes, which encode proteins that negatively regulate antirepressor synthesis. We have purified antirepressor protein and selected tryptic peptides of antirepressor, and have determined the amino terminal sequences and amino acid composition of these molecules. These data, in combination with the DNA sequence, locate the ant gene and define the complete amino acid sequence of antirepressor (300 residues)."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "Another early transcript is initiated from P ant in the unique immI region, giving rise to an antirepressor, Ant, which functions to inhibit c2 repressor function."
- **`file:genes/BPP22/ant/ant-uniprot.txt`**:
  > `CC   -!- FUNCTION: This protein prevents the prophage P22 c2 repressor protein from binding to its operators and also inhibits the action of other prophage repressor proteins, including those of phages lambda and 434. The synthesis of antirepressor is negatively regulated by the protein products of the two other immI genes, mnt and arc.`

## GO Annotation Decisions
- **Existing GOA**: Empty (`[]`).
- **Proposed `NEW` annotations**:
  - `GO:0140416` (`transcription regulator inhibitor activity`, `enables`) — Ant directly inhibits the DNA-binding transcription factor activity of the P22 C2 repressor (and lambda/434 cI repressors).
  - `GO:0046782` (`regulation of viral transcription`, `involved_in`) — by inhibiting the C2 transcriptional repressor, Ant derepresses viral transcription from `PL` and `PR`.
  - `GO:0019046` (`release from viral latency`, `involved_in`) — inhibition of prophage C2/cI repressors by Ant induces resident prophages out of latency.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
