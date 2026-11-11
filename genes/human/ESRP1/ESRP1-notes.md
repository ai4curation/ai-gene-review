# ESRP1 (human, Q6NXG1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ESRP1 was selected as the closest experimentally characterised relative
(ortholog) of the shark benchmark protein CALMI/A0A4W3GVU1. This review treats
human ESRP1 in its own right; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human ESRP1 --fallback perplexity-lite` failed:
falcon returned `403 Forbidden` at Edison auth (`Failed to authenticate`), and the
perplexity-lite fallback returned HTTP 401 `insufficient_quota`. No deep-research
file exists. The review was written from the cached primary literature below
(full text read where available) plus the UniProt record.

Additional papers cached with `just fetch-pmid` (IDs looked up via PubMed esearch):
PMID:20711167, PMID:19829082, PMID:22354987 (abstract only), PMID:26371508,
PMID:29107558.

### Evolutionary grounding

- PANTHER 19.0 classification (local `.cache/panther/PTHR19.0_human`,
  `PTHR19.0_mouse`, `PTHR19.0_fruit_fly`): human ESRP1 Q6NXG1 and mouse Esrp1
  Q3US41 are both in PTHR13976:SF37 (EPITHELIAL SPLICING REGULATORY PROTEIN 1);
  human ESRP2 Q9H6T0 is SF30; Drosophila fusilli (FBgn0023441) is SF25. So the
  mouse ISS donor is a same-subfamily 1:1 ortholog, while ESRP2 and fusilli are
  paralog/outgroup members of the ESRP clade.
- PAINT (interpro/panther/PTHR13976/PTHR13976-paint.tsv):
  - PTN001018050 (taxon:6072, Eumetazoa): GO:0003729 mRNA binding IBD, seeded by
    fusilli, ESRP1, ESRP2. ESRP1 is itself a seed (its IDA).
  - PTN000360053: GO:0005654 nucleoplasm, GO:0003723 RNA binding, GO:0043484
    regulation of RNA splicing IBD; seeds include hnRNP H1/H2/F, GRSF1-related,
    ESRP1, ESRP2.
  - PTN000359854 (taxon:2759): GO:1990904 ribonucleoprotein complex, seeded by
    hnRNP H1/F/H2 only (no ESRP seed).
- Family review PTHR13976-review.yaml has one term assessment (GO:0005634
  nucleus, scope UNRESOLVED); this review does not REMOVE nucleus.

### Experimental evidence on human ESRP1 itself

- PMID:19285943 (Warzecha 2009, full text): cDNA expression screen for FGFR2 exon
  IIIb regulators found Rbm35a/b (ESRP1/2). UV crosslinking in 293T nuclear extract
  with FLAG-mouse Esrp1 binds WT ISE/ISS-3 but not GU→AC mutant; endogenous human
  ESRP1 pulled down from KATO III nuclear extract by WT but not mutant ISE/ISS-3 RNA
  [PMID:19285943 "Immunoreactive bands of the expected size for ESRP1 and ESRP2 were identified in pulldowns from the wild-type, but not the mutant 3X ISE/ISS-3 sequence"].
  siRNA of ESRP1+ESRP2 in human PNT2 cells switches FGFR2 IIIb→IIIc; rescue with
  RNAi-resistant mouse Esrp1. Also regulates CD44, CTNND1, ENAH splicing.
  Note: much of the binding/overexpression work used mouse cDNA in human cells; the
  endogenous-protein pulldown and knockdown are on human ESRP1.
- PMID:19829082, PMID:20711167: genome-wide ESRP-regulated splicing in human
  epithelial lines; UGG/GGU-rich binding motif and position-dependent RNA map
  (downstream intronic binding → inclusion; exonic/upstream → skipping)
  [PMID:20711167 "binding sites in the downstream intron promote exon inclusion and binding within or upstream of an exon promote exon skipping"].
- PMID:22354987 (abstract only): ESRP regulates splicing and alternative
  polyadenylation; SELEX-Seq for ESRP1 motifs.
- PMID:29107558: biallelic ESRP1 mutations cause SNHL (DFNB109); patient iPSCs show
  splicing defects corrected by allele repair. Cochlear cell-fate phenotypes are
  from Esrp1-/- mouse embryos — downstream organismal consequences of a splicing
  regulator.
- PMID:26371508: mouse Esrp1 KO is neonatal lethal with cleft lip/palate; skin
  barrier defects with Esrp1/2 epidermal deletion. Phenotypes, not participation.

### Decisions summary

- MF core: mRNA binding (ACCEPT), plus NEW GO:0097157 pre-mRNA intronic binding
  (IDA, PMID:19285943; note GO:0097157 is under pre-mRNA binding, not under mRNA
  binding in GO, so it is not redundant with GO:0003729).
- BP core: regulation of RNA splicing → MODIFY to GO:0000381 regulation of
  alternative mRNA splicing, via spliceosome (is_a descendant, verified with
  runoak ancestors).
- CC: nucleoplasm ACCEPT; nucleus MODIFY → nucleoplasm; nuclear body (HPA)
  non-core; RNP complex IBA non-core.
- Protein binding (37 IPI rows, high-throughput Y2H/interactome screens): REMOVE as
  uninformative per protein-binding policy; the interactions are not disputed.
- GO:0042669 inner ear auditory receptor cell fate specification (ISS from mouse):
  MARK_AS_OVER_ANNOTATED — knockout developmental phenotype downstream of
  splicing regulation.
