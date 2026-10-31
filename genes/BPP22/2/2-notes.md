# Gene 2 (TERL_BPP22, P26745) Notes

## Overview
- **Gene symbol:** `2`
- **UniProt ID:** `P26745` (`TERL_BPP22`)
- **Protein name:** Terminase large subunit (gp2; L-terminase; DNA packaging protein gp2)
- **Length:** 499 AA

## Function & Structural Insights
- **Bifunctional ATPase and Endonuclease Motor:** Consists of an N-terminal P-loop ATPase translocation domain (residues 1-271) connected via a flexible linker to a C-terminal RNase H-like endonuclease domain (residues 289-499, PDB: `4DKW`, 2.02 Å resolution) [PMID:22715098, PMID:26301600].
- **Terminase Holoenzyme Assembly:** The N-terminal minimal binding domain (residues 1-58) of two L-terminase monomers associates stoichiometrically with the C-terminal tail (residues 140-162) of one nonameric S-terminase (gp3) ring to form a `1S-terminase:2L-terminase` "nutcracker"-like complex, stabilized by ATP binding [PMID:26301600].
- **Catalytic Mechanism of Nuclease Domain:** The C-terminal headful nuclease domain contains a central seven-stranded beta-sheet core coordinating two catalytic Mg2+ ions (M1 and M2) via acidic residues including Asp321 and Asp459. In isolation, the nuclease domain is inactive in vitro because a unique extended beta-hairpin (residues 352-373) blocks the DNA binding surface; in full-length gp2, interdomain crosstalk couples endonucleolytic cleavage to ATPase-driven packaging [PMID:22715098].
- **Sequence Specificity of Initial Cleavage:** While once thought to make purely nonspecific cuts, initial `pac`-site cleavage occurs with low sequence specificity predominantly at boxes `[5'-GAT-3']` within a 120-bp cleavage region [PMID:28134243].

## Domains & Orthology
- **HAMAP:** `MF_04148` (`TERL_BPP22`)
- **InterPro:** `IPR027417` (`P-loop_NTPase`), `IPR035421` (`Terminase_6C`), `IPR044265` (`Terminase_large_su_BPP22`)
- **Pfam:** `PF17289` (`Terminase_6C`), `PF03237` (`Terminase_6N`)
- **Gene3D:** `G3DSA:3.30.420.280`, `G3DSA:3.40.50.300`

## Curation Decisions
- `GO:0000166` (nucleotide binding, IEA): **MODIFY** to `GO:0005524` (`ATP binding`).
- `GO:0004518` (nuclease activity, IEA): **MODIFY** to `GO:0004519` (`endonuclease activity`).
- `GO:0004519` (endonuclease activity, IEA): **ACCEPT** — full-length gp2 exhibits Mg2+-dependent dsDNA endonuclease activity to cleave concatemeric viral DNA at initiation (`pac`) and headful termination [PMID:22715098, PMID:28134243].
- `GO:0005524` (ATP binding, IEA): **ACCEPT** — binds ATP at its N-terminal P-loop ATPase domain [PMID:26301600].
- `GO:0016787` (hydrolase activity, IEA): **MODIFY** to `GO:0016887` (`ATP hydrolysis activity`) and `GO:0004519` (`endonuclease activity`).
- `GO:0016887` (ATP hydrolysis activity, IEA): **ACCEPT** — hydrolyzes ATP to power viral DNA translocation into the procapsid, stimulated by gp3-DNA complexes [PMID:22771211, PMID:26301600].
- `GO:0019073` (viral DNA genome packaging, IEA): **MODIFY** to `GO:0098006` (`viral DNA genome packaging, headful`).
- `GO:0043493` (viral terminase complex, IDA, PMID:26301600): **MODIFY** to `GO:0098009` (`viral terminase, large subunit`).
- `GO:0046872` (metal ion binding, IEA): **ACCEPT** — coordinates two catalytic Mg2+ ions at the nuclease active site [PMID:22715098].
- `GO:0051276` (chromosome organization, IEA): **REMOVE** — over-propagated cellular process term; gp2 packages viral concatemeric DNA into procapsids (`GO:0098006`) rather than organizing host chromosomes.
- `GO:0098009` (viral terminase, large subunit, IDA & IEA): **ACCEPT** — gp2 is the large subunit of the P22 terminase complex [PMID:26301600].
