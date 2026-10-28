# Slik review notes

## Session 2026-10-28

- `just fetch-gene DROME Slik` resolved A4UZU8 (TrEMBL, FlyBase FBgn0035001, GeneID 37893),
  17 GOA rows. First attempts hit UniProt timeouts/429; succeeded on retry.
- Deep research providers unavailable; manual synthesis in `Slik-deep-research-manual.md`.
- Both GOA-cited papers (PMID:17060498, PMID:18283112) have full text cached and were read.
  Additional papers cached: 14624240, 15371338, 20215404, 25061859, 26170449, 31511253,
  32960945, 37794497, 40050674.

### Decisions

- Kinase MF: GO:0004674 accepted (IEA, IMP, IDA). The IDA from PMID:17060498 is weakly
  grounded in that paper itself (the authors state it is unclear whether Slik directly
  phosphorylates Merlin/Moesin [PMID:17060498 "It remains unclear whether Slik itself can
  directly phosphorylate either protein"]); accepted because direct in vitro kinase activity
  is shown in PMID:26170449 and PMID:32960945.
- GO:0106310 protein serine kinase activity (Rhea IEA): all documented sites are Thr
  (Moesin T559, Talin T152, activation-segment Thr); marked over-annotated.
- General MF terms (kinase activity, transferase activity, protein kinase activity,
  nucleotide binding) -> MODIFY to the specific supported terms.
- Mitotic process IMPs (spindle orientation, spindle organization, cell morphogenesis) kept
  as non-core: Slik acts on the cortex via Moesin, spindle phenotypes are downstream.
  Metaphase/anaphase transition marked over-annotated (delay is attributed by the authors to
  spindle defects; Slik is not a cell-cycle transition regulator).
- Spindle midzone IDA: not found in the text of PMID:18283112 (Slik parallels cortical
  p-Moesin); figure-only evidence cannot be checked -> UNDECIDED.
- NEW: apical cortex (PMID:26170449) and STRIPAK complex association (PMID:32960945,
  reciprocal co-IP of tagged proteins). No NEW process terms proposed (per NEW-term bar;
  cytoneme formation and JNK-apoptosis suppression left as questions).
