---
title: "Origins of Animal Multicellularity"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [SALRS, MONBE, CAPO3, OSCPE, AMPQE, human]
genes: [rosetteless, jumble, couscous, hippo, warts, yorkie, coHpo, coWts, coYki, VIN1, TLN, LATS1, STK3, YAP1, TEAD1, TLN1, VCL, TBXT, CSK, CTNNB1, SRC, ITGB1, PTK2, CTNNA1, COL4A1, CDH1, ABL1, MYC, NOTCH1, TP53, SrSeptin2, SrSeptin6, CoBra, coITGB2, coVIN]
---

# Project ORIGINS_OF_MULTICELLULARITY: Gene Function at the Origin of Animals

**Bottom line:** animals evolved from a single-celled ancestor they share
with choanoflagellates, and many genes that build animal bodies predate
animals and are present in their unicellular relatives. Examples are
cadherins, integrins and their adhesome, tyrosine kinases, Hippo signalling
and the T-box factor Brachyury. GO barely covers these relatives, so their
functions are annotated almost entirely by transfer from animals.

A GOA census on 2026-09-30 found how few experimental GO annotations these
relatives carry:

| Lineage | Experimental annotations |
|---|---:|
| Ichthyosporeans, ctenophores, placozoans | 0 |
| Choanoflagellates | 2, both `protein binding` |
| *Capsaspora* | 4, all on one histone |
| Sponges | 16 |
| Metazoa as a whole | about 952,000 |

We have 35 draft or updated reviews in four tracks:

- **Track A: 16 genes with direct genetic evidence in unicellular relatives
  and a sponge.**
  - *S. rosetta*: the rosette genes, the Hippo pathway and the septins.
  - *Capsaspora*: the Hippo pathway, Brachyury, integrin beta 2 and
    vinculin.
  - Sponge: vinculin and talin.
- **Track B: 19 human toolkit genes.** Each review records which functions
  are ancestral and which are animal recruitments.
- **Track C: a propagation audit.** It found animal tissue terms (organ
  growth), junction terms and fungal pathway terms reaching unicellular
  proteins.
  - Five TreeGrafter/PANTHER placement errors. Three of them graft
    unicellular proteins onto animal-only nodes:
    - choanoflagellate cadherins onto a node PAINT restricts to Bilateria;
    - *Capsaspora* integrin betas onto the vertebrate ITGBL1 node;
    - *Capsaspora* T-box factors onto an all-animal node carrying "cell fate
      specification".

    The other two are *Capsaspora* Warts with the ROCK/citron kinases, and
    the *S. rosetta* yorkie candidate with the MAGI scaffolds.
  - One PAINT node placed too deep: the organ-growth term on the LATS node.
- **Track D: one proposed GO term**, rosette colony development.

The pattern across Tracks A and B is consistent:
- **Ancestral:** core molecular activities, such as kinase activity, YAP-TEAD
  coactivation, talin-vinculin coupling, Myc-Max E-box binding and T-box DNA
  binding.
- **Animal-specific:** control of proliferation and organ size, coupling to
  classical cadherins, and basement-membrane collagen IV, so far as the
  evidence shows.

## Motivation

Multicellularity arose independently many times (animals, land plants, several
algal lineages, fungi, and aggregative forms such as *Dictyostelium*). Animal
multicellularity is the best studied of these, and comparative genomics of its
closest unicellular relatives has changed the question. The
choanoflagellate genome showed that cadherins, tyrosine kinases and other
"animal" signalling and adhesion families were already present before animals
[PMID:18273011 "The genome of the choanoflagellate Monosiga brevicollis and the origin of metazoans"].
*Capsaspora* carries an integrin adhesome and many animal-type transcription
factors [PMID:23942320 "The Capsaspora genome reveals a complex unicellular prehistory of animals"; PMID:20479219 "Ancient origin of the integrin-mediated adhesion and signaling machinery"].
Gene-family reconstructions of the animal stem lineage separate what was
co-opted from what was new
[PMID:29848444 "Gene family innovation, conservation and loss on the animal stem lineage"].
The origin of animal multicellularity is therefore largely a story of
**co-option**: ancestral proteins with unicellular functions (prey capture,
substrate adhesion, environmental sensing) taking on roles in a multicellular
body.

This makes the lineage a hard test of GO annotation practice:

1. **Annotation desert.** The organisms that best test these hypotheses have
   almost no experimental GO annotations (see the census below). What they
   have is IEA and IBA, transferred mainly from animals.
2. **Propagation direction.** An IBA placed at a node below the Holozoa split
   hands animal-derived functions to choanoflagellate and *Capsaspora*
   proteins. Where that function is biochemical (kinase activity,
   calcium-dependent adhesion), the transfer may be sound. Where it is a
   multicellular process (e.g. tissue development, cell-cell junction
   assembly in an epithelium), the transfer asserts something the organism
   may not do. Where the propagation actually lands is an open, testable
   question (see [IBA_REVIEW](IBA_REVIEW.md) and
   [HOMOLOGY_PROPAGATION](HOMOLOGY_PROPAGATION.md)).
3. **Ontology coverage.** GO has rich terms for animal development and for
   aggregative development in *Dictyostelium* (e.g. `GO:0031152` aggregation
   involved in sorocarp development), but it is not clear that it has terms
   for clonal colony formation in a unicellular holozoan, such as rosette
   development in *S. rosetta*.
4. **Toolkit genes in animals.** The human orthologs of the ancestral toolkit
   are heavily annotated. Reviewing them with the premetazoan evidence in
   mind helps separate the ancestral core activity from the animal-specific
   processes they were later recruited into.

## Phylogenetic frame

```mermaid
graph LR
  OP[Opisthokonta] --> FU[Fungi and relatives]
  OP --> HO[Holozoa]
  HO --> IC[Ichthyosporea<br/>e.g. Sphaeroforma, Creolimax]
  HO --> FI[Filasterea<br/>Capsaspora owczarzaki]
  HO --> CM[Choanozoa]
  CM --> CH[Choanoflagellata<br/>Salpingoeca rosetta, Monosiga brevicollis]
  CM --> ME[Metazoa]
  ME --> CT[Ctenophora<br/>Mnemiopsis]
  ME --> PO[Porifera<br/>Amphimedon, Oscarella]
  ME --> PL[Placozoa<br/>Trichoplax]
  ME --> CN[Cnidaria<br/>Nematostella]
  ME --> BI[Bilateria]
```

Branching among the early animal lineages is drawn as a polytomy. Chromosome-scale
synteny supports ctenophores as sister to all other animals
[PMID:37198475 "Ancient gene linkages support ctenophores as sister to other animals"],
but this project does not depend on resolving that question. Reviews
summarising the unicellular-to-multicellular transition:
[PMID:29065305 "The Origin of Animal Multicellularity and Cell Differentiation"],
[PMID:28479598 "The origin of Metazoa: a unicellular perspective"],
[PMID:33622103 "The origin of animals: an ancestral reconstruction of the unicellular-to-multicellular transition"].

Multicellularity modes in the unicellular relatives:

| Lineage | Organism | Multicellular stage | Mode |
|---|---|---|---|
| Choanoflagellata | *Salpingoeca rosetta* | Rosette colonies, induced by a bacterial sulfonolipid [PMID:23066504 "A bacterial sulfonolipid triggers multicellular development in the closest living relatives of animals"] | Clonal (incomplete cytokinesis) |
| Choanoflagellata | *Choanoeca flexa* | Cup-shaped colonies that invert their curvature in response to light, via a rhodopsin-cGMP pathway and actomyosin contractility [PMID:31624206 "Light-regulated collective contractility in a multicellular choanoflagellate"] | Colonial (mode to check in full text) |
| Filasterea | *Capsaspora owczarzaki* | Adherent, cystic and aggregative life stages [PMID:32857975 "the life cycle of C. owczarzaki (hereafter, Capsaspora) includes three distinct life stages: adherent; cystic; and aggregative"]; life-stage transitions track changes in chromatin and cis-regulation [PMID:27114036 "The Dynamic Regulatory Genome of Capsaspora and the Origin of Animal Multicellularity"] | Aggregative |
| (outgroup, Amoebozoa) | *Dictyostelium discoideum* | Fruiting body | Aggregative, independent origin; see [DICTYOSTELIUM_DEVELOPMENT](DICTYOSTELIUM_DEVELOPMENT.md) |

## Annotation census

Experimental GO annotations (ECO:0000269 and descendants) in GOA, queried from
QuickGO on 2026-09-30 by
[`annotation_census.py`](ORIGINS_OF_MULTICELLULARITY/annotation_census.py);
raw output in
[`annotation_census.tsv`](ORIGINS_OF_MULTICELLULARITY/annotation_census.tsv).

| Lineage | NCBI taxon | Experimental annotations | What they are |
|---|---|---:|---|
| Ichthyosporea | 127916 | 0 | none |
| Filasterea | 2687318 | 4 | all on one *Capsaspora* macroH2A histone (A0A0D2UG83), PMID:34887560 |
| Choanoflagellata | 28009 | 2 | `GO:0005515` protein binding (IPI) for two *M. brevicollis* proteins (A9V7T9, A9VAD3) from a cross-species bZIP interaction screen [PMID:23661758 "Networks of bZIP protein-protein interactions diversified over a billion years of evolution"] |
| Ctenophora | 10197 | 0 | none |
| Porifera | 6040 | 16 | *Oscarella pearsei* vinculin VIN1 and talin TLN [PMID:29880641 "Analysis of a vinculin homolog in a sponge (phylum Porifera) reveals that vertebrate-like cell adhesions emerged early in animal evolution"]; a *Chondrilla* galactose-binding lectin; an *Amphimedon* PI5P 4-kinase; a *Suberites* silicatein |
| Placozoa | 10226 | 0 | none |
| Cnidaria | 6073 | 319 | mostly *Nematostella* and corals (toxins, cGAS/STING) |
| Metazoa (all) | 33208 | 951,791 | |

Two notes from the census:

- The only sponge row for `GO:0098630` aggregation of unicellular organisms is
  on the *Chondrilla* lectin (C0HLX7). Its source reports agglutination of
  *Staphylococcus* and *E. coli* [PMID:29175164 "Antibacterial activity of a new lectin isolated from the marine sponge Chondrilla caribensis"],
  so the aggregating organisms are bacteria, not sponge cells. This row says
  nothing about sponge multicellularity.
- The sponge vinculin paper is the one experimental entry point for the
  adhesome in an early-branching animal, and it pairs naturally with the
  *Capsaspora* integrin work
  [PMID:32857975 "Integrin-Mediated Adhesion in the Unicellular Holozoan Capsaspora owczarzaki"].

## Work plan

### Track A: unicellular-relative genes with direct genetic evidence

Forward and reverse genetics in *S. rosetta* now exist
[PMID:25299189 "The Rosetteless gene controls development in the choanoflagellate S. rosetta."; PMID:32496191 "Genome editing enables reverse genetics of multicellular development in the choanoflagellate Salpingoeca rosetta."].
The genes below have phenotypes but, as of the census, no experimental GO
annotations. Accessions were resolved from the locus tags and GenBank
accessions given in the papers.

| Priority | Gene | Organism | UniProt | Evidence | Current UniProt name / GOA | Notes |
|---|---|---|---|---|---|---|
| 1 | rosetteless (*rtls*) | SALRS | F2U5Y1 (PTSG_03555) | Forward genetic screen; essential for rosette development; the protein forms an extracellular layer that coats and connects the basal poles of rosette cells [PMID:25299189] | "Lung surfactant protein A"; no GOA rows | C-type lectin domain (PF00059), signal peptide. The UniProt name is a similarity-derived label and looks like a naming error to report |
| 2 | jumble (*jmbl*) | SALRS | F2TWH0 (PTSG_00436; EGD72416) | Forward genetics; mutant cells aggregate into amorphous clumps instead of rosettes, with aberrant glycosylation of the basal ECM [PMID:30556809 "Predicted glycosyltransferases promote development and prevent spurious cell clumping in the choanoflagellate S. rosetta"] | "Uncharacterized protein"; no GOA rows | Predicted glycosyltransferase, one N-terminal TM helix |
| 3 | couscous (*cous*) | SALRS | F2UJ78 (PTSG_07368; EGD77026) | Forward genetics, same study [PMID:30556809] | "Apple domain-containing protein"; 7 IEA rows incl. `GO:0000026` alpha-1,2-mannosyltransferase activity | PF11051 mannosyltransferase plus PAN/apple domain; IEA MF is plausible, check the Golgi and "mannan biosynthesis"-type process IEAs |
| 4 | *hippo*, *warts* and *yorkie* (Hippo pathway) | SALRS | F2UQC7 (PTSG_10780), F2U943 (PTSG_04961), F2UDK1 (PTSG_06057), from the bioRxiv preprint DOI:10.1101/2024.07.13.603360 | CRISPR knockouts; warts-KO rosettes are larger than wild type, and Warts and Yorkie regulate ECM genes including couscous [PMID:41037400 "A selection-based knockout approach for a choanoflagellate reveals regulation of multicellular development by Hippo signaling."] | | Pairs with the premetazoan Hippo pathway in *Capsaspora* [PMID:22832104 "Premetazoan origin of the hippo signaling pathway"] |
| 5 | SrSeptin2, SrSeptin6 | SALRS | F2UEE2 (PTSG_07215, Group 4 Cdc12-like), F2UDE9 (PTSG_06009, Group 1B SEPT6-like) | Tagged septins localise to the basal poles of single cells and rosettes [PMID:30281390 "Transfection of choanoflagellates illuminates their cell biology and the ancestry of animal septins."] | | Localisation only; a role in rosette development is a hypothesis, so CC terms at most |
| 6 | integrin β2 (coITGB2) and vinculin (coVIN) | CAPO3 | A0A0D2WRB3 (CAOG_05058; = D7PE19, GenBank GU320673) and A0A0D2WSN3 (CAOG_05123), both named in the methods of the preprint DOI:10.1101/2020.02.27.967653 | Adherent cells attach through actin-dependent filopodia, where integrin β2 and vinculin localise as patches [PMID:32857975] | | Map the paper's "integrin β2" to a UniProt accession from its methods before fetching |
| 7 | Brachyury (CoBra) | CAPO3 | A0A0D2VUC6 (CAOG_005512), our assignment by T-subfamily similarity plus the Brachyury-specific Arg ([capsaspora-tbox](ORIGINS_OF_MULTICELLULARITY/capsaspora-tbox/RESULTS.md)) | Functional conservation shown in *Xenopus*; DNA-binding motif similar to metazoan Brachyury [PMID:24043797 "Early evolution of the T-box transcription factor family"] | | Premetazoan T-box factor; the paper argues metazoan-specific specificity arose later |
| 8 | VIN1 / TLN | OSCPE | A0A3B6UES5 / A0A3G2LGI8 | [PMID:29880641] | 5 experimental rows | Reviewed (DRAFT) |
| 9 | coHpo, coWts, coYki (Hippo pathway) | CAPO3 | A0A0D2WLF3 (CAOG_01932), A0A0D2VGR4 (CAOG_00619), A0A0D2WY30 (CAOG_07866) | Knockouts: coHpo and coWts mutants have nuclear coYki, elongated contractile cells and denser aggregates; coYki mutants bleb and make flatter aggregates; no proliferation effect [PMID:35659869 "Genome editing in the unicellular holozoan Capsaspora owczarzaki suggests a premetazoan role for the Hippo pathway in multicellular morphogenesis."; PMID:38517944 "The Hippo kinase cascade regulates a contractile cell behavior and cell density in a close unicellular relative of animals."] | IEA only | Reviewed (DRAFT); locus IDs from the key resources table of PMID:38517944 |

### Track B: the animal toolkit, reviewed with premetazoan evidence in mind

Human genes whose families predate animals and which the literature above
treats as part of the multicellularity toolkit. Reviews already in the repo
are marked; they need a pass focused on whether the core function is ancestral.

- **Cadherin/catenin adhesion:** CDH1 (review exists), CTNNB1, CTNNA1
- **Integrin adhesome:** ITGB1, TLN1, VCL, PTK2
- **Tyrosine kinase signalling:** SRC, CSK, ABL1 (review exists)
- **Hippo pathway:** STK3, LATS1, YAP1, TEAD1
- **Transcription factors with premetazoan origin:** MYC (review exists), TBXT, TP53 (review exists)
- **Animal-specific comparators:** NOTCH1 (review exists), COL4A1. Neither is
  present in choanoflagellates in the form it has in animals, so they are
  controls for "animal innovation".

**Batch 1 results (2026-10-01, all DRAFT).** Eight human genes, chosen to pair
with the Track A reviews.

| Gene | Rows | Accept | Non-core | Modify | Remove | Over-annot. | Undecided | NEW |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| LATS1 | 105 | 42 | 19 | 10 | 26 | 3 | 5 | 0 |
| STK3 | 162 | 43 | 16 | 8 | 89 | 5 | 1 | 0 |
| YAP1 | 314 | 99 | 42 | 30 | 136 | 5 | 2 | 0 |
| TEAD1 | 57 | 36 | 2 | 15 | 3 | 1 | 0 | 0 |
| TLN1 | 87 | 49 | 14 | 8 | 10 | 5 | 0 | 1 |
| VCL | 107 | 49 | 20 | 9 | 14 | 13 | 1 | 1 |
| TBXT | 39 | 21 | 11 | 4 | 1 | 0 | 0 | 2 |
| CSK | 87 | 41 | 16 | 6 | 16 | 6 | 0 | 2 |

Most removals are generic `protein binding` rows, removed as uninformative
under the repository policy, or replaced by a specific binding term where the
partner defines one.

What each review concluded is ancestral and what is an animal recruitment
(sources in each gene's notes):

| Gene | Ancestral (present in unicellular relatives) | Animal-specific (on current evidence) |
|---|---|---|
| STK3 / LATS1 / YAP1 / TEAD1 | Hippo kinase cascade that keeps Yorkie/YAP out of the nucleus; YAP-TEAD coactivation; TEA-domain DNA binding (older still, in fungi). In *Capsaspora* the cascade controls the cytoskeleton, contractility and aggregate shape | Control of proliferation, organ size, regeneration and contact inhibition; the *Capsaspora* knockouts show no proliferation effect |
| TLN1 / VCL | Talin binds integrin NPxY motifs and activates vinculin's F-actin binding at cell-substrate contacts (sponge biochemistry; *Capsaspora* filopodia) | Vinculin's alpha/beta-catenin link to cadherin junctions, so far documented only in bilaterians, though sponge vinculin is already at cell-cell contacts; platelet and leukocyte adhesion |
| TBXT | T-box DNA motif binding and transcriptional activation (*Capsaspora* CoBra binds a mouse-like motif) | Target selectivity, which the chimera experiments place in the N/C termini and attribute to cofactors; all developmental roles. Choanoflagellates have no T-box genes |
| CSK | Tyrosine kinase activity on the Src C-terminal tail | Adaptor recruitment (PAG, SCIMP) and immune-receptor signalling. Whether Csk already inhibited Src before animals is disputed: two choanoflagellate studies found weak or no inhibition, and a 2017 study reports inhibition |

**Batch 2 results (2026-10-01, all DRAFT).** Six genes with large
annotation sets; COL4A1 is the animal-innovation control for basement-membrane function.

| Gene | Rows | Accept | Non-core | Modify | Remove | Over-annot. | Undecided | NEW |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CTNNB1 | 723 | 254 | 112 | 217 | 126 | 13 | 1 | 0 |
| SRC | 551 | 241 | 103 | 67 | 125 | 13 | 1 | 1 |
| ITGB1 | 349 | 160 | 95 | 27 | 51 | 14 | 2 | 0 |
| PTK2 | 234 | 95 | 51 | 11 | 66 | 5 | 5 | 1 |
| CTNNA1 | 129 | 48 | 11 | 14 | 48 | 8 | 0 | 0 |
| COL4A1 | 60 | 47 | 8 | 0 | 2 | 2 | 1 | 0 |

| Gene | Ancestral | Animal-specific (on current evidence) |
|---|---|---|
| CTNNB1 / CTNNA1 | A catenin junction-and-polarity module without cadherins: *Dictyostelium* builds a polarized epithelium with Aardvark and an alpha-catenin (PMID:21393547) | The beta-catenin family itself (PTHR45976 is animal-only); classical-cadherin binding; TCF/LEF coactivation in Wnt signalling |
| SRC | Tyrosine kinase activity and working SH2/SH3 domains (choanoflagellate Src) | The focal-adhesion, junction and PDZ partner network; receptor-specific pathways |
| ITGB1 / PTK2 | Integrin beta receptors with cation-site ligand binding and NPxY tails, and bona fide FAK, in *Capsaspora*. Choanoflagellates lost integrins and FAK | Binding to animal matrix ligands; counter-receptor cell-cell adhesion; all tissue roles. No functional FAK data exist outside animals |
| COL4A1 | The gene only, and only in the filasterean *Ministeria vibrans*: a canonical type IV collagen, upregulated during aggregation, in an amoeba with no basement membrane (PMID:28726632, 42265479). Absent from choanoflagellates and *Capsaspora* (PMID:28418331) | The basement membrane and the structural role of collagen IV in it; present with basement membranes in ctenophores, placozoans and homoscleromorph sponges. So COL4A1 is a valid control for function but not for gene presence (corrected 2026-10-01) |

**Evolutionary re-check of existing reviews (2026-10-01).** The five
reviews that predate this project (all COMPLETE) received an additive pass:
a sourced evolutionary-origin section in each gene's notes, a sentence in the
description, new references and suggested questions. No review actions
changed.

| Gene | Ancestral | Animal-specific | Notable |
|---|---|---|---|
| CDH1 | Cadherin repeats (calcium binding, inferred from the fold) | Classical cadherins and the beta-catenin-binding tail (PF01049, absent from all unicellular holozoans) | Track C Case 6: choanoflagellate cadherins inherit Bilateria-node junction terms |
| ABL1 | Tyrosine kinase activity (choanoflagellate MbAbl2 is constitutively active, PMID:26090675) | Myristoyl-cap autoinhibition; the F-actin- and DNA-binding C-terminus | Matches the SRC/CSK picture: an ancestral catalytic module with later regulation |
| MYC | Myc-Max heterodimerization and E-box binding (*Monosiga*, PMID:21571926) | Proliferation, apoptosis and oncogenic roles | A ribosome-biogenesis target signature is inferred in *Monosiga* and *Capsaspora* but untested |
| NOTCH1 | Domain modules only; CSL is present in *Capsaspora* without a receptor | Receptor, DSL ligands, MAML (eumetazoan) | One choanoflagellate (*Mylnosiga*) has a Notch-like domain order, so a choanozoan origin with loss is open |
| TP53 | A p53-family DNA-binding domain in choanoflagellates, *Capsaspora* and ichthyosporeans (untested); germline DNA-damage apoptosis in cnidarian p63 | Somatic tumour suppression (vertebrate) | No functional study of any unicellular p53-family protein exists |

### Track C: propagation audit

For each Track A/B family, pull the IBA and IEA annotations on
choanoflagellate and *Capsaspora* orthologs and classify each by where the
PAINT node sits (pre-Holozoa, Holozoa, Choanozoa, Metazoa) and whether the
term is a biochemical activity or a multicellular process. Candidate error
types from the prediction-review taxonomy: `TAXON_CONSTRAINT_VIOLATION` and
`PATHWAY_CONTEXT_IGNORED`. Per CLAUDE.md, an IBA carries a phylogenetic
judgement: the question is whether the target sits inside the clade that
inherited the function, not how many donors there are.

**Report:** [Propagation audit](ORIGINS_OF_MULTICELLULARITY/propagation-audit.md)
(2026-10-01). Of 36 propagated rows in the 11 Track A reviews, 7 were
down-graded, all TreeGrafter IEAs, through three mechanisms:
- animal-tissue IBDs on the LATS node PTN002390470 that includes
  choanoflagellates (regulation of organ growth);
- cross-family grafts (*Capsaspora* Warts into the citron/ROCK family; the
  *S. rosetta* yorkie candidate into the MAGI-related family);
- a fungal mannan term on couscous.

The cases are also written up for the
[TreeGrafter evaluation](TREEGRAFTER/holozoan-hippo-case-study.md).

**Upstream tickets.** [Twelve ready-to-file reports](ORIGINS_OF_MULTICELLULARITY/upstream-tickets/README.md):
- 7 to PANTHER/PAINT (the LATS node, the cadherin graft, the Warts and
  Yorkie family boundaries, the mannan node, the integrin-ITGBL1 graft, the
  CoBra subfamily and T-box node);
- 3 to UniProt (the ITGB1-FLNB PMID, the Rosetteless name, the vinculin NOT
  row);
- 1 to the GO ontology (organ-term taxon constraints; NTR rosette colony
  development);
- 1 TreeGrafter QC rule.

None is filed yet; the trackers are outside this repository.

### Track D: ontology gaps

- Is there a GO process term for clonal colony (rosette) development in a
  unicellular organism? Candidates to check include `GO:0007275` multicellular
  organism development and its parent `GO:0032501` multicellular organismal
  process. Check whether their definitions or taxon constraints exclude
  non-animals before using them, and draft an NTR only if nothing fits.
- Is bacterial induction of development (RIF-1 sulfonolipid
  [PMID:23066504]; the chondroitinase that induces mating
  [PMID:28867285 "Mating in the Closest Living Relatives of Animals Is Induced by a Bacterial Chondroitinase."])
  representable on the choanoflagellate side, or only as a process of the
  bacterium?

## Open questions

- Is rosetteless's C-type lectin domain needed for its function, and does
  "Lung surfactant protein A" get propagated to other choanoflagellate
  proteins by name rules?
- Which UniProt entry is the "integrin β2" of PMID:32857975?
- Do choanoflagellate cadherins (e.g. the *M. brevicollis* MBCDH set,
  PMID:18273011) carry IEA `cell-cell adhesion` or `adherens junction` terms,
  and is there evidence for either?

## Related projects

[DICTYOSTELIUM_DEVELOPMENT](DICTYOSTELIUM_DEVELOPMENT.md) (independent,
aggregative origin), [ECM](ECM.md), [MECHANOBIOLOGY](MECHANOBIOLOGY.md),
[IBA_REVIEW](IBA_REVIEW.md), [HOMOLOGY_PROPAGATION](HOMOLOGY_PROPAGATION.md),
[CEPHALOPOD](CEPHALOPOD.md) (another annotation desert).

---

# STATUS

2026-09-30: Track A priorities 1–3 reviewed (DRAFT).

- [x] GOA experimental-annotation census across Holozoa
- [x] Resolve UniProt accessions for rosetteless, jumble, couscous
- [x] Resolve accessions for *S. rosetta* hippo, warts, yorkie and *Capsaspora* coHpo, coWts, coYki
- [x] Resolve and review *S. rosetta* SrSeptin2/SrSeptin6, *Capsaspora* integrin β2 (CAOG_05058), vinculin (CAOG_05123) and Brachyury (CAOG_005512, our assignment) — DRAFT
- [x] `just fetch-gene SALRS <accession> --alias <name>` for Track A priorities 1–3 (works for unreviewed TrEMBL entries)
- [x] Review: rosetteless (F2U5Y1) — DRAFT
- [x] Review: jumble (F2TWH0) — DRAFT
- [x] Review: couscous (F2UJ78) — DRAFT
- [x] Review OSCPE VIN1 and TLN — DRAFT
- [x] Review CAPO3 coHpo, coWts, coYki — DRAFT
- [x] Review SALRS hippo, warts, yorkie — DRAFT
- [x] Track B batch 1: LATS1, STK3, YAP1, TEAD1, TLN1, VCL, TBXT, CSK — DRAFT
- [x] Track B batch 2: CTNNB1, SRC, ITGB1, PTK2, CTNNA1, COL4A1 — DRAFT
- [x] Track B: premetazoan pass on existing CDH1, ABL1, MYC, NOTCH1, TP53 (additive; no actions changed)
- [x] Upstream tickets drafted ([index](ORIGINS_OF_MULTICELLULARITY/upstream-tickets/README.md)); filing is pending
- [x] Track C propagation audit for the Track A genes: [report](ORIGINS_OF_MULTICELLULARITY/propagation-audit.md), cross-posted to the TREEGRAFTER project
- [x] Track C: extend the audit to the Track B human genes' IBA nodes ([Case 6 and extension table](ORIGINS_OF_MULTICELLULARITY/propagation-audit.md))
- [ ] Track D ontology check (started: NTR "rosette colony development" drafted in the rosetteless review)
- [ ] Deep research (falcon) for the three SALRS genes, once a provider key is available

# NOTES

## 2026-09-30

Created project. Census numbers come from `annotation_census.py` and will
drift as GOA updates; rerun before quoting them elsewhere. All PMIDs on this
page were checked against PubMed esummary, and all UniProt accessions against
the UniProt REST API. The *S. rosetta* locus-to-gene mapping comes from the
full text of PMID:25299189 (PTSG_03555 = Rosetteless) and PMID:30556809
(GenBank EGD72416 = jumble, EGD77026 = couscous).

Later the same day: reviewed rosetteless, jumble and couscous (SALRS, all
DRAFT). No deep-research provider key was available, so each gene has a
manual `-notes.md` built from the cached full text instead of a
`-deep-research-*.md` file; falcon deep research is still to do. Cached the
choanoflagellate papers under `publications/` (PMID:41037400 is abstract-only,
so the 2025 knockout phenotypes are not yet captured). Findings:

- **rosetteless**: NEW `GO:0031012` extracellular matrix (IDA). Core function
  `GO:0005201` extracellular matrix structural constituent is inferred from
  location plus phenotype, not measured, and is kept out of the annotation
  rows. UniProt's name "Lung surfactant protein A" comes from the genome
  project's EMBL record and should be changed.
- **jumble**: NEW `GO:0005794` Golgi apparatus (IDA, tagged protein at the
  Golgi position; the non-functional L305P protein is retained in the ER).
  InterPro finds no domain; the glycosyltransferase call rests on fold
  recognition only, so the MF appears only in core_functions.
- **couscous**: 7 IEA rows. Accepted alpha-1,2-mannosyltransferase activity,
  glycosyltransferase activity, glycoprotein biosynthetic process and
  membrane. Golgi apparatus and Golgi membrane left UNDECIDED, because the
  tagged protein was "clearly not localized to the Golgi" (PMID:30556809).
  Removed mannan biosynthetic process.
- None of the three was given a rosette-development process term: jumble and
  couscous fail the participation test (necessity only, targets unknown), and
  GO has no suitable term. The NTR "rosette colony development" is in the
  rosetteless review, where the protein is a structural part of the colony
  matrix.

## 2026-10-01

Reviewed the *Capsaspora* Hippo kinase cascade and the sponge adhesome pair
(all DRAFT, manual notes because no deep-research key is available).

- **coWts: first Track C case.** TreeGrafter places coWts (A0A0D2VGR4) in
  PTHR22988:SF71 "CITRON RHO-INTERACTING KINASE", the ROCK/MRCK/citron family,
  while human LATS1/2 are in PTHR24356. Drosophila wts is also in PTHR22988, so
  the Warts/LATS clade is split across two PANTHER families. coWts therefore
  inherits cytoskeletal terms from a ROCK/citron node and misses the LATS-node
  hippo signaling IBA. Actomyosin structure organization was removed,
  cytoskeleton terms marked over-annotated, and hippo signaling added (IMP,
  coYki is nuclear in coWts-/- cells; PMID:38517944). The *S. rosetta* Warts
  (F2U943) is in PTHR24356, the LATS family.
- **coHpo:** signal transduction modified to hippo signaling; protein
  tetramerization removed (a p53-like tetramerisation fold match on the SARAH
  domain, which forms dimers).
- **coYki:** all five propagated rows hold, including hippo signaling and
  transcription coactivator activity; NEW DNA-binding transcription factor
  binding (IPI, co-IP with coSd). Its knockout shows no proliferation effect,
  so no proliferation term. A negative result for Track C.
- **Sponge VIN1/TLN:** both protein binding rows replaced by talin binding and
  vinculin binding. VIN1 binds F-actin only with talin peptide present; NEW
  cell-cell junction (IDA, endogenous protein at epithelial contacts). TLN
  cell-cell adhesion modified to cell-matrix adhesion.
- Resolved *S. rosetta* hippo, warts, yorkie from the bioRxiv preprint of
  PMID:41037400. The preprint full text could not be cached (bioRxiv rate
  limits; the Europe PMC copy returns 403) at first; a later retry cached the
  version 1 PDF. The PTSG locus IDs appear only in version 2 (read from
  bioRxiv XML, not cached); this is recorded in each gene's notes.
- **S. rosetta warts: second Track C case.** Its IBA rows come from the
  Metazoa-Choanoflagellida speciation node PTN002390470 of the LATS family.
  That node carries animal tissue-level terms: regulation of organ growth was
  removed (choanoflagellates have no organs; GO's taxon constraints do not
  exclude them), and positive regulation of apoptotic process and G1/S
  transition were marked over-annotated. hippo signaling was accepted. *M.
  brevicollis* Warts receives the same rows. This is a node-placement issue
  for the PAINT curators, not a family error.
- **S. rosetta yorkie: third Track C case.** TreeGrafter grafts F2UDK1 onto an
  Ecdysozoa node of the MAGI-related family PTHR10316, a family-placement
  error like coWts. Our motif scan (yorkie-bioinformatics/) finds four Warts
  phosphorylation motifs but no TEAD-interface motif, and PANTHER classes a
  different WW protein, F2U5K0, in the YAP1 family; the preprint nonetheless
  names PTSG_06057 (F2UDK1) as yorkie. Orthology needs a proper phylogeny.
- **S. rosetta hippo:** generic kinase and signal-transduction rows kept;
  hippo signaling not added, since hippo knockouts do not phenocopy warts
  (normal rosette size) and nothing places Hippo upstream of Warts in S.
  rosetta.
- **Track B batch 1** (eight human genes, table in Track B). Points for a
  human curator:
  - **VCL.** We removed the NOT actin binding IDA row (PMID:7816144). The
    cited abstract itself says the F-actin site is masked by head-tail
    autoinhibition, not absent.
  - **STK3.** The InterPro "protein tetramerization" row is marked
    over-annotated, whereas the same row on *Capsaspora* coHpo was removed.
    Human MST2 does sit in a 2:2 SAV1 complex, but SAV1 makes the contact
    that joins the two pairs.
  - **TBXT.** NEW notochord development (IMP, sacral agenesis variant;
    mouse T carries the term).
  - **CSK.** Choanoflagellate Src/Csk papers cached (PMID:16873552,
    18390552, 28939764).
- **Track B batch 2 and the re-check of existing reviews** (tables in Track B).
  - ITGB1 turned up a GOA miscitation: PMID:10676904, a bovine oocyte paper,
    is cited for ITGB1-FLNB. The intended paper is PMID:16076904, a digit
    transposition. Recorded as a `replacement` and written up in
    [MISCITATIONS](MISCITATIONS.md).
  - The CDH1 re-check found Track C Case 6: three *S. rosetta* cadherins
    graft onto a PAINT node restricted to Bilateria and inherit 30
    junction/catenin rows. Added to the propagation audit and the TreeGrafter
    case study.
  - Process note: a review agent ran `git stash` / `pop` mid-run, briefly
    removing other agents' uncommitted edits. All edits were recovered and
    verified against the stash before committing.
  - The TP53 agent observed that `just validate` accepted a slightly
    paraphrased quote ("UV irradiation" for "ultraviolet (UV) irradiation"),
    so the substring matching appears to tolerate small differences. The quote
    was corrected to the exact text.
- **Correction: collagen IV outside animals.** The COL4A1 review first stated
  that collagen IV is absent from all unicellular relatives (following
  PMID:28418331). A 2017 genome survey found a canonical type IV collagen gene
  in the filasterean *Ministeria vibrans* (PMID:28726632), and a 2026 study
  found it upregulated during *Ministeria* aggregation (PMID:42265479). The
  COL4A1 review now records this with a `finding_review` (OVERTURNED), and the
  Track B tables were corrected. Basement-membrane function remains
  animal-specific.
- **Remaining Track A genes and tickets.**
  - **Accessions.** Resolved the *S. rosetta* septins (PMID:30281390) and
    *Capsaspora* integrin beta 2 and vinculin (from the preprint methods,
    once bioRxiv allowed the download). We assigned *Capsaspora* Brachyury
    with our own analysis; the paper's "CoTbx3" turned out to belong to a
    new Tbx7 class, so it is not mapped.
  - **Reviews.** All five are DRAFT.
  - **New propagation cases.** Two more TreeGrafter grafts of unicellular
    proteins onto animal-only nodes: the integrin-ITGBL1 graft (Case 7) and
    the T-box node's "cell fate specification" (Case 8). With the cadherin
    case, that makes this the commonest failure mode in the audit. Both are
    added to the audit, the TreeGrafter case study and the tickets (now 12).
