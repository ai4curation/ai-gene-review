# gpx-3 (C11E4.2, UniProt Q95003) - manual literature review

`just mod-description-deep-research worm gpx-3` found no curated WormBase
description. This review was assembled from the local UniProt record, the local
PANTHER PTHR11592 review, the existing Luersen et al. publication cache and
targeted web/PubMed searches for `gpx-3`, `C11E4.2` and `Q95003`.

## Identity and sequence features

- gpx-3 / C11E4.2 (WormBase WBGene00007517; GeneID 182513), chromosome X, reviewed
  UniProtKB/Swiss-Prot entry Q95003, 224 aa, sequence version 1
  [file:worm/gpx-3/gpx-3-uniprot.txt].
- Member of the GPx family: InterPro IPR000889, Pfam PF00255 GSHPx,
  PIRSF000303, PROSITE PS00460/PS00763/PS51355 and PANTHER PTHR11592:SF88
  "GLUTATHIONE PEROXIDASE-RELATED" [file:worm/gpx-3/gpx-3-uniprot.txt].
- SF88 also contains the characterized Brugia malayi cuticular GPX GP29
  (P67877), Wuchereria bancrofti cuticular GPX (P35666), Dirofilaria immitis
  GPX (P52033)
  [file:interpro/panther/PTHR11592/PTHR11592-entries.csv].
- The C. elegans paralog GPX-5 (Q93204) is also in SF88 and has a complete
  review that made the same family-level peroxidase and reductant-specific
  glutathione-peroxidase calls [file:worm/gpx-5/gpx-5-uniprot.txt,
  file:worm/gpx-5/gpx-5-ai-review.yaml].
- UniProt predicts an N-terminal signal peptide at residues 1-18 and annotates
  the mature chain as residues 19-224 [file:worm/gpx-3/gpx-3-uniprot.txt]. The
  record has no transmembrane feature and the protein does not end in a canonical
  KDEL/HDEL ER-retention motif.
- The peroxidatic position is Cys73 in the motif NVATFCAYT, aligned to
  selenocysteine 49 of human GPX1. The residue is conserved as Cys in the SF88
  nematode proteins. This establishes a Cys-type GPx fold but not glutathione as
  the reductant.

## Experimental literature

- Luersen et al. 2013 included C11E4.2/gpx-3 in a small RNAi screen of predicted
  C. elegans glutathione-metabolism genes. The gpx-3 row reported 90.0 +/- 11.5
  percent survival under 0.15 mM juglone and 83.3 +/- 4.7 percent survival under
  3 mM arsenite, with no significance mark. The same screen did detect
  arsenite sensitivity for C11E4.1/gpx-5, which is the "extracellular GPX"
  discussed in the paper [PMID:23593298 "C11E4.2 gpx-3 X - 4D1290.0±11.583.3±4.7C11E4.1"].
- I found no direct GPX-3 biochemical assay, localization study or loss-of-function
  phenotype. Recent expression/RNAi hits mentioning gpx-3 do not identify a
  protein-level molecular activity.

## Curation notes

- ACCEPT GO:0004601 peroxidase activity and GO:0098869 cellular oxidant
  detoxification from the GPx-family signatures. The PANTHER review of PTHR11592
  already concluded that GPx-fold proteins share peroxide reduction but are
  heterogeneous in electron-donor systems.
- Leave GO:0004602 glutathione peroxidase activity UNDECIDED. The Sec-GPx PAINT
  donors show that this is a GPx-family enzyme but do not prove the reductant for
  the Cys-type nematode SF88 proteins.
- ACCEPT extracellular region. This is supported by the SignalP peptide and the
  secreted/cuticular SF88 family context, including the Brugia malayi GP29
  subcellular-location record, but the exact extracellular compartment for
  C. elegans GPX-3 remains unknown.
