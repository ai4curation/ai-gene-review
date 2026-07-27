# AFF3 (P51826) — review notes

Reviewer journal for the PAINT + affinage campaign. Third and last member of the AFF
family to be reviewed here, after AFF4 (PR #2349) and AFF1 (PR #2348), both of which merged
to `main` while this review was being written.

## What the gene is

AFF3 / LAF4 is a 1226-residue, almost entirely intrinsically disordered nuclear protein
of the AF4/FMR2 (ALF) family — `PTHR10528`, subfamily `PTHR10528:SF16`
[file:human/AFF3/AFF3-uniprot.txt "DR   PANTHER; PTHR10528:SF16; AF4_FMR2 FAMILY MEMBER 3; 1."].
It is the scaffolding subunit of **SEC-L3**, one of the four paralogous super elongation
complexes: PMID:22547686 reports
"biochemical isolation of SEC-like 2 (SEC-L2) and SEC-like 3 (SEC-L3) containing AFF2 and
AFF3 in association with P-TEFb, ENL/MLLT1, and AF9/MLLT3", and
"The SEC family members demonstrate high levels of polymerase II (Pol II) C-terminal domain
kinase activity; however, only SEC is required for the proper induction of the HSP70 gene
upon stress". Note the negative in that same sentence — AFF3/SEC-L3 is *not*
interchangeable with AFF4/SEC.

Where AFF3 differs from AFF1/AFF4 is in how it reaches chromatin. It is **recruited by
sequence-specific zinc-finger proteins**: PMID:28180295 shows
"ZFP281 recruits AFF3 to the Meg3 enhancer within the imprinted Dlk1-Dio3 locus, thus
regulating the allele-specific expression of the Meg3 polycistron" (mouse ES cells) and
concludes "different zinc finger proteins can recruit AFF3 to different regulatory elements
and differentially regulate the function of AFF3 in a context-dependent manner" (ZFP57 at
the IG-DMR). In human cells it binds a methylated CpG island directly:
PMID:30535390 (HEK293T + IMR-90)
"Quantitative PCR after chromatin immunoprecipitation (ChIP-qPCR) demonstrates that AFF3 is
associated with the XIST DMR in both IMR-90 and HEK293T", and
"Knockdown of AFF3 leads to de-repression of the inactive allele of XIST in terminally
differentiated cells".

Its own DNA binding is **not sequence-specific**: PMID:8555498
"In vitro-translated LAF-4 was able to bind strongly to double-stranded DNA cellulose",
and the same paper localises it — "Antibodies to LAF-4 showed it to be a nuclear protein
that showed an uneven, granular immunofluorescence pattern".

## The single most useful measurement: WITH/FROM resolution

`AFF3-bioinformatics/resolve_withfrom.py` (output `withfrom_resolution.json`) resolves every
token on all five IBA rows and then asks what evidence each donor itself carries for the
propagated term. Results:

| token | resolves to | reviewed | own experimental evidence for the propagated term |
|---|---|---|---|
| `MGI:MGI:106927` | **P51827 mouse Aff3 — the true orthologue** | Swiss-Prot | IDA + IMP `GO:0006355` (PMID:25162227) |
| `MGI:MGI:1100819` | O88573 mouse Aff1 (paralogue) | Swiss-Prot | IDA `GO:0045893` (positive) |
| `MGI:MGI:1202294` | O55112 mouse Aff2 (paralogue) | Swiss-Prot | IMP `GO:0007611` (PMID:11923441) |
| `FB:FBgn0041111` | Q9VQI9 *Drosophila* **lilli** (single fly AFF co-orthologue) | Swiss-Prot | IMP `GO:0003712`; IMP `GO:0007611`; IPI `GO:0032783`; IMP/IGI `GO:0006355` |
| `UniProtKB:P51825` | **P51826's paralogue, human AFF1** | Swiss-Prot | EXP `GO:0006354` (PMID:22547686) |
| `PANTHER:PTN000829417` | PANTHER tree node — not a protein | n/a | unqueryable |

All MGI/FB tokens returned **multiple** UniProt hits (10, 3, 3); the script reports every
candidate and queries the Swiss-Prot one, and it prints reviewed status using
`entryType.startswith("UniProtKB reviewed")` because `"reviewed" in entryType` also matches
*un*reviewed.

**The brief's question 3, resolved.** AFF1 and AFF4 both carry a byte-identical
`PANTHER:PTN000829417|UniProtKB:P51825` WITH/FROM on `GO:0006354`, self-referential on AFF1
and paralogue-derived on AFF4. AFF3 has the **same** field, and on AFF3 it is
**paralogue-derived** — P51825 is AFF1, P51826 is AFF3. So the same six bytes now carry
three different evidential meanings across three reviews. Recorded for the family write-up.

## The finding worth reporting upstream: PMID:22547686 annotated the wrong paralogue

`reference_projection.py` queries QuickGO by *reference* and counts distinct gene products
(entities, not annotations; pagination asserted against `len(results)`).

`PMID:22547686` — the paper whose headline result is the isolation of the **AFF3**-containing
SEC-L3 — has produced **exactly one annotation in the whole of GOA: `GO:0006354` EXP on
`UniProtKB:P51825` (AFF1)**, the paralogue the paper explicitly contrasts with SEC-L2/L3.
AFF3 got nothing directly and then received the term back second-hand, as an IBA whose
WITH/FROM points at AFF1.

This is the same shape as AFF4's sharpest datum (PMID:20159561, titled for AFF4, produced one
annotation and it was on AFF1). Two independent instances in one family, both with AFF1 as the
recipient. Filed as a `suggested_question`.

Same script, negative results worth recording:

- `PMID:20444755` → 1 annotation, 1 entity. `PMID:8555498` → 2 annotations, 2 entities
  (human + mouse, same term). `PMID:18616733` → 2 annotations, 2 entities. **No
  complex-projection pattern anywhere** (contrast ACTR8's ComplexPortal case).
- `PMID:18616733`'s split is *coherent* curation, not a defect: **IEP** on mouse P51827 (the
  embryo in-situ) and **IMP** on human P51826 (the patient deletion). Two evidence codes for
  two different observations in one paper, assigned to the right species each time.

## `GO:0034612 response to tumor necrosis factor` — REMOVE

The one clear error, and it is exactly the failure mode a disease gene invites: a clinical
drug-response association read as a cellular response-to-stimulus.

`PMID:20444755` is a pharmacogenetic study.
"Eighteen single nucleotide polymorphisms (SNPs) mapping to 11 genetic loci were genotyped in
1012 patients with RA receiving treatment with etanercept, infliximab or adalimumab", with the
outcome "the absolute change in 28 joint count disease activity score (DAS28) between baseline
and 6-month follow-up". The result is that
"SNPs mapping to AFF3 and CD226 had a statistically significant association with the response
to anti-TNF treatment".

Three independent grounds:

1. **Definitional.** `GO:0034612` requires "a change in state or activity of a cell or an
   organism ... as a result of a tumor necrosis factor stimulus". The study applies TNF
   **blockade** to patients. The direction of the perturbation is the opposite of the term's,
   and there is no TNF stimulus anywhere in the paper.
2. **Evidence code.** IMP requires a mutant phenotype. A common tag SNP associated with a
   6-month DAS28 change is neither a mutant nor a phenotype of the gene product.
3. **No assay.** The paper contains no cellular or biochemical experiment on AFF3 at all;
   it is genotyping plus multivariate linear regression.

It has **propagated**: mouse Aff3 (P51827) holds `GO:0034612` only by `ISO GO_REF:0000119`
`with UniProtKB:P51826` — i.e. from this human row. Removing the human row retracts it from
both species, which is why it is worth acting on rather than leaving.

Erratum status, per the campaign's correction rule: PubMed's record for `PMID:20444755` carries
an `ErratumIn` reference to *Ann Rheum Dis. 2011 Aug;70(8):1519* whose **PubMed id is null**
(see `corrections.json`, produced by `corrections_check.py`). It is not resolvable: Crossref
returns empty `relation`/`update-to`/`updated-by` for `10.1136/ard.2009.118406`, and Europe PMC
returns 0 hits both for that journal/year/page and for a citing Published Erratum. So its scope
is unestablished. **The verdict does not rest on the erratum** — it rests on the study design
stated in the paper's own full text — and I have deliberately not let an unresolvable correction
manufacture a hedge (the mistake AFF4 made in the other direction).

That check ran over all **31** PMIDs cited anywhere in the review YAML, these notes, or the
affinage record (`corrections.json` records the list): **1 of 31 flagged, and no
retractions and no expressions of concern.** The denominator has been 17, then 29, and is now
31 as these notes accumulated the donor, IntAct and review-round references; every number in
the committed artifacts is read from `corrections.json` rather than remembered, which is the
only reason it has stayed correct through three changes.

## `GO:0035116 embryonic hindlimb morphogenesis` — well founded, kept as non-core

My first instinct was that a single case report of a 500-kb deletion could not support a
gene-specific IMP. That was wrong, and an independent paper says so:
`PMID:25162227` states "A human microdeletion of 500 kb on chromosome 2q11.1 encompassing only
the LAF4 gene has been detected by array comparative genomic hybridization on peripheral
lymphocytes". So it is not a contiguous-gene deletion.

The evidence then triangulates, and it is specifically the **lower** limb:

- `PMID:18616733`: "We report on a girl with fibular agenesis, severely abnormal, triangular
  tibiae"; the deletion is de novo; and
  "In situ hybridization analysis of Laf4 in mouse embryos revealed expression in the
  developing brain, in the limb buds and in the zeugopod corresponding to the limb phenotype".
- `PMID:33961779`: "Whereas homozygous Aff3 knockout mice display skeletal anomalies, kidney
  defects, brain malformations, and neurological anomalies, knockin animals modeling one of the
  microdeletions and the most common of the missense variants identified in affected
  individuals presented with lower mesomelic limb deformities like KINSSHIP-affected
  individuals and early lethality".
- `PMID:24763282`: "By whole-mount in situ hybridization the mouse AFF3 ortholog shows strong
  regional expression in the developing brain, somites and limb buds in 9.5-12.5dpc mouse
  embryos".

`GO:0035116`'s definition is "the anatomical structures of the hindlimbs ... the posterior
limbs of an animal" — no taxon problem for a human lower limb, and the term is *more* apt than
the parent because both the patient and the knockin mice are lower-limb.

**The dosage point, and why it does not change the verdict.** AFF3's limb phenotypes arrive
from opposite directions — haploinsufficiency (deletion; promoter GCC silencing) and
gain-of-function degron stabilisation (KINSSHIP). `PMID:38811945` frames this as
"minute changes in AFF3 function are deleterious"; both homozygous LoF and homozygous KINSSHIP
isogenic lines perturb "more than a third of the AFF3 bound loci". A gene whose *increase* and
*decrease* both break limb development is participating in limb development either way, so
`involved_in` is right. What the evidence does **not** support is any claim about the KINSSHIP
protein's activity being AFF3's normal activity — KINSSHIP is a degradation-resistance defect,
not a new function — and nothing in this review annotates from the mutant protein's behaviour.
The same discipline applies to the MLL–AFF3 and RUNX1–AFF3 leukaemic fusions
(`PMID:12203795`, `PMID:12743608`, `PMID:17968322`): a fusion oncoprotein's behaviour is not
the wild-type protein's function, and **no GO row in this review derives from a fusion.**

## `GO:0050877 nervous system process` — the IBA is less precise than its donors, and that is correct here

`resolve_withfrom.py` shows both protein donors carry the *same*, *lower* experimental term:
mouse Aff2 `GO:0007611` IMP (`PMID:11923441`, Fmr2-knockout conditioned fear) and fly lilli
`GO:0007611` IMP (`PMID:18310460`). `term_relations.py` confirms `GO:0007611` **is** a
descendant of `GO:0050877`, so the propagation landed two levels above two agreeing donors —
the ACRV1 shape.

But refining it downward would be wrong. AFF3 has no learning-or-memory data of its own, and
its documented nervous-system involvement is **developmental**: cortical migration in mouse
(`PMID:25162227` — "we discovered that Laf4 is required for cortical cell migration"), ID and
seizures in KINSSHIP, and a GCC promoter expansion associated with
"a 2.4-fold reduced probability of completing secondary education" (`PMID:39313615`).
`term_relations.py` also verifies that `GO:0001764` is **NOT** a descendant of `GO:0050877` —
the developmental branch is not reachable from this term at all. So the honest reading is:
the row's propagation route is weak, the term itself stands on AFF3's own human genetics, and
the specificity AFF3 actually deserves lives in a different branch, proposed separately as
`GO:0021795`. Verdict `KEEP_AS_NON_CORE`, agreeing with both AFF1 and AFF4 but for a measured
reason rather than by convention.

## Sibling comparison: where I agree with AFF1/AFF4 and where I do not

Checked against `origin/main:genes/human/AFF4/...` and, initially,
`origin/paint/AFF1:genes/human/AFF1/...`. AFF1 merged (commit `92eb534fe`) partway through, and
the merged file is byte-identical to the branch head the comparison below was built from, so
nothing had to be redone.

| row | AFF1 | AFF4 | AFF3 (this review) |
|---|---|---|---|
| `GO:0006355` IBA | ACCEPT | ACCEPT | **ACCEPT** |
| `GO:0003712` IBA | ACCEPT | ACCEPT | **ACCEPT** |
| `GO:0032783` IBA | ACCEPT | ACCEPT | **ACCEPT** |
| `GO:0005634` IEA GO_REF:0000120 | ACCEPT | ACCEPT | **ACCEPT** |
| `GO:0050877` IBA | KEEP_AS_NON_CORE | KEEP_AS_NON_CORE | **KEEP_AS_NON_CORE** |
| `GO:0006354` IBA | MODIFY → `GO:0006368` | **ACCEPT** | **MODIFY → `GO:0006368`** |
| `GO:0010468` IEA GO_REF:0000002 | MODIFY → `GO:0006355` | **ACCEPT** | **ACCEPT** |

The two siblings disagree on exactly the two rows where I had to choose, and they disagree in
opposite directions, so "follow the family" gives no answer. The rule I used instead, applied
to both:

> MODIFY a broad term only when the more specific term the donor evidence supports is **not
> already annotated on this gene**. If it is, the broad row is a redundant ancestor and MODIFY
> buys nothing.

- `GO:0006354`: the donor's own evidence is human AFF1's EXP from `PMID:22547686`, a paper whose
  measurement is **Pol II** CTD kinase activity of the SEC family. `GO:0006368` is verified to
  be a descendant of `GO:0006354` and is **not** otherwise on AFF3 → MODIFY adds information.
- `GO:0010468`: `GO:0006355` is verified to be a descendant of `GO:0010468` and **is** already
  on AFF3, from a better-founded IBA whose donor set includes the true mouse orthologue with its
  own IDA+IMP → the InterPro row is a redundant ancestor, ACCEPT with a note.

So the divergences are not stylistic; each follows from a stated rule, and the rule reproduces
AFF1 on one row and AFF4 on the other.

**Where I diverge on `core_functions` shape, and why.** AFF1 and AFF4 independently put the
scaffolding in `molecular_function` as `GO:0030674` and the complex's catalytic contribution in
`contributes_to_molecular_function` as `GO:0003711`. I keep the second and place `GO:0003712`
alongside `GO:0030674` as the first core function's MF, because AFF3's own best-evidenced
molecular role is the *coregulator* one, and `GO:0003712`'s usage comment describes it exactly:
"Most transcription coregulators do not bind DNA. Those that do usually bind DNA either in a
non-specific or non-direct manner." AFF3 binds dsDNA non-specifically in vitro, is *recruited*
by ZFP281/ZFP57, and has no sequence motif of its own. AFF1/AFF4 had bare `GO:0005515` IPI rows
that needed an informative replacement and mapped interfaces to justify it; **AFF3 has zero
`GO:0005515` rows in GOA**, so nothing pushed me toward `GO:0030674` from that direction —
I propose it on independent grounds (below) instead of inheriting it.

`term_relations.py` caught me getting this wrong on the first pass: I assumed `GO:0030674` was
a descendant of `GO:0005515`. It is not — its only ancestors are `GO:0003674` and `GO:0060090`.
Proposing it is therefore a move into the molecular-adaptor branch, not a refinement of protein
binding, and the guard is what told me so.

## Two annotations that exist in UniProt but not in GOA — same route, opposite verdicts

AFF3's UniProt entry carries two GO cross-references that GOA does not have (QuickGO returns
exactly 11 annotations for P51826, matching the GOA TSV):

```
DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IEA:Ensembl.
DR   GO; GO:0003690; F:double-stranded DNA binding; IEA:Ensembl.
```

Both are Ensembl-Compara projections from mouse Aff3, and they should be handled oppositely:

- **`GO:0003690` is right and GOA is missing it.** The human protein binds dsDNA in a direct
  in vitro assay (`PMID:8555498`), UniProt's own FUNCTION line records it, and human ChIP places
  AFF3 on a specific CpG island (`PMID:30535390`). Proposed as a NEW row.
- **`GO:0003700` is wrong for AFF3.** Its definition requires "selective and non-covalent
  binding to a specific double-stranded genomic DNA sequence (sometimes referred to as a motif)
  within a cis-regulatory region", and its usage comment warns against exactly this case.
  `term_relations.py` confirms `GO:0003700` and `GO:0003712` are **siblings** — neither is an
  ancestor of the other — so this is a wrong term, not a coarse one. The mouse source rows
  (`PMID:25162227`, IDA + IMP) rest on ChIP-qPCR of **over-expressed HA-tagged** Laf4 at one
  promoter, and the paper's own framing is a hypothesis: "To determine whether Laf4 or a
  Laf4-containing complex is able to bind in or around the Mdga2 locus as a **potential** direct
  transcriptional regulator". Filed as a UniProt/Ensembl correction request in
  `suggested_questions`, **not** as a GO action — there is no GOA row to act on, and inventing
  one to express the concern would be an over-annotation of the opposite sign (the ADCK5 rule).

A related stale projection, noted while querying the donor: mouse Aff3 holds
`GO:0016604 nuclear body` and `GO:0005829 cytosol` by `ISO GO_REF:0000119` **from human
P51826**, while human AFF3 currently carries neither. The mouse rows are reflections of human
annotations that no longer exist.

## Automated-route provenance (checked, and mostly clean)

- **InterPro2GO.** AFF3 matches three signatures. Fetched each one's mapping directly:
  `IPR007797` (AF4/FMR2 family, 5800 proteins) → `GO:0010468`; `IPR043640` (C-terminal homology
  domain, 4950) → `GO:0005634`; `IPR043639` (AF4 interaction motif, 3235) → **nothing**.
  This **reproduces AFF4's published measurement exactly**, which is the precondition the
  campaign asks for before reporting one's own column. **No molecular-function term is produced
  by any signature** — so the fold-propagation lead does not confirm on AFF3 either. That is now
  the fourth non-confirmation in a row for that lead, and it is worth stating as a
  non-confirmation rather than manufacturing an instance.
- **ARBA.** The `GO_REF:0000120` nucleus row names `ARBA:ARBA00026330`. Fetched from
  `rest.uniprot.org/arba/ARBA00026330`: 1309 condition sets, of which exactly one touches AFF3 —
  `IPR007797 AND IPR043640 AND Eukaryota → GO:0005634`. A two-signature family conjunction for a
  nuclear localisation that AFF3's own IDA confirms. Sound.
- **Independence of the combinatorial reference.** `GO_REF:0000120`'s three tokens are
  `ARBA:ARBA00026330 | InterPro:IPR043640 | UniProtKB-SubCell:SL-0191`. They are **not three
  independent witnesses**: the ARBA rule's own condition set *is* `IPR007797 + IPR043640`, and
  SL-0191 derives from UniProt's `CC   -!- SUBCELLULAR LOCATION: Nucleus.` line, which carries
  no evidence tag. So one signature is counted twice and the third token is UniProt citing
  itself. Same shape as ADISSP's finding. It does not change the verdict — the row is
  independently confirmed by an IDA — but the apparent triple corroboration is illusory.
- **Bulk TAS import / cross-product checks.** None applicable: AFF3 has no TAS rows, and no
  pair of its 11 terms is a positive/negative regulation pair, so the ADIPOQ logical-opposite
  cross-product test is trivially negative. Recorded so the next reviewer knows it was run.

## IntAct: 14 records, and the reason there is nothing to adjudicate

AFF3 has **no `GO:0005515` rows in GOA at all**, so there are no per-partner verdicts to make.
Queried IntAct anyway (`findInteractions/P51826`, 14 records, all returned):

- **CDK9 in 6 records across 5 distinct publications and 3 distinct methods**
  (anti tag coip, pull down, tap), MI scores 0.35 and 0.73 - `PMID:23455922`, `PMID:23602568`, `PMID:28514442`,
  `PMID:32707033`, `PMID:33961781`. **These figures are computed** by
  `intact_partners.py`; the first, hand-counted version of this bullet said "5 records across 4
  publications and 4 methods with MI 0.73" and was wrong on every one of the four numbers,
  which is why the script exists.
- **MLLT1 (ENL)** in 2 records from 1 publication by anti-tag co-IP (`PMID:33961781`), MI 0.35 -
  a SEC module component.
- PIP4K2A in 2 records across 2 publications
  (`PMID:28514442`, `PMID:33961781`), MI 0.35 - not a singleton, as an earlier version of this
  bullet said.
- Genuine singletons, of unclear relevance: SYT2, DISC1 (2-hybrid fragment pooling), and
  ERP29/TFRC by crosslinking (`PMID:30021884`).

Two of these — CDK9 and MLLT1 — are the two SEC modules AFF3 is supposed to bridge, replicated
across independent studies and methods, and **GOA has curated none of them.** That is the
under-curation diagnosis AFF4 established, reproduced here from a different instrument.

## Deep research provider

`AFF3-deep-research-affinage.md`: `gates_passed: True`, 15 citations, all numeric PMIDs, no
`PMID:bio_*` preprint ids. Recall was good on this gene — unusually so, given the campaign's
experience — but two things it did not supply were decisive and both had to be found elsewhere:

1. **`PMID:22547686`** (the SEC-L3 isolation paper) is absent from the affinage citation list.
   It surfaced only from QuickGO, as the reference behind human AFF1's `GO:0006354` EXP — i.e.
   by following the WITH/FROM one level deeper, which is the brief's own recipe.
2. **`PMID:18616733`** and **`PMID:20444755`**, the two papers behind AFF3's only two
   experimental BP rows, are both absent from the affinage record. The provider returned the
   gene's *notable* literature; the *annotation-relevant* literature was a different set. Same
   characterisation as ADIPOQ.

Also worth recording: the affinage narrative says AFF3 "binds double-stranded DNA and carries a
domain that strongly activates transcription", citing `PMID:8555498`. That is faithful. But the
GAL4-fusion result it alludes to ("both LAF-4 and AF-4 had domains that activated transcription
strongly when fused to the GAL4 DNA-binding domain") is a *heterologous* transactivation assay,
which is why this review annotates coregulator activity rather than transcription factor
activity from it.

## Process

- GOA TSV rows: **11**. `existing_annotations` from the `fetch-gene` stub: **11**. They
  reconcile exactly, with no collapsed `GO:0005515` or same-term/different-assigner rows (the
  ADAMTSL5 under-seeding failure mode does not apply here). Total entries after review is 11 + 8
  NEW = 19.
- Tooling note: the OLS MCP was unusable this session (`Could not find a suitable TLS CA
  certificate bundle` — its venv's `certifi` had been pruned from the uv cache while the disk
  was full). All ontology lookups went through QuickGO instead, via committed scripts
  (`go_terms.py`, `go_search.py`, `term_relations.py`) so they are reproducible.
- `audit_claims.py` in the bioinformatics folder is the local gate: it walks the **emitted**
  YAML (not a generator), rejects duplicate mapping keys with a strict loader, reconciles raw
  against parsed quote counts, checks `knowledge_gaps[].provenance` which `checkquotes.py` does
  not walk, verifies every `file:` quote with an exact-substring test on a single physical line,
  and asserts every `core_functions` term is backed by an ACCEPT/KEEP_AS_NON_CORE/NEW row and
  vice versa. `verify_file_quotes.py` re-checks the same `file:` quotes with a **byte-exact**
  match — a different instrument, since CI checks none of them and normalisation hides a
  dash or curly-quote substitution. 14 break-test directions, each asserting the mutation
  changed the document, that the guard fired, and that the message was the expected one.

## The number that refused to add up, and the second retraction

After the PR was opened I re-derived a figure I had counted by eye. The review said IntAct
records "CDK9 in **five** records across **four** distinct publications and **four** distinct
methods with a MI score of 0.73". `intact_partners.py` computes **6 records, 5 publications,
3 methods, MI in {0.35, 0.73}**. Every one of the four numbers was wrong — the publication
count too low, the method count too high, and the MI presented as uniform when one record
(an isoform-2 pairing) sits at 0.35.

Two things worth recording about how it happened and how it was fixed:

1. **The wrong version was produced by an ad-hoc query that deduplicated on a composite key**,
   which silently dropped one CDK9 record, and then by counting the printed lines by eye. The
   corrected figures come from a committed script that asserts the subject is not in its own
   partner set and that every record IntAct reports is retrieved.
2. **The repair script's first anchor did not match**, because the notes use `×` and `—` where
   I had typed `x` and `-`. The anchor assertion caught it rather than the edit silently
   landing in 4 of 5 places — which is exactly the hyphen/en-dash trap the campaign brief
   warns about for quotes, arriving here in a find-and-replace instead.

The guard against the recurrence is **structural, not a phrase pin**: `audit_claims.py` parses
any prose stating CDK9's counts and compares them against `intact_partners.json`, so a
rewording cannot evade it. It is break-tested against `git show HEAD:...` — the version that
actually shipped — and has a vacuity direction that fires if the sentence disappears
altogether. The correction direction is favourable: 5 independent publications is a *stronger*
replication claim than 4.

## A third retraction, and the same lesson: the guard caught a claim I had already shipped

The `GO:0006355` row's original reason argued that the row should stay at the unsigned parent
"because the donors disagree in sign — mouse Aff1's descendant is positive regulation while
human AFF1's is in the negative-regulation-of-elongation branch". I had read `GO:0032786` as
negative by its proximity to `GO:0032785`. Adding it to `term_relations.py` refuted it
immediately: **`GO:0032786` is *positive* regulation of DNA-templated transcription, elongation**,
a verified descendant of `GO:0045893`. So every signed donor on that row points the same way,
and `GO:0045893` is itself a descendant of `GO:0006355`, meaning a positive child was available
and unused. The AEBP2 donor-disagreement test does not apply at all.

The verdict did not change, but the reason had to. What actually forbids refining the row is the
**recipient**, not the donors: AFF3 represses XIST from the silent allele in two human lines
while establishing a permissive state at the Meg3 enhancer with ZFP281 and raising 84% of the
transcripts it changes on over-expression in mouse cortical cells. A positive-only term would be
false for the repressive half — which is why the specific negative instance is a separate
`GO:0045892` row rather than a modification of this one.

Three retractions on this gene, and the common shape is worth naming: **each was an inference
from an identifier's or a label's neighbourhood rather than from a fetched fact.**
`GO:0030674` was assumed to be under `GO:0005515` because adaptor activity *sounds like* a kind
of protein binding; `GO:0032786` was assumed negative because it sits one integer from
`GO:0032785`; and the IntAct counts were read off a printed list instead of computed. In all
three cases the fix was to write the check, and in all three the check fired.

## Review round 1 (PR #2351, ai4c-reviewer): approved, six suggestions

Verdict was **approve** with no critical or important issues. Each suggestion's premise was
checked before conceding, and one was declined with evidence rather than accepted.

**Accepted, and each a real defect.**

1. **`GO:0030674` was an ill-formed IPI.** For IPI the WITH/FROM field takes the interactor, and
   the row had none. Added CDK9 (`UniProtKB:P50750`) and cyclin T1 (`UniProtKB:O60563`), both
   confirmed reviewed human entries by asserting `primaryAccession` on the fetch. The reviewer's
   alternative — recode as ISS on AFF1/AFF4, whose interfaces are mapped — was declined with a
   stated reason: the assay is a co-IP of AFF3 itself in human cells, so IPI is the correct code
   and what was missing was the entity, not the code. The unmapped-interface caveat belongs in
   the reason and in the knowledge gap, which is where it already was.
2. **`GO:0003711`'s reason asserted a sibling relation on one leg only** and read a kinase
   measurement as an elongation-factor claim without saying so. Both fixed: the inference is now
   named as an inference, and `term_relations.py` checks `GO:0003711` under `GO:0140110` as well
   as `GO:0003712`.
3. **`GO:0001822`'s second human quote is "urogenital tract malformations"**, which is broader
   than the kidney. The reason now says the mouse null is doing the work and the human quote
   corroborates the organ system rather than the organ.
4. **Two follow-ups the review was positioned to file but had not.** The `GO:0034612` removal's
   downstream consumer (mouse Aff3's ISO row) is folded into the MGI question so the retraction
   is actionable; and AFF4's merged review asks whether `GO:0032783` should reach AFF3 at all on
   the premise that AFF3 "has not been shown to be a subunit of that complex" — I verified that
   text at `AFF4-ai-review.yaml` before asserting it — which AFF3's own human biochemistry
   refutes, so that correction is now filed too.

**Half accepted, and the half that was wrong is the interesting part.** The reviewer observed
that the `GO:0050877` reason grounded the row in AFF3's human genetics while the same review
argues that AFF3's developmental nervous-system role is off-branch — so the grounding cited
evidence the review says belongs elsewhere. Checking it split the claim: **`GO:0050890 cognition`
IS a descendant of `GO:0050877`**, and `GO:0007611` sits one step under cognition, so the
intellectual disability, seizures and the education association are legitimately *inside* the
term; `GO:0021795` is **not** a descendant, so only the migration evidence is off-branch. The
reason had lumped the two halves together. It now rests primarily on the two donor IMPs, cites
the cognitive phenotypes as on-branch corroboration, and explicitly assigns the migration
evidence to the separate proposed row.

**Declined, with evidence.** The reviewer suggested `GO:0030674` or `GO:0003712` might capture
the class-switch core function better than `GO:0003690`. Both would over-claim, and the paper
says so itself: `GO:0030674` would assert a bridge between switch-region DNA and AID, but
`PMID:36001653` states "While the mechanism by which AID is recruited to switch regions is still
unclear, the following mechanisms have been proposed" and offers cohesin and P-TEFb as
alternatives — "AFF3 may regulate CSR by facilitating the interaction of AID with cohesin
factors". And `GO:0003712` belongs to transcription regulation whereas class switch recombination
is a DNA recombination reaction. What was measured is switch-region occupancy: "We detected
significant increases in the signals near the switch regions of IgM and IgG1, indicating that
AFF3 can bind to these regions". Those three quotes are now in the row's `supported_by`, so the
refusal is itself CI-checked rather than asserted in prose.

**A measurement the review round added.** Asked how large the `GO:0005515` coverage gap is,
one QuickGO call over all three paralogues answers it with its own positive controls: **AFF4 15
rows, AFF1 3, AFF3 zero** — so the endpoint works, the term is alive for the siblings in the
same request, and AFF3's zero is a real absence rather than a rejected query. Given that AFF3's
CDK9 contact is the most replicated of the three in IntAct, that is a curation asymmetry rather
than a biological one.

## Review round 2: five carried-over items were all the same failure

The round-2 review requested changes for one new issue plus five carried over, and the five
share a single cause worth naming: **round 1 fixed each claim on the surface the reviewer had
named and left it standing on a low-salience one.** The surviving instances were a
`reference_review` note, a `source_entities` comment, a script docstring, a notes bullet and the
top-level `description` — precisely the surfaces nobody re-reads.

Worse, **my own guard was structurally unable to catch two of them.** `fix_sign_claim.py`'s
narration exemption was **file-scoped**: it exempted `AFF3-ai-review.yaml` wholesale so that the
file could narrate its own retraction, which made the re-grep blind to every *unnarrated*
instance inside that same file. Two survived there. The exemption is now **per-occurrence** — a
sentence asserting the retracted premise passes only if the surrounding window marks it as
retracted — and the check has moved out of the one-shot script into `audit_claims.py`, so it runs
on every audit rather than once. It is break-tested against `git show 2bf0d3d5e:...`, the commit
that actually shipped the two survivors, and has a companion direction asserting it stays silent
on the narrated retractions that remain by design.

That is guard-defeat mode number ten for this campaign, and it has a name of its own:
**an exemption coarser than the thing it exempts.** The narration exemption was correct in
intent and one scope-level too wide in implementation, which made the guard report success over
exactly the file it was written for.

**The one new issue, partly declined.** Round 1's `GO:0001822` commit — whose stated purpose was
to *stop* over-reading the human evidence — changed "named partly for horseshoe kidney" to
"horseshoe **or hypoplastic** kidney". The reviewer is right that `PMID:33961779` spells the
acronym "KI for horseshoe kidney" and never says hypoplastic. But the phrase is not unsourced:
UniProt's DISEASE line for KINSSHIP reads
[file:human/AFF3/AFF3-uniprot.txt "facial features, horseshoe or hypoplastic kidney, and failure to"].
So the defect was **attribution, not fabrication** — the phrase sat next to a PMID quote and read
as the paper's. It is now attributed to UniProt explicitly on both surfaces. The lesson is still
the reviewer's, and sharper for being narrower: a commit that tightens a claim can loosen it in
the same breath, and the added words came from a different source than the quote beside them.

The other four: `:414`'s "all verified" was vacuous for `GO:0045893` (verified under itself) and
untrue of `GO:0032968`, whose ancestry claim was simply missing from the guard — now present, 20
claims; the speckle P-TEFb co-concentration is qualified on both surfaces, since the
redistribution of CDK9 and cyclin T1 to AFF3 sites required strong over-production and only
AFF3's own speckle localisation is a baseline observation; `intact_partners.py`'s docstring still
said "5 records" a full round after the prose had been corrected to 6; and PIP4K2A was listed as
a singleton when it has 2 records across 2 publications.

## Review round 3: approved, three tooling suggestions taken, and a stopping criterion

Round 3 approved on the head and raised three non-blocking suggestions. All three were taken,
because each closed a real hole rather than rewording prose:

1. **The new UniProt `file:` quote lived only in `AFF3-notes.md`**, which `verify_file_quotes.py`
   does not walk — so the one quote added to *answer* a fabrication-surface criticism was itself
   outside the gate. It is now in the `GO:0001822` row's `supported_by`, inside both quote
   checkers (15 `file:` quotes verified byte-exact, 75 total).
2. **The two prose guards were scoped to the review YAML** while the folder-wide sweep lived
   inside a one-shot repair script — which is precisely how the `intact_partners.py` docstring
   and the PIP4K2A bullet survived a round. `audit_sibling_surfaces()` now runs both guards over
   every `.md`, `.yaml` and `.py` in the gene folder on every audit, and it fails loudly if it
   scans zero files.
3. **The `GO:0003711`/`GO:0003712` reciprocal non-containment pair was unchecked**, unlike the
   equivalent `GO:0003700`/`GO:0003712` pair. Both directions now asserted — 22 claims.

**Widening the sweep immediately produced ten false positives, and that is the interesting
part.** Repair scripts must contain the retracted strings as their *find anchors*, and the guard
must contain them as *patterns* — so a naive folder-wide sweep forbids the guard from coexisting
with its own implementation. The exemption vocabulary was widened to cover anchors, patterns and
fixtures, kept strictly **per-occurrence** (never per-file, the mode that failed in round 2), two
find-anchors were labelled as such in `fix_intact_counts.py`, and both directions are
break-tested: the sweep fires on an unnarrated sign claim injected into the notes, and stays
silent on the anchors and narrated history that remain by design.

The synthetic IntAct-count break-test then failed **for the right reason and had to be repaired**:
the per-occurrence exemption legitimately suppressed the mutation, because the first of the two
CDK9 count sentences sits inside a window explaining the retraction. The test now selects an
un-narrated occurrence explicitly, asserts one exists, and uses a raw anchor unique to it — the
raw and whitespace-normalised forms differ because the phrase is line-wrapped differently at the
two sites. A break-test that fails because the exemption worked is not evidence the guard is
broken, and distinguishing the two took reading the window rather than the result.

**Stopping criterion.** Rounds 2 and 3 changed **no GO term, no action, no evidence code, no
quote and no reported number** in the curation itself — every item was about where a claim was
written, which surface a guard scanned, or which ancestry pair was pinned. The curation content
has been stable since `2bf0d3d5e`. So: I will still fix anything that misstates a number,
misattributes a source, or lets a guard report coverage it does not have. I will not keep
refining the guards' own prose, and I am not looking for further tooling symmetry for its own
sake. If a later round finds a factual defect in the annotations, that is a different matter and
gets fixed.

## Review round 4: the fix for round 3's false positives created a coverage hole

Round 4 requested changes for one item, **introduced by the round-3 commit and squarely inside
that commit's own stated stopping criterion** ("lets a guard report coverage it does not have").
The reviewer is right, and the diagnosis is worth recording because it is the same named mode a
third time, one level over each time.

**What happened.** Widening `check_intact_counts`' narration exemption fixed the ten false
positives on the repair scripts — but the function is called from *both* `audit()` (the review
YAML) and `audit_sibling_surfaces()` (the scripts and notes), and only the second needs the
exemption. The consequence is concrete: the YAML states the CDK9 counts about 170 characters
before "the hand-counted version of them was wrong", so **that occurrence became exempt from the
numeric check** — on the one file the guard exists for, at the sentence that announces the
correction.

**Demonstrated against the shipped code, not argued.** Extracting `audit_claims.py` and
`AFF3-ai-review.yaml` from `710a315df`, reverting the counts to the wrong 5/4 at that narrated
occurrence, and running the *shipped* guard reports **0 problems**. The current guard fires
there, and a new break-test direction pins it.

**The fix.** `allow_narrated` now defaults to `False` and is switched on only by the sibling
sweep. Verified before restoring the default that neither of the YAML's two count statements
quotes the retracted numbers, so nothing on that surface needs the exemption. And the vocabulary
is **split by surface**: the prose set is back to the original narrow retraction words, while the
code-shaped tokens (`anchor`, `pattern`, `fixture`, `guard`, `premise`, `startswith`, `finditer`,
`re.compile`) apply only on `.py` files — the reviewer's secondary point, that `guard` and
`premise` are ordinary words in this document and would have exempted a future unnarrated sign
claim written near either.

**Three instances of one mode, at three scopes.** Round 2: an exemption coarser in **file**
scope. Round 3: coarser in **surface** scope. Round 3 again, secondarily: coarser in
**vocabulary**. Each time the exemption was correct in intent and one level too wide in
implementation, and each time the symptom was a guard reporting success over exactly what it was
written to protect. The generalisable form: **when you widen an exemption to stop a false
positive, ask which callers need it and give it to those callers only** — the fix for a false
positive is almost always narrower in scope than the false positive's cause.
