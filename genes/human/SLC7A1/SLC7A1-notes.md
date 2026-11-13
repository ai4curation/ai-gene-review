# SLC7A1 (CAT-1 / hCAT-1) curation notes

UniProt: P30825 (CTR1_HUMAN). HGNC: SLC7A1. Taxon: 9606.
Aliases: ATRC1, ERR, REC1L; "System Y+ basic amino acid transporter"; "Ecotropic
retroviral leukemia receptor homolog".

## Summary of function (synthesized)

SLC7A1/CAT-1 is the prototypic high-affinity, low-capacity **cationic (basic)
L-amino acid transporter** of the y+ system. It is a polytopic plasma-membrane
protein (14 predicted TM helices; UniProt FT TRANSMEM ×14) of the APC superfamily,
CAT (TC 2.A.3.3) family. It mediates **Na+-independent facilitated diffusion
(uniport)** of L-arginine, L-lysine and L-ornithine, and is **trans-stimulated**
(the substrate on the trans side accelerates exchange), but its core mode is
facilitative uniport, not obligate antiport or symport. It is widely expressed
("ubiquitous") except in adult liver.

Key kinetic / substrate facts:
- L-arginine: KM ~0.11 mM; transport demonstrated in Xenopus oocytes
  [PMID:9174363]; UniProt catalytic activity L-arginine(in)=L-arginine(out),
  ChEBI:32682.
- L-lysine: KM ~98-100 uM; saturable uptake in oocytes [PMID:10485994]; polarized
  basolateral uptake KM ~68 uM in MDCK [PMID:11891586]; ChEBI:32551.
- L-ornithine: siRNA knockdown reduced L-[14C]ornithine uptake ~47% in RPE cells
  [PMID:17197568]; UniProt catalytic activity ChEBI:46911.
- L-homoarginine: KM ~175 uM, a genuine lower-affinity substrate [PMID:28684763].
- L-histidine: transported by the hCAT family; the IDA annotation GO:0005290 cites
  [PMID:11591158], a paper that primarily characterizes hCAT-3 (SLC7A3). Histidine
  is only cationic at acidic pH and is a minor/secondary y+ substrate for CAT-1.

Provenance for the central claims:
- [PMID:9174363 "When expressed in Xenopus oocytes, hCAT-1 and hCAT-2B demonstrated transport properties consistent with y+"] and "hCAT-1 had a 3-fold higher substrate affinity and was more sensitive to trans-stimulation than hCAT-2B."
- UniProt CC:FUNCTION: "High-affinity, low capacity permease involved in the transport of the cationic amino acids (arginine, lysine and ornithine) in non-hepatic tissues." (ECO:0000269|PubMed:10485994, PubMed:9174363).
- [PMID:10485994 "hCAT-1 cRNA injection into Xenopus laevis oocytes stimulated saturable lysine uptake (K(m) approximately 100 microM)"].
- [PMID:28684763 "L-Homoarginine is a substrate of the human cationic amino acid transporters CAT1, CAT2A and CAT2B"].

## Localization

- Core location: plasma membrane (GO:0005886). UniProt SUBCELLULAR LOCATION: "Cell
  membrane; Multi-pass membrane protein." Proteomics IDA in RPE [PMID:28112518].
- Polarized epithelia: in MDCK cells hCAT-1 localizes **solely basolateral**
  [PMID:11891586 "confocal microscopy ... revealed localization of the transporter solely on the basolateral domain of the cell"]; apical uptake was negligible there.
  In human RPE, transporters are present on both apical and basolateral surfaces
  [PMID:31791063]. So apical/basal/basolateral rows are tissue-specific refinements
  (kept non-core).

## Virus receptor

The MOUSE ortholog mCAT-1 (Q09143) is the receptor for ecotropic murine leukemia
virus. The gene was originally cloned as a homolog of the murine ecotropic
retroviral receptor [PMID:1718082]. Human CAT-1 is a structural homolog; the
virus-receptor (GO:0001618) and "symbiont entry into host cell" (GO:0046718)
annotations on P30825 are IEA, propagated from the mouse ortholog, and concern a
mouse (non-human) pathogen. Kept as KEEP_AS_NON_CORE, out of core functions.
(Note: ecotropic MLV restriction is species-specific; this is a non-core,
non-human-pathogen capacity of the family.)

## Oligomeric state / complex

CAT-1 functions on its own (homo-oligomer); unlike the SLC7 light chains
(LAT1/LAT2, y+LAT1/2, b0,+AT etc.), it does **not** require SLC3A2/4F2hc or rBAT
heavy chains. The GO:0032991 "protein-containing complex" (part_of, IDA,
[PMID:28246125]) is from an IFITM3 affinity-purification/MS study (ZMPSTE24 paper);
that paper characterizes ZMPSTE24-IFITM complexes and does not define a
functional CAT-1 complex. "protein-containing complex" is an uninformative generic
CC term and CAT-1 is not an obligate heteromeric complex member → marked
MARK_AS_OVER_ANNOTATED.

UniProt SUBUNIT also records: interaction with TM4SF5 (arginine sensing / mTORC1,
[PMID:30956113]); and "By similarity" tissue-specific complexes with ASL, ASS1 and
NOS1/NOS3 channeling arginine to NO synthesis (arginine regeneration / citrulline-
NO cycle). These are individual interactions, not evidence for the generic
GO:0032991 row.

## Physiological context (participation test applied)

- T-cell proliferation [PMID:26449889]: CD3/CD28 activation induces hCAT-1; siRNA
  knockdown impairs arginine uptake and proliferation. CAT-1 **supplies arginine**;
  it does not itself execute cell-cycle/proliferation steps → the
  GO:0042102 (positive regulation of T cell proliferation, acts_upstream_of)
  annotation is a genuine but non-core upstream role (KEEP_AS_NON_CORE). Does not
  pass the participation test for a core process annotation.
- Blood-brain barrier transport [PMID:26590417, PMID:30280653] (NAS review
  articles): CAT-1 transports cationic amino acids across BBB endothelium — a
  tissue-specific context of its core transport activity (KEEP_AS_NON_CORE).
- Ornithine cytotoxicity in gyrate atrophy RPE [PMID:17197568]: CAT-1 mediates the
  ornithine uptake that drives cytotoxicity in OAT-deficient cells — supports
  ornithine transport MF/BP (core transport).

## Over-annotations / errors found

- GO:0098655 "monoatomic cation transmembrane transport" (ISS from mouse MGI:88117):
  **incorrect**. CAT-1 transports cationic (organic) *amino acids*, not monoatomic
  (inorganic/single-atom) cations. This looks like a mis-mapping of "cationic amino
  acid" to "monoatomic cation." → REMOVE.
- GO:0032991 protein-containing complex: over-annotation (see above).
- All GO:0005515 protein binding (IPI) rows: removed per protein-binding policy
  (uninformative; many from high-throughput interactome screens PMID:32296183,
  25416956, 28514442, 40205054, 40355756; and TM4SF5 PMID:30956113).

## Core functions

1. L-arginine transmembrane transporter activity (GO:0061459) → L-arginine import
   across plasma membrane (GO:0097638); substrate L-arginine (CHEBI:32682); PM.
2. L-lysine transmembrane transporter activity (GO:0015189) → L-lysine
   transmembrane transport (GO:1903401); substrate L-lysine (CHEBI:32551); PM.
3. L-ornithine transmembrane transporter activity (GO:0000064) → L-ornithine
   transmembrane transport (GO:1903352); substrate L-ornithine (CHEBI:46911); PM.
The unifying MF is basic/cationic amino acid transmembrane transporter activity
(GO:0015174), system y+.

## ChEBI ids (verified against UniProt CATALYTIC ACTIVITY Rhea xrefs in -uniprot.txt)
- L-arginine: CHEBI:32682
- L-lysine: CHEBI:32551
- L-ornithine: CHEBI:46911
- (L-histidine: CHEBI:57595 — not used in core; histidine is a minor substrate)
