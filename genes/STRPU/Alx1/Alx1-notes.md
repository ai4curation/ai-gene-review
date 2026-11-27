# Alx1 (Strongylocentrotus purpuratus, UniProt Q7Z0W3) - curation notes

## Identity

- UniProt Q7Z0W3 (`Q7Z0W3_STRPU`, unreviewed/TrEMBL, 430 aa) is the S. purpuratus
  Alx1 protein deposited by the Ettensohn lab (EMBL AAP34698.1); its single RX
  line is PMID:12756175, the paper that named the gene. UniProt's automated
  RecName "Homeobox protein aristaless-like 4" is a family-level ARBA name and
  should not be read as a claim that this is the Alx4 paralogue: the sea urchin
  genome has a separate alx4 gene, and Alx1 is distinguished from Alx4 by the
  D2 domain (see below). The community symbol is `Alx1` (older literature also
  writes `alx-1`).
- Domain architecture (UniProt FT): paired-class homeodomain at 116-176
  (PROSITE PS50071), C-terminal OAR motif at 407-420, large N-terminal
  disordered region. PANTHER PTHR24329 (label not written from memory here).

## Place in the endomesoderm GRN

Alx1 is one of the four regulatory genes (with ets1, tbr, tel) plus delta that
are the direct targets of the Pmar1/HesC double-negative gate and that initiate
the skeletogenic (large micromere / primary mesenchyme cell, PMC) regulatory
state.

- Discovery and expression: [PMID:12756175 "We have identified a new and essential
  component of the gene network that controls large micromere specification, the
  homeodomain protein Alx1." ... "Alx1 is expressed exclusively by cells of the
  large micromere lineage beginning in the first interphase after the large
  micromeres are born."]
- Upstream control: [PMID:12756175 "Expression of Alx1 is cell autonomous and
  regulated maternally through beta-catenin and its downstream effector, Pmar1."]
- Double-negative gate: [PMID:17636127 "There are eight targets predicted for it
  in the GRN, of which the most important for present purposes are the genes
  encoding the Delta ligand and three regulatory genes, tbr , ets1 , and alx1 .
  These three genes lie upstream of all the rest of the micromere regulatory
  apparatus."] HesC knockdown derepresses alx1 globally: [PMID:17636127 "By 12 h
  after fertilization, the amount of transcript of delta and alx1 had increased
  4- to 7-fold above normal in the two experiments performed"].
- GRN summary: [PMID:18413610 "The five primary target regulatory genes of the
  double negative gate are indicated in Fig. 2 A . They are four essential
  regulators of downstream micromere lineage function: alx1 ( 29 ), ets1 ( 9 , 33 ),
  tbr ( 34 , 35 ), and tel ( 9 )"].

## cis-regulatory control of alx1 (Damle & Davidson 2011)

- [PMID:21723273 "The results entirely confirm the double negative gate control
  system at the cis-regulatory level, including definition of the functional
  HesC target sites"]. Drivers: Ets1 initially, then Alx1 itself plus Ets1.
- Autoregulation: [PMID:21723273 "we demonstrate that Alx1 protein is both an
  immediate, direct, auto-activator, and at higher concentrations an
  auto-repressor, and reveal the biochemical and gene-regulatory network
  architectural features that permit these opposing roles"]. The auto-repression
  at high concentration was attributed to dimerization (synthetic construct
  experiment).

## Function: loss- and gain-of-function

- Knockdown: [PMID:12756175 "Morpholino studies demonstrate that Alx1 is
  essential at an early stage of specification and controls downstream genes
  required for epithelial-mesenchymal transition and biomineralization."]
- Skeleton-minus and ingression phenotypes: [PMID:18413610 "The proper function
  of most of these regulatory genes is essential for expression of skeletogenic
  differentiation genes, and interference with their expression produces a
  skeleton-minus phenotype" ... "both it and alx1 target genes are required for
  ingression of the skeletogenic cells"].
- Exclusion of the alternative (non-skeletogenic mesoderm / pigment) fate:
  [PMID:18413610 "a role of the micromere lineage regulator alx1 is to repress
  gcm in that lineage. Thus if alx1 expression is blocked, expression of gcm and
  pks genes spreads across the vegetal plate, including the micromere domain" ...
  "Conversely, if alx1 mRNA is introduced into the egg, gcm expression is
  dramatically reduced"]. Whether gcm repression is direct is not established.
- Summary of MO/misexpression (eLife 2017, done in L. variegatus but stated for
  sea urchin Alx1 generally): [PMID:29154754 "Perturbation of alx1 function using
  antisense morpholinos (MOs) blocks PMC specification while misexpression of
  alx1 results in the ectopic activation of the skeletogenic program in non-PMC
  lineages"]. Structure-function: Domain 2 (D2), a 41-aa exonized motif absent
  from Alx4, is essential for skeletogenic function; Alx4 is not interchangeable
  unless D2 is inserted.

## Direct targets and DNA binding

- ChIP-seq in S. purpuratus: [PMID:31331943 "we used genome-wide ChIP-seq to
  identify" ... "Alx1-binding sites and direct gene targets" ... "many
  terminal differentiation genes receive direct transcriptional inputs from
  Alx1" ... "intermediate transcription factors previously shown to be downstream
  of Alx1 all receive direct inputs from Alx1"]. 18/23 tested ChIP peaks were
  active CRMs in GFP reporter assays, and in a representative CRM "a conserved,
  palindromic Alx1-binding site was essential for expression".
- Genome-wide functional targets (RNA-seq after Alx1 MO): [PMID:24496631 "We
  carried out genome-wide analysis of (1) functional targets of Ets1 and Alx1, two
  pivotal, early transcription factors in the PMC GRN"].
- DNA-binding biochemistry: [PMID:34157281 "Alx1 and Alx4 contain glutamine-50
  paired-type homeodomains, which interact preferentially with palindromic
  binding sites" ... "We find that Alx1 forms dimeric complexes on TAAT-containing
  half sites by" ... "a mechanism distinct from the well-known mechanism of
  dimerization on"]. EMSA with purified Flag-Alx1 on the Sp-mtmmpb CRM: "we show
  that Alx1 binds directly to several half sites. Moreover, Alx1 forms dimeric
  complexes at these sites". Two half-sites are essential for PMC-specific
  reporter activity of the Sp-mtmmpb CRM. Alx1 "positively regulates the
  transcription of most biomineralization genes expressed by these cells".
- Review: PMID:35152981 (Ettensohn, Guerrero-Santoro, Khor 2022, Curr Top Dev
  Biol) - Alx1 as "key regulator of skeletal cell identity throughout the phylum".

## Curation decisions (see the ai-review.yaml)

- Electronic rows: the InterPro/UniRule homeobox-derived MF/CC/BP terms are all
  consistent with the literature. GO:0048513 animal organ development (ARBA) is
  a vertebrate-Alx-family generalization; the embryonic larval skeleton is not an
  organ in the GO sense, so it is marked as over-annotated.
- NEW: GO:0001228 (activator, RNA pol II) IDA from the alx1 auto-activation
  cis-regulatory analysis and the Alx1-site-dependent CRM reporters;
  GO:0000978 IDA from EMSA/ChIP-seq; GO:0042803 IDA from EMSA dimer complexes;
  GO:0045944 IDA; GO:0007501 mesodermal cell fate specification IMP (PMC is the
  skeletogenic mesoderm lineage); GO:0010718 positive regulation of EMT IMP;
  GO:0070169 positive regulation of biomineral tissue development IMP.
- Not proposed: GO:0001227 repressor activity (gcm repression and auto-repression
  are perturbation-level, no direct repressive cis-regulatory test in S.
  purpuratus); left as a suggested question.
- No GO-CAM contains this gene (gocams/index.tsv has no Q7Z0W3 entry; the only
  "alx1" hit is the unrelated S. pombe gene).
