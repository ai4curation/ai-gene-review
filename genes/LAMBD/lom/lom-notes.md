# Gene Review Notes: `lom` (`P03701`, Outer membrane protein lom)

## Overview
- **Gene symbol**: `lom`
- **UniProtKB**: `P03701` (`LOM_LAMBD`), 206 AA (29-residue N-terminal signal peptide cleaved to yield mature 177-AA outer membrane beta-barrel protein)
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Function**: Lysogenic conversion outer membrane beta-barrel protein (`OmpX`/`PagC`/`Rck`/`Ail` family, `IPR000758`) expressed by prophage lambda during lysogeny in *Escherichia coli*. Incorporated into the bacterial host outer membrane, where it contributes to bacterial envelope properties and adhesion to mammalian epithelial cells.

## Key Literature & Evidence
- **[PMID:2144037](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_2144037.md)** (Barondess & Beckwith 1990, *Nature*): Demonstrated that `lom` and `bor` are accessory prophage genes expressed during lysogeny that encode host-cell envelope proteins, with `lom` localized to the bacterial outer membrane and homologous to enterobacterial virulence proteins (`PagC`/`Ail`).

## Review of Existing GO Annotations
- `GO:0020002` (`host cell plasma membrane`, `IEA` from `GO_REF:0000044`): **MODIFY** to `GO:0044384` (`host outer membrane`). In Gram-negative *E. coli*, `lom` is a beta-barrel outer membrane protein localized to the bacterial outer membrane rather than the inner plasma membrane [PMID:2144037], and `GO:0044384` (`host outer membrane`) is already annotated on `lom`.
- `GO:0044384` (`host outer membrane`, `IEA` from `GO_REF:0000002`): **ACCEPT**. Supported by direct experimental localization of Lom to the *E. coli* outer membrane [PMID:2144037].
