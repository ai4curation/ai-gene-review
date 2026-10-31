# awd (P08879, NDKA_DROME) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: the reviewed canonical awd product (awd-PE, 153 aa, FlyBase FBgn0000150). The
168-aa alternative-initiation model A0A0B4LHX6 is reviewed separately in `genes/DROME/awd/`.
I did not open any ProtNLM2 file or prediction-evidence folder for this review.

Deep research: `just deep-research-falcon DROME awd__P08879 --fallback perplexity-lite`
failed. Falcon gave "Exception: Failed to authenticate", and perplexity-lite gave HTTP 401
(insufficient quota). No deep-research file was produced. The review is based on the cached
primary literature below and the UniProt record.

### Evolutionary placement

- The PANTHER 19.0 classification files (`.cache/panther/PTHR19.0_*`) put P08879 in
  PTHR11349:SF91, together with yeast YNK1 (P36010) and worm ndk-1 (Q93576). In this release
  the human NME1 to NME4 proteins are each in a separate subfamily (SF69, SF57, SF54, SF49).
  Subfamily-level transfer from human NME proteins is therefore not justified by
  classification alone. Family-level NDPK activity is supported, though.
- PAINT puts NDPK activity, nucleoside triphosphate biosynthesis and cytoplasm at
  PTN000887110, a deep node spanning bacterial to animal NDPKs. Awd (FB:FBgn0000150) is one of
  its experimental donors.
- PAINT puts mitochondrion at a different node, PTN000142925, seeded by NME3, NME4, YNK1, a
  Dictyostelium mitochondrial NDPK and a plant one. There is no fly evidence that Awd is in
  mitochondria. I kept this row as non-core and flagged it as unverified.

### Experimentally established in Drosophila (usable for transfer)

- NDPK activity of the native, purified homohexamer [PMID:1320004 "Both proteins are purified
  as hexamers in their native state."], [PMID:2175255 "the awd gene codes for a nucleoside
  diphosphate kinase (NDP kinase)"].
- N-delta phosphohistidine intermediate, seen in the crystal structure [PMID:7669763 "the
  active site histidine was phosphorylated on N delta, and it was the only site of
  phosphorylation"].
- Catalysis is required in vivo: an H119A transgene does not rescue [PMID:8806830 "cannot be
  rescued at all by a transgene ... with a mutation that eliminates NDP kinase activity by
  replacement of the active site histidine with alanine"]. Human nm23-H2 rescues, but nm23-H1
  does not.
- Microtubule association and cytoplasmic location [PMID:2175255].
- Genetic requirement in dynamin-dependent endocytosis [PMID:11343655 "NDK regulates synaptic
  vesicle internalization at the stage where function of the dynamin GTPase is required"].
  The same requirement shows up in Btl/FGFR turnover in trachea [PMID:14630942], in
  Rab5-dependent adherens-junction turnover in follicle cells [PMID:19581292], and in Notch
  progression through early endosomes [PMID:24528630 "Notch accumulates in enlarged early
  endosomes"].

### Not established

- Local GTP supply to dynamin or Rab5. Authors propose it, but it has not been measured. I
  did not add an endocytosis process term as NEW: the evidence shows necessity rather than
  participation. I raised it as a suggested question instead.
- Protein (histidine-dependent) kinase activity on ovalbumin [PMID:8579610]. This is a single
  in vitro report and is not annotated.
- Mitochondrial location (IBA/ISS only).

### Action summary

- ACCEPT: NDPK activity (all 7 rows); cytoplasm (IBA, IEA); GTP, UTP and CTP biosynthesis
  (IEA and TAS rows); NTP, rNTP and dNTP biosynthesis.
- MODIFY: kinase activity → NDPK activity; cytoskeleton → microtubule; nucleotide metabolic
  process → GTP, UTP, CTP and dNTP biosynthesis.
- KEEP_AS_NON_CORE: ATP, GTP and Mg binding; microtubule; microtubule binding; plasma membrane
  (HDA); mitochondrion (IBA, ISS); mitotic cell cycle; microtubule-based process; all the
  tracheal and follicle-epithelium developmental terms.
- UNDECIDED: nuclear microtubule (an IMP-based location; cannot be checked from the abstract).
