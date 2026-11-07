# DDIT3 (CHOP / GADD153 / C/EBP-zeta) — curation notes

UniProt: P35638 (DDIT3_HUMAN), 169 aa, bZIP family, PE 1 (evidence at protein level).
Aliases: CHOP, CHOP10, GADD153, C/EBP zeta, C/EBP homologous protein.
PANTHER family: PTHR16833 (DNA DAMAGE-INDUCIBLE TRANSCRIPT 3 DDIT3).

Fetched 2026-11-01 with `just fetch-gene human DDIT3` (251 GOA rows).

## Deep research

`just deep-research human DDIT3 --provider perplexity` failed in this environment:

```
ERROR - Provider 'perplexity' not available. Available: claude_code
Provider perplexity exited with code 1
All providers failed
```

No `DDIT3-deep-research-*.md` file was therefore written, and per the repository rule
("NEVER write your own content and name it `-deep-research-{provider}.md`") this notes
file carries the literature synthesis instead. Everything below is cited to the cached
publications in `publications/` or to the UniProt flat file.

## What the protein is

A small, largely disordered bZIP transcription factor. The bZIP domain spans residues
99-162 with a basic motif at 101-130 and a leucine zipper at 134-148
(`DDIT3-uniprot.txt`, `FT DOMAIN 99..162`). MobiDB-lite calls residues 32-139
disordered, and this was shown experimentally: "CHOP is an intrinsically disordered
protein... Intrinsic fluorescence, NMR spectroscopy, and analytical size-exclusion
chromatography studies indicate that CHOP contains extensive disordered regions and
self-associate in solution" [PMID:18534616]. The N-terminal region (10-26) is the
transactivation/degradation module: "The CHOP N-terminal domain is necessary not only
for protein degradation but also for its transactivity and interaction with p300"
[PMID:17872950].

Absent under normal conditions, CHOP is induced by stress: "Up-regulated by oxidative
stress, amino-acid deprivation, hypoxia and endoplasmic reticulum stress... During ER
stress, induced by a EIF2AK3/ATF4 pathway and/or ERN1/ATF6 pathway"
(`DDIT3-uniprot.txt`, `CC INDUCTION`). It is cytoplasmic at rest and accumulates in the
nucleus on stress: "Present in the cytoplasm under non-stressed conditions and ER stress
leads to its nuclear accumulation" (`CC SUBCELLULAR LOCATION`, from PMID:29083303).

The gene was cloned as the growth-arrest/DNA-damage-inducible *GADD153*
[PMID:1339368 "the growth arrest and DNA-damage-inducible gene, GADD153"] and is the
3' partner of the *FUS-DDIT3* fusion in myxoid liposarcoma
[PMID:8510758 "In TLS-CHOP the RNA-binding domain of TLS is replaced by the DNA-binding
and leucine zipper dimerization domain of CHOP"].

## Core function: a dimerization-dependent bZIP that both activates and represses

CHOP has essentially no activity as a monomer; its specificity comes from which bZIP
partner it carries.

**DNA binding.** CHOP-C/EBP dimers bind a distinct element: "These sequences were found
to contain a unique core element PuPuPuTGCAAT(A/C)CCC... Deletions in the basic region
of CHOP lead to a loss of DNA binding" [PMID:8657121]. The basic region "deviates
considerably in sequence from that of other C/EBP proteins, and CHOP-C/EBP heterodimers
are incapable of binding to a common class of C/EBP sites" [PMID:8657121] — this is the
structural basis of the dominant-negative behaviour.

**Activation.** Direct, promoter-level activation is best documented at *TNFRSF10B*/DR5:
"we identified a potential CHOP-binding site in the 5'-flanking region of the DR5 gene.
Mutation of this site abrogated the enhanced reporter activity in response to THG
treatment" [PMID:15322075]; and DR5 induction needs CHOP together with Elk1 and c-Jun
[PMID:22065586] and ATF3 [PMID:24939851]. *TRIB3*/TRB3 is the other canonical target:
"the tunicamycin response region in the TRB3 promoter contains amino-acid response
elements overlapping the CHOP-binding site, and CHOP and ATF4 cooperated to activate
this promoter activity" [PMID:15775988]. UniProt adds IL6, IL8, IL23, PPP1R15A/GADD34,
BBC3/PUMA, BCL2L11/BIM and ERO1L to the positively regulated set (`CC FUNCTION`).

**Repression.** Two mechanisms, both well documented:

1. *Promoter-associated repression with a partner.* At *ASNS*, "CHOP suppressed the
   induction of the endogenous asparagine synthetase (ASNS) gene and inhibited
   transcription from a reporter gene driven by the ASNS promoter following activation by
   ATF4 or amino acid deprivation", and "The CHOP-dependent repression of the ASNS gene
   required the entire CHOP protein, arguing against the possibility of simple
   sequestration of ATF4 by the CHOP leucine zipper domain, and chromatin
   immunoprecipitation analysis showed association of CHOP with the ASNS and TRB3
   promoters" [PMID:18940792]. So this is corepression at a locus, not just titration.
2. *Dominant-negative sequestration of another transcription regulator.* At *PPARG*,
   "ER stress-induced CHOP suppressed PPARγ transcription by sequestering C/EBPβ and
   limiting availability of C/EBPβ binding to the PPARγ promoter" [PMID:20829347]. The
   ATF3 heterodimer is likewise inert: "an ATF3-interacting protein, gadd153/Chop10,
   forms a nonfunctional heterodimer with ATF3: the heterodimer, in contrast to the ATF3
   homodimer, does not bind to the ATF/cyclic AMP response element consensus site"
   [PMID:8622660]. The founding paper for this mode is the mouse 1992 description of CHOP
   as "a dominant-negative inhibitor of gene transcription" (PMID:1547942, the IDA behind
   the mouse `GO:0140416` annotation).

**Coactivation of another regulator.** The mirror case exists too: mouse CHOP carries an
IDA for `GO:0140537` from "CHOP enhancement of gene transcription by interactions with
Jun/Fos AP-1 complex proteins" (PMID:10523647), and the human in vitro study reports
"stimulation of c-Jun and sucrase-isomaltase reporter activity in intestinal colon cancer
cells" [PMID:18534616]. This is a real but secondary mode.

**Partners.** IntAct lists ~40 bZIP partners for P35638 (`CC INTERACTION`), and two
systematic coiled-coil/bZIP-array studies account for most of the GOA protein-binding
rows [PMID:20102225, PMID:23661758]. Functionally characterised ones: ATF4
[PMID:18940792, PMID:11478948], ATF3 [PMID:8622660], CEBPB [PMID:20829347], FOXO3
[PMID:22761832], TRIB3 and EP300 [PMID:15775988, PMID:17872950], TCF7L2
[PMID:16434966]. Named complexes exist in GO: CHOP-C/EBP (`GO:0036488`), CHOP-ATF4
(`GO:1990617`), CHOP-ATF3 (`GO:1990622`).

## Position in the integrated stress response

CHOP is the pro-apoptotic transcriptional arm downstream of eIF2α-P/ATF4, and is the
standard readout for ISR activation. The two 2020 papers that defined the mitochondrial
branch used CHOP induction as the screen phenotype: "we combine genome engineering and
haploid genetics to unbiasedly identify genes that affect the induction of C/EBP
homologous protein (CHOP), a key factor in the integrated stress response... the
mitochondrial protease OMA1 and the poorly characterized protein DELE1, together with
HRI, constitute the missing pathway that is triggered by mitochondrial stress"
[PMID:32132706]; the companion paper reached the same OMA1-DELE1-HRI architecture
[PMID:32132707]. CHOP is therefore legitimately part of the HRI branch's output as well
as of ISR signalling generally; the GDF15 work annotates it for `GO:0140467`
[PMID:30639358] and the ATF4 mitochondrial-stress multi-omics study for the same
[PMID:28566324].

Both UPR transducer branches feed it: PERK/ATF4 and ATF6 (`CC INDUCTION`), reviewed in
[PMID:14685163] and [PMID:22934019]. QRICH1 was subsequently identified as a parallel
PERK-eIF2α effector [PMID:33384352].

## Apoptosis and the terminal UPR

The core downstream claim, `GO:0070059`, rests on several independent human lines:

- DR5 induction: "inhibition of CHOP expression attenuated DR5 up-regulation and
  apoptosis induced by THG, whereas ectopic expression of DR5 restored the sensitivity of
  CHOP siRNA-transfected cells to THG-induced apoptosis" [PMID:15322075].
- BH3-only induction in neurons: "CHOP... was found to regulate both PUMA and BIM
  expression in response to ER stress", and "CHOP knockdown prevents perturbations in the
  AKT (protein kinase B)/FOXO3a (forkhead box, class O, 3a) pathway in response to ER
  stress" [PMID:22761832].
- TRB3 induction: "knockdown of TRB3 expression decreased ER stress-dependent cell
  death... it is involved in CHOP-dependent cell death during ER stress" [PMID:15775988].
- A non-ER route in endothelium: "METH mediated endothelial cell apoptosis through
  Nupr1-Chop/P53-PUMA/Beclin1 signaling pathway" [PMID:27031958].
- ER calcium release via ERO1α-IP3R1 is the mouse IMP behind `GO:0051209`
  (PMID:19752026), and S1T amplifies ER stress "through the PERK-eIF2alpha-ATF4-CHOP
  pathway" [PMID:19061639].

## Secondary / peripheral roles

- **Wnt inhibition.** "CHOP inhibits TCF-dependent transcription in human embryonic and
  colon cancer cell lines... CHOP binds to TCF factors, thereby preventing the binding of
  TCF to its DNA recognition site" [PMID:16434966]. The same paper's Xenopus
  mRNA-injection experiments ("Injection of CHOP mRNA into early Xenopus laevis embryos
  suppresses dorsal organizer formation and inhibits secondary axis formation") are the
  basis of the `GO:2000016` and `GO:0009948` rows — a gain-of-function assay in a
  heterologous embryo, not evidence that human CHOP patterns the A/P axis.
- **Inflammation.** CHOP raises IL-8 via PPARγ repression and NF-κB
  [PMID:20829347]; in activated human T cells essential-amino-acid restriction "induced a
  stress response mediated by DNA damage-inducible transcript 3 to attenuate cytokine
  production via inhibition of NF-κB and NFAT activities" [PMID:24038088].
- **Thermogenesis.** "TLR4 activation by LPS abolished cAMP-induced up-regulation of
  uncoupling protein 1 (UCP1) in primary human adipocytes, which was reversed by
  silencing of C/EBP homologous protein (CHOP)" [PMID:26370079].
- **Myogenesis.** CHOP represses MYOD1 (`CC FUNCTION`; mouse IMP PMID:22242125).
- **Vascular phenotypes.** Mouse `Ddit3` carries IMP rows for blood vessel maturation
  (PMID:22265908, eNOS control of postnatal neovascularization) and, from a single
  ENPP1-deficiency neointimal-hyperplasia study (PMID:24530784), for artery development,
  vascular smooth-muscle migration and proliferation, response to wounding, response to
  PDGF and gene expression. Those six mouse rows are the sole basis of the corresponding
  human IEA rows and are treated as over-annotation here: CHOP expression was a readout in
  that study, not a demonstrated participant in arterial development.

## Annotation problems found in this review

- **90 of the 251 rows are bare `GO:0005515` protein binding**, from large interaction
  screens [PMID:20102225, PMID:23661758, PMID:32296183, PMID:33961781 and others]. Removed
  per the protein-binding policy; the informative replacements already exist
  (`GO:0046982`, `GO:0043522`, `GO:0008140`, `GO:0061629`, `GO:0042803`, and the three
  named complexes).
- **`GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process**
  (IDA, PMID:17872950) annotates CHOP as a *participant* in proteasomal degradation when
  the paper shows it is the *substrate*: "We have previously demonstrated that CHOP is
  regulated by the ubiquitin-proteasome system" and "The CHOP N-terminal domain is
  necessary not only for protein degradation but also for its transactivity"
  [PMID:17872950]. Being consumed by a process is not participation in it.
- **`GO:0005737` cytoplasm with the `is_active_in` qualifier** (IBA). Cytoplasmic
  localisation is correct, but CHOP's activity is nuclear; recorded as a `WRONG_QUALIFIER`
  source defect against GO_CENTRAL (`is_active_in` -> `located_in`).
- **`GO:0005770` late endosome** (IEA) traces to a single mouse IDA from an anthrax
  lethal-toxin/MLN64 study (PMID:23028046) with no human support; marked as
  over-annotated rather than removed, since the mouse full text was not read.
- **`GO:0010467` gene expression** is an uninformative process term for a transcription
  factor and traces to the ENPP1 mouse paper above.

## AltDDIT3

`P0DPQ6-1` (AltDDIT3) is an alternative-initiation ORF in the same transcript, listed by
UniProt as a separate entry and as an interactor of isoform 1
("[Isoform 1]: Interacts with isoform AltDDIT3 of DDIT3", `CC SUBUNIT`), discovered in
the altORF survey [PMID:29083303]. Per `projects/MICROPROTEINS.md` it is a separate
UniProt entry with its own GOA rows and would get its own folder; it is listed in
`alternative_products` here only because `fetch-gene` reads UniProt's
`ALTERNATIVE PRODUCTS` block. Not reviewed here.
