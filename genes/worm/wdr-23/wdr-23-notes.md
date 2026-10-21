# wdr-23 (S6FN32): evidence and exact-input prediction review

The DCAF11/WDR-23 identity and qualified substrate-receptor prediction are supported by direct worm studies and preservation of the common WD-repeat region. The nucleus prediction requires isoform-specific evidence; the two ribosome-related GO predictions derive from RACK1 rather than WDR-23 evidence.

## Input identity and functional boundary

S6FN32/D2030.9d is exactly residues 74–571 of the longer P90794 WDR-23A sequence and residues 33–530 of P90794-2/WDR-23B. It therefore is not identical to either tested isoform. Every annotated WD repeat is retained. The missing isoform-specific N termini matter because primary experiments establish different nuclear and cytoplasmic behavior. The GO donor P69103 is trypanosome small ribosomal subunit protein RACK1, a different WD-repeat protein.

## Biological evidence

- [PMID:19273594 — The WD40 repeat protein WDR-23 functions with the CUL4/DDB1 ubiquitin ligase to regulate nuclear abundance and activity of SKN-1 in Caenorhabditis elegans.](https://pubmed.ncbi.nlm.nih.gov/19273594/): The primary worm study establishes association of WDR-23 with CUL-4/DDB-1 and regulation of SKN-1 abundance and activity.

> WDR-23, which interacts with the 
> CUL-4/DDB-1 ubiquitin ligase

- [PMID:31409866 — Nuclear and cytoplasmic WDR-23 isoforms mediate differential effects on GEN-1 and SKN-1 substrates.](https://pubmed.ncbi.nlm.nih.gov/31409866/): Primary worm isoform experiments show that compartment and regulatory outcome cannot be assigned independently of the N terminus.

> These opposing roles are mediated by two distinct isoforms: WDR-23A
> in the cytoplasm and WDR-23B in the nucleus.


> we identify
> GEN-1, a Holliday junction resolvase, as an evolutionarily conserved WDR-23
> substrate


> the N-terminal domain of WDR-23B that mediates nuclear localization does not interfere with binding of GEN-1 in vitro.

## Exact non-GO claims

The complete emitted record is preserved in [wdr-23-protnlm-source.json](wdr-23-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> DDB1- and CUL4-associated factor 11

CNN (CS 2). DDB1- and CUL4-associated factor 11 correctly identifies the WDR-23 lineage, independently supported by direct C. elegans interaction and substrate-regulation experiments. It does not specify the untested isoform localization.

### Function

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex

CNN (CS 2). The qualified “may function as a substrate receptor” wording is consistent with preservation of the complete common WD-repeat region and direct worm evidence for WDR-23–CUL-4/DDB-1 association. The prediction does not establish that the short product has all regulatory effects measured for WDR-23A or WDR-23B. [PMID:19273594](https://pubmed.ncbi.nlm.nih.gov/19273594/); [PMID:31409866](https://pubmed.ncbi.nlm.nih.gov/31409866/).

### Location

> Nucleus

UNC (CS 1). Both nuclear and cytoplasmic WDR-23 isoforms are experimentally documented. S6FN32 starts downstream of the distinctive N termini of both tested products, so it cannot simply inherit the WDR-23B localization. The missing N terminus does not by itself prove exclusion from the nucleus. [Isoform comparison](wdr-23-bioinformatics/isoform-b-comparison.json); [primary localization study](https://pubmed.ncbi.nlm.nih.gov/31409866/).

## Emitted GO claims

All 2 emitted GO claims are individually assessed in [wdr-23-protnlm-predictions-review.yaml](wdr-23-protnlm-predictions-review.yaml).

## Family integration

PTHR19847/SF7 identifies the DCAF11/WDR23 substrate-receptor lineage. A WD-repeat fold alone is insufficient to transfer the ribosome-associated functions of RACK1. Substrate identity and compartmental effects require finer resolution than family membership; nuclear inhibition and cytoplasmic activation of substrates are both compatible with a common adaptor architecture.

## Evidence limits

The 2019 report is available in full text; the 2009 cache is abstract-only. Neither directly assays D2030.9d/S6FN32. The genuine Falcon report provides useful primary leads, but its gene-level nuclear and SKN-1 conclusions require the exact isoform boundary documented here. No NEW experimental annotation is assigned to an untested protein product. No direct assay was found either establishing or refuting ribosome association.

Exact sequence mapping: [wdr-23-bioinformatics/RESULTS.md](wdr-23-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### Identity of the benchmark accession

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

### GOA state

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

### Evolutionary grounding

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

### Biology summary

- WDR-23 interacts with CUL-4/DDB-1 and represses SKN-1 levels, nuclear accumulation and activity
  [PMID:19273594 "SKN-1 protein levels, nuclear accumulation, and activity are repressed by the WD40 repeat protein WDR-23, which interacts with the CUL-4/DDB-1 ubiquitin ligase to presumably target the transcription factor for proteasomal degradation."].
- Identified genetically as xrep-1 / D2030.9
  [PMID:20585349 "D2030.9 encodes WDR-23, a nematode homologue of WDR23"].
- The isoforms differ in compartment and outcome
  [PMID:31409866 "These opposing roles are mediated by two distinct isoforms: WDR-23A in the cytoplasm and WDR-23B in the nucleus."]
  and localise to mitochondrial outer membranes and to nuclei
  [PMID:23555279 "WDR-23 isoforms differentially localize to the outer membranes of mitochondria and to nuclei"].
- GEN-1 is a second substrate (PMID:31409866).

### Module links

- `modules/nrf_oxidative_stress_response.yaml` uses WDR-23/CRL4 as the nematode counterpart of the
  KEAP1 step and already notes the S6FN32 isoform caveat.

### Changes in this re-review (2026-10-20)

- Removed every reference to, and dependence on, computational-prediction source files. The
  bioinformatics script now reads only the UniProt flat file, the P90794 JSON and the isoform-b FASTA.
  The obsolete prediction-derived comparison script and its output were deleted.
- Added the Hasegawa 2010 exon 4-11 rescue as direct proxy evidence for this product, and the DxR
  mapping from Staab 2013.
- Replaced generic GO:0060090 with GO:1990756. Added complex and process, grounded in PAINT
  PTN000457302 and in the human ortholog review.
