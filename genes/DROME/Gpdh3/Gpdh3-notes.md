# Gpdh3 (DROME) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Identity
- The benchmark accession E1JIT1 is **Gpdh3-PB** (1291 aa), one of three FlyBase products of
  Gpdh3/CG43343 (FBgn0263048): PA = Q8IN06 (1304 aa), PB = E1JIT1 (1291 aa), PC = Q9VD20 (1303 aa)
  [file:DROME/Gpdh3/Gpdh3-flybase.txt "Gpdh3-PB FBpp0297799 144.8 1291 4.81 E1JIT1 NP_001163685 ACZ94981"].
- None of the three is Swiss-Prot reviewed. PANTHER uses Q8IN06 (PA) as the gene's tree leaf, and the
  gene-level IBA/ISS annotations (cytosol ISS, IBA GO:0047952 and GO:0006072) sit on Q8IN06, not E1JIT1.
- PB is a genuine alternative isoform, not a fragment. Compared with PA it replaces the 14-residue
  segment EFPLFTAIHLICQS (PA 318-331) by a single D, right after the Pfam C-terminal GPDH domain
  (194..312). The rest is identical, including the whole ~950-residue C-terminal extension and every
  GPDH-core residue examined [file:DROME/Gpdh3/Gpdh3-bioinformatics/RESULTS-rereview.md].

### Evolutionary placement
- PANTHER PTHR11728:SF8 ("GLYCEROL-3-PHOSPHATE DEHYDROGENASE [NAD(+)]-RELATED"), the same subfamily
  as fly Gpdh1 (P13706), fly Gpdh2 (Q9W1U3), CG34149, yeast GPD1/GPD2 and others.
- PANTHER tree (v19, filtered to D. melanogaster): leaves Gpdh1 PTN000198085 (branch 0.179), Gpdh2
  PTN000198083 (0.606), Gpdh3 PTN002271176 (0.791), and CG34149 PTN001712215 (2.0) under PTN000198082.
  PAINT placed NOT (IRD) annotations for GO:0005829, GO:0047952 and GO:0006072 on the CG34149 leaf
  only. Gpdh3 keeps the positive IBAs from PTN000919759 (GO:0047952) and PTN000198006
  (GO:0006072, GO:0005829). I read this as a deliberate PAINT decision and did not REMOVE anything on
  the basis of family placement.
- Bao & Friedrich 2020 list Gpdh2 and Gpdh3 as testis-biased, long-branch paralogs of the
  muscle-specific cytosolic Gpdh1 [PMID:33083121 "Glycerol 3 phosphate dehydrogenaseGpdh1cytosolicmuscle specific0Gpdh211Gpdh311"].
  This fits Bgee's top tissue, early-mid elongation-stage spermatids.

### Residue-level divergence (new analysis, compare_isoforms_rereview.py / survey_orthologs_rereview.py)
- GPD1 K204 (UniProt ACT_SITE, proton acceptor) corresponds to **T205** in E1JIT1. The catalytic-loop
  window is GALKN in GPD1 and Gpdh1 but GTLTD in Gpdh3.
- The NAD-binding loop GSGNWG reads **GAEGWG** (middle Gly to Glu). This is conserved in every long
  Drosophilid Gpdh3 ortholog recovered, so it is ancestral to the Gpdh3 lineage.
- The catalytic Lys is retained in obscura-group, willistoni and lebanonensis orthologs, and lost
  (T/S/N) in the melanogaster group. In D. melanogaster it is T in all cDNA- and genome-derived
  entries, so it is not a gene-model error.
- Conclusion: canonical GPDH activity is ancestral to the lineage but doubtful in D. melanogaster.
  All catalytic and process annotations are now UNDECIDED. The direction-specific catabolic process
  and the UniPathway-derived glycerophospholipid term are MARK_AS_OVER_ANNOTATED. No core function
  is asserted.

### Changes vs previous review
- GO:0141152 ACCEPT -> UNDECIDED. GO:0006072 ACCEPT -> UNDECIDED. GO:0016616 MODIFY -> UNDECIDED.
  GO:0005975 MODIFY -> UNDECIDED. GO:0051287 KEEP_AS_NON_CORE -> UNDECIDED.
  GO:0046168 UNDECIDED -> MARK_AS_OVER_ANNOTATED. GO:0006650 UNDECIDED -> MARK_AS_OVER_ANNOTATED.
  GO:0042803 stays UNDECIDED.
- The previous description claimed "supporting retained ... interconversion chemistry" from domain
  presence alone. It has been rewritten.

### Literature
- Europe PMC search for Gpdh3/CG31169/CG43343 found no paper characterizing the protein. The falcon
  deep research agrees and warns that historical "GPDH-3" is an isozyme of the classical Gpdh1 locus
  (Bewley 1989, Wilanowski 1998), so those data were not used.

### Relative and modules
- Relative: E1JIT1 is an isoform (PB). The other products, PA (Q8IN06) and PC (Q9VD20), are TrEMBL
  entries with the same GPDH core and the same divergent residues. Q8IN06 is the PANTHER/GOA gene
  representative, but no product of the gene is a reviewed canonical entry, and this folder already
  covers the gene. The closest experimentally characterized relative is the in-subfamily paralog
  **Gpdh1 (P13706)**, SF8, the PTN000198082 clade; it has no review in the repo. No ortholog of
  Gpdh3 outside Drosophilidae is characterized.
- Modules: modules/glycerol_phosphate_shuttle.yaml and modules/glycerol_metabolism.yaml use PTHR11728
  for the cytosolic NAD-GPDH step. Gpdh3 should not be a representative of that step.
- Family review interpro/panther/PTHR11728/PTHR11728-review.yaml uses E1JIT1 as the SF8
  representative and states that "Every subfamily is an NAD-dependent glycerol-3-phosphate
  dehydrogenase". The subfamily placement is not in dispute: Gpdh3 is SF8 in both UniProt and the
  PANTHER tree. But the family-wide scope for GO:0141152 does not hold for D. melanogaster Gpdh3, and
  E1JIT1 is a poor representative for SF8; Gpdh1 P13706 would be better.
