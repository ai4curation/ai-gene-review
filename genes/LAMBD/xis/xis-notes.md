# Curation Notes for Escherichia phage lambda `xis` (P03699)

## Summary of Gene Product
Bacteriophage lambda excisionase (`xis`, UniProt `P03699`, 72 AA) is a small, basic winged-helix DNA-binding and architectural directionality factor required for excisive site-specific recombination (`attL` x `attR` -> `attP` + `attB`) when the prophage is induced to enter the lytic cycle [file:LAMBD/xis/xis-uniprot.txt; PMID:17287355]. Xis stimulates prophage excision ~10^6-fold while simultaneously inhibiting reintegration of the excised phage genome [PMID:17287355; PMID:17275024].

## Structural and Mechanistic Architecture
- **Winged-helix DNA-binding domain (residues 1–51)**: Recognizes the `X1`, `X1.5`, and `X2` binding sites within the `P` arm of `attR` via an alpha-helix that inserts into the major groove (`Glu19`, `Arg22`, `Arg23`, `Thr26`) and a basic beta-hairpin wing (`Arg11`, `Arg13`, `Arg14`, `Arg16`, `Lys41`) that contacts the adjacent minor groove and phosphodiester backbone [PMID:12460578; PMID:17287355; PMID:17275024].
- **Cooperative micronucleoprotein filament assembly**: Three Xis protomers bind in a head-to-tail orientation across the 33-bp `X1-X1.5-X2` regulatory element (`PMID:17287355`), inducing over 72 degrees of DNA curvature and slight DNA unwinding (`PMID:17287355`). The basic beta-hairpin wing mediates direct interprotomer contacts (`GO:0042802`, `identical protein binding`) that stabilize the cooperative trimeric filament [PMID:17287355].
- **C-terminal Integrase-recruitment tail (residues 52–72)**: A flexible C-terminal segment containing a short alpha-helix contacts the N-terminal arm-binding domain of integrase (`Int`, specifically around `Glu47`), cooperatively recruiting Int to the adjacent `P2` arm site required for excisive intasome assembly [file:LAMBD/xis/xis-uniprot.txt; PMID:12832614; PMID:15066428].

## Review of Existing GO Annotations
- **`GO:0003677` (`DNA binding`, IEA `GO_REF:0000120`)**: `ACCEPT`. Supported by NMR and X-ray crystal structures (`PMID:12460578`, `PMID:15066428`, `PMID:17275024`, `PMID:17287355`) showing direct winged-helix binding to the `X1-X1.5-X2` sites of `attR`.
- **`GO:0042802` (`identical protein binding`, IPI `PMID:17287355` with `UniProtKB:P03699`)**: `ACCEPT`. Directly supported by the 2.6-A crystal structure of the cooperative Xis-DNA complex (`PMID:17287355`), in which three Xis monomers oligomerize head-to-tail on DNA via specific protein-protein interfaces.
- **`GO:0032359` (`provirus excision`, IEA `GO_REF:0000043`)**: `ACCEPT`. Core biological role of Xis as the essential directionality factor that drives prophage excision [file:LAMBD/xis/xis-uniprot.txt; PMID:17287355].
- **`GO:0006310` (`DNA recombination`, IEA `GO_REF:0000120`)**: `TOO_GENERAL`. Entailed by `GO:0032359` (`provirus excision`), which specifically captures Xis-directed excisive site-specific recombination.
