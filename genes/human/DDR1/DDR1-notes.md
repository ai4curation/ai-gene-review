# DDR1 (Q08345) review notes

## Research provenance

No deep-research provider keys were available in this environment, so no
`-deep-research-*.md` file was generated. Research used the cached GOA-cited
publications, the UniProt record, the cached Reactome event R-HSA-2327738,
the Leitinger 2014 review (PMID:24725424, full text cached) and a PubMed search
(query: "Vogel WF discoidin domain receptor 1 essential role mammary gland
development", which returned PMID:11283268 and PMID:16167341). Many primary
papers are abstract-only in the cache (9659899, 12065315, 16337946, 18190796,
8302582, 8390675); full text was available for 21044884, 23382219, 33961781,
35384245, 19199708 and 24725424.

## Identity and architecture

DDR1 is a single-pass type I receptor tyrosine kinase with an N-terminal
discoidin (DS) domain, a DS-like domain, a long extracellular juxtamembrane
region, a transmembrane helix and a C-terminal tyrosine kinase domain
[PMID:8390675 "The DDR cDNA predicts a C-terminal tyrosine kinase domain and an N-terminal domain similar to the Dictyostelium discoideum lectin discoidin I"].
Alternative splicing of exons 10-12 yields DDR1a and DDR1b; DDR1b carries the
juxtamembrane ShcA docking site
[PMID:24725424 "A key adaptor molecule that binds to DDR1b, but not to DDR1a, is ShcA (Vogel et al., 1997)"].
UniProt isoform 3 (DDR1d) lacks the kinase domain and is annotated Secreted by
curator inference; it is predicted to be an NMD target.

## Core function: collagen receptor tyrosine kinase

- DDR1 binds and is activated by native triple-helical collagens
  [PMID:9659899 "Here, we show that the mammalian DDR receptors bind and are activated by specific types of collagen"]
  [PMID:9659899 "Stimulation of DDR receptor tyrosine kinase activity requires the native triple-helical structure of collagen"].
- Ligand specificity: fibrillar collagens I-III (GVMGFO motif) shared with DDR2;
  basement-membrane collagen IV only by DDR1
  [PMID:21044884 "Triple-helical peptides containing the GVMGFO motif induced DDR1 transmembrane signalling"]
  [PMID:21044884 "the basement membrane collagen IV being exclusively recognised by DDR1"]
  [PMID:24725424 "DDR1, but not DDR2, binds the basement membrane collagen type IV"].
  Reactome R-HSA-2327738 additionally lists collagen V (and XI in its title).
- Unusual activation: DDRs are pre-formed ligand-independent dimers; activation
  is slow and sustained
  [PMID:24725424 "The DDRs are unusual RTKs in that they form ligand-independent stable dimers that are non-covalently linked"]
  [PMID:21044884 "which results in slow and sustained autophosphorylation of cytoplasmic tyrosine residues"].
- Downstream docking: collagen-dependent phosphotyrosine sites recruit SH2
  proteins (ShcA, Nck2, SHP-2)
  [PMID:9659899 "Collagen activation of DDR1 induces phosphorylation of a docking site for the Shc phosphotyrosine binding domain"]
  [PMID:16337946 "Nck2 and Shp-2, two SH2 domain-containing proteins, bind to DDR1 in a collagen-dependent manner"].
  A PPxY motif binds the WW domains of KIBRA/WWC1
  [PMID:18190796 "KIBRA binds to a WW domain binding motif, PPxY, in the tyrosine kinase receptor DDR1"].

## Cellular outcomes (non-core)

- Smooth-muscle cell adhesion and migration, MMP-2/MMP-9 activity (mouse
  Ddr1-/- aortic SMCs, rescued with DDR1b; kinase-dead restores attachment only)
  [PMID:12065315 "DDR1(-/-) SMCs exhibited impaired attachment to and migration toward a type I collagen substrate"]
  [PMID:12065315 "kinase-dead mutants of DDR1 restored attachment but not migration and MMP production"].
  Attachment is kinase-independent (receptor ectodomain acting in adhesion);
  migration and MMP induction are kinase-dependent signalling outputs.
- Mammary gland development and lactation, blastocyst implantation (mouse
  knockout) [PMID:11283268 "the alveolar epithelium failed to secrete milk proteins into the lumen of the mammary gland"]
  [PMID:24725424 "The most pronounced defect are mammary gland branching abnormalities, with the epithelium failing to secrete milk."].
- PI3K/Akt pro-survival signalling in several cell types
  [PMID:24725424 "DDR1 activation is further linked to the PI-3 kinase/Akt signalling pathway in a variety of human normal and cancer cell lines"].
- Cell-cell junction localisation dependent on E-cadherin
  [PMID:24725424 "Localisation of DDR1 to cell-cell contacts requires E-cadherin function"].
- Ectodomain shedding [PMID:24725424 "Constitutive DDR1 shedding was first noticed by Alves et al."];
  this explains extracellular/colostrum/exosome proteomic detections.

## Annotation decisions (summary)

- Generic kinase MF terms (GO:0004672, GO:0004713, GO:0004714) -> MODIFY to
  GO:0038062 protein tyrosine kinase collagen receptor activity (consistent with
  DDR2 review and modules/collagen_ddr_signaling.yaml).
- GO:0007169 -> MODIFY to GO:0038063.
- Protein binding IPI rows: NCK2/PTPN11 -> SH2 domain binding (DDR1 supplies the
  pTyr docking site); WWC1 -> WW domain binding; DDR2 rows -> receptor tyrosine
  kinase binding (mirrors the DDR2 review's handling of the reciprocal rows).
- Signaling receptor complex IDA (PMID:23382219, MGI): the cached full text never
  names DDR1 (the PX-FERM cargo screen is likely in a figure/supplement), and a
  cargo-motif binding assay would not by itself show membership of a receptor
  complex. The claim itself is sound (DDRs are stable ligand-independent dimers),
  so both the IBA and IDA rows are ACCEPTed, deferring to the curator; the source
  question is raised in suggested_questions.
- GO:0160108 (ARBA) -> MARK_AS_OVER_ANNOTATED: a high-level grouping class from an
  ML rule; DDR1 developmental roles are indirect consequences of collagen signalling.
- No NEW annotations proposed: the core mechanism is already represented.

## Open questions

- Relative contribution of DDR1a vs DDR1b isoforms to collagen-induced
  signalling outputs (ShcA site is DDR1b-specific).
- Molecular determinants of collagen IV recognition by native DDR1 and whether
  collagen IV is a physiological ligand in basement membranes in vivo.
