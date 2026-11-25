# Curation Notes: Bacteriophage T4 `uvsW` (ATP-dependent DNA helicase UvsW, P0DXF1)

## Overview
- **Gene symbol:** `uvsW` (synonym: `dar`, gpUvsW)
- **UniProt ID:** `P0DXF1` (`UVSW_BPT4`)
- **Length:** 502 amino acids
- **Function:** Superfamily 2 (SF2) Rad54/RecG-like ATP-dependent 3'-5' branched-DNA helicase, DNA-rewinding motor, and strand-annealing protein that catalyzes Holliday junction branch migration, replication fork regression, and R-loop unwinding to regulate the transition from origin-dependent to recombination-dependent DNA replication and promote DNA repair.

## Biological Role and Mechanism
- UvsW is a 502-amino-acid monomeric SF2 helicase containing two RecA-like motor domains and a basic N-terminal substrate-binding domain (`PMID:9233823`, `PMID:17092935`, PubMed 15113838).
- Biochemically, UvsW exhibits ssDNA-dependent ATPase activity and 3' -> 5' DNA/RNA-DNA helicase activity with strong specificity for branched substrates (Y-forks, stalled replication forks, D-loops, R-loops, and Holliday junctions), as well as a potent single-stranded DNA annealing activity that is stimulated by ATP hydrolysis (`PMID:9233823`, `PMID:17092935`, `PMID:17823128`).
- During the early-to-late replication switch in T4 infection, UvsW unwinds persistent RNA-DNA hybrids (R-loops) at replication origins (`oriA`, `oriE`, `oriF`, `oriG`), repressing origin-dependent initiation and channeling viral replication into recombination-dependent replication (RDR) (`PMID:9233823`, PubMed 2388264).
- During DNA repair and recombination, UvsW catalyzes Holliday junction branch migration and drives regression of stalled replication forks into four-way chicken-foot intermediates (`PMID:17092935`, `PMID:17823128`, PubMed 23732982).

## Review of Existing GO Annotations
- `GO:0043138` (3'-5' DNA helicase activity, IEA, GO_REF:0000003): **ACCEPT**. Directly captures the core 3'-5' DNA unwinding and branch-migration motor activity of UvsW (`PMID:17092935`).
- `GO:0004386` (helicase activity, IEA, GO_REF:0000043): **MODIFY** to `GO:0043138` (3'-5' DNA helicase activity).
- `GO:0016887` (ATP hydrolysis activity, EXP, `PMID:17092935` & EXP, `PMID:9233823`): **ACCEPT**. Both experimental papers directly demonstrate ssDNA/branched-DNA-dependent ATPase activity of UvsW and its abolition by the Walker A mutation K141R (`PMID:9233823`, `PMID:17092935`).
- `GO:0016787` (hydrolase activity, IEA, GO_REF:0000120): **MODIFY** to `GO:0043138` (3'-5' DNA helicase activity) and `GO:0016887` (ATP hydrolysis activity).
- `GO:0005524` (ATP binding, IEA, GO_REF:0000120): **ACCEPT**. Essential for UvsW ATPase and branch-migration activity.
- `GO:0000166` (nucleotide binding, IEA, GO_REF:0000043): **MODIFY** to `GO:0005524` (ATP binding).
- `GO:0003677` (DNA binding, IEA, GO_REF:0000120): **ACCEPT**. UvsW binds branched DNA, Holliday junctions, and ssDNA (`PMID:9233823`, `PMID:17092935`).
- `GO:0016853` (isomerase activity, IEA, GO_REF:0000043): **REMOVE**. Automated keyword mapping artifact from EC 5.6.2.4 (`3'-5' DNA helicase`) triggering the broad isomerase keyword mapping. UvsW is an ATP-dependent DNA helicase/translocase, not an isomerase.
