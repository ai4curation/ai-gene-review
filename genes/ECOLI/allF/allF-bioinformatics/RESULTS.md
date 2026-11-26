# AllF: where the succinyl-CoA synthetase catalytic histidine went

Script: `catalytic_his_mapping.py`. Output: `results.yaml`. Run twice on 2026-11-22 with
`uv run catalytic_his_mapping.py > results.yaml` (about one minute; UniProt release 2026_04);
the two runs gave identical numbers. Run again the same day after two measurements were added
(result 7: His389 against the lobe 2 helix N-terminus, and His389 in the dimer frame); every
earlier number was unchanged.
Run again on 2026-11-24 after the distance of every AllF histidine to the superposed histidine
was added (result 7); again every earlier number was unchanged.

Everything is fetched at run time: sequences and the SucD active-site feature from UniProt, the
Pfam PF00549 profile from the InterPro API, and PDB entries 3DMY (AllF residues 101-555, no
ligand), 2SCU, 1CQI and 1JKJ (E. coli succinyl-CoA synthetase, SucD chain A and SucC chain B)
from RCSB. No coordinate or sequence file is stored here.

All SucD numbers below are UniProt P0AGE9 numbering. The crystal structures number the mature
protein, one lower, so the catalytic histidine is His247 here and His246 in the structural
literature. 3DMY uses UniProt Q47208 numbering (447 of 447 ordered residues of chain A match).

## Question

Does AllF keep the catalytic phosphohistidine of the succinyl-CoA synthetase alpha subunit, and
which AllF residue stands where that histidine stands in SucD? Two OpenScientist runs gave
different answers (Val293 and Gln467). This analysis was written to settle that.

## Results

1. AllF has no histidine at the position of the SucD catalytic histidine. This holds by the profile alignment and by the superposition on the crystal structure.
2. By the Pfam PF00549 profile, SucD His247 is on match column 102, and that column holds Gln467 in AllF, Gln466 in Salmonella FdrA and Gln483 in YahF.
3. By superposition on the AllF crystal structure, the profile register around that column is not the structural one. The SucD segment 242-251 (GKRMGHAGAI), which carries the catalytic histidine, has no AllF counterpart, and Gln467 superposes on SucD Lys262 (1.5-1.8 A), 18 A from the superposed histidine. AllF 462-476 (QCRSQQIATLEDAGI) pairs residue by residue with SucD 257-271 (GTADEKFAALEAAGV).
4. Val293 is not the equivalent of the catalytic histidine by either method. It lies outside the PF00549 domain (AllF 336-491), and in the superposition its CA is 26 A from the superposed His247 CA.
5. AllF has two lobes with the fold of the SucD C-terminal domain, residues 174-299 and 300-502. The SucD C-terminal domain superposes on each about equally well (TM-score 0.62 and 0.64 normalised by SucD, RMSD 2.4 and 2.6 A, 120 and 126-127 aligned residues). The histidine loop is missing from both: against lobe 1 the unpaired SucD run is 237/238-258/259.
6. In lobe 2 the position of the histidine side chain is taken by Met391 (selenomethionine in the crystal; SE 2.3-2.7 A from the superposed His247 NE2).
7. His389 is the nearest histidine. It lies in an insert after PF00549 match column 34 that SucD lacks. Its CA is 9.0-9.4 A from the superposed His247 CA and its closest atom is 4.5-5.0 A from the superposed NE2. These two distances are for the frame in which the SucD C-terminal domain is superposed on lobe 2 of the same chain. In the dimer frame of result 9, with the histidine placed through lobe 1 of chain A, His389 of chain B has its CA 15.1-15.4 A and its closest atom 9.5-9.8 A from the superposed histidine. Within each AllF chain, without any superposition, the His389 side chain is 3.2-3.4 A from the carbonyl oxygen of Thr338 and 5.3-5.6 A, 5.8-6.2 A and 8.4-8.8 A from the backbone nitrogens of Gly339, Gly340 and Thr341, the N-terminus of the lobe 2 power helix. Every histidine of both chains of 3DMY was measured against the superposed histidine in each frame. In the lobe 2 frame the next nearest after His389 is His364 of the same chain, closest atom 15.3-15.6 A. In the dimer frame the next nearest by closest atom is His362 of chain B at 11.8-12.0 A, and by CA His362 (10.5-10.7 A) is nearer than His389 (15.1-15.4 A).
8. The N-terminus of the phosphate-binding power helix is kept in both lobes. SucD Ser154-Gly155-Thr156 superposes on AllF Ser202-Gly203-Thr204 (0.6-1.4 A) and on AllF Gly339-Gly340-Thr341 (0.5-1.1 A).
9. In the 3DMY homodimer, lobe 1 of one chain and lobe 2 of the other together superpose on the SucD C-terminal domain plus SucC C-terminal domain pair (TM-score 0.63-0.64, RMSD 3.8-3.9 A, 248-249 aligned residues, 96-103 of them from SucC within 5 A). The arrangement is similar, not identical. Lobe 1 and lobe 2 of the same chain do not (TM-score 0.39-0.40, no SucC residue paired).
10. The Rossmann-like CoA-binding domain of SucD (residues 2-123) superposes on AllF only when AllF 503-555 is placed before 101-190 (TM-score 0.73-0.74, RMSD 2.4 A, 109 aligned residues). CoA carried over rigidly from the SucD structures then has 14-16 of its 48 atoms within 2.2 A of an AllF atom, against 0-1 in its own site. At a 3.0 A cut-off the counts are 26-30 of 48 against 3-8.
11. Family survey. All 53 reviewed UniProtKB entries of InterPro IPR005810 (succinyl-CoA synthetase alpha) have histidine at column 102. Of the 951 UniProtKB entries of InterPro IPR061301 (AllF family), 764 have glutamine, 7 have histidine, and the rest have Ala (72), Ser (40), Thr (36), Ile (14), Val (7), Glu (4), Cys (2), Leu (1) or Lys (1); in 3 the column is not covered.
12. The motif G[KR]PHPM that carries His389 is present in 884 of the 951 AllF-family entries and in none of the 53 succinyl-CoA synthetase alpha entries. In all 884 its histidine is in the insert after match column 34.
13. AllG and AllF domains occur in one polypeptide. Of 1769 UniProtKB entries with the AllG domain PF06545, 150 also carry the CoA-ligase domain PF00549, 119 the CoA-binding domain PF02629 and 149 the AllF N-terminal domain PF27530; 1 carries the AllH domain PF11392. The 150 entries with PF06545 and PF00549 are 848-1039 residues long (median 1002; AllF is 555 and AllG 419), and none has histidine at column 102 (Ala 65, Ser 36, Thr 28, Gln 17, Cys 4).

## The two reports

- Run 1 (`allF-hypotheses/carbamoyltransferase-site-not-in-allf/openscientist.md`) maps SucD His247 to AllF Val293. That is wrong (result 4). Its conclusion that AllF has no histidine at the catalytic position is right.
- Run 2 (`allF-hypotheses/sca-alpha-phosphohistidine-retained/openscientist.md`) maps SucD His247 to AllF Gln467 and reads the loop GHAGA as QQIAT. That is what the PF00549 profile gives (result 2), but it is not the structural equivalent (result 3): the loop is absent, not substituted. Its statements that Met391 fills the histidine position, that His389 is the nearest histidine and that the power helix is kept are reproduced (results 6-8).

## Limits

- One superposition program (the tmtools port of TM-align) and one AllF structure. No second algorithm was run, and the AlphaFold model was not used, so residues 1-100 and the disordered residues 358-360 and 498-502 are not covered.
- The lobe windows (174-299, 300-502) and the permuted order of the Rossmann-like domain were chosen by hand and are inputs of the script.
- 3DMY is AllF alone. Nothing here says where AllG and AllH bind, which subunit holds the carbamoyltransferase site, or whether the dimer seen in the crystal exists in the enzyme.
- The distances of His389 to the superposed histidine depend on which lobe is given the role of the SucD C-terminal domain (result 7). The 4.5-5.0 A figure holds for lobe 2 only; if lobe 1 takes that role, as in the trans arrangement of result 9, His389 is 9.5-9.8 A away.
- A superposition shows where residues are, not what they do. That no phosphoenzyme forms, and whether His389 or the power helices take part in catalysis, are not shown.
- The CoA transplant is rigid, on a ligand-free crystal form, with no relaxation. It shows that the SucD binding pose is blocked in this structure, not that AllF cannot bind CoA.
- Column 102 is a profile column, and result 3 shows the profile register is off by 15 residues in AllF. The family counts in result 11 therefore say that no AllF-family member has the SucD loop sequence at that column (the seven histidines sit in contexts such as QSYDGHVKQLR, not GHAGA); they do not locate a structural equivalent in each sequence.
- The co-occurrence counts in result 13 are counts of Pfam cross-references on UniProtKB entries, most of them unreviewed. Domain order, redundancy and taxonomic spread were not examined, and a read-through gene model would count as a fusion.
- The seven AllF-family entries with histidine at column 102 are all unreviewed and were not examined further.
