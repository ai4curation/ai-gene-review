# ADAMTSL5 (Q6ZMM2) — bioinformatics support for the GO annotation review

Reproduce with:

```bash
uv run python genes/human/ADAMTSL5/ADAMTSL5-bioinformatics/resolve_withfrom.py
uv run python genes/human/ADAMTSL5/ADAMTSL5-bioinformatics/family_propagation_census.py
```

`resolve_withfrom.py` must be run first — the census reads its `withfrom_resolution.json`.
All numbers below are produced by those two scripts; none is hand-entered.

---

## 1. ADAMTSL5 has no metallopeptidase domain — verified three independent ways

The campaign brief flagged "ADAMTSL proteins lack the catalytic metalloprotease domain"
as a *lead to establish, not a premise*. It is established here:

| source | finding |
|---|---|
| UniProt `CC CAUTION` | "Although strongly similar to members of the ADAMTS family it lacks the metalloprotease and disintegrin-like domains which are typical of that family." |
| The gene's own primary paper (`PMID:23010571`) | "In contrast to ADAMTS proteases, ADAMTSLs lack a catalytic domain and thus have no proteolytic activity." |
| Sequence scan (this analysis) | The zinc-binding metalloprotease signature `HExxHxxGxxHD` is **absent**, and there is **no `HExxH` substring at all** in the 481-residue sequence. |
| InterPro match set | TSP1 repeat, netrin domain, TIMP-like OB-fold, ADAMTS spacer-1, ADAMTS cys-rich-3. **No peptidase/reprolysin (M12B) signature.** |

**The predicted failure mode did NOT occur.** ADAMTSL5's GOA contains no
peptidase/metallopeptidase term of any kind — no `GO:0004222`, no `GO:0008237`, no
`GO:0006508`. This was a *hypothesis*, and it is reported here as **not confirmed**,
not as a finding. PAINT in fact handled the catalysis question correctly (§3).

Domain architecture (UniProt FT): signal peptide 1–42, mature chain 43–481,
TSP type-1 domain 45–97, NTR domain 360–479. At 481 aa ADAMTSL5 is by far the
smallest member of the family (others 951–1935 aa).

Incidental, verified: the psoriasis autoantigen peptide `VRSRRCLRL` (`PMID:26621454`)
occupies residues **67–75**, inside the TSP type-1 domain.

---

## 2. The `GO:0031012` IBA is exceptionally well supported — 16/16 donors

WITH/FROM has **17 tokens**: 16 protein donors + the tree node `PANTHER:PTN000347317`.
The GOA field matches the cached PAINT seed list **exactly** (asserted in code:
`goa_tokens - seeds == {"PANTHER:PTN000347317"}` and `seeds - goa_tokens == set()`).

**All 16 protein donors carry their own experimental (IDA/HDA) annotation** to
`GO:0031012` or a descendant. So `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK`
would be factually contradicted by the measurement; there is no propagation defect to
report on this row.

One token is **self-referential** (`UniProtKB:Q6ZMM2`) — a PAINT curator judging the
function core, which is valid.

### The donor set is heterogeneous, so the general term is the LCA

| donor location | donors |
|---|---|
| `GO:0031012` extracellular matrix | 14 |
| `GO:0005604` basement membrane | 4 |
| `GO:0005614` interstitial matrix | 1 |
| `GO:0001527` microfibril | 1 |

Four distinct locations. `GRANULARITY_MISMATCH` requires the donors to **agree**; they
do not, so `GO:0031012` **is** the correct LCA and refining it would mean arbitrarily
preferring one donor's compartment. → **ACCEPT, no specificity upgrade.**

Also checked (ACRV1-style, negative): the IBA does **not** land above its donors — 14
of 16 donors hold the term itself — so **no downward MODIFY is warranted**.

### Resolver gotchas measured here (each cost a cycle)

- **QuickGO's `geneProductId` rejects MOD ids outright** (HTTP 400, "contains invalid
  values") for `MGI:MGI:109249`, `MGI:109249`, `FB:FBgn0003137`, `FBgn0003137`,
  `WB:WBGene00003242`, `RGD:621241`. It indexes UniProtKB only. A donor's own evidence
  can therefore only be queried through its resolved UniProt accession. The first
  version of the script silently printed "NONE" for every MOD token — a *silent
  degradation reading as a null result*. Fixed, and unqueryable is now its own state.
- **UniProt does not index the WBGene id.** `xref:wormbase-WBGene00003242` returns `[]`;
  UniProt keys WormBase xrefs on the CDS name (`C37C3.6`). Resolved via the WormBase
  REST (`WBGene00003242` → `mig-6`) then a UniProt symbol search.
- **That symbol search must be `gene_exact:`, not `gene:`.** Fuzzy `gene:mig-6` also
  returns mig-10 / mig-5 / mig-14 / mig-18 and puts the **wrong entry first** — the
  `size=1` trap in a new guise. With `gene_exact` the token resolves uniquely to
  `O76840` PPN1_CAEEL papilin (Swiss-Prot, 2167 aa), which holds `GO:0005604` by IDA.
  Getting 16/16 via a fuzzy head match would have been the right number for the wrong
  reason.
- 13 of 16 tokens are **multi-hit** (a Swiss-Prot entry plus TrEMBL fragments). All
  candidates are reported; the reviewed entry is the one queried.
- **QuickGO strips the DB prefix from WITH/FROM tokens.** `withFrom[].connectedXrefs[]`
  returns `{"db": "FB", "id": "FBgn0003137"}` as two separate fields, so comparing the
  bare `id` set against a GOA TSV WITH/FROM string yields **17 vs 17 tokens reported as
  "not identical"** for data that is actually the same. Reassemble as `db + ":" + id`
  before any set comparison.

### Cross-check against the concurrently reviewed sibling ADAMTSL3

Derived from QuickGO directly rather than read off the sibling branch. ADAMTSL3
(`P82987`) carries a `GO:0031012` IBA whose WITH/FROM token set is **exactly identical**
to ADAMTSL5's — same node, same 17 tokens, verified as a set equality in a single
serialisation. Two independent derivations of one node agree. ADAMTSL3 also shares the
`GO:0071953` TAS from `PMID:23962539` and the InterPro `GO:0030198` IEA, so all three of
this review's non-ACCEPT verdicts have a direct counterpart there.

---

## 3. The real PAINT defect: one node, incoherent propagation across the family

All eight human ADAMTSL/papilin proteins are in **PTHR13723**, and node
`PTN000347317` carries four IBD annotations (`GO:0031012`, `GO:0030198`,
`GO:0004222`, `GO:0006508`). Who actually received them:

| gene | subfamily | GO:0031012 | GO:0030198 | GO:0004222 | GO:0006508 |
|---|---|---|---|---|---|
| ADAMTSL1 | SF157 | – | – | – | – |
| ADAMTSL2 | SF147 | IBA | IBA | **NOT-IBA** | – |
| ADAMTSL3 | SF169 | IBA | – | – | – |
| ADAMTSL4 | SF144 | IBA | IBA | – | – |
| **ADAMTSL5** | SF173 | **IBA** | – | – | – |
| THSD4 | SF16 | IBA | IBA | – | – |
| PAPLN | SF281 | – | – | – | – |
| *ADAMTS1/9/10/17 (catalytic controls)* | | IBA | IBA | IBA | IBA |

**What PAINT got right.** The catalytic terms reached all four catalytic controls and
**none** of the seven non-catalytic members — with ADAMTSL2 carrying an explicit
`NOT|enables GO:0004222` (IKR at node `PTN002673039`). The family's loss of catalysis
is modelled correctly. This is the counter-example to the campaign's usual finding.

**What is incoherent.** From a *single* node, `GO:0031012` reached 5 of 7 and
`GO:0030198` reached 3 of 7, in no biologically coherent pattern:

- **PAPLN receives neither**, although **three of its own orthologs are seeds** for
  `GO:0031012` at that very node — fly `Ppn` (`FB:FBgn0003137`), mouse `Papln`
  (`MGI:MGI:2386139`) and worm `mig-6/ppn-1` (`WB:WBGene00003242`). Human PAPLN has
  **no IBA at all** (5 annotations, all IEA/TAS).
- **ADAMTSL1 receives neither** and likewise has **no IBA at all** (4 annotations).
- **ADAMTSL3 and ADAMTSL5 receive the location term but not the process term**, while
  ADAMTSL2/ADAMTSL4/THSD4 receive both.

**Consequence for this review, stated as a limit rather than as support:** ADAMTSL5's
*absence* of a `GO:0030198` IBA **cannot** be read as a deliberate curatorial judgement
that the process does not apply. The same gap left ADAMTSL1 and PAPLN with nothing at
all, so it is more likely a propagation failure than a decision. The case against
`GO:0030198` for ADAMTSL5 therefore rests on §4 and §5 only.

---

## 4. `GO:0030198` comes from a family signature that bundles proteases with non-proteases

`InterPro:IPR013273` is named, literally, **"ADAMTS/ADAMTS-like"** (family, 26,580
proteins) and carries exactly one GO mapping: `GO:0030198 extracellular matrix
organization`. The signature therefore lumps the catalytic ADAMTS proteases — for which
ECM organization is a direct consequence of ECM proteolysis — together with the
non-catalytic ADAMTS-like proteins, which have no such activity (§1).

This is the campaign's familiar shape one aspect over: not "a domain's name is not an
activity" (MF), but **a family signature too broad to carry a process** (BP).

## 5. The only direct test of ECM organization by ADAMTSL5 was negative

From `PMID:23010571` (full text): after showing colocalisation with fibrillin
microfibrils, the authors report

> "However, comparison of microfibril density in fBNL cell cultures grown in the
> presence of ADAMTSL5 or vector conditioned medium, did not identify a consistent
> difference (data not shown)."

and the abstract states colocalisation occurred "but without discernible effect on
microfibril assembly". Direct binding to fibronectin was also **not** supported.

**Weight of this negative, stated honestly:** it is a *"data not shown"* result from a
single exogenous-protein assay. It argues that no role in ECM/microfibril organization
has been **demonstrated**; it does not refute one. That supports
`MARK_AS_OVER_ANNOTATED`, and is **not** strong enough to earn `REMOVE`.

---

## 6. The three `GO:0005515` rows are one Y2H screen, on three hub proteins

All three rows come from `PMID:32296183` (HuRI). IntAct shows each partner logged under
**three sub-methods of the same experiment** — `two hybrid array` + `two hybrid prey
pooling approach` + `validated two hybrid`, MI-score 0.56. UniProt's `NbExp=3` is
therefore **one screen counted three ways**, replicating the ACRV1 finding on a second
gene.

Distinct-partner counts (derived as an entity *set*; IntAct records are not partners):

| protein | IntAct records | **distinct partners** | localisation | length |
|---|---|---|---|---|
| CYSRT1 (A8MQ03) | 1670 | **517** | cornified envelope | 144 aa |
| KRTAP5-9 (P26371) | 842 | **213** | intracellular hair-keratin matrix | 169 aa |
| FHL5 (Q5TD97) | 316 | **108** | nucleus (spermatid nuclei) | 284 aa |
| **ADAMTSL5 (Q6ZMM2)** | 22 | **12** | secreted / ECM | 481 aa |

Each partner is **topologically incompatible** with ADAMTSL5, a signal-peptide
(1–42) secreted ECM glycoprotein: it does not enter the cytoplasm, nucleus, or cornified
envelope. Decided **per partner**, all three come out the same way — unreplicated
screen noise → `MARK_AS_OVER_ANNOTATED`.

All three partner accessions resolve to **reviewed canonical Swiss-Prot** entries with
matching lengths — no TrEMBL/ORFeome substitution of the ACRV1 kind. Reported as a
negative.

The gene's **real** binding partners, FBN1 and FBN2, come from the same IntAct record
by `pull down` from `PMID:23010571`, and are captured by `GO:0050436 microfibril
binding`.

---

## 7. `GO:0071953 elastic fiber` is a bulk review-based assignment

Projection test by reference (entities derived as a set, not from the annotation total):

| reference | annotations | distinct entities | per-term spread |
|---|---|---|---|
| `PMID:23010571` (primary paper) | 6 | **2** | `GO:0031012` 2; the rest 1 each |
| `PMID:23962539` (elastic-fibre review) | 66 | **62** | `GO:0071953` **41 entities**; `GO:0001527` 15 |

`PMID:23010571` annotates only ADAMTSL5 and its mouse ortholog — **gene-specific
curation, not a projection.** Negative result, reported.

`PMID:23962539` is a **review** (`publication_type: REVIEW`, `full_text_available:
false`) used as the TAS source for **62 entities**, assigning `GO:0071953` to **41** of
them. Its abstract never mentions ADAMTSL5. Notably the *same* curation from the *same*
review assigned the more specific `GO:0001527 microfibril` to 15 other proteins —
including THSD4/ADAMTSL6 — so the specific term was demonstrably available and was not
chosen for ADAMTSL5.

### The specific term is missing from GOA but present in UniProt

UniProt's DR block carries `GO:0001527; C:microfibril; IDA:UniProtKB`, but **GOA does
not have it** (verified: QuickGO returns exactly 12 annotations for Q6ZMM2, matching the
GOA TSV, and `GO:0001527` is not among them). So the gene's best-evidenced and most
specific localisation is absent from GOA while a weaker, broader TAS row is present.

`GO:0001527` is current (not obsolete, no `secondaryIds`) and is a **`part_of` child of
`GO:0071953`** — so replacing the TAS row with it retains the parent by closure while
gaining precision, and matches the merged ADAMTSL4 review, which independently proposed
`GO:0001527` as a NEW term.

### An ontology issue this surfaces

`GO:0001527 microfibril` is `part_of` `GO:0071953 elastic fiber`, which asserts that
every microfibril is part of an elastic fiber. That contradicts `GO:0001527`'s **own
definition** — "Extracellular matrix components occurring independently **or** along
with elastin" — and contradicts the ciliary zonule, a fibrillin-microfibril structure
essentially devoid of elastin. Recorded in `suggested_questions`.

---

## 8. Checks run that came back negative (recorded so they are not re-run blind)

- **Retraction / erratum / expression-of-concern**: all 9 PMIDs relied on
  (23010571, 23962539, 32296183, 26621454, 27857980, 28482118, 33197513, 37330172,
  38524140) checked via PubMed publication types **and** each record's own
  `CommentsCorrections` (a Publisher Correction is invisible to a pubtype query).
  **None flagged.** `PMID:26621454` has two `Comment in` entries — commentaries, not
  corrections.
- **Partner accession integrity**: all three IPI partners are reviewed canonical
  Swiss-Prot entries at their canonical lengths. No dead or truncated accessions.
- **IBA-above-donor precision defect** (ACRV1 shape): absent — the IBA sits at the term
  14 of 16 donors hold.
- **Reference projection** for the primary paper: absent — 2 entities.
- **Dead-accession check**: every WITH/FROM UniProt lookup returns a named entry; the
  script raises rather than reporting a silent zero.
