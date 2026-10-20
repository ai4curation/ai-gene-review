# CBL10 (SCaBP8, At4g33000, UniProt Q7FRS8) - curation notes

## Session 1 (2026-10-19): new review

No deep-research provider is available in this environment, so these notes record
manual literature research (cached publications under `publications/`, PubMed
E-utilities, web search). Most CBL10 primary papers are abstract-only in the cache;
PMID:19448033 and PMID:31858132 have full text.

### Identity and domain architecture

- 256 aa calcineurin B-like (CBL) calcium sensor with four EF-hands; UniProt:
  "Belongs to the calcineurin regulatory subunit family." Only EF-hand 4 has a
  full canonical PROSITE Ca2+-binding loop annotated (residues 207-218).
- Unlike CBL4/SOS3 it has no N-myristoylation motif; an N-terminal hydrophobic
  extension targets it to membranes [PMID:19448033 "While SCaBP8 lacks an N-terminal
  myristoylation motif, an N-terminal 25–amino acid hydrophobic domain is required for
  SCaBP8 plasma membrane localization"]. UniProt (from PMID:19832944): "The N-terminal 40
  amino acids are necessary and sufficient for vacuolar and endosomal targeting."
- Two splice isoforms differing at the N terminus (isoform 2: MTTGRPNNILALKIST -> MEQVSS);
  both interact with CIPK24 per IntAct.

### Calcium binding and kinase activation (shoot SOS branch)

- Quan et al. 2007 [PMID:17449811 "SCABP8 is further shown to bind calcium, interact with
  SOS2 both in vitro and in vivo, recruit SOS2 to the plasma membrane, enhance SOS2
  activity in a calcium-dependent manner, and activate SOS1 in yeast"]. Shoot-preferential
  role [PMID:17449811 "the SOS3 homolog SOS3-LIKE CALCIUM BINDING PROTEIN8
  (SCABP8)/CALCINEURIN B-LIKE10 functions mainly in the shoot response to salt toxicity"].
  Partial redundancy with SOS3/CBL4 [PMID:17449811 "SCABP8 and SOS3 are only partially
  redundant in their function"].
- Phosphorylation by SOS2 at the C terminus (Ser-237 in the isoform numbering used by the
  paper; UniProt maps it to Ser-247 of the canonical isoform 1) stabilizes the complex at the
  membrane [PMID:19448033 "In vivo, this phosphorylation was induced by salt stress,
  occurred at the membrane, stabilized the SCaBP8-SOS2 interaction, and enhanced plasma
  membrane Na+/H+ exchange activity"]. scabp8 has reduced PM Na+/H+ exchange
  [PMID:19448033 "Na + /H + exchange at the plasma membrane of Arabidopsis is severely
  reduced in the scabp8 mutant"].
- General CBL mechanism: CIPK phosphorylates a conserved CBL C-terminal Ser
  [PMID:22253446 "We identified a conserved serine residue within the C terminus of CBLs as
  being phosphorylated by their interacting CIPKs"].
- CIPK8 is a second CBL10 partner activating SOS1 [PMID:31858132 "These results suggest
  that CIPK8-mediated activation of SOS1 is CBL10-dependent and SOS3-independent"].

### Vacuolar branch / localization

- Kim et al. 2007 [PMID:17825054 "the CBL10-CIPK24 (SOS2) complex is associated with the
  vacuolar compartments that are responsible for salt storage and detoxification in plant
  cells"]; cbl10 shoots have *lower* Na+ [PMID:17825054 "the Na(+) content of the cbl10
  mutant, unlike other salt-sensitive mutants identified thus far, was significantly lower
  than in the wild type under either normal or high-salt conditions"].
- Batistic et al. 2010: N-terminal targeting signals determine CBL localization
  [PMID:19832944 "distinct targeting signals located in the N-terminal domain of CBL
  proteins determine the spatially discrete localization of CBL/CIPK complexes"]. UniProt:
  "Exclusively targeted to the tonoplast when interacting with CIPK24 (PubMed:19832944)."
- Localization is therefore dual (PM per Quan 2007 / Lin 2009; tonoplast + endosomes per
  Kim 2007 / Batistic 2010). Lin 2009 (Pardo unpublished) found tonoplast Na+/H+ exchange
  unchanged in scabp8, so the vacuolar mechanism is not settled [PMID:19448033 "Our
  unpublished results (J.M. Pardo) indicate that Na + /H + exchange in tonoplast vesicles
  is not altered in the scabp8 mutant"].
- Soluble pool also exists [PMID:19448033 "SCaBP8 protein is present in both soluble and
  membrane fractions"] - basis for cytoplasm IDA. No evidence for nuclear localization
  (nucleus row is an AtSubP prediction).

### Kinase-independent regulation of AKT1

- Ren et al. 2013 [PMID:23331977 "CBL10 directly interacted with AKT1, as verified in
  yeast two-hybrid, BiFC and co-immunoprecipitation experiments"; "CBL10 impairs
  AKT1-mediated inward K+ currents"; "CBL10 may compete with CIPK23 for binding to AKT1 and
  negatively modulate AKT1 activity"]. Evidence is from overexpression lines plus
  oocyte/protoplast electrophysiology; supports GO:0019870 potassium channel inhibitor
  activity and negative regulation of K+ transport, but it is a single study.

### Reproductive development

- Monihan et al. 2016 [PMID:26979332 "CBL10 functions early in reproductive development
  before fertilization"; "Neither SOS2 nor SOS3 function in reproductive development in
  response to salt"]. Not annotated in GOA; this is a salt-conditional phenotype and I did
  not add a NEW developmental term (necessity, not demonstrated participation).

### Curation decisions (summary)

- Ca2+ binding (IBA/IDA/IEA): accept.
- Protein binding IPI x3: per policy, MODIFY to informative MFs (CIPK24 activation ->
  GO:0030295 protein kinase activator activity; Kim 2007 binding only -> GO:0019901 protein
  kinase binding; AKT1 -> GO:0019870 potassium channel inhibitor activity).
- kinase binding IEA: MODIFY to GO:0030295 (specific supported activity).
- vacuolar membrane IEA -> MODIFY to plant-type vacuole membrane (is_a descendant, already
  IDA/IBA on the gene).
- nucleus ISM: REMOVE (prediction; contradicted by membrane targeting data).
- regulation of potassium ion transport IMP -> MODIFY to GO:0043267 negative regulation.
- monoatomic ion homeostasis IMP -> MODIFY to GO:0055078 sodium ion homeostasis.
