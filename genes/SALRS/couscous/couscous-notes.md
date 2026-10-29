# couscous (Salpingoeca rosetta, F2UJ78, PTSG_07368) — review notes

> Automated deep research was **unavailable** for this gene (no deep-research
> provider API keys in the curation environment). These notes are the reviewer's
> own reading of the cached primary literature in `publications/`. No
> `*-deep-research-*.md` file exists for this gene.

## Identity

- UniProt F2UJ78 (TrEMBL, unreviewed), 866 aa, ORF PTSG_07368, GenBank EGD77026,
  RefSeq XP_004990866 / XM_004990809.
- UniProt name: "Apple domain-containing protein". Domains: PAN/Apple (PF00024,
  PS50948, aa 18-114), PF11051 Mannosyl_trans3 (two hits), InterPro IPR022751
  Alpha_mannosyltransferase, IPR029044 nucleotide-diphospho-sugar transferase fold.
- PANTHER PTHR31646 "ALPHA-1,2-MANNOSYLTRANSFERASE MNN2" (subfamily SF1). The family
  also contains MNN5 (SF6) - i.e. the fungal Mnn2/Mnn5 alpha-1,2-mannosyltransferase
  clade (UniProt: "Belongs to the MNN1/MNT family" via ARBA).
- N-terminus `MARVVGLDVLAPMVLVACSLIAVSVSA` is a short hydrophobic segment: SignalP calls
  a signal peptide (1-27); ARBA calls a type II signal anchor. Unresolved whether it
  is cleaved (secreted/luminal) or retained as a membrane anchor.
- Mutant allele couscous^lw1 was originally named "Branched" in Levin et al. 2014.

## Primary paper: Wetzel et al. 2018 eLife (PMID:30556809, full text cached)

### Phenotype (demonstrated)
- Class C rosette-defect mutant; never forms rosettes, forms amorphous clumps.
  [PMID:30556809 "For this study, we focused on four Class C mutants — Seafoam, Soapsuds, Jumble, and Couscous (previously named Branched in Levin et al., 2014) — that form amorphous, tightly packed clumps of cells, both in the presence and absence of RIFs, but never develop into rosettes"]
- Clumps re-form by aggregation (not division), are shear sensitive; up to 75 cells in
  30 min for Couscous. [PMID:30556809 "Within 30 min after disruption by shear force, cell clumps as large as 75, 55, 32, and 23 cells formed in Couscous, Soapsuds, Seafoam, and Jumble mutant cultures, respectively."]
- Mutant cells also stick to wild-type cells. [PMID:30556809 "Cell aggregation was not strain-specific, as unlabeled Jumble and Couscous mutant cells adhered to wild type cells identified by their expression of cytoplasmic mWasabi"]

### Mapping and rescue (demonstrated)
- Single-nucleotide deletion on supercontig 22, frameshift -> early stop.
  [PMID:30556809 "The mutation causes a predicted frameshift leading to an early stop codon in the mutant protein, Couscouslw1"]
- Transgenic rescue with couscous-mTFP or mTFP-couscous (not mutant allele or mTFP).
  [PMID:30556809 "Rosette formation in Couscous mutant cells can be rescued by transgenic expression of couscous-mTFP or mTFP-couscous, but not couscouslw1-mTFP, mTFP-couscouslw1, or mTFP alone."]

### Predicted biochemistry (NOT demonstrated)
- Alpha-mannosyltransferase domain related to yeast/Candida MNN2 (28%/35% identity),
  conserved DXD. [PMID:30556809 "The predicted mannosyltransferase domain shares 28% and 35% amino acid sequence identity to alpha 1–2 mannosyltransferase (MNN2) proteins in Saccharomyces cerevisiae and Candida albicans, respectively, including the conserved DXD motif found in many families of glycosyltransferases"]
- No enzymatic assay, no donor/acceptor identified. [PMID:30556809 "While we have not uncovered the target(s) of the predicted glycotransferases or the exact nature of the interplay between the two phenotypes"]
- PAN/Apple domain predicted. [PMID:30556809 "In addition to the mannosyltransferase domain, Couscous is predicted to have a PAN/Apple domain composed of a conserved core of three disulfide bridges"]

### Localization (tagged overexpression; NOT Golgi)
- Couscous-mWasabi in puncta through cytosol, collar and cell membrane.
  [PMID:30556809 "In wild type cells transfected with a couscous-mWasabi transgene under the efl promoter, Couscous was found in puncta scattered throughout the cytosol, collar and cell membrane"]
- Explicitly not Golgi, possibly ER (untested), with caveats about tag/overexpression.
  [PMID:30556809 "While Couscous-mWasabi was clearly not localized to the Golgi, the puncta may co-localize with the ER, where glycosyltransferases are also known to function"]
  [PMID:30556809 "Therefore, we are currently uncertain about the subcellular localization of Couscous protein."]
- Contrast: Jumble (the other predicted GT) does localize to the Golgi-like apical region.

### Glycosylation phenotype (demonstrated, mechanism unresolved)
- 21 of 22 lectins unchanged; jacalin basal-pole staining lost in Couscous (and Jumble),
  apical staining normal. [PMID:30556809 "In contrast with wild type cells, the basal patch of jacalin staining was absent or significantly diminished in Couscous and Jumble mutants, both in the presence and absence of RIFs"]
- Rescue restores jacalin pattern. [PMID:30556809 "The same was true for Couscous cells, in which transformation with couscous-mTFP rescued both rosette development and the wild type glycosylation pattern"]
- Authors leave open trafficking vs glycosylation. [PMID:30556809 "The loss of basal jacalin staining in Jumble and Couscous mutants indicated that jumblelw1 and couscouslw1 either disrupt proper trafficking of sugar-modified molecules to the basal pole of cells or alter the glycosylation events themselves."]

### Effect on Rosetteless (demonstrated, downstream)
- Rosetteless localizes basally but is not upregulated/secreted on RIF induction.
  [PMID:30556809 "In both Jumble and Couscous cells, Rosetteless protein properly localized to the basal pole, but its expression did not increase nor was it secreted upon treatment with RIFs, as normally occurs in wild type cells"]

### Hypotheses (not tested)
- Regulatory glycosylation of adhesion molecules (cadherins); protective glycocalyx
  layer; analogy to yeast MNN2 role in flocculation.

## Other literature
- Levin et al. 2014 (PMID:25299189): original screen; the "Branched" mutant (= Couscous)
  forms branched chain colonies. [PMID:25299189 "In contrast, classes D–F developed into highly branched chain colonies"]
- Larson et al. 2020 PNAS (PMID:31896587): frames couscous as an ECM regulator.
  [PMID:31896587 "Interestingly, all 3 genes known to be required for rosette development are regulators of the extracellular matrix (ECM): a C-type lectin called rosetteless (18) and 2 predicted glycosyltransferases called jumble and couscous (19)."]
- Combredet et al. 2025 Cell Rep (PMID:41037400, abstract only): CRISPR KO of couscous
  (reverse-genetic confirmation, details not in cached abstract); couscous transcript
  regulated by Warts/Yorkie. [PMID:41037400 "We inactivated three known S. rosetta multicellular developmental regulators (rosetteless, couscous, and jumble)"]
  [PMID:41037400 "RNA sequencing revealed that Warts and Yorkie regulated several extracellular matrix genes involved in multicellularity (including couscous)"]

## Curation reasoning summary
- MF alpha-1,2-mannosyltransferase: homology-only (TreeGrafter, fungal MNN2 family,
  conserved DXD). Accept as best-supported prediction; flag unverified.
- Golgi terms: family default; directly contradicted (with caveats) by tagged
  localization -> UNDECIDED.
- mannan biosynthetic process: GO definition is plant hemicellulose; fungal cell-wall
  mannan usage does not apply to a choanoflagellate -> REMOVE.
- No NEW process annotations: rosette development / cell adhesion phenotypes are
  necessity evidence, substrate unknown; GO lacks a rosette/clonal colony development
  term (proposed as new term instead).
