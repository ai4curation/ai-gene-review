# MS4A1 (CD20) review notes

## Setup / provenance

- `just fetch-gene human MS4A1` run beforehand (UniProt P11836, GOA tsv, stub review).
- `just fetch-gene-pmids human MS4A1` cached all 11 GOA PMIDs. Most are abstract-only
  (12920111, 18474602, 20458337, 2448768, 32792392, 3925015, 7684739); full text is
  available for 22664934, 23874341, 25416956, 32296183.
- Additional papers cached with `ai-gene-review fetch-pmid`: PMID:20038800 (human CD20
  deficiency), PMID:14688067 (mouse CD20 knockout), PMID:32079680 (CD20-rituximab
  cryo-EM), PMID:22615937 (CD20 palmitoylation; full text).
- Deep research: first `just deep-research-falcon human MS4A1` attempt failed with
  Edison API `429 Too Many Requests`; a retry was launched (see end of file for outcome).

## Identity and structure

- B-lymphocyte antigen CD20, founding member of the MS4A (membrane-spanning 4-domains
  subfamily A) family; four transmembrane segments, N and C termini cytoplasmic
  [PMID:7684739 "each CD20 monomer possesses four membrane spanning domains, and both the amino and carboxy termini reside within the cytoplasm"].
- Non-glycosylated four-pass protein with a large extracellular loop between TM3 and TM4;
  S-palmitoylated in B cells [PMID:22615937 "CD20 is a non-glycosylated four-pass transmembrane protein with a large extracellular loop located between the third and fourth transmembrane segments"].
- Cryo-EM: CD20 is a compact double-barrel dimer [PMID:32079680 "revealing CD20 as a compact double-barrel dimer bound by two RTX antigen-binding fragments (Fabs)"].
  Earlier co-IP work proposed tetramers [PMID:18474602 "we provide here direct evidence of CD20 homo-oligomerization into tetramers"]. The dimer seen by cryo-EM may be the
  unit of higher-order assemblies; tetramer claim remains biochemical.

## Expression

- B-cell restricted, from pre-B through mature B cells, lost on plasma cells
  [PMID:3925015 "expressed exclusively by B cells from the mid pre-B until the plasma cell stage of differentiation"];
  mouse CD20 likewise B-cell restricted [PMID:14688067 "CD20 expression was B cell restricted and was initiated during late pre-B cell development"].

## Localization

- Plasma membrane, constitutively in membrane rafts [PMID:12920111 "raft-associated tetraspan protein CD20"]; GFP-CD20 at plasma membrane of BJAB cells [PMID:23874341 "GFP-MS4A4A and GFP-MS4A8B, like GFP-CD20, appeared to be expressed at the plasma membrane"].
- Found in B-cell exosomes, co-IP with MHC II [PMID:20458337 "These include HSC71, HSP90, 14-3-3ɛ, CD20 and pyruvate kinase type M2 (PKM2)"].
- Tear-fluid proteomics (PMID:22664934) gives the "extracellular region" HDA; CD20 is
  an integral membrane protein with no signal sequence [PMID:2448768 "apparently lacks a signal sequence and contains three extensive hydrophobic regions"], so presence in
  tears likely reflects shed cells/vesicles -> over-annotation.

## Function: BCR-coupled calcium entry

- Ectopic CD20 generates a Ca2+ conductance [PMID:7684739 "Transfection of human T and mouse pre-B lymphoblastoid cell lines with CD20 cDNA and subsequent stable expression of CD20 specifically increased transmembrane Ca2+ conductance"].
- CD20 is a component of a store-operated Ca entry pathway activated by the BCR; siRNA
  knockdown reduces BCR-stimulated influx [PMID:12920111 "B cell receptor-stimulated influx was significantly reduced by downregulation of CD20 expression using short interfering RNA and also by cholesterol depletion"].
- Physically associates with IgM heavy/light chains of BCR; dissociates on BCR engagement,
  with recruitment of phosphoproteins and calmodulin-binding proteins
  [PMID:18474602 "Two major surface-labeled proteins that coprecipitated with CD20 were identified as the heavy and light chains of cell surface IgM"].
- Mouse knockout: reduced CD19-induced Ca2+ responses, otherwise largely normal B cells
  [PMID:14688067 "CD19-induced intracellular calcium responses were significantly reduced in CD20(-/-) B cells, with a less dramatic effect on IgM-induced responses"].
- Whether CD20 is itself a channel pore or a regulator/organizer of an SOC channel
  (e.g., ORAI/STIM-based) is unresolved -> no channel MF asserted; knowledge gap.

## Function: humoral immunity

- Human CD20 deficiency (CVID5): normal B-cell development, impaired T-independent antibody
  responses [PMID:20038800 "antibody formation, particularly after vaccination with TI antigens, was strongly impaired in the patient"].
- Mouse KO: T-dependent responses normal, B cell proliferation normal
  [PMID:14688067 "B cell development, tissue localization, signal transduction, proliferation, T cell-dependent antibody responses and affinity maturation were normal in CD20(-/-) mice"].
  -> B cell proliferation / differentiation annotations (based on anti-CD20 mAb
  perturbation, PMID:3925015) are not core; mAb crosslinking effects are not
  loss-of-function evidence.

## Interactions

- 30 IPI "protein binding" rows from HuRI/HI-II-14 Y2H (PMID:32296183, PMID:25416956);
  partners largely ER/membrane proteins (REEP2/4, TMX2, SLC10A1, HSD17B11...). These are
  uninformative for function; removed per project policy on GO:0005515.
- EGFR binding IEA (from rat Ensembl Compara) has no supporting evidence for B-cell CD20.

## Therapeutics (context, not GO)

- Target of rituximab, ofatumumab, obinutuzumab; type I vs II mAb mechanisms
  [PMID:32792392 "type II mAbs form terminal complexes that preclude recruitment of additional mAbs and complement components"].
