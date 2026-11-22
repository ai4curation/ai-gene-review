# vps1302 bioinformatics results

## 1. Relationship of Spo2 (C6Y4C2) to Vps1302 (O42926)

Script: `compare_spo2.py` (run with `uv run --script compare_spo2.py`). It reads both
sequences from the UniProt flat files in the gene folders.

Output (2026-10-21):

```
vps1302 (O42926) length: 3131
spo2 (C6Y4C2) length: 133
Exact match of full Spo2 at vps1302 residues 2999-3131
Best ungapped placement: vps1302 2999-3131, 133/133 identical (100.0%)
Spo2 residue 1: M; vps1302 residue at placement start: M
vps1302 C-terminal end reached by placement: True
```

Interpretation: the entire Spo2 protein is identical to the last 133 residues of
Vps1302 (residues 2999-3131), and Spo2 Met1 corresponds to Vps1302 Met2999. Spo2 is
therefore a nested product of the 3' end of the vps1302 locus, not a homologue.
A consequence for interpreting phenotypes: a full-length vps1302 deletion also removes
the Spo2 coding sequence, so meiosis/sporulation phenotypes of vps1302 deletion
strains cannot be attributed to the long Vps1302 protein alone.

## 2. Family and subfamily placement (from repository PANTHER files)

Source: `interpro/panther/PTHR16166/PTHR16166-entries.csv` and
`interpro/panther/PTHR16166/PTHR16166-paint.tsv`.

- O42926 (vps1302) is in PTHR16166:SF93 "INTERMEMBRANE LIPID TRANSFER PROTEIN VPS13",
  the same subfamily as S. cerevisiae VPS13 (Q07878), Drosophila Vps13 (A1Z713) and
  Chaetomium thermophilum VPS13 (G0S3B8).
- The S. pombe paralog vps1301 (P87319) is in a different subfamily, PTHR16166:SF145.
- PAINT nodes reaching vps1302: PTN000414878 (phospholipid transfer activity,
  intermembrane lipid transfer; seeded by SGD:S000003963 = S. cerevisiae VPS13) and
  PTN000414879 (mitochondrial outer membrane, endosome membrane, mitochondrion
  organization, macroautophagy).
- Terms experimentally annotated to S. cerevisiae VPS13 that PAINT did not propagate
  (e.g. prospore membrane, Golgi to endosome transport, nucleus-vacuole junction,
  reticulophagy) are treated as deliberate omissions.
