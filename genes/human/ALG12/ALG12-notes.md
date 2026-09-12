# ALG12 (human, Q9BV10) review notes

## Summary of function

ALG12 is an ER membrane, ER-lumenal-facing alpha-1,6-mannosyltransferase (glycosyltransferase
family GT22; CAZy GT22, Pfam PF03901 Glyco_transf_22) of the dolichol-linked oligosaccharide
(LLO) assembly pathway for protein N-glycosylation. It transfers the **eighth mannose** from
**dolichyl-phosphate-mannose (Dol-P-Man)** in an alpha-1,6 linkage onto Man7GlcNAc2-PP-dolichol
to give Man8GlcNAc2-PP-dolichol (EC 2.4.1.260; RHEA:29535). The lumenal mannose additions of LLO
assembly use Dol-P-Man as donor, not GDP-Man.

- [UniProt Q9BV10 FUNCTION, "In the lumen of the endoplasmic reticulum, adds the eighth mannose residue in an alpha-1,6 linkage onto Man(7)GlcNAc(2)-PP-dolichol to produce Man(8)GlcNAc(2)-PP-dolichol."]
- [UniProt Q9BV10 SUBCELLULAR LOCATION "Endoplasmic reticulum membrane"; "Multi-pass membrane protein" — 12 predicted TM helices]
- [UniProt Q9BV10 SIMILARITY "Belongs to the glycosyltransferase 22 family."]

## Disease

Loss of ALG12 mannosyltransferase activity causes **ALG12-CDG / congenital disorder of
glycosylation type Ig (CDG-Ig, MIM:607143)**, a multisystem disorder with under-glycosylated
serum glycoproteins, psychomotor/developmental retardation, hypotonia, dysmorphism,
immunodeficiency.

## Key references (all abstract-only in cache; quotes verbatim from abstracts)

- **PMID:11983712** (Chantret et al 2002, J Biol Chem) — identified human ALG12 as ortholog of
  yeast ALG12 encoding the dolichyl-P-Man:Man7GlcNAc2-PP-dolichyl alpha6-mannosyltransferase;
  CDG-Ig patient fibroblasts "deficient in their capacity to add the eighth mannose residue onto
  the lipid-linked oligosaccharide precursor"; homozygous F142V; WT rescue. Establishes MF, BP,
  and disease. Basis of the EXP/IMP/IDA annotations.
- **PMID:12093361** (Thiel et al 2002, Biochem J) — "Deficiency of the endoplasmic reticulum
  enzyme dolichyl-phosphate mannose (Dol-P-Man):Man(7)GlcNAc(2)-PP-dolichyl mannosyltransferase";
  reduced activity, Man7GlcNAc2-PP-Dol accumulation; L158P + C-terminal truncation; WT rescue.
- **PMID:12217961** (Grubenmann et al 2002, Hum Mol Genet) — "a deficiency in the ALG12 ER
  alpha1,6-mannosyltransferase"; ER/lumenal localization inference; yeast alg12 complementation;
  T67M and R146Q. Basis of the IC (lumenal side of ER membrane) and NAS (ER; protein folding)
  annotations.
- **PMID:19946888** (Ghosh et al 2010, J Mass Spectrom) — NK-cell membrane proteome MS study
  (1843 proteins); basis of HDA "membrane" annotation. Generic membrane localization only.

## Annotation decisions (high level)

- Core MF: GO:0052917 (dol-P-Man:Man(7)GlcNAc(2)-PP-Dol alpha-1,6-mannosyltransferase activity) —
  EXP/IMP ACCEPT (core). Exact GOA current term (EC 2.4.1.260).
- GO:0000009 (alpha-1,6-mannosyltransferase activity, IBA) ACCEPT — correct but less specific
  than GO:0052917.
- GO:0000030 (mannosyltransferase activity, TAS Reactome x2) MODIFY -> GO:0052917 (too general).
- GO:0016757 (glycosyltransferase activity, IEA InterPro) ACCEPT as correct-but-broad parent.
- Core BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) IMP/IDA/TAS and
  GO:0006487 (protein N-linked glycosylation) IBA/IMP — ACCEPT (core).
- Core CC: GO:0005789 (ER membrane) IBA/IEA/TAS — ACCEPT. GO:0098553 (lumenal side of ER
  membrane, IC) ACCEPT (more specific, correct topology). GO:0005783 (ER, NAS) ACCEPT as broader.
- GO:0016020 (membrane, HDA PMID:19946888) MARK_AS_OVER_ANNOTATED — uninformative generic
  membrane from a proteome survey; ER membrane is the specific term.
- GO:0006457 (protein folding, NAS PMID:12217961) — MARK_AS_OVER_ANNOTATED. ALG12 does not fold
  proteins; N-glycosylation is upstream of/supports folding but "protein folding" mis-describes
  the molecular role. Downstream/indirect.
