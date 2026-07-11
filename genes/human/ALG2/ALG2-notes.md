# ALG2 (Q9H553) review notes

## Summary of gene function

ALG2 (alpha-1,3/1,6-mannosyltransferase ALG2) is a bifunctional GDP-mannose:dolichol-linked
oligosaccharide mannosyltransferase acting on the cytoplasmic face of the ER membrane in the
early (cytosolic) phase of N-glycan lipid-linked oligosaccharide (LLO) assembly. It catalyses
addition of the **second and third mannose** residues onto Man1GlcNAc2-PP-dolichol
(M1Gn2-PDol) to form the branched Man3GlcNAc2-PP-dolichol (M3Gn2-PDol) core, adding one mannose
in an alpha-1,3 linkage and one in an alpha-1,6 linkage. The M3Gn2-PDol product is the substrate
for ALG11 (next enzyme). It is a single-pass / single membrane-binding-domain ER membrane protein
in human (topology differs from yeast). EC 2.4.1.132 (alpha-1,3) and EC 2.4.1.257 (alpha-1,6);
CAZy family GT4 (glycosyltransferase group 1, GT4 subfamily).

Deficiency causes ALG2-CDG (congenital disorder of glycosylation type Ii / CDG-Ii, MIM:607906)
and congenital myasthenic syndrome type 14 (CMS14, MIM:616228).

## Key references

- [PMID:12684507 Thiel et al. 2003 J Biol Chem, "hALG2 was shown to act as an alpha1,3-mannosyltransferase"]
  Identified hALG2 as the CDG-Ii gene; deficiency of "GDP-Man:Man1GlcNAc2-PP-dolichol mannosyltransferase (hALG2)";
  patient fibroblasts accumulate Man1GlcNAc2-PP-dolichol and Man2GlcNAc2-PP-dolichol; WT hALG2 rescues both patient
  fibroblasts and yeast alg2-1. Establishes CDG-Ii, MF (a1,3-MTase), pathway (LLO biosynthesis), and used the yeast
  ALG2 (P43636) ortholog for identification (IGI to P43636). Abstract-only in cache.

- [PMID:35136180 Xiang et al. 2022 Commun Biol, "Alg2 catalyzes addition of both the second and third mannose to
  M1Gn2-PDol to form a branched Man(alpha1,3)Man(alpha1,6)-M1Gn2-PDol (M3Gn2-PDol)"] Full text available.
  Purified recombinant hAlg2 shown bifunctional (both a1,3 and a1,6 MTase); ER membrane localization confirmed by
  IF (co-localizes with Calnexin) and membrane fractionation; FPP/protease-protection + Suc2A glycosylation-reporter
  assays show both N- and C-termini are cytosolic, i.e. the catalytic domain / active site is on the cytoplasmic side
  of the ER membrane; single membrane-binding domain in human (vs 4 hydrophobic domains in yeast). Kinetics: prefers
  a1,3 then a1,6 route under physiological conditions.

- [PMID:23404334 Cossins et al. 2013 Brain] "Congenital myasthenic syndromes due to mutations in ALG2 and ALG14."
  Establishes CMS14; variant V68G decreases protein abundance. NOT in publications cache (no annotation cites it in GOA).

- [PMID:32814053 Haenig et al. 2020 Cell Rep] Y2H interactome; source of the two IntAct protein-binding IPIs
  (ALG2 vs ATXN1 P54253 and HTT P42858). ND-focused interactome; ATXN1 and HTT are neurodegeneration proteins.
  Bare protein binding, not an informative MF for ALG2's enzymatic role.

- [PMID:19946888 Ghosh et al. 2010 J Mass Spectrom] NK-cell membrane proteome (YTS cell line); source of the HDA
  "membrane" localization. Large-scale MS, generic "membrane".

## GO term / label check (from GOA 2026 refresh)

- GO:0004378 = "GDP-Man:Man(1)GlcNAc(2)-PP-Dol alpha-1,3-mannosyltransferase activity" (EC 2.4.1.132)
- GO:0102704 = "GDP-Man:Man(2)GlcNAc(2)-PP-Dol alpha-1,6-mannosyltransferase activity" (EC 2.4.1.257)
- GO:0000033 = "alpha-1,3-mannosyltransferase activity" (parent/generic MF)
- GO:0006488 = "dolichol-linked oligosaccharide biosynthetic process"
- GO:0006487 = "protein N-linked glycosylation"
- GO:0005789 = "endoplasmic reticulum membrane"
- GO:0098554 = "cytoplasmic side of endoplasmic reticulum membrane"

## Curation decisions rationale

- The two specific bifunctional MF terms GO:0004378 (a1,3) and GO:0102704 (a1,6) are the core molecular functions,
  strongly supported by IDA in both PMID:12684507 and PMID:35136180 -> ACCEPT (core).
- GO:0000033 "alpha-1,3-mannosyltransferase activity" is the generic parent; IDA (PMID:35136180) and IBA support it,
  but it is less precise than GO:0004378. Keep/accept (correct, just broader). GO:0016757 "glycosyltransferase activity"
  IEA is a very broad parent -> ACCEPT as broad-but-correct.
- Core BP: GO:0006488 dolichol-linked oligosaccharide biosynthetic process (multiple IDA/IBA/TAS) -> ACCEPT (core).
  GO:0006487 protein N-linked glycosylation (acts_upstream_of_positive_effect, IDA) -> ACCEPT (upstream regulatory role).
  GO:0009101 glycoprotein biosynthetic process -> broad parent, correct -> ACCEPT/KEEP_AS_NON_CORE (broad).
- Localization: GO:0005789 ER membrane (EXP/TAS, IDA-backed) -> ACCEPT (core). GO:0098554 cytoplasmic side of ER membrane
  (IDA) -> ACCEPT (adds active-site sidedness). GO:0012505 endomembrane system (IBA) broad but correct -> ACCEPT/non-core.
  GO:0016020 membrane (HDA, NK proteome) -> uninformative broad CC -> MARK_AS_OVER_ANNOTATED.
- Protein binding GO:0005515 (two IPIs, PMID:32814053) -> bare protein binding, uninformative; per policy do not REMOVE
  experimental IPIs -> MARK_AS_OVER_ANNOTATED.
</content>
