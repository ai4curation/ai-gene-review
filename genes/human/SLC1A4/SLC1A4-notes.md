# SLC1A4 (ASCT1 / SATT / Neutral amino acid transporter A) — curation notes

UniProt: P43007 (SATT_HUMAN). HGNC:10942. Taxon: Homo sapiens (NCBITaxon:9606).
TCDB 2.A.23.3.1 (DAACS family). PANTHER PTHR11958:SF20. Pfam PF00375 (SDF).

## One-line function
Plasma-membrane, sodium-coupled **obligate antiporter (exchanger)** of small neutral
amino acids (L-/D-serine, L-alanine, L-threonine, L-cysteine, L-asparagine; weakly
proline/4-hydroxyproline), with a substrate-gated uncoupled anion conductance. A member
of the SLC1/DAACS family that also contains the glutamate transporters (EAATs) and ASCT2.
It is **mechanistically an exchanger, not a net symporter**, and it does **not** transport
the acidic amino acids (glutamate/aspartate) carried by the related EAATs.

## Transport mode (central to judging GO terms)
- ASCT1 is an electroneutral exchanger with negligible net amino acid flux
  [PMID:8910405 "an electroneutral exchanger that mediates negligible net amino acid flux"];
  it mediates "only homo- and heteroexchange of amino acids and is insensitive" to K+
  [PMID:8910405 "ASCT-1 mediates only homo- and heteroexchange of amino acids and is insensitive"].
- "ASCT proteins, in contrast, do not concentrate their substrates, but perform the
  obligatory exchange of the amino acid pools, although the transport is still coupled to Na+"
  [PMID:34630942 "perform the obligatory exchange of the amino acid pools"].
- Na+-coupled but no proton/K+ coupling, unlike EAATs
  [PMID:24808181 "amino acid exchange by the ASCTs does not require protons or the"].
- UniProt: "Sodium-coupled antiporter of neutral amino acids." (CC FUNCTION); keyword "Antiport".
- Family note: "Belongs to the dicarboxylate/amino acid:cation symporter (DAACS) (TC 2.A.23)
  family. SLC1A4 subfamily." — the *family* name contains "symporter" (true of the EAATs),
  but SLC1A4 itself is an exchanger/antiporter. => **GO:0015293 symporter activity (IEA from
  InterPro) is the wrong transport mode** for this member.

## Substrate scope (what IS and ISN'T transported)
- Transported (Na+-dependent exchange): L-serine, D-serine, L-alanine, L-threonine,
  L-cysteine, L-asparagine; weakly L-proline and trans-4-hydroxy-L-proline.
  - Original clones: alanine, serine, cysteine evoked Na+-dependent currents
    [PMID:8101838 "Superfusion of alanine, serine, and cysteine evoked sodium-dependent inward"];
    HeLa uptake of L-serine, L-alanine, L-threonine
    [PMID:8340364 "Expression of SATT cDNA in HeLa cells induced stereospecific uptake of L-serine,"].
  - Proline/hydroxyproline transport (lower Vmax; hydroxyproline high affinity)
    [PMID:14502423 "demonstrates for the first time the ability of ASCT1"; "K(0.5) was 33.2 +/- 4.3 microM"].
  - D-serine is a genuine substrate (homo/hetero-exchange)
    [PMID:27272177 "SLC1A4 (ASCT1) and SLC1A5 (ASCT2) mediate homo- and hetero-exchange of D-serine with"].
  - UniProt curated catalytic activities include L-cysteine exchange
    (Rhea:RHEA:84347 "L-cysteine(out) + L-alanine(in) + Na(+)(out)").
- NOT transported: L-glutamate, L-aspartate and related dicarboxylates
  [PMID:8340364 "radiolabeled L-cysteine, L-glutamate, or related dicarboxylates"];
  also not glutamine [PMID:34630942 "ASCT1 is not capable to transport glutamine"].

### Cystine vs cysteine (annotation/ontology issue)
The GOA rows use **GO:0015184 "L-cystine transmembrane transporter activity"** and
**GO:0015811 "L-cystine transport"**. L-cystine is the oxidized disulfide dimer, which is a
substrate of system xc− (SLC7A11), **not** ASCT1. The experiments actually assayed the
**monomer L-cysteine**, and UniProt curates L-cysteine (not cystine) as the catalytic
substrate. Resolution used in this review:
- Positive L-cystine MF/BP IDA rows (PMID:8101838, PMID:8910405) → MODIFY to
  **GO:0033229 L-cysteine transmembrane transporter activity** / **GO:0042883 L-cysteine transport**.
- The NOT|L-cystine rows (PMID:8340364): the paper reported no cysteine uptake in HeLa
  ("lack of mutual inhibition between serine and cysteine"), which is contradicted for
  cysteine by the Kavanaugh-lab oocyte work and UniProt catalytic activity; but read as
  literal cystine (dimer), ASCT1 genuinely does not transport cystine, so the NOT is retained
  (ACCEPT) and the discrepancy is noted.

## Glutamate/aspartate over-annotations (IBA/TAS/ISS/IEA)
- **GO:0005313 L-glutamate transmembrane transporter activity** (IBA GO_REF:0000033; TAS
  PMID:21757002), **GO:0015813 L-glutamate transmembrane transport** (IBA), **GO:0098712
  L-glutamate import across plasma membrane** (TAS PMID:21757002): glutamate is not an ASCT1
  substrate (direct human evidence PMID:8340364). The IBA glutamate rows rest on the broad
  SLC1 node (PANTHER:PTN000238242 / PTN002278999) whose donors are EAATs (P43003/SLC1A3/EAAT1,
  P43004/SLC1A2/EAAT2, P43005/SLC1A1/EAAT3, P48664/EAAT5, etc.). ASCT1 sits in the neutral-AA subfamily
  (PTN002632762) — the glutamate function was not inherited into this branch; this is
  propagation from the wrong subfamily. The TAS rows rest on PMID:21757002, an FXR/hepatic
  glutamine-glutamate metabolism paper that does **not** demonstrate glutamate transport by
  ASCT1. => glutamate transport rows REMOVE; glutamate homeostasis GO:0090461
  MARK_AS_OVER_ANNOTATED (indirect; ARBA-derived or resting on the same mis-classification).
- **GO:0015183 L-aspartate transmembrane transporter activity** and **GO:0140009 L-aspartate
  import** (IBA/ISS/IEA, mostly from mouse Slc1a4 O35874): aspartate is acidic/dicarboxylate,
  not an ASCT1 substrate (PMID:8340364 "related dicarboxylates" not transported) =>
  MARK_AS_OVER_ANNOTATED.

## Chloride / anion channel
Substrate-gated, thermodynamically uncoupled anion conductance (a shared SLC1 property),
permeability SCN− > NO3− > I− > Cl− [PMID:8910405 "thermodynamically uncoupled chloride
conductance"; UniProt "Displays sodium- and amino acid-dependent but uncoupled channel-like
anion conductance with a preference SCN(-) > NO3(-) > I(-) > Cl(-)"]. GO:0005254 chloride
channel activity (IDA) and GO:1902476 chloride transmembrane transport are genuine but
non-core (Cl− is actually the least permeant of the tested anions).

## Brain D-serine / L-serine homeostasis (physiological role)
- L-serine is synthesized in the brain (poor BBB permeability), confined to astrocytes, and
  shuttled to neurons by ASCT1 [PMID:26041762 "within the brain because of its poor
  permeability by the blood-brain barrier."; "The data underscore that ASCT1 is essential in"].
- ASCT1 regulates extracellular D-serine, the NMDA-receptor co-agonist
  [PMID:27272177 "SLC1A4 (ASCT1) may represent an important route of Na-dependent D-serine flux in"].
- UniProt FUNCTION: "In astrocytes at excitatory synapses, mediates electrogenic D-serine
  influx coupled to L-serine efflux and L-serine shuttling to neurons for de novo D-serine synthesis".
- Expression altered in schizophrenia/bipolar (correlative) [PMID:16897601 "The altered
  expression of ASCT-1 in neurons and astrocytes"]. This links ASCT1 to glutamatergic
  neurotransmission indirectly (via D-serine), a non-core role; "cognition" (IMP) rests on the
  disease phenotype.

## Disease
Biallelic LoF → Spastic tetraplegia, thin corpus callosum, progressive microcephaly
(SPATCCM, MIM:616657). Variants E256K (reduced Vmax, altered affinity), R457W (loss of
transport), L315fs, Y191*, W453*. Mutants retain plasma-membrane localization but lose
transport [PMID:26041762 "the mutations did not affect the protein level at the plasma
membrane but abolished or markedly"; "reduced L-serine transport for p.R457W and p.E256K
mutations, respectively."]. Structure: homotrimer, one-gate elevator mechanism, cryo-EM 4.2 Å
[PMID:34630942].

## Localization
- Core: plasma membrane (cell membrane), multi-pass. Multiple ACCEPT rows (IBA/IC/IEA/IMP/TAS).
- GO:0016020 membrane (HDA/IDA/IEA/NAS) → MODIFY to plasma membrane (transporter convention).
- Cell surface (HDA), extracellular exosome (HDA), melanosome membrane (EXP melanosome
  proteomics + SubCell IEA), dendrite / neuronal cell body / synapse (mouse IEA, neuronal
  expression) → KEEP_AS_NON_CORE.
- GO:0005813 centrosome (HPA IDA, GO_REF:0000052) and GO:0005882 intermediate filament
  (IEA/ISS from mouse) → MARK_AS_OVER_ANNOTATED: biologically implausible for a polytopic
  plasma-membrane transporter; single-method HPA immunofluorescence / propagated mouse
  annotation, uncorroborated.

## Protein binding (GO:0005515, IPI, PMID:36115835)
18 IntAct rows, all from a PDZ-domain quantitative fragmentomics interactome
(DLG1-4, MAGI1/2, GRIP1/2, PATJ, SCRIB, MPDZ, PDZK1, NHERF4/PDZD3, FRMPD2, LNX1/2,
APBA1/2, IL16, TJP1/ZO-1, GRID2IP). These bind the ASCT1 C-terminal class-I PDZ ligand
(...ESKESVL). Real interactions, but bare "protein binding" is uninformative and no specific
informative MF is established => REMOVE per protein-binding policy (removal does not imply the
interactions are false; they belong in scaffold/trafficking commentary, not as GO:0005515).

## BBB
GO:0150104 transport across blood-brain barrier (NAS, from general BBB reviews PMID:26590417,
PMID:30280653 — neither names SLC1A4-specific BBB transport). ASCT1 is an obligate exchanger
(no net flux) and brain L-serine is made in situ because of poor BBB permeability
[PMID:26041762], so a net BBB-transport role is mechanistically implausible =>
MARK_AS_OVER_ANNOTATED.

## Core functions (summary)
1. Sodium-coupled neutral amino acid antiport/exchange across the plasma membrane
   (L-/D-serine, L-alanine, L-threonine, L-cysteine, L-asparagine).
2. Brain L-serine / D-serine homeostasis (astrocyte-neuron serine shuttle; regulation of the
   NMDA co-agonist D-serine).

## Update (2026-11-13): cystine/cysteine NOT rows + antiport MF (PR #6338 review)
- The NOT|L-cystine rows (GO:0015184 MF, GO:0015811 BP; UniProt, PMID:8340364) are kept ACCEPT
  (cystine dimer genuinely not transported), but the dimer-vs-monomer distinction is NOT asserted
  as coming from PMID:8340364 (which tested the monomer L-cysteine). The cystine↔cysteine term
  mis-mapping is now recorded as `review.source_defects` (WRONG_TERM, resource UNIPROT, REPOINT to
  GO:0033229 / GO:0042883), and the genuine conflict (cysteine-negative in HeLa vs cysteine-positive
  in oocytes PMID:8101838 + UniProt Rhea:RHEA:84347) is recorded as a `finding_review`
  (finding_status DISPUTED, superseded_by PMID:8101838) on the PMID:8340364 reference.
- GO:0015293 symporter activity (IEA/InterPro) is a lateral transport-mode correction → MODIFY to
  GO:0015297 antiporter activity (not MARK_AS_OVER_ANNOTATED).
- Added a core_functions entry for GO:0015297 antiporter activity (the obligate-exchange mechanism),
  mirroring ASCT2/SLC1A5.
- EAAT accession mapping corrected: P43003=SLC1A3=EAAT1, P43004=SLC1A2=EAAT2, P43005=SLC1A1=EAAT3.
- PMID:8340364 quotes re-cut to begin at "did not induce the transport of ..." so the negation is
  explicit; removed the PMID:34630942 glutamine quote from the GO:0005313 REMOVE row.
