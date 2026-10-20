# Curation Notes: Bacillus phage phi29 Gene 12 (Pre-neck appendage protein gp12 / gp12*, P20345)

## Summary of Gene Function
- **Product**: Pre-neck appendage protein gp12 (UniProt `P20345`, 854 aa, ~92.4 kDa precursor), which undergoes post-trimerization intramolecular autocleavage between Ser-691 and Asp-692 to yield the mature 691-aa (~74 kDa) neck appendage protein **gp12\*** and a cleaved C-terminal autochaperone domain (residues 692–854) that is released in an ATP-dependent manner ([PMID:7241648](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_7241648.md), [12-uniprot.txt](file:///Users/cjm/.gemini/antigravity-cli/brain/4b846598-3920-4c66-ba84-db24d924c2d1/scratch/prd1_phi29/genes/BPPH2/12/12-uniprot.txt)).
- **Stoichiometry & Architecture**: Twelve homotrimeric appendages (36 monomers of gp12*) hang radially from the lower collar (`gp11`) around the phi29 neck/tail. Each gp12* monomer contains an N-terminal collar-binding domain, a central right-handed parallel beta-helix pectin lyase-like catalytic domain that binds Ca2+ and Mg2+ and hydrolyzes *Bacillus subtilis* cell wall poly(glycerol phosphate) teichoic acids, and a C-terminal receptor-binding domain stabilized by Zn2+.
- **Biological Role**: Mediates initial reversible adsorption and receptor recognition on the *B. subtilis* surface (`GO:0019062`, `GO:0098671`) and enzymatically degrades cell wall teichoic acids to clear a path through the outer cell wall polymers (`GO:0098994`), allowing the tail tip (`gp13`/`gp9`) to access the underlying peptidoglycan layer.

## Review of Existing GO Annotations
1. `GO:0000166` (`nucleotide binding`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0005524` (`ATP binding`).
2. `GO:0005524` (`ATP binding`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE** — ATP binds the cleaved C-terminal autochaperone domain after post-trimerization autocleavage to trigger its release from mature gp12*; peripheral to the mature virion appendage function.
3. `GO:0019058` (`viral life cycle`, IEA `GO_REF:0000117`): **TOO_GENERAL** — Entailed by `GO:0019062`, `GO:0098671`, and `GO:0098994`.
4. `GO:0019062` (`virion attachment to host cell`, IDA `PMID:7241648` and IEA `GO_REF:0000043`): **ACCEPT** — Directly demonstrated by serum-blocking and purified appendage competition assays in [PMID:7241648](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_7241648.md).
5. `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0098994` (`symbiont entry into host cell via disruption of host cell envelope`).
6. `GO:0046872` (`metal ion binding`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE** — Correct cofactor binding (Ca2+, Mg2+, Zn2+), supportive of structure and catalytic teichoic acid degradation.
7. `GO:0051701` (`biological process involved in interaction with host`, IEA `GO_REF:0000117`): **TOO_GENERAL** — Entailed by `GO:0019062`, `GO:0098671`, and `GO:0098994`.
8. `GO:0098015` (`virus tail`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0098024` (`virus tail, fiber`).
9. `GO:0098024` (`virus tail, fiber`, IEA `GO_REF:0000043`): **ACCEPT** — Mature gp12* trimers form the 12 tail fibers (neck appendages) of the phi29 virion.
10. `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA `GO_REF:0000043`): **ACCEPT** — Core function of the gp12* appendages in binding *B. subtilis* cell wall teichoic acid receptors.
11. `GO:0098994` (`symbiont entry into host cell via disruption of host cell envelope`, IEA `GO_REF:0000043`): **ACCEPT** — Core function of gp12* in digesting host cell wall teichoic acids during entry.
