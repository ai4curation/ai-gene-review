# Fas (rat, UniProt Q63199) - manual literature synthesis

No deep-research API was available for this review. This file was compiled by hand from
the cached publications in `publications/` (all PMIDs cited in the rat GOA file plus
PMID:16987298), the rat UniProt record (`Fas-uniprot.txt`) and the existing human FAS
review (`genes/human/FAS/FAS-ai-review.yaml`). Quotes are verbatim from the cached text.

## Identity and architecture

- Rat Fas (TNFRSF6, CD95, APO-1) is a 324-aa single-pass type I membrane protein: signal
  peptide 1-21, extracellular 22-171 with three TNFR cysteine-rich repeats, TM 172-188,
  cytoplasmic 189-324 containing a death domain (219-303) [file:rat/Fas/Fas-uniprot.txt,
  "Contains a death domain involved in the binding of FADD, and maybe to other cytosolic
  adapter proteins."].
- UniProt function (by similarity to human P25445): "Receptor for TNFSF6/FASLG. The adapter
  molecule FADD recruits caspase CASP8 to the activated receptor." [file:rat/Fas/Fas-uniprot.txt]
- Fas does not bind TNF; GO:0005031 "tumor necrosis factor receptor activity" is defined as
  combining with tumor necrosis factor. The appropriate MF is GO:0005035 death receptor
  activity (as used in the human FAS review).

## Rat experimental evidence for receptor / DISC function

- Spinal cord injury: "SCI resulted in FasL and Fas translocation into membrane raft
  microdomains where Fas associates with the adaptor proteins Fas-associated death domain
  (FADD), caspase-8, cellular FLIP long form (cFLIPL ), and caspase-3, forming a
  death-inducing signaling complex (DISC)." [PMID:17518537]
- Cortical neurons: "immunoprecipitation verified formation of the Fas/FasL complex after
  phenylalanine treatment" and anti-Fas neutralising antibody blocked apoptosis and
  caspase-8/3 activation [PMID:23940767].
- Rat hepatocytes: intracellular CD95 is targeted to the plasma membrane after CD95L, with
  DISC formation and ROS generation [PMID:18045865].
- Neonatal ventricular myocytes: Fas activation raised diastolic Ca2+ and caused
  arrhythmias without apoptosis under normoxia; hypoxia increased Fas and sensitised to
  rFasL-induced apoptosis [PMID:12031707]. Recombinant FasL activated AP-1 in
  cardiomyocytes, and Fas localised to the sarcolemma [PMID:10715265].
- Fas knockdown (siRNA) in type II alveolar epithelial cells and in nucleus pulposus
  cells reduced apoptosis [PMID:19823951, PMID:19902128].
- Agonist anti-Fas antibody induced endplate chondrocyte apoptosis [PMID:16582846];
  antagonist ZB4 antibody blocked CoCl2-induced caspase-8 activation in PC12 cells
  [PMID:15519734].
- Non-apoptotic outputs: in gastric mucosal cells low-level Fas stimulation leads to
  cFLIP-ERK1/2-NF-kB proliferative signalling [PMID:17991709]; in PC12 cells Fas ligation
  supported neurite regrowth through JNKs (Fas-Fc ligand trap reduced regrowth)
  [PMID:18692025].
- Soluble Fas: ectodomain shedding in hepatocytes after partial hepatectomy [PMID:12522536];
  secretory-granule localisation and soluble Fas secretion in castrated prostate epithelium
  [PMID:11332701]; a rat variant mRNA encodes a 65-aa truncated extracellular fragment
  [PMID:7507668].

## Expression-only papers (IEP)

Many rat GOA rows are IEP annotations from papers reporting Fas mRNA/protein changes
(cycloheximide [PMID:9253159], TRH [PMID:16392621], doxorubicin [PMID:16687611],
fluoride [PMID:20568470], p,p'-DDE [PMID:21384494], maternal food restriction
[PMID:19616844], IL-10 [PMID:17105443, PMID:16609999], ethanol [PMID:27939985], liver
regeneration [PMID:10632538], oestrous cycle [PMID:16461545], early embryos
[PMID:11331665], etc.). These show regulation of Fas expression, not that Fas performs
the process. PMID:16987298 (n-butylidenephthalide in glioblastoma) likewise reports that
the compound "significantly induced Fas expression (from one to 41.3-fold vs. one to
7.7-fold in DBTRG-05MG and RG2 cells, respectively)"; it is an expression observation in a
rat glioma line, not a functional test of Fas.

## Annotation attributed to the wrong gene

PMID:29970988 perturbs only the ligand gene Faslg (siRNA and overexpression) in Schwann
cells; Fas itself is not knocked down or measured as a variable. The two IMP rows on rat
Fas (negative regulation of Schwann cell proliferation / migration) appear to be a
ligand-to-receptor mis-attribution.
