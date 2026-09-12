# AGGF1 (Q8N302) — bioinformatics results

Everything below is produced by the scripts in this folder from live UniProt /
QuickGO / IntAct / NCBI queries. Nothing is hand-entered except the literature
anchor residues in `domain_residues.py`, which are re-verified against the live
sequence at run time and abort the script on mismatch.

```
uv run python resolve_withfrom.py    # WITH/FROM resolution + donor evidence
uv run python gap_by_reference.py    # QuickGO-by-reference; G-patch reference class
uv run python intact_partners.py     # IntAct, paginated; per-partner detail
uv run python domain_residues.py     # FHA and G-patch residue conservation
uv run python retraction_check.py    # retraction / erratum / EoC
uv run python check_terms.py         # QuickGO obsoletion + secondaryIds
uv run python reconcile_goa.py       # GOA rows <-> existing_annotations
```

The gene's own name, *Angiogenic factor with G-patch and FHA domains 1*, makes
three separable claims. They are tested separately, and they do not all survive
in the same form.

---

## 1. The G-patch is intact and canonical — 8/8

`domain_residues.py` pulls every reviewed human protein carrying an annotated
G-patch (`IPR000467`) — **34 annotated domains across 33 proteins** — aligns each
to AGGF1's domain-local window (619–665 ± 30) and computes per-column agreement.
Nothing about the panel or the columns is hand-picked.

| AGGF1 position | panel consensus | agreement | AGGF1 has | |
|---|---|---|---|---|
| 631 | G | 100% of 34 | G | match |
| 635 | G | 97% | G | match |
| 637 | G | 97% | G | match |
| 638 | L | 94% | L | match |
| 639 | G | 100% | G | match |
| 644 | G | 94% | G | match |
| 659 | G | 82% | G | match |
| 661 | G | 85% | G | match |

**8/8.** AGGF1's G-patch is not a degenerate remnant.

Mapping the same eight columns onto **NKRF** — the one human G-patch resolved in
complex with DHX15 (PMID:32179686), so a position whose structural role is known
rather than merely conserved — gives 8/8 again, every residue identical and every
one inside NKRF's own annotated G-patch:

```
AGGF1 G631 <- NKRF G563    AGGF1 G639 <- NKRF G570    AGGF1 G659 <- NKRF G590
AGGF1 G635 <- NKRF G566    AGGF1 G644 <- NKRF G575    AGGF1 G661 <- NKRF G592
AGGF1 G637 <- NKRF G568    AGGF1 L638 <- NKRF L569
```

Three of these are carried into the review YAML as `residue_claims`, including the
one non-glycine column (L638/L569), which is there to test the alignment rather
than to re-confirm a glycine-rich stretch.

## 2. …but `GO:0003676 nucleic acid binding` is a domain-name mapping, not a measurement

`gap_by_reference.py` asks what molecular function GO actually gives the G-patch
proteins, using the two DEAH helicases DHX15/DHX16 as controls:

```
G-PATCH REFERENCE CLASS SUMMARY (controls DHX15/DHX16 excluded): 12 queried, 11 reported;
  11 carry GO:0003676 nucleic acid binding;
  11 carry it by IEA and NOTHING ELSE;
  0 carry it with any experimental code;
  6 carry GO:0003723 RNA binding (or a child) with an experimental code.
```

So across **every** reviewed human G-patch protein the query reports — NKRF,
GPKOW, RBM17, SUGP1, CMTR1, GPATCH1, GPATCH4, RBM5, PINX1, ZGPAT and AGGF1 —
`GO:0003676` is carried by IEA and by nothing else. Not one instance anywhere in
the class rests on an experiment. Where anyone *has* measured, the answer lands
on the child term `GO:0003723 RNA binding` (NKRF HDA; GPKOW IDA+IMP; SUGP1 HDA;
GPATCH4 HDA; RBM5 HDA+IDA; PINX1 `GO:0070034` IDA).

(TFIP11 returned 318 MF annotations, past the page limit, and is reported as
truncated rather than counted — `qg()` refuses to read a page total as a whole.)

## 3. The FHA is intact at every phosphothreonine-anchoring position — but nothing has been measured

Two methods, because the first one has no power here.

**Column consensus fails on FHA and that is itself informative.** The same
panel machinery run over `IPR000253` gives **32 annotated FHA domains across 32
reviewed human proteins** (AFDN, CEP170, CHEK2, FOXK1/2, the KIF13/14/16/1
kinesins, MCRS1, MDC1, MKI67, NBN, RNF8, TIFA …) with a **maximum per-column
agreement of 0.69** and therefore **zero** columns above the 0.80 threshold. The
human FHA superfamily is too divergent for consensus scoring. Reporting `0/0`
rather than lowering the threshold until something appeared is the point.

**Literature-anchor transfer does work.** Phosphothreonine recognition needs an
Arg in the β3–β4 loop preceded by a Gly, a Ser in β4–β5, and an Asn in β6–β7
(Durocher et al. 2000, PMID:11106755). Anchors are taken from two structurally
characterised FHA domains, verified against the live sequence, and transferred by
**domain-local** alignment:

| anchor | → AGGF1 | identical | inside AGGF1 FHA (434–487) |
|---|---|---|---|
| CHEK2 G116 | **G437** | yes | yes |
| CHEK2 R117 | **R438** | yes | yes |
| CHEK2 S140 | **S454** | yes | yes |
| CHEK2 N166 | **N478** | yes | yes |
| Rad53 FHA1 S85 | **S454** | yes | yes |
| Rad53 FHA1 N107 | **N478** | yes | yes |
| Rad53 FHA1 G69 | gap | — | — |
| Rad53 FHA1 R70 | gap | — | — |

**6/8 strict.** The two anchor sets are independent and **agree exactly wherever
both resolve** (S454, N478); the two that gap out are the β3–β4 loop pair, which
is the most variable region and which the closer human anchor resolves. AGGF1
therefore retains the complete canonical FHA pThr-recognition set
**G437-R438, S454, N478**.

### The mutational data agree on the same surface

`PMID:33069768` assayed six COSMIC somatic FHA-domain missense changes.
Loss of function: **G437E**, Q467H, Y469N, N483T. **No effect: R447Q and V497I.**
Set against the alignment: **G437 is the conserved Gly of the pThr-anchoring
G-R pair**, while R447 is *not* the conserved Arg (that is R438, nine residues
earlier) and V497 lies outside the annotated 434–487 core entirely. A mutation on
the predicted anchor is damaging; two mutations off it are not.

### What is still missing, and it is the whole claim

**No experiment has ever measured phosphopeptide, phosphothreonine or
phospho-dependent binding by AGGF1's FHA domain.** The two published FHA
functions are both plain co-immunoprecipitation with deletion constructs:
p53 (PMID:33069768) and 14-3-3α/β (PMID:33471274). Neither used a phosphatase, a
phospho-site mutant, or peptide competition. There is also **no experimental
structure of any part of human AGGF1** (UniProt Q8N302 carries zero PDB
cross-references).

So the FHA half of the gene's name is **untested, not refuted** — and a retained
site is not an activity. No phosphoprotein-binding term is proposed here.

## 4. Every AGGF1 interaction that GOA annotates, by independent experiment

`intact_partners.py` paginates IntAct to completion (**742 evidence records,
695 distinct partners, 22 publications**; the guard compares accumulated rows to
the server's own `totalElements`, never to the page size). `NbExp=3` is one
screen logged three ways, so the records are expanded:

| GOA partner | IntAct records | independent experiments |
|---|---|---|
| **O43143 DHX15** | 3 | **1** — HuRI Y2H (PMID:32296183) as array + prey-pooling + "validated two hybrid" |
| **Q96EZ8 MCRS1** | 3 | **1** — same HuRI screen, same three sub-methods |
| **Q9NVF7 FBXO28** | 3 | **1** — same HuRI screen, same three sub-methods |
| **Q8N8X9 MAB21L3** | 5 | **2** — HuRI/Fragoza Y2H **plus** anti-tag co-IP in human U2OS (PMID:40205054) |
| **Q9UL45 BLOC1S6** | 3 | **2** — Rual Y2H **plus** BioPlex anti-tag co-IP in HEK293T |
| **Q8N302 self** | 3 | **2** — two separate Y2H screens. The third record is BioID, and IntAct gives AGGF1 `experimentalRoleA=bait` in **all 635** proximity records: a BirA\*-fusion bait biotinylates itself, so recovering it is a property of the method, not evidence of homodimerisation |
| **O43508 TNFSF12** | **0** | not in IntAct at all; UniProt curated it from PMID:14961121 (Y2H + GST pull-down + co-IP), and PMID:39905000 later re-confirmed it by co-IP in human retinal endothelial cells |

Three things follow. **634 of the 742 records are a single BioID screen**
(PMID:39251607, K562), which is what makes AGGF1 look like a 695-partner hub.
**The self-interaction row derived from that screen is an artefact of the assay**
(bait biotinylates bait), while the two Y2H self-interaction rows are real: a Y2H
self-hit requires the DB- and AD-fusions to associate, and AGGF1 carries a
70-residue coiled coil (18-88) that would do it.
And **three of the four HuRI partners carry `GO:0005634` nucleus with
experimental evidence** — DHX15 (EXP), MCRS1 (EXP + IDA), FBXO28 (EXP) — on a
gene whose entire GOA localisation record is cytoplasm plus extracellular. The
fourth, MAB21L3, has **zero** cellular-component annotations in GOA and no
UniProt `SUBCELLULAR LOCATION` comment, so it is neither support nor
counter-evidence; saying "all four are nuclear" would have been an over-claim.

**Isoform caveat, computed not assumed.** 24 IntAct records are logged against
`Q8N302-2`. Fetching each isoform gives Q8N302-1 = 714 aa, **Q8N302-2 = 109 aa,
Q8N302-3 = 176 aa** — so isoforms 2 and 3 contain **neither** the FHA domain
(434–487) **nor** the G-patch (619–665) **nor** the 604–613 angiogenic motif.
None of those 24 records can speak to any domain this review adjudicates. None of
them reached GOA.

## 5. The GO record ignores two decades of work

`gap_by_reference.py` queries QuickGO **by reference** for every paper this
review touches:

```
SUMMARY: 35 papers; 22 produced NO GO annotation anywhere;
         3 annotate other genes but nothing on AGGF1.
```

The 10 remaining split into 8 high-throughput interaction datasets (too large to
page, so entity counts are reported as unavailable rather than guessed) and
**exactly two** papers that produced an AGGF1 annotation: `PMID:14961121`
(Tian 2004, 7 rows) and `PMID:15905966` (a review, 1 TAS row).

Everything mechanistic is in the 22 — integrin α5β1 as the receptor
(PMID:34551592), integrin α7 on smooth muscle (PMID:35202649, PMID:37081014),
paraspeckles and NEAT1 RNA binding (PMID:35608889), general splicing regulation
(PMID:40035560), FHA-dependent p53 stabilisation (PMID:33069768),
FHA/14-3-3-dependent nucleocytoplasmic transport (PMID:33471274),
JNK-dependent autophagy (PMID:27513923). **This is a coverage defect, not an
over-annotation defect**, and the review says so.

## 6. IBA donors: both rows are sound

`resolve_withfrom.py` — 24 GOA rows, 19 (row, token) pairs, 13 distinct tokens,
**zero unresolved protein tokens**.

- `GO:0001525 angiogenesis` ← `ZFIN:ZDB-GENE-060929-836` resolves to **zebrafish
  aggf1, Q08CK9, TrEMBL, 774 aa** — a true ortholog, not a paralog — and QuickGO
  shows it carries its own **IMP** for `GO:0001525` from PMID:23197652. The donor
  is not resting on a family-level inference.
- `GO:0005576 extracellular region` ← `UniProtKB:Q8N302` is **AGGF1 itself**: a
  self-referential IBA recording a PAINT curator's judgement that the function is
  core. Its own evidence is AGGF1's IDA from PMID:14961121. `NO_FAILURE_CORE`.

## 7. Retraction / erratum sweep: 2 flagged, both cosmetic

`retraction_check.py` reads `CommentsCorrections/RefType` on each *cited*
article's own PubMed record, because a Publisher Correction is not discoverable
by a publication-type search. 22 PMIDs checked, 2 flagged:

- `PMID:39251607` → `ErratumIn` **PMID:39468017**: a **missing author affiliation**
  ("Arc Institute, Palo Alto, CA"). No data affected.
- `PMID:40205054` → `ErratumIn` **PMID:41039152**: a **typo in a Methods
  equation** (subscripts `Ty`/`Sy` → `Tx`/`Sx` in the loss function). No data
  affected.

Neither touches the interaction evidence relied on here. Reported because a check
that was run and came back clean is a finding.

## 8. Coverage reconciliation

`reconcile_goa.py` matches on the full `(GO term, evidence code, reference,
WITH/FROM)` key, not on row counts, because the `fetch-gene` stub is known to
collapse rows that share the first three and differ only in the fourth:

```
GOA data rows              : 24
existing_annotations entries: 32
actions                    : {'ACCEPT': 10, 'KEEP_AS_NON_CORE': 10,
                              'MARK_AS_OVER_ANNOTATED': 1, 'MODIFY': 3, 'NEW': 8}
GOA rows with no review entry : 0
review entries with no GOA row: 8   (all action: NEW)
```

The stub did **not** collapse anything on this gene — it seeded 24 entries for 24
rows with per-partner WITH/FROM intact. The script asserts all three invariants
(no uncovered GOA row; every extra entry is `NEW`; 24 + 8 = 32) and fails loudly
rather than printing a number.

## 9. Term hygiene

`check_terms.py` resolves all 22 terms this review either reviews or proposes
against QuickGO `/complete`. **None obsolete.** `secondaryIds` recorded where
present (`GO:0003676` ← GO:0000496; `GO:0003723` ← GO:0000498, GO:0044822;
`GO:0007155` ← GO:0098602; `GO:0048018` ← GO:0071884).

---

## Checks that came back negative, recorded so the next reviewer knows they ran

- **Paralog transfer into the IBA set** (the ACTR10 defect): absent. The single
  protein donor is the zebrafish ortholog, not a paralog.
- **IBA landing above its donor** (the ACRV1 defect): absent. The zebrafish donor
  holds `GO:0001525` itself, the same term that propagated.
- **Reference-projection across a complex** (the ACTR8 defect): not applicable —
  AGGF1 has no complex-membership annotation, and no reference in its GOA
  annotates it alongside a subunit panel.
- **Partner accession substitution** (the ACRV1 TSC1 defect): absent. All seven
  GOA-named partners resolve to **reviewed Swiss-Prot canonical** entries at
  their canonical lengths.
- **Dead accession returning a vacuous zero** (the ACTR10 defect): absent. Every
  accession queried returned an entry name.
- **The predicted `PSEUDOENZYME_OVERANNOTATION`**: not confirmed, and could not
  be — AGGF1 carries **no catalytic MF term at all** in GOA. There is no EC
  number, no hydrolase, nothing to argue against. The name-derived over-reach on
  this gene is a *binding* term, not a catalytic one.
