# SLC25A6 (ANT3 / ADP,ATP carrier protein 3) — review notes

UniProt: P12236 (ADT3_HUMAN). Gene: SLC25A6; synonyms AAC3, ANT3. HGNC:10992.
Species: Homo sapiens (NCBITaxon:9606). 298 aa. Located in pseudoautosomal region 1
(PAR1) of X and Y chromosomes; escapes X-inactivation.

## Core identity and function

SLC25A6 is one of the four human adenine nucleotide translocase (ANT) isoforms
(SLC25A4/ANT1, SLC25A5/ANT2, SLC25A6/ANT3, SLC25A31/ANT4), members of the
mitochondrial carrier (SLC25 / TC 2.A.29) family. ANT3 is the ubiquitously
expressed isoform.

Its core molecular function is an **ADP/ATP antiporter** (ATP:ADP antiporter
activity, GO:0005471) of the mitochondrial inner membrane: it exchanges matrix ATP
for cytosolic ADP, importing ADP for ATP synthesis by the F1Fo-ATP synthase and
exporting the newly made ATP to the cytosol.

- UniProt FUNCTION: "ADP:ATP antiporter that mediates import of ADP into the
  mitochondrial matrix for ATP synthesis, and export of ATP out to fuel the cell"
  [file:human/SLC25A6/SLC25A6-uniprot.txt].
- UniProt CATALYTIC ACTIVITY: "Reaction=ADP(in) + ATP(out) = ADP(out) + ATP(in)"
  (Rhea RHEA:34999) [file:human/SLC25A6/SLC25A6-uniprot.txt].
- It operates by an alternating-access mechanism, cycling between a
  cytoplasmic-open (c-state) and matrix-open (m-state) with a single
  substrate-binding site [file:human/SLC25A6/SLC25A6-uniprot.txt].
- Earliest sequence/identification: Cozens, Runswick & Walker 1989 characterized the
  human nuclear genes for the ADP/ATP translocase and describe the biochemical role:
  "It carries ATP from the matrix into the intermembrane space and transports ADP
  back." [PMID:2541251 "It carries ATP from the matrix into the intermembrane space
  and transports ADP back."]. (This paper is the NAS reference for GO:0005471; it is a
  gene/sequence paper, hence NAS not IDA.)
- The direct human ADP/ATP antiporter activity annotation is transferred by ISS from
  bovine ANT1 (UniProtKB:P02722) and human ANT2 (P48962) orthologs; the mechanistic
  detail (alternating access, c-/m-states, BKA/CATR inhibition) in UniProt is likewise
  "By similarity" from those characterized orthologs.

Topology: 6 transmembrane helices, 3 tandem mitochondrial-carrier (Solcar) repeats;
matrix and intermembrane-space facing loops; nucleotide carrier signature motif at
235-240 [file:human/SLC25A6/SLC25A6-uniprot.txt]. This is a transporter, NOT an
enzyme — no catalytic/EC MF should be assigned.

## Localization

- Mitochondrion inner membrane (GO:0005743), multi-pass membrane protein
  [file:human/SLC25A6/SLC25A6-uniprot.txt: "SUBCELLULAR LOCATION: Mitochondrion inner
  membrane"]. This is the authoritative, core location, supported by IBA, ISS, and
  Reactome TAS.
- High-throughput proteomics place it in mitochondrion (HDA PMID:20833797 muscle
  mitochondrial phosphoproteome; HTP PMID:34800366 high-confidence mito proteome) and
  in "membrane" (IDA PMID:27641616, which detects ANT3 at protein level in
  erythrocyte membranes — the basis of the UniProt "Membrane / May localize to
  non-mitochondrial membranes" note and TISSUE SPECIFICITY "Expressed in erythrocytes
  (at protein level)").
- Nucleus (GO:0005634, HDA PMID:21630459) comes from a **human sperm nucleus**
  proteome; ANT3 is a very abundant inner-membrane protein and is a classic
  contaminant in such fractionation studies. There is no functional evidence for a
  nuclear role; treat as over-annotation.

## Apoptosis / mitochondrial permeability transition pore (mPTP)

- ANT (including ANT3) is a regulatory component associated with the mitochondrial
  permeability transition pore complex (PTPC) that contributes to apoptosis; whether it
  is a pore-forming or purely regulatory component is unresolved.
  UniProt: "Also plays a key role in mPTP opening ... It is however unclear if
  SLC25A6/ANT3 constitutes a pore-forming component of mPTP or regulates it"
  [file:human/SLC25A6/SLC25A6-uniprot.txt].
- Influenza A PB1-F2 induces apoptosis via direct interaction with ANT3 (inner
  membrane) and VDAC1 (outer membrane) of the PTPC (Zamarin et al. 2005):
  [PMID:16201016 "the viral protein uniquely interacts with the inner mitochondrial
  membrane adenine nucleotide translocator 3 and the outer mitochondrial membrane
  voltage-dependent anion channel 1, both of which are implicated in the mitochondrial
  permeability transition during apoptosis."].
  Same paper on ANT3's biochemical role and conditional pore behavior:
  [PMID:16201016 "ANT3 is an inner mitochondrial membrane protein that functions as an
  antiporter catalyzing the exchange of ATP for ADP"].
- Because ANT3 is ubiquitous and shares this with the other ANT isoforms, the
  mPTP-complex membership (GO:0005757) and regulation-of-membrane-permeability
  (GO:0046902) annotations are IBA family-level inferences. They are biologically
  plausible for ANT3 but are NON-CORE relative to the transport function; retain as
  KEEP_AS_NON_CORE.

## Proton transport / uncoupling (context)

UniProt notes an additional H+-transport (uncoupling/thermogenesis) activity
transferred "By similarity" (CATALYTIC ACTIVITY: "Reaction=H(+)(in) = H(+)(out)",
RHEA:34979), based largely on Bertholet et al. 2019 (PMID:31341297) work on the ANT
family. There is no human-ANT3-specific GOA annotation for proton transport, so no
existing annotation covers it; it is noted here for completeness only.

## Protein interactions (bare "protein binding" GO:0005515, IPI)

Many GO:0005515 IPI annotations come from large-scale interactome / affinity-MS
studies deposited in IntAct (AP2B1, KRT31, LRRK2, LZTS2, MID2, MTUS2, NOTCH2NLA,
SLC25A4/ANT1, TEKT4, TRAF1, TRIM23, TRIP6, VDAC1, and viral PB1-F2). The cited
interactome papers (e.g. PMID:21516116, 25416956, 29128334, 29892012, 33961781,
40355756) are high-throughput maps that do not name SLC25A6/ANT3 in their
abstracts/cached text, and the LRRK2-focused papers (PMID:21370995, 24725412,
35266954) are about LRRK2 biology. "protein binding" is uninformative as a molecular
function; per curation policy these IPI annotations are kept but MARK_AS_OVER_ANNOTATED
(never removed), and none is a core function. The functionally meaningful interactions
(VDAC1, PB1-F2) are captured through the mPTP/apoptosis annotations instead.

## TIM23 translocase complex membership (GO:0005744)

GOA carries a TAS annotation (from PMID:2541251) placing ANT3 as part_of the TIM23
import translocase complex. ANT is a well-known SUBSTRATE / cargo of the carrier
(TIM22) import pathway, not a stable structural subunit of the TIM23 presequence
translocase. The 1989 Cozens paper is a gene-sequencing paper and does not assay
translocase-complex membership; this looks like a mis-mapped legacy TAS. UniProt's own
GO set does list "TIM23 ... translocase complex TAS:UniProtKB", so I retain it as
UNDECIDED / non-core rather than asserting removal, but flag it as likely
substrate-not-subunit.

## Summary of curation decisions

Core function:
- MF: GO:0005471 ATP:ADP antiporter activity
- BP: GO:1990544 mitochondrial ATP transmembrane transport + GO:0140021 mitochondrial
  ADP transmembrane transport (the antiport couples these)
- CC: GO:0005743 mitochondrial inner membrane

Non-core but retained (KEEP_AS_NON_CORE): mPTP complex (GO:0005757), regulation of
mitochondrial membrane permeability (GO:0046902), and the well-supported redundant
localization annotations.

Over-annotations (MARK_AS_OVER_ANNOTATED): all bare "protein binding" GO:0005515 IPI;
generic "membrane" GO:0016020; nucleus GO:0005634 (sperm-nucleus contaminant).

Generic IEA that duplicate specific terms are ACCEPTed where correct (transmembrane
transport GO:0055085) or KEEP as redundant.
