# ARHGAP4 bioinformatics — results

Seven rerunnable analyses supporting `genes/human/ARHGAP4/ARHGAP4-ai-review.yaml`. Each
derives the repo root rather than hardcoding a worktree path, and each takes
`--self-test`, which breaks its input or its anchor on purpose and requires every guard
to fire, with negative controls that must stay silent.

```bash
uv run --with biopython --with requests python arginine_finger.py    # -> arginine_finger.json
uv run --with requests python check_gap_terms.py                     # -> gap_terms.json
uv run --with requests python reference_coverage.py                  # -> reference_coverage.json
uv run --with requests python resolve_entities.py                    # -> entities.json
uv run --with requests python comparator_terms.py                    # -> comparator_terms.json
uv run --with requests python impc_phenotypes.py                     # -> impc_phenotypes.json
uv run --with pyyaml python audit_review.py                          # no network
```

The first six query live services (UniProt, RCSB, QuickGO, OLS4, the GO API, the
Alliance, IMPC), so their JSON outputs are committed as the record of what those services
returned on the run that produced the numbers quoted below. `audit_review.py` needs no
network and checks the review document against itself.

---

## 1. `reference_coverage.py` — the defect is coverage, not over-annotation

The headline result. QuickGO was queried **by reference** rather than by gene, for 19
primary papers about ARHGAP4. The query is deliberately species-blind, because two of the
three mechanistic papers used the rat protein and the human `GO_REF:0000107` rows are
Ensembl-Compara projections from rat.

**16 of 19 primary papers produced no GO annotation on ARHGAP4 in any species.**

The three that did are the first three rows below. PMID:16417406 is listed for
completeness but is **not one of the 19** — it is an interactome screen, held in the
script's separate `screen_papers` set, so the arithmetic is 3 + 16 = 19.

| PMID | in the 19? | rows on ARHGAP4 (any species) |
|---|---|---|
| 8570618 Tribioli 1996 | yes | human: `GO:0005096`, `GO:0007010`, `GO:0007266`, `GO:0005737`, all TAS |
| 12414125 Foletta 2002 | yes | **rat**: `GO:0005096` **IDA**, `GO:0007399` IEP, `GO:0035023` NAS, `GO:0005874` IDA |
| 17804252 Vogt 2007 | yes | **rat**: `GO:0010764` IMP, `GO:0030517` IMP, `GO:0030426` IDA |
| the other 16 primary papers | yes | none |
| 16417406 Weiner 2006 | no — screen | human: `GO:0005515` IPI |

The 16 include every human-genetics paper, the ARHGAP4–SEPT2–SEPT9 complex, the EMT
screen, and all eight cancer papers. No result set was truncated, so these are zeros and
not page artefacts; the script reports a truncated result as *unknown* rather than as
zero, and its self-test uses BioPlex 3.0 (`PMID:33961781`) to confirm that branch fires.

Querying the projection donors directly shows the human record is a faithful shadow
rather than a free-floating inference. `UniProtKB:A0A0G2JVF0` and `RGD:628901` both carry
19 annotations, including `GO:0005096` **IDA** from `PMID:12414125` assigned by RGD, and
`GO:0010764`/`GO:0030517` **IMP** plus `GO:0030426` **IDA** from `PMID:17804252`. Every
`GO_REF:0000107` row on human ARHGAP4 projects one of these.

Two asymmetries fall out. The rat gene carries `GO:0035023 regulation of Rho protein
signal transduction` (NAS), which human does not, because NAS does not project. And the
Golgi localisation announced in the *title* of `PMID:12414125` has no GO annotation in
either species, while the microtubule half of the same observation has one and has been
projected.

## 2. `check_gap_terms.py` — GO cannot express GAP substrate specificity

Verified across **independent services**, not two endpoints of one, because QuickGO
**silently resolves merges**: ask it for a merged id and it returns the *surviving*
term's record flagged `isObsolete: false`. The script detects that behaviour rather than
trusting it, and reported it for **7 of the 9** ids queried.

| term | OLS4 | GO API | repo `cache/go/terms.csv` | QuickGO |
|---|---|---|---|---|
| `GO:0005096` GTPase activator activity | live | resolves | present | — |
| `GO:0005100` Rho GAP activity | obsolete → `GO:0005096` | empty record | absent | masks merge |
| `GO:0005099`, `GO:0005098` Ras | obsolete → `GO:0005096` | empty record | absent | masks merge |
| `GO:0008060` ARF | obsolete → `GO:0005096` | empty record | absent | masks merge |
| `GO:0005097` Rab | obsolete → `GO:0005096` | empty record | absent | masks merge |
| `GO:0046582` Rap | obsolete → `GO:0005096` | empty record | absent | masks merge |
| `GO:0017048` Rho GTPase binding | obsolete → `GO:0031267` | empty record | absent | masks merge |
| `GO:0031267` small GTPase binding | live | resolves | present | — |

The independent services agree on every term.

**`GO:0005096` has zero `is_a` children.** It is *not* childless, and the distinction
matters: QuickGO reports exactly one child, `GO:1902773 GTPase activator complex`, via
**`capable_of`** — a complex that is capable of the activity, not a more specific
activity. OLS4's asserted-subclass endpoint returns zero for `GO:0005096` while returning
five for `GO:0030695`, so the zero is a measurement and not a broken query.

The merged terms' names survive only as **synonyms** of `GO:0005096`: "Rho GTPase
activator activity", "Rac GAP activity", "Ras GAP activity", "ARF GAP activity", "Rab",
"Ral", "Ran", "Rap".

**Consequence.** Reactome files ARHGAP4 under `R-HSA-9013144 RAC1 GAPs stimulate RAC1
GTPase activity` and the rat assay covers RAC1, CDC42 and RHOA, but neither commitment is
expressible in GO. The merge was deliberate, so no replacement is proposed and no new
term requested. Substrate identity is recorded in `core_functions[].substrates` and as an
`RO:0002233 has_input` extension.

**A second absence, established by walking rather than searching.** ARHGAP4's only
interaction row is `GO:0005515 protein binding` with NCKAP1L (Hem-1), which says nothing
about function, so a more informative term was looked for. GO search is **token-based** —
"WAVE complex binding" can never match a term lacking those tokens — and a failed search
has justified wrong `REMOVE`s in this campaign before. So the branch was enumerated
instead, unbounded in depth and deduplicated: the **105** distinct descendants of
`GO:0044877 protein-containing complex binding` — reached over 106 parent-child edges,
the deepest four levels below the root — contain exactly **one** actin-machinery term,
`GO:0071933 Arp2/3 complex binding`, and no term for binding the WAVE/SCAR or Hem-1
complex. `GO:0031209 SCAR complex` exists, but
as a cellular component rather than as something to bind. The self-test requires the walk
to find `GO:0071933` (so a zero cannot be a broken query) and requires it *not* to find a
WAVE/SCAR/Hem binding term.

## 3. `arginine_finger.py` — the residue is present, and it settles nothing

**The anchor is verified structurally, not assumed.** PDB **1TX4** is the
RHOA·GDP·AlF4⁻·p50RhoGAP transition-state complex. SIFTS maps chain A residues 1–198 onto
`Q07960` 234–431, so ARHGAP1 Arg-282 is deposited residue 49 — and the script confirms
that residue 49 of chain A is **ARG**, with its guanidinium nitrogens **2.73 Å** from the
AlF4⁻ moiety. Displacing the SIFTS offset makes the check raise rather than silently
resolve to a neighbouring residue.

UniProt-delimited Rho-GAP domains were aligned to ARHGAP1's and the anchor column read
off. An independent second opinion — UniProt's PROSITE-ProRule `SITE` annotation — agrees
in **all 11** panel members.

| protein | role | aligned position | residue |
|---|---|---|---|
| ARHGAP1/p50 | positive control, PDB 1TX4 | 282 | **R** |
| **ARHGAP4** | **target** | **543** | **R** |
| ARHGAP35/p190A | positive control | 1284 | R |
| STARD13/DLC2 | positive control | 699 | R |
| ARHGAP21 | positive control | 1184 | R |
| ARHGAP11A | positive control | 87 | R |
| ARHGAP11B | retains residue, curated `NOT` | 87 | R |
| ARHGAP36 | known-dead (Amin 2016) | 258 | T |
| DEPDC1B | known-dead (Amin 2016) | 231 | I |
| OCRL1 | known-dead (Amin 2016) | 757 | Q |
| INPP5B | known-dead (Amin 2016) | 852 | Q |

A control that came out wrong would mean the anchor had moved, so the run aborts on one
rather than reporting it; the self-test confirms this by flipping a known-dead control's
expectation and requiring the abort.

**Residue identity and curated activity are decoupled in both directions.** This is
demonstrated from GOA rather than asserted:

- *arginine present, activity denied* — **ARHGAP11B** (`Q3KRB8`) retains the arginine and
  carries **two `NOT|enables GO:0005096` IDA rows** (`PMID:25721503`, `PMID:27957544`).
  UniProt names it "Inactive Rho GTPase-activating protein 11B". (It also carries a
  *positive* `GO:0005096` TAS from Reactome, so GOA contradicts itself on this protein —
  noted in passing, not this review's to fix.)
- *arginine absent, activity annotated* — **OCRL1** carries `GO:0005096` by **IDA**
  (`PMID:12915445`), ARHGAP36 by IBA, ARAP2 by IEA and IBA, FAM13B by TAS.

Scope note, so the table is not read as more than it is: the alignment here independently
recomputes the residue for ARHGAP36, DEPDC1B, OCRL1 and INPP5B — the four of Amin's seven
whose Rho-GAP domain UniProt delimits as a single feature. For ARAP2, DEPDC1 and FAM13B
the "no arginine finger" status is Amin's assignment, cited rather than re-derived.

The claim about ARHGAP4 itself is recorded in the review as a machine-checkable
`residue_claims` entry (anchor `Q07960`:282 R, target `P98171`:543 R, `RETAINED`, method
`MSA`), so `just validate-families` resolves it against the actual sequences on every CI
run that touches this gene. Mutation-tested: changing the claimed target residue to `C`
makes that validator report `target UniProtKB:P98171:543 claimed C but the sequence has R`
and exit non-zero, so the claim is genuinely covered rather than merely present.

So R543 is consistent with catalytic competence and is evidence against a
pseudo-enzyme reading, but on its own it licenses no conclusion about activity. The
family-level frame says the same thing from the other side: Amin et al. 2016
(`PMID:27481945`) report that the isolated RHOGAP domain "is nonselective and in some
cases rather inefficient under cell-free conditions" and that specificity comes from the
other domains. ARHGAP4 appears in that paper exactly once — entry 42 of Table 1, under
its old name p115 — inside the 57 predicted-catalytic RHOGAPs but **outside the 14 whose
kinetics were measured**. (A web-search summary claiming the paper assayed an
"ARHGAP4-R543K mutant by FRET" is not in the text and was not used.)

## 4. `resolve_entities.py` — WITH/FROM identities and PAINT node placement

Every WITH/FROM token in the committed GOA TSV, resolved against the authority that owns
its namespace. 16 of 18 resolved; the two that did not are
`UniProtKB-SubCell:SL-0086` and `ensembl:ENSRNOP00000069460`, recorded unresolved rather
than replaced with a guess.

`MGI:MGI:109605` = Srgap2 · `MGI:MGI:2152936` = Srgap1 · `MGI:MGI:2152938` = Srgap3 ·
`RGD:628901` = rat Arhgap4 · `O75044` = SRGAP2 · `P0DJJ0` = SRGAP2C · `P0DMP2` = SRGAP2B ·
`WB:WBGene00006406` = *C. elegans* srgp-1 · `P55160` = NCKAP1L.

ARHGAP4 sits in **PTHR14166 "SLIT-ROBO Rho GTPase-activating protein"**, whose other
members are SRGAP1/2/3 and the hominin-specific SRGAP2B/2C. Joining the WITH/FROM tokens
onto PANTHER's PAINT export:

| node | term | taxon | seeds | target lineage in seeds? |
|---|---|---|---|---|
| PTN002306152 | `GO:0005096` | Opisthokonta | Srgap2, Srgap1, **Arhgap4**, SRGAP2, srgp-1 | yes |
| PTN001021265 | `GO:0030336` | Eumetazoa | **Arhgap4**, SRGAP2, srgp-1 | yes |
| PTN002680572 | `GO:0005737` | Euteleostomi | **ARHGAP4 alone** | yes (self) |
| PTN008351815 | `GO:0007399` | (unscoped) | Srgap2, **Arhgap4**, SRGAP2, SRGAP2C | yes |
| PTN008351815 | `GO:0051963` | (unscoped) | Srgap2, Srgap3, SRGAP2C, SRGAP2B | **no** |
| PTN002680580 | `GO:0043197`, `GO:0098978` | Euteleostomi | — | **not inherited by ARHGAP4** |

Three readings follow.

1. `PTN002680572` is seeded by `UniProtKB:P98171` alone. Per `CLAUDE.md` this is the
   expected marker that experimental grounding exists on the target — ARHGAP4 has
   cytoplasm by IDA — and is explicitly **not** circular.
2. `GO:0051963 regulation of synapse assembly` is the only inherited assertion whose seed
   set contains no ARHGAP4-lineage member, and two of its four seeds are SRGAP2B and
   SRGAP2C, partial duplicates of SRGAP2 that arose on the human lineage.
3. The same curator put the *synaptic localisation* terms on a **sibling** node that
   ARHGAP4 does not inherit. The exclusion of ARHGAP4 from the synaptic compartment was
   drawn deliberately, which is what makes the synapse-assembly inheritance anomalous.

The self-test requires the join to find both an inherited node and a non-inherited one;
if every node came back inherited the join key would be wrong and reading 3 would be
vacuous.

## 5. `comparator_terms.py` — the check that refuted three of my own four proposals

Four term replacements looked right on reading. Each is a falsifiable prediction about
other genes, so it was tested against seven well-curated RhoGAPs (ARHGAP1, ARHGAP35,
ARHGAP17, ARHGAP21, ARHGAP24, SRGAP2, DLC1) before being acted on.

| proposal | comparators on current | on proposed | verdict |
|---|---|---|---|
| `GO:0007266` → `GO:0035023` / `GO:0035024` | 2/7 | 1/7, 2/7 | **dropped** |
| `GO:0007165` → `GO:0035023` | **7/7** | 1/7 | **dropped** |
| `GO:0005737` → `GO:0005938` cell cortex | 4/7 | **0/7** | **dropped** |
| `GO:0007010` → `GO:0051497` | **0/7** | 1/7 (DLC1, IDA) | **kept** |

- `GO:0007266` on a RhoGAP is established practice (ARHGAP1 by TAS, ARHGAP35 by IBA), not
  an error to correct.
- `GO:0007165` is a uniform InterPro2GO product on all seven, so rewriting one gene's row
  would be idiosyncratic and would not survive the next mapping refresh.
- No comparator carries `GO:0005938`, despite the 1996 paper describing "a narrow
  cytoplasmic region just below the plasma membrane". That observation is therefore
  recorded as a knowledge gap rather than as an annotation.
- `GO:0007010 cytoskeleton organization` is the real outlier: **no** comparator carries
  it, and the cited observation is inhibition of stress fibres, which is a regulation
  term. This is the one `MODIFY` in the review.

The query aborts on pagination rather than truncating, because a clipped page turns a
present term into an absent one; the self-test exercises that on TP53.

## 6. `impc_phenotypes.py` — a tested absence, not an untested one

Four rows of the review argue that ARHGAP4 is dispensable, and each leans on the mouse
knockout having no phenotype. Stated as "IMPC reports zero significant phenotypes" that
claim is unverifiable and, worse, ambiguous: **an untested gene returns exactly the same
zero.** Two Solr cores separate the cases — `genotype-phenotype` holds one document per
*significant* association, `statistical-result` one per *test performed*.

| gene | significant | tests | verdict |
|---|---|---|---|
| **Arhgap4** | **0** | **413** | tested and clean |
| Srgap2 | 0 | 46 | tested and clean |
| Srgap1 | 0 | **0** | **untested** — the zero says nothing |
| Srgap3 | 0 | **0** | **untested** — the zero says nothing |
| Lepr *(positive control)* | 105 | 244 | — |
| Dmd *(positive control)* | 23 | 842 | — |
| Trp53 *(positive control)* | 6 | 653 | — |

413 tests and nothing significant is a real negative result. Srgap1 and Srgap3 sitting at
0/0 in the same table is what makes that reading legible rather than assumed, and the
self-test requires one of them to still be untested — if the paralogs are ever phenotyped
the guard fails loudly rather than quietly losing its comparator. The run aborts if a
positive control comes back empty, since that would mean the query shape is wrong and no
zero in the table could be trusted.

Note on the two counts for a positive control: Lepr reports **105 associations** but
**49 distinct MP terms**, and that gap is real rather than a truncation. One association
is one (allele, zygosity, sex, parameter) result, and several map to the same MP term.
The term list is fully paginated and `significant_terms()` raises if it reads fewer
documents than the service reports, which the self-test exercises by forcing a 10-row
page size and requiring the result to equal the default-page result. An earlier version
capped at one 50-row page while the count came from an independent `numFound`, so a
silently short list sat beside a correct count — caught in review, not by the script.

This does not say ARHGAP4 does nothing. It says the knockout was looked at hard, in a
standardised pipeline, and nothing measurable fell out — which is what a redundancy
hypothesis predicts, and which is the version of the claim the review makes.

## 7. `audit_review.py` — invariants over the review document

Six checks, none of which the repository validator covers. Current state: **23 GOA data
rows to 23 non-NEW entries**, **38 quotes verified verbatim** under whitespace
normalisation, all six invariants holding.

1. **Row reconciliation** against the GOA TSV by `(term, evidence, reference, with/from)`
   multiset. The `fetch-gene` stub is known to collapse distinct `GO:0005515` partner
   rows into one entry; here it did not, but the correspondence is asserted rather than
   eyeballed.
2. **Duplicate YAML keys**, via a `SafeLoader` subclass that raises on a repeat. PyYAML
   keeps the last occurrence and discards the earlier one silently, so data destroyed by
   parsing cannot fail any gate that walks the parsed document.
3. **Quote verbatimness for both `PMID:` and `file:` references.** CI checks only the
   former, and an agent in this campaign fabricated two `file:` quotes that passed every
   gate.
4. **No line of a wrapped scalar ends in a hyphen.** YAML folds a newline into a space,
   so `A-kinase-\nanchoring` publishes as `A-kinase- anchoring`; both forms are legal, so
   only rendering shows the damage.
5. **No row left `PENDING`**, no surviving `TODO`, `status: COMPLETE`.
6. **Reference completeness** — every `PMID:` cited anywhere resolves to a `references`
   entry. The repo validator only checks `original_reference_id`.

Check 6 caught a real defect on its first run: `PMID:10425039`, `PMID:18489790`,
`PMID:22965914` and `PMID:40817404` were named in `review_notes` without being declared,
and adding them as full entries is what brought in the Schöneberg 16-year follow-up,
which is now the strongest single piece of evidence in the review.

Its scope is deliberately narrow in one place. It strips **only** the reference `id`
lines before scanning for citations: scanning the whole `references` block would let a
deleted entry satisfy the check with its own id, and excluding the block entirely would
lose PMIDs cited inside another entry's notes — which is exactly where all four of the
above were.

Two other things went wrong while writing it, both caught by running it rather than by
reading it. `repo_root()` probed for a `publications/` directory and resolved to
`genes/human`, because a stray `genes/human/publications/PMID_12345.md` exists in this
repo from an old cache-warming run; it now requires `pyproject.toml` alongside. And the
self-test's mutation anchor for check 3 matched **twice**, because the same sentence
appears under an annotation's `supported_by` and under the reference's `findings` — the
exactly-once assertion fired instead of silently mutating the wrong row, which is the
behaviour it exists for.

---

## What none of these can check

None of these scripts validates a quote **against the claim it is attached to**. They
confirm that a term is merged, that a residue is an arginine, that a reference produced
*n* annotations — all mechanical. Whether a `supporting_text` actually supports the
sentence above it was checked by re-reading each `summary` next to its quote, and that
remains the weakest link. Nor can they resolve the two substantive unknowns: which
Rho-family GTPase ARHGAP4 acts on in a cell, and why losing the gene costs neither mouse
nor human anything measurable.
