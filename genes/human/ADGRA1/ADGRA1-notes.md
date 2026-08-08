# ADGRA1 (GPR123) — review notes

UniProt: **Q86SQ6** (`AGRA1_HUMAN`), 560 aa, Swiss-Prot, `PE 1: Evidence at protein level`,
HGNC:13838, chromosome 10. Accession verified independently against
`projects/paint/human-no-IBA-simple.csv` (`human,Q86SQ6,ADGRA1`) and against the UniProt REST
record, which returns `uniProtkbId: AGRA1_HUMAN`, `geneName: ADGRA1`, synonym `GPR123`.

Computed evidence for everything numeric below lives in
`ADGRA1-bioinformatics/` (`analyze_adgra1.py` → `RESULTS.md`, `results.json`).
Nothing in that report is hardcoded; it is re-read from UniProt, IntAct and QuickGO on each run.

## Row reconciliation (done before reviewing, per CLAUDE.md)

| | count |
|---|---|
| `ADGRA1-goa.tsv` data lines (40 total − 1 header) | **39** |
| distinct lines (no byte-identical duplicates) | **39** |
| `fetch-gene` stub `existing_annotations` | **19** |
| final review `existing_annotations` | **39** |

The stub under-seeded by 20. Cause is the known one:
`GOAValidator.seed_missing_annotations` keys entries on
`(GO ID, evidence_type, reference, negated, qualifier)` and **omits WITH/FROM**, so the 22
`GO:0005515` rows — which differ *only* in the partner accession — collapsed to 2 entries
(one per reference). All 22 were restored so every partner carries its own verdict; that
matters here because the partners split 8/13 on whether an affinity was actually measured.

## What ADGRA1 is

ADGRA1 is the **structural outlier of the 33-member adhesion GPCR family**. Two independent
sources say so:

- UniProt's own feature table: `TOPO_DOM 1..19 Extracellular`, then `TRANSMEM 20..40`. The
  canonical isoform (Q86SQ6-3) has a **19-residue** extracellular N-terminus — there is
  physically no room for the GAIN/GPS module every other aGPCR carries.
- [PMID:12565841 "All the novel receptors have a GPS domain in their N-terminus, except GPR123, as well as long Ser/Thr rich regions forming mucin-like stalks."]
- [PMID:41961591 "ADGRA1 lacks both N-terminal extracellular adhesion domains and the GAIN domain, suggesting unique functions and signaling mechanisms compared to other aGPCRs."]

The mass of the protein is on the **inside**: `TOPO_DOM 306..560 Cytoplasmic`, a 255-residue
tail ending in `...WKNETTV`. `ETTV` matches the class I PDZ-binding consensus `X-[ST]-X-[VIL]`
exactly, which the analysis script checks against the retrieved sequence rather than asserting.
[PMID:41961591 "ADGRA1 exhibits a 7-transmembrane (7-TM) GPCR followed by a relatively large cytoplasmic tail"]
and the motif was already predicted from sequence conservation twenty years ago
[PMID:17212699 "GPR123 was found to be well conserved within the vertebrate lineage, especially within the transmembrane regions and in the distal part of the cytoplasmic tail, containing a potential PDZ binding domain."].

**UniProt does not annotate this motif.** There is no `FT MOTIF` feature in the entry
(checked programmatically), even though the entry's own `CC -!- INTERACTION` block lists 21
PDZ-domain partners. See "UniProt corrections" below.

Expression is CNS-restricted
[PMID:17212699 "The real-time PCR data indicates that GPR123 is predominantly expressed in CNS."],
and HPA calls the gene `Tissue enriched (brain)`.

## Finding 1 — the `protein binding` rows are a PDZ interactome, and they say so

All 22 `GO:0005515` rows come from two papers, and **both are PDZ-specific by construction**:

- `PMID:24550280` — proteomic peptide-phage display.
  [PMID:24550280 "we generated phage libraries containing all human and viral C-terminal peptides using custom oligonucleotide microarrays"];
  [PMID:24550280 "With these libraries we screened the nine PSD-95/Dlg/ZO-1 (PDZ) domains of human Densin-180, Erbin, Scribble, and Disks large homolog 1 for peptide ligands."]
  The ADGRA1 "interactor" here is its **C-terminal peptide**, selected by a DLG1 PDZ domain.
- `PMID:36115835` — the holdup assay.
  [PMID:36115835 "we measure the affinities of 65,000 interactions involving PDZ domains and their target PDZ-binding motifs (PBM)"]

Measured, not asserted: **21 of 21** GOA partners carry at least one annotated PDZ domain
(`RESULTS.md` Q2; range 2–13 domains, all reviewed Swiss-Prot entries at canonical length —
no TrEMBL or ORFeome substitutions, unlike ACRV1's `Q86WV8`). IntAct's own curation agrees
independently: every record annotates the ADGRA1 side as feature `PDZ-binding motif`
(`featureTypes: sufficient to bind`) and the partner side as `PDZ domain`.

**Topology check: passes.** The tail is cytoplasmic (`TOPO_DOM 306..560`) and all 21 partners
are cytoplasmic/membrane-associated scaffolds. This is the opposite of the ACRV1 pattern,
where a secretory-lumen protein had only cytosol-facing partners.

So `GO:0005515 protein binding` is uninformative where a mechanism is in hand:
**MODIFY → `GO:0030165 PDZ domain binding`** on all 22 rows.

**Do not over-read the motif, though.** The one experiment that tested what it *does* found
nothing: [PMID:41961591 "ADGRA1-ΔPDZ localized to synapses comparable to the WT, suggesting that other sequence features are responsible for synaptic localization."]
The motif binds PDZ domains; it does not target the receptor to synapses. The review says the
first and not the second.

## Finding 2 — GOA's 21 partners were chosen by domain count, not by affinity

This started as a numeric discrepancy and turned out to be the bug report, as usual.

IntAct holds 124 ADGRA1 records over 80 partners; 122 are `holdup assay` from `PMID:36115835`.
GOA/UniProt keep 21. Asking *which* 21:

- UniProt's `NbExp` **equals the IntAct record count for 21 of 21 partners** — so `NbExp` here
  is not a count of experiments at all. It counts **how many PDZ domains of the same partner
  protein were assayed** inside one dataset. PATJ's `NbExp=9` is nine PATJ PDZ domains, not
  nine experiments. (Third instance of the `NbExp` trap this campaign, after ACRV1 and
  ADAMTSL5; the first two were sub-methods of one screen, this one is domains of one protein.)
- The cut is exactly `NbExp ≥ 2`. 22 IntAct partners have ≥2 records; 21 are in GOA. The one
  exception is **NHERF4/PDZD3** — checked rather than rounded away.
- Consequence one: **13 of the 21 GOA partners have no quantified affinity.** IntAct carries a
  `kd:1(molar)` placeholder for them, consistent with the paper's own statement that
  [PMID:36115835 "pKd quantification thresholds, defined as the limit above which affinity constants could be quantified in each assay, were mostly comprised between 4 (Kd = 100 μM) and 3.1 (Kd = 800 μM)."]
- Consequence two: **23 partners with a genuinely measured Kd are excluded.** The sharpest
  statement is a single pair, because it isolates the variable: **SNX27, at 3.7 µM the tightest
  binder measured anywhere in the dataset, is excluded, while DLG1 at 4.6 µM — the second
  tightest — is retained.** Affinity is not what separates them; PDZ-domain count is (SNX27 has
  one PDZ domain, DLG1 has three). Of the four tightest binders overall — SNX27 3.7, DLG1 4.6,
  MAST2 4.9, MAGI3 5.1 µM — three are excluded and only DLG1 is kept.

  *(Corrected in round 2. The first version ranked the three excluded partners against DLG1 in
  the wrong direction. Lower Kd is tighter, so MAST2 (4.9) and MAGI3 (5.1) are in fact **weaker**
  than the retained DLG1 (4.6), and DLG1 is itself second-tightest overall rather than a
  ceiling. The reviewer caught it; I recomputed the full ranking from `results.json` and the
  reviewer is right. The corrected form is the stronger argument anyway, because one pair
  isolates the variable where three loosely-ranked numbers did not. The four retracted phrasings
  are now in `WITHDRAWN_PHRASES` in `audit_adgra1_claims.py`, and that check was verified to fire
  against the exact blocked revision via `git show 3ce38c99e`. Note the guard's limitation, which
  this very paragraph ran into: a literal-phrase matcher cannot distinguish a claim being
  retracted from a claim being asserted, so the retracted wording is described here rather than
  reproduced. It also cannot catch a paraphrase — prose surfaces still need re-reading by hand.)*

I did **not** convert this into per-row `MARK_AS_OVER_ANNOTATED` verdicts on the 13. The
`kd:1(molar)` placeholder means "not quantified", and IntAct's `negative` flag is `False` on
all 124 records, so the pairs were curated as detected positives. Treating an
under-determined placeholder as a refutation would be over-calling in the same shape as the
AADACL2 topology argument that measurement declined to confirm. The affinity split is recorded
per row as a fact and the verdict is the same MODIFY for all 22.

## Finding 3 — the adhesion-GPCR classification block, alive in GOA

Campaign calibration says the "structural class became a molecular function" error was swept
out of GOA when Swiss-Prot keyword annotations (`GO_REF:0000043`, `IEA:UniProtKB-KW`) were
retired around April 2026. **On ADGRA1 that is only half true**, and the half that survives is
worth reporting.

Checked at the UniProt layer first, as instructed: the entry carries **no `EC=`**, and its
`DR GO;` block contains **no `IEA:UniProtKB-KW` line at all** — the SPKW sweep did reach this
entry. `KW G protein-coupled receptor; Receptor; Transducer;` remain but no longer generate GO.

But GOA still carries `GO:0004930` four times, and the three non-IEA lines cite papers that
contain no functional experiment of any kind:

| row | code | reference | what the paper actually is |
|---|---|---|---|
| `GO:0004930` | NAS | PMID:12565841 | genome-database mining + phylogenetics [PMID:12565841 "We report six novel members of the superfamily of human G-protein coupled receptors (GPCRs) found by searches in the human genome databases"] |
| `GO:0004930` | NAS | PMID:17212699 | in-situ/qPCR expression map; its functional claim is explicitly a speculation [PMID:17212699 "The CNS specific expression, together with the high sequence conservation between the vertebrate sequences investigated, indicate that GPR123 may have an important role in the regulation of neuronal signal transduction."] |
| `GO:0004930` | TAS | PMID:15203201 | repertoire catalogue + EST charts [PMID:15203201 "EST expression charts for the entire repertoire of adhesion-GPCRs in human and mouse were established."] |

The TAS row is not a one-gene problem. Querying QuickGO **by reference** rather than by gene:
`PMID:15203201` carries **78 annotations across 27 distinct entities** — `GO:0016020` on 27,
`GO:0007186` on 26, `GO:0004930` on 25 — i.e. essentially **the entire human adhesion-GPCR
family**, all TAS, all from GDB, from a paper that performed no perturbation on any of them.
Applying the two-question projection test from ACTR8/ACTRT3: (1) 27 entities from one
reference; (2) the "functional" term does **not** stay on a perturbed gene, because no gene was
perturbed — the paper is a catalogue. So this is a block projection of family membership into
a molecular function, and it entered through **GDB TAS**, a route the SPKW retirement never
touched.

**But the term is nonetheless correct**, which is the part I did not expect. See Finding 4.

## Finding 4 — a 21-year-old unsupported annotation that became true in 2026

`PMID:41961591` (Cell Reports, Apr 2026) measured it:
[PMID:41961591 "Full-length ADGRA1 activated several G proteins, most notably Gα13"], validated
by dose–response —
[PMID:41961591 "Gα11, Gα15, and Gα13 all exhibited a plasmid copy-number-dependent change in BRET2, supporting the specificity of these measurements"]
— with GαoB as an unresponsive control.

Three qualifications that the review records rather than smooths over:

1. **The construct is mouse, not human.**
   [PMID:41961591 "Mouse ADGRA1 corresponded to Uniprot #Q8C4G9 and contained an N-terminal HA tag for expression studies."]
   So for the human gene this supports an **ISS** row with `supporting_entities: [UniProtKB:Q8C4G9]`, not IDA.
2. **The activation is agonist-independent.** No ligand is known, and the receptor's entire
   19-residue ectodomain is dispensable for it:
   [PMID:41961591 "The G protein coupling profile of ΔN-ADGRA1 was similar to full-length ADGRA1, suggesting that this extracellular sequence is not involved in basal G protein activation"].
3. `GO:0004930`'s definition is *"Combining with an extracellular signal and transmitting the
   signal across the membrane by activating an associated G-protein…"* (QuickGO). The **second**
   conjunct is now demonstrated; the **first** is unestablished, and experiment 2 above argues
   it is not what is happening in the assay. Same for `GO:0007186`, whose definition begins
   *"The series of molecular signals initiated by a ligand binding to its receptor."*

Verdict: **ACCEPT** `GO:0004930` and `GO:0007186` — GO routinely annotates orphan and
constitutively active GPCRs here and there is no ligand-free sibling term (checked: no such
term found; `GO:0004888` also requires "combining with a signal"). The ligand half is raised as
an ontology question, not converted into a GO action, and the three classification papers are
flagged `MISCITED` in `reference_review` — which is precisely what that field is for. A **NEW**
`GO:0004930` ISS row gives the term its first real evidence line.

So the fold/class-propagation lead came back **partly confirmed and partly inverted**: the
annotation *provenance* is as bad as predicted (a 27-gene block from a catalogue paper), and the
*claim* turns out to be right anyway. `REMOVE` would have been wrong.

## Finding 5 — PAINT node placement here is good, and that is the answer to the paralog question

Both halves of the node question, from `RESULTS.md` Q5:

| node | human reach | terms given |
|---|---|---|
| `PTN001738137` | ADGRA1, ADGRA2, ADGRA3 | `GO:0005886`, `GO:0007166` |
| `PTN002914505` | **ADGRA1 only** | `GO:0014069`, `GO:0098978` |
| `PTN002914520` | ADGRA2 only | `GO:0002040`, `GO:0007417`, `GO:0090263`, `GO:1990909` |
| `PTN002914494` | ADGRA3 only | `GO:0009897` |

**The paralog-transfer hypothesis is NOT confirmed, and the denominator makes that a
measurement rather than a hedge.** The ADGRA2 donors carry a large body of their own
experimental annotation — mouse Adgra2 alone has 15 experimental rows (angiogenesis, Wnt
signalling, CNS development), human ADGRA2 has 9 including `GO:1990909 Wnt signalosome` IDA,
zebrafish adgra2 has 10. Of all of that, exactly **two of the most generic terms** reached
ADGRA1, and every ADGRA2-specific Wnt/BBB term stayed on the ADGRA2-only node
`PTN002914520`. PAINT walled the characterised paralog's biology off correctly.

What *is* true is narrower and is recorded as provenance, not as a verdict: **1 of 6** IBA
donor tokens is an ADGRA1 ortholog. `GO:0005886` and `GO:0007166` reach ADGRA1 from a donor set
that is **entirely ADGRA2/ADGRA3**. Following the ACTA2 discipline of separating the two
claims: that is *provenance*, and on its own supports no verdict. The *circularity* question
resolves the other way — the terms are independently corroborated for ADGRA1 by its own
ortholog node (postsynaptic density is plasma membrane) and by surface-labelled HA-ADGRA1
puncta in the 2026 paper. So both rows are ACCEPT with the paralog-only donor set noted.

**Precision check (the ACRV1 test): negative.** Mouse Adgra1 holds `GO:0014069` and
`GO:0098978` by IDA/EXP from `PMID:28935861`, i.e. the *same* terms that propagated — not more
specific ones. So no downward MODIFY is warranted, unlike ACRV1 where the IBA landed three
levels above its donor's IDA. Reported because a null result from a check is a finding.
The donor evidence itself is sound:
[PMID:28935861 "Using super-resolution microscopy on primary neuronal culture we confirmed the postsynaptic localization of PLEKHA5 and ADGRA1."]

### The reciprocal half: what `PTN002914505` did *not* give

`PTN002914505`'s human reach is exactly ADGRA1, and it gives **two CC terms and nothing else**.
ADGRA1 therefore receives **no molecular function and no functional biological process from
PAINT at all**, and its only two IBA terms trace to a 2017 sub-cellular proteomics survey.

The 2026 Cell Reports work is ortholog-node evidence of exactly the kind that node exists to
propagate — G-protein coupling and a PV-interneuron-specific conditional-knockout phenotype in
mouse *Adgra1*, the very gene behind `MGI:MGI:1277167`. Recommending it to PAINT is the single
highest-value action available on this gene, and it is filed in `suggested_questions`.

## Finding 6 — the compartment and the process did not line up (round-2 fix)

GOA places ADGRA1 at the **glutamatergic** synapse and postsynaptic density, both by IBA from
the 2017 proteomics survey. The 2026 study localises it at the **inhibitory** synapse:
[PMID:41961591 "HA-ADGRA1 localized with inhibitory vGAT slightly higher in PV+ neurons than in SST+ neurons"],
from HA-ADGRA1 delivered by AAV into the dentate gyrus of PV-Cre and SST-Cre mice.

The first version of this review filed the *process* half of that experiment (`GO:0032230`) and
not the *compartment* half, so `core_functions` asserted a molecular function at the
glutamatergic postsynapse while asserting positive regulation of GABAergic transmission as the
process. **`GO:0098982` GABA-ergic synapse is now filed as a second NEW ISS row** on the same
reference, same organism, same evidence strength, and added to the `locations` of both core
functions. The existing `GO:0098978` ACCEPT is untouched — deferring to the SynGO curator is
right, and the two terms are not exclusive for a receptor at a subset of synapses of both kinds.

**`GO:0098793` presynapse was considered and declined**, and the reasons matter more than the
verdict because they run against the obvious reading. vGAT is a presynaptic marker and the
rescue works when the receptor is restored in the presynaptic PV cell
[PMID:41961591 "supporting a role for ADGRA1 in presynaptic PV+ cells that target DG GCs"] — but
that is a statement about *which cell*, not about which side of the synapse the protein sits on.
Against it, and keeping the two kinds of argument apart — a distinction the reviewer was right to
press: the **localisation** case is weak on its own terms, because the sentence is hedged
("*suggesting* subcellular localization") and rests entirely on overexpressed tagged protein
[PMID:41961591 "Given the absence of reliable antibodies for ADGRA1, we expressed HA-tagged ADGRA1 in primary hippocampal cultures"].
Those are the grounds for declining `GO:0098793`. Separately, on **function**, the paper's own
controls show the presynaptic release apparatus is intact —
[PMID:41961591 "PV-cKO GCs displayed no changes in the PPR or coefficient of variation in eIPSCs, supporting that presynaptic release probability is preserved"]
and [PMID:41961591 "the overall density of PV terminals labeled with synaptotagmin-2 (Syt2) was unaltered throughout the hippocampus"].
That is a mechanistic gap in its own right and says nothing about where the protein is; the first
round of this review recruited it as if it did. Both filed as a knowledge gap rather than a term.
Restraint argued per term from the measured numbers, not applied uniformly: `GO:0098982` in,
`GO:0098793` out.

## Cross-review check against the concurrent ADGRA2 and ADGRA3 reviews

Run per the AADACL2/3/4 lesson: when three paralogs are reviewed independently, compare the
rows they share rather than diverging silently. Sibling PRs #2314 (ADGRA2) and #2315 (ADGRA3).

Eleven rows are shared by all three genes (identical term + evidence code + reference; the two
IBA rows also have byte-identical WITH/FROM). **Eight of the eleven are resolved differently.**

| shared row | ADGRA1 | ADGRA2 | ADGRA3 |
|---|---|---|---|
| `GO:0005515` IPI (both refs) | MODIFY→`GO:0030165` | MODIFY→`GO:0030165` | MODIFY→`GO:0030165` |
| `GO:0005886` IBA | ACCEPT | ACCEPT | ACCEPT |
| `GO:0004930` IEA | ACCEPT | MARK_AS_OVER_ANNOTATED | ACCEPT |
| `GO:0004930` TAS | ACCEPT | **REMOVE** | ACCEPT |
| `GO:0007186` IEA | ACCEPT | MARK_AS_OVER_ANNOTATED | ACCEPT |
| `GO:0007186` TAS | ACCEPT | **REMOVE** | ACCEPT |
| `GO:0007166` IBA / IEA | ACCEPT | KEEP_AS_NON_CORE | ACCEPT |
| `GO:0016020` TAS | MODIFY→`GO:0005886` | KEEP_AS_NON_CORE | MODIFY→`GO:0005886` |
| `GO:0004888` IEA | MODIFY→`GO:0004930` | KEEP_AS_NON_CORE | ACCEPT |

**All three independently reached MODIFY → `GO:0030165` on the PDZ rows.** Three separate
reviews converging on the same replacement for the same 21-partner holdup dataset is the
strongest single result in this comparison.

**All three independently found the `PMID:15203201` GDB block.** ADGRA2's review derived the
same 78-annotations/27-entities/25-with-`GO:0004930` figures I did, and went one step further:
it checked *by name* which two entities miss `GO:0004930`, so that the pseudogene recipients
are confirmed rather than inferred from the count. I reproduced that claim from QuickGO and it
is **correct** — the two are `ADGRG3` and `ADGRV1`, and the pseudogenes `ADGRE4P` and
`ADGRF2P` do receive the molecular function. Two reviews deriving the same block independently
is much stronger than either alone; cited in agreement.

### Where I disagree, and why it is mostly not a disagreement

The `GO:0004930`/`GO:0007186` split (ADGRA1 ACCEPT, ADGRA3 ACCEPT, ADGRA2 REMOVE) is
**evidence-driven, not method-driven**, and by the ACTR1A/ACTR10 rule that needs no
reconciliation: all three reviews apply the same standard — annotate what has been measured on
*this* gene — and the measurements differ.

- ADGRA1: `PMID:41961591` (Cell Rep, Apr 2026), TRUPATH 14-sensor panel, Gα13/Gα11/Gα15, dose-response.
- ADGRA3: `PMID:40127866` (J Biol Chem, May 2025), "Complex G-protein signaling of the adhesion
  GPCR, ADGRA3" — Gi and Gs, stachel-dependent, DVL-independent. Verified at PubMed; the paper
  is real and is what the sibling says it is.
- ADGRA2: no coupling assay, and gene-specific evidence pointing away from one (IUPHAR lists no
  transducer; UniProt states the characterised tethering activity does not rely on its GPCR
  structure; the one reported heterotrimeric contact runs the other way, Gβγ binding the C-tail).

So three different verdicts on one row can all be right here, unlike the AADACL case where one
row on one node had to have one answer.

### One correction I owe the ADGRA2 review

Its REMOVE reason states: *"No G-protein coupling assay for ADGRA1, ADGRA2 or ADGRA3 exists in
the systematic adhesion-GPCR coupling literature ... and none for the ADGRA clade."*

**That clade-wide negative is false**, and it is refuted twice over by work the two sibling
reviews found independently: `PMID:41961591` assays ADGRA1 and `PMID:40127866` assays ADGRA3.
Neither is cited in the ADGRA2 review. The miss is instructive rather than careless for the
first — a hippocampal-circuits paper will not surface in a pharmacology-literature sweep — but
`PMID:40127866` is squarely inside the literature that was swept, so the sweep was incomplete.

This does **not** flip ADGRA2's verdict. Its gene-specific arguments are untouched by either
paper, and coupling in ADGRA1 and ADGRA3 says nothing about ADGRA2. What it removes is a
*strengthener*: the row cannot be argued down on the grounds that the clade as a whole is
uncoupled, only on ADGRA2's own evidence. An absence asserted at clade level, when two of three
members have since been assayed, is exactly the "an absence is not a finding" failure this
campaign has recorded before.

Its other cross-gene premise — *"across all three human ADGRA paralogs there is no
molecular-function IBA at all"* — I checked independently and it is **correct** (see the
node-reach table in `RESULTS.md`: no node in this family carries an MF term).

## Checks run that came back negative (recorded so the next reviewer knows)

- **Retraction / erratum / expression-of-concern sweep** over all 15 cited PMIDs, reading
  `CommentsCorrections/RefType` on each *cited* article's own PubMed record (a Publisher
  Correction is not findable by a publication-type search). One hit: `PMID:36115835` carries an
  Author Correction, `PMID:36477203`. Read it — it is **figure formatting only** ("errors in
  Fig. 2, Fig. 4 and Fig. 5 … PCC values were missing … axes labels were missing … the order of
  panels did not match"). It touches no data, and ADGRA1's data are in Supplementary Data 1
  regardless. Nothing rests on a corrected figure. No retractions anywhere.
- **Crossref `relation`/`update-to` check** for null-PMID corrigenda on the three load-bearing
  DOIs (`10.1016/j.celrep.2026.117255`, `10.1038/s41467-022-33018-0`,
  `10.1073/pnas.1312296111`): no `update-to` on any; the only relations are `has-preprint`.
- **Partner-accession discipline** (the ACRV1 `Q86WV8` check): all 21 resolve to reviewed
  Swiss-Prot entries at canonical length. No partial ORFeome constructs.
- **IBA-precision check** (ACRV1): negative, see above.
- **Dead-accession check**: every accession lookup prints its entry name and fails loudly on an
  empty one. None was empty.

## Things affinage got right, and one it did not

`gates_passed: True`, `faith_pct: 100.0`, no `PMID:bio_*` pseudo-identifiers in the citation
list. Its narrative is broadly accurate and it surfaced `PMID:28935861` and `PMID:41961591`,
which are the two most load-bearing references here.

Two corrections:

- It cites `PMID:40766348` as a 2025 bioRxiv finding **and** `PMID:41961591` as a separate 2026
  Cell Reports finding. They are the **same study** — PubMed records `UpdateIn: 41961591` on the
  preprint. Counting them as two dated findings inflates the apparent evidence base. The review
  cites the published version and marks the preprint `LOW`/superseded.
- Its SST claim ("PV and SST interneurons", "deficits in learning and memory") is the
  **preprint's** abstract. The published Cell Reports abstract is narrowed to PV
  [PMID:41961591 "ADGRA1 deletion in PV interneurons impairs intrinsic excitability and reduces inhibitory synaptic strength onto dentate gyrus granule cells."].
  The SST work survives in the published paper's body, but the headline claim was scoped down
  between versions, so the preprint wording should not be quoted as the finding.

It also never mentions the PDZ interactome, which is the best-evidenced molecular fact about
this protein.

## UniProt corrections to report (no GO row exists for these)

1. `CC -!- FUNCTION: Orphan receptor.` is the entire function annotation. It predates
   `PMID:41961591` (Gα13/Gα11/Gα15 coupling of the mouse ortholog) and `PMID:36115835`
   (21 PDZ partners with measured affinities). "Orphan" is still right about the *ligand*;
   it is now wrong as a summary of what is known.
2. **No `FT MOTIF` for the C-terminal PDZ-binding motif** (residues 557–560, `ETTV`), despite
   the entry listing 21 PDZ-domain interactors in its own `CC -!- INTERACTION` block and the
   motif being predicted in the literature since 2007. This is the single most useful missing
   feature on the entry.
3. `CC -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}` is sequence-predicted only, while
   SynGO holds IDA `GO:0014069`/`GO:0098978` on the mouse ortholog from `PMID:28935861`.
4. `NbExp` in the `CC -!- INTERACTION` block counts PDZ domains assayed, not experiments (see
   Finding 2). Every one of the 21 values is the IntAct record count for that partner.

## Verdict summary

Over the 39 GOA rows: **ACCEPT 11, MODIFY 28**. Plus **2 NEW** proposed rows, counted separately (41 `existing_annotations` entries in total).

MODIFY breakdown, summing to 28: 22 × `GO:0005515` → `GO:0030165`; 4 × `GO:0016020` →
`GO:0005886`; 1 × `GO:0004888` → `GO:0004930`; 1 × `GO:0007165` → `GO:0007166`.

ACCEPT breakdown, summing to 11: 4 IBA (`GO:0005886`, `GO:0007166`, `GO:0014069`,
`GO:0098978`); 3 InterPro IEA (`GO:0004930`, `GO:0007166`, `GO:0007186`); 2 NAS and 1 TAS
`GO:0004930`; 1 TAS `GO:0007186`.

NEW: `GO:0032230` (positive regulation of GABAergic synaptic transmission) and `GO:0098982`
(GABA-ergic synapse), both ISS from `PMID:41961591` with `UniProtKB:Q8C4G9` as the supporting
entity — the process and the compartment halves of the same experiment.
`GO:0004930` is deliberately **not** filed as NEW even though it needs a real evidence line —
the term is already in GOA four times, and `action: NEW` is for terms GOA lacks (the repo
validator enforces this, correctly). The request to attach `PMID:41961591` as an ISS evidence
line to the existing term is made in `suggested_questions` and in each `GO:0004930` row's reason.

**No `REMOVE` anywhere.** Nothing on this gene is demonstrably wrong — only under-specified
(`protein binding`, `membrane`, `signal transduction`) or, in the `GO:0004930` case,
under-evidenced by references that a 2026 paper has since overtaken. These counts are
enforced against the YAML by `ADGRA1-bioinformatics/audit_adgra1_claims.py`.
