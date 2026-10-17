# Gene Review Notes: `bor` (`P26814`, Lipoprotein bor)

## Overview
- **Gene symbol**: `bor`
- **UniProtKB**: `P26814` (`BOR_LAMBD`), 97 AA (16-residue lipoprotein signal peptide cleaved at Cys17, which is N-palmitoylated and S-diacylglyceroylated)
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Function**: Lysogenic conversion cell-envelope lipoprotein expressed by prophage lambda during lysogeny in *Escherichia coli*. Highly homologous to the plasmid ColV2-K94 `iss` (increased serum survival) virulence determinant, Bor localizes to the bacterial host cell envelope/outer membrane and confers resistance to complement-mediated serum killing of the lysogenic *E. coli* host.

## Key Literature & Evidence
- **[PMID:2144037](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_2144037.md)** (Barondess & Beckwith 1990, *Nature*): Identified `bor` as a prophage gene expressed during lysogeny encoding a host-cell envelope protein homologous to `iss` that significantly increases survival of *E. coli* host cells in animal serum.

## Review of Existing GO Annotations
- `GO:0020002` (`host cell plasma membrane`, `IEA` from `GO_REF:0000044`): **ACCEPT** (or `MODIFY` to `GO:0044384` `host outer membrane`). Note that UniProt subcellular location `SL-0375` (`Host cell membrane`) maps via `GO_REF:0000044` to `GO:0020002` (`host cell plasma membrane`), and Barondess & Beckwith (1990) [PMID:2144037] describe `bor` and `lom` as encoding host-cell envelope proteins (`file:LAMBD/bor/bor-uniprot.txt` annotates `Host cell membrane; Lipid-anchor`). Accepting `GO:0020002` (or refining to `GO:0044384`) captures its localization to the bacterial host cell envelope membrane.
