# LATS1 (human, O95835) review notes

Automated deep research was unavailable: no provider keys. These notes were compiled
by hand from the UniProt record, the cached publications in `publications/`, the
GO-CAM index and the PANTHER PAINT file. No `*-deep-research-*.md` file was created.

## Core biology

- Hippo pathway effector kinase. LATS1 binds and phosphorylates YAP and keeps it in the cytoplasm
  [PMID:18158288 "LATS1 inactivates YAP oncogenic function by suppressing its transcription regulation of cellular genes via sequestration of YAP in the cytoplasm after phosphorylation of YAP."];
  the S127 site creates a 14-3-3 binding site
  [PMID:22863277 "Lats1/2 inhibit YAP by direct phosphorylation at S127, which results in YAP binding to 14-3-3 and cytoplasmic sequestration"].
- Activation: WWC proteins bring LATS1/2 together with SAV1, which recruits MST1/2
  [PMID:35429439 "WWC proteins (WWC1/2/3) directly interact with LATS1/2 and SAV1, and SAV1, in turn, brings in MST1/2 to phosphorylate and activate LATS1/2."].
  MOB1A and MOB1B are the LATS-binding coactivators
  [PMID:19739119 "only hMOB1A and hMOB1B interact with both LATS1 and LATS2 in vitro and in vivo."].
- Nuclear pool. CRL4-DCAF1 ubiquitylates and inhibits nuclear Lats1/2
  [PMID:25026211 "Here, we provide evidence that de-repressed CRL4DCAF1 targets Lats1 and 2 for ubiquitylation and inhibition in the nucleus and thus activates YAP-driven transcription and oncogenesis."].

## Mitosis and cytokinesis (LATS1-specific literature)

- Localization: centrosome in interphase, then spindle poles, spindle and midbody in mitosis
  [PMID:10518011 "The h-warts protein has a serine/threonine kinase domain and is localized to centrosomes in interphase cells. However, it becomes localized to the mitotic apparatus, including spindle pole bodies, mitotic spindle, and midbody, in a highly dynamic manner during mitosis."].
- CDK1 regulation
  [PMID:9988268 "In mammalian cells, LATS1 is phosphorylated in a cell-cycle-dependent manner and complexes with CDC2 in early mitosis."].
- Ploidy and the tetraploidy checkpoint
  [PMID:15122335 "WARTS thus plays a critical role in maintenance of ploidy through its actions in both mitotic progression and the G(1) tetraploidy checkpoint."].
- Cytokinesis via LIMK1
  [PMID:15220930 "Our findings indicate that LATS1 is a novel cytoskeleton regulator that affects cytokinesis by regulating actin polymerization through negative modulation of LIMK1."].

## Other functions

- ERalpha degradation in breast epithelium, independent of kinase activity
  [PMID:28068668 "In the presence of LATS, ERα was targeted for ubiquitination and Ddb1-cullin4-associated-factor 1 (DCAF1)-dependent proteasomal degradation.";
  PMID:28068668 "suggesting that the kinase activity of LATS1 is dispensable for ERα regulation"].
- NLRP3 inflammasome
  [PMID:39173637 "where LATS1/2, pre-recruited to MTOC during priming, phosphorylates NLRP3 to further facilitate its interaction with NIMA-related kinase 7 (NEK7)"].
- Wnt crosstalk via TAZ-DVL
  [PMID:20412773 "the Hippo pathway restricts Wnt/beta-Catenin signaling by promoting an interaction between TAZ and DVL in the cytoplasm."].

## GO-CAM

`gocams/index.tsv` lists LATS1 in 7 human models. In six Hippo models (core components; the
WWC2 and WWC3 variants; MAP4K4; STRIPAK/STRN4; TAZ cytoplasmic retention) it is
`protein serine/threonine kinase activity`, part of `hippo signaling`, in the `cytoplasm`. In
model 66e382fb00002738 (ZDHHC1-NLRP3) it is the kinase acting on NLRP3, part of
`positive regulation of NLRP3 inflammasome complex assembly`. This matches core function 1.

## PAINT / IBA

PTHR24356 node PTN002390470 carries four IBDs that reach human LATS1:
- hippo signaling: seeds fly wts, mouse Lats1/2, human LATS1/2. ACCEPT; LATS1 is itself a
  seed, which is expected and not circular.
- regulation of organ growth: seed mouse Lats2. KEEP_AS_NON_CORE for human.
- positive regulation of apoptotic process: seed fly wts only. KEEP_AS_NON_CORE, indirect.
- G1/S transition: seeds LATS2 only. MARK_AS_OVER_ANNOTATED for LATS1, a LATS2-specific
  claim. Human LATS1 data concern the tetraploidy checkpoint.
The propagation audit (projects/ORIGINS_OF_MULTICELLULARITY/propagation-audit.md) found
these organ-growth, apoptosis and G1/S IBDs over-reach into choanoflagellate Warts. That is a
node-placement issue and does not decide the human rows.

## Ancestral versus animal-specific

- Ancestral (premetazoan): Warts-dependent cytoplasmic retention of Yorkie. In Capsaspora,
  [PMID:38517944 "Loss of either kinase results in increased nuclear localization of coYki, showing that the regulatory activity of the Hippo kinase cascade is conserved."].
  The kinase biochemistry is also conserved: a Fonticula Warts can replace LATS1/2 in mammalian cells
  [PMID:38729842 "the nuclear localization of YAP/TAZ in MST1/2- or LATS1/2-deficient mammalian cells can be rescued by the Acanthamoeba Hippo ortholog or the Fonticula Warts ortholog, respectively"].
- Ancestral output looks cytoskeletal rather than proliferative
  [PMID:38517944 "Loss of coHpo or coWts does not increase cell proliferation, consistent with our previous conclusion that the Hippo pathway does not significantly affect proliferation in Capsaspora.";
  PMID:38729842 "these results suggest that the ancestral function of the Hippo pathway in unicellular organisms may have involved regulation of the cytoskeleton and not cell proliferation."].
  The human LATS1-LIMK1 cytokinesis axis is a cytoskeletal function, but no paper shows it
  directly descends from the premetazoan role. That remains a question.
- In S. rosetta, warts knockout enlarges rosettes but slows proliferation
  [DOI:10.1101/2024.07.13.603360 "warts pac1 cells grew into giant rosettes containing about twice as many cells as wild-type ones";
  DOI:10.1101/2024.07.13.603360 "On the other hand, hippopac1 and warts pac1 KO clones proliferated markedly slower"].
  This is a preprint.
- Animal-specific: proliferation and organ-size control
  [PMID:38729842 "functional support for proliferation and tissue size control through inhibition of Yorkie by the Hippo kinase module is currently restricted to bilaterians."].
  The ERalpha, mammary-differentiation and NLRP3-inflammasome roles also involve
  vertebrate-specific partners. Their age has not been tested.

## Decisions worth flagging

- 35 `protein binding` rows. 26 were REMOVEd as uninformative. 9 were MODIFYed: kinase partners
  (CDK1, CDK2, LIMK1, STK11, STK3, NUAK1) to protein kinase binding, SIAH2 to ubiquitin protein
  ligase binding, and ESR1 to nuclear receptor binding.
- GO:0030331 obsolete nuclear estrogen receptor binding: MODIFY to GO:0016922.
- The ISS nucleus row cites YAP1 (P46937) as WITH/FROM, which is an odd source. Kept as
  non-core because of the separate CRL4-DCAF1 nuclear-pool evidence.
- UNDECIDED: TGF-beta regulation (mouse ISS/IEA), and the synaptic terms from rat via Ensembl.
  The source papers are not cached.
- MARK_AS_OVER_ANNOTATED: hormone-mediated signaling, which comes from systemic phenotypes of
  Lats1 knockout mice.
