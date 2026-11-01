# kil (P14111) — Curation Notes

## Overview
- **Gene symbol**: `kil`
- **UniProt ID**: `P14111` (`VKIL_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Host cell division inhibitor Kil (62 AA)

## Sequence & Domain Architecture
- **Length**: 62 AA (`file:genes/BPP22/kil/kil-uniprot.txt`)
- **Domains**:
  - `InterPro:IPR020298` (`Kil_phage_P22-type`), `Pfam:PF17519` (`DUF5444`)
  - Note: Although P22 `kil` maps to the same position in the `PL` operon as coliphage lambda `kil` and causes an analogous host cell filamentation and killing phenotype, P22 Kil shares no sequence homology with lambda Kil ([PMID:2738922]).

## Biological Function
- **Inhibitor of host bacterial cell division causing filamentation and cell death**:
  - Semerjian et al. ([PMID:2738922]) identified and sequenced the P22 `kil` gene in the `PL` operon and showed that expression of P22 `kil` inhibits host cell division, causing bacterial filamentation and cell death, and is essential for lytic phage growth in the absence of `abc` (`file:genes/BPP22/kil/kil-uniprot.txt`, [PMID:2738922]).
  - Because the direct molecular target of P22 Kil (`InterPro:IPR020298` / `Pfam:PF17519`) has not been biochemically proven (unlike lambda Kil, which was shown to inhibit FtsZ polymerization in [PMID:24563033]), we annotate `GO:0051782` (`negative regulation of cell division`) and `GO:0030430` (`host cell cytoplasm`) without over-asserting a specific molecular function beyond what is experimentally established.

## Key Literature & Verbatim Evidence
- **[PMID:2738922]** (Semerjian et al., 1989, *Gene*):
  > "P22 kil, like lambda kil, kills the host cell when it is expressed. The two kil genes, although analogous in cell killing and map location, have no apparent sequence homology. The functions of the P22 and lambda kil genes are unknown; however, P22 kil is essential for lytic growth in the absence of abc."
- **`file:genes/BPP22/kil/kil-uniprot.txt`**:
  > `CC   -!- FUNCTION: P22 kil is essential for lytic growth in the absence of abc. Expression of P22 kil causes filamentation and cell death.`

## GO Annotation Decisions
- **Existing GOA**: Empty (`[]`).
- **Proposed `NEW` annotations**:
  - `GO:0051782` (`negative regulation of cell division`, `involved_in`) — expression of P22 Kil causes host cell filamentation (inhibition of cytokinesis/septation) and cell death (`file:genes/BPP22/kil/kil-uniprot.txt`, [PMID:2738922]).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
