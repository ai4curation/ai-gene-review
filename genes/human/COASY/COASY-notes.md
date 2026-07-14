# COASY (Q13057) — gene review notes

## Identity
- UniProt Q13057, HGNC:29932, human, 564 aa, chromosome 17q21.2.
- Names: Bifunctional coenzyme A synthase / CoA synthase; NBP; POV-2.
- Two enzymatic activities are captured in the UniProt "Includes:" blocks:
  - Phosphopantetheine adenylyltransferase (PPAT), EC 2.7.7.3
    [file:human/COASY/COASY-uniprot.txt "RecName: Full=Phosphopantetheine adenylyltransferase"]
  - Dephospho-CoA kinase (DPCK), EC 2.7.1.24
    [file:human/COASY/COASY-uniprot.txt "RecName: Full=Dephospho-CoA kinase"]

## Core biology
COASY catalyses the last two (fourth and fifth) steps of the five-step coenzyme A
biosynthetic pathway that converts pantothenate (vitamin B5) into CoA:
- Step 4 (PPAT domain): (R)-4'-phosphopantetheine + ATP -> 3'-dephospho-CoA + diphosphate
  [file:human/COASY/COASY-uniprot.txt "Reaction=(R)-4'-phosphopantetheine + ATP + H(+) = 3'-dephospho-CoA +"]
- Step 5 (DPCK domain): 3'-dephospho-CoA + ATP -> CoA + ADP
  [file:human/COASY/COASY-uniprot.txt "Reaction=3'-dephospho-CoA + ATP = ADP + CoA + H(+);"]

UniProt FUNCTION: "Bifunctional enzyme that catalyzes the fourth step of the coenzyme A
biosynthetic pathway, the adenylation of 4'-phosphopantetheine, and the fifth step, the
phosphorylation of dephospho-CoA to CoA."
[file:human/COASY/COASY-uniprot.txt]

Domain architecture (from UniProt FT lines): the PPAT (adenylyltransferase) domain sits in
the central region (~180-358) and the DPCK domain in the C-terminus (~360-563). Both
domains and both catalytic activities were reconstituted / verified biochemically for the
recombinant human protein.

## Key primary experimental support for the two MFs
- Daugherty et al. 2002 (PMID:11923312): identified the human genes for the last four CoA
  pathway steps by comparative genomics; overexpressed and purified the recombinant human
  bifunctional PPAT/DPCK, kinetically characterized it, and reconstituted the whole pathway
  in vitro. "Human recombinant bifunctional phosphopantetheine
  adenylyltransferase/dephospho-CoA kinase was kinetically characterized."
  [PMID:11923312] — GOA uses this for IDA on GO:0004595, GO:0004140, GO:0015937.
- Aghajanian & Worrall 2002 (PMID:11994049): cloned the human gene; "The recombinant
  564-amino-acid human protein confirmed the associated transferase and kinase activities,
  and gave similar kinetic properties to the wild-type pig enzyme."
  [PMID:11994049] — GOA uses this for IDA on GO:0004595 and GO:0004140; also SUBUNIT=Monomer.
- Dusi et al. 2014 (PMID:24360804): NBIA disease paper; also re-verified both catalytic
  activities (EXP on GO:0004595 and GO:0004140) and characterized loss-of-function disease
  variants. The R499C variant causes "loss of dephospho-CoA kinase activity"
  [file:human/COASY/COASY-uniprot.txt].
  Abstract: "CoA synthase is a bifunctional enzyme catalyzing the final steps of CoA
  biosynthesis by coupling phosphopantetheine with ATP to form dephospho-CoA and its
  subsequent phosphorylation to generate CoA." [PMID:24360804]

Both catalytic MFs therefore have multiple independent experimental (IDA/EXP) supports and
are unambiguously CORE.

## Localization — genuinely unsettled in the literature
- UniProt SUBCELLULAR LOCATION: "Cytoplasm, cytosol ... Mitochondrion matrix ... Note=The
  protein is mainly cytosolic and active in the cytosol (PubMed:40925986). Present in the
  mitochondrial matrix, probably anchored to the inner mitochondrial membrane
  (PubMed:24360804)." [file:human/COASY/COASY-uniprot.txt]
- Reactome (R-HSA-196754, R-HSA-196773): places the enzyme at the "mitochondrial outer
  membrane (Zhyvoloup et al. 2003)." So GOA carries mitochondrial outer membrane (TAS,
  Reactome), mitochondrial matrix (IDA, PMID:24360804 and IEA SubCell), mitochondrion (IDA,
  HPA / HTP), and cytosol (IDA/IEA). The exact membrane/compartment (outer membrane vs inner
  membrane vs matrix) is not consistent across sources.
- Liu et al. 2025 (PMID:40925986): pan-chain acyl-CoA profiling. Concludes "Despite a small
  fraction of the mitochondria-localized CoA synthase COASY, de novo CoA biosynthesis is
  primarily cytosolic and supports cytosolic lipid anabolism." [PMID:40925986]
  So the dominant, functionally-active pool is CYTOSOLIC; a minor pool is mitochondrial.
  This paper is the basis for the is_active_in cytosol (IDA) annotation.

Interpretation for the review: the cytosol is where the bulk of de novo CoA synthesis
occurs (core location); a minor mitochondrial pool exists. The mitochondrial annotations are
kept but not all treated as core; the mitochondrial-outer-membrane Reactome placement is
inconsistent with the newer matrix/cytosol data but comes from experimental TAS and is
retained (KEEP_AS_NON_CORE), not removed.

## Interactions (protein binding IPI/IEA)
- EDC4 (PMID:22982864): "CoAsy forms a complex with enhancer of mRNA-decapping protein 4
  (EDC4) ... EDC4 strongly inhibits the dephospho-CoA kinase activity of CoAsy in vitro."
  [PMID:22982864] Regulatory interaction — a real, functionally meaningful partner, but the
  bare GO:0005515 "protein binding" term is uninformative; kept as MARK_AS_OVER_ANNOTATED
  (never removed per policy; more informative would be an enzyme-regulator / negative
  regulation of kinase activity relationship).
- CFTR (PMID:35156780 membrane two-hybrid screen; PMID:36012204 proximity-labeling): COASY
  appears as a CFTR interactor in high-throughput CFTR interactome screens. These are
  bare "protein binding" IPI annotations of uncertain biological significance for COASY's
  own function; MARK_AS_OVER_ANNOTATED.

## Disease
- Neurodegeneration with brain iron accumulation 6 (NBIA6) / COASY protein-associated
  neurodegeneration (CoPAN); MIM 615643. Dusi et al. 2014 (PMID:24360804); Evers et al. 2017
  (PMID:28489334). [file:human/COASY/COASY-uniprot.txt]
- Pontocerebellar hypoplasia 12 (PCH12); MIM 618266. van Dijk et al. 2018 (PMID:30089828);
  biallelic loss-of-function. [file:human/COASY/COASY-uniprot.txt]
These are downstream phenotypes of impaired CoA biosynthesis, not separate molecular
functions.

## Other
- Monomer (SUBUNIT, PMID:11994049). [file:human/COASY/COASY-uniprot.txt]
- Phosphoserine at S178 and S183 (large-scale phosphoproteomics) — regulatory PTMs, no GO
  annotation implication here.
- Extracellular exosome (GO:0070062, HDA, PMID:19056867): urinary-exosome mass-spec catch;
  not a site of function. KEEP_AS_NON_CORE (large-scale HDA localization, standard for the
  proteome; not removed).

## Core function conclusion
Two catalytic molecular functions, both experimentally established, both core:
- GO:0004595 pantetheine-phosphate adenylyltransferase activity (PPAT / step 4)
- GO:0004140 dephospho-CoA kinase activity (DPCK / step 5)
Core biological process: GO:0015937 coenzyme A biosynthetic process.
Primary location: cytosol (GO:0005829), with a minor mitochondrial pool.
