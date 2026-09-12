# AGTRAP (ATRAP, Q6RW13) — review notes

Human gene, HGNC:13539, 159 aa, UniProt `PE 1: Evidence at protein level`.
PANTHER `PTHR16521` / InterPro `IPR009436` / Pfam `PF06396`, a single-subfamily
family (`PTHR16521:SF3`) with **1380 member proteins but only 5 Swiss-Prot
entries** (human, mouse, rat, orangutan, *Xenopus* — all AGTRAP orthologues, no
paralogues). Reviewed-member counts from `interpro/panther/PTHR16521/` are the
Swiss-Prot subset, not the family.

## The shape of this gene's GO record

`AGTRAP-goa.tsv` has **199 rows**. The `fetch-gene` stub seeded **199**
`existing_annotations` entries, so nothing was collapsed here (unlike ACTR5 /
ADAMTSL5). Counts reconciled before review began:

```
wc -l < AGTRAP-goa.tsv        -> 200 (199 + header)
grep -c '^- term:' *-ai-review.yaml -> 199
```

Composition of the 199 rows:

| rows | content |
|---|---|
| 187 | `GO:0005515` protein binding, IPI, IntAct |
| 1 | `GO:0042802` identical protein binding, IPI (self, isoform 2) |
| 3 | UniProt SubCell IEAs (ER membrane, Golgi membrane, cytoplasmic vesicle membrane) |
| 1 | `GO:0005794` Golgi apparatus, IDA, HPA |
| 2 | IBA (plasma membrane; regulation of blood pressure) |
| 1 | `GO:0038166` angiotensin-activated signaling pathway, IEA from InterPro |
| 4 | Ensembl Compara IEAs (`GO:0004945`, `GO:0001666`, `GO:0005886`, `GO:0005938`) |

So **94% of this gene's GO record is `protein binding`**, and the interaction
that the gene is named for — AGTR1 — is **not in it at all**.

## Finding 1: `GO:0004945 angiotensin type II receptor activity` is a symbol confusion amplified by orthology projection

The human row is `enables GO:0004945`, IEA (`ECO:0000265`, `GO_REF:0000107`,
Ensembl Compara) with `UniProtKB:Q9WVK0` = mouse Agtrap (Swiss-Prot,
`ATRAP_MOUSE`, a true 1:1 orthologue — resolved, not assumed).

Going one level deeper than the donor (QuickGO,
`geneProductId=UniProtKB:Q9WVK0`): mouse Agtrap holds `GO:0004945` by **IMP from
`PMID:10425188`**, assigned by MGI. That paper is *"Increased vasoconstrictor
response of the mouse lacking angiotensin II type 2 receptor"* — an **Agtr2**
knockout study. Its abstract never mentions Agtrap/ATRAP.

Querying **by reference** rather than by gene makes the mechanism explicit:

```
QuickGO annotation/search?reference=PMID:10425188  -> 13 annotations, 3 entities
  Agt    (P11859)  5 rows
  Agtr2  (P35374)  5 rows  incl. GO:0004945 enables IGI   <- the correct holder
  Agtrap (Q9WVK0)  2 rows  incl. GO:0004945 enables IMP   <- the confusion
```

Agtr2 and Agtrap both received `GO:0004945` from the same paper. Only one of
them is an angiotensin receptor.

Independent of provenance, the term is biologically false for this protein:

- `GO:0004945` is defined as *"An angiotensin receptor activity that acts via Gi
  protein coupling and cGMP (NO) generation"*. AGTRAP is a 159-aa protein with
  **three** TM helices (UniProt FT 24-44, 56-76, 87-107), not a 7TM GPCR, and
  has no G-protein coupling anywhere in its record.
- The gene's founding paper tested exactly this and excluded it:
  `PMID:10358057` — *"ATRAP interacts specifically with the carboxyl-terminal
  domain of the AT1a receptor but not with those of angiotensin II type 2 (AT2),
  m3 muscarinic acetylcholine, bradykinin B2, endothelin B, and
  beta2-adrenergic receptors."*

So the annotation asserts, of the protein named for the **type-1** receptor, an
activity of the **type-2** receptor that was experimentally excluded for it.
Action: `REMOVE`.

**The error has spread to three species.** Rat Agtrap (`Q642A2`) carries
`GO:0004945` twice — by Ensembl IEA *and* by RGD ISO — so human, rat and mouse
all currently assert it. Fixing the MGI row would clear all three.

## Finding 2: `GO:0008217 regulation of blood pressure` — right term, wrong evidence

The human row is IBA from `PANTHER:PTN002703102` + `MGI:MGI:1339977`. The PAINT
file (`interpro/panther/PTHR16521/PTHR16521-paint.tsv`) shows the family has
exactly **two** IBD annotations, both seeded from mouse Agtrap alone:

```
PTHR16521  PTN002314244  GO:0005886  C  IBD  MGI:MGI:1339977  taxon:6072
PTHR16521  PTN002703102  GO:0008217  P  IBD  MGI:MGI:1339977  taxon:117571
```

and mouse Agtrap's **only** experimental `GO:0008217` row is the same
`PMID:10425188` IMP from Finding 1. So the chain human IBA -> PAINT node ->
mouse IMP terminates in a paper about a different gene.

The conclusion nevertheless survives on evidence nobody curated: `PMID:20093357`
(Oppermann/Castrop, JASN 2010) — *"Mean systolic BP was significantly higher in
Atrap-/- mice compared with wild-type mice."* Kept as `KEEP_AS_NON_CORE`
(organism-level physiology downstream of AT1R restraint, not AGTRAP's own
molecular function), with a `suggested_question` asking MGI to re-reference.

This is the inverse of the usual campaign finding: the propagation is sound and
the **donor's citation** is the defect.

## Finding 3: `GO:0001666 response to hypoxia` rests on one rat IEP

Human row: IEA from rat `Q642A2` (Swiss-Prot `ATRAP_RAT`, true orthologue).
Rat's own evidence: a single **IEP** from `PMID:17033689`, *"Vascular response to
hypoxic preconditioning in the immature brain"*. That reference annotates
exactly **2 entities in all of GOA** (rat Agtrap and Angptl4), both IEP — i.e. a
transcript-abundance change in neonatal rat brain. Same shape as AFF4's
`GO:0034976`. `MARK_AS_OVER_ANNOTATED`.

## Finding 4: 94% of the interaction record is one assay class, and the informative partners are in the other one

IntAct (`/intact/ws/interaction/findInteractions/Q6RW13`, all 617 evidences
retrieved; `len(results) == totalElements` asserted):

| publication | evidences | methods |
|---|---|---|
| PMID:32296183 (HuRI) | 276 | `validated two hybrid` 92 + `two hybrid array` 92 + `two hybrid prey pooling approach` 92 |
| PMID:25416956 (HI-II-14) | 202 | 68 + 67 + 67, same three sub-methods |
| 21 others | 139 | mostly Y2H; 27 `anti tag coip`, 3 BioID, 2 `anti bait coip`, 1 crosslink, 1 CLASH |

**92 x 3 and ~68 x 3 is the arithmetic of one screen logged three ways.** This
is the `NbExp=3` artefact (ACRV1, ADAMTSL5) confirmed by exact counts rather
than inferred: UniProt's `NbExp=3` for most AGTRAP partners is one experiment.
Overall **583/617 = 94.5%** of evidences are two-hybrid, and only **23 of 213
distinct pairs** carry any non-two-hybrid method.

The GOA import is drawn entirely from the Y2H side: all 188 binding rows trace
to 9 CCSB-lineage publications. Partner accessions resolved (132 distinct; all
resolved, `entryType.startswith("UniProtKB reviewed")` used so TrEMBL is not
silently promoted): **121 Swiss-Prot, 11 TrEMBL**, and several TrEMBL ones are
partial ORFeome clones rather than the canonical protein —

| GOA partner | length | canonical |
|---|---|---|
| `A0A0S2Z3E9` "FGA" | 84 aa | `P02671` 866 aa |
| `A0A0S2Z4D9` "GAD1" | 111 aa | `Q99259` 594 aa |
| `Q96AL5` "PBX3" | 367 aa | `P40426` 434 aa |
| `Q5JS98` "PBX3" | 455 aa | `P40426` 434 aa |
| `Q7L1H2` "STAG3L1" | 79 aa | — |

Topology check (`scratchpad/topology.py`): AGTRAP's only substantial
cytosol-facing surface is TOPO_DOM 108-159 — **52 residues**, 20 of them
disordered. Of the 131 non-self GOA partners, **28 are confined to the
mitochondrial matrix/inner membrane, the nucleoplasm, or the extracellular
space** and cannot reach that surface; 17 more are mixed; 67 are cytosol-facing;
19 have no recorded location. Reported as it came out — this is a supporting
argument, not the decisive one, because a majority of partners *are* nominally
accessible. The decisive argument is the assay structure above.

**The property that every screen row's verdict rests on, stated exactly.** An
earlier draft said, on all 178 rows, that "searching this partner independently
of the AGTRAP symbol found no follow-up study". I did not run 131 separate
partner searches, so that was an over-claim, and it was replaced by what was
actually measured (`scratchpad/nony2h_vs_goa.py`, which asserts
`len(results) == totalElements` and then asserts the property per partner):

```
GOA partner accessions (base): 132
GOA partners with no IntAct record under Q6RW13: 0
IntAct partners with any non-two-hybrid method: 23
   of those, present in GOA: 0
ASSERTION HELD: every GOA partner found in IntAct has two-hybrid methods only
```

Every one of the 132 GOA partners resolves in IntAct, every one is
two-hybrid-only, and the 23 partners that do have orthogonal support are
**disjoint** from the GOA set.

**The contrast is the finding.** The 23 pairs with non-Y2H (AP-MS / co-IP /
BioID) evidence are almost all membrane proteins — CYB5D2, ENPP6, MBLAC2,
TMEM47, TMEM106B, LAMP5, SLC15A3, SLC15A4, TMEM63A, CFTR, CHRNB1, SLC1A1,
SLC18A2, PAFAH2, TNFRSF10C — a coherent ER/endolysosomal membrane neighbourhood
for a 3-TM ER/Golgi protein. **None of them is in GOA.** GOA imported the assay
class whose partners are largely implausible and none of the class whose
partners fit the protein's own cell biology.

### A count that refused to add up, and what it turned out to be

First draft of the `PMID:16189514` reference note said "3 binding rows". The TSV has
**2**. The 3 was an IntAct *evidence* count, and the extra evidence is a canonical
`Q6RW13`-`Q6RW13` **self-pair that GOA did not import**. Chasing it corrected a
second claim: the `GO:0042802` row had been written as a self-interaction "detected
once, in the HuRI screen", which is true of the GOA row and false of IntAct —
`PMID:16189514` and `PMID:25416956` also report a canonical self-pair. All three are
the same CCSB clone collection in the same two-hybrid system, so the verdict
(`MARK_AS_OVER_ANNOTATED`) is unchanged, but it now rests on "recurrence on one
platform, never tested by another method" rather than on "seen once", which was
simply wrong.

Per-reference GOA binding-row counts, re-derived from the TSV rather than from prose:
`32296183` 91 (90 + the self row) · `25416956` 66 · `31515488` 10 · `26871637` 8 ·
`21516116` 4 · `25910212` 3 · `16189514` 2 · `19060904` 2 · `29892012` 2 = **188**.

### Three Y2H partners that survive scrutiny

Searching the partners rather than the symbol (the recall gap affinage cannot
close) turned up orthogonal validation for three. "Three" is what this search
found, not a proof that no fourth exists — the exhaustive statement available is
the IntAct one above, that no GOA partner has non-two-hybrid evidence:

- **PITPNC1 / RdgBβ** (`Q9UKF7`, 4 GOA rows) — `PMID:21728994`, titled for
  RdgBβ, not for AGTRAP: *"the PITP domain of RdgBβ interacts with the integral
  membrane protein ATRAP ... causing membrane recruitment"*. This is the one
  partner that yields an informative MF for AGTRAP itself: it is the membrane
  anchor. `MODIFY` -> `GO:0043495 protein-membrane adaptor activity` (a term
  already used for integral-membrane tethers such as SUN1/SUN2 and GPR179).
- **FAM114A1** (`Q8IWE2`, 1 GOA row) — `PMID:35671117`, titled for FAM114A1.
  It explicitly starts from the Y2H hit and validates it: *"we validated the
  interaction between AGTRAP and FAM114A1 in mouse heart lysates and cultured
  PMCFs by IP and Western blotting"*. `KEEP_AS_NON_CORE`.
- **PBX3** (`Q96AL5` / `Q5JS98`, 4 GOA rows) — `PMID:35414770`: *"we performed
  co-IP assays in MDA-MB-453 and T47D cells transfected with Flag-tagged ATRAP,
  which revealed that ATRAP can directly bind with PBX3"*. Corroborated but in a
  breast-cancer over-expression context, and both GOA accessions are unreviewed
  non-canonical clones. `KEEP_AS_NON_CORE`.

The remaining 178 `GO:0005515` rows and the `GO:0042802` self-row get
`MARK_AS_OVER_ANNOTATED` — not `REMOVE`, matching the ADAMTSL5 precedent for
comparable unreplicated Y2H rows (and diverging deliberately from ADAMTSL4's
`REMOVE`; the divergence is flagged rather than silent).

## Finding 5: the gene's defining interaction is absent from human GOA

AGTR1 binding is measured, curated by UniProt on the **human** entry
(`SUBUNIT: Interacts with RACK1, and with the C-terminal region of AGTR1.`,
`ECO:0000269|PubMed:11733189, ECO:0000269|PubMed:12960423`), given a feature
(`FT REGION 110..122 /note="Interaction with AGTR1"`), and present as
`GO:0005515` IPI with `P29754` (mouse Agtr1a) on the **mouse** orthologue — yet
it is nowhere in the human GO record.

`GO:0031702 type 1 angiotensin receptor binding` exists and is exactly right
(Daviet showed the binding is AT1a-specific and excludes AT2). Proposed as `NEW`.

**A claim I had to retract here.** The first draft said its 197 holders were *all*
angiotensinogen orthologues by IEA — read off page 1 of a paginated QuickGO result,
which is exactly the failure the brief warns about. Paging the whole thing (197
annotations over 188 gene products, `len(results)` asserted against `numberOfHits`)
gives 175 IEA, 10 ISO, 9 IPI, 3 IDA, and **16 entities with non-IEA evidence**:

| holder | evidence | what it binds |
|---|---|---|
| AGT | human IPI, mouse IDA, rat ISO | the ligand precursor |
| ARRB2 | rat IPI, mouse ISO | receptor cytoplasmic face |
| JAK2 | rat IPI, mouse ISO/IEA | receptor cytoplasmic face |
| TYK2 | rat IPI, mouse ISO | receptor cytoplasmic face |
| ARAP1 | rat IPI, mouse ISO | receptor cytoplasmic face |
| BDKRB2, EDNRB | human/rat IPI, ISO | heteromeric receptor partners |

So the term is **already** used for cytoplasmic-face binders — AGTRAP's exact class —
which makes the proposal stronger than the retracted version claimed, not weaker. What
is genuinely thin is human coverage: five human entities, only AGT and BDKRB2 by IPI,
the rest Ensembl projections.

Note the composite-claim trap in UniProt's SUBUNIT line: the RACK1 half comes
from `PMID:11733189` and the AGTR1 half from `PMID:12960423`. `PMID:11733189`
reports the human AGTRAP-**RACK1** interaction (Y2H + GST pull-down + co-IP +
SPR) and does **not** itself assay AGTR1. Cited accordingly.

RACK1 (`P63244`) is likewise absent from GOA despite four orthogonal assays on
the human protein. Recorded as a coverage gap, not proposed as a bare
`protein binding` row.

## Finding 6: `GO:0038166` asserts pathway membership where the data show negative regulation

The row is IEA from `InterPro:IPR009436` — the AGTRAP family signature, i.e. a
term derived from the family's *name*. Every functional measurement on this
protein runs the other way: PLC inhibition (`PMID:10358057`), reduced inositol
lipids / c-fos / proliferation (`PMID:12960423`), elevated BP and increased
surface AT1R on knockout (`PMID:20093357`). GO keeps regulation terms outside
the process they regulate, so `MODIFY` -> `GO:0110062 negative regulation of
angiotensin-activated signaling pathway`, which carries the direction the data
actually support.

## Finding 7: a second, AT1R-independent molecular activity

`PMID:27015675` (titled for SERCA2a, not for AGTRAP): pull-down + MALDI-MS,
co-IP and SPR place Atrap on the cardiac Ca2+-ATPase SERCA2a, and *"Atrap
enhanced the SERCA-dependent Ca(2+) uptake in isolated SR membrane vesicles"*;
Atrap-/- myocytes show prolonged Ca2+-transient decay and the mice a reduced
maximum ventricular filling rate. All of it is mouse, so proposed for human as
**ISS**: `GO:0141109 transporter activator activity`, the sibling of
`GO:0141110 transporter inhibitor activity` that phospholamban holds by IDA.
Not in GOA in any form.

## Finding 8: the coverage gap is symmetric, and mouse shows it is fixable

Every finding above looks at AGTRAP's own record. Querying each **partner's** GO
record instead (`scratchpad/reciprocity.py`, paging asserted against
`numberOfHits`) shows the missing curation is not a quirk of this gene's entry —
the targeted papers produced nothing on either side:

| paper | partner | annotations from that paper on the partner |
|---|---|---|
| `PMID:12960423` | human AGTR1 `P30556` | **0** of 79 |
| `PMID:11733189` | human RACK1 `P63244` | **0** of 166 |
| `PMID:21728994` | human PITPNC1 `Q9UKF7` | **0** of 28 |
| `PMID:27015675` | human ATP2A2 `P16615` | **0** of 84 |
| `PMID:35414770` | human PBX3 `P40426` | **0** of 23 |
| `PMID:35671117` | **mouse** Fam114a1 `Q9D281` | **10**, incl. reciprocal `GO:0005515` IPI with `Q9WVK0` |

Five targeted interaction papers, ten opportunities across both partners, zero
human annotations. The single counter-example is the one that matters: MGI
curated `PMID:35671117` **reciprocally** — mouse Fam114a1 IPI with `Q9WVK0` and
mouse Agtrap IPI with `Q9D281` — and also gave Fam114a1 `GO:0038166` by IMP. So
the same paper yields a curated, reciprocal, experimentally-grounded pair in
mouse and nothing at all in human.

Two consequences worth stating. First, this is a **curation** defect rather than
a biology one, which is the distinction AFF4's review drew; the diagnosis for
AGTRAP is "uncharacterised in GO", not "over-annotated", even though 181 rows are
marked over-annotated — those two coexist here because the 188 screen rows and
the missing targeted rows come from different places. Second, human AGTRAP's only
`GO:0038166` row is an InterPro family-name mapping, while mouse *Fam114a1* — its
partner — holds `GO:0038166` by **IMP**. The experimental grounding for
angiotensin-signalling involvement exists in the neighbourhood; it just never
reached this gene.

The three PITPNC1 back-references that do exist on the partner side
(`PMID:16189514`, `PMID:19060904`, `PMID:25416956`, all IntAct `GO:0005515` IPI)
are the same CCSB screens already counted here — reciprocity of the screen, not
of the targeted study.

## Checks run that came back negative (recorded so the next reviewer knows)

- **Retractions / errata / expressions of concern**: all 21 PMIDs relied on were
  checked via `CommentsCorrections/RefType` on each cited article's own PubMed
  record *and* publication types. **None** is retracted, corrected, or under an
  expression of concern; the only hits are three benign `CommentIn` entries
  (25416956, 25910212, 26871637).
- **Paralogue transfer**: `PTHR16521` contains no paralogues — all 5 reviewed
  members are AGTRAP orthologues — so `WRONG_ORTHOLOG_OR_PARALOG` does not apply
  to any row here. Both Compara donors (`Q9WVK0` mouse, `Q642A2` rat) and the
  PAINT seed (`MGI:MGI:1339977`) are true orthologues.
- **Dead/obsolete accessions**: all 132 GOA partner accessions resolved to live
  UniProt entries with a gene name, as did **both** distinct `UniProtKB:`
  WITH/FROM accessions on the 11 non-binding rows — `Q9WVK0` (3 rows) and
  `Q642A2` (1 row). (An earlier draft of this line said "all 4 WITH/FROM protein
  accessions", conflating 4 *rows* with 4 *accessions*; there are 2. The
  `O15507` failure mode from ACTR10 — a dead accession that answers every query
  with a silent zero — is absent here.)
- **IBA landing above its donor** (ACRV1 pattern): mouse Agtrap holds
  `GO:0005886 plasma membrane` by IDA and the human IBA is at the same term, so
  no downward `MODIFY` is warranted.
- **Sibling-review inconsistency**: no paralogue reviews exist to cross-check;
  the nearest precedent is the treatment of CCSB Y2H rows in ADAMTSL5 (followed)
  vs ADAMTSL4 (diverged from, deliberately, and said so).

## affinage recall

`gates_passed: True`, `faith_pct: 100`, 21 citations, all numeric PMIDs, no
bioRxiv-style ids. It supplied the decisive partner-titled papers
(`PMID:21728994`, `PMID:27015675`, `PMID:35414770`) — better recall than this
campaign's 52% average. It **missed** `PMID:35671117` (FAM114A1, the only
orthogonal validation of a HuRI hit) and `PMID:10425188` / `PMID:17033689`, the
two donor references that turned out to carry the review's biggest findings.
Neither of the latter is findable from an AGTRAP-keyed literature search; both
came from querying donor evidence in QuickGO.

## Scripts

Reproducible helpers used for this review live in the session scratchpad, not in
the repo, because they are one-off queries against live services rather than
analyses whose outputs are committed: `partners.py` (resolve every WITH/FROM
partner, assert 199 GOA rows and 0 unresolved accessions), `topology.py`
(compartment classification), `intact2.py` (IntAct evidence/method/publication
tabulation with a `len(results) == totalElements` assertion).
