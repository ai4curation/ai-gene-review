# VSIG4 (CRIg, Z39Ig) review notes

UniProt: Q9Y279 (VSIG4_HUMAN). X-linked type I transmembrane protein of the Ig superfamily
(one IgV domain in the short isoform; IgV + IgC2 in the long isoform), expressed on resting
tissue macrophages, especially liver Kupffer cells.

## Deep research status

- `just deep-research-falcon human VSIG4` was launched in parallel with publication caching.
  See the end of this file for its final status. Literature below was gathered directly from
  PubMed (PubMed MCP) and cached into `publications/`.

## Function summary with provenance

### Complement C3 fragment receptor on macrophages (phagocytic clearance)
- Identified as a Complement Receptor of the Ig superfamily that binds C3b and iC3b; required on
  Kupffer cells for clearance of C3-opsonized pathogens [PMID:16530040 "Here we report the
  identification and characterization of a Complement Receptor of the Immunoglobulin superfamily,
  CRIg, that binds complement fragments C3b and iC3b."; "CRIg expression on Kupffer cells is
  required for efficient binding and phagocytosis of complement C3-opsonized particles."]
  (mouse knockout data; human CRIg also characterized).
- Peritoneal macrophage subset; CRIg binds opsonized targets without divalent cations, unlike CR3
  [PMID:19017980 "CRIg internalized monovalent ligands and was able to bind complement-opsonized
  targets in the absence of Ca(2+) and Mg(2+)"].
- Downstream signaling in macrophages: CRIg engagement promotes intracellular killing of Listeria
  via CLIC3 bound to the CRIg cytoplasmic tail [PMID:23280470 "CLIC3, an intracellular chloride
  channel protein, was essential for CRIg-mediated LM killing by directly interacting with the
  cytoplasmic domain of CRIg"], and induces autophagosome formation [PMID:27440002 "VSIG4
  signaling triggered by C3-opsonized Listeria (opLM) or by agonistic anti-VSIG4 monoclonal
  antibody (mAb) induced macrophages to form autophagosomes."]. This supports VSIG4 being a
  signaling receptor (GO:0004877 complement component C3b receptor activity), not just a binder.
- Complement-independent pattern recognition of Gram-positive bacteria through lipoteichoic acid
  (mouse in vivo, intravital imaging) [PMID:27345697 "CRIg bound Staphylococcus aureus
  specifically through recognition of lipoteichoic acid (LTA), but not cell-wall-anchored surface
  proteins or peptidoglycan."]. Single study; not proposed as NEW annotation.

### Inhibitor of alternative pathway C3/C5 convertases
- Crystal structure of C3b-CRIg; CRIg mutants show it inhibits AP convertases
  [PMID:17051150 "We show that CRIg is not only a phagocytic receptor, but also a potent inhibitor
  of the alternative pathway convertases."]. Human CRIg; abstract-only in cache.
- Soluble CRIg selectively inhibits the AP in vitro and in vivo; conserved human/mouse
  [PMID:17548523 "This study presents CRIg as the first complement receptor that, in its soluble
  form, selectively inhibits the AP in vitro and in vivo."]. Note: much of this evidence uses
  soluble CRIg-Fc; the physiological contribution of membrane CRIg to AP regulation in vivo is
  less clear.

### Coinhibitory B7-family-related ligand for T cells
- VSIG4-Ig fusion inhibits mouse and human T cell proliferation and IL-2 production
  [PMID:17016562 "In vitro experiments using VSIG4-Ig fusion molecules showed that VSIG4 is a
  strong negative regulator of murine and human T cell proliferation and IL-2 production."].
  Counter-receptor on T cells unknown.
- Expression restricted to resting tissue macrophages, lost on LPS activation [PMID:17016562].

### Negative regulation of macrophage inflammatory activation
- Vsig4-/- mice show excessive macrophage inflammation; VSIG4 activates PI3K/Akt-STAT3 -> PDK2,
  reducing pyruvate oxidation and mtROS [PMID:29109438 "VSIG4 negatively regulates macrophage
  activation by reprogramming mitochondrial pyruvate metabolism."]. Includes human VSIG4+THP-1
  experiments.
- VSIG4 forms a surface signaling complex with MS4A6D (mouse) and represses Nlrp3/Il1b
  transcription via JAK2-STAT3-A20 [PMID:30662948 "VSIG4 interacts with MS4A6D in the formation
  of a surface signaling complex."].

### Interactome (HuRI)
- Y2H interactions with VAMP5, JAGN1, FATE1 [PMID:32296183]; these are high-throughput binary
  interactions among membrane proteins with no functional follow-up; uninformative for function.

## Curation decisions (summary)
- C3b binding (IBA, IPI) and negative regulation of AP complement activation (IBA, IPI): ACCEPT.
- negative regulation of T cell proliferation (IBA, IEA): ACCEPT; IL-2 production: KEEP_AS_NON_CORE.
- negative regulation of macrophage activation (IEA): KEEP_AS_NON_CORE.
- membrane (IEA): ACCEPT (correct, general).
- protein binding x3 (HuRI): REMOVE (uninformative generic term).
- protein-containing complex (IPI, C3 co-crystal): MARK_AS_OVER_ANNOTATED.
- NEW: complement component C3b receptor activity (GO:0004877), complement component iC3b binding
  (GO:0001852), phagocytosis, recognition (GO:0006910), plasma membrane (GO:0005886).
  Comparator check: CR1 (P17927) carries GO:0004877 by IDA, so the receptor term is used for
  C3b-binding phagocytic receptors.
