# SPTSSA (ssSPTa) review notes

UniProtKB:Q969W0 — Serine palmitoyltransferase small subunit A (ssSPTa). 71 aa, two
predicted transmembrane helices, ER membrane. HGNC:20361. Formerly C14orf147 / SSSPTA.

## Core biology (verified)

SPTSSA is a small **regulatory/accessory subunit** of the serine palmitoyltransferase
(SPT) complex. The catalytic core is the SPTLC1 + SPTLC2 (or SPTLC3) heterodimer;
SPTSSA (or its paralog SPTSSB) is a small subunit that is **required for full SPT
activity** and **determines the acyl-CoA chain-length specificity** of the complex.
SPTSSA is itself non-catalytic — it "stimulates the catalytic activity and plays a role
in substrate specificity" (UniProt FUNCTION, based on PubMed:19416851, PubMed:33558761).

- Discovery paper PMID:19416851 (Han et al. 2009, PNAS): identified ssSPTa and ssSPTb,
  each of which "substantially enhance the activity of mammalian SPT" and "confer full
  enzyme activity"; the two isoforms differ in acyl-CoA preference. SPTLC1-SPTLC2-SPTSSA
  strongly prefers C16-CoA (palmitoyl-CoA) [UniProt FUNCTION synthesis of this paper].
  Cached publication is ABSTRACT-ONLY (`full_text_available: false`); the abstract
  supports the enhancement/substrate-specificity claims. Many GOA IDA annotations
  (UOS_MCB, UniProtKB, ComplexPortal) cite this paper — curators read the full text.

- Structural papers PMID:33558761 (Wang et al.), PMID:33558762 (Li et al.),
  PMID:37308477 (Xie et al.): cryo-EM of the human SPT holocomplex.
  "ssSPTa engages SPTLC2 and shapes the tunnel to determine substrate specificity"
  (33558761 abstract). "SPTssa participates in acyl-CoA coordination, thereby stimulating
  the SPT activity and regulating the substrate selectivity" (33558762 abstract).
  Complex composed of SPTLC1, SPTLC2 (or SPTLC3) and SPTssa (or SPTssb), plus ORMDL
  regulatory subunit (37308477 full text). SITE 28 in UniProt "defines the length of the
  acyl chain-binding pocket, determining the acyl-CoA substrate preference"; MUTAGEN M28K
  strongly decreases SPT catalytic activity (PubMed:33558762).

## Localization

ER membrane, multi-pass membrane protein (UniProt SUBCELLULAR LOCATION,
ECO:0000269|PubMed:23510452). Topology: cytoplasmic 1-12, TM 13-29, lumenal 30-34, TM
35-57, cytoplasmic 58-71. So the N- and C-termini face the cytoplasm; GOA carries
"cytoplasmic side of endoplasmic reticulum membrane" (GO:0098554, is_active_in). Also
ER (GO:0005783) and ER membrane (GO:0005789) from multiple sources.

## Second, independent function (MBOAT7/LPIAT1)

PMID:23510452 (Hirata et al. 2013): ssSPTa was found as an MBOAT7 (LPIAT1)-interacting
protein by split-ubiquitin Y2H; co-IP and colocalization confirmed. Knockdown of ssSPTa
decreased LPIAT1-dependent incorporation of arachidonic acid into PI and reduced LPIAT1
protein in the crude mitochondrial fraction, suggesting ssSPTa facilitates MBOAT7
localization to mitochondria-associated membranes (MAM). This is the basis for the
"intracellular protein localization" (GO:0008104) IDA and the MBOAT7/Q96N66 protein
binding IPI. This is a genuine, SPT-independent activity for the SAME gene.

## Disease

SPTSSA variants cause complex hereditary spastic paraplegia (SPG90A dominant, SPG90B
recessive), a juvenile-ALS-like / HSP-spectrum neurodegenerative disorder, via
dysregulation of SPT (impaired ORMDL3 down-regulation → increased sphingolipid
synthesis). PMID:36718090 (Srivastava et al. 2023, Brain) — NOT in publications cache;
supported by UniProt DISEASE + VARIANT/MUTAGEN annotations. Not directly a GO annotation
but informs the biological description.

## GOA annotation assessment summary

- serine C-palmitoyltransferase activity GO:0004758: correct at complex level. SPTSSA is
  a non-catalytic activator, so `contributes_to` is the accurate qualifier. IBA
  (contributes_to) ACCEPT. IDA `enables` (UniProt) and IDA `contributes_to` (UOS_MCB,
  x2) — accessory subunit does not independently enable catalysis, but curators read the
  full text; ACCEPT the contributes_to forms; the bare `enables` (UniProt IDA, MGI IDA)
  is defensible as complex-level activity, ACCEPT (do not remove experimental).
- serine palmitoyltransferase complex GO:0017059 (part_of): well supported by structures
  and ComplexPortal (CPX-6663, CPX-6665). ACCEPT all.
- ER membrane GO:0005789 (located_in): ACCEPT (EXP PMID:23510452 is the anchor; IEA,
  NAS, TAS all consistent). ER GO:0005783 IDA ACCEPT. cytoplasmic side of ER membrane
  GO:0098554 is_active_in IDA: ACCEPT (consistent with topology).
- BP: sphingolipid biosynthetic process GO:0030148 (TAS) — core, ACCEPT. ceramide
  biosynthetic process GO:0046513, sphingosine biosynthetic process GO:0046512,
  glycosphingolipid biosynthetic process GO:0006688, sphingomyelin biosynthetic process
  GO:0006686, sphingolipid metabolic process GO:0006665 — all downstream of SPT; the
  gene contributes to the whole sphingolipid biosynthetic network. Keep GO:0030148 as
  core; the more specific downstream branches are best treated as non-core / over-
  annotated because SPTSSA acts only at the first committed step and the downstream
  products (SM, GlcCer, sphingosine) require many other enzymes.
  - GO:0006686 sphingomyelin biosynthetic process cites PMID:30242129 (SMS1-GCS
    complex); SPTSSA is NOT mentioned anywhere in that full-text paper -> over-annotated
    (MARK_AS_OVER_ANNOTATED; experimental, so not REMOVE).
- protein binding GO:0005515 (IPI): SPTLC1 (O15269), MBOAT7 (Q96N66), and several HuRI
  hits (CYSRT1, GET1, HERPUD2, RHBDL1). SPTLC1 and MBOAT7 are biologically meaningful;
  bare `protein binding` is uninformative -> MARK_AS_OVER_ANNOTATED (per policy, not
  REMOVE), captured better by complex membership / MBOAT7 localization role.
- intracellular protein localization GO:0008104 (IDA, PMID:23510452): the MBOAT7-MAM
  localization role; KEEP_AS_NON_CORE (secondary, SPT-independent function).
