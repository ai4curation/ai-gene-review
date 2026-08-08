# ADISSP (Q9GZN8) — review notes

Working journal for the PAINT + affinage review. Process history and negative results live here
rather than in the review YAML.

## 1. Identity: the gene was renamed, and the worklist contains a look-alike

Resolved before anything else, because the assignment I was given described ADISSP as "formerly
C5orf46/SSSP1". That is wrong, and the two genes both appear in the worklist:

| | ADISSP | C5orf46 |
|---|---|---|
| HGNC | HGNC:15873 | HGNC:33768 |
| previous symbol | **C20orf27** (changed 2022-12-12) | — |
| aliases | FLJ20550 | MGC23985, **SSSP1**, AP-64 |
| locus | 20p13 | 5q32 |
| UniProt | Q9GZN8, 174 aa | Q6UWT4, 87 aa |
| MANE | ENST00000379772.4 / NM_001258429.2 | ENST00000318315.5 / NM_206966.3 |

`projects/paint/human-no-IBA-simple.csv` line 1540 is `human,Q9GZN8,ADISSP`; line 5884 is
`human,Q6UWT4,C5orf46`. Different chromosomes, different proteins, and `SSSP1` (skin and saliva
secreted protein 1) belongs to the second. The gene reviewed here is **Q9GZN8 / ADISSP /
formerly C20orf27**. Both accessions were fetched with an assertion that `primaryAccession` equals
the accession requested, so neither is a merged-accession artefact.

Two ADISSP pseudogenes exist (ADISSPP1, HGNC:58498, 12q13.12; ADISSPP2, HGNC:58499, 16p11.2).
Neither has a UniProtKB entry — a gene-name search returns zero results for each, while the same
query returns three entries for ADISSP, so the route works and the zero is real. The
"pseudogene carrying a molecular function" tell therefore cannot arise here.

## 2. GOA row reconciliation

```
GOA TSV data rows                     13
distinct annotations                  12
seeded `- term:` entries in the stub  12
```

The gap is not a stub collapse of the kind seen on ADAMTSL5. Two rows are the same annotation:
`GO:0005576 / ISS / GO_REF:0000024 / UniProtKB:Q9D1K7 / located_in / UniProt`, identical in every
column except the date (2022-12-15 and 2025-10-27). One annotation, re-dated. The review has one
entry for the pair and says so in its summary. Final count: 12 reviewed entries plus one `NEW`
proposal = 13 entries.

## 3. The worklist's "no-IBA" name is accurate here — checked, not assumed

Seven genes this campaign were on `human-no-IBA-simple.csv` while carrying IBA rows, so this was
queried rather than inferred from the filename. A fully paginated QuickGO query
(`numberOfHits == len(results)` asserted) returns 13 annotations for Q9GZN8 with evidence
`{IDA:1, IEA:4, IMP:2, ISS:5, ND:1}` and **zero IBA**. Positive control from the same endpoint in
the same call pattern: ACTB (P60709) returns 286 annotations including 11 IBA. So the endpoint can
see IBA rows and ADISSP genuinely has none. PAINT contributes nothing to this gene, and the whole
propagation apparatus applies instead to Ensembl Compara and UniProt ISS.

## 4. The three non-PAINT routes: all three are non-confirmations

Each was tested with a control, because a rejected query and a genuine zero look identical.

- **InterPro2GO.** ADISSP matches three signatures — `IPR026794` (ADISSP family), `PF15006`
  (DUF4517) and `PTHR13287`. Grepping the current `interpro2go` file (30,127 lines) returns **zero**
  mappings for all three. Control: `IPR001879`, the entry that supplied `GO:0004930` on ADGRA2,
  returns 2. So the file and the grep work, and no GO term reaches this gene from a signature. The
  family signature is named after the gene and the Pfam entry is a domain of unknown function, so
  there is no fold-to-activity claim available to make.
- **Bulk classification imports carrying TAS.** ADISSP has no TAS row at all. Nothing to test.
- **ARBA.** No `GO_REF:0000117` row, and no `ARBA…` token in any WITH/FROM, so there is no rule to
  fetch at `rest.uniprot.org/arba/<id>`.

Worth recording the correction that came out of this: **`GO_REF:0000120` is not the ARBA
reference.** Reading it from the GO reference metadata, it is *"Combined Automated Annotation using
Multiple IEA Methods"*, which integrates identical annotations from UniRule, ARBA, InterPro2GO,
TreeGrafter2GO, RHEA2GO, KeyWord2GO, SubCellular2GO, EC2GO and Ensembl Compara. ARBA on its own is
`GO_REF:0000117`.

## 5. Main finding: a combined-methods reference recording one source as three witnesses

`GO:0005576 IEA GO_REF:0000120` carries three WITH/FROM tokens:

```
UniProtKB:Q9D1K7 | ensembl:ENSMUSP00000099477 | UniProtKB-SubCell:SL-0243
```

The whole purpose of GO_REF:0000120 is to record that several independent electronic pipelines
produced the same annotation, so three tokens read as three witnesses. They are not independent:

1. `UniProtKB:Q9D1K7` is mouse Adissp, which holds `GO:0005576` by IDA from PMID:36496438.
2. `ensembl:ENSMUSP00000099477` is that same mouse protein in a second namespace.
3. `UniProtKB-SubCell:SL-0243` is the UniProt vocabulary term "Secreted", which on the **human**
   entry is asserted as `CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q9D1K7}` —
   by similarity to the same mouse protein.

So the SubCellular2GO arm re-reads the Compara arm's own conclusion. All three reduce to Q9D1K7.
The annotation is correct; the *agreement* it advertises is one source counted three ways. Filed as
a question to GOA/UniProt rather than as a GO action, since the term itself is right.

## 6. The human/mouse exchange is reciprocal, not circular — a negative result

Worth stating because it is the shape that usually turns out to be circular. Human ADISSP's eight
IEA/ISS rows come from mouse Q9D1K7; mouse Q9D1K7's twelve annotations include three (`GO:0008157`,
`GO:0030511`, `GO:1901224`) that arrive by ISO/IEA **from human Q9GZN8**. Two directions of
transfer, but they carry *different* terms:

- mouse → human: the four terms resting on mouse experiments in PMID:36496438
  (`GO:0005576` IDA, `GO:0007189` IDA, `GO:0042593` IMP, `GO:1990845` IDA);
- human → mouse: the three terms resting on the human experiments in PMID:32024300.

No term is transferred back to its own origin. There is no circular chain, and every propagated
term has genuine experimental evidence at its source. `SOURCE_WEAK_OR_INFERRED` would have been
factually wrong on every row.

The similarity judgement is also unusually safe: both proteins are exactly 174 residues and
**90.2% identical (157/174) over an ungapped alignment with no indels**, far above the 40% peptide
identity that GO_REF:0000107 requires.

## 7. ADISSP is secreted, and it has no signal peptide — both are true

The task brief warned that a signal peptide is not the same thing as a correct secretion
annotation. Here the direction of that caution is inverted: there is *no* signal peptide and the
protein *is* secreted, by a non-classical route, and this is measured rather than inferred.

- No `FT SIGNAL` feature on either the human or the mouse entry. The human mature chain is
  `FT   CHAIN           2..174` with `/note="N-acetylalanine"` at residue 2 from mass spectrometry
  (`ECO:0007744|PubMed:22814378`), i.e. the initiator Met is removed and residue 2 becomes the
  N-terminus — not the topology of a protein whose signal peptide has been cleaved.
- Endogenous protein is in the medium: [PMID:36496438 "we were able to detect endogenous Adissp
  present in conditioned medium of mouse brown adipocyte culture"], and a Flag knock-in at the
  native locus puts the tag on the endogenous protein [PMID:36496438 "When probed with a Flag
  antibody, Adissp-Flag was detected in conditioned medium of differentiated knock-in adipocytes"].
- The route is non-classical, with an internal control: [PMID:36496438 "While adiponectin secretion
  was inhibited by brefeldin A and monensin as expected, Adissp secretion was instead increased"],
  the authors noting [PMID:36496438 "It has been reported that brefeldin A and monensin enhance the
  secretion of non-classically secreted proteins IL-1β and migration inhibitory factor"].
- Third, independent line: to purify secreted protein the authors had to add a signal peptide that
  the protein does not have [PMID:36496438 "To increase the yield and facilitate the purification of
  secreted Adissp, we added a signal peptide at the N-terminus of Adissp and a 6×His tag at its
  C-terminus"].
- The **human** protein specifically was shown to leave a cell [PMID:36496438 "this injection
  resulted in acute expression of ADISSP in the liver and its secretion into circulation with a
  concentration of about 0.45 μg/mL"], and the 2026 follow-up states [PMID:42030391 "Adissp is
  efficiently secreted by both mouse and human adipocytes (24, 25) and is present in human
  circulation (26, 27) (The human Protein Atlas)."].

This matters twice over. It makes the `GO:0005576` rows well founded rather than
prediction-derived, and it **defuses a topological argument I would otherwise have made** against
`GO:0008157`: a secreted protein binding cytosolic PP1c looks impossible, and on a signal-peptide
protein in a secretory lumen it would be (the ACRV1 pattern). A leaderless protein necessarily has
a cytosolic pool, so the two annotations are compatible. The unconventional secretion route is what
rescues the interaction, which is not obvious from either annotation alone.

Note what is *not* claimed: ADISSP is the cargo, not the machinery, so no protein-secretion process
term is proposed for it.

## 8. Reading trap in PMID:36496438 — which panels used the human protein

The paper infuses three adenoviruses: GFP, mouse Adissp, and human ADISSP. Only the
circulating-protein detection is credited to the human construct ("As shown with human ADISSP
adenovirus…", Fig. 4a). The browning and glucose-tolerance panels in the same figure are labelled
`Adissp`, i.e. the mouse protein. So the human protein has been shown to be **secreted** and
nothing more. It would be easy, and wrong, to read the paragraph as showing that human ADISSP
produced the metabolic phenotype.

## 9. `GO:0007189` names a receptor class nobody measured — MODIFY to `GO:0141163`

**This section was rewritten after review. The first version concluded `MARK_AS_OVER_ANNOTATED`
with no replacement, on the stated grounds that no correct term existed. That was wrong, and it was
wrong for an instructive reason: I checked the ancestors of `GO:0007189` and one sideways candidate
(`GO:0141156`), and stopped. I never looked at the regulation-of branch, which is exactly where an
extracellular ligand whose measured output is "the cAMP/PKA cassette runs harder" belongs. The
reviewer on PR #2340 pushed on precisely that gap.**

What PMID:36496438 measures, well: cAMP rises in transgenic inguinal WAT and falls in the
adipose-specific knockout; PKA substrate and HSL phosphorylation move both ways; purified protein
activates PKA dose- and time-dependently; labelled protein binds the adipocyte surface competably
[PMID:36496438 "a specific binding of Adissp to adipose tissue sections was detected, which can be
competed away by incubation with Adissp-containing conditioned medium"]. Both directions in one
sentence: [PMID:36496438 "Adipose-specific Adissp deletion decreases cAMP content and PKA activity,
suppresses inguinal WAT browning, and leads to HFD-induced obesity and hyperglycemia"].

What it does not measure: that the receptor is a G-protein-coupled receptor. The authors call it
putative throughout [PMID:36496438 "Together, our data suggest that Adissp activates PKA signaling
through binding to a putative receptor at adipocyte surface"], and the entire G-protein link is one
experiment [PMID:36496438 "induction of Ucp1 expression by Adissp was reduced by a merely 2-h
treatment with the PKA inhibitor H89 and was blocked by Melittin, an inhibitor for Gαs subunit of
the heterotrimeric G protein"] — melittin, a membrane-active bee-venom peptide, at 1 µM for 24 h,
n = 3.

Four candidate homes were then evaluated and three rejected; the resolution is `MODIFY` to
**`GO:0141163 positive regulation of cAMP/PKA signal transduction`**:

| candidate | verdict |
|---|---|
| an ancestor of `GO:0007189` | impossible — **every** ancestor retains the GPCR in its definition |
| `GO:0141156 cAMP/PKA signal transduction` | wrong — defined as an *intracellular* signalling cassette, which an extracellular ligand is not part of |
| `GO:0045762 positive regulation of adenylate cyclase activity` | closer, but asserts more than the data (see below) |
| **`GO:0141163 positive regulation of cAMP/PKA signal transduction`** | **fits** — a regulation term, so a ligand can regulate the cassette without being in it, and it makes no claim about receptor class |

`GO:0045762` was the reviewer's own suggestion and is the one to explain declining. The paper
measures **cAMP content** in transgenic and knockout tissue, not adenylate cyclase activity, and a
rise in cAMP content does not discriminate increased synthesis from reduced phosphodiesterase
activity. `GO:0045762` would assert the synthesis mechanism specifically; `GO:0141163` is satisfied
either way, so it asserts exactly what was shown. GO itself points the same way: the obsoletion
comment on `GO:0043950 positive regulation of cAMP-mediated signaling` directs users to
`GO:0141163` (naming `GO:0045762`-style cyclase regulation only as the alternative).

Verified before use: `GO:0141163` is current, is a biological process, and neither it nor
`GO:0007189` is an ancestor of the other — so this is a move between branches, not a change of
granularity, which is consistent with `MODIFY`. `REMOVE` would still be wrong: the receptor's class
is unmeasured, not refuted, and the missing receptor identity is recorded in `knowledge_gaps`.

## 10. `GO:1901224` → `GO:0043123`: canonical, not non-canonical

The cleanest defect on the gene, and it is decidable from the definitions plus the paper's figures.

- `GO:0038061` **non-canonical** NF-κB signal transduction requires NIK-dependent processing: NIK →
  IKKα → p100 phosphorylation → processing to p52.
- `GO:0007249` **canonical** NF-κB signal transduction is IKK-complex-dependent activation through
  IκB to the RelA-containing dimer.

PMID:32024300 measures phospho-IKK, phospho-IκB and phospho-p65 (RelA), in both directions
[PMID:32024300 "with C20orf27 overexpression in HCT15 and DLD-1 cells, the expression of p-TGFβR1,
p-TAK1, p-IKK, p-IĸB, and p-p65 was increased"] and [PMID:32024300 "in HT29 and SW480 cells with
C20orf27 silencing, p-TGFβR1, p-TAK1, p-IKK, p-IĸB, and p-p65 expressions were reduced"]. NIK,
p100/p52 and RelB appear nowhere in the paper. Those are canonical markers exclusively.

Sibling-versus-ancestor test run rather than assumed: the `is_a`/`part_of` ancestor closures of
`GO:1901224` and `GO:0043123` were fetched and **neither contains the other**. So this is a wrong
term, not an imprecise one, and the action is `MODIFY` rather than a granularity note. One
gotcha for anyone re-running it: neither regulation term has its target cascade in its `is_a`
closure either, because GO links them by `positively_regulates`, which does not subsume.

## 11. `GO:0005575` ND: a 2012 placeholder that its own file now contradicts

`GO:0005575`'s own comment says the term is recommended for gene products whose cellular component
is unknown, and that using it indicates no information was available. BHF-UCL made this row on
2012-07-16. The same GOA record now carries three `GO:0005576` extracellular region rows, one
tracing to a mouse IDA. The assertion the ND row encodes is no longer true. `REMOVE`. Not a
propagation failure of any kind — there is no WITH/FROM and no source to inspect.

## 12. PP1 binding: independently replicated, but the count needs its null

`GO:0008157` is the only molecular function ADISSP has, and the only one mouse Adissp has either
(checked: QuickGO returns 1 MF annotation for Q9GZN8 and 2 for Q9D1K7, all `GO:0008157`).

The cited evidence is a CoIP between two transfected tagged plasmids [PMID:32024300 "the C20orf27
and PP1c plasmids with the marker were transfected into HCT15 and DLD-1 cells"], which is not a
direct assay at native levels; for a physical interaction the code should be IPI with the partner
in WITH/FROM, and this row's WITH/FROM is empty.

IntAct corroborates it well beyond the cited paper. Twenty-seven records
(`totalElements == len(content)` asserted), 16 distinct pairs, of which ADISSP appears with PPP1CA,
PPP1CB, PPP1CC and the regulatory subunit PPP1R7 across **seven publications the annotation does
not cite** — PMIDs 24366813, 27173435, 27880917, 28330616, 28514442, 33961781, 40205054 — by
anti-tag co-IP, TAP and pull-down. (Three further records are `socioaffinity inference`, a
computational method, and are excluded from that count.)

**The null makes that less impressive than it first looks**, and it should be stated: PP1 catalytic
subunits are among the most frequently recovered proteins in affinity proteomics.

| protein | IntAct records |
|---|---|
| PPP1CA | 1012 |
| PPP1CC | 927 |
| PPP1CB | 571 |
| PPP1R7 | 150 |
| **ADISSP** | **27** |

Recurring in tag pulldowns is therefore weak evidence on its own. The informative direction is the
subject-centric one: **4 of ADISSP's 13 distinct IntAct protein partners are PP1-module
components**, so
the PP1 module dominates this small protein's own sparse interactome, rather than ADISSP being one
more name on PP1's long list. The term is also correctly left isoform-agnostic, since the paper
identified only "PP1c" by mass spectrometry and IntAct recovers all three catalytic subunits.

## 13. A motif scan that was discarded because its own controls failed

A first-pass scan for the canonical RVxF PP1-docking motif reported two candidate hits in ADISSP
(`RSIRF` at 13, `KVGF` at 54, against a composition-derived null expectation of 0.22 per protein),
both conserved in mouse. **No claim rests on this and none is made in the review**, because the
scan's own positive controls failed: of five characterised PP1-interacting proteins, PPP1R2/I-2 and
PPP1R13L scored zero RVxF hits. A scan whose known positives come back negative cannot certify its
positives either, and building a properly validated motif model is a project of its own rather than
a step in this review. Recorded here so the next reviewer knows the question was asked, what the
provisional answer looked like, and why it was not used. Mapping the PP1-docking surface is filed
under `suggested_experiments` instead.

## 14. Checks that came back negative, reported as such

- **Logical-opposite citation cross-product.** ADISSP has two `positive regulation of…` terms and no
  `negative regulation of…` term, so no logically opposed pair exists and the check is not
  applicable. The pair-finder was verified against a synthetic positive/negative pair to confirm it
  fires.
- **Reference-projection test.** `PMID:32024300` → 3 annotations over **1** entity;
  `PMID:36496438` → 4 annotations over **1** entity. Both fully paginated. Neither is a bulk import
  or a complex-to-subunit projection. `PMID:42030391` returns **0** annotations, which is a coverage
  gap rather than a projection.
- **Retraction / erratum / expression-of-concern.** All seven cited PMIDs clean by two independent
  routes: the article's own `PublicationType` and `CommentsCorrections` fields, and Crossref
  `relation`/`update-to`/`updated-by`. Positive control: PMID:32125225 fires on both
  `ptype:Retracted Publication` and `cc:RetractionIn->PMID:35078223`, so the detector works.
  This check found a bug in itself first: an unanchored `.//ArticleId` XPath was picking up DOIs
  from each article's **reference list**, so a Cancers 2020 paper appeared to have a 2017 Signal
  Transduction DOI. Anchoring to `PubmedData/ArticleIdList` fixed it, and the corrected DOIs were
  cross-checked by confirming each Crossref title matches its PubMed title.
- **Pseudogene molecular-function tell.** Not present; neither ADISSP pseudogene has a UniProtKB
  entry (with a working-route control, see §1).

## 15. affinage assessment

`gates_passed: False` (its own head-to-head self-evaluation scored `pairwise = tie` rather than
`win`). All five citations are real numeric PMIDs — no `PMID:bio_*` preprint identifiers — and all
five resolve to the papers and journals claimed, so its *precision* is fine. Its **recall is the
problem**, and the misses are exactly the facts the review turns on:

- the non-classical secretion result, and the absence of a signal peptide;
- the measurement of human ADISSP secretion into circulation;
- the canonical-versus-non-canonical NF-κB mismatch;
- the seven independent IntAct datasets behind the PP1 interaction;
- the stale ND root annotation.

One garbled claim: it renders PMID:40690096 as "acts upstream of NT5E as a downstream target",
which is self-contradictory; the paper's title is "C20orf27 promotes hepatocellular carcinoma
progression via NT5E." Its own GO grounding proposed `GO:0048018 receptor ligand activity`, which
independently agrees with the `NEW` term reached here from the primary literature.

**No affinage sentence is quoted anywhere in the review**, and its arithmetic was not carried over —
every number in the review was re-derived from the primary source or computed here. The validation
warning "No annotations reference available deep research files" is therefore left standing on
purpose: satisfying it would mean citing the provider for mechanistic claims, which this campaign
forbids.

## 16. Verification performed

- `checkquotes.py`: 81 quotes, 0 problems. Break-tested: a corrupted quote (cAMP → cGMP) is
  rejected.
- `just validate human ADISSP`: `✓ Valid`, one standing warning (see §15).
- All 31 candidate quotes verified verbatim before use; every `file:` quote confirmed to lie on a
  single physical line of `ADISSP-uniprot.txt`, since the repository's reference validator skips
  `file:` quotes entirely.
- `source_entities` built **from** the GOA WITH/FROM column with a drift assertion, not by hand.
  Break-tested by deleting one entity GOA lists, after first asserting the mutation target was
  present so the mutation could not be a silent no-op: the guard fires with the drift message and
  exits non-zero.
- Summary-opener-versus-action sweep over all 13 rows; `core_functions` ↔ ACCEPT/NEW checked in
  **both** directions; hedge-versus-structured-field sweep; and a per-row check that every quote
  names its subject. All four break-tested on a deliberately mutated copy, each firing with the
  right message. The subject-naming sweep found a real defect on its first run — the melittin quote
  was truncated so that it no longer named Adissp — which was fixed by quoting the full sentence.
  Two exceptions are encoded deliberately rather than left to discredit the check: a `file:` quote
  into the gene's own UniProt entry, and one quote that states a general premise about non-classical
  secretion rather than an observation about ADISSP.
- `cache/go/terms.csv`: one legitimate addition (`GO:0008157`), nothing lost, no new duplicates,
  verified by **multiset** comparison rather than by reading the diff; `cache_lint` exits 0.

## 17. Sibling cross-check against the merged ADIPOQ review — non-confirmation

The campaign brief records that ADIPOQ "shipped a false ancestry claim" about `GO:0048018`, which is
the term proposed here, so the merged review on `main` was checked for a surviving instance. It
asserts that `GO:0005179 hormone activity` sits "under GO:0048018 receptor ligand activity ->
GO:0140677 -> GO:0098772". **That claim is true**, verified against QuickGO: `GO:0005179`'s
`is_a`/`part_of` ancestor closure contains `GO:0048018`, `GO:0030545`, `GO:0140677` and `GO:0098772`,
and contains neither `GO:0005102` nor `GO:0005488`. I suspected a defect, tested it, and there is
none — the brief's note refers to a claim that was corrected before merge, not one still standing.

The check paid for itself anyway, because the ancestry it establishes bears directly on this gene.
`GO:0005179`, which ADIPOQ and LEP both carry, is a **descendant** of the `GO:0048018` proposed here.
So the two are not competing choices: the parent was chosen because the endocrine claim inside
hormone activity is established for the mouse protein and untested for the human one, and refining
to `GO:0005179` later would retract nothing. The `suggested_questions` entry now states this
relationship rather than merely contrasting the terms.

## 18. Review round on PR #2340

Approved on the first pass with four non-blocking suggestions, all four addressed. Recording what
changed, and what the process taught, since two of the four found genuine holes.

**1. The regulation-of branch (real gap, verdict changed).** See the rewritten §9. My argument for
"no replacement term exists" had checked the ancestors of `GO:0007189` and one sideways candidate,
and never looked at regulation-of. `GO:0007189` is now `MODIFY` → `GO:0141163 positive regulation of
cAMP/PKA signal transduction`. Note that the term I landed on is *not* the one suggested
(`GO:0045762`), and the reason for preferring it — cAMP *content* was measured, not cyclase
activity, so `GO:0045762` would assert a synthesis-versus-degradation distinction the data do not
make — is itself worth keeping.

**2. Prose-only IntAct evidence (real gap, artifact added).** Seven PMIDs, the 1012-versus-27 hub
null and the 4-of-13 partner fraction were asserted inside a `reason` string with nothing behind
them. They are now computed by `ADISSP-bioinformatics/analyze_adissp.py`, which reproduces every
figure I had written by hand and adds one I had not checked: the annotation's own reference,
PMID:32024300, is **not** among the seven IntAct publications, so those datasets are genuinely
additional rather than the same evidence re-counted.

**3. The 90.2% identity figure (provenance, artifact added).** Same script, with a self-identity
positive control and a refusal to compare unequal-length sequences rather than truncating them.

**4. Two uncited cached publications (addressed).** `PMID:22814378` (the N-acetylome study behind
UniProt's `ECO:0007744` evidence for N-acetylalanine at residue 2) and `PMID:12665801` (the direct
protein sequencing of residues 2–11 that underlies `PE 1`) are now listed in `references` with
`reference_review` notes explaining what each supports and why nothing is quoted from them.

### Two defects in my own harness, found this round

- **A stale claim survived one edit.** After changing the action, a `knowledge_gaps` statement still
  read "the GPCR term is flagged as over-annotated on its receptor clause". Found by grepping the
  *stable entity* (`GO:0007189` plus the verdict word) across every surface rather than re-reading
  the prose. This is the "fixed in N places, landed in N−1" recurrence, caught only because the
  sweep was run.
- **A guard-verification harness defeated by shell quoting.** My break-test loop reported
  `exit=0` for three break-tests that were in fact failing correctly, because
  `echo "$(basename $f) exit=$?"` evaluates `$?` *after* the command substitution, so it reports
  `basename`'s status, not the tested script's. For several minutes I had three guards that looked
  broken and were fine. The rule this reinforces: capture the exit status into a variable on the
  line immediately after the command, before any other command — including one hidden inside a
  string. A verification harness is code and fails like code.

Also worth recording as a **non-confirmation**: the anchor-assertion discipline earned its keep
twice this round. Both times I guessed at a multi-line string to replace and guessed wrong; both
times the `assert anchor in text` refused to run rather than silently changing nothing.

### Sweep B rescoped, and why

Making `GO:0007189` a `MODIFY` immediately produced a **false positive** in my own
`core_functions` ↔ rows check: it demanded that `GO:0043123`, the NF-κB `MODIFY` replacement, appear
in `core_functions`, when that row is deliberately non-core. The two directions need different
scopes, and conflating them is what caused it:

- **direction 1 (permitted):** a `core_functions` term must be backed by a row kept in some form —
  `ACCEPT`, `NEW`, *or* a `MODIFY` row's proposed replacement;
- **direction 2 (required):** only `ACCEPT`/`NEW` rows must appear in `core_functions`. A `MODIFY`
  row can be non-core exactly as a `KEEP_AS_NON_CORE` row is.

Both directions were then break-tested independently, plus the happy path that had been falsely
firing, so neither direction is vacuous and the exception is not a blanket widening.

## 19. Round 3: the review found a wrong set hiding behind a right number

Approved again, with two 🔵 notes. Both were real; the first is the most instructive defect in this
review, and **the reviewer's diagnosis of it was itself wrong in two checkable ways** — which is worth
recording, because conceding a wrong diagnosis would have put a false statement in the review.

### What the reviewer flagged

That `distinct_partners = 13` was not 13 protein partners: the set contained `ADISSP` itself and
`mrna_adissp`, so the "4 of 13" fraction was diluted. They attributed it to
`partner = b if id_a.endswith(SUBJECT) else a` mis-resolving when `idA` is an isoform form, and
concluded that "no real partner can be lost this way" and that the error "runs in the conservative
direction (4 of 11 protein partners would be a *stronger* claim than 4 of 13)".

### What was actually wrong

The mechanism is worse. IntAct returns ids **with a trailing database tag** — `"Q9GZN8 (uniprotkb)"` —
so `endswith("Q9GZN8")` was **never true for any record**, not merely for isoform forms. The resolver
therefore took `partner = moleculeA` in all 27 records. Consequences:

- every partner that appears **only** as `moleculeB` was **dropped** — `RALYL` (Q86SE5) and a PRO
  chain of P0C6X7. So real partners *were* lost, and the first premise is false.
- `ADISSP` entered its own partner set, and `mrna_adissp` entered from a CLASH record in which
  **neither** side is ADISSP (it pairs the ADISSP mRNA with a miRNA).
- the correct count of distinct **protein** partners is **13**, not 11 — so the fraction is unchanged
  at 4 of 13 and the error was not conservative. It was a *different wrong set that produced the same
  number*.

That last point is the finding. Two spurious entries and two dropped ones cancelled exactly, so the
count survived a hand check, a review, and a table. **A right-looking number is not evidence of a
right set**, and this is the sharpest instance of it I have seen: no arithmetic discrepancy existed to
notice, because there was none.

### The fix, and its guard

`base_accession()` now strips the database tag and the isoform/PRO suffix for subject matching while
retaining the full name for partners (a PRO chain is a distinct participant). `resolve_partners()`
determines the partner as the non-subject side, **raises** if both sides resolve to the subject, and
excludes — while counting and reporting — records in which neither side is the protein. `RESULTS.md`
now states all three numbers separately: 27 total records, 26 involving the ADISSP protein, 1 involving
the locus but not the protein.

A committed `--self-test` covers six directions, and it was validated the two ways that matter:

- **Run against the defect that actually shipped.** Taking the resolver logic verbatim from
  `git show HEAD:...` and applying it to the live IntAct response reproduces the wrong set —
  13 partners including `ADISSP` and `mrna_adissp`, missing `RALYL` and the PRO chain — against the
  fixed resolver's 13 with those two recovered. Same count, different set, demonstrated rather than
  asserted.
- **Prove the test can fail.** Reinstating the shipped defect inside `resolve_partners` makes
  direction 1 fail with exactly its own diagnosis ("a partner appearing only as moleculeB was
  dropped"), plus directions 4 and 6; disabling the self-interaction guard makes direction 3 fail with
  its own message. Both mutations were applied only after asserting the target string was present, so
  neither could be a silent no-op, and both exit non-zero.

The self-test also **declares one thing it cannot do** (direction 1b): the "subject appears in its own
partner set" invariant keys on accessions, so a partner named by gene *symbol* — which is exactly how
the spurious `ADISSP` entry appeared — cannot be matched against the subject accession. That invariant
would not have caught the shipped bug. What catches it is direction 1's set-equality assertion on a
fixture. Saying so is better than letting the invariant read as coverage it does not have.

### The other note, and a two-way dependency earned its keep

The reviewer also spotted that both `reason` strings said "Three candidate homes were checked" against
a four-row table — three rejected plus one chosen. Corrected in the YAML and in §9.

Regenerating `RESULTS.md` broke a `file:` quote that cited the changed "PP1-module partners" line, in
**two** places, and `checkquotes.py` caught both. This is the two-way dependency a quote into a
generated artifact creates: the prose you will edit is coupled to citations you will forget. It only
worked because the quote check was re-run *after* regeneration.

## 20. Round 4: three hygiene items, and the recurrence caught twice in one sitting

All three remaining 🔵 items fixed. Two are worth recording for what they show about process rather
than about ADISSP.

**Dead code with a comment contradicting its neighbour.** `self_test()` contained a nested
`regressed()` that was defined and never called, left behind when I pivoted from "simulate the
regression" to "declare that the invariant cannot catch it". Its comment claimed to do the thing the
comment two lines below explains is not informative. Deleted; the direction-1b declaration is the
honest version and stands alone.

**"Fixed in N places, landed in N−1", twice, on the round that documents the pattern.** The
`protein` qualifier on the partner count reached 2 of 4 sites. Then, fixing it, the same thing happened
again for a new reason: my patch script asserted an anchor in the annotation builder, the anchor had
drifted, the `AssertionError` aborted the script — and the *later* edit in the same script, to the
notes file, never ran. Both misses were found the same way: **grep the number (`13`, `thirteen`), not
the phrase.** The phrase is what gets reworded; the number does not.

The second miss generalises to something I had not thought about. An anchor assertion protects the
edit it guards, but if several independent edits share one script, a failed assertion silently cancels
every edit after it. So either put one edit per script, or collect failures and apply what can be
applied — and in all cases **re-grep afterwards rather than trusting the exit status**, because a
script that aborts halfway looks the same from outside as one that had nothing to do. The anchor
assertions still earned their keep: they refused to run against drifted text on three separate
occasions across rounds 3 and 4, and each refusal was a real drift, not a false alarm.

**Grammar in generated output.** `render()` emitted "1 involve" and pushed a hand-wrapped line past
its break. Both were string-assembly artefacts with no data behind them; `render()` now selects
singular or plural from the count.

**On wiring `--self-test` into CI**, which the reviewer rightly notes is not done: deliberately not
done here. `.github/workflows/` is shared configuration outside the scope of a single gene review, and
the campaign's standing rule is not to edit it from inside a gene PR. The self-test protects against
regression when the script is next run, and the script is only ever run to regenerate `RESULTS.md`, at
which point a regression would surface. That is a real limitation and is stated rather than papered
over.

### Stopping criterion

Rounds 2 and 3 each changed something substantive — a GO term and an action in round 2, a partner set
and a verdict-bearing figure in round 3. Round 4 changed no term, no action, no evidence code, no
quote, and no reported number: the partner count, the identity figure, the seven PMIDs and every
verdict are identical to round 3. What moved was dead code, a qualifier's coverage, and a plural verb
in generated prose.

By the campaign's own rule — when the last round moves nothing in a deliverable, the loop has migrated
from the curation to the harness — this is the line. I will still fix anything that misstates a number,
breaks a quote, or could misfire on another machine. I will not keep iterating on the phrasing of the
harness's own commentary.

## 21. Round 5: the one carve-out the stopping criterion named

The reviewer flagged two trailing observations and said explicitly that neither was a request and
neither was worth a round 5. One of them was, and it is worth being precise about why, because the
point of stating a stopping criterion is that it decides cases rather than ending discussion.

The criterion I stated was: *"I will still fix anything that misstates a number, breaks a quote, or
could misfire on another machine."* Observation 1 is the third of those. `render()`'s exclusion
sentence pluralised its leading clause from the count but left the tail and a **hardcoded
parenthetical** — *"(a CLASH record pairing the ADISSP mRNA with a miRNA), and is excluded … as a
partner"* — behind. With one excluded record that reads correctly. With two it would emit
*"2 records involve … and **is** excluded … as **a partner**"*, and the parenthetical would describe
one record while claiming to describe both. Nothing is wrong today; the wrongness is reachable by new
IntAct data alone, which is the worst kind of latent bug because no past run exercises it. The
reviewer's own diagnosis names the shape exactly: the fix that made the singular correct left the
other branch behind — the qualifier miss, one level down.

The fix removes the branch rather than repairing it. `resolve_partners()` now returns a **description
of each excluded record built from the data** instead of a bare count, and `render()` lists them, so
the prose cannot disagree with the data at any count and there is nothing hardcoded to go stale:

> 1 record(s) involve the locus but not the protein and are excluded from the partner set rather than
> counted as partners: mrna_adissp / (human) hsamir320a3p by clash.

A new self-test direction 2b exercises the multiple-exclusion path with two fixtures, which the
previous version could not reach — the old singular-only assertion would have passed against the
broken plural branch. That is the "advertises N directions, implements fewer" mode, avoided by adding
the fixture rather than the assertion.

Observation 2 — `PROTEIN` in caps at one of four sites where the others are lowercase — is purely
cosmetic prose and by the criterion I would not have reopened for it. It is lowercased here only
because it was one edit in a push that was already happening for observation 1, which makes all four
sites read identically.

**This is the last push.** Everything remaining in the thread is commentary on the harness's own
prose, which is where the criterion draws the line.
