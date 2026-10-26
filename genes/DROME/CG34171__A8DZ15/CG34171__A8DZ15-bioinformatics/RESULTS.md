# CG34171-PB (A8DZ15): subfamily placement, catalytic residues and C-terminal hydropathy

Reproduce from this directory with
`uv run subfamily_analysis.py <repo_root> .` (MAFFT L-INS-i and Biopython 1.85; sequences
are fetched live from UniProt REST). Raw output is in `subfamily_output.txt` and
`subfamily_results.json`. The alignment (`sf_members_plus_trypsin.aln.fasta`) and NJ tree
(`sf_members_plus_trypsin_nj.nwk`) are kept beside them. Run date 2026-10-21.

## PANTHER placement

The PANTHER 19.0 fruit-fly HMM classification places A8DZ15 in PTHR24260:SF136 (GH08193P-RELATED), a subfamily of 13 D. melanogaster proteins: c-SPH166, CG30091, CG18223, CG15873, CG6592, modSP, CG13527, CG30323, CG17837, CG6067, CG34171, CG30086 and SPH199. The UniProt record instead cross-references PTHR24276:SF96, and the GOA IBA rows come from PTHR24256 node PTN000667087. The three sources disagree on the family, so no subfamily-level function is assumed from any of them.

Of the FlyBase seeds that PAINT used at PTN000667087, only modSP is in SF136. The others are psh, MP1 and spirit (SF135), scaf (SF145), SPE (SF144), grass (SF140) and sphinx1/sphinx2 (SF134).

## Catalytic residues

Bovine trypsin P00760 was aligned as an active reference, with its UniProt active sites at H63, D107 and S200. A8DZ15 has H72 and D124 at the His and Asp columns and F222 at the Ser column, so its catalytic triad is not intact. This matches the earlier analysis of the gene (file:DROME/CG34171/CG34171-bioinformatics/RESULTS.md).

Among the 13 SF136 members, the triad is intact only in modSP (H414/D472/S563), CG6592 (H166/D215/S311) and CG30091 (H77/D133/S228). The other ten members have substitutions at one or more triad positions, so the subfamily consists mostly of serine protease homologs.

## Relationship to the characterised subfamily member

modSP is the one SF136 member with published experimental function and the only SF136 PAINT seed. Over aligned columns it is 23.4% identical to A8DZ15, and its S1 domain is preceded by four LDL-receptor class A modules and two Sushi modules. A8DZ15 has only a signal peptide and a single S1 domain. A8DZ15 is no more than 28.8% identical to any SF136 member; the closest is CG15873. In the NJ tree, A8DZ15 does not group with modSP, and there is no one-to-one relationship to any characterised protein. modSP's specific role as a Toll-pathway initiator protease is therefore not transferred.

## C-terminal hydrophobic segment

UniProt annotates no transmembrane helix, but a Kyte-Doolittle scan (19-residue window) finds a strongly hydrophobic C-terminal segment, residues 274-292, FIADRFSLFSFIILMLSIV, with a mean hydropathy of 2.01. A hydrophobic C-terminal tail after a signal peptide fits either a GPI-anchor attachment signal or a C-terminal membrane anchor. It could also be cleaved during processing. This analysis does not decide between these, so the protein's final location (secreted versus cell-surface anchored) is unresolved.

## Limitations

These results are based on sequence alone. No folding, expression, secretion or partner data were generated. Identity is calculated over aligned columns of a multiple alignment of divergent proteins and is approximate. The NJ tree uses identity distances and has no bootstrap support.
