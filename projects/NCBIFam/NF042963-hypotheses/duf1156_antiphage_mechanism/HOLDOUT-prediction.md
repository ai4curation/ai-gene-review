# Held-out prediction (recorded BEFORE the OpenScientist run)

Recorded 2026-07-18, prior to reading `openscientist.md`. This is our own
independent inference from UniProt/InterPro/domain evidence, held out so the
OpenScientist conclusion can be compared against it blind. **Not fed into the
prompt** (the prompt gives only the phenotype + representative sequence).

## Our expectation for NF042963 / DUF1156

- Mechanism: the ~1000-aa members are **N6-adenine, SAM-dependent DNA
  methyltransferases** (a bona fide MTase module), i.e. **modification-based**
  anti-phage defense (epigenetic marking of self DNA / restriction-modification-
  or BREX/DISARM-like methylation), **not** a nuclease or abortive-infection
  effector as the primary activity.
- Evidence base (public, not our holdout bioinformatics): family members carry
  InterPro **IPR029063** (S-adenosyl-L-methionine-dependent methyltransferase
  superfamily) and, in a subset, **IPR014455** (DNA methylase, N-6 adenine-
  specific, MK1259 type); several members are already UniProt-named "Adenine-
  specific DNA methylase, contains a Zn-ribbon domain".
- DUF1156 (PF06634 / IPR009537) itself is predicted to be **accessory**
  (nucleic-acid-binding / targeting), not the catalytic MTase, per its Pfam
  "may bind nucleic acids" structural note.

## What would make the OpenScientist run *add* value beyond this

1. Structural (Foldseek) confirmation that the MTase module has an **intact**
   catalytic site with the N6-adenine **DPPY/NPPY** motif and the Rossmann SAM-
   binding motif (vs a degraded/pseudo-MTase).
2. A structure-grounded call on **what DUF1156 actually is** (the currently
   "unknown function" domain) and the role of the Zn-ribbon.
3. Which specific defense class (plain RM vs BREX/DISARM/other) the architecture
   implies.

## GO consequence to revisit after the run

If confirmed an N6-adenine DNA MTase: the seed's BP mapping
`GO:0051607 defense response to virus` could be complemented by an **MF** term
(site-specific DNA-methyltransferase / N6-adenine-specific activity), and the
`proposed_new_terms` "defense response to bacteriophage" request stands. If the
MTase site is degraded (pseudoenzyme), the mechanism is something else and the
MF mapping must be withheld.
