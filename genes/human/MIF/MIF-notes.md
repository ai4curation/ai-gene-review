# MIF (Macrophage Migration Inhibitory Factor) — Curation Notes

## Overview

- **Gene symbol**: `MIF` (HGNC:7097)
- **UniProtKB**: `P14174` (`MIF_HUMAN`, 115 aa; initiator Met-1 is cleaved to expose the N-terminal catalytic Pro-2 residue)
- **PANTHER family**: `PANTHER:PTHR11954` (`D-DOPACHROME DECARBOXYLASE`), subfamily `PANTHER:PTHR11954:SF6` (`MACROPHAGE MIGRATION INHIBITORY FACTOR`), metazoan ancestor `PANTHER:PTN000237513`, eukaryotic root `PANTHER:PTN000237510`
- **Vertebrate paralog**: `DDT` (`UniProtKB:P30046`, D-dopachrome decarboxylase / D-dopachrome tautomerase, also designated MIF-2; `PANTHER:PTHR11954:SF22`, 118 aa, ~34% sequence identity to MIF)

## Biological Summary

1. **CD74–CD44 receptor complex and canonical MIF signaling (`GO:0035691`)**:
   - MIF is a pro-inflammatory cytokine secreted via a non-classical leaderless export pathway involving the Golgi-associated protein p115 (`USO1`) and ABCA1-dependent transport [PMID:19454686, "Depletion of p115 from monocytes/macrophages decreases the release of MIF conversion after stimulation with lipopolysaccharide or Chlamydia pneumoniae"].
   - Extracellular MIF binds the cell-surface form of the MHC class II invariant chain `CD74` (`UniProtKB:P04233`) with high affinity ($K_d \approx 9\text{ nM}$), which is required for MIF-induced activation of the ERK1/2 (`MAPK3`/`MAPK1`) mitogen-activated protein kinase cascade, cell proliferation, and prostaglandin $E_2$ ($\text{PGE}_2$) production [PMID:12782713, "MIF binds to the extracellular domain of CD74 with high affinity (Kd = 9.0 x 10(-9) M), and CD74 is required for MIF-induced activation of the extracellular signal-regulated kinase-1/2 mitogen-activated protein kinase cascade, cell proliferation, and PGE2 production"].
   - Because `CD74` lacks an intrinsic intracellular signaling domain, MIF binding to `CD74` recruits and activates the transmembrane co-receptor `CD44` (`UniProtKB:P16070`); MIF stimulation induces PKA-dependent serine phosphorylation of `CD74` and `CD44`, activating Src-family tyrosine kinase signaling and sustained ERK1/2 phosphorylation, which suppresses p53-dependent apoptosis and promotes cell survival [PMID:17045821, "We show that CD74 forms a complex with CD44, which is essential for the MIF-induced signaling cascade"].
   - The paralog `DDT` (MIF-2) also binds `CD74` with high affinity ($K_d \approx 1.07 \times 10^{-8}\text{ M}$), competes with MIF for `CD74` binding, and activates the same CD74–CD44–ERK1/2 and proinflammatory cascade [PMID:21817065, "Pull-down and surface plasmon resonance experiments revealed that D-DT binds the MIF ectodomain receptor CD74 with high affinity (K(d) = 1.07 × 10(-8) M) and competes with MIF for binding to CD74"].

2. **Non-cognate chemokine receptor agonism (`CXCR2` and `CXCR4`)**:
   - In addition to CD74–CD44, MIF contains a pseudo-(E)LR motif and N-terminal loop that enable it to act as a non-cognate ligand for the CXC chemokine receptors `CXCR2` (`UniProtKB:P25025`) and `CXCR4` (`UniProtKB:P61073`), often in heteromeric complexes with `CD74`, driving leukocyte chemotaxis (`GO:0042056` *chemoattractant activity*) and tumor cell invasion [PMID:19602265].

3. **Tautomerase / isomerase catalytic activity (`GO:0050178`, `GO:0004167`)**:
   - MIF forms a homotrimeric barrel-shaped structure (three $\beta\alpha\beta\beta\alpha\beta$ subunits) with three catalytic pockets located at the monomer–monomer interfaces [PMID:17526494].
   - Following cleavage of the initiator methionine (`Met-1`), the N-terminal `Pro-2` residue has an unusually low $\text{p}K_a$ (~5.6) and serves as a catalytic general base for the tautomerization of phenylpyruvate (`GO:0050178`, EC 5.3.2.1) and the isomerization of D-dopachrome (`GO:0004167`, EC 5.3.3.12), assisted by substrate-binding residues `Lys-33`, `Ile-65`, and `Asn-98` [PMID:11439086; PMID:16285950; PMID:17526494; PMID:21817065].
   - Although the physiological endogenous substrate for this tautomerase activity in mammals remains uncertain, the catalytic pocket overlaps with or allosterically modulates the `CD74` receptor-binding surface [PMID:20534506].

4. **Intracellular interactions**:
   - Cytoplasmic MIF interacts with `COPS5`/`JAB1` (`UniProtKB:Q92905`) to inhibit AP-1 transcriptional activity and modulate cell cycle progression [PMID:11089976], suppresses p53 (`TP53`) activity to inhibit apoptosis and cellular senescence [PMID:10562313], and binds `BCL2L11` (`Bim`) to inhibit Bim-mediated apoptosis [PMID:18677096].

## Signaling Pathway Annotation Gap (`GO:0035691`)

- In GOA (as captured in `projects/LIGANDS_IN_SIGNALING/results/triage.json:371-381`, `:2668-2678`, `:5387-5397`), `GO:0035691` (*macrophage migration inhibitory factor signaling pathway*) is annotated only to the receptor `CD74` (`CD74` in human, `mCD74/iso:Long` in mouse, `Cd74` in rat), and to **neither ligand (`MIF` or `DDT`)**:
  - Human `MIF` (`UniProtKB:P14174`, `genes/human/MIF/MIF-goa.tsv`) was annotated in 2003 (`PMID:12782713`) to the parent term `GO:0007166` (*cell surface receptor signaling pathway*, `IDA`) before `GO:0035691` was created in the ontology, and that annotation was never updated to the specific pathway term.
  - Human `DDT` (`UniProtKB:P30046`) was annotated from `PMID:21817065` (`BHF-UCL`, `20170726`) only to `GO:0005126` (*cytokine receptor binding*, `IDA`) and `GO:0070374` (*positive regulation of ERK1 and ERK2 cascade*, `IGI` with `UniProtKB:P14174`), without `GO:0035691` or `GO:0005125` (*cytokine activity*).
- In `MIF-ai-review.yaml`:
  - `GO:0007166` (`IDA`, `PMID:12782713`) is marked `MODIFY` with `proposed_replacement_terms: [GO:0035691]` (*macrophage migration inhibitory factor signaling pathway*, supported by `PMID:12782713`, `PMID:17045821`, `PMID:21817065`).
  - `GO:0005125` (*cytokine activity*, an `is_a` child of `GO:0048018` *receptor ligand activity*) is `ACCEPT`ed as the primary molecular function, and `GO:0005126` (*cytokine receptor binding*, `PMID:17045821`, `PMID:21817065`) is marked `MODIFY` $\rightarrow$ `GO:0005125` (*cytokine activity*) per Decision 4 in `projects/LIGANDS_IN_SIGNALING.md`.
