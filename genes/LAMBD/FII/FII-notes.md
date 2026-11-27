# Gene Review Notes: `FII` (`P03714`, Head-tail connector protein FII / gpFII)

## Overview
- **Gene symbol**: `FII`
- **UniProtKB**: `P03714` (`VGF2_LAMBD`), 117 AA
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Function**: Head-tail connector (head completion) protein `gpFII` that assembles as a hexameric ring onto the `gpW`-capped portal vertex of the DNA-filled capsid at the final step of head morphogenesis. `gpFII` forms the bottom surface of the head-tail connector (`gpB12`-`gpW6`-`gpFII6`) and directly binds the tail terminator protein `gpU` of the pre-assembled tail to join the head and tail into an infectious virion. Structurally, `gpFII` shares a conserved fold with the tail tube protein `gpV` and tail terminator protein `gpU`.

## Key Literature & Evidence
- **[PMID:20660769](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_20660769.md)** (Cardarelli et al. 2010, *PNAS*): Solved the solution NMR structure of `gpFII` and mapped its head-binding (N-terminal region interacting with `gpW`) and tail-binding (bottom surface loops interacting with the tail) interfaces via site-directed mutagenesis and dominant-negative assays.

## Review of Existing GO Annotations
- `GO:0019068` (`virion assembly`, `IDA` and `IMP` from `PMID:20660769`, `IEA` from `GO_REF:0000002`): **ACCEPT**. `gpFII` mediates the final step of virion assembly by joining the completed DNA-filled capsid head to the pre-assembled tail [PMID:20660769].
- `GO:0030430` (`host cell cytoplasm`, `IEA` from `GO_REF:0000044`): **ACCEPT**. Head-to-tail joining takes place in the *E. coli* cytoplasm prior to host cell lysis.
