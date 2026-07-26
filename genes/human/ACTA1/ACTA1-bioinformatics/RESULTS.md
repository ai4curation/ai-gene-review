# ACTA1 bioinformatics: WITH/FROM provenance and actin-isoform peptide specificity

Two analyses plus two consistency checks. Run each with `uv run python <script>` from the
repository root. The two analyses are stdlib-only; the two checks additionally use `yaml`
and `ruamel.yaml`, both already in the project environment.

| script | question | output |
|---|---|---|
| `resolve_withfrom.py` | Who are ACTA1's WITH/FROM donors, and what evidence does each carry for the term it donated? | `withfrom_resolution.json` |
| `actin_peptide_specificity.py` | Can shotgun proteomics attribute an actin peptide to ACTA1 specifically? | `peptide_specificity.json` |
| `build_source_entities.py` | Do the review's `source_entities` and `supporting_entities` still match the GOA? | rewrites the review YAML; `--check` verifies |
| `audit_claims.py` | Do the review, the notes and this file still agree on every load-bearing number? | `--self-test` exercises the checks |

Re-run order after any change: `resolve_withfrom.py` and `actin_peptide_specificity.py`
(recompute), then `build_source_entities.py` (rewrite), then `audit_claims.py` (verify).

`resolve_withfrom.py --self-test` exercises five guards, each stating the failure it
prevents. Two of them were written *because* they caught a defect in an earlier
version of this script (see "Guards" below).

---

## 1. WITH/FROM resolution: every donor resolves, and every donor is real

Counts are derived from the GOA TSV, never by hand: the script asserts that the
number of resolved sources equals the number of `|`-separated tokens in column 11
for every row.

**26 GOA rows carry a WITH/FROM field. Zero unresolved tokens, zero unverified
mappings.** Each model-organism resolution is confirmed against the resolved
UniProt entry's own cross-references, so a free-text match cannot pass as a
mapping.

### The two phylogenetic rows are well founded

| row | term | protein donors | with own experimental evidence for the term | reviewed (Swiss-Prot) |
|---|---|---|---|---|
| 1 | `GO:0015629` actin cytoskeleton | 24 | **24 / 24** | 22 / 24 |
| 2 | `GO:0005200` structural constituent of cytoskeleton | 10 | **10 / 10** | 10 / 10 |

These are two separate numbers on purpose. The two unreviewed donors on row 1
(`CGD:CAL0000191211` → A0A1D8PFR4, *C. albicans* ACT1; `WB:WBGene00000067` →
O45815, *C. elegans* act-5) both carry their own IDA, but neither entry's *name* is
citable as evidence of what the family does, because the names are automatic.

`GO:0005200` is asserted at exactly one node in PTHR11937 — `PTN000940351`, the
conventional-actin node — and **negated by IRD at eight descendant nodes**. ACTA1
sits on the accepting side of that split, which is the whole point of this gene:
it is the recipient the term was meant for. Its ten donors include human ACTB
(`EXP`, `IDA`, `IMP`, `TAS`), *S. cerevisiae* ACT1, ARP1 and ARP10, and human ARP2
and ARP3.

### Four rows are self-referential, and that is valid

Rows 3-6 (`GO:0001725`, `GO:0005865`, `GO:0005884`, `GO:0030240`) have WITH/FROM
`PANTHER:PTN000233075 | UniProtKB:P68133` — ACTA1 itself. The PAINT file confirms
all four as IBD at `PTN000233075` seeded from `UniProtKB:P68133`, taxon 32523
(Tetrapoda), dated 2019-03-01. This records a PAN-GO curator judging those four
terms core for ACTA1; it is not circularity. It does mean, however, that the
quality of each row is exactly the quality of the ACTA1 experimental annotation
underneath it — which matters for `GO:0001725` (see §3).

### The single defective block: five ISS rows from a chicken *smooth-muscle* actin

Rows 19-23 (`GO:0010628` positive regulation of gene expression, `GO:0030027`
lamellipodium, `GO:0030175` filopodium, `GO:0044297` cell body, `GO:0090131`
mesenchyme migration) all have WITH/FROM `UniProtKB:P08023`, which resolves to
**ACTA2 — actin, aortic smooth muscle — of *Gallus gallus***.

The donor's evidence is sound, not weak: P08023 carries all five terms itself by
IDA/IMP, and all five trace to **one paper**, PMID:10633868, an antisense-knockdown
study of endothelial-mesenchymal transformation in chick cardiogenesis.

What is wrong is the propagation, on three counts:

1. **Wrong paralog.** Chicken ACTA2 is the ortholog of human *ACTA2*, not of human
   ACTA1. Chicken has its own ACTA1 (`P68139`, ACTS_CHICK) — the correct ortholog
   exists in the same species and was not used.
2. **Wrong tissue and process.** Lamellipodium, filopodium, cell body and
   mesenchyme migration are properties of a migratory mesenchymal cell.
   `GO:0044297` is defined as "the portion of a cell bearing surface projections
   such as axons, dendrites, cilia, or flagella"; ACTA1 is a sarcomeric
   thin-filament protein.
3. **ISS cannot discriminate here.** See §2: ACTA1 is 97.9% identical to ACTA2 and
   98.9% to ACTC1, so a sequence-similarity transfer between α-actins is satisfied
   trivially and carries no isoform information.

**Scope, from QuickGO.** The block did not land on ACTA1 alone. It is present, by
ISS/AgBase, on **all four human α-actins and on mouse Acta1**:

| gene | legitimate recipient? |
|---|---|
| ACTA2 (P62736) aortic smooth muscle | **yes** — true ortholog of the donor |
| ACTG2 (P63267) enteric smooth muscle | arguable — smooth muscle |
| **ACTA1 (P68133) skeletal muscle** | **no** — sarcomeric |
| **ACTC1 (P68032) cardiac muscle** | **no** — sarcomeric |
| mouse Acta1 (P68134) | **no** — sarcomeric |

The cytoplasmic actins ACTB and ACTG1 did **not** receive it. So the block was
propagated by α-actin-ness, spraying a smooth-muscle-specific developmental
finding onto the striated-muscle actins. Retracting it from ACTA1, ACTC1 and mouse
Acta1 fixes three genes in one edit.

---

## 2. Actin-isoform peptide specificity

`actin_peptide_specificity.py` fetches all six conventional human actins, does an
in-silico trypsin digest (cleave C-terminal to K/R, not before P; up to 2 missed
cleavages), and asks how much of ACTA1's MS-detectable peptide space is
distinguishable from the other five.

Missed cleavages are *included* deliberately: a peptide spanning a missed site is
more likely to carry an isoform-specific residue, so excluding them would bias the
answer towards "distinguishable".

### Identity

ACTA1|ACTA2 **97.9%**, ACTA1|ACTC1 **98.9%**, ACTA2|ACTC1 98.4%, ACTB|ACTG1 98.9%.
The isoforms are 375-377 aa (they differ in N-terminal processing), so 11 of the 15
pairs are unequal-length and are reported as skipped rather than compared off-frame;
the script names them.

### Peptides

| quantity | value |
|---|---|
| ACTA1 tryptic peptides, 7-30 aa | 63 |
| distinguishing (present in no other human actin) | **9 (14.3%)** |
| shared with ≥1 other human actin | 54 |
| of those, shared with ACTB and/or ACTG1 | **29** |
| **independent** distinguishing regions | **3** |

The nine peptides collapse to three regions, because most are nested
missed-cleavage variants of the same span. Reporting nine would overstate the
evidence:

- `1-30` `MCDEDETTALVCDNGSGLVKAGFAGDDAPR` (the N-terminus, where actins diverge)
- `287-317` `CDIDIRKDLYANNVMSGGTTMYPGIADRMQK`
- `338-361` `KYSVWIGGSILASLSTFQQMWITK`

### What this does and does not establish

**It does not refute the five HDA rows** (`GO:0070062` ×3, `GO:0072562`,
`GO:0005576`), placing ACTA1 in prostatic-secretion exosomes, parotid exosomes,
trabecular-meshwork exosomes, plasma microparticles and tears. Three distinguishing
regions exist, so ACTA1-specific attribution is achievable, and a study reporting a
peptide from one of them would settle the matter.

**What it establishes is that attribution is not automatic.** 85.7% of ACTA1's
detectable peptide space is shared, and 29 of those peptides are shared with ACTB
and/or ACTG1 — which are expressed in every tissue those five studies sampled,
whereas none of the five sampled skeletal muscle (HPA: ACTA1 is "Tissue enriched
(skeletal)"). So these rows are **untested rather than confirmed**: they rest on an
isoform assignment that the analysis shows cannot be assumed.

This is the same distinction the ACTL8 review drew between its filament-interface
result (refuted) and its ATP-site result (untested) — reported separately because
the evidence differs in strength.

---

## 3. Checks run that came back negative

Recorded so the next reviewer knows they were run, not skipped.

- **Reference-projection check** (the ACTR8 defect). Every one of ACTA1's
  functional and localisation references was queried by PMID in QuickGO and counted
  by entity. `PMID:1423520` → **1** annotation total; `PMID:11333380` → **1**;
  `PMID:15198992` → **3**, all on ACTA1; `PMID:12849983` → **3** (2 on ACTA1, 1 the
  reciprocal on DNASE1); `PMID:10508519` → **5**, all on ACTA1. **No projection:**
  no reference annotates a complex plus its subunits, and no phenotype term spreads
  beyond the gene assayed. The high-count references (`PMID:32814053` → 20,010;
  `PMID:33961781` → 9,514; `PMID:28514442` → 3,731) are declared screens whose
  evidence codes already say so.
- **Retraction / erratum / expression-of-concern check.** 28 cited PMIDs were read
  from `CommentsCorrections/RefType` on each *cited* article's own PubMed record —
  not by a publication-type search, which cannot see a Publisher Correction. **Zero
  flagged.**
- **IBA-precision check** (the ACRV1 defect: a propagation landing above its
  donor). Rows 3-6 land at the *same* terms their donor holds, because the donor is
  ACTA1 itself. No downward MODIFY warranted.
- **Heterogeneous-donor / LCA check** (the AADACL4 caveat) on `GO:0005200`. It does
  **not** apply: the donor set agrees — all ten are conventional actins or Arps that
  hold `GO:0005200` themselves — so the term is not a broad LCA papering over a
  mixed clade, and no specificity upgrade is available or needed.
- **Partner-accession check** (the ACRV1 TrEMBL/ORFeome substitution). All ten
  annotated interaction partners resolve to **reviewed** entries. The one non-canonical
  identifier is `Q6ZQX7-4`, which is a declared *isoform* of LIAT1 rather than a
  partial clone.

## 4. Keeping the numbers honest

Two of the four scripts exist only to stop the review's own claims drifting, because
that - not a wrong term or a fabricated quote - is what has actually gone wrong most
often in this campaign: one claim asserted at several sites and corrected at all but one.

`build_source_entities.py` is the **only** thing that writes `source_entities`. Every
hand-maintained source list in this campaign has drifted, and the drift was only ever
caught by scripting a diff against the GOA. It also verifies the hand-restored
`supporting_entities`: the `fetch-gene` stub collapsed the seven `PMID:32814053`
interaction rows into one, and since those seven share a
(term, evidence, reference) key the test is a multiset comparison against the GOA's
WITH/FROM fields under that key - **11 interaction rows match one-to-one, no duplicates,
no omissions, no invented partners.** It checks the converse direction too, so a dropped
row is an error rather than an absence.

Two things it got wrong first:

- **The three-part key is not unique.** The first version asserted it was and aborted on
  the seven interaction rows. The assertion was right to fire; the fix is that a key maps
  to a *list* of token lists, and uniqueness is demanded only where one answer is needed.
- **`yaml.safe_load` + `yaml.dump` is not a round trip.** It reflowed every prose scalar
  and deleted all 36 section comments - a mutation far larger than the intended one, and
  invisible to a re-run of the checker. It now uses `ruamel.yaml` round-trip mode and
  refuses to write if the comment count drops.

`audit_claims.py` pins the numbers that appear on more than one prose surface (the review
YAML, the notes, this file) and derives every expected value **from the JSON outputs, not
from literals**, so a recomputation that changes a number fails the lint instead of
silently disagreeing. It also carries a list of *retracted* phrasings - each one a claim
that was wrong at some point in this review's history - and fails if any reappears. Its
own two false positives are worth recording: claims routinely straddle a line break in
wrapped prose (fixed by matching whitespace-normalised text), and prose legitimately
spells a small count as a word in one place and a digit in another (fixed by letting a
claim carry equivalent variants). Both were reporting a regression where none existed,
which is how a lint gets switched off.

## 5. Guards

`resolve_withfrom.py --self-test` has five cases. Three are ordinary; two exist
because they caught real defects in this script:

- **Case 2** pairs a real WITH/FROM token with a real but unrelated accession and
  requires verification to *fail*. Without it the mapping check would be decorative.
- **Case 4** revealed that the accession-match liveness guard is **insufficient**.
  `O15507` — the dead accession the ACTR10 review found — comes back *with its own
  `primaryAccession`* and an otherwise empty record, so matching the accession
  passes it. The authoritative signal is `entryType: "Inactive"`, and UniProt
  further reports `inactiveReason: {MERGED → P56159}`. The guard now reads that
  field and names the replacement. Case 5 then requires a live accession to still
  pass, so the guard discriminates rather than refusing everything.
- **Case 3** covers a silent zero: QuickGO's annotation endpoint **rejects every
  non-UniProtKB gene-product id** used in this file's WITH/FROM fields (`MGI:`,
  `SGD:`, `RGD:`, `WB:`, `dictyBase:`, `PomBase:`, `FB:`, `CGD:` all return HTTP
  400). The script treats 400 as non-retryable, re-queries via the resolved UniProt
  accession, and records the fallback route in the output. An earlier version
  returned a vacuous `0` for the four WormBase donors, which read as "these sources
  carry no evidence" when in fact they had never been asked.
