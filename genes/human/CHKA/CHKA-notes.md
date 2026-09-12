# CHKA (Choline kinase alpha) — review notes

UniProt: P35790 (CHKA_HUMAN), 457 aa, gene CHKA (synonyms CHK, CKI). HGNC:1937.
Chromosome 11. EC 2.7.1.32 (choline kinase) and EC 2.7.1.82 (ethanolamine kinase).

## Core biology

CHKA is choline kinase alpha, the enzyme that catalyzes the first committed step
of the CDP-choline (Kennedy) pathway of phosphatidylcholine (PC) biosynthesis:
phosphorylation of choline by ATP to give phosphocholine (+ ADP), Mg2+-dependent.

- "Choline kinase, responsible for the phosphorylation of choline to phosphocholine
  as the first step of the CDP-choline pathway for the biosynthesis of
  phosphatidylcholine, has been recognized as a new target for anticancer therapy."
  [PMID:17007874 "Choline kinase, responsible for the phosphorylation of choline to phosphocholine as the first step of the CDP-choline pathway for the biosynthesis of phosphatidylcholine, has been recognized as a new target for anticancer therapy."]
- The ChoK/EtnK domain "confers the capacity to catalyze the phosphorylation of
  choline (Cho) to phosphocholine (PCho) ... This constitutes the first step in the
  biosynthesis pathway of phosphatidylcholine (PC)."
  [PMID:19915674 "capacity to catalyze the phosphorylation of choline (Cho) to phosphocholine (PCho)"] and
  [PMID:19915674 "first step in the biosynthesis pathway of phosphatidylcholine"]
- UniProt FUNCTION: "Plays a key role in phospholipid biosynthesis by catalyzing the
  phosphorylation of free choline to phosphocholine, the first step in
  phosphatidylcholine biosynthesis." [file:human/CHKA/CHKA-uniprot.txt]

## Ethanolamine kinase activity (secondary)

CHKA also phosphorylates ethanolamine to phosphoethanolamine (EC 2.7.1.82),
contributing to phosphatidylethanolamine (PE) biosynthesis, but choline is the
preferred substrate.

- UniProt FUNCTION: "Also phosphorylates ethanolamine, thereby contributing to
  phosphatidylethanolamine biosynthesis (PubMed:17007874, PubMed:19915674). Has
  higher activity with choline." [file:human/CHKA/CHKA-uniprot.txt]
- ChoKalpha1 shows dual choline/ethanolamine kinase role; Km for ethanolamine
  (12 mM) is far higher than for choline (0.2 mM), i.e. choline is preferred
  [PMID:19915674 "ChoKalpha1 present a dual choline/ethanolamine kinase role"; UniProt kinetics
  KM=12 mM ethanolamine vs 0.2 mM choline, file:human/CHKA/CHKA-uniprot.txt].
- Reactome R-HSA-1483222: CHK dimer (CHKA/CHKB homo- or heterodimer) or ETNK1/2
  phosphorylates ethanolamine to phosphoethanolamine
  [file:reactome/R-HSA-1483222.md].

## Quaternary structure / activity regulation

Homodimer; also forms heterodimer with CHKB. Dimerization is required for
choline/ethanolamine kinase activity.

- UniProt SUBUNIT: "Homodimer (PubMed:17007874, PubMed:20299452, PubMed:34077757).
  Heterodimer with CHKB (By similarity)." [file:human/CHKA/CHKA-uniprot.txt]
- UniProt ACTIVITY REGULATION: "Homodimerization or heterodimerization is required
  for the choline and ethanolamine kinase activities." [file:human/CHKA/CHKA-uniprot.txt]
- protein homodimerization activity annotated IDA from PMID:34077757.

## Structure

Multiple crystal structures (2CKO/2CKP/2CKQ apo/ADP/phosphocholine; 3G15 with
hemicholinium-3; 4DA5). Eukaryotic choline kinase fold (protein-kinase-like fold,
SSF56112; Pfam PF01633 Choline_kinase; CDD cd05156 ChoK_euk). ATP-binding residues
117-123, 146, 207-213, 308, 330; phosphocholine binding 119-121.
An iso double-displacement mechanism via a phospho-enzyme intermediate was proposed
[PMID:23416529 "an iso double displacement mechanism, in which the γ-phosphate from ATP is transferred to choline in two distinct steps via a phospho-enzyme intermediate"].

## Subcellular location

Cytoplasm/cytosol (bulk enzyme). Isoform 1 (CHKalpha2 in some nomenclature; note
UniProt isoform names are inverted vs the paper's) relocalizes to lipid droplets on
glucose deprivation.

- UniProt: "SUBCELLULAR LOCATION: Cytoplasm, cytosol." [file:human/CHKA/CHKA-uniprot.txt]
- Isoform 1: "SUBCELLULAR LOCATION: [Isoform 1]: Lipid droplet ... Isoform 1
  localizes to lipid droplets following phosphorylation by AMPK."
  [file:human/CHKA/CHKA-uniprot.txt]

## Moonlighting protein-tyrosine kinase (isoform 1, cancer context)

On glucose deprivation, AMPK phosphorylates CHKalpha2/isoform-1 at Ser279 -> lipid
droplet localization -> KAT5 acetylation at Lys247 -> monomerization -> the monomer
converts into a protein-tyrosine kinase that phosphorylates PLIN2 (Y232) and PLIN3
(Y251), promoting lipid droplet lipolysis, fatty-acid oxidation, and glioblastoma
growth.

- [PMID:34077757 "glucose deprivation induces the binding of choline kinase (CHK) α2 to lipid droplets, which is sequentially mediated by AMPK-dependent CHKα2 S279 phosphorylation and KAT5-dependent CHKα2 K247 acetylation. Importantly, CHKα2 with altered catalytic domain conformation functions as a protein kinase and phosphorylates PLIN2 at Y232 and PLIN3 at Y251."]
- This is a moonlighting/isoform-specific activity, distinct from the canonical
  small-molecule choline kinase function; treated as non-core.

## Disease / cancer

- Frequently over-expressed / up-regulated in cancers (breast, lung, colon,
  glioblastoma); oncometabolic drug target (hemicholinium-3, MN58b inhibitors).
  [PMID:23416529 "ChoKα is frequently up-regulated in human cancers, and expression of ChoKα is sufficient to transform cells."]
  [PMID:10363580 "Both choline kinase activity and phosphocholine levels were increased in colon cancer and adenoma tissue."]
- Bi-allelic loss-of-function variants cause an autosomal-recessive
  neurodevelopmental disorder with epilepsy and microcephaly (NEDMIMS, MIM 620023);
  variants reduce choline kinase activity.
  [PMID:35202461 "we determined that these variants reduce the enzymatic activity of CHKA and confer a significant impairment of the first enzymatic step of the Kennedy pathway."]

## Annotation review decisions (summary)

- choline kinase activity (GO:0004103): CORE MF. Multiple EXP/IDA (17007874,
  35202461, 23416529, 34077757, 19915674) + TAS (10363580) + IBA + IEA. ACCEPT.
- ethanolamine kinase activity (GO:0004305): real but secondary (choline preferred).
  EXP 17007874, IDA 19915674, IBA, IEA. ACCEPT (kept, choline preferred).
- ATP binding (GO:0005524): not in GOA TSV (only UniProt DR KW) — added to
  core_functions as a molecular function underpinning catalysis (BINDING residues
  in UniProt FT).
- PC biosynthetic process (GO:0006656): CORE BP. IDA×3 + IEA. ACCEPT.
- CDP-choline pathway (GO:0006657): CORE BP (more specific). IBA. ACCEPT.
- PE biosynthetic process (GO:0006646): secondary BP. IBA/IEA/IDA. KEEP_AS_NON_CORE.
- cytosol (GO:0005829): ACCEPT (IDA 34077757 + IEA + Reactome TAS).
- cytoplasm (GO:0005737): IBA, less specific than cytosol. KEEP_AS_NON_CORE.
- lipid droplet (GO:0005811): isoform-1 specific, EXP 34077757 + IEA. KEEP_AS_NON_CORE.
- protein tyrosine kinase activity (GO:0004713): isoform-1 moonlighting, EXP 34077757
  + IEA(Rhea). KEEP_AS_NON_CORE.
- protein homodimerization activity (GO:0042803): IDA 34077757; required for kinase
  activity. ACCEPT (non-core structural MF).
- lipid metabolic process (GO:0006629): TAS 10363580, too general. KEEP_AS_NON_CORE.
- lipid transport (GO:0006869): TAS 10363580. CHKA is a kinase, not a lipid
  transporter; abstract does not support transport. MARK_AS_OVER_ANNOTATED.

## Nomenclature caution

The two UniProt isoforms are named counter-intuitively relative to the Liu et al.
2021 paper: UniProt isoform 1 (P35790-1, displayed) is called "CHKalpha2/alpha-2",
and isoform 2 (P35790-2) is "CHKalpha1/alpha-1". The Liu et al. (PMID:34077757)
"CHKα2" moonlighting protein-kinase corresponds to UniProt isoform 1.
