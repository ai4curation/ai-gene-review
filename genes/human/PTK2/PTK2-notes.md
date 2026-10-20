# PTK2 (human, Q05397) review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were compiled manually from the UniProt
record, the cached publications in `publications/` (abstract-only for many; see
`full_text_available:` in each file), the Reactome cache, QuickGO and
`gocams/index.tsv`. No `*-deep-research-*.md` file was created.

## Identity and architecture

- Focal adhesion kinase (FAK1), 1052 aa. FERM - kinase - proline-rich regions - FAT
  (focal adhesion targeting) domain. Isoform 6 (FRNK) is the C-terminal non-catalytic
  fragment that inhibits FAK signalling (UniProt).
- Catalytic activity: EC 2.7.10.2, L-tyrosyl-[protein] + ATP (UniProt; RHEA:10596).

## Core molecular function: tyrosine kinase at integrin adhesions

- Autophosphorylation at Tyr397 is the activating switch and creates the Src docking
  site [PMID:12391143 "Autophosphorylation of FAK on Tyr-397 is a critical event, allowing binding of Src family kinases and activation of signal transduction pathways"].
  Note: these experiments used rat FAK isoforms [PMID:12391143 "In all experiments, we used rat FAK + ( 2 ) or isoforms FAK +6,7 , FAK +7 , and FAK +6,7,28"].
- Substrates: Cas proteins [PMID:9360983 "FAK directly phosphorylates Cas proteins primarily at the YDYVHL sequence that is conserved among all Cas proteins"];
  N-WASP [PMID:14676198 "N-WASP is phosphorylated by FAK at a conserved tyrosine residue, Tyr(256)"].
- FAK-Src dual kinase complex [PMID:16919435 "Activated FAK-Src functions to promote cell motility, cell cycle progression and cell survival"];
  Src binding is through pTyr397-SH2 [PMID:16291744 "Phosphorylation at Tyr-397 activates FAK and creates a binding site for Src family kinases"],
  with an additional proline-rich/SH3 contact [PMID:21266176 "The interaction between a peptide encompassing the SH3 and SH2 binding motifs of focal adhesion kinase (FAK) and the Src SH3-SH2 domains has been investigated with NMR spectroscopy and calorimetry"].
- Other pTyr-SH2 partners: GRB2 [PMID:7597091 "tyrosine-phosphorylated pp125FAK directly interacts with the SH2 domain of Grb2"];
  p120RasGAP [PMID:15077193 "the Y397 residue of FAK plays a role in the formation of this complex and in the activation of Ras"].

## Adhesion targeting

- Paxillin binding targets FAK to FAs [PMID:7561682 "These findings strongly suggest that pp125FAK is localized to focal adhesions by the direct association with paxillin"].
- Talin: direct FAT-talin binding; FAK recruits talin to nascent adhesions
  [PMID:22270917 "The direct binding site for talin on FAK was identified, and a point mutation in FAK (E1015A) prevented talin association and talin localization to nascent adhesions"];
  [PMID:22270917 "FAK promotes talin recruitment to nascent adhesions occurring independently of talin binding to β1 integrins"].
- Integrins: [PMID:26763945 "integrin β1 binding to FN is necessary for FAK association with integrin β1 and subsequent FAK activation"];
  [PMID:27178753 "Activated β4 integrin interacts with FAK and subsequently induces FAK phosphorylation at Tyr397"].
- Integrin dependence of FAK phosphorylation, even downstream of GPCRs
  [PMID:9636140 "tyrosine phosphorylation of paxillin and FAK elicited by stimulation of muscarinic m3 receptors with the acetylcholine analog carbachol is inhibited by soluble peptides containing the arginine-glycine-aspartate motif"].

## Processes

- Migration via GEF/GAP control of Rho GTPases [PMID:19525103 "FAK is in a unique signaling position to modulate RhoGTPase activity in space and time, thereby affecting various steps (integrin activation, leading edge formation, FA turnover, and trailing edge retraction) needed for efficient directional cell migration"].
- Survival: PI3K/Akt [PMID:15166238 "Blocking FAK by pharmacologic inhibition or by dominant negative FAK attenuated phosphorylation of p85 subunit of PI3K and Akt"]; anoikis suppression [PMID:22402981].
- Nuclear scaffold for p53 degradation [PMID:18206965 "These studies define a scaffolding role for nuclear FAK in facilitating cell survival through enhanced p53 degradation under conditions of cellular stress"];
  direct p53 binding [PMID:15855171 "the N-terminal fragment of FAK directly interacts with the N-terminal transactivation domain of p53"].
- Development (review): [PMID:20552554 "Various published data supported the role of the molecule in the development of the placenta, as well as of several organ systems, like the musculoskeletal, nervous, cardiovascular, genitourinary and respiratory organ systems"].

## Premetazoan evidence (ancestral vs animal-specific)

- Canonical FAK is holozoan, not animal-specific: [PMID:20479219 "bona fide FAK are only present in Metazoa and C. owczarzaki"];
  [PMID:20479219 "C. owczarzaki FAK have all of the functional domains involved in its protein–protein interactions"].
- Choanoflagellates lost it (with integrins and the IPP complex), retaining only a FAK-related kinase domain:
  [PMID:20479219 "lack both integrin β and α, the full IPP complex, and one of the signaling molecules involved in the integrin adhesome, FAK"];
  [PMID:20479219 "M. brevicollis has a gene encoding a tyrosine kinase domain that, by phylogenetic analysis, seems to be related to FAK"].
- Apusozoan Amastigomonas has most of the adhesome but not FAK or c-Src
  [PMID:20479219 "including all of the components of the canonical metazoan complex, except for the signaling molecules FAK and c-Src"].
  The authors' preferred scenario is a holozoan origin of the canonical machinery, with the
  alternative that FAK and c-Src were lost in apusozoans.
- Capsaspora integrin adhesion is functional, but FAK was not examined (abstract only):
  [PMID:32857975 "during the adherent life stage, C. owczarzaki adheres to surfaces using actin-dependent filopodia"];
  [PMID:32857975 "We show that integrin β2 and its associated protein vinculin localize as distinct patches in the filopodia"].
- Interpretation:
  - Ancestral, inferred from domain conservation only: the FAK domain set (FERM, kinase, FAT) and so,
    plausibly, kinase signalling at integrin adhesions. There is no functional FAK data from any
    non-animal.
  - Animal-specific on current evidence: all developmental roles (placenta, heart, vasculature,
    neurons), growth-factor/GPCR/netrin/Eph receptor crosstalk, immune contexts, nuclear p53 regulation,
    and specialised locations such as ciliary basal bodies.
  - This matches the TLN1/VCL reviews, where the integrin-talin-vinculin linkage is treated as ancestral
    (sponge biochemistry; Capsaspora filopodia), and the CSK review on Src-family regulation.

## GO-CAM

`gocams/index.tsv` has PTK2 in two models, both with GO:0004715 non-membrane spanning protein
tyrosine kinase activity:
- 682fbcd000002551 (FAISL): part of GO:0051894 positive regulation of focal adhesion assembly.
- 689e7a5d00003515 (Ephrin-A1/EPHA2 negative regulation of cell adhesion mediated by integrin):
  part of GO:0033634 positive regulation of cell-cell adhesion mediated by integrin, in focal adhesion.
  The model gives FAK a positive role that EphA2/SHP2 suppresses. That is why the GOA row
  "negative regulation of cell adhesion mediated by integrin" on FAK was marked over-annotated.
  The cell-cell restriction does not fit the matrix-adhesion assays, so the positive row was
  modified to GO:0033630.

## Annotation decisions (summary)

- 75 generic protein-binding rows: 66 removed under the repository policy. 9 modified where the
  binding mode is defined: SH2 domain binding (SRC pY397, GRB2 pY925, Src SH3-SH2 peptide), SH3
  domain binding (Src SH3 NMR), p53 binding (x2), integrin binding (ITGB4), PH domain binding
  (Etk/BMX), talin binding.
- Protein tyrosine phosphatase activity (IMP, PMID:9360983) was modified to tyrosine kinase activity.
  The paper shows FAK phosphorylating Cas, and FAK has no phosphatase domain.
- UNDECIDED: actin binding (PMID:16803572, abstract silent on FAK); JUN kinase binding (PMID:10925297,
  abstract describes Jak2, possible JAK/JNK mix-up); two IL-34/macrophage IGI rows (PMID:26754294,
  abstract silent on FAK); molecular function activator activity (PMID:12467573, structure paper).
- NEW: peptidyl-tyrosine autophosphorylation (GO:0038083). FAK itself catalyses the Tyr397 step
  (Reactome R-HSA-354073).
