# ADPRS (ARH3 / ADPRHL2, Q9NX46) — review notes

## Identity: which symbol is current

The worklist, UniProt and GOA do not all use the same name, so this was settled first.

- **HGNC:21304**: approved symbol **`ADPRS`**, name *ADP-ribosylserine hydrolase*.
  `prev_symbol: ["ADPRHL2"]`, `prev_name: ["ADP-ribosylhydrolase like 2"]`,
  `alias_symbol: ["ARH3", "FLJ20446"]`, `date_name_changed: 2019-11-01`.
  `uniprot_ids: ["Q9NX46"]`, MANE `ENST00000373178.5` / `NM_017825.3`, locus 1p34.3.
- **UniProt Q9NX46** = `ADPRS_HUMAN`, reviewed, 363 aa, `GN Name=ADPRS
  {ECO:0000312|HGNC:HGNC:21304}; Synonyms=ADPRHL2, ARH3`.
- **The worklist agrees**: `projects/paint/human-no-IBA-simple.csv` has
  `human,Q9NX46,ADPRS`.

So `ADPRS` is current; `ADPRHL2` is the retired symbol and `ARH3` the protein
nickname used throughout the literature. Most primary papers, and UniProt's own
`DE RecName`, still say ARH3, and the two 2018 disease papers are titled for
*ADPRHL2* — worth knowing when searching.

The worklist file is named `human-no-IBA-simple.csv` and **ADPRS carries six IBA rows**
(`GO:0004649`, `GO:0005634`, `GO:0005739`, `GO:0071451`, `GO:0140290`, `GO:0140292`),
matching UniProt's `DR PAN-GO; Q9NX46; 6 GO annotations based on evolutionary models`.
Another instance of the stale-snapshot problem; the IBA rows turned out to be the
highest-yield rows on the gene.

## Row reconciliation, done before reviewing

```
GOA TSV data lines                57
distinct (term, ev, ref, qual, with/from)  57
fetch-gene stub `- term:` entries 56
```

One collapse, and it is the documented `GOAValidator.seed_missing_annotations` key
omission: the two `GO:0005515` IPI rows from `PMID:32296183` differ only in WITH/FROM
(`UniProtKB:O95271` vs `UniProtKB:Q9NQX1-2`), which is not part of the seeding key. Both
were restored so each partner gets its own verdict. The review has **57** entries and
no `NEW` proposals, so the counts reconcile exactly.

## Verdicts

Counted from the emitted YAML, not by hand: 47 ACCEPT + 7 MODIFY + 3
MARK_AS_OVER_ANNOTATED = 57, and 26 MF + 19 CC + 12 BP = 57.

| aspect | ACCEPT | MODIFY | MARK_AS_OVER_ANNOTATED | total |
|---|---|---|---|---|
| MF | 22 | 2 | 2 | 26 |
| CC | 19 | 0 | 0 | 19 |
| BP | 6 | 5 | 1 | 12 |
| **all** | **47** | **7** | **3** | **57** |

The seven MODIFY rows: `GO:0004553` → `GO:0140292`; `GO:0004649` IMP `PMID:33769608` →
`GO:0140292`; `GO:0071451` ×3 → `GO:0070301`; `GO:0060546` ×2 → `GO:0062099`.
The three MARK_AS_OVER_ANNOTATED rows: `GO:0006287` TAS, and `GO:0005515` ×2.
No REMOVE, and no `NEW` proposals, so `existing_annotations` equals the GOA row count
exactly.

## Finding 1 — the annotated ROS species is the wrong one

`GO:0071451 cellular response to superoxide` sits on ADPRS three times (IMP, IBA, ARBA
IEA). **Every experiment behind it used hydrogen peroxide.**

- Human IMP: [PMID:30401461 "cell viability was reduced upon hydrogen peroxide exposure,
  although it was rescued by expression of wild-type ADPRHL2 mRNA as well as treatment
  with a PARP1 inhibitor"]. Superoxide is not mentioned anywhere in the record.
- The IBA's donor is mouse Adprs (`MGI:MGI:2140364` = `Q8CG72`), whose `GO:0071451` IMP
  cites [PMID:24191052 "PARG and ARH3, acting in tandem, regulate nuclear and cytoplasmic
  PAR degradation following hydrogen peroxide (H2O2) exposure"].

`GO:0071451` and `GO:0070301 cellular response to hydrogen peroxide` are **siblings**
under `GO:0034614 cellular response to reactive oxygen species` — verified by fetching
both ancestor closures; neither contains the other. So this is not a broad parent that
quietly covers the data, it names a different chemical species.

Reach: `PANTHER:PTN008564042` was fully paginated — 132 annotations over 33 gene
products, all ADPRS orthologues, **every one carrying `GO:0071451`**. Fixing the single
mouse MGI row would retract the error from all 33 at once. Filed as a question to MGI
and GO Central.

## Finding 2 — parthanatos annotated as necroptosis

`GO:0060546 negative regulation of necroptotic process` reaches human ADPRS twice (ISS
from `Q8CG72`, plus the Compara IEA mirror of the same mouse row). QuickGO confirms the
mouse row is an IDA from `PMID:30830864`.

`GO:0060546` regulates `GO:0070266`, whose definition requires *"activation of
receptor-interacting serine/threonine-protein kinase 1 and/or 3 (RIPK1/3 …) and …
critical dependence on mixed lineage kinase domain-like (MLKL)"*. What ARH3 restrains
is **parthanatos**, which uses none of those:
[PMID:34479984 "removal of PAR prevents excessive PAR accumulation which can lead to free
PAR formation, release of apoptosis inducing factor (AIF) from mitochondria, and
induction of cell death via the parthanatos pathway"], and
[PMID:24191052 "A protective effect of ARH3 results from its lowering of PAR levels in the
nucleus and the cytoplasm, thereby preventing release of AIF from mitochondria and its
accumulation in the nucleus"].

GO itself records the ambiguity rather than asserting the identity — the comment on
`GO:0097527 necroptotic signaling pathway` says PARP-dependent cell death *"is sometimes
referred to as PARP-dependent cell death or parthanatos; it is still being debated if it
constitutes an independent cell death modality."* That is why the action is a one-step
generalisation to `GO:0062099 negative regulation of programmed necrotic cell death`
(verified to be an ancestor of `GO:0060546`, so nothing new is asserted) rather than a
removal, with a GO term request for `parthanatos` filed alongside.

## Finding 3 — a paper with no poly(ADP-ribose) in it, annotated to PARG activity

`GO:0004649 poly(ADP-ribose) glycohydrolase activity` IMP `PMID:33769608`. Reading the
full text: the paper synthesises **mono**-ADP-ribosylated Ser/Thr/Cys peptides and asks
which hydrolase reverses each linkage. The only ARH3 result is
[PMID:33769608 "We found that ARH3, but not its catalytic mutants D77 N or D78 N, is
capable of hydrolysing the glycosidic linkage in 24 (Ser) and 27 (Thr)"]. No polymer is
used anywhere.

`GO:0004649` is correct for this gene from eleven other rows; this citation does not
substantiate it, and the same experiment substantiates `GO:0140292` exactly. Hence
MODIFY, not REMOVE. This is a deliberate same-term/different-action divergence and the
repo validator warns about it; the divergence is per-reference rather than per-term and
suppressing it would have meant discarding the finding.

Ten other `GO:0004649` rows were checked for the same defect and all are genuine PAR
studies (`PMID:34321462`, `PMID:34019811`, `PMID:34479984`, `PMID:33894202`,
`PMID:22433848`, `PMID:16278211`, `PMID:17075046`, `PMID:30830864`, plus the IBA, the
ARBA IEA and the Reactome TAS). **Reported as a mostly-negative sweep**, so the next
reviewer knows all twelve were looked at rather than one.

## Finding 4 — a mitochondrial reaction inheriting a nucleoplasmic BER term

`GO:0006287 base-excision repair, gap-filling` TAS `Reactome:R-HSA-110373`. Traced end to
end in Reactome's own data:

- ADPRS has exactly one Reactome reaction, `R-HSA-8952903` *ADPRHL2 hydrolyses
  poly(ADP-ribose)*, whose compartment is **mitochondrial matrix** and whose input and
  output species are both `[mitochondrial matrix]`.
- Reactome nests it under `R-HSA-110362` *POLB-Dependent Long Patch Base Excision Repair*
  and then `R-HSA-110373`, both compartment **nucleoplasm**.
- `R-HSA-110373`'s own `goBiologicalProcess` field **is** `GO:0006287` — the export route.

`GO:0006287`'s definition requires an apurinic endonuclease degrading bases and a
polymerase synthesising a patch. ARH3 does neither. Reference-projection test, fully
paginated: `R-HSA-110373` gives `GO:0006287` to exactly five entities — POLB, LIG1, FEN1,
PARG and ADPRS — the first three being the actual gap-filling machinery.

Not REMOVE: ARH3 does participate in the ADP-ribose signalling that accompanies
single-strand-break repair, and `GO:0006281 DNA repair` (IMP, human, `PMID:30045870`)
already carries that at the right granularity.

Contrast the *other* Reactome reference on this gene: `R-HSA-8952903` projects to
**1 entity, 2 annotations** — a gene-specific curated reaction, correctly used for
`GO:0004649` and `GO:0005759`. The same database is both right and wrong on this gene,
and the discriminator is reaction-level versus pathway-level export.

## Finding 5 — a GO branch-placement question, with its own positive control

| term | acceptor atom | under `GO:0016799` N-glycosyl | under `GO:0004553` O-glycosyl |
|---|---|---|---|
| `GO:0003875` ADP-ribosylarginine-[protein] hydrolase | guanidino **N** | yes | no |
| `GO:0140292` ADP-ribosylserine-[protein] hydrolase | serine hydroxyl **O** | yes | no |
| `GO:0140293` ADP-ribosylglutamate-[protein] hydrolase | carboxylate **O** | yes | no |
| `GO:0004649` poly(ADP-ribose) glycohydrolase | ribose 1''–2' **O** | no | yes |

`GO:0003875` — ADPRH's term — is the internal control: arginine's acceptor really is a
nitrogen, so its placement is right. The serine and glutamate terms share that placement
while their acceptor atoms are oxygens, and UniProt/RHEA name the substrates
`O-(ADP-D-ribosyl)-L-seryl-[protein]` (RHEA:58256) and
`5-O-(ADP-D-ribosyl)-L-glutamyl-[protein]`. The literature is explicit:
[PMID:29907568 "ARH3 preferentially hydrolyzes O-linkages attached to the anomeric C1″ of
ADP-ribose"].

Practical consequence on this gene: `GO:0004553` is annotated from `PMID:30045870`, which
measured only serine-linked hydrolysis, and because the two terms sit in disjoint
branches the generalisation a curator would expect does not hold. Raised as a question
for GO rather than curated around; the MODIFY to `GO:0140292` stands on the simpler
ground that it is the activity the paper measured.

Caveat recorded honestly: UniProt also assigns EC 3.2.2.- (an *N*-glycosylase subclass)
to the serine activity, so the convention may be deliberate rather than an error. Hence
a question, not an assertion.

## Finding 6 — both protein-binding rows are one two-hybrid screen

`GO:0005515` ×2, both `IPI PMID:32296183` (HuRI). Expanding IntAct:

| partner | records from PMID:32296183 | methods | MI score |
|---|---|---|---|
| TNKS (`O95271`) | 3 | two hybrid array; two hybrid prey pooling approach; validated two hybrid | 0.56 |
| PRDM5 (`Q9NQX1-2`) | 3 | two hybrid array; two hybrid prey pooling approach; validated two hybrid | 0.56 |

Third recorded instance of *`NbExp=3` is one screen counted three ways* (after ACRV1 and
ADAMTSL5). Both partners resolve to **reviewed canonical** Swiss-Prot entries at full
length (TNKS1_HUMAN 1327 aa; PRDM5_HUMAN 630 aa), so neither is a TrEMBL/ORFeome
substitution — a check reported as negative rather than skipped. Likewise the topology
check is negative: both partners and ADPRS are nuclear/cytoplasmic, so there is no
compartment objection of the ACRV1 kind.

The TNKS hit is superficially attractive — an ADP-ribose eraser meeting a PARP writer —
which is why it was checked rather than accepted. Tankyrase-1's UniProt catalytic
activities install ADP-ribose on **aspartate and glutamate** side chains
(`4-O-(ADP-D-ribosyl)-L-aspartyl-[protein]`, `5-O-(ADP-D-ribosyl)-L-glutamyl-[protein]`),
a linkage class reversed by the macrodomain hydrolases (`GO:0140293`), not by ARH3, whose
measured scope is Ser/Thr/Tyr, PAR and O-acetyl-ADP-ribose. Promiscuity: TNKS has 186
IntAct partners and PRDM5 96, against ADPRS's 35. PubMed returns no study of an
ARH3–tankyrase or ARH3–PRDM5 interaction. `MARK_AS_OVER_ANNOTATED`, not `REMOVE` — the
interactions are unreplicated and uninformative, not demonstrated false.

## Checks that came back negative (recorded so they are not re-run blindly)

- **Logical-opposite citation cross-product.** ADPRS has exactly one regulation term
  (`GO:0060546`, negative) and no positive counterpart, so no opposed pair exists and the
  ADIPOQ-style cross-product cannot fire. Scripted rather than eyeballed.
- **Paralog-specificity leak.** The obvious hypothesis for this family — that ADPRH's
  arginine activity or ADPRHL1's inactivity leaks across — **did not confirm**. No
  `GO:0003875` row on ADPRS; both PANTHER nodes were fully paginated and neither reaches
  `P54922` (ADPRH) or `Q8NDY3` (ADPRHL1). Consistent with what the concurrent ADPRH review
  (PR #2332) found from the other direction.
- **Retractions and errata.** 26 PMIDs scanned via `CommentsCorrections/RefType`. No
  retractions and no expressions of concern. Three errata, all retrieved and read:
  `PMID:30659162` corrects one author's affiliation on `PMID:30045870`; `PMID:30388405`
  and `PMID:34861176` are author-list corrections to `PMID:30100084`. None touches data.
- **Reference-projection on the two TAS references.** `R-HSA-8952903` → 2 annotations /
  1 entity (clean). `R-HSA-110373` → 5 annotations / 5 entities (the finding above).
- **IBA landing above its donor** (the ACRV1 shape). It happens once: mouse Adprs holds
  `GO:0005759 mitochondrial matrix` by EXP while the IBA lands on `GO:0005739
  mitochondrion`. No action taken, because human ADPRS already holds `GO:0005759` by two
  EXP rows of its own, so nothing is lost; recorded as a PAN-GO restricted-term-set
  observation.

## Affinage record

`gates_passed: True`, 18 citations, `faith_pct: 100`. All 18 were resolved against
PubMed and **every one is genuinely about ARH3/ADPRS** — none of the cross-gene
miscitation seen on the sibling ADPRH. Two are preprints and were excluded from anything
load-bearing: `PMID:bio_10.1101_2024.08.28.610034` is a bioRxiv DOI in a PMID-shaped
field (not a PubMed id at all), and `PMID:36945462` is a real PubMed id whose record
type is `Preprint` (bioRxiv, the Arh3 cardiac study).

Recall assessment: the record found the mechanistic literature well, but it **missed the
two papers that decide the review's largest findings** — `PMID:24191052` (the mouse
donor experiment behind both the superoxide and the necroptosis terms) and
`PMID:33769608` (the mis-attributed `GO:0004649` row). Both were found from the GOA
WITH/FROM chain and from UniProt's own reference list, not from the provider. Consistent
with the campaign note that `gates_passed` measures precision, not recall.

No affinage sentence is used as `supporting_text` anywhere in the review; the leads it
supplied (α-NAD+, Tyr-ADPr) were re-grounded on `PMID:31599159` and `PMID:39342999`
directly. The validator therefore warns "No annotations reference available deep research
files", and that warning is left standing deliberately.

## GO gaps proposed

1. **ADP-ribosylthreonine-[protein] hydrolase activity.** Measured
   ([PMID:33769608, above]); UniProt's FUNCTION says "proteins ADP-ribosylated on serine
   and threonine"; no GO term exists between the arginine, serine and glutamate terms.
2. **poly(ADP-ribose) catabolic process.** ADPRS degrades **protein-free** PAR, which
   `GO:0051725 protein de-ADP-ribosylation` cannot cover by its own definition, and free
   PAR is a distinct signalling species (the AIF-releasing death signal). Searched
   QuickGO and OLS for "poly(ADP-ribose) catabolic", "ADP-ribose catabolic" and
   "ADP-ribose metabolic process": absent. Positive control that the searches worked:
   they do return `GO:1990966 ATP generation from poly-ADP-D-ribose`.
3. **parthanatos.** See Finding 2.

Also raised as questions rather than proposed, because each turns on a curation
convention rather than on missing data: whether `GO:0072570 ADP-D-ribose binding` should
be annotated (measured micromolar affinity —
[PMID:17015823 "Recombinant hARH3 binds free ADP-ribose with micromolar affinity and
efficiently de-ADP-ribosylates poly- but not monoADP-ribosylated proteins."] — nine
ADP-ribose co-crystals, and recruitment to lesions depending on it, against the
convention that an enzyme is not annotated to binding its own product); and whether the
α-NAD+ hydrolase activity (RHEA:68792) needs an anomer-specific term, since `GO:0003953
NAD+ nucleosidase activity` is unqualified and the enzymes tested hydrolyse α- but
explicitly not β-NAD+.

## A superseded negative, flagged so it is not re-imported

The 2006 structure paper states that hARH3 *"efficiently de-ADP-ribosylates poly- but not
monoADP-ribosylated proteins"* (`PMID:17015823`). That was overturned in 2017 —
[PMID:28650317 "we identified ARH3/ADPRHL2 as capable of efficiently and specifically
removing Ser-ADPr of histones and other proteins"] — and the two results are compatible
once the substrate is specified: the 2006 assay used **arginine**-linked mono-ADP-ribose,
on which ARH3 genuinely is inactive — UniProt's FUNCTION comment states that it does not
hydrolyse ADP-ribosyl-arginine, -cysteine, -diphthamide or -asparagine bonds, citing
`PubMed:16278211` and `PubMed:33769608` (the sentence spans a `CC` continuation line in
`ADPRS-uniprot.txt`, so it is paraphrased rather than quoted). Reference marked `DISPUTED` with the
reconciliation in `review_notes`, so nobody turns it into a NOT annotation.

## Incidental repository finding

`genes/human/publications/PMID_12345.md` exists on `main` (committed in `21c5e7489`,
"batch9") — a stray, wrong-directory publication cache containing a 1976 paper about
tablet granulation. It is not in `publications/`, so nothing cites it, but any script
that locates the repo root by walking up for a `publications/` directory resolves to
`genes/human/` instead of the repo root. `verify_adprs_claims.py` hit exactly that and
failed loudly rather than reporting zeroes; the fix (anchor on `publications/` **and**
`genes/` together) is committed with a comment explaining why. Not deleted here because
it is outside this gene's scope.

## Computed evidence

`ADPRS-bioinformatics/verify_adprs_claims.py` re-derives every number above from the
public APIs and the local publication cache, writes `results.json`, and renders
`RESULTS.md` from it (`--check` fails if the two disagree). It carries five break-tests,
including one that flips a single boolean to prove the report is sensitive to the
sibling-versus-descendant claim rather than merely to a blanked input. What it explicitly
does **not** mechanise is the reading judgement in Finding 3 — a phrase-presence check
cannot prove the absence of an experiment, and the file says so.

## Round 2 — the reviewer found nine quotes that were verbatim and off-topic

The repo's reference validator checks that a `supporting_text` is a **verbatim substring**
of its cited paper. It does not check that the sentence is *about the row it sits under*.
Nine `supported_by` entries here passed every automated gate while citing something else —
a mitochondrial-matrix sentence under `nucleus`, one sequence-identity sentence reused
under `cytoplasm` and twice under PARG activity, a localisation sentence under an activity
row, and the paper's own **title** under both protein-binding rows. All nine are fixed.

Two of the fixes are not "find a better quote", because for four rows **no better quote
exists in the cached record**:

- `GO:0005634 EXP PMID:17991898` — the cached copy is abstract-only and the abstract is
  entirely mitochondrial. UniProt records `Nucleus {ECO:0000269|PubMed:17991898}` from the
  full text.
- `GO:0005737 EXP PMID:16278211` — abstract-only, and purely biochemical; no localisation
  sentence at all.
- `GO:0140290` / `GO:0140292` `IDA PMID:33186521` — abstract-only, and the one ARH3
  sentence names mono-ADPr without naming the **serine** linkage that both terms assert.
- `GO:0005634 IDA PMID:30045870` — abstract-only; supports recruitment to DNA lesions
  (necessarily nuclear) but never says "nucleus". Note UniProt cites this paper for
  *Chromosome*, not *Nucleus*, which matches what the abstract says.

Those rows now carry a `full_text_unavailable: true` marker plus an explicit statement of
the limitation in `reason`, and the claim is anchored on a paper that does state it. A
recorded absence beats a verbatim quote about something else, which looks checked and is
not.

A fifth case is worth separating: `GO:0005759 EXP PMID:34479984` has **full text
available**, and the word "matrix" occurs **0 times** in it (against 89 for
"mitochondri"). The paper measures the organelle by MitoID imaging and fractionation;
UniProt's *matrix* assignment for this reference must rest on detail the text does not
spell out. Per CLAUDE.md an experimental call is not overruled from incomplete evidence,
so the row stays ACCEPT with the limitation stated, and the matrix claim is anchored on
`PMID:17991898`, which demonstrates PAR-degrading activity *inside* the matrix directly.

### The guard, and its own three defects

`ADPRS-bioinformatics/audit_row_quotes.py` makes the rule executable: every row must have
a quote matching a topic pattern declared **for its GO id** (the stable entity), or a
`full_text_unavailable` marker **and** a stated limitation — both halves, or the escape
hatch becomes a bypass for the defect it guards.

Running it caught three more rows the reviewer had not listed, and **three defects in the
guard itself**:

1. `\bMg\b` did not match **`MgA`/`MgB`** — the exact residues the `GO:0000287` row is
   about. A word-boundary pattern that excludes the specific form of the word it is
   looking for.
2. `Ser-ADPr` did not match **`Ser-linked`**, the Drosophila paper's wording.
3. **A MODIFY row was judged against the term it is moving away from.** On
   `GO:0004649 IMP PMID:33769608` the whole finding is that the quote is *not* about
   poly(ADP-ribose); the guard should test against the **replacement** term. Fixed by
   collecting topics from `proposed_replacement_terms` too — and by failing loudly if a
   replacement term has no declared pattern, rather than skipping it.

Break-test F runs the guard against the YAML at commit `aa019d486` — the version that
actually shipped the defect — and it fires on precisely the `GO:0005634` row. A self-test
proves the guards you thought of fire; running against the shipped defect is the stronger
claim.

### A provider error inherited into `core_functions`

`core_functions` said the O-acetyl-ADP-ribose rate exceeds the poly(ADP-ribose) rate "by
orders of magnitude". `PMID:17075046` says only
[PMID:17075046 "ARH3-catalyzed generation of ADP-ribose from O-acetyl-ADP-ribose was
significantly faster than from poly(ADP-ribose)."] The 250-fold figure in the same
abstract is a **different comparison** —
[PMID:17075046 "The rate of O-acetyl-ADP-ribose hydrolysis by recombinant ARH3 was
250-fold that observed with ARH1; ARH2 and poly(ADP-ribose) glycohydrolase were
inactive."] — ARH3 against **ARH1**, not against PAR.

The affinage record makes exactly that conflation: *"at a rate 250-fold faster than its
hydrolysis of poly(ADP-ribose)"*. So this is a provider error that reached the review
through background knowledge rather than through a quoted sentence — the campaign rule
"never quote an affinage sentence" does not protect against absorbing its arithmetic. Both
sentences are now quoted side by side so the distinction cannot collapse again.

### Two suggestions judged, one taken and one declined

- **`GO:0000287` as a standalone core function — taken.** Removed. Magnesium is a property
  of ADPRS's catalytic centre, not a function anyone would list if asked what the gene
  does; the two Mg quotes and the MgA/MgB role split moved into the serine-hydrolase core
  function's description, where they explain catalysis. The GOA row stays ACCEPT.
- **`GO:0006287` as REMOVE rather than MARK_AS_OVER_ANNOTATED — declined, on a specific
  ground.** The compartment argument shows the *route* is invalid (a mitochondrial-matrix
  reaction cannot inherit a nucleoplasmic pathway's GO term); it does not show the biology
  is false. ADPRS is genuinely recruited to nuclear DNA lesions and erases the ADP-ribose
  marks laid down during single-strand break repair, and PARG — the other non-gap-filling
  recipient of the identical Reactome term — is likewise a real participant. REMOVE would
  need a positive demonstration that ADPRS is absent from base-excision repair, and none
  exists.
