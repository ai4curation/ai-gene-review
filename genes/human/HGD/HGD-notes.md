# HGD (homogentisate 1,2-dioxygenase) — review notes

UniProtKB: Q93099 (HGD_HUMAN); HGNC:4892; EC 1.13.11.5; 445 aa.

## Core biology (grounding: HGD-uniprot.txt, reactome/R-HSA-71164.md, ~/repos/dismech/kb/disorders/Alkaptonuria.yaml)

- Cytosolic Fe(II)-dependent ring-cleaving dioxygenase; catalyzes the THIRD committed
  step of tyrosine (and, upstream, phenylalanine) catabolism:
  homogentisate + O2 -> 4-maleylacetoacetate + H+ (RHEA:15449, EC 1.13.11.5).
  [UniProt CATALYTIC ACTIVITY; ECO:0000269|PubMed:8782815]
- Cofactor: one Fe cation per monomer (CHEBI:24875). Fe-binding residues His335, Glu341,
  His371. [UniProt COFACTOR/BINDING; ECO:0000269|PubMed:10876237, PDB:1EY2/1EYB]
- Quaternary structure: homohexamer arranged as a dimer of trimers.
  [UniProt SUBUNIT; ECO:0000269|PubMed:10876237]
- Belongs to homogentisate dioxygenase family; cupin/RmlC-like jelly-roll fold
  (Pfam PF04209 HgmA_C, PF20510 HgmA_N; InterPro IPR005708; TIGR01015 hmgA).
- Pathway: UniPathway UPA00139 (L-phenylalanine degradation; acetoacetate and fumarate
  from L-phenylalanine, step 4/6). Reactome R-HSA-8963684 Tyrosine catabolism;
  R-HSA-71164 "HGD dioxygenates homogentisate" (cytosolic).
- Tissue: highest in prostate, small intestine, colon, kidney, liver (HPA: kidney/liver
  enriched).

## Disease
- Alkaptonuria (AKU; MIM:203500; MONDO:0008753), autosomal recessive. Biallelic
  loss-of-function HGD variants -> HGA accumulation -> ochronotic pigment deposition in
  connective tissue -> dark urine, ochronotic arthropathy/spondyloarthropathy, cardiac
  valve and renal disease. Many characterized loss-of-activity variants (e.g. G161R,
  P230S "complete loss", M368V, E168K). Nitisinone inhibits the upstream enzyme HPPD to
  lower HGA production; does not correct HGD deficiency.

## Annotation-by-annotation reasoning

- GO:0004411 homogentisate 1,2-dioxygenase activity (IBA, IEA, IMP PMID:8782815, TAS
  PMID:8782815): CORE MF. ACCEPT all. Directly established biochemically; EC 1.13.11.5;
  RHEA:15449. IMP/8782815 = loss-of-function missense shown biochemically.
- GO:0006559 L-phenylalanine catabolic process (IBA, IEA, TAS PMID:8782815): CORE-ish BP.
  HGD is in the Phe->...->fumarate+acetoacetate subpathway (UPA00139 step 4/6). ACCEPT.
- GO:0006572 L-tyrosine catabolic process (IMP PMID:36555443, TAS PMID:8782815): CORE BP,
  most direct process term (HGA is the tyrosine-catabolism intermediate acted on). ACCEPT.
- GO:0042802 identical protein binding (IPI PMID:25416956; IPI PMID:32296183, with Q93099):
  reflects the homohexamer (self-interaction). Real but not the core function -> KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI PMID:21044950 with TERF1/P54274; IPI PMID:32296183 with
  NTAQ1/Q96HA8): bare "protein binding", uninformative per curation guidelines. These are
  large HT interactome/complementation screens (TERF1 telomere Y2H screen; HuRI binary
  interactome). MARK_AS_OVER_ANNOTATED (do not REMOVE HT-supported IPI; not a core function
  and no informative MF captured). NTAQ1 interaction is also recorded in UniProt INTERACTION.
- GO:0070062 extracellular exosome (HDA PMID:23533145 prostatic-secretion exosomes;
  PMID:19056867 urinary exosomes): HGD is cytosolic; exosome detection is bulk proteomic
  co-purification, not a functional localization. KEEP_AS_NON_CORE (bystander detection).
- GO:0005829 cytosol (TAS Reactome:R-HSA-71164): CORE CC; enzyme is cytosolic. ACCEPT.

## References used
- PMID:8782815 (cloning of HGO=AKU gene; function; catalytic activity) — abstract only in
  cache but is the canonical primary functional reference.
- PMID:36555443 (untargeted NMR metabolomics of AKU; full text) — describes hexameric HGD
  and tyrosine/phenylalanine catabolic role.
- PMID:10876237 (crystal structure, Fe sites, hexamer) — via UniProt, not cited in GOA rows.
- Reactome R-HSA-71164 (cytosolic localization / reaction).
- file: dismech Alkaptonuria.yaml for disease pathophysiology.
