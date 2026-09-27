# ACTA2 (P62736) — review notes

Smooth muscle α-actin, aortic type. HGNC:130, chromosome 10q23. 377-aa precursor; the mature
protein is residues 3–377 after removal of Met1 and the N-acetylated Cys2 (UniProt CHAIN
`2..377` "intermediate form" → CHAIN `3..377`). All structural numbering below is mature-actin
numbering, i.e. precursor − 2; the offset is verified in
[`ACTA2-bioinformatics/RESULTS.md`](ACTA2-bioinformatics/RESULTS.md) against three sources that
state both numbers, one of which is the literature itself
[PMID:26637293 "R179 (R177 in α1-actin)"].

## What the protein is

The single sentence that frames every annotation decision here is from the paper that
established the gene's disease association:

> [PMID:17994018 "SMC contractile force requires cyclic interactions between SMC alpha-actin
> (encoded by ACTA2) and the beta-myosin heavy chain (encoded by MYH11)."]

and the isoform's tissue scope:

> [PMID:19409525 "The vascular smooth muscle cell (SMC)-specific isoform of alpha-actin (ACTA2)
> is a major component of the contractile apparatus in SMCs located throughout the arterial
> system."]

> [PMID:20734336 "SMC lineage in these organs is characterized by cellular expression of the SMC
> isoform of α-actin, encoded by the ACTA2 gene."]

ACTA2 is also the canonical myofibroblast marker, and that dual identity — contractile protein
and lineage marker — is the source of most of the questionable rows in its GOA (see
"marker-expression annotations" below).

UniProt's own FUNCTION line is generic to the family ("Actins are highly conserved proteins that
are involved in various types of cell motility and are ubiquitously expressed in all eukaryotic
cells") and the CATALYTIC ACTIVITY (ATP + H2O = ADP + phosphate + H+) and SUBUNIT
("Polymerization of globular actin (G-actin) leads to a structural filament (F-actin) in the form
of a two-stranded helix. Each actin can bind to 4 others.") carry `ECO:0000250` — by similarity
from `UniProtKB:P68137`, which is **Sus scrofa** ACTA1, not human ACTA1. That is the classical
biochemical preparation of actin, so it is a strong transfer, but it is worth stating the species
correctly.

## Finding 1 (headline): `GO:0005884 actin filament` is attached to three sub-clade nodes, so the two smooth-muscle actins are the only conventional actins that lack it

Computed, not asserted — see RESULTS.md §1 and §2.

`GO:0005884` reaches human genes by IBA from **three separate PANTHER nodes**:

| node | human recipients |
|---|---|
| `PTN002631586` | ACTB, ACTG1, ACTBL2, **ACTL8**, POTEE, POTEF, POTEI, POTEJ, POTEKP |
| `PTN000748220` | ACTC1 |
| `PTN000233075` | ACTA1 |

There is no assertion at any node ancestral to all conventional actins, and **ACTA2 and ACTG2
receive nothing**. They are the only two of the six conventional human actins with no `actin
filament` annotation of any kind (ACTA1 IBA+IDA, ACTB IBA, ACTG1 IBA+IDA, ACTC1 IBA+IDA;
ACTA2 0, ACTG2 0).

The measured filament-protomer interface makes the inversion stark. Scored on the same 38
inter-protomer contact residues of PDB 6DJO chain C that the merged ACTL8 and ACTL10 analyses
used (and reproducing ACTL8's committed numbers for nine shared panel members, asserted in code):

| protein | identical | conservative | non-cons | compatible / 38 | has GO:0005884? |
|---|---|---|---|---|---|
| ACTA1 | 38 | 0 | 0 | 38 | yes |
| **ACTA2** | **38** | **0** | **0** | **38** | **no** |
| ACTG2 | 38 | 0 | 0 | 38 | no |
| ACTC1 | 38 | 0 | 0 | 38 | yes |
| ACTB | 37 | 1 | 0 | 38 | yes |
| ACTG1 | 37 | 1 | 0 | 38 | yes |
| Arp53D (Dm) | 29 | 4 | 5 | 33 | — |
| ACTL8 | 8 | 3 | 24 | 11 | **yes** |

So `actin filament` is withheld from a protein that is perfect at all 38 interface positions and
granted to one that is compatible at 11 — and granted to it through the β-actin node whose
membership the merged ACTL8 review argued is itself the defect. This is the AADACL "right term,
wrong node" shape: the supporting feature (polymerisation into a two-stranded filament) is
family-wide among conventional actins, but the term sits at three sub-clade nodes. One PAINT edit
— assert `GO:0005884` at the conventional-actin ancestor — fixes ACTA2 and ACTG2 together.

Stated once, for both genes, in `suggested_questions`. A sibling agent reviewed ACTG2 in parallel
(PR #2303) and derived the same three-node set independently; I confirmed the zero-reach claim for
ACTA2 with `goUsage=descendants` as well as `exact`, so it is not an artefact of asking only about
the exact term.

### The same node, asked the other way round

The forward question ("which node gives ACTA2 term X") cannot find a node that gives ACTA2 nothing
it should have. The reverse question ("what is this node *for*") can, and it is what turns the
finding from a gap into a diagnosis. Computed reach of every PTHR11937 node that touches a
conventional human actin:

| node | human genes reached | terms |
|---|---|---|
| `PTN000233075` | ACTA1 | GO:0001725, GO:0005865, GO:0005884, GO:0030240 |
| `PTN000748220` | ACTC1 | GO:0005884, GO:0007015, GO:0017022, GO:0030017, GO:0033275, GO:0060047 |
| `PTN002631586` | ACTB, ACTBL2, ACTG1, **ACTL8**, POTEE/F/I/J/KP | GO:0005884, GO:0098973 |
| `PTN004322804` | **ACTA2, ACTG2 — exactly the smooth-muscle pair** | GO:0005576 only |

So PTHR11937 does have a node whose entire human output is the two smooth-muscle actins, and the
one thing it gives them is `extracellular region`. Meanwhile `PTN000748220` — a single-gene node —
holds not only `actin filament` but `GO:0017022 myosin binding`, `GO:0033275 actin-myosin filament
sliding` and `GO:0007015 actin filament organization`, all confined to ACTC1. This is the AADACL
"right term, wrong node" shape at family scale, and it is the same underlying defect behind three
of this review's findings rather than three separate problems.

### `GO:0017022 myosin binding` is the sharpest instance

Of 102 human `GO:0017022` annotations, exactly four are on actin-family genes: three on ACTC1 (IBA
from `PTN000748220`, plus its own IPI and IDA) and one TAS on ACTA1. **ACTA2, ACTG2, ACTB and
ACTG1 have none, at any granularity.**

For ACTA2 this is not a missing inference, it is a missing *measurement that exists*.
[PMID:26153420 "In an in vitro motility assay, smooth muscle myosin moves R258C filaments more
slowly than WT, and the slowing is exacerbated by smooth muscle tropomyosin."] — the wild-type arm
of that comparison is baculovirus-expressed human smooth muscle α-actin being translocated by
smooth muscle myosin. The gene whose every disease phenotype is a failure of the actin-myosin
interaction has no term recording that it interacts with myosin. Proposed as `NEW` with `IDA`
rather than `IPI`, because the cached text does not state the species of the myosin preparation
and I will not assert a `with/from` accession I cannot verify.

## Finding 2: ACTA2 is in the retained set for `GO:0005200`, but the retained set is the four MUSCLE actins, not "the four conventional actins"

The background handed to this review said the genes still receiving `GO:0005200 structural
constituent of cytoskeleton` from `PTN000940351` are "the four conventional actins (ACTA1,
ACTA2, ACTB, ACTG1)". Verified against QuickGO, and it is wrong in both directions:

- The node projects onto **10** human genes: **ACTA1, ACTA2, ACTC1, ACTG2** (the four *muscle*
  actins), **ACTR10**, and **ACTL9, ACTL10, ACTRT1, ACTRT2, ACTRT3**.
- **ACTB and ACTG1 receive no IBA at all.** They hold the term by other routes — ACTB by `TAS`
  (PMID:6202424) and ACTG1 by `IC` from `GO:0005856` (PMID:16130169). ACTB does not receive an
  IBA because it is one of the ten IBD **seeds**.

So the count (4 + 1 + 5 = 10) was right and the identity of the four was not. ACTA2 **is** in the
retained set, and for ACTA2 the term is well founded: 38/38 at the filament interface, 19/19
chemically compatible at the nucleotide site, unchanged under a second substitution matrix and
gap model.

## Finding 3: two of the ten seeds that justify `GO:0005200` are inside clades where PAINT has negated it

PAINT asserts `GO:0005200` exactly once in PTHR11937, at `PTN000940351` (IBD, 2025-08-05, ten
seeds), and negates it by IRD at eight descendant nodes. Two of those ten seeds are
**human ACTR2 (P61160)** and **human ACTR3 (P61158)** — and `PTN000233596` (the ARP2 clade,
seeded by P61160 for its other terms) and `PTN000233796` (the ARP3 clade, seeded by P61158) are
two of the eight IRD-negated nodes.

Arp2 and Arp3 therefore supply experimental support for the term at the family root while their
own clades are exempted from the term they support. Reported as a PAINT question, not as a defect
in either individual row: it is a *tree* inconsistency and it does not weaken ACTA2's inheritance
(eight of the ten seeds carry their own experimental evidence for the exact term; the two that do
not are ACTB, which holds only `TAS`, and rat Actg1, which holds only `ISO`).

## Finding 4: the disease variants are polymer-interface and nucleotide-cleft residues — but a single-chain contact set says the opposite

This one reversed itself in the middle of the analysis and the reversal is the point.

Scoring the 19 UniProt `FT VARIANT` positions against chain C's 38-residue contact set gave
**zero** pathogenic variants on the interface. That reading is an artefact: 6DJO holds four
protomers, so chain C has its i−2, i−1 and i+1 neighbours but **no i+2 neighbour**, and actin
protomer contacts are not symmetric — a residue that reaches only "upward" is invisible from
chain C. Taking the minimum over every chain:

| ACTA2 pos | disease | min Å to another protomer | via | min Å to nucleotide |
|---|---|---|---|---|
| 326 | AAT6 | 2.82 | same-strand (i±2) | 30.9 |
| 145 | AAT6 | 3.04 | same-strand | 14.2 |
| 292 | AAT6 | 3.21 | same-strand | 24.0 |
| 196 | *not disease-linked* (rs1803028) | 3.28 | cross-strand (i±1) | 17.6 |
| 353 | AAT6 | 3.53 | same-strand | 23.4 |
| 179 | MYMY5, SMDYS | 4.42 | cross-strand | 8.11 |
| 149 | AAT6 | 5.16 | same-strand | 17.4 |
| 212 | AAT6 | 10.1 | same-strand | **4.25** |
| 185 | AAT6 | 10.5 | cross-strand | **4.24** |

Four AAT6 variants (145, 292, 326, 353) make direct ≤4 Å inter-protomer contacts; two more (185,
212) sit ~4.2 Å from the bound nucleotide. **R179 is at 4.42 Å across the strand** — just outside
a 4.0 Å cutoff, which is why the cutoff-based answer read as a refutation of
[PMID:26637293 "Whereas R179 localizes to a short β-strand in actin subdomain 3, R258 is situated
in an α-helix in subdomain 4."]. The paper's mechanism survives measurement: it names L112 (same
molecule) and **K193 and T196 of the paired molecule** as R179's inter-strand contacts, and all
three map into the independently computed contact set (K193→191 and T196→194, both contacting
chain B). That is used in code as a literature-derived control on the contact set itself.

Two consequences for curation:

1. `GO:0005200` and the proposed `GO:0005884` are not merely "true of actins in general" for
   ACTA2 — the specific residues its disease alleles hit are the polymer contacts and the
   nucleotide cleft. The structural annotation and the disease mechanism are the same statement.
2. It remains true that the mechanism is largely **allosteric**, so the variants must not be read
   as mapping a binding site: [PMID:26153420 "Many of the observed defects cannot be explained by
   a direct interaction with the mutated residue, and thus the mutation allosterically affects
   multiple regions of the monomer."] The best-studied allele, R258C, is 7.0 Å from the nearest
   protomer, and its measured defects are filament instability
   [PMID:26153420 "R258C filaments are less stable than WT and more susceptible to severing by
   cofilin."], loss of tropomyosin protection [PMID:26153420 "Smooth muscle tropomyosin offers
   little protection from cofilin cleavage, unlike its effect on WT actin."] and a shifted monomer
   pool [PMID:26153420 "Unexpectedly, profilin binds tighter to the R258C monomer, which will
   increase the pool of globular actin (G-actin)."].

The interesting negative: the only variant position sitting *in* the ≤4 Å cross-strand contact
set is **T196S (rs1803028), a non-pathogenic polymorphism**. Interface contact is neither
necessary nor sufficient for pathogenicity here.

## Finding 5: five of the eight Ensembl-Compara rows, and all five AgBase ISS rows, are single-experiment projections

The reference-projection check applied to the *donors* rather than to ACTA2:

- **`PMID:24204762`** (rat, hepatic stellate cells) is the sole source of **five** rat Acta2
  annotations that Compara transfers to human: `GO:0061870`, `GO:0061874`, `GO:2000491`,
  `GO:0070374` (all IMP) and `GO:0001725` (IDA). One siRNA experiment → five human rows.
  The paper's own framing matters for one of them: [PMID:24204762 "In this study, we hypothesized
  that Acta2, which is upregulated during stellate cell activation, has a critical functional
  role in stellate cell phenotypic behavior during the wound healing response."] — Acta2 is
  *downstream of* activation, and the assays reported are motility and contraction of
  already-activated cells [PMID:24204762 "Inhibition of Acta2 using several different techniques
  had no effect on cytoplasmic actin isoform expression, but led to reduced cellular motility and
  contraction."]. The ERK row rests on a correlation the authors state as one
  [PMID:24204762 "Additionally, Acta2 knockdown was associated with a significant reduction in
  Erk1/2 phosphorylation compared to control cells."].
- **`PMID:10633868`** (chick cardiogenesis, antisense knockdown of smooth-muscle α-actin) is the
  sole source of **all five** chicken ACTA2 (P08023) annotations that AgBase transferred to human
  by ISS: `GO:0010628`, `GO:0030027`, `GO:0030175`, `GO:0044297` (IDA) and `GO:0090131` (IMP).
- The two `GO:0019901 protein kinase binding` rows (IEA-Compara and ISS-ParkinsonsUK-UCL) are the
  **same inference from the same source**: mouse Acta2 (P62737), one IPI, `PMID:21307259`, with
  the partner recorded as `Q5S007` = **LRRK2**. Two pipelines, one line of evidence. The paper is
  a synaptic-vesicle study, a compartment where the actin present is overwhelmingly β/γ
  cytoplasmic; the isoform assignment is the curator's and is left standing, but recorded as
  worth confirming.

## Finding 6: nine Reactome rows are one assertion

`GO:0005829 cytosol` TAS appears nine times, once per Reactome reaction (R-HSA-445699, -445700,
-445704, -445705, -9604664, -9914537, -9934294, -9934410, -9934486). These are per-reaction
exports of a single statement — that ACTA2 participates as a cytosolic entity — not nine
findings. Reviewed once, with the other eight rows pointing at that reasoning.

## Marker-expression annotations, and the bulk-proteomics rows

ACTA2 is the standard immunohistochemical marker for smooth muscle, pericytes, mesangial cells,
peritubular myoid cells and myofibroblasts. Several GOA rows are the residue of that use:

- `GO:0072144 glomerular mesangial cell development` IEP rests on a paper that says outright what
  the antibody was for: [PMID:17464107 "In order to determine the characteristics of human
  glomerular development, we investigated the process of glomerular development by staining fetal
  and infant kidneys for CD31, CD34 and FB21, markers for endothelial cells, alpha-smooth muscle
  actin (alpha-SMA), a marker for mesangial cells, and nephrin, a marker for podocytes."]
- `GO:0072051 juxtaglomerular apparatus development` IEP transfers from rat Acta2, whose source
  (PMID:30645697) is an *in vitro* differentiation of amniotic-fluid stem cells into
  "juxtaglomerular-like cells".
- `GO:0005604 basement membrane` transfers from a rat IDA whose source (PMID:30476341) is a fetal
  rat testis toxicology study, where α-SMA stains the peritubular myoid cell layer that lies
  *against* the seminiferous tubule basement membrane. Adjacency, not localisation. **This row is
  ACTA2-specific: ACTG2 does not carry it**, so basement membrane is not a smooth-muscle-actin-wide
  annotation the way the extracellular HDA rows are. And it must be kept apart from the
  `GO:0005576` IBA below: the IDA is on a different term and reaches human ACTA2 by Ensembl
  Compara, not through PAINT, so "the seed's basement-membrane IDA was generalised upward into the
  IBA" is a reconstruction that neither source records.
- `GO:0006936 muscle contraction` transfers from a rat IDA whose source (PMID:11953441) is a
  paper on transcriptional regulation of the *Acta2 promoter* in osteoblasts. The conclusion is
  right for ACTA2 on entirely independent grounds; the donor row is not what makes it right.
- `GO:0005576 extracellular region` (IBA) comes from `PTN004322804`, a node with a **single**
  seed, rat Acta2 — whose own evidence for that exact term is itself only an `IBA`. The
  descendant IDA it does hold is the basement-membrane row above. **This row is the review's one
  `REMOVE`, and I changed my mind about it.** My first pass wrote `MARK_AS_OVER_ANNOTATED` on the
  ground that ACTA2 really is detected extracellularly. Two checks dissolved that ground.
  (Two facts here, kept apart. *Who seeded the node* is readable **directly from the GOA row** —
  the WITH/FROM is two tokens, `PANTHER:PTN004322804|RGD:621676`, one tree node and exactly one
  gene product — and the cached PAINT export
  `PTHR11937  PTN004322804  GO:0005576  C  IBD  false  RGD:621676` says it independently. The
  *circularity* is a different claim: that seed is also a co-recipient, carrying the identical
  `GO:0005576` IBA from the same node, so its own evidence for the exact term is an IBA. I had
  wrongly hedged the first as unreadable from GOA; the seed id simply arrives in RGD's namespace
  rather than as a UniProt accession.) First,
  the detection is already carried by this gene's own two HDA rows (`GO:0005576` from tears,
  `GO:0070062` from urinary exosomes) under `located_in` — the correct, weaker qualifier — so
  removing the IBA deletes an unsupported *functional* claim and keeps every observation. Second,
  the node audit shows **all six** conventional actins carry those same HDA rows, so extracellular
  detection is a family-wide bulk-proteomics signal, and PAINT nonetheless singled out only ACTA2
  and ACTG2 for an `is_active_in` assertion. The parallel ACTG2 review reached `REMOVE`
  independently; I verified ACTG2 has the identical pair of HDA references, so the two genes have
  the same evidence and a split verdict would have been a defect rather than a difference.
- `GO:0009615 response to virus` IEP: `PMID:16548883` carries this term for **20 entities**, all
  IEP, from one microarray/2-DE screen of EV71-infected rhabdomyosarcoma cells
  [PMID:16548883 "Altered transcripts include those encoding components of cytoskeleton, protein
  translation and modification; cellular transport proteins; protein degradation mediators; cell
  death mediators; mitochondrial-related and metabolism proteins; cellular receptors and signal
  transducers."]
- `GO:0005576` HDA (`PMID:23580065`, tears): **95 entities, all HDA**. `GO:0070062 extracellular
  exosome` HDA (`PMID:23533145`, prostatic-secretion exosomes): [PMID:23533145 "The analysis
  workflow is summarized in Figure 1A, and in total, close to 900 proteins were identified in the
  two EPS-urine exosome pools, representing the most comprehensive data for this clinically
  relevant fluid to date (Supplemental Table 2)."]
- `GO:0032991 protein-containing complex` IDA: `PMID:18468998` carries this term for **36
  entities**. Applying the ACTRT3 discriminator, the *phenotype* does not spread with it —
  `GO:0003073` stays on 3 entities — so this is per-protein complex-membership curation rather
  than a phenotype projection. It is still the root of the complex branch with no complex named.

## `GO:0005515` — five partners, one method

Ten rows: five partners × two references. Both references are BioPlex releases
(`PMID:28514442`, `PMID:33961781`) and IntAct logs the interactions under one method. IntAct holds
**320** interactions for P62736, of which **275 are `anti tag coip`**, and **172 of 239 partners
are singletons**. All five partner accessions resolve to reviewed canonical Swiss-Prot entries of
normal length (no ORFeome/TrEMBL substitution of the ACRV1 kind), but two are topologically
incompatible with cytosolic F-actin:

| partner | length | UniProt location |
|---|---|---|
| SCGB1A1 (P11684) | 91 aa | Secreted |
| GM2A (P17900) | 193 aa | Lysosome |
| YIPF2 (Q9BWQ6) | 316 aa | cis/trans-Golgi and late-endosome membrane |
| TCP11L2 (Q8N4U5) | 519 aa | Cytoplasm, cytoskeleton |
| MAP1LC3C (Q9BXW4) | 147 aa | Cytoplasm, cytoskeleton; autophagosome membrane |

## Retraction / erratum audit

21 cited PMIDs checked against both the publication-type list and each cited article's own
`CommentsCorrections` block. One flagged: **`PMID:17994018` carries an erratum**, visible in the
cached record as "Erratum in Nat Genet. 2008 Feb;40(2):255." PubMed's correction record has a
**null PMID** — the corrigendum was never indexed as its own PubMed entry — so it is invisible to
both a publication-type search and a PMID follow. Crossref resolves it:
`10.1038/ng0208-255c`, recorded as `update-to: 10.1038/ng.2007.6` with type `erratum`. Its content
is not retrievable from any open source queried here. Nothing in this review rests on
`PMID:17994018` alone: seven of its nine reported variants (T117, Q118, C149, A154, C258, H258,
N353) are independently reported by `PMID:19409525`, and the two that are not (H135, G292) are
used here only as variant positions, not as evidence for any GO term.

## Annotation gaps

0. **`GO:0017022 myosin binding`** — Finding 1, "sharpest instance". Proposed with `IDA` from
   `PMID:26153420`.
1. **`GO:0005884 actin filament`** — Finding 1. Proposed.
2. **`GO:0006939 smooth muscle contraction`** — live term, definition explicitly
   "Force generation involves a chemo-mechanical energy conversion step that is carried out by the
   actin/myosin complex activity" and "Smooth muscle differs from striated muscle in the much
   higher actin/myosin ratio". 30 human annotations across 17 gene products, **including MYH11 and
   MYLK — but not ACTA2 or ACTG2**, the actins of the very complex the definition names, and
   MYH11 is ACTA2's partner in that complex and in the same disease family. Proposed as the
   replacement for the generic `GO:0006936`.
3. **`GO:0005524 ATP binding`** — UniProt carries the `ATP-binding` and `Nucleotide-binding`
   keywords and a `GO:0016887 ATP hydrolysis activity` ISS, but GOA has no `GO:0005524` row.
   The gap is family-wide rather than gene-specific (ACTA1 has it by TAS, ACTC1 by IDA; ACTA2,
   ACTB, ACTG1, ACTG2 have none). Likely cause: `GO_REF:0000043`, the Swiss-Prot-keyword route,
   now returns **zero** human annotations — verified, so the keyword no longer produces a GO row
   for any human protein.

   **The obvious donor for the ISS is wrong, and checking it is the point.** The natural choice
   was `P68137` (Sus scrofa ACTA1), which already supplies this gene's `GO:0016887` ISS. But
   QuickGO returns **zero** `GO:0005524` rows for `P68137` and zero annotations anywhere under
   `GO:0000166 nucleotide binding` — so an ISS from it would have transferred an annotation the
   donor does not hold. That is the same shape as the WITH/FROM discipline applied to incoming
   rows, turned on an outgoing proposal. The donor used instead is **human ACTC1 (`P68032`), which
   holds `GO:0005524` by IDA** from [PMID:16611632], a same-species conventional actin with direct
   experimental evidence.

## Cross-gene note for the ACTG2 reviewer (a claim, not a fact — please verify)

ACTG2 carries `GO:0032982 myosin filament` by ISS (`GO_REF:0000024`, AgBase) from
`UniProtKB:F1P476`, which resolves to an **unreviewed TrEMBL chicken entry whose gene name is
ACTA2**, not ACTG2. Three separate concerns — an actin annotated to a myosin structure, a
paralog donor, and an unreviewed source. Not investigated further here because it is not an
ACTA2 row.

Where the two reviews agree, each having derived it independently: the three-node structure of
`GO:0005884` and the zero-reach for both smooth-muscle actins; the `PTN004322804` reverse-reach
result; `REMOVE` on the `GO:0005576` IBA; and `GO:0005200` being correctly retained (I verified
ACTA2 is in the ten-gene retained set and that none of the eight IRD-negated nodes contains it,
rather than inheriting the claim). Where they should still differ: ACTA2 is the vascular/aortic
isoform with an arterial disease spectrum (AAT6, MYMY5) plus multisystemic SMDYS, while ACTG2 is
the enteric/visceral isoform with a visceral-myopathy/megacystis-microcolon spectrum, so the
tissue-specific process terms must not be harmonised between them.

Two method notes prompted by #2303, checked here:

- **The `"reviewed" in entryType` substring bug does not affect this script.** "reviewed" is a
  substring of "unreviewed (TrEMBL)", so that test silently promotes every TrEMBL source. This
  analysis tests `"Swiss-Prot" in entryType`, which is not a substring of the unreviewed form;
  verified by grep over the source. The two TrEMBL donors it reports (Candida ACT1, *C. elegans*
  act-5) are correctly labelled.
- **The panel reproduces ACTL8's committed numbers on all nine shared members**, not four of
  fourteen. That is because this script inherited ACTL8's hand-defined conservative amino-acid
  groups by way of the ACTL10 analysis, rather than re-deriving them as `BLOSUM62 > 0`. Same-named
  metric, different measurement — and the divergence falls on exactly the divergent genes, where
  the two definitions disagree most. Whoever harmonises these panels should fix the *definition*
  once rather than the numbers repeatedly.

## Reproducibility

`ACTA2-bioinformatics/analyze_acta2.py` regenerates `results.json` and `RESULTS.md` in full from
public APIs and repo files; `git diff` after a run is the check that nothing in the report was
hand-edited. Guards that abort the run rather than degrade: single point of `GO:0005200`
assertion in PAINT; reproduction of ACTL8's committed interface tallies for nine shared panel
members; ACTA2's own sequence length against the panel median (the ACTL10 truncation artefact);
the three numbering controls; the `PMID:26637293`-derived contact-set control; QuickGO page
coverage with explicit pagination; strict duplicate-YAML-key loading with raw-vs-parsed
`reference_id` reconciliation; and `existing_annotations` minus `NEW` rows against the GOA row
count.
# Current interpretation notice

The 2026-09-26 source audit appended at the end supersedes the earlier action recommendations and several historical computational interpretations below. In particular, exact-term-only donor searches do not demonstrate circular PAINT evidence; extracellular detection is not disproved by the intracellular core role; broad cytoplasmic locations remain core; and a structural protein can contribute to context-dependent signaling. The earlier journal and immutable bioinformatics artifacts are retained as provenance, not as current conclusions.

## 2026-09-26 — source-specific re-review

This audit used the review, annotation-reviewer, and core-function-synthesizer skills. The verified starting point was main `0efff18e63a816029f64fa64bea40bef0c68c320`, with no overlapping open ACTA2 PR. Human ACTA2 is HGNC:130 / UniProt:P62736; the cached record lists ACTSA and ACTVS as synonyms and GIG46 as an ORF name. The [HGNC-linked Ensembl record](https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107796) and [Reactome ACTA2 entity](https://reactome.org/content/detail/R-HSA-445792) corroborate the identity. All local starting files, including the pre-existing bioinformatics directory and genuine Affinage report, matched the remote main blobs.

The starting review had 50 source annotations and three prior NEW proposals. All fields outside `review` on the 50 source annotations were preserved, including qualifiers and identifiers. The redundant prior NEW actin-filament location was withdrawn: [GO:0005884](https://amigo.geneontology.org/amigo/term/GO:0005884) is part of the already represented actin cytoskeleton. ACTA2 filament formation remains central in the biological summary and core descriptions. The two specific molecular-function proposals, myosin binding and ATP binding, were retained with revised, bounded evidence. No new biological-process term was added. There was no ACTA2/P62736 entry in the cached GO-CAM index.

### Research access and provenance

The required Falcon research and publication-cache tasks ran concurrently. Falcon dependency setup failed after three PyPI DNS retries (about 8.5 seconds); the configured perplexity-lite fallback also failed during dependency setup after three retries (about 10.7 seconds). Neither provider was reached, and neither generated an artifact. The actual wrapper log is `/tmp/ACTA2-falcon.log`; no manual text was written under a provider filename. The existing `ACTA2-deep-research-affinage.md` is genuine pre-existing output and was read as a lead, not as primary evidence. Publication caching completed successfully with all 32 PMIDs cited in the starting YAML and notes already present (`/tmp/ACTA2-publications.log`). No machine source was changed and no additional publication identifier was introduced by this audit.

Source availability in the YAML describes the local cache. External access does not make the local cache complete. In particular, the local 26153420 and 30476341 records lack full Results/Methods coverage; 33961781 is incomplete; and the 18468998 extraction lacks the key Table 3 cells. These limitations are recorded even where indexed primary text supplied the missing material. Abstract-only records remain marked unavailable for full text. CAPTCHA, publisher access failures, and incomplete extraction were not treated as evidence that the full paper omits an assay.

### PAINT, mappings, and donor chains

The cached `interpro/panther/PTHR11937/PTHR11937-paint.tsv` was inspected. IBA source entities now use the ancestral PTN node, rather than a list of extant members. PTN004322804 is the extracellular-region assertion; PTN002631484 is actin cytoskeleton; PTN000940351 is structural constituent of cytoskeleton. The extracellular node has experimental descendant grounding in the rat basement-membrane annotation. The historical exact-term-only query found IBA at the parent but IDA at its descendant; that result does not establish circularity. Human extracellular HDA provides independent support for a broad non-core extracellular pool. No claim about a particular secretion route or extracellular actomyosin mechanism is made.

All Compara and ISS rows now include proximate source identifiers and source-specific assessments. Rat P62738 and ENSRNOP00000073101 denote the same donor; dual identifiers are not classified as circular evidence. Mouse P62737/ENSMUSP00000048218 supply the kinase-partner inference; chicken P08023 supplies the five developmental localization/process rows; pig skeletal actin P68137 supplies intrinsic ATP-hydrolysis similarity. The existing JSON/report were inspected as historical source snapshots, not rerun. Their raw provenance and sequence comparisons remain useful; donor counts, exact-term-only evidence exclusions, and guessed pipeline or PAINT repair explanations are not adopted.

### Decisions that required primary-source reassessment

**Rat stellate-cell experiments (PMID:24204762).** The full cached study was read, including culture timing and Figure 7. Antisense interventions began during activation of freshly isolated cells, so the experiments cannot be dismissed as applying only after activation. Acta2 perturbation affects migration and collagen-lattice contraction. Acta2 siRNA reduces ERK1/2 phosphorylation while the measured beta-actin and tubulin controls are unchanged. The contextual migration, contraction, activation, and positive ERK regulation assignments are retained as non-core. This does not assign kinase activity to ACTA2 or prove isoform exclusivity. The mouse cardiac-fibroblast compensation study (PMID:36007455) addresses a different cell type and perturbation context and does not refute these rat results.

**Rat basement membrane (PMID:30476341).** [Indexed primary PMC Results and figure text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6390659/) describe both staining around the basement-membrane region, presumed peritubular myoid cells, and basement-membrane deposition. The distinction between extracellular matrix incorporation and closely apposed Acta2-positive cells remains unresolved at the described imaging resolution. The exact basement-membrane transfer is UNDECIDED. Absence of a signal peptide is not used to disprove extracellular localization, and the paper is not confidently labeled a miscitation.

**Human ACTA2–myosin experiments (PMID:26153420).** [Indexed primary Results and Methods/SI](https://pmc.ncbi.nlm.nih.gov/articles/PMC4534267/) specify recombinant human ACTA2 and human smooth-muscle myosin MYH11 with light chains. This resolves the earlier uncertainty about myosin species/source. Wild-type human ACTA2 filament motility provides direct support for the myosin-binding proposal and for the smooth-muscle contraction refinement. The paper also measures filament dynamics and regulatory-protein interactions; its actin-activated myosin ATPase measurements are not intrinsic ATP hydrolysis by ACTA2. No claim is made that every ACTA2 variant acts exclusively through myosin binding. The [smooth-muscle contraction definition](https://amigo.geneontology.org/amigo/term/GO:0006939) includes the force-generating actin/myosin apparatus; ACTA2 contributes the structural actin component itself. The [myosin-binding definition](https://flybase.org/cgi-bin/cvreport.pl?id=GO:0017022) matches the direct interaction.

**Adrenergic-receptor purification (PMID:18468998).** An independent annotation-reviewer consultation recovered [primary Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC2441552/): aortic smooth-muscle actin was detected in TAP-alpha1D-adrenergic-receptor purification from HEK293 cells, with one distinct peptide, 4% coverage, and a 42-kDa listing. It was not the ACTA2-specific follow-up target in the dystrophin/syntrophin experiments. Broad protein-complex association is retained as non-core at the purification resolution. Lack of an ACTA2-specific receptor mechanism does not negate the positive association.

**Chicken developmental annotations (PMID:10633868).** The abstract explicitly supports alpha-SMA in lamellipodia/filopodia and an antisense effect on motile appendages and mesenchymal-cell migration. These are retained as non-core. The separate gene-expression regulation and cell-body localization experiments could not be resolved without full text and remain UNDECIDED. [GO:0044297](https://amigo.geneontology.org/amigo/term/GO:0044297) is the body of a projection-bearing cell and is not restricted to neurons. Reuse of one paper for several different assays is not itself an annotation defect.

**Kidney and kinase-partner uncertainties.** PMID:17464107 is a human fetal/infant alpha-SMA marker study, independently matched to the [J-STAGE primary abstract](https://www.jstage.jst.go.jp/article/tjem/212/1/212_1_81/_article) by the consulting reviewer. The unavailable full Results leave mesangial-development participation unresolved. PMID:30645697 similarly leaves juxtaglomerular-development participation unresolved beyond accessible rat renal-like-cell marker expression. Neither is rejected merely because its evidence code is IEP. Mouse Acta2–LRRK2 provenance from PMID:21307259 is resolved at the database level, but the isoform-specific primary experiment/table was unavailable; both inferred kinase-binding rows remain UNDECIDED. A neuronal study context alone does not establish a wrong-actin assignment.

**Expression response versus effector mechanism.** The cached UniProt induction statement explicitly identifies ACTA2 upregulation in the EV71 study PMID:16548883. The [response-to-virus definition](https://amigo.geneontology.org/amigo/term/GO:0009615) includes stimulus-dependent gene-expression changes; the contextual response is retained without assigning antiviral effector activity. The rat TGF-beta response from PMID:17043753 is likewise explicitly supported by the accessible alpha-SMA induction result.

**Broad locations and generic binding.** Broad cytoplasm/cytosol/cytoskeleton terms are retained as core when they correctly locate ACTA2 at the source's resolution. Abstract-only primary IDAs are not forced into more specific compartments or assigned invented counterstain methods. Reactome events were read individually, separating the ACTA2-containing entity's cytosol location from myosin catalysis, NOTCH expression regulation, or extracellular ligands of the dystrophin complex. Extracellular HDA detections are retained as non-core with peptide-level access limits, without claiming contamination. The ten BioPlex generic protein-binding rows are removed because no specific molecular function is established for those pairs. This does not deny the associations or infer impossible contacts from usual subcellular compartments; matching BioPlex 2.0/3.0 pairs receive the same decision.

**ATP binding and hydrolysis.** UniProt explicitly records ATP hydrolysis by similarity to pig ACTA1 P68137. The ATP-binding proposal remains an inference from conserved conventional-actin biochemistry, the cached sequence/structure comparison, and UniProt ATP-binding classification. Human ACTC1 P68032 has historical ATP-binding IDA provenance from PMID:16611632, but the original binding assay was not independently inspected. No human ACTA2 affinity or intrinsic hydrolysis rate is invented, and no pipeline retirement is inferred from a zero-result query. The [ATP-binding term](https://amigo.geneontology.org/amigo/term/GO:0005524) is a binding-branch term distinct from the seeded hydrolysis activity.

### Core and reference coherence

The core now has three distinct molecular activities: structural contribution, myosin binding, and intrinsic actin ATP hydrolysis. The duplicate structural myofibroblast core was consolidated, preserving context-dependent isoform compensation in the prose. Structural contact distances from the historical modeled comparison were removed from core prose; they are not experimentally measured distances on human ACTA2. Every reference assessment was reread, and source-identity verification is explicitly separated from unresolved scientific support. The 17994018 corrigendum exists at [the publisher DOI](https://doi.org/10.1038/ng0208-255c), but its content could not be inspected; an unread correction is not evidence of a disputed biological conclusion. The current core uses independent supporting sources.

The independent consultation supported the bounded receptor-complex retention and confirmed the human renal-marker source. A complete independent review of the stable draft was requested from the campaign coordinator. Targeted schema, ontology, quote, history, and rendering results are recorded in the matching new history and final publication manifest.

## 2026-09-26 PR #3164 review follow-up

Reviewed formal review 5850935287 in full against published head 45e0a9ceda8dfce51f0917c3da490bd9c917bea9. All 50 original GOA source assertions and the source fields of both retained NEW proposals remain unchanged.

- The extracellular-region IBA now remains UNDECIDED specifically for its `is_active_in` assertion. The PTN ancestral evidence and human HDA detection do not resolve extracellular ACTA2 molecular activity. This does not deny extracellular occurrence, alter the qualifier, or infer that the donor experiment is wrong. The separate HDA `located_in` judgment remains non-core.
- The mesangial-development row remains UNDECIDED, with its actual cached assay stated explicitly: alpha-SMA is used as a mesangial marker. The quote is now attached to the review. Marker expression does not demonstrate mechanistic participation; full-paper access remains insufficient to claim the curator had no additional evidence.
- `full_text_unavailable` is false for PMID:26153420, PMID:18468998, PMID:30476341 and PMID:33961781 because extracted full-text sections are available locally. This supersedes the earlier availability convention in these notes: an incomplete extraction is not the same as no full-text sections. All existing warnings about missing Results, table cells or pair records remain. In particular the rat ACTA2 staining descriptions came from indexed primary PMC Results/figures at https://pmc.ncbi.nlm.nih.gov/articles/PMC6390659/ and are absent from the local extraction; they were not newly cached or silently inserted.
- The two retained NEW molecular functions pass a same-role comparator check in existing immutable GOA records: human ACTA1 has myosin binding and ATP binding (TAS), and ACTB has ATP binding (IEA through UniProtKB-KW:KW-0067). These comparisons support appropriateness of the functions, while the myosin proposal depends on direct human ACTA2 experiments and the ATP-binding inference on the conserved pocket plus its UniProt record. No cause for a missing electronic annotation is inferred.
- The ATP-hydrolysis core now describes hydrolysis without adding a redundant separate binding core. Binding is an intrinsic prerequisite for the reaction and remains the separately reviewed MF proposal. The biological summary includes the experimentally identified MYH11 partner, myosin light-chain phosphorylation control, regulator interactions, and the curated vascular/multisystem disease scope.
- Reference identity is separated from claim support. UNVERIFIED judgments retain the specific uninspected experiment/corrigendum caveat; verified title/identifier alone does not resolve the scientific claim. In particular, an unread corrigendum does not establish that an ACTA2 conclusion is disputed.

No cache or machine-source content was edited. Targeted validation, append-only history validation, source-object comparison and HTML regeneration are recorded in the handoff manifest.

## 2026-09-27 status-label follow-up

The biological review has approval and all required publications are cached.
Two validation advisories nevertheless remain: qualifier-dependent extracellular
decisions and no direct annotation quote from the retained provider report.
Set `status: DRAFT` to follow the literal status enum, which reserves `COMPLETE`
for reviews without validation warnings. This changes no biological decision,
reference assessment, source assertion or core function. The existing approval
describes the preceding biological content; the status-only commit is separately
validated and remains subject to the normal PR checks.
