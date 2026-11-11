# Capsl (mouse, Q6P8Y1) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This was the first review of mouse Capsl. It was done as the experimental reference for transfer
to human CAPSL (Q8WWF8). ProtNLM2 output was not consulted.

### Provenance / process
- `just fetch-gene mouse Capsl` gave 11 GOA rows: 6 MGI IMP from PMID:39264149, 2 IEA and 3 ND.
- Deep research failed. Falcon gave an authentication error ("Exception: Failed to authenticate"),
  and the perplexity-lite fallback returned HTTP 401 (insufficient quota). The review rests on primary
  literature read directly: PMID:39264149 (full text), PMID:31186450 (full text), PMID:18775726, and
  the bovine transition-zone preprint DOI:10.64898/2026.06.11.731632 (abstract only).

### Evolutionary grounding
- UniProt places mouse Capsl in PANTHER PTHR34524:SF5 (calcyphosin-like protein), the same
  subfamily as human CAPSL. Both proteins are 208 aa. Position-by-position (ungapped) identity is
  197/208 = 94.7%, computed from the two UniProt sequences.
- The paralog calcyphosin (CAPS) is in a different subfamily (SF2). Its crystal structure
  (PMID:18775726) is used only for the family-level fact of a calcium-loaded fold of two EF-hand
  pairs.
- No PAINT/IBA node covers this subfamily, so no phylogenetically curated transfer is available.
- EF-hand loops, taken from the UniProt sequence:
  - EF1 (52-63) is DDNNNRTLDFKE and keeps the Glu at position 12.
  - EF2 (88-99) is DRDGSGTIDFNE and is canonical.
  - EF3 (124-135) is DKTGDGVITIED and EF4 (167-178) is DSPYDKDGLVTP. Both lack the
    position-12 Glu, so they are probably not calcium-binding.

### What is experimental in mouse
- iECKO (Capsl flox/flox; Pdgfb-iCreER, tamoxifen P1-P3) at P5 [PMID:39264149 "the radial vascular growth, vessel density, and vascular branching were dramatically reduced in P5 iECKO retina relative to Ctrl mice"]:
  - less radial outgrowth, lower vessel density and branching, fewer tip cells and filopodia;
  - lower EdU+ endothelial proliferation;
  - more vessel regression (empty Collagen IV sleeves);
  - tip-cell nuclei more spherical and not oriented toward the avascular area.
- Later stages and other tissues:
  - delayed hyaloid regression and deep-plexus growth at P10 and P14;
  - the defect is resolved by P21;
  - MYC target genes are reduced in mouse lung (RT-qPCR).
- Normal in iECKO retinas: astrocytes, VEGFA, pericytes, barrier integrity and fibronectin
  [PMID:39264149 "In conclusion, EC-specific knockout of Capsl may mainly lead to defects in retinal vascular ECs rather than other vascular-associated cells."].
- 3T3-L1 (mouse cell line): Capsl KO enhanced adipogenic differentiation [PMID:31186450 "CapslKO cells showed enhanced propensity for differentiation, while CapslOE cells showed no proper lipid accumulation"]. Not annotated.

### What is NOT experimental in mouse
- All mechanistic data come from human HRECs, not mouse:
  - MYC protein reduced, with MYC mRNA unchanged;
  - CDC42, RAC1, RHOA and MYL9 reduced;
  - Golgi polarity, filopodia and lamellipodia, and wound closure impaired;
  - TopFlash reporter unaffected.
- Localization: the cytoplasm/nucleus statement in the eLife paper cites the Human Protein Atlas,
  and its ICC used overexpressed human CAPSL in 293T cells. Transition-zone MIP status comes from
  bovine cilia (preprint). There is no mouse localization experiment.
- Calcium binding is predicted only.

### Decisions
- angiogenesis: MODIFY to sprouting angiogenesis (GO:0002040), because the phenotypes are tip/stalk-cell readouts.
- vasculogenesis: MARK_AS_OVER_ANNOTATED. Deletion was postnatal, and no de novo vessel formation was assayed.
- endothelial cell proliferation and endothelial cell migration: ACCEPT, both with the
  acts_upstream_of_or_within qualifier. These are the core in-species findings.
- retina development: MODIFY to retina vasculature development in camera-type eye (GO:0061298).
- gene expression: MARK_AS_OVER_ANNOTATED. It is a downstream readout.
- calcium ion binding (IEA): ACCEPT, as an inferred function.
- cytoplasm (IEA): KEEP_AS_NON_CORE.
- ND rows:
  - MF and CC ND: ACCEPT, because there is still no mouse experimental MF or CC data.
  - BP ND: REMOVE, because IMP BP data now exist.
- No NEW terms were added. The ciliary transition zone and microtubule binding are left as
  suggested questions and experiments, because the only evidence is an abstract-only bovine
  preprint. They should not be presented as mouse-experimental.
