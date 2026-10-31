# UNC119B (A6NIH7) curation notes

## Deep research status
`just deep-research-falcon human UNC119B` first failed (falcon timed out at 600 s; perplexity-lite fallback unavailable in this environment). Re-run with `--timeout 2400` succeeded: see UNC119B-deep-research-falcon.md.

## Summary of function
- UNC119B is a myristoyl-binding cargo carrier of the PDE6D/UNC119 family (Ig-like beta-sandwich pocket) [PMID:22085962 "Here we report that UNC119 is a myristoyl-binding protein that binds to a subset of myristoylated proteins, including NPHP3 and cystin, and that the small GTPase ARL3 regulates myristoyl–cargo binding."]
- Pocket phenylalanines are required for myristate binding [PMID:22085962 "we identified highly conserved phenylalanines within a hydrophobic β sandwich to be essential for myristate binding"].
- ARL3-GTP releases cargo [PMID:22085962 "Furthermore, we found that binding of ARL3-GTP serves to release myristoylated cargo from UNC119."]; only ARL3 (not ARL2) allosterically releases cargo, and UNC119B releases more readily than UNC119A [PMID:22960633 "However, UNC119b seems to be more prone to cargo release than UNC119a."].
- Paralog specificity in cells: UNC119B, not UNC119A, is required for NPHP3 ciliary targeting, and the myristoyl pocket is required [PMID:22085962 "Strikingly, the myristoyl-binding mutant tdTomato-UNC119b Mut-4 failed to rescue to the same extent, indicating that NPHP3 ciliary targeting indeed requires the myristoyl-binding activity of UNC119b."]. GPCR delivery is unaffected [PMID:22085962 "indicating that delivery of nonmyristoylated proteins to the cilium is not disrupted by the depletion of ARL3 pathway components"].
- Localization: transition zone and proximal cilium [PMID:22085962 "More importantly, the LAP-UNC119b was enriched at the transition zone and extended into the proximal end of the cilium"].
- Zebrafish morphant data indicate ciliary dysfunction (KV, body curvature, vision) for the UNC119B-like zebrafish gene [PMID:22085962 "Furthermore, in zebrafish, knockdown of unc119a lead to three cilia-related phenotypes (curved body, KV defect, and vision impairment)"], but cilia still form in human knockdown cells; treated cilium assembly as non-core.

## Key decisions
- protein binding rows: ARL3 row -> MODIFY to small GTPase binding (GO:0031267); cargo rows (NPHP3, cystin) -> REMOVE (captured by lipid binding GO:0008289); MACIR row -> REMOVE.
- GO:0031997 (N-terminal myristoylation domain binding) is obsolete (verified in OLS), so lipid binding is the MF used.
- NEW: protein localization to ciliary membrane (GO:1903441), IMP PMID:22085962; comparator PDE6D carries protein localization to cilium (GO:0061512).
- HPA sperm flagellum rows (midpiece/principal/end piece): KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role
- Module (primary_cilium_life_cycle, stage 5 membrane composition): "myristoylated cargo carrier", process protein localization to cilium.
- HPA v25 (member_evidence.md): no primary cilium / basal body / centrosome call; main locations Annulus; Cytokinetic bridge; Cytosol; Flagellar centriole; Mitotic spindle. GOA HPA rows are sperm midpiece, principal piece and end piece (GO_REF:0000052). The Hansen et al. 2025 cilium atlas [PMID:41005307 "Our analysis identified the subciliary locations of 715 proteins across three cell lines, examining 128,156 individual cilia."] did not report UNC119B at primary cilia in the HPA cell lines.
- Interpretation: absence of an HPA cilium call is not evidence against the module role. UNC119B is a soluble carrier that concentrates at the transition zone/proximal cilium only transiently when it delivers cargo, and tagged-protein localization in RPE cells did show a ciliary pool. The cytosol call fits a soluble carrier. core_functions agree with the module role (lipid binding / small GTPase binding; lipoprotein transport; protein localization to ciliary membrane, a child of the module's GO:0061512).

## Additional points from deep research (falcon)
- A 2025 study (Horne et al., PNAS, doi:10.1073/pnas.2420961122; not cached) reports that purified UNC119B binds and allosterically activates the kinase PSKH1 independently of PSKH1 lipidation. Not used for annotation (no cached paper); noted as a possible second activity in suggested questions territory.
- Yelland et al. 2021 (Biochemistry) report UNC119B-myristoyl-LCK and UNC119B-ARL3 structures; Jaiswal et al. 2016 measured sub-nM affinities for NPHP3/cystin peptides. Deep research: "UNC119 proteins preferentially carry N-myristoylated cargo, whereas PDE6D is primarily a prenyl-cargo carrier."
- Zebrafish nomenclature caution: zebrafish unc119a is the ortholog of human UNC119B.
