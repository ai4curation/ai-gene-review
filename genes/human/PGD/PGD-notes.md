# PGD (6-phosphogluconate dehydrogenase, decarboxylating) — review notes

UniProtKB: P52209 (6PGD_HUMAN), gene PGD (HGNC:8891), EC 1.1.1.44, 483 aa.

## Core biology
PGD is the **third enzyme** of the oxidative pentose phosphate pathway (oxiPPP) and its
**second NADPH-producing step**. It catalyses the oxidative decarboxylation of
6-phospho-D-gluconate to D-ribulose-5-phosphate + CO2, reducing NADP+ to NADPH.

- UniProt FUNCTION: "Catalyzes the oxidative decarboxylation of 6-phosphogluconate to
  ribulose 5-phosphate and CO(2), with concomitant reduction of NADP to NADPH."
  [file:human/PGD/PGD-uniprot.txt]
- CATALYTIC ACTIVITY (RHEA:10116, EC 1.1.1.44): "Reaction=6-phospho-D-gluconate + NADP(+)
  = D-ribulose 5-phosphate + CO2 + NADPH" [file:human/PGD/PGD-uniprot.txt]
- PATHWAY: "Carbohydrate degradation; pentose phosphate pathway; D-ribulose 5-phosphate
  from D-glucose 6-phosphate (oxidative stage): step 3/3." [file:human/PGD/PGD-uniprot.txt]
- SUBUNIT: Homodimer (PDB 2JKV, 4GWG, 4GWK, 5UQ9). NADP+ binding site is shared between
  dimeric partners. [file:human/PGD/PGD-uniprot.txt]
- SUBCELLULAR LOCATION: Cytoplasm/cytosol. [file:human/PGD/PGD-uniprot.txt]

The product ribulose-5-phosphate feeds the non-oxidative PPP, ultimately supplying
ribose-5-phosphate for nucleotide biosynthesis; NADPH supports reductive biosynthesis and
antioxidant (glutathione/thioredoxin) systems.

## Literature supporting function
- PMID:3965621 (Weisz et al. 1985): purified human brain 6PGD; kinetic mechanism with
  NADP+/6-phosphogluconate; products CO2, ribulose 5-phosphate, NADPH. Supports the
  catalytic MF (GO:0004616), IDA. Abstract-only cache; experimental annotation.
- PMID:23153533 (Hitosugi et al. 2012): recombinant human 6PGD assayed; 3-PG competitively
  inhibits 6PGD ("an enzyme that also produces NADPH while converting 6-phosphogluconate
  into ribulose 5-phosphate in the presence of NADP+"). Crystal structures of apo- and
  3-PG-bound 6PGD (1.39/1.53 Å). Supports GO:0004616 (IDA).
- PMID:31586547 (Gao et al. 2019): 6PGD is "the third oxiPPP enzyme"; its product Ru-5-P
  inhibits LKB1-AMPK. 6PGD knockdown (IMP) reduces oxiPPP flux, NADPH and Ru-5-P; supports
  involvement in oxidative branch of PPP (GO:0009051), acts_upstream_of_or_within.

## Localization over-annotations (proteomics HDA)
PGD is an abundant cytosolic housekeeping enzyme. HDA mass-spec detections in:
- extracellular exosome GO:0070062 (PMID:23533145 prostatic-secretion exosomes;
  PMID:19056867 urinary exosomes; PMID:20458337 B-cell exosomes) — abstract-only; PGD not
  named in abstracts; passenger/contaminant of abundant cytosolic protein in vesicle preps.
- nucleus GO:0005634 (PMID:21630459 sperm nucleus proteome) — abstract-only; PGD not named.
These reflect co-purification in large proteomic datasets, not a distinct biological role.
Marked MARK_AS_OVER_ANNOTATED (protein genuinely detected, location not core biology).
IEA cytoplasm/cytosol (SubCell/Ensembl) and TAS cytosol (Reactome) are correct.

## PMID:3858849 caveat
The IDA on GO:0009051 (oxidative branch of PPP) cites PMID:3858849, which is a study of
**6-phosphogluconolactonase (PGLS/6PGL, EC 3.1.1.31)** deficiency — the *second* oxiPPP
enzyme, not PGD. The paper concerns the oxidative PPP branch broadly (and G6PD interaction)
but is not primarily about PGD. Per curation policy (do not REMOVE experimental
annotations on incomplete evidence, abstract-only cache), left as UNDECIDED: the oxidative-
branch involvement of PGD is well supported by other annotations, but this specific
reference does not clearly assay PGD.

## Weak / broad IEA MF binding terms
- GO:0030246 carbohydrate binding and GO:0031406 carboxylic acid binding (Ensembl IEA):
  these are generic reflections of substrate (6-phospho-D-gluconate, a phosphorylated
  sugar acid) binding, transferred from ortholog. Not informative molecular functions;
  the catalytic MF GO:0004616 captures the real activity. Marked as over-annotated.

## Disease
No common Mendelian disease. Rare partial 6PGD deficiency variants exist but are largely
asymptomatic. PGD is included here as the terminal step of the oxidative PPP for the
metabolic-pathways curation.
