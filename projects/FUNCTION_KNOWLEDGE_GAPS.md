# Function Knowledge Gaps

What does biology genuinely *not* know about how a gene works — and how do we state it
rigorously enough that someone could close it?

This project builds a curated, literature-grounded register of **function knowledge gaps**:
specific, defensible statements of what is unknown about a gene product's molecular function,
mechanism, partners, or biological role. It is the inverse of the rest of this repository.
Everywhere else we adjudicate what *is* known; here we adjudicate, with the same evidentiary
discipline, what is *not*.

The framing is deliberately ambitious. If a foundation set out to systematically eliminate the
conserved "unknome," the first deliverable would not be more experiments — it would be an honest
map of where the real gaps are, sharp enough to fund. That map is the goal.

## Why this matters: the unknome

Decades into the genomic era, a large fraction of even well-studied proteomes remains
functionally dark:

- ~20% of proteins in well-studied model organisms still lack any informative description of
  their biological role, and many of these are conserved from yeast to human — implying
  fundamental, not peripheral, functions (Wood et al. 2019, *Open Biology*, "Hidden in plain
  sight", PMID:30938578, [DOI](https://doi.org/10.1098/rsob.180241)).
- The Unknome database, which ranks proteins by an evidence-weighted "knownness" score
  (manual annotation = 0.9, electronic = 0.0; "unknown" = score ≤ 1.0), found 23% of human
  protein clusters still below that threshold — down from 43% a decade earlier, i.e. slow
  progress. RNAi screening of 260 conserved-unknown *Drosophila* genes found 62 essential for
  viability and 59 with measurable phenotypes — the dark set is dense with real biology
  (Rocha, Freeman et al. 2023, *PLOS Biology*, PMID:37552676,
  [DOI](https://doi.org/10.1371/journal.pbio.3002222)).

Genes stay dark largely for sociological reasons — research concentrates on what is already
famous (the streetlight effect / Matthew effect; Stoeger et al. 2018, *PLOS Biology*,
PMID:30226837; Edwards et al. 2011, *Nature*, "Too many roads not taken", PMID:21307913). The
same neglected set is over-represented among unsolved Mendelian disease, unannotated GWAS
peaks, and the druggable-but-unexplored proteome (the NIH IDG program; Oprea et al. 2018,
*Nat Rev Drug Discov*, PMID:29472638; Kustatscher et al. 2022, *Nat Methods*, "Understudied
proteins", PMID:35534633). Closing function gaps is the denominator problem under all of these.

## Core principle: a knowledge gap is a curated judgment, not a metric

The central methodological commitment of this project: **a knowledge gap is determined by
reading the primary literature and exercising judgment, not by a pattern in the annotations.**

We tested the alternative and it failed instructively. A score that flags genes with no
specific molecular function (à la Unknome, but using our adjudicated `core_functions`) marks
~14% of our reviewed genes as "MF-dark" — reassuringly close to Wood's ~20% and Unknome's 23%.
But when the conserved subset of those was inspected, "no molecular function" decomposed into
four completely different things:

| What the score called a "gap" | Share | What it actually is | Owner |
|---|---|---|---|
| Structural/accessory subunits (TOM, TRAPP, ESCRT, V-ATPase…) | ~64% | Function *is* "be part of the machine"; the GO MF aspect can't express it | **Ontology** |
| Function-kind known, MF term simply not filled (e.g. SOX9) | ~14% | Curation incompleteness | **Curation** |
| Stub / incomplete reviews (`TODO` descriptions) | ~3% | Data hygiene | — |
| Genuinely unknown mechanism (CFAP300, tam10, P3R3URF…) | ~18% | The true unknome | **Experiment** |

(Snapshot over ~2,100 reviewed genes; proportions are triage-grade, not curated.) A heavily
annotated gene can hide a gaping mechanistic hole; a sparsely annotated one can be perfectly
understood and merely under-curated. **Only reading tells them apart.** The metric is therefore
demoted to a back-of-house triage aid that produces a *read-list*, and never appears in the
product.

## A taxonomy of function knowledge gaps

Two axes. First, *what kind of ignorance* (this determines who can fix it):

1. **Biology gap** — nobody knows. Resolved by experiments. *This is the unknome and the
   project's primary target.*
2. **Curation gap** — the knowledge exists in the literature but is not yet annotated, or is
   annotated too generically. Resolved by curation (much of it in-house).
3. **Ontology gap** — the knowledge exists but no GO term can express it (e.g. "structural
   subunit of complex X", or a novel activity). Resolved by ontology development;
   tracked via `proposed_new_terms`.

Most real entries are a *blend* (CFAP300 below is biology-dominant with an ontology shadow),
and naming the blend is the actionable part.

A useful third framing emerged from curation, cutting across the above: the **residual sub-gap** —
a gene whose *core* function is textbook-solid but which still hides one sharp, load-bearing
mechanistic hole (e.g. RAB9A's unidentified GEF/GAP, RASA1's catalysis-independent scaffolding,
atg101's WF-finger recruit). These are easy to miss precisely because the gene *looks* finished;
flagging them is high-value because the hole is often the rate-limiting unknown for the pathway.

Second, *which GO aspect is dark* — most "dark" genes are not uniformly dark:

- **MF-dark** — process/location known, molecular mechanism unknown (the most common and most
  insidious: rich BP/CC make the gene *look* known). The `protein binding` smell lives here.
- **BP-dark** — an activity is known but not what it is *for* (common in microbial/plant
  metabolism).
- **CC-dark** — function known, but where/when unknown.
- **Wholly dark** — only root terms / IEA / `protein binding` survive review (the deep unknome).

## The unit of work: anatomy of a gap entry

Each gap is a small, defensible scholarly object. Required elements:

- **Gap statement** — the specific unknown, stated precisely. Not "role unclear" but
  "the direct substrate / the catalytic activity / the essential partner is undetermined."
- **Boundary of knowledge** — what *is* established, so the gap is sharply delimited.
- **Provenance for the gap itself** — evidence that the unknown is real and not merely
  uncurated. The gold standard is the field's own admissions: primary-literature hedges
  ("remains to be determined", "the precise role is unknown"), "domain of unknown function"
  names, and a literature *trajectory* that confirms-but-never-mechanizes. Cited with the same
  `[PMID:xxxx "supporting text"]` discipline this repo uses for positive claims.
- **Type judgment** — biology / curation / ontology (or blend), per the taxonomy.
- **Significance** — why closing it matters.
- **What would resolve it** — the experiment, ontology term, or curation action.

This is strictly more than the existing `suggested_questions` field (which asks the right things
but cites nothing): the added value is the **adjudicated boundary plus provenance for the
unknown**.

## Worked example: the CFAP300 molecular-function gap

CFAP300 (formerly C11orf70) is a dynein axonemal assembly factor; loss-of-function causes
primary ciliary dyskinesia (PCD). It is in the KB (`genes/human/CFAP300/`) and is an ideal
exemplar: clear biomedical importance, a clearly established *role*, and a sharp, durable
*mechanistic* silence.

**Boundary (what is firmly known):**
- LOF causes PCD with *combined* outer + inner dynein arm (ODA+IDA) loss; CFAP300 is required
  for cytoplasmic preassembly of axonemal dyneins and their IFT-dependent delivery into the
  axoneme (Höben et al. 2018, *AJHG*, PMID:29727693, [DOI](https://doi.org/10.1016/j.ajhg.2018.03.025);
  Fassad et al. 2018, *AJHG*, PMID:29727692, [DOI](https://doi.org/10.1016/j.ajhg.2018.03.024)).
- Localizes mainly to cytoplasm, moves into cilia by IFT, and interacts with the preassembly
  factor DNAAF2 (Höben 2018).
- Re-confirmed in 2025: LOF → no CFAP300 protein → total ODA+IDA loss (Demchenko et al. 2025,
  *IJMS*, PMID:40806783, [DOI](https://doi.org/10.3390/ijms26157655)).

**Gap statement:** *The biochemical activity of CFAP300 is unknown.* It is unresolved whether
it acts as a chaperone/co-chaperone, a scaffold, or an adaptor; what its client/substrate is;
and whether it acts at one common step upstream of both arm types or in parallel ODA- and
IDA-specific steps.

**Provenance that the gap is real (the judgment):**
1. Both founding papers describe the gene as *"uncharacterized"* and frame the mechanism as a
   **hypothesis** ("supporting our hypothesis that C11orf70 is a preassembly factor") — they
   establish *requirement* and *localization*, never a biochemical activity (PMID:29727692,
   PMID:29727693).
2. Its sole domain is **DUF4498 — a "domain of unknown function"**
   (`genes/human/CFAP300/CFAP300-deep-research-falcon.md`).
3. **The trajectory is the strongest evidence:** seven years and many cohorts on (Polish 2019
   PMID:30916986; Cypriot 2021 PMID:33715250; Russian 2024 PMID:39180133; ALI-culture 2025
   PMID:40806783), every follow-up is *diagnostic* — confirming loss — not *mechanistic*. A
   durable mechanistic silence despite clear motivation is the signature of a genuine gap, and
   reading the arc of the literature is the only way to see it.

**Type judgment:** biology gap (dominant) with an ontology shadow — even "a dynein-preassembly
factor" has no adequate GO MF term, which is why the gene reads as MF-dark.

**Significance:** this is the assembly step whose failure removes *all* axonemal dynein motors —
mechanistically central to motile ciliopathy.

**What would resolve it:** proximity/affinity proteomics of the CFAP300–DNAAF2 module;
in vitro reconstitution of dynein assembly intermediates; structural characterization of
DUF4498.

## Worked gap entries (from the seed read-list)

The following entries were curated by reading each gene's `-deep-research-*.md` and notes/GOA
files for the field's *own* statements of ignorance, in the CFAP300 format but condensed. Every
PMID cited below was independently verified against PubMed; ignorance quotes are reproduced
verbatim and attributed to the source file. Where a gene's deep-research file cited sources only
by DOI, or by PMIDs that failed verification, the gap is provenance-anchored to the **file path**
rather than to an unverified PMID (see the KCTD14 caution).

### swrD (BACSU) — ~71-aa swarming-motility factor

- **Boundary:** Required for swarming on soft agar; increases per-flagellum motor torque/power at
  the level of MotAB **stator activity** (not stator abundance); deletion cuts single-flagellum
  torque ~6-fold and is rescued by *motAB* overexpression (Hall et al. 2018, *J Bacteriol*,
  PMID:29061663, [DOI](https://doi.org/10.1128/JB.00529-17)). GOA carries only one BP term
  (GO:0071978, swarming motility) — no MF, no CC.
- **Gap statement:** SwrD's direct binding partner(s), biochemical activity, membrane/motor
  localization, and structural domain are undefined.
- **Provenance (verbatim):** *"they proposed that SwrD may reduce stator dynamism by facilitating
  stator retention at the motor, but were unable to directly visualize stator dynamics due to
  nonfunctional fluorescent fusions—thus mechanistic details remain hypothetical"*; *"Experimental
  localization of SwrD ... remains undetermined"*; *"no resolved structural domain showing
  stomatin/SPFH"* (`genes/BACSU/swrD/swrD-deep-research-falcon.md`).
- **Type:** biology gap (primary) with an ontology/curation shadow — genetics support an MF in
  stator/torque modulation, but no MF term is assignable.
- **Resolve:** functional tagged-SwrD co-IP + super-resolution to test direct MotAB binding/
  retention; in vitro reconstitution or cryo-EM of the SwrD–stator interface.

### mxaC (METEA) — methanol-oxidation auxiliary VWA protein

- **Boundary:** In the *mxa* methanol-oxidation cluster and genetically required for methanol
  oxidation — the founding paper states *mxaC* is required while "the function of the other two
  genes is still unknown" (Morris et al. 1995, *J Bacteriol*, PMID:7592474,
  [DOI](https://doi.org/10.1128/jb.177.23.6825-6831.1995)). Encodes a von Willebrand factor A
  (VWA) domain protein; recent work implicates it in Ca²⁺ loading during methanol-dehydrogenase
  (MDH) maturation alongside a MoxR AAA+ ATPase module (Zhou et al. 2025, *Nat Commun* — cited by
  DOI in the file; no PMID present).
- **Gap statement:** Whether MxaC's VWA/MIDAS domain itself binds Ca²⁺, and how it delivers Ca²⁺
  into the MxaF active site (adaptor vs scaffold vs transporter), is undemonstrated.
- **Provenance (verbatim):** *"Direct physical interaction data (e.g., co-purification of MxaC with
  MxaR) are not shown in the retrieved excerpts."*; *"There is no direct localization assay for
  MxaC in the retrieved materials..."* (`genes/METEA/mxaC/mxaC-deep-research-falcon.md`); *"Does
  MxaC directly bind Ca²⁺ through its vWFA domain?"* (`genes/METEA/mxaC/mxaC-notes.md`).
- **Type:** biology gap (primary) + ontology gap (no GO term for "metal incorporation into
  metalloenzyme" / MDH-complex assembly).
- **Resolve:** MIDAS-mutant Ca²⁺-binding assays on purified MxaC; cryo-EM / co-purification of the
  MxaR/S/C/L module with MDH maturation intermediates.

### TRAPPC12 (human) — moonlighting TRAPP subunit

- **Boundary:** Bona fide TRAPP subunit acting at an early stage of ER-to-Golgi trafficking
  (Scrivens et al. 2011, *Mol Biol Cell*, PMID:21525244,
  [DOI](https://doi.org/10.1091/mbc.E10-11-0873)); member of TRAPPIII/autophagy machinery (Kim et
  al. 2016 review, PMID:27066478, [DOI](https://doi.org/10.3389/fcell.2016.00020)). Separately, a
  mitotic "moonlighting" role: depletion gives noncongressed chromosomes and mitotic arrest, it
  regulates CENP-E recruitment to kinetochores, and is phospho-cycled through mitosis (Milev et al.
  2015, *J Cell Biol*, PMID:25918224, [DOI](https://doi.org/10.1083/jcb.201501090)).
- **Gap statement:** The molecular mechanism of the mitotic kinetochore function — and how it is
  biochemically partitioned from the TRAPP trafficking role — is undefined; the CENP-E interaction
  is captured only as uninformative `protein binding`.
- **Provenance (verbatim):** *"TRAMM cycles between its role in TRAPP in interphase cells, and its
  newly identified roles during mitosis"*; *"Small amounts of TRAMM associated with chromosomes"*
  (`genes/human/TRAPPC12/TRAPPC12-notes.md`, re PMID:25918224).
- **Type:** blend — biology gap (mechanism of the second, non-TRAPP pool) + curation/ontology gap
  (CENP-E recruitment under-captured as `protein binding`).
- **Resolve:** separation-of-function/domain-mapping mutants that uncouple kinetochore binding from
  TRAPP assembly; mitotic-phase proximity proteomics of the non-TRAPP TRAMM pool.

### AGR3 (human) — noncanonical PDI-family protein

- **Boundary:** ER-resident thioredoxin/PDI-family protein restricted to ciliated airway
  epithelium; required for Ca²⁺-mediated regulation of ciliary beat frequency and mucociliary
  clearance but **not** for ciliogenesis (Bonser et al. 2015, *Am J Respir Cell Mol Biol*,
  PMID:25751668, [DOI](https://doi.org/10.1165/rcmb.2014-0318OC)); binds α-dystroglycan and C4.4a
  by yeast two-hybrid in a cancer context (Fletcher et al. 2003, *Br J Cancer*, PMID:12592373,
  [DOI](https://doi.org/10.1038/sj.bjc.6600740)). Has a noncanonical thioredoxin motif (DCYQS,
  lacking the second catalytic cysteine of CXXC PDIs).
- **Gap statement:** Whether AGR3's noncanonical motif retains any thiol-disulfide catalytic
  activity, what its physiological substrates/folding clients are, and the receptor that mediates
  extracellular-AGR3 signaling, are all unknown.
- **Provenance (verbatim):** *"no definitive AGR3-specific enzymatic substrate, direct folding
  client, or biochemical turnover measurement is established"*; *"much of AGR3 biochemistry remains
  inferential rather than directly measured"* (`genes/human/AGR3/AGR3-deep-research-falcon.md`).
- **Type:** biology gap (primary) + curation gap (GOA carries only generic `protein binding` plus a
  single experimental `dystroglycan binding`; no MF for the core ciliary/Ca²⁺ role).
- **Resolve:** thiol-disulfide / reductase assays on WT vs catalytic-Cys-mutant AGR3 plus
  proximity labeling for ER clients; identify the surface receptor for extracellular AGR3.

### tam10 (SCHPO) — meiotic sequence orphan

- **Boundary:** Bona fide protein-coding gene (RT-PCR / RNA-seq / RACE confirmed), named for
  "transcripts altered in meiosis"; deletion is viable / non-essential under standard conditions;
  the only direct functional GO terms (RNA binding, nucleolus) are ISO/ISS transfers, never
  validated in *S. pombe* (`genes/SCHPO/tam10/tam10-deep-research.md`; `tam10-goa.tsv`).
- **Gap statement:** No experimentally determined molecular activity, RNA/protein substrate,
  partner, or in vivo role exists; the RNA-binding/nucleolus annotations are unverified
  computational transfers.
- **Provenance (verbatim):** *"no specific molecular function has been ascribed to Tam10"*;
  *"classifying it as a 'sequence orphan' with no obvious homology to characterized proteins"*
  (`tam10-deep-research.md`); *"No evidence-supported enzymatic activity, substrate specificity,
  transport substrate, or pathway membership can be asserted."* (`tam10-deep-research-falcon.md`).
  (The two providers even disagree on whether it has any annotatable domain.)
- **Type:** blend — biology gap (primary) + curation gap (unverified ISO/ISS; provider
  disagreement on domain content).
- **Resolve:** GFP localization + AP-MS / CLIP to test the predicted nucleolar/RNA-binding role;
  meiosis-specific phenotyping of *tam10Δ* (sporulation, spore viability, meiotic timing).

### P3R3URF (human) — uORF microprotein (non-canonical-ORF dark matter)

- **Boundary:** Protein-coding locus encoding a ~95-aa microprotein from an ORF upstream of
  *PIK3R3*; UniProt evidence at protein level (PE1); testis / late-spermatid enriched; the sole
  GOA term is **IBA** (GO:0019221, cytokine-mediated signaling — phylogenetic inference, not
  experiment) (`genes/human/P3R3URF/P3R3URF-deep-research-openai.md`; `P3R3URF-goa.tsv`).
- **Gap statement:** Whether the microprotein is stably expressed as an independent protein, where
  it localizes, and what its molecular function/partner is — every current functional claim is
  computational inference.
- **Provenance (verbatim):** *"direct, P3R3URF-specific functional evidence is very limited in the
  accessible corpus"*; *"Primary function ... Unknown in the accessible corpus."*
  (`P3R3URF-deep-research-falcon.md`); *"While direct experimental evidence is still lacking..."*
  (`P3R3URF-deep-research-openai.md`). In the one dataset that tested for it, the transcript was
  not detected.
- **Type:** blend — biology gap (primary) + curation gap (IBA-only term risks conflation with
  canonical PIK3R3 / p55γ).
- **Resolve:** mass-spec detection of a P3R3URF-unique peptide + Ribo-seq initiation evidence in
  testis; ORF-specific perturbation (sparing the PIK3R3 CDS) with interactome/localization readout.
- This is the deliberately-included *"we did not even know there was a player"* frontier.

### KCTD14 (human) — least-studied KCTD-family BTB protein *(with a provenance caution)*

- **Provenance caution:** the KCTD14 `-deep-research-cyberian.md` file cites PMIDs that fail
  verification — e.g. its "PMID:30929316" is an SGLT/endothelial-senescence paper and its
  "PMID:36362138" is a xylanase paper, neither about KCTD14. This entry is therefore anchored to
  **file paths and the verifiable MGI statement only**; the unverified structural/CUL3 claims are
  reported as *claims in the deep-research file*, not as established facts. (A live example of why
  this project verifies every PMID.)
- **Boundary:** small BTB/POZ-domain member of the 26-protein KCTD family; forms homo-oligomers
  (IEA, GO:0051260). The deep-research files report (unverified) that it does *not* form a stable
  CUL3 complex and so is unlikely to be a canonical CRL3 substrate adaptor. GOA carries only
  homo-oligomerization (IEA) plus generic `protein binding`.
- **Gap statement:** Its biochemical activity, bona fide substrate/partner, and biological process
  are unknown (does it bind CUL3 at all? what, if anything, does it target?).
- **Provenance (verbatim):** *"MGI reports that there is no experimental evidence to support
  Molecular Function, Biological Process, or Cellular Component annotations for Kctd14 following
  literature review"* (`genes/human/KCTD14/KCTD14-deep-research-cyberian.md`); *"there are no
  specific enzymatic activities or substrates definitively attributed to it yet, and it has not
  been conclusively tied to a particular signaling pathway or genetic disorder"*
  (`genes/human/KCTD14/KCTD14-deep-research-openai.md`).
- **Type:** biology gap (primary) + curation gap (literature interactors uncaptured; GOA holds only
  IEA oligomerization + generic binding).
- **Resolve:** endogenous AP-MS to fix the partner/substrate, plus a CUL3 co-IP to confirm the
  reported negative; knockout/knockdown phenotyping with proteomics to assign a process.

### C18orf21 (human) — ORF-named gene, a *closing* gap

- **Boundary:** 220-aa UPF0711-family protein with a single DUF4674 domain and no enzymatic motifs;
  ubiquitously expressed, nucleolar-enriched; a recurrent CRISPR fitness-screen hit. 2025 preprints
  propose it is a metazoan **RNase MRP-specific subunit** (alias RMRPP1) required for pre-rRNA
  processing (`genes/human/C18orf21/C18orf21-deep-research.md`;
  `C18orf21-deep-research-falcon.md`).
- **Gap statement:** Whether C18orf21 is genuinely a constitutive RNase MRP RNP subunit (and its
  mechanistic role in RMRP stabilization / pre-rRNA cleavage) versus an uncharacterized DUF4674
  protein is not yet established in peer-reviewed, GO-curated form.
- **Provenance (verbatim):** *"evolutionarily conserved protein of 220 amino acids with no
  well-characterized biochemical function"*; *"current databases report no defined Gene Ontology
  molecular function for this gene"*; *"To date, there are no published studies focusing
  exclusively on C18orf21's function."* (`C18orf21-deep-research.md`).
- **Type:** curation / recency gap (leaning) — function-defining evidence currently exists only as
  2025 bioRxiv preprints (no PMIDs) and has not propagated to GOA (empty) or UniProt (still
  "UPF0711").
- **Resolve:** peer-reviewed validation of RNase MRP-specific membership (reciprocal AP-MS vs
  RPP21; RIP-seq showing RMRP, not RPPH1, enrichment) plus a pre-rRNA-processing readout.
- A clean illustration of a *closing* gap — and of why preprint-only evidence must **not** be
  auto-annotated.

## Worked gap entries — second batch (read-list deepening)

Curating the un-vetted leads surfaced a useful third category alongside the wholly-dark genes:
the **residual sub-gap** — a gene whose *core* function is textbook-solid, but which still hides a
sharp, specific mechanistic hole (RAB9A's missing GEF/GAP, RASA1's catalysis-independent
scaffolding, atg101's WF-finger recruit). These matter because a heavily annotated gene can *look*
finished while a load-bearing mechanism is undetermined — exactly the failure mode the project's
core principle warns about. All eight leads adjudicated to **real gaps** (none were spurious);
every PMID below was PubMed-verified, and one mis-attributed citation was caught and dropped.

### MTC7 (yeast / *S. cerevisiae*) — telomere-capping sequence orphan

- **Boundary:** small ~139-aa basic protein; *mtc7Δ* clusters genetically with short-telomere /
  telomere-maintenance deletions and is synthetically sick with *cdc13-1* in a genome-wide screen
  (Addinall et al. 2008, *Genetics* — cited in the files only by DOI/PMC, no verified PMID;
  [DOI](https://doi.org/10.1534/genetics.108.092577)). GOA marks every functional aspect **ND**
  (no data) plus one IEA membrane keyword.
- **Gap statement:** Mtc7's biochemical activity, substrate/partner, and the mechanism by which it
  influences telomere capping/length are entirely unknown.
- **Provenance (verbatim):** *"MTC7 (YEL033W) encodes a protein of unknown molecular function. No
  enzymatic activity or specific biochemical function has been demonstrated to date"*
  (`genes/yeast/MTC7/MTC7-deep-research.md`); *"No study in the retrieved corpus provides a direct
  molecular function for Mtc7 ... MTC7 remains functionally unannotated mechanistically"*
  (`genes/yeast/MTC7/MTC7-deep-research-falcon.md`).
- **Type:** biology gap (primary) + curation gap (a telomere-maintenance BP is arguably capturable
  from the genetic evidence as IGI, yet GOA still carries only ND).
- **Resolve:** AP-MS / Y2H for physical partners; GFP localization + telomere-length / TPE assays
  in *mtc7Δ*.

### RAB9A (human) — known Rab, unknown switch *(residual sub-gap)*

- **Boundary:** endosome-to-TGN retrograde Rab GTPase that recycles mannose-6-phosphate receptors
  (Lombardi et al. 1993, *EMBO J*, PMID:8440258,
  [DOI](https://doi.org/10.1002/j.1460-2075.1993.tb05701.x)); has well-defined effectors including
  the p40 effector (Díaz et al. 1997, *J Cell Biol*, PMID:9230071,
  [DOI](https://doi.org/10.1083/jcb.138.2.283)) and TIP47/GCC185 (deep-research files).
- **Gap statement:** The specific GEF that activates RAB9A on late endosomes and the GAP that
  inactivates it have not been definitively identified.
- **Provenance (verbatim):** *"the specific guanine nucleotide exchange factor (GEF) that activates
  RAB9A and the GTPase-activating protein (GAP) that inactivates it have not been definitively
  identified"* (`genes/human/RAB9A/RAB9A-deep-research-cyberian.md`); *"Regulators specific to
  RAB9A (cognate GEFs/GAPs) ... remain less well defined"*
  (`genes/human/RAB9A/RAB9A-deep-research-falcon.md`). (A claim in the openai file that DENND2 is
  the GEF rests on a general DENN-domain paper covering *other* Rabs, not RAB9A — an
  over-extrapolation that reinforces that no validated RAB9A GEF exists.)
- **Type:** biology gap — the regulators are genuinely undiscovered.
- **Resolve:** in vitro GEF assays across candidate DENN-domain GEFs; a TBC-domain GAP screen with
  a CI-MPR mis-sorting readout on knockdown.

### RASA1 (human) — catalysis solved, scaffolding unsolved *(residual sub-gap)*

- **Boundary:** p120 RasGAP; accelerates Ras GTP hydrolysis ~10⁵-fold via the arginine finger
  Arg789, structurally defined with the transition-state (AlF) mimic (Scheffzek et al. 1997,
  *Science*, PMID:9219684, [DOI](https://doi.org/10.1126/science.277.5324.333)); multidomain
  (SH2-SH3-SH2, PH, C2, GAP) with tandem-SH2 phosphotyrosine engagement
  (`genes/human/RASA1/RASA1-deep-research-falcon.md`).
- **Gap statement:** The molecular mechanism of RASA1's GAP-activity-**independent** (scaffolding)
  functions — e.g. how p190RhoGAP recruitment drives directed cell movement and contributes to
  blood-vessel formation independently of its own Ras-GAP activity — is unresolved.
- **Provenance (verbatim):** *"Experimental evidence indicates RASA1 is necessary for directed cell
  movement in vitro, and this role depends on its ability to recruit p190^RhoGAP (independent of
  RASA1's own Ras-GAP activity)"*; *"the embryonic blood vessel defects in RASA1-null embryos are
  partly due to Ras-independent actions of RASA1"* (`RASA1-deep-research-openai.md`); *"How these
  two functions are coordinated, and whether they can be separated therapeutically, warrants
  further study."* (`RASA1-deep-research-cyberian.md`).
- **Type:** blend — biology gap (the scaffolding mechanism is unresolved) + curation gap (GO
  captures the catalytic GAP branch; the p190RhoGAP-recruitment role in migration is
  under-annotated).
- **Resolve:** GAP-dead (Arg789) vs scaffold-dead (SH2/SH3) separation-of-function knock-ins
  scoring migration / vascular tube formation; BioID of GAP-dead RASA1 to map the
  catalysis-independent interactome.

### BAIAP2L2 (human) — Pinkbar, dark in its native tissue

- **Boundary:** epithelial I-BAR/IMD protein ("Pinkbar") that binds phosphoinositide membranes and
  generates planar membrane sheets, localizing to Rab13 vesicles and intercellular junctions in
  intestine/kidney (Pykäläinen et al. 2011, *Nat Struct Mol Biol*, PMID:21743456,
  [DOI](https://doi.org/10.1038/nsmb.2079)). In cochlear hair cells it is a row-2 stereocilia-tip
  component (deep-research files).
- **Gap statement:** The molecular function of BAIAP2L2/Pinkbar in its name-defining native
  intestinal/renal epithelium — what membrane/junctional structure it builds, and through which
  partner — is unknown, because knockout mice show no overt epithelial phenotype.
- **Provenance (verbatim):** *"mice lacking BAIAP2L2 display normal kidney and colon tissue
  morphology and maintain normal electrolyte homeostasis and tissue architecture under
  physiological conditions"*; *"BAIAP2L2's relationship to microvillar formation and maintenance in
  intestinal brush borders remains incompletely understood."*
  (`genes/human/BAIAP2L2/BAIAP2L2-deep-research-perplexity.md`).
- **Type:** biology gap (primary; the epithelial MF was never measured) + curation gap (the
  epithelial GO terms are IEA/ISS/IBA inferences).
- **Resolve:** challenge-condition / conditional-KO phenotyping of intestinal & renal epithelium
  (barrier integrity, brush-border architecture under stress); Pinkbar proximity-labeling
  interactome in polarized enterocytes.

### SCGB1C1 (human) — orphan secretoglobin

- **Boundary:** small secreted secretoglobin-fold protein localized to Bowman's glands of the
  olfactory mucosa, with a hydrophobic cavity capable of binding small ligands; in a mouse
  OVA-asthma model, recombinant SCGB1C1 suppressed Th2 inflammation and expanded Tregs (Kim et al.
  2024, *Int J Mol Sci*, PMID:38892470, [DOI](https://doi.org/10.3390/ijms25116282)). GOA carries
  only a single IEA extracellular-region term.
- **Gap statement:** The endogenous physiological ligand(s) SCGB1C1 binds in vivo, and the
  cell-surface receptor / signaling mechanism behind its immunomodulatory (Treg-expanding) effect,
  are unidentified.
- **Provenance (verbatim):** *"The specific hydrophobic ligands that SCGB1C1 binds in vivo remain
  incompletely characterized."*; *"The exact receptors and signaling cascades through which SCGB1C1
  mediates these immunomodulatory effects remain to be definitively identified, representing an
  important area for future investigation."* (`SCGB1C1-deep-research-perplexity.md`).
- **Type:** biology gap (ligand + receptor genuinely undiscovered) + curation gap (only one IEA CC
  term; the established secretoglobin fold and the mouse phenotype are uncaptured).
- **Resolve:** a biochemical ligand-binding screen (lipidomic / odorant affinity) on recombinant
  human SCGB1C1; receptor identification by pulldown/proximity-labeling on Tregs + LOF validation.

### FGFRL1 (human) — a receptor that signals without a kinase

- **Boundary:** atypical FGFR with three Ig-like ectodomains but **no** tyrosine-kinase domain;
  binds FGF ligands and heparin and acts as a decoy receptor (Trueb et al. 2003, *J Biol Chem*,
  PMID:12813049, [DOI](https://doi.org/10.1074/jbc.M300281200)); forms constitutive dimers and
  mediates HSPG-dependent cell adhesion (Rieckmann et al. 2007, *Exp Cell Res*, PMID:18061161,
  [DOI](https://doi.org/10.1016/j.yexcr.2007.10.029)); essential for kidney, diaphragm and skull
  development, with the cytoplasmic tail dispensable (deep-research files).
- **Gap statement:** The precise molecular mechanism by which kinase-dead FGFRL1 modulates
  FGF/FGFR signaling in vivo (pure ligand sink vs inhibitory FGFR complexes vs intracellular
  Sprouty/Spred recruitment), and the identity of its Ig3 cell-fusion partner, are unknown.
- **Provenance (verbatim):** *"manipulating FGFRL1 levels in vitro did not measurably change cell
  proliferation or ERK phosphorylation"*; *"How exactly does FGFRL1 regulate FGF signaling in vivo?
  Is it purely by sequestering FGFs (acting as a sink), or does it form inhibitory complexes with
  the signaling receptors?"*; *"The 'target protein' involved in FGFRL1-mediated cell fusion is
  currently unknown."* (`genes/human/FGFRL1/FGFRL1-deep-research.md`).
- **Type:** biology gap (primary; transduction mechanism undetermined) + curation gap (the GOA term
  `GO:0005007` "fibroblast growth factor receptor activity" overstates canonical signaling for a
  kinase-dead receptor — a candidate MODIFY).
- **Resolve:** FGFRL1–FGFR1/2/3/4 co-IP + live-cell co-imaging during ligand stimulation to test
  sink-vs-complex models; a fusion-defective Ig3 point-mutant knock-in plus a screen for the Ig3
  partner.

### atg101 (SCHPO) — known subunit, unknown recruit *(residual sub-gap)*

- **Boundary:** core subunit of the *S. pombe* Atg1/ULK autophagy-initiation complex (Yu et al.
  2021, *J Cell Sci*, PMID:34499173, [DOI](https://doi.org/10.1242/jcs.258774)); forms an obligate
  HORMA heterodimer that stabilizes the Atg13 HORMA domain, and its conserved "WF finger" recruits
  downstream factors (Suzuki et al. 2015, *Nat Struct Mol Biol*, PMID:26030876,
  [DOI](https://doi.org/10.1038/nsmb.3036)).
- **Gap statement:** The molecular identity of the downstream factor(s) recruited by the Atg101
  WF-finger surface in *S. pombe* is unknown, despite that surface being genetically required for
  autophagy independent of Atg13 binding.
- **Provenance (verbatim):** *"A WF-finger triple mutant (W110A, P111A, F112A) retained Atg13
  binding but impaired autophagy, indicating Atg101 has functional roles beyond stabilizing/binding
  Atg13."* (`atg101-deep-research-falcon.md`; the underlying WF-finger result is from a thesis, no
  PMID); *"The precise protein targets of the WF finger motif remain incompletely characterized,
  though WIPI family proteins represent likely candidates."* (`atg101-deep-research-perplexity.md`).
- **Type:** biology gap (the binding partner is unidentified) + minor curation gap (no MF term for
  the WF-finger recruitment; the key evidence sits in an uncited thesis, not a curatable PMID).
- **Resolve:** IP-MS comparing WT vs WF-finger AAA mutant in starved *S. pombe*; targeted binding
  tests against candidate WIPI / Atg18 orthologs.

### irg-1 (worm) — famous reporter, mystery protein

- **Boundary:** intestinal infection-response gene transcriptionally induced by *Pseudomonas
  aeruginosa* via the bZIP factor ZIP-2 (Estes et al. 2010, *PNAS*, PMID:20133860,
  [DOI](https://doi.org/10.1073/pnas.0914643107)); annotated to antibacterial innate immune
  response by IEP (expression) evidence; the protein carries predicted NADAR/YbiA-like domains (a
  domain prediction only).
- **Gap statement:** The actual biochemical/enzymatic activity of the IRG-1 protein — whether its
  predicted NADAR/YbiA-like domain confers a real catalytic function, and on what substrate — is
  undefined; everything known concerns its transcriptional *induction*, not what the protein
  *does*. GOA records `molecular_function` as **ND**.
- **Provenance (verbatim):** *"irg-1 enables GO:0003674 molecular_function ... ND"*
  (`genes/worm/irg-1/irg-1-goa.tsv`); *"Despite domain predictions (NADAR/YbiA-like), no direct
  enzymatic reaction, substrate specificity, or transport function has been experimentally defined
  for the IRG-1 protein in C. elegans."* (`genes/worm/irg-1/irg-1-deep-research-falcon.md`).
- **Type:** biology gap (MF genuinely unknown), honestly reflected as an MF ND annotation — not a
  curation/ontology defect. A clean BP-known / MF-dark exemplar.
- **Resolve:** assay recombinant IRG-1 for NADAR-family activity (NAD / ADP-ribose-related
  hydrolase) against candidate substrates; structure-guided catalytic-residue mutagenesis + rescue.

## Methodology

For each candidate gene:

1. **Deep literature search** — use cached publications, the gene's `-deep-research-*.md`,
   PubMed, and full text where available. Read primarily for the *boundary* and for the field's
   *own statements of ignorance*.
2. **Harvest ignorance signals** — author hedges ("remains unknown / unclear / to be
   determined"), DUF / "uncharacterized" / hypothetical-protein naming, orphan-activity vs
   orphan-gene framing, and the diagnostic-not-mechanistic trajectory.
3. **Judge the type** — separate biology gaps from curation gaps from ontology gaps. This is
   the irreducible human/curatorial step.
4. **Write the gap entry** with full provenance.
5. **Route it** — experiment (suggested_experiments), ontology (proposed_new_terms), or
   curation (a normal review action).

Selection of *which genes to read* is curatorial, in the spirit of PomBase's "priority
unstudied genes" determination (Wood 2019) — informed, but not decided, by the triage
read-list.

## Relation to existing KB machinery

The building blocks already exist and are reused, not replaced:

| Signal | Existing field | Gap role |
|---|---|---|
| Open questions | `suggested_questions` | Seed for biology-gap statements (to be elevated with provenance) |
| Proposed experiments | `suggested_experiments` | The "what would resolve it" |
| Missing GO terms | `proposed_new_terms` | Ontology-gap entries |
| Unresolvable annotation | `action: UNDECIDED` | Often a curation gap (esp. literature inaccessible) |
| `protein binding` avoidance rule | curation guideline | Flags MF-mechanism gaps |

**Schema direction (deferred):** the cleanest long-term home would elevate `suggested_questions`
into a provenance-bearing `knowledge_gaps` structure (gap statement + boundary + `supported_by`
quotes + type) so gaps become first-class and queryable. We are *not* committing to a schema
change here; this project first proves the unit and the method on curated examples.

## Prioritization (curatorial, not computed)

When choosing what to read next, weight toward gaps that are both high-value and tractable:

- **Conservation depth** — LECA-deep conservation implies fundamental function (Wood filter).
- **Disease / GWAS / IDG overlap** — for human genes; the funder hook. (Disease-mechanism
  prioritization can be handed to / shared with Monarch's dismech.)
- **A coevolution handle** — phylogenetic-profile or co-expression clustering with a *known*
  module gives instant guilt-by-association and a ready hypothesis.
- **Microproteins / smORFs / non-canonical ORFs** — a deliberately included frontier where the
  gap is "we did not even know there was a player" (e.g. P3R3URF).

## Seed read-list (triage candidates — to be read, not yet curated)

From the conserved-MF-dark triage, after stripping structural-subunit and curation-completeness
false positives. These are *candidates for deep reading*; the eight marked **worked** now have
gap entries above.

| Gene | Org | Status | Why interesting |
|---|---|---|---|
| CFAP300 | human | **worked** | Dynein preassembly; mechanism unknown; DUF4498 (full exemplar) |
| P3R3URF | human | **worked** | 95-aa microprotein from a uORF; non-canonical-ORF dark matter |
| tam10 | SCHPO | **worked** | Meiotic sequence orphan; only ISO/ISS transfers |
| AGR3 | human | **worked** | Noncanonical PDI-family; catalytic activity / clients unknown |
| swrD | BACSU | **worked** | ~71-aa swarming-motility enhancer; mechanism unknown |
| mxaC | METEA | **worked** | VWA auxiliary protein for methanol oxidation; mechanism unknown |
| TRAPPC12 | human | **worked** | Moonlighting TRAPP factor; mitotic function ill-defined |
| KCTD14 | human | **worked** | Least-studied KCTD BTB protein; no MF/BP/CC evidence (MGI) |
| C18orf21 | human | **worked** | ORF-named; a *closing* gap (2025 RNase MRP preprints) |
| MTC7 | yeast | **worked** | Telomere-capping sequence orphan; all GO aspects ND |
| RAB9A | human | **worked** | *Residual sub-gap*: known Rab, cognate GEF/GAP unidentified |
| RASA1 | human | **worked** | *Residual sub-gap*: catalysis solved, scaffolding mechanism unsolved |
| BAIAP2L2 | human | **worked** | Pinkbar; native epithelial function unmeasured (KO normal) |
| SCGB1C1 | human | **worked** | Orphan secretoglobin; ligand + receptor unidentified |
| FGFRL1 | human | **worked** | Kinase-dead FGFR; signaling mechanism unresolved |
| atg101 | SCHPO | **worked** | *Residual sub-gap*: WF-finger recruitment partner unknown |
| irg-1 | worm | **worked** | BP-known / MF-dark; IRG-1 protein activity undefined (MF ND) |

### Reproducible read-list (ignorance-signal scan)

A grep of every `genes/**/*-deep-research-*.md` for author hedges (`remains unknown / unclear /
undetermined / elusive / uncharacterized / to be determined`) and for `precise (function|role|
mechanism) ... (unknown|unclear|not)` surfaced **~60 files** carrying explicit ignorance
statements — a reproducible candidate pool beyond the triage table. The strongest leads from that
scan have now been curated (the second-batch entries above); remaining un-vetted clusters worth
reading next include the METEA *mxa/mll/xox* methanol-oxidation auxiliary genes (mllA/F/G/H/J,
mxbM, mxcQ, xoxG, mluI) as a group, plus human/MAP7D1, human/POLE4, human/AP3B2, and SCHPO/atg2.

> **Curation caution (learned here):** deep-research files frequently cite sources only by DOI,
> and some cite PMIDs that do not resolve to the right paper (e.g. the KCTD14 cyberian file). Every
> PMID promoted into a gap entry must be verified against PubMed before use; otherwise anchor the
> gap to the deep-research **file path** and verbatim quote.

## Prior art and references

- Wood et al. 2019, *Open Biology* — "Hidden in plain sight" (PMID:30938578)
- Rocha, Freeman et al. 2023, *PLOS Biology* — Functional unknomics / Unknome database (PMID:37552676)
- Stoeger et al. 2018, *PLOS Biology* — why important genes are ignored (PMID:30226837)
- Edwards et al. 2011, *Nature* — "Too many roads not taken" (PMID:21307913)
- Oprea et al. 2018, *Nat Rev Drug Discov* — unexplored therapeutic genome / IDG (PMID:29472638)
- Kustatscher et al. 2022, *Nat Methods* — understudied proteins initiative (PMID:35534633)
- de Crécy-Lagard et al. 2025 — enzymes/proteins of unknown function, prediction error types (PMID:40703034)
- Related internal projects: `STRUCTURE_FUNCTION.md` (dark proteome via structure),
  `IBA_REVIEW.md` (how orthology propagation manufactures false knowledge),
  `OVER_ANNOTATION_PATTERNS.md` (annotation that masks gaps).
- External model: monarch-initiative/dismech — Claude-Code-curated disease-mechanism KB with
  the same per-record-YAML + verbatim-quote evidentiary discipline; derives gap/priority
  dashboards over its corpus.

## Status

- [x] Literature scan (unknome / Wood; Unknome database; dismech approach)
- [x] Survey of how gaps are captured in the KB today
- [x] Core principle established: gaps are curated judgments, not metrics
- [x] Gap taxonomy (biology / curation / ontology; MF/BP/CC darkness)
- [x] Unit defined (anatomy of a gap entry)
- [x] One worked exemplar (CFAP300)
- [x] Curate the seed read-list into worked gap entries (8 added: swrD, mxaC, TRAPPC12, AGR3, tam10, P3R3URF, KCTD14, C18orf21; all cited PMIDs PubMed-verified)
- [x] Reproducible ignorance-signal read-list established (~60 deep-research files)
- [x] Read-list deepening, batch 2 (8 added: MTC7, RAB9A, RASA1, BAIAP2L2, SCGB1C1, FGFRL1, atg101, irg-1; all adjudicated to real gaps; PMIDs PubMed-verified)
- [x] Third gap framing identified: the *residual sub-gap* of otherwise well-characterized genes
- [ ] Read-list deepening, batch 3: METEA mxa/mll/xox cluster, MAP7D1, POLE4, AP3B2, atg2
- [ ] Decide unit granularity (per-gap vs per-gene narrative)
- [ ] Decide home: standalone register vs `knowledge_gaps` schema element (deferred)
- [ ] Conservation / disease prioritization pass over candidates

## Notes

- 2026-06: Project initiated. Brainstorm grounded in (a) the unknome literature, (b) the
  dismech curation model, and (c) how gaps are recorded in this KB today. Key finding from a
  throwaway triage script: apparent "missing molecular function" is dominated (~64% of the
  conserved subset) by GO's inability to describe complex *subunits*, not by true ignorance —
  reinforcing that the gap call must be made by reading, not counting. CFAP300 curated as the
  first worked exemplar.
- 2026-06: Eight seed-list genes curated into worked gap entries by reading their
  `-deep-research-*.md` / notes / GOA for the field's own ignorance statements (verbatim quotes).
  Established a reproducible "ignorance-signal grep" over deep-research files (~60 hits) as a
  standing read-list. Verified every promoted PMID against PubMed and caught a deep-research file
  (KCTD14 cyberian) citing PMIDs that resolve to unrelated papers — codified the verify-or-anchor-
  to-file-path rule. *Span of gap types now covered:* enzyme-adjacent bacterial (swrD, mxaC),
  moonlighting eukaryotic (TRAPPC12), noncanonical-fold (AGR3), sequence orphan (tam10),
  microprotein (P3R3URF), unstudied family member (KCTD14), and a *closing* gap (C18orf21).
- 2026-06: Second curation batch — eight read-list leads (MTC7, RAB9A, RASA1, BAIAP2L2, SCGB1C1,
  FGFRL1, atg101, irg-1) each adjudicated by reading their deep-research/GOA files; all eight were
  genuine gaps (no spurious calls). Surfaced the *residual sub-gap* category (RAB9A GEF/GAP, RASA1
  scaffolding, atg101 WF-finger) — a sharp mechanistic hole inside an otherwise well-characterized
  gene. PMID verification again paid off: PMID:36323259, cited by a deep-research summary as the
  RASA1 tandem-SH2 reference, resolves to an unrelated stem-cell/ILC paper and was dropped;
  RASA1's domain architecture is anchored to the file path instead. Sixteen worked entries now
  span bacterial, fungal (budding + fission yeast), nematode, and human genes.
