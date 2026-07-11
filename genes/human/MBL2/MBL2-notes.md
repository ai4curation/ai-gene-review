# MBL2 (Mannose-binding lectin 2 / mannan-binding lectin) — Research notes

UniProt: P11226 (MBL2_HUMAN). HGNC:6922. Chr 10. 248 aa precursor (chain 21-248).

## One-line summary

MBL2 encodes the secreted, liver-derived serum collectin "mannose-binding lectin" (MBL,
mannan-binding protein, MBP-C). It is a Ca2+-dependent C-type lectin pattern-recognition
molecule of innate immunity that recognizes terminal mannose/GlcNAc/fucose on microbial
surfaces and, via associated MASP serine proteases, initiates the LECTIN PATHWAY of complement.

## Architecture (from UniProt P11226)

- Signal peptide 1-20; mature chain 21-248.
- Collagen-like domain ~42-99 (Gly-X-Y repeats; hydroxyproline at Pro-47,73,79,82,88 — collagen-type post-translational modification) [UniProt FT, ECO from PMID:7982896].
- Coiled-coil 112-130 — mediates trimerization of the subunit [PMID:7634089].
- C-type lectin / carbohydrate-recognition domain (CRD) 134-245; PROSITE C_TYPE_LECTIN.
- Ca2+ binding residues (CRD): 188,192,209,210,212,214,215,220,221,230,232,233; glycosyl-ligand contacts 212,214,220,232,233 [PMID:7634089, PDB 1HUP].
- Disulfides 155-244, 222-236.
- Domains: Pfam Collagen (PF01391) + Lectin_C (PF00059). PANTHER PTHR24024 (collectin / surfactant-protein-A family). NOT a CAZyme (lectin, not glycoside hydrolase/transferase).
- Quaternary structure: structural subunit = homotrimer; functional serum protein = oligomers of 3+ homotrimers ("bouquet"); S-MBP ~18 subunits, L-MBP ~9 [PMID:7982896]; trimeric vs tetrameric oligomers differ in binding/complement activation [PMID:27104295].

## Core molecular function — Ca2+-dependent carbohydrate (mannose) binding

- Serum lectin specific for mannose and N-acetylglucosamine; Ca2+-dependent, saturable, Kd ~2.3e-9 M; distinct from CRP/SAP [PMID:6643429 "A serum lectin specific for mannose and N-acetylglucosamine residues was isolated from human serum", "Binding of the isolated lectin to 125I-labeled mannan was dependent upon the presence of Ca2+"].
- MBP is "a calcium-dependent plasma lectin"; binding to bacteria inhibited by mannose and N-acetyl-D-glucosamine [PMID:8082295 "Mannan-binding protein (MBP), a calcium-dependent plasma lectin", "The binding was inhibited by unlabelled MBP, by mannose and by N-acetyl-D-glucosamine"].
- Binds repetitive carbohydrate on viruses/bacteria/fungi/protozoa (Reactome R-HSA-166721).
- SARS-CoV-2 spike binding is glycan-dependent and calcium-dependent [PMID:35102342 "MBL bound trimeric spike protein, including that of variants of concern (VoC), in a glycan-dependent manner"; UniProt: "the interaction is calcium-dependent"].

GO mapping: GO:0005537 D-mannose binding (MF, verified active), GO:0030246 carbohydrate
binding (MF parent, verified), GO:0120153 calcium-dependent carbohydrate binding (MF,
verified active 2026-06; definition "capability to attach to a carbohydrate molecule when
calcium ions are present"). The Ca2+-dependent sugar binding is the defining, evolutionarily
conserved core MF; this should be the apex of core_functions rather than "protein binding".

## Pattern-recognition receptor activity + complement lectin pathway

- MBL is "a prototypic pattern recognition molecule that is able to recognize the molecular patterns that decorate a wide range of microorganisms" [PMID:15148336 full text].
- MBL binds carbohydrates and activates complement through associated serine proteases (MASP-1/p100 and MASP-2), similar to C1r/C1s of the classical pathway; structurally related to C1q [PMID:9087411 "MBL is structurally related to the complement C1 subcomponent, C1q", "complement activation through MBL, like the classical pathway, involves two serine proteases"].
- In normal human serum MASP-1 is the exclusive activator of MASP-2; both MBL-MASP and ficolin-MASP complexes contain MASP-1 [PMID:22691502 "In normal human serum, MASP-2 activation strictly depends on MASP-1"].
- MASP-1 crucial for LP activation; MASP-1 and MASP-2 co-complex on MBL [PMID:22966085 "MASP-1 dramatically increases lectin pathway activity ... through direct activation of MASP-2", "MASP-1 and MASP-2 can associate in the same MBL complex"].
- Architecture of the 450 kDa MBL/MASP-1 initiating complex [PMID:25579818 "the complex of mannan-binding lectin (MBL) and MBL-associated serine protease-1 (MASP-1) initiates the pathway by activating a second protease, MASP-2"].
- 9-aa sequence at start of collagen-like domain required for complement activation; only S-MBP (18 subunits) not L-MBP (9 subunits) activates complement [PMID:7982896].

GO mapping: GO:0038187 pattern recognition receptor activity (MF, IDA); GO:0001867 complement
activation, lectin pathway (BP, IDA — strongly supported); GO:0045087 innate immune response;
GO:0042742 defense response to bacterium. These are core.

## Opsonization / phagocytosis / defense (downstream effector roles)

- Low serum MBP correlates with a common opsonic defect (~5-7% of population); purified MBP corrects the defect dose-dependently [PMID:2573758 "the presence of the defect was linked with low levels of mannan-binding protein (MBP), a calcium-dependent serum lectin", "Purified MBP corrected the defect in a dose-dependent way"].
- MBL-null mice (Mbl1/Mbl2 double KO) highly susceptible to S. aureus (100% mortality vs 45%) — direct in vivo evidence for defense role [PMID:15148336]. NOTE: this is the rodent ortholog system (mouse MBL-A/MBL-C); annotation transferred to human MBL2 is a defensible functional assertion but cross-species.
- Opsonization / positive regulation of opsonization (GO:0008228, GO:1903028); positive regulation of phagocytosis (GO:0050766, IBA). Core process roles but the most downstream effector consequences (phagocytosis, opsonization) are arguably KEEP_AS_NON_CORE as they are mediated by complement deposition rather than a direct MBL activity.

## Interactions = the MASP/MAp/regulator network (basis of "protein binding" IPI)

Most GO:0005515 "protein binding" / GO:0042802 "identical protein binding" /
GO:0048306 "calcium-dependent protein binding" IPI annotations come from a coherent body of
interaction studies, NOT from random partners:
- MASP-1, MASP-2, MASP-3, MAp19/MAp44, MAP-1 (the lectin-protease complex): PMID:11290788, 9087411, 15117939, 18177377 (calreticulin co-receptor via MASP-binding site), 19939495, 20956340 (CL-11), 21035894 (MAP-1), 21054788 (CD91/LRP1 via MASP-binding site), 22607836, 22854970 (MAP-1 structure), 25579818 (initiating complex).
- CR1 (complement receptor 1, CCP24-25): PMID:23460739, 29563915.
- Cross-talk / pentraxins: PMID:21106539 (PTX3/SAP heterocomplexes), 32041782 (CTRP6/collectin-11), 32759297 (β2-glycoprotein I).
- TLR4: PMID:21383675 (MBL binds TLR4 ectodomain, suppresses LPS-induced cytokines) — a regulatory/immunomodulatory interaction.
- SRGN serglycin: PMID:21268013 (GAG-mediated inhibition of LP). DMBT1/SALSA/gp340: PMID:22811680.
- HCV glycoproteins: PMID:21203938 (inhibits HCV entry). High-throughput interactome: PMID:32296183, 33961781 (HuRI / BioPlex; generic, low specificity).

These IPI "protein binding" terms are real but UNINFORMATIVE as MF. Per curation guidelines
they should not be the gene's representative MF. The MASP-binding interactions are best captured
in core_functions via complex membership (GO:1905370 serine-type endopeptidase complex /
ComplexPortal CPX-6170, CPX-6203) plus the carbohydrate-binding MF, rather than retained as
generic "protein binding". Action plan: MARK_AS_OVER_ANNOTATED most generic GO:0005515 IPI
(keep, but non-representative); ACCEPT/KEEP the MASP-relevant identical/Ca2+-dependent protein
binding that documents complex assembly; downgrade in core_functions toward carbohydrate binding.

## Possible miscitations / careful handling

- PMID:2477488 "Lipopolysaccharide (LPS) binding protein opsonizes LPS-bearing particles..." —
  this paper is about LBP (LPS-binding protein), NOT MBL2. It defines LBP as an opsonin and is
  an acute-phase reactant. Yet GOA (BHF-UCL TAS) uses it to ground MBL2: cell surface,
  defense response to bacterium, acute-phase response, opsonization, AND D-mannose binding (TAS).
  The D-mannose-binding TAS to an LBP paper looks like a wrong-paper citation. The functions
  themselves (opsonin, acute-phase) are TRUE of MBL but supported elsewhere; the citation is
  questionable. Per "do not overrule curators from incomplete evidence", I will not REMOVE the
  process terms (they are correct functions, well supported by other refs) but will flag the
  reference as MISCITED/LOW relevance and prefer better references; the D-mannose-binding TAS on
  this ref I will mark for MODIFY/over-annotation reasoning toward the IDA-supported mannose binding.
- PMID:23544079 "Serum amyloid P is a sialylated glycoprotein inhibitor of influenza A viruses" —
  primarily about SAP, but the full text discusses MBL as a β-type C-type-lectin inhibitor of IAV
  and uses purified human MBL as a comparator/reagent ("Mannose-binding lectin (MBL), another β
  inhibitor of IAV, is a serum collectin"; "human MBL ... prepared by affinity purification from
  pooled human plasma using mannan agarose"). MBL IS discussed/handled, so per CLAUDE.md I will NOT
  REMOVE on title grounds; but the paper's primary subject is SAP, so the MBL annotations
  (D-mannose binding IDA, negative regulation of viral process, innate immune response,
  extracellular region) are weakly/comparatively supported here → KEEP_AS_NON_CORE / note lower
  relevance. The antiviral (anti-IAV) role of MBL is genuine but this is not the strongest ref.

## Disease / polymorphism (process-level, mostly non-core)

Structural variants in exon 1 (codon 52 R>C, 54 G>D [rs1800450], 57 G>E [rs1800451]) disrupt the
collagen helix and lower serum MBL; promoter variants modulate levels. MBL deficiency (~5% of
Europeans, ~10% sub-Saharan Africans) predisposes to infection in toddlers, neutropenic
chemotherapy and transplant patients; associations with HBV recovery, COVID-19 severity,
M. africanum TB protection [UniProt POLYMORPHISM; PMID:1675710, 1304173, 15994813, 21695215,
35102342]. These are downstream susceptibility/pleiotropy, not the core molecular function.

## Core function synthesis (for review)

1. Ca2+-dependent mannose/GlcNAc/fucose (carbohydrate) binding by the CRD — the apex MF.
   (GO:0005537 / GO:0030246 / GO:0120153)
2. Pattern-recognition receptor activity — recognizes microbial carbohydrate PAMPs.
   (GO:0038187), located in extracellular region (GO:0005576) and at pathogen/symbiont cell
   surface (GO:0106139).
3. Initiation of the complement lectin pathway via the MBL-MASP complex (member of a
   serine-type endopeptidase complex, GO:1905370), driving innate immune defense / opsonization.
   (GO:0001867 process; complex GO:1905370)

## Validation targets

- core_functions MF ids: GO:0005537, GO:0030246, GO:0120153, GO:0038187 (all verified MF, active).
- BP ids: GO:0001867, GO:0042742, GO:0045087 (verified, active).
- CC/location ids: GO:0005576 extracellular region (verified CC); GO:0009986 cell surface.
- complex id: GO:1905370 serine-type endopeptidase complex (verified CC, is_a descendant of
  GO:0032991 protein-containing complex — appropriate for in_complex).

## Falcon integration (2026-06-21)

FutureHouse Falcon deep-research report generated 2026-06-21 (genes/human/MBL2/MBL2-deep-research-falcon.md,
template gene_research_go_focused_compat.md). Verified its claims against the primary literature.

Findings USED (corroborated, concordant with primary literature):
- Core MF = Ca2+-dependent carbohydrate binding; substrate specificity D-mannose / GlcNAc / L-fucose /
  glucose, discriminating against D-galactose (consistent with C-type-lectin 3'/4'-OH coordination).
- Domain architecture (N-terminal Cys-rich + collagen-like + neck/coiled-coil + CRD) and oligomerization
  (multimers of homotrimers; higher-order assembly required for full activity); disease variants impair
  oligomerization (Larsen 2004 J Biol Chem, real DOI). Reinforces my oligomer/macropattern proposed term.
- Core BP = lectin-pathway complement activation, innate defense, opsonization; MBL-MASP1/2/3 complexes.
- Explicitly flags cytoplasm / cytosol / nucleus / synapse / apoptosis-execution / pyroptosis / neuronal /
  developmental roles as UNSUPPORTED, high-risk. (None of these are in the MBL2 GOA, so no action needed,
  but this independently supports my REMOVE of multivesicular body and surfactant homeostasis as off-target.)
- Apoptotic-cell clearance (Nauta 2004 J Immunol) noted as a context-specific role — consistent with UniProt
  RN[18] PubMed:14515269; not present in the current GOA so not annotated, recorded here as context.

Falcon citations checked: all 11 key references resolve to real, peer-reviewed published papers with valid
DOIs (Takahashi 2006, Jack 2001, Dobó 2024, Yongqing 2012, Larsen 2004, Cedzyński 2023, Mu 2020, Zhou 2016,
Andrade 2024, Bayarri-Olmos 2024, Nauta 2004). No preprint-only or unresolvable-PMID claims were found.

Findings NOT used / treated with caution:
- The report's own citation keys (e.g. "mu2020...", "nauta2004...") are not PMIDs and several of these papers
  are not in our publications/ cache, so I did NOT add them as YAML supporting_text references (which require a
  verbatim cached substring). The Falcon report itself is cited as a file: reference with a verbatim quote, and
  flagged MEDIUM relevance / VERIFIED in reference_review.
- Mu 2020 (calreticulin/opsonophagocytosis) is in an "early vertebrate" (teleost) model — cross-species; used
  only as context, not to drive a human MBL2 annotation.
- No new GO annotations were created solely on Falcon's say-so; every accepted/added term is grounded in the
  primary literature and verified GO IDs.

## Review outcome summary (2026-06-21)

- Verdict distribution across 79 existing annotations: ACCEPT 33; KEEP_AS_NON_CORE 16; MARK_AS_OVER_ANNOTATED 26;
  REMOVE 3; MODIFY 1.
- Downgraded all 23 generic GO:0005515 "protein binding" IPI annotations (MARK_AS_OVER_ANNOTATED), plus the
  D-mannose-binding TAS miscited to the LBP paper, the proteolysis IDA (MBL is not a protease), and the
  signaling-receptor-binding IPI (an altered-self/CK1 ligand, not a signaling receptor), toward the informative
  carbohydrate-binding MF / complex-membership representation.
- 1 MODIFY: GO:0048306 calcium-dependent protein binding (PMID:35102342, SARS spike) ->
  GO:0120153 calcium-dependent carbohydrate binding (the spike interaction is glycan-mediated via the CRD).
- 3 REMOVE: GO:0005771 multivesicular body and GO:0043129 surfactant homeostasis (IBA over-propagation from
  surfactant-protein paralogs), and GO:0006979 response to oxidative stress (misattributes the host endothelial
  stress response to MBL, which merely recognizes the exposed CK1 ligand).
- Core functions: (1) Ca2+-dependent carbohydrate binding (GO:0120153); (2) D-mannose binding (GO:0005537);
  (3) pattern-recognition-receptor activity (GO:0038187) as part of the MBL-MASP serine-type endopeptidase
  complex (GO:1905370) driving the lectin pathway (GO:0001867) and innate defense (GO:0045087, GO:0042742).
- 1 proposed new term: "collectin oligomer carbohydrate-pattern recognition" (multivalent oligomer-dependent
  macropattern discrimination).
