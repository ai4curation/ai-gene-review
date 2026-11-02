# TFAP2B (AP-2beta, Q92481) review notes

## 2026-10-08 — initial review (claude-code, project NEURAL_CREST_ORIGINS, Tier 4)

### Identity and molecular activity

- AP-2beta is a sequence-specific AP-2 family transcription factor. It binds GCC(N3)GGC-type sites and activates
  AP-2-dependent promoters [PMID:7555706 "AP-2 beta binds specifically to a series of well-characterized AP-2 binding sites, consensus to the sequence G/CCCN3GGC, and transactivates transcription from a reporter plasmid under the control of an AP-2-dependent promoter."].
- It dimerizes through the conserved C-terminal HSH domain, both with itself and with AP-2alpha
  [PMID:7555706 "A C-terminal domain known to mediate homodimerization of the previously cloned AP-2 alpha transcription activator is highly conserved and sufficient to mediate interaction between the two proteins."].
  Char syndrome missense mutants still dimerize but bind DNA abnormally and poison wild-type TFAP2B
  [PMID:10802654 "Mutant TFAP2B proteins dimerized properly in vitro, but showed abnormal binding to TFAP2 target sequence."],
  [PMID:10802654 "Dimerization of both mutants with normal TFAP2B adversely affected transactivation, demonstrating a dominant-negative mechanism."],
  [PMID:11505339 "two, R225C and R225S, failed to bind target sequence in vitro and that all four had dominant negative effects when expressed in eukaryotic cells"].
- Coactivator: CITED2 (with p300/CBP) [PMID:11694877 "We show that CITED2 interacts with and co-activates all isoforms of transcription factor AP-2 (TFAP2)."],
  [PMID:12586840 "CITED2 interacted with the dimerization domain of TFAP2C, which is highly conserved in TFAP2A/B."].
  Corepressor-like inhibitor: KCTD1 [PMID:19115315 "we found that KCTD1 interacted with three major members of the AP-2 family and inhibited their transcriptional activities"].
  SUMOylation by UBC9 lowers activity [PMID:12072434 "Transient transfection studies indicate that sumolation of AP-2 decreases its transcription activation potential"].
- Repression is context-dependent: in chick, TFAP2B represses TFAP2C, probably directly
  [PMID:31848212 "TFAP2B overexpression resulted in the strong down-regulation of TFAP2C mRNA levels in the neural folds, whereas TFAP2A expression remained unchanged"];
  in mouse limb it activates Bmp2 and represses Bmp4 [PMID:21829553 "due to direct control of Bmp2 and Bmp4 promoter activity by Tfap2b"].
- MF conclusion: GO:0001228 (activator) is core; GO:0042803/GO:0046982 dimerization are accepted;
  CITED2 rows -> GO:0001223, KCTD1 -> GO:0001222 (consistent with the TFAP2A review). No pioneer-factor MF term exists.

### Name confusion: PMID:7559606 ("AP-2B") is about an AP-2alpha isoform

- Two IDA rows (GO:0001228, GO:0000122) cite Duan & Clemmons 1995. The cached abstract uses a human AP-2 (alpha) expression
  construct and "AP-2B" as a dominant negative: [PMID:7559606 "In AP-2 abundant fibroblasts, expression of AP-2B, a dominant-negative inhibitor of AP-2, suppressed IGFBP-5 promoter activity."].
  AP-2B is an alternatively spliced product of the AP-2alpha gene (TFAP2A), not AP-2beta:
  [PMID:8321221 "Analysis of overlapping genomic clones spanning the entire AP-2 gene proves that AP-2A and AP-2B transcripts are alternatively spliced from the same gene."].
  AP-2beta was only cloned the month before (PMID:7555706, Sept 1995). Both rows REMOVED; the activator function is kept
  by the PMID:7555706 IDA rows. Report to the source curator.

### Network layer: neural crest specifier (not a border specifier)

- Chick (Rothstein & Simoes-Costa 2020, full text). TFAP2B comes on only at the onset of specification
  [PMID:31848212 "TFAP2B transcripts were not detected until just before the onset of specification, when the gene became robustly expressed in the neural crest lineage"].
  Knockdown spares the border and disrupts specification
  [PMID:31848212 "TFAP2B knockdown produced no effects on the neural plate border but resulted in the disruption of the specification program"].
  It forms heterodimers with TFAP2A in vivo [PMID:31848212 "Pulldown of TFAP2A with streptavidin beads resulted in co-IP of both FLAG-tagged TFAP2B and TFAP2C, confirming that these factors form heterodimers in avian embryos"]
  and recruits TFAP2A to specification enhancers [PMID:31848212 "Together, these data support the idea that TFAP2B is required for the recruitment of TFAP2A to specification loci."].
  TFAP2C cannot replace it [PMID:31848212 "These results indicate that TFAP2B is specialized in its ability to promote neural crest specification."],
  and premature TFAP2B drives premature specification [PMID:31848212 "this manipulation resulted in a premature onset of specification, with early activity of NC1 in the reprogrammed side of the embryo"].
  Upstream: TFAP2A/C heterodimers plus induction genes activate TFAP2B; TFAP2B then represses TFAP2C (the partner switch).
- Frog: Pax3 and Zic1 activate tfap2b without new protein synthesis
  [PMID:24360906 "We demonstrated that the neural border specifiers Pax3 and Zic1 are direct upstream regulators of neural crest specifiers Snail1/2, Foxd3, Twist1, and Tfap2b."].
  Note: the body of the same paper lists tfap2b among "known neural border specifiers"; the abstract calls it a crest
  specifier. The chick timing data settle the layer.
- Chick cranial circuit: Lhx5/Dmbx1 activate Tfap2b, and Tfap2b activates Ets1
  [PMID:27339986 "Finally, Tfap2b activates expression of Ets1 as the neural crest becomes specified"].
  Sox8 + Tfap2b + Ets1 together (not singly) reprogram trunk crest to cranial, chondrogenic identity
  [PMID:27339986 "Early cranial-specific factors (Brn3c, Lhx5 and Dmbx1), or individual late factors, were unable to activate the cranial enhancer in the trunk."],
  [PMID:27339986 "Thus, introducing components of the cranial-specific transcriptional circuit is sufficient to reprogram trunk neural crest and to drive them to adopt an additional cartilaginous fate."].
  But Tfap2b expression itself is pan-axial in chick and skate [PMID:31645763 "In contrast to their cranial-specific expression, Tfap2b and Sox10 are pan-NC genes expressed all along the body axis"]:
  what is cranial-specific is the circuit wiring, not TFAP2B.
- Mouse: TFAP2B is largely redundant with TFAP2A in crest. Single Tfap2b KO crest forms; sympathetic ganglia are reduced
  by progenitor apoptosis [PMID:21539825 "In the AP-2β knockout only sympathetic ganglia (SG) are targeted, leading to a reduction in ganglion size by about 40%, which is also caused by apoptotic death of neural crest progenitors."];
  the double KO loses sympathetic and sensory ganglia [PMID:21539825 "The elimination of both AP-2α and AP-2β results in the virtually complete absence of sympathetic and sensory ganglia due to apoptotic cell death of migrating NCC."].
  Van Otterloo 2022 (full text) states that in mouse no AP-2alpha/beta heterodimer function is irreplaceable
  [PMID:35333176 "One notable observation, though, is that no unique and irreplaceable function exists for any AP-2α/ß heterodimers in the mouse ectoderm or neural crest."].
- Zebrafish: tfap2a+tfap2b double deficiency removes crest cartilage, via ectoderm [PMID:15944192 "Zebrafish embryos deficient for both tfap2a and tfap2b show defects in epidermal cell survival and lack NCC-derived cartilages."];
  tfap2b crispants have fewer enteric neurons [PMID:35874825 "Disruption of tfap2b in zebrafish led to decreased enteric neuronal numbers and delayed transit time."].

### Decision on the NC-branch term

- **GO:0014036 neural crest cell fate specification, NEW (ISS, from chick PMID:31848212).** Not GO:0014029: TFAP2B has no
  border role (absent at border stages; knockdown spares border markers), so the border-inclusive term would misplace it.
  Not GO:0014034: GO:0014036 is part_of GO:0014034 and the evidence is specifically on the reversible specification step
  (timing, enhancer recruitment). This matches the project convention (crest specifiers -> GO:0014036).
- Participation test: passed. TFAP2B is a DNA-binding heterodimer partner that itself occupies specification enhancers
  and redirects TFAP2A there; it does part of the work, not merely being required.
- Caveat for curators: necessity is shown only in chick. In mouse TFAP2B is redundant with TFAP2A. Redundancy does not
  negate participation, but the transfer to human rests on one species plus conserved protein activity and on human
  Char syndrome being a crest-derivative disorder [PMID:10802654 "suggests that Char syndrome results from derangement of neural-crest-cell derivatives"].
  Flagged for sign-off.

### Comparator check (QuickGO, 2026-10-08)

Query: annotations to GO:0014029/GO:0014033/GO:0001755/GO:0014032 and descendants (is_a, part_of), all evidence, all taxa.
- No TFAP2B in any species (human Q92481, mouse Q61313, rat, chicken A0A8V0XPT7 etc., X. laevis tfap2b.L, X. tropicalis,
  zebrafish tfap2b) carries any neural-crest-branch term.
- Paralogs: zebrafish tfap2a carries GO:0014036 (IMP, PMID:14534133; IGI PMID:20885782) and GO:0014032; zebrafish tfap2c carries
  GO:0014036 (IGI, PMID:20885782) and GO:0014032; mouse Tfap2a GO:0014032 (IMP, PMID:8622766); rat Tfap2a GO:0014032 (ISO).
  Human TFAP2A/C/D/E: none in GOA (TFAP2A has a NEW GO:0014029 in this repository only).
- Same-layer peers (frog sox10, sox9-a, sox8, snai2, snai1) carry GO:0014036 (see project notes).
- Interpretation: the absence on TFAP2B is explained, not a convention. The paralog-specific specification evidence is a
  single 2020 chick paper, and chicken TFAP2B entries are unreviewed TrEMBL with only electronic annotation; mouse and
  zebrafish single mutants do not block specification because of redundancy. Mouse Tfap2b does carry crest-derivative
  terms (GO:0048485 sympathetic NS development, IGI PMID:21539825); zebrafish tfap2b carries GO:0048484 enteric NS
  development (IMP, PMID:35874825) and GO:0051216 cartilage development (IGI, PMID:15944192).
- No GO-CAM model in gocams/index.tsv contains TFAP2B.

### Other roles (pleiotropic, outside the crest GRN)

- Ductus arteriosus: human Char syndrome / PDA2; mouse KO ductus stays open
  [PMID:21829553 "Histological examination of ductus arteriosus from Tfap2b knockout mice 6 hours after birth revealed that they were not closed."];
  ductal smooth muscle programme [PMID:18635823 "Our data indicate that Tfap2beta, Et-1, and Hif2alpha act in a transcriptional network during ductal smooth muscle development"].
- Limb: [PMID:21829553 "Lack of Tfap2b resulted in bilateral postaxial accessory digits."].
- Kidney: distal tubule/collecting duct epithelial survival [PMID:9271117 "At the end of embryonic development expression of bcl-X(L), bcl-w, and bcl-2 is down-regulated in parallel to massive apoptotic death of collecting duct and distal tubular epithelia."],
  [PMID:12695560 "our studies reveal essential, nonredundant roles of AP-2 beta in renal tubular functions"]. Not seen in Char patients.
- Sympathoadrenal / noradrenergic neurons: survival of progenitors (mouse) and noradrenergic differentiation in neuroblastoma
  [PMID:26598443 "In IMR-32 cells, TFAP2B induced neuronal differentiation, which was accompanied by up-regulation of the catecholamine biosynthesizing enzyme genes DBH and TH"].
- Adipocyte / T2D association rows (PMID:15940393, 19325541, 16373396): genetic association plus overexpression; glucose
  metabolism and insulin secretion IMP rows judged over-annotated.
- Retinoblastoma overexpression rows (PMID:20607706): over-annotated, matching the TFAP2A review.

### Evolution

- Amphioxus has a single AP-2, expressed in non-neural ectoderm, not at the border [PMID:31645763 "the basal chordate Amphioxus lacks expression at the neural plate border of genes like Dmbx, Brn3, Ets, as well as core NC genes like SoxE, FoxD, Tfap2, and Id, although these genes are expressed in other tissues"].
- Lamprey Tfap2 is expressed in crest at all axial levels [PMID:31645763 "Tfap2 was enriched at all axial levels in both chicken and lamprey"].
- The TFAP2A/B/C paralogs come from the vertebrate genome duplications. Rothstein & Simoes-Costa read the nested
  expression as subfunctionalisation [PMID:31848212 "the expression patterns of TFAP2C and TFAP2B are contained within the TFAP2A expression domain, suggesting subfunctionalization of these paralogs over the course of evolution"].
  So the border->crest partner switch is a jawed-vertebrate (at least amniote) elaboration of a crest role that one AP-2
  already played in the vertebrate ancestor; how the partition is drawn differs between lineages (chick: non-redundant
  B for specification; mouse: A dominant, B redundant; zebrafish: A+C for induction).

### Module suggestions (not edited here)

- Crest fate specification part: TFAP2A–TFAP2B heterodimer annoton (GO:0001228 / GO:0046982, part_of GO:0014036).
- Edges: Pax3+Zic1 -> tfap2b (frog, translation-independent); TFAP2A/C + border genes -> TFAP2B (chick CUT&RUN peaks in locus);
  TFAP2B -| TFAP2C (chick, likely direct); TFAP2A/B -> FOXD3 NC1, SOX9, SNAI2, SOX10 enhancers; Tfap2b -> Ets1 (chick ChIP).
- Cranial ectomesenchyme part: Sox8–Tfap2b–Ets1 combination (sufficient only together).
