# Casp9 (rat, Q9JHK1): manual literature synthesis

No deep-research provider was available for this session, so this file summarizes
literature read directly from the cached `publications/` files. Quotes are verbatim
from those files.

## Identity

- UniProt Q9JHK1 (unreviewed TrEMBL; 454 aa), gene Casp9, RGD:61867, GeneID 58918.
- Peptidase C14A family; N-terminal CARD (1-92), caspase p20 (197-329) and p10
  (369-453) domains; catalytic His275 and Cys325 (PIRSR features).
- Ortholog of human CASP9 (P55211) and mouse Casp9 (Q8C3Q9). A local alignment
  (`Casp9-bioinformatics/RESULTS.md`) shows conservation of the catalytic dyad and
  the ABL1 site (human Tyr153 = rat Tyr191), but not the human AKT1 site Ser196
  (rat Trp234).

## Core biochemistry (established mainly in human and mouse)

- Caspase-9 is the apoptosome initiator protease: "Caspase-9 and Apaf-1 bind to each
  other via their respective NH2-terminal CED-3 homologous domains in the presence of
  cytochrome c and dATP, an event that leads to caspase-9 activation. Activated
  caspase-9 in turn cleaves and activates caspase-3." [PMID:9390557]
- It is "the most upstream member of the apoptotic protease cascade that is triggered
  by cytochrome c and dATP" [PMID:9390557].
- The apoptosome "directly cleaves/activates procaspase-7" [PMID:16352606].
- Structural work: "disk assembly and pc-9 binding create an asymmetric proteolysis
  machine" [PMID:21827945].
- DNA damage: "c-Abl phosphorylates caspase-9 on Tyr-153 in vitro and in cells
  treated with DNA damaging agents" and "caspase-9 autoprocessing is regulated by
  c-Abl in the apoptotic response to genotoxic stress" [PMID:15657060].

## Genetics (mouse)

- "Casp9 is a critical upstream activator of the caspase cascade in vivo"; knockouts
  die perinatally with enlarged cerebrum and lack Casp3 activation [PMID:9708735].
- "Casp9-/- embryonic stem cells and embryonic fibroblasts are resistant to several
  apoptotic stimuli, including UV and gamma irradiation" [PMID:9708736].
- "DNA damage-induced neural precursor cell apoptosis, both in vitro and in vivo, was
  critically dependent on p53 and caspase 9" [PMID:11092819].

## Localization

- Human pituitary cells: "caspase-9 is in the cytoplasm of non-apoptotic pituitary
  cells. The activation of apoptosis with rotenone triggers the redistribution of
  caspase-9 to mitochondria." [PMID:12782307]
- Rat hepatocytes: "Procaspase-9 underwent cleavage in mitochondria and translocation
  to the nucleus, where increased caspase-9 activity was detected." [PMID:18316105]
- Rat epidermis (IHC): "Bid, Apaf-1 and cleaved caspase-9 were restricted in the SG"
  (within a description of cytoplasmic staining) [PMID:21630211].

## Rat-specific experimental literature (all from GOA rows; mostly abstract-only)

Nearly all rat papers use caspase-9 cleavage or LEHD-substrate activity as a marker
of intrinsic apoptosis in an injury or drug model:

- Ischemia/reperfusion heart: "cleavage of caspase-9 was observed primarily in
  endothelial cells" and a caspase-9 inhibitor "prevented endothelial apoptosis"
  [PMID:11934844].
- Kainate seizures: "KA triggered neuronal death in the ipsilateral CA3 subfield of
  the hippocampus and activation of caspase-3 and -9" [PMID:16336964].
- t-BHP hepatocytes: "A caspase-9 inhibitor, Z-LEHD-FMK, also reduced t-BHP-induced
  apoptosis, suggesting that caspase-9 plays a critical role in this process"
  [PMID:18316105].
- Gentamicin cochlea: a caspase-3 inhibitor decreased hair cell loss "but caspase-8
  and -9 inhibitors did not" [PMID:17869439] -- this abstract does not support a
  positive role of caspase-9 in this model (see notes).
- Expression/activity readouts in response to hypoxia-ischemia (miR-210)
  [PMID:24089674], CoCl2/estradiol in PC12 [PMID:18598848], LPS intrauterine
  inflammation [PMID:18289516], glioma T11TS therapy [PMID:18931364], PDT in LT12
  leukemia cells [PMID:26861981], sevoflurane [PMID:27498600], renal development
  [PMID:27665619], ethanol/saffron [PMID:30926569], indole-3-carbinol
  [PMID:17297389], and n-butylidenephthalide in RG2 glioma cells, where "Both
  procaspase 9 and procaspase 3 were highly activated in DBTRG-05MG, DBTRG 8401 and
  RG2 cells after BP treatment" [PMID:16987298].

## Synthesis

Rat Casp9 is the CARD-containing initiator caspase of the intrinsic (mitochondrial)
apoptotic pathway. It is recruited to the cytochrome c/Apaf-1 apoptosome in the
cytosol, activated there, and cleaves executioner procaspase-3 and -7. Rat studies
confirm its activation and requirement (by peptide inhibitor) in several models of
intrinsic apoptosis, but provide no rat-specific biochemistry beyond activity assays.
The many "response to X" IEP annotations reflect use of caspase-9 activation as a
cell-death marker rather than participation in those responses.
