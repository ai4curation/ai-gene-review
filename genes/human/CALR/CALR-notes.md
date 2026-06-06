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
