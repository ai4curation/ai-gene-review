# Citations for Research Query

**Query:** # PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR11558 — SPERMIDINE/SPERMINE SYNTHASE
- **Subfamily of interest:** PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1
- **Representative member:** NaPMT3 (A0A314LG79), NICAT / NICAT
- **GO term currently propagated at/near this node:** spermidine synthase activity (GO:0004766)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1 sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.

**Provider:** falcon
**Generated:** 2026-06-24T04:50:40.042537

1. pegg2010sperminesynthase pages 4-6
2. fuell2010polyaminebiosyntheticdiversity pages 4-6
3. kozbial2005naturalhistoryof pages 6-7
4. shoji2015polyaminederivedalkaloidsin pages 1-4
5. michael2017evolutionofbiosynthetic pages 9-12
6. kozbial2005naturalhistoryof pages 15-16
7. fuell2010polyaminebiosyntheticdiversity pages 3-4
8. pegg2010sperminesynthase pages 6-8
9. fuell2010polyaminebiosyntheticdiversity pages 6-6
10. tong2025dnamethylationvalley pages 2-4
11. riechers1999structureandexpression pages 10-12
12. shoji2024geneticregulationand pages 2-3
13. pegg2010sperminesynthase pages 1-2
14. michael2017evolutionofbiosynthetic pages 14-15
15. riechers1999structureandexpression pages 1-2
16. riechers1999structureandexpression pages 4-5
17. riechers1999structureandexpression pages 12-14
18. shoji2024geneticregulationand pages 3-4
19. tong2025dnamethylationvalley pages 1-2
20. https://doi.org/10.1186/1472-6807-5-19,
21. https://doi.org/10.1007/s00018-009-0165-5,
22. https://doi.org/10.1016/j.plaphy.2010.02.008,
23. https://doi.org/10.1042/bcj20160823,
24. https://doi.org/10.3389/fpls.2025.1647622,
25. https://doi.org/10.1023/a:1006342018991,
26. https://doi.org/10.1093/jxb/erad341,
27. https://doi.org/10.1007/978-4-431-55212-3\_16,