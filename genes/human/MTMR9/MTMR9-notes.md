# MTMR9 notes


## 2026-09-08 paired human–horse review



MTMR9 is a catalytically inactive myotubularin-family protein that binds active myotubularins and regulates their activity, substrate preference and stability. Association with MTMR6 favors phosphatidylinositol-3,5-bisphosphate turnover, whereas association with MTMR8 regulates phosphatidylinositol-3-phosphate and autophagy. Its GRAM and phosphatase-like regions provide a conserved noncatalytic regulatory architecture.

## Catalytically inactive does not mean functionally inert

MTMR9 lacks intrinsic phosphatase catalysis but dimerizes with active MTMR6, MTMR7 and MTMR8. Human MTMR6/MTMR9 and MTMR8/MTMR9 studies directly measure altered catalytic rates, substrate preferences, cellular phosphoinositide levels and downstream phenotypes. The 2009 study also finds increased partner abundance consistent with stabilization. The 2012 study distinguishes the MTMR6/R9 anti-apoptotic role from MTMR8/R9 inhibition of autophagy. These are positive reasons to retain regulatory and process participation claims. The molecular-function distinction between generic phosphatase regulation and binding specifically to a protein phosphatase still needs attention because the experimentally studied partners are lipid phosphatases.

## Decisive inspected evidence

From [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/):

> Complex formation between the active myotubularins and MTMR9 increases their catalytic activity and alters their substrate specificity

## Evidence inventory

- [PMID:19038970: MTMR9 increases MTMR6 enzyme activity, stability, and role in apoptosis.](https://pubmed.ncbi.nlm.nih.gov/19038970/). [DOI:10.1074/jbc.M804292200](https://doi.org/10.1074/jbc.M804292200). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:22647598: Myotubularin-related protein (MTMR) 9 determines the enzymatic activity, substrate specificity, and role in autophagy of MTMR8.](https://pubmed.ncbi.nlm.nih.gov/22647598/). [DOI:10.1073/pnas.1207021109](https://doi.org/10.1073/pnas.1207021109). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.

## Transfer to the selected horse protein

The exact target is [A0A9L0T3C1](https://www.uniprot.org/uniprotkb/A0A9L0T3C1/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/MTMR9/MTMR9-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: phosphatidylinositol biosynthetic process, protein binding, protein phosphatase binding. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 76 GOA rows, the description and core functions. No ProtNLM2 file or prediction-evidence folder was opened.

### Identity
Q96QG7 is the canonical reviewed UniProt entry for human MTMR9 (549 aa), not a fragment or alternative gene model. Isoform 2 (Q96QG7-2, VSP_056209) lacks residues 1-85, most of the PH-GRAM domain (4-99). No annotation in GOA is isoform-specific.

### Catalytic status (new analysis)
`MTMR9-bioinformatics/catalytic_motif_rereview.py` → `RESULTS-rereview.md`: the HCX5R loop at 332-340 reads HGTEGTDST in human and mouse MTMR9, where the active partners MTMR6/7/8 have HCSDGWDRT. Both the catalytic Cys (G333) and Arg (S339) are lost [file:human/MTMR9/MTMR9-bioinformatics/RESULTS-rereview.md "MTMR9 lacks both the catalytic cysteine and the catalytic arginine"]. UniProt states the same thing [UniProt CAUTION "lacks the conserved active site cysteine residue at position 333"].

### Evolutionary grounding (PAINT, PTHR10807)
- MTMR9 is in subfamily PTHR10807:SF56 (MYOTUBULARIN-RELATED PROTEIN 9) together with mouse Mtmr9 (Q9Z2D0).
- PTN000086907 (MTMR9-lineage node, Bilateria) has IRD NOT for GO:0004438 and GO:0106018: the curator recorded loss of catalysis. At this node they did NOT negate GO:0046856 phosphatidylinositol dephosphorylation. At the other inactive-myotubularin node PTN000850005 they negated both MF and process. I read keeping GO:0046856 for MTMR9 as a deliberate decision (MTMR9 is the activating subunit of the dimer that does the step). So the IBA for GO:0046856 is ACCEPTed.
- PTN002246859 (Eumetazoa) carries GO:0019903 and GO:0010507, seeded only by MTMR9 itself. This is expected, not circular.

### Key evidence (abstract-level; the cached papers are abstract-only)
- MTMR6-MTMR9 [PMID:19038970 "MTMR9 increased the 3-phosphatase activity of MTMR6 up to 6-fold"; "the formation of this heteromer in cells resulted in increased protein levels of both MTMR6 and MTMR9"].
- MTMR8 vs MTMR6 specificity [PMID:22647598 "Complex formation between the active myotubularins and MTMR9 increases their catalytic activity and alters their substrate specificity"; "the MTMR8/R9 complex inhibits autophagy"].
- MTMR7 (mouse) [PMID:12890864 "The binding of MTMR9 increased the Ins(1,3)P2 phosphatase activity of MTMR7"].
- Macropinocytosis [PMID:24591580 "its binding partner MTMR9, are required for macropinocytosis"]. This is necessity evidence from siRNA, so no NEW process term was added.

### Decisions (counts: ACCEPT 16, MODIFY 27, REMOVE 27, KEEP_AS_NON_CORE 6)
- GO:0005515 (49 rows): applied the protein-binding policy. Rows whose partner is MTMR6, MTMR7 or MTMR8 → MODIFY to GO:0019902 phosphatase binding (22 rows). All other high-throughput partners (EMILIN1, MOS, NMI, LNX1, VAC14, DEPDC5, GRAMD4 and others) → REMOVE as uninformative (26 rows). The PMID:12890864 row → REMOVE: its GOA partner Q59HJ6 currently resolves to bovine LONP1, which the abstract does not mention. This is probably a stale or remapped accession; I have not read the full text.
- GO:0019903 protein phosphatase binding (IBA + 2 IPI) → MODIFY to GO:0019902. The partners are lipid phosphatases, and the children of GO:0019903 are protein-substrate phosphatases. This is raised as a suggested question because PAINT uses GO:0019903 for MTM-MTM binding elsewhere too (PTN000849982).
- GO:0006661 PI biosynthetic process (Reactome TAS) → MODIFY to GO:0046856.
- GO:0030234 enzyme regulator activity (IEA) → MODIFY to GO:0019211.
- Changes from the previous review: negative regulation of autophagy (IBA, IPI) goes from ACCEPT to KEEP_AS_NON_CORE, because it is a downstream consequence based on cell-culture evidence. Protein-containing complex goes from KEEP_AS_NON_CORE to ACCEPT, because the heterodimer is the functional unit and GO has no specific complex term for it.
- Core functions: (1) GO:0019211 phosphatase activator activity, directly involved in GO:0060304 and GO:0046856, in the cytosol; (2) GO:0019902 phosphatase binding, directly involved in GO:0050821 protein stabilization.

### Not verified / not used
The falcon report attributes ERGIC/Golgi localization and VSVG/WNT3A secretion effects to a 2020 study and a 2024 thesis (knop2024). Neither source is cached and the primary paper was not identified, so no annotation was based on them. This is listed in suggested_questions.

### Relative
The closest characterised relative by phylogeny is mouse Mtmr9 (Q9Z2D0), the ortholog in the same PANTHER subfamily PTHR10807:SF56 (the catalytic loop is identical). It has experimental data on MTMR7 binding and macropinocytosis/ruffles. The repo has no mouse Mtmr9 review.
No module or GO-CAM in the repo contains MTMR9.
