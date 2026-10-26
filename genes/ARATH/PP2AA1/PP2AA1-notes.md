# PP2AA1 (RCN1, EER1; At1g25490; Q38845) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative (co-ortholog by phylogeny) of
WHEAT/F6LAX4. No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon ARATH PP2AA1 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity fallback returned HTTP 401 (quota exceeded). No
deep-research file exists. The review was built from the UniProt record, the PAINT rows for
PTHR10648, and cached publications (most abstract-only; full text for PMID:18162590,
PMID:25085430, PMID:26888284, PMID:25628632).

### Evolutionary placement

- PANTHER PTHR10648:SF29 ("A alpha isoform"), per UniProt DR line and
  `interpro/panther/PTHR10648/PTHR10648-entries.csv`. The wheat target sits in SF4. This is a
  subfamily-model boundary, not a functional divide; all A subunits descend from
  PTN000068663 (eukaryotic A-subunit node: PP2A complex, nucleus, cytosol) and PTN000068596
  (cytoplasm; protein phosphatase regulator activity in the GOA snapshot; protein complex
  scaffold activity in the 2026-06-03 PAINT snapshot).
- PAINT did not propagate the animal/fungal PTN000068664 terms (spindle assembly,
  meiotic centromeric cohesion) to plants. I treat that as deliberate and add nothing of the kind.
- The NOT cytosol IRD at PTN000068762 is a single PP2AA3 leaf. It does not cover PP2AA1, and the
  family review judges it unjustified.

### What is experimentally established in Arabidopsis (for later transfer)

- PP2A A-subunit identity and scaffolding: RCN1 complements yeast tpd3-1
  [PMID:8641277 "The RCN1 gene rescues the rcn1 mutant phenotype and also complements the
  temperature-sensitive phenotype of the Saccharomyces cerevisiae PP2A-A mutation, tpd3-1."].
  Interactions with C (PP2A-5), B' and B''/TON2 subunits.
- Positive regulator of PP2A activity in vivo [PMID:10607292 "PP2A activity is decreased in
  extracts from rcn1 mutant seedlings, and this decrease is not due to a reduction in catalytic
  subunit expression."]. RCN1 is the dominant A isoform (PMID:14973165).
- Nucleus and cytosol [PMID:22404109 "the PP2A A-subunits A1, A2 and A3 all reside in both the
  nucleus and cytosol of the cell"], with developmentally regulated nuclear entry and membrane
  association (PMID:18162590).
- Genetic (rcn1) process roles: regulation of polar auxin transport and PIN1 internalization
  (PMID:11449059, PMID:26888284), positive regulation of early ABA signalling and ABA-induced stomatal
  closure (PMID:12417706), dampening of ethylene responses (eer1 = rcn1; PMID:11161061,
  PMID:12787251), negative regulation of PTI through the A1-C4-B'eta/zeta holoenzyme bound to BAK1
  (PMID:25085430). These are mutant-phenotype findings for a holoenzyme scaffold. Substrate-level
  mechanism is known only partly (PIN, BAK1 phosphostatus).

Inferred only (not experimental for this gene): protein complex scaffold activity term
assignment via PAINT (the experimental basis is complementation and subunit binding, not a
structure of the plant protein).

### Decisions

- Protein binding IPI rows: MODIFY to GO:0140378 for the PP2A-subunit partners (PMID:10091592 C
  subunit PP2A-5; PMID:11971138 TON2); REMOVE the others (ROC7, AtCHIP study, LIP1, RON3,
  phytohormone Y2H network) per policy.
- NEW GO:0140378 protein complex scaffold activity (IBA, current PAINT node PTN000068596).
- GO:0009926 auxin polar transport -> MODIFY to GO:2000012 regulation of auxin polar transport.
- Salicylic acid binding (HDA screen): MARK_AS_OVER_ANNOTATED. The paper says its PP2A candidate
  failed validation, but does not name the subunit.
- Cell wall HDA: MARK_AS_OVER_ANNOTATED (likely contaminant). Plasma membrane HDA: KEEP_AS_NON_CORE.
- PTI role not added as NEW. TAIR annotated only B'ZETA (GO:0045824) from PMID:25085430 (QuickGO
  check); raised as a suggested question instead.
