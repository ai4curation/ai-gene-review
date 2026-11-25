# puc (puckered) notes

Gene: puckered (puc), FBgn0243512, CG7850. UniProt Q9VHV8 (unreviewed TrEMBL, 476 aa; the
entry FlyBase/GOA project the gene's annotations onto). PANTHER PTHR10159 (dual specificity
protein phosphatase), subfamily SF528.

## Sources and searches (2026-11-16)

- Cached GOA references: 27 PMIDs, nearly all abstract-only. Full text available for
  PMID:16542414, PMID:17483425, PMID:19540338, PMID:30062057, PMID:31409797.
- FlyBase hand-written description (`puc-deep-research-flybase.md`), fetched 2026-11-16.
- Searches run: WebSearch "Puckered Drosophila dual specificity phosphatase dephosphorylates JNK
  Basket threonine tyrosine in vitro"; "GST-Puc phosphatase JNK embryo extracts puckered 1998";
  Europe PMC `TITLE_ABS:(puckered) AND (p38 OR ERK OR substrate OR nuclear OR isoform)`;
  Europe PMC `puckered AND (JNK phosphatase)`. Bard et al. 2006 supplementary tables (lab website PDF)
  for the puc screen result. PMC full text of Martin-Blanco 1998 (PMC316530) is a scanned article
  with no machine-readable body, so only the abstract is quotable.
- Newly cached: PMID:34830088 (Karkali and Martin-Blanco 2021, full text), PMID:22266315
  (Karkali and Panayotou 2012, abstract).
- No Falcon/Perplexity deep research was available for this batch.

## Biochemistry

- Puc is a VH1-family dual-specificity phosphatase (DUSP/MKP), not a serine/threonine
  phosphatase of the PPP/PPM families [PMID:9472024 "The latter is mediated by a subset of
  phosphatases with dual specificity (VH-1 family). Here, we describe a new member of this family
  encoded by the puckered gene of Drosophila."]; [PMID:34830088 "puc is an immediate-early gene
  responding to JNK activity, that encodes a dual-specificity MAPK phosphatase that acts to
  down-regulate DJNK/Bsk activity through dephosphorylation"].
- Catalytic domain (PROSITE PS50054 dual-specificity phosphatase domain, residues 132-272) with the
  active-site motif HCHAGISRS at 215-223 and the phosphocysteine nucleophile Cys216
  (UniProt FT ACT_SITE 216, PROSITE ProRule). The N-terminal ~130 residues and the region 277-413
  are predicted disordered (MobiDB-lite). Sequence inspection only: a basic stretch
  (KMRIKREAPCLLL, ~51-63) resembles a kinase interaction motif, but no rhodanese domain is
  annotated and no experiment has mapped a docking site.
- Specificity: JNK-specific among fly MAPKs [PMID:16079158 "Puckered (Puc), the sole Drosophila Jun
  N-terminal kinase (JNK)-specific MKP"]; [PMID:22266315 "In Drosophila, Puckered has been identified
  as a DUSP, exhibiting specificity towards the c-Jun-N-terminal kinase (JNK)."]. Puc is also
  phosphorylated by JNK and p38 and binds both [PMID:22266315 "Finally, phosphorylation of Puckered
  enhanced its interaction both with JNK and p38."]. ERK signalling (kek-lacZ) is unaffected in puc
  clones in follicle cells (PMID:17483425 text).
- Martin-Blanco et al. 1998 full text (not quotable here; secondary summaries and the FlyBase IDA/IMP
  rows): a GST-Puc fusion had phosphatase activity, wild-type embryo extracts had JNK phosphatase
  activity that was absent from puc mutant extracts, and JNK but not ERK activity was elevated in puc
  mutants. The abstract states [PMID:9472024 "We show that puckered mutations result in the
  hyperactivation of DJNK, and that overexpression of puc mimics basket mutant phenotypes."].
- Feedback: puc is the prototype JNK/AP-1 target gene; its induction limits JNK output
  [PMID:9472024 "JNK signaling has a dual role: to activate an effector, encoded by decapentaplegic,
  and an element of negative feedback regulation encoded by puckered."].
- Turnover: Puc is degraded by the ubiquitin-proteasome system (PMID:22266315 abstract); the IntAct
  IPI with Roadkill/HIB (Q9VFP2-2) comes from the Cul3-HIB degron paper (PMID:19955409).

## Localization

- No experiment on endogenous Puc localization found. Reactome's manually curated fly event
  R-DME-209157 ("Phosphorylated BSK kinase is dephosphorylated and deactivated by PUC phosphatase")
  places the reaction in the cytosol (Reactome ContentService, queried 2026-11-16; not cached).
- The FlyBase IDA ER and Golgi rows cite Bard et al. 2006 (PMID:16452979, abstract-only here). In
  that paper's Supplementary Table S1, the puc dsRNA DRSC17034 scored z = -0.64 and -2.11 in the two
  HRP-secretion replicates; in Table S3 puc is a class D gene ("no obvious change" in Golgi
  organisation). Puc is not one of the TANGO genes whose products were tagged, and I could not find
  a Puc localization image. Puc has no signal peptide or TM segment. Left UNDECIDED.

## PANTHER/PAINT (PANTHER 19.0, PAINT 2026-08-28; IBD.gaf and treeinfo fetched 2026-11-16)

Path from the puc leaf to the root of PTHR10159:
PTN004128558 (root, horizontal transfer; IBD GO:0004721, GO:0007165) > PTN001605855 (duplication;
IBD GO:0005737, GO:0043409) > PTN002562845 (Eukaryota; IBD GO:0008330, GO:0017017, GO:0033550) >
... > PTN000806866 (Eumetazoa; IBD GO:0005829) > PTN008494682 (duplication) > PTN000741272
(Bilateria) > Protostomia > Arthropoda > ... > puc.

- PTN000741272 contains, among human/mouse/fly genes, only DUSP10 (Q9Y6W6), mouse Dusp10 and puc:
  puc is the fly DUSP10/MKP-5 ortholog. The ERK-type MKPs (DUSP6/7/9, fly Mkp3, worm lip-1) are in
  the sister clade under PTN000806866.
- In the vertebrate DUSP10 lineage, PAINT placed GO:0046329 negative regulation of JNK cascade at a
  Chordata duplication node (PTN001605539), so puc does not inherit it. In the ERK-MKP clade PAINT
  placed GO:0004722 protein serine/threonine phosphatase activity (PTN000806881); puc does not
  inherit that either.
- No IKR/IRD (loss) annotations found on the puc lineage for the terms under review.

Verdicts on the IBA rows that no other row covers:
- GO:0017017 MAP kinase Y/S/T phosphatase (PTN002562845, Eukaryota): ACCEPT; puc keeps the catalytic
  motif and is a demonstrated JNK phosphatase.
- GO:0008330 protein Y/T phosphatase (same node, seed DUSP10): ACCEPT; this is the dual specificity
  that rebuts the FlyBase "serine/threonine" wording.
- GO:0033550 MAP kinase tyrosine phosphatase (same node, seeds Mkp3, pmp1, SGD): KEEP_AS_NON_CORE;
  true of a DUSP but names only the tyrosine half of the reaction.
- GO:0043409 negative regulation of MAPK cascade (PTN001605855): ACCEPT; the fly-specific refinement
  (negative regulation of JNK cascade) is made by modifying the JNK cascade IMP row.
- GO:0005829 cytosol (PTN000806866, Eumetazoa): ACCEPT.

## Process annotations

Almost all process rows are phenotypes of puc loss or overexpression in JNK-dependent processes:
dorsal closure, epidermal differentiation, imaginal disc eversion and thorax closure, wound healing,
follicle cell/dorsal appendage morphogenesis, gut and genitalia chirality, apoptosis, oxidative
stress tolerance and lifespan, immunity, border cell migration (only with reduced PVR), G2/M in S2
cells. They are kept as non-core consequences of JNK restraint. Points of disagreement:

- GO:0007254 JNK cascade (IMP, PMID:9472024): sign correction to negative regulation of JNK cascade.
- GO:0050778 positive regulation of immune response (IMP, PMID:17681604): puc heterozygotes have
  enhanced pathogen resistance [PMID:17681604 "We found that puc heterozygous animals, as well as
  chico homozygous and heterozygous flies, have enhanced pathogen resistance."], so wild-type puc
  limits the response; sign corrected to negative regulation of immune response.
- GO:0008362 chitin-based embryonic cuticle biosynthetic process (PMID:16079158): the puc cuticle
  phenotype is the consequence of dorsal closure failure/apoptosis, not cuticle synthesis.
- GO:0009306 protein secretion (PMID:16452979): weak screen hit, class D.
- GO:0010628 positive regulation of gene expression (UniProt, PMID:20379222, abstract-only): the
  paper is about scarface as a JNK target; the direction expected for puc would be negative. UNDECIDED.

## FlyBase description verdict

"puckered (puc) encodes a serine/threonine protein phosphatase that mediates a feedback loop that
regulates the Jun-N-terminal kinase pathway." The feedback-loop clause is correct. The enzyme class is
wrong: Puc is a VH1-type dual-specificity (tyrosine/threonine) MAPK phosphatase. Recorded as a
WRONG_STATEMENT, CONFIRMED by PMID:9472024 and PMID:34830088. UniProt Q9VHV8 has no FUNCTION comment
(unreviewed), so there is no UniProt FUNCTION text to assess.
