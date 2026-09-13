---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/NTRK1
affinage_run_date: 2026-06-10T05:19:52
uniprot_accession: P04629
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 34
citation_count: 34
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for NTRK1 (human)

## Current model (mechanistic narrative)

NTRK1/TrkA is a nerve growth factor (NGF)-responsive receptor tyrosine kinase that transduces neurotrophin signals into survival, differentiation, and death decisions in neurons and tumor cells [PMID:11313867, PMID:22442072]. Ligand engagement is governed by its extracellular Ig-like subdomains, where the D5 (IgC2) region contains the NGF-binding hot spot and an overlapping NT-3 docking site, while D4 (IgC1) provides an allosteric NT-3 site that tunes agonism [PMID:17439940]; proNGF and the NGF pro-region also bind and activate TrkA, the latter at a distinct site [PMID:18808449]. Receptor dimerization of the intracellular kinase domain is itself sufficient to drive downstream signaling, as shown by optogenetic homo-interaction that activates PI3K/AKT and Raf/ERK in the absence of NGF [PMID:29975841], and a constitutively dimerizing extracellular linker mutation (P203A) produces ligand-independent phosphorylation and cellular transformation [PMID:11313867]. The kinase operates by an ordered sequential bi-bi mechanism with ATP binding before substrate [PMID:9448714], and autophosphorylation at the Y490 and Y785 docking sites couples the receptor to adaptors and effectors including IRS-1/IRS-2, which recruit p85-PI3K, SHP-2, and Grb2 to activate PI3K and SRE-driven transcription [PMID:11147812, PMID:23266087]. TrkA surface presentation and signaling competence are tightly controlled by N-glycosylation, which both prevents constitutive activation and is required for cell-surface targeting [PMID:10235685], and by trafficking machinery: STX8 directs Golgi-to-plasma-membrane transport [PMID:24872407], GGA3 mediates Arf6-dependent recycling that sustains NGF-induced Akt and survival [PMID:26446845], and retrograde signaling endosomes evolve from multivesicular bodies in a kinase-activity-dependent manner [PMID:29381137]. Receptor abundance and activity are further set by opposing ubiquitination events — TRAF4-mediated K27/K29-linked ubiquitination of the kinase domain enhances activity [PMID:29715200], whereas a KFG juxtamembrane element and Nedd4-2 binding to the C-terminal PPXY motif drive degradative sorting [PMID:24623787, PMID:21332718]. TrkA delivers divergent outputs depending on context: it promotes p53-dependent apoptosis of neuroblastoma cells and engages the CCM2 juxtamembrane adaptor to mediate cell death [PMID:19755102, PMID:15961390], while supporting neuronal survival and basal forebrain cholinergic development through ERK signaling [PMID:22442072]. Its activity is modulated by co-receptor and cross-talk partners including p75NTR, which selectively augments Shc phosphorylation [PMID:9547236, PMID:15056278], APP (reciprocal regulation and Y682 phosphorylation) [PMID:21849536], and oncogenic interactions with CD44 and EphA2 [PMID:25840418, PMID:30771434]. NTRK1 transcription is positively controlled by Brn3a and Klf7 in sensory neurons [PMID:17011544] and epigenetically repressed by EZH2-deposited H3K27me3 at the P1 promoter [PMID:29507419].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity, GO:0140657 ATP-dependent activity, GO:0060089 molecular transducer activity, GO:0048018 receptor ligand activity
- **localization:** GO:0005886 plasma membrane, GO:0005768 endosome, GO:0005794 Golgi apparatus, GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-392499 Metabolism of proteins, R-HSA-5357801 Programmed Cell Death, R-HSA-1266738 Developmental Biology, R-HSA-4839726 Chromatin organization
- **partners:** NGFR, SHC1, IRS1, IRS2, CCM2, APP, CD44, NEDD4L
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | Medium | TrkA-mediated rescue of oligodendrocytes from p75-dependent apoptosis involves both activation of MAPK survival signals and simultaneous suppression of c-jun kinase (JNK) activity initiated by p75, while p75-induced NFκB activity was unaffected, demonstrating competitive signaling between TrkA and p75 receptors. | PMID:9547236 | The Journal of neuroscience |
| 1999 | High | N-glycosylation of TrkA serves two distinct functions: (1) preventing ligand-independent activation — unglycosylated TrkA is constitutively phosphorylated and interacts constitutively with Shc and PLC-γ; (2) localizing TrkA to the cell surface — unglycosylated TrkA is trapped intracellularly and cannot activate the Ras/MAP kinase cascade (MEK and Erk), despite constitutive kinase activity. | PMID:10235685 | Journal of neurobiology |
| 1996 | Medium | TrkA is cleaved at its ectodomain in a membrane-proximal region by a cell-surface proteolytic system regulated by protein kinase C and NGF, generating a cell-associated fragment that is phosphorylated on tyrosine residues; this phosphorylation requires an intact TrkA kinase domain (not detected in kinase-dead TrkA mutants), suggesting elevated kinase activity of the truncated fragment. | PMID:8636219 | The Journal of cell biology |
| 1996 | High | The p75 neurotrophin receptor (gp75) forms a complex with TrkA on the cell surface; the TrkA extracellular domain is sufficient for this association, but interactions involving other receptor domains (transmembrane/intracellular) also contribute. TrkA kinase activity is not required for complex formation. gp75 does not copatch with TrkB, PDGFR-β, or Torso, demonstrating specificity. | PMID:8603925 | The Journal of cell biology |
| 1998 | High | The TrkA kinase domain follows a sequential ordered bi-bi kinetic mechanism, with ATP binding prior to the exogenous substrate PLC-γ/GST, followed by release of phosphorylated product before ADP release; the inhibitor K-252a acts as a competitive inhibitor with respect to ATP. | PMID:9448714 | Archives of biochemistry and biophysics |
| 2001 | High | A point mutation P203A in the extracellular linker region between leucine repeats and the first Ig-like domain of TrkA increases NGF binding affinity by decreasing ligand dissociation rate, causes spontaneous receptor dimerization and constitutive phosphorylation in the absence of ligand, promotes ligand-independent neurite outgrowth, and transforms fibroblasts to form tumors in nude mice. | PMID:11313867 | Oncogene |
| 2001 | High | IRS-1 and IRS-2 are tyrosine-phosphorylated substrates of both TrkA and the oncogenic TRK-T1 fusion; this leads to recruitment of p85PI3K, SHP-2, and Grb2, increased PI3-kinase activity associated with IRS-1, and activation of c-fos SRE. TRK-T1-stimulated DNA synthesis requires IRS-1 (abolished in IRS-1-/- fibroblasts). Yeast two-hybrid experiments showed direct TrkA–IRS interaction. | PMID:11147812 | Journal of cellular physiology |
| 2007 | Medium | The TrkA D5 (IgC2) extracellular subdomain contains both the cognate NGF binding hot spot and a distinct but partially overlapping NT-3 docking/activation hot spot (site 1); additionally, D4 (IgC1) contains an allosteric NT-3 binding site (site 2). NT-3 docking on both sites 1 and 2 affords full TrkA agonism additive with NGF, while docking solely on site 1 is partially agonistic but noncompetitively antagonizes NGF binding. | PMID:17439940 | The Journal of biological chemistry |
| 2008 | High | TrkA receptor endosomal/lysosomal degradation is both ubiquitin- and proteasome-dependent: the polyubiquitin tag (K485 on TrkA) directs receptor sorting; proteasomal deubiquitinating enzymes trim K63-ubiquitin chains from TrkA prior to lysosomal delivery. The K485R ubiquitin-deficient TrkA mutant fails to deubiquitinate and escapes degradation. | PMID:18419753 | Traffic (Copenhagen, Denmark) |
| 2008 | Medium | ProNGF (cleavage-resistant mutant M-proNGF) binds TrkA with lower affinity than NGF, induces TrkA and ERK1/2 phosphorylation, neurite outgrowth in PC12 cells, and survival but less effectively than NGF; additionally, the NGF pro-region alone binds TrkA at a site distinct from NGF binding, causing TrkA and ERK1/2 phosphorylation. | PMID:18808449 | Journal of neurochemistry |
| 2009 | High | CCM2 interacts with the juxtamembrane region of TrkA via its PTB domain and mediates TrkA-induced cell death; both the PTB domain (conferring interaction specificity) and the Karet domain (linking to death pathways) are required. Downregulation of CCM2 in medulloblastoma or neuroblastoma cells attenuates TrkA-dependent death. | PMID:19755102 | Neuron |
| 2011 | High | TrkA phosphorylates APP at Y682; APP interacts with TrkA and this interaction requires Y682. Reciprocally, APP (specifically Y682) regulates activation of the NGF/TrkA signaling pathway in vivo, controls subcellular distribution of TrkA, and modulates neuronal sensitivity to NGF. | PMID:21849536 | The Journal of neuroscience |
| 2012 | High | Conditional forebrain-specific TrkA knockout in mice causes dysfunction of basal forebrain cholinergic neurons (BFCNs): developmental increase of choline acetyltransferase expression becomes dependent on TrkA signaling (via the ERK pathway) before neuronal connections are established; TrkA loss results in anatomical and physiological deficits in BF cholinergic circuitry and selective cognitive impairment. | PMID:22442072 | The Journal of neuroscience |
| 2014 | High | The majority of retrograde TrkA signaling endosomes in sympathetic neurons are multivesicular bodies (MVBs). Retrogradely transported TrkA+ MVBs evade lysosomal fusion upon arriving in cell bodies and instead evolve into TrkA+ single-membrane signaling vesicles; TrkA kinase activity associated with retrogradely transported MVBs determines endosome evolution and fate. | PMID:29381137 | eLife |
| 2014 | High | A 3-amino-acid (KFG) domain in TrkA negatively regulates TrkA level and function by promoting ubiquitination; deletion of this domain in knock-in mice reduces TrkA ubiquitination, increases TrkA protein levels and activity, and results in enhanced thermal sensitivity and inflammatory pain without affecting DRG neuron numbers. | PMID:24623787 | The Journal of neuroscience |
| 2011 | Medium | Nedd4-2 (E3 ubiquitin ligase) binds the C-terminal PPXY motif of TrkA and mediates multimonoubiquitination. Mutations at the hydrophobic residues Leu784 and Val790 increase Nedd4-2 binding and ubiquitination, directing receptors to the lysosomal pathway instead of recycling; multimonoubiquitination does not impair signaling cascade activation but potentiates TrkA-mediated differentiation (neurite outgrowth). | PMID:21332718 | Journal of neurochemistry |
| 2015 | High | GGA3 interacts directly with the TrkA cytoplasmic tail through an internal DXXLL motif and mediates functional recycling of TrkA to the plasma membrane via an Arf6-dependent mechanism; GGA3 depletion delays TrkA recycling, accelerates TrkA degradation, attenuates sustained NGF-induced Akt activation, and reduces cell survival. | PMID:26446845 | Molecular biology of the cell |
| 2014 | High | Syntaxin 8 (STX8, a Q-SNARE protein) binds TrkA and facilitates its transport from the Golgi to the plasma membrane, regulating TrkA cell surface levels specifically (not TrkB); STX8 modulates downstream NGF-induced TrkA signaling and NGF-dependent DRG neuron survival; STX8 knockdown in rat DRG via AAV6 RNAi produced analgesic effects on formalin-induced inflammatory pain. | PMID:24872407 | The Journal of biological chemistry |
| 2018 | High | TRAF4 E3 ubiquitin ligase promotes K27- and K29-linked ubiquitination at the TrkA kinase domain, increasing TrkA kinase activity; mutation of TRAF4-targeted ubiquitination sites abolishes TrkA tyrosine autophosphorylation and its interaction with downstream proteins; TRAF4 knockdown suppresses NGF-stimulated TrkA downstream p38 MAPK activation and invasion-associated gene expression in prostate cancer cells. | PMID:29715200 | The Journal of clinical investigation |
| 2016 | High | X-ray crystal structures of TrkA kinase domain complexed with selective inhibitors reveal a non-active-site binding pocket formed by residues from both the kinase domain and the juxtamembrane (JM) region; three distinct binding modes with the JM region were characterized and found to underlie TrkA selectivity over TrkB and TrkC. | PMID:28039433 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | High | X-ray crystal structure of TrkA kinase domain plus juxtamembrane (JM) region bound to a selective inhibitor A1 reveals that the JM region creates a unique inhibitor-binding pocket conferring potency and selectivity over TrkB and TrkC; in vitro assays validated the importance of the JM region for inhibitor potency. | PMID:28159414 | Bioorganic & medicinal chemistry letters |
| 2012 | Medium | TrkA has two established intracellular docking sites (Y490 and Y785) directly involved in signal propagation; phosphoproteomic dissection using Y490F and Y785F TrkA mutants identified a clear subset of downstream phosphorylation events not dependent on either docking site. | PMID:23266087 | Advances in biological regulation |
| 2004 | Medium | p75NTR enhances TrkA signaling by specifically augmenting phosphorylation of the 46- and 52-kDa isoforms of Shc during NGF-induced TrkA activation; p75NTR physically co-immunoprecipitates with Shc; Akt serine phosphorylation downstream of Shc is also p75NTR-dependent; p75NTR does not enhance tyrosine phosphorylation of other TrkA substrates. | PMID:15056278 | Journal of neurochemistry |
| 2005 | Medium | TrkA induces apoptosis of neuroblastoma cells via a p53-dependent mechanism: TrkA increases p53 target protein expression; kinase-inactive TrkA or p53 inactivation (dominant inhibitory p53, E1B55K, or p53 mutation) prevents TrkA-induced apoptosis; caspase inhibitor or Bcl-XL overexpression also prevents TrkA apoptosis. Conversely, TrkA overexpression in non-transformed sympathetic neurons suppresses p53 and enhances survival. | PMID:15961390 | The Journal of biological chemistry |
| 2019 | Medium | The ganglioside GM1 oligosaccharide directly contacts TrkA at the cell surface to promote neuroblastoma differentiation: photoactivatable cross-linking with GM1 derivatives bearing the photoactivable group on the oligosaccharide (but not the ceramide) generated cross-linked TrkA-GM1 complexes. GM1 resides in detergent-resistant raft fractions while TrkA is in the soluble fraction, suggesting TrkA interacts with GM1 by extending its extracellular domain toward the membrane. | PMID:30776097 | Journal of neurochemistry |
| 2015 | High | NGF stimulation induces CD44 binding to TrkA at the plasma membrane, activating the p115RhoGEF/RhoA/ROCK1 pathway to stimulate breast cancer cell invasion independently of TrkA kinase activity; this TrkA kinase-independent CD44 signaling contributes to resistance to the TrkA kinase inhibitor lestaurtinib. | PMID:25840418 | Oncotarget |
| 2019 | High | ProNGF binding to sortilin induces sequential formation of a sortilin/TrkA/EphA2 complex at the plasma membrane, leading to TrkA phosphorylation-dependent Akt activation and EphA2-dependent Src activation; EphA2 inhibition abolishes proNGF-stimulated clonogenic growth of breast cancer cells. | PMID:30771434 | Cancer letters |
| 2006 | High | Brn3a and Klf7 transcription factors cooperate to control TrkA expression in sensory neurons: in vitro, they synergistically activate the TrkA enhancer; in vivo, TrkA expression is severely reduced in Brn3a-/-;Klf7-/- double-mutant trigeminal ganglia compared to single mutants, and all Trk+ neurons are lost by birth in double mutants. | PMID:17011544 | Developmental biology |
| 2018 | High | EZH2 represses NTRK1 (TrkA) transcription via H3K27me3 histone modifications at the NTRK1 P1 promoter region; EZH2 knockdown or inhibition de-represses NTRK1 expression and induces neuroblastoma cell differentiation (neurite extension); depletion of NTRK1 cancels EZH2 knockdown-induced differentiation, establishing NTRK1 as a downstream effector. | PMID:29507419 | Oncogene |
| 2018 | Medium | Light-inducible activation of TrkA intracellular domain homo-interaction (using cryptochrome 2 optogenetics) in the absence of NGF activates PI3K/AKT and Raf/ERK signaling pathways, promotes neurite growth in PC12 cells, and supports survival of dorsal root ganglion neurons, demonstrating that kinase domain dimerization/interaction is sufficient for TrkA downstream signaling. | PMID:29975841 | ACS synthetic biology |
| 2020 | Medium | Site-dependent phosphorylation of individual intracellular tyrosines in TrkA controls MAPK/ERK signaling: using light-sensitive tyrosine analogues (p-azido-L-phenylalanine and caged-tyrosine via amber codon suppression), specific TrkA tyrosine mutants were identified that can activate the ERK pathway in the absence of NGF upon light illumination, revealing which phosphorylation sites drive defined downstream signaling. | PMID:33239753 | Communications biology |
| 2014 | High | TrkA promotes MDM2-mediated ubiquitination and degradation of AGPS (alkylglyceronephosphate synthase): TrkA phosphorylates AGPS at Y451, promoting AGPS-MDM2 interaction and proteasomal degradation of AGPS, thereby suppressing ferroptosis in prostate cancer cells; TrkA inhibitor larotrectinib increases susceptibility of prostate cancer cells to ferroptosis. | PMID:38200609 | Journal of experimental & clinical cancer research |
| 2006 | Medium | P2Y2 GPCR and TrkA receptor tyrosine kinase interact via Src family kinases (SFK): SFK inhibitors block P2Y2-mediated enhancement of TrkA signaling and neuronal differentiation in PC12 cells and DRG neurons, and abrogate co-immunoprecipitation of TrkA, P2Y2, and SFK, identifying SFK as a convergence point for GPCR-RTK crosstalk. | PMID:16842754 | Biochemical and biophysical research communications |
| 2018 | Medium | NTRK1 inhibition induces phosphorylation of LATS1 and controls YAP subcellular localization, suppressing YAP-driven transcription, cancer cell proliferation and migration; NTRK1 regulates YAP oncogenic activity in vivo in mouse xenograft models, establishing crosstalk between the NGF-NTRK1 and Hippo pathways. | PMID:30542115 | Oncogene |

## Citations

- PMID:10235685
- PMID:11147812
- PMID:11313867
- PMID:15056278
- PMID:15961390
- PMID:16842754
- PMID:17011544
- PMID:17439940
- PMID:18419753
- PMID:18808449
- PMID:19755102
- PMID:21332718
- PMID:21849536
- PMID:22442072
- PMID:23266087
- PMID:24623787
- PMID:24872407
- PMID:25840418
- PMID:26446845
- PMID:28039433
- PMID:28159414
- PMID:29381137
- PMID:29507419
- PMID:29715200
- PMID:29975841
- PMID:30542115
- PMID:30771434
- PMID:30776097
- PMID:33239753
- PMID:38200609
- PMID:8603925
- PMID:8636219
- PMID:9448714
- PMID:9547236
