# CMPK2 notes

## 2026-11-25

CMPK2 is the human outlier in PTHR10344. The existing family review already distinguishes the
true thymidylate kinases from vertebrate CMPK2 and records the PAINT IRD at PTN001620248 for
GO:0004798 dTMP kinase activity. `just paint-losses human CMPK2` reported only that loss:
PTN001620248 blocks the root dTMP kinase node PTN000038985 and is not re-annotated below.

Human CMPK2 experimental support:

- PMID:17999954 cloned the mitochondrial UMP-CMP kinase, localized it to mitochondria by GFP
  fusion, mapped the mitochondrial targeting signal to the N-terminal 22 aa, and assayed
  phosphorylation of dUMP, dCMP, CMP and UMP with ATP. This is the main evidence that the dUMP
  and dCMP kinase activities are real and that dTMP is not the characterized substrate set.
- PMID:23416111 is abstract-only locally and mostly discusses AK9. UniProt cites it for CMPK2
  nucleoside-diphosphate kinase activity; the GOA IDA row is accepted by deferring to the
  UniProt full-text curation rather than second-guessing it from the AK9-forward abstract.
- PMID:34142025 and PMID:37075076 place induced CMPK2 at mitochondria during DENV/ZIKV work and
  support its flavivirus restriction role. The ZIKV study also shows the N-terminal domain is
  sufficient for that antiviral effect even though the kinase domain supplies CMP/UMP/dCMP/dUMP
  phosphorylation.
- PMID:36443312 links recessive CMPK2 loss of function to brain calcification and shows mutant
  CMPK2 constructs lose mitochondrial localization in cell assays. The phenotype is useful
  context but not a direct GO annotation here.

Family and module scope:

- Keep PTHR10344 as a family review and simply attach the CMPK2 review path. Its term
  assessments already carry CMPK2 member exceptions for the dTMP/dTDP/dTTP rows.
- Do not extend `modules/thymidylate_synthesis.yaml` or `modules/dntp_de_novo_synthesis.yaml`;
  both model the DTYMK dTMP-to-dTDP step and intentionally exclude CMPK2.
- Do not create a one-member CMPK2 module. The antiviral flavivirus activity is real, but the
  current evidence does not identify a reusable multi-part mechanism with a GO-CAM or module
  boundary that belongs in this family PR.
