# SOS1 (NHX7 / SALT OVERLY SENSITIVE 1) — curation notes

UniProt: Q9LKW9 (NHX7_ARATH). Gene: NHX7, synonym SOS1, At2g01980. 1146 aa, 127 kDa.
TC family 2.A.36.7.6 (monovalent cation:proton antiporter-1, CPA1).

## Core biology

SOS1 is a plasma-membrane Na+/H+ antiporter that extrudes Na+ (and Li+) from the
cytosol in exchange for H+, using the inwardly directed proton motive force generated
by plasma-membrane H+-ATPases. It is the effector at the bottom of the SOS (Salt Overly
Sensitive) signaling module: the Ca2+ sensor CBL4/SOS3 activates the kinase CIPK24/SOS2,
which phosphorylates SOS1 to relieve autoinhibition.

Topology: ~12 N-terminal transmembrane helices (UniProt models 11 TM helices, residues
29–441) followed by a large (~700 aa) cytoplasmic C-terminal tail (442–1146) that carries
the regulatory/autoinhibitory machinery [UniProt FT TOPO_DOM/TRANSMEM].

## Molecular function

- Electroneutral Na+(in)/H+(out) exchange across the plasma membrane.
  [UniProt FUNCTION "Acts in electroneutral exchange of protons for cations such as Na(+) or Li(+) across plasma membrane"]
  [UniProt CATALYTIC ACTIVITY RHEA:29419 Na(+)(in) + H(+)(out) = Na(+)(out) + H(+)(in); Evidence ECO:0000269|PubMed:12239394]
- Na+ specificity demonstrated functionally: when expressed in a yeast mutant lacking
  endogenous Na+ transporters, SOS1 reduced Na+ accumulation and improved salt tolerance,
  but was "inefficient for K+ efflux or uptake in vivo"
  [PMID:11884687 "SOS1 activity was specific for Na+ because the plant protein was inefficient for K+ efflux or uptake in vivo"].
- KM ≈ 22.8 mM for Na+ [UniProt BIOPHYSICOCHEMICAL PROPERTIES; ECO:0000269|PubMed:12805632].
- A K+/H+ antiporter catalytic activity is also curated (RHEA:29467) with the same
  evidence (PubMed:12239394), but the in vivo data argue SOS1 is Na+-specific and the
  sos1 K+ phenotype is indirect (linked Na+/K+ exchange at the xylem/symplast boundary)
  [PMID:11884687 "net Na+/K+ exchange was achieved by coupling Na+/H+ and K+/H+ antiport activities at the xylem/symplast boundary"; "Perhaps under low K+ availability, a functional SOS1 is required to enable K+ loading to the xylem"].

## Localization

- Plasma membrane, multi-pass. SOS1-GFP fusion localizes to the plasma membrane in
  transgenic Arabidopsis [PMID:11884687 "confocal imaging of the SOS1-GFP fusion protein indicated a plasma membrane localization of SOS1"].
  Also IDA in PMID:10823923 (TAIR) and consistent with the predicted topology.
- A single proteomic study reports SOS1 in a "mixed" chloroplast envelope preparation
  [PMID:12938931]; this is a large-scale organelle proteomics dataset (392 nonredundant
  proteins) without targeted validation, contradicted by the strong PM localization and
  the SOS signaling biology. Treated as likely contaminant / over-annotation.
- A phosphoproteomics study (PMID:14506206) identifies SOS1 among PM phosphoproteins —
  consistent with PM location and with regulation by phosphorylation.

## Biological processes

- Cytosolic Na+/Li+ detoxification (efflux to apoplast) conferring salt tolerance.
  [UniProt FUNCTION "Required for cytoplasmic Na(+) and Li(+) detoxification by secreting them from the cytoplasm to the extracellular space"]
  sos1 mutants are >20x more sensitive to NaCl [PMID:12239394 abstract].
- Long-distance Na+ transport (root-to-shoot) and control of xylem Na+ load. SOS1 is
  expressed in parenchyma cells at the xylem/symplast boundary and regulates xylem sap
  Na+ content [PMID:11884687 "SOS1 is critical for controlling long-distance Na+ transport from root to shoot"; "Regulates Na(+) content of the xylem sap" — UniProt FUNCTION].
- Response to salt stress (IMP/IEP in multiple papers; SOS1 transcript induced by Na+ in
  a SOS-pathway-dependent manner) [PMID:10823923 "SOS1 gene expression in plants is up-regulated in response to NaCl stress"].
- Oxidative-stress / ROS modulation: SOS1 C-terminal tail interacts with RCD1 and SOS1
  influences ROS-related gene expression; sos1 mutants over-accumulate ROS under salt but
  are MORE tolerant to chloroplastic ROS (methyl viologen) — SOS1 plays a "negative role"
  in oxidative-stress tolerance via apoplastic pH/NADPH-oxidase
  [PMID:17023541 "SOS1 interacts through its predicted cytoplasmic tail with RCD1, a regulator of oxidative-stress responses"]
  [PMID:17996020 "mutations in the SOS1 gene render sos1 mutants more tolerant to paraquat ... indicating that SOS1 plays negative roles in tolerance of oxidative stress"].
  These ROS roles are real but secondary/indirect to the core Na+/H+ antiport function.

## Regulation

- SOS2-SOS3 phosphorylation relieves C-terminal autoinhibition.
  [PMID:21262798 "SOS1 is maintained in a resting state by a C-terminal auto-inhibitory domain that is the target of SOS2-SOS3"; "SOS1 is relieved from auto-inhibition upon phosphorylation of the auto-inhibitory domain by SOS2-SOS3"]
  Phosphosite Ser1138 (recognition Ser1136) [PMID:21262798 Discussion].
- Interactors (IntAct): CIPK24/SOS2 (Q9LDI3) and RCD1 (Q8RY59) [UniProt INTERACTION].

## GOA annotation assessment summary

- MF GO:0015385 sodium:proton antiporter activity (IBA via UniProt; IEA InterPro) — ACCEPT, core.
- MF GO:0015297 antiporter activity (IEA) — accurate but generic parent; ACCEPT (broader IEA ok).
- MF GO:0015386 potassium:proton antiporter activity (EXP, PMID:12239394) — MARK_AS_OVER_ANNOTATED;
  in vivo SOS1 is Na+-specific (PMID:11884687); K+ link is indirect.
- MF GO:0005515 protein binding (IPI x2: RCD1, CIPK24) — uninformative; REMOVE.
- CC GO:0005886 plasma membrane (IDA x2, HDA, IEA, ISM) — ACCEPT, core.
- CC GO:0009941 chloroplast envelope (HDA, PMID:12938931) — REMOVE/over-annotated (proteomics artifact).
- CC GO:0016020 membrane (IEA) — accurate generic parent; ACCEPT.
- BP GO:0098719 sodium ion import across plasma membrane (IBA) — directionally questionable
  (SOS1 mainly exports Na+ from cytosol), but SOS1 also retrieves Na+ from xylem under
  severe stress; keep but note import is one mode. ACCEPT (IBA, captures Na+ PM transport).
- BP GO:0006814 sodium ion transport (IMP) — ACCEPT core.
- BP GO:0006812 monoatomic cation transport (IEA) — generic parent, ACCEPT.
- BP GO:0055085 transmembrane transport / GO:1902600 proton transmembrane transport (IEA) — ACCEPT (generic but correct).
- BP GO:0009651 response to salt stress (IMP/IEP x3) — ACCEPT core.
- BP GO:0051453 regulation of intracellular pH (IBA) — KEEP_AS_NON_CORE (antiport alters
  cytosolic/apoplastic pH; supported by Shabala 2005 cited in PMID:17996020).
- BP GO:0071805 potassium ion transmembrane transport (IMP, PMID:12239394) — KEEP_AS_NON_CORE
  (genetic K+-acquisition phenotype is indirect, not direct K+ transport by SOS1).
- BP ROS/oxidative terms GO:2000377, GO:0000302, GO:0006979, GO:0042542 (x2) — KEEP_AS_NON_CORE
  (real but secondary, indirect via apoplastic pH/RCD1/NADPH oxidase).
- BP GO:0006814 from PMID:11874577 — the PCD paper only uses sos1 as a salt-sensitive
  genetic background; it supports salt-sensitivity, indirectly sodium transport. Keep but non-core.

## New term candidates considered

Did not add a "sodium ion export across plasma membrane" NEW annotation because I could
not verify a GO ID via OLS in this session; GO:0098719 (import) and GO:0006814 (sodium ion
transport) already cover plasma-membrane Na+ transport. Noted as a suggested question instead.

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)

The Falcon deep-research report (`SOS1-deep-research-falcon.md`) corroborates the existing
review and adds recent (2022-2025) synthesis without changing any curation decisions.

Corroborations now cross-referenced as `supported_by` in the review:
- Core MF (Na+/H+ antiport): "SOS1/NHX7 mediates active Na+ efflux from the cytosol in
  exchange for H+, lowering cytosolic Na+ during salt stress."
- Proton transport coupling: "Transport is driven by the proton electrochemical gradient
  generated by the plasma-membrane H+-ATPase" (the PM H+-ATPase supplies the pmf).
- Plasma-membrane localization: confocal SOS1:GFP recruitment to the PM (Gámez-Arjona 2024).
- Salt-stress process: loss-of-function sos mutants are strongly salt sensitive; SOS pathway
  essential for salt tolerance via ion homeostasis.
- Long-distance Na+ transport (GO:0098719 import / core_functions): roles in both direct Na+
  efflux at the root surface and regulation of long-distance Na+ transport via xylem
  loading/unloading.

New mechanistic detail not previously captured (recorded here, not yet annotated because the
primary papers are not in the publications cache and no new verifiable GO ID was identified):
- Phosphoregulation: SOS2/CIPK24 phosphorylates conserved serines Ser1136/Ser1138 in the
  C-terminal self-inhibitory domain to relieve autoinhibition (Xie et al. 2022 review).
  Complements the existing Ser1138/recognition-Ser1136 note from PMID:21262798.
- SOS3/CBL4 directly binds SOS1 at a mapped S3BD (K460-L482) and controls salt-inducible PM
  recruitment/stability of SOS1, while inversely directing proteasomal degradation of HKT1;1
  (Gámez-Arjona et al. 2024, PNAS 10.1073/pnas.2320657121). This is a candidate basis for a
  more specific protein-interaction / localization-regulation annotation than bare
  GO:0005515, but the primary paper is not cached, so no annotation change was made.
- CBL10/SCaBP8 branch and PP2C.D phosphatase inhibition add further regulatory layers
  (root SOS3 vs shoot SCaBP8 specialization).

Decisions unchanged: no UNDECIDED actions existed; the two GO:0005515 protein binding
annotations remain REMOVE (the SOS3/SOS2 interactions are real but bare "protein binding"
stays uninformative); GO:0015386 K+/H+ antiporter remains MARK_AS_OVER_ANNOTATED; chloroplast
envelope remains REMOVE. No NEW GO annotation added (no new verifiable GO ID).

## PR #1417 review fix (ai4c-agent comment)

Reviewer flagged an internal inconsistency: GO:0098719 (sodium ion import across
plasma membrane) was ACCEPTed as core in existing_annotations while the description and
proposed_new_terms both state Na+ EXPORT/efflux is the defining core function and that an
export term is the missing core annotation. Accepting import as core while proposing export
as the missing core is contradictory.

Fix: changed GO:0098719 action ACCEPT -> KEEP_AS_NON_CORE. Updated summary/reason to state
that Na+ export/efflux from the cytosol is the core physiological function, and that the
import direction captured by this term is a secondary, condition-dependent xylem-retrieval
mode under severe salt stress (reflecting antiporter reversibility). Supporting_by evidence
(PMID:11884687, falcon deep-research) retained unchanged. No other annotations weakened.
Validation: Valid (1 pre-existing benign warning that GO:0098719 in core_functions[1] is not
mirrored as a NEW annotation in existing_annotations).
</content>
</invoke>
