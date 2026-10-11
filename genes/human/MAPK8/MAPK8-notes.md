# MAPK8 (JNK1) curation notes

UniProt P45983; HGNC MAPK8; synonyms JNK1, SAPK1c, PRKM8. CMGC Ser/Thr kinase, MAP kinase
subfamily, JNK branch (InterPro IPR008351 MAPK_JNK; PANTHER PTHR24055).

## Identity and activation

- Proline-directed Ser/Thr MAP kinase; activation-loop TPY motif (Thr183/Tyr185).
  [file:human/MAPK8/MAPK8-uniprot.txt "Dually phosphorylated on Thr-183 and Tyr-185 by MAP2K7 and MAP2K4"]
- MKK4 prefers Tyr185, MKK7 prefers Thr183; the two act synergistically.
  [PMID:11062067 "MKK4 shows a striking preference for the tyrosine residue (Tyr-185), and MKK7 a striking preference for the threonine residue (Thr-183)"]
- MKK7 docks on JNK1 through three N-terminal D-sites; D-site peptides compete with substrates.
  [PMID:16533805 "Full-length MKK7 containing combined D1/D2 mutations was compromised for binding to JNK1 and exhibited reduced JNK1 kinase activity"]
- Pin1 isomerises the phospho-Thr-Pro in the activation loop, promoting activation and substrate association.
  [PMID:21660049 "Pin1 associates with JNK1, and then catalyzes prolyl isomerization of the phospho-Thr-Pro motif in JNK1 from trans- to cis-conformation."]
- Inactivated by dual-specificity phosphatases (MKP-7/DUSP16, DUSP8, MKP-1).
  [PMID:11489891 "MKP-7 works as a JNK-specific phosphatase in vivo"]
- Scaffolds: JIP1/MAPK8IP1, JIP2/MAPK8IP2, JIP3, JIP4. JIP1 also retains JNK1 in the cytoplasm and
  inhibits it (structural basis PMID:15141161).
  [PMID:15141161 "Overexpression of JIP1 deactivates the JNK pathway selectively by cytoplasmic retention of JNK"]

## Molecular function (core)

- MAP kinase activity (GO:0004707), JUN kinase activity (GO:0004705): c-Jun Ser63/73, ATF2, Elk-1.
  [PMID:8654373 "The protein kinase activity of these JNK isoforms was measured using the transcription factors ATF2, Elk-1 and members of the Jun family as substrates."]
- JDP2 and ATF2 phosphorylated by human JNK1 co-expressed in E. coli (direct activity).
  [PMID:18307971 "we were able to phosphorylate mouse and human Jun dimerization protein 2 (JDP2) and human activation transcription factor 2 (ATF-2) by the action of human JNK1"]
- Many other direct substrates (all with in vitro kinase evidence):
  - HSF1 (inhibitory) [PMID:10747973 "JNK binds to HSF-1 in the conserved mitogen-activated protein kinases binding motifs and phosphorylates HSF-1 in the regulatory domain"]
  - BAD Thr201 (pro-survival) [PMID:14967141 "JNK phosphorylates BAD at threonine 201, thereby inhibiting BAD association with the antiapoptotic molecule BCL-X(L)"]; EPO-driven in erythroid cells [PMID:21095239]
  - SIRT1 Ser27/Ser47/Thr530 [PMID:20027304 "human SIRT1 was phosphorylated by JNK1 on three sites: Ser27, Ser47, and Thr530"]
  - SIRT6 Ser10 [PMID:27568560 "phosphorylates SIRT6 on serine 10 in response to oxidative stress"]
  - YAP [PMID:21364637 "We identified JNK1 and JNK2 as robust YAP kinases"]
  - Cdt1 Thr29 [PMID:21856198 "JNK phosphorylates Cdt1 on threonine 29"]
  - NFAT3 Ser213/217 [PMID:17875713]
  - 4E-T/EIF4ENIF1 (P-body assembly) [PMID:22966201]
  - BMAL1/CLOCK [PMID:22441692 "preactivated JNK1, JNK2 or JNK3 phosphorylated glutathione S -transferase (GST)–BMAL1"]
  - NLRP3 Ser194 (inflammasome priming) [PMID:28943315 "JNK1-mediated NLRP3 phosphorylation at S194 is a critical priming event"]
  - ALKBH5 (ERK/JNK) [PMID:34048572]
  - BIM, BMF (release from dynein/myosin V motor complexes) [Reactome:R-HSA-139918, R-HSA-139908]
  - BCL2 (autophagy) [PMID:26546165 "Phosphorylation of Bcl-2 in response to starvation is mediated by JNK1"]
  - Elk-1 (via Rev7) [PMID:17296730]; HSF4b [PMID:16581800]; CapZIP [PMID:15850461]

## Processes

- Core: JNK cascade (GO:0007254) / stress-activated MAPK cascade (GO:0051403); terminal kinase tier.
- Downstream/pleiotropic (non-core): apoptosis (both pro- and anti-apoptotic depending on context:
  BIM/BMF release vs BAD inactivation), autophagy (BCL2), NLRP3 inflammasome priming, circadian
  photic response, DNA repair (SIRT6), energy homeostasis/insulin resistance (mouse), neuronal
  development (basal dendrites; mouse TAOK2 paper PMID:22683681), responses to UV, ROS, LPS,
  amino acid (glutamine) deprivation.
- Inhibitor-only (SP600125) evidence cannot distinguish JNK1/2/3: CD38 induction/cyclase activity
  (PMID:22027397), DR5 expression (PMID:22065586; JNK siRNA not isoform specific).

## Localization

- Cytoplasm and nucleus; active JNK translocates to nucleoplasm to phosphorylate TFs.
  [Reactome:R-HSA-450348 "c-Jun NH2 terminal kinase (JNK) plays a role in conveying signals from the cytosol to the nucleus"]
- HA-JNK1 uniform cytoplasm + nucleus [PMID:22966201 "Immunofluorescence of HA-tagged JNK1 in untreated U2OS cells resulted in uniform staining throughout the cytoplasm and the nucleus"]
- Neuronal: axons/synapses (rodent, ISS).

## Annotation issues noted

- GO:1903749 (TAS, Reactome BIM/BMF) is obsolete in current GO (QuickGO: "represents a phenotype and was
  added in error"); replace with positive regulation of intrinsic apoptotic signaling pathway (GO:2001244).
- GO:0120283 IPI PMID:11865055 WITH/FROM UniProtKB:P27448 (MARK3, "C-TAK1"), but the paper studies
  TAK1 = MAP3K7 ("XIAP, NAIP, and JNK1 bind to TAK1"). The term remains correct (TAK1 is a Ser/Thr
  kinase) but the partner identifier looks mis-mapped.
- GO:0071260 IEP PMID:19593445: the cached full text (BAD in prostate cancer) never mentions JNK or a
  mechanical stimulus; could not verify -> UNDECIDED.
- GO:0005515 rows: replaced with partner-class MFs consistent with MAPK14/MAPK1 reviews
  (MAPKK binding, scaffold protein binding, protein phosphatase binding, protein kinase binding,
  DNA-binding transcription factor binding); non-informative partners (CBL, PIK3R1, CLDN6, RPTOR,
  EIF4ENIF1, Pdcd4, MECOM, APBB1) removed.
- GO-CAMs: 635b1e3e00002004 (NLRP3 inflammasome, MAPK8 kinase -> positive regulation of NLRP3
  inflammasome assembly), 622aace900000522 (SIRT6/oxidative stress), 6494e2e900002525 (energy homeostasis).

## Isoform/paralog caveat

Most "JNK" literature uses pan-JNK reagents (SP600125, phospho-JNK antibodies). JNK1 and JNK2 are
redundant for many functions (shared PAINT node PTN001171982), so process annotations based on
inhibitor data are weak for MAPK8 specifically.

## Review session log (2026-09-25)

Audited the notes above against cached sources (quotes used in the review were checked by the
reference validator). Final decisions in MAPK8-ai-review.yaml:

- Core: GO:0004707 MAP kinase activity / GO:0004705 JUN kinase activity in GO:0007254 JNK cascade
  (IBA PTN001171982 accepted; consistent with modules/jnk_cascade.yaml). GO:0106310 and GO:0004674
  experimental rows accepted (as in MAPK14).
- GO:0005515 rows: MKK4/MKK7 -> GO:0031434; JIP1/JIP2/JIP-1b -> GO:0097110; DUSP8 -> GO:0019903;
  JNK2 -> GO:0019901 (MAPK14 convention); c-Jun and HSF1 -> GO:0140297. Removed: MECOM, Pdcd4, CBL,
  PIK3R1 (x2), APBB1, H2AX, EIF4ENIF1, RPTOR, CLDN6.
- GO:0120283 (TAK1 row): full text confirms TAK1 = MAP3K7 ("TAK1 is an upstream MAP3 kinase that
  activates JNK1 and p38"); WITH/FROM P27448 (MARK3/C-TAK1) looks mis-mapped. MODIFY -> GO:0031435.
- GO:1903749 (obsolete per QuickGO) x2 -> GO:2001244 positive regulation of intrinsic apoptotic
  signaling pathway.
- GO:0035033 histone deacetylase regulator activity: MARK_AS_OVER_ANNOTATED (kinase acting on SIRT1).
- GO:0071260 IEP PMID:19593445 and GO:0009612 IBA (PTN008602925, only descendant = MAPK8 itself):
  UNDECIDED, same stance as MAP2K4/MAP3K1.
- Inhibitor/pan-JNK process rows (CD38 cyclase, protein metabolic process, DR5 gene expression) and
  Reactome cell killing: MARK_AS_OVER_ANNOTATED.
