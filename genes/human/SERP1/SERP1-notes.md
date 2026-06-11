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
