# CERK1 (CHITIN ELICITOR RECEPTOR KINASE 1, LysM RLK1, LYK1) — review notes

UniProt: A8R7E6 (CERK1_ARATH); locus AT3G21630; 617 aa precursor; EC 2.7.11.1.

## Protein architecture (from UniProt A8R7E6)
- Signal peptide 1-23; extracellular topo domain 24-232; single transmembrane helix 233-253; cytoplasmic domain 254-617.
- Three LysM domains in the ectodomain: LysM1 46-74 (degenerate), LysM2 108-140 (degenerate), LysM3 168-211.
- Chitin-binding residues 109-115 and 137-143 (ChEBI:CHEBI:17029).
- Protein kinase domain 322-594; ATP binding 328-336 and 349; active site (proton acceptor) Asp-441.
- Phosphosites: Ser-266, Ser-268, Ser-274, Thr-519 (PMID:20610395). N-glycosylation at Asn-40/52/102/123/152; disulfides 25-93, 29-155, 91-153 (PMID:22654057).
- Crystal structures 4EBY/4EBZ (ectodomain 25-230).

## Core molecular functions
- **Chitin binding** via LysM ectodomain. First direct in vitro binding shown with Kd ~82 nM [PMID:19951949 "we present the first evidence for direct binding of LysM RLK1 to chitin"]. Endogenous CERK1 is a major chitin-binding protein and all three LysM domains are needed [PMID:20610395 "the CERK1 ectodomain binds chitin and partially deacetylated chitosan directly without any requirement for interacting proteins and that all three LysM domains are necessary for chitin binding"]. Structure: binding mediated by one LysM and three NAG residues [PMID:22654057 "directly binds chitin through its lysine motif (LysM)-containing ectodomain (AtCERK1-ECD)"].
- **Chitosan binding** also direct [PMID:20610395 "binds chitin and partially deacetylated chitosan directly"].
- **Protein Ser/Thr kinase activity** of the intracellular domain; autophosphorylation + MBP kinase activity [PMID:18042724 "an intracellular Ser/Thr kinase domain with autophosphorylation/myelin basic protein kinase activity"]; autophosphorylated in vitro [PMID:19951949 "LysM RLK1-yEGFP was autophosphorylated in vitro"].
- **Transmembrane receptor kinase**: extracellular LysM + intracellular kinase [PMID:18042724 "CERK1 is a plasma membrane protein containing three LysM motifs in the extracellular domain and an intracellular Ser/Thr kinase domain"].
- **Homodimerization activity**: chitin octamer is a bivalent ligand driving dimerization required for activation [PMID:22654057 "a chitin octamer induces AtCERK1-ECD dimerization that is inhibited by shorter chitin oligomers"; "chitin-induced AtCERK1 dimerization is critical for its activation"]. Confirmed by structural review [PMID:22740685 "Receptor activation and immune signaling requires, however, ligand-induced CERK1 homodimerization"].

## Core biological process — chitin-triggered immunity
- Essential for chitin signaling; KO loses MAPK activation, ROS, gene expression [PMID:18042724 "The KO mutants for CERK1 completely lost the ability to respond to the chitin elicitor, including MAPK activation, reactive oxygen species generation, and gene expression"]. "Master switch" of the cascade.
- Required for chitin response and fungal resistance [PMID:18263776 "blocked the induction of almost all chitooligosaccharide-responsive genes and led to more susceptibility to fungal pathogens"].
- Signal transduction into cytoplasm via intracellular kinase [PMID:18042724 "the transduction of the signal into the cytoplasm via its intracellular serine/threonine kinase activity"].
- Downstream: phosphorylates RLCK PBL27 connecting to MPK3/6 [PMID:24750441 "PBL27...is an immediate downstream component of the chitin receptor CERK1"; PMID:27679653 title "connects chitin perception to MAPK activation"]. Also phosphorylates LIK1 [PMID:25036661 "LIK1 was directly phosphorylated by CERK1"].

## Receptor complex with LYK5 (important caveat)
- LYK5 is the high-affinity primary chitin receptor; binds chitin much more tightly than CERK1 and recruits CERK1 in a chitin-dependent complex [PMID:25340959 "AtLYK5 interacts with AtCERK1 in a chitin-dependent manner. Chitin binding to AtLYK5 is indispensable for chitin-induced AtCERK1 phosphorylation."]. CERK1 still binds chitin directly (above) but contributes the kinase/signal-output activity in vivo. LYK4 also contributes [PMID:22744984].

## Secondary / pleiotropic roles (kept as non-core)
- Bacterial perception: with LYM1/LYM3 senses peptidoglycan, restricts bacterial growth [PMID:22106285 "PGN sensing and immunity to bacterial infection in Arabidopsis thaliana requires three lysin-motif (LysM) domain proteins"; PMID:19816132 "plays an essential role in restricting bacterial growth on plants"].
- Abiotic stress: chitin signaling via CERK1 also encompasses salinity/heavy-metal tolerance [PMID:22461667 "chitin-induced signaling mediated by LysM RLK1 receptor is not limited to biotic stress response but also encompasses abiotic-stress signaling"].

## Regulation / host-pathogen (basis for REMOVE on generic protein binding)
- Negative regulation by U-box E3 ligases PUB12/PUB13 binding the autophosphorylated intracellular domain [PMID:29182677 "the ARM domains of PUB12 and its paralog PUB13 interacted with the intracellular domain of CERK1 in a manner that was dependent on its autophosphorylation"].
- Targeted for degradation by P. syringae effector AvrPtoB [PMID:19249211 "AvrPtoB ubiquitinates the CERK1 kinase domain in vitro and targets CERK1 for degradation in vivo"].
- Interacts with malectin-like/LRR-RLK IOS1 in PTI [PMID:27317676].

## Curation decisions summary
- ACCEPT (core MF/BP/CC): chitin binding (x4), chitosan binding, Ser/Thr kinase activity (x2), protein serine kinase activity, ATP binding, transmembrane receptor kinase activity (x2), homodimerization activity (x2), identical protein binding, autophosphorylation (x3), protein phosphorylation, plasma membrane (x4), cell surface PRR signaling, intracellular signal transduction, innate immune response (x2), cellular response to chitin (x2), response to chitin, defense response to fungus, detection of molecule of fungal origin (x2).
- MARK_AS_OVER_ANNOTATED: protein kinase activity (broad parent, IEA + IMP), kinase activity (broad), cellular response to oxygen-containing compound (uninformative ARBA).
- KEEP_AS_NON_CORE: response to bacterium, cellular response to molecule of bacterial origin, defense response to bacterium, detection of peptidoglycan (genuine bacterial/PGN role, secondary to core fungal-chitin function).
- REMOVE: all GO:0005515 "protein binding" (uninformative; PUB12, IOS1, PBL27 x2, LYK5, AvrPtoB); GO:0005576 extracellular region (ISM/AtSubP misprediction — protein is plasma-membrane-anchored, only the ectodomain faces apoplast).

No proposed_new_terms: existing terms (chitin binding, transmembrane receptor protein kinase activity, cell surface PRR signaling pathway, detection of molecule of fungal origin) already capture CERK1 biology well. OLS MCP was unavailable, so no unverified GO IDs were introduced.

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)

A Falcon deep-research report (`CERK1-deep-research-falcon.md`) was reviewed to augment the existing curation. Findings fully corroborated the prior decisions; no actions were weakened, no UNDECIDED items existed, and no NEW GO terms with verifiable IDs were warranted.

Key corroborating points (with verbatim support added as `file:` supported_by entries):
- Architecture/MF: "CERK1 is a single-pass membrane receptor with" three LysM motifs, TM/juxtamembrane, and intracellular Ser/Thr kinase; "CERK1 has intrinsic kinase activity with autophosphorylation and myelin basic protein phosphorylation in vitro." Reinforces GO:0004674, GO:0019199.
- Ligand specificity: "evidence supports preferential recognition of longer chitin oligomers, especially chitin heptamers/octamers, and GlcNAc8-driven receptor activation/dimerization"; "All three LysM domains are required for full chitin responsiveness." Reinforces GO:0008061 and homodimerization (GO:0042803; "Early model: CERK1 can homodimerize upon chitin binding.").
- Localization: "CERK1 is localized to the plasma membrane." Reinforces GO:0005886.
- Immunity/PRR/signaling: "CERK1 is a key PRR component required for chitin-induced PTI outputs including MAPK activation, ROS burst, and defense gene induction"; "Loss-of-function cerk1 mutants lose chitin-elicitor responses..."; downstream relay "Activated CERK1 signals through RLCK-VII kinases including PBL27, BIK1, and PBL19...". Reinforces GO:0045087, GO:0002752, GO:0032491, GO:0035556.
- Fungal defense quantification: "Disease phenotype against Alternaria brassicicola showed lesion size 1.37 ± 0.57 mm in cerk1-2 versus 1.14 ± 0.56 mm in Col-0." Reinforces GO:0050832.
- Bacterial (non-core): LysM partners "including LYM1/LYM3 for peptidoglycan signaling and LYM2 for plasmodesmal chitin responses." Reinforces non-core GO:0009617 etc.

Note: The report also surfaces additional biology not separately annotated in GOA (LYK5-CERK1-PBL27-SLAH3 stomatal-immunity module; phosphosite-specific ROS-vs-MAPK branching; PUB12/13 / EXO70B2 / CIPP1 receptor-turnover modules). Several phosphosite assignments are secondarily sourced (reviews/theses), so they were not used to introduce new annotations. These remain candidates for GO-CAM modeling rather than new term proposals.
