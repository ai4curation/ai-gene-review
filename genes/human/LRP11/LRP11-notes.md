# LRP11 review notes

## Identity, topology, and sequence evidence

Human LRP11 is UniProtKB Q86VZ4, a 500-aa precursor. The reviewed record calls it
a single-pass type-I membrane protein; it does **not** specify plasma membrane
[file:human/LRP11/LRP11-uniprot.txt "SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass type I"].
The predicted topology is a signal peptide (1-37), extracellular region (38-450),
one transmembrane helix (451-473), and a short cytoplasmic tail (474-500)
[file:human/LRP11/LRP11-uniprot.txt "FT   TRANSMEM        451..473"].

The extracellular region contains MANSC, PKD, and one LDL-receptor class-A module
[file:human/LRP11/LRP11-uniprot.txt "FT                   /note=\"LDL-receptor class A\""].
This establishes receptor-like architecture, not a specific ligand or an LDL-uptake
function. The UniProt similarity statement is only family-level evidence
[file:human/LRP11/LRP11-uniprot.txt "Belongs to the LDLR family."]. General functions
of LRP1, LRP5/6, LRP8, VLDLR, or SORL1 must therefore not be transferred to LRP11.
In particular, older literature often calls SORL1/SORLA “LR11”; that is a different
gene and must not be confused with HGNC LRP11.

## Isoforms

The reviewed record lists two splice isoforms
[file:human/LRP11/LRP11-uniprot.txt "Event=Alternative splicing; Named isoforms=2;"].
Isoform 1 is the displayed 500-aa sequence. Isoform 2 replaces residues 205-237 and
lacks residues 238-500, thereby removing the canonical PKD/LDLRA region,
transmembrane helix, and cytoplasmic tail. The underlying citation is the Mammalian
Gene Collection resource, whose aim was full-ORF cDNA sequencing rather than
functional characterization [PMID:15489334 "designed to generate and sequence a publicly accessible cDNA resource containing"].
The existence of cDNA isoforms does not establish their endogenous protein abundance
or distinct functions.

## Existing human experimental annotation: beta-arrestin screen

PMID:17620599 is a global beta-arrestin interactome experiment, not an LRP11-focused
study. It reports hundreds of mass-spectrometry interactors
[PMID:17620599 "102 interacted with both beta-arrestins."] and states that only a
random subset of new partners was validated
[PMID:17620599 "The binding of 16 randomly selected newly identified beta-arrestin"].
The cached abstract/main text does not name LRP11; the protein lists and validation
details reside in supplementary tables that are not present in the project cache.
Therefore the IMP phosphoprotein-binding annotation and the dependent IC
plasma-membrane annotation cannot be judged from PMID:17620599 alone. However,
PMID:38272565 used LRP11 blocking antibody on intact T cells, independently
supporting an accessible cell-surface pool; the
plasma-membrane row is therefore accepted. The beta-arrestin-screen hit does not by itself
show that LRP11 binds a phosphorylated partner, and the study explicitly
places interactors in multiple compartments
[PMID:17620599 "in the cytoplasm, but also in the nucleus as well as other subcellular"].

## Mouse stress study and orthology-transfer boundary

The seven human stress-process IEAs all transfer from mouse Lrp11 (Q8CB67) through
Ensembl Compara. The actual donor paper is PMID:25262641. It measured Lrp11 mRNA and
protein in mouse amygdala after stress
[PMID:25262641 "investigate the expression variation of Lrp11 in amygdala tissue after exposure"].
Live QuickGO donor inspection on 2026-08-19 showed that each of the seven mouse
Q8CB67 source rows uses IEP with PMID:25262641. IEP is valid evidence for a response
annotation; the concern is instead the second-step transfer to human, the single-tissue
mouse context, and the accessible abstract's failure to identify which individual
stress paradigm supports each term.
A local PANTHER lookup fetched on 2026-08-19 returned human Q86VZ4 and mouse Q8CB67
together in PTHR46876:SF1
[file:interpro/panther/PTHR46876/PTHR46876-entries.csv, "Q86VZ4,Low-density lipoprotein receptor-related protein 11,protein,9606,Homo sapiens,Homo sapiens (Human),LRP11,500,PTHR46876:SF1,LOW-DENSITY LIPOPROTEIN RECEPTOR-RELATED PROTEIN 11,True"]
[file:interpro/panther/PTHR46876/PTHR46876-entries.csv, "Q8CB67,Low-density lipoprotein receptor-related protein 11,protein,10090,Mus musculus,Mus musculus (Mouse),Lrp11,483,PTHR46876:SF1,LOW-DENSITY LIPOPROTEIN RECEPTOR-RELATED PROTEIN 11,True"].
The authors observed higher abundance in stressed mice
[PMID:25262641 "We found the quantity of Lrp11 was more obvious in stress models than"].
That expression-response evidence is informative in mouse amygdala but is too
underspecified for seven term-level human orthology transfers.

The paper also depleted Lrp11 in HEK293T and SH-SY5Y cells and observed altered
expression of Xpnpep1, Maneal, Pgap1, and Uprt
[PMID:25262641 "influence of Lrp11 depletion on the expression of Xpnpep1, Maneal, Pgap1 and"].
This supports a candidate regulatory network but still does not establish the seven
specific stress processes in human LRP11. Accordingly, those transfers are marked
over-annotated rather than treated as core functions.

## Direct primary studies and biological scope

Human cervical-cancer experiments show that LRP11 knockdown reduced proliferation,
migration, and invasion in SiHa and CaSki cells and slowed xenograft growth
[PMID:31507330 "The silencing of LRP11 in SiHa"]. These are direct perturbation
phenotypes, but they are cancer-context outcomes and do not identify a normal ligand
or proximal receptor activity.

In human prostate-cancer cell lines, gain/loss experiments placed LRP11 upstream of
beta-catenin-dependent PD-L1 expression
[PMID:31865764 "LRP11 induced PD-L1 expression through β-catenin signalling."].
LRP11 overexpression also suppressed Jurkat-cell behavior in coculture, and antibody
blockade reversed the effect [PMID:31865764 "The effects of LRP11 could be blocked by"].
Again, this is a disease-context regulatory phenotype rather than a settled normal
core function.

PMID:38272565 supplies the strongest ligand-linked mechanism: a chimeric-receptor
screen reported that LRP11 interacted with LDL and activated TCF1
[PMID:38272565 "we showed that LRP11 interacted with LDL and activated TCF1."], with
MAPK13 placed between receptor activation and TCF1 phosphorylation
[PMID:38272565 "Then, MAPK13 phosphorylates TCF1, leading"]. The species boundary is
essential: the receptor constructs used mouse genes
[PMID:38272565 "The sequence encoding the extracellular portion of the mouse-indicated genes"],
the in-vivo tumor experiments were in mice, and only selected assays used human PBMCs
[PMID:38272565 "Human peripheral blood mononuclear cell (PBMC) were collected"].
This supports a context-specific LDL-Lrp11-MAPK13-TCF1 axis in T cells but does not
yet justify transferring a generic LDL-receptor/lipoprotein-endocytosis function to
human LRP11.

## Working synthesis boundary

Secure statements at this stage are: LRP11 is a type-I membrane protein with MANSC,
PKD, and one LDLRA module; two cDNA isoforms are recorded; direct studies connect it
to tumor-cell and immune-cell signaling contexts; and a mouse-dominant study proposes
LDL as a ligand. The normal human tissue ligand, trafficking itinerary, biochemical
binding specificity, isoform expression, and physiological process remain unresolved.
