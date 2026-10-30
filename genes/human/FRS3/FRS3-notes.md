# FRS3 (O43559) curation notes

## Identity

- FRS3 = FGFR substrate 3 = FRS2beta = SNT-2. 492 aa, N-myristoyl Gly2, IRS-type PTB domain
  (13-115), long disordered C-terminal tail with tyrosines (UniProt O43559). PANTHER
  PTHR21258:SF39 (FIBROBLAST GROWTH FACTOR RECEPTOR SUBSTRATE 3), paralog of FRS2 (SF40).
- Cloned as SNT-2 by Xu et al. 1998 [PMID:9660748 "we show that FRS2/SNT-1 and a newly isolated
  SNT-2 protein directly bind to FGF receptor-1 (FGFR-1)"].

## Does FRS3 itself realize the FGFR docking step? (comparison with FRS2)

Direct, FRS3-specific evidence for each sub-step:

1. **FGFR binding via PTB domain** - yes, direct.
   - [PMID:9660748 "A juxtamembrane segment of FGFR-1 and the phosphotyrosine-binding domain of
     SNTs are both necessary and sufficient for interaction in yeast and in vitro"]
   - [PMID:10629055 "Here we show that the PTB domains of both the alpha and beta isoforms of FRS2
     bind directly to the FGF or NGF receptors"] (FRS2beta = FRS3)
   - [PMID:28483978 "FRS2 (also called FRS2α) and FRS3 (also called FRS2β), which constitutively
     interact with the juxtamembrane region of FGFRs"]
2. **Phosphorylation by the receptor** - yes.
   - [PMID:9660748 "FGFR-mediated SNT tyrosine phosphorylation in vivo requires these segments of
     receptor and SNT"]
   - [PMID:15738000 "When FGF receptor 1 is activated, it phosphorylates FRS2beta, recruits Shp2, and
     releases Rnd1 from FRS2beta"]
3. **GRB2 / SHP2 recruitment** - yes, shown for FRS3 itself (Dixon et al. 2006; Meakin lab).
   - [PMID:16697063 "the signaling molecules Grb2 and Shp2 bind FRS3 at consensus sites that are
     highly conserved among FRS family members and that Shp2, in turn, becomes tyrosine
     phosphorylated"]
   - Caveat: Reactome notes FRS3 carries only three of the four FRS2 GRB2 sites
     [Reactome:R-HSA-5654578 "By sequence comparison, FRS3 has the 2 PPTN11/SHP2-binding sites and
     has three of the four GRB2-binding sites."]. Most Reactome GRB2:SOS1 / SHP2 / RAS events are
     written for "p-FRS" (a set containing FRS2 and FRS3) with summaries that describe FRS2 residues.
4. **Downstream MAPK output** - yes, FRS3 can substitute for FRS2.
   - [PMID:15094036 "We further show that FRS2beta can compensate for the loss of FRS2alpha for
     activation of MAP kinase when expressed in fibroblasts from Frs2alpha(-/-) mouse embryos"]
   - [PMID:16697063 "these data demonstrate that FRS3 supports ligand-induced Map kinase
     activation"]
5. **In vivo** - FRS3 is a minor, partially redundant mediator.
   - [PMID:28483978 "Frs3 germline knock-out mice develop normally into adulthood"]
   - [PMID:28483978 "We found that Frs2 and Frs3 are together required for the differentiation of a
     subset of medial ganglionic eminence (MGE)-derived neurons"]
   - [PMID:29155277 "FRS2 and FRS3, are together required for postnatal brain development"]

Conclusion: FRS3 genuinely performs the same FGFR docking-protein activity (GO:0005068) as FRS2,
biochemically; its in vivo contribution is restricted by neural-enriched expression and FRS2
dominance. The module's paralog-variant modelling is appropriate.

## Other receptors

- Trk receptors: [PMID:16697063 "We demonstrate that FRS3 binds all neurotrophin Trk receptor
  tyrosine kinases and becomes tyrosine phosphorylated in response to NGF, BDNF, NT-3 and FGF
  stimulation in transfected cells and/or primary cortical neurons"]; TRK oncogenes
  [PMID:12586769 "both fibroblast growth factor receptor substrate (FRS)2 and FRS3 are recruited and
  activated by TRK-T1 and TRK-T3"]. NPM-ALK: PTB domain NMR structure with ALK peptide
  [PMID:20454865].
- BMI genetics: [PMID:40133257 "We characterize FRS3 as a BMI-associated gene, encoding an adaptor
  protein known to act downstream of BDNF and TrkB"]. Association only; mechanism unknown.

## FRS3-specific (non-FRS2) activities

- ERK2 binding and negative feedback on EGFR family:
  [PMID:15485655 "forms a complex with ERK2 via the region of 186-252 amino acid residues"];
  [PMID:20228838 "We mapped the residues important for the FRS2beta and ERK interaction to two
  docking (D) domain-like sequences on FRS2beta and two aspartic acid residues in the common docking
  (CD) domain of ERK"]; [PMID:16702953 "SNT-2 constitutively bound to EGFR through the
  phosphotyrosine binding (PTB) domain both with and without EGF stimulation"].
  -> proposed NEW GO:0051019 mitogen-activated protein kinase binding (MF). The negative regulation
  of EGFR signalling process is from one lab; left as a suggested question rather than NEW.
- Microtubule binding in neurons: [PMID:19943849 "we demonstrate that neuronal Frs3 binds
  microtubules comparable to the microtubule-associated protein, MAP2, while Frs2 does not"].
  -> GO:0008017 microtubule binding not proposed: rodent material (human would be ISO at best),
  abstract-only, and directness unverified; kept as a suggested question (PR #3886 review).
- Rnd1/Rnd2 binding to the C-terminal tail [PMID:15738000].
- ULK2 binds the PTB domain [PMID:16887332].

## Localization

- Myristoylated; membrane plus soluble pools [PMID:19943849 "Subcellular fractionation studies
  demonstrate that endogenous Frs3 is both soluble and plasma membrane associated while Frs3
  expressed in 293T cells associates exclusively with lipid rafts"]. Plasma membrane accepted.
- Neural-restricted expression [PMID:19187780 "expression of FRS2beta was restricted to neural
  tissues and it colocalized with Tuj1, a neuronal marker"].

## Annotation decisions (summary)

- IBA/IEA/IPI/IGI for GO:0005068, GO:0005104, GO:0008543: ACCEPT.
- Plasma membrane TAS (Reactome, 31 rows) + IEA: ACCEPT.
- GO:0007165 signal transduction TAS: MODIFY -> GO:0008543 (too general).
- GO:0005515 protein binding (101 IPI rows, mostly HuRI/Y2H screens): REMOVE as uninformative
  (interactions not disputed; mostly unrelated partners such as keratins/KRTAPs/HOX from
  high-throughput Y2H).
- GO:0042802 identical protein binding (2 screens): KEEP_AS_NON_CORE (no known function for
  self-association).

## Deep research caveat

The falcon deep-research report leans heavily on an unpublished 2012 thesis (Gamble) for the
microtubule/kinesin/PSD claims; only the peer-reviewed Hryciw et al. 2010 microtubule-binding
result [PMID:19943849] was used here.
