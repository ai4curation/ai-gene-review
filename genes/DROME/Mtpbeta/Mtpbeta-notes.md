# Mtpbeta (Q9W1H8; CG4581; dHADHB) research notes

Drosophila melanogaster gene Mtpbeta / FBgn0025352 / CG4581, the fly ortholog of human
HADHB. UniProt entry is unreviewed TrEMBL (Q9W1H8_DROME), RecName acetyl-CoA
C-acyltransferase, EC 2.3.1.16.

## Identity / orthology

- FlyBase symbol Mtpbeta (Mtpβ), synonyms ACoT, dHADHB, Dmel\CG4581, l(2)k09828, MTP,
  Thiolase. FlyBase FBgn0025352. RefSeq NP_477378.1. Chromosome 2R.
- Single-copy fly ortholog of human HADHB (P55084). eggNOG KOG1392; PANTHER
  PTHR18919:SF153 "TRIFUNCTIONAL ENZYME SUBUNIT BETA, MITOCHONDRIAL"
  [genes/DROME/Mtpbeta/Mtpbeta-uniprot.txt line 222].
- WebSearch (NCBI Gene 37784; FlyBase FBgn0025352): "The Drosophila genome carries the
  dHADHB (CG4581) gene as a single orthologue of the human HADHB gene."

## Domain / family

- Belongs to the thiolase-like superfamily, thiolase family
  [uniprot.txt lines 171-172 "Belongs to the thiolase-like superfamily. Thiolase family."].
- Thiolase N-terminal domain (PF00108, aa 44-315) + Thiolase C-terminal (PF02803, aa 322-462)
  [uniprot.txt lines 238-243]. CDD cd00751 thiolase; PROSITE THIOLASE_1/2/3.
- 469 aa, 50.6 kDa; predicted N-terminal mitochondrial targeting extension (the mature
  MTP beta is imported into mitochondria).

## Molecular function

- Provides the long-chain 3-ketoacyl-CoA thiolase (acetyl-CoA C-acyltransferase,
  EC 2.3.1.16) activity of the mitochondrial trifunctional protein (MTP), the alpha2beta2
  heterotetramer with Mtpalpha (fly ortholog of HADHA). By analogy with human HADHB
  (PMID:8135828, human), the beta subunit carries ONLY the thiolase activity; the hydratase
  and 3-hydroxyacyl-CoA dehydrogenase activities reside in the alpha subunit.
- UniProt RecName / EC: "acetyl-CoA C-acyltransferase ... EC=2.3.1.16"
  [uniprot.txt lines 6-7]. Note GOA also carries an EC-mapping IEA to
  GO:0003985 (acetyl-CoA C-acetyltransferase, EC 2.3.1.9) — this is the shorter-chain
  homolog activity and reflects EC/InterPro cross-mapping breadth of the thiolase family
  rather than the specific long-chain function; GO:0003988 (acetyl-CoA C-acyltransferase,
  EC 2.3.1.16) is the more accurate MF for the MTP beta subunit.

## Biological process / pathway

- UniProt PATHWAY: "Lipid metabolism; fatty acid beta-oxidation."
  [uniprot.txt lines 168-169]. Reactome R-DME-77285/77305/77310/77346/77348/77350
  (beta oxidation of acyl-CoAs) and R-DME-1482798 (acyl chain remodeling of CL)
  [uniprot.txt lines 193-199].
- Direct fly genetic evidence for beta-oxidation function:
  [PMID:22342726 Kishita et al 2012, "Both Mtpα(KO) and Mtpβ(KO) flies were viable, but
  demonstrated reduced lifespan, defective locomotor activity, and reduced fecundity"]
  and [PMID:22342726 "both Mtpα(KO) and Mtpβ(KO) flies accumulated acylcarnitine and
  hydroxyacylcarnitine, diagnostic markers of MTP deficiencies in humans. Our results
  indicated that both Mtpα(KO) and Mtpβ(KO) flies were impaired in long-chain fatty acid
  β-oxidation."]. This is the basis of the IMP GO:0006635 annotation (FlyBase).
  Paper is abstract-only in cache (full_text_available: false).

## Subcellular localization

- UniProt SUBCELLULAR LOCATION: "Mitochondrion" [uniprot.txt line 170].
- HDA GO:0005739 mitochondrion from LOPIT organelle-proteomics of Drosophila embryos
  [PMID:19317464 Tan et al 2009, "we apply LOPIT, a mass-spectrometry based technique that
  simultaneously maps proteins to specific subcellular compartments, to Drosophila embryos.
  We determine the subcellular distribution of hundreds of proteins, and protein
  complexes."]. Abstract-only; the specific Mtpbeta assignment is in the full dataset,
  not the abstract.
- ISM GO:0005739 mitochondrion from a Drosophila peroxisome-inventory bioinformatics
  survey [PMID:22758915 Faust et al 2012], which predicted subcellular localizations
  from targeting signals. Abstract-only. (This study is about peroxisomes; the mitochondrion
  prediction for Mtpbeta is a by-product of the proteome-wide localization prediction.)
- By strong orthology to human HADHB the functional pool is the mitochondrial inner
  membrane as part of the membrane-associated MTP complex, but the fly annotations only
  assert the general "mitochondrion" compartment.

## Additional fly phenotype literature (not in GOA; notes only)

- Neuron-specific dHADHB knockdown: [PMID:30953623 Kishita/Aigaki et al 2019,
  "Neuron-specific knockdown of Drosophila HADHB induces a shortened lifespan, deficient
  locomotive ability, abnormal motor neuron terminal morphology and learning disability"
  — title from PubMed via WebSearch]. Pan-neuronal dHADHB knockdown shortened lifespan,
  reduced locomotor/learning ability, caused abnormal NMJ synapse morphology and reduced
  CNS ATP/ROS. This paper is the likely basis of the FlyBase IMP GO:0008340 "determination
  of adult lifespan" annotation that appears in the UniProt GO cross-refs (uniprot.txt
  line 208). NOTE: that GO:0008340 annotation is NOT present in the QuickGO goa.tsv export
  used to seed this review, and PMID:30953623 is not cached in publications/, so it is not
  reviewed as an existing_annotation here. Recorded for context / suggested follow-up.

## Annotation-review reasoning summary

- Core MF: acetyl-CoA C-acyltransferase / 3-ketoacyl-CoA thiolase activity (GO:0003988,
  EC 2.3.1.16). GO:0003985 (C-acetyltransferase, EC 2.3.1.9) is a closely related family
  activity captured by EC/PANTHER phylogenetic mapping; keep as non-core (the precise
  long-chain activity is GO:0003988).
- Core BP: fatty acid beta-oxidation (GO:0006635) — supported experimentally in fly
  (PMID:22342726 IMP) and by IBA.
- Core CC/complex: mitochondrial fatty acid beta-oxidation multienzyme complex
  (GO:0016507, MTP) — IBA + ISS from human HADHB (P55084). General mitochondrion
  (GO:0005739) kept as non-core (less specific).
- Broad IEA transferase parents (GO:0016746, GO:0016747) and the oxidoreductase keyword
  term: keep as non-core (uninformative parents) — note GO:0016491 oxidoreductase from
  UniProtKB-KW appears in uniprot.txt line 207 but is NOT in goa.tsv, so not reviewed.
</content>
