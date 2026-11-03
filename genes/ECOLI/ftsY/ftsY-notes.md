# ftsY (E. coli K-12) review notes

## 2026-11-02

Reviewed as an experimentally characterized exemplar for the bacterial SRP
cotranslational targeting module. No deep-research provider run was made for
this gene in this session (no provider credentials available); the review rests
on the Swiss-Prot record and the cached publications cited by GOA. All seeded
GOA rows were reviewed against the cached abstracts or full texts.

Key evidence:

- FtsY binds SRP like the mammalian receptor [PMID:8107852, "Here we show that
  the Ffh/4.5S ribonucleoprotein binds tightly to FtsY in a GTP-dependent
  manner."] and is required for export [PMID:8194520, "Depletion of FtsY is
  shown to cause the accumulation of the precursor form of beta-lactamase, OmpF
  and ribose binding protein in vivo"].
- The SRP and receptor GTPases share an active site [PMID:17682051, "form a
  unique complex in which hydrolyses of both guanosine triphosphates (GTP) are
  activated in a shared active site"].
- FtsY is almost entirely membrane-bound in vivo [PMID:19912622, "the vast
  majority of FtsY was localized to the inner membrane and that soluble FtsY
  constituted only a negligible species in vivo"], so the cytosol row is kept as
  non-core.
- (p)ppGpp inhibits FtsY rather than FtsY carrying out the stringent response
  [PMID:35217658, "(p)ppGpp binds to the SRP GTPases Ffh and FtsY, and inhibits
  the formation of the SRP receptor-targeting complex"].

## 2026-11-03

PR #5924 review: added GO:0005543 phospholipid binding as a NEW IDA row and a
core function. Binding is direct [PMID:19414018, "both helices bind to
negatively charged phospholipids, with a preference for phosphatidyl
glycerol"], also involves PE [PMID:11353766, "FtsY assembles on membranes via
interactions with phosphatidylethanolamine"], and the membrane contact is
needed for function [PMID:19912622, "requires membrane contact of FtsY for
efficient SRP-RNC recruitment"]. GO:0005543 rather than phosphatidylglycerol
binding, because the evidence covers both PG and PE.
