# AHNAK (Q09666) — review notes

Working journal for the GO annotation review. Provenance is given inline as
`[PMID:xxxx "verbatim text"]` or as the query that produced a number.

## What AHNAK is

5,890 aa, ~629 kDa by UniProt's own calculation (the literature says "700 kDa", which is the
apparent mass on a gel). Architecture from the UniProt feature table:

- `FT DOMAIN 9..90 /note="PDZ" /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"` — predicted, not
  experimentally solved, but see the holdup finding below, which is functional evidence that it
  really is a PDZ.
- **No `FT REPEAT` features at all**, despite `KW Repeat`. The tandem 128-residue central repeat
  units that the entire literature describes are not modelled in the entry. The published counts
  differ — [PMID:14699089 "a large central region of 4,390 amino acids composed of the 128-aa unit
  repeated 26 times"] for the 5,643-aa sequence, against [PMID:10318799 "about 30 repeated motifs
  each 128 amino acids in length"] — so this review says "26 to 30" rather than picking one. The
  22 `FT REGION` features are all MobiDB-lite "Disordered".
- Five predicted NLS motifs, all in the C-terminal region (4971-4979, 5019-5027, 5034-5039,
  5706-5716, 5772-5779).
- 13 VARIANTs, all dbSNP; the I5236T variant that PMID:16319140 characterises functionally is
  **not** among them.
- `CC -!- FUNCTION: May be required for neuronal cell differentiation.` — one hedged sentence
  for a protein with a thirty-year literature. Raised as a UniProt suggestion.
- `CC -!- SUBCELLULAR LOCATION: Nucleus.` — also a single word, against four plasma-membrane
  IDAs on the same protein.
- Isoform 2 (Q09666-2) = residues 1-149 with 115-149 replaced by a 22-residue alternative, i.e.
  ~136 aa = the PDZ domain alone. This is almost certainly the "small 17 kDa AHNAK" of
  PMID:21940993. Corroborating: mouse has TrEMBL entries `Q8CEX7` and `A0A494B8Y7` (176 aa),
  both named "PDZ domain-containing protein" / "AHNAK nucleoprotein".

## Row reconciliation (done first, per campaign procedure)

```
wc -l AHNAK-goa.tsv        -> 67 (66 data rows)
grep -c '^- term:' stub    -> 66
```
**66 : 66, exact.** The `fetch-gene` under-seeding defect seen on ADAMTSL5 and ACTR5 (collapsed
`GO:0005515` partner rows) is **absent here** — all 26 protein-binding rows were seeded
individually. Verified programmatically by matching on
`(term, evidence, reference, sorted(WITH/FROM), negated)` with an assertion that every TSV row
is consumed exactly once and no review key goes unused. Final file = 66 GOA rows + 8 NEW.

## WITH/FROM resolution (every token)

| token | resolves to | status |
|---|---|---|
| `PANTHER:PTN001156025` | tree node, 74 gene products; human reach = AHNAK, AHNAK2, PRX | node, not a protein |
| `MGI:MGI:108176` | mouse **Prx** / Periaxin, O55103, Swiss-Prot, 1391 aa | **paralogue** |
| `MGI:MGI:1316648` | mouse **Ahnak**, E9Q616, **TrEMBL**, 5656 aa | ortholog, unreviewed |
| `MGI:MGI:2144831` | mouse **Ahnak2**, A0A7N9VR94 (+2 shorter TrEMBL hits) | paralogue |
| `RGD:619960` | rat **Prx**, Q63425, Swiss-Prot, 1383 aa | paralogue |
| `UniProtKB:Q9BXM0` | human **PRX**, Swiss-Prot, 1461 aa | paralogue |
| `UniProtKB:Q8IVF2` | human **AHNAK2**, Swiss-Prot, 5795 aa | paralogue |
| `UniProtKB:Q09666` | AHNAK itself | self-referential |
| `UniProtKB:E9Q616` / `ensembl:ENSMUSP00000090633` | the **same** mouse protein twice | one donor, not two |
| `UniProtKB-SubCell:SL-0191` | vocabulary term "Nucleus" | not evidence |
| `ARBA:ARBA00026971`, `ARBA:ARBA00027801` | ARBA rules | not gene products |

Zero unresolved tokens. Note there is **no Swiss-Prot mouse Ahnak** — every Compara and CAFA row
on this gene descends from an unreviewed TrEMBL entry. Its GO annotations are curated
experimental ones; its protein *name* is automatic. Those are two different things (the
evidence-provenance vs name-provenance distinction).

## Finding 1 — the membrane-repair annotation is a complex projection over a negative result

`GO:1905686 positive regulation of plasma membrane repair`, NAS, `PMID:22940583`, ComplexPortal.

The cited paper is a crystallography paper. Its only AHNAK content is a 3.5 Å structure of a
C-terminal peptide on the S100A10/annexin A2 heterotetramer; membrane repair appears only in the
framing sentence
[PMID:22940583 "Here, we present the three-dimensional structure of a multiprotein complex that
includes S100A10, annexin A2, and AHNAK, which along with dysferlin, functions in muscle and
cardiac tissue repair."]. NAS is the correct code for that.

Projection test (QuickGO by *reference*, not by gene):

```
reference=PMID:22940583 -> 16 annotations, 10 distinct entities, complete=True
  GO:1905686 NAS -> 10 entities   (CPX-850, CPX-853, CPX-898, CPX-905,
                                   ANXA2+S100A10+AHNAK human, ANXA2+S100A10 mouse, Ahnak mouse)
  GO:0045921 NAS ->  6 entities
```
All `assignedBy: ComplexPortal`, identical evidence code. This is the ACTR8 shape: the *phenotype
term spreads across the whole set*. The ACTRT3 discriminator (does the functional term stay on the
gene that was actually perturbed?) cannot even apply, because nothing was perturbed — it is a
structure paper.

**And the only experiment that ever tested it is negative:**
[PMID:20833135 "A laser wounding assay with AHNAK1-deficient fibers suggests that AHNAK1 is not
involved in membrane repair."]

Verdict: `MARK_AS_OVER_ANNOTATED`, not `REMOVE`. The negative is one assay, in mouse skeletal
muscle, hedged by its own authors, and AHNAK's partners (dysferlin, ANXA2, S100A10) genuinely are
repair proteins. But a *positive-regulation* assertion with no supporting experiment anywhere and a
loss-of-function negative in the obvious assay does not deserve to stand unqualified.

## Finding 2 — a plasma-membrane IDA on a paper that predates the gene

`GO:0005886`, IDA, `PMID:3126079`, ComplexPortal. That paper is Osborn et al. 1988 on p11 and p36
[PMID:3126079 "p36, a major cytoplasmic substrate of pp60 src kinase, is present beneath the plasma
membrane."] — i.e. S100A10 and annexin A2, with **no AHNAK experiment**, and it could not have one:
the AHNAK gene was first reported in **1992** [PMID:1608957 "A human gene (AHNAK) encoding an
unusually large protein"].

```
reference=PMID:3126079 -> 14 annotations, 10 entities
  GO:0005886 IDA -> 8 entities incl. UniProtKB:Q09666 AHNAK, assignedBy ComplexPortal
```

The **term** is right — plasma membrane is held on this gene by an HPA IDA and two literature IDAs
— so this is a *reference* defect, not a term defect. Action `ACCEPT` with the provenance recorded
and `reference_review.correctness: MISCITED`; raised for ComplexPortal as "can projections be
restricted to references postdating the subunit's identification?".

## Finding 3 — one holdup screen supplies 8 of the 26 protein-binding rows

IntAct expansion of `Q09666`: **649 interaction records, 608 distinct partners**. Of those,
**415 records come from `PMID:36115835` alone**, every one with `detectionMethod: holdup assay`,
AHNAK always the *prey*, partners always the *bait*. The paper describes the design
[PMID:36115835 "we expressed a recombinant PDZome library covering all the 266 known human PDZs"]
against a library of 448 C-terminal 10-mer PDZ-binding motifs, measured by
[PMID:36115835 "we used the holdup method, a high-throughput comparative chromatographic retention
assay that we developed previously"].

So those 8 GO rows report an affinity between AHNAK's isolated ~80-residue PDZ domain and a
10-residue peptide. This is the ACRV1 `NbExp=3` pattern at a larger scale: **one experiment
becoming eight annotations**.

Judged **per partner**, not wholesale:

| partner | orthogonal record? | action |
|---|---|---|
| CFTR | co-IP (26618866) + BioID (36012204) | KEEP_AS_NON_CORE |
| HSPA5 | co-IP (26496610) | KEEP_AS_NON_CORE |
| U2AF2 | BioID (39251607) | KEEP_AS_NON_CORE |
| MCM7 | co-IP (23764002) | KEEP_AS_NON_CORE |
| ITK | crosslink-MS (30021884) | KEEP_AS_NON_CORE |
| CTBP1 | co-IP (31041561) | KEEP_AS_NON_CORE |
| COMMD3 | pulldown (30833792) | KEEP_AS_NON_CORE |
| **RPS6KA1** | **none anywhere in IntAct**; MI-score 0.44, lowest of the eight | **MARK_AS_OVER_ANNOTATED** |

The flip side is a genuine positive: the screen is functional evidence that AHNAK's
`ECO:0000255`-predicted PDZ domain really folds and binds PDZ ligands.

**Negative results from the sibling checks, reported because they were run:**
- *Partner-accession check* (the ACRV1 TSC1/ORFeome trap): all **15** distinct `GO:0005515`
  partner accessions resolve to **reviewed canonical Swiss-Prot entries at full length** — the HCV
  row correctly uses the mature-chain id `P27958-PRO_0000037576` rather than a truncated clone. No
  ORFeome-fragment substitutions. The fragment on these rows is on AHNAK's side, not the partner's.
  (This claim is about *partner* accessions only. Several **WITH/FROM donor** accessions are
  **TrEMBL**, not Swiss-Prot — mouse Ahnak `E9Q616` and all three mouse Ahnak2 entries — as the
  table above records. Conflating the two sets would have made a false 19-of-19 claim.)
- *Topological-impossibility check*: mostly negative. HSPA5/BiP is ER-lumenal against a
  cytosol-facing AHNAK, which is worth noting, but the other partners are all cytosol- or
  nucleus-accessible, so the ACRV1-style "every partner is on the wrong side of a membrane"
  argument does not apply here.

## Finding 4 — GO:0043484 is one experiment reaching 74 proteins by three routes

Donor-evidence query for `GO:0043484` across the family:

| gene product | evidence |
|---|---|
| mouse Ahnak `E9Q616` | **IDA `PMID:21940993`** + IBA |
| mouse Prx `O55103` | IBA only |
| rat Prx `Q63425` | IBA + ISO only |
| human PRX `Q9BXM0` | IBA only |
| human AHNAK2 `Q8IVF2` | IBA only |

So the **only experimental annotation to this term anywhere in the family** is the single mouse
IDA. PAINT node `PTN001156025` then gives it to **74 gene products**, and human AHNAK receives it
**three times** — IBA, Ensembl Compara IEA, and CAFA ISS — from that one experiment.

Two mitigations that make the PAINT call more defensible than it first looks:
1. The paper tests **both** family members: [PMID:21940993 "A small 17-kDa isoform of Periaxin
   similarly traffics between the cytoplasm and the nucleus to regulate mRNA splicing."] So the
   node has two members behind it, not one. (Corollary: Periaxin's experimental result was never
   captured as an experimental annotation — human/mouse/rat PRX all hold the term by IBA/ISO only.
   Raised for PAINT.)
2. The node's placement is clean — `PTN001156025` gives exactly `GO:0005634`, `GO:0005737`,
   `GO:0043484` to exactly the same 74 entities, and all three human members get exactly the same
   three terms. **No AADACL-style node-misplacement defect here**; reported as a negative.

What *is* wrong is the level: the activity belongs to the **short nuclear isoform** (Q09666-2), not
to the 700 kDa protein the canonical accession represents. All three rows → `KEEP_AS_NON_CORE`.

## Finding 5 — the CAFA ISS block cites one paper for five different terms

Five ISS rows (`GO:0005634`, `GO:0005829`, `GO:0043034`, `GO:0043484`, `GO:0097493`), all citing
`PMID:21940993`, all donor `UniProtKB:E9Q616`. But the donor's own evidence for two of them is in
a **different paper**:

```
E9Q616 -> GO:0043034 : IDA PMID:20833135     (costamere / vinculin colocalisation)
E9Q616 -> GO:0097493 : IMP PMID:20833135     (AFM fibre stiffness)
E9Q616 -> GO:0005829 : IDA PMID:21940993     (agrees with the row)
E9Q616 -> GO:0043484 : IDA PMID:21940993     (agrees with the row)
```

`PMID:21940993` is about alternative splicing at the AHNAK locus and contains neither the costamere
nor the stiffness experiment. Block-assigned ISS rows carrying one reference for the whole block is
the mechanism. Raised for UniProt/CAFA.

## Finding 6 — an MF term inferred from whole-fibre mechanics

`GO:0097493 structural molecule activity conferring elasticity` — definition: *"The action of a
molecule that contributes to the structural integrity of a complex or assembly within or outside a
cell, providing elasticity and recoiling."*

Its entire evidence is one mouse IMP: [PMID:20833135 "Using atomic force microscopy (AFM), we
observed a significantly higher transverse stiffness of AHNAK1⁻/⁻ fibers."]

Care with direction — I initially wanted to call this an inversion and it is **not**: losing AHNAK
making fibres stiffer is *consistent* with AHNAK providing compliance. The objection is about
**level**, not sign: a whole-fibre knockout phenotype is being read as a molecular property of the
protein. No force spectroscopy, extensibility measurement or reconstitution on AHNAK or its repeats
has ever been published. Both rows → `MARK_AS_OVER_ANNOTATED`; the experiment that would settle it
is in `suggested_experiments`.

## Finding 7 — the T-tubule contradiction that dissolved on checking

Initial read: `GO:0030315 T-tubule` NAS from `PMID:17185750` ["In normal skeletal muscle, dysferlin
and AHNAK colocalize at the sarcolemmal membrane and T-tubules."] is flatly contradicted by
[PMID:20833135 "In contrast, no AHNAK expression was detected in the T-tubule system."], and the
later paper used AHNAK1- and AHNAK2-specific antibodies while the earlier did not — a textbook
paralogue cross-reactivity artefact.

**Then I checked a third paper and the story changed.** [PMID:12153988 "Confocal microscopy of
human left ventricular tissue localized the carboxyl-terminal ahnak portion to the sarcolemma
including the T-tubular system and the intercalated disks of cardiomyocytes."] The disagreement is
confined to *skeletal* muscle; in *human cardiac* muscle the localisation is independently
supported. So it is a tissue difference, not a contradiction, and the honest action is `ACCEPT`
with both observations recorded — not the `MARK_AS_OVER_ANNOTATED` I was heading for.

Logged as a reminder: the campaign's over-annotation bias nearly produced a confident wrong answer
here, exactly as the AADACL4 "a general term can be correct" note warns.

## The real diagnosis: this is a coverage defect, not an over-annotation defect

Aspect breakdown of the 66 GOA rows:

- **CC: 31 rows, 16 distinct terms.** Plasma membrane ×5, nucleus ×4, exosome ×3, cytosol ×3,
  cytoplasm ×3, costamere ×2, sarcolemma ×2, plus plasma membrane protein complex, membrane raft,
  cell-cell contact zone, vesicle, T-tubule, membrane, actin cytoskeleton, focal adhesion,
  lysosomal membrane.
- **MF: 31 rows, 5 distinct terms** — and **26 of the 31 are bare `GO:0005515`** (21 assigned by
  IntAct, 4 by UniProt, 1 by AgBase). The other four terms are `GO:0044548` ×1, `GO:0045296` ×1,
  `GO:0003723` ×1 and `GO:0097493` ×2, the last of which this review marks over-annotated.
- **BP: 4 rows, 2 distinct terms** — `GO:0043484` ×3 (all three routes out of one experiment) and
  the unsupported `GO:1905686` ×1.

  (Counted with `awk -F'\t' 'NR>1 {print $7}' AHNAK-goa.tsv | sort | uniq -c`. My first pass
  hand-counted these off a printed row list and got 39/23/4 with 17/4/2 distinct — wrong in five
  places. Derive the number, do not eyeball it.)

So a protein with hundreds of papers has **effectively zero curated biological process** and **no
informative molecular function at all**. The things AHNAK is actually known for are absent:

| what is known | where it is measured | in GOA? |
|---|---|---|
| binds Cavβ2, Kd 55-60 nM, PxxP motif | 12153988, 20607281, 22497893 | **no** |
| brake on I(CaL), relieved by PKA | 16319140, 14722071 | **no** |
| required for L-type surface expression | 18191595, 19497879, 30760886, 19261907 | **no** |
| binds G-actin, cosediments with F-actin | 12153988 | **no** |
| bundles actin filaments | 15001564 | **no** |
| binds/activates PKC-α, breaks PKC-PP2A | 18174170, 15033986 | **no** |
| binds/activates PLC-γ1 | 10318799 | **no** |
| restrains 53BP1 oligomerisation (human KO) | 33961796 | **no** |
| cortical actin organisation (siRNA) | 14699089 | **no** |
| stimulates LIG4-XRCC4 double-stranded ligation (purified proteins) | 15177040 | **no** |

The last row was nearly missed. `PMID:15177040` entered this review only as the source of the
"weak DNA-binding activity" caveat on the `GO:0003723` row — cited, but supporting no annotation.
Re-reading it for that caveat surfaced the actual result: [PMID:15177040 "We characterised AHNAK as
a protein that stimulates the double-stranded (DS) ligation activity of DNA ligase IV-XRCC4."],
with purified proteins and an in-cell co-IP. A cited reference that supports no annotation is a
flag, in the same way the brief flags an empty `findings:` list on a full-text reference.

Term choice was constrained: `GO:0051106 positive regulation of DNA ligation` is **obsolete**
(checked at QuickGO, not inferred from an empty search), and `involved_in GO:0006303` would
over-reach because no cellular repair assay exists. `GO:0008047 enzyme activator activity` —
*"A molecular function regulator that increases a catalytic activity"* — is what was measured.

Hence 9 `NEW` rows. The two `MODIFY`s move bare `GO:0005515` S100A10 rows to `GO:0044548`, which the
gene already carries — the only partner on this protein with crystal structures behind it.

`GO:0005515` on DYSF/myoferlin was left as-is deliberately: it is the strongest IPI on the gene
(direct, Ca-independent, domain-mapped both ways) but GO has **no term for binding a ferlin**, and
`GO:0019904 protein domain specific binding` would be true and no more informative. Filed as an
ontology question rather than forced.

## Reference hygiene

- **Retraction/erratum sweep** over all 58 PMIDs touched, reading `CommentsCorrections/RefType`
  from each cited article's own PubMed record (a Publisher Correction is invisible to a
  publication-type search): **0 retractions**, **5 errata** — `36115835`→`36477203`,
  `39251607`→`39468017`, `26466345`→`26629899`, and `1608957` and `15489334` with errata carrying
  no PMID. All are Author Corrections; none has an abstract, so scope could not be established.
  Recorded in the relevant `reference_review` blocks. Nothing load-bearing rests on them.
- **affinage**: gates clear, 45 numeric-PMID citations, no `PMID:bio_*` preprint ids. Spot checks
  found it accurate except that it describes `PMID:26466345` as BMP2-driven where the paper reports
  BMP4/SMAD1. **It supplied `PMID:20833135`, this review's decisive reference, which appears
  nowhere in AHNAK's GOA reference set** — a recall win worth recording. Per campaign policy no
  affinage sentence is quoted as `supporting_text`; every claim it contributed was re-grounded on
  the primary paper. This is why `just validate` reports the "no annotations reference available
  deep research files" warning, which is left standing deliberately.
- All 87 `supporting_text` entries verified (85 literature via the repo's own
  `SupportingTextValidator`, 2 `file:` quotes by literal substring, since CI does **not** check
  `file:` quotes). Checker self-tested by breaking it three ways: a mutated literature quote, a
  fabricated `file:` quote, and a `file:` quote spanning a UniProt `CC` continuation line — all
  three fired.

## A number that refused to add up

First dump: `raw supporting_text keys=68` against `parsed quote entries=87`. Resisting the urge to
find a story, the gap traced to **PyYAML anchors and aliases** — shared Python dicts became
`&id001`/`*id001`. Accounting: 14 aliased entries from the two shared holdup quote dicts (8 uses),
2 from the shared splicing quote dicts, 2 from the shared splicing *list*, 1 from the shared
elasticity list = **exactly 19 = 87 − 68**. `copy.deepcopy` does **not** fix this (it preserves
internal sharing by design); a dumper with `ignore_aliases` does. The builder now asserts no
anchor survives and that raw == parsed.

## What I did not do

- No bioinformatics analysis. The claims in this review rest on published measurements and on
  database queries (QuickGO, IntAct, UniProt REST) whose commands are recorded above; nothing here
  needed a new alignment or structure calculation.
- Did not read the full text of `PMID:21423176`, `PMID:25468996` or `PMID:36115835` beyond the
  parts quoted; AHNAK appears in the first two only in supplementary tables. Those rows are
  `KEEP_AS_NON_CORE` accordingly.
