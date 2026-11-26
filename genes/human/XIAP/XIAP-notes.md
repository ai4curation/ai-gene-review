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


## 2026-10-26 systematic mammalian apoptosis audit

Reviewed every seeded annotation from the review YAML, preserving every original machine-sourced field and adding no NEW rows. Original terms, evidence, references, relationship fields and supporting entities are unchanged. The gene-level assessment includes functions outside the apoptosis module. Existing source-specific evidence guides and prior history records remain intact.

The review and annotation-reviewer workflow was applied. Default Falcon research and normal publication caching were launched in parallel. Falcon and the perplexity-lite fallback failed for all four targets (provider access errors; command logs under `.cache/module-audit-logs/execution-deep-*`). `fetch-gene-pmids` completed successfully for each. No provider-branded research file was fabricated. This manual notebook and the normal primary publication/UniProt caches supply the research trail.

XIAP has two separable molecular roles: direct caspase inhibition and RING E3 activity. Human caspase-3/7 inhibition (PMID:9230442; PMID:11257230) and BIR3/caspase-9 biochemistry (PMID:12620238) do not support pan-caspase inhibition or extrapolation to every IAP paralog. Mouse neuro2a/mutant-SOD1 experiments show XIAP suppressing caspase-3 activity and death (PMID:12153481); sympathetic neurons retain XIAP-dependent resistance despite endogenous SMAC release (PMID:14623868). Mouse Fas/hepatocyte data (PMID:19626005) support a context-dependent XIAP barrier, not a native-SMAC requirement established merely from a SMAC mimetic.

RIPK2 ubiquitination and LUBAC recruitment (PMID:22607974, PMID:29452636, PMID:30026309) establish major innate NOD/NF-kappaB signaling roles. Positive regulation of linear ubiquitination describes LUBAC recruitment, not XIAP directly making linear chains. The cIAP-heavy PMID:21931591 paper does not contradict independent XIAP evidence; its weaker XIAP results are not grounds to delete the shared process. Wnt/TLE monoubiquitination (PMID:22304967; PMID:36749823), CCS ubiquitination/copper regulation (PMID:20154138), and direct human cell-cycle findings (PMID:23720779, newly normally fetched) are retained on biological merits. In the interferon source (PMID:36394357), CUL3-KLHL22 directly targets IRF7; this is not evidence that XIAP directly ubiquitinates IRF7.

Corrected previous removal/overannotation based only on broadness, nucleolar localization lacking a special function, or biological roles lying outside apoptosis. Identical-protein binding has structural support and is not bare GO:0005515. XIAP survival after DNA damage (PMID:18049476), TNF-associated survival (PMID:11865055), and native intestinal crypt homeostasis (PMID:30389919) remain contextual valid claims. PMID:21849505 full text explicitly says “In addition, XIAP associated with USP19”; Figure 1B resolves the old abstract-only uncertainty, but the generic binding term is removed as uninformative without disputing the interaction.

LPS source PMID:35263589 remains UNDECIDED: the accessible abstract concerns Reg3gamma/EXTL3/BCL10 and does not expose the XIAP experiment; targeted searching did not recover it. Absence from an abstract is not proof of wrong-gene annotation. The GO:0010804 QuickGO definition was verified: any decrease in the rate or extent of TNF signaling qualifies, so inhibiting an apoptotic branch does not require suppressing all TNF downstream outputs.
