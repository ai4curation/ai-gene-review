# FGF1 (human, P05230) review notes

## 2026-09-30 initial review

Context: reviewed as the representative paracrine ligand of the FGFR signaling module
(`modules/fgfr_signaling.yaml`, modelled with GO:0005104). FGF8 review used as comparator.

### Canonical extracellular ligand function
- Universal FGFR ligand: [PMID:8663044 "These studies demonstrate that FGF 1 is the only FGF that can activate all FGF receptor splice variants."]
- Structural basis: [PMID:10830168 "These structures provide a molecular basis for FGF1 as a universal FGFR ligand"];
  FGFR2 complex [PMID:10618369 "We have crystallized a complex between human FGF1 and a two-domain extracellular fragment of human FGFR2."];
  FGFR3c complex [PMID:14732692 "FGF1, an FGF that binds promiscuously to each of the seven principal FGFRs"].
- Heparin binding: heparin-binding channel [PMID:20145243 "part of the long cationic channel that constitutes the FGF-1 heparin binding site"];
  4xE charge reversal abolishes heparin binding [PMID:18441324 "the 4xE mutant did not show affinity to heparin"].
- Mitogen / angiogenic factor [PMID:1693186 "is a mitogen for a variety of mesoderm- and neutroectoderm-derived cells in vitro as well as an angiogenic factor in vivo."];
  angiogenesis blocked by R50E [PMID:23469107 "excess R50E suppressed FGF1-induced migration and tube formation of endothelial cells"].
- Integrin alphaVbeta3 binding (Takada lab) [PMID:18441324 "We discovered that FGF1 directly bound to soluble and cell-surface integrin alphavbeta3"]; treated as non-core (single-lab co-receptor model).

### Non-classical secretion
- Cu2+/S100A13/Syt1 aggregate [PMID:11432880 "FGF1, p40 Syt1, and S100A13 are able to bind Cu2+ with similar affinity and to interact in the presence of Cu2+ to form a multiprotein aggregate"].
- Stress release [PMID:12746488 "enables the release of FGF1 in response to stress"]; serum deprivation release in melanoma [PMID:18400376].
- AHNAK2 [PMID:25560297 "Upon stress, FGF1 is transported to the plasma membrane where it localizes prior to transmembrane translocation."].

### Intracellular / nuclear
- Endosome-to-cytosol translocation and nuclear import [PMID:22321063 "Fibroblast growth factor 1 (FGF1) taken up by cells into endocytic vesicles can be translocated across vesicular membranes into the cytosol and the nucleus"].
- FGFR-independent anti-apoptotic activity, NLS not required [PMID:35159330]; requires p53, direct binding to p53 DBD [PMID:37783936 "We also found that FGF1 directly interacts with p53 in cells and that the binding region is located in the DBD domain of p53."].
- Decision: intracellular CC terms kept as non-core. No NEW apoptosis-regulation term proposed: evidence comes from one laboratory and the mechanism (what FGF1 does to p53) is not defined; raised as a suggested question instead.

### Physiology / metabolism
- Fgf1-null mice essentially normal [PMID:10688672 "Essentially no abnormalities were found in mice lacking only FGF1."].
- High-fat-diet phenotype [PMID:22522926 "mice lacking FGF1 develop an aggressive diabetic phenotype coupled to aberrant adipose expansion when challenged with a high-fat diet."].
- Pharmacological insulin sensitization via FGFR1 [PMID:25043058 "the glucose-lowering activity of FGF1 can be dissociated from its mitogenic activity and is mediated predominantly via FGF receptor 1 signalling"].
- Decision: no NEW metabolic process terms; mouse phenotypes and pharmacology are downstream of FGFR signaling and the endogenous human role is not established.

### Key annotation decisions
- 9 generic protein-binding rows with FGFR partners -> MODIFY to GO:0005104; VBP1 (HuRI) row -> REMOVE.
- Signal transduction (NAS, sequencing paper) -> MODIFY to GO:0008543.
- Anatomical structure morphogenesis (TAS, speculative) -> MARK_AS_OVER_ANNOTATED.
- Positive regulation of transcription by RNA Pol II (apoE/LXR in astrocytes) -> MARK_AS_OVER_ANNOTATED.
- PMID:16756958 (FGF16/18 paper, abstract-only) rows kept as non-core, deferring to curator's full-text reading.
- Ureteric bud rows (in vitro exogenous FGF1, PMID:11731227) non-core; no in vivo requirement.
- 157 Reactome TAS extracellular-region rows accepted.

### Module relevance
- Supports modelling FGF1 as the paracrine FGFR ligand with GO:0005104 in the extracellular region, with heparin binding (GO:0008201) as the HS co-receptor contribution.
- Note: GO:0005615 extracellular space is obsolete in the current GO build; use GO:0005576.
