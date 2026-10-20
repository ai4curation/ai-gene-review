# Curation Notes for Salmonella phage P22 `gtrA` (P57021)

## Summary of Gene Product
`gtrA` encodes the bactoprenol-linked glucose translocase (flippase) GtrA (UniProt `P57021`, 120 amino acids, 13.5 kDa) of *Salmonella* phage P22 [PMID:11053393]. It is the first gene of the prophage-expressed `gtrABC` (`conABC` / `a1`) serotype-converting operon located immediately clockwise of `attP` between `attP` and `int` [PMID:11053393, PMID:12562822].

## Molecular Function, Biological Process, and Mechanism
- **Flippase activity (`GO:0140326`)**: In the three-step phage O-antigen glucosylation pathway conserved across *Salmonella* and *Shigella* phages (GtrA-GtrB-GtrC), GtrB first transfers glucose from UDP-glucose to undecaprenyl phosphate (bactoprenol phosphate) on the cytoplasmic face of the inner membrane, GtrA translocates (flips) undecaprenyl-phosphate-beta-D-glucose across the inner membrane to the periplasmic face, and the phage-specific glucosyltransferase GtrC transfers the glucose residue onto the galactose unit of the repeating O-antigen subunit at the C-6 position (converting *S. enterica* serovar Typhimurium from O-antigen form 4,12 to 1,4,12, i.e., antigen O1) [PMID:11053393].
- **Lipopolysaccharide biosynthetic process (`GO:0009103`)**: By flipping the lipid-linked glucose donor across the inner membrane for O-antigen modification, GtrA directly participates in host lipopolysaccharide O-antigen biosynthesis and serotype conversion during lysogeny [PMID:11053393].

## Subcellular Localization and Topology
- **Host cell plasma membrane (`GO:0020002`)**: TMHMM and UniProt sequence analyses show that GtrA is a multi-pass integral inner membrane protein with four transmembrane alpha-helices (residues 10-30, 34-54, 65-85, and 90-110) and both its N- and C-termini oriented toward the cytoplasm [PMID:11053393].

## Domain Architecture
- InterPro: `IPR016480` (`Glc_translocase_bactprenl-link`), `IPR051401` (`GtrA_CellWall_Glycosyl`), `IPR007267` (`GtrA_DPMS_TM`)
- PANTHER: `PTHR38459` (`PROPHAGE BACTOPRENOL-LINKED GLUCOSE TRANSLOCASE HOMOLOG`), `PTHR38459:SF1` (`PROPHAGE BACTOPRENOL-LINKED GLUCOSE TRANSLOCASE HOMOLOG`)
- Pfam: `PF04138` (`GtrA_DPMS_TM`)
- PIRSF: `PIRSF006298` (`GtrA_prd`)
