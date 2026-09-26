# Does human ADM5 retain what a functional adrenomedullin-family peptide needs?

Run 2026-09-26. Script: `analyze_adm5.py` (no dependencies; fetches live from the UniProt
REST API and computes the alignment — nothing is hardcoded). Raw output: `run-output.txt`.

## Why this was asked

Human ADM5 (C9JUS6) carries **seven IBA annotations** asserting hormone activity, adrenomedullin
receptor signalling, and regulation of blood pressure, heart rate and urine volume — all
propagated from the ancestral AM5 node. But UniProt's own function line for the human entry reads
"Probable non-functional remnant of adrenomedullin-5", and every functional AM5 experiment in the
literature is in pufferfish, medaka, Xenopus, pig, rat or sheep. The question is whether the human
protein could execute the propagated functions at all.

Reference: pig ADM5 (A5LHG2), the reviewed mammalian ortholog with an experimentally
characterised, feature-annotated mature peptide.

## What a functional peptide of this family requires

1. The intramolecular **disulfide ring** (C-x-x-x-x-C).
2. **C-terminal alpha-amidation** — encoded in the precursor as the amidated residue followed by
   a glycine donor and a dibasic cleavage site (`X-G-[KR][KR]`). Amidation is required for
   receptor activation across the CGRP/adrenomedullin family, so losing the signal abolishes
   hormone activity no matter what else survives.

## Result

| Feature | Pig (functional) | Human | Verdict |
|---|---|---|---|
| Mature peptide | residues 26–77, annotated | no peptide feature | — |
| Disulfide ring | C38–C43 | C39–C44 | **retained** |
| Amidated residue | Tyr77 (Tyrosine amide) | projects to Pro92 | lost |
| Amidation motif after it | `GRR` | `GFR` | **lost** — no dibasic |
| `G[KR][KR]` anywhere in the protein | **two** (pos 68 `GRK`, pos 78 `GRR`) | **none** | **lost** |
| Length | 108 aa | 153 aa (+45 C-terminal) | diverged |

Global identity across aligned columns: 52/108 (48.1%).

## Reading

**The ring survived; the amidation signal did not.** That combination is the informative one. A
retained disulfide ring is the kind of feature that keeps a degenerate sequence looking plausible
to similarity- and phylogeny-based methods — it is why the IBA node reaches this gene at all —
while the feature that actually licenses receptor activation is gone.

The single most robust line in the table is the last one, because it does **not** depend on the
alignment: scanning each sequence independently, pig contains two `G[KR][KR]` motifs and human
contains none. The projected position of pig Tyr77 onto human Pro92 *is* alignment-dependent and
should be treated as indicative only — the offset is large, and the two proteins have clearly
diverged in that region (consistent with the 45-residue C-terminal extension in human, the shape
a frameshift leaves).

This was reached independently of UniProt's curated judgment and agrees with it.

## Limitations, stated plainly

- Two sequences only. This is a targeted feature check against one functional reference, not a
  phylogenetic reconstruction of when AM5 was lost in the primate lineage.
- Absence of a `G[KR][KR]` motif is strong evidence against amidation but is a motif argument,
  not a measurement; nobody has assayed the human peptide.
- The analysis cannot exclude that human ADM5 acquired some unrelated function, only that it
  cannot act as an amidated adrenomedullin-family hormone.
- It says nothing about whether the locus is transcribed. UniProt lists human ADM5 at protein
  existence level PE=2 (evidence at transcript level).
