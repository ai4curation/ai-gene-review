# SLC1A2 (EAAT2 / GLT-1, UniProt P43004) — curation notes

De-novo GO annotation review. No deep-research provider file was present; research done
directly from the cached publications, the UniProt record, Reactome entries, and QuickGO/OLS.

## Identity and family
- HGNC:10940, SLC1A2. UniProt P43004 (EAA2_HUMAN), 574 aa, PE 1 (protein level).
- "Excitatory amino acid transporter 2"; synonyms EAAT2, GLT-1, GLT1, glutamate/aspartate
  transporter II. Dicarboxylate/amino acid:cation symporter (DAACS, TC 2.A.23) family, SLC1A2
  subfamily [file UniProt, "Belongs to the dicarboxylate/amino acid:cation symporter"].
- PANTHER PTHR11958:SF93 (EXCITATORY AMINO ACID TRANSPORTER 2). PAINT node for the family-level
  glutamate-transport IBA is PTN000238242; the glutamate/aspartate import IBAs use PTN004328784.
- Paralogs: SLC1A1/EAAT3 (P43005), SLC1A3/EAAT1 (P43007), SLC1A6/EAAT4 (P46411), SLC1A7/EAAT5
  (O00341); the neutral-AA ASCT branch SLC1A5/ASCT2 (Q15758) sits in the same family tree.
  Rat ortholog = P43006 (source of most Ensembl IEA rows); bovine ortholog = F1MUJ6 (ARUK-UCL ISS).

## Core molecular function (well established)
- Na+-dependent, high-affinity symporter: imports one L-glutamate (or L-/D-aspartate) with 3 Na+
  and 1 H+, countertransporting 1 K+ [file UniProt CC:FUNCTION, "Functions as a symporter that
  transports one amino acid molecule"; CATALYTIC ACTIVITY Rhea:70699/70851/71379].
- KM ~18-97 µM for L-glutamate; also L-aspartate (KM 7 µM) and D-aspartate (KM 13-54 µM)
  [PMID:7521911 "The affinities of the EAAT subtypes for L-glutamate were similar, with Km
  determinations varying from 48 to 97 microM in the mammalian cell assay"; UniProt BIOPHYSICOCHEMICAL].
- EAAT2 is distinguished from EAAT1/3 by potent inhibition by kainate and dihydrokainate
  [PMID:7521911].
- Functional unit is a homotrimer of identical subunits, conserved from archaea/bacteria to human
  [PMID:15265858 "assembled as trimers composed of three identical subunits"; PMID:15483603
  "bowl-shaped trimer"; UniProt SUBUNIT "Homotrimer"].
- Carries a thermodynamically uncoupled anion (Cl-) conductance built into the transport pore —
  genuine biophysical property but secondary to amino-acid transport [PMID:14506254 "a
  stoichiometrically coupled transport of glutamate, Na+, K+, and H+, and a pore-mediated anion
  conductance"; UniProt "Mediates Cl(-) flux that is not coupled to amino acid transport"]. Note
  EAAT2 anion channels, unlike EAAT4, show no glutamate-modified voltage-dependent gating
  [PMID:14506254 "EAAT4 but not EAAT2 anion channels displayed voltage-dependent gating"].

## Biological role / localization
- Dominant CNS glutamate transporter: highest expression, largest share of total glutamate uptake;
  its loss raises extracellular glutamate to excitotoxic levels [PMID:21258616 "EAAT2 exhibits the
  highest level of expression, is responsible for the largest proportion of total glutamate
  transport and its functional inactivation raises extracellular glutamate to toxic levels"].
- Chiefly astrocytic, perisynaptic: in human neocortex ~77% of EAAT2 immunoreactivity is in
  astrocytic processes, ~14% in axon terminals (a real but minority neuronal pool)
  [PMID:21258616 "In both astrocytic processes and axon terminals, most EAAT2a is perisynaptic"].
- Expression largely restricted to brain, with lower expression elsewhere (e.g. perivenous
  hepatocytes, pancreas) [PMID:7521911 "expression of EAAT2 was largely restricted to brain";
  Reactome R-HSA-428015 "GLT1 is expressed mainly in the brain and is essential for terminating the
  postsynaptic action of glutamate by rapidly removing released glutamate from the synaptic cleft"].
- Associates with cholesterol-rich lipid raft/membrane microdomains of the plasma membrane;
  raft association is lost in Alzheimer brain [PMID:20193040 "EAAT2 is associated with lipid raft
  microdomains of the plasma membrane"]. Surface level is regulated by PKC-triggered,
  flotillin-1-dependent endocytosis [PMID:21399631] and negatively by caveolin-1 [PMID:26690923].
- Hepatic role: glutamate uptake into perivenous hepatocytes feeds glutamine synthesis; FXR
  regulates this axis [PMID:21757002 "Glutamate is taken up by perivenous hepatocytes and is the
  main source for the synthesis of glutamine, catalyzed by glutamine synthase (GS)"].
- Disease: autosomal-dominant developmental and epileptic encephalopathy 41 (DEE41), de novo
  variants G82R, L85P, P289R [UniProt DISEASE; PMID:27476654, PMID:28777935].

## Decisions of note (see review YAML for per-row reasoning)
- Core MF kept as glutamate:sodium symporter activity (GO:0015501) + high-affinity L-glutamate
  transmembrane transporter activity (GO:0005314); the plainer parent GO:0005313 and the mechanism
  parent GO:0015293 symporter activity marked TOO_GENERAL (entailed, verified via OLS getAncestors).
- `membrane` (GO:0016020) -> MODIFY to plasma membrane (GO:0005886) per transporter convention.
- Broad process parents entailed by specific accepted children -> TOO_GENERAL: GO:0015813
  (vs GO:0098712 import), GO:0070778 (vs GO:0140009 L-Asp import), GO:0006836 neurotransmitter
  transport (vs GO:0098810 reuptake), GO:0006865 amino acid transport, GO:0098657 import into cell.
- Over-annotations: GO:0015175 neutral L-amino acid transporter activity + GO:0015804 (EAAT2 is an
  acidic-AA transporter; the neutral-AA term fits the ASCT paralogs on the shared node);
  GO:0033229 / GO:1903712 L-cysteine transport (minor/promiscuous; EAAT3 is the dedicated cysteine
  transporter); GO:0006750 glutathione biosynthetic process (precursor supply via cysteine, EAAT2
  performs no biosynthetic step); GO:0071314 cellular response to cocaine (expression regulation, not
  a function EAAT2 executes); GO:0070633 transepithelial transport and GO:0150104 transport across
  blood-brain barrier (ISS from bovine F1MUJ6 / NAS from BBB reviews that do not mention EAAT2;
  EAAT2 is a glial uptake transporter, not an endothelial transcellular carrier — checked that
  PMID:30280653 and PMID:26590417 contain no EAAT2/SLC1A2/glutamate-transport text).
- Both GO:0005515 protein binding IPI rows (MAPT/tau P10636; HTT P42858) -> REMOVE per the
  protein-binding policy (uninformative). Interactions are disease-context Y2H/pull-down.
- Anion conductance kept as genuine secondary function: GO:0008509 / GO:0098656 KEEP_AS_NON_CORE.
- Homotrimerization (GO:0070207) ACCEPT (directly shown for hEAAT2).
