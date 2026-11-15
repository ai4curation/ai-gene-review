# SLC1A3 (EAAT1 / GLAST) — curation notes

UniProt: P43003 (EAA1_HUMAN). HGNC:10941. 542 aa. Chromosome 5p13.
PANTHER: PTHR11958:SF24 (EXCITATORY AMINO ACID TRANSPORTER 1). DAACS family (TC 2.A.23), SLC1A3 subfamily.

## Summary of gene function

SLC1A3 encodes **EAAT1** (Excitatory Amino Acid Transporter 1), also called **GLAST**
(glutamate/aspartate transporter). It is a secondary-active, Na+-coupled, high-affinity
transporter that clears the excitatory neurotransmitter L-glutamate (and L-/D-aspartate)
from the extracellular space. It is one of five human EAATs (EAAT1-5 = SLC1A3, SLC1A2,
SLC1A1, SLC1A6, SLC1A7). EAAT1 is the predominant glutamate transporter of the cerebellum
(Bergmann glia) and is also expressed in retina (Müller glia), inner ear, and some peripheral
tissues (adipocytes).

### Molecular mechanism
- Electrogenic symporter: co-transports one acidic amino acid with 3 Na+ and 1 H+, coupled to
  the counter-transport (antiport) of 1 K+ [UniProt CC:FUNCTION; PMID:20477940].
  UniProt curated reaction (Rhea:70699): `K(+)(in) + L-glutamate(out) + 3 Na(+)(out) + H(+)(out) = K(+)(out) + L-glutamate(in) + 3 Na(+)(in) + H(+)(in)`.
- Also carries a thermodynamically **uncoupled Cl- conductance** (glutamate-gated anion channel
  mode) that is not coupled to amino acid transport; this dissipates charge from the Na+/aspartate
  symport [UniProt CC:FUNCTION: "Mediates Cl(-) flux that is not coupled to amino acid transport;
  this avoids the accumulation of negative charges due to aspartate and Na(+) symport"; PMID:20477940].
- High affinity: Km ~20-62 µM for L-glutamate; transports L-glutamate, L-aspartate and D-aspartate
  [UniProt BIOPHYSICOCHEMICAL PROPERTIES; PMID:7521911; PMID:8123008 Km=78.4 µM].

### Substrate scope
- Acidic amino acids: L-glutamate, L-aspartate, D-aspartate [PMID:7521911; PMID:28424515].
  EAAT1 is NOT a neutral amino acid transporter — that activity belongs to the ASCT paralogs
  (SLC1A4/ASCT1, SLC1A5/ASCT2) in the same SLC1 family.

### Structure / subunit
- Homotrimer; each protomer has a scaffold domain (TM1-2, TM4-5) and a transport domain
  (TM3, TM6-8, re-entrant hairpins HP1-2) that moves ~15-18 Å during the elevator transport cycle
  [PMID:28424515 "The structure of EAAT1cryst shows a symmetric homotrimer"; UniProt SUBUNIT/DOMAIN].
- First human/eukaryotic SLC1 crystal structure (Canul-Tec 2017, PDB 5LLM/5LM4), with allosteric
  inhibitor UCPH-101.

### Localization
- Plasma membrane / cell membrane, multi-pass (8 TM + 2 hairpins) [UniProt SUBCELLULAR LOCATION;
  PMID:20477940; PMID:7521911; PMID:8123008; PMID:28032905; PMID:26690923].
- At astroglial / Bergmann-glia plasma membrane, including perisynaptic processes
  [PMID:28424515 "expressed at the plasma membrane of astrocytes and neurons"].
- In polarized epithelia (retina) it can be basolateral/basal; trafficking regulated by PDZ
  scaffolds (GRIP1, DLG family) and caveolin-1 [PMID:26690923].

### Physiological role
- Rapid removal of synaptically released glutamate, terminating glutamatergic signalling and
  preventing excitotoxicity [UniProt CC:FUNCTION; PMID:16116111].
- Isoform 2 (EAAT1ex9skip, P43003-2) localizes to ER, has no uptake activity, and is a dominant-negative
  regulator of isoform 1 [UniProt MISCELLANEOUS, ALTERNATIVE PRODUCTS; PMID:16042756].

### Disease
- **Episodic ataxia type 6 (EA6)**, with seizures, migraine and alternating hemiplegia; caused by
  heterozygous SLC1A3 variants (e.g. P290R) that reduce glutamate uptake and act dominant-negatively
  [PMID:16116111 "a heterozygous mutation in EAAT1 can lead to decreased glutamate uptake...to cause
  seizures, hemiplegia, and episodic ataxia"; UniProt DISEASE MIM:612656].

## Annotation-review reasoning highlights

- **Core MF**: glutamate:sodium symporter activity (GO:0015501) and high-affinity L-glutamate
  transmembrane transporter activity (GO:0005314). The broader parents (GO:0005313 L-glutamate
  transporter activity, GO:0015172 acidic amino acid transporter activity, GO:0015293 symporter
  activity) are true but entailed → TOO_GENERAL.
- **Neutral amino acid transporter activity (GO:0015175, IBA) and neutral amino acid transport
  (GO:0015804)** are over-annotations propagated from the SLC1 family node that bundles the ASCT
  (neutral AA) paralogs. EAAT1 is an acidic-amino-acid transporter → MARK_AS_OVER_ANNOTATED.
- **Chloride transmembrane transport (GO:1902476, IDA)** and **potassium ion transmembrane transport
  (GO:0071805, IDA)** are genuine parts of the transport cycle (uncoupled anion conductance; K+ antiport)
  → KEEP_AS_NON_CORE. Proposing NEW GO:0005254 chloride channel activity for the uncoupled anion-channel MF.
- **Protein binding (GO:0005515, 21 IPI rows)** from large-scale interactome screens (HuRI PMID:32296183,
  BioPlex PMID:33961781, fragmentomics PMID:36115835) → REMOVE as uninformative per protein-binding policy.
  Many partners are PDZ-domain scaffolds (DLG1-4, GRIP1/2, MAGI1/2, PATJ, MPDZ, PDZK1) relevant to
  C-terminal anchoring/trafficking, but a specific MF cannot be asserted from binary-interaction data alone.
- **transport across blood-brain barrier (GO:0150104, NAS/ISS)** — the NAS rows cite general BBB reviews
  (PMID:26590417, PMID:30280653) that do not establish an EAAT1 BBB-transport function; EAAT1's role is
  perisynaptic/astroglial glutamate uptake → MARK_AS_OVER_ANNOTATED.
- **chemical synaptic transmission (GO:0007268, TAS)** — EAAT1 terminates/regulates transmission by
  clearing glutamate rather than performing transmission → MARK_AS_OVER_ANNOTATED; the precise role is
  captured by neurotransmitter uptake (GO:0001504).
- **membrane (GO:0016020)** → MODIFY to plasma membrane (GO:0005886).
- IBA MF/CC rows (GO:0005313, GO:0005886, GO:0015501) sit on node PTN000238242 and include the target's
  own experimental annotation in WITH/FROM — correct and expected, not circular.
