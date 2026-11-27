# W (P68660) - Head-to-tail joining protein W (gpW)

## Summary
- **Gene symbol**: `W`
- **UniProt ID**: `P68660`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Head-to-tail joining protein W (`gpW`, 68 aa)

## Biological Function
- Structural head-completion / neck adaptor protein (`gpW`) that assembles as a hexameric ring on the portal vertex (`gpB` dodecamer) immediately after unit-length viral DNA packaging is completed and the terminase complex dissociates [PMID:14569303, PMID:20660769].
- Forms the middle ring of the lambda head-tail connector (`gpB`-`gpW`-`gpFII`), plugging the portal channel to prevent egress of the tightly packaged dsDNA chromosome from the mature head and creating the binding interface required for subsequent incorporation of six copies of `gpFII` and attachment of the pre-assembled tail [PMID:14569303, PMID:20660769].
- NMR solution structure (`PMID:14569303`) reveals a compact $\alpha/\beta$ fold (two $\alpha$-helices packed against a two-stranded antiparallel $\beta$-hairpin) with a disordered C-terminal tail containing a conserved hydrophobic Leu-Pro-Met-Leu-Arg motif essential for assembly into the virion head.

## Curation Decisions
- **MODIFY**:
  - `GO:0019058` (`viral life cycle`, IEA `GO_REF:0000002`) -> `GO:0019069` (`viral capsid assembly`) (and `GO:0019068` `virion assembly`), because `gpW` specifically functions as the head-completion adaptor protein that stabilizes packaged DNA inside the capsid head and recruits `gpFII` for head-to-tail joining [PMID:14569303, PMID:20660769].
- **Core Function**:
  - Structural constituent of the virion head-tail connector (`GO:0039660` `structural constituent of virion`) involved in `GO:0019069` (`viral capsid assembly`) and `GO:0019068` (`virion assembly`), located in `GO:0019028` (`viral capsid`) and `GO:0030430` (`host cell cytoplasm`).
