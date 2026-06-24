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

- **PANTHER family:** PTHR11926 — GLUCOSYL/GLUCURONOSYL TRANSFERASES
- **Subfamily of interest:** PTHR11926:SF1392 GLYCOSYLTRANSFERASE
- **Representative member:** NaUGT1_candidate_UGT85A2_0 (A0A2H4GSI3), NICAT / NICAT
- **GO term currently propagated at/near this node:** quercetin 3-O-glucosyltransferase activity (GO:0080043)

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
3. **Subfamily of interest.** Where does PTHR11926:SF1392 GLYCOSYLTRANSFERASE sit — does it carry the
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
**Generated:** 2026-06-24T05:45:07.839998

1. gachon2005plantsecondarymetabolism pages 3-4
2. rehman2018comparativegenomicand pages 13-13
3. gharabli2024thesugardonor pages 3-4
4. gharabli2024thesugardonor pages 1-3
5. lethe2024similaritiesinstructure pages 4-5
6. lethe2024similaritiesinstructure pages 5-7
7. bowles2006glycosyltransferasesoflipophilic pages 6-7
8. lim2004aclassof pages 4-5
9. bowles2006glycosyltransferasesoflipophilic pages 9-10
10. gachon2005plantsecondarymetabolism pages 4-5
11. bowles2006glycosyltransferasesoflipophilic pages 16-17
12. gachon2005plantsecondarymetabolism pages 5-7
13. bowles2006glycosyltransferasesoflipophilic pages 7-9
14. lim2004aclassof pages 5-7
15. zhou2021metabolicengineeringfor pages 7-8
16. nielsen2008metabolonformationin pages 1-2
17. nielsen2008metabolonformationin pages 2-3
18. selmar2010biosynthesisofcyanogenic pages 22-25
19. zhou2021metabolicengineeringfor pages 8-10
20. lim2004aclassof pages 3-4
21. lethe2024similaritiesinstructure pages 1-4
22. rehman2018comparativegenomicand pages 3-6
23. bowles2006glycosyltransferasesoflipophilic pages 14-16
24. https://doi.org/10.3389/fbioe.2024.1396268,
25. https://doi.org/10.3390/biology11030441,
26. https://doi.org/10.1016/j.tplants.2005.09.007,
27. https://doi.org/10.3390/ijms25052782,
28. https://doi.org/10.1038/s41598-018-19535-3,
29. https://doi.org/10.1146/annurev.arplant.57.032905.105429,
30. https://doi.org/10.1038/sj.emboj.7600295,
31. https://doi.org/10.1007/s00253-021-11419-3,
32. https://doi.org/10.1016/j.phytochem.2007.06.033,
33. https://doi.org/10.1002/9781444320503.ch3,
34. https://doi.org/10.1093/nar/gkaa1106,