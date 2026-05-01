# Project CEPHALOPOD: AI Gene Review for Cephalopod Genes

## Motivation

Cephalopods (octopus, squid, cuttlefish) represent one of the most fascinating gaps in functional
gene annotation. Despite possessing the largest invertebrate nervous systems, sophisticated
adaptive camouflage, and remarkable cognitive abilities, cephalopod genes have only **27 experimental
GO annotations** across all species (0.008% of 333,921 total annotations). This project aims to review
experimentally characterized cephalopod genes using the ai-gene-review framework, synthesizing
literature evidence with computational predictions to fill this annotation desert.

## Genomic Resources

### Sequenced Genomes

| Species | Common Name | Taxon ID | Genome Size | Predicted Genes | Assembly Quality | Notes |
|---------|-------------|----------|-------------|-----------------|-----------------|-------|
| *Octopus bimaculoides* | California two-spot octopus | 37653 | 2.7 Gb | 15,842 (RefSeq) / ~33,000 (original) | Scaffold-level | First cephalopod genome (Albertin et al. 2015, Nature) |
| *Octopus vulgaris* | Common octopus | 6645 | ~2.7 Gb | 23,423 | Chromosome-level | G3 2023; CephRes genome browser |
| *Octopus sinensis* | East Asian common octopus | 2607531 | 2.72 Gb | 18,886 (RefSeq) | Chromosome-level (30 pseudochromosomes) | PacBio + Hi-C; Ensembl Metazoa |
| *Octopus minor* | Common long-arm octopus | - | 5.09 Gb | 30,010 | Contig N50: 197 kb | Kim et al. 2018, GigaScience |
| *Amphioctopus fangsiao* | Gold-ringed octopus | - | 4.34 Gb | - | Chromosome-level | ONT + Hi-C; single-nucleus brain transcriptome |
| *Doryteuthis pealeii* | Longfin inshore squid | 34683/1051067 | ~4.5 Gb | >24,900 | Chromosome-level | PacBio + Hi-C; Nature Communications 2022 |
| *Euprymna scolopes* | Hawaiian bobtail squid | 6613 | - | ~18,296-18,890 | Chromosome-scale | BRAKER2 annotation with Iso-Seq; dedicated genome portal |
| *Euprymna berryi* | Berry's bobtail squid | - | - | - | - | CRISPR-amenable model (Ahuja et al. 2023) |
| *Sepia officinalis* | Common cuttlefish | 6625 | 5.68 Gb | - | Chromosome-scale (47 chr) | PacBio HiFi + Hi-C (2025, eLife) |
| *Nautilus pompilius* | Chambered nautilus | - | 730 Mb | - | PacBio + Illumina | Compact genome; outgroup (2021, Nat Ecol Evol) |
| *Architeuthis dux* | Giant squid | - | ~2.7 Gb | - | Draft (scaffold N50: 4.8 Mb) | 100+ protocadherins; 2020 GigaScience |

### Cephalopod-Specific Databases

- **CephRes Genome Browser** (cephalopodresearch.org/ceph_gdatab/) — O. vulgaris, O. bimaculoides, O. minor, H. maculosa, E. scolopes, A. dux
- **Euprymna Genome Portal** (metazoa.csb.univie.ac.at) — Dedicated E. scolopes resource
- **Ensembl Metazoa** — O. sinensis
- **CephSeq Consortium** — International coordination for cephalopod genome resources

### GO Annotation Status (QuickGO, May 2026)

**Total annotations for Cephalopoda (taxon:6605): 333,921**

| Evidence Type | Count | % |
|---------------|-------|---|
| IEA (InterPro/HAMAP) | 149,500 | 44.8% |
| IBA (TreeGrafter) | 101,488 | 30.4% |
| IEA (UniProt/UniRule) | 53,446 | 16.0% |
| IEA (UniProt subcell) | 22,065 | 6.6% |
| IEA (GOC) | 7,337 | 2.2% |
| ISS | 50 | 0.01% |
| **IDA** | **19** | **0.006%** |
| TAS | 6 | 0.002% |
| **EXP** | **4** | **0.001%** |
| **IEP** | **2** | **0.001%** |

**Top annotated species**: *O. sinensis* (118,991), *A. pharaonis* (105,672), *O. vulgaris* (89,576), *O. bimaculoides* (3,499), *S. officinalis* (1,021)

**UniProt reviewed (Swiss-Prot) entries**: ~151 across ~23 cephalopod species

### All 27 Experimental GO Annotations

Only 11 gene products across 7 species have any experimental GO evidence:

| UniProt | Gene | Species | Evidence | GO Terms | PMID |
|---------|------|---------|----------|----------|------|
| A0A7E6FSU6 | DDO | *O. vulgaris* | IDA, EXP (4) | D-aspartate oxidase activity, FAD binding, D-amino acid catabolic process | 7915543 |
| Q9U6M6 | AP180 | *D. pealeii* | IDA, IMP (4) | Clathrin coat assembly, neurotransmitter secretion, synaptic vesicle endocytosis | 10575017, 12807910 |
| P86702 | Nautilin-63 | *N. macromphalus* | IDA (3) | Chitin binding, regulation of biomineralization, extracellular region | 21585656 |
| P85067 | OJP1 | *S. officinalis* | IDA, IEP (3) | Regulation of muscle contraction, sexual reproduction | 16434122 |
| P85069 | OJP3 | *S. officinalis* | IDA, IEP (3) | Regulation of muscle contraction, sexual reproduction | 16434122 |
| P31356 | RHO | *T. pacificus* | IDA (2) | Retinal binding, membrane | 17554166 |
| Q7SIG4 | DFPase | *L. vulgaris* | IDA (2) | Calcium ion binding, DFPase activity | 11134940, 15966726 |
| Q7YW31 | CTR1 | *O. vulgaris* | IDA (1) | Protein-hormone receptor activity | 15504101 |
| Q5WA50 | CTR2 | *O. vulgaris* | IDA (1) | Protein-hormone receptor activity | 15504101 |
| C6KYS2 | Symplectin | *S. oualaniensis* | IDA (1) | Bioluminescence | 12054553 |
| C4N147 | ReP1-NCXSQ | *D. pealeii* | EXP (2) | Cytoplasm, membrane | 19168028, 24269200 |
| D2X5V5 | Beta-MSP | *D. pealeii* | EXP (1) | Extracellular region | 21315594 |

## Gene Candidates for Review

### Tier 1: Strong candidates (experimental GO evidence + deep literature)

#### 1. DDO (D-aspartate oxidase) — *Octopus vulgaris*
- **UniProt**: A0A7E6FSU6
- **Existing GO**: 4 experimental annotations (IDA, EXP) — most of any cephalopod gene
- **Function**: Oxidizes D-aspartate and D-amino acids; FAD-dependent; role in amino acid metabolism and neuromodulation
- **Key papers**: D'Aniello et al. 1993 (biological role, JBC, PMID:7903300); PMID:7915543
- **Why review**: Best-annotated cephalopod gene; well-characterized enzyme; important for D-amino acid signaling in nervous system

#### 2. AP180 (clathrin assembly protein) — *Doryteuthis pealeii*
- **UniProt**: Q9U6M6
- **Existing GO**: 4 experimental annotations (IDA, IMP) — includes mutant phenotype evidence
- **Function**: Regulates clathrin coat assembly; essential for synaptic vesicle endocytosis
- **Key papers**: PMID:10575017, PMID:12807910
- **Why review**: Only cephalopod gene with IMP evidence; classic squid giant synapse model

#### 3. Rhodopsin (RHO) — *Multiple species*
- **UniProt**: P31356 (*T. pacificus*), P09241 (*E. dofleini*), O16005 (*S. officinalis*), + others
- **Existing GO**: 2 experimental annotations (IDA)
- **Function**: Visual photopigment and extraocular photoreceptor
- **Key papers**: Ramirez & Oakley 2015 (LACE, [DOI](https://doi.org/10.1242/jeb.110908)); Kingston et al. 2015 (dermal phototransduction, [DOI](https://doi.org/10.1242/jeb.117945)); Maselli et al. 2025 (extraocular in suckers/optic lobes, [DOI](https://doi.org/10.1111/1749-4877.13002))
- **Why review**: Deep literature; dermal light sensing is a remarkable cephalopod-specific function

#### 4. CTR1/CTR2 (cephalotocin receptors) — *Octopus vulgaris*
- **UniProt**: Q7YW31 (CTR1), Q5WA50 (CTR2)
- **Existing GO**: 1 IDA each
- **Function**: GPCRs for cephalotocin (oxytocin/vasopressin superfamily peptide)
- **Key papers**: Kanda et al. 2003 ([DOI](https://doi.org/10.1677/joe.0.1790281)); Kim et al. 2022 (antidiuretic activity, [DOI](https://doi.org/10.3390/md20050328))
- **Why review**: Functionally characterized with Xenopus oocyte expression; first invertebrate with dual OT/VP peptides

#### 5. Symplectin — *Sthenoteuthis oualaniensis*
- **UniProt**: C6KYS2
- **Existing GO**: 1 IDA (bioluminescence)
- **Function**: Photoprotein for bioluminescence using coelenterazine; evolved from pantetheinase
- **Key papers**: Francis et al. 2017 ([DOI](https://doi.org/10.7717/peerj.3633)); Galeazzo et al. 2019 ([DOI](https://doi.org/10.1111/php.13106))
- **Why review**: Novel luciferase unrelated to any other bioluminescence system

### Tier 2: Strong literature but no/few existing GO annotations

#### 6. ADAR1/ADAR2 — RNA editing enzymes — *Doryteuthis pealeii*
- **Function**: Adenosine deaminase acting on RNA; recodes >60% of neural transcripts
- **Key papers**: Vallecillo-Viejo et al. 2023 (novel sqADAR1 domain, [DOI](https://doi.org/10.3389/fgeed.2023.1181713)); Voss & Rosenthal 2023 ([DOI](https://doi.org/10.1093/bfgp/elad034))
- **Why review**: Cephalopod-defining innovation; unprecedented scale of protein recoding

#### 7. Reflectin — *Doryteuthis spp., Euprymna scolopes*
- **Function**: Structural protein in iridophores; phosphorylation-driven Bragg reflectance
- **Key papers**: 29 papers; Naughton et al. 2016 ([DOI](https://doi.org/10.1002/adma.201601666)); Chatterjee et al. 2018 ([DOI](https://doi.org/10.1088/1748-3190/aab804)); origin traced to *V. fischeri* transposon (Crookes et al. 2017, [DOI](https://doi.org/10.1016/j.cub.2017.07.061))
- **Why review**: Cephalopod-specific; no homologs in other animals; key to adaptive camouflage

#### 8. SLC6A4/SERT (serotonin transporter) — *Octopus bimaculoides*
- **Function**: Serotonin reuptake transporter; mediates prosocial behavior
- **Key papers**: Edsinger & Dölen 2018 (MDMA-induced social behavior, [DOI](https://doi.org/10.1016/j.cub.2018.07.061))
- **Why review**: Conserved MDMA binding site; remarkable behavioral pharmacology study

#### 9. TDO/IDO — *Euprymna berryi, Doryteuthis pealeii*
- **Function**: Tryptophan/indoleamine 2,3-dioxygenases; ommochrome pigment biosynthesis
- **Key papers**: Ahuja et al. 2023 (CRISPR albino line, [DOI](https://doi.org/10.1016/j.cub.2023.05.066)); Crawford et al. 2020 (first squid knockout, [DOI](https://doi.org/10.1016/j.cub.2020.06.099))
- **Why review**: First CRISPR knockouts in any cephalopod; reverse genetics proof of function

#### 10. S-crystallins — *Multiple species*
- **UniProt**: P18425/P18426 (*N. sloanii*), P27009-P27012 (*E. dofleini*), P27013-P27015 (*O. vulgaris*)
- **Function**: Lens structural proteins evolved from GST; 24+ family members
- **Key papers**: Tomarev et al. 1995 ([DOI](https://doi.org/10.1007/BF00173186))
- **Why review**: Textbook enzyme crystallin co-option

### Tier 3: Additional candidates with good literature

| Gene | Species | UniProt | Key Finding | PMID |
|------|---------|---------|-------------|------|
| Protocadherins | *O. bimaculoides* | - | >160 genes; massive expansion for neural wiring | 26268193 |
| Synaptotagmin | *O. bimaculoides* | - | Temperature-dependent RNA editing tunes Ca2+ binding | 37295402 |
| Synapsins | *O. vulgaris* | - | Three isoforms in brain and reproductive organs | 31659209 |
| TLR4-1 | *O. sinensis* | - | RNAi knockdown activates MyD88/TRIF pathways | 39265964 |
| OJP1/OJP3 | *S. officinalis* | P85067/P85069 | Ovarian peptides with 3 IDA/IEP annotations each | 16434122 |
| Hemocyanin | *S. officinalis* | P56824/P56825 | Copper-based oxygen transport; dual immune role | multiple |
| FMRFamide | *S. officinalis* | P91889 | Neuropeptide precursor; 14 bioactive peptides | 11060217 |
| OPR | *O. vulgaris* | Q5W9T5 | Octopressin receptor (vasopressin superfamily) | - |
| Complexin | *D. pealeii* | Q95PA1 | Synaptic vesicle fusion regulator | - |
| Kinesin | *D. pealeii* | P21613 | Axonal transport; RNA editing target | 37295402 |
| elav1 | *S. officinalis* | - | First neurogenesis map in a cephalopod | 23047428 |
| ascl1/neurogenin | *O. vulgaris* | - | Neural progenitors with vertebrate-like migration | 34425939 |
| Nautilin-63 | *N. macromphalus* | P86702 | Shell biomineralization; 3 IDA annotations | 21585656 |
| DFPase | *L. vulgaris* | Q7SIG4 | Diisopropyl-fluorophosphatase; 2 IDA annotations | 11134940 |
| Pax6 | *D. pealeii* | - | Eye development; unconventional expression in gills/suckers | 27510978 |
| IR25 | *S. officinalis* | - | First cephalopod olfactory receptor | 34718445 |

## Species Selection Strategy

**Primary species** (genome + UniProt entries + research community):
- *Octopus vulgaris* (NCBI:6645) — 21 Swiss-Prot entries, most experimental GO annotations
- *Octopus bimaculoides* (NCBI:37653) — Reference genome, camouflage/behavior studies
- *Doryteuthis pealeii* (NCBI:34683) — 13 Swiss-Prot entries, neuroscience model, RNA editing
- *Euprymna scolopes* (NCBI:6613) — Symbiosis model (0 Swiss-Prot, but genome available)
- *Sepia officinalis* (NCBI:6625) — 12 Swiss-Prot entries, cuttlefish development

**Note**: *Euprymna berryi* is important for CRISPR work but has fewer genomic resources.

## Organism Directory Naming

Following the existing convention in this repo (UniProt mnemonic style):
```
genes/
  OCTVU/    # Octopus vulgaris
  OCTBI/    # Octopus bimaculoides
  DORPE/    # Doryteuthis pealeii
  EUPSC/    # Euprymna scolopes
  SEPOF/    # Sepia officinalis
```

## Recommended Initial Review Set (10 genes)

| Priority | Gene | Species | UniProt | Rationale |
|----------|------|---------|---------|-----------|
| 1 | DDO | *O. vulgaris* | A0A7E6FSU6 | Most experimental GO annotations (4); clear enzyme function |
| 2 | AP180 | *D. pealeii* | Q9U6M6 | 4 exp. annotations incl. IMP; synaptic vesicle biology |
| 3 | RHO | *T. pacificus* / *O. vulgaris* | P31356 | IDA evidence; dermal photoreception novelty |
| 4 | CTR1 | *O. vulgaris* | Q7YW31 | IDA; functionally expressed; OT/VP superfamily |
| 5 | Symplectin | *S. oualaniensis* | C6KYS2 | IDA; novel bioluminescence mechanism |
| 6 | ADAR2 | *D. pealeii* | - | Cephalopod innovation; >60% neural transcripts edited |
| 7 | Reflectin | *D. opalescens* | - | Cephalopod-specific; camouflage |
| 8 | SLC6A4/SERT | *O. bimaculoides* | - | Social behavior pharmacology |
| 9 | TDO | *E. berryi* | - | CRISPR validated |
| 10 | S-crystallin | *O. vulgaris* | P27013 | Enzyme crystallin evolution |

## Literature Landscape (PubMed, May 2026)

| Topic | Papers | Key Focus |
|-------|--------|-----------|
| Euprymna-Vibrio symbiosis | 135+ | Mostly *V. fischeri* genes; some host immune genes |
| RNA editing (ADAR) | ~10 | Transcriptome-wide recoding; temperature-dependent editing |
| Reflectin | 29 | Structure, self-assembly, biomaterials |
| Chromatophore/camouflage | Growing | Opsins, phototransduction, scRNA-seq cell atlases |
| Eye development | ~15 | Pax6, Notch, RDGN network |
| Neuropeptides | ~20 | FMRFamide, OT/VP superfamily, neuropeptidome |
| Octopus genome | Strong | Albertin et al. 2015 flagship; protocadherins, ZNFs |
| CRISPR in cephalopods | 2 | *D. pealeii* TDO (2020); *E. berryi* TDO+IDO (2023) |
| Innate immunity | ~10 | TLR4, lysozyme, NF-kappaB, hemocyanin-derived AMPs |
| Neuroscience | ~20 | Giant axon, synapse, neurogenesis, optic lobe cell atlas |

## Challenges

1. **Near-zero experimental GO annotations** — Only 27 exist across all cephalopods; most of our curation will be novel
2. **Fragmented UniProt coverage** — Many experimentally characterized proteins lack reviewed entries; *E. scolopes* has 0 Swiss-Prot entries despite being a major model
3. **Non-model organism** — No standard gene nomenclature committee; gene names inconsistent across species
4. **Multi-species biology** — Same gene may be studied in different species; need to decide per-species or consolidated reviews
5. **Large genomes** — 2.7-5.7 Gb with 42-71% repetitive content; gene prediction counts vary 2-fold between methods
6. **Limited reverse genetics** — Only 2 CRISPR papers exist; most functional evidence is expression/localization/pharmacology

## Key Genomic Features of Cephalopods

- **Protocadherin expansion**: >160 genes in octopus (vs ~70 in mammals); clustered, neural-enriched
- **C2H2 zinc finger expansion**: Another vertebrate-convergent gene family amplification
- **Extensive RNA editing**: A-to-I recoding at >57,000 sites; temperature-responsive
- **Taxonomically restricted genes**: Hundreds of cephalopod-specific genes in skin, suckers, nervous system
- **Horizontal gene transfer**: 12 bacterial HGT genes identified in *O. bimaculoides*, including immune defense genes

## References

Key genome and review papers:
- Albertin et al. 2015. The octopus genome. *Nature* 524:220-4. [DOI](https://doi.org/10.1038/nature14668)
- Albertin et al. 2022. *D. pealeii* and cephalopod evolution. *Nat Commun*. [DOI](https://doi.org/10.1038/s41467-022-29748-w)
- Kim et al. 2018. *O. minor* genome. *GigaScience* 7(11). [DOI](https://doi.org/10.1093/gigascience/giy119)
- Ahuja et al. 2023. CRISPR albino squid. *Curr Biol* 33:2774-2783. [DOI](https://doi.org/10.1016/j.cub.2023.05.066)
- Crawford et al. 2020. First squid CRISPR knockout. *Curr Biol*. [DOI](https://doi.org/10.1016/j.cub.2020.06.099)
- Voss & Rosenthal 2023. RNA editing in coleoids. *Brief Funct Genomics* 22:525-532. [DOI](https://doi.org/10.1093/bfgp/elad034)
- Vallecillo-Viejo et al. 2023. Squid ADARs. *Front Genome Ed* 5:1181713. [DOI](https://doi.org/10.3389/fgeed.2023.1181713)
- Wang & Ragsdale 2017. Octopus cadherins. *Semin Cell Dev Biol* 69:151-157. [DOI](https://doi.org/10.1016/j.semcdb.2017.06.007)
- Edsinger & Dölen 2018. Octopus MDMA social behavior. *Curr Biol*. [DOI](https://doi.org/10.1016/j.cub.2018.07.061)
- Kanda et al. 2003. Cephalotocin receptor. *J Endocrinol* 179:281-91. [DOI](https://doi.org/10.1677/joe.0.1790281)
