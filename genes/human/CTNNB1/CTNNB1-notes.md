# CTNNB1 (human, P35222) - curation notes

**Automated deep research was unavailable** (no deep-research provider keys in this
environment). These notes were written by hand from the cached publications in
`publications/` (many are abstract-only; see `full_text_available:`), the UniProt
record, the sister reviews of human VCL, sponge VIN1 and human CDH1, and a small
UniProt/PANTHER census in `CTNNB1-bioinformatics/`. No `-deep-research-*.md` file
exists for this gene.

## Core molecular functions

### 1. Wnt/TCF transcriptional coactivator (nuclear pool)

- Coactivator of LEF/TCF [PMID:11751639 "beta-catenin, a dedicated coactivator of LEF/TCF enhancer-binding proteins"];
  [PMID:11751639 "recombinant beta-catenin strongly enhances binding and transactivation by LEF-1 on chromatin templates in vitro"].
- TCF4 activity depends on beta-catenin [PMID:9065401 "hTcf-4 transactivates transcription only when associated with beta-catenin"];
  constitutive complexes in APC-/- cells [PMID:9065401 "Nuclei of APC-/- colon carcinoma cells were found to contain a stable beta-catenin-hTcf-4 complex that was constitutively active"].
- Structure of the TCF4-beta-catenin complex [PMID:11713476 "it interacts with the Adenomatous polyposis coli (APC) protein and TCF/Lef family transcription factors"].
- BCL9-Pygopus recruitment [PMID:17052462 "Stimulation of the Wnt pathway leads to the association of beta-catenin with Tcf and BCL9 in the nucleus"];
  [PMID:11955446 "Wnt transduction is mediated by the association of beta-catenin with nuclear TCF DNA binding factors"].
- CBP/p300 [PMID:21751375 "p300/CBP (CREB-binding protein) is recruited by nuclear β-catenin to regulate a wide array of T-cell factor (TCF)-dependent gene expression"].
- Other DNA-binding partners: FOXO [PMID:15905404 "beta-Catenin binds directly to FOXO and enhances FOXO transcriptional activity in mammalian cells"];
  nuclear receptors [PMID:22187462 "The LRH-1 binding site in β-catenin is also required for association with androgen receptor"].
- ICAT blocks TCF binding but not cadherin binding [PMID:12408824 "We show that ICAT selectively inhibits beta-catenin/Tcf binding in vivo, without disrupting beta-catenin/cadherin interactions"].

### 2. Cadherin and alpha-catenin binding (junctional pool)

- Binds cadherins [PMID:11713476 "The multifunctional protein beta-catenin is important for cell adhesion, because it binds cadherins"];
  links VE-cadherin to the cytoskeleton [PMID:18287330 "linking the VE-cadherin junction complex to the cytoskeleton"].
- Stabilizes the E-cadherin complex [PMID:18593713 "Smad7 increases the stabilized beta-catenin to form a complex with E-cadherin and stabilizes the E-cadherin-beta-catenin complex"];
  surface E-cadherin via vinculin [PMID:20086044 "an interaction between beta-catenin and vinculin is crucial for stabilizing E-cadherin at the cell surface"].
- Alpha-catenin binding through the N-terminal half [PMID:7890674 "although the amino-terminal half independently binds alpha-catenin"];
  reciprocal site on alpha-catenin [PMID:9264463 "Here we have now identified the reciprocal complementary binding site in alpha-catenin which mediates its interaction with beta-catenin and plakoglobin"].

### Regulation (destruction complex)

- APC binding [PMID:8638126 "The APC protein binds to the cellular adhesion molecule beta-catenin"];
  GSK3/Axin [PMID:17318191 "Axin/GSK3beta binding to beta-catenin and its subsequent S/T phosphorylation"].
- SCF(beta-TrCP) recognition [PMID:12820959 "The F box protein beta-TrCP1 recognizes the doubly phosphorylated DpSGphiXpS destruction motif, present in beta-catenin and IkappaB"].
- Oncogenic stabilizing mutations [PMID:9065402 "colorectal tumors with intact APC genes were found to contain activating mutations of beta-catenin that altered functionally significant phosphorylation sites"].

### Peripheral functions

- PDZ-binding motif [PMID:17242191 "such as the one between the β-catenin PDZ motif and the PDZ2 domain"];
  proteome-scale PDZ affinity map [PMID:36115835 "both containing PBMs that detectably bound to PDZs in our quantified interactome"].
- Centrosome [PMID:18086858 "We show that beta-catenin binds to and is phosphorylated by Nek2"];
  [PMID:20300119 "Wnt/β-catenin signalling and conductin regulate centrosomal cohesion by altering the phosphorylation status of β-catenin at the centrosomes"].
- PML SUMOylation [PMID:22155184 "β-catenin inhibited Ran-binding protein 2-mediated SUMOylation of PML-IV"].

## GO-CAM

`gocams/index.tsv` lists one CTNNB1 activity: model 62900b6400001630 "PTEN in excitatory
hippocampal synapse long-term depression (Human)", activity
gomodel:62900b6400001630/62900b6400001715, enabled by CTNNB1 (ISS from rat RGD:70487):
GO:0003713 transcription coactivator activity, part of GO:0045944 positive regulation of
transcription by RNA polymerase II, occurring in GO:0000785 chromatin. This model is the source of the
ISS rows for chromatin, transcription coactivator activity (RGD:70487) and long-term
synaptic depression. The MF typing agrees with core function 1.

## Annotation review summary (723 rows)

- **Protein binding (335 IPI rows).** Following repository policy:
  - MODIFY where the partner defines a specific binding function: cadherins to cadherin
    binding, alpha-catenins to alpha-catenin binding, TCF/LEF/SOX/FOXM1/RUNX3/NF-kappaB
    and other DNA-binding factors to DNA-binding transcription factor binding, nuclear
    receptors to nuclear receptor binding, protein kinases (GSK3B, SRC, ABL1, NEK2, TNIK,
    RTKs) to protein kinase binding, PTPs to protein phosphatase binding, beta-TrCP and
    other E3s to ubiquitin protein ligase binding, PDZ proteins to PDZ domain binding,
    CBP/p300 to histone acetyltransferase binding, HDAC6 to histone deacetylase binding,
    and BCL9/BCL9L, TBL1/TBLR1, parafibromin, MLLT10, CITED1, YAP/TAZ to transcription
    coregulator binding.
  - REMOVE otherwise. This includes the destruction-complex scaffolds APC, Axin and AMER1
    (captured by the destruction complex CC rows), ICAT (captured by the beta-catenin-ICAT
    complex row) and the neurodegeneration Y2H screen PMID:32814053.
  - Two specific REMOVE cases:
    - PMID:12370829 PTPRC: the abstract reports that CD45 did *not* bind catenins
      [PMID:12370829 "Catalytic domains of the tyrosine phosphatases PTP-PEST, CD45, and PTPbeta did not interact with proteins of the catenin family to detectable levels"].
    - PMID:19433865 HDAC1/2/APPL: the association goes through Reptin
      [PMID:19433865 "The ability of Reptin to bind both β-catenin and HDAC1 further suggested the formation of a β-catenin-Reptin-HDAC1 complex at the promoter"].
- **Substrate-type process rows removed** (participation test): protein polyubiquitination
  and proteasome-mediated catabolism (PMID:29374064), and regulation of protein
  ubiquitination (PMID:15829978). Beta-catenin is the substrate in all three
  [PMID:29374064 "IRF2BPL in turn interacted with β-catenin, increasing its ubiquitination and degradation"].
- **MODIFY of non-binding rows:**
  - Obsolete GO:0030331 nuclear estrogen receptor binding to GO:0016922. QuickGO
    confirms the obsolescence and gives GO:0016922 as the consider term.
  - GO:0070602 regulation of centromeric sister chromatid cohesion to GO:0030997
    regulation of centriole-centriole cohesion. The cited paper (PMID:20300119) is
    about centrosome cohesion.
  - GO:0019900 kinase binding with GSK3B to protein kinase binding.
  - Enzyme binding with HDAC6 to histone deacetylase binding.
- **UNDECIDED:** GO:0045892 negative regulation of DNA-templated transcription (IMP,
  PMID:19653274). The abstract says the LEF-1 isoform effect is beta-catenin-independent
  [PMID:19653274 "Forced expression of Lef-1 Deltaexon VI inhibited E-cadherin expression in a beta-catenin-independent way"],
  and the full text is not cached.
- **Over-annotated:**
  - Chromatin binding (beta-catenin has no DNA-binding domain).
  - Detection of mechanical stimulus and detection of muscle stretch.
  - Wnt signalosome.
  - Negative regulation of canonical Wnt signaling.
  - Response to xenobiotic stimulus (sulindac) and response to indole-3-methanol (both
    expression-change evidence).
  - Bicellular tight junction, focal adhesion (HDA) and extracellular exosome (HDA).
- **Non-core:** the many mouse-derived developmental, neural and synaptic terms. These
  are downstream outputs of Wnt/TCF target genes or tissue-specific instances of
  junctional localization.
- **IBA rows** (PAINT node PTN001153077): cadherin binding, alpha-catenin binding, catenin
  complex, adherens junction, cell-cell adhesion, transcription coactivator activity,
  canonical Wnt signaling, nucleus/cytoplasm, nuclear receptor binding, protein
  phosphatase binding and positive regulation of Pol II transcription. All accepted.
  Human CTNNB1 among the donors is expected, not circular. The donors are bilaterian
  (fly arm, worm hmp-2/bar-1/sys-1, mouse, zebrafish, human JUP).

## Premetazoan evidence: ancestral vs animal-specific

**Bioinformatics** (`CTNNB1-bioinformatics/RESULTS.md`):
- PANTHER PTHR45976, the beta-catenin/Armadillo family containing CTNNB1 as SF4, has 4921
  metazoan UniProt members.
- It has 0 members in choanoflagellates, Filasterea, Ichthyosporea or Dictyostelium. The
  only 2 non-metazoan hits are isolated plant entries, probably contamination.
- Dictyostelium Aardvark (Q54I71) is classified in PTHR22895 "ARMADILLO REPEAT-CONTAINING
  PROTEIN 6", not in the beta-catenin family.

**Literature (all read in the cache):**
- *Beta-catenin as an animal-specific family:* catenin beta is a core animal-specific
  family [PMID:29848444 "this set of genes includes seven from the Wnt pathway (including Frizzled, Dishevelled, TCF/LEF and β-catenin)"].
  Wnt-pathway genes are largely absent outside animals
  [PMID:20883218 "Most of these genes are not detected in the choanoflagellate and other nonmetazoan eukaryotic genomes"].
- *The armadillo fold is older* [PMID:23481191 "the cadherin repeat domain and the armadillo repeat domain, predate metazoans"].
- *Dictyostelium (Amoebozoa, an independent origin of multicellularity):*
  - Aardvark acts at actin-associated junctions and separately in signalling
    [PMID:11130075 "We have isolated a gene encoding a beta-catenin homologue, aardvark, which is a component of the junctional complex, and, independently, is required for cell signalling"].
  - The authors concluded [PMID:11130075 "the dual role of beta-catenin in cell-cell adhesion and cell signalling evolved before the origins of metazoa"].
  - The later study showed that an alpha-catenin ortholog binds Aardvark to build a
    polarized epithelium without cadherins
    [PMID:21393547 "Although D. discoideum lacks a cadherin homolog, we identify an α-catenin ortholog that binds a β-catenin-related protein"];
    [PMID:21393547 "the role of the catenins in cell polarity predates the evolution of Wnt signaling and classical cadherins"].
  - Aardvark's signalling role does not go through GSK-3, i.e. it is not Wnt-like
    destruction-complex signalling
    [PMID:12128211 "This process does not involve the kinase GSK-3"].
- *Classical cadherins are an animal innovation*
  [PMID:22837400 "the later appearance of classical cadherins coincides with metazoan origins"].
  - The sponge beta-catenin keeps the residues that bind cadherin
    [PMID:22837400 "Oc_bcat has two lysine residues (homologous to positions K312 and K435 in mouse) required for the interaction of mouse β-catenin with E-cadherin"].
  - A Y2H screen with the sponge beta-catenin recovered the sponge classical cadherin (same paper).
- *Nuclear signalling is ancient within animals:* cnidarian nuclear beta-catenin
  specifies endoderm
  [PMID:14647383 "translocated into nuclei in cells at the site of gastrulation and used to specify entoderm"].
- *Sponge vinculin* did not bind a beta-catenin peptide
  [PMID:29880641 "Moreover, Op vinculin bound talin but not β-catenin"].
  The VCL review notes that this peptide was the alpha-catenin-binding region, so the
  result does not test the human vinculin-beta-catenin N-terminal interface.

**Synthesis:**
- Ancestral (pre-animal), in the broad sense: an armadillo-repeat catenin working with
  alpha-catenin to organize cell polarity and junctions. The evidence comes from
  Dictyostelium. Whether Aardvark shares descent with beta-catenin or converged on this
  role is unresolved: PANTHER does not place it in the beta-catenin family, and no
  beta-catenin-family protein is classified in unicellular holozoans.
- Animal-specific:
  - The beta-catenin family itself (by current classification).
  - Binding of classical cadherins (the partners arise with animals, though present in
    sponges).
  - TCF/LEF-dependent transcriptional coactivation in Wnt signalling (TCF/LEF and Wnt are
    animal-specific).
  - All of the developmental, tissue and synaptic process terms.
- Both the junctional and the Wnt/TCF roles were present in the last common ancestor of
  animals (sponge cadherin-binding residues; sponge Wnt-pathway components; cnidarian
  nuclear beta-catenin).
- Unverified background, not cited: whether ctenophores have a TCF-coupled beta-catenin.
  I did not read primary data on this.
