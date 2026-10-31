# SoxB1 (Q9Y0D7, Strongylocentrotus purpuratus) — curation notes

## Identity

- UniProt Q9Y0D7 (TrEMBL, Q9Y0D7_STRPU, "Transcription factor SoxB1", EMBL AAD40688.3)
  is the SpSoxB1 cDNA reported by Kenny et al. 1999 (Development 126:5473; the RX
  reference on the record) [PMID:10556071 "We have identified a Sox family transcription
  factor, SpSoxB1, that is asymmetrically distributed among blastomeres of the sea urchin
  embryo during cleavage, beginning at 4th cleavage."]. 344 aa; HMG box (DNA_BIND) at
  residues 61-129; Pfam HMG_box (PF00505) + SOXp (PF12336); InterPro IPR022097 SOX family.
  PANTHER PTHR10270:SF324 on the record (label not asserted here; see CLAUDE.md).
- Community names: SpSoxB1, SoxB1, soxb1. SoxB-group (Sox1/2/3-like) HMG-box factor; Wei
  et al. 2011 note that "SoxB1 is most closely related to Sox1, Sox2, and Sox3, which have
  been shown to maintain a neural precursor state in mouse embryos" [PMID:21576476]. The
  paralog SpSoxB2 is a distinct gene with partly distinct functions [PMID:14499650].
- No identity doubt: the accession, the RX paper, the EMBL entry and the GRN literature
  all refer to the same maternal SoxB1 gene product.

## Expression and protein distribution (Kenny 1999, Angerer 2005)

- Maternal mRNA is uniform in the egg; protein is nuclear in all cells of 4- and 8-cell
  embryos, then lost from micromere nuclei at 4th cleavage [PMID:10556071 "SpSoxB1 maternal
  transcripts are uniformly distributed in the unfertilized egg and the protein accumulates
  to similar, high concentrations in all nuclei of 4- and 8-cell embryos. However, at
  fourth cleavage, the micromeres, which are partitioned by asymmetric division of the
  vegetal 4 blastomeres, have reduced nuclear levels of the protein, while high levels
  persist in their sister macromeres and in the mesomeres."].
- Zygotic transcription is nonvegetal, and the nuclear-SoxB1-free vegetal domain expands
  until only ectoderm retains nuclear protein [PMID:10556071 "The vegetal region lacking
  nuclear SpSoxB1 gradually expands so that, after blastula stage, only cells in
  differentiating ectoderm accumulate this protein in their nuclei."]. It is "the earliest
  known spatially restricted regulator of transcription along the animal-vegetal axis of
  the sea urchin embryo" [PMID:10556071].
- Clearance from vegetal lineages is post-translational and beta-catenin dependent
  [PMID:15689377 "We show that SoxB1 is regulated at the level of protein turnover in these
  lineages. This mechanism is dependent on nuclear beta-catenin function. It can be
  activated by Pmar1, but not by Krl, both of which function downstream of
  beta-catenin/TCF-Lef."]. Macromere turnover requires nuclear entry; mesomeres (ectoderm)
  do not turn it over but show negative autoregulation [PMID:15689377 "However, in
  mesomeres, SoxB1 appears to be subject to negative autoregulation that helps to maintain
  tight regulation of SoxB1 mRNA levels in presumptive ectoderm."]. SpKrl (Blimp1/Krox),
  a direct beta-catenin/TCF target, represses soxb1 transcription [PMID:11152635 "SpKrl
  negatively regulates expression of the animalizing transcription factor, SpSoxB1."].
- In the Davidson micromere GRN, absence of nuclear SoxB1 is one of the three initial
  micromere-specific character states [PMID:18413610 "Concomitantly, the maternal
  transcription factor SoxB1 enters the nuclei of all early cleavage blastomeres except the
  micromeres (ref. 28 and Fig. S4 )." ... "SoxB1 is believed to act as an antagonist of the
  transcriptional cofactor function of β-catenin."].

## Molecular function: sequence-specific DNA binding, DNA bending, activation of SpAN

- SpSoxB1 binds the Sox cis element of the SpAN (tolloid/BMP1-related) promoter in EMSA;
  the antiserum supershifts the nuclear-extract complex [PMID:10556071 "In vitro
  translated SpSoxB1 forms a specific complex with this cis element whose mobility is
  identical to that formed by a protein in nuclear extracts. An anti-SpSoxB1 rabbit
  polyclonal antiserum specifically supershifts this DNA-protein complex"].
- The Sox site is essential in vivo (20-fold) but SoxB1 does not act as a classical
  activator; it bends DNA and works architecturally [PMID:11763999 "Regulatory sites that
  bind SpSoxB1 and CBF (CCAAT binding factor) are essential for strong transcriptional
  activity because mutations of these elements reduce promoter activity in vivo 20- and
  10-fold, respectively." ; "Here we show that multimerized SpSoxB1 elements cannot
  activate transcription from the SpAN basal promoter in vivo." ; "However, like other
  factors containing HMG-class DNA binding domains, SpSoxB1 does induce strong bending of
  DNA." ; "The results described above suggest a model in which SpSoxB1 promotes
  transcription of the SpAN gene primarily through DNA bending, rather than through
  transcriptional activation."]. Circular-permutation EMSAs with in vitro translated
  protein were used to show the bending (full text cached).

## Antagonism of nuclear beta-catenin / the endomesoderm program (Kenny 2003)

- Overexpression animalizes: [PMID:14499650 "Here we show that elevated and ectopic
  expression of this factor suppresses differentiation of all vegetal cell types, a
  phenotype that is very similar to that caused by the suppression of beta-catenin nuclear
  function by cadherin overexpression."]. The effect is at the protein-protein level, not
  via DNA binding [PMID:14499650 "Suppression of vegetal fates involves interference at
  the protein-protein level because a mutation of SpSoxB1 that prevents its binding to DNA
  does not significantly reduce this activity."].
- Loss of function raises TCF/beta-catenin reporter output in vivo, i.e. SoxB1 normally
  dampens canonical Wnt/beta-catenin transcriptional output [PMID:14499650 "Reduction in
  SpSoxB1 level results in elevated TCF/Lef-beta-catenin-dependent expression of a
  luciferase reporter gene in vivo, indicating that in the normal embryo this protein
  suppresses the primary vegetal signaling mechanism that is required for specification of
  mesenchyme and endoderm."]. Summarised in Angerer 2005 [PMID:15689377 "Patterning of cell
  fates along the sea urchin animal-vegetal embryonic axis requires the opposing functions
  of nuclear beta-catenin/TCF-Lef, which activates the endomesoderm gene regulatory network,
  and SoxB1, which antagonizes beta-catenin and limits its range of function."].
- Paradoxically, normal SoxB1 is also required for gastrulation and endoderm
  differentiation [PMID:14499650 "Surprisingly, normal expression of SpSoxB1 is required
  for gastrulation and endoderm differentiation, as shown by both morpholino-mediated
  translational interference and expression of a dominant negative protein."]. The authors
  attribute this to SoxB target genes required for gastrulation, not to SoxB1 being an
  endoderm specifier; this is treated as an indirect/pleiotropic requirement here.

## Ectoderm GRN: activator of ectodermal regulatory genes (Range 2007, Barsi 2015)

- nodal cis-regulation: the 5' module of nodal has essential Sox sites, and zygotic nodal
  and univin expression depend on SoxB1 [PMID:17855430 "This work shows that Tcf, SoxB1 and
  Univin play essential roles in the regulation of nodal expression in the sea urchin and
  suggests that some of the regulatory interactions controlling nodal expression predate
  the chordates."].
- Ciliated-band and ectoderm regulatory states: soxb1 MASO downregulates nearly all CB
  regulatory genes [PMID:25655703 "Remarkably, almost all of the regulatory genes
  specifically expressed within these domains are downregulated by interference with
  SoxB1 expression, implying their common activation by this factor." ; "However, most of
  its target genes utilize SoxB1 as a transcriptional activator."]. It is described as
  "a pan-ectodermal transcription factor that is known to affect many other regulatory
  genes of the oral and aboral ectoderm GRNs" [PMID:25655703]. Negative autoregulation and
  repression of otx beta1/2 are also seen [PMID:25655703 "As these analyses show, SoxB1
  controls its own level of expression through negative feedback on the soxb1 gene, so that
  soxb1 MASO produces a large increase in the prevalence of its own mRNA." ; "Furthermore,
  SoxB1 evidently represses otxβ1/2 transcription."].
- Slota et al. 2018 count soxb1 among the proneural TFs expressed in all three neural
  territories and note its earlier ectoderm role [PMID:30413529 "soxb1 was a special case in
  that it is involved in early specification of ectoderm ( Barsi et al., 2015 ) and is
  eliminated post-translationally from the EM ( Angerer et al., 2005 )."].

## Neurogenesis (Wei 2011, Slota 2018)

- SoxB1 marks uncommitted neural precursors and is lost from differentiating neurons in
  ectoderm and foregut [PMID:21576476 "Just as these factors disappear when neurons
  differentiate in mouse embryos, so also is SoxB1 eliminated from differentiating neurons
  in ectoderm and foregut endoderm in sea urchin embryos."]. Persistent foregut SoxB1 is
  proposed to preserve neural potential there by antagonising Wnt/beta-catenin [PMID:21576476
  "We propose that SoxB1 function supports retention of pluripotency in this region, at
  least in part by antagonizing canonical Wnt signaling that drives endomesoderm
  development."]. Because soxb1 knockdown blocks gastrulation, its requirement for foregut
  neurons could not be tested [PMID:21576476].
- Slota 2018 used a soxb1 MO and found domain-specific effects on other proneural genes
  [PMID:30413529 "Expression of the six proneural transcription factors shows that the
  response to knockdown of soxC , sip1 or soxb1 differs when the three territories are
  compared"]. Neural involvement is real but pleiotropic and mostly expression-based, so
  the IBA neuron differentiation row is kept as non-core rather than promoted.

## Curation decisions (summary)

- IBA MF rows (GO:0000978 cis-regulatory DNA binding, GO:0001228 activator) ACCEPT: EMSA
  binding to the SpAN Sox element; the site is essential in vivo; most ectoderm targets use
  SoxB1 as an activator. Caveat recorded that SpAN activation is architectural (DNA
  bending) rather than classical transactivation.
- IBA BP GO:0045944 ACCEPT (core); GO:0000122 KEEP_AS_NON_CORE (negative autoregulation,
  otx beta1/2 repression); GO:0030182 neuron differentiation KEEP_AS_NON_CORE; GO:0007420
  brain development MARK_AS_OVER_ANNOTATED (echinoderm embryos have an apical organ, not a
  brain; vertebrate/fly-seeded node).
- IEA rows (DNA binding, nucleus, regulation of transcription) ACCEPT as generic parents.
- NEW: GO:0090090 negative regulation of canonical Wnt signaling pathway (IMP, Kenny 2003);
  GO:0008301 DNA binding, bending (IDA, Kenny 2001); GO:0001715 ectodermal cell fate
  specification (IMP, Barsi 2015 + Kenny 2003 animalisation).
- Not proposed: endoderm/gastrulation terms (requirement is indirect); GO:0000981 (ancestor
  of the accepted GO:0001228 row); neurogenesis-specific terms (expression-based).
- gocams/index.tsv has no entry for Q9Y0D7/SoxB1.
- PMID:26511925 (Garner et al. 2016) was fetched while screening neurogenesis literature but
  concerns SoxB2/SoxC and is not cited.
