# GSTF6 (At1g02930, P42760) — curation notes

## Identity
- Phi-class glutathione S-transferase, 208 aa, GST N-terminal (2-83) and C-terminal (89-208) domains; EC 2.5.1.18 (UniProt P42760).
- Synonyms ERD11, GST1, and (historically) AtGSTF3. Caution: in current Arabidopsis GST nomenclature GSTF3 is a different locus (At2g02930); the deep research flags this [file:ARATH/GSTF6/GSTF6-deep-research-falcon.md "“GSTF3” is an ambiguous historical alias"]. This matters for the Dixon et al. 2011 ligand-binding annotations (below).
- Tandem duplicate of GSTF7 [PMID:15159623 "closely related members of the same class ( GSTF6 and GSTF7 ), arising via tandem duplication, may be regulated differently"].

## Expression
- Dehydration-inducible (ERD11) [PMID:8253194 "The expression of the genes for ERD11 and ERD13 was induced by dehydration"].
- Broadly stress-inducible [PMID:12090627 "AtGSTF6 was upregulated by all treatments"] (phytohormones, herbicides, oxidative stress, Peronospora).
- SA-induced protein, retained on glutathione affinity [PMID:15159623 "glutathione-affinity chromatography"].
- Cd-responsive root proteome [PMID:17075075].

## Biochemistry
- Recombinant GSTF6 is soluble and catalyses GSH conjugation [PMID:12090627 "All GSTs except AtGSTF10 formed soluble proteins which catalysed a specific range of glutathione conjugation or glutathione peroxidase activities"].
- CDNB activity reported as very low (0.87 nmol/min/mg; Wangwattana 2008, no PMID, via deep research). Physiological substrate(s) unknown.

## Camalexin
- Su et al. 2011 [PMID:21239642 "GSTF6 overexpression increased and GSTF6-knockout reduced camalexin production"; "Arabidopsis GSTF6 expressed in yeast cells catalyzed GSH(IAN) formation"].
- Full text (PMC3051237, read via WebFetch, not cached, so not quoted in YAML): knockout effect ~27-28% reduction; overexpression +10-30%; GFP-expressing control yeast also formed GSH(IAN), GSTF6 adding only 40-61% more. So the yeast assay shows enhancement over a substantial non-GSTF6 background (spontaneous or endogenous yeast GST).
- Reviews repeat GSTF6 as the conjugating enzyme [PMID:21712415 "After an unknown activation step, GSTF6 catalyzes the conjugation to GSH to give GS-IAN"], [PMID:23449503 "provided support for the involvement of GSTF6 in the camalexin pathway"].
- Counterevidence (Mucha 2019, PMID:31511315; full text not cached; via deep research): gstf2 gstf3 gstf6 triple knockout and quadruple knockdown had no significant camalexin change after AgNO3; GSTF6 did not boost camalexin in N. benthamiana reconstruction; 41/54 Arabidopsis GSTs supported GS-IAN formation with CYP71A13 in yeast. Activated intermediate (indole cyanohydrin) can react spontaneously with GSH. [file:ARATH/GSTF6/GSTF6-deep-research-falcon.md "Such findings point to enzyme redundancy, spontaneous chemistry, host-dependent effects, or spatial organization, rather than unique GSTF6 substrate specificity"].
- GSTU4 (not GSTF6) is the GST physically recruited to the P450 metabolon, and it is NOT a pathway enzyme [PMID:31511315 "This shows that GSTU4 is not directly involved in camalexin biosynthesis but rather plays a role in a competing mechanism."]. Do not transfer metabolon membership to GSTF6.
- GOA has no camalexin biosynthesis annotation for GSTF6 (QuickGO, checked 2026-10-03), while CYP71A13, CYP71B15, GGP1 carry GO:0010120. The ComplexPortal camalexin metabolon (CPX-2833) does not include GSTF6.
- Decision: no NEW GO:0010120. Evidence is contributory/partially redundant and contested; module records GSTF6 as "implicated". Raised as a suggested question.

## Localization
- No targeting peptide; predicted cytosolic [PMID:21712415 "The fourth enzyme, GSTF6, lacks predicted signaling peptides and is therefore most likely cytosolic."]. Cytosolic SEC proteome (PMID:25293756) agrees.
- Organelle/wall/vacuole/PD/extracellular HDA hits are best read as contamination of an abundant soluble protein (e.g. PD proteome "still has a significant number (35%) of putative cytoplasmic contaminants" [PMID:21533090]).
- Stress granule (Kosmacz 2019) — kept as non-core.

## Ligand binding (Dixon et al. 2011, PMID:21631432)
- Abstract reports camalexin and quercetin-3-O-rhamnoside binding by GSTF2; heterocycle binding by "GSTF2 and GSTF3". GSTF6 is not named in the abstract and the full text is paywalled (403). Could be a GSTF3/GSTF6 alias issue, but I cannot verify -> UNDECIDED.

## Not anthocyanin carrier
- gstf6-1 has no anthocyanin defect; TT19 binds C3G 8.4x better (deep research; Wangwattana 2008, Sun 2012).
