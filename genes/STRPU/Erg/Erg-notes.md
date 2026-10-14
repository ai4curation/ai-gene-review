# Erg (Strongylocentrotus purpuratus, UniProt Q6R7X7) - curation notes

## Identity

- UniProt Q6R7X7 (`Q6R7X7_STRPU`, unreviewed/TrEMBL, 498 aa) is "Transcription
  factor Erg" deposited by Rizzo & Arnone (EMBL AY508725 / AAR92036.1, Dec 2003,
  submission title "Role of the sea urchin Erg homolog in mesenchyme formation").
  The RX line is PMID:11493577 (Zhu et al. 2001, the PMC EST project), which
  produced the EST from which the cDNA was recovered; that paper does not
  discuss erg as such. RefSeq NP_999833 / GeneID 397069; the CTD cross-reference
  is to human ERG (2078). Community symbol: `Erg` (`Sp-Erg`, `erg` in GRN papers).
- Domain architecture (UniProt FT): PNT/SAM-pointed domain 91-176 (PROSITE
  PS51433), ETS winged-helix DNA-binding domain 328-408 (PS50061), disordered
  N-terminal and central regions. CDD cd08531 "SAM_PNT-ERG_FLI-1", i.e. the
  ERG/FLI1 subfamily of ETS factors. PANTHER PTHR11849 (family label not written
  from memory). An earlier Lytechinus variegatus genomic fragment of the erg
  homolog defined the ERG/FLI-1-specific "R" region [PMID:1457815 "the remainder
  of the sequence is only homologous with the human ERG and murine Fli-1 genes.
  This latter region, designated R, represents a highly conserved erg-specific
  domain."].
- Identity check: the accession, the GRN gene "erg" (Oliveri 2008 ref 9 = Rizzo
  et al. 2006) and the Rizzo/Arnone "Sp-Erg" are the same gene; there is a
  single ERG-subfamily ets gene in the S. purpuratus genome
  [PMID:16997294 "this sea urchin has 11 members of the ets gene family ...
  almost all vertebrate ets subfamilies ... are each represented by one
  orthologous sea urchin gene"]. No identity doubt.

## Expression

- Genome-wide ets survey: [PMID:16997294 "five of the nine sea urchin ets genes
  expressed during embryogenesis are exclusively (Sp-Ets1/2, Sp-Erg, Sp-Ese) or
  additionally (Sp-Tel, Sp-Pea) expressed in mesenchyme cells and/or their
  progenitors."] Sp-Erg is not in the maternal set ("Five ets genes (Sp-Ets1/2,
  Sp-Tel, Sp-Pea, Sp-Ets4, Sp-Erf) are also maternally expressed"), i.e. it is
  zygotically activated in the skeletogenic micromere lineage.
- Later, oral non-skeletogenic mesoderm (NSM): [PMID:23261933 "At this time three
  genes that are first expressed in the SM, erg, hex, and ets1/2 are activated
  specifically in the oral NSM (Fig. 1O–R). The exact timing of erg activation
  varies even within a single batch of embryos. About a quarter of the embryos
  express erg in the oral NSM already at 21 hpf, but all embryos express it by
  24 hpf. The hex gene is activated next, followed by ets1/2."]. Oral NSM erg
  is confined by the aboral regulators: [PMID:23261933 "If gcm or gataE
  expression are blocked by treatment with MASOs we see an expansion of ese,
  prox1, gataC, and erg expression"].

## Place in the skeletogenic micromere GRN (Oliveri, Tu, Davidson 2008)

- Position: immediately downstream of the four double-negative-gate targets
  (alx1, ets1, tbr, tel), in the state-stabilization subcircuit:
  [PMID:18413610 "immediately downstream of the initial four regulatory genes
  activated by the double negative gate ( Fig. 2 A ), three additional genes are
  activated: one encoding the Ets family factor Erg ( 9 ), and the other two, hex
  and tgif , encoding homeobox factors ( 5 ). These genes are engaged in
  interlocking positive double feedback loops ( erg with hex ; and hex with tgif
  ). Interference with expression of any of these genes severely depresses
  transcript levels of the others ( Fig. S3 ). Thus they dynamically stabilize
  all aspects of the regulatory state downstream of themselves."]
- Inputs: hex feeds back on erg ("the outputs of hex go to erg"); erg is
  downstream of ets1/alx1 per the GRN diagram (Fig. 3A). Perturbation basis:
  [PMID:18413610 "measured by QPCR assessment of alterations in levels of
  transcripts of all other genes in the GRN, at various developmental times, and
  when warranted, by WMISH (perturbation data are listed in Fig. S3 )"].
- Outputs to differentiation genes (feed-forward architecture):
  [PMID:18413610 "these differentiation genes require as drivers products of all
  of the now familiar components of the skeletogenic regulatory state ( alx1 ,
  ets1 , tbr , tel , erg , hex , foxb , dri )" ... "Almost all of the linkages to
  the differentiation genes are feeds forward (A > C; A > B; B > C)" ... "The alx1
  and erg genes play both roles, but the ets1 gene ( 9 ) is used in these gene
  batteries only as the A driver"].
- Interpretation by the authors: [PMID:18413610 "The tgif-hex and erg-hex loops
  in the skeletogenic micromere GRN are canonical examples. Outputs of these
  genes not only serve as drivers for one another but also feed multiple other
  nodes of the GRN, so that their activity ensures the persistence of surrounding
  activities."]
- Not shown in the cached text: a morphological (skeleton-minus) phenotype for
  erg MASO in S. purpuratus. The skeleton-minus panels of Fig. 3 are for tbr,
  hex, tgif, ets1 and alx1; erg's effects in Oliveri 2008 are at the level of
  transcript changes (Fig. S3, Table S1). No cis-regulatory analysis of an
  Erg-dependent module is cached, so all Sp evidence for Erg activity is
  perturbation-level (IMP), not direct (IDA).

## Corroboration from Lytechinus variegatus (not the reviewed gene product)

- EMT sub-circuits: [PMID:24598159 "Three TFs highest in the GRN specified and
  activated EMT (alx1, ets1, tbr) and the 10 TFs downstream of those (tel, erg,
  hex, tgif, snail, twist, foxn2/3, dri, foxb, foxo) were also required for
  EMT."] and [PMID:24598159 "In the Lv PMC GRN, snail regulates erg and erg
  regulates hex"]. This confirms the erg -> hex linkage in a second species and
  adds an EMT requirement for erg in L. variegatus; it is not used as the
  primary basis for an S. purpuratus annotation.

## Curation decisions (see the ai-review.yaml)

- Electronic rows: the IBA/InterPro/UniRule TF terms (GO:0000981, GO:0003700,
  GO:0043565, nucleus, regulation of transcription by RNA pol II) are consistent
  with an ETS-domain factor whose perturbation depresses its targets; ACCEPT.
  Generic GO:0003677 DNA binding -> MODIFY to GO:0043565; GO:0006351
  (DNA-templated transcription, UniRule) -> MODIFY to the regulation term, since
  a sequence-specific TF regulates transcription rather than performing it;
  GO:0006355 and GO:0030154 -> KEEP_AS_NON_CORE as generic parents.
- NEW (all IMP, PMID:18413610): GO:0045944 positive regulation of transcription
  by RNA polymerase II (erg MASO depresses hex and the differentiation genes it
  drives); GO:0001710 mesodermal cell fate commitment (erg-hex feedback loop
  locks down the skeletogenic mesenchyme regulatory state); GO:0070169 positive
  regulation of biomineral tissue development (erg is an A/B feed-forward driver
  of the skeletogenic differentiation gene battery).
- Not proposed: GO:0001228 activator activity (no cis-regulatory/direct assay in
  S. purpuratus; the positive sign is inferred from perturbation only, so the
  sign-neutral GO:0000981 is kept as MF); positive regulation of EMT (only Lv
  evidence); any NSM-specific process term (expression only).
- No GO-CAM contains this gene (gocams/index.tsv has no Q6R7X7 entry).
