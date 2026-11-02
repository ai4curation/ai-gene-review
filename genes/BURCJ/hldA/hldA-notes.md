# hldA review notes

## 2026-10-25: ADP-heptose module audit

RCSB 4E84 entity 1 contains 352 residues, including the complete 316-residue B4EB35 sequence at zero-based offset 36. Its source taxon is 216591 (J2315), and the SIFTS reference covers 100% of B4EB35. PMID23256532 uses K56-2 for its genetic complementation assays, so that phenotype is not described as a J2315 assay.

Mapping was checked against https://data.rcsb.org/rest/v1/core/polymer_entity/4E84/1 and the fetched UniProt sequence by exact substring comparison after removing sequence-line whitespace. N-terminal construct residues were excluded by locating the full native sequence; no inference of native activity was made from a PANTHER label.

The split HldA/HldC system is distinguished from fused HldE. PANTHER labels containing “BIFUNCTIONAL PROTEIN HLDE” cannot establish that both activities are present in a monofunctional representative. GO definitions were retrieved from QuickGO on 2026-10-25: GO:0016773 requires an alcohol acceptor, whereas GO:0016779 transfers a nucleotidyl group; HldC acts on the sugar phosphate.

Default Falcon research and perplexity-lite fallback were attempted concurrently with publication caching. Falcon returned HTTP403 and the fallback failed authentication/quota; no provider report was authored manually. Manual source review underlies these decisions. FEBA fetch was attempted but no local or reachable source was available for this organism.

PMID:23256532 directly supports kinase chemistry and the homodimeric structure. Its full text states: “HldA and HldC are homologous to the N- and the C-terminal domains of HldE, respectively.” The cytosol annotation remains UNDECIDED because neither structural nor complementation evidence directly localizes the native protein. Two electronic nucleotidyltransferase claims are contradicted by the single kinase architecture.
