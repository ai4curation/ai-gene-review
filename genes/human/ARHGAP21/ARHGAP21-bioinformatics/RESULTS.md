# ARHGAP21 provenance analyses — results

Five checks supporting `genes/human/ARHGAP21/ARHGAP21-ai-review.yaml`. All are
rerunnable and derive the repo root rather than hardcoding a worktree path.

```bash
uv run --with requests python resolve_partners.py      # -> partners.json
uv run --with requests python check_corrections.py     # -> corrections.json
uv run --with requests python check_gap_terms.py       # -> gap_terms.json
uv run --with requests python reference_coverage.py    # -> reference_coverage.json
uv run --with requests python intact_methods.py        # -> intact_methods.json
uv run python audit_review.py --self-test              # invariants over the review YAML
```

`audit_review.py` needs no network. The other four query UniProt, QuickGO,
NCBI E-utilities and IntAct, so their JSON outputs are committed as the record
of what those services returned.

---

## 1. `check_gap_terms.py` — GO cannot express GAP substrate specificity

The headline result. Each historical substrate-specific GAP term was resolved
through QuickGO's `/complete` endpoint, which is the only endpoint that
distinguishes a **merged** id from an **absent** one (OLS reports both
identically).

| requested | resolves to |
|---|---|
| `GO:0005099` Ras GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0005100` Rho GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0008060` ARF GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0005097` Rab GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0017137` Rab GTPase binding | **MERGED** → `GO:0031267` |
| `GO:0017048` Rho GTPase binding | **MERGED** → `GO:0031267` |

`GO:0005096` has **0 `is_a` children** (its only child is `GO:1902773 GTPase
activator complex`, via `capable_of`).

**Consequence.** `GO:0005096` is already maximal, so ARHGAP21's contested
substrate preference — Cdc42 vs RhoA vs RhoC — is not expressible in the GO
molecular-function branch. No replacement term is proposed and no new term is
requested, since the merge was deliberate. Substrate identity is instead recorded
as `core_functions[].substrates` and as `has_input` (`RO:0002233`) extensions.

A separate query settles the PDZ question: a QuickGO full-text search over GO
returns exactly two PDZ terms, one obsolete. The survivor, `GO:0030165`, is
defined *"Binding to a PDZ domain of a protein"* — the ligand side — and has no
descendants. GO has no term for the PDZ-domain side of a PDZ/PBM pair.

## 2. `reference_coverage.py` — coverage, not over-annotation

QuickGO queried **by reference**, not by gene. None of the ten primary-paper
result sets was paginated, so these counts are complete.

| PMID | annotations in all GOA | on ARHGAP21 |
|---|---|---|
| 15793564 Dubois 2005 | 1 | `GO:0005096` IDA |
| 16184169 Sousa 2005 | 2 | **0** (both on CTNNA1) |
| 16527809 Klein 2006 | 0 | 0 |
| 17347647 Ménétrey 2007 | 2 | `GO:0005515` IPI |
| 20525016 Hehnly 2010 | 12 | 5 rows |
| 21173159 Anthony 2011 | 0 | 0 |
| 22922005 Bigarella 2012 | 0 | 0 |
| 23200924 Lazarini 2013 | 0 | 0 |
| 23235160 Barcellos 2013 | 0 | 0 |
| 29212046 Rodrigues 2017 | 0 | 0 |

**Seven of ten primary papers produced no GO annotation anywhere.** Every paper
reporting RhoA or RhoC activity is in that set, so the GO record is silent on
that half of the literature for a reason independent of the ontology gap.

**Symbol-collision check: negative.** Both 2005 papers call the protein
ARHGAP10, which is this gene's former symbol and now belongs to a different gene
(`A1A4S6`). No annotation from any primary paper landed on `A1A4S6`. The seven
large-scale screens are paginated, so for those the check is reported as *not
possible* rather than as clean — an empty first page of 18,539 annotations is
not evidence.

## 3. `intact_methods.py` — per-partner evidence quality

502 IntAct rows, 440 distinct partners. Domain column maps IntAct's recorded
participant ranges onto UniProt's domains (PDZ 50–159, PH 931–1040, RhoGAP
1147–1339).

| partner | rows | distinct pubs | ARHGAP21 domain | methods |
|---|---|---|---|---|
| YWHAZ | 5 | **4** | – | anti tag coip; BioID; pull down |
| SFN | 4 | 2 | – | BioID; tap |
| Arf1 | 3 | 1 | **PH** | cosedimentation; **x-ray diffraction** |
| CFTR | 7 | 2 | **PDZ** | holdup; BioID |
| CTNNB1 | 3 | 3 | **PDZ** | anti tag coip; holdup; tap |
| AXIN1 | 2 | 2 | **PDZ** | anti tag coip; holdup |
| APC | 2 | 2 | **PDZ** | anti tag coip; holdup |
| MYO18A | 2 | 2 | **PDZ** | anti tag coip; holdup |
| SAPCD1 | 3 | 3 | **PDZ** | anti tag coip; holdup |
| PTEN | 2 | 1 | **PDZ** | holdup |
| RPS6KA1 | 2 | 1 | **PDZ** | holdup |
| E6 (HPV16) | 2 | 1 | **PDZ** | holdup |
| E6 (HPV18) | 2 | 1 | **PDZ** | holdup |
| EEF1D | 2 | 1 | – | display technology; tap |

Two conclusions the GOA rows alone cannot give:

- Every `holdup assay` row maps to the **PDZ domain**. This mattered because
  `PMID:36115835`'s full text never names ARHGAP21 (0 occurrences of `ARHGAP` in
  302 kB), so the claim had to be checked against participant ranges rather than
  assumed.
- **14-3-3 binding is genuinely replicated** — 4 distinct publications and 3
  orthogonal methods for YWHAZ — not one screen logged under several sub-method
  names. This is what justifies modifying those rows to `GO:0071889` while the
  other generic-binding rows are removed.

*Implementation note.* The first version parsed IntAct ids as `db:ACC` and
reported **0 partners from 502 rows**, i.e. every GOA partner "ABSENT" — a
silent zero that reads as a finding. IntAct's format is `ACC (db)`. The script
now asserts that a non-zero fraction of rows parsed and that not every GOA
partner is absent, so the same failure would abort rather than report.

## 4. `resolve_partners.py` — WITH/FROM and partner identities

15 distinct accessions: **0 dead, 0 TrEMBL, 15 reviewed Swiss-Prot**, 3
non-human (mouse Arf1 `P84078`, HPV16 E6, HPV18 E6).

**The one `Xeno` flag is harmless.** UniProt records ARHGAP21's ARF1 interaction
against mouse `P84078` rather than human `P84077`, which would normally mean an
`IPI` row asserts a cross-species interaction. Fetching both FASTA records shows
they are **sequence-identical, 181 aa**. Bookkeeping, not a biological defect —
recorded as a negative result.

All seven IBA rows are **self-referential**: WITH/FROM is `PANTHER:PTN…` plus
ARHGAP21's own accession `Q5T5U3`. That is the expected marker of a PAINT
curator judging the function core, classified `NO_FAILURE_CORE`, never
`CIRCULAR_OR_REDUNDANT`. Two nodes are involved: `PTN008592632` carries
`GO:0005096`; `PTN002754039` carries the six Golgi / actin / junction /
microtubule-transport terms.

PANTHER `PTHR23175` holds **5182 proteins**, of which **7 are reviewed
(Swiss-Prot)** — the entries CSV is the Swiss-Prot subset, not the family.
ARHGAP21 sits in SF16 with its mouse and *Xenopus* orthologs; **ARHGAP23**
(`Q9P227`) is the close paralog, in SF5. ARHGAP10 (`A1A4S6`) is absent from the
family, so the symbol collision is not a phylogenetic relationship.

## 5. `check_corrections.py` — retractions and errata

`CommentsCorrectionsList/RefType` read off each cited article's own PubMed
record. This is the only way a Publisher Correction is discoverable; a
publication-type query cannot see one.

All **30** cited PMIDs returned. **One** flag: `PMID:36115835` →
`PMID:36477203`, an Author Correction whose scope is *"errors in Fig. 2, Fig. 4
and Fig. 5"* — missing PCC values, axis labels, legends and panel ordering.
**Cosmetic; no data changed**, so the interactions it reports stand. **No
retractions.**

Mutation-tested by inserting `PMID:32125225`, a known retracted paper, which the
checker flagged `retracted_by_pubtype=True` with `RetractionIn: PMID:35078223`.

## 6. `audit_review.py` — invariants over the review YAML

Current state: **47 GOA data rows → 47 non-NEW entries + 4 NEW = 51**, and **50
`supporting_text` quotes verified verbatim** under whitespace normalisation.

Checks, each covering something the repo validator does not:

1. **Row reconciliation** against the GOA TSV by `(term, evidence, reference,
   with/from)` multiset. The `fetch-gene` stub is known to collapse distinct
   `GO:0005515` partner rows; here it did not, but the count is asserted rather
   than eyeballed.
2. **Duplicate YAML keys**, via a `SafeLoader` subclass that raises on repeats.
   PyYAML keeps the last occurrence and discards the earlier one silently, and
   every other gate in this repo walks the *parsed* document — so data destroyed
   by parsing cannot fail them.
3. **Quote verbatimness** for both `PMID:` and `file:` references. CI checks only
   the former.
4. **No row left `PENDING`**, no surviving `TODO`, `status: COMPLETE`.

`--self-test` mutates an in-memory copy for each check and requires the check to
fire; every mutation asserts its anchor exists first, so a drifted anchor is an
error rather than a false pass. A passing self-test proves the guards that exist
work — it cannot say which guard was never written.

### What no script here can check

None of these gates validates a quote **against the claim it is attached to**.
Two rows in this review initially carried a verbatim, correctly-attributed quote
from `PMID:15161933` describing *that* paper's 14-3-3 affinity-column method,
sitting under summaries about BioPlex AP-MS. Every mechanical check passed. It
was found by re-reading each `summary` next to its quote, and fixed by quoting
each row's own paper.

Review round 2 found **four more of the same class**, which is the strongest
available evidence that this gap is structural rather than a one-off:

- `GO:0032956`'s summary asserted a stress-fibre phenotype that appears nowhere
  in the cited abstract (it is a UniProt `MISCELLANEOUS` line, and one that
  spans a `CC` continuation so it cannot be quoted verbatim at all).
- The same row's `reason` justified its evidence code using the *other* NEW
  row's two-hybrid partner.
- `GO:0051684` **maintenance** of Golgi location was quoted with the
  nocodazole-washout sentence, which is **establishment** evidence.
- `GO:0005794` IDA was quoted with an introduction sentence ending in reference
  callouts "(23, 24)" — prior work, not the paper's own observation.

All four passed every gate here: real PMIDs, verbatim strings, correct terms,
correct actions. Two cheap heuristics came out of it and are worth applying
before attaching any quote to an experimental row: **a sentence containing
reference callouts is background, not result**, and **check that the assay in
the quote is the assay the term names** (re-establishment after dispersal is not
maintenance).
