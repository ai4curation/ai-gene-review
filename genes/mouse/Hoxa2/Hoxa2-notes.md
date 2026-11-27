# Hoxa2 (mouse, P31245) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Hoxa2 is the experimentally characterised donor for the donkey
EQUAS/HOXA2 (A0A9L0JBM7) rows. Both are in PANTHER subfamily PTHR45664:SF3
(HOMEOBOX PROTEIN HOX-A2), per `interpro/panther/PTHR45664/PTHR45664-entries.csv`
and the UniProt DR PANTHER line. No ProtNLM2 output was opened or used.

### Deep research
`just deep-research-falcon mouse Hoxa2 --fallback perplexity-lite` failed. Falcon
returned 403 Forbidden at the Edison auth endpoint, and perplexity reported 401
insufficient_quota. No deep-research file exists. The review is built from the
cached GOA publications plus four key papers fetched with `just fetch-pmid`
(PMID:9636074, 18547144, 22223247, 25640223).

### Evolutionary grounding
- SF3 holds only HOXA2/hoxa2 orthologs (human O43364, rat P31246, chicken, bovine,
  zebrafish hoxa2b, and others). Human-to-mouse ISO/Compara transfers stay inside SF3.
- The IBA rows come from PANTHER:PTN005228379, a deep anterior-Hox ancestral node.
  Its donors include mouse Hoxa2 itself (MGI:96174), so there is experimental
  grounding on this target. PAINT propagated only DNA binding, Pol II TF activity,
  Pol II transcription regulation and nucleus. No developmental process was
  propagated, which I treat as a deliberate decision.

### What is experimentally established in mouse (for transfer)
- Sequence-specific binding of Pol II cis-regulatory DNA:
  - the Six2 promoter [PMID:15634706 "Hoxa2 binds to this promoter region"];
  - the Robo2 Hox-Pbx site by ChIP [PMID:18547144 "Robo2 is a direct target of Hoxa2 in vivo"];
  - genome-wide ChIP-seq [PMID:22223247 "Hox and Pbx-Hox recognition sequences"].
- Co-occupancy with Meis/Pbx and enhancement of Meis binding [PMID:25640223].
- Repression (Six2) and activation (Krox20 element C, Robo2).
- Nuclear localization by IHC [PMID:10536059].
- Second-arch selector and A-P identity, by loss and gain of function
  [PMID:7903600, 7903601, 16221728, 25889273].
- r2/r3 identity and D-V hindbrain patterning [PMID:9367425, 10230789].
- Restriction of chondrogenesis upstream of Sox9 and of dermal bone upstream of
  Cbfa1/Runx2 [PMID:9636074]; Runx2 repression in ST2 cells [PMID:21324897].
- Repression of crest neurogenesis [PMID:18164701]; pontine neuron migration via
  Robo2 [PMID:18547144].
- Only the molecular function (TF activity, DNA binding) and nuclear location
  are both experimental here and phylogenetically propagated. The developmental
  processes are mouse-specific experimental findings. They are plausibly
  conserved across SF3, but PAINT did not propagate them.

### Issues found
- PMID:7508007 (SV40 T-antigen PNET tumour paper) is cited by MGI for the
  rhombomere 2 IMP and rhombomere 3 IGI rows. It is unrelated to Hoxa2. The terms
  are kept (supported by PMID:9367425 / 10230789) and the citation is recorded as
  a WRONG_REFERENCE source defect.
- GO:0035284 brain segmentation: PMID:7903601 says rhombomeric segmentation is
  not affected. The phenotype is segment identity, so the row is kept as non-core
  with this caveat.
- Two rows are UNDECIDED: the muscle structure development row (PMID:25889273,
  abstract has no muscle data) and the retinoic acid response row
  (PMID:23723417, abstract does not mention Hoxa2).

### NEW proposals
- GO:0032331 negative regulation of chondrocyte differentiation (PMID:9636074).
- GO:2001222 regulation of neuron migration (PMID:18547144, via direct Robo2
  regulation). It is a regulation term and not migration itself, because Hoxa2
  sets guidance-receptor levels rather than executing migration.
