# MTH_1557 (O27599, FwdA): metal-site conservation against the M. wolfeii Fwd structure

## Method

`map_fwd_metal_sites.py` downloads PDB entry 5T5I (tungsten formyl-methanofuran
dehydrogenase Fwd(ABCDFG)2 of *Methanothermobacter wolfeii*, Wagner et al. 2016,
PMID:27846502) from RCSB, takes the canonical sequence of chain A (FwdA), aligns it
globally to O27599 (Needleman-Wunsch, BLOSUM62, linear gap -6), and maps every
residue that the mmCIF `_struct_conn` table lists as a metal ligand (`metalc`).

Run: `python3 map_fwd_metal_sites.py ../MTH_1557-uniprot.txt A <cache_dir>`

## Output (verbatim, output_chainA.txt)

```
5T5I chain A (Tungsten formylmethanofuran dehydrogenase subunit fwdA): 569 aa; target MTH_1557-uniprot.txt: 569 aa
aligned positions 569, identical 542 (95.3% of aligned)
  HIS57 (label_seq) -> ZN A602: target H57
  HIS59 (label_seq) -> ZN A602: target H59
  ARG69 (label_seq) -> K A604: target R69
  ARG72 (label_seq) -> K A604: target R72
  SER76 (label_seq) -> K A604: target S76
  KCX178 (label_seq) -> ZN A601: target K178
  KCX178 (label_seq) -> ZN A602: target K178
  HIS231 (label_seq) -> ZN A601: target H231
  ASP264 (label_seq) -> K A605: target D264
  HIS271 (label_seq) -> ZN A601: target H271
  ASP300 (label_seq) -> K A605: target D300
  VAL340 (label_seq) -> MG A603: target V340
  THR344 (label_seq) -> MG A603: target T344
  ASP385 (label_seq) -> ZN A602: target D385
  ILE412 (label_seq) -> NA A610: target I412
  GLY414 (label_seq) -> NA A610: target G414
  LEU416 (label_seq) -> NA A610: target L416
```

## Interpretation

- The M. wolfeii FwdA chain (569 aa) and O27599 (569 aa) align end to end with
  95.3% identity, so the structure is a close template for FwdA of strain Delta H.
- The two zinc ions of the FwdA active site (ZN A601, ZN A602) are bridged by the
  carboxylated lysine KCX178 and held by His57, His59, His231, His271 and Asp385.
  All seven ligand positions are conserved in O27599 (H57, H59, K178, H231, H271,
  D385). This is the binuclear-metal site of the amidohydrolase superfamily
  (cd01304 FMDH_A; Pfam PF07969 Amidohydro_3).
- The Mg, K and Na sites are backbone-carbonyl or solvent-exposed sites that
  are probably from the crystallisation buffer; they are not taken as functional.
- Conclusion: O27599 carries a conserved binuclear Zn site with a carbamylated
  lysine bridge, consistent with FwdA catalysing the amide-forming
  (formate + methanofuran) half reaction.
