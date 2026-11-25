# HP1507 construct and NADP-contact assessment

## 2026-11-05 manual interpretation

The 8H52 PDB header identifies native residues 1–399 as UniProt A0A2X5A3P4, not O26037. Residues −5 through 0 are an expression tag. The native NCTC11637 protein is therefore 399 residues, whereas frozen O26037 from 26695 is 385 residues. Aligning the shared C-terminal region places O26037 residue 1 at native residue 15 (V in the structural construct, M in O26037); native residues 1–14 are absent. This explains the previously observed 20-residue difference including the six-residue tag.

**The absent segment contributes directly to the deposited NADP-binding geometry.** Among native residues 1–14, five have a heavy atom within 4.0 Å of the NAP ligand: Gly8 (3.947 Å), Ala9 (3.287 Å), Gly10 (3.053 Å), Gly11 (2.906 Å), and Val12 (3.258 Å). For example, the backbone nitrogen of Gly11 is 2.906 Å from NADP atom O1N, and the backbone nitrogen of Ala9 is 3.287 Å from O3B. These are coordinate distances, not experimentally assigned binding energies or proof of specific hydrogen bonds. Results are in `results/8H52-NADP-contacts.json`.

The same generic script was run on the independent C. jejuni decarboxylase structure 3N29 using ligand PLP and residues 35–45. It recovered the expected close contact of Lys41 NZ to PLP C4A (1.531 Å), consistent with the Schiff-base linkage described in PMID20534592, and an Ala39 contact (3.344 Å). This control tests parsing, ligand selection, residue ranges and distance calculations on another protein; it is not biological evidence about HP1507.

The missing region is thus not merely a dispensable terminal tail inferred from sequence identity. Loss of its cofactor-contacting backbone creates a target-specific reason to withhold transfer of NADPH-dependent catalytic activity to the exact shorter sequence. This does not prove that native 26695 lacks CASDH: the reference start may be incorrect, an alternative start may exist, or the shortened protein might retain activity through structural rearrangement. Neither the structure nor the accessible abstract tests these possibilities. The source literature full text remains inaccessible.

Consequently, withdraw the two previous NEW ISS claims and the core-function assertion for HP1507. Retain an unresolved CASDH-family candidate and a knowledge gap, with priority on verifying the native translation start and measuring NADP binding/product formation for exact 385-residue and extended constructs. Native substrate preference against agmatine is a second unresolved question even if cofactor competence is restored.

## Reproducibility and quality checklist

- [x] Script has no hardcoded input/output files, ligand, chain, residue interval or distance threshold.
- [x] Script was exercised on a second protein/ligand input (3N29/PLP).
- [x] Both analyses completed normally and found the requested ligand and protein atoms.
- [x] Raw input structures and direct JSON outputs are retained in this folder.
- [x] Interpretation identifies source, sequence correspondence, numerical results, and limits; coordinate proximity is not equated with demonstrated loss of activity.

Python 3.12.9; no third-party Python packages. Commands and URLs are in `justfile` and README.md. Data fetched from RCSB on 2026-11-05. Input SHA256:

- `3N29.pdb`: `592b46b8d9c81680947852e5fc5c9eead0183d05893d34ed4d0323d956fcb0ce`
- `8H52.pdb`: `ec3fc32013e43ff43b82b5318d266d71ff8723d1620a7079ea9564d56a05c85e`
