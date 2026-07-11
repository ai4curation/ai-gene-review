# HSD3B2 (P26439) review notes

## Identity
- 3 beta-hydroxysteroid dehydrogenase / Delta 5-->4-isomerase **type 2** (3-beta-HSD II).
- The **adrenal and gonadal** isozyme (type I is placenta/skin). UniProt AltName "3-beta-HSD adrenal and gonadal type".
- 372 aa, single-pass membrane protein of the ER (and mitochondrion membrane). EC 1.1.1.145 (dehydrogenase) + EC 5.3.3.1 (isomerase).
- Family: 3-beta-HSD family; NAD(P)-binding Rossmann fold (Pfam PF01073 3Beta_HSD; InterPro IPR002225).

## Function (bifunctional NAD+-dependent)
- Catalyzes the obligatory early step common to ALL steroid hormone classes: oxidation of the 3beta-hydroxyl (dehydrogenase) then isomerization of the Delta5 double bond to Delta4 (isomerase).
- Substrate pairs: pregnenolone->progesterone; 17-hydroxypregnenolone->17-hydroxyprogesterone; DHEA->androstenedione.
- UniProt FUNCTION: "3-beta-HSD is a bifunctional enzyme, that catalyzes the oxidative conversion of Delta(5)-ene-3-beta-hydroxy steroid, and the oxidative conversion of ketosteroids. The 3-beta-HSD enzymatic system plays a crucial role in the biosynthesis of all classes of hormonal steroids." [ECO:0000269|PubMed:1741954]
- PMID:1944309 (Rheaume 1991) abstract: "The 3 beta-hydroxysteroid dehydrogenase/delta 5-delta 4 isomerase (3 beta HSD) enzyme catalyzes the oxidation and isomerization of delta 5-3 beta-hydroxysteroid precursors into delta 4-ketosteroids, thus leading to the formation of all classes of steroid hormones." Type II is "the almost exclusive 3 beta HSD mRNA species in the human adrenal gland, ovary, and testis."
- PMID:25322271 (Baquedano 2015) CONTEXT: "3betaHSD2 is a bifunctional microsomal NAD+-dependent enzyme crucial for adrenal and gonad steroid biosynthesis, converting Delta5-steroids to Delta4-steroids." G250V mutant: "impaired enzymatic activity for the conversion of pregnenolone to progesterone and dehydroepiandrosterone to androstenedione (20% and 27% of WT at 6 h, respectively)."

## Localization
- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane {ECO:0000269|PubMed:25322271}; Single-pass membrane protein. Mitochondrion membrane; Single-pass membrane protein."
- HPA IDA (GO_REF:0000052): endoplasmic reticulum (GO:0005783).
- PMID:25322271 EXP: ER membrane; G250V "no effect on endoplasmic reticulum location."
- Mitochondrial inner membrane / intermembrane space ISS (GO:0005743/GO:0005758) transferred from rat P14060 — weaker; the primary experimentally supported site is the ER. Mitochondrial membrane NAS from PMID:1944309.

## Disease
- Adrenal hyperplasia 2 (AH2 / 3beta-HSD-deficiency congenital adrenal hyperplasia), MIM:201810. Salt-wasting to non-classic forms; ambiguous genitalia. Recessive loss-of-function HSD3B2 mutations. Many characterized missense variants (A10E, G15D, E142K, G250V, etc.).

## Annotation calls (summary)
- MF core: GO:0003854 (3-beta-hydroxy-Delta5-steroid dehydrogenase (NAD+) activity) + GO:0004769 (steroid Delta-isomerase activity). Both experimentally supported (IDA PMID:1944309; IMP PMID:25322271). ACCEPT.
- GO:0004022 alcohol dehydrogenase (NAD+) activity (RHEA IEA) — over-broad/incorrect mapping from the pregnenolone RHEA:43924; the substrate is a steroid, not a simple alcohol. MARK_AS_OVER_ANNOTATED (RHEA auto-mapping artifact).
- GO:0016616 (oxidoreductase, CH-OH/NAD) IBA + IEA — correct but a generic parent of GO:0003854; KEEP_AS_NON_CORE / MODIFY toward GO:0003854.
- BP core: GO:0006694 steroid biosynthetic process (IDA/IMP/IBA/IEA). ACCEPT. GO:0006702 androgen biosynthetic process and GO:0008207 C21-steroid hormone metabolic process are true sub-roles; the enzyme also feeds mineralo/glucocorticoid synthesis. KEEP_AS_NON_CORE (individual downstream branches).
- CC: ER (GO:0005783) IDA + ER membrane (GO:0005789) EXP/TAS/IEA — ACCEPT (primary site). Mito membrane/inner membrane/IMS and smooth ER membrane — weaker (NAS/ISS); KEEP_AS_NON_CORE. cytoplasm IBA (GO:0005737) generic; KEEP_AS_NON_CORE. membrane GO:0016020 NAS generic; MODIFY toward ER membrane.
- GO:0005515 protein binding (IPI PMID:32814053, GLE1 + SPRED1, IntAct) — bare protein binding, high-throughput Y2H interactome; MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).

## References cited
- PMID:1944309 (Rheaume 1991) — cloning + kinetics of type II; adrenal/gonad specificity.
- PMID:25322271 (Baquedano 2015) — bifunctional NAD+ enzyme, G250V CAH, ER localization.
- PMID:32814053 (Haenig 2020) — ND interactome Y2H (source of the IntAct protein-binding IPIs).
- file:human/HSD3B2/HSD3B2-uniprot.txt — UniProt P26439 record.
- Reactome R-HSA-193052/193073/193961/196350/196372 — the individual dehydrogenation/isomerization reactions in the ER.
