# EMC6 (Q9BV81) review notes

## Identity
- ER membrane protein complex subunit 6; synonym TMEM93 (TMEM93). HGNC:28430, gene 83460, chromosome 17.
- Small 110 aa polytopic ER membrane protein with three transmembrane helices (TM1 29-44, TM2 51-71, TM3 90-106) and an N-cytoplasmic/C-lumenal topology [file:human/EMC6/EMC6-uniprot.txt "TRANSMEM        29..44"].
- Belongs to the EMC6 family [file:human/EMC6/EMC6-uniprot.txt "Belongs to the EMC6 family"].

## Function: EMC insertase core
- Component of the ER membrane protein complex (EMC), a conserved ~9-subunit ER insertase/chaperone for membrane proteins [file:human/EMC6/EMC6-uniprot.txt "Component of the ER membrane protein complex (EMC)"].
- EMC enables energy-independent insertion of newly synthesized membrane proteins into the ER membrane; it preferentially handles TMDs that are weakly hydrophobic or contain destabilizing charged/aromatic residues [file:human/EMC6/EMC6-uniprot.txt "enables the energy-independent insertion into endoplasmic"].
- EMC is a transmembrane domain insertase [PMID:29242231 "EMC is a transmembrane domain insertase"]; it inserts tail-anchored (TA) proteins with moderately hydrophobic TMDs post-translationally [PMID:29242231 "tail-anchored membrane proteins with moderately hydrophobic transmembrane"].
- EMC3 is the catalytic insertase subunit (YidC/Get1/Oxa1 superfamily); EMC6 packs against EMC3 to form the hydrophilic insertase vestibule in the membrane. EMC6 mutagenesis of Asp-27 and Thr-31 (cytoplasmic/TM1 boundary) does NOT affect EMC assembly but decreases membrane insertion of hydrophobic-TMD client proteins, demonstrating EMC6's direct contribution to the insertase reaction [file:human/EMC6/EMC6-uniprot.txt "No effect on EMC assembly but decreased"]. This experimental separation of assembly from activity is why "membrane insertase activity" (GO:0032977, contributes_to) is defensible CORE for EMC6, not merely the bulk EMC.
- Cotranslational role: EMC engages multipass membrane protein clients cotranslationally to enable their biogenesis [PMID:29809151 "biogenesis of multipass membrane proteins"].
- Topogenesis role: EMC controls topology of multipass proteins (e.g., GPCRs) by inserting the first N-terminal TMD in N-exo orientation [PMID:30415835 "EMC Is Required to Initiate Accurate Membrane Protein Topogenesis"]; clients include the beta1-adrenergic receptor and other GPCRs [PMID:30415835 "β1-adrenergic receptor (β1AR) and other G protein-coupled receptors (GPCRs)"].
- In vivo IMP evidence in Drosophila: EMC (including EMC6) is required for TMD membrane insertion of the TA client Xport-A [PMID:34918864 "EMC is required for Xport-A TMD membrane insertion"]; this paper underpins the FlyBase-assigned GO:0032977 contributes_to membrane insertase activity and GO:0071816 (TA insertion).

## Subcellular location
- ER membrane, multi-pass membrane protein [file:human/EMC6/EMC6-uniprot.txt "Endoplasmic reticulum membrane"]. IDA support PMID:22119785 (identified EMC in ERAD network), PMID:30415835, PMID:32439656.

## Autophagy annotations (GO:0000045, GO:1903349)
- A single 2013 study (abstract-only in cache, full_text_available: false) reported EMC6/TMEM93 as an ER-localized protein interacting with RAB5A and BECN1/Beclin1, colocalizing with the omegasome marker DFCP1/ZFYVE1, and regulating autophagosome formation [PMID:23182941 "It was shown to regulate "; PMID:23182941 "colocalized with the omegasome marker ZFYVE1/DFCP1"].
- This predates the insertase-core understanding of EMC. The autophagy/omegasome phenotype is plausibly an INDIRECT/secondary consequence of impaired biogenesis of membrane-protein clients (EMC's "indirect client" model is explicitly discussed in PMID:34918864). The IMP autophagosome-assembly and IDA omegasome-membrane annotations rest on this one experimental paper whose full text the curator read; per guidelines, do not REMOVE experimental annotations on incomplete evidence -> keep as NON_CORE (not the core insertase function). The IBA autophagosome-assembly term (PAN-GO) propagates this single experimental observation across the family; although weakly supported, it is retained as peripheral rather than removed -> KEEP_AS_NON_CORE (consistent with the IMP/IDA handling above, and matching the action recorded in the YAML).

## protein binding (GO:0005515)
- Many IPI annotations (IntAct/UniProt) to EMC client/partner proteins (MMGT1/EMC10, AQP6, AQP9, GPCR clients, SLC transporters, etc.) and to RAB5A/BECN1. Bare "protein binding" is uninformative per curation guidelines -> KEEP_AS_NON_CORE. PMID:32296183 (HuRI binary interactome) and PMID:33961781 (BioPlex) are high-throughput; PMID:22119785 (EMC10/MMGT1) and PMID:32439656 (EMC assembly) reflect genuine EMC partnerships.

## Core function call for EMC6
1. EMC complex (GO:0072546) membership - CORE structural identity.
2. ER membrane (GO:0005789) - CORE location.
3. Membrane insertase activity (GO:0032977, contributes_to) - CORE MF: EMC6 + EMC3 form the catalytic insertase core; EMC6 D27/T31 mutants reduce insertion without disrupting assembly.
4. TA insertion (GO:0071816) and stop-transfer/multipass insertion (GO:0045050) - CORE biological processes of the insertase.

## Reference relevance
- HIGH: PMID:29242231, PMID:30415835, PMID:32439656, PMID:34918864 (insertase mechanism/structure/in vivo), PMID:22119785 (EMC discovery in human, ER loc).
- MEDIUM: PMID:29809151 (multipass cotranslational role).
- LOW/contextual: PMID:32296183, PMID:33961781 (HT interactome), PMID:23182941 (autophagy; pre-insertase, indirect).

## Falcon deep-research findings (incorporated 2026-06)

New EMC6-relevant references verified against PubMed and added to the review (all additive; no action changes). These reinforce EMC6's core role in the EMC3/EMC6 insertase vestibule.

- 2023 selectivity-filter study consolidates the **EMC3/EMC6 hydrophilic vestibule** as the central insertion route and a charge-based selectivity filter enforcing the positive-inside rule; EMC6 mutations had milder effects than EMC3 in the tested context but EMC6 remains part of the vestibule-enclosing core. [PMID:37199759 "membrane insertion through a hydrophilic vestibule ... selectivity filter"]
- EMC acts as a **holdase/chaperone** during assembly of the multipass CaV1.2 channel (TM and Cyto client docks), extending EMC function beyond insertion. [PMID:37196677 "the EMC functions as a channel holdase that facilitates channel assembly"]
- 2024 human EMC cryo-EM (apo + VDAC-bound) places EMC6 in the **EMC3-EMC6 core**; a vestibule **gating plug** (assigned to EMC3) changes conformation between states, and the EMC engages **VDAC at mitochondria-ER contact sites**. [PMID:38517390 "identified a gating plug located inside the EMC hydrophilic vestibule"]
- 2025 chaperone study names EMC6 as part of a **lipid-filled cavity (EMC1/EMC3/EMC5/EMC6)** distinct from the canonical insertase site, supporting a broader EMC chaperone/quality-control role; the EMC engages TMDs via EMC1. [PMID:40753078 "we characterize an additional chaperone function of the EMC"]
- Core EMC6 call is unchanged: EMC complex membership + ER membrane localization + membrane insertase activity (contributes_to, via the EMC3/EMC6 vestibule) + TA and stop-transfer/multipass insertion processes. Autophagy/omegasome annotations remain KEEP_AS_NON_CORE.
