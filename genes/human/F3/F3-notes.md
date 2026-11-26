# F3 (tissue factor, coagulation factor III, CD142) — review notes

## 2026-11-23 session

### Deep research status
- `just deep-research human F3 --provider perplexity` failed twice: first because
  `UV_OFFLINE=1` blocked the uvx tool download, then (online) because the perplexity
  provider is not configured in this environment ("Provider 'perplexity' not available.
  Available: asta, openscientist, claude_code"). No provider file was produced. The
  notes below are my own reading of the cached publications, the UniProt record and the
  cached Reactome events.
- Almost every cited PMID is cached abstract-only (`full_text_available: false`); only
  PMID:19065458 and PMID:19581412 have full text. Curator calls on rows whose full text
  I cannot see are not overruled.

### Identity and architecture
- Single-pass type I membrane glycoprotein: signal 1-32, extracellular 33-251,
  TM 252-274, short cytoplasmic tail 275-295 (UniProt P13726). The cDNA paper notes no
  homology to the serine proteases or coagulation cofactors
  [PMID:3037536 "The amino acid sequence of tissue factor shows no significant homology
  with the vitamin K-dependent serine proteases, coagulation cofactors, or any other
  protein"]. It is a class II cytokine-receptor-fold protein (PANTHER PTHR20859
  "Type II Cytokine and Tissue Factor Receptors"), but its ligand is the protease FVII/FVIIa.
- It is not a protease. It is the membrane cofactor and allosteric activator of FVIIa
  [Reactome:R-HSA-140748 "FVIIa is allosterically activated by TF, which increases the
  amidolytic activity of FVIIa by restructuring the active site region"]
  [PMID:12652293 "Tissue factor (TF) is an essential enzyme activator that forms a catalytic
  complex with FVII(a) and initiates coagulation by activating FIX and FX"].
- Binding to FVII/FVIIa is Ca2+-dependent and species-specific [PMID:3455766 "These
  interactions required calcium ions"]; crystal structure of FVIIa:sTF
  [PMID:8598903 "Blood coagulation is initiated when tissue factor binds to coagulation
  factor VIIa to give an enzymatically active complex which then activates factors IX and
  X"].
- Reconstitution: [PMID:3455766 "A system consisting of tissue factor, factor VIIa, calcium
  ions, and coagulation factor X generated activated factor X at an appreciable rate."]
- FIX activation by FVIIa-TF needs an intact FIX Gla domain [PMID:8632006 "its
  phospholipid-dependent activation by the factor VIIa-tissue factor complex is
  diminished"].
- FXa product inhibition of TF-VIIa on phospholipid surfaces [PMID:17469850]. The
  phospholipid-binding measurements in that abstract are of fX and fXa, not of TF
  ("we found the dissociation constants of fX and fXa for 100 nm diameter phospholipid
  vesicles"), so the GO:0005543 IDA on TF from this paper is not verifiable from the
  abstract -> UNDECIDED.

### Location
- Cell surface / plasma membrane of subendothelial cells, cryptic vs decrypted pools
  [Reactome:R-HSA-140761]. Absent from normal endothelium; in adventitia, media and in
  plaque matrix [PMID:2704749 "Significant TF protein staining was found deposited in the
  extracellular matrix surrounding mRNA-positive cells"].
- Alternatively spliced soluble isoform asHTF (isoform 2) lacks TM and circulates
  [PMID:12652293 "asHTF is soluble, circulates in blood, exhibits pro-coagulant activity
  when exposed to phospholipids"]. Plasma TF measured in pregnancy [PMID:19065458].

### Signalling (non-core)
- TF:FVIIa and TF:FVIIa:FXa signal through PAR2/PAR1; a distinct, cryptic TF pool forms
  TF.PAR2 complexes [PMID:16959886 "This antibody inhibits formation of the TF.PAR2 complex
  and TF.VIIa signaling"]. TF/FVIIa transactivates PDGFRbeta [PMID:17991872], drives mTOR
  activation and migration of breast-cancer cells [PMID:18612547], and F3 knockdown
  reduces IL8/CTGF/PAI-1 expression [PMID:22556343]. Exogenous TF modulates endothelial
  proliferation/apoptosis in a concentration-dependent way [PMID:17898544]. These are
  real but context-specific; kept as non-core.

### Decisions worth flagging
- Cytokine receptor activity (GO:0004896) and cytokine-mediated signaling (GO:0019221)
  IBA from PTN000466212 (family root). TF is inside the clade, but TF has diverged: its
  ligand is a protease, and its signalling is via PAR cleavage by the bound protease, not
  ligand-induced signal transmission through TF. TF is not among the IBD seeds for these
  two terms (it is a seed only for plasma membrane). REMOVE both; a PAINT IKR/loss on the
  TF subfamily would be appropriate.
- `contributes_to` serine-type endopeptidase activity (IDA, miR-19b paper): the
  TF:FVIIa complex is proteolytically active, but the catalytic work is FVIIa's and the
  row's evidence is a TF-knockdown procoagulant readout. Marked over-annotated; the
  cofactor role is captured as NEW GO:0061133 endopeptidase activator activity, matching
  how the F5 review annotated factor Va.
- Bare protein binding: REMOVE, except rows whose abstracts show the FVII-TF binding
  itself (PMID:8598903, 8940045, 9414278) -> MODIFY to protease binding, and PAR2
  (PMID:16959886) -> MODIFY to G protein-coupled receptor binding.
- `membrane` rows -> TOO_GENERAL (plasma membrane asserted elsewhere).
- Blood coagulation IDA from PMID:8632006 (FIX activation by FVIIa-TF) -> MODIFY to
  GO:0007598 blood coagulation, extrinsic pathway, whose definition is literally the
  TF-initiated cascade.

## 2026-11-24 PR review follow-up
- GO:0002541 (IDA, PMID:17469850) changed from MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE. In
  GO 2026-07-26, GO:0002543 is_a GO:0030194 and part_of GO:0002526; GO:0002541 is_a GO:0016485 and
  part_of GO:0002526. The two are siblings under acute inflammatory response, not parent and child,
  so TOO_GENERAL does not apply; the inflammatory framing applies equally to the accepted GO:0002543.
