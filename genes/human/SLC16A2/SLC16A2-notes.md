# SLC16A2 (MCT8) review notes

UniProt: P36021 (MOT8_HUMAN). HGNC:10923. Gene synonyms MCT8, MCT7, XPCT.
Taxon: Homo sapiens (NCBITaxon:9606). 539 aa, 12 TM helices, MFS fold.

## One-line identity

MCT8 is a **specific, facilitative (equilibrative) thyroid hormone transmembrane
transporter** that mediates bidirectional uptake and efflux of iodothyronines
across the plasma membrane. It is the gene mutated in Allan-Herndon-Dudley
syndrome (MCT8 deficiency).

## Core molecular function and mechanism

- UniProt CC FUNCTION: [file:human/SLC16A2/SLC16A2-uniprot.txt "Specific thyroid hormone transmembrane transporter, that mediates both uptake and efflux of thyroid hormones across the cell membrane independently of pH or a Na(+) gradient. Major substrates are the iodothyronines T3 and T4 and to a lesser extent rT3 and 3,3-"] (text wraps to "diiodothyronine (3,3'-T2)").
- Energy-independent, bidirectional, Na+/H+-independent facilitated diffusion:
  [PMID:20628049 "mediates energy-independent bidirectional transport of iodothyronines across the plasma membrane"] and
  [PMID:40680733 "It mediates the flux of T3 and T4 across the plasma membrane through facilitated diffusion independent of proton or sodium gradient"].
  This equilibrative, uncoupled mechanism is the key distinction from the
  proton-coupled lactate transporters MCT1-4 (SLC16A1/A3/A7/A8), and MCT8 does
  not require an ancillary chaperone (basigin/embigin/neuroplastin) for surface
  expression: [PMID:19797118 "hMCT8 does not form heterodimers with the ancillary proteins basigin, embigin, or neuroplastin, unlike other MCTs"].
- Substrate specificity: L-iodothyronines requiring iodine on the aromatic ring:
  [PMID:20628049 "human MCT8 is specific for"] L-iodothyronines... (full text: "requires at least one iodine atom per aromatic ring").
- Core MF GO term: **GO:0015349 thyroid hormone transmembrane transporter activity**
  (QuickGO-verified definition: "Enables the transfer of thyroid hormones from one
  side of a membrane to the other..."). is_a ancestry (QuickGO): GO:0022857
  transmembrane transporter activity -> GO:0005215 transporter activity. (GO places
  it under GO:0015291 secondary active transmembrane transporter activity in the
  ontology, which is a known ontology-structure quirk; MCT8 itself is facilitative.)
  Importantly GO:0015349 is NOT a descendant of GO:0015171 amino acid transmembrane
  transporter activity nor of GO:0008028 monocarboxylic acid transmembrane
  transporter activity, so those are separate (parallel) claims, not general parents.

### Transport substrates (UniProt curated CC CATALYTIC ACTIVITY, Rhea reactions)
- T3 (3,3',5-triiodo-L-thyronine): CHEBI:533015, RHEA:71811
- T4 (L-thyroxine): CHEBI:58448, RHEA:71819
- rT3 (3,3',5'-triiodo-L-thyronine): CHEBI:57261, RHEA:71815
- 3,3'-T2 (3,3'-diiodo-L-thyronine): CHEBI:176514, RHEA:71823
- DIT (3,5-diiodo-L-tyrosine), efflux: CHEBI:57506, RHEA:82879 [PMID:38661522]
- MIT (3-iodo-L-tyrosine), efflux: CHEBI:59898, RHEA:82883 [PMID:38661522]
- UniProt: [file:human/SLC16A2/SLC16A2-uniprot.txt "Mediates the efflux of 3,5-diiodo-L-tyrosine (DIT) and 3-iodo-L-tyrosine (MIT)"]. These iodotyrosines are amino acids, which grounds the (non-core) amino acid transmembrane transporter activity annotation.

## Localization

- Plasma membrane, multi-pass: UniProt SUBCELLULAR LOCATION "Cell membrane ... Multi-pass membrane protein"; direct experimental PM localization in many studies (PMID:19022891, 21315799, 26426690, 20628049, 23550058, 25527620, 40680733). Core location: **GO:0005886 plasma membrane**.
- Apical plasma membrane at the choroid plexus epithelium / BBB microvessels:
  [PMID:18687783 "MCT8 is concentrated on the epithelial cell apical surface"] (choroid plexus). GO:0016324 apical plasma membrane — real sub-location in these polarized cells.

## Physiological roles (what MCT8 itself does)

- Cellular thyroid hormone transport (uptake and efflux): **GO:0070327 thyroid hormone transport** — core process, abundant IDA/IMP support.
- Thyroid hormone transport across the blood-brain barrier, especially T3 import into brain:
  [PMID:28526555 "We demonstrate that T3 transport across the BBB is dependent on MCT8, likely driving the decreased concentrations of T3 observed in MCT8-deficient brains"];
  [PMID:40680733 "MCT8 and OATP1C1 are two membrane transporters of the major facilitator superfamily (MFS) responsible for passage of thyroid hormones across the blood-brain barrier (BBB) and into neurons and glial cells"].
  MCT8 is the transporter executing this step at the BBB endothelium, so
  GO:0150104 transport across blood-brain barrier passes the participation test.
- UniProt BBB statement: [file:human/SLC16A2/SLC16A2-uniprot.txt "Acts as an important mediator of thyroid hormone transport, especially T3, through the blood-brain barrier"].

## Participation test — processes NOT performed by MCT8 (necessity != participation)

- **GO:2000178 negative regulation of neural precursor cell proliferation** (IMP, acts_upstream_of, PMID:19022891): the James et al. paper shows MCT8 overexpression repressed proliferation of NT2 cells. This is a downstream consequence of altered intracellular T3 availability, not a step MCT8 catalyses. MARK_AS_OVER_ANNOTATED (indirect developmental effect).
- **GO:0042403 thyroid hormone metabolic process** (IGI, acts_upstream_of, with UniProtKB:P55073 = DIO3): MCT8 transport gates substrate supply to deiodinases; transport is "rate-limiting for intracellular metabolism" (PMID:16887882 title). Correctly modeled with acts_upstream_of, so KEEP_AS_NON_CORE (MCT8 does not itself metabolize TH).
- **GO:0006520 amino acid metabolic process** (IGI, acts_upstream_of, with UniProtKB:P49895 = DIO1): over-broad; MARK_AS_OVER_ANNOTATED.

## Family-name / misclassification issues

- MCT8 is named for the SLC16/MCT family (monocarboxylate transporters) by homology,
  but it does NOT transport the classic monocarboxylates (lactate, pyruvate, ketone
  bodies). UniProt SIMILARITY: "Belongs to the major facilitator superfamily.
  Monocarboxylate porter (TC 2.A.1.13) family."
- **GO:0008028 monocarboxylic acid transmembrane transporter activity** (TAS) and
  **GO:0015718 monocarboxylic acid transport** (TAS) both trace to PMID:9425115
  (Price, Jackson & Halestrap 1998), the MCT-family cloning paper, which classified
  XPCT/MCT8 by sequence homology and demonstrated NO monocarboxylate transport for
  it. These are family-name-based over-annotations: MARK_AS_OVER_ANNOTATED.
  (T3/T4 technically carry one carboxyl, but the term reflects the MCT family
  misnomer, not a demonstrated lactate/pyruvate-type function.)

## Amino acid transporter rows

- **GO:0015171 amino acid transmembrane transporter activity** (IDA PMID:26305885; IEA ARBA): MCT8 transports iodotyrosines (MIT, DIT) and iodothyronines, which are amino acids, so an amino acid transporter activity is a genuine but non-core characterization. KEEP_AS_NON_CORE. (Note: PMID:26305885 "Transport of Iodothyronines by Human L-Type Amino Acid Transporters" is primarily about LAT1/LAT2 etc.; ARUK-UCL curated several MCT8 rows from it. The amino acid transport claim is independently supported by the DIT/MIT efflux UniProt curation, so it is kept rather than removed.)
- **GO:0089718 amino acid import across plasma membrane** (IDA PMID:26305885): MCT8 imports iodothyronines (amino acid derivatives); non-core. KEEP_AS_NON_CORE.

## Oligomerization

- MCT8 exists as monomer, homodimer and homooligomer: UniProt SUBUNIT "Monomer ... Homodimer ... Homooligomer". GO:0042802 identical protein binding (IDA PMID:19797118) captures homodimerization — informative, KEEP_AS_NON_CORE (not bare protein binding).

## Generic protein-binding rows (removed per policy)

- GO:0005515 protein binding (IPI x2, partner UniProtKB:Q9H0X4 = FAM234A; from OpenCell PMID:35271311 and the SLC interactome PMID:40355756): bare protein binding, uninformative. REMOVE per protein-binding policy. Removal does not imply the interaction is false.

## Source defect

- GOA rows citing **PMID:4036896** for GO:0015349 (IMP) and GO:0070327 (IMP), assigned
  by UniProt, dated 2025-11-12 alongside the 2025 cryo-EM papers 40140416 and 40680733.
  PMID:4036896 resolves to an unrelated 1985 paper ("On-line documentation of
  measles-mumps-rubella vaccine inoculation"). Almost certainly a digit-dropping
  transposition of PMID:40368961 (Tassinari et al. 2025, "Molecular mechanism of
  thyroxine transport by monocarboxylate transporters"), which is UniProt reference
  RN[19] for this entry. Recorded as a SUSPECTED WRONG_REFERENCE source defect
  (REPOINT PMID:4036896 -> PMID:40368961). The annotations themselves (core THH
  transporter activity / transport) are correct and amply supported, so ACCEPT with
  the defect flagged.

## Disease

- Allan-Herndon-Dudley syndrome / MCT8 deficiency (MIM:300523), X-linked. Severe
  psychomotor retardation, central hypotonia, spastic quadriplegia; characteristic
  thyroid profile of high/elevated serum T3 with low T4. UniProt DISEASE section.
  Loss of MCT8 impairs brain T3 uptake. This is disease/phenotype context, not a GO
  molecular function; captured in description, not as process annotations.

## Structure

- Multiple 2025 cryo-EM structures (PDB 9DWY, 8ZKN/8ZKO, 9FKN/9FOT/9GF8/9GV5),
  MFS fold, outward/inward-facing states (PMID:40680733, 40140416, 40368961).
  Key substrate/transport residues: R371, D424 (abolish transport when mutated),
  N119, Y335; dimer interface residues F182, H186, F271.

## Action tally (48 annotations)
- ACCEPT: plasma membrane (EXP/IBA/IDA/IEA/IMP/TAS), apical PM (IDA/IEA), GO:0015349
  THH transporter activity (IBA/IDA/IEA/IMP), GO:0070327 TH transport
  (IBA/IDA/IEA/IMP), GO:0150104 transport across BBB (IMP/NAS).
- KEEP_AS_NON_CORE: GO:0042802 identical protein binding; GO:0015171 amino acid
  transporter activity (IDA/IEA); GO:0089718 amino acid import; GO:0042403 TH
  metabolic process (acts_upstream_of).
- MARK_AS_OVER_ANNOTATED: GO:0008028 / GO:0015718 monocarboxylate transport
  (family-name); GO:2000178 neural precursor proliferation; GO:0006520 amino acid
  metabolic process.
- TOO_GENERAL: GO:0022857 transmembrane transporter activity; GO:0055085
  transmembrane transport.
- REMOVE: GO:0005515 protein binding (x2, protein-binding policy).
