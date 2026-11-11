# C (P03711) - Protease C (gpC) and Scaffolding protein Nu3 (gpNu3)

## Summary
- **Gene symbol**: `C`
- **UniProt ID**: `P03711`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Capsid maturation serine protease `gpC` (439 aa, `P03711-1`) and internal in-frame overlapping scaffolding protein `gpNu3` (145 aa, `P03711-2`, corresponding to the C-terminal residues 295-439 of `gpC`).

## Biological Function
- **Scaffolding protein `gpNu3` (`P03711-2`)**: Expressed from an internal in-frame translation initiation site within gene `C`. Transiently associates (~100-200 copies) with the portal complex (`gpB`), major capsid protein (`gpE`), and `gpC` to promote proper icosahedral procapsid assembly before being proteolytically degraded and expelled from the prohead [PMID:20620152, PMID:21821043, PMID:21943085].
- **Procapsid maturation protease `gpC` (`P03711-1`)**: Incorporates into the procapsid by sharing the C-terminal scaffolding domain (`gpNu3`) and contains an N-terminal S78/ClpP-like serine protease domain with an unusual Ser164-His132-Asp catalytic triad [PMID:20620152, PMID:21821043].
- During procapsid maturation, `gpC` catalyzes: (1) degradation of the internal scaffolding protein `gpNu3`, (2) cleavage of the N-terminal 22 residues of portal protein `gpB` to `gpB*`, (3) trans-fusion / transpeptidation of 10-12 copies of `gpC` with major capsid protein `gpE` followed by autoproteolysis to generate the minor capsid proteins `pX1` and `pX2`, and (4) autoproteolytic cleavage and exit of the remaining protease fragments from the prohead [PMID:20620152, PMID:21821043, file:LAMBD/C/C-uniprot.txt].

## Curation Decisions
- **ACCEPT**:
  - `GO:0008236` (`serine-type peptidase activity`, IEA `GO_REF:0000043`, supported by `PMID:20620152`, `PMID:21821043`)
  - `GO:0006508` (`proteolysis`, IEA `GO_REF:0000120`)
  - `GO:0046797` (`viral procapsid maturation`, IEA `GO_REF:0000043`)
  - `GO:0042802` (`identical protein binding`, IPI `PMID:21943085`)
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000043`)
  - `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`)
- **MODIFY**:
  - `GO:0008233` (`peptidase activity`) -> `GO:0008236` (`serine-type peptidase activity`)
  - `GO:0016787` (`hydrolase activity`) -> `GO:0008236` (`serine-type peptidase activity`)
