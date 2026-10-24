# mtd (Bordetella phage BPP-1) — Curation Notes

## Overview
- **Gene symbol**: `mtd`
- **UniProt ID**: `Q775D6` (`MTD_BPBPP`, `bbp9`)
- **Organism**: *Bordetella* phage BPP-1 (`NCBITaxon:2885909`)
- **Product**: Major tropism determinant (`Mtd`, Tail fiber receptor-binding protein; 381 aa, ~40.4 kDa; PDB `1YU0`–`1YU4`, `2IOU`)

## Biological Function and Mechanism
- **Distal tail fiber receptor-binding protein**: `Mtd` is the hypervariable receptor-binding protein localized to the bilobed globular distal ends of the six phage BPP-1 tail fibers (two `Mtd` homotrimers per tail fiber, 12 trimers / 36 subunits per virion), as directly demonstrated by cryo-electron tomography of immunogold-labeled BPP-1 virions [PMID:20160083; PMID:24127622].
- **C-type lectin (CLec) fold and variable region (`VR1`)**: X-ray crystal structures (`PDB:1YU0`–`1YU4`) show that `Mtd` forms an intertwined, pyramid-shaped homotrimer consisting of an N-terminal beta-prism domain, a central beta-sandwich domain, and a C-terminal C-type lectin (`CLec`) fold domain that houses the 134-bp variable region (`VR1`, residues 331–381) [PMID:16170324]. The `CLec` scaffold stabilizes a main-chain conformation-invariant binding surface displaying 12 adenine-encoded variable amino acid residues capable of generating ~`10^13` distinct sequences via `bRT`-mediated diversity-generating retroelement (DGR) mutagenic homing [PMID:11910109; PMID:15386016; PMID:16170324].
- **Selective receptor recognition and avidity amplification**: In the prototypical `Mtd-P1` variant, the trimeric `Mtd` receptor-binding sites bind the `Bvg+` phase outer-membrane autotransporter adhesin pertactin (`Prn`, `UniProtKB:Q03035`) asymmetrically (`3:1` stoichiometry per trimer; `PDB:2IOU`) [PMID:18532877]. Although monovalent `Mtd-P1` affinity for pertactin is modest (`Kd ~ 3 µM`), multivalent display of 12 `Mtd` trimers across the virion tail fibers amplifies binding strength by ~`10^6`-fold (`picomolar` avidity), allowing recently evolved low-affinity `Mtd` variants (such as `Mtd-M1`, which binds `Bvg-` phase receptors) to mediate productive host cell attachment and infection [PMID:18532877].

## Curation Decisions
- **Existing annotations**:
  - `GO:0005515` (`protein binding`, IPI with pertactin `Q03035` from PMID:16170324 and PMID:18532877): `REMOVE`. Bare `GO:0005515` (`protein binding`) is uninformative per GO protein-binding policy; the specific functional role of binding host adhesion receptors is captured by `GO:0098671`.
  - `GO:0098024` (`virus tail, fiber`, IEA): `ACCEPT`. Cryo-electron tomography directly localizes `Mtd` to the distal globular ends of the phage tail fibers [PMID:20160083].
  - `GO:0098015` (`virus tail`, IEA): `TOO_GENERAL` (entailed by `GO:0098024`).
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA): `ACCEPT`. `Mtd-P1` directly binds the host outer-membrane adhesion protein pertactin (`Prn`) to mediate virion attachment [PMID:18532877].
  - `GO:0019062` (`virion attachment to host cell`, IEA) and `GO:0046718` (`symbiont entry into host cell`, IEA): `TOO_GENERAL` (both entailed by `GO:0098671`).
  - `GO:0098678` (`viral tropism switching`, IEA): `ACCEPT`. `Mtd` is the variable effector protein whose C-terminal `VR1` sequence switches phage host tropism across *Bordetella* phase states [PMID:11910109; PMID:15386016; PMID:16170324].
