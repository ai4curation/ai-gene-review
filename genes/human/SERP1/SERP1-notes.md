# SERP1 / RAMP4 (Stress-associated endoplasmic reticulum protein 1) — review notes

UniProt: Q9Y6X1 (SERP1_HUMAN), 66 aa; AltName "Ribosome-attached membrane protein 4" (RAMP4). Single-pass ER membrane protein (TM 39-59), small tail-anchored-like topology.

## Core identity / function
- Small translocon-associated ER membrane protein that stabilizes/protects nascent membrane proteins at the Sec61 translocon during and after ER stress.
  - UniProt FUNCTION: "Interacts with target proteins during their translocation into the lumen of the endoplasmic reticulum. Protects unfolded target proteins against degradation during ER stress. May facilitate glycosylation of target proteins after termination of ER stress. May modulate the use of N-glycosylation sites on target proteins." [UniProt Q9Y6X1]
  - UniProt SUBUNIT: "Interacts with SEC61B, SEC61A1 and the SEC61 complex. Interacts with CANX." -> translocon-associated.
- Defining paper: [PMID:10601334 "Stress-associated endoplasmic reticulum protein 1 (SERP1)/Ribosome-associated membrane protein 4 (RAMP4) stabilizes membrane proteins during stress and facilitates subsequent glycosylation"]. Induced by ER stress/hypoxia; associates with the Sec61 translocon; stabilizes nascent membrane proteins during stress; facilitates their glycosylation after stress ends.
- Belongs to the RAMP4 family. Tightly linked to UPR (ER unfolded protein response).

## Annotation assessment
- GO:0005783 endoplasmic reticulum (IBA is_active_in; IEA; TAS PMID:10601334) — CORE localization/site of action, ACCEPT.
- GO:0005789 ER membrane (IEA, ISS, TAS Reactome) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA, ISS) — generic parent; KEEP_AS_NON_CORE.
- GO:0030968 ER unfolded protein response (IBA involved_in) — CORE biological process; SERP1 is stress-associated and acts during ER stress. ACCEPT.
- GO:0005840 ribosome (TAS PMID:10601334) — RAMP4 = "ribosome-associated membrane protein 4"; associates with the translocon/ribosome at the ER. ACCEPT as KEEP_AS_NON_CORE (the term "ribosome" is broad; it is ribosome/translocon-associated at the ER). Defensible TAS.
- GO:0009101 glycoprotein biosynthetic process (TAS PMID:10601334) — "facilitates subsequent glycosylation" / "modulate the use of N-glycosylation sites". KEEP_AS_NON_CORE (real but secondary/modulatory).
- GO:0036211 protein modification process (TAS PMID:10601334) — very general (parent of glycosylation). KEEP_AS_NON_CORE.
- GO:0007009 plasma membrane organization (TAS PMID:10601334) — weakly supported; SERP1 stabilizes nascent membrane proteins, indirectly affecting PM protein expression. KEEP_AS_NON_CORE / borderline. Keep as non-core (the paper showed effects on membrane-protein expression at the cell surface).
- GO:0005829 cytosol (TAS Reactome:R-HSA-9609921, SGTA tail-anchored protein) — SERP1 is an ER membrane protein; cytosol annotation from a TA-protein pathway context. KEEP_AS_NON_CORE (the cytosol-facing portion / pathway context). Defensible but not core; keep.
- GO:0005881 cytoplasmic microtubule (IDA PMID:23264731) — **PROBLEM**. PMID:23264731 is "MTR120/KIAA1383, a novel microtubule-associated protein" — entirely about MTR120/KIAA1383 (a ~120 kDa MT-associated protein), NOT SERP1/RAMP4. Full text is available and contains NO mention of SERP1/RAMP4/Q9Y6X1. SERP1 is a 66-aa single-pass ER membrane protein; cytoplasmic-microtubule localization is biologically implausible. This IDA is a mis-attribution. Action: REMOVE (full text read; wrong gene).
- GO:0005515 protein binding (IPI PMID:25416956 TMEM79; PMID:32296183 large HuRI set of membrane-protein partners) — bare protein binding; KEEP_AS_NON_CORE. The HuRI partners are largely nascent/membrane substrate proteins consistent with SERP1's translocon-substrate-stabilizing role, but the term itself is uninformative.

## Core function summary
SERP1/RAMP4 is a stress-induced, Sec61-translocon-associated single-pass ER membrane protein that stabilizes and protects nascent membrane/secretory proteins during ER stress and facilitates their N-glycosylation after stress resolves; functions in the ER unfolded protein response.

## Falcon deep-research findings (incorporated 2026-06)
- 2024 cryo-EM directly resolves RAMP4/SERP1 as a structural component of the Sec61 translocon: "a large proportion of translocon complexes contains RAMP4 intercalated into Sec61's lateral gate, widening Sec61's central pore and contributing to its hydrophilic interior" [PMID:38896445 abstract]. This upgrades the mechanistic basis for the translocon-associated, gating-modulating role (added to GO:0005783 IBA supported_by).
- The authors propose RAMP4 can stabilize an open-but-plugged Sec61 state and may act as a "surrogate signal peptide" after the substrate signal peptide is released; RAMP4 reported present in ~81% of non-MPT RTCs, ~85% of Sec61·TRAP·OSTA and ~53% of Sec61·TRAP RTCs [PMID:38896445, Falcon report Lewis pages 6-8]. (Quantitative occupancy figures from Falcon synthesis; structural localization verbatim-supported by abstract.)
- NOTE on citation: Falcon cited the bioRxiv preprint DOI 10.1101/2023.12.22.572959; the published version is eLife 2024, PMID:38896445, DOI 10.7554/eLife.95814 (PubMed-verified). Added the published PMID.
- SERP1 is a DENV-2 NS4B-interacting host factor; "A drastic increase (34.5-fold) in the SERP1 gene expression was observed in the DENV-2-infected or replicon-transfected Huh7.5 cells" and "SERP1 overexpression inhibited viral yields (37-fold)" [PMID:31461934 abstract]. Establishes ER-stress inducibility and an antiviral/proteostasis-protective role. Added as reference (HIGH relevance).
- In acute hepatic injury, "SERP1 regulated ERS via the GSK3beta/beta-catenin/TCF/LEF signaling pathway, thereby reducing inchoate acute hepatic injury"; SERP1 overexpression reduced GRP78/GRP94/CHOP, apoptosis and inflammation [PMID:35419615 abstract]. Cytoprotective ER-stress role; downstream/physiological readout. Added as reference (MEDIUM relevance).
- Gemmer & Forster 2020 translocon review provides authoritative family-level context: RAMP4/SERP1 is among ribosome-associated membrane proteins recovered with Sec61 translocon fractions [PMID:32019826]. Added as reference (MEDIUM).
- No existing actions/annotations were changed; additions are reference-level plus one supported_by id (PMID:38896445) on the GO:0005783 IBA. None of these papers are cached in publications/, so no paraphrased verbatim supporting_text was added.
