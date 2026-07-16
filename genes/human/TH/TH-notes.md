# TH (Tyrosine hydroxylase / tyrosine 3-monooxygenase) — review notes

UniProt: P07101 (TY3H_HUMAN). HGNC:11782. Gene symbol TH (synonym TYH).
NCBI taxon 9606. EC 1.14.16.2.

## Core biology (grounded in UniProt P07101 and cited literature)

TH is the **rate-limiting enzyme of catecholamine biosynthesis**. It catalyzes the
hydroxylation of **L-tyrosine to L-DOPA (L-3,4-dihydroxyphenylalanine)**, the first and
committed step in synthesis of the catecholamines dopamine, noradrenaline and adrenaline.

- Reaction (UniProt CATALYTIC ACTIVITY, RHEA:18201):
  `(6R)-L-erythro-5,6,7,8-tetrahydrobiopterin + L-tyrosine + O2 = (4aS,6R)-4a-hydroxy-...-tetrahydrobiopterin + L-dopa`
  [file:human/TH/TH-uniprot.txt CATALYTIC ACTIVITY block].
- FUNCTION: "Catalyzes the conversion of L-tyrosine to L-dihydroxyphenylalanine (L-Dopa),
  the rate-limiting step in the biosynthesis of catecholamines, dopamine, noradrenaline,
  and adrenaline. Uses tetrahydrobiopterin and molecular oxygen to convert tyrosine to
  L-Dopa" [file:human/TH/TH-uniprot.txt FUNCTION].
- COFACTOR: **Fe(2+)** (non-heme ferrous iron) [file:human/TH/TH-uniprot.txt COFACTOR;
  BINDING sites at residues 361, 366, 406 for Fe cation].
- Member of the **biopterin-dependent aromatic amino acid hydroxylase family** (SIMILARITY);
  can also hydroxylate Phe and Trp with lower specificity (By similarity).
- **Homotetramer** [file:human/TH/TH-uniprot.txt SUBUNIT; PubMed:24947669, PDB 2XSN].
- **Cytosolic**; also reported perinuclear region, nucleus (Ser19-phospho form), axon,
  synaptic/secretory vesicles [SUBCELLULAR LOCATION].
- PATHWAY: "Catecholamine biosynthesis; dopamine biosynthesis; dopamine from L-tyrosine:
  step 1/2" [file:human/TH/TH-uniprot.txt PATHWAY; UPA00747/UER00733; Reactome R-HSA-209905].
- TISSUE: mainly brain and adrenal glands (catecholaminergic neurons, adrenal chromaffin cells).

## Regulation

- **Feedback inhibition** by catecholamines (esp. dopamine), competing with BH4 cofactor
  [ACTIVITY REGULATION; PubMed:15287903].
- **Phosphorylation** of N-terminal Ser residues (Ser19 by CaMK2; Ser62; Ser71 by CaMK2 and
  PKA) modulates activity; Ser62/Ser71 phospho activates; Ser71 phospho counteracts
  catecholamine feedback inhibition [PTM; PubMed:1680128, PubMed:7901013, PubMed:15287903].
- **Cys modification**: NEM / dopamine-oxide modification of Cys176 (numbering in hTH1;
  = Cys207 in hTH4/full-length) inactivates the enzyme [PubMed:34922205].
- Interacts with **YWHAG** (14-3-3γ) when phosphorylated at Ser19; with NT5DC2 (reduces
  activity) [SUBUNIT; PubMed:24947669].
- Ser19/Ser62 phospho triggers proteasomal degradation [PTM; PubMed:21392500].

## Disease

- **Segawa syndrome, autosomal recessive (ARSEGS)** [MIM:605407] = autosomal-recessive
  DOPA-responsive dystonia / infantile parkinsonism-dystonia. Many missense variants
  characterized biochemically (loss of TH activity / stability); L-DOPA-responsive
  [DISEASE; PubMed:24753243, PubMed:8528210, and many variant refs].
- Possible role in Parkinson disease (rare TH deletion) [PubMed:20809526].

## Annotation review reasoning

### Core molecular function
- **GO:0004511 tyrosine 3-monooxygenase activity** — the defining MF. Supported by many
  independent EXP/IDA annotations (PMID:15287903, 17391063, 24753243, 34922205, 8528210,
  1680128, 11943812, 12631248, 2896667, 16338639) plus IBA and IEA. ACCEPT the experimental
  ones as core; ACCEPT the IBA/IEA on the gene's own correct MF (do not down-rank correct core).
  Verified current label via OLS (GO:0004511, not obsolete).
- **GO:0005506 iron ion binding** (IEA/InterPro) — correct; TH uses a non-heme Fe(II) center
  (COFACTOR Fe2+; BINDING residues 361/366/406). ACCEPT as core MF.
- GO:0004497 monooxygenase activity (IEA) — correct but a parent/less-specific term; the
  specific GO:0004511 is annotated, so this is redundant-general. KEEP_AS_NON_CORE.
- GO:0016714 oxidoreductase activity, ...reduced pteridine... (IEA/InterPro) — accurate
  mechanistic parent of GO:0004511. KEEP_AS_NON_CORE (subsumed by specific term).
- GO:0019899 enzyme binding (IPI, PMID:19703902, with DJ-1/PARK7 Q99497) — real interaction
  (DJ-1 directly binds and activates TH), but "enzyme binding" is uninformative regulatory
  adapter binding, not TH's own MF. KEEP_AS_NON_CORE.
- GO:0042802 identical protein binding — appears in UniProt DR (IntAct, TH homotetramer
  self-interaction) but is NOT in the GOA TSV, so not in review set.
- GO:0005515 protein binding (IPI) — bare "protein binding", uninformative. Two annotations
  (PMID:19703902 with DJ-1/Q99497; PMID:11943812 with α-synuclein/P37840). Both are real
  interactions but the term is uninformative → MARK_AS_OVER_ANNOTATED (policy: never REMOVE
  bare protein-binding IPI).

### Core biological process
- **GO:0042416 dopamine biosynthetic process** — core BP; TH makes L-DOPA, the dopamine
  precursor. Multiple IDA (PMID:17391063, 19703902, 12457228) + IEA. ACCEPT experimental/core.
- **GO:0006585 dopamine biosynthetic process from tyrosine** — most precise BP term
  (matches PATHWAY "dopamine from L-tyrosine: step 1/2"). IBA + NAS. ACCEPT as core.
- GO:0042418 epinephrine biosynthetic process; GO:0042421 norepinephrine biosynthetic
  process; GO:0042423 catecholamine biosynthetic process — TH is the rate-limiting entry
  step for all catecholamines, so these are correct downstream-pathway BPs. The direct
  chemical product is L-DOPA→dopamine; epi/norepi are further downstream (require DBH, PNMT).
  ACCEPT (gene contributes to the pathway, upstream committed step). Catecholamine
  biosynthetic process is the general parent → KEEP_AS_NON_CORE (subsumed by dopamine-specific).
- GO:0009072 aromatic amino acid metabolic process (IEA) — true but very general parent.
  KEEP_AS_NON_CORE.

### Behavioral / physiological / peripheral BPs (genuine but non-core, mostly ISS/IBA from mouse ortholog P24529)
- GO:0001963 synaptic transmission, dopaminergic; GO:0050890 cognition; GO:0007612 learning;
  GO:0007613 memory; GO:0007617 mating behavior; GO:0007626 locomotory behavior — downstream
  consequences of dopamine/catecholamine signaling, transferred from ortholog. Genuine but
  peripheral → KEEP_AS_NON_CORE.
- GO:0007601 visual perception; GO:0042462 eye photoreceptor cell development;
  GO:0048596 embryonic camera-type eye morphogenesis; GO:1990384 hyaloid vascular plexus
  regression — retinal/eye roles from mouse ortholog (UniProt FUNCTION "Positively regulates
  the regression of retinal hyaloid vessels ... By similarity"). Peripheral/developmental →
  KEEP_AS_NON_CORE.
- GO:0007507 heart development; GO:0003007 heart morphogenesis; GO:0008016 regulation of
  heart contraction; GO:0009887 animal organ morphogenesis; GO:0009653 anatomical structure
  morphogenesis — reflect the mouse-KO phenotype (embryos die of cardiovascular failure;
  PMID:7715703) and sympathetic control of the heart. Indirect, mediated by catecholamines →
  KEEP_AS_NON_CORE. GO:0003007 (NAS, PMID:12113410) is a human LV-mass polymorphism
  association study — indirect → KEEP_AS_NON_CORE.
- GO:0043473 pigmentation (TAS, PMID:12631248) — TH isoform I in melanosomes may contribute
  to L-DOPA for melanin synthesis; peripheral/speculative → KEEP_AS_NON_CORE.
- GO:0045471 response to ethanol (IDA, PMID:18343820) — the paper (SH-SY5Y cells) shows
  ethanol raises TH protein via cAMP/PKA+HSP90; TH is the responder. Genuine but peripheral →
  KEEP_AS_NON_CORE.
- GO:0001666 response to hypoxia (IDA, PMID:17520326) — the cited paper is an in vitro
  enzymology study of the O2 Km of purified TH (oxygen dependence of catalysis), NOT a
  cellular hypoxia-response assay. The GO term "response to hypoxia" is not supported by this
  evidence → MARK_AS_OVER_ANNOTATED (experimental code, so not REMOVE).

### Cellular component
- **GO:0005737 cytoplasm / GO:0005829 cytosol** — TH is a cytosolic enzyme. Multiple IDA
  (PMID:21392500, 10907721), TAS (Reactome), IBA, IEA, ISS. ACCEPT cytoplasm/cytosol as core.
- GO:0030424 axon; GO:0043204 perikaryon; GO:0043005 neuron projection — TH is in
  catecholaminergic neurons' soma and axons; consistent with SUBCELLULAR LOCATION
  (axon, dopaminergic axon terminals). ACCEPT axon/neuron projection as legitimate active
  location (IBA/IDA); KEEP perikaryon as non-core (ISS).
- GO:0005634 nucleus (IDA PMID:21392500, ISS, IEA) — Ser19-phospho TH shows nuclear
  distribution (PMID:21392500: "molecules phosphorylated at Ser19 were found mainly in the
  nucleus"); UniProt lists Nucleus. Real but a minor phospho-dependent pool → KEEP_AS_NON_CORE.
- GO:0048471 perinuclear region of cytoplasm (ISS/IEA) — from UniProt SUBCELLULAR LOCATION
  (perinuclear region). KEEP_AS_NON_CORE.
- GO:0008021 synaptic vesicle (IEA-SubCell) — from UniProt (secretory/synaptic vesicle,
  By similarity). Plausible transport pool → KEEP_AS_NON_CORE.
- GO:0031410 cytoplasmic vesicle (IDA PMID:12457228) — TH in cytoplasmic granules of
  stimulated human PBMCs. KEEP_AS_NON_CORE (peripheral non-neuronal context).
- GO:0009898 cytoplasmic side of plasma membrane (IDA PMID:12457228) — TH at the plasma
  membrane in unstimulated PBMCs; unusual/context-specific → KEEP_AS_NON_CORE.
- GO:0033162 melanosome membrane (IDA PMID:12631248) — TH isoform I in melanosomes of
  epidermal melanocytes; peripheral → KEEP_AS_NON_CORE.
- GO:0005790 smooth endoplasmic reticulum (IDA PMID:12457228) — the PBMC ultrastructure
  paper localizes TH to plasma membrane and cytoplasmic granules, not specifically to smooth
  ER; this CC is not well supported by the cited abstract but is an experimental annotation →
  KEEP_AS_NON_CORE (do not REMOVE experimental; the primary/core location is cytosol).

## Provenance for peripheral/localization publications
- PMID:12457228: human PBMC ultrastructure; TH at plasma membrane (unstimulated) and
  cytoplasmic granules (PHA-stimulated) [abstract]. Basis for GO:0009898, GO:0031410,
  GO:0005790, and PBMC dopamine/epi/norepi biosynthesis IDAs.
- PMID:12631248: TH isoenzyme I in human melanosomes/cytosol; L-DOPA production in
  melanosomes [abstract]. Basis for GO:0033162, GO:0043473, and a TH-activity IDA.
- PMID:10907721 / PMID:17135716: TH/GCH1 coexpression in human brain neurons (localization
  studies); basis for cytoplasm IDA (10907721), neuron projection IDA (17135716), and a
  dopamine-biosynthesis-from-tyrosine NAS.
- PMID:19703902 (DJ-1/PARK7): DJ-1 "directly bound to TH and DDC and positively regulated
  their activities in human dopaminergic cells" [full text]. Basis for enzyme binding IPI,
  protein binding IPI (with DJ-1 Q99497), a TH-activity IDA, and dopamine-biosynthesis IDA.
- PMID:11943812 (α-synuclein/SNCA P37840): α-synuclein interacts with and inhibits TH
  [full text]. Basis for protein binding IPI (with P37840) and a TH-activity IDA.
- PMID:7715703: mouse Th knockout embryonic lethality (cardiovascular failure), rescued by
  L-DOPA — basis for anatomical-structure-morphogenesis TAS and the heart/development ISS set.

## Core functions selected
1. tyrosine 3-monooxygenase activity (GO:0004511) — MF, with iron ion binding (GO:0005506).
2. dopamine biosynthetic process from tyrosine (GO:0006585) + dopamine biosynthetic
   process (GO:0042416) — BP, acting in the cytoplasm/cytosol (GO:0005737).
