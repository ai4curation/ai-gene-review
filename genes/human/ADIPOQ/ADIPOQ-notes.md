# ADIPOQ (adiponectin, Q15848) — review notes

Working journal for the GO annotation review. Computed evidence lives in
`ADIPOQ-bioinformatics/` (`analyze_adipoq.py` → `results.json` → `RESULTS.md`);
the review YAML is emitted by `ADIPOQ-bioinformatics/build_review.py`, which is
the source of truth for it — do not hand-edit the YAML.

## Identity, verified rather than assumed

`projects/paint/human-no-IBA-simple.csv` line 2500 reads `human,Q15848,ADIPOQ`.
UniProt confirms `Q15848` = `ADIPO_HUMAN`, *Homo sapiens* (NCBITaxon:9606), 244
aa, Swiss-Prot reviewed, `PE 1: Evidence at protein level`.

**The worklist's "no-IBA" name is wrong for this gene.** ADIPOQ has **four** IBA
rows in GOA (`GO:0005179`, `GO:0005576`, `GO:0010642`, `GO:0045599`). Curiously,
UniProt's own cross-reference line says the opposite — `DR PAN-GO; Q15848; 0 GO
annotations based on evolutionary models.` — so PAN-GO and GO_Central disagree
about this gene. Worth knowing before trusting either.

## What kind of gene this is, and what that predicts

Unlike most of this campaign, ADIPOQ is heavily studied: 161 GOA rows, 76 of
them molecular function, across 33 references. The predicted dominant defect was
therefore over-annotation from pleiotropy rather than absence. That prediction
was **partly** right and partly wrong, and the ways it was wrong are the more
interesting findings.

- **Right:** 62 of 64 `GO:0005515` rows are one two-hybrid screen; a large block
  of BP rows is downstream physiology of receptor signalling.
- **Wrong:** the biggest single defects are not pleiotropy at all. They are (a)
  an IDA that inverts a paper's finding, (b) a 2×2 citation cross-product
  supporting a proposition and its negation, and (c) two bulk imports. None of
  these is "too many true things"; each is a false thing.
- **Also wrong:** the record has real *gaps*. Two of adiponectin's three
  characterised receptors are absent from GO entirely.

## Row reconciliation, done first

```
GOA TSV data rows                161   (161 distinct; no duplicate lines)
fetch-gene stub entries          103
collapsed                         58
```

The stub under-seeds by 58, all of it the known `WITH/FROM`-blind seeder key.
Every partner and every assigner now has its own entry. 161 GOA rows + 1 `NEW`
proposal = **162** entries, asserted in `build_review.py`.

## Finding 1 — `GO:0033691 sialic acid binding` inverts its own reference

The sharpest error in the record, and the one I would have missed by reading
the label instead of the source.

`GO:0033691` is defined as *"Binding to a sialic acid"*. Its sole support is
`PMID:19855092`, whose title is *"Sialic acid modification of adiponectin is not
required for multimerization or secretion but determines half-life in
circulation"*. The paper is a PTM study: it maps sialylated O-linked glycans
onto adiponectin's **own** threonines and shows that stripping them accelerates
plasma clearance [PMID:19855092 *"sialylation occurs on previously unidentified
O-linked glycans on Thr residues of the variable domain in human adiponectin"*].
Adiponectin is the glycoprotein carrying the sugar, not the lectin reading it.
The only receptor the paper implicates is the hepatic **asialo**glycoprotein
receptor, which binds *desialylated* adiponectin — the traffic runs the other
way [PMID:19855092 *"plasma clearance of desialylated adiponectin was
accelerated compared with that of control adiponectin"*].

Three corroborations:

1. **UniProt encodes the same reference correctly** — as `CARBOHYD` features at
   Thr-21 and Thr-22 and a PTM comment, not as a binding activity.
2. **Architecture.** Adiponectin's only two modules are a collagen-like repeat
   (42–107) and a C1q jelly-roll (108–244). There is no lectin domain.
3. **It is the only annotation this reference carries in all of GOA** (QuickGO
   `?reference=PMID:19855092` → `numberOfHits: 1`), so it is a single curation
   slip rather than an import.

**It has already propagated.** Mouse Adipoq (`Q60994`) holds `GO:0033691` only
by `IEA GO_REF:0000107` and `ISO GO_REF:0000119` — both orthology transfers from
this human row. The human IDA is the sole origin in either species, so
retracting it retracts the error everywhere. → `REMOVE`.

## Finding 2 — the cold-thermogenesis 2×2 cross-product, and it starts at MGI

`GO:0120162` (**positive**) and `GO:0120163` (**negative**) regulation of
cold-induced thermogenesis are logical opposites. GOA cites **both terms to both
of the same two references**:

| | PMID:24531262 | PMID:26166748 |
|---|---|---|
| `GO:0120162` positive | ISS | ISS |
| `GO:0120163` negative | ISS | ISS |

The detector in `analyze_adipoq.py` reports `is_full_cross_product: true` from
the TSV alone — this is a defect *independent of what the papers say*, because
the same evidence cannot support a proposition and its negation.

Reading the two settles which is which, and each paper is unambiguous:

- **PMID:24531262** (Diabetologia 2014) — *"This study demonstrates that
  adiponectin suppresses thermogenesis"*; knockouts run hotter [PMID:24531262
  *"The CBTs of adiponectin knockout mice (Adipoq(-/-)) were significantly
  higher than those of wild type (WT) mice"*]. **Negative only.**
- **PMID:26166748** (Cell Metab 2015) — [PMID:26166748 *"Chronic cold
  exposure-induced accumulation of M2 macrophages, activation of beige cells,
  and thermogenic program were markedly impaired in scWAT of adiponectin
  knockout (ADN KO) mice"*]. **Positive only.**

**The defect is upstream, not in the human ISS.** Querying mouse `Q60994`
(fully paginated, 190 annotations) shows `GO:0120162` **IMP** from *both*
references and `GO:0120163` **IMP** from *both* — MGI made the cross-product
from the primary experiments, and the four human rows are ISS/IEA reflections of
it. So the fix belongs at MGI: four IMP rows should be two. Filed as a
suggested question naming both species.

Note what this is **not**: the underlying biological disagreement between the
two labs is genuine and unresolved (different alleles, different cold protocols,
BAT vs subcutaneous beiging). Both `reference_review`s are marked `DISPUTED`.
The annotation defect can be fixed without adjudicating the science, and I have
not tried to adjudicate it.

## Finding 3 — the `GO:0005515` block is one Y2H screen wearing five hats

64 `GO:0005515` rows, 61 distinct partners. IntAct for Q15848:

```
286 interactions, 7 publications
171 from PMID:32296183 (HuRI) alone
196 two-hybrid, logged as FIVE sub-methods:
    two hybrid array (66) · validated two hybrid (65)
    two hybrid prey pooling approach (57) · two hybrid pooling (4)
    two hybrid bait and prey pooling approach (4)
240 of 264 partners appear in exactly one publication
0 orthogonal biophysical assays (no SPR, no ITC, no endogenous co-IP)
```

The five sub-method names are why UniProt shows `NbExp=3` on nearly every
partner — the third instance of this pattern in the campaign (after ACRV1 and
ADAMTSL5), and here it is `NbExp=3` from *one* experiment logged three ways.

The topological objection is about the **assay**, not primarily the partners:
adiponectin has a cleaved signal peptide (`SIGNAL 1..18`) and a secreted mature
chain, while two-hybrid requires both partners in the yeast nucleus — a
compartment the native protein never enters, and where its disulfide-linked
hexamers, hydroxylysines and glycans cannot form either. As a secondary
observation, six partners (SGTA, COQ9, HTT, FASN, MRM1, TRIM35) are annotated
*only* to cytosol/nucleus/mitochondrion.

**Negative results from this check, recorded because they were run:** all 61
partners resolve to **reviewed Swiss-Prot** entries at canonical length — no
TrEMBL clones and no partial ORFeome constructs of the ACRV1 kind. Thirteen are
cited as isoform accessions, which is normal for ORFeome screens and not a
defect. The `"reviewed" in entryType` substring bug is guarded against by
`startswith("UniProtKB reviewed")` plus an assertion that the test discriminates.

SGTA (`O43765`) is the only partner in three publications — but all three
(PMID:25910212, PMID:31515488, PMID:32296183) are two-hybrid interactome
datasets from one methodological lineage, so it is the same assay run again, not
replication. SGTA is a cytosolic co-chaperone for mislocalised tail-anchored
proteins, a known promiscuity source.

→ 62 rows `MARK_AS_OVER_ANNOTATED` (unmeasured, not refuted). The two exceptions
are judged per partner, as they should be:

- **`P01127` PDGFB / PMID:12070119** → `MODIFY` to `GO:0019838 growth factor
  binding`. This is a hypothesis-led human experiment with a measured, selective
  binding [PMID:12070119 *"Adiponectin specifically bound to (125)I-PDGF-BB and
  significantly inhibited the association of (125)I-PDGF-BB with HASMCs"*] and
  an explicit negative control against PDGF-AA and HB-EGF.
- **`Q96A54` ADIPOR1 / PMID:16622416** → `MODIFY` to `GO:0005102 signaling
  receptor binding`. The reciprocal row exists on ADIPOR1. Caveat recorded: this
  paper is primarily about APPL1 and what it shows is that ligand *stimulates*
  the APPL1–AdipoR1 association, not a direct adiponectin–AdipoR1 binding
  measurement; the direct evidence is PMID:12802337.

## Finding 4 — two bulk imports, and one non-confirmation

Reference-projection test, fully paginated:

| reference | entities | our term | verdict |
|---|---|---|---|
| PMID:36399478 MatrisomeDB 2.0 | **272** on `GO:0140149` | `GO:0140149` | import → `MARK_AS_OVER_ANNOTATED` |
| PMID:28675934 ECM proteomics | **41** on `GO:0005201` (RCA) | `GO:0005201` | import → `REMOVE` |
| PMID:10095105 gene structure | **1** | `GO:0006091` | **not** an import |

`GO:0005201 extracellular matrix structural constituent` is the campaign's
fold-to-activity error arriving by a route the brief predicted: not the retired
SPKW keyword path but a **bulk RCA block**. The trigger is almost certainly the
collagen-like domain — but UniProt's SUBUNIT is explicit that those repeats
build adiponectin's *own* triple-helical trimer, not a matrix. Adiponectin does
adsorb to matrix; that is *binding*, not *constituting*, and no GO row currently
makes the binding claim.

**PMID:10095105 is a genuine non-confirmation of the projection hypothesis** and
is recorded as one. It carries exactly one annotation in all of GOA, so it is
not an import — it is a single unsupported TAS from a paper (*"Organization of
the gene for gelatin-binding protein (GBP28)"*, FISH mapping to 3q27, three
exons, no TATA box) that performs no metabolic experiment. Removed on content,
not on provenance.

## Finding 5 — role conflation: the hormone annotated to the process it regulates

A coherent class, and the largest single group of `MODIFY`s:

| row | replacement |
|---|---|
| `GO:0006006` glucose metabolic process ×2 | `GO:0010906` regulation of glucose metabolic process |
| `GO:0006635` fatty acid beta-oxidation ×2 | `GO:0046321` positive regulation of fatty acid oxidation |
| `GO:0019395` fatty acid oxidation | `GO:0046321` |
| `GO:0050873` brown fat cell differentiation | `GO:0090336` positive regulation of brown fat cell differentiation |
| `GO:0009967` positive regulation of signal transduction | `GO:0033211` adiponectin-activated signaling pathway |

Adiponectin has no catalytic activity; it changes the rate at which responding
cells oxidise fat and consume glucose, via AdipoR1/R2 and AMPK [PMID:12368907
*"stimulation of glucose utilization and fatty-acid oxidation by Ad occurs
through activation of AMPK"*]. The regulation-grade terms already exist and
ADIPOQ already carries several of them, so these are grain corrections with no
loss of content. The same conflation exists upstream — mouse Adipoq holds
`GO:0006006` by IDA/IMP and `GO:0019395` by IDA — so it is a shared MGI/UniProt
pattern rather than a one-off.

The mirror of the same shape is `GO:0071466 cellular response to xenobiotic
stimulus`, which runs the *other* way: the mouse IDA behind it is
`PMID:19109165`, *"The peroxisome proliferator-activated receptor gamma agonist
rosiglitazone ameliorates murine lupus by induction of adiponectin"* — the datum
is that a drug **induces adiponectin**, making adiponectin the output of the
response, not machinery within it. → `MARK_AS_OVER_ANNOTATED`, both rows.

## Finding 6 — coverage gaps on the receptor side

Measured, not asserted (`receptor_coverage` in `results.json`):

| receptor | on ADIPOQ's GOA | annotations naming Q15848 |
|---|---|---|
| ADIPOR1 `Q96A54` | yes | 1 (`GO:0005515` IPI PMID:16622416) |
| **ADIPOR2 `Q86V24`** | **no** | **0** of 21 |
| **T-cadherin CDH13 `P55290`** | **no** | **0** of 60 |

T-cadherin is the established receptor for hexameric and HMW adiponectin
[PMID:15210937 *"We identified T-cadherin as a receptor for the hexameric and
high-molecular-weight species of adiponectin but not for the trimeric or
globular species"*] and mediates the M2-macrophage recruitment in PMID:26166748
[PMID:26166748 *"adiponectin was recruited to the cell surface of M2 macrophages
via its binding partner T-cadherin"*]. Neither gene records the other.

**Why I did not simply propose `GO:0045296 cadherin binding`:** its definition
is *"Binding to cadherin, a type I membrane protein involved in cell adhesion"*,
and T-cadherin is **GPI-anchored**, not a type I membrane protein. The
definition as written excludes the one cadherin that is a hormone receptor.
That is filed as a definition-correction question rather than acted on — another
instance of the rule that decided four calls this campaign: read the definition,
not the label.

## Non-confirmations, reported as such

1. **PAINT node placement is correct here.** Both halves of the reciprocal
   question were asked and both came back clean. `PTN008559544` reaches
   **exactly one human gene, ADIPOQ** (checked against all 82 human `GO:0005179`
   IBA rows, all 3 `GO:0045599` rows, and the single human `GO:0010642` IBA row,
   each fully paginated) and carries ortholog-specific terms.
   `PTN008355511` reaches ADIPOQ + C1QA/B/C + C1QTNF2/5/7/9/9B and gives them
   `GO:0005576 extracellular region` — for a clade mixing complement C1q chains
   with CTRP adipokines, the generic term *is* the LCA. No misplaced term, no
   mis-clustered member.
2. **All four IBAs are sound.** 21/21 donor tokens resolved, 21/21 carry their
   own experimental evidence for the propagated term, and every row's WITH/FROM
   includes `UniProtKB:Q15848` itself — self-referential IBAs, valid by
   construction (`root_cause: NO_FAILURE_CORE`). MGI and RGD tokens are rejected
   by QuickGO's `geneProductId` with HTTP 400 and were resolved through
   UniProt's `xref:` indexes instead; the fallback route is recorded per token.
3. **No InterPro2GO fold-to-activity row exists on this gene.** The campaign's
   live route was checked and is absent here; the fold error arrived by RCA
   instead.
4. **No TrEMBL or ORFeome partner substitutions**, unlike ACRV1.

## Retractions and errata

All 38 PMIDs relied on were checked for retraction, erratum and expression of
concern, by publication type **and** by `CommentsCorrections/RefType` on each
cited article's own record. No retractions. **Two unflagged errata, both with
NULL PubMed ids** — exactly the hole the standard query misses:

- `PMID:16622416` → Nat Cell Biol 2006;8(6):642, resolved via Crossref to
  `10.1038/ncb1422`;
- `PMID:12802337` → Nature 2004;431:1123, resolved via Crossref to
  `10.1038/nature03091` (*"Erratum: corrigendum: Cloning of adiponectin
  receptors that mediate antidiabetic metabolic effects"*).

Neither erratum's content was retrievable here, so nothing beyond the quoted
abstract sentences rests on either reference. Both are recorded in
`reference_review`.

## Where affinage helped and where it did not

`gates_passed: True`, 19 citations, all real PMIDs, no `PMID:bio_*` preprint
ids. Its multimer-state narrative (trimer→AMPK, hexamer/HMW→NF-κB and
T-cadherin) is accurate and is cited on the `GO:0043123` row.

**But `gates_passed` is precision, not recall, and the recall gap here was
decisive.** Affinage returned **none** of the papers that drive the four largest
findings: PMID:19855092 (the sialylation inversion), PMID:24531262 and
PMID:26166748 as a *pair* (it returned neither), PMID:36399478 and PMID:28675934
(the bulk imports), PMID:19109165 (the rosiglitazone role inversion),
PMID:19460854, PMID:18431508 and PMID:12070119 (the only measured
molecular-function experiment on the human protein). Its citation list is a
textbook-history reading list, which is a reasonable thing for it to be, but it
is not a review of *this gene's annotations*. Every finding above came from the
GOA rows and their references, not from the provider.

## Things I checked and got wrong on the first pass

- I expected 24 literal `source_note` keys in the builder and there were **36**.
  The assertion caught it. I did not invent a reconciliation; I re-counted.
- I initially wrote `GO:0038002 endocrine signaling` as `KEEP_AS_NON_CORE` while
  simultaneously listing it under `core_functions`. The validator's consistency
  warning caught the contradiction. Resolved toward `ACCEPT`: for a hormone,
  endocrine signalling is not peripheral, and the definition matches exactly.
- I put `GO:1904706`/`GO:1904753` (smooth-muscle proliferation and migration)
  in `core_functions[1].directly_involved_in`, then removed them. PDGF-BB
  sequestration acts on the receptor pathway; proliferation and migration are
  consequences of it. Function is not phenotype, including in my own summary.
- **I asserted a GO ancestry that does not exist, and it reached the shipped
  YAML.** The `GO:0005102` rows argued the term was the coarser grain of
  `GO:0005179`, "which is a descendant of GO:0048018 receptor ligand activity,
  **which is a descendant of this term**". False: `GO:0048018` sits under
  `GO:0140677 molecular function activator activity` → `GO:0098772 molecular
  function regulator activity`, in the **activity** branch, while `GO:0005102`
  is a **binding** term. GO deliberately keeps them apart. Found only by
  scripting the ancestry check I had been making by eye — the same shape as the
  regulation-is-not-subsumption trap, one step sideways. The correction
  *strengthens* the ACCEPT: the two rows are not redundant, they state
  different things. All ten relations the prose depends on are now fetched,
  recorded under `term_relations` in `results.json`, and asserted by a guard
  that fails if any disagrees.
- My first topology heuristic classified partners by signal peptide or TM helix
  and so counted multipass membrane proteins as "reachable" when only their
  cytosolic loops are Y2H-detectable. The six-partner cytosol-only figure is
  therefore a **floor**, and `RESULTS.md` says so; the argument rests on the
  assay, not the count.

## Review round 1 (PR #2328)

`ai4c-reviewer` approved with no CRITICAL or IMPORTANT findings and four
non-blocking suggestions. It independently re-derived the per-term multiset
from the GOA TSV and confirmed the 161 + 1 coverage term by term, confirmed the
`GO:0033691` reversal, confirmed that "absorption", "reabsorption" and
"tubular" genuinely do not occur in PMID:18431508's cached full text, and
confirmed the `GO:0005515` summaries are per-partner rather than boilerplate.
It also recorded that neither `just` nor `uv` was available in its sandbox, so
it could not run `just validate` — a useful caveat to have stated.

All four suggestions taken, three as written and one with an argument:

1. **The `GO:0120163`/PMID:26166748 REMOVE quoted a mechanism sentence** (M2
   recruitment via T-cadherin) rather than the direction-establishing one. Fair
   — the whole point of that row is that the paper shows *enhancement*, so the
   quote must carry the direction. Swapped to the impaired-thermogenic-program
   sentence, the same one the paired KEEP row uses, which is exactly the
   contrast being drawn.
2. **`full_text_unavailable`.** Set — but derived from each cached
   publication's own `full_text_available` field in `build_review.py` rather
   than hand-listed, so it cannot drift and cannot go stale in the direction
   that suppresses evidence extraction. That flags 27 of 42 references, not
   just the three under the REMOVEs.
3. **`substrates:` was the wrong home for a sequestered ligand.** Correct —
   adiponectin has no catalytic activity, so PDGF-BB is an input, not a
   substrate. Replaced with an `extensions` block on the annotation itself
   (`predicate: RO:0002233` has_input, as a bare CURIE, not an inlined Term).
4. **`GO:0042802 identical protein binding` is uninformative as a core MF.**
   True, and kept anyway, with the reason stated in the core function itself:
   it is the most specific *correct* MF available. `GO:0042803` names a
   stoichiometry adiponectin does not adopt, and `GO:0070207 protein
   homotrimerization` — the term that does state it — exists only in the
   biological process branch. Searching the ontology for a homotrimerisation or
   homooligomerisation *molecular function* returns nothing. The imprecision is
   the ontology's, not the annotation's, and dropping the MF would lose the
   fact entirely.

## terms.csv

`just validate` added three rows (`GO:0010642`, `GO:0033211`, `GO:0038002`) and,
as documented, **silently collapsed main's two pre-existing duplicate curies**
(`GO:0001675` 2→1, `GO:0009566` 2→1). Caught by a `Counter` multiset comparison,
not by reading the diff — the change reads as reordering. Repaired by restoring
`origin/main`'s file verbatim and appending only the three new rows at the end
(never re-sorting), then re-running `just validate` and re-checking: no rows lost
from main, three added, and the two pre-existing duplicates intact.
