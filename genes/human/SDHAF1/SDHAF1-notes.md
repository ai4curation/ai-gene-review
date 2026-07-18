# SDHAF1 (Succinate dehydrogenase assembly factor 1, mitochondrial) — review notes

UniProt: A6NFY7 (SDHF1_HUMAN). Gene: SDHAF1 (HGNC:33867); synonym LYRM8. Human, 115 aa.

## Summary of biology

SDHAF1 is a small (115 aa) mitochondrial-matrix **assembly factor** for succinate
dehydrogenase (SDH, respiratory Complex II). It is a **LYR-motif protein** (complex I LYR
family, SDHAF1 subfamily) and is NOT a structural subunit of the mature Complex II and is
not itself succinate-dehydrogenase catalytic. Its documented job is to promote maturation
of the iron-sulfur (Fe-S) subunit **SDHB**: it binds SDHB and recruits the Fe-S transfer
machinery (HSC20/HSCB co-chaperone + HSPA9 chaperone + ISCU scaffold) via direct binding
to the co-chaperone HSC20, thereby helping insert Fe-S clusters into SDHB.

- "Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme
  complex (also referred to as respiratory complex II)" [file:human/SDHAF1/SDHAF1-uniprot.txt].
- "Promotes maturation of the iron-sulfur protein subunit SDHB of the SDH catalytic dimer,
  protecting it from the deleterious effects of oxidants" [file:human/SDHAF1/SDHAF1-uniprot.txt].
- "Contributes to iron-sulfur cluster incorporation into SDHB by binding to SDHB and
  recruiting the iron-sulfur transfer complex formed by HSC20, HSPA9 and ISCU through direct
  binding to HSC20" [file:human/SDHAF1/SDHAF1-uniprot.txt].
- Subcellular location: "Mitochondrion matrix" [file:human/SDHAF1/SDHAF1-uniprot.txt].
- Family: "Belongs to the complex I LYR family. SDHAF1 subfamily." [file:human/SDHAF1/SDHAF1-uniprot.txt].
- Keyword: "Chaperone" [file:human/SDHAF1/SDHAF1-uniprot.txt].

## Molecular function reasoning

There is no catalytic MF here. The honest, specific, experimentally supported MF is
**protein-folding chaperone binding (GO:0051087)**: SDHAF1 binds the DnaJ/Hsp40-type
co-chaperone HSC20 (HSCB) directly through its N-terminal LYR motif. HSC20 is "the sole
human DnaJ type III cochaperone dedicated to Fe-S cluster biogenesis" and works with its
cognate HSP70 chaperone HSPA9 [PMID:24606901 full text]. SDHAF1 also acts as a
substrate-recruiting adaptor for SDHB, but "protein binding" (GO:0005515) is uninformative;
the chaperone-binding term captures the specific, defining molecular activity.

Supporting text:
- "members of the LYR motif family which assist assembly of complexes II or III, SDHAF1 and
  LYRM7, respectively, are HSC20 binding partners" [PMID:24606901,
  publications/PMID_24606901.md, full text].
- "SDHAF1 (LYRM8), which is involved in SDH assembly" [PMID:24606901].
- "SDHAF1 associates with SDHB through a non-LYR binding site, and utilizes its own LYR
  motif to position an ISCU-HSC20-HSPA9 complex" [PMID:24606901].
- "SDHAF1 transiently binds to aromatic peptides of SDHB through an arginine-rich region in
  its C terminus and specifically engages a Fe-S donor complex, consisting of the scaffold,
  holo-ISCU, and the co-chaperone-chaperone pair, HSC20-HSPA9, through an LYR motif near its
  N-terminal domain" [PMID:26749241 abstract, publications/PMID_26749241.md].

## Biological process reasoning

Core BP = **mitochondrial respiratory chain complex II assembly (GO:0034553)**. This is the
exact term used in both GOA (IMP PMID:19465911; IBA; IEA) and in the UniProt DR GO line
(GO:0034553 IMP:UniProtKB). Verified current/non-obsolete via OLS. The founding paper showed
loss-of-function causes SDH deficiency, rescued by wild-type re-expression:
- "SDHAF1, encoding a LYR complex-II specific assembly factor, is mutated in SDH-defective
  infantile leukoencephalopathy ... SDHAF1 is the first bona fide SDH assembly factor
  reported in any organism" [PMID:19465911 abstract].
- "SDH activity and amount were restored in mutant fibroblasts proportionally with
  re-expression of the wild-type gene" [PMID:19465911].

## Cellular component

Mitochondrial matrix (SL-0170 -> GO:0005759) and mitochondrion (GO:0005739). UniProt DR GO
gives GO:0005739 IDA:UniProtKB and GO:0005759 TAS:Reactome. GOA also has HPA IDA
(GO_REF:0000052), FlyBase HTP (PMID:34800366 mito proteome), and IDA PMID:19465911 to
mitochondrion. All consistent; matrix is the more specific/accurate compartment.
- "SUBCELLULAR LOCATION: Mitochondrion matrix" [file:human/SDHAF1/SDHAF1-uniprot.txt].

## Protein-binding (GO:0005515) IPI annotations

GOA carries several bare GO:0005515 "protein binding" IPI annotations from IntAct-curated
interaction datasets:
- PMID:24606901 with SDHB (P21912) and HSCB/HSC20 (Q8IWL3) — the functionally meaningful
  interactions (substrate + co-chaperone).
- PMID:26749241 with SDHB (P21912) and HSCB (Q8IWL3) — disease-mechanism paper.
- PMID:28380382 with HSCB (Q8IWL3) — HSC20-centered Fe-S delivery paper.
- PMID:32296183 (HuRI binary interactome) with KRT27 (Q7Z3Y8) and CIDEB (Q9UHD4) —
  large-scale Y2H; keratin/CIDEB are not biologically meaningful partners for a matrix
  assembly factor (likely screen artifacts / non-physiological).
- PMID:33961781 (BioPlex) with SDHB (P21912).

Per policy, IPI "protein binding" annotations are not removed; the meaningful ones
(SDHB, HSCB) are kept as non-core (they underpin, but are less informative than, the
GO:0051087 chaperone-binding MF), and the large-scale screen hits (KRT27, CIDEB) are
marked as over-annotated because "protein binding" is uninformative and the partners are
not physiologically relevant to SDHAF1's matrix assembly-factor role.

## Disease

Biallelic SDHAF1 variants cause mitochondrial complex II deficiency, nuclear type 2
(MC2DN2; MIM 619166) = infantile leukoencephalopathy with succinate accumulation; riboflavin
responsive [file:human/SDHAF1/SDHAF1-uniprot.txt; PMID:26749241 abstract].

## References consulted

- PMID:19465911 (Nat Genet 2009) — abstract only; founding paper, IMP for GO:0034553 and
  IDA mitochondrion.
- PMID:24606901 (Cell Metab 2014) — full text available; HSC20/LYR-motif specificity;
  supports chaperone-binding MF.
- PMID:26749241 (Cell Metab 2016) — abstract only; disease mutations impair Fe-S transfer to
  SDHB; SDHAF1-HSC20/HSPA9/ISCU and SDHAF1-SDHB interactions.
- PMID:28380382 (Cell Metab 2017) — abstract + partial full text; HSC20-centered Fe-S
  delivery to complexes I-III (SDHAF1 in LYR-family context).
- PMID:32296183 (Nature 2020, HuRI) — full text; binary interactome; KRT27/CIDEB screen hits.
- PMID:33961781 (Cell 2021, BioPlex 3.0) — full text; AP-MS interactome; SDHB.
- PMID:34800366 (Cell Rep 2021) — high-confidence mito proteome (HTP localization).
- Reactome R-HSA-9854984, R-HSA-9855212, R-HSA-9855252 — SDH assembly reaction context.
