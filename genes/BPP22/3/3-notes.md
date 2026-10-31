# Gene 3 (TERS_BPP22, P04893) Notes

## Overview
- **Gene symbol:** `3`
- **UniProt ID:** `P04893` (`TERS_BPP22`)
- **Protein name:** Terminase small subunit (gp3; S-terminase)
- **Length:** 162 AA

## Function & Structural Insights
- **Oligomeric state and structure:** Forms a stable homononameric ring (~166 kDa) with a central channel ~23 Å in diameter (PDB: `3P9A`, 1.75 Å resolution) [PMID:18775728, PMID:22771211]. An alternative decameric ring (~185 kDa) can also form in vitro [PMID:17945256].
- **DNA binding and pac site recognition:** Recognizes the 22-bp packaging initiation site (`pac`, located within the coding sequence of `3` between residues 89 and 97) on viral concatemeric dsDNA and also binds dsDNA nonspecifically via electrostatic interactions mediated by its basic C-terminal tail (residues 140-162, particularly basic residues 143-152) rather than its N-terminal helix-turn-helix motif [PMID:18775728, PMID:22771211].
- **Terminase complex assembly and ATPase stimulation:** Residues 140-162 of the S-terminase bind stoichiometric amounts of the N-terminal minimal binding domain (residues 1-58) of the large terminase subunit (gp2, L-terminase), assembling into a `1S-terminase:2L-terminase` holoenzyme (1 nonameric gp3 ring + 2 gp2 monomers) [PMID:26301600]. Upon binding viral DNA, gp3 acts as a specific activator of gp2 ATPase activity, coupling viral DNA recognition to genome translocation [PMID:22771211].

## Domains & Orthology
- **InterPro:** `IPR032066` (Bacteriophage P22, terminase small subunit, `GP3_package`)
- **Pfam:** `PF16677` (`GP3_package`, 1 hit)
- **Gene3D:** `G3DSA:1.10.132.80` (`TERS_P22-like`, 1 hit)

## Curation Decisions
- `GO:0003677` (DNA binding, IEA): **ACCEPT** — directly supported by biochemical and structural studies demonstrating `pac`-specific and nonspecific dsDNA binding via the C-terminal basic region [PMID:18775728, PMID:22771211].
- `GO:0042802` (identical protein binding, IPI, PMID:22771211): **KEEP_AS_NON_CORE** — gp3 self-associates into a homononameric ring [PMID:22771211], which is a structural oligomerization property rather than the primary effector activity.
- `GO:0043493` (viral terminase complex, IDA, PMID:26301600): **MODIFY** to `GO:0097710` (`viral terminase, small subunit`) — `GO:0097710` is a more specific `part_of` child of `GO:0043493` already present in the annotation set and supported by the same study [PMID:26301600].
- `GO:0097710` (viral terminase, small subunit, IDA, PMID:26301600): **ACCEPT** — gp3 is the small subunit of the P22 terminase complex [PMID:26301600].
