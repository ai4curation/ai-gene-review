# P2rx2 (rat, P49653) review notes

## Session 2026-10-28

- `just fetch-gene rat P2rx2` resolved UniProt P49653 (P2RX2_RAT), with 91 GOA rows.
  `just fetch-gene-pmids` cached the 16 GOA PMIDs. I also cached key background papers
  (PMID:7523952, 8961184, 9119082, 10440098, 14672995, 16322458, 23345450, 15961431,
  12937291, 17706883, 10813788, 12395104).
- No deep-research provider was available. The literature summary is in
  `P2rx2-deep-research-manual.md`.
- Full text was read for PMID:18616429, PMID:16000618 and PMID:11160443. The other GOA
  papers are abstract-only.

### Key judgements

- Core: extracellularly ATP-gated non-selective cation channel (GO:0004931), in the plasma
  membrane, as homo- or heterotrimers (signaling receptor complex)
  [UniProt P49653 "ATP-gated nonselective transmembrane cation channel permeable to potassium, sodium and calcium"].
- PMID:18616429 (key paper): cysteine scanning of pre-TM2 in rat P2X2. Surface biotinylation
  in HEK-293 cells directly supports the cell surface IDA
  ["The mutant K308A was efficiently expressed at the cell surface"]. This row is kept as
  non-core because plasma membrane is the better location term.
- Neuronal action potential (IDA/IMP from 16190872, 16934235, 15317863): the abstracts
  describe voltage-clamp recordings of ATP-gated currents (oocytes, HEK cells, trigeminal
  neurons), not action potentials
  [PMID:16190872 "the cDNA for the wild-type receptor was injected to Xenopus laevis oocytes and examined 48-72 h later by the two-electrode voltage-clamp technique"].
  I marked these MARK_AS_OVER_ANNOTATED rather than removing them, because the full texts
  were not available, and flagged them for an expert.
- Response to ischemia (IMP, PMID:12849743): the evidence is upregulation plus
  non-selective P2 antagonists (suramin, basilen blue), so MARK_AS_OVER_ANNOTATED.
- The four generic protein binding IPI rows (P2X3, P2X4, P2X6 heteromers) were removed under
  the protein-binding policy. Heteromer assembly is captured by the signaling receptor complex
  and channel rows.
- Protein-containing complex binding (IDA, from the trimer and stoichiometry papers):
  subunit co-assembly is not binding to a complex, so MARK_AS_OVER_ANNOTATED.
- Metal binding (Cu, Zn, Ni, Co, Cd, Hg; PMID:16190872, 17517890): all are allosteric
  modulators that potentiate ATP currents, Cu and Zn through the His120/His192/His213/His245
  site. Kept as non-core. Mercury acts at a different, histidine-independent site.
- Phosphatidylinositol binding (IMP, PMID:16857707): modified to GO:1901981
  phosphatidylinositol phosphate binding, because the data show binding to PIPs and PIP2s.
- Mouse ISO rows: the hypoxia/carotid body, taste, hearing, pain, peristalsis, NMJ and
  synaptic transmission rows are kept, because the receptor does part of the work by
  transducing ATP. Response to carbohydrate, bladder smooth muscle contraction and skeletal
  muscle fiber development are MARK_AS_OVER_ANNOTATED, because each over-interprets an
  afferent or secondary phenotype. Neuronal dense core vesicle is UNDECIDED (source not
  traced).
- No NEW annotations were added. The knockout phenotypes alone do not justify new process
  terms, and the channel and synaptic transmission terms already capture what the protein does.
