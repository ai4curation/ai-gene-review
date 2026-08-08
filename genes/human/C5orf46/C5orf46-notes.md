# C5orf46 — review notes

## Identity, settled before anything else

The worklist row is `human,Q6UWT4,C5orf46`, and a `C#orf#` placeholder is often renamed, so
the current approved symbol was established from three independent sources rather than
assumed:

| source | symbol | id | location | length | note |
|---|---|---|---|---|---|
| HGNC | **C5orf46** | HGNC:33768 | 5q32 | — | `status: Approved`, `prev_symbol: null`, `date_symbol_changed: null` |
| UniProt | **C5orf46** | Q6UWT4 (`CE046_HUMAN`) | — | 87 aa | reviewed (Swiss-Prot), `Uncharacterized protein C5orf46` |
| NCBI Gene | **C5orf46** | 389336 | 5q32 | — | `chromosome 5 open reading frame 46` |

All three agree; **the symbol has never been changed.** HGNC records the aliases
`MGC23985`, `SSSP1` and `AP-64`, and the alias name *skin and saliva secreted protein 1* —
which matters below, because it independently corroborates the tissue distribution that the
only functional paper derives from a database rather than measuring.

`Q6UWT4` was verified live: `primaryAccession == Q6UWT4`, so no merged-accession
substitution. (The committed analysis script asserts this on every UniProt fetch, and
break-tests it against `O15507`, which returns HTTP 200 and a complete reviewed record for
GFRA1.)

**This gene is not ADISSP.** ADISSP is HGNC:15873 / `Q9GZN8` / formerly C20orf27 / 20p13 /
174 aa, a separate row in the same worklist, already reviewed. The two share nothing but the
`C#orf#` naming convention.

## The worklist's "no IBA" name is accurate here — and that was checked, not assumed

The worklist is `human-no-IBA-simple.csv` and is known to be stale. Queried directly:
Q6UWT4 has **16** GOA annotations, evidence codes **IPI 14, IEA 1, HDA 1**, and **zero IBA**.
Positive controls in the identical call pattern returned ADGRA2 **6** IBA and ACTB **11**, so
the zero is a genuine absence rather than a rejected query. UniProt's own
`DR PAN-GO; Q6UWT4; 0 GO annotations based on evolutionary models` agrees. There is no PAINT
propagation on this gene to adjudicate, and no `propagation_review` is owed.

GOA row reconciliation, done before reviewing anything: the TSV has **16** data lines, all
distinct; the `fetch-gene` stub seeded **5** entries. Twelve `GO:0005515` rows differing only
in their WITH/FROM partner had been collapsed into one — the documented
`seed_missing_annotations` behaviour, whose key omits WITH/FROM. All twelve were restored so
each partner gets its own verdict, giving 16 review entries for 16 TSV rows.

## The dominant defect is absence, and it is quantifiable

`PMID:33804835` is the sole functional characterisation of this gene. It purified the mature
peptide, measured bactericidal activity against four Gram-negative species with a dose
response and MICs, imaged the killed bacteria by SEM, showed no activity against two
Gram-positive species or yeast, and protected mice against a lethal *E. coli* O157:H7
challenge.

**GOA contains zero annotations citing that paper, for any gene in any organism.** Positive
control from the same endpoint: `PMID:19199708` returns 396. So the endpoint works and the
absence is real.

The family is uncurated in the same way. PANTHER `PTHR37864` holds 153 proteins across 426
taxa; three are reviewed. The mouse orthologue `Q3V2D2` (Gm94, 93 aa) carries MGI's
**ND — "no biological data available"** root-term annotation in all three aspects
(`GO:0003674`, `GO:0008150`, `GO:0005575`, GO_REF:0000015), *despite the same paper reporting
that Gm94 is itself bactericidal and protective in vivo* [PMID:33804835 "our data shows that
Gm94 (mouse C5orf46) also exhibits the similar antibacterial ability"]. Bovine `Q3T146` has
one IEA localisation row. So across the whole reviewed family there is not one functional
annotation.

## The sibling molecule WAS curated — which is the strongest form of the request

The coverage gap looked at first like GO simply not covering this class. It is not that, and
finding out inverted the framing.

The same laboratory had previously characterised **C10orf99 as AP-57**, "Antimicrobial Peptide
with 57 amino acid residues", and the AP-64 paper cites that work as its own predecessor
[PMID:33804835 "Previously, we identified an uncharacterized peptide, chromosome 10 open reading
frame 99 (C10orf99), as a type of human AMP, which was termed AP-57 [11]."]. **That gene was
curated.** `Q6UWK7` (GPR15LG) carries four IDA rows from `PMID:25585381`, including
`GO:0050830` defense response to Gram-positive bacterium and `GO:0050832` defense response to
fungus, all assigned by UniProt — and UniProt took *"Antimicrobial peptide with 57 amino acid
residues"* into the entry as an alternative name.

And the two peptides are near-mirror images, so the comparison is sharp rather than loose:
AP-57 is basic (net +14, pI 11.28) with four cysteines and kills Gram-positives and a fungus
[PMID:25585381 "AP-57 is a short basic amphiphilic peptide with four cysteines and a net charge
+14 (MW = 6.52, PI = 11.28)"]; AP-64 is anionic (pI 4.54) with no cysteines and kills
Gram-negatives while leaving Gram-positives and yeast alone. `GO:0050829` is therefore the
exact counterpart of the `GO:0050830` the sibling already holds. That converts "please curate
this" into "you applied this treatment to the sibling from an equivalent paper and missed this
one", which is a much better-founded request.

**An accession error of mine that nearly inverted the conclusion.** I first looked C10orf99 up
as `Q6UWT2` — reasoning from accession proximity to `Q6UWT4`, which is not reasoning at all.
`Q6UWT2` is **adropin (ENHO)**, 76 aa, an entirely different protein, and its record (7
annotations, none antibacterial) would have supported precisely the wrong conclusion: that GO
does not curate this class. The correct accession is `Q6UWK7`, confirmed by `primaryAccession`
and by the entry's gene synonyms including `C10orf99`. Same failure shape as the merged-accession
trap the analysis script guards against, arrived at from a different direction — a plausible
accession that resolves to a real, reviewed, wrong protein.

## Cross-review consistency of the 14 protein-binding verdicts

Checked rather than assumed, because "three independent reviews gave one identical row three
different answers" is a known campaign defect. Across the 1,769 merged human reviews on `main`,
excluding this one, **803** `GO:0005515` rows cite HuRI (`PMID:32296183`):

| action | rows | share | genes |
|---|---|---|---|
| `MARK_AS_OVER_ANNOTATED` | 554 | 69% | 465 |
| `KEEP_AS_NON_CORE` | 142 | 18% | 142 |
| `REMOVE` | 87 | 11% | 85 |
| `MODIFY` | 12 | 1% | 9 |
| `ACCEPT` | 6 | 1% | 6 |
| `UNDECIDED` / `PENDING` | 1 / 1 | — | 2 |

The 14 `MARK_AS_OVER_ANNOTATED` verdicts here follow the dominant convention. Note this is a
convention check, not an argument: it would not justify the verdict on its own, and it is
recorded separately from the evidence for exactly that reason.

## Two brief hypotheses tested, both non-confirmations

Recorded so the next reviewer knows the checks were run rather than skipped.

1. **Fold/domain name becomes an activity.** Did not happen, and cannot: `IPR027950`
   (DUF4576, Pfam `PF15144`) is the gene's only InterPro signature and has **no interpro2go
   mapping at all**. Verified against all 30,122 `InterPro:` lines of the current
   `external2go/interpro2go`, with `IPR001879` as a positive control proving the lookup
   works. Nor is there a `GO_REF:0000117` (ARBA) or `GO_REF:0000120` (combinatorial) row, so
   none of the three non-PAINT routes touches this gene. The gene's one IEA comes from
   `GO_REF:0000044` (UniProt SubCell), whose liveness was confirmed at 139,714 human
   annotations against `GO_REF:0000043` at 0 — the retired keyword route.
2. **Model organism lacks the orthologue** (the ADIRF pattern). It does not. Mouse Gm94 is a
   genuine orthologue in the same PANTHER subfamily and was assayed directly alongside the
   human peptide. So the heterologous-expression caveat that reframes ADIRF's whole record
   does not apply, and ISS/ISO support is possible in principle — it simply has not been
   made, because the source annotation does not exist either.

## The molecule identity question, answered before using the paper

The standing hazard with a named peptide (`AP-64`) derived from a larger ORF is that
pharmacology on a synthetic fragment gets attributed to the parent gene — the ADNP/NAPVSIPQ
pattern. Here it is not a fragment. Recomputing from UniProt's annotated `CHAIN 24..87`:
**64 residues, 7.22 kDa, pI 4.54, zero cysteines**, against the paper's stated
*"antimicrobial peptide with 64 amino acid residues (AP-64)"*, `MW = 7.2`, `PI = 4.54` and
*"AP-64 contains no cysteines"*. Positive control on the instrument: the same routine
reproduces UniProt's stated 9693 Da for the 87-residue precursor. So AP-64 **is** this gene's
physiological mature secreted product, and the paper's evidence is evidence about this gene.

The construct was recombinant, made in *E. coli* as a SUMO fusion and cleaved. Worth noting
because the paper's own control is informative: *"SUMO-AP-64 was expressed in a soluble form
but failed to inhibit the growth of DH5α cells. After removal of the SUMO tag, AP-64
exhibited strong antibacterial effects."* An N-terminal blocking group abolishes the activity,
which argues the activity is a property of the free peptide rather than of the preparation.

## Sufficiency versus requirement — which one the evidence gives

Every functional experiment on this gene is **exogenous addition of purified peptide**:

- *in vitro* — peptide added to bacterial cultures, 0.1–10 µM, with MICs;
- *in vivo* — peptide injected intraperitoneally at 500 µg/kg 30 min after a lethal
  bacterial challenge, raising 24 h survival from 20% to 90%;
- *cytotoxicity* — peptide added to cultured mammalian cells.

All three establish **sufficiency**: the peptide can kill Gram-negative bacteria and can
protect an animal when administered. **Nothing establishes requirement.** No knockout,
knockdown or patient loss-of-function has ever been challenged with a pathogen in either
species, so no claim that endogenous C5orf46 is *needed* for antibacterial defence is
available. GO's evidence codes do not distinguish the two, so the proposed rows say which
they have in their `reason`, and the gap is filed under `knowledge_gaps`.

The one loss-of-function experiment that exists is unrelated to bacteria: siRNA knockdown in
two renal-carcinoma lines reduces proliferation and migration and raises apoptosis
[PMID:35504177]. That is a cancer-cell-line dependency, in a paper whose own title says
*"Preliminary study"*, with no mechanism and no rescue. It is deliberately **not** turned
into a proliferation or apoptosis GO term — the brief's phenotype-read-as-function trap. It
is recorded in `knowledge_gaps` and `suggested_experiments` instead.

## Where I had to correct the affinage record

The record passed its gates (`gates_passed: True`, `faith_pct: 100.0`, 3 citations, all
numeric PMIDs, no bioRxiv-in-a-PMID-field). Retraction/erratum status of all seven PMIDs
used here is clean by two independent routes — PubMed `PublicationType` plus
`CommentsCorrections/RefType` on each record, and Crossref `relation`/`update-to`/`updated-by`
on each DOI (all HTTP 200; two records returned non-empty `relation` keys, so the field is
genuinely being read).

Two problems with the record all the same, neither of them a fabricated quote:

1. **A framing that implies tumour selectivity the paper contradicts.** The record reports
   *"AP-64 (C5ORF46 protein product) exhibits cytotoxic effects against human T-cell lymphoma
   Jurkat and B-cell lymphoma Raji cells"* as a standalone finding. The paper's own next
   sentence is *"Subsequently, we tested the toxicity of the peptides to T cells, Hacat, and
   MEF cells. Our data showed that these cells were susceptible to the peptide treatment."*
   Normal T cells, keratinocytes and mouse embryonic fibroblasts are killed too. Presented
   without that, the finding reads as selective anti-tumour activity; it is general cytotoxicity
   at 10 µM. No GO term is proposed from it, and the qualification is stated wherever the
   cytotoxicity is mentioned. This is the "read the whole paragraph around the sentence you
   are about to quote" failure, caught on the affinage record rather than on my own quote.
2. **The narrative asserts a mechanism the paper declines to settle.** *"functions as a
   secreted antimicrobial peptide"* is fine; but the record's overall shape invites a
   membrane-permeabilisation reading. The paper offers two alternatives and settles neither:
   *"its action might be related to cell envelope damage"* and *"The multiplication of growth
   might also hint at an intracellular target of the peptide."* So **no molecular function
   term is proposed**, and no pore-forming or membrane-disrupting activity is claimed. The
   α-helix is a PSIPRED prediction with CD support for helical content — that a helix exists,
   not that it forms a pore. A small protein invites structural over-reading and this is
   where it would have happened.

Recall, separately from precision: the record returned **3** of the papers, and missed the
three GOA interaction references entirely. It also did not surface `PMID:19199708`, the
reference behind an existing annotation. `gates_passed: True` is a floor on precision and
says nothing about recall.

## The 14 protein-binding rows

Full analysis in `C5orf46-bioinformatics/RESULTS.md`. The short version:

- 14 rows, 13 distinct partners; the duplicate is TMBIM6, from BioPlex 2.0 and its 3.0
  expansion — one `anti tag coip` method in two releases, not two independent assays.
- 12 partners come from a single publication, HuRI (`PMID:32296183`), logged under **three
  names of the same yeast two-hybrid screen** (`two hybrid array`, `two hybrid prey pooling
  approach`, `validated two hybrid`). That is why UniProt reads `NbExp=3` for twelve partners
  and `NbExp=5` for SLC30A2, where two of the three sub-methods are logged twice. Third
  instance of this pattern in the campaign, with a new shape (five records for one screen).
  All share one MI-score, 0.56.
- **The partner set has exactly one shared property: hydrophobicity.** 11 of 13 are integral
  membrane proteins (44 annotated TM segments across the set); the 2 that are not are SGTA
  and SGTB, the two human members of the SGT family of TPR co-chaperones. **The
  hydrophobic-client function is curated for SGTA only** — [UniProt SGTA `FUNCTION`: *"binding
  more rapidly the transmembrane domain of newly synthesized proteins"*] — while SGTB's whole
  `FUNCTION` is *"Co-chaperone that binds directly to HSC70 and HSP70 and regulates their
  ATPase activity"*, with no hydrophobic-client claim. SGTB is SGTA's paralogue, 55.6%
  identical over the shorter sequence with the same TPR array, so its presence is consistent
  with the hydrophobicity reading without being curated evidence for it. I first wrote this as
  a property of both and had to correct it on five surfaces; the fix is recorded below because
  the overstated version is the more persuasive one and would have gone unchallenged. C5orf46 was the **bait** in 29 of 41 records, and the bait is the
  full ORF whose most hydrophobic 19-residue window (KD-19 **+2.51**) is the uncleaved signal
  peptide — more hydrophobic than anything in the mature chain (**+1.08**).
- `Q0VAB0`, annotated as TBXA2R, is an **unreviewed 259-aa TrEMBL clone**; canonical TBXA2R is
  `P21731`, reviewed, 343 aa. The named partner is not the canonical protein.
- Promiscuity, reported with its exceptions rather than smoothed: 12 of 13 partners exceed the
  subject's 14 distinct IntAct partners, up to AQP6 at 382 — but PEX12 at 37 is only 2.6× and
  the truncated TBXA2R clone at 13 is **below** the subject.

Verdict per partner rather than per gene, as the brief requires — but the evidence is uniform
across the twelve HuRI rows, so they resolve the same way: `MARK_AS_OVER_ANNOTATED`, not
`REMOVE`. These are real database records from a real screen; what they are not is replicated,
orthogonally validated, or informative about function. `REMOVE` would need a positive argument
that the interaction is false, and I do not have one — the honest statement is that the set
looks like the screen's design rather than the peptide's biology.

## Checks that came back negative, recorded as such

- **Reference-projection test on `PMID:19199708`** (the exosome HDA): fully paginated, **396
  annotations over 396 distinct entities**, every one to `GO:0070062` alone, all HDA, all
  assigned by UniProt. One entity, one annotation, one localisation term, and **no functional
  or phenotype term anywhere in the reference** — so this is a proteomic inventory, not the
  ACTR8-style complex projection where a phenotype spreads across a set. The check was run and
  it is clean.
- **HuRI and BioPlex projection tests are uninformative** at 85,343 / 9,514 / 3,731
  annotations. Stated rather than substituted with a first-page count.
- **Logical-opposite citation cross-product** (the ADIPOQ check): not applicable — the gene has
  three distinct terms and no regulation terms at all, so no positive/negative pair exists to
  intersect.
- **Locus/transcript confusion:** no antisense or overlapping-transcript gene shares this
  locus's annotations; all 16 GOA rows are on Q6UWT4 itself, and the two annotated isoforms
  differ only by the C-terminal 15 residues (`VSP_031115`), which no cited experiment
  distinguishes.
- **Self-inclusion and non-protein entities** in the IntAct partner set: none, asserted.

## What the extracellular localisation rests on

`GO:0005576` arrives by `IEA` from `GO_REF:0000044` with `UniProtKB-SubCell:SL-0243`, i.e. from
UniProt's `SUBCELLULAR LOCATION: Secreted {ECO:0000305}` — a curator inference from the
predicted signal peptide (`SIGNAL 1..23 /evidence="ECO:0000255"`, also a prediction). On its own
that is a prediction chain, and would deserve caution.

But the conclusion is independently measured three ways, none of which is in the annotation's
own evidence path: the protein is identified in human **plasma** by mass spectrometry
[PMID:31308252 abstract, "we identify C5ORF46 as a previously uncharacterized human plasma
protein" — abstract-only cache, so nothing beyond the abstract is claimed]; it is catalogued in
the **parotid saliva exosome** fraction [PMID:19199708, the `GO:0070062` HDA row]; and UniProt
records `PE 1: Evidence at protein level` with a `Proteomics identification` keyword. HGNC's
alias name for the gene is literally *skin and saliva secreted protein 1*, and HPA calls the
expression `Group enriched (blood vessel, salivary gland, skin)`. So both CC rows are accepted
as core, with the caveat that the *route* by which `GO:0005576` was asserted is weaker than the
conclusion it reached.

Note the tissue claim in `PMID:33804835` — *"AP-64 is mainly expressed in the salivary glands
and skin"* — is derived from a database, not measured there; the paper says so in its own
limitations: *"the mRNA expression of AP-64 in the skin and salivary gland was discovered using
the TCGA database"*. It is used here only as agreement with HPA and the HGNC alias, never as
primary evidence.

## Review round 1: the exosome row was accepted as a core location, and should not have been

The blocking point was right, and it found a hole in a guard I had written for exactly this
class of defect.

`GO:0070062` was `ACCEPT` and appeared in `core_functions.locations`. The evidence is a single
HDA detection in one shotgun-proteomics inventory, and **the row's own summary conceded it was
"not strong evidence on its own"** while the structured field asserted it as a core location.
That is precisely the hedge-versus-structured-field defect my `check_document` sweep exists to
catch — and it missed, because the sweep covered only `molecular_function`,
`contributes_to_molecular_function`, `substrates` and `in_complex`. **`locations` was outside
its scope.** A guard scoped to the failure I had thought of, run against a document with a
different one.

The substantive argument is the reviewer's, and it is the better one: `core_functions.locations`
asserts a compartment of *action*, and nothing shows the peptide acting in an exosome lumen.
Every activity measurement used free peptide added to a culture or injected into an animal, and
the paper's own SUMO-fusion control — activity abolished by an N-terminal tag and restored on
cleavage — argues the functional species is free soluble peptide, not vesicle cargo.

I verified the convention numbers before conceding rather than after. The reviewer said
`GO:0070062` gets `KEEP_AS_NON_CORE` 342×, `MARK_AS_OVER_ANNOTATED` 158× and `ACCEPT` 43× across
merged human reviews; I measure **346 / 161 / 42** excluding this gene, so the claim holds.
**And there is a sharper version of it that the reviewer did not use:** `GO:0070062` appears in
`core_functions.locations` in only **2 of 1,769** merged reviews — GAPDH and PDCD6IP, both with
genuine exosome biology. That is a much stronger statement than the row-action ratio, and it
settled the question.

Fixes: the row is `KEEP_AS_NON_CORE`, it is out of `core_functions.locations` (leaving
`GO:0005576` alone), the summary no longer calls it core or "more informative", the
`core_function` description states positively that the core location is the extracellular region
and not the exosome, and the guard now has a **second hedge sweep** — any term whose row is
`KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED`, `REMOVE` or `UNDECIDED` must not appear in
`locations`, `anatomical_locations` or `directly_involved_in`. Two new break-tests run it against
the shape that actually shipped.

One of the existing break-tests then failed, for the right reason: `drop_cf_term` removed
`GO:0070062` from `core_functions.locations` to test direction 1, and once that term was
legitimately gone the mutation became a **silent no-op**, so the guard correctly did not fire and
the break-test reported it as broken. Fixed by dropping whatever the first location actually is
and asserting the mutation changed something. Third time today that "assert the target is present
before mutating" earned its place.

### The sharpest item: my cache narrowing removed the evidence for the claim the same commit made

The reviewer's formulation is the one to keep: *"The claim is right; the evidence for it left with
the projection."*

Commit `98c086d` corrected the SGTA-versus-SGTB claim — the hydrophobic-client function is curated
for SGTA only — and the same body of work had narrowed the cached UniProt projection to the fields
the analysis read. `FUNCTION` was not among them. So the correction was right, was stated in
fourteen places, and **could not be verified from the committed tree at all**: only 1 of 18 cached
UniProt records retained a `FUNCTION` comment, and neither SGT entry was that one.

This is a failure mode worth naming, because it is the inverse of the usual one. The usual defect
is a claim without evidence. Here the evidence existed, was correct, was checked interactively —
and was then removed by a *separate, individually justified* optimisation whose interaction with
the claim nobody looked for. Narrowing a projection is a reduction of a set, and this brief's own
`no-silent-caps` rule says every stage that reduces a set must state what it dropped. A cache
projection is such a stage, and I did not apply the rule to it.

Fixes: `cc_function` and `cc_similarity` are retained in the projection (cache 588K → 604K, so the
cost was nothing), and the asymmetry is now **computed** as check H rather than asserted — it scans
both entries' `FUNCTION` comments for hydrophobic-client cues and their `SIMILARITY` statements for
SGT-family membership. Four directions are break-tested, and the first of them **reproduces the
defect that shipped**: stripping `FUNCTION` from the cache must raise "no FUNCTION comment cached"
rather than passing quietly. The other three are SGTB gaining the role, SGTA losing it, and the
family statement breaking — because a guard that only checks the direction you happened to fear is
the guard that fails next time.

Result from the cache: SGTA's `FUNCTION` contains both `hydrophobic` and `transmembrane`, SGTB's
contains neither, and both carry `Belongs to the SGT family`.

**Generalisable rule: when you narrow a cached projection, list what each committed claim depends
on and confirm none of it is in the dropped set.** The check that enforces it here is the one that
fails loudly when the field is absent, rather than a comment saying which fields matter.

### The three non-blocking suggestions

1. **The dermcidin precedent was asserted, not queried — and querying it weakened it.** Every
   other quantitative claim here has a cached query behind it; this one had an interactive lookup
   that no reader of the tree could check. It is now check **G**, and the result is not what I
   wrote: dermcidin holds `GO:0031640` by **InterPro2GO IEA (`GO_REF:0000002`)**, not by a
   curator's experimental call. Its experimental defence rows are `GO:0042742` and `GO:0140367`,
   both IDA. So it is precedent that the term is *used* for this class, not that it was assigned
   from an experiment, and the prose now says so. The reviewer's observation that the
   non-redundancy argument does not depend on it is correct — that rests on the closure fetch.
   The same check covers the C10orf99 precedent, which **is** IDA and is unaffected, and it
   asserts the subject holds none of the six defence/killing terms, because if it did the two
   `NEW` proposals would not be new.
2. **Shared boilerplate.** The two long shared blocks are collapsed into one compressed
   `SET_CONTEXT`: the duplicated trailing text falls from 3,066 to 1,946 characters per row
   (42,924 → 27,244 across the fourteen) and the file from 1,752 to 1,638 lines. I kept per-row
   self-containment deliberately, and one part of the stated rationale does not apply: a future
   correction does **not** have to be made in fourteen places, because the text is a single
   shared constant. Two corrections today — the bait-count scoping and the SGTA/SGTB
   qualification — were each made once and landed in all fourteen emitted sites, verified by a
   whitespace-normalised sweep.
3. **The body-fluid discriminator now lives in the YAML**, not only here. Both `GO:0019731` and
   `GO:0061844` require the response to occur in a body fluid, and every assay was in culture
   medium or by injection; without that sentence, declining them while accepting `GO:0050829`
   from the same experiments reads as inconsistent.
4. On the fourth suggestion, about quote line-wrapping: the distinction is deliberate rather
   than a lapse, and is now stated. The "single physical line" rule applies **only to `file:`
   quotes**, because the repo's reference validator skips those entirely, so a broken one passes
   silently and the quote is the only thing standing between prose and fabrication. `PMID:`
   quotes *are* validated, with whitespace normalisation, so a quote spanning a wrapped line in a
   cached abstract is checked and safe. All 62 `file:` quotes here are single physical lines and
   were additionally hand-verified with `grep -F`.

## Review round 2: implicit string concatenation, three times, and the guard that ends it

The remaining item was one word — `"…of the body surfaces.surfaces. The core location is…"` in the
curator-facing `core_functions` description. The cause is Python's implicit concatenation of
adjacent string literals: correcting the exosome call, I added the new sentence as a **fresh
literal without removing the `"surfaces."` it was meant to extend**, so the two joined and doubled
the word.

It reached the shipped artifact because it is **invisible in the builder source** — two adjacent
string literals look exactly like two lines of one paragraph. This was the third instance of the
class in one PR: the dangling "That role" antecedent, this one, and one more that nobody had
reported.

**Scripting the check found the unreported one.** Re-reading the tree caught `surfaces.surfaces`;
a sweep over the *assembled* prose then found a second, in `suggested_questions[0]`: *"…there is
none anywhere in the family.and there is none anywhere in the family. What makes…"*. Same cause,
same edit session, and reading had missed it because it sits 1,400 characters into a long
question. That is the campaign's "anything you can compute, compute — then compare it against
what you wrote", earning its place again: reading found one, computing found two.

The sweep is now committed in `check_document`, and getting it right took three attempts, each
instructive:

1. **A window-based whitelist let a false positive through.** `core_functions.locations` trips a
   naive "period followed by lower case" rule, and my ±12-character window clipped the leading
   `core_`, so the allowance never matched. Replaced with **exact-token masking**, which cannot
   be defeated that way. A generic "dotted lowercase word" allowance is deliberately *not* used —
   it would whitelist `surfaces.surfaces`, which is the defect itself. If a new identifier appears
   in prose the check fires and the token is added: a loud failure, which is the right default.
2. **A fixture below the threshold made a direction silently untested.** My repeated-word
   break-test used `"is is"`, and the regex requires 3+ characters, so it never fired — the guard
   looked broken when the fixture was. Fixed to `"peptide peptide"`, and a companion assertion now
   documents the threshold by checking that a two-character repeat is *not* flagged, so the limit
   is stated in code rather than discovered later.
3. **Both defects that actually shipped are now fixtures.** `shipped_surfaces` and
   `shipped_clause` reproduce them by mutating the real document, each asserting its anchor is
   present first so the mutation cannot become a no-op. Running a guard against the defect that
   shipped is a stronger claim than any synthetic case.

The offsets are asserted to survive masking (`len(scan) == len(s)`), so the excerpt a problem
reports still points at the right place in the unmasked text.

**Generalisable rule: when you extend a wrapped string constant, delete the fragment you are
extending — and check the assembled output, not the source, because implicit concatenation is
invisible where you are typing.**

## Terms proposed, and terms deliberately declined

Proposed (both as `NEW` rows, `IDA`, from `PMID:33804835`):

- `GO:0050829 defense response to Gram-negative bacterium`. Chosen over its parent
  `GO:0042742` because the Gram-negative/Gram-positive distinction was *measured in both
  arms*: four Gram-negative species killed, *S. aureus* and *L. monocytogenes* not. Ancestry
  verified — `GO:0042742` is in `GO:0050829`'s `is_a`/`part_of` closure, so the specific term
  asserts the general one and nothing is lost.
- `GO:0031640 killing of cells of another organism`. Both closures were fetched:
  `GO:0031640` is **not** a descendant of `GO:0042742` — it sits under `GO:0001906 cell
  killing` — so this is not redundant with the row above but a second, non-overlapping
  statement about the same experiment. Dermcidin, the anionic cysteine-free comparator the
  paper itself names, holds it.

Declined, each for a stated reason:

- `GO:0061844 antimicrobial humoral immune response mediated by antimicrobial peptide` and
  `GO:0019731 antibacterial humoral response` — both require an **immune response in a body
  fluid**. The peptide is in plasma and in saliva, and it kills bacteria in a tube, but no
  experiment shows the endogenous peptide mounting a response in either fluid. Requirement is
  not shown; these would convert a sufficiency result into an organism-level process claim.
- `GO:0140367 antibacterial innate immune response` — its definition requires components that
  *"directly recognize components of potential pathogens"*. No target is identified; the paper
  explicitly leaves envelope damage and an intracellular target open.
- Any **molecular function**. There is no candidate: the mechanism is unresolved by the
  authors' own statement, and inventing a pore-forming or membrane-disrupting activity from a
  predicted helix is precisely the structural over-reading to avoid. `core_functions` therefore
  carries a process and a location and no MF, and the MF gap is stated in `knowledge_gaps`.
- Any term from `PMID:35504177` — see the sufficiency/requirement section above.
- Any term for the cytotoxicity — it is not tumour-selective (normal T cells, HaCaT and MEF
  are killed too), so it reads as a general property of an amphipathic peptide at 10 µM rather
  than a biological function.

## Process notes

- One break-test of my own was defective in a way worth recording: the partner-set membership
  mutation dropped `real[-1]`, which happens to be `P55061` — a **duplicate**, since that
  accession is on two GOA rows. The *set* was unchanged, the guard correctly did not fire, and
  the break-test reported the guard as broken. The mutation has to be as fine as the claim.
  Replaced with three mutations including a **length-preserving substitution**, which a
  cardinality check cannot see, and the script now prints that fact so the membership
  assertion is demonstrably load-bearing rather than decorative.
- A second self-inflicted one: an edit-verification assertion of the form
  `assert new in t and old not in t` **cannot pass** when `old` is a prefix of `new`. The edit
  had landed; the check was wrong. Verify by outcome (is the new text present exactly once?),
  not by the absence of a string you deliberately extended.
- The IntAct truncation guard caught a real defect in my own first version: a single request
  with `pageSize=1000` silently dropped 32 of AQP6's 1032 records. The `--self-test` now
  re-runs that exact call and requires it to raise, which is a stronger claim than a synthetic
  fixture.
- A number that was true and wrongly scoped. I first wrote "C5orf46 was the bait in 29 of its
  41 IntAct records" and used it to argue that the two-hybrid bait was the full ORF. The 29 is
  correct but it pools two assay types: **26 of the 38 HuRI records** (the other twelve are
  the same interactions re-logged as `validated two hybrid` with both partners as
  `neutral component`) plus all **3 BioPlex** records. The argument only concerns the yeast
  two-hybrid construct, so the scoped 26/38 is the number that belongs in it. The claim lived
  in a single shared prose constant, so one rebuild corrected all fourteen emitted sites at
  once — which is the single-sourcing that the campaign's "fixed in N places, landed in N−1"
  recurrence argues for, and the reason the surface sweep found zero stale instances rather
  than one.
- Checking the bait roles also produced a discrimination worth keeping: C5orf46 is the tagged
  **bait** in both BioPlex records, so the TMBIM6 row is a pull-down of an over-expressed
  signal-peptide protein recovering an abundant resident of the ER it genuinely transits. That
  makes it the one row in the set that is topologically coherent — and equally, the kind of
  encounter that co-residence produces without a functional relationship. It is stated on that
  row rather than flattened into the shared argument.
- The consistency sweep (banned commentary in `description`, the hedge sweep over
  `molecular_function`/`substrates`/`in_complex`, summary-opener agreement with `action`, the
  ACCEPT/NEW-versus-`core_functions` correspondence in **both** directions, and reference
  declaration) began life as a script in `/tmp`. It is now `check_document()` inside
  `build_review.py`, with one break-test per advertised direction plus a vacuity test that an
  empty document fails loudly. A check written in a scratch file gets described as enforcement
  by the same commit that throws it away.
- One of my own verification assertions was itself the bug: after an edit I asserted
  `new in text and old not in text`, which can never pass when `old` is a prefix of `new`. The
  edit had landed correctly. Verify by outcome — is the new text present, exactly once? — not
  by the absence of a string you deliberately extended.
- **The overstatement I nearly shipped, and how it was caught.** I wrote that SGTA *and* SGTB
  both have "binding exposed hydrophobic transmembrane segments" as their curated function.
  Only SGTA does; SGTB's entire UniProt `FUNCTION` is HSC70/HSP70 ATPase regulation. Nothing
  automated could catch it — the SGTA quote I cited was verbatim and correct, and the sentence
  it supported silently extended the claim to a second protein. It was found only by going
  back to fetch SGTB's own record rather than reasoning from the pair. The corrected version
  is weaker and still sufficient: the argument now rests on SGTA specifically, with SGTB as
  family-and-architecture corroboration (55.6% identity, same TPR array) rather than as a
  second curated instance.
- **The stale-phrase sweep needed context reading, exactly as predicted.** Its final run
  reported four hits: `Q6UWT2` in `RESULTS.md` and in the builder, and "That role is curated
  for SGTA only" and "bait in 29 of" in this file. All four are **the retractions narrating
  themselves** — the accession-caution paragraph and the two process-findings bullets above.
  Each was confirmed in context rather than counted, and one of them (`Q6UWT2`) only matched
  after whitespace normalisation because the sentence wraps. A phrase count is not a defect;
  the check has to end in reading.
- **Two overlapping string edits produced a dangling antecedent.** Correcting the above, I
  applied two replacements whose anchors overlapped inside one prose constant. Both landed, and
  the result read *"the small glutamine-rich TPR co-chaperones of the SGT family. That role is
  curated for SGTA only"* — where "that role" no longer had an antecedent, because the second
  edit had deleted the phrase the first one left behind. Assertions on both replacements passed
  in isolation. The fix was to **rewrite the whole constant once** rather than patch it twice,
  which is the campaign's "at three rounds, change the shape" rule arriving early: two
  overlapping edits to one paragraph are already one too many.
