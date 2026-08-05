# AFF3 — computed evidence for the GO review

This file is **hand-written**, not generated. It records and interprets the output of the
committed scripts in this folder; the machine-readable outputs (`withfrom_resolution.json`,
`reference_projection.json`, `corrections.json`) are the artifacts a re-run reproduces. Writing
it by hand deliberately avoids the regeneration trap where a hand-edit to a generated report is
silently reverted by the next run — the JSON is the claim, this prose interprets it.

Reproduce with:

```
uv run python genes/human/AFF3/AFF3-bioinformatics/resolve_withfrom.py
uv run python genes/human/AFF3/AFF3-bioinformatics/reference_projection.py
uv run python genes/human/AFF3/AFF3-bioinformatics/term_relations.py
uv run python genes/human/AFF3/AFF3-bioinformatics/corrections_check.py
uv run python genes/human/AFF3/AFF3-bioinformatics/intact_partners.py
uv run python genes/human/AFF3/AFF3-bioinformatics/audit_claims.py --self-test
uv run python genes/human/AFF3/AFF3-bioinformatics/verify_file_quotes.py
```

`fix_intact_counts.py`, `fix_sign_claim.py`, `fix_pmid_count.py`, `apply_review_round1.py` and
`apply_review_round2.py` are one-shot repairs, already applied. They are committed so that every correction this review made
to itself is reproducible and auditable rather than an untraceable hand-edit, and because each
one records in its docstring what was wrong and how the wrong version arose. Each asserts its
anchors are present before replacing, re-greps afterwards, and asserts `detected == changed`.

## 1. WITH/FROM resolution and donor evidence (`resolve_withfrom.py`)

Every token on all five IBA rows, resolved through UniProt (with `primaryAccession` asserted
equal to the requested accession, `size=10` so an ambiguous xref is reported rather than
silently reduced, and reviewed status tested with `entryType.startswith("UniProtKB reviewed")`),
then queried in QuickGO for its own evidence on the propagated term.

| token | accession | entry | status | organism / gene | candidates returned | own EXP codes for the propagated term |
|---|---|---|---|---|---|---|
| `MGI:MGI:106927` | P51827 | AFF3_MOUSE | Swiss-Prot | mouse Aff3 — **true orthologue** | 10 | IDA, IMP |
| `MGI:MGI:1100819` | O88573 | AFF1_MOUSE | Swiss-Prot | mouse Aff1 — paralogue | 10 | IDA |
| `MGI:MGI:1202294` | O55112 | AFF2_MOUSE | Swiss-Prot | mouse Aff2 — paralogue | 3 | IMP |
| `FB:FBgn0041111` | Q9VQI9 | AFFL_DROME | Swiss-Prot | *Drosophila* lilli — sole fly AFF | 3 | IMP, IGI, IPI |
| `UniProtKB:P51825` | P51825 | AFF1_HUMAN | Swiss-Prot | human AFF1 — **paralogue of the recipient** | 1 | EXP, IMP |
| `PANTHER:PTN000829417` | — | — | n/a | PANTHER tree node, not a protein | — | unqueryable |

Per-row donor counts, exactly as GOA gives them:

| row | tokens | protein tokens | donors with own experimental evidence |
|---|---|---|---|
| `GO:0006355` regulation of DNA-templated transcription | 5 | 4 | 4 |
| `GO:0003712` transcription coregulator activity | 2 | 1 | 1 |
| `GO:0006354` DNA-templated transcription elongation | 2 | 1 | 1 |
| `GO:0050877` nervous system process | 3 | 2 | 2 |
| `GO:0032783` super elongation complex | 2 | 1 | 1 |

So the "these donors only carry the same family-level inference" objection is **false on every
row** — it is testable here, and it fails, which is the expected outcome given that IBA
WITH/FROM lists experimentally-annotated members by construction.

**Which term each donor actually holds** (the ACRV1 question — not merely *whether* it holds one):

| row | donor | donor's own term | verdict on precision |
|---|---|---|---|
| `GO:0006355` | mouse Aff3 P51827 | `GO:0006355` (IDA+IMP, PMID:25162227) | lands exactly on the donor's term |
| `GO:0006355` | mouse Aff1 O88573 | `GO:0045893` (IDA, PMID:9365243) | donor is one level below; sign-specific |
| `GO:0006355` | human AFF1 P51825 | `GO:0032786`, `GO:0032968` (IMP) | donors below; two different children |
| `GO:0003712` | lilli Q9VQI9 | `GO:0003712` (IMP, PMID:11171404) | lands exactly on the donor's term |
| `GO:0006354` | human AFF1 P51825 | `GO:0006354` (EXP, PMID:22547686) | lands exactly, but the donor's paper measured **Pol II** |
| `GO:0050877` | mouse Aff2 O55112 | `GO:0007611` (IMP, PMID:11923441) | donor is **two levels below** |
| `GO:0050877` | lilli Q9VQI9 | `GO:0007611` (IMP, PMID:18310460) | donor is **two levels below** |
| `GO:0032783` | lilli Q9VQI9 | `GO:0032783` (IPI, PMID:22195968) | lands exactly on the donor's term |

**RETRACTED, and corrected here rather than deleted.** An earlier draft of §1 stated that the
`GO:0006355` donors disagree in *sign* — reading `GO:0032786` as negative-branch by proximity to
`GO:0032785`. §3 refutes it: `GO:0032786` is **positive** regulation of transcription elongation,
a descendant of `GO:0045893`, so **every signed donor on that row points the same way**, and
`GO:0045893` is itself a descendant of `GO:0006355`, i.e. a positive child was available and
unused. The AEBP2 donor-disagreement test therefore does **not** apply.

What keeps the row at the unsigned parent is the **recipient**, not the donors: AFF3's own output
runs both ways — it represses XIST from the silent allele in HEK293T and IMR-90, while with
ZFP281 it establishes a permissive chromatin state at the Meg3 enhancer and its over-expression
raises 84% of the transcripts it changes in mouse cortical cells. A positive-only term would be
false for the repressive half. The specific negative instance is proposed as a separate
`GO:0045892` row instead of by refining this one.

The `GO:0050877` donors, by contrast, **agree** on `GO:0007611` and the row sits two levels
above it. That is a granularity mismatch relative to the donors — but the specific term is not
supported for AFF3 itself, so the row is kept general rather than refined.

AFF3's own human nervous-system evidence then splits across the branch boundary, and §3 measures
where the boundary falls. `GO:0050890 cognition` **is** under `GO:0050877`, so the intellectual
disability, seizures and the GCC-expansion education association are *inside* the term and do
corroborate the row; `GO:0021795` and `GO:0001764` are **not**, so the cortical-migration evidence
is outside it and belongs on the separately proposed row. Offering both halves together as the
row's grounding — which an earlier draft did — conflates on-branch corroboration with off-branch
evidence, and that is what review round 1 caught.

## 2. The byte-identical WITH/FROM that means three different things

`GO:0006354` carries `PANTHER:PTN000829417|UniProtKB:P51825` on AFF1, AFF4 **and** AFF3 —
identical bytes in all three GOA records.

| recipient | is `P51825` the recipient? | evidential status of the row |
|---|---|---|
| AFF1 (P51825) | **yes** | self-referential: a PAINT curator judging the function core |
| AFF4 (Q9UHB7) | no | paralogue-derived |
| **AFF3 (P51826)** | **no** | **paralogue-derived** |

## 3. Ancestry claims, fetched not assumed (`term_relations.py`)

22 claims, all verified against QuickGO with `relations=is_a,part_of` only (so `regulates`
edges cannot be mistaken for subsumption). The script exits non-zero if any claim is wrong.

| claim | result |
|---|---|
| `GO:0006368` is a descendant of `GO:0006354` | true — the MODIFY is a downward move |
| `GO:0006355` is a descendant of `GO:0010468` | true — the InterPro row is a redundant ancestor |
| `GO:0007611` is a descendant of `GO:0050877` | true — the donors sit below the propagated term |
| `GO:0001764` is a descendant of `GO:0050877` | **false** — the developmental branch is unreachable from this term |
| `GO:0016607` is a descendant of `GO:0005654` | true — nuclear speck refines the nucleoplasm IDA |
| `GO:0003700` is a descendant of `GO:0003712` | **false** |
| `GO:0003712` is a descendant of `GO:0003700` | **false** — the two are SIBLINGS, so this is a wrong term, not a coarse one |
| `GO:0030674` is a descendant of `GO:0005515` | **false** |
| `GO:0030674` is a descendant of `GO:0060090` | true — adaptor activity is a separate MF branch, not a refinement of protein binding |
| `GO:0035116` is a descendant of `GO:0030326` | true |
| `GO:0003712` is a descendant of `GO:0140110` | true |
| `GO:0045190` is a descendant of `GO:0002443` | true |
| `GO:0032786` is a descendant of `GO:0045893` | true — it is in the POSITIVE branch |
| `GO:0032786` is a descendant of `GO:0045892` | **false** — which is what the retracted §1 premise assumed |
| `GO:0045893` is a descendant of `GO:0006355` | true — a positive child was available and unused |
| `GO:0050890` is a descendant of `GO:0050877` | true — cognition IS on-branch, so the ID phenotype is valid grounding |
| `GO:0007611` is a descendant of `GO:0050890` | true — the donors' term sits one step under cognition |
| `GO:0021795` is a descendant of `GO:0050877` | **false** — the migration evidence is the off-branch half |
| `GO:0003711` is a descendant of `GO:0140110` | true — closes the sibling claim's second leg |
| `GO:0032968` is a descendant of `GO:0045893` | true — the third signed donor term is positive too |
| `GO:0003711` is a descendant of `GO:0003712` | **false** |
| `GO:0003712` is a descendant of `GO:0003711` | **false** — the reciprocal pair, so the sibling claim is checked in both directions |

**This guard has now caught two of my own claims, which is the argument for having it.**

1. The `GO:0030674`/`GO:0005515` claim was written the **wrong way round** on the first pass.
   It is retained in the script with the corrected expectation and a comment recording the error.
2. The `GO:0032786` rows were added *after* the review was written, to check the §1
   sign-disagreement premise. They refuted it: `GO:0032786` is positive, not negative, so the
   donors agree and the original argument for keeping `GO:0006355` unsigned was false. The
   verdict survived on a different and better ground (the recipient's own mixed output), but the
   reason had to be rewritten. **A claim I had already shipped, corrected by a check written
   afterwards.**
3. The last four rows were added in review round 1. Three of them settle a tension the reviewer
   found in the `GO:0050877` reason — the row was grounded in AFF3's human genetics, while the
   review argues elsewhere that AFF3's developmental nervous-system role is off-branch. The
   reviewer was **half right**: `GO:0050890 cognition` **is** under `GO:0050877`, so the
   intellectual-disability and language/education phenotypes are legitimate on-branch grounding,
   whereas `GO:0021795` is **not**, so the migration evidence is the off-branch half. The reason
   now separates the two instead of lumping them, and rests primarily on the donor IMPs. The
   fourth closes the second leg of the `GO:0003711`/`GO:0003712` sibling claim, which the reason
   asserted while only one leg was checked.

## 4. Reference-projection test (`reference_projection.py`)

Distinct gene products per reference (entities, not annotations; pagination asserted against
`len(results)`, never against a page-size constant).

| reference | annotations | distinct entities | terms | projection? |
|---|---|---|---|---|
| `PMID:20444755` | 1 | 1 | `GO:0034612` IMP on P51826 | no |
| `PMID:18616733` | 2 | 2 | `GO:0035116` IMP on P51826; `GO:0035116` **IEP** on P51827 | no — two codes for two observations |
| `PMID:8555498` | 2 | 2 | `GO:0005634` IDA on P51826 and P51827 | no |
| `PMID:22547686` | 1 | 1 | `GO:0006354` **EXP on P51825 (AFF1)** | no — see below |

**The finding.** `PMID:22547686` is the paper that isolated the **AFF3**-containing SEC-L3, and
its only annotation in all of GOA is on **AFF1**, the paralogue it contrasts SEC-L3 against.
AFF3 receives the term back as an IBA pointing at AFF1. This is the second instance of the
shape in this family: AFF4's review found `PMID:20159561`, titled for AFF4, likewise produced
one annotation and it was on AFF1.

The `PMID:18616733` result is worth recording as a clean negative: the split is *correct*
curation, `IEP` for the mouse embryo in-situ and `IMP` for the human patient deletion, assigned
to the right species each.

## 5. Automated-route provenance

**InterPro2GO** — each of AFF3's three signatures, mapping fetched individually:

| signature | name | proteins | interpro2go mapping |
|---|---|---|---|
| `IPR007797` | AF4/FMR2 family | 5800 | `GO:0010468` regulation of gene expression |
| `IPR043640` | AF4/FMR2, C-terminal homology domain | 4950 | `GO:0005634` nucleus |
| `IPR043639` | AF4 interaction motif | 3235 | **none** |

This reproduces AFF4's committed measurement exactly. **No molecular-function term is produced
by any signature**, so the fold-to-activity hypothesis does not confirm on AFF3 — reported as a
non-confirmation, not manufactured into a GO action.

**ARBA** — `ARBA00026330`, named in the `GO_REF:0000120` row's WITH/FROM, has 1309 condition
sets; exactly one reaches AFF3:

```
IPR007797 AND IPR043640 AND taxon Eukaryota  ->  GO:0005634
```

**The combinatorial reference is not three independent witnesses.** `GO_REF:0000120`'s tokens
are `ARBA:ARBA00026330 | InterPro:IPR043640 | UniProtKB-SubCell:SL-0191`. The ARBA rule's own
condition set *is* `IPR007797 + IPR043640`, so `IPR043640` is counted twice; and `SL-0191`
derives from UniProt's own `SUBCELLULAR LOCATION: Nucleus.` line, which carries no evidence
tag. One signature, counted twice, plus UniProt citing itself. The row is still correct — AFF3
has its own nucleus IDA — but the apparent triple corroboration is illusory.

## 6. UniProt carries two GO terms GOA does not — and they resolve oppositely

QuickGO returns exactly **11** annotations for `UniProtKB:P51826`, matching the 11 rows of
`AFF3-goa.tsv`. UniProt's `DR GO` lines additionally carry two Ensembl-Compara projections:

| term | UniProt route | verdict |
|---|---|---|
| `GO:0003690` double-stranded DNA binding | `IEA:Ensembl` | **correct and missing from GOA** — proposed as a NEW row on the human in vitro assay (PMID:8555498) |
| `GO:0003700` DNA-binding transcription factor activity | `IEA:Ensembl` | **wrong for AFF3** — filed as a UniProt/Ensembl correction, not a GO action |

`GO:0003700` requires binding "a specific double-stranded genomic DNA sequence (sometimes
referred to as a motif) within a cis-regulatory region", and its usage comment warns against
this exact case. AFF3 is *recruited* by ZFP281/ZFP57 and its own DNA binding is non-specific.
The mouse source rows (PMID:25162227, IDA + IMP) rest on ChIP-qPCR of over-expressed HA-tagged
Laf4 at a single promoter, framed by the authors as testing a "potential direct transcriptional
regulator".

**Correction to a sibling review's premise.** AFF4's merged review states that AFF3's only
experimental molecular function is DNA-binding transcription factor activity. Read from AFF3's
own record, **human AFF3 has no experimental molecular-function annotation at all** — its only
MF row is the `GO:0003712` IBA. The `GO:0003700` IDA is on *mouse* Aff3.

A related stale projection, found while querying the donor: mouse Aff3 holds
`GO:0016604 nuclear body` and `GO:0005829 cytosol` by `ISO GO_REF:0000119` **from human
P51826**, while human AFF3 currently carries neither.

## 7. Corrections check (`corrections_check.py`)

31 PMIDs cited anywhere in the review, the notes or the affinage record, checked by two routes:
`PublicationType` on the article, and `CommentsCorrections/RefType` on the article's own record
(the second catches Errata and Publisher Corrections that a publication-type search cannot see).

**1 of 31 flagged; no retractions and no expressions of concern.**

`PMID:20444755` carries an `ErratumIn` reference to *Ann Rheum Dis. 2011 Aug;70(8):1519* whose
**PubMed id is null**. Not resolvable by the two fallback routes either: Crossref returns empty
`relation`, `update-to` and `updated-by` for `10.1136/ard.2009.118406`, and Europe PMC returns 0
hits both for that journal/year/page and for a citing Published Erratum. Its scope is therefore
unestablished — and the `REMOVE` verdict on that row deliberately does **not** rest on it.

## 8. Checks that came back negative, recorded so the next reviewer knows they were run

- **Complex-projection test** (a reference annotating a complex plus every subunit with
  identical evidence): none of the four references annotates more than two entities. Negative.
- **Logical-opposite citation cross-product** (a term and its negation sharing a reference set):
  AFF3's 11 terms contain no positive/negative regulation pair. Trivially negative.
- **Per-partner `GO:0005515` adjudication**: AFF3 has **no** `GO:0005515` rows in GOA, so there
  is nothing to adjudicate. IntAct nonetheless returns 14 records (all
  retrieved) over 7 distinct partners. Computed per-partner counts, from
  `intact_partners.py` / `intact_partners.json`:

  | partner | records | publications | methods | MI scores |
  |---|---|---|---|---|
  | CDK9 (P50750) | 6 | 5 | 3 | 0.35 and 0.73 |
  | PIP4K2A (P48426) | 2 | 2 | 1 | 0.35 |
  | MLLT1 (Q03111) | 2 | 1 | 1 | 0.35 |
  | TFRC (P02786) | 1 | 1 | 1 | 0.4 |
  | ERP29 (P30040) | 1 | 1 | 1 | 0.4 |
  | SYT2 (Q8N9I0) | 1 | 1 | 1 | 0.35 |
  | DISC1 (Q9NRI5) | 1 | 1 | 1 | 0.37 |

  The two SEC modules AFF3 bridges, CDK9 and MLLT1/ENL, are both present and GOA has curated
  neither - an under-curation datum, not an over-annotation one. **The scale of the gap,
  measured across the family in one QuickGO call so a zero cannot be a rejected query:**

  | gene | `GO:0005515` rows in GOA |
  |---|---|
  | AFF4 (Q9UHB7) | 15 |
  | AFF1 (P51825) | 3 |
  | **AFF3 (P51826)** | **0** |

  The two paralogues are the positive controls: the endpoint works and the term is alive for
  them in the same request, so AFF3's zero is a real absence. It is a curation asymmetry rather
  than a biological one — AFF3's CDK9 contact is the most replicated of the three in IntAct. **The first version of this
  section was hand-counted and said "5 records across 4 distinct publications and 4 distinct
  methods with MI 0.73" for CDK9. All four numbers were wrong.** That is why the counts are now
  derived from a committed script and quoted from its output table rather than written in prose.
- **GOA-stub under-seeding** (the ADAMTSL5 failure mode): the GOA TSV has 11 data rows and the
  `fetch-gene` stub seeded 11 entries. They reconcile exactly; no `GO:0005515` or
  same-term/different-assigner rows were collapsed.
- **Fold-to-activity propagation**: not confirmed (§5). Fourth consecutive non-confirmation of
  that lead in this campaign.
