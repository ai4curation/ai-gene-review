# XIAP manual curation notes

## 2026-09-30

- Completed a manual XIAP review from GOA, UniProt, cached PubMed records,
  PAINT/PANTHER context, and Reactome/GO-CAM caches.
- Kept direct apoptotic caspase inhibition as the apoptosis-facing core
  function. Deveraux et al. established that human XIAP directly inhibits
  caspase-3 and caspase-7 [PMID:9230442, "directly inhibits at least two
  members of the caspase family"], and the BIR2/linker structural papers
  support the specific effector-caspase mechanism for caspase-3 and caspase-7
  [PMID:11257230; PMID:11257231; PMID:11257232]. Shiozaki et al. establish the
  distinct BIR3 mechanism for caspase-9 inhibition by keeping caspase-9
  monomeric [PMID:12620238, "XIAP sequesters caspase-9 in a monomeric state"].
- Treated XIAP as a genuine RING E3 ubiquitin ligase, but kept the substrate
  contexts separate. The NOD arm is especially strong: XIAP ubiquitylates RIPK2
  downstream of NOD2 and recruits LUBAC [PMID:22607974, "XIAP ubiquitylates
  RIPK2 and recruits the linear ubiquitin chain assembly complex"], NOD2
  signaling depends on XIAP-dependent RIP2 ubiquitination sites
  [PMID:29452636], and RIPK2 ATP-pocket inhibitors can work by blocking
  XIAP-mediated RIPK2 ubiquitination rather than by blocking RIPK2 catalytic
  output [PMID:30026309].
- Preserved the nuclear Wnt/TLE branch as non-apoptotic XIAP biology.
  Hanson et al. show that Wnt pathway activation recruits XIAP to TCF/Lef and
  that XIAP monoubiquitylates Groucho/TLE [PMID:22304967, "XIAP is recruited to
  TCF/Lef where it monoubiquitylates Groucho (Gro)/TLE"], but this does not
  make XIAP a Notch regulator just because Gro/TLE proteins can participate in
  other transcriptional repressor complexes.
- Kept copper and interferon rows non-core. XIAP promotes COMMD1 degradation
  and copper retention in cultured cells and Xiap-deficient mouse tissues
  [PMID:14685266]; also ubiquitinates the copper chaperone CCS [PMID:20154138,
  "CCS is a target of the E3 ubiquitin ligase activity of XIAP"]. XAF1 inhibits
  XIAP in the antiviral IRF7 axis and thereby promotes IRF7 degradation through
  CUL3-KLHL22 [PMID:36394357, "XAF1 is associated specifically with IRF7 and
  inhibits the activity of XIAP"].
- Removed most generic `GO:0005515 protein binding` rows. DIABLO/SMAC, HTRA2,
  HTRA3, HTRA4, ARTS/SEPTIN4, SIAH1, TRIM32, USP19, and XAF1 are mostly XIAP
  antagonists or degradation/adaptor factors; their binding rows are true edges
  but not informative XIAP molecular functions. HtrA2, for example, moves to
  the cytosol after UV irradiation and can counteract XIAP protection
  [PMID:11604410], while ARTS bridges Siah-1 to XIAP to destroy XIAP rather
  than acting through XIAP catalysis [PMID:21185211, "ARTS serves as an adaptor
  to bridge Siah-1 to XIAP"].
- Narrowed broad `GO:0004842 ubiquitin-protein transferase activity` and other
  loose ubiquitin-process rows to `GO:0061630 ubiquitin protein ligase activity`
  or to specific RIPK2/NOD, Wnt/TLE, PTEN, CCS, IRF7, or BCL2 substrate
  contexts where the cited paper supported direct XIAP RING action.
