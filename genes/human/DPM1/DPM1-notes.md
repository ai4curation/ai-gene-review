# DPM1 review notes

UniProtKB:O60762, human DPM1 (dolichol-phosphate mannosyltransferase subunit 1). 260 aa, chromosome 20. HGNC:3005. Glycosyltransferase 2 family (CAZy GT2, Pfam PF00535, InterPro IPR039528 DPM1-like). EC 2.4.1.83.

Deep research: falcon provider OUT OF CREDITS (HTTP 402) at time of review; no `-deep-research-falcon.md` produced. Review grounded in DPM1-uniprot.txt, seeded GOA, and cached publications/PMID_*.md (all cited PMIDs present; all abstract-only per `full_text_available: false`).

## Core biology (from UniProt + primary literature)

- **Function**: catalytic subunit of the dolichol-phosphate mannose (DPM) synthase complex. Transfers mannose from GDP-mannose to dolichol monophosphate to form Dol-P-Man. [UniProt FUNCTION; PMID:10835346]
  - Reaction (RHEA:21184, EC 2.4.1.83): di-trans,poly-cis-dolichyl phosphate + GDP-alpha-D-mannose = di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate + GDP. [UniProt CATALYTIC ACTIVITY]
- **Dol-P-Man** is the mannosyl donor for: GPI anchor synthesis, lumenal N-glycan mannose additions (ALG3/9/12 branch of the LLO precursor), protein O-mannosylation, and protein C-mannosylation. [PMID:10835346 "generates mannosyl donors for glycosylphosphatidylinositols, N-glycan and protein O- and C-mannosylation"; PMID:9535917; PMID:16280320]
- **Complex**: DPM1 (catalytic) + DPM2 + DPM3. DPM1 lacks a hydrophobic transmembrane domain (unlike yeast Dpm1p) and is tethered to the ER membrane by DPM3 via a C-terminal coiled-coil; DPM2 stabilizes DPM3 and enhances activity ~10x. [PMID:9535917 "lacking a hydrophobic transmembrane domain"; PMID:10835346; PMID:16280320; PMID:9724629]
  - ComplexPortal CPX-6268 "Dolichol-phosphate mannosyltransferase complex"; GO complex term GO:0033185 dolichol-phosphate-mannose synthase complex.
- **Localization**: ER membrane (peripheral/tethered by DPM3). [UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum; PMID:9724629; PMID:16280320]
- **Metal**: binds 1 divalent metal cation (Mg2+/Mn2+/Ca2+), by similarity to Q8U4M3. Multiple GDP-mannose BINDING residues; residue 120 also binds Mg2+/Mn2+. [UniProt COFACTOR/BINDING, ECO:0000250]

## Disease

- **DPM1-CDG / CDG type Ie (CDG1E)**, MIM 608799. Variants R92G, G152V (abolishes DPM3 interaction), S248P. Some patients have dystroglycanopathy-type congenital muscular dystrophy (O-mannosylation defect on alpha-dystroglycan). [PMID:10642597; PMID:10642602; PMID:15669674; PMID:23856421]

## Annotation review decisions (highlights)

- MF: GO:0004582 dolichyl-phosphate beta-D-mannosyltransferase activity = the core catalytic function. ACCEPT all (IBA, IEA, EXP, IGI, IDA). This is the exact current GOA label.
- BP core: GO:0180047 dolichol phosphate mannose biosynthetic process (IDA/ISS) = the most specific/direct BP (the DPM synthesis reaction). ACCEPT. GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IBA/TAS) and GO:0043048 dolichyl monophosphate biosynthetic process are broader/downstream; ACCEPT (upstream-of processes DPM feeds into). GO:0006506 GPI anchor biosynthetic process and GO:0035269 protein O-linked glycosylation via mannose = downstream pathways DPM feeds — KEEP_AS_NON_CORE (via upstream provision of Dol-P-Man mannosyl donor).
- CC: GO:0005789 ER membrane = correct primary location; ACCEPT. GO:0005783 ER (parent) ACCEPT/KEEP_AS_NON_CORE. GO:0033185 dolichol-phosphate-mannose synthase complex ACCEPT (IDA). GO:0016020 membrane = uninformative parent, MARK_AS_OVER_ANNOTATED. GO:0005634 nucleus (HDA, sperm-nucleus proteome) = spurious/contaminant, REMOVE (HDA proteomics artifact, contradicts well-established ER localization; not an experimental functional annotation).
- MF GO:0005515 protein binding IPI x7: bare, uninformative. DPM3 interaction (Q9P2X0) is functionally meaningful but the term is uninformative -> MARK_AS_OVER_ANNOTATED (do NOT remove per policy). Others (MEOX2/Q6FHY5, TDO2/P48775, Q9UNE7) are large-scale/interactome — MARK_AS_OVER_ANNOTATED.
- MF GO:0046872 metal ion binding (ISS, from Q8U4M3): supported by BINDING features (Mg2+/Mn2+ at res 120). KEEP_AS_NON_CORE (real but ancillary to the transferase MF).

## Interactor PMIDs (protein binding IPI)
- PMID:10835346 (Q9P2X0=DPM3): the defining complex paper — DPM1-DPM3 direct interaction. Meaningful but term uninformative.
- PMID:16280320 (Q9UNE7 in GOA line): DPM3 tethering paper.
- PMID:10944123 (Q9P2X0=DPM3): PIG-P / DPM2 GPI-GnT regulation paper (abstract does not describe a direct DPM1 binary interaction; IntAct-sourced).
- PMID:23856421 (Q9P2X0=DPM3): DPM1-CDG G152V abolishes DPM3 binding.
- PMID:25416956, 25910212, 32296183 (P48775=TDO2, Q6FHY5=MEOX2): large-scale binary interactome maps (HuRI/Rolland/Luck). Generic.
