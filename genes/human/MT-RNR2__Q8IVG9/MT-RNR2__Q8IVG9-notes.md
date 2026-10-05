# Humanin (Q8IVG9, HUNIN_HUMAN) — curation notes

Folder follows the `<HOST>__<ACC>` convention for alternative-ORF peptides
(CLAUDE.md, "Alternative-ORF peptides"): UniProt files humanin under the host
symbol `MT-RNR2`, the mitochondrial 16S rRNA gene, and the peptide has its own
accession and its own GOA rows (76).

## 1. What the gene is

Humanin (HN) is a 24-residue peptide (`MAPRGFSCLL LLTSEIDLPV KRRA`) whose ORF
lies inside the mitochondrial 16S rRNA gene MT-RNR2. It was found by functional
screening of an Alzheimer brain cDNA library for a factor protecting neurons
from familial AD genes [PMID:11371646 "A rescue factor abolishing neuronal cell
death by a wide spectrum of familial Alzheimer's disease genes and Abeta"].

## 2. The coding question is genuinely unresolved

UniProt itself carries a CAUTION on this entry. Three distinct uncertainties:

1. **Genetic code / peptide length.** The ORF read with the cytoplasmic code
   gives 24 aa; read with the mitochondrial code the last three residues are
   lost (21 aa). UniProt: "If translation of the mRNA occurs in the
   mitochondrion rather than in the cytoplasm, then the usage of the
   mitochondrial genetic code would lead to the production of a shorter peptide
   lacking the last three C-terminal residues."
2. **Where translation happens.** No mechanism has been shown for export of an
   mtDNA-encoded mRNA to the cytoplasm, nor for secretion of a peptide made in
   the matrix. UniProt: "The mechanisms allowing the production and the
   secretion of humanin remain unclear."
3. **Which locus actually makes the active peptide.** 13 nuclear MT-RNR2-like
   loci (NUMT-derived MTRNR2L1-13) are predicted to encode 15 full-length
   HN-like peptides, and at least ten are expressed [PMID:19477263 "We provide
   bioinformatic and expression data suggesting the existence of 13 MT-RNR2-like
   nuclear loci predicted to maintain the open reading frames of 15 distinct
   full-length HN-like peptides"]. Guo et al. made the same point from the other
   direction [PMID:12732850 "Notably, the mitochondrial genome contains an
   identical open reading frame, and the mitochondrial version of HN can also
   bind and suppress Bax"]. In-vivo peptide detection used an anti-HN antibody
   that cannot distinguish the mitochondrial product from the nuclear paralogs
   [PMID:12009529 "Immunoblot analysis detected a 3-kDa protein with HN
   immunoreactivity in the testis and the colon in 3-week-old mice"].

Consequence for curation: every immunodetection-based localization row on this
entry (nucleus, mitochondrion, sperm compartments) is in principle a statement
about "HN immunoreactivity", not about this accession specifically. I have not
used this to remove well-replicated locations, but it is the reason I treat the
single-study nuclear and perinuclear rows as over-annotations.

A second, pervasive caveat: most functional work uses **synthetic peptide added
exogenously**, frequently at micromolar concentrations, and frequently the
S14G ("HNG") analogue, which is 2-3 orders of magnitude more potent than HN
[PMID:12787071 "we found that HN with D-Ser at position 14 exerts
neuroprotection more potently than HN by two to three orders of magnitude"].

## 3. Direct molecular activities (what HN itself does)

**Receptor ligand.** Two receptor systems, both with direct binding data.
- GPCRs FPR2/FPRL1 and FPR3/FPRL2: [PMID:15465011 "We have discovered that
  humanin (HN) acts as a ligand for formyl peptide receptor-like 1 (FPRL1) and 2
  (FPRL2)"], with direct membrane binding ("We demonstrated by binding
  experiments using [(125)I]-W peptide that HN and fHN directly interacted with
  hFPRL1 on the membrane") and EC50 3.5 nM for HN at FPRL1. Functional output:
  chemotaxis of mononuclear phagocytes [PMID:15153530 "Humanin induced
  chemotaxis of mononuclear phagocytes by using a human G protein-coupled
  formylpeptide receptor-like-1 (FPRL1) and its murine counterpart FPR2"].
  HN also competes with Abeta42 for the same receptor, which is the basis of the
  `receptor antagonist activity` annotation.
- A gp130-family cytokine receptor complex: [PMID:19386761 "Overexpression of
  ciliary neurotrophic factor receptor alpha (CNTFR) and/or the IL-27 receptor
  subunit, WSX-1, but not that of any other tested gp130-related receptor
  subunit, up-regulated HN binding to neuronal cells, whereas siRNA-mediated
  knockdown of endogenous CNTFR and/or WSX-1 reduced it"]. Downstream signalling
  is JAK/STAT3 [PMID:16005025 "we simultaneously provide evidence that
  neuroprotection by HN in F11 cells is mediated by the STAT3 transcription
  factor as well as by certain tyrosine kinases"], confirmed in RPE cells
  [PMID:26990160 "Humanin protected RPE cells from oxidative stress-induced cell
  death by STAT3 phosphorylation and inhibiting caspase-3 activation"].
  Note PMID:16005025 explicitly dissociates the two systems: FPR2 knockdown did
  not abolish HN rescue in F11 cells.

**BH3-domain / BCL-2-family binding.** The intracellular arm.
- BAX: [PMID:12732850 "Here we show that Bax interacts with humanin (HN), an
  anti-apoptotic peptide of 24 amino acids encoded in mammalian genomes. HN
  prevents the translocation of Bax from cytosol to mitochondria"].
- BID/tBID: [PMID:15661737 "Synthetic HN peptide binds purified Bid and tBid in
  vitro and blocks tBid-induced release of cytochrome c and SMAC from isolated
  mitochondria"].
- BimEL only: [PMID:15661735 "we demonstrated that HN binds directly to the
  extra long isoform of Bim (BimEL) but not the long (BimL) or short (BimS)
  isoforms"].
- Mechanism: co-fibrillation and sequestration [PMID:31690630 "Our findings
  reveal for the first time a potential mechanism by which BAX can be sequestered
  by fibril formation, which can prevent it from initiating MOMP and committing
  the cell to apoptosis"]; [PMID:33106313 "BID fibers are similar to those
  produced using BAX; however, the structures differ in final conformations of
  the BCL-2 proteins"]. Both are in-vitro recombinant studies.

**Amyloid-beta binding / anti-fibrillization.**
[PMID:28282805 "Thioflavin-T assay indicated that both HN and HNG delay the
formation and reduce the final amount of Abeta42 fibrils"];
[PMID:27349871 "we demonstrated that Humanin d-Ser14 exhibited potent inhibitory
activity against fibrillation of amyloid-beta and remarkably higher binding
affinity for amyloid-beta than that of the Humanin wild-type and S14G mutant"].

**IGFBP3 binding.** High-affinity, functionally consequential, but GO has no
term for it (no "insulin-like growth factor binding protein binding").
[PMID:14561895 "By using a yeast two-hybrid screen to identify
IGFBP-3-interacting proteins, we cloned humanin (HN) as an IGFBP-3-binding
partner"]; Kd 5.05 uM and competition with importin-beta1
[PMID:26216267 "humanin binds to IGFBP3 with a Kd of 5.05 uM and 2) both humanin
(IC50 of 18.1 uM) and HN 3-19 (IC50 of 10.3 uM) interfere with the binding of
importin-beta1 to IGFBP3 in vitro"]. Mapped to the IGFBP3 heparin-binding
domain, and competitive with hyaluronan for the same segment
[PMID:30184438 "Either HA or humanin could bind to this IGFBP-3 segment, but not
simultaneously"].

**Homodimerization.** Required for neuroprotection, Ser7-dependent
[PMID:12787071 "Multiple series of experiments indicated that Ser7 is necessary
for self-dimerization of HN, which is essential for neuroprotection by this
factor"].

**Low-value interactions.** TRIM11 (Y2H; destabilizes HN, so TRIM11's substrate
rather than HN's function) [PMID:12670303]; alpha-actinin-4 (bacterial two-hybrid
+ GFP-fusion colocalization) [PMID:15619032]; MPP8 (Y2H/co-IP, no functional
consequence shown) [PMID:23532874 "Further studies on functional consequences of
the interaction between the potential oncopetide and the oncoprotein may
elucidate some aspects of the molecular mechanisms of carcinogenesis"]; VSTM2L,
a secreted antagonist [PMID:21393573 "VSTM2L is the first example of a secreted
antagonist of HN"].

## 4. Localization

Secretion is well supported [PMID:11371646 "Transfected HN cDNA was transcribed
to the corresponding polypeptide and then was secreted into the cultured
medium."] and residues required for it were mapped [PMID:12860203 "Arg
substitution revealed that the two structures-Leu9-Leu11 and Pro19-Va120-were
essential for the secretion of full-length HN"]. HN circulates and declines with
age [PMID:19623253 "circulating levels of HN were decreased with age in humans
and mice"]. Cytoplasmic pool is needed for the BAX arm. Mitochondrial signal is
reported by EM-immunohistochemistry [PMID:15567815] and by uptake of labelled
peptide [PMID:26990160 "Exogenous HN was taken up by RPE and colocalized with
mitochondria."] — i.e. exogenous peptide entering mitochondria, not evidence of
matrix synthesis. Sperm midpiece/flagellum localization is replicated by two
groups [PMID:20542501; PMID:30920769 "Humanin was expressed in the midpiece of
the spermatozoa"].

## 5. Downstream phenotypes (the over-annotation zone)

A single HUVEC study generates five GOA rows (IL-1 production, IL-18 production,
inflammatory response, NLRP3 inflammasome assembly, response to oxidative
stress) [PMID:32923762 "Consequently, humanin inhibited the expression of IL-1beta
and IL-18."]. Others: astrocyte neuroinflammation [PMID:23277413], PGC1A-driven
mitochondrial biogenesis in MIN6 beta-cells [PMID:29432738], ER-stress
protection via mitochondrial GSH [PMID:27783653 "We further show that HN has a
protective effect against ER stress-induced apoptosis by restoring mitochondrial
GSH"], insulin sensitivity [PMID:19623253 "Continuous infusion of HN
intra-cerebro-ventricularly significantly improved overall insulin
sensitivity"]. These are consequences of receptor signalling in whichever cell
type was assayed; they are not separate activities of the peptide, and the
IL-1/IL-18-production and oxidative-stress rows in particular are two steps
downstream of anything HN touches.

Two rows are flatly unsupported:
- `GO:0006879 intracellular iron ion homeostasis` (NAS) rests only on humanin
  immunoreactivity being seen near iron deposits in villonodular synovitis
  [PMID:15567815 "Electron microscopy disclosed immunolocalisation of this
  peptide, predominantly around dense iron deposits withi"]. Proximity to iron
  is not iron homeostasis. REMOVE.
- `GO:0048471 perinuclear region of cytoplasm` rests on GFP-HN overexpression
  colocalizing with endogenous actinin in HEK293 [PMID:15619032 "Green
  fluorescent protein-fused humanin and endogenous actinin colocalized mainly in
  the perinuclear cytoplasm of HEK293 cells"].

## 6. Decisions taken

- Bare `GO:0005515 protein binding` (12 rows) handled per CLAUDE.md: MODIFY to an
  informative term where one exists (BH3 domain binding for BAX/BID/BimEL,
  cytokine receptor binding for CNTFR/WSX-1, amyloid-beta binding for Abeta42),
  REMOVE where the partner supports no informative MF and no function was
  demonstrated (ACTN4, MPP8, VSTM2L), and a new-term request for IGFBP3 binding.
- `GO:0048019 receptor antagonist activity` retained: the term definition
  ("interacts with a receptor to decrease the ability of the receptor agonist to
  bind and activate the receptor") does describe HN blocking Abeta42 access to
  FPR2, even though HN is itself an FPR2 agonist. The IBA at the same term is
  mechanical descent from the node carrying that claim and stands or falls with
  it.
- No NEW process terms proposed. The candidate ("negative regulation of
  intrinsic apoptotic signaling pathway") would be an ancestor/descendant
  neighbour of terms the gene already carries (GO:0043066, GO:1900118), which
  CLAUDE.md excludes as redundancy rather than coverage.
