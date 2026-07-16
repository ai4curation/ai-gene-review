# RABGGTA (Q92696) review notes

## Identity and family

RABGGTA encodes the alpha subunit of Rab geranylgeranyltransferase (RabGGTase / geranylgeranyltransferase
type II / GGTase-II). UniProt recommended name: "Geranylgeranyl transferase type-2 subunit alpha", EC 2.5.1.60
[file:human/RABGGTA/RABGGTA-uniprot.txt "RecName: Full=Geranylgeranyl transferase type-2 subunit alpha; EC=2.5.1.60"].

The protein belongs to the protein prenyltransferase subunit alpha family
[file:human/RABGGTA/RABGGTA-uniprot.txt "Belongs to the protein prenyltransferase subunit alpha family"].
It contains six PFTA (prenyltransferase alpha-subunit) repeats and five leucine-rich repeats (LRRs)
per the UniProt feature table (REPEAT features 44-241, 363-397 PFTA; 442-555 LRR), consistent with the
Pfam PPTA (PF01239, x5), LRR_1 (PF00560), and RabGGT_insert (PF07711) domains listed in the UniProt
cross-references.

## Core molecular function: Rab geranylgeranyltransferase (heterodimer with RABGGTB)

RabGGTase is a heterodimer; the alpha subunit (RABGGTA) pairs with the beta subunit RABGGTB (P53611) to
form the catalytic "component B" of the enzyme. Historically, Seabra et al. 1991 established that protein
farnesyltransferase (FTase) and (at the time) "geranylgeranyltransferase" share a common alpha subunit
[PMID:2018975 "We show here that the alpha subunit is shared with another prenyltransferase that attaches 20 carbon geranylgeranyl to Ras-related proteins."]. Note that the FTase/GGTase-I shared alpha subunit is FNTA;
RABGGTA is the distinct alpha subunit of the Rab-specific (type II) enzyme. The 1991 Cell paper predates
the molecular cloning distinction, and its GO annotations were curated to RABGGTA by PINC (see below).

The reaction transfers a geranylgeranyl moiety from geranylgeranyl diphosphate to cysteine(s) of Rab
substrates [file:human/RABGGTA/RABGGTA-uniprot.txt "Catalyzes the transfer of a geranylgeranyl moiety from"]; the CATALYTIC ACTIVITY block gives Rhea:RHEA:21240 and EC 2.5.1.60
[file:human/RABGGTA/RABGGTA-uniprot.txt "ChEBI:CHEBI:86021; EC=2.5.1.60;"].

Unlike FTase and GGTase-I, RabGGTase does NOT recognize its Rab substrate directly. The Rab must first be
presented to the enzyme by a Rab escort protein (REP; component A), CHM (REP1, P24386) or CHML (REP2). The
UniProt ACTIVITY REGULATION states this explicitly
[file:human/RABGGTA/RABGGTA-uniprot.txt "The enzymatic reaction requires the aid of a Rab"] and the SUBUNIT block describes the CHM:RGGT:Rab heterotrimer
[file:human/RABGGTA/RABGGTA-uniprot.txt "Heterotrimer composed of RABGGTA, RABGGTB and CHM; within this"].

## Double geranylgeranylation of Rab C-terminal cysteines (experimental)

Farnsworth et al. 1994 (PMID:7991565) is the primary experimental reference (UniProt EXP/IDA for the
catalytic activity). Using recombinant RabGGTase + REP + [3H]GGpp on Rab1A (-XXCC), Rab3A (-XCXC) and
Rab5A (-CCXX), they showed both C-terminal adjacent cysteines are geranylgeranylated
[PMID:7991565 "found that for each protein both C-terminal adjacent cysteines were geranylgeranylated"].
The Rab-specific enzyme was already recognized as distinct
[PMID:7991565 "Rab proteins are substrates of a unique Rab-specific geranylgeranyltransferase"].
Substrate motifs -XXCC / -XCXC / -CCXX match the UniProt FUNCTION statement (RAB1A, RAB3A, RAB5A, RAB7A).

## Location

RabGGTase is a soluble cytosolic enzyme. UniProt/GOA place it in cytoplasm (IBA) and cytosol (Reactome TAS).
The Reactome "plasma membrane" TAS annotations (R-HSA-6801089/6801101/6801109) come from pathway reactions
in which RABGGTA participates (e.g. p53 -> RABGGTA transcription; RGGT/CHM binding); RABGGTA itself is not a
plasma-membrane protein. The catalytic action delivers the geranylgeranyl anchor that lets Rab GTPases
localize to membranes, but the enzyme is cytosolic.

## Biological process

Rab protein geranylgeranylation / protein prenylation is the direct process (GO:0018344 protein
geranylgeranylation, ISS from rat ortholog Q08602). This modification anchors Rab GTPases to membranes and
is required for vesicular trafficking. The IBA "ER to Golgi vesicle-mediated transport" (GO:0006888) reflects
the downstream trafficking role that prenylated Rabs (e.g. Rab1A) support, propagated across the PANTHER
family; it is a downstream/pleiotropic consequence rather than the direct enzymatic function of RABGGTA.

## Disease link: choroideremia

Choroideremia (X-linked retinal degeneration) is caused by loss of the Rab escort protein REP1 (CHM gene),
i.e. deficiency of "component A" of Rab GGtransferase, NOT of RABGGTA (which is component B)
[PMID:8380507 "The mutant gene in human choroideremia ... encodes a protein that resembles component A of rat Rab GG transferase."],
[PMID:8380507 "Lymphoblasts from choroideremia subjects showed a marked deficiency in the activity of component A, but not component B, of Rab GG transferase."].
The "visual perception" (GO:0007601) TAS annotation on RABGGTA derives from this choroideremia paper
(PMID:8380507), which is about REP1/CHM function; visual perception is not a function of RABGGTA and this is
best treated as an over-annotation (indirect/disease-context, curated by PINC in 2003).

## Interactions (IPI annotations)

The IPI "protein binding" annotations (GO:0005515) come from focused and high-throughput interaction studies.
The GOA WITH/FROM interactors are CHM/REP1 (P24386) and RABGGTB (P53611) — i.e. the two physiological
partners of RABGGTA (escort protein and catalytic beta subunit), consistent with the UniProt INTERACTION
block [file:human/RABGGTA/RABGGTA-uniprot.txt "Q92696; P24386: CHM; NbExp=7; IntAct=EBI-9104196, EBI-2515129;"],
[file:human/RABGGTA/RABGGTA-uniprot.txt "Q92696; P53611: RABGGTB; NbExp=10; IntAct=EBI-9104196, EBI-536715;"].
- PMID:21905166 (Esposito 2011): CHM/REP1 (P24386) — a choroideremia REP1 missense variant p.H507R prevents
  REP1 binding to RabGGTase [PMID:21905166 "a missense variant that prevents the binding of REP1 with Rab geranylgeranyl transferase"].
- PMID:28514442 (BioPlex/Huttlin 2017): CHM (P24386) and RABGGTB (P53611), AP-MS.
- PMID:31209342 (Kuchay 2019, GGTase3): WITH RABGGTB (P53611). This paper is about a NEW prenyltransferase
  GGTase3 = PTAR1 + RabGGTB; RABGGTB is the shared beta subunit. The interaction captured here is the
  RABGGTA-RABGGTB dimer context [PMID:31209342 "an orphan prenyltransferase α-subunit, PTAR1, and the catalytic β-subunit of GGTase2, RabGGTB"].
- PMID:32296183 (HuRI/Luck 2020): RABGGTB (P53611), Y2H binary interactome.
- PMID:33961781 (BioPlex 3.0/Huttlin 2021): CHM (P24386) and RABGGTB (P53611).
- PMID:35271311 (OpenCell 2022): CHM (P24386) and RABGGTB (P53611), endogenous tagging + IP-MS.
- PMID:40205054 (Schaffer 2025, multimodal cell maps): CHM (P24386) and RABGGTB (P53611).

All are physiologically meaningful (escort protein + beta subunit), but bare "protein binding" is
uninformative. These are MARK_AS_OVER_ANNOTATED per curation policy for bare GO:0005515 IPI; the informative
functional content (heterodimer with RABGGTB; escort-protein-mediated substrate presentation via CHM) is
captured in core_functions via in_complex GO:0005968 and small GTPase binding.

## Other annotations

- GO:0008270 zinc ion binding (IEA InterPro, IPR009087/IPR036254). The RabGGTase active site does contain a
  catalytic zinc, but structural/biochemical data place the catalytic zinc coordination on the beta subunit
  (RABGGTB), not the alpha subunit. The InterPro signature here maps to the alpha-subunit insert domain, so
  a zinc-binding MF on RABGGTA is questionable. Marked as over-annotated (not removed; leave IEA in place but
  flag). Kept conservative.
- GO:0004661 (protein geranylgeranyltransferase activity) and GO:0008318 (protein prenyltransferase activity)
  are correct but LESS SPECIFIC parents of GO:0004663 (Rab geranylgeranyltransferase activity), which is the
  precise MF. GO:0004661 IEA (Rhea GO_REF:0000116) and IEA InterPro GO:0008318 -> MODIFY toward GO:0004663.
  The EXP annotation to GO:0004661 (PMID:7991565) -> MODIFY to GO:0004663 (experimental, cannot REMOVE).

## Core function summary

Molecular function: contributes_to Rab geranylgeranyltransferase activity (GO:0004663) as the alpha subunit
of the Rab-protein geranylgeranyltransferase complex (GO:0005968); presents/binds Rab small GTPases
indirectly via the escort protein CHM (small GTPase binding GO:0031267).
Biological process: protein geranylgeranylation (GO:0018344) of Rab GTPases, anchoring them to membranes for
vesicular transport.
Location: cytosol (GO:0005829).
