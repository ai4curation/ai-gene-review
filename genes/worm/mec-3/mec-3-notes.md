# mec-3 (C. elegans) review notes

## Provenance and method

- Automated deep research was not available for this review: no FutureHouse,
  Perplexity or OpenAI keys exist in this environment, so `just deep-research*`
  was not run. The literature search below was done by hand.
- Queries run (2026-11-16), PubMed E-utilities: `"mec-3"[tiab] AND elegans`
  (53 hits, all titles screened); the egl-44 and egl-46 searches for the companion
  reviews (see `../egl-44/egl-44-notes.md`, `../egl-46/egl-46-notes.md`).
- Full text cached for PMID:26096732, PMID:23889932, PMID:39423233,
  PMID:37729192, PMID:26547238, PMID:20537990 and PMID:29031632. The classic
  papers (PMID:2898300, PMID:2576011, PMID:2646709, PMID:1361171, PMID:7664734,
  PMID:8103239, PMID:9735371, PMID:10899123, PMID:10848606, PMID:10993673,
  PMID:12124626, PMID:14568548, PMID:21368126) are abstract-only;
  PMID:7227647 (Chalfie and Sulston 1981) has no abstract in the cache.
- The UniProt fetch was run with `--uniprot-id P09088` to avoid the UniProt
  gene-symbol search, which was rate-limited (HTTP 429) during the egl-46 fetch.

## Identity

- P09088, 321 aa; two LIM domains (27-86, 87-152) and a homeodomain (217-276).
  One of the three founding LIM homeodomain proteins (Lin-11, Isl-1, Mec-3).
  [PMID:2898300 "The putative coding sequence of mec-3 contains a homeobox"].
- Isoforms: UniProt lists a (displayed) and c (lacking 1-43). MBL-1/Muscleblind
  promotes inclusion of an exon that gives the long, fully active isoform
  [PMID:39423233 "MBL-1 is required to maintain a sufficient level of MEC-3
  activity by promoting the splicing of the mec-3 long isoform over the shorter
  isoform, which has a truncated LIM domain and is less active."]. Whether
  UniProt isoform c corresponds to the papers' short isoforms was not checked.

## Touch receptor neuron (TRN) terminal selector, with UNC-86

- [PMID:2898300 "In mutants lacking mec-3 activity, the touch receptors express
  none of their unique differentiated features and appear to be transformed into
  other types of neurons."]; [PMID:2646709 "A third gene, mec-3, specifies the
  differentiation of the touch cells, probably by acting as a transcription
  factor."].
- Expression and its control: [PMID:2576011 "These cells are the touch receptors,
  which mediate the response to gentle touch, and the FLP and PVD neurons."];
  [PMID:2576011 "unc-86, another homeo-box-containing gene, is necessary for all
  mec-3-lacZ expression"]; [PMID:2576011 "mec-3 activity appears to be required
  for maintained expression of the mec-3-lacZ fusion in all cells in which it is
  expressed."]; [PMID:2576011 "In a mec-17 mutant, mec-3-lacZ expression is not
  maintained in the touch receptors, but is not affected in the FLP and PVD
  neurons."]. Hox guarantors: [PMID:26547238 "CEH-13 and EGL-5 increase the
  probability of mec-3 transcriptional activation by the POU-homeodomain
  transcription factor UNC-86 using the same Hox/Pbx binding site."]. ALR-1
  feedback: [PMID:21368126 "ALR-1 provides a second positive feedback loop that
  increases mec-3 expression, by restricting variability, and thus ensures TRN
  differentiation."].
- Heterodimer with UNC-86 on DNA: [PMID:8103239 "bind cooperatively as a
  heterodimer to the mec-3 promoter."]; [PMID:8103239 "Heterodimer formation
  increases DNA binding stability and, therefore, increases DNA binding
  specificity."]; [PMID:1361171 "Both unc-86 and mec-3 proteins bind
  specifically to the promoter of the mec-3 gene"]; but in embryo extracts
  [PMID:7664734 "the LIM homeodomain protein, MEC-3, failed to bind DNA or
  activate transcription on its own."] and [PMID:7664734 "in the presence of both
  UNC-86 and MEC-3, we observed cooperative binding to the mec-3 promoter and
  synergistic activation of transcription in vitro."]. Targets: [PMID:9735371
  "UNC-86::MEC-3 hetero-oligomer-binding sites are also found in the promoters of
  two presumed targets of mec-3, the mec-4 and mec-7 genes"]; [PMID:12124626
  "more than 50 previously unknown mec-3-dependent genes"]; the TRN motif
  [PMID:12124626 "an over-represented heptanucleotide, AATGCAT, that is needed
  for the expression of touch receptor genes."].
- UNC-86 interface: [PMID:10899123 "Residues P145 and L195, which are altered by
  these mutations, are located in the POU-specific domain and abolish the
  physical interaction of UNC-86 with the LIM homeodomain protein, MEC-3."];
  [PMID:10848606 "as well as mutations that prevent coactivation by MEC-3"].
  Authors draw the analogy to the OCA-B coactivator of Oct-1.
- LDB-1: [PMID:10993673 "C. elegans LDB-1 is able to specifically bind LIM
  domains in yeast two-hybrid assays."]; [PMID:10993673 "ldb-1 is necessary for
  several neuronal functions mediated by LIM-HD proteins, including the
  transcriptional activation of mec-2"].

## Neuron identity choices

- ALM versus BDU: [PMID:26096732 "We show that the MEC-3 LIM homeodomain protein
  can outcompete the execution of a neuropeptidergic differentiation program by
  direct interaction with the UNC-86/Brn3 POU homeodomain protein."].
- FLP: MEC-3/UNC-86 are also in FLP, where EGL-44/EGL-46 block TRN genes
  (PMID:30291162, PMID:22087002).
- PVD and touch neurons, by MEC-3 level: [PMID:23889932 "Low levels of MEC-3
  specify the elaborate branching pattern of PVD nociceptors, whereas high MEC-3
  is correlated with the simple morphology of AVM and PVM touch neurons."];
  [PMID:23889932 "AHR-1 specifies AVM touch neuron fate by elevating MEC-3 while
  simultaneously blocking expression of nociceptive genes such as the MEC-3
  target, the claudin-like membrane protein HPO-30"]; PVD branching is
  cell-autonomous [PMID:20537990 "These results are consistent with a
  cell-autonomous role for mec-3 in promoting PVD dendritic branching."]; PVD
  function [PMID:2576011 "The PVD neurons no longer mediate a response to harsh
  mechanical stimuli in the mutants."]; egl-46 is a MEC-3 target
  [PMID:29031632 "This experiment confirmed that egl-46 mRNA is significantly
  reduced in a mec-3 mutant in comparison to wild type"]; PVD level control
  [PMID:37729192 "MEC-3 is fine-tuned by alternative splicing and the ubiquitin
  system to produce the optimal level of dendrite branches."].

## Annotation decisions (summary)

- Core MF: Pol II DNA-binding transcription factor activity as the UNC-86/MEC-3
  heterodimer; BP: TRN (mechanoreceptor) differentiation and positive regulation
  of Pol II transcription. A NEW `mechanoreceptor differentiation` (GO:0042490)
  row is added (IMP, PMID:2898300); in C. elegans only mec-17 currently carries
  it. The four `neuron differentiation` rows are kept, since MEC-3 also acts in
  FLP and PVD and the IBA is family-level.
- `protein binding` (LDB-1) is modified to `transcription coregulator binding`.
- `transcription coactivator activity` (IDA) is kept as non-core: the authors
  describe MEC-3 as coactivating UNC-86, but MEC-3 is itself a DNA-binding
  partner in the complex.
- PVD rows on `neuron projection organization` are modified to `dendrite
  arborization`.

## WormBase and UniProt text check

- WormBase: all claims check out (LIM homeodomain founder; TRN differentiation;
  expression in mechanosensory neurons; initiation by UNC-86; maintenance by
  MEC-3 and mec-17, the latter only in the TRNs per PMID:2576011). Missing: the
  UNC-86/MEC-3 heterodimer on target promoters (mec-4, mec-7), the ALM/BDU
  competition with PAG-3, the PVD dendrite role and its level-dependent control
  (AHR-1, MBL-1), and the ALR-1 feedback loop.
- UniProt: FUNCTION correct and cited. The TISSUE SPECIFICITY line lists the six
  TRNs and FLP but not PVD, which PMID:2576011 reports and which the FUNCTION text
  itself discusses.
