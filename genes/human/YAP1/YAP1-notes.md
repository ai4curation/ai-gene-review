# YAP1 (human, P46937) - curation notes

**Automated deep research was unavailable** (no deep-research provider keys in this
environment). These notes were written by hand from the cached publications in
`publications/` (several are abstract-only; see `full_text_available:`) and from the
sister reviews of Capsaspora coYki (`genes/CAPO3/coYki/`) and S. rosetta yorkie
(`genes/SALRS/yorkie/`). No `-deep-research-*.md` file exists for this gene.

## Core molecular function

- YAP1 has no DNA-binding domain. It is a coactivator that pairs with TEADs
  [PMID:20368466 "interact with YAP (which lacks a DNA-binding domain but contains an activation domain) to form functional heterodimeric transcription factors"].
- TEADs are required for YAP-dependent transcription and growth
  [PMID:18579750 "Here we demonstrate that the TEAD family transcription factors are essential in mediating YAP-dependent gene expression"];
  [PMID:18579750 "TEAD is also required for YAP-induced cell growth, oncogenic transformation, and epithelial-mesenchymal transition"].
- Structure of YAP(50-171) bound to TEAD1
  [PMID:20123905 "The TEAD family of transcription factors binds directly to and mediates YAP-induced gene expression"].
- WW domain-PPxY interactions: p73 [PMID:11278685 "The WW domain of YAP and the PPPPY motif of p73 are directly involved in the association"];
  PTPN14 [PMID:22525271 "through the WW domain of YAP and the PPxY domain of PTPN14"];
  angiomotins [PMID:21187284 "We demonstrate that AMOTL1 and AMOTL2 can regulate YAP1 cytoplasm-to-nucleus translocation through direct protein-protein interaction"].
- p73 coactivation after DNA damage
  [PMID:18280240 "Tyrosine-phosphorylated Yap1 is a more stable protein that displays higher affinity to p73 and selectively coactivates p73 proapoptotic target genes"].

## Regulation (Hippo pathway)

- LATS phosphorylation leads to cytoplasmic retention
  [PMID:17974916 "Phosphorylation by the Lats tumor suppressor kinase leads to cytoplasmic translocation and inactivation of the YAP oncoprotein"];
  [PMID:18158288 "LATS1 inactivates YAP oncogenic function by suppressing its transcription regulation of cellular genes via sequestration of YAP in the cytoplasm after phosphorylation of YAP"].
- S127 phosphorylation leads to 14-3-3 binding, and a phosphodegron leads to degradation
  [PMID:20048001 "which results in YAP 14-3-3 binding and cytoplasmic retention"].
- Junction and polarity sequestration: [PMID:21145499 "TAZ/YAP dictate the localization of active SMAD complexes"];
  [PMID:31835537 "Dsg3 formed a complex with phospho-YAP and sequestered it to the plasma membrane"].

## Animal tissue-level roles (downstream, animal-specific)

- Epidermal stem cell proliferation via TEAD
  [PMID:21376238 "Yap1 is a critical modulator of epidermal stem cell proliferation and tissue expansion"].
- gp130/IL-6 family to Src/Yes to YAP in intestinal regeneration
  [PMID:25731159 "Through YAP and Notch, intestinal gp130 signalling stimulates epithelial cell proliferation"].
- Organ size [PMID:21808241 "Extensive research led to the identification of the Hippo tumour-suppressor pathway as a key regulator of organ size in Drosophila and mammals"].
- MSC fate (YAP1/TAZ together) [PMID:29496737 "kindlin-2 regulates MSC differentiation through controlling YAP1/TAZ at both the transcript and protein levels"].
- Ciliogenesis (YAP/TAZ together) [PMID:25849865 "knockdown of YAP/TAZ is sufficient to induce ciliogenesis"].

**Paralog caution:** many studies (PMID:25849865, PMID:29496737, PMID:25796446,
PMID:21145499, PMID:35429439) manipulate YAP and TAZ (WWTR1) together. I accepted
those rows as YAP1 annotations in deference to the curators, but flagged the issue as
a suggested question.

## Premetazoan evidence: what is ancestral vs animal-specific

- **Ancestral (present in Capsaspora):** TEAD binding and TEAD-dependent coactivation
  [PMID:22832104 "co-expression of Co-Sd and Co-Yki stimulated the transcription of the HRE-luciferase reporter in Drosophila S2R+ cells"];
  tandem WW domains and HXRXXS LATS sites [PMID:38729842 "Like Yorkie and YAP, Capsaspora Yorkie (coYki) contains two WW domains (Figure 2)."];
  regulation by cytoplasmic sequestration via the Hippo kinase cascade, and transcriptional
  output that depends on the TEAD interface [PMID:38517944 "This result indicates that these phenotypes are mediated by the transcriptional activity of coYki."].
- **Not ancestral, i.e. an animal recruitment:** control of proliferation and organ size.
  [PMID:35659869 "we demonstrate that coYki regulates cytoskeletal dynamics at the cell cortex but is dispensable for the proliferation of Capsaspora cells"];
  [PMID:38729842 "We describe new evidence indicating that the ancestral function of this pathway was not regulation of proliferation, but of cytoskeletal dynamics, and that this pathway function predated the emergence of animals"].
- **Choanoflagellate caveat:** srYki (S. rosetta) TBD is degenerate
  [PMID:38729842 "with srYki lacking conserved residues within the α2 helix that are critical for YAP-TEAD interaction in mammals"].
  The repo's motif scan (`genes/SALRS/yorkie/yorkie-bioinformatics/RESULTS.md`) found no
  LxxLF or PxSFF TEAD-binding motif in F2UDK1. So YAP-TEAD coupling may have diverged or been
  lost in that lineage. This is inconclusive.

Interpretation for the GO annotations: GO:0003713, GO:0140297, GO:0140552, GO:0070064 and
GO:0035329 describe ancestral activities. The proliferation, organ-growth, regeneration
and differentiation process rows are animal-specific outputs. I kept them as non-core,
except for the IBA-supported positive regulation of epithelial cell proliferation, which I accepted.

## GO-CAM

`gocams/index.tsv` lists YAP1 (P46937 / P46937-2) in 12 models. In most of them
(Hippo signaling core components; WWC2/WWC3 variants; MAP4K4; STRIPAK; contact
inhibition; AARS1/SIRT1 lactylation; GPR87) YAP1 is a `transcription coregulator activity`
node part_of `hippo signaling` in the nucleus. In the KRT14/KRT15 models (69c59f8a...) it is
`transcription coactivator activity` in positive regulation of keratinocyte proliferation.
In the ZDHHC7-SCRIB model (62900b6400001749) it is `transcription coactivator activity` in
polarized epithelial cell differentiation. That model is the source of the IC row for
GO:0030859, which I kept as non-core rather than removing.

## Decision summary

- 164 `protein binding` IPI rows. Rows whose partners are DNA-binding TFs (TEADs, p73/p63,
  RUNX1, SMAD1, NFE2) are MODIFY to GO:0140297. Rows whose partners are 14-3-3 are MODIFY to
  GO:0071889. All others (mixed or regulatory partners, high-throughput screens) are REMOVE as
  uninformative; the interactions themselves are not disputed.
- REMOVE GO:0000976 and GO:0000978 (sequence-specific DNA binding): YAP1 lacks a DBD.
- MARK_AS_OVER_ANNOTATED: chromatin binding (indirect), heart process, protein-containing
  complex assembly (x2), negative regulation of gene expression.
- UNDECIDED (abstract only): GO:0000122 (PMID:25849865) and GO:0035331 (PMID:35429439).
- No NEW annotations proposed.
