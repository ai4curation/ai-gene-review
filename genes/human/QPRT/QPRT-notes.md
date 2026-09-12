# QPRT (Q15274) review notes

Gene: **QPRT** — quinolinate phosphoribosyltransferase; HGNC:9755; UniProt NADC_HUMAN, Q15274; human (NCBITaxon:9606); 297 aa; chromosome 16.

## Identity and enzymatic function

UniProt recommended name: **Nicotinate-nucleotide pyrophosphorylase [carboxylating]**, AltName **Quinolinate phosphoribosyltransferase [decarboxylating]** (QAPRTase/QPRTase), **EC 2.4.2.19** [file:human/QPRT/QPRT-uniprot.txt "RecName: Full=Nicotinate-nucleotide pyrophosphorylase [carboxylating]"], [file:human/QPRT/QPRT-uniprot.txt "AltName: Full=Quinolinate phosphoribosyltransferase [decarboxylating]"].

Catalytic activity (UniProt, EC 2.4.2.19, RHEA:12733):
`nicotinate beta-D-ribonucleotide + CO2 + diphosphate = quinolinate + 5-phospho-alpha-D-ribose 1-diphosphate + 2 H(+)` [file:human/QPRT/QPRT-uniprot.txt "Reaction=nicotinate beta-D-ribonucleotide + CO2 + diphosphate ="]. The physiological direction is quinolinate + PRPP -> nicotinate mononucleotide (NaMN) + CO2 + PPi; the decarboxylation makes the step essentially irreversible [PMID:17868694 "The decarboxylation which occurs along with the phosphoribosyl transfer 27 is essentially an irreversible step."].

GO catalytic term **GO:0004514 nicotinate-nucleotide diphosphorylase (carboxylating) activity** (OLS-verified current label; definition matches the UniProt/EC reaction exactly). This is the single, well-supported core molecular function. Supported by:
- IDA/EXP in multiple primary papers: enzymatic + kinetic characterization of recombinant hQPRTase [PMID:17868694 "Steady-state kinetic analysis of hQPRTase was carried out using a continuous UV-assay which monitored the appearance of product."], with km ~21-23 uM for QA.
- functional complementation: human cDNA rescued a QPRTase-defective (nadC) E. coli strain [PMID:9473669 "Introduction of the human cDNA into a QPRTase defective (nadC) E. coli strain brought about an abrupt increase in QPRTase activity and allowed the cells to grow in the absence of nicotinic acid."].
- crystal structure + inhibition kinetics [PMID:24038671].

Key catalytic/substrate-binding residues (from mutagenesis + structures): QA-binding site formed by R102* (from partner subunit), R138, K139, H159, R161, K171 [PMID:17868694 "In the hQPRTase structure, this surface is composed of R102*, R138, K139, H159, R161 and K171"]. R138Q, K139A/S, R161Q, K171A/S abolish activity [PMID:17868694 "The mutants R138Q, K139A, K139S, R161Q and K171A, K171S completely abolished hQPRTase activity."].

Mg2+ dependence: Reactome states the reaction is "strictly dependent on Mg2+ ions being present" [Reactome:R-HSA-197268 "Its activity is strictly dependent on Mg2+ ions being present."]. Note: UniProt does NOT annotate a discrete metal-binding site (all BINDING features are for quinolinate); magnesium binding is therefore a plausible but not GOA-supported MF and is listed only as a candidate, not asserted in core_functions.

## Quaternary structure

Type II PRTase; alpha/beta barrel fold; functional unit is a **hexamer formed by 3 homodimers** [file:human/QPRT/QPRT-uniprot.txt "Hexamer formed by 3 homodimers."], [PMID:17868694 "The human enzyme adopts a hexameric arrangement, which places the active sites in close proximity to each other."], [PMID:26805589 "human QPRT acts as a hexamer for cooperative reactant binding via three dimeric subunits"]. The active site sits at a dimer interface and requires the partner subunit (R102* is contributed in trans). N-terminal helix alpha1 (res ~1-12) stabilizes the hexamer; deleting it yields dimers [PMID:26805589]. This grounds the GO:1902494 "catalytic complex" (part_of, IDA) and GO:0042802 "identical protein binding" (homo-oligomer) annotations.

## Biological process / pathway

Final committed step of **de novo NAD+ biosynthesis from L-tryptophan** via the kynurenine pathway: QPRT converts quinolinate to NaMN, which then enters the common NAD+ salvage/de novo pathway [PMID:17868694 "to provide the de novo source of NAMN for NAD biosynthesis"], [PMID:24038671 "QPRT at the junction of two different pathways, that is, de novo NAD(+) biosynthesis and the kynurenine pathway of tryptophan degradation."]. UniProt PATHWAY: NAD(+) biosynthesis; nicotinate D-ribonucleotide from quinolinate: step 1/1 [file:human/QPRT/QPRT-uniprot.txt "Cofactor biosynthesis; NAD(+) biosynthesis; nicotinate D-"].

- **GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan** (TAS, Reactome) — most specific correct BP; CORE.
- **GO:0009435 NAD+ biosynthetic process** (IBA/IEA) — correct parent, less specific; keep as non-core (subsumed by GO:0034354).
- **GO:0034213 quinolinate catabolic process** (multiple IDA + IBA) — the same reaction viewed from the substrate side (QPRT consumes/detoxifies quinolinate). Correct and experimentally supported; CORE (detox role). QA is a potent endogenous excitotoxin, so QPRT's consumption of it is physiologically important [PMID:9473669 "Quinolinate acts as a most potent endogenous exitotoxin to neurons."], [PMID:3409840 "the excitotoxic and convulsant agent quinolinic acid (QUIN)"].

## Localization

Cytosolic enzyme.
- **GO:0005829 cytosol** (TAS, Reactome) — CORE location; consistent with a soluble cytosolic metabolic enzyme.
- **GO:0005737 cytoplasm** (IBA) — appears in UniProt DR GO list but NOT in the GOA TSV rows seeded here; broader parent of cytosol.
- **GO:0070062 extracellular exosome** (HDA, PMID:23533145) — high-throughput exosome/EPS-urine proteomics detection; a generic MS "found-in-exosome" annotation, not indicative of a functional extracellular role. KEEP_AS_NON_CORE (do not treat as a real localization for a cytosolic metabolic enzyme).

## Protein-protein interactions (bare "protein binding")

The IntAct/IPI GO:0005515 rows are individual binary interactions, not informative molecular functions:
- NLGN3 (Q9NZ94-2): Y2H screen for neuroligin-3 partners [PMID:25464930]; QPRT was one of 51 candidates validated in neuroblastoma cells/brain tissue [PMID:25464930 "including EEF1A1, FLNA, ITPRIP, CYP11A1, MT-CO2, GPR175, ACOT2, and QPRT, were further validated"]. Biological significance for QPRT function unclear.
- KRTAP10-8 (P60410), KRTAP1-1 (Q07627), ADAMTSL4 (Q6UY14-3): from the HuRI binary interactome map [PMID:32296183]. Keratin-associated proteins are common Y2H sticky/false-positive preys; no functional relevance to NAD metabolism.
Per curation policy, bare "protein binding" (GO:0005515) IPI is uninformative -> MARK_AS_OVER_ANNOTATED (never REMOVE an IPI). "identical protein binding" (GO:0042802) is meaningful here because QPRT is a homo-oligomer -> ACCEPT/KEEP_AS_NON_CORE.

## Other annotations

- **GO:0016763 pentosyltransferase activity** (IEA, InterPro2GO) — correct but a broad parent of the specific GO:0004514; MARK_AS_OVER_ANNOTATED / redundant with the specific MF.
- IBA/IEA duplicates of GO:0004514 and GO:0009435 — accept the phylogenetic MF; the pipeline IEA/IBA process terms are correct-but-general.

## Disease / physiology context (not for GO annotation directly)

QPRT activity is reduced in epileptic human brain tissue [PMID:3409840 "A specific reduction of QPRTase activity was observed in tissue primarily involved in the epileptic discharge"]. QPRT loss raises quinolinate, implicated in neurodegeneration (Huntington's, Alzheimer's, epilepsy, AIDS dementia) [PMID:26805589 "malfunction of QPRT increases QA levels, which is strongly involved in a series of severe neurodegenerative disorders including Huntington's disease, Alzheimer's disease, Epilepsia and AIDS dementia complex"]. Studied as a target in malignant glioma [PMID:26805589]. These are downstream/physiological and are captured biologically by the QA-catabolism and NAD-biosynthesis process terms.

## Core function summary

1. **GO:0004514** nicotinate-nucleotide diphosphorylase (carboxylating) activity (MF) — the catalytic quinolinate phosphoribosyltransferase activity.
2. Directed at BP **GO:0034354** 'de novo' NAD+ biosynthetic process from L-tryptophan and **GO:0034213** quinolinate catabolic process, in **GO:0005829** cytosol, as part of the hexameric catalytic complex (GO:1902494).
</content>
</invoke>
