# ALKBH6 (Q3KRA9) review notes

## 2026-10-04: PAINT/affinage review

ALKBH6 is an AlkB-family dioxygenase whose substrates are free methylated nucleotides.
- **Substrates:** [PMID:40885392 "we demonstrate that ALKBH6 effectively demethylates N-7-methyl-GMP, and N-1-methyl-adenosine monophosphate."]
- **Substrate requirement:** a phosphate group is required, and there is no activity on bases or nucleosides.
- **2OG turnover:** measured directly (PMID:39845104).

Decisions:
- **2-oxoglutarate-dependent dioxygenase rows (IDA x2, IEA): ACCEPT.** No more specific GO term exists for demethylating free nucleotides, so an NTR "methylated nucleoside monophosphate demethylase activity" is proposed under GO:0016706.
- **Nucleus and cytoplasm (IBA, IDA, IEA): ACCEPT** (PMID:17979886, tagged protein in both compartments).
- **VCPKMT protein-binding row: REMOVE** per policy.
- **Knowledge gap:** PMID:33897761 reports E. coli alkB complementation and alkylation sensitivity in pancreatic cancer cells. That does not fit an enzyme with no nucleic-acid activity, so it is recorded as a BP_DARK gap.
