# Gene Review Notes: `Fi` (`P03709`, DNA-packaging protein FI / gpFI)

## Overview
- **Gene symbol**: `Fi`
- **UniProtKB**: `P03709` (`VGFI_LAMBD`), 132 AA
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Function**: Abundant late-expressed DNA-packaging chaperone protein (`gpFI`) that accelerates assembly of the packaging complex by bridging the terminase-concatemeric DNA complex (`Complex I`, `gpA`/`gpNu1`/`IHF`/`cos` DNA) and the major capsid protein `gpE` on the procapsid (`Complex II`). `gpFI` has a two-domain architecture connected by a flexible linker, with its C-terminal domain directly binding the E-loop region of `gpE` on the prohead shell and its N-terminal domain proposed to interact with viral DNA/terminase.

## Key Literature & Evidence
- **[PMID:22801427](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_22801427.md)** (any structural/biochemical study by Davidson lab, *J Biol Chem* 2012): Demonstrated that `gpFI` is a two-domain DNA packaging chaperone whose C-terminal domain directly binds the major head protein `gpE`, and that mutations weakening `gpFI`-`gpE` binding reduce biological activity in viral DNA packaging.

## Review of Existing GO Annotations
- `GO:0019072` (`viral genome packaging`, `IDA` from `PMID:22801427`): **MODIFY** to `GO:0019073` (`viral DNA genome packaging`), as phage lambda is a dsDNA bacteriophage and `gpFI` specifically chaperones packaging of concatemeric viral dsDNA into proheads [PMID:22801427].
- `GO:0030430` (`host cell cytoplasm`, `IEA` from `GO_REF:0000044`): **ACCEPT**. `gpFI` operates in the host bacterial cytoplasm during lytic virion assembly.
