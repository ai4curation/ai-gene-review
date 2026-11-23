# SLC22A3 (OCT3 / EMT) — curation notes

UniProt: O75751 (S22A3_HUMAN). HGNC:10967. Chromosome 6q25.3. 556 aa, MFS fold,
7 predicted TM helices (UniProt FT; cryo-EM structures 7ZH0/7ZH6/7ZHA). Member of
the SLC22 organic cation transporter (OCT) sub-branch (OCT1/SLC22A1, OCT2/SLC22A2,
OCT3/SLC22A3).

## Identity and core function

SLC22A3 is the **extraneuronal monoamine transporter (EMT)**, the molecular correlate
of classical "uptake-2": a low-affinity, high-capacity, corticosterone/steroid-sensitive
clearance system for biogenic monoamines in the extracellular space, complementing the
high-affinity neuronal uptake-1 transporters NET/DAT/SERT (SLC6 family).

- Original EMT identification: [PMID:10196521 "Molecular identification of the corticosterone-sensitive extraneuronal catecholamine transporter."].
- UniProt FUNCTION: "Electrogenic voltage-dependent uniporter that mediates the transport of a variety of organic cations such as endogenous bioactive amines, cationic drugs and xenobiotics" and "Functions as a Na(+)- and Cl(-)-independent, bidirectional uniporter" (CC:FUNCTION, ECO:0000269|PubMed:12538837). It is "Implicated in monoamine neurotransmitters uptake such as dopamine, adrenaline/epinephrine, noradrenaline/norepinephrine, histamine, serotonin and tyramine" (CC:FUNCTION).

Mechanistically it is a **facilitated (uniport) polyspecific organic cation transporter**:
Na+-/Cl--independent, electrogenic, membrane-potential-driven, and bidirectional — NOT a
coupled symporter. Transport is driven by the electrochemical potential (membrane potential +
concentration gradient) [PMID:10966924 "The transport process was electrogenic"].

### Monoamine substrate profile (quantitative)
[PMID:20858707] expressed hOCT3 in HEK293 Flp-in and measured kinetics; hOCT3 is "less
selective than hPMAT toward the monoamines, and the V(max)/K(m) rank order for hOCT3 is:
histamine > norepinephrine, epinephrine > dopamine >5-HT"; hOCT3 "represents a major
uptake(2) transporter for histamine, epinephrine, and norepinephrine." KM values are high
(uptake-2 low affinity): histamine 641 µM, adrenaline 458 µM, noradrenaline 923 µM,
serotonin 988 µM, dopamine 1033 µM (UniProt BIOPHYSICOCHEMICAL PROPERTIES, from PubMed:20858707).
[PMID:16581093] (rat brain / HEK): OCT2 and OCT3 "share a similar monoamine preference
profile, with higher transport efficacies for epinephrine and histamine than for the other
monoamines."

Verified ChEBI substrates (UniProt CATALYTIC ACTIVITY / Rhea):
(R)-noradrenaline CHEBI:72587, (R)-adrenaline CHEBI:71406, serotonin CHEBI:350546,
dopamine CHEBI:59905, histamine CHEBI:58432, tyramine CHEBI:327995, agmatine CHEBI:58145,
choline CHEBI:15354.

### Polyspecific organic cation / xenobiotic / drug transport
OCT3 transports prototypical organic cations tetraethylammonium (TEA) and the neurotoxin
MPP+, and clinical drugs including metformin, cimetidine, and the platinum drug oxaliplatin.
[PMID:10966924]: cloned OCT3 "capable of mediating potential-dependent transport of a variety
of organic cations including tetraethylammonium ... plays an important role in the renal
clearance of cationic drugs." UniProt MISCELLANEOUS: "Mediates the uptake of clinically used
drugs including neurotoxin 1-methyl-4-phenylpyridinium (MPP(+)) and platinum-based drug
oxaliplatin ... Plays a role in the anticancer activity of oxaliplatin."
Additional in-vitro substrates: agmatine [PMID:12538837], guanidine (PubMed:10966924),
choline (low affinity, KM ~9.9 mM) [PMID:40972734 "SLC22A1-3 were confirmed as choline
transporters, albeit with low affinity"], cyclo(his-pro) and salsolinol (dopaminergic
neuromodulators, low efficiency) [PMID:17460754 — note: this paper's primary focus is OCT2,
but OCT3 is assayed in parallel].

### Localization
- **Plasma membrane is the functional location** (core). Direct human evidence:
  [PMID:15817714] (bronchial epithelium, immunolocalization), [PMID:20858707], [PMID:23137377]
  (hCMEC/D3 BBB proteomics), Reactome. UniProt CC:SUBCELLULAR LOCATION: "Cell membrane",
  "Apical cell membrane", "Basolateral cell membrane" (localization is polarized and
  tissue-dependent).
- Apical: enterocyte brush border [PMID:16263091], ciliated bronchial cells [PMID:15817714].
- Basolateral: intermediate cells of bronchus [PMID:15817714].
- **Intracellular membrane localizations (mitochondrial membrane, nuclear/outer nuclear
  membrane, endomembrane system) rest only on the mouse ortholog (ISS from UniProtKB:O88446 /
  Q9WTW5) and "By similarity" statements** — never demonstrated for human OCT3. UniProt notes
  these are speculative: "May mediate intracellular transport of organic cations due to its
  localization on endomembranes ... (By similarity)." Treated as over-annotation in this review.
- The automated `GO:0098793 presynapse` annotation (inter-ontology inference from serotonin
  uptake) is inconsistent with OCT3's defining **extraneuronal / non-neuronal (glial, uptake-2)**
  role; marked over-annotated.

### Tissue expression
Broad: liver, kidney (proximal tubule), intestine, placenta, heart, skeletal muscle, adrenal
gland, aorta, brain (glia and monoaminergic regions), respiratory epithelium, testis
(peritubular myoid and Leydig cells [PMID:35307651]). [PMID:20858707] RT-PCR: hOCT3
"selectively and highly expressed in adrenal gland and skeletal muscle."

### Regulation / structure
- C-terminal PDZ-binding motif (sequence ends ...VSRSHL): captured in a high-throughput
  PDZ-PBM affinity screen [PMID:36115835] binding DLG1-4, PDZK1, SCRIB, MPDZ/MUPP1, MAGI2,
  GRIP1/2, LNX1/2, MPP-family, etc. PDZ scaffolds (e.g. PDZK1) regulate OCT surface
  expression. ABL1 SH3 interaction [PMID:17474147] relates to a proline-rich motif /
  phosphotyrosine regulatory switch (PubMed:26979622, not cached).
- DOMAIN (UniProt): "Contains one proline-rich sequence (Pro-Glu-Ser-Pro-Arg) that is
  required for transport activity" (PubMed:26979622).

## Curation decisions summary
- **Core MF**: GO:0008504 monoamine transmembrane transporter activity (non-obsolete, verified)
  + GO:0015651 quaternary ammonium group transmembrane transporter activity (the polyspecific
  organic cation / TEA / MPP+ / drug function). NOTE: GO:0015101 "organic cation transmembrane
  transporter activity" is **OBSOLETE** (unnecessary grouping term, no replacement), as is the
  BP GO:0015695 "organic cation transport"; so the quaternary-ammonium and monoamine MF terms
  carry the organic-cation function.
- **Core processes**: neurotransmitter / catecholamine / monoamine uptake (uptake-2), histamine
  transport, quaternary ammonium / xenobiotic (drug) transport, all at plasma membrane.
- GO:0022857 (transmembrane transporter activity) and GO:0055085 (transmembrane transport) and
  GO:0016020 (membrane) are root/generic terms imprecise on their own → TOO_GENERAL (per
  2026-11-14 maintainer ruling; more specific substrate-naming terms asserted elsewhere).
- 21 bare GO:0005515 protein binding rows → REMOVE (protein-binding policy; uninformative).
  The PDZ interactome merits a GO:0030165 PDZ domain binding annotation (suggested).
- GO:0072530 "obsolete purine-containing compound transmembrane transport" → REMOVE (obsolete
  grouping term; the abacavir/nucleoside Reactome link does not justify a defunct class).
- Intracellular membrane localizations (mito/nuclear/endomembrane) → MARK_AS_OVER_ANNOTATED
  (mouse-ISS / By-similarity only, no human evidence).
- Participation test (CLAUDE.md): OCT3 *performs* monoamine/cation uptake — these transport
  processes are participation and are ACCEPTed. Blood-brain-barrier transport (NAS, review-only)
  is contextual → KEEP_AS_NON_CORE.
