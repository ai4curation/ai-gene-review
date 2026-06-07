# BCL2L13 (Bcl-rambo / Mil1) curation notes

UniProt: Q9BXK5 (B2L13_HUMAN). Synonyms: Bcl-rambo, Mil1, BCL2L13, ORFNames=CD003.
485 aa (canonical isoform 2 displayed, Q9BXK5-1). Single-pass tail-anchored membrane protein
(FT TRANSMEM 460..480). Contains BH4 (14..30), BH3 (100..116), BH1 (147..157), BH2 (193..206)
motifs, plus a unique ~250 aa insertion with two tandem repeats (A, B) preceding the C-terminal
transmembrane anchor.

## Core function synthesis

BCL2L13/Bcl-rambo is a mitochondrial outer-membrane (tail-anchored) BCL-2-family protein. The two
best-established, distinct activities reported in the literature are:

1. **Mitophagy receptor** — BCL2L13 is the mammalian functional homolog of yeast Atg32. It carries a
   WXXL-type LIR (LC3-interacting region) and binds LC3/GABARAP-family proteins to recruit the
   autophagy machinery to mitochondria, inducing mitochondrial fragmentation and mitophagy. The
   foundational study (Murakawa et al., Nat Commun 2015, PMID:26471991) is NOT among the GOA-cited
   references and is NOT cached in this repo, so it cannot be used for verbatim supporting_text;
   however, the UniProt IntAct interaction table directly records BCL2L13 binding to the human Atg8
   ortholog GABARAPL2 (P60520), consistent with the LIR-dependent receptor model.
   [file:human/BCL2L13/BCL2L13-uniprot.txt "Q9BXK5; P60520: GABARAPL2; NbExp=4; IntAct=EBI-747430, EBI-720116;"]
   UniProt/Ensembl GOA also carries GO:0000423 mitophagy (IEA:Ensembl) and GO:0007005 mitochondrion
   organization (IEA:Ensembl), reflecting this role, though these specific terms are not in the
   seeded existing_annotations set.
   [file:human/BCL2L13/BCL2L13-uniprot.txt "GO:0000423; P:mitophagy; IEA:Ensembl."]

2. **Apoptosis (original characterization)** — Bcl-rambo was first described as a pro-apoptotic
   BCL-2 homolog whose cell-death activity is induced by its membrane-anchored C-terminal domain
   (the unique insertion + TM), NOT by its BH motifs, and is blocked by caspase inhibitors/IAPs but
   not by Bcl-xL. Notably it does NOT heterodimerize with other BCL-2-family members.
   [PMID:11262395 "Bcl-rambo was localized to mitochondria, and its overexpression induces apoptosis that is specifically blocked by the caspase inhibitors, IAPs, whereas inhibitors controlling upstream events of either the 'death receptor' (FLIP, FADD-DN) or the 'mitochondrial' pro-apoptotic pathway (Bcl-x(L)) had no effect."]
   [PMID:11262395 "No interaction of Bcl-rambo with either anti-apoptotic (Bcl-2, Bcl-x(L), Bcl-w, A1, MCL-1, E1B-19K, and BHRF1) or pro-apoptotic (Bax, Bak, Bik, Bid, Bim, and Bad) members of the Bcl-2 family was observed."]
   [PMID:11262395 "Bcl-rambo constitutes a novel type of pro-apoptotic Bcl-2 member that triggers cell death independently of its BH motifs."]

The apoptosis function is the basis of the GOA NAS annotations (PMID:11262395): apoptotic process
(GO:0006915), mitochondrion (GO:0005739), cysteine-type endopeptidase activator activity involved
in apoptotic process (GO:0008656, i.e. caspase-3 activation), and membrane (GO:0016020, IDA).
UniProt FUNCTION: "May promote the activation of caspase-3 and apoptosis."
[file:human/BCL2L13/BCL2L13-uniprot.txt "FUNCTION: May promote the activation of caspase-3 and apoptosis."]

The original overexpression-driven apoptosis phenotype is the historical view; the more recent and
mechanistically distinct mitophagy-receptor role (Atg32 homolog) is now regarded as a central,
conserved function. Distinguishing CORE (mitophagy receptor / mitochondrial fragmentation) from the
context-dependent apoptosis annotations is the main curation task.

## Legionella SidF (apoptosis inhibition by pathogen)

Legionella pneumophila effector SidF specifically interacts with and neutralizes BNIP3 and Bcl-rambo
to inhibit host macrophage apoptosis, confirming Bcl-rambo as a genuine pro-death host protein and a
pathogen target. UniProt IntAct records Q9BXK5-sidF (Q5ZSD5, Xeno).
[PMID:17360363 "SidF contributes to apoptosis resistance in L. pneumophila-infected cells by specifically interacting with and neutralizing the effects of BNIP3 and Bcl-rambo, two proapoptotic members of Bcl2 protein family."]
[PMID:17360363 "binding of SidF to Bcl-rambo can be detected under various conditions, including in cells in which SidF is delivered directly from the bacterium"]
The seeded GO:0005515 protein binding IPI from PMID:17360363 corresponds to this SidF interaction;
as bare protein binding it is uninformative and is marked over-annotated.

## Localization

UniProt: Isoform 2 (canonical, Q9BXK5-1): Mitochondrion membrane; Single-pass membrane protein;
Nucleus. Isoform 1 (Q9BXK5-2, a short 201-aa form): Nucleus.
[file:human/BCL2L13/BCL2L13-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Mitochondrion membrane"]
Mitochondrial (outer) membrane is the core functional location. The Nucleus localization is reported
(largely for the truncated isoform 1, which lacks the TM anchor) and is secondary; isoform 1
(Q9BXK5-2) ends at residue 201 (VSP_000526/VSP_000527) and is nuclear.

## Protein binding annotations

Many GO:0005515 protein binding IPI annotations derive from high-throughput interactome papers
(16189514, 25416956, 25910212, 26871637, 28514442, 32296183, 32814053, 33961781) plus the specific
SidF study (17360363). The UniProt IntAct table is dominated by membrane-protein partners (many
single-pass TM proteins, e.g. PLN, MAL, PLP1, VAMP3/4, syntaxins), consistent with a
membrane-embedded tail-anchored protein; most are not functionally informative. "protein binding"
is uninformative and marked over-annotated. The functionally meaningful interaction is with the
Atg8-family protein GABARAPL2 (mitophagy receptor activity), but that is recorded as an IntAct hit,
not among the seeded protein-binding annotations with a cached PMID.

## Key existing annotation classification summary

CORE (mitophagy receptor / mitochondrial fragmentation): mitochondrion (GO:0005739) localization,
membrane (better as mitochondrial outer membrane). NOTE: the defining mitophagy MF/BP terms are not
in the seeded set (they exist in UniProt GOA as IEA: GO:0000423 mitophagy, GO:0007005 mitochondrion
organization) — proposed as new/expanded annotation.

SECONDARY / NON-CORE: apoptotic process, regulation of apoptotic process, caspase-3 activator
activity (GO:0008656), nucleus localization.

OVER-ANNOTATED / UNINFORMATIVE: protein binding (GO:0005515) — all instances.

## Caveat

The strongest evidence for the mitophagy-receptor / Atg32-homolog function (Murakawa et al. 2015)
is not in the cached publications, so verbatim supporting_text for that function is drawn only from
the UniProt record (GABARAPL2 IntAct interaction; GO:0000423 mitophagy IEA) and is reflected in the
description, core_functions, and proposed_new_terms rather than asserted from an inaccessible PMID.

## Falcon deep research findings (2026-06-07)

PMID correction: the foundational Murakawa et al. Nat Commun 2015 mitophagy/Atg32 paper is
**PMID:26146385** (DOI 10.1038/ncomms8527), not PMID:26471991 as guessed earlier in these notes.
Verified via PubMed ID conversion (DOI->PMID) and metadata lookup. None of the new papers below are
cached in publications/, so they are added to the review as statement-only findings (no
verbatim supporting_text).

- CONFIRMS (now with a citable primary PMID): BCL2L13 is the mammalian Atg32 homolog; it binds LC3
  via a WXXI/LIR motif and induces both mitochondrial fragmentation and mitophagy. BH domains drive
  fragmentation; the WXXI/LIR motif drives mitophagy. Fragmentation occurs without DRP1/DNM1L, and
  mitophagy proceeds in Parkin-deficient cells (ubiquitin-independent, Parkin-independent).
  [PMID:26146385 "Bcl2-L-13 binds to LC3 through the WXXI motif and induces mitochondrial fragmentation
  and mitophagy in HEK293 cells... BH domains are important for the fragmentation, while the WXXI motif
  facilitates mitophagy... induces mitochondrial fragmentation in the absence of Drp1, while it induces
  mitophagy in Parkin-deficient cells"] (Murakawa 2015, Nat Commun). This grounds the existing
  description/core_functions that were previously inferred only from UniProt.

- NEW (mechanism): Phosphorylation regulates the receptor. A Ser site adjacent to the LIR
  (Ser272, mouse numbering; human LIR is WQQI at ~276-279) tunes LC3 binding and mitophagic activity;
  PGAM5 acts as a negative regulator by dephosphorylating BCL2L13, and BCL2L13 has been reported to
  recruit the ULK1 complex to the mitochondrial outer membrane to initiate autophagosome formation.
  Additional reported interactors/modulators include ULK1, PGAM5, ANT (SLC25A4), VDAC, and CERS2/CERS6.
  Source: Kataoka 2022 review [PMID:36589739] (review-level; mechanistic detail, treat as provisional
  where based only on review synthesis).

- NEW (localization/process): Beyond the mitochondrial outer membrane, BCL2L13 also localizes at
  ER-mitochondria contact sites / mitochondria-associated membranes (MAMs) and regulates
  ER-mitochondria Ca2+ homeostasis in skeletal muscle. Knockdown alters cytosolic Ca2+ release and
  mitochondrial Ca2+ uptake without changing the NUMBER of ER-mito contacts (a functional, not
  structural, contact-site effect); Bcl2l13-KO zebrafish show impaired muscle structure/function and
  decreased mitochondrial complex activity. [PMID:39175772 "BCL2L13 at mitochondria, ER, and
  mitochondria-associated membranes... knockdown of BCL2L13 in C2C12 cells changes cytosolic Ca release
  and mitochondrial Ca uptake"] (Grepper 2024, iScience). This is a genuinely new functional context
  (Ca2+ homeostasis at MAMs) not in the existing review.

- NEW (disease / context-dependent fission wiring): In glioblastoma, BCL2L13 is upregulated and
  promotes mitochondrial fission and high mitophagy flux by targeting DNM1L at Ser616, supporting tumor
  proliferation/invasion. This is notable because it is DNM1L(DRP1)-DEPENDENT, in apparent contrast to
  the DRP1-independent fragmentation seen by Murakawa 2015 - i.e., context-dependent fission wiring.
  [PMID:37660127 "BCL2L13 targeted DNM1L at the Ser616 site, leading to mitochondrial fission and high
  mitophagy flux"] (Wang 2023, Cell Death Dis). Do NOT use this to override the DRP1-independent core
  claim; both are valid in their respective contexts.

- NEW (interactor/pathway, disease): In diabetic kidney disease, BCL2L13 was identified by LC-MS/MS as
  an interacting partner of the inner-membrane protease YME1L; YME1L promotes BCL2L13 phosphorylation,
  strengthening BCL2L13-LC3 binding and mitophagy to restrain renal tubular senescence.
  [PMID:38494498 "BCL2L13... as an interacting partner of YME1L. Furthermore, YME1L was found to
  promote the phosphorylation of BCL2L13"] (Luo 2024, Biol Res). New YME1L interactor.

- NEW (disease, prognosis): In clear-cell and papillary renal cell carcinoma, BCL2L13 is downregulated
  and lower expression correlates with poorer prognosis (independent of grade); BCL2L13 is positively
  correlated with and acts through SLC25A4/ANT in its pro-apoptotic pathway. [PMID:34193180
  "Down-regulation of BCL2L13 renders poor prognosis in ccRCC and pRCC... actively correlates with
  SLC25A4"] (Meng 2021, Cancer Cell Int). Contrasts with the pro-survival/oncogenic role in GBM,
  reinforcing strong context/tissue dependence.

- PROVISIONAL / not used to change annotations: a 2024 study reports miR-449b-5p directly targets the
  BCL2L13 3'UTR in hypoxic AC16 cardiomyocytes, with BCL2L13 suppression being protective via PI3K/AKT
  (Jiang 2024, Appl Biochem Biotechnol, DOI 10.1007/s12010-024-04931-5; 0 citations at report time).
  Low-confidence/peripheral to GO core function; kept in notes only, no PMID added to the review.

Curation impact: existing annotation actions are unchanged. The new primary references (Murakawa 2015,
Kataoka 2022, Grepper 2024, Wang 2023, Luo 2024, Meng 2021) are added to references: as statement-only
findings. Murakawa 2015 now provides a citable primary basis for the mitophagy-receptor core function.
Grepper 2024 (ER-mito contact / Ca2+) and the YME1L/SLC25A4 interactors are the main genuinely-new
biology; added suggested questions/experiments accordingly.
