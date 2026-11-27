---
provider: manual
date: 2026-11-24
---

# Manual deep research for S. pombe oct1

The Falcon deep-research provider and the Perplexity fallback were unavailable in this checkout, so this file records a manual synthesis of the cached literature and database records used for the review.

S. pombe Oct1 should be curated as a matrix mitochondrial intermediate peptidase whose core role is maturation of imported mitochondrial precursor intermediates by removing an N-terminal octapeptide after MPP cleavage.

## Core conserved activity

The S. pombe protein Q10415 is the `PTHR11804:SF79` mitochondrial intermediate peptidase ortholog. Its UniProt record predicts a mitochondrial transit peptide, places it in the M3A_MIP InterPro family, assigns EC 3.4.24.59, and maps the protein to the mitochondrial matrix by similarity.

S. cerevisiae Oct1/Mip1, the PomBase ISO source `SGD:S000001617` and UniProt ISS source `P35999`, is a direct experimental anchor. Isaya et al. cloned yeast `MIP1/OCT1`, showed that the 772-aa yeast protein was homologous to rat MIP and carried the conserved `HEXXH` zinc-binding motif, and showed that `mip1` mitochondria failed to complete the second cleavage of imported CoxIV and Rieske Fe-S precursors while plasmid YMIP restored MIP activity and respiratory growth (`PMID:8035833`). Vogle et al. later showed in vivo and in organello that Oct1 removes destabilizing N-terminal octapeptides from yeast precursor intermediates to stabilize mature mitochondrial proteins (`PMID:21525245`). Gomes et al. showed Oct1-dependent matrix processing of yeast Prx1 and human PRDX3 expressed in yeast (`PMID:28821623`), and Horvath et al. showed Oct1 processing of yeast Psd1 after MPP cleavage (`PMID:22984266`).

Older biochemical work with purified mammalian MIP established the EC-level chemistry and octapeptide specificity: mitochondrial precursors can require two independent matrix peptidases, MPP and MIP, and amino-terminal octapeptides of MPP-generated intermediates direct recognition by MIP (`PMID:1672532`, `PMID:1560019`). These older mammalian/Neurospora studies are useful background but the S. cerevisiae literature above is the better transfer source for fission-yeast Oct1.

## Iron homeostasis

The S. pombe `GO:0006879` row is an ISO transfer from S. cerevisiae `OCT1`. Branda et al. showed that the yeast mitochondrial intermediate peptidase functionally interacts with frataxin/Yfh1 and helps maintain mitochondrial iron levels, likely by maturing ferrochelatase and other iron-utilizing mitochondrial proteins (`PMID:10332043`). That supports transfer as a real mitochondrial consequence of Oct1 loss, but it is less direct than the precursor-processing reaction because Oct1 contributes through maturation of selected iron-using proteins rather than binding or transporting iron itself.

## GO-CAM context

The GO-CAM activity for `PomBase:SPAC1F3.10c` uses `GO:0004222`, `GO:0034982`, and `GO:0005759`, which are consistent with the review. The model attaches many substrate input edges without edge evidence and has duplicated causal edges toward the Cym1 presequence-peptidase activity; those are model-level curation notes to record in the final GO-CAM consistency PR, not changes for the Oct1 gene PR.
