# Bra (SpBra, brachyury) - Strongylocentrotus purpuratus - curation notes

## Identity of the UniProt accession

- UniProt A0A7M7PDZ1 is a TrEMBL genome-project entry ("T-box transcription factor T
  homolog", alt name "Brachyury protein homolog"), 503 aa, PE=4, with no literature link.
  Its xrefs are RefSeq XP_030850405.1 / XM_030994545.1 (transcript variant X2) and
  GeneID 576774 (LOC576774). The sibling accession A0A7M7PHL2 (504 aa) is RefSeq
  XP_030850404.1 / XM_030994544.1 (transcript variant X1) of the same GeneID 576774, so
  the two accessions are two predicted isoforms of one locus, not two genes.
- NCBI Gene 576774 is annotated "T-box transcription factor T homolog | brachyury protein
  homolog" on scaffold NW_022145607.1. A GenBank nuccore search for S. purpuratus T-box
  genes finds only one "T-box transcription factor T homolog" locus (LOC576774); the other
  T-box loci in the genome are Tbx2/3, TBX3 (LOC592389), TBX1 (LOC585491) and H15
  (LOC100889015). S. purpuratus EST clones (e.g. CX697415, CX691184) from the same locus
  were annotated "similar to SW:BRAC_HEMPU Q25113 BRACHYURY PROTEIN HOMOLOG" (the
  Hemicentrotus HpTa protein).
- Domain evidence on the record itself: InterPro IPR002070 "TF_Brachyury", PRINTS
  PR00938 BRACHYURY, CDD cd20192 T-box_TBXT_TBX19-like, FunFam 2.60.40.820:FF:000002
  "T-box transcription factor Brachyury".
- The sea urchin brachyury gene is single copy [PMID:7555703 "The HpTa gene is present
  as a single copy per haploid genome."], so the one T-homolog locus in the S. purpuratus
  genome must be SpBra, the gene cloned by Peterson et al. 1999 [PMID:10068473 "SpBra,
  the orthologue of the vertebrate Brachyury gene"] and used for the target-gene screen
  of Rast et al. 2002 [PMID:12027442 "Brachyury expression patterns for
  Strongylocentrotus purpuratus reported in this paper are entirely consistent with
  data from other echinoderm species."].
- Confidence: HIGH. I could not locate the GenBank accession of the 1999 SpBra cDNA to
  do a direct sequence comparison (the nearest hit in the protein database, AAD20328, is
  the SpNot cDNA from the same paper), but a single-copy gene, a single genomic locus
  and Brachyury-specific signatures on the record leave no realistic alternative.

## What the gene is

Bra encodes the sea urchin orthologue of vertebrate Brachyury (T/TBXT), the founding
member of the T-box family of DNA-binding transcription factors. The protein has an
N-terminal T-box DNA-binding domain (residues 45-220 on A0A7M7PDZ1) and a
low-complexity C-terminal region. Sea urchin Brachyury was first cloned from
Hemicentrotus pulcherrimus (HpTa) [PMID:7555703 "in the T domain of the N terminus the
amino acid identity was 73% (sea urchin/mouse)"].

## Expression

- S. purpuratus (Peterson et al. 1999): embryonic expression in the vegetal plate and
  the secondary mesenchyme founder cells, then extinguished; re-expressed a week later
  in the larval vestibule of the adult rudiment and in the mesoderm of both hydrocoels
  [PMID:10068473 "this gene is expressed during embryogenesis in the embryonic vegetal
  plate and secondary mesenchyme founder cells, and expression is then extinguished";
  "SpBra is also expressed in the mesoderm of both left and right hydrocoels, and it
  is not expressed in any larva-specific tissues"].
- Rast et al. 2002 refined the S. purpuratus vegetal-plate pattern to the endoderm
  [PMID:12027442 "Brachyury expression in the vegetal plate is confined to the
  presumptive endodermal cells."].
- Endoderm GRN timing (Peter & Davidson 2010, 2011): bra is part of the veg2 endoderm
  regulatory state by 18 h, together with foxA, blimp1b and hox11/13b [PMID:19895806
  "foxA, blimp1b, hox11/13b and brachyury showed very similar expression patterns."],
  and by 24 h it is transcribed instead in the veg1 (future hindgut) endoderm
  [PMID:21623371 "By 24 h post-fertilization, hox11/13b and brachyury, which are both
  expressed in veg2 endoderm at 18 h, are being transcribed instead in veg1
  endodermal progenitors, where eve also continues to be expressed"].
- A second, oral-ectoderm domain around the future mouth is seen in every sea urchin
  examined: Lytechinus [PMID:11784024 "The second domain of LvBrac expression first
  appears broadly in the oral ectoderm at mesenchyme blastula stage and at later
  embryonic stages is refined to just the stomodael opening."], Paracentrotus
  [PMID:11819120 "PlBra is expressed around the blastopore and in the stomodaeum area
  as in most basal deuterostomes"], and S. purpuratus by scRNA-seq [PMID:35038441 "In
  sea urchin embryos, Brachyury is expressed in the invaginating endoderm, and in the
  oral ectoderm of the invaginating mouth opening."; "This suggests that the ventral
  organizer contains Brachyury-positive cells which invaginate to form the
  stomodeum."]. In the S. purpuratus scRNA-seq atlas all three endoderm clusters (two
  veg2-derived, one veg1-derived) express Brachyury in blastulae [PMID:35038441 "Our
  results showed that cells of all three endoderm clusters expressed Brachyury in
  blastulae."].
- Lytechinus protein data (anti-LvBrac serum): the vegetal domain is a torus of
  constant size around the blastopore through which endoderm cells transit
  [PMID:11784024 "This torus-shaped area of LvBrac expression remains constant in
  size as endoderm cells express LvBrac upon moving into that circumference and cease
  LvBrac expression as they leave the circumference."].

## Inputs (upstream regulators)

- Vegetal expression depends on autonomous beta-catenin signalling in the macromeres
  (Lytechinus) [PMID:11784024 "Vegetal LvBrac expression depends on autonomous
  beta-catenin signaling in macromeres and does not require micromere or
  veg2-inductive signals."].
- In the S. purpuratus endoderm GRN the inputs are Tcf/beta-catenin, Otx, Hox11/13b and
  (later) GataE [PMID:19895806 "Both genes appear to be expressed under the control of
  Tcf, Hox11/13b and Otx, as mentioned above, and are also ultimately affected by
  GataE."]. Tcf/Groucho repression restricts the domain: [PMID:19895806 "Mutation of
  Tcf binding sites in the cis-regulatory regions of hox11/13b, foxA and brachyury,
  and eve results in dramatic ectopic expression of reporter constructs in all or most
  domains of the embryo."]. Hox11/13b is a driver in both veg2 and veg1 phases
  [PMID:21623371 "In both the early veg2 and the later veg1 endoderm GRNs, Hox11/13b
  functions as a driver of brachyury expression, as shown by the specific reduction of
  endodermal brachyury expression in embryos injected with hox11/13b MASO"].
- Note that the Tcf/Otx/GataE cis-regulatory work on the bra locus is cited in Peter &
  Davidson 2010 as unpublished (Cameron, Theodoris, Ben-Tabou de-Leon, Davidson); I did
  not find a stand-alone S. purpuratus bra cis-regulatory paper by eutils search.

## Outputs and function

- Rast et al. 2002 (S. purpuratus, Bra morpholino and premature misexpression,
  differential macroarray screen): the endodermal Bra-dependent genes are effector
  genes, cytoskeletal modulators and gut enzymes, not regulatory genes [PMID:12027442
  "Some of the endodermal genes that respond to Brachyury are cytoskeletal modulators
  that may play a role in gut morphogenesis. This finding is consistent with the block
  in gastrulation induced by interfering with Brachyury function in sea urchins";
  "the brachyury gene transduces information about the state of endodermal
  specification to genes that modulate morphogenesis and genes that perform terminal
  functions in the gut"]. SMC/pigment genes in the screen were judged indirect
  [PMID:12027442 "the SMC genes are likely to be indirect targets of Brachyury-induced
  signaling from the surrounding endoderm to the central mesoderm"].
- Gross & McClay 2001 (Lytechinus, LvBrac-Engrailed dominant repressor): gastrulation
  movements blocked, but endoderm and mesoderm specification intact [PMID:11784024
  "Microinjection of mRNA encoding this LvBrac-EN construct resulted in a block in
  gastrulation movements but not expression of endoderm and mesoderm marker genes.";
  "It was then determined that LvBrac is necessary for the morphogenetic movements
  occurring in both expression regions."]. Half-embryo injections suggest the
  downstream effect is non-autonomous [PMID:11784024 "injection of LvBrac-EN into one
  of two blastomeres resulted in normal gastrulation movements of tissues derived from
  the injected blastomere"].
- Hemicentrotus overexpression: HpTa mRNA suppresses vegetal plate and SMC formation
  (interpreted as cofactor squelching) [PMID:16351823 "The overexpression of HpTa
  resulted in suppression of the formation of vegetal plate and secondary mesenchyme
  cells."].
- Endoderm-kernel feedback in S. purpuratus: bra MASO strongly reduces otx-beta
  transcripts, so bra feeds back positively into the otx/blimp1b/gatae kernel
  [PMID:19895806 "perturbation of brachyury expression strongly depressed expression
  levels of otx–β transcripts"; "Otx is activated by its own gene product as well as
  the products of its target genes blimp1b and brachyury."]. The gatae decrease in bra
  MASO is an indirect consequence via otx [PMID:19895806 "this is an expected indirect
  result of the depression of otx expression by brachyury MASO"]. bra MASO does not
  affect foxA at 18 h [PMID:19895806 "Injection of a brachyury MASO did not affect the
  expression levels of foxA at 18 hpf."], although Brachyury sites in a foxA module act
  later (cited as unpublished).
- Hedgehog ligand expression in the endoderm is downstream of Brachyury and FoxA
  (Lytechinus/S. purpuratus) [PMID:19393640 "At gastrulation the Hh ligand is expressed
  by the endoderm downstream of the Brachyury and FoxA transcription factors in the
  endomesoderm gene regulatory network."].
- Genome-wide direct targets: Brachyury ChIP-seq in S. purpuratus (and Nematostella)
  identifies an ancestral Brachyury-FoxA-canonical Wnt feedback loop [PMID:36396969
  "we present a genome-wide target-gene screen using chromatin immunoprecipitation
  sequencing in the sea anemone Nematostella vectensis, an early branching
  non-bilaterian, and the sea urchin Strongylocentrotus purpuratus"; "Our analysis
  reveals an ancestral gene regulatory feedback loop connecting Brachyury, FoxA and
  canonical Wnt signalling involved in axial patterning"], and shows that the
  vertebrate mesodermal targets are largely absent in sea urchin [PMID:36396969
  "hardly any of the key mesodermal downstream targets in vertebrates are found in
  the sea anemone or the sea urchin"].

## GO decisions (summary)

- MF: keep GO:0003700 and GO:0000978 (ChIP-seq direct genomic binding in
  S. purpuratus); generic GO:0003677 marked non-core. NEW GO:0000981 (Pol II-specific
  DNA-binding TF activity), IDA from the ChIP-seq study plus the MASO/misexpression
  target-gene screen. I did not propose the activator child GO:0001228: the sign is
  strongly implied (MASO/dominant-repressor loss of function abolishes target
  expression; misexpression induces it) but no S. purpuratus reporter/site-mutagenesis
  study of a Brachyury target module is published in the cached literature.
- CC: nucleus, ACCEPT.
- BP: GO:0045893 modified to the Pol II-specific GO:0045944 with IMP support (otx-beta
  depression in bra MASO; Hh downstream of Bra). GO:0006355 kept non-core as the generic
  parent. NEW GO:0007369 gastrulation (IMP): Bra-dependent effector genes drive
  archenteron morphogenesis, and blocking Bra function blocks gastrulation movements in
  S. purpuratus (Rast 2002) and Lytechinus (Gross & McClay 2001). Comparator: mouse T
  (P20293) carries GO:0007509 mesoderm migration involved in gastrulation (IMP) and
  GO:0001707 mesoderm formation, so gastrulation-branch terms are the convention for
  brachyury orthologues.
- Not annotated: endodermal cell fate specification (endoderm markers are unaffected by
  Bra loss of function; Bra is downstream of endoderm specification, and its positive
  feedback on otx-beta is a maintenance input rather than the specification step);
  mouth/stomodeum formation (functional evidence is Lytechinus dominant-negative only;
  raised as a question); secondary mesenchyme differentiation (SMC effects judged
  indirect by Rast 2002).
