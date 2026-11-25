# olf413 (Q6NP60) review notes

## Identity
- "MOXD1 homolog 2"; copper type II ascorbate-dependent monooxygenase family (PANTHER PTHR10157:SF40), paralog of Tbh (SF29).
- Predicted TM segments at 47-67 and 740-760 (UniProt).

## Literature
- Only primary paper: Ramya et al. 2024.
  [PMID:38326892 "Homozygous loss of function mutants show reduced levels of octopamine, and this finding supports the proposed function of the gene in octopamine biogenesis."]
  [PMID:38326892 "We find that, in all the trials, the mutant heads consistently showed reduced quantity of octopamine compared to that of the head samples from the control."]
  [PMID:38326892 "loss of function of olf413 causes embryonic lethality"]
- No enzymology. Tbh nulls are octopamine-less [PMID:8656284 "T beta h-null flies are octopamine-less but survive to adulthood."] (see Tbh review), so olf413 cannot replace Tbh.

## PAINT
- GO:0004836 IBA from PTN000016555 (taxon Ecdysozoa), seeded only by WB tbh-1; Tbh's own IBA comes from PTN002562791.

## Decisions
- Core MF: family-level GO:0016715; TBH activity rows UNDECIDED (no biochemistry; paralog).
- dopamine beta-monooxygenase and extracellular region: over-annotations.
- octopamine biosynthesis kept as non-core (IMP shows partial reduction; mechanism unresolved).

## Deep research (falcon) additions
- [file:DROME/olf413/olf413-deep-research-falcon.md "decreased octopamine in a mutant demonstrates a pathway association, not that purified Olf413 converts tyramine directly into octopamine"]
- Independently supports leaving TBH activity UNDECIDED and octopamine biosynthesis non-core.
