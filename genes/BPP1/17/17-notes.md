# 17 / lyz (Q37875) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `17` (renamed `lyz` by Schmidt et al. 1996, [PMID:8576044]).
- **Protein**: Endolysin / Lysozyme (`Lyz` / `gp17`; 185 aa, 20.1 kDa, `EC:3.2.1.17`, GH24 family).
- **Biological role & mechanism**:
  - P1 `Lyz` (`gp17`) is the prototype **SAR (signal-anchor-release) endolysin** [PMID:15090650, PMID:15637279].
  - Unlike canonical T4-type cytoplasmic endolysins that depend on pore-forming holins to cross the inner membrane, P1 Lyz possesses an N-terminal transmembrane SAR domain (`aa 7–24`, rich in weakly hydrophobic Ala/Gly/Ser/Thr residues) that directs Sec-dependent integration into the host inner membrane (`GO:0020002` `host cell plasma membrane`) as an uncleaved type II bitopic protein with its catalytic domain in the periplasm [PMID:15090650].
  - In the membrane-tethered state, Lyz is kept catalytically inactive by two mechanisms: topological tethering to the bilayer and an intramolecular disulfide bond between `Cys44` and the catalytic triad residue `Cys51` (`Glu42–Cys51–Thr57`, equivalent to T4 lysozyme `Glu11–Asp20–Thr26`) that sterically and chemically blocks the active site [PMID:15637279].
  - When the P1 holin (`LydA`, controlled by antiholin `LydB`) depolarizes the host cytoplasmic membrane (or progressively at a low spontaneous rate), the SAR helix exits the lipid bilayer into the periplasm and refolds. This brings `Cys13` within the liberated SAR domain into proximity with the `Cys44–Cys51` disulfide, triggering an intramolecular thiol-disulfide isomerization (`Cys13` attacks `Cys44` to form a `Cys13–Cys44` disulfide bond) that liberates the catalytic sulfhydryl `Cys51` and remodels the active-site cleft [PMID:15090650, PMID:15637279].
  - Activated periplasmic Lyz hydrolyzes the $\beta(1\rightarrow 4)$ glycosidic bonds between $N$-acetylmuramic acid and $N$-acetyl-D-glucosamine in the host peptidoglycan sacculus (`GO:0003796` `lysozyme activity`, `GO:0009253` `peptidoglycan catabolic process`), causing cell lysis and progeny phage release [PMID:8576044, PMID:15090650, PMID:15637279, PMID:15489417].

## Review of Existing GOA Annotations
- `GO:0003796` (`lysozyme activity`, IEA, `GO_REF:0000002` / `GO_REF:0000043` / `GO_REF:0000120`): **ACCEPT**. Core enzymatic activity of P1 Lyz (`gp17`), demonstrated genetically, biochemically, and structurally [PMID:8576044, PMID:15090650, PMID:15637279].
- `GO:0003824` (`catalytic activity`, IEA, `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0003796` (`lysozyme activity`).
- `GO:0009253` (`peptidoglycan catabolic process`, IEA, `GO_REF:0000043` / `GO_REF:0000117`): **ACCEPT**. P1 Lyz degrades the host peptidoglycan layer to lyse the bacterium at the end of the lytic cycle [PMID:15090650, PMID:15637279, PMID:15489417].
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0003796` (`lysozyme activity`).
- `GO:0016798` (`hydrolase activity, acting on glycosyl bonds`, IEA, `GO_REF:0000117`): **TOO_GENERAL**. Entailed by `GO:0003796` (`lysozyme activity`).
- `GO:0016998` (`cell wall macromolecule catabolic process`, IEA, `GO_REF:0000043` / `GO_REF:0000119`): **TOO_GENERAL**. Entailed by `GO:0009253` (`peptidoglycan catabolic process`).
- `GO:0020002` (`host cell plasma membrane`, IEA, `GO_REF:0000043` / `GO_REF:0000044`): **ACCEPT**. P1 Lyz is initially integrated into the *E. coli* cytoplasmic (inner) membrane via its N-terminal SAR transmembrane domain before release into the periplasm upon membrane depolarization [PMID:15090650, PMID:15637279].
- `GO:0031640` (`killing of cells of another organism`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0078): **MODIFY** -> `GO:0019076` (`viral release from host cell`). This annotation comes from UniProt's `Bacteriolytic enzyme` keyword mapping; for a bacteriophage endolysin, the biological process is lysis-mediated exit of progeny virions from the infected host cell (`GO:0019076` `viral release from host cell`).
- `GO:0042742` (`defense response to bacterium`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0078): **REMOVE**. Automated keyword mapping from `Bacteriolytic enzyme` (which is appropriate for eukaryotic antibacterial lysozymes) misassigns `defense response to bacterium` to a bacteriophage endolysin whose function is host cell lysis for viral progeny release, not host immune defense.
