# MYD88 (human, Q99836) review notes

## Status of inputs

- UniProt, GOA (236 rows, 229 seeded annotations after de-duplication) and all 63 GOA PMIDs were
  cached before review. Two extra PMIDs were fetched to trace mouse-sourced IEA rows
  (PMID:18319258, PMID:31164412).
- Falcon deep research had not been produced when the review was drafted (MYD88 was queued behind
  the TLR batch); see the end of this file for its status.

## Biology summary (with provenance)

- MYD88 is a cytosolic TIR-domain adaptor with an N-terminal death domain (DD), an intermediate
  domain and a C-terminal TIR domain. It couples IL-1 receptor family and TLR receptors to the IRAK
  kinases. [PMID:9430229 "MyD88 binds to both IRAK (IL-1 receptor-associated kinase) and the
  heterocomplex (the signaling complex) of the two receptor chains and thereby mediates the
  association of IRAK with the receptor."] [PMID:9430229 "it couples a serine/threonine protein
  kinase to the receptor complex."]
- General adaptor for the Toll/IL-1R family. [PMID:9734363 "our findings implicate MyD88 as a
  general adaptor/regulator molecule for the Toll/IL-1R family of receptors for innate immunity."]
- Recruitment to TLR4 (and TLR2) needs the bridging adaptor TIRAP, which is targeted to PIP2 at the
  plasma membrane. [PMID:16751103 "TIRAP then functions to facilitate MyD88 delivery to activated
  TLR4 to initiate signal transduction."] [PMID:17258210 "We show that the TLR adaptor Mal is
  critical for linking Myeloid Differentiation primary response protein 88 (MyD88) to TLR2 and
  TLR4."]
- DD-mediated oligomerisation builds the Myddosome with IRAK4 and IRAK1/2. [PMID:36865541 "Next, the
  MyD88 DDs interact with IRAK4's DDs, in a stoichiometry of 6 to 8 molecules of MyD88 to 4
  molecules of IRAK4."] [PMID:36865541 "The myddosome is a supramolecular signaling complex
  assembled upon dimerization of IL-1Rs and most TLRs (except TLR3), and is composed of MyD88,
  IRAK4, IRAK1 and/or IRAK2, in addition to TRAF6."] Endogenous MyD88 forms barrel-like scaffolds
  [PMID:38961291 "within most myddosomes, MyD88 forms barrel-like structures that function as
  scaffolds for effector protein recruitment."]
- IRAK4 variants in the DD lose MyD88 binding [PMID:24316379 "the variant of IRAK4, R12C, as well as
  R20W, located in the death domain of IRAK4 and regarded as a SNP, caused a loss of interaction
  with MyD88."]
- Endosomal TLR7/8/9: MyD88–IRF7 complex drives IFN-alpha [PMID:15361868 "The death domain of MyD88
  interacted with an inhibitory domain of IRF7, and this interaction resulted in activation of the
  IFN-alpha-dependent promoters."]; TLR9 phosphorylation is needed for MyD88 recruitment
  [PMID:40980882 "Phosphorylated TLR9 is critical for interaction with its adaptor protein, MyD88,
  and activating downstream signaling."]; TLR8 in human macrophages [PMID:33718825 "Thus the
  TLR8/MYD88 pathway is required for viral GU-rich RNA-induced IL-1β, TNF, and IL-6 expression
  from human macrophages"].
- IL-1 family receptors: IL-1R, IL-18R, IL-33R all use MyD88 [PMID:36865541 "Responses to these
  cytokines are mediated by the IL-1 receptor (IL-1R) and the closely related IL-18R and IL-33R, all
  of which employs MyD88 as signaling adaptor, similarly to TLRs"]; IL-33-driven human/mouse T cell
  polarisation needs MyD88 [PMID:18802081 "This polarization requires IL-1R-related molecule and
  MyD88 but not IL-4 or STAT6."].
- Non-TIR receptor: TACI binds MyD88 [PMID:20676093 "the cytoplasmic domain of TACI encompasses a
  conserved motif that bound MyD88"].
- Regulation by ubiquitin: OTUD5 [PMID:38605168 "This polyubiquitin cleavage enhances MyD88
  oligomerization after LPS stimulation"]; USP3 [PMID:37971847 "The cytoplasmic USP3 specifically
  removes the K63-linked polyubiquitin chains on MyD88"].
- Human genetics: MyD88 deficiency phenocopies IRAK-4 deficiency [PMID:21057262 "The clinical
  features of IRAK-4 and MyD88 deficiency were indistinguishable."].

## Curation decisions and problems found

1. **GO:0008063 Toll signaling pathway (IBA and rat-sourced IEA).** GO:0008063 is defined for
   ligand binding to "the receptor Toll" and is NOT an ancestor of GO:0002224 toll-like receptor
   signaling pathway (checked in OLS). The IBA node PTN000386853 spans fly Myd88 and vertebrate
   MYD88; the ancestral adaptor role is sound, but for a vertebrate the pathway is the TLR/IL-1R
   pathway. MODIFY to GO:0002755. This is the project's Toll-vs-TLR conflation issue on an adaptor.
2. **GO:0005121 Toll binding (rat IEA)** — same issue; MODIFY to GO:0035325 Toll-like receptor
   binding.
3. **ATP-dependent histone chaperone activity / chromatin organization / chromatin remodeling (IEA)**
   — traced to mouse Myd88 IMP from PMID:18319258, which shows only that MyD88 signaling is required
   for nucleosome remodeling at secondary-response promoters ("MyD88 is required for nucleosome
   remodeling and histone H3K4 trimethylation at secondary response promoters"). This is an indirect
   downstream effect; MYD88 has no histone chaperone activity. REMOVE all three. (Source defect is
   on the mouse Myd88 MGI annotation; no mouse review exists in this repo.)
4. **GO:0005123 death receptor binding (TAS PMID:9374458)** — MYD88 binds IL-1R, not TNFR-family
   death receptors. MODIFY to GO:0005149 interleukin-1 receptor binding.
5. **Phagocytosis (IMP PMID:30883606)** — the paper states "MyD88 silencing did not significantly
   reduce phagocytosis of either E. coli or S. aureus" in human macrophages; only mouse Myd88-/-
   iBMDMs showed reduced E. coli uptake. MARK_AS_OVER_ANNOTATED.
6. **Cellular response to mechanical stimulus (IEP PMID:19593445)** — the cited full text (BAD in
   prostate cancer) contains no mention of MyD88 or mechanical stimulation. Likely a wrong PMID;
   UNDECIDED rather than REMOVE, flagged in reference_review.
7. **Cell surface (IDA PMID:22851693)** — MYD88 is a cytoplasmic adaptor; the paper studies
   membrane-associated IL-1R complex I. MODIFY to GO:0031234.
8. **protein binding IPI rows** — MODIFY to TIR domain binding (TIRAP, SARM1, TLR partners in MAPPIT),
   Toll-like receptor binding (TLR2/TLR4 co-IP), death domain binding (FADD, IRAK4 DD–DD), protein
   kinase binding (IRAK1/IRAK4), TNFR superfamily binding (TACI); REMOVE for high-throughput screens
   with incidental partners, pathogen proteins and regulators (SPOP, STAP2, HDAC6, DOCK8, DHX9/36,
   TcpB, HCV NS5A).
9. **Type I interferon-mediated signaling pathway (IMP PMID:23633945)** — the miR-21 paper measures
   IFN effector genes downstream of HCV-induced type I IFN production; MYD88 acts in the TLR arm
   that produces IFN, not in IFNAR signaling. MARK_AS_OVER_ANNOTATED (keep the sibling
   GO:0032481 positive regulation of type I interferon production as non-core).
10. NLRP3 inflammasome complex assembly (NAS, IRAK review) — MYD88 does not assemble NLRP3; it
    primes/licenses via TLR signaling. MODIFY to GO:1900227 positive regulation of NLRP3
    inflammasome complex assembly (which is also separately supported by IMP PMID:33718825).

## NEW annotations considered

- GO:0035655 interleukin-18-mediated signaling pathway: UniProt states involvement; supported in
  review PMID:36865541 (IL-18R uses MyD88). MYD88 performs the adaptor step in IL-18R signaling
  (participation test passes: it is the adaptor that bridges IL-18R1 TIR to IRAK4). Comparator:
  IRAK4/IRAK1 human are annotated in IL-18 pathway in GOA? Not verified here, so this was NOT added
  as NEW; raised as a suggested question instead.
