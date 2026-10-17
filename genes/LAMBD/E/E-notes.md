# Gene Review Notes: `E` (`P03713`, Major capsid protein gpE)

## Overview
- **Gene symbol**: `E`
- **UniProtKB**: `P03713` (`CAPSD_LAMBD`), 341 AA
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Function**: Major capsid protein (`gpE`, HK97-fold family) that self-assembles around the `gpNu3` internal scaffold and `gpB` portal ring to form the $T=7$ *laevo* icosahedral procapsid shell (405 copies per head: 60 hexamers and 11 pentamers, with the 12th vertex occupied by the portal). Upon viral DNA packaging, the `gpE` shell undergoes a large irreversible conformational expansion (from ~50 nm to ~60 nm diameter, thinning the shell wall and exposing hydrophobic E-loops at three-fold and quasi-three-fold axes for `gpD` decoration). A subset (10–12 copies) of `gpE` is covalently fused and proteolytically processed with `gpC` to form minor capsid proteins `pX1` and `pX2`.

## Key Literature & Evidence
- **[PMID:265585](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_265585.md)** (Murialdo 1979, *Virology*): Demonstrated in vitro assembly of biologically active lambda proheads in host cytoplasmic extracts, showing that `gpE` monomers or small oligomers polymerize with `gpNu3`, `gpB`, and `gpC` to form proheads.
- **[PMID:2141087](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_2141087.md)** (Katsura 1990, *J Mol Biol*): Genetic and mutational dissection of the form-determining major capsid protein `gpE`, showing that single amino acid substitutions in `gpE` alter head shell size/shape (petit or monster heads) or block head maturation.
- **[PMID:8411174](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_8411174.md)** (Dokland & Murialdo 1993, *J Mol Biol*): Cryo-EM reconstruction of procapsids and mature capsids demonstrating that `gpE` forms hexamers and pentamers on a $T=7$ icosahedral lattice, and undergoes dramatic subunit rotation and flattening during procapsid-to-capsid expansion.

## Review of Existing GO Annotations
- `GO:0019028` (`viral capsid`, `IDA` from `PMID:2141087` and `IEA` from `GO_REF:0000120`): **MODIFY** to `GO:0039620` (`T=7 icosahedral viral capsid`), which is already annotated on `E` and captures the exact $T=7$ icosahedral architecture established by cryo-EM [PMID:8411174].
- `GO:0039620` (`T=7 icosahedral viral capsid`, `IDA` from `PMID:8411174` and `IEA` from `GO_REF:0000043`): **ACCEPT**.
- `GO:0030430` (`host cell cytoplasm`, `EXP` from `PMID:265585` and `IEA` from `GO_REF:0000044`): **ACCEPT**. `gpE` is synthesized and assembles into procapsids in the *E. coli* cytoplasm.
