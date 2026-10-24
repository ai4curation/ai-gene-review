# phd (Q06253) — Curation Notes

## Summary
- **Gene symbol**: `phd` ("prevent host death")
- **UniProtKB**: `Q06253` (`PHD_BPP1`, 73 aa, 8.1 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Antitoxin protein Phd of the `phd-doc` Type II toxin-antitoxin (plasmid addiction) module. Performs two coupled core functions:
  1. **Toxin sequestration / neutralization (`GO:0097351`)**: Its intrinsically disordered C-terminal domain (residues 52-73) folds into an alpha-helix upon binding the Fic-fold kinase toxin Doc (`Q06259`), sterically blocking the EF-Tu substrate-binding site of Doc and neutralizing its toxicity. In plasmid-free daughter cells, labile Phd is degraded by the host ClpXP ATP-dependent protease, freeing Doc to phosphorylate EF-Tu and arrest translation.
  2. **Autorepression of the `phd-doc` operon via conditional cooperativity (`GO:0001217`, `GO:0045892`)**: Its N-terminal domain (residues 1-49) forms a homodimer (`GO:0042803`) that binds two adjacent 10-bp palindromic operator sites (`OR1` and `OR2`, consensus `5'-GTGTACACAC-3'`) in the `phd-doc` promoter (`GO:0043565`, `GO:0032993`). At low Doc:Phd ratios, Doc bridges two operator-bound Phd dimers via two distinct binding sites (`H` and `L` on Doc) and allosterically orders the N-terminal DNA-binding domain of Phd to strongly enhance transcriptional repression; at high Doc:Phd ratios, saturation of both Phd C-terminal tails by Doc disrupts the operator complex through steric repulsion and derepresses transcription ("conditional cooperativity").

## Literature Evidence
- **Lehnherr, Maguin, Jafri & Yarmolinsky 1993 (`PMID:8411153`)**:
  - Discovered and sequenced the P1 plasmid addiction operon (`M95666`), showing that it encodes the 73-aa antitoxin Phd ("prevent host death") and the 126-aa toxin Doc ("death on curing"), which kills plasmid-free segregants.
  - Quote: `"Lose of P1 is prevented by the action of a plug-in "addiction module" that causes the death of plasmid-free segregants."`
  - Quote: `"Death is caused by a 126-aa protein named Doc (death on curing); toxicity is prevented by a 73-aa protein named Phd (prevent host death)."`
- **Magnuson, Lehnherr, Mukhopadhyay & Yarmolinsky 1996 (`PMID:7724551`)**:
  - Note: Cached `PMID_7724551.md` is an unrelated paper, so we do not cite `PMID:7724551` in `supported_by`.
- **Magnuson & Yarmolinsky 1998 (`PMID:9829946`)**:
  - Showed that Phd binds the `phd-doc` operator DNA on its own and represses transcription in vivo, while Doc does not bind DNA by itself but acts as a corepressor that forms a cooperative ternary complex with Phd on operator DNA.
  - Quote: `"Consistent with these in vivo results, we found that Phd binds to the operator DNA whereas Doc, which does not bind to the DNA by itself, greatly enhances the affinity and cooperativity of binding in combination with Phd."`
- **Gazit & Sauer 1999 (`PMID:9915794`)**:
  - Purified Phd and characterized its thermodynamic stability, homodimerization, and operator DNA binding. Showed that Phd is largely unfolded as a monomer at physiological temperatures (`Tm ~ 32°C`), dimerizes at higher concentrations (`Tm ~ 48°C` at 45 µM), and binds a single 10-bp palindromic subsite (`OR1`) as a Phd dimer and the full two-site operator (`OR1-OR2`) as two Phd dimers (`Kd ~ 7 × 10^-14 M^2`).
  - Quote: `"A single Phd dimer binds to the 10-base pair palindromic OR1 subsite of the phd-doc operator, and two dimers bind to the intact operator, which contains the adjacent OR1 and OR2 subsites."`
- **Garcia-Pino et al. 2008 (`PMID:18757857`) & Garcia-Pino et al. 2010 (`PMID:20603017`) & Garcia-Pino et al. 2016 (`PMID:20696400` in UniProt)**:
  - Determined crystal structures (`PDB:3K33`, `PDB:3KH2`, `PDB:3DD7`) and biophysical mechanisms of the Phd-Doc complex and free Phd. Showed that the C-terminal toxin-neutralizing domain of Phd (residues 52-73) is intrinsically disordered in isolation and folds into an alpha-helix upon binding Doc, that a monomeric Doc molecule bridges two Phd dimers via two asymmetric binding interfaces (`H` and `L`), and that Doc binding allosterically structures the N-terminal DNA-binding domain of Phd (`residues 1-49`) to mediate conditional cooperativity.
  - Quote (`PMID:20603017`): `"The C-terminal domain of Phd is intrinsically disordered in isolation and folds into an α helix upon binding to Doc. This coupled folding and binding of the C-terminal domain of Phd switches the N-terminal DNA-binding domain to an ordered conformation competent for operator binding"`
  - Quote (`PMID:20603017`): `"We show that a monomeric Doc molecule bridges two Phd dimers"`

## Annotation Review Decisions
- `GO:0001217` (`DNA-binding transcription repressor activity`, EXP: `PMID:9915794`): **ACCEPT**. Phd directly binds the `OR1-OR2` operator in the `phd-doc` promoter to repress transcription (`PMID:9915794`, `PMID:9829946`, `PMID:20603017`).
- `GO:0003677` (`DNA binding`, IDA: `PMID:20603017`): **TOO_GENERAL**. True, but uninformative because more specific terms `GO:0043565` (`sequence-specific DNA binding`) and `GO:0001217` (`DNA-binding transcription repressor activity`) are already asserted on this gene.
- `GO:0005515` (`protein binding`, IPI: `PMID:20603017`, with `UniProtKB:Q06259`): **REMOVE**. Removed per the `GO:0005515` protein-binding curation policy as uninformative; the specific functional interaction with Doc (`Q06259`) is already captured by `GO:0097351` (`toxin sequestering activity`).
- `GO:0032993` (`protein-DNA complex`, IDA: `PMID:9915794`): **ACCEPT**. Phd dimers assemble with `OR1-OR2` operator DNA (and Doc) into a nucleoprotein repressor complex (`PMID:9915794`, `PMID:20603017`).
- `GO:0042803` (`protein homodimerization activity`, IDA: `PMID:9915794`): **ACCEPT**. The N-terminal domain of Phd forms a homodimer required for binding each 10-bp palindromic operator subsite (`PMID:9915794`, `PMID:20603017`).
- `GO:0043565` (`sequence-specific DNA binding`, IDA: `PMID:9915794`): **ACCEPT**. Phd dimers specifically recognize the 10-bp palindromic `OR1` and `OR2` operator subsites (`PMID:9915794`).
- `GO:0045892` (`negative regulation of DNA-templated transcription`, IEP: `PMID:20603017`): **ACCEPT**. Phd autorepresses transcription of the `phd-doc` operon (`PMID:9829946`, `PMID:20603017`).
- `GO:0097351` (`toxin sequestering activity`, EXP: `PMID:20603017`): **ACCEPT**. Phd binds and sequesters the Doc kinase toxin via its C-terminal domain (residues 52-73) to prevent host cell death (`PMID:8411153`, `PMID:18757857`, `PMID:20603017`).
