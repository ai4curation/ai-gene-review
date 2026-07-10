# HSD17B3 (P37058) review notes

## Identity / summary
- 17-beta-hydroxysteroid dehydrogenase type 3 (17β-HSD3); testicular isozyme; SDR family (12C2 / SDR12C2).
- Testis-specific NADPH-dependent oxidoreductase, ER-membrane bound, that catalyses the final step of testosterone biosynthesis: reduction of the 17-keto group of androstenedione (Δ4-androstene-3,17-dione) to the 17β-hydroxyl giving testosterone. Also reduces other 17-ketosteroids (DHEA, epiandrosterone, androstanedione, 11-oxygenated C19 steroids).
- Deficiency causes 46,XY disorder of sex development (17β-HSD3 deficiency / male pseudohermaphroditism with gynecomastia, MIM:264300): undervirilized 46,XY individuals; diagnostic hallmark is a decreased testosterone-to-androstenedione ratio.

## Key provenance (from UniProt P37058 + cached PMIDs)
- UniProt FUNCTION: "Catalyzes the conversion of 17-oxosteroids to 17beta-hydroxysteroids ... Favors the reduction of androstenedione to testosterone ... Uses NADPH while the two other EDH17B enzymes use NADH." (PubMed:16216911, 23856005, 26545797, 27927697, 8075637). [file:human/HSD17B3/HSD17B3-uniprot.txt]
- Catalytic activity: testosterone + NADP+ = androst-4-ene-3,17-dione + NADPH + H+ (RHEA:14981, EC 1.1.1.64), physiological direction right-to-left (i.e. androstenedione -> testosterone). [file:human/HSD17B3/HSD17B3-uniprot.txt]
- Also: 17β-estradiol + NADP+ = estrone + NADPH + H+ (RHEA:24616, EC 1.1.1.62) - the estradiol 17β-dehydrogenase activity underlying the IEA EC mapping. [file:human/HSD17B3/HSD17B3-uniprot.txt]
- SUBCELLULAR LOCATION: Endoplasmic reticulum (PubMed:16216911, 26545797). ER membrane per Reactome. N-terminal hydrophobic segment anchors to ER membrane. [file:human/HSD17B3/HSD17B3-uniprot.txt]
- TISSUE SPECIFICITY: Testis (PubMed:8075637). [file:human/HSD17B3/HSD17B3-uniprot.txt]
- PATHWAY: Hormone biosynthesis; testosterone biosynthesis. Steroid metabolism. [file:human/HSD17B3/HSD17B3-uniprot.txt]
- SIMILARITY: short-chain dehydrogenases/reductases (SDR) family, 17-beta-HSD 3 subfamily. Rossmann fold NAD(P)-binding; ACT_SITE Tyr198; NADP binding 48-77. [file:human/HSD17B3/HSD17B3-uniprot.txt]
- DISEASE (MPH / 46,XY DSD): "inadequate testicular synthesis of testosterone ... a diagnostic hallmark of this disorder is a decreased plasma testosterone-to-androstenedione ratio." [file:human/HSD17B3/HSD17B3-uniprot.txt]

## Cached publications
- PMID:8075637 (Geissler 1994, Nat Genet) abstract-only. Isolated cDNA encoding "a microsomal 17 beta-HSD type 3 isozyme ... uses NADPh as a cofactor, and is expressed predominantly in the testes"; mutations cause male pseudohermaphroditism via defective androstenedione->testosterone conversion "in the fetal testes". Basis for MF (testosterone 17β-DH), tissue (testis), disease, and male genitalia development annotations.
- PMID:26545797 (Engeli 2016, JSBMB) abstract-only. G133R mutant: "conversion of Δ4-androstene-3,17-dione (androstenedione) to testosterone was almost completely abolished for mutant G133R compared with wild-type 17β-HSD3"; "Wild-type 17β-HSD3 and mutant G133R showed comparable expression levels and intracellular localization." Supports MF (androstenedione->testosterone reduction) and ER localization (IDA). NADPH cofactor pocket residue G133.
- PMID:28514442 (Huttlin 2017, BioPlex/interactome) and PMID:33961781 (Huttlin 2021) - high-throughput AP-MS interactome papers; IntAct IPI protein-binding annotations (interactor P62166 = NCS1). Not informative MF; over-annotation.

## Annotation decisions (summary)
- MF testosterone dehydrogenase (NADP+) activity GO:0047045 (IBA, IDA, TAS): ACCEPT - core catalytic function.
- MF 17-beta-hydroxysteroid dehydrogenase (NADP+) activity GO:0072582 (IEA/RHEA): ACCEPT - accurate general MF for the reaction family (matches Rhea reactions incl. RHEA:69284 the generic 17β-OH steroid + NADP reaction). Broader-but-correct.
- MF estradiol 17-beta-dehydrogenase [NAD(P)+] activity GO:0004303 (IEA EC 1.1.1.62): KEEP_AS_NON_CORE - real minor activity (estradiol<->estrone) documented in UniProt, but not the physiological role; keep, non-core.
- MF oxidoreductase activity, acting on CH-OH group of donors GO:0016614 (IEA ARBA): ACCEPT (parent) - correct but general.
- MF protein binding GO:0005515 x2 (IPI, NCS1): MARK_AS_OVER_ANNOTATED - uninformative bare protein binding from HT interactome screens.
- BP androgen biosynthetic process GO:0006702 (TAS Reactome): ACCEPT - core process (testosterone is an androgen; final step).
- BP testosterone biosynthetic process GO:0061370 (IEA UniPathway): ACCEPT - core, most specific BP.
- BP steroid biosynthetic process GO:0006694 (IBA): ACCEPT (parent) - correct but general.
- BP lipid biosynthetic process GO:0008610 (IEA ARBA): MARK_AS_OVER_ANNOTATED - technically steroids are lipids but far too general/uninformative for this enzyme.
- BP male genitalia development GO:0030539 (TAS PMID:8075637): KEEP_AS_NON_CORE - downstream physiological consequence (testosterone drives male development); not the molecular/biosynthetic core.
- CC endoplasmic reticulum GO:0005783 (IBA, IEA, IDA): ACCEPT.
- CC endoplasmic reticulum membrane GO:0005789 (TAS Reactome): ACCEPT - most specific/correct (membrane-anchored ER protein).
- CC intracellular membrane-bounded organelle GO:0043231 (TAS PMID:8075637): MODIFY -> ER (GO:0005783); overly general given known ER localization.

## Core functions
- MF GO:0047045 testosterone dehydrogenase (NADP+) activity; directly_involved_in GO:0006702 androgen biosynthetic process (+ GO:0061370 testosterone biosynthetic process); located_in GO:0005789 endoplasmic reticulum membrane.
