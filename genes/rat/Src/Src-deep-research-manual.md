# Src (rat, UniProtKB:Q9WUD9) - manual literature synthesis

No deep-research provider was available for this session; this synthesis was written by
hand from the cached publications in `publications/` and the UniProt record
(`Src-uniprot.txt`). Quotes are verbatim from those sources.

## Identity and domain architecture

- Rat proto-oncogene tyrosine-protein kinase Src (c-Src, pp60c-src), 536 aa, GeneID 83805,
  RGD:620795. N-myristoylated Gly2; SH3 (84-145), SH2 (151-248) and tyrosine kinase domain
  (270-523), proton acceptor Asp389, activating autophosphorylation at Tyr419 and inhibitory
  CSK site Tyr530 [UniProtKB:Q9WUD9].
- UniProt: "Non-receptor protein tyrosine kinase which is activated following engagement of
  many different classes of cellular receptors including immune response receptors,
  integrins and other adhesion receptors, receptor protein tyrosine kinases, G
  protein-coupled receptors as well as cytokine receptors." [UniProtKB:Q9WUD9]
- Three isoforms: c-Src, neuron-specific N1-Src (6-aa SH3 n-src loop insert) and N2-Src
  (17-aa insert). [PMID:26026271 "N2-Src also had a higher basal kinase activity than N1- and
  C-Src in vitro and in cells, which could be explained by weakened intramolecular
  interactions."] N1-Src drives neurite elongation [PMID:28220894 "PDN1 also inhibited
  L1-CAM-dependent neurite elongation in cerebellar granule neurons"].

## Catalytic activity (rat-specific evidence)

- GPCR to MAP kinase via Pyk2 in PC12 cells: [PMID:8849729 "tyrosine phosphorylation of Pyk2
  leads to binding of the SH2 domain of Src to tyrosine 402 of Pyk2 and activation of Src."]
- Gastrin/progastrin-induced c-Src kinase activity in intestinal epithelial cells (PMID:12488346).
- ATP-induced Src autophosphorylation in brain mitochondria [PMID:18583343 "ATP addition
  induced Src autophosphorylation at Tyr-416 in its catalytic site, leading to its
  activation"].

## Neuronal / synaptic role (rat)

- Src is an NMDA receptor-associated kinase that up-regulates NMDA channel activity:
  [PMID:9005855 "the endogenous tyrosine kinase Src was shown to regulate the activity of
  NMDA channels"; "Src coprecipitated with NMDA receptor proteins"].
- Anchoring via ND2: [PMID:15069201 "ND2 acts as an adapter protein anchoring Src to the
  N-methyl-d-aspartate (NMDA) receptor complex, and is crucial for Src regulation of
  synaptic NMDA receptor activity."]
- PSD-95 binding: [PMID:14529711 "PSD-95 GST fusion proteins bind directly to purified
  recombinant Lyn, Src, and Yes in vitro."]
- Ischemia: NR2A-PSD-95-Src module, Pyk2-facilitated NR2A phosphorylation
  (PMID:11478920, PMID:12618293, PMID:15814199, PMID:20197063).
- Learning correlates with Src up-regulation in hippocampal synaptic membranes
  (PMID:10884433, expression only).

## Vascular smooth muscle / GPCR signalling (rat)

- [PMID:7586216 "These data are the first to show that pp60c-src is activated by Ang II."]
- [PMID:8626602 "a G protein-coupled receptor such as the AT1 receptor can activate the Ras
  protein cascade via the tyrosine kinase pp60c-src."]
- [PMID:9227431 "the pp60c-src tyrosine kinase is necessary and specific for vascular smooth
  muscle cell proliferation and DNA synthesis in response to G protein-coupled receptors"].

## Growth factor signalling, adhesion, other contexts

- PDGF in mesangial cells: [PMID:16530387 "PDGF-activated c-Src tyrosine kinase relays signals
  to PI 3 kinase/Akt and MAPK"].
- Adhesion: r-PTPeta activates c-Src by dephosphorylating Tyr529 and increases adhesion
  (PMID:15735685).
- Caveolae endocytosis/transcytosis: [PMID:15007081 "Src-mediated phosphorylation of
  dynamin-2 is an essential requirement for scission of caveolae"].
- Osteoclastic bone resorption (pharmacological, PMID:8514886).
- Mitochondria: rat brain mitochondria contain Src (PMID:12007793, PMID:18583343,
  PMID:21063895).
- Testis: Src in Sertoli cells, spermatids, adherens junction complexes (PMID:7530000,
  PMID:10698670, PMID:15389520, PMID:15591141) - largely expression/correlation.
- v-Src in Rat-1 fibroblasts depends on annexin 2 for membrane targeting and transformation:
  [PMID:19193640 "Our findings reveal a dual role for annexin 2, first as a regulator of v-Src
  trafficking and targeting and second as a v-Src effector in the reorganization of actin."]
  This concerns the viral oncoprotein, not rat c-Src, though the authors note c-Src-GFP behaved
  similarly (data not shown).

## Caveats

Most rat papers use pharmacological inhibitors (PP1, PP2, herbimycin A) or antibodies that do
not distinguish Src from other Src-family kinases; many GOA rows are IEP rows reflecting
Src activation or expression after a stimulus rather than a demonstrated role.
