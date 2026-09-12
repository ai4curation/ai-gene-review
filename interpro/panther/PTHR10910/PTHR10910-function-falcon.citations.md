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

- **PANTHER family:** PTHR10910 — EUKARYOTE SPECIFIC DSRNA BINDING PROTEIN
- **Subfamily of interest:** PTHR10910:SF62 AT07585P-RELATED
- **Representative member:** ADAR2 (C1JAR3), DOROP / DOROP
- **GO term currently propagated at/near this node:** tRNA-specific adenosine deaminase activity (GO:0008251)

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
3. **Subfamily of interest.** Where does PTHR10910:SF62 AT07585P-RELATED sit — does it carry the
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
**Generated:** 2026-06-24T04:56:22.200164

1. fisher2024structuralperspectiveson pages 5-6
2. ashley2024adarfamilyproteins pages 7-8
3. mannion2015newinsightsinto pages 1-4
4. keegan2004adenosinedeaminasesacting pages 3-4
5. palladino2000dadaradrosophila pages 2-4
6. savva2012theadarprotein pages 1-2
7. keegan2004adenosinedeaminasesacting pages 1-2
8. palladino2000dadaradrosophila pages 1-2
9. palladino2000dadaradrosophila pages 10-11
10. keegan2004adenosinedeaminasesacting pages 5-6
11. keegan2004adenosinedeaminasesacting pages 2-3
12. savva2012theadarprotein pages 2-4
13. keegan2017adarrnaediting pages 1-2
14. zhang2025adarspleiotropyin pages 4-4
15. zhang2025adarspleiotropyin pages 2-4
16. huebert2025frommetabolismto pages 22-24
17. keegan2004adenosinedeaminasesacting pages 6-7
18. ashley2024adarfamilyproteins pages 4-7
19. keegan2017adarrnaediting pages 3-5
20. https://doi.org/10.1016/j.omtn.2024.102284,
21. https://doi.org/10.3390/cimb46050243,
22. https://doi.org/10.3390/biom5042338,
23. https://doi.org/10.1186/gb-2004-5-2-209,
24. https://doi.org/10.1186/gb-2012-13-12-252,
25. https://doi.org/10.1261/rna.079266.122,
26. https://doi.org/10.1017/s1355838200000248,
27. https://doi.org/10.1261/rna.060921.117,
28. https://doi.org/10.1093/nar/gkaf672,
29. https://doi.org/10.20944/preprints202510.0048.v1,