# PHGDH (human) — gene review notes

UniProt: O43175 (SERA_HUMAN). Gene symbol PHGDH (HGNC:8923); synonym PGDH3. 533 aa.
Taxon: Homo sapiens (NCBITaxon:9606).

## Core identity and function

PHGDH is **D-3-phosphoglycerate dehydrogenase** (3-PGDH; EC 1.1.1.95), the first and
rate-limiting enzyme of the phosphorylated pathway of de novo L-serine biosynthesis.
It catalyzes the NAD+-dependent oxidation of 3-phospho-D-glycerate (a glycolytic
intermediate) to 3-phosphonooxypyruvate (3-phosphohydroxypyruvate).

- UniProt FUNCTION: "Catalyzes the reversible oxidation of 3-phospho-D-glycerate to
  3-phosphonooxypyruvate, the first step of the phosphorylated L-serine biosynthesis
  pathway." [file:human/PHGDH/PHGDH-uniprot.txt CC FUNCTION]
- UniProt PATHWAY: "Amino-acid biosynthesis; L-serine biosynthesis; L-serine from
  3-phospho-D-glycerate: step 1/3." [file:human/PHGDH/PHGDH-uniprot.txt]
- Catalytic activity (Rhea RHEA:12641, EC 1.1.1.95):
  "(2R)-3-phosphoglycerate + NAD(+) = 3-phosphooxypyruvate + NADH + H(+)"
  [file:human/PHGDH/PHGDH-uniprot.txt CC CATALYTIC ACTIVITY], evidence
  ECO:0000269|PubMed:11751922.
- Belongs to the D-isomer specific 2-hydroxyacid dehydrogenase family
  [file:human/PHGDH/PHGDH-uniprot.txt CC SIMILARITY]. Homotetramer (SUBUNIT).
- Cofactor: NAD+ (multiple BINDING sites 78, 155-156, 175, 207, 234-236, 260, 283-286;
  KW NAD; DrugBank NADH). Active sites at His236/Glu265/His283-region.

## Secondary (moonlighting / side) activities

Human PHGDH also has demonstrated secondary NAD+-dependent 2-hydroxyacid dehydrogenase
side-activities, established biochemically:
- 2-oxoglutarate reductase (EC 1.1.1.399): "(R)-2-hydroxyglutarate + NAD(+) = 2-oxoglutarate
  + NADH + H(+)" [file:human/PHGDH/PHGDH-uniprot.txt], evidence ECO:0000269|PubMed:25406093.
  This is the basis of PHGDH producing the oncometabolite D-2-hydroxyglutarate
  (Fan et al. 2015, ACS Chem Biol; PubMed:25406093 — "Human phosphoglycerate dehydrogenase
  produces the oncometabolite D-2-hydroxyglutarate"). GOA has the reverse-direction MF
  GO:0120568 (R)-2-hydroxyglutarate (NAD+) dehydrogenase activity as IEA from EC:1.1.1.399.
- Malate dehydrogenase (EC 1.1.1.37): "(S)-malate + NAD(+) = oxaloacetate + NADH + H(+)"
  [file:human/PHGDH/PHGDH-uniprot.txt], evidence ECO:0000269|PubMed:25406093. GOA has
  GO:0030060 L-malate dehydrogenase (NAD+) activity IEA from EC:1.1.1.37.

These side-activities are catalytically minor relative to the physiological 3-PGDH
reaction (kcat 4.5/min for 3PG oxidation vs 4.7/min for 2-OG reduction, 10.6/min for OAA
reduction; but the physiological pathway role is serine biosynthesis)
[file:human/PHGDH/PHGDH-uniprot.txt CC BIOPHYSICOCHEMICAL PROPERTIES]. Treated as
non-core moonlighting activities in this review; the malate-DH assignment in particular is
in-vitro promiscuity, not a described physiological role.

## Localization

Cytosolic enzyme. GOA: cytosol GO:0005829 (TAS Reactome:R-HSA-977348).
UniProt DR lists C:cytosol TAS:Reactome. Also repeatedly detected in extracellular exosome
proteomics (GO:0070062, four HDA annotations from PMID:23533145, 19199708, 19056867,
20458337) — a common non-specific finding for abundant cytosolic metabolic enzymes; kept
as non-core.

## Biological process / disease

- L-serine biosynthetic process GO:0006564 is the core BP.
- Loss-of-function → **3-phosphoglycerate dehydrogenase deficiency (PHGDHD; MIM 601815)**,
  an autosomal recessive inborn error of serine biosynthesis: congenital microcephaly,
  psychomotor retardation, seizures [file:human/PHGDH/PHGDH-uniprot.txt CC DISEASE].
  Original description Jaeken et al. 1996 [PMID:8758134 "a decreased activity was
  demonstrated of 3-phosphoglycerate dehydrogenase, the first step of serine biosynthesis"].
- More severe biallelic LOF → **Neu-Laxova syndrome 1 (NLS1; MIM 256520)**, a lethal
  multiple-malformation syndrome (Shaheen et al. 2014, PubMed:24836451, cited by UniProt).
- PHGDH is amplified/overexpressed in a subset of cancers (melanoma, breast) where de novo
  serine synthesis supports proliferation (context; not directly in cached pubs).
- Haploinsufficiency implicated in macular telangiectasia type 2 (MacTel) retinal disease
  [PMID:33758422].

## Provenance for GO-relevant experimental annotations

- **GO:0004617 phosphoglycerate dehydrogenase activity, IMP, PMID:33758422** (assigned by
  FlyBase; ECO:0000315). The paper functionally assays human PHGDH enzymatic activity of
  patient/engineered variants: "Enzyme activity was determined using 3-phosphoglycerate as
  a substrate and monitoring the reduction of the cofactor NAD+ to NADH." and "All but one
  tested variants reduced PHGDH activity". Supports the MF for human PHGDH (loss of activity
  by mutation = IMP). [PMID:33758422, full_text_available: true]
- **GO:0006564 L-serine biosynthetic process, IMP, PMID:33758422**. Same paper shows the
  variant reduces serine synthesis flux: "13C abundance of both serine and glycine was
  significantly reduced in p.Gly228TrpHet RPE, indicating decreased synthesis of
  serine/glycine via PHGDH" and "35% decrease in serine abundance in RPE and a 58% decrease
  in the secretory flux of serine". Supports the BP. [PMID:33758422]
- **GO:0004617 / GO:0009055 / GO:0007420, TAS, PMID:8758134**. This is the Jaeken 1996
  clinical/biochemical description of 3-PGDH deficiency (abstract-only cache;
  full_text_available: false). The abstract supports 3-PGDH activity ("a decreased activity
  was demonstrated of 3-phosphoglycerate dehydrogenase, the first step of serine
  biosynthesis") and the brain/serine-deficiency link (microcephaly, dysmyelination),
  hence brain development TAS is defensible but non-core (downstream phenotype, not the
  molecular function). It does NOT support electron transfer activity (GO:0009055) — that
  IEA/TAS assignment appears to be a legacy mis-mapping (a dehydrogenase transferring
  hydride to NAD+ is not an "electron transfer activity" carrier in the GO sense; that
  branch is for electron transport chain carriers). Marked as over-annotation, not removed
  (TAS on an experimental disease paper).

## Protein-binding IPI annotations (all WITH/FROM UniProtKB:Q9Y6I3 = EPN1)

Three GO:0005515 "protein binding" IPI annotations, all from high-throughput
interactome/proteostasis screens, all listing partner Q9Y6I3 (EPN1, epsin-1):
- PMID:25036637 (Taipale 2014, chaperone/co-chaperone interaction network, LUMIER/AP-MS).
- PMID:33961781 (Huttlin 2021, BioPlex 3.0 dual proteome-scale AP-MS network).
- PMID:35271311 (Cho 2022, OpenCell endogenous-tagging spatial/interaction map).
UniProt records the EPN1 interaction (IntAct EBI-350495, EBI-713198; NbExp=5). Bare
"protein binding" is uninformative for molecular function; per policy these IPI annotations
are MARK_AS_OVER_ANNOTATED (not removed) and excluded from core_functions. No specific,
functionally meaningful complex is established for PHGDH from these screens.

## Summary of core functions

1. Molecular function: phosphoglycerate dehydrogenase activity (GO:0004617), with NAD
   binding (GO:0051287) as cofactor requirement.
2. Biological process: L-serine biosynthetic process (GO:0006564).
3. Location: cytosol (GO:0005829).

Non-core / moonlighting: (R)-2-hydroxyglutarate (NAD+) dehydrogenase (GO:0120568,
D-2-HG production), L-malate dehydrogenase (GO:0030060, in-vitro promiscuity),
extracellular exosome localization, brain development (downstream phenotype).
