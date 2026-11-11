# mllDE (C5B1I6, MexAM1_META1p4134) notes

## 2026-10-16: cytoplasm NEW row withdrawn (issue #4419)

The review previously carried a reviewer-proposed `NEW` annotation to
GO:0005737 cytoplasm (NAS). Its only `supported_by` quote was the falcon deep
research stating the opposite of support:
["No retrieved source directly determines the **subcellular localization** of
the mllDE gene product" -- file:METEA/mllDE/mllDE-deep-research-falcon.md].

Rechecked for direct sequence evidence before deciding:

- UniProt C5B1I6 (TrEMBL, PE 4) carries no `FT SIGNAL`, `FT TRANSMEM` or
  `CC SUBCELLULAR LOCATION` lines; the only feature is the PROSITE Carrier
  domain (4..82). Absence of a predicted feature in an unreviewed entry is not
  a positive localization call.
- The perplexity deep research asserts that "standard transmembrane topology
  prediction algorithms do not identify membrane-spanning helices or signal
  sequences", but names no predictor, run, or output, and cites only the
  cluster papers; it also concedes that direct experimental verification of localization "has
  not been reported in the primary literature". This is an
  unvetted LLM summary, not checkable sequence evidence.
- No GOA row for mllDE asserts any cellular component.

Decision: removed the NEW cytoplasm row rather than keep a localization that
rests only on the absence of targeting features (the default-localization
pattern). Biosynthesis of NIS/NRPS-type metallophores is generally cytosolic,
so cytoplasm remains plausible. A clean negative from a signal-peptide/TM
predictor (e.g. SignalP 6 / DeepTMHMM on the C5B1I6 sequence) would still be
an argument from absent features and should not on its own re-open the
proposal. Positive grounds would be a fractionation/tagging experiment on
MllDE, or a primary publication placing the AsbD/AsbE homologs (petrobactin
NIS assembly machinery) in the cytoplasm, which the perplexity report asserts
but does not anchor to a resolvable citation.
