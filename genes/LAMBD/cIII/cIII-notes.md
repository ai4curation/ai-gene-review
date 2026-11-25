# cIII (P03044) - Curation Notes

## Overview
- **Gene symbol**: `cIII`
- **UniProt ID**: `P03044` (`RPC3_LAMBD`)
- **Protein name**: Protease inhibitor III (Regulatory protein cIII, 54 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Competitive inhibitor of host FtsH (HflB) metalloprotease**: CIII is a small 54-amino-acid polypeptide expressed from the early leftward promoter `PL` that promotes lysogeny by protecting the phage transcriptional activator CII from rapid degradation by the *Escherichia coli* inner-membrane ATP-dependent metalloprotease FtsH (HflB) [PMID:17426811, "Here we show that the protease inhibitor CIII is present as oligomeric amphipathic alpha helical structures and functions as a competitive inhibitor of FtsH by preventing binding of the CII substrate."; PMID:18721134, "The CIII protein of bacteriophage lambda exhibits antiproteolytic activity against the ubiquitous metalloprotease HflB (FtsH) of Escherichia coli, thereby stabilizing the lambdaCII protein and promoting lysogenic development of the phage."].
- **Amphipathic alpha-helical structure and direct FtsH binding**: A conserved central region of CIII (residues 14-37) forms an oligomeric amphipathic alpha-helix that binds directly to FtsH, competitively blocking access of both phage CII and the host heat-shock sigma factor sigma32 (RpoH) to the protease, while CIII itself is also slowly degraded by FtsH [PMID:17426811; PMID:18721134].

## Review of Existing GO Annotations
- `GO:0019042` (viral latency, IEA, `GO_REF:0000043`): **ACCEPT**. By inhibiting host FtsH and stabilizing CII, CIII directly promotes the establishment of viral latency (lysogeny).
- In `core_functions`, we also capture CIII's core molecular activity as `GO:0008237` / `GO:0004866` (endopeptidase inhibitor activity) or `GO:0030414` (peptidase inhibitor activity) alongside `GO:0019042` (viral latency).
