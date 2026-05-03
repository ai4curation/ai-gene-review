---
title: Cephalopod Neuro Gene Reviews
species: [OCTVU, OCTBM, DORPE, SEPOF, STHOU, DOROP, EUPSC]
status: IN_PROGRESS
---
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

### Future candidates (not yet reviewed)

| Gene | Species | UniProt (mnemonic) | Key Finding | PMID |
|------|---------|---------|-------------|------|
| Protocadherins | *O. bimaculoides* | - | >160 genes; massive expansion for neural wiring | 26268193 |
| Synaptotagmin | *O. bimaculoides* | - | Temperature-dependent RNA editing tunes Ca2+ binding | 37295402 |
| Synapsins | *O. vulgaris* | - | Three isoforms in brain and reproductive organs | 31659209 |
| TLR4-1 | *O. sinensis* | - | RNAi knockdown activates MyD88/TRIF pathways | 39265964 |
| OJP1/OJP3 | *S. officinalis* | P85067/P85069 (OJP1_SEPOF) | Ovarian peptides with 3 IDA/IEP annotations each | 16434122 |
| Hemocyanin | *S. officinalis* | P56824/P56825 (HCYCD_SEPOF) | Copper-based oxygen transport; dual immune role | multiple |
| Nautilin-63 | *N. macromphalus* | P86702 (NAU63_NAUMA) | Shell biomineralization; 3 IDA annotations | 21585656 |
| DFPase | *L. vulgaris* | Q7SIG4 (DFPP_LOLVU) | Diisopropyl-fluorophosphatase; 2 IDA annotations | 11134940 |
| GnRH receptor | *O. vulgaris* | Q2V2K5 (GNRHR_OCTVU) | Reproductive GPCR | 16367741 |
| Cephalotocin | *O. vulgaris* | P80027 (CEPHT_OCTVU) | OT/VP neuropeptide ligand | - |
| Beta-MSP | *D. pealeii* | D2X5V5 (MSPH_DORPE) | Male aggression pheromone; EXP evidence | 21315594 |
| elav1 | *S. officinalis* | - | First neurogenesis map in a cephalopod | 23047428 |
| ascl1/neurogenin | *O. vulgaris* | - | Neural progenitors with vertebrate-like migration | 34425939 |
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

Following UniProt mnemonic codes:
```
genes/
  OCTVU/    # Octopus vulgaris (6645)
  OCTBM/    # Octopus bimaculoides (37653)
  DORPE/    # Doryteuthis pealeii (34683)
  SEPOF/    # Sepia officinalis (6625)
```

## Completed Reviews (16 genes, 7 species)

| Gene | Species | UniProt | Highlights |
|------|---------|---------|------------|
| DDO | OCTVU | A0A7E6FSU6 | D-amino-acid oxidase IEA corrected; D-Asp in retina at 2.30 umol/g |
| AP180 | DORPE | Q9U6M6 | Spurious ARBA "locomotion" removed; IDR with 12-19 clathrin motifs |
| cpx | DORPE | Q95PA1 | Dual clamp/activator; syntaxin binding (IPI) from crystal structure |
| CTR1 | OCTVU | Q7YW31 | "Vasopressin receptor" corrected; gastric ganglion expression |
| OPR | OCTVU | Q5W9T5 | Antidiuretic function via hemolymph osmolarity |
| FMRFa | SEPOF | P91889 | Differential oviduct effects; immune regulation (NO inhibition) |
| khc | DORPE | P21613 | 8nm step/ATP (Vale 1985); tissue-specific velocities via RNA editing |
| RHO | SEPOF | O16005 | GO:0030265 PLC-activating opsin signaling; dermal photoreception |
| OCBIM_22006518mg | OCTBM | A0A0L8FVQ9 | CRT1: contact chemosensation, feeding, maternal behavior |
| sympp | STHOU | C6KYS2 | Novel bioluminescence; K+ > Rb+ > Na+ cation specificity |
| CTR2 | OCTVU | Q5WA50 | Peripheral expression (branchia, vas deferens); positions 2-5 selectivity |
| OCTS1 | OCTVU | P27013 | GST over-annotated (1/700 kcat); PDB 5B7C; colloidal gel assembly |
| TDO | DORPE | A0A7G4RN94 | First CRISPR target; *D. pealeii* lacks IDO unlike *E. berryi* |
| OCBIM_22008529mg | OCTBM | A0A0L8FU48 | SLC6A4/SERT: social behavior (MDMA, Edsinger 2018) |
| Q6WDN4 | EUPSC | Q6WDN4 | Reflectin: 380 mg/mL in platelets; condensate scaffold activity |
| ADAR2 | DOROP | C1JAR3 | tRNA deaminase removed; axon cytoplasm; 37 editing sites in motor domain |

## Surprises and Lessons from Deep Research

### Annotation errors systematically exposed

1. **Vasopressin receptor mis-annotation is pervasive**: All three OT/VP receptors (CTR1, CTR2, OPR)
   had GO:0005000 (vasopressin receptor activity) from IEA. None bind vasopressin. The correct term
   is GO:0008188 (neuropeptide receptor activity). This is a systematic IEA pipeline failure for
   invertebrate OT/VP superfamily members.

2. **ARBA generates false positives for non-model organisms**: Kinesin annotated with "locomotion",
   "nuclear migration", "isomerase activity"; AP180 with "locomotion", "Golgi apparatus". These
   are transferred from vertebrate biology without cephalopod evidence.

3. **Ancestral function annotations persist after functional divergence**: S-crystallin (OCTS1)
   retains GO:0004364 (GST activity) despite having 1/700 the catalytic efficiency of real GST.
   The protein binds GSH 43-fold tighter than GST-sigma — for structural stabilization (raises Tm
   by 7C), not catalysis. A textbook case of over-annotation from sequence homology.

4. **tRNA deaminase vs RNA deaminase confusion**: ADAR2 was annotated with GO:0008251
   (tRNA-specific adenosine deaminase activity) — this is ADAT function, not ADAR. TreeGrafter
   confused the two related but distinct enzyme families.

### Novel biology captured for the first time in GO

5. **Dermal photoreception**: Rhodopsin expressed in skin chromatophores mediates LACE (light-
   activated chromatophore expansion). The most precise GO term is GO:0030265 (PLC-activating
   opsin-mediated signaling pathway) — a child of BOTH GPCR signaling AND phototransduction.

6. **Contact chemosensation**: CRT1 is a cephalopod-specific ion channel (no homologs outside
   Cephalopoda) that evolved from nAChRs via retrotransposition (26 intronless genes on one
   chromosome). It detects hydrophobic molecules by direct contact, mediating feeding behavior
   AND maternal care. The 2025 Sepela paper (Cell) showed bacterial metabolites on eggs activate
   CRT1 for brooding behavior — a remarkable microbiome-receptor-behavior circuit.

7. **Annotation deserts are real**: FMRFa (2 annotations), SLC6A4 (0), reflectin (0) — all
   well-characterized genes with extensive literature but near-zero GO coverage. The project
   proposed 19 annotations across these 3 genes alone.

### Deep research integration insights

8. **DDO has a visual system role**: Deep research revealed D-aspartate at 2.30 umol/g in
   octopus retina (PMID:15491279), with radiotracer evidence for D-Asp transport from optic
   lobes to retina. DDO controls D-Asp levels in visual circuits, not just liver/kidney.

9. **Symplectin may be bifunctional**: Conserved pantetheinase catalytic triad (E60-K163-C196)
   suggests symplectin retains ancestral hydrolase activity alongside its bioluminescence
   function. The monovalent cation specificity (K+ > Rb+ > Na+, NOT Ca2+) is unique among
   photoproteins.

10. **Kinesin velocities are tissue-specific via RNA editing**: Single-molecule assays show
    optic lobe variants at ~520 nm/s, unedited at ~587 nm/s, stellate ganglion at ~620-674 nm/s.
    37 editing sites in the motor domain alone. This is the most direct functional demonstration
    of RNA editing tuning protein properties in any organism.

11. **Complexin has a dual clamp/activator role**: Not just a fusion clamp — the N-terminal
    domain (residues 1-26) actively promotes fusion while the central helix clamps spontaneous
    release. The squid giant synapse was where this was first demonstrated.

12. **OPR is an antidiuretic hormone receptor**: Deep research added the Sakamoto 2015 paper
    showing octopressin injection decreases hemolymph osmolarity and reduces Ca2+/Na+ in blood
    and urine — a parallel to vertebrate vasopressin/ADH function that wasn't in the initial review.

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
