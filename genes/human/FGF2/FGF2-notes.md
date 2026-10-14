# FGF2 (human, P09038) curation notes

## Identity and isoforms

- Basic fibroblast growth factor; heparin-binding growth factor family, beta-trefoil fold.
  [file:human/FGF2/FGF2-uniprot.txt "SIMILARITY: Belongs to the heparin-binding growth factors family."]
- Alternative translation initiation (CUG codons) gives a low-molecular-weight (18 kDa, AUG) form and
  N-terminally extended high-molecular-weight (HMW) forms. UniProt lists four isoforms (P09038-1..-4).
  [file:human/FGF2/FGF2-uniprot.txt "Event=Alternative initiation; Named isoforms=4;"]
- HMW forms are nuclear and form nuclear complexes; FIF/API5 binds HMW FGF2 specifically.
  [PMID:11075807 "three high molecular mass (HMM) nuclear forms of FGF-2 are part of a 320-kDa protein complex while the cytoplasmic AUG-initiated form is included in a 130-kDa complex"]

## Secretion (unconventional)

- No signal peptide; exported by direct translocation across the plasma membrane, dependent on
  PI(4,5)P2 and HSPGs; Tec kinase phosphorylates FGF2 (Y82 of 18 kDa form = Y215 in UniProt numbering).
  [PMID:20230531 "Unconventional secretion of FGF2 occurs by direct translocation across plasma membranes, a process that depends on the phosphoinositide phosphatidylinositol 4,5-biphosphate (PI(4,5)P(2)) at the inner leaflet as well as heparan sulfate proteoglycans at the outer leaflet of plasma membranes"]
- Caspase-1 activity is required for FGF2 secretion in keratinocytes; FGF2 physically associates with
  caspase-1 but is not a substrate. [PMID:18329368 "secretion of the leaderless proteins proIL-1alpha, caspase-1, and fibroblast growth factor (FGF)-2 depends on caspase-1 activity"]
- Consequence for GO: the 18 kDa form is genuinely cytosolic before export, so the IBA "cytoplasm"
  annotation is defensible for FGF2 (unlike signal-peptide FGFs such as FGF8).

## Receptor binding (core MF)

- Ligand for FGFR1-4, with mitogenic assays across receptor splice variants.
  [file:human/FGF2/FGF2-uniprot.txt "FUNCTION: Acts as a ligand for FGFR1, FGFR2, FGFR3 and FGFR4"]
  [PMID:8663044 "we have engineered mitogenically responsive cell lines expressing the major splice variants of all the known FGF receptors"]
- Structures: FGF2-FGFR1 2:2 dimer [PMID:10490103 "Two FGF2:FGFR1 complexes form a 2-fold symmetric dimer."];
  FGF2-FGFR2 [PMID:10830168]; 2:2:2 FGF2-FGFR1-heparin [PMID:11030354 "heparin makes numerous contacts with both FGF and FGFR, thereby augmenting FGF-FGFR binding"];
  Apert FGFR2 and Pfeiffer/Muenke FGFR1/FGFR3 mutants crystallized with FGF2 [PMID:11390973, PMID:14613973].
- Mouse FGFR1 expressed in CHO cells binds bFGF and signals DNA synthesis and proliferation [PMID:2161540].
- Heparin/HS binding: basic canyon on FGF2 [PMID:10490103 "A positively charged canyon formed by a cluster of exposed basic residues likely represents the heparin-binding site."].
  No heparin binding row is currently in GOA for human FGF2, so I proposed it as NEW (MF only; the
  comparator FGF1 is a classical heparin-binding FGF, and heparin-binding is the family's name).
- Integrin alphaVbeta3 binding (Takada lab), proposed as needed for FGF2 signaling
  [PMID:28302677]. Accepted as integrin binding but not made core: single-lab model.

## Extracellular binding partners (from IPI "protein binding" rows)

- FGFR1/FGFR2 (structural and SPR papers; HuRI and RTK interactome screens): converted to FGFR binding.
- FGFBP1 [PMID:16257968], PTX3 [PMID:20363749, PMID:22267482], CXCL13 [PMID:11708770], caspase-1
  [PMID:18329368]: these are regulators/sequestrators of FGF2; from the FGF2 side there is no
  informative MF term, so the generic protein binding rows are removed (the interactions are real).
- Intracellular: RPS19 [PMID:11716516], CEP57/Translokin [PMID:12717444 "Translokin, a cytoplasmic protein of relative molecular mass 55,000 (M(r) 55K), interacts specifically with the 18K form of FGF-2"],
  API5/FIF [PMID:11075807] -- trafficking/nuclear-function partners; generic binding rows removed.

## Nuclear localization

- Exogenous FGF2 is imported into the nucleus after endocytosis and translocation to cytosol, via
  CEP57 and importins [PMID:22321063 "Nuclear import of exogenous FGF2, which depends on CEP57/Translokin, was independent of LRRC59, but was dependent on Kpnα1 and Kpnβ1"].
- Nuclear association required for mitogenic activity of internalized FGF2 [PMID:12717444 "Our data show that the nuclear association of internalized FGF-2 is essential for its mitogenic activity"].

## Physiology (in vivo)

- Fgf2-/- mice are viable and fertile; cortical neuron density reduced and wound healing delayed.
  [PMID:9576942 "FGF2, although not essential for embryonic development, plays a specific role in cortical neurogenesis and skin wound healing in mice"]
- This is the key reason I treated broad embryogenesis terms from rat IEA as over-annotation, and
  the numerous angiogenesis/endothelial terms as non-core outcomes of FGFR signaling (FGF2 is not
  required for developmental angiogenesis in the knockout).

## Downstream signaling in endothelial cells

- PI3K and PLCgamma1 activation, Ca2+ rise, Akt S473, migration and tubulogenesis in HUVEC
  [PMID:20011604 "We show that FGF-2 activates PLC c1 in HUVECs measured by analysis of total inositol phosphates production upon metabolic labelling of cells and intracellular calcium increase."]
- Sustained MAPK activation [PMID:16756958 "FGF2, which is mitogenic on endothelial cells and hepatocytes stimulates a sustained MAPK activation in both cell types"].

## Problem annotations

- GO:0090722 receptor-receptor interaction (IDA, PMID:24157794): FGF2 was the agonist that increased
  FGFR1 homodimerization in FGFR1-5-HT1A heteroreceptor complexes; the MF belongs to the receptors.
  MODIFY -> FGFR binding.
- GO:0030214 hyaluronan catabolic process (IDA, PMID:19577615): abstract says bFGF *inhibited* HA
  degradation by lowering HYAL2 expression, i.e. an indirect negative effect on expression; the
  ligand does not take part in HA catabolism. Marked as over-annotation.
- GO:0061045 negative regulation of wound healing (IDA, PMID:19577615): based on an in vitro scratch
  ("wound healing") assay of fibrosarcoma cell migration; not tissue wound healing, and in vivo
  FGF2 promotes wound healing [PMID:9576942]. MODIFY -> negative regulation of fibroblast migration.
- GO:0043537 negative regulation of blood vessel endothelial cell migration (IDA, PMID:18555217):
  abstract describes TSP-1 inhibiting FGF-2-stimulated migration; full text not available, so
  UNDECIDED rather than REMOVE.
- GO:0062072 histone H3K9me2/3 reader activity and derived GO:0006325 chromatin organization
  (IEA from rat Fgf2 via Ensembl Compara): source experiment not visible; UNDECIDED.
