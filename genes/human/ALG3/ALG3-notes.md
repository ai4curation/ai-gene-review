# ALG3 (Q92685) review notes

## Summary of function

ALG3 is the human Dol-P-Man:Man(5)GlcNAc(2)-PP-dolichol alpha-1,3-mannosyltransferase
(EC 2.4.1.258), the enzyme catalysing the **first ER-lumenal step** of dolichol-linked
oligosaccharide (LLO) assembly for protein N-glycosylation.

- Assembly of the LLO begins on the **cytosolic face** of the ER membrane and finishes
  in the **lumen**. After Man5GlcNAc2-PP-dolichol is flipped to the lumenal face, ALG3
  transfers the **sixth mannose** (the first mannose derived from **dolichyl-phosphate-mannose,
  Dol-P-Man**, rather than GDP-Man) in an **alpha-1,3 linkage** onto Man5GlcNAc2-PP-Dol to
  give **Man6GlcNAc2-PP-dolichol**. The product is the substrate for ALG9, the next enzyme
  in the pathway [UniProt Q92685 FUNCTION; PMID:10581255].
- ALG3 is a **polytopic ER membrane protein** (11 predicted TM helices; UniProt features),
  member of the glycosyltransferase ALG3 family / CAZy GT58, active on the lumenal side of
  the ER membrane.
- It is the structural and functional orthologue of *S. cerevisiae* ALG3
  [PMID:10581255 "The mannosyltransferase is the structural and functional orthologue of the
  Saccharomyces cerevisiae ALG3 gene."].

## Disease

Deficiency causes **ALG3-CDG (congenital disorder of glycosylation type Id / CDG1D;
MIM:601110)**, originally described as CDGS type IV. Characterised by microcephaly,
severe epilepsy, minimal psychomotor development, dysmorphism, and partial deficiency of
sialic acids in serum glycoproteins; the defect causes accumulation of the
Man5GlcNAc2-PP-Dol intermediate and transfer of truncated oligosaccharides
[PMID:10581255; PMID:15840742]. Pathogenic variants include G118D and R171Q.

## Key references
- PMID:10581255 (Körner et al. 1999, EMBO J): identified ALG3 as the deficient
  mannosyltransferase in CDGS type IV; defines catalytic activity, pathway, subcellular
  location, and disease. Abstract-only in cache (full_text_available: false) but abstract
  is rich. This is the primary experimental reference for MF/BP/CC IDA/IC annotations.
- PMID:15840742 (Sun et al. 2005): CDG1D variant R171Q; clinical presentation.
- PMID:29547901 (Hacker et al. 2018, Hum Mol Genet): Y2H interactome of hNOT/ALG3;
  homodimers, and interactions with OSBP, OSBPL9, LRP1, SYPL1, CREB3. Abstract-only.
  Provides functional context for the IntAct protein-binding annotations. 33% identity
  with yeast ALG3.

## Annotation review decisions

GOA MF term = **GO:0052925** (dol-P-Man:Man(5)GlcNAc(2)-PP-Dol alpha-1,3-mannosyltransferase
activity) — this is the specific, correct current MF; used in IBA, IEA(EC/RHEA), and IDA.

- Core MF: GO:0052925 (IDA PMID:10581255, plus IBA and EC/RHEA IEA) — ACCEPT.
- GO:0000030 mannosyltransferase activity (IEA InterPro) and GO:0000033
  alpha-1,3-mannosyltransferase activity (TAS Reactome): correct but **less specific**
  parents of GO:0052925 -> MODIFY to GO:0052925 (over-general MF).
- Core BP: GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IDA + TAS) and
  GO:0006487 protein N-linked glycosylation (IDA + IEA) — ACCEPT.
- GO:0009101 glycoprotein biosynthetic process (IBA): correct but broad parent of
  GO:0006487 -> KEEP_AS_NON_CORE (acceptable broader IBA).
- Core CC: GO:0005789 endoplasmic reticulum membrane (IDA + IEA + TAS) — ACCEPT;
  GO:0098553 lumenal side of ER membrane (IC) — ACCEPT (precise topology).
  GO:0005783 endoplasmic reticulum (IBA) — KEEP_AS_NON_CORE (broader parent of ER membrane).
- GO:0005515 protein binding (IPI x11 across 5 interactome papers): bare, uninformative
  MF from high-throughput screens -> MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
