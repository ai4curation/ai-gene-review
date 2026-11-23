# RSL1D1 (O76021) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RSL1D1 is reviewed in its own right as the closest experimentally
characterised relative of DROME/CG13096. ProtNLM2 outputs were not opened or used.

### Deep research

`just deep-research-falcon human RSL1D1 --fallback perplexity-lite` failed: falcon
raised "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review is based on the
publications cached in `publications/` (listed below), read directly.

### Evolutionary placement

- UniProt: "Belongs to the universal ribosomal protein uL1 family. Highly divergent."
  Pfam PF00687 (Ribosomal_L1), InterPro IPR023674/IPR028364/IPR016095.
- PANTHER 19.0 (local `.cache/panther/PTHR19.0_*`): RSL1D1 is PTHR23105:SF31
  "RIBOSOMAL L1 DOMAIN-CONTAINING PROTEIN 1". SF31 also contains mouse/rat Rsl1d1,
  budding yeast UTP30 (P36144), two S. pombe and two Arabidopsis proteins. Yeast CIC1
  (P38779) is in a different subfamily (SF203), and DROME CG13096 is in a different
  family altogether (PTHR48162:SF1). PTHR23105 itself in v19 lumps the L7Ae/L30e
  proteins (SNU13, NHP2, RPL7A) with uL1 (RPL10A).
- IBA rows: GO:0003723 RNA binding from PTN004606439, a deep node whose donors span
  L7Ae-family members (SNU13 P55769, NHP2 Q9NX24) as well as uL1-like proteins; and
  GO:0005730 nucleolus (is_active_in) from PTN000559994 with donors mouse Rsl1d1, yeast
  CIC1, yeast UTP30 and RSL1D1 itself. PAINT did not propagate any ribosome-biogenesis
  process or SSU-processome component term to RSL1D1, which I treat as a deliberate
  decision. No human experiment I could read places RSL1D1 in pre-rRNA processing.
- Implication for transfer to CG13096: only the general nucleolar localisation and
  RNA binding are shared at a level that phylogeny supports. The mRNA UTR binding,
  PTEN translation repression, MDM2/p53 regulation and senescence roles are
  RSL1D1-specific experimental findings in human cells and should not be transferred.

### Literature (human, experimental)

- Ma et al. 2008 [PMID:18678645 "CSIG interacted with PTEN mRNA in the 5' untranslated
  region"]; immunofluorescence "human CSIG is predominantly localized in the nucleolus";
  polysome fraction; PTEN 5'UTR reporter derepressed on knockdown; overexpression delays,
  knockdown accelerates replicative senescence. The full text contains no apoptosis
  experiments, so the GOA IDA "regulation of apoptotic process" keyed to this paper
  probably belongs to PMID:22419112 (UniProt FUNCTION line cites both).
- Li et al. 2012 [PMID:22419112 "p33ING1-CSIG axis functions as a novel pro-apoptotic
  regulator in response to DNA damage"]: UV-induced apoptosis via BAX; binds p33ING1.
- Meng et al. 2006 [PMID:17158916 "Loss of RSL1D1 expression reduces the compartmental
  size and amount of nucleostemin in the nucleolus"]: Y2H with mouse Rsl1d1, knockdown
  in human U2OS cells.
- Xie et al. 2016 [PMID:27811966 "CSIG interacts directly with the MDM2 RING finger domain
  and inhibits MDM2 E3 ubiquitin ligase activity"]; nucleolar retention is RNase
  sensitive ("the nucleolar localization of CSIG depends on rRNA"); relocates to
  nucleoplasm on nucleolar stress.
- Li et al. 2021 [PMID:34362424 "RSL1D1 directly interacted with and recruited p53 to HDM2
  to form a ternary RSL1D1/HDM2/p53 protein complex and thereby enhanced p53
  ubiquitination and degradation"] -- opposite direction to Xie 2016; also stabilizes
  HDM2 mRNA. Follow-up PMID:35597299 maps binding to the p53 DNA-binding domain.
  The MDM2/p53 direction is contested, so no MF/BP term for it is proposed.
- 3'UTR mRNA stabilization: PPARG [PMID:35940221], FTH1 [PMID:36913375] (both
  abstract-only, two groups). Supports GO:0003730 and a NEW mRNA stabilization.
- Other: c-MYC protein stabilization in HCC [PMID:25749381]; PPM1A myristoylation
  [PMID:30201805]; L1 domain and Lys-rich region required [PMID:26686419]. Kept as
  context, not annotated.
- PMID:16213212 (Takagi 2005, RPL26/nucleolin and p53 UTRs) is abstract-only in the
  cache and the abstract does not mention RSL1D1; the CAFA-assigned UTR-binding IDAs
  cannot be verified from what I can read. The functions themselves are independently
  supported, so I defer to the curator rather than remove.

### Decisions summary

- RNA binding (HDA x2, IBA): ACCEPT; nucleolus (IBA, IDA x2, IEA): ACCEPT.
- mRNA 5'-UTR binding, mRNA 3'-UTR binding: ACCEPT (core).
- regulation of cellular senescence: MODIFY -> negative regulation of cellular senescence.
- regulation of protein localization: MODIFY -> positive regulation of protein
  localization to nucleolus (nucleostemin).
- regulation of apoptotic process: KEEP_AS_NON_CORE (directions conflict between
  UV-apoptosis and CRC knockdown studies) + source defect (reference).
- osteoblast differentiation (HDA, expression profiling): REMOVE.
- membrane, cadherin binding (HDA): MARK_AS_OVER_ANNOTATED.
- protein binding x7: REMOVE per policy.
- NEW: negative regulation of translation (PMID:18678645); mRNA stabilization
  (PMID:35940221, PMID:36913375).
