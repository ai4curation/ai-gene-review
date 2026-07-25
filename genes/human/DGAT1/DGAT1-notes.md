# DGAT1 (human) — gene review notes

UniProt: O75907 (DGAT1_HUMAN), 488 aa. HGNC:2843. EC 2.3.1.20 (DGAT), EC 2.3.1.76 (retinol O-fatty-acyltransferase). Gene MIM 604900; disease MIM 615863 (DIAR7).

## Core identity and function

DGAT1 = **diacylglycerol O-acyltransferase 1**, a multi-pass endoplasmic-reticulum membrane enzyme of the **membrane-bound O-acyltransferase (MBOAT) family** (Pfam PF03062 MBOAT; sterol O-acyltransferase / ACAT subfamily) that catalyzes the **terminal and only committed step of triacylglycerol (TAG) synthesis**: acyl-CoA + 1,2-diacyl-sn-glycerol -> triacyl-sn-glycerol + CoA (Rhea:RHEA:10868, EC 2.3.1.20).

- [file:human/DGAT1/DGAT1-uniprot.txt "Catalyzes the terminal and only committed step in"] triacylglycerol synthesis by using diacylglycerol and fatty acyl CoA as substrates (FUNCTION comment; supported by PubMed:16214399, 18768481, 28420705, 32433610, 32433611, 9756920).
- Original cloning of a DGAT: [PMID:9789033 "Acyl CoA:diacylglycerol acyltransferase (DGAT, EC \n2.3.1.20) catalyzes the terminal and only committed step in triacylglycerol \nsynthesis, by using diacylglycerol and fatty acyl CoA as substrates."] (mouse ortholog; established the enzyme family; DGAT1 = human ARGP1 from PMID:9756920).
- Human DGAT1 was originally described as "ACAT-related gene product 1 (ARGP1)": [PMID:9756920 "ARGP1, unlike any other member of \nthis multigene family, possesses a predicted diacylglycerol binding motif \nsuggesting that it may perform the last acylation in triglyceride biosynthesis."]

## Structure (2020 cryo-EM)

Two Nature 2020 cryo-EM structures established the mechanism, topology, and oligomeric state:
- [PMID:32433610 "Each DGAT1 protomer has \nnine transmembrane helices, TM1–9"] and the MBOAT fold "forms a hollow chamber in the membrane that encloses highly conserved catalytic residues."
- Active site His415 (and Glu416): [PMID:32433610 "Mutations to active site residues, His415 and Glu416, abolish the enzymatic activities"].
- Oligomeric state: [PMID:32433610 "DGAT1 can exist as either a homodimer or a homotetramer and the \ntwo forms have similar enzymatic activity."] Basis for the IPI GO:0042802 identical protein binding annotations (self-interaction, homo-oligomer).
- [PMID:32433611 "DGAT1 has a broader acyl-acceptor substrate specificity"] than DGAT2 — the molecular basis for DGAT1's secondary acyltransferase activities.

## Broad acyl-acceptor specificity (secondary activities — real but non-core)

DGAT1 esterifies acceptors beyond DAG. These are genuine biochemical activities but are NOT the defining/core physiological function (TAG synthesis):

- **Retinol -> retinyl ester** (ARAT; EC 2.3.1.76, GO:0050252): [PMID:16214399 "DGAT1 appears to have the highest specific activity"] among TAG-synthesis enzymes for the ARAT reaction; "approximately 64% of total retinyl ester formation occurs via \nDGAT1/ARAT" in Caco-2 cells. In skin, DGAT1 is the major ARAT maintaining retinoid homeostasis (UniProt FUNCTION).
- **Monoacylglycerol acyltransferase (MGAT)** — 2-acylglycerol O-acyltransferase activity (GO:0003846, Rhea:37911/38071). UniProt: "acyl CoA:monoacylglycerol acyltransferase (MGAT)" activity.
- **Long-chain-alcohol O-fatty-acyltransferase / wax synthase** (GO:0047196, Rhea:38167/38171) — "wax monoester and wax diester synthases (By similarity)".
- **Ether-lipid (monoalkylglycerol) acylation**: [PMID:28420705 "DGAT1 is the predominant enzyme responsible for the \nintracellular synthesis of MADAG in this model system"] — DGAT1 uses 1-monoalkylglycerol as an acyl acceptor to make monoalkyl-monoacylglycerol/monoalkyl-diacylglycerol. Supports GO:0006640 monoacylglycerol biosynthetic process (IDA).

## Localization

Endoplasmic reticulum membrane, multi-pass. [file:human/DGAT1/DGAT1-uniprot.txt "Multi-pass membrane protein"]; UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane". 9 TM helices; N-terminus cytosolic, C-terminus luminal (PMID:32433610/32433611). Reactome ER-membrane TAS annotations (R-HSA-1482889, R-HSA-75900) are the correct compartment. GO:0005886 plasma membrane and GO:0035579 specific granule membrane (both Reactome TAS via the "Neutrophil degranulation" bulk proteomic pathway, R-HSA-6799350) are NOT the physiological site of DGAT1 action and are over-annotations of an ER enzyme.

## Physiology / disease

- Essential for **intestinal dietary fat absorption** ([PMID:32433610 "its \nactivity is essential for dietary fat absorption"]); expressed highly in small-intestine epithelium (UniProt; HPA "Tissue enhanced (intestine)").
- Liver fat storage; mammary/milk fat; may contribute to **VLDL assembly** ([PMID:15308631 "Overexpression of human DGAT1 in rat hepatoma McA-RH7777 cells resulted in \nincreased synthesis, cellular accumulation, and secretion of TG."] — this is overexpression, not a physiological requirement; supports IMP GO:0034379 VLDL particle assembly and GO:0006869 lipid transport, but note the effect is via TG loading, upstream/positive-effect qualifier).
- **DIAR7** (diarrhea 7, protein-losing enteropathy type; MIM 615863): biallelic loss-of-function causes a congenital diarrheal disorder (UniProt DISEASE; PubMed:23114594, 30237576).
- Host factor for HCV: DGAT1 recruits HCV core/NS5A to lipid droplets ([PMID:23420847 "DGAT1 forms a complex with NS5A and core and facilitates the interaction between both \nviral proteins."]) — basis for the GO:0005515 protein binding (IPI) annotation (interaction with viral NS5A PRO_0000045602 of Q99IB8). Not a core cellular function; keep as protein-binding evidence only.

## Annotations attributed to papers about other enzymes (do NOT remove — experimental)

- **PMID:18458083** (LPEAT2 / AYTL3) and **PMID:18238778** (AGPAT6 / GPAT4): the cached abstracts are about *different* acyltransferases. GOA carries DGAT1 GO:0004144 (IDA, MGI) and GO:0019432 (IDA) from these. Almost certainly DGAT1 was assayed as a positive control in the full text. Per policy, experimental (IDA) annotations are not removed on the basis of the abstract topic; the assigned function (DGAT / TAG synthesis) is DGAT1's true core function, so ACCEPT (deferring to curator) rather than second-guessing. Full text not in cache.

## Term-level judgments (summary)

- Core MF: GO:0004144 diacylglycerol O-acyltransferase activity (multiple EXP/IDA + IBA/IEA/TAS) — ACCEPT.
- Core BP: GO:0019432 triglyceride biosynthetic process (IDA/IBA + IEA) — ACCEPT.
- Core CC: GO:0005789 endoplasmic reticulum membrane (ISS/IBA/TAS/IEA) — ACCEPT.
- Secondary MF (KEEP_AS_NON_CORE): GO:0050252 retinol O-fatty-acyltransferase (EXP/IEA), GO:0003846 2-acylglycerol O-acyltransferase (IEA), GO:0047196 long-chain-alcohol O-fatty-acyltransferase (IEA).
- GO:0004806 triacylglycerol lipase activity (IEA, RHEA:38379): a Rhea-direction artifact — the mapped reaction is DAG + free fatty acid -> TAG (esterification), the reverse of physiological TAG hydrolysis; the "lipase" label misrepresents DGAT1. MARK_AS_OVER_ANNOTATED.
- GO:0016747 / GO:0016746 acyltransferase (general parent MF, IEA/TAS): ACCEPT as correct-but-general parents (do not over-annotate the gene's own true MF branch).
- GO:0005886 plasma membrane, GO:0035579 specific granule membrane (Reactome TAS, neutrophil degranulation): MARK_AS_OVER_ANNOTATED — wrong compartment for an ER enzyme.
- GO:0034379 VLDL particle assembly, GO:0006869 lipid transport (IMP, overexpression): KEEP_AS_NON_CORE — indirect/context-dependent, from overexpression.
- GO:0042572 retinol metabolic process (IEA, inter-ontology from GO:0050252): KEEP_AS_NON_CORE.
- GO:0019915 lipid storage, GO:0055089 fatty acid homeostasis, GO:0035336 long-chain fatty-acyl-CoA metabolic process, GO:0046339 diacylglycerol metabolic process, GO:0046486 glycerolipid metabolic process, GO:0006641 triglyceride metabolic process, GO:0006640 monoacylglycerol biosynthetic process: downstream/related BP — ACCEPT the ones central to TAG metabolism (glycerolipid/TAG/DAG/lcFA-CoA), KEEP_AS_NON_CORE the peripheral ones (lipid storage, fatty acid homeostasis).
</content>
</invoke>
