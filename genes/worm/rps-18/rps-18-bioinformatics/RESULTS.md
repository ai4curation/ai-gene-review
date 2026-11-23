# rps-18 (O18240, uS13) structural contact analysis

Script: `us13_contacts.py` (run with `uv run --script us13_contacts.py [9CAI.cif.gz]`;
downloads PDB 9CAI from RCSB if no path is given). The uS13 chain is identified from the
mmCIF struct_ref mapping to UniProt O18240, not hardcoded.

## Input

PDB 9CAI, cryo-EM structure of the C. elegans 80S ribosome (2.59 A; Sehgal et al. 2024,
PMID:39209556). Contact cutoff: any atom pair within 4.0 A.

## Output (verbatim from the run of 2026-10-28)

```
Entities mapped to O18240: ['16'] [("'Small ribosomal subunit protein uS13'", 'polymer')]
uS13 chain(s): ['AS']
RNA chains: {'DA': 'tRNA', 'A7': "'5S rRNA'", 'A8': "'5.8S rRNA'", 'B2': "'18S rRNA'", 'A5': "'28S rRNA'", 'DC': 'mRNA'}
RNA chain B2 ('18S rRNA'): 50 uS13 residues within 4.0 A of 35 nucleotides
  uS13 residues: ARG24 LYS25 TYR28 THR31 ILE33 LYS34 GLY35 VAL36 GLY37 ARG38 ARG39 PHE40 ASN53 ARG55 TRP82 PHE83 LEU84 ASN85 ARG86 GLN87 LYS88 GLN97 VAL103 LEU107 ASP110 LEU111 ARG113 MET114 HIS120 ARG121 ARG124 HIS125 LEU129 ARG130 VAL131 ARG132 GLY133 GLN134 HIS135 THR136 LYS137 THR138 THR139 GLY140 ARG141 LYS142 GLY143 ARG144 THR145 VAL146
RNA chain DA (tRNA): 5 uS13 residues within 4.0 A of 4 nucleotides
  uS13 residues: ARG144 THR145 GLY147 VAL148 SER149
```

## Interpretation

- RPS-18/uS13 is chain AS of the C. elegans 80S structure and makes extensive direct
  contacts with 18S rRNA (50 uS13 residues within 4 A of 35 nucleotides), spanning the
  N-terminal helix-two-turn-helix region (residues 24-40) and the basic C-terminal region
  (residues 113-146). This is direct structural evidence that the worm protein binds rRNA
  in the assembled small subunit.
- Five residues of the C-terminal tail (144-149) lie within 4 A of the tRNA modelled in the
  structure. This is consistent with the conserved contact of the uS13 C-terminal tail with
  the tRNA in the ribosome, but the analysis does not establish which tRNA site is occupied
  and a contact in one structure is not by itself evidence of a tRNA-binding function.
- No 28S rRNA contacts were found at this cutoff.
