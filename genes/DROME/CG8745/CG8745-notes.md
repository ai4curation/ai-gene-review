# CG8745 (Q9VU95) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9VU95 is the canonical, Swiss-Prot reviewed product of CG8745 (FBgn0036381). It is 494 aa,
sequence version 2, with a single chain PRO_0000287669. It is not a fragment, isoform or alternative gene
model. The PLP-attachment lysine K291 is present.

Phylogenetic placement (`CG8745-bioinformatics/RESULTS-rereview.md`, `phylo_placement.py`):
- The PANTHER classification is PTHR45688:SF13 ("ALANINE--GLYOXYLATE AMINOTRANSFERASE 2-LIKE"). SF13
  is heterogeneous. It also contains a bacterial dialkylglycine decarboxylase (P16932), an
  aminohexanolactam racemase (Q7M181), S. pombe SPAC1039.07c and Arabidopsis AGT3. None of these group
  with CG8745 in the tree.
- CG8745 is 54% identical to human ETNPPL (SF1) and 50-51% identical to PHYKPL (SF6), against 37-42%
  for the AGXT2 transaminases (SF3). With worm eppl-1, it branches basal to the vertebrate ETNPPL+PHYKPL
  clade, which makes it a co-ortholog of both. The other fly family member, CG11241, is in SF3 (AGXT2-like).
- PAINT placed GO:0050459 at PTN002904331, a Euteleostomi node (taxon:117571). That node excludes CG8745,
  so the curator deliberately did not extend the phosphoethanolamine-specific term to invertebrates.

Literature: PMID:22241472 (full text) shows that ETNPPL degrades phosphoethanolamine, that PHYKPL degrades
phosphohydroxylysine, and that neither is a transaminase. There are no CG8745 biochemical, localisation or
loss-of-function data. The falcon report cites Delclos et al. 2024 (eLife, house fly Obp56h), in which CG8745
transcripts rise after Obp56h RNAi. This is transcriptional only and supports no annotation.

Decisions:
- GO:0030170 PLP binding (IEA): ACCEPT.
- GO:0035094 response to nicotine (IEP, PMID:17237783): changed from UNDECIDED to KEEP_AS_NON_CORE. The
  annotation records a transcript-trait association made by a curator who read the full text, and it says
  nothing about mechanism.
- GO:0050459 ethanolamine-phosphate phospho-lyase activity (ISS from Q8TBG4): changed from UNDECIDED to
  MODIFY, replaced by GO:0016838 carbon-oxygen lyase activity, acting on phosphates. Because CG8745 is a
  co-ortholog of both the phosphoethanolamine and the phosphohydroxylysine lyase, the substrate cannot be
  inferred.
- Core functions: GO:0016838 and GO:0030170. No localisation or process terms were proposed.

Relative to review next: human ETNPPL (Q8TBG4). It is the ISS donor and the closest characterised
co-ortholog, and it has no review in the repo. PHYKPL (Q8IUZ5) already has a complete review.
