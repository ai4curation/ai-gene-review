# HMGCS1 (Q01581) review notes

Human hydroxymethylglutaryl-CoA synthase, cytoplasmic (HGNC:5007). EC 2.3.3.10.
Deep research via falcon was unavailable (provider out of credits, HTTP 402); this
review is grounded in the cached UniProt record, the seeded GOA, and cached
`publications/PMID_*.md` and `reactome/*.md`.

## Core biology (provenance)

- Function: condenses acetyl-CoA + acetoacetyl-CoA (+ H2O) to form (3S)-HMG-CoA + CoA,
  the first committed / second step of the cytosolic **mevalonate pathway** that
  feeds isoprenoid and **cholesterol** biosynthesis. HMG-CoA is subsequently reduced
  by HMGCR to mevalonate.
  - [file:human/HMGCS1/HMGCS1-uniprot.txt "Catalyzes the condensation of acetyl-CoA with acetoacetyl-CoA to form HMG-CoA, which is converted by HMG-CoA reductase (HMGCR) into mevalonate, a precursor for cholesterol synthesis."]
  - CATALYTIC ACTIVITY: RHEA:10188, EC=2.3.3.10 (acetoacetyl-CoA + acetyl-CoA + H2O = (3S)-3-hydroxy-3-methylglutaryl-CoA + CoA + H+).
  - PATHWAY: "(R)-mevalonate from acetyl-CoA: step 2/3." (UniPathway UPA00058, UER00102).
  - [PMID:20346956 abstract "The eukaryotic cytosolic isoform also participates in the mevalonate pathway but its end product is cholesterol."] — distinguishes HMGCS1 (cytosolic, cholesterol) from HMGCS2 (mitochondrial, ketogenesis).
  - [reactome:R-HSA-191323 "The cytosolic form of 3-hydroxy-3-methylglutaryl Coenzyme A synthase (HMGCS1) catalyzes the condensation of acetyl CoA with acetoacetyl CoA to produce HMG-CoA. HMGCS1 is ubiquitously expressed in the body and is involved in synthesis of isoprenoids and cholesterol biosynthesis (Rokosz et al. 1994)."]

- Distinct from mitochondrial HMGCS2 (P54868), which makes HMG-CoA for ketone body
  synthesis (ketogenesis). Both are in the same PANTHER family (PTHR43323); HMGCS1 =
  subfamily SF4 (cytoplasmic).

- Catalytic mechanism: Cys129 is the active-site nucleophile forming the acetyl-thioester
  intermediate. Cys129Ala/Ser abolishes activity.
  - [PMID:7913309 abstract "Mutation of Cys129 to serine or alanine destroys HMG-CoA synthase activity by disrupting the first catalytic step in HMG-CoA synthesis, enzyme acetylation by acetyl coenzyme A."]
  - UniProt ACT_SITE 129 "Acyl-thioester intermediate"; MUTAGEN 129 "C->A,S: Loss of activity."

- Quaternary structure: homodimer (crystal structure 2P8U, thiolase-like fold).
  - [PMID:20346956 abstract "we report high-resolution crystal structures of the human cytosolic (hHMGCS1) and mitochondrial (hHMGCS2) isoforms in binary product complexes."]
  - UniProt SUBUNIT "Homodimer."

- Localization: cytoplasm / cytosol.
  - [file:human/HMGCS1/HMGCS1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]
  - HPA IDA GO:0005829 cytosol; Reactome cytosol.

- Regulation: SREBP-regulated cholesterogenic gene (UniProt DR Reactome R-HSA-2426168
  "Activation of gene expression by SREBF (SREBP)"; also R-HSA-1989781 PPARA target).

- Disease: biallelic HMGCS1 variants cause congenital myopathy 28 with rigid spine
  (CMYO28); rescuable with mevalonic acid in a zebrafish model. Highly expressed in
  cerebral cortex.
  - [file:human/HMGCS1/HMGCS1-uniprot.txt "HMGCS1 variants cause rigid spine syndrome amenable to mevalonic acid treatment"] (PMID:39531736; not cached as full text)

## Annotation-specific notes

- IPI `protein binding` (GO:0005515) x2 (PMID:28514442 BioPlex 2.0; PMID:33961781
  BioPlex 3.0): both are large-scale AP-MS interactome screens. Per curation policy,
  bare `protein binding` -> MARK_AS_OVER_ANNOTATED (uninformative), NOT REMOVE. The
  single UniProt-listed interactor is SLC22A5 (O76082, the WITH/FROM), an OCTN2
  carnitine transporter — not obviously functionally meaningful for a cytosolic
  metabolic enzyme.

- GO:0005886 plasma membrane (IDA, HPA GO_REF:0000052): inconsistent with a soluble
  cytosolic mevalonate-pathway enzyme; likely an HPA antibody-based artifact / non-core.
  MARK_AS_OVER_ANNOTATED (HPA IDA, do not REMOVE experimental).
- GO:0005654 nucleoplasm (IDA, HPA): similarly non-core; MARK_AS_OVER_ANNOTATED.
- GO:0016746 acyltransferase activity (IEA InterPro IPR016039 Thiolase-like): correct
  but a very general parent of the specific HMG-CoA synthase activity. MODIFY ->
  GO:0004421.
- GO:0006084 acetyl-CoA metabolic process (IBA + IEA): acetyl-CoA is a substrate;
  accurate but generic/non-core relative to the cholesterol/mevalonate role. ACCEPT
  IBA (phylogenetically reviewed); KEEP_AS_NON_CORE.
- GO:0006629 lipid metabolic process (NAS, ProtInc): very general; the specific
  cholesterol/mevalonate terms are better. MARK_AS_OVER_ANNOTATED (too general).
- PMID:7911016 (IC for GO:0006695): this cited paper is actually about cytosolic
  acetoacetyl-CoA thiolase (ACAT2), the enzyme immediately upstream of HMGCS1; the
  annotation is IC (inferred by curator from GO:0004421). The cholesterol biosynthetic
  process conclusion is correct for HMGCS1, so ACCEPT the term, but flag the reference
  choice in reference_review (MISCITED wrt this gene).
