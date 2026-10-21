# wdr-23 (S6FN32) review notes

## Identity of the benchmark accession

S6FN32 is the TrEMBL entry for WormBase product D2030.9d (498 aa, RefSeq NP_001293282.1). It is
**not** the canonical product: the Swiss-Prot entry for the gene is P90794 (WDR-23A, 571 aa), with
isoform P90794-2 (WDR-23B, 530 aa). S6FN32 is identical to P90794 residues 74-571 and to P90794-2
residues 33-530 (`wdr-23-bioinformatics/RESULTS.md`). Met1 of S6FN32 is the first methionine of
the region shared by both isoforms (P90794 Met74), so S6FN32 is an N-terminally shorter
alternative-start or alternative-model product:

- Missing: the WDR-23A-specific N terminus, which carries the predicted NESs
  [PMID:31409866 "cytoplasmic WDR-23A is predicted to encode two nuclear export signals (NES) in the N-terminal region that are not found in nuclear WDR-23B"],
  the WDR-23B-specific N terminus, which drives nuclear localisation
  [PMID:31409866 "the N-terminal domain of WDR-23B that mediates nuclear localization does not interfere with binding of GEN-1 in vitro."],
  and about 18 shared residues (P90794 56-73).
- Retained: all six UniProt-annotated WD repeats of P90794 (and the seven repeats in the papers),
  and both DDB-1-binding DxR boxes, D340-K-R342 and D387-L-R389 in WDR-23A, which are R269 and R316 in
  S6FN32. These are exactly the arginines whose R342H/R389H mutation abolishes function
  [PMID:23555279 "we mutated the final arginines in the DxR boxes required for DDB binding to make WDR-23(DxR)"].

Best experimental proxy for this product: Hasegawa and Miwa 2010 built a WDR-23A cDNA without
exons 1-3 (the isoform-specific exons). Because P90794 56-73 contains no Met, that construct must
start at Met74, the same start as S6FN32. It fully rescued the xrep-1 phenotype
[PMID:20585349 "Also the xrep-1aProm acDNAEx4-11::gfp fusion gene completely rescued the xrep-1(k1007) phenotype"].
The paper did not report its subcellular localisation separately. (Inference: the residue-74 start is
deduced from the absence of an upstream in-frame Met in the shared exon. The paper itself does not
state the start codon.)

## GOA state

`wdr-23-goa.tsv` has no rows for S6FN32. All GO annotations for the gene are filed on P90794
(QuickGO, 2026-10-20). They include IPI binding rows, IMP GO:0043161 and GO:0000122 from
PMID:19273594, IBA GO:0043161 and GO:0080008 from PANTHER node PTN000457302, IDA nucleus, and
lifespan and stress terms. This review therefore has no inherited rows to judge. It adds three NEW
gene-product-level assertions for the shared core activity (adaptor MF, CRL4 complex, proteasomal
catabolism). It deliberately leaves out nucleus (only WDR-23B is nuclear, through an N terminus
S6FN32 lacks) and the downstream organismal terms (lifespan, synaptic and neuromuscular
phenotypes, which are intestinal and SKN-1-mediated and cell-non-autonomous
[PMID:23555279 "negative regulation of SKN-1 by WDR-23 in the intestine, but not at neuromuscular junctions, is necessary and sufficient for proper neuromuscular function"]).
The evidence codes on the NEW rows point at the gene-level experiments. Only PMID:20585349 used a
construct equivalent to this product.

## Evolutionary grounding

- PANTHER: S6FN32 and P90794 are both PTHR19847:SF7 (DDB1- AND CUL4-ASSOCIATED FACTOR 11), as are
  human DCAF11 Q8TEB1 and mouse Dcaf11 (`interpro/panther/PTHR19847/PTHR19847-entries.csv`).
- PAINT: PTN000457302 (taxon Eukaryota) carries IBD GO:0080008 (seed Q8TEB1) and GO:0043161 (seed
  WBGene00008419) (`interpro/panther/PTHR19847/PTHR19847-paint.tsv`). PAINT did not propagate the
  donors' nucleus or transcription-regulation terms. That omission is respected here.
- Closest characterised relative outside worm: human DCAF11 (Q8TEB1), the reviewed ortholog with a
  complete review (`genes/human/DCAF11/DCAF11-ai-review.yaml`; core MF GO:1990756, complex GO:0080008,
  process GO:0043161). This review matches it.
- Family review `interpro/panther/PTHR19847/PTHR19847-review.yaml`: no disagreement about subfamily
  placement (SF7 for S6FN32, P90794 and Q8TEB1). Its `term_assessments` use the generic GO:0060090. The
  specific GO:1990756 used here is a refinement, not a conflict.

## Biology summary

- WDR-23 interacts with CUL-4/DDB-1 and represses SKN-1 levels, nuclear accumulation and activity
  [PMID:19273594 "SKN-1 protein levels, nuclear accumulation, and activity are repressed by the WD40 repeat protein WDR-23, which interacts with the CUL-4/DDB-1 ubiquitin ligase to presumably target the transcription factor for proteasomal degradation."].
- Identified genetically as xrep-1 / D2030.9
  [PMID:20585349 "D2030.9 encodes WDR-23, a nematode homologue of WDR23"].
- The isoforms differ in compartment and outcome
  [PMID:31409866 "These opposing roles are mediated by two distinct isoforms: WDR-23A in the cytoplasm and WDR-23B in the nucleus."]
  and localise to mitochondrial outer membranes and to nuclei
  [PMID:23555279 "WDR-23 isoforms differentially localize to the outer membranes of mitochondria and to nuclei"].
- GEN-1 is a second substrate (PMID:31409866).

## Module links

- `modules/nrf_oxidative_stress_response.yaml` uses WDR-23/CRL4 as the nematode counterpart of the
  KEAP1 step and already notes the S6FN32 isoform caveat.

## Changes in this re-review (2026-10-20)

- Removed every reference to, and dependence on, computational-prediction source files. The
  bioinformatics script now reads only the UniProt flat file, the P90794 JSON and the isoform-b FASTA.
  The obsolete prediction-derived comparison script and its output were deleted.
- Added the Hasegawa 2010 exon 4-11 rescue as direct proxy evidence for this product, and the DxR
  mapping from Staab 2013.
- Replaced generic GO:0060090 with GO:1990756. Added complex and process, grounded in PAINT
  PTN000457302 and in the human ortholog review.
