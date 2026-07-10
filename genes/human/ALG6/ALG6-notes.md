# ALG6 (human) curation notes

UniProtKB:Q9Y672 — Dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase; EC 2.4.1.267.
HGNC:23157. 507 aa multi-pass ER membrane protein (UniProt lists 10 TM helices).

> Note: falcon deep research was unavailable (API out of credits, HTTP 402). This review is
> grounded in the UniProt record (`ALG6-uniprot.txt`), the seeded GOA (`ALG6-goa.tsv`), and the
> cached publications under `publications/`. No `-deep-research-falcon.md` was fabricated.

## Core biology

ALG6 is the ER-lumenal alpha-1,3-glucosyltransferase that adds the **first of three glucoses**
to the dolichol-linked oligosaccharide (LLO). It transfers glucose from dolichyl-phosphate-glucose
(Dol-P-Glc; **not** UDP-Glc) onto Man9GlcNAc2-PP-dolichol to give Glc1Man9GlcNAc2-PP-dolichol,
the substrate for the next enzyme ALG8.

- UniProt FUNCTION: "In the lumen of the endoplasmic reticulum, adds the first glucose residue from
  dolichyl phosphate glucose (Dol-P-Glc) onto the lipid-linked oligosaccharide intermediate
  Man(9)GlcNAc(2)-PP-Dol to produce Glc(1)Man(9)GlcNAc(2)-PP-Dol. Glc(1)Man(9)GlcNAc(2)-PP-Dol is a
  substrate for ALG8, the following enzyme in the biosynthetic pathway."
  [ECO:0000269|PubMed:10359825, ECO:0000269|PubMed:25792706]
- CATALYTIC ACTIVITY: RHEA:30635, EC=2.4.1.267; donor = di-trans,poly-cis-dolichyl beta-D-glucosyl
  phosphate (Dol-P-Glc).
- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane; Multi-pass membrane protein.
- Belongs to the ALG6/ALG8 glucosyltransferase family (CAZy GT57; Pfam PF03155 Alg6_Alg8;
  InterPro IPR004856).

Glucosylation of the LLO is required for **efficient transfer** of the glycan to nascent protein by
the oligosaccharyltransferase (OST). Loss of ALG6 causes accumulation of Man9GlcNAc2-PP-Dol and
protein hypoglycosylation.

## Disease

ALG6 deficiency causes **ALG6-CDG / congenital disorder of glycosylation type Ic (CDG1C; MIM:603147)**,
one of the most common CDG-I subtypes. Recessive; many missense/deletion/splice variants (e.g. A333V —
the most common; S478P; delI299; exon-3 skipping). F304S is a common mild/polymorphic allele that can
exacerbate other CDGs. [UniProt DISEASE; PMID:10359825, PMID:10924277, PMID:10914684, etc.]

## Key references (cached; all abstract-only except PMID:33961781)

- **PMID:10359825** (Imbach 1999, PNAS): cloned human ALG6 as ortholog of yeast ALG6 "dolichyl
  pyrophosphate Man9GlcNAc2 alpha1,3-glucosyltransferase"; mutant human ALG6 fails to complement yeast
  alg6 hypoglycosylation; defines CDGS type-Ic. Origin of MF (IDA/IGI/IC), BP, N-glycosylation, and
  lumenal-side localization annotations.
- **PMID:10924277** (Westphal 2000, Mol Genet Metab): "This enzyme is required for the addition of the
  first glucose residue to the lipid-linked oligosaccharide precursor for N-linked glycosylation."
  IDA acts_upstream_of_or_within N-glycosylation.
- **PMID:25792706** (Shrimal & Gilmore 2015, Glycobiology): ALG6-deficient cells assemble
  Dol-PP-GlcNAc2Man9 as largest donor; hypoglycosylation of OST sites. IMP for MF/BP/N-glyc.
- **PMID:19946888** (Ghosh 2010): NK-cell membrane proteome MS; supports membrane localization (HDA).
- **PMID:33961781** (Huttlin 2021, BioPlex): interactome AP-MS; ALG6–ALG8 (Q9BVK2) interaction (bare
  protein-binding IPI). UniProt INTERACTION record: "Q9Y672; Q9BVK2: ALG8; NbExp=2".

## Annotation decisions (summary)

- MF **GO:0042281** dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase activity — the
  exact GOA/EC 2.4.1.267 term. ACCEPT (IBA, IMP, IEA). Core MF.
- MF **GO:0004583** dolichyl-phosphate-glucose-glycolipid alpha-glucosyltransferase activity (Reactome
  TAS) — the parent/donor-focused MF; correct chemistry (Dol-P-Glc donor) but less precise than
  GO:0042281 → MODIFY to GO:0042281.
- MF **GO:0016758** hexosyltransferase activity (IEA InterPro) — correct but general grouping → MODIFY
  to GO:0042281 (or KEEP; chose MODIFY, over-general).
- MF **GO:0046527** glucosyltransferase activity (IDA) — correct but general parent → MODIFY to
  GO:0042281.
- MF **GO:0005515** protein binding (IPI, ALG8) — bare protein binding, uninformative → MARK_AS_OVER_ANNOTATED.
- BP **GO:0006488** dolichol-linked oligosaccharide biosynthetic process — core BP. ACCEPT.
- BP **GO:0006487** protein N-linked glycosylation — downstream process ALG6 is required for. ACCEPT.
- CC **GO:0005789** endoplasmic reticulum membrane — correct localization. ACCEPT.
- CC **GO:0098553** lumenal side of ER membrane (IC) — active-site topology; correct. ACCEPT.
- CC **GO:0016020** membrane (HDA proteomics) — correct but general → MODIFY to GO:0005789.
</content>
</invoke>
