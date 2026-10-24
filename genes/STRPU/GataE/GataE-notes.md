# GataE (Sp-GataE / Spgatae; UniProt Q64HK6) - curation notes

## Identity of the UniProt entry

- Q64HK6 (`Q64HK6_STRPU`, unreviewed/TrEMBL, 567 aa) is the S. purpuratus GATA
  transcription factor deposited by the Davidson lab (EMBL AAU21562.1, gene name
  `gatae`); its single RX line is PMID:15567710 (Lee & Davidson 2004), the
  expression paper for Spgatae. The cDNA in that paper is GenBank AY623814, which
  is also the cDNA used to define the exon structure in Lee, Nam & Davidson 2007
  [PMID:17570356 "Comparison of the gatae BAC sequence to that of gatae cDNA
  (Genbank Accession No. AY623814 ) revealed that the gatae gene contains 6 exons
  extending over 29 kb of genomic DNA"]. So the accession is the GRN gene, not a
  paralogue; there is no identity doubt. The sea urchin has a second GATA gene,
  gatac (GATA1/2/3 class), which is a different node of the mesoderm GRN.
- Orthology: [PMID:15567710 "Spgatae is the sea urchin ortholog of the vertebrate
  gata4/5/6 genes, as confirmed by phylogenetic analysis."]; also
  [PMID:17570356 "The gatae gene of Strongylocentrotus purpuratus is orthologous
  to vertebrate gata-4,5,6 genes."]. PANTHER PTHR10071 (family) / PTHR10071:SF337
  (subfamily), labels looked up in `interpro/panther/panther.obo`, not from memory.
- Domain architecture (UniProt FT): two GATA-type zinc fingers at 256-311 and
  311-364 (PROSITE PS50114); [PMID:17570356 "The two class IV zinc fingers are
  encoded in exons 3 and 4."]. Long disordered N- and C-terminal regions.

## Expression (timing and lineage)

- [PMID:15567710 "Expression was first detected in the 15 h blastula. The number
  of Spgatae RNA molecules increases steadily during blastula stages, with
  expression peaking during gastrulation."]
- [PMID:15567710 "Whole mount in situ hybridization showed that Spgatae
  transcripts were first detected in a ring of prospective mesoderm cells in the
  vegetal plate. Spgatae expression then expands to include the entire vegetal
  plate at the mesenchyme blastula stage. During gastrulation Spgatae is
  expressed at the blastopore, and at prism stage strongly in the hindgut and
  midgut but not foregut, and also in mesoderm cells at the tip of the
  archenteron."] Terminal pattern: midgut plus coelomic pouches.
- Two phases, two lineages: an early non-skeletogenic mesoderm (NSM) phase
  identical to gcm, then an endoderm phase. [PMID:23261933 "before its
  endodermal expression phase gataE is expressed identically with gcm (Ransick
  and Davidson, 2006), first in a ring (Fig. 1F), and then exclusively in the
  aboral NSM (Fig. 1G), and eventually in both aboral NSM and endoderm"].
  [PMID:19895806 "Even though gataE is expressed exclusively in mesoderm
  precursor cells at hatched blastula stage, it is a component of the endoderm
  GRN at later stages"]. GataE protein was detected with a specific antibody
  (Kiyama & Klein 2007, PMID:17710433), which also identified the Fog1 cofactor.

## cis-regulation of gatae (inputs)

- Lee, Nam & Davidson 2007 (full text cached) built a gatae BAC-GFP knock-in
  that reproduces the whole pattern and mapped two intronic modules:
  [PMID:17570356 "Module 10 produces early expression in mesoderm and endoderm
  cells up to the early gastrula stage, while module 24 generates late
  endodermal expression at gastrula and pluteus stages."] BAC deletion showed
  [PMID:17570356 "Module 10 is uniquely necessary and sufficient to account for
  the early phase of gatae expression during endomesoderm specification."]
- Delta/Notch input (NSM phase): [PMID:22306924 "The cis-regulatory module
  controlling gataE expression also contains functional Su(H) sites, thus
  proving that, like gcm, gataE is a direct target of D/N signaling"]; in the
  regulome-wide D/N perturbation, [PMID:22306924 "In our data set, gcm, gataE,
  foxA, and foxY are significantly affected in their expression level in repeat
  experiments"].
- Gcm input (feed-forward with Delta/Notch): [PMID:23261933 "An important result
  is that embryos in which the Gcm factor is depleted display a significant
  reduction in the level of gataE transcripts at the 15 and 18 hour time points
  (Fig. 6A)."]; abstract: [PMID:23261933 "A linchpin of this network is gataE
  which as we show is a direct Gcm target and part of a feedback loop locking
  down the aboral regulatory state."]
- Otx input (endoderm phase) and the otx-gatae feedback loop: [PMID:19895806
  "their data show that otx expression depends on Otx itself, GataE and
  Blimp1b, which are themselves encoded by Otx target genes."]; [PMID:21623371
  "The models proposed here include previously identified linkages such as the
  positive feedback circuit between blimp1b, otx and gatae."]; a brachyury MASO
  effect on gatae is indirect via otx [PMID:19895806 "this is an expected
  indirect result of the depression of otx expression by brachyury MASO (Yuh et
  al., 2004), and is not to be considered a direct linkage"].

## Outputs: what GataE itself does

### Direct activator of endoderm regulatory genes (endoderm specification)

- [PMID:17570356 "Perturbation analysis using morpholino antisense
  oligonucleotides (MASO), and many other observations, reveal that prior to
  gastrulation gatae is a direct activator of a number of genes encoding
  transcription factors, including the endodermal transcription factors foxA,
  brachyury , and β1/2-otx"]
- The otx node was verified at the DNA level: [PMID:15110718 "It requires
  gatae, otx, and krox inputs, as predicted, and it operates as an "AND" logic
  processor in that removal of any one of these inputs essentially destroys
  activity."] and [PMID:15110718 "For spatial expression in the endoderm, one
  particular pair of Gata sites is essential and these function synergistically
  with an adjacent Otx site."] The site mutations phenocopied the gatae MASO
  [PMID:15110718 "mutation of these sites was demonstrated to produce the same
  respective effects on construct expression as does blocking its regulatory
  inputs by treatment with morpholino antisense oligonucleotides"].
- Lock-down loop: [PMID:17570356 "These two genes cross-regulate, generating a
  positive feedback loop which serves to lock down the state of endoderm
  specification"]. Conserved for ~500 My with starfish: [PMID:14595011 "The
  gatae gene is soon also engaged in this loop, requiring otx expression for
  function, and it, in turn, positively crossregulates otx ."] and
  [PMID:14595011 "The gatae gene is a major regulator of many other endodermal
  control genes ( 4 , 5 ), among which are foxa and brachyury ( bra )"]. Note
  that the perturbation experiments in Hinman et al. 2003 are in the starfish
  Asterina miniata; the sea urchin statements rest on Davidson et al. 2002
  (PMID:12027441, PMID:11872831).
- Requirement: [PMID:17570356 "This gene is expressed in the endomesoderm in
  the blastula and later the gut of the embryo, and is required for normal
  development."]

### Aboral NSM / pigment cell specification

- GataE MASO phenotype (two MASOs, translation- and splice-blocking):
  [PMID:23261933 "At 48 hpf GataE MASO embryos lack pigment cells altogether, as
  shown by the absence of pks expression (Fig. 6J,J)."]; [PMID:23261933
  "Transcript levels of six1/2 and z166 are also greatly reduced in embryos
  bearing GataE MASO, about equally to embryos bearing Gcm MASO, so gataE is
  likely to provide direct inputs into these genes of the aboral GRN"].
- Restriction of the oral NSM state: [PMID:23261933 "If gcm or gataE expression
  are blocked by treatment with MASOs we see an expansion of ese, prox1, gataC,
  and erg expression"]; the authors note the spatial repressor is
  [PMID:23261933 "either GataE or a gene downstream of it"], so direct
  repression is not established.
- Direct activation of the pigment differentiation gene pks: [PMID:20122918
  "The mutagenesis of these DNA-binding sites indicated that SpGcm, SpGataE and
  SpKrl are direct positive regulators of SpPks."]; corroborated by
  [PMID:22509525 "the essential pigment cell differentiation gene, pks, has
  direct GataE inputs (Calestani and Rogers, 2010)"] and gataE upstream of six1
  [PMID:22509525 "six1 is one of just two transcription factor mRNAs, the level
  of which is significantly depressed following knockdown of gataE
  transcripts"].

### Repression of an ectoderm gene (spec2a)

- Kiyama et al. 2005 (abstract only): [PMID:15882584 "The proximal element bound
  to SpGATA-E, an endomesoderm-specific transcription factor. Treatment with
  SpGATA-E and SpGsc morpholino antisense oligonucleotides (MASOs) resulted in
  enhanced transcriptional activity from the proximal element, suggesting that
  both factors functioned as repressors at this site."] and [PMID:15882584
  "SpGATA-E MASO-treated embryos failed to express ectoderm markers, indicating
  a role for SpGATA-E in ectoderm differentiation."] The ectoderm-marker effect
  is hard to interpret for a gene that is never expressed in ectoderm, and the
  repressor conclusion is hedged ("suggesting"), so I do not propose a
  repressor MF term; raised as a question instead.
- Cofactor: [PMID:17710433 "we identified an S. purpuratus fog ortholog, spfog1,
  and showed that SpGataE and SpFog1 physically interacted."] but Fog1 MASO had
  no effect on endomesoderm specification, so the interaction is not annotated
  (and `protein binding` is avoided per repo policy).

## Curation decisions (summary)

- Existing rows are all IEA (InterPro2GO / UniProt SubCell). GO:0003700,
  GO:0006357 and nucleus: ACCEPT (core; direct cis-regulatory evidence). GO:0006355:
  KEEP_AS_NON_CORE (redundant generic parent). GO:0008270 zinc ion binding:
  KEEP_AS_NON_CORE (structural to the class IV zinc fingers). GO:0043565: MODIFY
  to GO:0000978.
- NEW: GO:0001228 (activator MF, IDA: Gata sites in otx module; pks module),
  GO:0000978 (IDA), GO:0045944 (IDA), GO:0001714 endodermal cell fate
  specification (IMP/IDA), GO:0007501 mesodermal cell fate specification (IMP,
  aboral NSM), GO:0050942 positive regulation of pigment cell differentiation
  (IMP + direct pks input).
- Participation test: GataE is itself the transcription factor that installs
  and locks down the endoderm regulatory state (direct inputs into otx, foxA,
  brachyury) and the aboral NSM state (direct inputs into pks, and likely
  six1/2, z166), so the specification terms are participation, not mere
  necessity. Comparators: vertebrate GATA4/5/6 carry endoderm/mesoderm
  specification and cell fate terms; Otx and Blimp1 sibling reviews in this
  repository (the other members of the lock-down loop) carry endodermal cell
  fate specification.
- gocams/index.tsv has no entry for Q64HK6 / gatae.
