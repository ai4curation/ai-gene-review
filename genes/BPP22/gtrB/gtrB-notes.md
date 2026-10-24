# Curation Notes for Salmonella phage P22 `gtrB` (P57022)

## Summary of Gene Product
`gtrB` encodes the bactoprenol glucosyltransferase GtrB (UniProt `P57022`, 310 amino acids, 35.1 kDa) of *Salmonella* phage P22 [PMID:11053393]. It is the second gene of the prophage-expressed `gtrABC` (`conABC` / `a1`) serotype-converting operon located between `attP` and `int` [PMID:11053393, PMID:12562822].

## Molecular Function, Biological Process, and Mechanism
- **Hexosyltransferase activity (`GO:0016758`)**: GtrB is a glycosyltransferase family 2 (`GT2`) enzyme that catalyzes the first committed step of the phage O-antigen glucosylation pathway: transfer of a glucosyl residue from cytoplasmic UDP-alpha-D-glucose to the lipid carrier undecaprenyl phosphate (bactoprenol phosphate) on the cytoplasmic face of the inner membrane, forming undecaprenyl-phosphate-beta-D-glucose [PMID:11053393].
- **Lipopolysaccharide biosynthetic process (`GO:0009103`)**: Together with the GtrA flippase and the GtrC periplasmic O-antigen glucosyltransferase, GtrB mediates C-6 glucosylation of the galactose unit in the *S. enterica* serovar Typhimurium lipopolysaccharide O-antigen repeating unit, converting the host serotype from 4,12 to 1,4,12 (antigen O1) during lysogeny [PMID:11053393].

## Subcellular Localization and Topology
- **Host cell plasma membrane (`GO:0020002`)**: GtrB is a multi-pass integral protein of the host bacterial inner membrane (plasma membrane) containing an N-terminal cytoplasmic GT2 catalytic domain followed by two C-terminal alpha-helical transmembrane segments (residues 229-249 and 263-283), placing both its N- and C-termini in the cytoplasm [PMID:11053393].

## Domain Architecture
- CDD: `cd04187` (`DPM1_like_bac`)
- InterPro: `IPR001173` (`Glyco_trans_2-like`), `IPR050256` (`Glycosyltransferase_2`), `IPR063169` (`GtrB_C`), `IPR029044` (`Nucleotide-diphossugar_trans`)
- PANTHER: `PTHR48090:SF1` (`PROPHAGE BACTOPRENOL GLUCOSYL TRANSFERASE HOMOLOG`), `PTHR48090` (`UNDECAPRENYL-PHOSPHATE 4-DEOXY-4-FORMAMIDO-L-ARABINOSE TRANSFERASE-RELATED`)
- Pfam: `PF00535` (`Glycos_transf_2`), `PF30648` (`GtrB_C`)
