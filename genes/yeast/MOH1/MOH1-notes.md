# MOH1 (YBL049W, P38191) — research notes

Research journal for the AI GO-annotation review. MOH1 is a genuinely
understudied ("dark") *S. cerevisiae* gene. This file separates what is KNOWN
from what is NOT known, with inline provenance.

## Identity / basic facts (KNOWN)

- UniProt **P38191**, gene **MOH1**, systematic name **YBL049W** (chromosome II,
  left arm). 138 aa, 16 kDa. SGD **S000000145**. **Verified ORF, protein of
  unknown function** (SGD).
- Member of the **Yippee family** (UniProt SIMILARITY: "Belongs to the yippee
  family"). InterPro: IPR034751 (Yippee), IPR004910 (Yippee/Mis18/Cereblon),
  IPR039058 (Yippee_fam); Pfam PF03226 (Yippee-Mis18); PROSITE PS51792 (YIPPEE);
  PANTHER PTHR13848.
- **Single yeast ortholog of the human YPEL1–YPEL5 family.** The human paralogs
  arose by gene duplication; yeast has one member.

## Domain / molecular architecture (KNOWN, independently verified)

- UniProt annotates a **Yippee domain (residues 41–138)** with a structural
  **Zn(2+) site coordinated by Cys45, Cys48, Cys101, Cys104** (ProRule
  PRU01128).
- My own bioinformatics analysis (`MOH1-bioinformatics/`) independently
  confirms the Yippee zinc signature: two CxxC pairs **C45-x2-C48 … C101-x2-C104**
  separated by a 52-residue spacer — the canonical Yippee motif
  (Cys-X₂-Cys-X₅₂-Cys-X₂-Cys). See `file:yeast/MOH1/MOH1-bioinformatics/RESULTS.md`.
- Conservation vs human YPEL1–5: ~37–45% identity; **all four Zn-cysteines are
  perfectly conserved in every human ortholog**, supporting a retained structural
  zinc site. (Bioinformatics RESULTS.md.)
- The Yippee/Mis18/CULT fold is a **zinc-stabilized β-fold with a cradle-shaped
  pocket implicated in protein/nucleic-acid binding** — a binding/scaffold module,
  **not a recognized catalytic fold**. No EC number; no catalytic motif detected.
  [PMID:11240639 "Yippee contains a putative zinc-finger-like metal binding domain"]

## What the primary literature actually establishes

### Ashrafi, Farazi & Gordon 1998 (JBC) — the founding paper (KNOWN, but indirect)
- MOH1/YBL049W was identified as a **putative N-myristoylprotein** whose deletion
  (in NMT1 cells) mimics the starvation-sensitive phenotype of an nmt1 mutant.
  [PMID:9748261 "Removal of any one of the following nine substrates produced a
  loss of CFU similar to that observed in nmt1-451Dfaa4Delta cells: Arf1p, Arf2p,
  Sip2p, Van1p, Ptc2p, YBL049W (homology to Snf7p), YJR114W, YKR007W, and
  YMR077C"]
- The paper's parenthetical "(homology to Snf7p)" is an **early, superseded**
  homology guess; the protein was later recognized as a Yippee-family member.
- This links MOH1 (phenotypically) to **maintenance of proliferative potential /
  survival during stationary phase**, not to a molecular activity.
  [PMID:9748261 "specific N-myristoylproteins contribute to stationary-phase
  survival" — paraphrase; verbatim: "These proteins provide opportunities to
  further define the molecular mechanisms that regulate survival during stationary
  phase"]
- NOTE: whether Moh1 is genuinely N-myristoylated in vivo was inferred from a
  genome-wide sequence search for Nmt substrates plus deletion phenotype, not
  demonstrated biochemically here. Treat "N-myristoylprotein" as predicted.

### Lee et al. 2017 (J Microbiol Biotechnol) — the "pro-apoptotic" paper (KNOWN, moderate quality)
- Basis for UniProt's "Pro-Apoptotic protein MOH1" RecName and the Apoptosis
  keyword. moh1Δ shows **enhanced viability** under apoptogenic stress (UV, MMS,
  camptothecin, 50°C heat shock, 1.2 M KCl), and Moh1 protein is **up-regulated**
  under stress. [PMID:28173693 "The moh1Δ mutant exhibited enhanced cell viability
  compared with the WT-MOH1 strain when treated with lethal UV irradiation, 1.8 mM
  MMS, 100 µ CPT, heat shock at 50°C, or 1.2 M KCl"]
- Human **YPEL5** (and other YPELs) partially complement moh1Δ; YPEL5 conferred
  UV sensitivity similar to WT-MOH1. [PMID:28173693 "the transformant bearing
  pYES2-YPEL5 was more sensitive to lethal UV irradiation and its UV sensitivity
  was similar to that of the WT-MOH1 strain"]
- Authors frame this as "mitochondria-dependent apoptosis induced by DNA damage."
  [PMID:28173693 "their involvement in mitochondria-dependent apoptosis induced by
  DNA damage"]
- CAVEAT (my judgment): "yeast apoptosis" / metacaspase-dependent regulated cell
  death is a **contested framework**; the assay is a heterologous-complementation
  viability study, abstract-only in our cache. The robust, model-independent
  observation is that **moh1Δ increases stress resistance and Moh1 is
  stress-induced** — i.e. Moh1 *sensitizes* cells to lethal stress. The molecular
  mechanism is not established. This is a "pro-death phenotype," not a demonstrated
  molecular activity, and does not by itself justify a GO apoptosis annotation for
  a yeast gene.

### Roxström-Lindquist & Faye 2001 (Insect Mol Biol) — family founding paper (KNOWN, context)
- Defines the Yippee family; Drosophila Yippee found as interactor of Hemolin;
  "putative zinc-finger-like metal binding domain"; family conserved slime-mould
  → human. Human clone 76% identical to Drosophila Yippee.
  [PMID:11240639 "It is the first characterized member of a conserved gene family
  of proteins present in diverse eukaryotic organisms"]
- Even the founding family paper leaves molecular function open:
  [PMID:11240639 "the Hemolin-Yippee interaction remains to be further
  elucidated"].

### Wang et al. 2018 (Metallomics) — the RCA zinc annotation source (KNOWN, computational)
- GO:0008270 (zinc ion binding, RCA, PMID:30358795) derives from a proteome-wide
  bioinformatic + MS survey of the yeast zinc proteome; MOH1 is included among 582
  known/potential zinc-binding proteins by domain/motif prediction, not by direct
  metal-binding assay of Moh1. [PMID:30358795 "The yeast zinc proteome of 582
  known or potential zinc-binding proteins was identified using a bioinformatics
  analysis that combined global domain searches with local motif searches"]

### Olgun et al. 2025 (bioRxiv preprint 10.1101/2025.10.30.685511) — most recent (KNOWN, NOT peer-reviewed)
- Title: "Yippee-like protein Moh1 links gene expression to metabolism and
  selective stress resistance in Saccharomyces cerevisiae." Preprint, no PMID.
- Reports: moh1Δ increases sensitivity to sodium azide and sulfuric acid but
  **increases resistance to H2O2 and acetic acid**; H2O2 resistance attributed to
  **decreased cellular uptake from altered membrane permeability**, not lowered
  mitochondrial ROS; transcriptional reprogramming + metabolic remodeling (lipids,
  proteins, cell-wall polysaccharides).
- This reinforces a role in **stress resistance / membrane and metabolic
  remodeling** but still does not assign a molecular activity. Because it is a
  non-peer-reviewed preprint with no PMID, it is used here for context/knowledge-gap
  framing only (status CLOSING/NARROWING for some gaps), NOT as the basis of a
  positive GO core function. Verbatim quoting deferred (no cached full text; the
  reference validator only checks PMID/file: quotes).

## SGD-curated phenotypes (KNOWN, from SGD locus S000000145)

- Null mutant: **increased innate thermotolerance, increased chemical resistance,
  increased UV resistance, decreased stationary-phase survival, decreased
  chronological lifespan, increased competitive fitness**; haploinsufficient;
  abnormal vacuolar morphology; decreased vegetative growth (large-scale).
- Interactions: ~49 total (11 affinity-capture-MS, 26 negative genetic, 8 positive
  genetic, etc.) — no single strong, function-defining partner has emerged.
- "Essential for stationary-phase survival; not required for growth on
  nonfermentable carbon sources; possibly linked with vacuolar transport" (SGD).

## Synthesis of KNOWN

MOH1 is a small, low-abundance, cytoplasmic (inferred) Yippee-family zinc-binding
protein — the single yeast representative of the metazoan YPEL family. Its
structural Zn(2+) site is intact and deeply conserved. Loss of MOH1 makes cells
**more resistant** to multiple lethal stresses (UV, MMS, CPT, heat, hyperosmotic,
H2O2, acetic acid) while impairing **long-term stationary-phase/chronological
survival**; Moh1 is stress-induced. It is functionally interchangeable enough with
human YPEL5 for partial cross-complementation.

## What is NOT known (the deliverable)

1. **Molecular activity.** No biochemical activity is demonstrated. Zinc binding
   (GO:0008270) is predicted from the domain, and the fold is a putative
   binding/scaffold module, but what Moh1 *does* biochemically (binds what? acts
   on what?) is unknown. No catalytic activity is supported.
2. **Direct physical partners / substrates.** Despite ~49 recorded interactions,
   no functionally validated, direct partner or cargo is established. The
   Drosophila Yippee–Hemolin interaction has no yeast counterpart.
3. **Mechanism linking Moh1 to stress resistance and stationary-phase survival.**
   Why does deletion *increase* acute stress resistance yet *decrease* long-term
   survival? The 2025 preprint proposes altered membrane permeability/metabolic
   remodeling, but the causal molecular step (and whether Moh1 acts directly on
   membranes, transcription, or metabolism) is undetermined.
4. **Whether the "pro-apoptotic"/regulated-cell-death framing is the correct
   biological process.** The apoptosis label rests on one heterologous
   complementation study in a contested yeast-apoptosis paradigm.
5. **Subcellular localization.** No reliable curated localization; UniProt/GOA
   record cellular_component unknown (ND). "Possibly linked with vacuolar
   transport" (SGD) is a hypothesis.
6. **Whether Moh1 is actually N-myristoylated in vivo** (predicted in 1998; not
   biochemically confirmed).

## Annotation-review plan

- GO:0000151 ubiquitin ligase complex (IBA, GO_REF:0000033, from PANTHER node
  PTN002302768 seeded by human YPEL5 P62699): **scrutinize.** No yeast evidence
  places Moh1 in a ubiquitin-ligase complex; the IBA is a family-level
  propagation from the Mis18/cereblon(CULT) neighborhood. The Yippee fold is
  related to cereblon's thalidomide-binding CULT domain (which *is* a substrate
  receptor of a CRL4 E3), but Moh1/YPEL proteins are not established E3 components.
  Lean MARK_AS_OVER_ANNOTATED (family over-propagation; not core), unless deep
  research surfaces yeast evidence.
- GO:0008270 zinc ion binding (RCA, PMID:30358795): **KEEP** — corroborated by
  UniProt features and my bioinformatics; the only defensible molecular function.
  Structural zinc, so KEEP_AS_NON_CORE / ACCEPT (it is the core molecular feature
  even if biochemical output is unknown).
- GO:0005575 cellular_component (ND) and GO:0008150 biological_process (ND):
  root/placeholder ND annotations — ACCEPT as-is (standard ND practice; they
  correctly record "unknown").

### Martinez et al. 2004 (Mol Biol Cell) — dedicated stationary-phase genetics (KNOWN)
- Surfaced by the falcon deep-research report and added as PMID:15456898. Genome-wide
  stationary-phase study that identified 32 genes essential for survival in stationary
  phase at 37C; MOH1 is among the stationary-phase-essential set and is NOT required
  for growth on nonfermentable carbon sources — i.e. a specific quiescence-survival
  role, not a generic respiratory defect. [PMID:15456898 "32 genes essential for
  survival in stationary-phase at"]. (MOH1-specific numbers are in the full text; the
  cached record is abstract-only.) The paper also (per full text, via falcon) still
  described Moh1p using the superseded "related to Snf7p" homology and as a
  "myristolated protein of unknown function."

## Deep research outcome (falcon)

The falcon deep-research job completed successfully (~1553 s, Edison Scientific
model, 26 citations) → `MOH1-deep-research-falcon.md`. It is on the correct gene
and organism and independently corroborates every substantive conclusion here: the
Yippee/Mis18/Cereblon β-tent fold with a Zn-coordinating CXXC pair and a
cradle-shaped binding pocket; MOH1 as the single yeast member of the human YPEL1–5
family; stationary-phase-survival requirement (Martinez 2004); and the explicit
conclusion that "MOH1 is not an enzyme, transporter, or structural protein in the
classical sense" but a "small regulatory or adaptor protein" whose "precise
biochemical activity in budding yeast remains unresolved." It adds context sources
(Mis18 centromere biology, cereblon/CULT, FAM72, C. glabrata MOH1 Y5H variant that
did NOT confer echinocandin resistance) but no new yeast molecular function.

## Provenance discipline note

Cached publications are abstract-only (full_text_available: false for
PMID:9748261, 28173693, 30358795, 11240639, 15456898). All PMID supporting_text
quotes are verbatim substrings of the cached abstracts (grep-verified). The 2025
bioRxiv preprint has no PMID and no cached full text; it is cited as context only in
prose, with no fabricated quotes. file: quotes (bioinformatics RESULTS.md, falcon
report) were grep-verified as verbatim substrings before use.
