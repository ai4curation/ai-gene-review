# CALR (Calreticulin, P27797) curation notes

## Overview
CALR is the soluble ER-luminal paralog of calnexin, one of the two central ER lectin
chaperones of the calnexin/calreticulin (CNX/CRT) cycle. It binds monoglucosylated
N-glycans (Glc1Man9GlcNAc2) on nascent glycoproteins, recruits ERp57 (PDIA3) for
oxidative folding, retains/triages misfolded glycoproteins for ER quality control,
and is a major high-capacity Ca2+-binding protein that regulates ER calcium storage.
It is a key chaperone in MHC class I peptide loading. Beyond the ER, CALR has
well-documented secondary roles: a cell-surface/extracellular "eat-me" signal driving
immunogenic cell death and phagocytosis, and a variety of context-specific reported
functions (integrin cytoplasmic-tail binding, nuclear-export receptor for steroid
receptors, transcriptional/translational modulation).

## Core function evidence

- UniProt FUNCTION [file:human/CALR/CALR-uniprot.txt]:
  "Calcium-binding chaperone that promotes folding, oligomeric assembly and quality
  control in the endoplasmic reticulum (ER) via the calreticulin/calnexin cycle. This
  lectin interacts transiently with almost all of the monoglucosylated glycoproteins
  that are synthesized in the ER".

- Review [PMID:15474971 "Calreticulin is a 46-kDa Ca2+-binding chaperone found across a
  diverse range of species. The protein is involved in the regulation of intracellular
  Ca2+ homeostasis and endoplasmic reticulum (ER) Ca2+ storage capacity. Calreticulin is
  also an important molecular chaperone involved in "quality control" within secretory
  pathways."]. This review supports the calcium-binding, chaperone, and quality-control
  core functions (TAS-grade synthesis source).

- Lectin/glycan binding: CALR binds monoglucosylated MHC I glycans; [PMID:15056662
  "Major histocompatibility complex class I molecules expressed with monoglucosylated
  N-linked glycans bind calreticulin independently of their assembly status."] Carbohydrate
  binding (GO:0030246) is a core MF.

- MHC class I peptide loading complex (PLC): CALR is a structural component of the PLC
  and supports peptide-receptive MHC I. [PMID:35948544 "peptide-receptive MHC I molecules
  are stabilized by multivalent chaperone interactions including the calreticulin-engulfed
  mono-glucosylated MHC I glycan, which only becomes accessible for processing by
  α-glucosidase II upon loading of optimal epitopes."] CALR-null cells have impaired MHC I
  assembly [PMID:11825569 title]. This is a specialized but well-supported application of
  the core chaperone function; I treat PLC membership / peptide antigen assembly as
  core-adjacent (ACCEPT for the direct IDA in the human PLC structure paper, KEEP_AS_NON_CORE
  for ISS transfers).

- Client chaperone examples: insulin receptor [PMID:17563366 "calreticulin (CRT) and Hsp90
  exert distinct effects on the stability and cell surface levels of native and misfolded
  forms of the human insulin receptor"]. Mutant CALR perturbs the glycoproteome [PMID:36417879
  "Calreticulin mutations affect its chaperone function and perturb the glycoproteome."].

## Calcium
- Ca2+ binding (IBA, IEA, TAS PMID:15474971, TAS PMID:7841019, TAS PMID:11149926):
  core. CALR is the major high-capacity low-affinity Ca2+ store of the ER. The IMP from
  PMID:21705382 is about Bcl2l10 signature sequences, weak for CALR directly.
- intracellular calcium ion homeostasis (TAS PMID:11149926): core ER calcium role.

## Cell surface / extracellular ("eat-me" / immunogenic cell death) — REAL but non-core
- Cell surface localization on activated T cells, in association with MHC I
  [PMID:10358038 "the 60-kDa calreticulin was labeled by cell surface biotinylation and
  precipitated from the surface of activated T cells"]. Surface CALR is the prototypic
  pre-apoptotic "eat-me" signal driving phagocytosis (GO:0050766 positive regulation of
  phagocytosis); a real biology but secondary to the ER chaperone role -> KEEP_AS_NON_CORE.
- C1q binding (GO:0001849): CALR (cC1qR) binds the C1q collagen-like tail; relevant to
  apoptotic-cell clearance and complement [PMID:9922153 title]. Non-core.
- Cytolytic/lytic granule (GO:0044194 EXP PMID:8418194): CALR is a major constituent of
  CTL lytic granules; real localization, non-core.
- Extracellular region/matrix/exosome (HDA, IEA, TAS): secreted/extracellular pools exist
  but are non-core.
- Endothelial/trophoblast migration (PMID:22377355), dendritic cell chemotaxis (PMID:16140380
  via C1q/gC1qR), substrate adhesion/spreading (PMID:11859136): context-specific extracellular/
  surface activities -> KEEP_AS_NON_CORE.

## Nuclear / cytosolic moonlighting — non-core / over-annotated
- Nuclear export receptor activity (GO:0005049) and protein export from nucleus (GO:0006611):
  cytosolic CALR was reported to export the glucocorticoid receptor DNA-binding domain
  [PMID:11149926 "Calreticulin Is a receptor for nuclear export."]. Real but minor/disputed
  moonlighting; KEEP_AS_NON_CORE.
- Nuclear hormone receptor inhibition / negative regulation of transcription / steroid receptor
  signaling (PMID:8107809, PMID:8107808): CALR binds the KxFFKR motif in the GR/AR/RAR
  DNA-binding domain and inhibits their activity in vitro [PMID:8107809 "Inhibition of nuclear
  hormone receptor activity by calreticulin."]. The cluster of transcription/steroid-signaling
  BP terms (GO:0000122, GO:0045892, GO:0033144, GO:0042921, GO:0048387, GO:0045665, GO:0006355,
  GO:0050681, GO:0010628 etc.) derive from this in-vitro work and ortholog transfer; the
  DNA-binding domain motif interaction is the same one used for integrin binding (KLGFFKR).
  Mark the bare transcription/steroid BP terms as over-annotated or non-core; keep the specific
  androgen-receptor binding as non-core.
- Integrin binding (GO:0005178, PMID:1911778): in-vitro binding to KLGFFKR integrin alpha
  cytoplasmic tail peptide; biochemically real but cytosolic and not the conserved ER function
  -> KEEP_AS_NON_CORE.
- mRNA binding / negative regulation of translation (PMID:14726956 p21, PMID:12242300 C/EBP):
  cytosolic CALR reported to bind specific mRNAs and repress translation; moonlighting,
  non-core. The associated cell-cycle/senescence/proliferation BP terms (PMID:14726956) are
  downstream and over-broad.
- RNA binding (GO:0003723 HDA PMID:22658674), DNA binding (GO:0003677 NAS), zinc/iron ion
  binding (GO:0008270, GO:0005506): high-throughput or weakly supported; over-annotated for a
  functional MF.

## Over-broad ortholog (GO_REF:0000107) phenotype/response cluster
- A large block of IEA Ensembl-Compara terms: spermatogenesis, cardiac muscle cell
  differentiation, cellular response to electrical stimulus/lithium/virus, response to
  estradiol/testosterone/peptide/glycoside/biphenyl/xenobiotic, senescence, cell-cycle,
  postsynapse/glutamatergic synapse, acrosomal vesicle, etc. These are phenotype-/response-
  transfer over-annotations; most -> MARK_AS_OVER_ANNOTATED, a few developmental ones (cardiac)
  reflect the mouse CALR-knockout cardiac phenotype and are KEEP_AS_NON_CORE at most.

## protein binding (GO:0005515) cluster
Numerous IPI "protein binding" annotations from interactome maps and individual partner
studies (HLA-F/HLA-E, GABARAP, MBL, ERp57, etc.). Per guidelines, bare "protein binding"
is uninformative -> MARK_AS_OVER_ANNOTATED.

## Summary of core functions
1. MF: monoglucosylated N-glycan (carbohydrate) binding lectin / unfolded protein binding
   chaperone activity in the ER lumen.
2. MF: calcium ion binding (high-capacity ER Ca2+ buffering).
3. BP: protein folding / glycoprotein quality control in the ER (CNX/CRT cycle); protein
   maturation/stabilization.
4. BP: peptide antigen assembly with MHC class I (PLC) — specialized but well supported.
5. BP: ERAD pathway (triage of terminally misfolded clients).
6. CC: endoplasmic reticulum lumen.
Secondary (non-core): cell-surface eat-me signal / phagocytosis, extracellular pools,
C1q binding, cytosolic/nuclear moonlighting (nuclear export, integrin binding, mRNA binding).

## Falcon deep research findings (2026-06-07)

The Falcon report (`CALR-deep-research-falcon.md`) overwhelmingly CONFIRMS the existing
review for canonical biology (ER-luminal lectin chaperone of the CNX/CRT cycle, binds
monoglucosylated N-glycans, recruits ERp57/PDIA3 via the P-domain, high-capacity/low-affinity
ER Ca2+ buffer, KDEL retrieval, ecto-CALR eat-me/ICD role). The genuinely NEW material is the
oncogenic exon 9 mutant-CALR / MPN axis, which is entirely absent from the existing
`existing_annotations` (correctly, since these are neomorphic disease mutations not in GOA),
plus a more explicit receptor mechanism for the eat-me signal. Key points:

- NEW (disease, well established): Somatic exon 9 frameshift (+1 bp) CALR mutations are driver
  lesions in JAK2/MPL-nonmutated myeloproliferative neoplasms (essential thrombocythemia,
  primary myelofibrosis), replacing the acidic Ca2+-binding C-terminus + KDEL with a shared
  novel basic tail. First described in two 2013 NEJM papers [PMID:24325356 "Somatic insertions
  or deletions in exon 9 of CALR"; PMID:24325359 "Mutations were located in exon 9 and
  generated a +1 base-pair frameshift"]. Type 1 (del52) and type 2 (ins5) ~80% of mutant cases.
  This is mutation biology, not a function of WT CALR -> does NOT alter existing_annotations;
  recorded here and as statement-only references for context.

- NEW (mechanism): Mutant CALR gains a neomorphic, ligand(TPO)-independent interaction with the
  thrombopoietin receptor MPL (N-domain recognition of MPL N-glycans plus the mutant basic
  C-terminus), driving constitutive JAK2/STAT5(3), ERK1/2 and AKT activation and megakaryocytic
  transformation; MPL is required [PMID:27177927 Han 2016 "Exogenous expression of MPL led to
  constitutive activation of STAT3 and 5, ERK1/2, and AKT, cytokine-independent growth"]. Mutant
  CALR also shows accelerated degradation and Golgi-mediated secretion (same paper).

- NEW (mechanism, ties to Ca2+ core): Type 1 (but not type 2) mutants lose more acidic
  Ca2+-binding residues, directly impairing Ca2+ binding -> ER Ca2+ depletion -> selective
  activation of the IRE1alpha/XBP1 UPR arm; IRE1alpha/XBP1 inhibition selectively kills type 1
  mutant cells in vivo [PMID:35405004 Ibarra 2022 "loss of Ca2+ binding residues in the type I
  mutant CALR protein directly impairs its Ca2+ binding ability...activation of the IRE1alpha/XBP1
  pathway"]. Mechanistically links the WT high-capacity Ca2+-buffer function to disease.

- CONFIRMS + refines (interaction/pathway): ecto-CALR drives pro-phagocytic clearance via the
  LRP1/CD91 receptor on phagocytes/APCs (the existing review notes phagocytosis/eat-me and SCARF1/
  MSR1 scavenger receptors but not LRP1/CD91 by name). Falcon supports this only via 2024 review
  sources (janssens2024, reid/galassi2024), not primary data -> treat as PROVISIONAL receptor
  detail; not used to change annotations. GO:0050766 (positive regulation of phagocytosis) already
  KEEP_AS_NON_CORE.

- CONFIRMS (translational, not GO-actionable): mutant-CALR neo-C-terminus is a cell-surface
  neoantigen; active immunotherapy programs (peptide vaccine NCT05025488; bispecific JNJ-88549968
  NCT06150157) and antibody efforts (kramer2024 review). Context only; no annotation impact.

- Provenance caveats: Falcon's quantitative MPN prevalence figures vary across sources
  (~20% MPN / ~25-30% ET / ~40% ET+PMF) due to different denominators; the Faiz 2023 source is a
  thesis ("Unknown journal") and reid2024 has 0 citations -> low-confidence, kept out of the YAML.
  Only the four primary/peer-reviewed PMIDs above were resolved (via PubMed) and added as
  statement-only references.
