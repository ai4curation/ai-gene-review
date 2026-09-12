# ADPRH (ARH1, P54922) — review notes

Human ADP-ribosylhydrolase ARH1. 357 aa, EC 3.2.2.19, `PE 1: Evidence at protein level`,
four X-ray structures (3HFW, 6G28, 6G2A, 6IUX).

Accession verified independently: `projects/paint/human-no-IBA-simple.csv:2907` reads
`human,P54922,ADPRH`, and UniProt returns `P54922 / ADPRH_HUMAN / Homo sapiens`,
`entryType: UniProtKB reviewed (Swiss-Prot)`.

## Row reconciliation (done before reviewing)

```
tail -n +2 ADPRH-goa.tsv | wc -l         -> 15
tail -n +2 ADPRH-goa.tsv | sort -u | wc  -> 15   (no duplicate TSV lines)
grep -c '^- term:' ADPRH-ai-review.yaml  -> 15
```

15 / 15 / 15. The `fetch-gene` stub did **not** collapse any rows on this gene — the two
`GO:0005515` IPI rows differ by reference as well as by WITH/FROM partner, so the seeder key
(GO id, evidence, reference, negated, qualifier) kept them separate. Reported as a
non-confirmation of the ADAMTSL5 stub-collapse defect.

## The worklist name is unreliable — ADPRH *does* have IBAs

`human-no-IBA-simple.csv` is a stale snapshot. Queried GOA directly: ADPRH carries **two IBA
rows**, `GO:0003875` and `GO:0051725`, both from PANTHER node `PTN009030515`. They were
adjudicated with the full propagation apparatus rather than skipped.

## What the enzyme actually does, and at what granularity

UniProt is explicit and residue-anchored:

- `[ADPRH-uniprot.txt:104]` `CC   -!- FUNCTION: Specifically acts as an arginine mono-ADP-ribosylhydrolase by`
- `CC   -!- CATALYTIC ACTIVITY: Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]`,
  `Rhea:RHEA:14885`, `EC=3.2.2.19`, `PhysiologicalDirection=left-to-right`,
  `ECO:0000269|PubMed:30472116`.
- `CC   -!- COFACTOR: Name=Mg(2+)`; `Note=Binds 2 magnesium ions per subunit.`
- `CC   -!- SUBUNIT: Monomer. {ECO:0000269|PubMed:19407395}.`
- **No `SUBCELLULAR LOCATION` comment at all**, and no `SIGNAL` or `TRANSMEM` feature.

The primary source is unambiguous about specificity:
[PMID:30472116 "Whereas ARH1 is specific for the N-glycolytic linkage of mono(ADP-ribosylated)
arginines, ARH3 specifically cleaves the O-glycolytic linkage of mono(ADP-ribosylated) serine
and, at least in vitro, other linkages as well, such as those in poly(ADP-ribose) chains."]
and its Figure 1A legend [PMID:30472116 "Arginine de-modification is catalyzed by ARH1,
PARylation is removed by PARG and to a lesser extend ARH3, MARylation on glutamate/aspartate
residues is hydrolyzed by macrodomain proteins, whereas the terminal modification on serine
residues is removed by ARH3."].

**GO:0003875's definition matches the measured reaction exactly** — "Catalysis of the
reactions: H2O + N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] = ADP-D-ribose +
L-arginyl-[protein] …" — so the annotated activity is right *and* at the right granularity.
There is no more specific child and no more general term is warranted.

### Reaction-direction check (the brief's specific ask): passes

The GOA contains no term asserting that ADPRH *performs* ADP-ribosylation. Every MF row is a
hydrolase term and every BP row is a de-modification term. The one row that looked like a
direction problem, `GO:0036211 protein modification process`, is not: GO places
`GO:0051725 protein de-ADP-ribosylation` **is_a** `GO:0043412 macromolecule modification`
**is_a** `GO:0036211`. Verified against QuickGO's ancestors endpoint with
`relations=is_a,part_of` — `GO:0036211` is in the ancestor set of `GO:0051725`. So the 1993
IMP row is a *granularity* problem (a strict ancestor of a term the gene already holds by
IDA), not a direction inversion. Action `MODIFY` → `GO:0051725`, not `REMOVE`.

### Logical-opposite cross-product check: negative

No `positive regulation of X` / `negative regulation of X` pair exists anywhere in the 15 GOA
rows, so the ADIPOQ cross-product test has nothing to intersect. Recorded as a null result so
the next reviewer knows it was run.

## The paralog-specificity question, measured

`genes/human/ADPRH/ADPRH-bioinformatics/` contains a committed, reproducible census
(`catalytic_residue_census.py`, `--self-test` clean, report regenerates byte-identically).

It tests the five ADPRH residues whose single substitutions UniProt records as
"Complete loss of activity" (`S54`, `D55`, `D56`, `D302`, `S305`, all
`ECO:0000269|PubMed:30472116`) across all **31 reviewed (Swiss-Prot) members of PTHR16222**,
which is **0.104% of the family's 29,860 proteins** — every statement below is about the
reviewed subset only.

| clade | n | % id to ADPRH | residues retained | disruptive in EVERY member | hold GO:0003875 |
|---|---|---|---|---|---|
| ADPRH (ARH1) | 5 | 48.4–100 | 5/5 | none | 5/5 |
| ADPRHL1 (ARH2) | 7 | 42.6–47.7 | 1–2 of 5 | **D56, S305** | **7/7** |
| ADPRS (ARH3) | 7 | 25.8–28.1 | 3–4 of 5 | none | 0/7 |
| other/non-vertebrate | 12 | 20.0–32.5 | 0–4 of 5 | none | 4/12 |

Three findings, in order of strength.

1. **The specificity leak this gene was expected to show is absent.** No serine-hydrolase
   (`GO:0140292`), PARG (`GO:0004649`), OAADPr-deacetylase (`GO:0061463`) or
   peptidyl-serine/glutamate de-ADP-ribosylation term appears anywhere on ADPRH. The
   discrimination is made deliberately and in two independent places: `IPR012108`
   ("ADP-ribosylarginine hydrolase") matches ADPRH and ADPRHL1 but **not** ADPRS, and PAINT
   keeps the two activities on different nodes — `PTN009030515` (`GO:0003875` + `GO:0051725`,
   seeded from `UniProtKB:P54922 | MGI:MGI:1098234 | RGD:2052`) reaches only ADPRH
   orthologues, while `PTN008564042` (`GO:0004649`, `GO:0140290`, `GO:0140292`, `GO:0071451`,
   seeded from `UniProtKB:Q9NX46 | MGI:MGI:2140364`) reaches only ADPRS orthologues. The same
   paper that annotated ADPRH, `PMID:30472116`, gave the serine/PARG terms to
   `UniProtKB:H3BCW1` (coelacanth ADPRS) and the arginine terms to `UniProtKB:P54922`, in the
   same curation pass. Hypothesis not confirmed — and worth as much as a finding.

2. **The reciprocal half is a real, filable defect.** ADPRHL1, whose Swiss-Prot record is
   titled "Inactive ADP-ribosyltransferase ARH2" and carries the CAUTION *"Although it belongs
   to the ADP-ribosylglycohydrolase family, lacks the metal-binding and substrate-binding
   residues, suggesting that it has no hydrolase activity"*, holds `GO:0003875` by
   `IEA GO_REF:0000120` and `GO:0000287` by `IEA GO_REF:0000002`. All **7** reviewed ADPRHL1
   orthologues hold `GO:0003875`, and all 7 have lost `D56` (→N or G) and `S305` (→A). The
   `IPR012108` → `GO:0000287`/`GO:0003875`/`GO:0051725` mapping and the ARBA route cannot see
   the residues; PAINT can, and gave the ADPRHL1 clade **nothing**. So this is not "GO is
   careless": it is one route succeeding where another fails, in the same family, on the same
   protein. Same shape as ADAM5's M12B measurement.

3. **A low residue count at low identity is not evidence.** A single identity threshold was
   tried first and **rejected**: the largest gap in the observed distribution lands at 65.4%,
   between *Dictyostelium* ADPRH (48.4%) and mouse Adprh (82.4%) — a taxonomic boundary that
   would have discarded the ADPRHL1 signal entirely. Clade-consistency plus substitution
   chemistry were used instead. The positive control is decisive: *Rhodospirillum rubrum*
   **DraG** (`P14300`) is at 27.5% identity and scores only 3/5, yet holds `GO:0003875` by its
   own `EXP` evidence — and **both** of its substitutions are S→T, which keeps the
   nucleophilic hydroxyl. Zero disruptive substitutions. The ADPRHL1 clade has 2–3 disruptive
   substitutions at ~45% identity. So the argument rests on *which* residues changed and to
   what, not on a count.

## ADP-ribosylation cycle context

ADPRH is the eraser half of a cycle whose writer is the arginine-specific transferase ARTC1
and, pathologically, cholera toxin:

- Gsα: [PMID:17526733 "Effects of intoxication on murine ADPRH-/- cells were greater than
  those on wild-type cells and were significantly reduced by overexpression of wild-type
  ADPRH in ADPRH-/- cells, as evidenced by both ADP-ribose-arginine content and Gsalpha
  modification."]
- TRIM72/MG53: [PMID:30429362 "The membrane repair protein TRIM72 was identified as a
  substrate for ART1 and ARH1; ADP-ribosylated TRIM72 levels were greater in ARH1-deficient
  mice following ischemia/reperfusion injury."]
- Tumour suppression: [PMID:21697277 "More significantly, ARH1(-/-) and ARH1(+/-) mice
  spontaneously developed lymphomas, adenocarcinomas, and metastases more frequently than
  wild-type ARH1(+/+) mice."]

None of these is in GOA for the human gene. They are mouse-knockout phenotypes, so they are
recorded as suggested experiments/questions rather than proposed human annotations.

An extra substrate demonstration that GOA does not carry and affinage did not return: IntAct
holds an `enzymatic study` / `cleavage` record pairing ADPRH with histone H1.1 from
`PMID:19895577`, a paper titled for *trypanosome* sirtuin ADP-ribosylation — ARH1 was used
there as the reagent establishing that arginine is the acceptor. Found by querying IntAct, not
by any ADPRH-keyed search. Consistent with the brief's "a paper titled for a partner can hold
the only experiment on your gene".

## An ontology gap: α-NAD+ hydrolysis has no GO term

UniProt records a second catalytic activity with experimental evidence:
`Reaction=alpha-NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)`, `Rhea:RHEA:68792`,
`ChEBI:CHEBI:77017`, `ECO:0000269|PubMed:31599159`. The paper is explicit that the
stereochemistry is the point: [PMID:31599159 "Here, we report that ARH1, ARH3, and macrodomain
proteins (i.e., MacroD1, MacroD2, C6orf130 (TARG1), Af1521, hydrolyzed α-NAD+ but not
β-NAD+."]

`GO:0003953 NAD+ nucleosidase activity` is **not** the right term and this is a label trap:
its definition is "Catalysis of the reaction: NAD+ + H2O = ADP-D-ribose + nicotinamide + H+"
with the single xref `EC 3.2.2.5`, i.e. the β-anomer reaction that ARH1 explicitly does
**not** catalyse. QuickGO and OLS searches for an α-NAD+ term return nothing (`GO:0003953`,
`GO:0061809 … cyclic ADP-ribose generating`, `GO:0050135 NADP+ nucleosidase activity` are the
only nucleosidase hits in this space). Filed under `proposed_new_terms`; no GO row is invented
to express it.

Caveat kept explicit: `PMID:21498885` states in its abstract that "ARH1 also hydrolyzed OAADPr
and poly(ADPr) as well as ADP-ribose-arginine", but that paper is **titled for ARH3**, is
cached abstract-only (`full_text_available: false`), and the statement is a one-line
restatement of earlier work rather than the paper's measurement. Recorded as a knowledge gap,
not used to propose `GO:0004649` or `GO:0061463` for ADPRH — especially since Rack et al.
place both of those activities on ARH3 in a head-to-head comparison.

## The extracellular row, traced to its origin

`GO:0005576 extracellular region`, `IEA GO_REF:0000107` (Ensembl Compara), WITH/FROM
`UniProtKB:Q02589 | ensembl:ENSRNOP00000034815` = rat Adprh. Querying the donor: rat Adprh
holds `GO:0005576` by a single `IDA` from `PMID:9037477`, assigned by RGD. The
reference-projection test on that PMID returns **1 annotation on 1 entity** (fully paginated),
so it is a single curator call, not a bulk import.

Reading it: the paper is *"Immunohistochemical localization of ADP-ribosylarginine hydrolase in
rodent CNS"*, and its content is overwhelmingly **intracellular** neuronal staining. The
extracellular claim rests on one western blot of a body fluid: [PMID:9037477 "On Western blot
analysis of rat cerebrospinal fluid (CSF), the anti-AAH antibodies recognized a protein with a
molecular mass of 38 kDa."], and the authors' own summary is [PMID:9037477 "the presence of
extracellular AAH in rat CSF."].

I am not overruling RGD's IDA on the rat gene — I have only the abstract. What I am reviewing
is the *projection onto human*, and it is weak in three independent ways: ADPRH has no signal
peptide, no transmembrane segment and no `SUBCELLULAR LOCATION` comment in UniProt; both of
its verified substrates (Gsα on the cytoplasmic leaflet, TRIM72) are intracellular; and a
38-kDa immunoreactive band in CSF is equally consistent with release from damaged cells.
`MARK_AS_OVER_ANNOTATED`, not `REMOVE` — a 38-kDa band in CSF is unexplained, not refuted, and
`GO:0005576` is a bare "space external to the outermost structure of a cell" with no secretion
mechanism implied.

Note also that the UniProt DR line still reads `GO; GO:0005615; C:extracellular space;
IEA:Ensembl` — `GO:0005615` was **obsoleted 2026-03-06** and `replaced_by GO:0005576`
(QuickGO `isObsolete: true`), which is why GOA shows the replacement id.

## Potassium

`GO:0030955 potassium ion binding`, `IDA`, `PMID:19407395`. The claim is real:
[PMID:19407395 "hARH1 has been cloned, expressed heterologously in Escherichia coli, purified
and crystallized in complex with K(+) and ADP."] and PDB 3HFW's
`nonpolymer_bound_components` are exactly `['K', 'MG']`. But the K+ came from the
crystallisation cocktail — [PMID:19407395 "A prerequisite for obtaining well diffracting
crystals was the performance of X-ray fluorescence analysis on poorly diffracting apo hARH1
crystals, which revealed the presence of trace amounts of K(+) in the crystal."] — and it does
**not** recur: 6G28 (1.23 Å) and 6IUX (1.20 Å) both contain only `AR6` + `MG`. UniProt records
six Mg2+ `BINDING` features and **no K+ feature**, and names only Mg2+ in `COFACTOR`.

Following the ADGB `GO:0019825` lesson, I checked the definition rather than the label:
`GO:0030955` is exactly "Binding to a potassium ion (K+)" — no functional-requirement claim —
so a resolved K+ ion satisfies it and deleting the row would be the mirror error. Not `REMOVE`.

**Revised in round 2 from `KEEP_AS_NON_CORE` to `MARK_AS_OVER_ANNOTATED`**, on the reviewer's
suggestion, after finding a third argument I had not made. The first two were already here —
the ion's provenance is the crystallisation cocktail, and it appears in 1 of 4 structures (now
computed and tabulated in `RESULTS.md`: magnesium 4/4, potassium 1/4). The decisive one is that
**UniProt read this same paper and reached the opposite conclusion** — it created six Mg2+
`BINDING` features citing `ECO:0000269|PubMed:19407395` and created no potassium feature at all.
That makes the disagreement two curators over one paper rather than this review against a
curator, which is what `MARK_AS_OVER_ANNOTATED` is for. The ADGB precedent still holds for the
*floor* — a measured complex satisfying a bare-binding definition is never a `REMOVE` — but
ADGB's oxy complex was measured in solution at physiological affinity, and a buffer-derived ion
in the lowest-resolution of four structures is not the same evidence.

## Interaction rows: one Y2H screen each, `NbExp` counting sub-methods again

Both `GO:0005515` rows resolve to reviewed canonical Swiss-Prot partners with matching lengths
— `Q12800 TFCP2_HUMAN` (502 aa) and `Q96BD6 SPSB1_HUMAN` (273 aa) — so no TrEMBL/ORFeome
substitution of the ACRV1 kind. But expanding the IntAct records reproduces the ACRV1 /
ADAMTSL5 pattern for a third time: UniProt's `NbExp=3` for each partner is **one screen logged
as three sub-methods**.

| partner | PMID | IntAct methods | distinct experiments |
|---|---|---|---|
| TFCP2 | 25416956 (HI-II-14) | `two hybrid array`, `two hybrid prey pooling approach`, `validated two hybrid` | 1 |
| SPSB1 | 32296183 (HuRI) | `two hybrid array`, `two hybrid prey pooling approach`, `validated two hybrid` | 1 |

Both MI-score 0.56, host `Saccharomyces cerevisiae`, no orthogonal assay anywhere in IntAct's
17 records for P54922. Promiscuity: TFCP2 has **350** distinct IntAct interactions and SPSB1
**78**, against ADPRH's 17. Neither partner appears in any ADPRH functional study, and no
follow-up exists for either. `MARK_AS_OVER_ANNOTATED` on both — and per CLAUDE.md, bare
`protein binding` would be uninformative even if replicated.

The remaining IntAct partners (BCAT1, OBSL1, XRN1, COQ8A, ZNF286A from BioPlex `anti tag
coip`; ACD by BiFC; SRPK1/SRPK2 as *kinases acting on* ADPRH) are not in GOA and are not
proposed.

## affinage record: `gates_passed: False`, and two verified provider errors

The run is flagged (`self_evaluation_pairwise: tie`). Re-checking every claim I might use
against the cited PMIDs found two real defects, both name/paralog collisions:

1. **`PMID:12464675` is about a different gene.** The affinage table asserts it establishes
   "ARH1 as a functional adaptor required for LDL receptor-dependent LDL internalization".
   The paper's "ARH1" is the **autosomal recessive hypercholesterolaemia adaptor
   (LDLRAP1)**, mapped in that paper to **chromosome 1p36**; ADPRH is at 3q22.1. The finding
   has nothing to do with ADP-ribosylhydrolase 1. Marked `WRONG_IDENTIFIER`.
2. **`PMID:16278211`'s mutagenesis is ARH3's, not ARH1's.** The affinage row reads "Critical
   vicinal acidic amino acids required for catalytic activity were identified by mutagenesis"
   as an ARH1 finding. The abstract attributes it to ARH3: *"Critical vicinal acidic amino
   acids in ARH3, identified by mutagenesis (Asp(77) and Asp(78)), are located in a region
   similar to that required for activity in ARH1"*. Marked `MISCITED`.

`PMID:36945646` is a **bioRxiv preprint** (`pubmed_publication_types: [Preprint]`) despite
having a numeric PMID; no claim rests on it.

Retraction / erratum sweep over all 21 PMIDs consulted (efetch, reading
`PublicationType` **and** `CommentsCorrections/RefType`): 21 of 21 records returned, **zero**
retractions, errata, corrections or expressions of concern; the only flag is the preprint type
above. Crossref `update-to`/`relation` was additionally checked for the four load-bearing
DOIs (30472116, 8349667, 19407395, 31599159) — all empty. Two DOIs (30429362, 17526733)
returned HTTP 404 from Crossref and are therefore *unchecked* by that route rather than clean.

Recall, as the brief predicts, is the weak axis: affinage returned neither `PMID:9037477` (the
sole origin of the extracellular annotation), nor `PMID:1375222` (the rat experimental source
behind the ortholog annotations), nor `PMID:25416956`/`PMID:32296183` (the two references
actually cited by GOA rows), nor `PMID:19895577`. Four of the papers that decide rows in this
review were absent from the provider record.

## Verdict summary

| # | term | ev | ref | action |
|---|---|---|---|---|
| 1 | GO:0003875 | IBA | GO_REF:0000033 | ACCEPT |
| 2 | GO:0051725 | IBA | GO_REF:0000033 | ACCEPT |
| 3 | GO:0000287 | IEA | GO_REF:0000002 | ACCEPT |
| 4 | GO:0003875 | IEA | GO_REF:0000120 | ACCEPT |
| 5 | GO:0051725 | IEA | GO_REF:0000002 | ACCEPT |
| 6 | GO:0005515 (TFCP2) | IPI | PMID:25416956 | MARK_AS_OVER_ANNOTATED |
| 7 | GO:0005515 (SPSB1) | IPI | PMID:32296183 | MARK_AS_OVER_ANNOTATED |
| 8 | GO:0005576 | IEA | GO_REF:0000107 | MARK_AS_OVER_ANNOTATED |
| 9 | GO:0000287 | IDA | PMID:30472116 | ACCEPT |
| 10 | GO:0003875 | IDA | PMID:30472116 | ACCEPT |
| 11 | GO:0051725 | IDA | PMID:30472116 | ACCEPT |
| 12 | GO:0000287 | IDA | PMID:19407395 | ACCEPT |
| 13 | GO:0030955 | IDA | PMID:19407395 | MARK_AS_OVER_ANNOTATED |
| 14 | GO:0003875 | IMP | PMID:8349667 | ACCEPT |
| 15 | GO:0036211 | IMP | PMID:8349667 | MODIFY → GO:0051725 |

No `REMOVE`. The gene's own annotation set is in unusually good shape; the defects found are
the human extracellular projection, two unreplicated Y2H rows, one redundant ancestor term,
and — outside this gene's rows — the ADPRHL1 catalytic over-annotation and the missing α-NAD+
term.

## Round 2: the cross-row citation slip, and a wrong inference of my own

The reviewer blocked on one thing, and it was a real defect of a kind no mechanical gate in
this repo can see: **three `supporting_text` quotes attached to `GO:0000287 magnesium ion
binding` never mentioned magnesium.** Two quoted the ARH1-vs-ARH3 arginine/serine specificity
sentence and a catalytic-positions line; the third quoted *"…crystallized in complex with K(+)
and ADP"* — which is the evidence for the **potassium** row two entries below it. Every quote
was verbatim, correctly attributed, and passed `checkquotes.py`; the error is in the join
between the quote and the row, exactly the ACBD3 diagnosis that *"quote validation cannot catch
these; the error is in the joins."*

Fixed three ways, not just by swapping text:

1. `PMID:30472116`'s cached full text has an on-point sentence and it is now quoted:
   [PMID:30472116 "The active sites of hARH1 and LchARH3 are structurally very similar and
   contain residues for the coordination of two Mg2+ ions."]
2. `PMID:19407395`'s cache is **abstract-only and contains no magnesium mention at all**
   (`grep -ci 'magnesium|Mg2+|Mg(2'` returns 0), so no better quote exists in it. Rather than
   leave a quote that cannot carry the claim, the census script was extended to query RCSB for
   all four ADPRH structures, and the row now cites the computed table. The abstract quote is
   retained with `full_text_unavailable: true`, which is what it is.
3. The evidence is now **born in the repository**: `RESULTS.md` carries a metals table —
   magnesium in **4 of 4** structures, potassium in **1 of 4** (3HFW, the lowest resolution) —
   so the magnesium and potassium claims are both checkable by a reader with no network.

**And a guard for it.** `audit_adprh_review.py` check `I` requires every `supporting_text` to
contain a surface form of its own row's term, keyed on the **GO id** rather than on any wording
that can drift. Run against `d86ff17d6` — the exact commit the reviewer blocked — it fires on
precisely the three sites flagged and nothing else, and it is clean on the current file. The
check declares its own limitation in the source: it matches surface forms, so it catches a
cross-row slip and nothing subtler, and a term with quotes but no declared forms is a **loud
failure** rather than a vacuous pass.

### A wrong inference, corrected by measurement

Both the reviewer and I read the standing `Label mismatch for 'GO:0003875'` warning as coming
from a stale *ontology snapshot* used by the term validator; the reviewer suggested "refreshing
the ontology snapshot", and I wrote in the PR body that the review should not be rewritten to
match it. The premise was wrong. A controlled test settles it: with the stale label in
`cache/go/terms.csv` the warning appears, and with the current label in that same file it
disappears. **The expected label is read from `cache/go/terms.csv`.** So the fix was one line
in the cache — which also stops this PR writing the older synonym into shared state, the
reviewer's actual concern — and `just validate human ADPRH` is now `✓ Valid` with no warnings.

The general point: the warning had been carried for two rounds with a confident explanation
attached, and one thirty-second experiment refuted it.

### Suggestions taken, and the one declined

Taken: `GO:0030955` → `MARK_AS_OVER_ANNOTATED`; `PMID:16278211` `correctness` back to
`VERIFIED`, because `correctness` describes *this* review's use of a reference and the
miscitation is the provider's (kept in `review_notes`); `is_invalid` dropped from
`PMID:12464675`, which is a wrong-gene collision rather than a retraction, with
`relevance: NONE` + `correctness: WRONG_IDENTIFIER` carrying the signal; a clause added to
`core_functions[0]` making the **mouse** provenance of both substrates explicit; and a line in
`RESULTS.md` stating that % identity uses an aligned-columns denominator.

Declined, with a reason: folding `core_functions[1]` (magnesium) into the hydrolase entry.
`molecular_function` is single-valued in the schema, so folding means dropping `GO:0000287`
from `core_functions` altogether — and the audit's check `G2` requires every ACCEPTed
molecular-function term either to appear in `core_functions` or to carry a written exemption,
precisely so a term cannot be quietly dropped. Writing that exemption would be the honest
alternative, but the biology does not call for it: the two Mg2+ are coordinated by the same
five residues whose substitution abolishes activity, so the ion is part of the catalytic
machine rather than an accessory to it. Keeping it visible as a core function and saying why
is better than hiding it behind an exemption.

## Round 3: the reviewer's script-hygiene items, and what enforcing one of them found

Four 🔵 items, all labelled "changing no annotation". Two of them did change what a *cited*
artifact asserts, so all four were fixed rather than deferred.

1. **A generated report asserted something it had not computed.** The metals paragraph opened
   *"Two magnesium ions per subunit are coordinated by the catalytic residues…"* — a UniProt
   `COFACTOR` statement that RCSB's `nonpolymer_bound_components` cannot support — **and that
   sentence was quoted as `supporting_text` on `core_functions[1]`.** The generator now emits
   only what it computes, and the stoichiometry lives in the row's `reason`, where it is
   attributed to UniProt.
2. **Two surface-form sets both matched the same table row.** `GO:0000287` listed `", mg |"`
   and `GO:0030955` listed `"| k, mg |"`, so the `| 3HFW | 1.92 | K, MG | … |` row satisfied
   *both* — the check could not have discriminated the two terms on the one row where it
   mattered. Table-cell fragments were dropped in favour of word forms, and **disjointness is
   now asserted rather than assumed**.

   Enforcing it immediately found **four more overlaps I had introduced myself**: `hydrolase`
   in both `GO:0003875` and `GO:0051725`, and `modification` / `reversible modification` /
   `de-modification` colliding across `GO:0036211` and `GO:0051725`. The reviewer spotted one
   instance; the assertion found the class. Check `I` still fires on exactly the three sites
   of `d86ff17d6` afterwards, so tightening the forms did not cost it its sensitivity.
3. **The docstring said "every" where the predicate is "any".** A row may legitimately carry a
   corroborating quote alongside the on-point one; the predicate was always `any`. Corrected,
   since a guard misdescribed in its own docstring is how the ADCK5 lint got past its author.
4. **`PDB_ENTRIES` was a literal.** Now derived from UniProt's `xref_pdb` cross-references, so
   a new deposition is picked up instead of silently omitted. The derived set reproduced the
   hardcoded one exactly — `3HFW, 6G28, 6G2A, 6IUX` — which is the confirmation worth having.

And one defect of my own, found while writing #4: the new `pdb_ids_of` self-test had a `try`
with no `else`, so an accession that happened to resolve would have passed it **silently**.
That is the fifth vacuous-pass instance this gene has produced, and the only reason it was
caught is that the campaign brief names the pattern explicitly.

### Stopping criterion

Rounds 2 and 3 changed one action (`GO:0030955`), four quotes, one reference `correctness`,
one `is_invalid`, and the surface-form table. Everything remaining that I can see is prose
about the harness rather than about what the harness computes. **If a further round produces
only items of that kind, I will fix anything that could misfire on another machine or misstate
a number, and decline changes that only reword an explanation** — the ADCK2 line.

## Round 4: applying that criterion to itself

Round 3's re-review returned three 🔵 items and the criterion above sorted them cleanly, which
is the point of stating it in advance.

**Fixed — misstated a number.** The notes and the `ADPRH-bioinformatics/README.md` both still
said "eight invariant checks (A–H)" after check `I` was added, and so did the PR body: **three
surfaces, drifted at once**, the "fixed in N places, landed in N−1" shape running in reverse.
The durable response is not to correct the three sentences but to make the one surface that
*can* enforce itself do so: `--self-test` now asserts that the letters enumerated in the module
docstring are exactly the checks the code implements. Writing it exposed a real subtlety — check
`A` is enforced by `StrictLoader` at **parse** time and never reaches `problems`, so a naive
implementation reported it as documented-but-missing. It is now credited only after the loader
is *demonstrated* to reject a duplicate key, and both directions are break-tested: deleting the
`I` docstring line fires it, and disabling the duplicate-key rejection fires it too.

**Fixed — could misfire on another machine.** The resolution clause computed "better-resolved
structures" as *structures without potassium*, conflating the two properties. With the present
four entries the answer is the same, but a structure tied at the worst resolution would have
been mislabelled as better-resolved, and a null resolution would have been silently dropped.
Now computed from resolution, with an explicit branch for ties and a printed note for any entry
whose resolution is unavailable. The regenerated report is unchanged for the current data,
which is the right outcome: **the fix was to the reasoning, not to the number.**

**Declined — already-declared limitation.** That disjoint surface forms are necessary but not
sufficient, since a quote can contain both its own term's form and another's (the `GO:0036211`
quote also contains `arginine`). True, and the source already says so: check `I` matches surface
forms, catches a cross-row slip, "and nothing subtler". Widening it to co-occurrence would mean
forbidding quotes that legitimately mention two entities, which is the guard-that-gets-worked-
around failure mode. The honest limitation stays declared rather than papered over.

**And a coupling the fix exposed.** Rewording the generated sentence from "the 3
better-resolved structures" to "all 3" **broke a `supporting_text` that quotes it** — four
quotes in this review cite `RESULTS.md`, so any edit to the generator's prose can silently
invalidate them. `checkquotes.py` caught it, which is precisely why it runs last, after the
report has been regenerated. Worth stating as a general hazard: **a quote into a generated
artifact is a two-way dependency**, and the direction that bites is the one where the
generator changes and the quote does not.

## Round 5: the same bug's third form, and why it was worth another round

The reviewer found that `better` was computed against the **worst** potassium-bearing
resolution with no potassium filter — so with two potassium structures at different
resolutions, the first branch would have emitted *"all N better-resolved structures … contain
none"* **naming a potassium-bearing structure**. A false sentence, and one that is quoted into
the review YAML. It is inside the stopping criterion twice over: it misstates a fact and it
misfires on data other than the current four. Fixed.

What makes this worth recording is that it is **the third form of one confusion** in three
consecutive rounds:

| round | `better` computed as | wrong because |
|---|---|---|
| 3 | structures *without potassium* | says nothing about resolution |
| 4 | resolution < **worst** K-bearing | a K-bearing structure can sit below the worst |
| 5 | resolution < **best** K-bearing | correct — "contains none" is then true by construction |

Three attempts at one sentence, each fixing the previous objection and introducing the next.
Two responses, because a third correction of the same shape would otherwise be inevitable:

1. **Define the set so the claim is true by construction**, rather than filtering after the
   fact — anything strictly better-resolved than *every* potassium structure cannot contain
   potassium. The code then **asserts** that property instead of trusting it.
2. **Extract the clause into a pure function** and unit-test *both* branches on synthetic
   entries, including the reviewer's exact scenario. The live four structures only ever reach
   branch 1, so branch 2 had never been executed — and `PDB_ENTRIES` is now derived from
   UniProt, so the set grows on its own and branch 2 becomes reachable with nobody editing the
   script. **Untested code that only new data can reach is the worst kind**; deriving the input
   made the script more correct and simultaneously more exposed.

The regenerated sentence is unchanged for the current data, which is the right outcome again.

Also taken: the docstring/implementation assertion moved out of `--self-test` and into
`audit()`, so it runs on every invocation like the disjointness assertion (break-tested: it
now fires from a plain `audit` run); the docstring's `I` entry reordered after `H`; and the
dead `worst` variable removed by the rewrite.

## Committed guards

`ADPRH-bioinformatics/audit_adprh_review.py` holds nine invariant checks (A–I) over the
emitted review YAML — strict duplicate-key loader, anchors/aliases, raw-vs-parsed quote
reconciliation, GOA row reconciliation, the logical-opposite citation cross-product,
summary-opener-vs-action agreement, `core_functions` agreement in both directions,
"a COMPLETE review contains no PENDING rows", and (added in round 2) "every row's
`supporting_text` set must mention that row's own term". `--self-test` is clean and every check is
break-tested in the direction it exists to catch.

Three things were learned by breaking it rather than by reading it, and they are the part
worth reporting:

1. **Check B did not fire.** The anchor detector was line-anchored (`^\s*-?\s*&id\d+`),
   which matches the `- &id024` form PyYAML emits but misses an inline `key: &id001`.
   Broadened to match anywhere.
2. **Check C's mutation was a silent no-op.** It inserted a *commented-out*
   `supporting_text:` line, which the raw regex correctly ignores — so the mutation
   proved nothing while reporting success. Replaced with a mutation on the parsed side,
   which is the shape a duplicate key or alias actually produces.
3. **Running the audit against the un-reviewed `fetch-gene` stub cleared it on 7 of 8
   checks**, with all 15 rows still `action: PENDING` and `description: TODO`. That is
   the defect that would actually have shipped, and only `G` caught it. Check `H` was
   added in response; the stub now produces four problems instead of one.

Running the guard against the state that would really have shipped is a stronger test
than any self-test, and it is free — the stub is one `git show` away.
