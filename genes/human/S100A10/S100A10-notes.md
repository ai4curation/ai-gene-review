# S100A10 (p11, annexin A2 light chain) - curation notes

UniProt: P60903 (human). 97 aa S100 family protein. PANTHER PTHR11639:SF74.

## Deep research status

- `just deep-research-falcon human S100A10` was launched at the start of this review
  (run in parallel with `just fetch-gene-pmids`). See end of file for outcome.
- Literature was gathered directly from cached publications (publications/PMID_*.md)
  and PubMed searches; additional key papers cached: PMID:16400147, PMID:12050667,
  PMID:21768297, PMID:12660155.

## Core biology

### Calcium-insensitive S100 protein; obligate homodimer
- UniProt: "Does not appear to bind calcium. Contains 2 ancestral calcium site related to
  EF-hand domains that have lost their ability to bind calcium." [file:human/S100A10/S100A10-uniprot.txt]
- [PMID:9886297 "p11 is a member of the S100 EF-hand protein family, which is unique in
  having lost its calcium-binding properties"]; [PMID:9886297 "The basic unit for p11 is a
  tight, non-covalent dimer."]
- Consequence: the IBA-propagated `calcium ion binding` and `calcium-dependent protein binding`
  are inherited from the family ancestor but are lost in the S100A10 lineage (target-specific
  divergence). Ca2+-independence of its target binding is the defining feature that lets
  S100A10 hold ANXA2 in a permanent complex.

### AnxA2-S100A10 heterotetramer (AIIt, calpactin I)
- [PMID:9886297 "each annexin II peptide forms hydrophobic interactions with both p11
  monomers, thus providing a structural basis for high affinity interactions"]
- [PMID:23091277 "N-terminal acetylation of AnxA2 is required for S100A10 binding"]
- [PMID:23091277 "only the complex is firmly anchored in the plasma membrane, where it
  functions in the plasma membrane targeting/recruitment of certain ion channels and receptors"]
- Submembranous localisation coupled to AnxA2: [PMID:3126079 "In tissue culture cells
  p11-specific antibodies decorated the same submembranous compartment previously seen with
  antibodies to p36"].

### Adaptor: bridging AnxA2 to third-party proteins (AHNAK, SMARCA3)
- AHNAK: [PMID:14699089 "The S100A10 subunit serves to mediate the interaction between annexin 2
  and the COOH-terminal regulatory domain of AHNAK."]
- Structures: [PMID:22940583 "a single region from the AHNAK C terminus is recruited by an
  S100A10-annexin A2 heterotetramer, forming an asymmetric ternary complex"];
  [PMID:23275167 "Binding of AHNAK to the surface of (p11)(2)(AnxA2)(2) is governed by several
  hydrophobic interactions between side chains of AHNAK and pockets on S100A10."]
- Membrane repair context (AHNAK/dysferlin): [PMID:22940583 "which along with dysferlin,
  functions in muscle and cardiac tissue repair"].
- SMARCA3 (HLTF): [PMID:23415230 "SMARCA3, a chromatin-remodeling factor, is a target for the
  p11/annexin A2 heterotetrameric complex"]; [PMID:23415230 "Formation of this complex
  increases the DNA-binding affinity of SMARCA3 and its localization to the nuclear matrix
  fraction."]

### Trafficking / surface presentation of channels and receptors (best-supported core role)
- TASK-1 (KCNK3): [PMID:12198146 "association with p11 is essential for trafficking of TASK-1 to
  the plasma membrane"]; masks ER retention signal.
- NaV1.8 (SCN10A): [PMID:12050667 "p11 binds directly to the amino terminus of Na(V)1.8 and
  promotes the translocation of Na(V)1.8 to the plasma membrane, producing functional channels."]
- TRPV5/TRPV6: [PMID:12660155 "the S100A10-annexin 2 complex plays a crucial role in routing of
  TRPV5 and TRPV6 to plasma membrane."]
- 5-HT1B receptor: [PMID:16400147 "p11 increases localization of 5-HT1B receptors at the cell
  surface."] and depression-like phenotype in KO mice.
- CCR10: [PMID:26941067 "S100A10 binds directly to the C-terminal cytoplasmic tail of CCR10 and
  that this interaction regulates the CCR10 cell surface presentation"]
- TRPM4 peptide binding in an S100ome-wide FP screen (PMID:31837246; abstract only).

### Cell-surface plasminogen receptor / plasmin generation
- [PMID:9836589 "The fluid-phase recombinant p11 subunit stimulated the rate of t-PA-dependent
  activation of [Glu]plasminogen about 46-fold"]; [PMID:9836589 "the C-terminal lysine residues
  of the p11 subunit bind plasminogen and participate in the stimulation of t-PA-dependent
  activation of plasminogen by AIIt"]
- In vivo: [PMID:21768297 "S100A10-null mice displayed increased deposition of fibrin in the
  vasculature and reduced clearance of batroxobin-induced vascular thrombi"]
- S100A10 acts as a cofactor/template (binds plasminogen through C-terminal lysines),
  so positive regulation of plasminogen activation is well founded.

### Peripheral / indirect phenotypes
- Actin stress fibres/cell spreading via Rac1 (siRNA): [PMID:23129259 "Depletion of S100A10
  induced disruption of stress fiber formation and delay in cell spreading."] Indirect.
- Lipid domain/budding in GUVs (PMID:23861394): the property is AnxA2's; S100A10 is
  dispensable ("This property is observed for the full-length monomeric protein").
- Proteomics: urinary exosomes (PMID:19056867), vein ECM (PMID:27068509), ECM protocol
  (PMID:28675934) - HTP detections.

## Annotation decisions (summary)
- Core: AnxA2-p11 complex; transmembrane transporter (ion channel) binding; protein
  localization to plasma membrane; positive regulation of plasminogen activation;
  cytoplasmic face of plasma membrane; homodimerization.
- Remove: calcium ion binding (IBA), calcium-dependent protein binding (IBA) - lost in S100A10;
  mRNA transcription by RNA pol II (IEA) - not a transcription machinery component.
- Generic protein binding: MODIFY where the cited paper supports adaptor activity
  (AHNAK/SMARCA3 recruitment), transmembrane transporter binding (TRPM4), GPCR binding (CCR10);
  REMOVE otherwise (interactions captured by GO:1990665 complex membership).
