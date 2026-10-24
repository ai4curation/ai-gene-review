# Nepl19 / Q9VAS1

Q9VAS1 is the exact 671-residue Nepl19 product. [PMID:34189422](https://pubmed.ncbi.nlm.nih.gov/34189422/) is cached with full text and classifies the expanded fly M13 family into catalytic Nep and motif-deficient Nepl proteins. [Reproducible exact-sequence alignment](Nepl19-bioinformatics/RESULTS.md) compares human neprilysin P08473 and mouse positive control Q61391 using both L-INS-i and G-INS-i. The result is specific: H584/E585 become Q511/Q512; H588, E647 and D651 map to retained H515, E560 and D564. Thus the HExxH motif is disrupted without relying solely on the Nepl name.

The N-terminal signal peptide and lack of a mature membrane anchor support secretion. Existing plasma-membrane assignments are modified to extracellular region; both NOT peptidase assertions are accepted. Proteolysis participation remains unresolved because loss of intrinsic catalysis does not prove lack of regulatory involvement. No specific core molecular function is claimed.

## Sequence and research provenance

The selected frozen UniProt record is retained in [Nepl19-uniprot-source.json](Nepl19-uniprot-source.json), with the complete original prediction metadata in [Nepl19-predictions-source.json](Nepl19-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Completed provider readback

The completed Falcon report was read in full. Its classification of Nepl19 as a predicted secreted inactive M13 homolog agrees with the independently inspected primary family study (PMID:34189422) and exact-sequence alignment. The report identifies spermathecal transcript detection as a possible experimental context; this is not evidence of a peptide substrate, reproductive function or catalytic activity and does not change the annotations. Its generic peptide-sequestration model remains an untested hypothesis. The decisive catalytic evidence remains the independently reproducible H584/E585-to-Q511/Q512 substitutions, not the provider verdict.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Benchmark accession Q9VAS1 is the canonical 671-aa FlyBase product of Nepl19 (CG14523,
FBgn0039612). It is not a fragment or alternative gene model. UniProt has other entries for the same
gene: A8WHM2 and C1C550 are 671/675-aa cDNA entries, and Q8T0H9 is a 408-aa cDNA fragment. Those are
redundant TrEMBL entries. The benchmark target is the full-length product. It has the signal peptide
(1-24), both M13 domains (N-terminal domain 76-425, C-terminal domain 472-665) and the ENIAD motif
(560-564). HExxH is QQLAH (511-515).

**Phylogenetic placement.** PANTHER puts Nepl19 in PTHR11733:SF238 (FI07649P-RELATED). This subfamily
is insect-specific. Its fly members are Nepl15, Nepl17, Nepl18, Nepl19, Nepl20, Nepl21, Nep6 and Nep4,
so there is no vertebrate ortholog. In a new MAFFT L-INS-i plus NJ identity tree
([RESULTS-rereview.md](Nepl19-bioinformatics/RESULTS-rereview.md), script
`subfamily_tree_rereview.py`; no bootstrap support), Nepl19 groups with its 98F1 tandem paralogs. Its
identity to Nepl17, Nepl18, Nepl20 and Nepl21 is 31-33%. Nepl15 is the next branch out at 27.5%
identity. Nep4 falls outside the Nepl clade, beside Nep2. All four 98F1 paralogs keep an intact HExxH
motif. Nepl19 is the only one that has lost it, so the loss is lineage-specific. Nepl15 (CG4721) has
also lost the His and Glu (RQMLH), and on this tree that loss is independent. The interpro/panther
PTHR11733 family review lists Nepl19 as the SF238 representative. I found no disagreement about
subfamily placement. The family review gives the subfamily only a family-level description and does
not record that SF238 also contains the active Nep4 and Nep6.

**Annotation decisions.**
- Plasma membrane (IBA) and plasma membrane (IEA, from the ARBA SubCell line): MODIFY to extracellular
  region. Nepl19 has a signal peptide and no anchor, so the ancestral membrane location at PTN000199753
  was not inherited. I added a structured propagation_review.
- Proteolysis (IEA, InterPro2GO): changed from UNDECIDED to REMOVE. A domain-signature mapping does not
  establish proteolysis for a protein that has lost its catalytic residues. Being involved in a process
  requires doing some of its work, and Nepl19 has no known substrate, partner or regulatory activity.
  Keeping the row would contradict the accepted NOT peptidase activity rows.
- NOT peptidase activity (IKR, GO_REF:0000047 and PMID:34189422): ACCEPT. Both rows now also cite the
  re-review analysis, which shows the loss is specific to Nepl19.
- Core functions: none asserted. No molecular activity has been established. I added a knowledge gap,
  suggested questions and suggested experiments.

**Closest characterised relative.** Nepl15 (CG4721, UniProt Q9VCU1) is a paralog in the same
subfamily and the nearest branch outside the 98F1 cluster. It is a secreted, non-catalytic Nepl
studied in vivo: Banerjee et al. 2021, PMID:33483521, "The Drosophila melanogaster Neprilysin Nepl15
is involved in lipid and carbohydrate storage", and a 2026 deletion study, PMID:42523199. I transferred
no function from it, because it diverged independently. Nep4 is in the same PANTHER subfamily but is
an active peptidase, and the tree places it outside the Nepl clade. The repo has no review for Nepl15
or Nep4.

**Modules / GO-CAMs.** No module or GO-CAM covers Nepl19. modules/kallikrein_kinin_cascade.yaml
mentions neprilysin (MME) only as a vertebrate bradykinin-degrading enzyme, which is not relevant here.
