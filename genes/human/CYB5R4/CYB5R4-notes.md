# CYB5R4 (NCB5OR / b5+b5R) review notes

UniProt: Q7L1T6 (NB5R4_HUMAN), 521 aa, EC 1.6.2.2. Gene synonym NCB5OR.

## Identity and domain architecture
- Multidomain redox enzyme: an N-terminal CS/Hsp20-like (p23_NCB5OR) domain, a cytochrome b5-like heme-binding domain, and a C-terminal FAD-dependent cytochrome-b5-reductase (FNR-type FAD + NAD-binding) module. UniProt domains: Cytochrome b5 heme-binding (54-130), CS (165-256), FAD-binding FR-type (273-385) [file:human/CYB5R4/CYB5R4-uniprot.txt].
- "First example of an animal flavohemoprotein containing cytochrome b5 and cytochrome b5 reductase domains" [PMID:15131110 "NCB5OR is the first example of an animal flavohemoprotein containing cytochrome b5 and cytochrome b5 reductase domains"].
- Binds heme (axial residues His-89, His-112), FAD, and NAD(P)H prosthetic groups; lacks a membrane anchor [PMID:10611283 "b5+b5R also has binding motifs for heme, FAD, and NAD(P)H prosthetic groups but no membrane anchor"].
- Recombinant protein contains stoichiometric amounts of heme and FAD; six-coordinate low-spin heme by resonance Raman [PMID:15131110 "Recombinant NCB5OR is soluble and has stoichiometric amounts of heme and flavin adenine dinucleotide"].

## Catalytic activity / molecular function
- EC 1.6.2.2 NADH-cytochrome b5 reductase; Rhea RHEA:46680: 2 Fe(III)-[cytochrome b5] + NADH = 2 Fe(II)-[cytochrome b5] + NAD+ + H+ [file:human/CYB5R4/CYB5R4-uniprot.txt].
- NAD(P)H oxidoreductase: can be reduced by NAD(P)H, reduces cytochrome c, methemoglobin, ferricyanide in vitro [PMID:15131110 "reduces cytochrome c, methemoglobin, ferricyanide, and molecular oxygen in vitro"; PMID:10611283 "The recombinant b5+b5R protein can be reduced by NAD(P)H ... cytochrome c reduction in vitro"].
- Redox potential at the heme center is -108 mV [PMID:15131110 "The redox potential at the heme center of NCB5OR is -108 mV"].

## Superoxide / oxidase activity — conflicting evidence
- 1999 paper proposed it as an NAD(P)H oxidase, observing superoxide production with air and excess NAD(P)H and proposed it as a candidate oxygen sensor [PMID:10611283 "demonstrated by superoxide production in the presence of air and excess NAD(P)H ... a plausible candidate oxygen sensor"].
- 2004 paper revised this: both full-length and truncated NCB5OR produce superoxide only with very slow turnover (kcat ~0.05 and ~1 s-1) and concluded it preferentially reduces substrates rather than transferring electrons to O2, and is therefore NOT an NAD(P)H oxidase for superoxide production [PMID:15131110 "these data suggest that endogenous NCB5OR is a soluble NAD(P)H reductase preferentially reducing substrate(s) rather than transferring electrons to molecular oxygen and therefore not an NAD(P)H oxidase for superoxide production"].
- This is the basis for the GOA NOT annotation on GO:0016174 (NAD(P)H oxidase H2O2-forming activity) from PMID:15131110, while the positive GO:0016174 annotation from PMID:10611283 represents the superseded earlier interpretation.

## Localization
- Soluble protein, no membrane anchor [PMID:10611283 "no membrane anchor"; file:human/CYB5R4/CYB5R4-uniprot.txt "Note=Soluble protein"].
- 1999: cytosolic, perinuclear space localization in COS-7 cells [PMID:10611283 "confocal microscopy revealed a cytosolic localization at the perinuclear space"].
- 2004: colocalizes with calreticulin (ER marker) by subcellular fractionation and confocal microscopy [PMID:15131110 "we show that NCB5OR colocalizes with calreticulin, a marker for endoplasmic reticulum"]. UniProt subcellular location: Endoplasmic reticulum.

## Physiological role
- UniProt FUNCTION: involved in ER stress response; protects pancreatic beta-cells against oxidant stress, possibly by limiting ROS buildup [file:human/CYB5R4/CYB5R4-uniprot.txt].
- Ncb5or-null mouse: diabetes/lipoatrophy phenotype motivates the beta-cell protection model (cited by PMID:15131110 framing).
- Widely/ubiquitously expressed across human tissues [PMID:10611283 "expressed at similar levels in all tissues and cell lines"; PMID:15131110 "widely expressed in human tissues"].

## GOA annotation assessment summary
- Core MF: GO:0004128 cytochrome-b5 reductase activity acting on NAD(P)H (IDA PMID:10611283; also IBA/IEA/TAS) — ACCEPT. GO:0016653 oxidoreductase acting on NAD(P)H heme protein acceptor (IDA PMID:15131110) — ACCEPT. GO:0020037 heme binding — ACCEPT. GO:0090524 (acting on NADH) and GO:0016491 (oxidoreductase activity) — correct but redundant/general → KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- GO:0016174 NAD(P)H oxidase H2O2-forming activity: NOT|enables (PMID:15131110) ACCEPT (negated, correct); positive enables (PMID:10611283) REMOVE — superseded/refuted.
- Localization: GO:0005783 ER (IDA PMID:15131110) ACCEPT; GO:0005789 ER membrane (TAS Reactome) — protein is soluble/no membrane anchor → MARK_AS_OVER_ANNOTATED; GO:0048471 perinuclear region of cytoplasm (IDA PMID:10611283) ACCEPT/KEEP_AS_NON_CORE.
- BP: GO:0072593 ROS metabolic process (IDA), GO:0006801 superoxide metabolic process (IDA/IBA) — supported by in vitro superoxide/ROS data; ACCEPT/KEEP. GO:0003032 detection of oxygen (NAS PMID:10611283) — based on the superseded oxygen-sensor hypothesis → MARK_AS_OVER_ANNOTATED. 
- ISS transfers from mouse ortholog Q3TDX8 (GO_REF:0000024): GO:0030073 insulin secretion, GO:0042593 glucose homeostasis, GO:0048468 cell development — phenotype-driven (Ncb5or-null mouse) → KEEP_AS_NON_CORE. GO:0046677 response to antibiotic — implausible/spurious ISS transfer → REMOVE/MARK_AS_OVER_ANNOTATED.
- GO:0015701 bicarbonate transport (TAS Reactome R-HSA-1237044, "Erythrocytes take up carbon dioxide and release oxygen") — CYB5R4 is not a bicarbonate transporter; pathway-context artifact → MARK_AS_OVER_ANNOTATED.

## Proposed new terms
- GO:0050660 flavin adenine dinucleotide binding — well supported (stoichiometric FAD; FAD-binding domain) but absent from GOA.
