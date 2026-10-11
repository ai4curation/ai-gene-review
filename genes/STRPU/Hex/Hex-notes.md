# Hex (Strongylocentrotus purpuratus, UniProt A0A7M7R9J9) - curation notes

## Identity

- UniProt A0A7M7R9J9 (`A0A7M7R9J9_STRPU`, unreviewed/TrEMBL, 317 aa) is an
  EnsemblMetazoa-derived "Homeobox domain-containing protein" with no literature
  RX line. Cross-references: RefSeq XP_781292.3 / XP_030841717.1, GeneID 575826
  and GeneID 115918645 (two loci in the current assembly, both named by NCBI
  "hematopoietically-expressed homeobox protein HHEX homolog"; checked via NCBI
  gene esummary, 2026-10-03), PANTHER PTHR24324:SF5 (official label, from
  `interpro/panther/panther.obo`: "HEMATOPOIETICALLY-EXPRESSED HOMEOBOX PROTEIN
  HHEX"), FunFam 1.10.10.60:FF:000721 "Hematopoietically-expressed homeobox
  protein HHEX". Single homeodomain at 186-246 (PROSITE PS50071) flanked by
  disordered N- and C-terminal regions, as in vertebrate HHEX.
- The GRN gene `hex` (Oliveri, Tu & Davidson 2008, where it is cited to the
  homeobox survey of Howard-Ashby et al. 2006, ref. 5) is the sea urchin HHEX
  orthologue: Saunders & McClay state that of the 13 PMC EMT transcription
  factors they studied, "12 of the 13 TFs are the sole member of their subfamily
  represented in the sea urchin genome" and [PMID:24598159 "All orthologs but hex
  (hhex) are found within a subfamily of two or three members."], i.e. hex is the
  single HHEX-class gene. Since A0A7M7R9J9 is the only HHEX-subfamily homeodomain
  protein in the S. purpuratus proteome, the accession and the GRN gene are the
  same gene. Confidence: high. The only residual caveat is that the two NCBI
  GeneIDs (575826, 115918645) with identical descriptions may be assembly
  duplicates (haplotypes) rather than two genes; the UniProt entry maps to both.
- Community symbol: `Hex` (`hex`, `Sp-Hex`, `SpHex` in the GRN literature).
- The homeobox survey that first characterized the S. purpuratus homeobox
  complement (including hex) is abstract-only in the cache:
  [PMID:17055477 "A set of 96 homeobox transcription factors was identified in
  the Strongylocentrotus purpuratus genome ... QPCR time course measurements
  revealed that 65% of these genes are expressed within the first 48 h of
  development"]. Its hex-specific data (WMISH in the micromere lineage) are not
  visible in the cached abstract.

## Expression

- Zygotic, skeletogenic micromere / primary mesenchyme cell (PMC) lineage;
  listed among the genes expressed selectively in the large micromere-PMC
  lineage: [PMID:30264451 "These include alx4, dri, erg, fos, jun, foxB,
  foxN2/3, foxO, hex, mitf, nfkbil1L, nk7, nurr1, smad1/5/8, smad2/3, tbr, tel,
  and tgif"].
- Second, later domain in the oral non-skeletogenic mesoderm (NSM) after PMC
  ingression: [PMID:23261933 "At this time three genes that are first expressed
  in the SM, erg, hex, and ets1/2 are activated specifically in the oral NSM
  (Fig. 1O–R)."] [PMID:23261933 "The hex gene is activated next, followed by
  ets1/2."] The same cohort (gataC, ets1/2, hex, erg) characterizes sea star
  embryonic mesoderm [PMID:23261933 "the sea star embryonic mesoderm regulatory
  state resembles that of the oral NSM of sea urchins, including transcripts of
  gataC, etsl/2, hex, and erg"].

## Place in the skeletogenic micromere GRN (Oliveri, Tu & Davidson 2008)

- Upstream: hex lies downstream of nuclear beta-catenin and pmar1 (the
  double-negative gate) and of the first-tier regulators, especially ets1 and
  alx1: [PMID:30264451 "overexpression of pmar1 or a form of cadherin that
  interferes with β-catenin function have shown that erg, foxN2/3, hex, tel, and
  tgif are all downstream of β-catenin and pmar1 (Oliveri et al., 2008"];
  [PMID:30264451 "Oliveri et al. (2008) reported significant changes in the
  expression of erg, tgif, and hex following Ets1 knockdown, while Rafiq and
  co-workers (Rafiq et al., 2014) did not detect such changes."] (so the ets1 ->
  hex input is reported by one lab and not reproduced by the other).
- Position: the dynamic state-stabilization subcircuit immediately downstream
  of alx1/ets1/tbr/tel: [PMID:18413610 "immediately downstream of the initial
  four regulatory genes activated by the double negative gate ( Fig. 2 A ), three
  additional genes are activated: one encoding the Ets family factor Erg ( 9 ),
  and the other two, hex and tgif , encoding homeobox factors ( 5 )"].
- Feedback: [PMID:18413610 "These genes are engaged in interlocking positive
  double feedback loops ( erg with hex ; and hex with tgif ). Interference with
  expression of any of these genes severely depresses transcript levels of the
  others ( Fig. S3 ). Thus they dynamically stabilize all aspects of the
  regulatory state downstream of themselves."] Hex is the hub of both loops.
- Outputs: [PMID:18413610 "In addition to tgif , the outputs of hex go to erg ,
  to differentiation genes as we see below, and to foxo , a late activated
  regulatory gene the functions of which occur beyond the time frame of this
  GRN."]
- Differentiation genes: hex is one of the feed-forward drivers of the
  biomineralization gene battery [PMID:18413610 "these differentiation genes
  require as drivers products of all of the now familiar components of the
  skeletogenic regulatory state ( alx1 , ets1 , tbr , tel , erg , hex , foxb ,
  dri )"].
- Phenotype of hex MASO (the key loss-of-function result): skeleton-minus with
  normal ingression, i.e. a differentiation rather than an EMT defect in S.
  purpuratus: [PMID:18413610 "interference with their expression produces a
  skeleton-minus phenotype, as illustrated in Fig. 3 B–G for tbr , hex , tgif ,
  ets1 , and alx1"]; [PMID:18413610 "This is not the case for tbr , hex , or
  tgif : interference with their expression results in embryos with a full
  complement of ingressed cells of the micromere lineage but these cells are
  unable to create the biomineral skeleton. ( Fig. 3 C–E )."]
- Interpretation of the loop by Ettensohn's group: [PMID:30264451 "One prominent
  example is a set of mutual regulatory interactions among erg, hex, and tgif
  that reinforces the expression of all three genes."] [PMID:30264451 "Such
  feedback loops may convert the transient expression of pmar1 into a more
  stable regulatory state in the skeletogenic lineage and buffer against initial
  variation in the level of expression of these genes."]

## Lytechinus variegatus EMT data (Saunders & McClay 2014; not S. purpuratus)

- LvHex was cloned from the Sp annotation and knocked down with two MASOs;
  hex is one of the 10 downstream PMC TFs required for EMT: [PMID:24598159 "the
  10 TFs downstream of those (tel, erg, hex, tgif, snail, twist, foxn2/3, dri,
  foxb, foxo) were also required for EMT."] Specifically it is a terminal node
  of the apical-constriction and motility sub-circuits: [PMID:24598159 "apical
  constriction is controlled by a complex forward cascade that feeds into five
  terminal TFs: tel, hex, foxn2/3, foxb and foxo."] [PMID:24598159 "Foxn2/3, hex
  and foxo do not have any regulatory inputs into one another, and therefore the
  motility sub-circuit functions via parallel inputs."] In the Lv PMC GRN "snail
  regulates erg and erg regulates hex".
- This contrasts with the S. purpuratus result that hex morphants ingress
  normally (Oliveri 2008, Fig. 3C-E). Because of the species difference and the
  conflicting ingression phenotype, no EMT annotation is proposed for the Sp
  gene product; recorded as a question.

## Curation decisions

- All seven GOA rows are electronic (IEA InterPro/UniRule, IBA PAINT on the HHEX
  node PTN001963821). The IBA rows (sequence-specific cis-regulatory DNA
  binding, regulation of Pol II transcription, cell differentiation) are
  consistent with the GRN data and were accepted / kept as non-core. Generic
  DNA binding (IEA) -> MODIFY to sequence-specific DNA binding. Generic
  regulation of DNA-templated transcription -> KEEP_AS_NON_CORE.
- NEW (all IMP from Oliveri 2008 morpholino/QPCR and phenotype data):
  GO:0045944 positive regulation of transcription by RNA polymerase II (hex
  drives erg, tgif, foxo and the differentiation genes), GO:0001710 mesodermal
  cell fate commitment (state lockdown of the skeletogenic mesenchyme), and
  GO:0070169 positive regulation of biomineral tissue development (skeleton-
  minus phenotype with normal ingression). No activator MF (GO:0001228) because
  no cis-regulatory or binding assay exists for Sp-Hex; the sign is inferred
  from perturbation only.
- `gocams/index.tsv` has no entry for A0A7M7R9J9.
- Sibling reviews with the same subcircuit: Erg (genes/STRPU/Erg), Ets1, Alx1.
