# wts-1 (O45797, T20F10.1) – manual literature research

No deep-research API was available for this review. This is a manual synthesis built from
the cached publications in `publications/` and PubMed searches ("wts-1 elegans", 12 hits).
Provenance is given inline.

## Identity

- UniProt O45797 (WARTS_CAEEL), 908 aa, ORF T20F10.1, WBGene00007047. It is the single
  C. elegans ortholog of Drosophila Warts and human LATS1/LATS2 (NDR/LATS subfamily of AGC kinases).
- Domains: protein kinase domain 502-807 and AGC-kinase C-terminal domain 808-874, with
  proton-acceptor active site D625 (UniProt FT). Lee et al. 2019 also describe two N-terminal
  PPxY motifs and an N-terminal regulatory (NTR) domain [PMID:31358532 "The N-terminus region of WTS-1, including two putative PPxY motifs and a N-terminal regulatory domain (NTR)"].
- UniProt family note: "Belongs to the protein kinase superfamily. AGC Ser/Thr protein kinase family."

## Earliest phenotype

- In an RNAi survey of C. elegans homologues of yeast MEN/SIN genes, T20F10.1 was listed as a putative
  Dbf2p homologue: [PMID:12213836 "Depletion of the ORF T20F10.1, one of the putative Dbf2p homologues, caused the offspring of injected worms to arrest at an early larval stage (L1)."]
  The authors did not pursue it further, and no embryonic cell-cycle or cytokinesis role was found:
  [PMID:12213836 "However, given the absence of a striking phenotype in the early C. elegans embryo, the study of these kinases was not pursued."]
  This paper is the first loss-of-function report for wts-1 but makes no mechanistic claim about it.

## Localization and intestinal apical membrane integrity (Kang et al. 2009)

- [PMID:19605499 "WTS-1, the C. elegans Lats homolog, localized primarily to the subapical region in the intestine."]
- [PMID:19605499 "A loss-of-function mutation in wts-1 resulted in an early larval arrest and defects in the structure of the intestinal lumen."]
- Not a proliferation or apoptosis phenotype: [PMID:19605499 "The wts-1 phenotype was not caused by cell proliferation or apoptosis defects."]
- [PMID:19605499 "Heat-shock-driven pulse-chase expression experiments showed that WTS-1 regulates the localization of newly synthesized apical actins."]
- The exocyst is genetically downstream: [PMID:19605499 "RNAi of the exocyst complex genes suppressed the mislocalization phenotype of wts-1 mutation."]
- Abstract-only in cache; the GOA rows citing it (defecation, apical protein localization, post-embryonic
  digestive tract morphogenesis, plasma membrane, cytoplasm, apical plasma membrane) were curated from the full text.

## Development (Cai et al. 2009)

- [PMID:19737560 "The null allele of Ce-wts-1 causes L1 lethality."]
- RNAi reveals pleiotropic roles: [PMID:19737560 "Ce-wts-1 is involved in many developmental processes such as larval development, growth rate regulation, gut granule formation, pharynx development, dauer formation, lifespan and body length control."]
- [PMID:19737560 "CE-WTS-1::GFP is enriched near the inner cell membrane, implying its possible membrane-related function."]
- Abstract-only in cache.

## WTS-1 -> YAP-1 (Iwasa et al. 2013; Lee et al. 2019)

- Iwasa et al. identified YAP-1 (F13E6.4): [PMID:23396260 "wts-1 (LATS ortholog) and ftt-2 (14-3-3 ortholog) knockdowns cause nuclear accumulation of YAP-1"].
  UniProt cites this paper for "Phosphorylates yap-1 which may negatively regulate yap-1 nuclear localization" and for the
  WTS-1 N-terminus / YAP-1 WW-domain interaction. Abstract-only in cache; the IPI (transcription coactivator binding),
  IMP (protein serine/threonine kinase activity) and IMP (negative regulation of protein import into nucleus) rows derive from its full text.
- Lee et al. 2019 (full text): suppressor screen of wts-1 lethality recovered yap-1 and egl-44 (TEAD) alleles.
  [PMID:31358532 "WTS-1 bound directly to YAP-1 and inhibited its nuclear accumulation in intestinal cells."]
  [PMID:31358532 "WTS-1 bound GST fused YAP-1, but not GST alone; this result indicates that WTS-1 interacts directly with YAP-1"]
  [PMID:31358532 "Normally, WTS-1 is present only at the subapical region of intestinal cells"]
  NFM-1 (NF2/Merlin) acts in the same pathway and is needed for WTS-1 apical restriction.
  A hydrophobic-motif mutation T863I is lethal: [PMID:31358532 "independent genetic screening for lethal mutations detected a single point mutation (T863I) in the hydrophobic motif of WTS-1, caused early larval lethality"].
- Huynh et al. 2026 (full text): [PMID:41746831 "Upon WTS-1 loss, endogenous YAP-1 translocated from cytosol to nucleus in the epithelium and intestine."]
  [PMID:41746831 "Tissue-specific depletion revealed that intestinal but not epithelial WTS-1 is essential for progression past L2."]
  CST-1/2 (Hippo/MST) act upstream of WTS-1 in the epithelium but not the intestine.

## Other roles

- Touch-neuron maintenance (full text): [PMID:40178516 "Loss of wts-1 leads to premature decline of TRNs both in structure and function, and downstream effectors, yap-1 and egl-44, are required in this phenomenon."]
- Endocytic recycling (abstract only; PMID:34817059): WTS-1 is reported on sorting endosomes in intestinal cells and to restrain endosomal F-actin with PTRN-1 and UNC-60A. Not cached as full text; not used for annotation.
- Commentary (PMID:23843471, not cached) questioned whether a canonical Hippo pathway exists in C. elegans; Huynh 2026 resolves this as Hippo-dependent in epithelia and Hippo-independent in intestine.

## What is not supported

- No evidence that WTS-1 controls cell proliferation, G1/S transition or apoptosis in C. elegans (Kang 2009 negative result;
  UniProt "Does not appear to regulate apoptosis and proliferation"). C. elegans organ sizes are invariant [PMID:41746831 "classical Hippo phenotypes such as tissue overgrowth are absent"].
- Direct in vitro kinase assay on purified WTS-1 is not in the cached full texts; catalytic activity in UniProt is by similarity to LATS1 (O95835).
