# ADCK5 (Q3MIX3) — review notes

Human ADCK5, 580 aa, chromosome 8, HGNC:21738. Pharos class **Tdark**.
UniProt name: "Uncharacterized aarF domain-containing protein kinase 5".

## Starting hypothesis and how it resolved

The task brief proposed that `GO:0004672 protein kinase activity` / `GO:0006468 protein
phosphorylation` on ADCK5 would be fold-name-propagated-into-activity errors, on the grounds
that the characterised UbiB members COQ8A/COQ8B turned out not to be canonical protein
kinases.

**Outcome: the mechanism is real and demonstrable, but the predicted annotation error is not
in GOA.** ADCK5's entire GOA record is four rows and contains no molecular-function term
other than `GO:0005515 protein binding`. QuickGO returns **0 hits** for `GO:0004674` with
`goUsage=descendants` on Q3MIX3. There is nothing to REMOVE or MODIFY on kinase grounds.

The unsupported kinase claim does exist — but one layer up, in UniProt:

- `DE  RecName: ... EC=2.7.11.-` (protein-serine/threonine kinase)
- `KW  Serine/threonine-protein kinase;`
- `DR   GO; GO:0004674; F:protein serine/threonine kinase activity; IEA:UniProtKB-KW.`

…in the same entry that says *"The function of this protein is not yet clear."* and *"It is
not known if it has protein kinase activity and what type of substrate it would
phosphorylate (Ser, Thr or Tyr)."* GOA no longer imports keyword-derived (SPKW) annotations,
so the GO record is clean while the UniProt record is not. Reported as a UniProt correction
request rather than a GO action.

**Verified rather than assumed, with a control.** QuickGO returns **0** human annotations for
`GO_REF:0000043` (the Swiss-Prot-keyword pipeline, retired ~April 2026), against **139,714**
for `GO_REF:0000044` (SubCell) and **1,862** for `GO_REF:0000041` (UniPathway) — so the zero is
specific to the keyword pipeline, not an artefact of the query. And `GO:0004674` itself is
alive in GOA: PRKACA (P17612) carries 31 annotations to it, by ARBA and by many IDAs. ADCK5
receives it by no route at all.

## Family and structural basis (see `ADCK5-bioinformatics/`)

ADCK5 is a UbiB-family atypical kinase. Stefely et al. defined the UbiB-specific features
[PMID:25498144 "including a unique and invariant KxGQ motif"; "an atypical AAAS motif in an
alanine-rich (A-rich) loop that replaces the canonical glycine-rich (G-rich)
nucleotide-binding loop"], and argued they inhibit protein-kinase function — [PMID:25498144
"the KxGQ domain is likely to be an autoinhibitory domain because it fills the space
normally occupied by peptide or protein substrates in typical protein kinases"].

A MAFFT alignment of the five human UbiB proteins + yeast Coq8p + *E. coli* UbiB + PKA Cα
(negative control), with every published reference residue asserted before use, shows
**ADCK5 retains both inhibitory features and the full catalytic core**:

| feature | ADCK5 | PKA Cα | discriminates? |
|---|---|---|---|
| KxGQ lysine (COQ8A K276) | **K147** | *gap* | yes |
| A-rich loop Ala (COQ8A A339 ≡ PKA G53) | **A209** | G | yes |
| catalytic-loop Asp (COQ8A D488) | D360 | D | no |
| DFG Asp (COQ8A D507) | D382 | D | no |
| β3 Lys (PKA K73) | K228 | K | no |
| αC Glu (PKA E92) | E281 | E | no |
| catalytic-loop Asn (PKA N172) | N365 | N | no |

So ADCK5 is neither a canonical protein kinase nor a dead pseudokinase: it has an intact
nucleotide-binding/catalytic core behind a UbiB-type occluded substrate pocket.

The A209 assignment is corroborated two ways — the motif `AAAS` sits at 207–210 in ADCK5
exactly as it sits at 337–340 in COQ8A, and the COQ8A-anchored and PKA-anchored columns
resolve to the same alignment column (391).

## The mirror error, avoided

"UbiB proteins are not protein kinases" would be too strong. COQ8A/Coq8p indeed lack
generic in-trans activity [PMID:27499294 "neither catalyzes canonical protein kinase
activity"], but **COQ8B has a demonstrated protein substrate**: [PMID:38425362 "COQ3, but
not COQ6, is phosphorylated by COQ8B at multiple sites"]. The same paper excludes
small-molecule kinase activity for COQ8B [PMID:38425362 "GC/MS analyses did not detect any
phosphorylated CoQ intermediates, suggesting that the enzyme is not a small-molecule
kinase"]. (Caveat worth carrying: that study used ancestral-sequence-reconstructed COQ8
proteins, so it is a statement about the reconstructed tetrapod enzyme.)

So the right reading for ADCK5 is: *generic* Ser/Thr kinase activity is unsupported and
architecturally disfavoured; a *specific*, substrate-restricted activity is open and would
need direct assay. GOA reflects this correctly today by carrying no MF term at all.

## Localisation

- UniProt gives only `SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane`
  protein `{ECO:0000305}` — a curator inference from a *predicted* `TRANSMEM 50..67`
  (`ECO:0000255`). That maps to SubCell `SL-0162` → the `GO:0016020 membrane` IEA row.

- The mitochondrion is better supported: MitoCoP high-confidence mitochondrial proteome
  (PMID:34800366, HTP); [PMID:25498144 "In eukaryotes, UbiB homologs are found exclusively
  in mitochondria"]; and 17 of ADCK5's 25 distinct IntAct partners from the mitochondrial
  interactome study (PMID:27499296) are UniProt-annotated to the mitochondrion.

- **Asymmetry worth reporting, correctly attributed.** ADCK1 and ADCK2 receive
  `SL-0173 Mitochondrion` → `GO:0005739` from UniProt; ADCK5 receives only `SL-0162 Membrane`.
  My first reading was that the difference lay in UniProt's `SUBCELLULAR LOCATION` line rather
  than in the evidence, since all three carry the same MitoCoP HTP row. **That was wrong**, and
  checkable in-tree once ADCK1's review merged: `ADCK1-uniprot.txt:117` reads
  `SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:33988507}`, MitoCoP is not cited in
  that entry at all, and ADCK2's entry carries the same `ECO:0000269|PubMed:33988507`. Both
  paralogs have a dedicated experimental localisation that ADCK5 does not.

- **But the reason ADCK5 lacks it is absence of testing, not a negative result** — that study
  states plainly [PMID:33988507 "ADCK5 and OBSCN were absent from the library"]. QuickGO
  returns 0 annotations for Q3MIX3 from that reference, consistent with never having been
  assayed. So the UniProt correction request stands, but on ADCK5's own evidence (MitoCoP HTP;
  17/25 mitochondrial interactome partners; family-wide mitochondrial distribution) rather
  than on a parity that does not hold.

- Submitochondrial assignment (inner membrane?) is **not** established for ADCK5. Combining
  "mitochondrion (HTP)" with "membrane (predicted TM)" to assert `GO:0031966` would be a
  composite claim; left as a suggested experiment instead.

## PAINT

`PTHR43173` (ADCK5 = SF28, ADCK1 = SF19) has exactly **one** annotated node,
`PTN005148758`, seeded by a single yeast protein, MCP2 (`SGD:S000004243`, itself SF19),
carrying `GO:0005743`, `GO:0007005`, `GO:0055088`. ADCK1 inherits all three; ADCK5 inherits
nothing, because the node sits in the SF19 clade.

ADCK5 is the **only** human UbiB gene with zero IBA rows — UniProt states it independently:
`PAN-GO; Q3MIX3; 0 GO annotations based on evolutionary models.` This is the inverse of this
campaign's usual finding: under-reach, not over-propagation. Filed as a question to PAINT,
not as an action, because ADCK5 genuinely sits outside the annotated node's clade and the
node's evidence is a single yeast seed.

## `GO:0005515` — the NOTCH2NLA rows

Both rows name the same partner, NOTCH2NLA (Q7Z3S9). UniProt records `NbExp=4`, but expanding
IntAct shows PMID:25416956 logs the interaction **three times as three sub-method labels of
one Y2H screen** (`two hybrid array` + `two hybrid prey pooling approach` + `validated two
hybrid`), and PMID:31515488 adds one more `two hybrid array` from the same CCSB resource
lineage. MI score 0.67 throughout; no orthogonal assay in any of ADCK5's 54 IntAct records.
Third occurrence of this `NbExp` trap in the campaign (after ACRV1, ADAMTSL5).

NOTCH2NLA is `Secreted`/`Cytoplasm`, human-specific, and functions in neural progenitor
proliferation. Y2H places both proteins in the yeast nucleus and so removes the targeting
constraint.

**The compartment argument is an assumption, and is stated as one.** It holds if ADCK5's
kinase-like domain faces the matrix, as COQ8A's C-terminus is measured to do [PMID:27499294
"endogenous COQ8A is partially buried in the inner mitochondrial membrane with its C-terminus
facing the matrix"] — but ADCK5's own sidedness has never been measured, and an outer-membrane
anchor presenting the domain to the cytosol is not excluded. That is the same uncertainty that
stops this review proposing `GO:0031966`, so leaning on the compartment argument while
declining the localisation refinement would be inconsistent. The verdict does not need it: the
method-replication argument stands alone. (Caught by the PR reviewer; conceded.)

Checks that came back **negative** (recorded so they are not re-run blindly):
- NOTCH2NLA resolves to a reviewed, canonical, full-length Swiss-Prot entry — no
  TrEMBL/partial-ORFeome substitution as on ACRV1.
- PMID:34800366 is a proteome-wide localisation census carrying no functional/phenotype
  term, so the ACTR8 complex-to-subunit projection failure mode does not apply.
- No retraction, erratum or expression of concern on any cited PMID
  (`CommentsCorrections/RefType` on each cited record, plus Crossref `relation`/`update-to`
  for the six load-bearing DOIs).

## Literature quality

The only ADCK5-specific functional paper is PMID:32277958 (lung cancer, SOX9/PTTG1). Its
abstract is hedged throughout — "showed that ADCK5 might regulate the expression of tumor
oncogene human pituitary tumor transforming gene-1 (PTTG1) by phosphorylating transcription
factor SOX9" — and it reports no in vitro kinase assay; the SOX9 S181 claim rests on
mutagenesis of the substrate plus a motif-match argument, "The serine 181 site of SOX9 is in
a motif that is targeted by ADCK5." Full text unavailable. The affinage record restates this
as fact ("ADCK5 phosphorylates the transcription factor SOX9 at serine 181"); the abstract
does not support that strength. No GOA row rests on this paper, so nothing needed changing —
recorded because the discrepancy is the kind that would otherwise propagate.

affinage `gates_passed: True`, `faith_pct: 50.0`, 5 citations, all numeric PMIDs (no
`PMID:bio_*` preprint ids). Its remaining findings (senescence, JQ1, asthma) are
low-confidence, single-study, and none underpins a GOA row.

## Verdicts

| row | term | evidence | action |
|---|---|---|---|
| 1 | GO:0016020 membrane | IEA GO_REF:0000044 | ACCEPT (true but prediction-derived and less informative than the evidence allows) |
| 2 | GO:0005515 protein binding (NOTCH2NLA) | IPI PMID:25416956 | MARK_AS_OVER_ANNOTATED |
| 3 | GO:0005515 protein binding (NOTCH2NLA) | IPI PMID:31515488 | MARK_AS_OVER_ANNOTATED |
| 4 | GO:0005739 mitochondrion | HTP PMID:34800366 | ACCEPT |

No `core_functions` are asserted. ADCK5's molecular activity is genuinely undetermined —
UniProt says so, Pharos calls it Tdark, and this review found no measurement to replace
that. Per CLAUDE.md the "No core functions defined" warning is left standing rather than
silenced with invented content.

That absence is now recorded positively rather than only as a warning: two `knowledge_gaps`
entries carry it, a `BIOLOGY`/`WHOLLY_DARK` gap for the undetermined activity, substrate and
process, and an `ONTOLOGY`/`MF_DARK` gap for GO's inability to express the UbiB
occluded-pocket architecture. Both are grounded in quotes already verified in this review.
(The reviewer's point, and a good one: as prose in `suggested_questions` the finding is read
once; in `knowledge_gaps` it feeds the Function Knowledge Gaps project.)

## A break-test can be too destructive to discriminate

Worth recording because it is a failure mode this campaign has not named, and it kept a
defect alive across two rounds of this review.

I reported that a vacuity counter had been "moved inside the sentence loop". I had *added* the
inner increment and left the outer one, so the guard still reported itself exercised whenever
a unit tripped the pre-filter even if no sentence routed — the precise blindness it exists to
detect. The reason it survived my own break-testing is the general point:

> the only committed vacuity break-test blanked the topic from the surface entirely, driving
> **both** increments to zero, so it passed identically against the correct and the incorrect
> implementation.

Blanking a whole surface proves only that the check reads the surface at all. To certify
"the counter is inside the loop", the mutation has to *be* that difference: a unit that trips
the pre-filter while **no sentence routes**. That probe (`"COQ8A is a paralog of interest. The
row is IDA."` — paralog and token present, never in one sentence) reports the guard exercised
under the old implementation and reports vacuity under the new one, so it discriminates.

**The mutation must be as fine as the claim.** A coarser mutation still goes green, and green
is what makes it feel tested. This sits alongside the other guard failures found here — a
check that failed on *perfect* agreement, an unreachable branch that read as coverage, a probe
placed where it was easier to catch than the real thing — and it is the subtlest of them,
because the break-test genuinely ran and genuinely passed.

## Reconciliation

GOA TSV: 4 data rows. `existing_annotations`: 4 entries. No collapse; the two `GO:0005515`
rows share a partner but differ by reference, and the seeder keys on reference, so both
survived.
