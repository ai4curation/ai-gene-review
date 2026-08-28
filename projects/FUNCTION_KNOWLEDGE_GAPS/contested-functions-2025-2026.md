---
title: "Contested Functions: a 2025-2026 read-list"
species: [human]
---

# Contested Functions — a 2025-2026 read-list

A survey of literature published between January 2025 and August 2026, looking for
**individual human genes whose molecular function is actively disputed**, and turning each
dispute into a question a GO curator could adjudicate.

This is a companion to the [parent project](../FUNCTION_KNOWLEDGE_GAPS.md), which registers what
biology does not know. Here the problem is the opposite and, for curation, sharper: biology
knows *two incompatible things*, both published, both often already in GOA.

## The contested-function gap

The parent page's taxonomy has three kinds of gap — **biology** (nobody knows), **curation**
(known but unannotated), **ontology** (known but inexpressible). Cases below mostly belong to a
fourth kind:

> **Contested-function gap** — two or more lines of experimental work assign the gene product
> mutually incompatible molecular functions, and no consensus has formed. Neither `UNDECIDED`
> (which implies we could not access the evidence) nor `ACCEPT` (which implies the matter is
> settled) is quite right, and the annotations frequently coexist in GOA with **experimental
> evidence codes on both sides**.

Two properties make these unusually high-value curation targets:

1. **The dispute is already inside GOA.** For TMEM175 the GOA carries `proton channel activity`
   (IDA, three references) *and* `potassium ion leak channel activity` (IDA, two references),
   all positively qualified. For **TMEM65** it carries `calcium:sodium antiporter activity`
   twice — once as `enables`/IDA and once as **`NOT|enables`/IDA** — citing the two conflicting
   2025 papers, so the controversy is encoded literally as a positive and a negative annotation
   of the same term on the same gene. A reviewer does not have to go looking for the problem;
   it is sitting in the annotation set.

   **Read the qualifier, always.** An early draft of this page asserted that GOA carried the
   ion-channel claim for TMEM120A. It does not: the three experimental annotations of
   `monoatomic ion channel activity` are all **`NOT|enables`**. Reading only the term and
   evidence code inverts the meaning of the annotation, and the mistake is invisible unless the
   qualifier field is fetched explicitly.
2. **A downstream literature usually keeps building on the contested claim.** The pattern is
   consistent: a methods-level or biochemical challenge appears in one venue while a large
   disease-biology literature continues to assume the original assignment. NAT10, FTO, NSUN2 and
   TRMT6/TRMT61A are all in this state.

**A caution that applies to every entry below.** A live dispute is *not* a licence to `REMOVE`
an experimental annotation. Per the repo's standing rule, curators who made an IDA read the full
text and we have not. The right output for most of these is a `MODIFY` to a term the evidence
actually supports, a `KEEP_AS_NON_CORE`, or an `ACCEPT` whose `reason` states plainly that the
assignment is contested and names the challenge. The value here is in **writing the dispute
down**, not in picking a winner from an abstract.

## How this list was built

Free-text PubMed searching for "controversy"-type phrasing is close to useless — the API's query
translator silently drops phrase clauses and ANDs everything else, so `"remains controversial"`
returns nothing while a five-term query returns zero rather than an error. The searches that
actually worked were:

- **Title-negative patterns** — `"does not"[Title]`, `"is not required"`, `"dispensable"`,
  restricted to a handful of journals. This is what surfaced the TMEM175, DR6 and AGO1 items.
- **Publication-type filters** — `Comment`, `Published Erratum` — restricted to high-impact
  journals. Highest yield of all; this is how the SULT1B1 Matters Arising exchange was found.
- **Direct probes of proteins suspected of live disputes**, then reading what 2025-2026 added.

Every PMID below was verified against PubMed by re-fetching title, journal, year and DOI; the
DOIs were extracted from the article's own `ELocationID`/`ArticleIdList`, **not** from the
reference list, which is an easy way to attach a real-looking but wrong DOI to an entry. Current
GO molecular-function annotations were read live from QuickGO. Repo status was checked directly
against `genes/human/`.

What was **not** done: no full texts were read. Confidence ratings reflect journal, assay type,
independence of the labs, and whether the two sides actually engage each other — not a judgment
on the underlying experiments.

## Shortlist

Ranked by curation value = (sharpness of the dispute) × (exposure in GOA) × (absence of an
existing review).

| Gene | The dispute | Already in GOA? | Repo | Conf. |
|---|---|---|---|---|
| TMEM175 | H⁺-selective channel vs K⁺ channel with incidental H⁺ permeability | **Both, IDA each way** | none | High |
| TMEM120A | Mechanosensitive channel (TACAN) vs ER acyl-CoA/lipid-synthesis protein | Channel term is **`NOT`**×3; one stray positive ISS | none | High |
| TMEM65 / SLC8B1 | Which protein *is* the mitochondrial Na⁺/Ca²⁺ exchanger — and is it Na⁺ at all? | **`enables` + `NOT\|enables`, same term, both IDA** | none | High |
| FTO | mRNA m⁶A demethylase vs m⁶Am/snRNA enzyme vs hydroxylase (no demethylation) | Yes, IDA+IMP | none | High |
| NAT10 | mRNA ac4C writer vs 18S rRNA/tRNA only | Yes, IDA | none | High |
| TRMT61A | mRNA m1A methyltransferase vs tRNA-A58 only (mapped sites are inosine) | Yes, IDA | none | High |
| GSDMC | Plasma-membrane pore vs Rab7-vesicle permeabilizer vs nuclear scaffold | Only IBA lipid binding | none | High |
| CASP4 | Binds LPS molecules vs LPS *membranes of positive curvature*; substrate identity | Yes, IDA | none | High |
| MEFV | Indirect Rho/PKN sensing vs direct CDC42 binding by B30.2 | No GTPase binding term | **937 lines, no CDC42** | High |
| SLC45A4 | Neuronal plasma-membrane polyamine vs peroxisomal putrescine transporter | **Both, IDA** (+ legacy sucrose IBA) | none | High |
| ALKBH1 | Genomic 6mA demethylase vs mt-tRNA f5C oxidase (is mammalian 6mA real?) | Yes, `EXP` | none | High |
| NSUN7 | Catalytically inactive pseudoenzyme vs active m5C writer | `methyltransferase activity` IEA | none | High |
| GRID1 | Non-ionotropic scaffold vs acetylcholine receptor vs glutamate/glycine-gated | Yes — and a `GABA receptor activity` IDA | none | High |
| TMEM63B | Mechanosensitive cation channel vs mechanically activated lipid scramblase | **Both, IDA** | none | High |
| ZBP1 | Can the Zα domains actually convert dsRNA to Z-form? Human vs mouse signalling | `Z-RNA immune receptor` ISS | none | High |
| PRSS23 | Serine protease vs serine pseudoprotease | `serine-type endopeptidase` IEA | none | High |
| GPR50 / GPR37 / GPR158 / GPR75 | Contested or absent deorphanizations | Varies; GPR75 IBA-only | none | Med-High |
| ALDH4A1 | Non-catalytic subunit of the MPC complex, or is MPC an MPC1/MPC2 dimer? | No MPC term | **452 lines, no MPC** | Med-High |
| LRRC8A | Is cGAMP transport physiological or an overexpression artifact? | Yes, IDA | none | Med-High |
| SLC7A11 | Lysosomal proton *channel*, or H⁺ leak secondary to antiport? | — | **1443 lines; overstated** | Med |
| PNPLA3 | Own lipase activity vs ABHD5 sequestration vs neomorph | Yes, many EXP/IDA | none | Med |
| MTCH2 / MTCH1 | Insertase vs BAX/BAK pore factor vs CPT1 regulator vs SLC25 carrier | insertase IDA (MTCH1 too) | **341 lines, thin** | Med |

## Worked entries

### TMEM175 — potassium channel or proton channel? *(top pick)*

- **Boundary:** Lysosomal cation channel of the Parkinson's-risk locus; that it conducts K⁺ and
  that it matters for lysosomal pH are not in dispute. What is disputed is the **selectivity that
  defines its molecular function**, and therefore which GO MF term is correct.
- **The dispute, head to head in the same year:**
  - Ren and Mindell labs: *"TMEM175 does not function as a proton-selective ion channel to
    prevent lysosomal over-acidification"* — in lysosomes it predominantly conducts K⁺, and the
    native lysosomal H⁺ leak is ~0.02 fA, "strongly arguing against major contributions from an
    ion channel" (PMID:41134537, *J Cell Biol* 2026,
    [DOI](https://doi.org/10.1083/jcb.202501145)).
  - Rauh/Grimm/Thiel: *"Proton-selective conductance and gating of the lysosomal cation channel
    TMEM175"* (PMID:41533442, *PNAS* 2026, [DOI](https://doi.org/10.1073/pnas.2503909123)).
  - The journal itself frames it as open: *"Is the Parkinson's-associated protein TMEM175 a
    proton channel: Yay or nay?"* (PMID:41295951, *J Cell Biol* 2026,
    [DOI](https://doi.org/10.1083/jcb.202511084)).
- **What GO says now:** both, experimentally. `GO:0015252` proton channel activity — IDA from
  PMID:35333573, PMID:35750034, PMID:37390818. `GO:0022841` potassium ion leak channel activity —
  IDA from PMID:26317472, PMID:32228865, plus IBA. `GO:0005267` potassium channel activity — IDA
  from PMID:28723891. UniProt's recommended name is already committed: *"Endosomal/lysosomal
  **proton** channel TMEM175"*.
- **Curator question:** Should the proton-channel IDAs be retained as core, downgraded, or
  qualified — and does the ~0.02 fA native-leak measurement bear on the *molecular function* or
  only on its physiological weight? Note the two are separable: a channel can be genuinely
  H⁺-permeable and still not be the physiological H⁺ leak.
- **Type:** contested-function gap, curation-actionable now.

### TMEM120A — mechanosensitive channel, or an ER lipid enzyme's activator?

- **Boundary:** TMEM120A was named TACAN on the strength of a 2020-2021 claim that it is a
  mechanosensitive ion channel in nociceptors. Independent structural work did not support an
  obvious pore, and the 2025-2026 work assigns it a different compartment and a different job.
- **The dispute:**
  - Lipid-metabolism side: *"TMEM120A maintains adipose tissue lipid homeostasis through ER CoA
    channeling"* — an **ER-resident CoA-binding protein** partnering ACSL1/ACSL3 (PMID:41423633,
    *Nat Commun* 2025, [DOI](https://doi.org/10.1038/s41467-025-67870-7)); and TMEM120A as the
    **GPAT4-activating protein**, acting with CHP1 to drive glycerolipid synthesis
    (PMID:42098142, *Nat Commun* 2026, [DOI](https://doi.org/10.1038/s41467-026-72786-x)).
  - Channel side persists: a 2026 review still lists TMEM120A/TACAN among pain-transducing ion
    channels (PMID:41967766, *Life Sci* 2026,
    [DOI](https://doi.org/10.1016/j.lfs.2026.124391)), and a 2026 methods paper assays TMEM120A
    M207A against the mechanosensitive-channel gating-modifier peptide GsMTx4 (PMID:42184262,
    *J Vis Exp* 2026, [DOI](https://doi.org/10.3791/69348)).
- **What GO says now — and this is the interesting part:** GOA has already sided against the
  channel. `GO:0005216` monoatomic ion channel activity appears three times, every one of them
  **`NOT|enables`**: IMP from PMID:34374645 (*"TMEM120A is a coenzyme A-binding membrane protein
  with structural similarities to ELO..."*, eLife 2021), IDA from PMID:34409941 (*"TMEM120A
  contains a specific coenzyme A-binding site and **might not mediate poking- or
  stretch-induced channel activities**"*, eLife 2021) and IDA from PMID:34465718 (Cell Discov
  2021 cryo-EM). `GO:0120225` coenzyme A binding is positively annotated, IDA from
  PMID:34374645.
- **The residual problem:** one positive `enables GO:0005216` **ISS** survives, projected from
  the mouse ortholog (Q8C1E7) via GO_REF:0000024. It directly contradicts the three
  experimental `NOT` annotations on the same term, on the same protein.
- **Curator question:** the sharp, immediately actionable one is whether that stray ISS should
  be removed — an inference from orthology standing against three experimental negatives is
  exactly the pattern the repo's rules say to argue down. Beyond that: is `coenzyme A binding`
  the right MF altitude now that the mechanism looks like acyl-CoA channelling *plus* activation
  of GPAT4, which may need an `enzyme activator activity` term?
- **Type:** curation gap (the stray ISS) sitting on top of a mostly-resolved contested-function
  gap, with an ontology shadow if "activates GPAT4" needs a term. Worth reviewing precisely
  because it shows what a *well-handled* controversy looks like in GOA.

### TMEM65 and SLC8B1 — who is the mitochondrial Na⁺/Ca²⁺ exchanger, and is it sodium?

This is the cleanest three-way conflict found, and GOA encodes it directly.

- **Position A — TMEM65 *is* the exchanger:** *"TMEM65 functions as the mitochondrial Na⁺/Ca²⁺
  exchanger"*; purified, liposome-reconstituted TMEM65 shows mito-NCX activity (PMID:40691517,
  *Nat Cell Biol* 2025, [DOI](https://doi.org/10.1038/s41556-025-01721-x)).
- **Position B — TMEM65 is a required *regulator* of NCLX:** *"TMEM65 regulates and is required
  for NCLX-dependent mitochondrial calcium efflux"* — a binding partner, with NCLX deletion
  ablating the TMEM65 effect (PMID:40200126, *Nat Metab* 2025,
  [DOI](https://doi.org/10.1038/s42255-025-01250-9)).
- **Position C — the counterion is wrong for both:** the NCLX cryo-EM structure reports *"an
  unexpected transport function of NCLX as a H⁺/Ca²⁺ exchanger, rather than as a Na⁺/Ca²⁺
  exchanger as widely believed"* — the canonical Na⁺-binding residues are absent (PMID:40931067,
  *Nature* 2025, [DOI](https://doi.org/10.1038/s41586-025-09491-0)). A second structure agrees
  the Na⁺ sites are missing but concludes broader selectivity (Na⁺/K⁺/Li⁺/H⁺) rather than
  H⁺-specificity (PMID:42431881, *Nat Commun* 2026,
  [DOI](https://doi.org/10.1038/s41467-026-75483-x)).
- **The field has noticed:** *"Mitochondrial sodium-calcium exchange — Can TMEM65 do it alone?"*
  (PMID:41061666, *Cell Metab* 2025, [DOI](https://doi.org/10.1016/j.cmet.2025.09.005)).
- **What GO says now:** the contradiction is recorded verbatim. On **TMEM65**, `GO:0005432`
  calcium:sodium antiporter activity appears **twice**: `enables`/IDA citing PMID:40691517
  (Position A) and **`NOT|enables`/IDA** citing PMID:40200126 (Position B). The same term also
  sits positively on **SLC8B1** with IDA, IMP, IBA and TAS. If Position C holds, the term is
  wrong for both proteins regardless of which of A or B wins.
- **Why this is the most instructive case on the list:** GOA did not paper over the conflict, it
  annotated both sides. A review that simply `ACCEPT`s the positive TMEM65 IDA without engaging
  the co-existing `NOT` would be asserting a resolution the evidence does not have.
- **Curator question:** Which protein carries the transport MF, and is `calcium:sodium
  antiporter activity` the right term or should it be a proton-coupled or
  broad-cation-coupled exchanger term? Reviewing either gene alone will not settle it — this is
  a two-gene review.

### FTO, NAT10, TRMT61A, ALKBH1, NSUN2, NSUN7 — the epitranscriptomic writer/eraser cluster

Six genes with the same structural problem, and they are best reviewed together because the
methodological argument is shared: **the enzyme is real, but the claimed substrate class may be
a mapping artifact**, while a large disease literature continues to build on it.

- **FTO** — a 2025 *Nucleic Acids Res* study finds human FTO *"catalyses hydroxylation of
  N6-methyladenosine without direct formation of a demethylated product"*, unlike ALKBH5/2/3, and
  notes "conflicting reports concerning the FTO products" (PMID:40874592,
  [DOI](https://doi.org/10.1093/nar/gkaf813)). A Jaffrey-lab preprint reports FTO depletion does
  not alter mRNA m⁶A stoichiometry by direct nanopore sequencing, with FTO loss instead raising
  snRNA m⁶Am (PMID:41279954, *bioRxiv* 2025 — **preprint**,
  [DOI](https://doi.org/10.1101/2025.10.22.681652)). GOA carries `GO:1990931` mRNA
  N6-methyladenosine dioxygenase activity with IBA, IDA, IEA **and IMP**.
- **NAT10** — the base-resolution methods disagree, and the exchange is on the record:
  *"Detection of ac4C in human mRNA is preserved upon data reassessment"* (PMID:38640896,
  *Mol Cell* 2024, [DOI](https://doi.org/10.1016/j.molcel.2024.03.018)), responding to
  disagreement between RedaC:T-seq (PMID:35679869,
  [DOI](https://doi.org/10.1016/j.molcel.2022.05.016)) and ac4C-seq (PMID:33772246,
  [DOI](https://doi.org/10.1038/s41596-021-00501-9)). GOA carries **`GO:0106162` mRNA cytidine
  N-acetyltransferase activity with IDA** alongside `GO:1990883` 18S rRNA (EXP) and `GO:0051392`
  tRNA (IBA). The 2025-2026 disease literature does not engage the dispute at all (e.g.
  PMID:42592486, PMID:42315153).
- **TRMT61A** — *"Validation of the mRNA epitranscriptome: SCARPET reveals that mapped m1A sites
  are inosine"*, concluding mRNA m1A "is extremely rare" (PMID:42337368, *EMBO Rep* 2026,
  [DOI](https://doi.org/10.1038/s44319-026-00840-2)), against a stream of TRMT6/TRMT61A mRNA-m1A
  cancer papers (PMID:42003777, PMID:41103012). GOA carries `GO:0061953` mRNA
  (adenine-N1-)-methyltransferase activity with **IDA**.
- **ALKBH1** — its `GO:0141131` DNA N6-methyladenine demethylase activity has an **EXP** code,
  but a 2025 *Nat Genet* survey concludes robust 6mA occurs only in AMT1-encoding unicellular
  lineages and attributes mammalian reports to "methodological artifacts" (PMID:41254163,
  [DOI](https://doi.org/10.1038/s41588-025-02409-6)). The same question undercuts **YTHDF3** as a
  DNA-6mA reader (PMID:40715766, *EMBO J* 2025,
  [DOI](https://doi.org/10.1038/s44318-025-00512-2)).
- **NSUN2** — `GO:0062152` mRNA (cytidine-5-)-methyltransferase activity carries EXP, IBA, IDA
  and IEA, while a 2026 review is titled *"m5C Methylation of mRNA: Still More Questions Than
  Answers"* (PMID:42587746, [DOI](https://doi.org/10.3390/cells15151336)).
- **NSUN7** — the inverse case, and the cleanest: *"NSUN7 is a catalytically inactive RNA m5C
  methyltransferase essential for sperm flagellum assembly"* — no SAM binding (motif IV
  Asp→Leu), and knockout does not change RNA m5C (PMID:41381527, *Nat Commun* 2025,
  [DOI](https://doi.org/10.1038/s41467-025-67233-2)); corroborated structurally (PMID:40545153)
  and functionally as an RNA-binding destabilizer (PMID:40032361). GOA carries only
  `GO:0008168` methyltransferase activity, **IEA** — an unsupported electronic inference of
  exactly the kind the repo's rules permit arguing against.

**Curator question for the cluster:** where the writer/eraser activity on rRNA or tRNA is
solid but the mRNA claim rests on a contested mapping method, is the right action `MODIFY` to
the well-supported substrate, or `ACCEPT` with the dispute recorded? A shared position across
the six would be more valuable than six independent calls.

### GSDMC — three incompatible molecular functions, none of them in GOA

- **Position A — intracellular vesicle permeabilization, not pyroptosis:** cathepsin-S-cleaved
  GSDMC targets **Rab7⁺ vesicles rather than the plasma membrane**; epithelial cell death "is not
  the main consequence", and inserting a single amino acid into its lipid-binding motif to match
  the other gasdermins is what makes it oligomerize and kill (PMID:40701157, *Immunity* 2025,
  [DOI](https://doi.org/10.1016/j.immuni.2025.06.018)).
- **Position B — nuclear chromatin scaffold:** GSDMC translocates to the nucleus via
  IPO7-KPNB1-NUP93 and "functions as a scaffold molecule, recruiting NAT10 to mediate histone H3
  acetylation and recruiting BAZ1B/SMARCA5 to modulate chromatin remodeling" (PMID:42176271,
  *Cell Rep* 2026, [DOI](https://doi.org/10.1016/j.celrep.2026.117427)).
- **Position C — classical pyroptotic executioner:** granzyme-B-cleaved GSDMC executes
  pyroptosis in melanoma cells, shown via a compound (DdBIC) acting through the nuclear receptor
  Nur77 (PMID:41407678, *Signal Transduct Target Ther* 2025,
  [DOI](https://doi.org/10.1038/s41392-025-02528-w)). Note this is pharmacologically induced
  cleavage, so it establishes that GSDMC *can* form a lytic pore, not that this is its
  physiological role — which is precisely what Position A denies.
- **The field has named the problem:** *"Cutting the Gordian knot: Untangling gasdermin C from
  pyroptosis"* (PMID:41092892, *Immunity* 2025,
  [DOI](https://doi.org/10.1016/j.immuni.2025.09.015)).
- **What GO says now:** essentially nothing — only IBA-propagated phospholipid-binding terms
  (`GO:0001786`, `GO:0005546`, `GO:0070273`) inherited from the gasdermin family. This is
  therefore a **curation gap layered on a contested-function gap**: the family-level IBA asserts
  the pore-forming lipid-binding paradigm that Position A specifically argues GSDMC does not
  follow.

### MEFV — the highest-value *update* to an existing review

- **Boundary:** Pyrin, the FMF gene. The repo review (`genes/human/MEFV/`, 937 lines, no PENDING
  annotations) is built on the canonical model: RhoA inactivation → loss of PKN1/2
  phosphorylation → 14-3-3 release → inflammasome assembly.
- **What changed:** three simultaneous *Sci Immunol* papers (2026) plus a commentary identify
  **CDC42 as a direct ligand of the pyrin B30.2/SPRY domain**, i.e. "dual regulation of pyrin by
  two RHO family GTPases" — a molecular function (small-GTPase binding) the canonical model does
  not contain (PMID:42566498, [DOI](https://doi.org/10.1126/sciimmunol.aea0515); PMID:42566497;
  PMID:42566500, [DOI](https://doi.org/10.1126/sciimmunol.aea0705), a genotype-first screen of
  265 MEFV variants finding classical FMF variants bind CDC42 tightly while certain non-FMF
  variants hyperactivate pyrin CDC42-independently; commentary PMID:42566502).
- **Verified repo status:** `grep -ic CDC42` returns **0**; RhoA/PKN appear 9 times. The review
  is not wrong, it is superseded in part.
- **Curator question:** does MEFV acquire a small-GTPase-binding MF, and does the
  CDC42-independent hyperactivation of some variants imply more than one activation route?

### PRSS23 — a clean IEA-versus-experiment case

- **The finding:** PRSS23 is secreted as a processed, glycosylated protease-homology domain that
  retains the catalytic triad but **lacks the canonical Ile16-Asp194 zymogen activation switch**.
  No serine hydrolase activity was detectable by activity-based probe labelling of conditioned
  media or by chromogenic substrate assay, and the pro-tumorigenic phenotype survived mutation of
  the putative catalytic serine. The authors propose reclassification as a **serine
  pseudoprotease** (PMID:41985786, *J Biol Chem* 2026,
  [DOI](https://doi.org/10.1016/j.jbc.2026.111450)).
- **What GO says now:** `GO:0004252` serine-type endopeptidase activity, **IEA only**, from
  InterPro IPR001254/IPR018114 — a fold-based electronic inference with no experimental support,
  now contradicted by direct assay. This is squarely within the repo's stated grounds for
  `REMOVE`: an electronic inference that can be argued against on biological grounds.
- Related pseudoenzyme case: **CA8**, whose `GO:0004089` carbonate dehydratase activity rests on
  IEA plus a 1996 **TAS** (PMID:8977131), while the protein lacks a catalytic histidine and the
  HGNC name is already "carbonic anhydrase 8 (**inactive**)" (review: PMID:42268453,
  [DOI](https://doi.org/10.1007/s11033-026-12124-y)). Lower novelty, but a tidy over-annotation
  fix.

### SLC7A11 — a correction our own review needs

Not a literature controversy so much as an internal inconsistency the controversy exposes.

- The repo review (1443 lines, no PENDING) states in its `description` that SLC7A11 has
  *"novel lysosomal proton channel activity"* (line 17) and repeats it at line 152.
- The verbatim `supporting_text` it quotes from the same source says something materially
  weaker: SLC7A11 *"mediates a slow lysosomal H+ leak **through downward flux of cystine and
  glutamate**"* (PMID:40280132, *Cell* 2025, [DOI](https://doi.org/10.1016/j.cell.2025.04.004)).
  That is antiport-coupled H⁺ movement, not channel activity.
- The distinction matters more now that PMID:41134537 argues the native lysosomal H⁺ leak is
  ~0.02 fA and unlikely to be channel-mediated at all.
- **Action:** tighten the `description` to match the quoted evidence. Cheap, and it removes a
  claim the repo is currently asserting more strongly than its own citation does.

## Second tier — verified, worth reading, lower priority

- **CASP4** — four 2026 papers give incompatible pictures of ligand engagement and substrate.
  Broz lab: caspase-4 *"binds to LPS membranes with positive curvature"* rather than individual
  LPS molecules, requiring GBP1-deformed geometry (PMID:41702406, *Immunity* 2026,
  [DOI](https://doi.org/10.1016/j.immuni.2025.12.017)); a *PNAS* study finds no single
  stoichiometry (PMID:42546204); a *PLoS Pathog* study reports CASP4/5 directly cleave
  CASP3/CASP7 and that most GSDMD cleavage in non-canonical signalling is CASP1-mediated
  (PMID:42044191, [DOI](https://doi.org/10.1371/journal.ppat.1014178)). GOA carries
  `GO:0001530` lipopolysaccharide binding (IDA).
- **ZBP1** — a biophysics preprint argues the long-assumed A→Z RNA conversion by Zα1/Zα2 "was
  never experimentally validated and does not occur" for unmodified RNA (PMID:42079158,
  *bioRxiv* — **preprint**); separately, human ZBP1 signals via RIPK1 RIPK3-independently,
  unlike mouse, with the authors warning against transferring mouse annotations (PMID:42436309,
  *EMBO Rep* 2026, [DOI](https://doi.org/10.1038/s44319-026-00866-6)). GOA carries
  `GO:7770073` left-handed Z-RNA immune receptor activity as **ISS**.
- **GRID1 (GluD1)** — *"GluD1 is localized at cholinergic synapses and is an acetylcholine
  receptor"* (PMID:42270762, *Mol Psychiatry* 2026,
  [DOI](https://doi.org/10.1038/s41380-026-03675-4)) against a review asserting GluD1's "lack of
  classical ion channel activity" and recasting it as a non-ionotropic scaffold (PMID:41345253,
  [DOI](https://doi.org/10.1038/s41401-025-01696-3)). GOA is already incoherent here, carrying
  `GO:0016917` **GABA receptor activity** (IDA), `GO:0004971` AMPA glutamate receptor activity
  (IBA) and `GO:0099530` GPCR activity in one MF set.
- **TMEM63B** — mechanosensitive channel vs mechanically activated lipid scramblase
  (PMID:41617699, *Nat Commun* 2026, [DOI](https://doi.org/10.1038/s41467-026-68919-x);
  PMID:42573579, *J Gen Physiol* 2026, describing a channel-to-scramblase switch in pathogenic
  variants, [DOI](https://doi.org/10.1085/jgp.202614003)). GOA already carries both
  `GO:0140135` and `GO:0017128` with IDA. A dual-function protein is a legitimate outcome here —
  the curation question is whether both are core.
- **SLC45A4** — plasma-membrane neuronal polyamine transporter (PMID:40836097, *Nature* 2025,
  [DOI](https://doi.org/10.1038/s41586-025-09326-y)) vs peroxisomal putrescine transporter
  feeding GABA synthesis (PMID:41266324, *Nat Commun* 2025,
  [DOI](https://doi.org/10.1038/s41467-025-62721-x)). Both are in GOA with IDA. Separately, the
  legacy family-level `GO:0008506` **sucrose:proton symporter activity** (IBA, ISS) is supported
  by neither paper and looks like a clean over-propagation.
- **ALDH4A1** — claimed as a non-catalytic structural component of the mitochondrial pyruvate
  carrier (PMID:40355545, *Nat Cell Biol* 2025,
  [DOI](https://doi.org/10.1038/s41556-025-01651-8)), while three 2025 cryo-EM structures resolve
  MPC as an MPC1/MPC2 heterodimer only (PMID:40101766, *Nature* 2025,
  [DOI](https://doi.org/10.1038/s41586-025-08873-8); PMID:40044865; PMID:40691140). The repo's
  452-line ALDH4A1 review has **zero** mentions of MPC or pyruvate — verified.
- **LRRC8A** — a cGAMP-mediated antitumour response proceeds *without* LRRC8/VRAC channels
  (PMID:41419196, *J Biol Chem* 2026, [DOI](https://doi.org/10.1016/j.jbc.2025.111060)), against
  work treating VRAC-mediated cGAMP transport as a real tunable function (PMID:41371222,
  *Mol Cell* 2025). GOA carries `GO:0140360` cyclic-GMP-AMP transmembrane transporter activity
  with IDA.
- **PNPLA3** — loss-of-function vs gain-of-function vs neomorph, with a dedicated editorial about
  the conflict (PMID:39892821, *J Hepatol* 2025; PMID:39550037; PMID:41046517, *Cell Rep* 2025,
  [DOI](https://doi.org/10.1016/j.celrep.2025.116371)). GOA carries a large and partly
  contradictory set of lipase and acyltransferase MF terms with EXP/IDA codes.
- **MTCH2 / MTCH1** — the repo's 341-line MTCH2 review (status `INITIALIZED`) commits fully to
  the insertase model and predates: the 2026 cryo-EM family structure (PMID:42308315, *Sci Adv*,
  [DOI](https://doi.org/10.1126/sciadv.aeh2957)), a BAX/BAK apoptotic-pore role (PMID:42056306,
  *Nat Struct Mol Biol* 2026, [DOI](https://doi.org/10.1038/s41594-026-01805-8)), a CPT1
  regulatory role (PMID:41044057, *Nat Commun* 2025,
  [DOI](https://doi.org/10.1038/s41467-025-63880-7)), and the awkward observation that **MTCH1,
  not MTCH2**, rescues the yeast MIM complex (PMID:40704594, *J Cell Sci* 2025,
  [DOI](https://doi.org/10.1242/jcs.263736)).
- **Contested and absent deorphanizations.** **GPR50**: L-LEN proposed as endogenous ligand
  (PMID:41495223, *Nat Chem Biol* 2026, [DOI](https://doi.org/10.1038/s41589-025-02098-6)) while
  a cryo-EM structure the following month reports the receptor ligand-free and states
  "endogenous agonists have not been characterized" (PMID:41666959, *Mol Cells* 2026,
  [DOI](https://doi.org/10.1016/j.mocell.2026.100331)). **GPR37**: prosaposin, protectin D1 and
  now osteocalcin all asserted concurrently (PMID:41679312; PMID:42649016; PMID:42144155); GOA
  carries `GO:0036505` prosaposin receptor activity with IDA. **GPR158**: osteocalcin receptor vs
  metabotropic glycine receptor vs ligand-independent RGS7 anchor; GOA carries `GO:0160079`
  G protein-coupled glycine receptor activity with IDA. **GPR75**: GOA asserts `GO:0016493` C-C
  chemokine receptor activity on IBA/IEA/ISS alone, while a 2026 cryo-EM structure reports a
  collapsed extracellular domain with **no orthosteric pocket** and IUPHAR still lists it as an
  orphan (PMID:41545757, *Acta Pharmacol Sin* 2026,
  [DOI](https://doi.org/10.1038/s41401-025-01720-6)).
- **TNFRSF21 (DR6)** — *"Death receptor 6 does not regulate axon degeneration and Schwann cell
  injury responses during Wallerian degeneration"* (PMID:41891813, *eLife* 2026,
  [DOI](https://doi.org/10.7554/eLife.108389)). GOA carries only `protein binding` as MF, so the
  exposure is in BP rather than MF.
- **MICU1/2/3** — claimed to form Ca²⁺-dependent metabolons with FADH₂-linked dehydrogenases
  *independently of MCU*, displacing the textbook matrix-Ca²⁺ model (PMID:42129466, *Nat Metab*
  2026, [DOI](https://doi.org/10.1038/s42255-026-01513-z)). No published rebuttal yet.
- **CLYBL** — physiological function reassigned from itaconate catabolism to malyl-CoA metabolite
  repair (PMID:40108300, *Nat Chem Biol* 2025,
  [DOI](https://doi.org/10.1038/s41589-025-01857-9)). A clean `MODIFY`-shaped question.
- **P2RX7** — *"The neuronal P2X7R controversy: Revisiting evidence, methods, and unresolved
  questions"* (PMID:41672132, *Neuropharmacology* 2026,
  [DOI](https://doi.org/10.1016/j.neuropharm.2026.110876)). The dispute is about cell-type
  expression, so it bears on CC/BP rather than MF.
- **SULT1B1** — a textbook Matters Arising exchange: *"Mass spectrometry and enzyme assays refute
  histone tyrosine sulfation"* (PMID:40890505, *Nat Chem Biol* 2025,
  [DOI](https://doi.org/10.1038/s41589-025-01994-1)), the authors' reply (PMID:40890506), and an
  Author Correction to the 2023 original (PMID:40890508; original PMID:36805701) — while a 2026
  *Cancer Res* paper claims a **different** enzyme, GAL3ST1, writes the same disputed mark
  (PMID:41686426, [DOI](https://doi.org/10.1158/0008-5472.CAN-25-2452)). **Included as a
  negative control rather than a target:** GO never took the bait — SULT1B1 carries only aryl
  sulfotransferase terms, no histone sulfotransferase activity. Useful as a worked example of
  the system behaving correctly.

## Checked and set aside

Recorded so the same ground is not re-covered.

- **AARS1 lactyltransferase** — no published rebuttal found in the window, and the repo's
  1860-line review already qualifies the activity to elevated-lactate, substrate-specific
  contexts rather than dominant basal global lactylation. Handled well already.
- **AAGAB** — the 2025 *Structure* paper formally classifying its N-terminus as a class I
  pseudoGTPase (PMID:40752490, [DOI](https://doi.org/10.1016/j.str.2025.07.009)) is an
  incremental citation for an 892-line review that already describes the pseudoGTPase domain and
  the σ-subunit interface. Not a re-review.
- **AIFM2/FSP1, GPX4, ACSL4, IFI16, MAP3K20** — substantive repo reviews exist and the 2025-2026
  literature is complementary rather than conflicting.
- **Irisin/FNDC5** — 2025-2026 output is clinical/biomarker meta-analysis, not molecular function.
- **PTBP1** — the glia-to-neuron reprogramming replication failure is live, but what is disputed
  is a cellular reprogramming role, not the splicing-repressor MF.
- **mPTP identity (ATP5F1A / SLC25A4)** — still unresolved (PMID:42584469, *J Gen Physiol* 2026,
  [DOI](https://doi.org/10.1085/jgp.202614066)), but both genes already have large reviews and
  the dispute is about a supramolecular pore rather than either gene's MF.
- **JMJD6, CGAS, POLR2A condensates, SAMHD1, TSPO, TMEM106B** — real mechanistic uncertainty,
  but no in-window head-to-head paper; the conflict is with standing literature, which makes
  them weaker curation targets right now.

## Suggested first picks

If three genes are to be reviewed from this list:

1. **TMEM175** — sharpest dispute, both sides in GOA with IDA, a journal commentary framing it as
   open, no existing review. The single best test of whether our review format can represent a
   live controversy honestly.
2. **TMEM65 + SLC8B1 together** — forces a two-gene review and a decision about a transport MF
   that GOA currently duplicates across two proteins.
3. **MEFV** — highest-value update to work already done; a 937-line review with a documented,
   verified hole (no CDC42) that three simultaneous 2026 papers fill.

`NSUN7` and `PRSS23` are the cheapest wins if a quick demonstration is wanted: both are
pseudoenzyme reclassifications where the contested GO annotation is IEA-only.

## Provenance and caveats

Three separate verification failures were caught while assembling this page. They are recorded
because each is a reusable trap, not because they are interesting individually.

- **Titles.** All 90+ PMIDs cited were re-fetched from PubMed and checked for title/journal/year
  agreement. Four claims from the underlying survey were corrected during that check: two
  publication years, and two papers whose content had been paraphrased into something the title
  did not say (one of which, PMID:41407678, turned out on reading the abstract to support the
  claim after all — but via pharmacological induction, which changes what it licenses).
- **DOIs.** DOIs were taken from each article's own `ELocationID`/`ArticleIdList`. An earlier
  pass that read the last DOI anywhere in the PubMed XML produced **nine wrong DOIs out of
  twenty**, every one a plausible-looking journal DOI harvested from the reference list. A
  well-formed identifier is not a verified one.
- **GO qualifiers.** Fetching `goId` + `goEvidence` without `qualifier` inverted the meaning of
  the TMEM120A annotations and would have put a flatly false claim on this page. Any tooling
  that summarises GOA for review purposes must carry the qualifier through; `NOT|enables` with
  an IDA is a *stronger* statement than no annotation at all, and it is the single most
  informative thing GOA can say about a contested function.
- GO annotation states are a snapshot read from QuickGO during this survey and will drift.
- Preprints are flagged inline. PMIDs 41279954, 42079158 and 42539190 are bioRxiv.
- No full texts were read. Every entry states a *question*, not a verdict.
