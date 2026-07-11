# ALG9 (Q9H6U8) review notes

## Summary of verified biology
ALG9 is an ER-lumenal alpha-1,2-mannosyltransferase in the dolichol-linked oligosaccharide (LLO)
assembly pathway for protein N-glycosylation. It catalyses **two** sequential lumenal steps using
**Dol-P-Man** (dolichyl-phosphate-mannose, NOT GDP-Man) as the mannose donor:

- Adds the **7th mannose** onto Man(6)GlcNAc(2)-PP-dolichol → EC 2.4.1.259 → GO:0052926
  (RHEA:29531). Reactome R-HSA-446215.
- Adds the **9th mannose** onto Man(8)GlcNAc(2)-PP-dolichol → EC 2.4.1.261 → GO:0052918
  (RHEA:29539). Reactome R-HSA-446216.

Multi-pass ER membrane protein (7 TM helices per UniProt topology); catalytic mannose transfer
occurs on the lumenal side of the ER membrane. GT22 family (CAZy), Glyco_transf_22 Pfam,
InterPro IPR005599.

## Disease
- ALG9-CDG (CDG-Il / CDG type IL), MIM:608776. Frank et al. 2004 (PMID:15148656, E523K) and
  Weinstein et al. 2005 (PMID:15945070, p.Y286C in the abstract's numbering). LLO profiling
  shows accumulation of GlcNAc2Man6 and GlcNAc2Man8 lipid-linked structures — exactly the two
  substrates whose downstream mannose is missing when ALG9 is defective.
- Gillessen-Kaesbach-Nishimura syndrome (GIKANIS), MIM:263210 — Tham et al. 2016
  (PMID:25966638), severe skeletal dysplasia / polycystic kidney disease.
- DIBD1 / bipolar association (PMID:12030331 translocation) was later refuted (PMID:16859551).

## Annotation review decisions
- GOA carries BOTH EC-specific MF terms (GO:0052926 Man6→7th; GO:0052918 Man8→9th) plus the
  parent GO:0000026 (alpha-1,2-mannosyltransferase activity). The two specific terms are the
  core MFs; GO:0000026 (parent) and GO:0016757 (glycosyltransferase activity, generic) are
  correct-but-general.
- BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) is the most precise
  core BP; GO:0006487 (protein N-linked glycosylation) is the correct broader outcome.
- CC: GO:0005789 (ER membrane) core; GO:0098553 (lumenal side of ER membrane) is a precise
  IC-supported refinement consistent with lumenal catalysis; GO:0016020 (membrane) HDA is
  correct but general (over-annotation).

## Provenance
All supporting_text quotes are verbatim substrings of the cited cached publication
(publications/PMID_15148656.md, PMID_15945070.md), the cached Reactome entries, or
file:human/ALG9/ALG9-uniprot.txt. All publications are abstract-only (full_text_available:
false) — experimental IMP/IGI/IC annotations from those PMIDs are ACCEPTED (curator read the
full text), not removed.
