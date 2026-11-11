# CG6830 (Q9VGJ8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used.

### Identity
- Q9VGJ8 is the sole product of CG6830 (FlyBase: 1 transcript, 1 unique polypeptide;
  891 aa). Not an isoform, fragment or alternative gene model. Two SMART CHK
  kinase-like domains (174-369, 605-797); synonym Dro24-1 (Drosophila genus-level
  clade Dro24 of Scanlan et al.).
- Motif scan (file:DROME/CG6830/CG6830-bioinformatics/RESULTS-rereview.md): both CHK
  domains keep the HxDxxxxN catalytic loop (H297/D299/N304; H725/D727/N732).

### Evolutionary placement
- PANTHER PTHR11012:SF6 (CHK DOMAIN OV1-RELATED), shared only with CG31099 among fly
  genes. Characterised ecdysteroid 22-kinases are in other subfamilies (BmEc22K SF54;
  AgEcK2 ortholog CG5644 SF47). No PAINT/IBA annotations exist for SF6.
- Scanlan & Robin 2024 [PMID:38291829 "the only two genes known to encode ecdysteroid
  kinases belong to different subfamilies"]. The deep-research report (falcon), from
  Fig. 3C of that paper, places Dro24 in EcKL subfamily H, Diptera clade Dip4,
  detoxification score 3; this placement is figure-derived and not verbatim-checkable
  in our text cache. The text states Dip4 (subfamily H) is an expanded clade worth
  testing for detoxification [PMID:38291829 "Dip1, Dip3, and Dip4 EcKLs in other
  dipterans should be investigated for possible detoxification functions"].
- Family review interpro/panther/PTHR11012/PTHR11012-review.yaml: functional_coherence
  UNKNOWN, GO:0106389 scope UNRESOLVED. Agrees with this review; no placement conflict.

### Experimental data
- Only direct data: UAS-ORF misexpression screen [PMID:39208453 "Only misexpression of
  CG6830 and CG5644 caused significant developmental arrest before the adult stage"].
  Gain-of-function toxicity; not evidence of normal process participation. Not
  annotated. CG6830 was listed among prior detoxification candidates [PMID:39208453].
- Wallflower is CG13813, not CG6830; Wall data not used.

### Annotation decision
- GO:0106389 ecdysteroid 22-kinase activity (TAS, PMID:32540344): UNDECIDED. Abstract
  only; no target assay; subfamily differs from both characterised C-22 kinases.
- Core function recorded at the level supported by fold + catalytic motifs: putative
  small-molecule phosphotransferase to an alcohol acceptor (GO:0016773), flagged as an
  inference.

### Relative
- No characterised ortholog or SF6 member exists. Closest SF6 paralog CG31099
  (Q8IMT2) has a COMPLETE review (also uncharacterised). Nearest experimentally
  characterised EcKL by phylogeny is not in SF6; CG5644 (AgEcK2 ortholog, SF47) is
  in a different subfamily, so no function is transferred.
