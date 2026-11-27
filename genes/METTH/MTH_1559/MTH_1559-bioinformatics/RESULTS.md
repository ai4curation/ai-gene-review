# MTH_1559 (O27601, FwdB): metal-site conservation against the M. wolfeii Fwd structure

## Method

`map_fwd_metal_sites.py` (same script as in the MTH_1557 folder) downloads PDB entry
5T5I (tungsten formyl-methanofuran dehydrogenase of *Methanothermobacter wolfeii*,
Wagner et al. 2016, PMID:27846502) from RCSB, takes the canonical sequence of chain B
(FwdB), aligns it globally to O27601 (Needleman-Wunsch, BLOSUM62, linear gap -6), and
maps every residue that the mmCIF `_struct_conn` table lists as a metal ligand.

Run: `python3 map_fwd_metal_sites.py ../MTH_1559-uniprot.txt B <cache_dir>`

## Output (verbatim, output_chainB.txt)

```
5T5I chain B (Tungsten formylmethanofuran dehydrogenase subunit B): 432 aa; target MTH_1559-uniprot.txt: 437 aa
aligned positions 432, identical 423 (97.9% of aligned)
  GLU138 (label_seq) -> MG A603: target E143
  GLY305 (label_seq) -> K A604: target G310
  CYS9 (label_seq) -> SF4 B501: target C14
  CYS12 (label_seq) -> SF4 B501: target C17
  CYS16 (label_seq) -> SF4 B501: target C21
  CYS35 (label_seq) -> SF4 B501: target C40
  SER40 (label_seq) -> K B506: target S45
  LYS41 (label_seq) -> K B506: target K46
  VAL43 (label_seq) -> K B506: target V48
  CYS118 (label_seq) -> W B502: target C123
  ASP128 (label_seq) -> CA B508: target D133
```

## Interpretation

- The M. wolfeii FwdB chain (432 aa) aligns to O27601 (437 aa) with 97.9% identity
  over 432 positions; O27601 numbering is offset by +5 from the PDB chain.
- The tungsten (W B502) is coordinated by the thiolate of Cys118 in 5T5I. The other
  W ligands (the dithiolene sulfurs of two MGD, metallopterin guanine dinucleotide,
  and a terminal sulfido ligand modelled as H2S) are non-protein partners, so the
  script does not print them; they are metalc43-47 of the 5T5I \_struct\_conn table
  (inspected by hand). The protein ligand maps to Cys123 of O27601.
- O27601 contains no selenocysteine: the UniProt sequence has no U, and the
  W-coordinating residue is a cysteine, as in M. wolfeii.
- The single [4Fe-4S] cluster of FwdB (SF4 B501; Cys9, Cys12, Cys16, Cys35 in 5T5I)
  maps to Cys14, Cys17, Cys21 and Cys40 of O27601, all conserved.
- Mg, K, Ca sites are not taken as functional.
- Conclusion: O27601 has the conserved tungsten-bis(pterin) site with a Cys ligand
  and one [4Fe-4S] cluster, the formate dehydrogenase-like CO2-reducing half of Fwd.
