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
uv run python term_choice_checks.py  # the two MODIFY targets vs GO's own usage
uv run python lab_independence.py    # which labs produced this literature
uv run python proposed_term_check.py # proposed term is not a duplicate; projection test
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

`proposed_term_check.py` runs the projection test on the three papers behind the
`NEW` biological-process rows and finds **no projection pattern** — but it sharpens
the coverage point rather than merely coming back negative. PMID:27513923 and
PMID:34551592 produced **zero** GO annotations on any gene product, so there is
nothing to project. PMID:40035560 produced ten, over ten entities, and **every one
of them is `GO:0048514` blood vessel morphogenesis in *zebrafish*** — four on
`aggf1` by IMP, six on `srsf6a`/`srsf6b` by IGI. A paper whose entire finding is
that AGGF1 is a general splicing factor regulating 436 genes produced ten GO
annotations, all about vessel morphogenesis in fish, and not one about splicing in
any species.

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
existing_annotations entries: 33
actions                    : {'ACCEPT': 10, 'KEEP_AS_NON_CORE': 10,
                              'MARK_AS_OVER_ANNOTATED': 1, 'MODIFY': 3, 'NEW': 9}
GOA rows with no review entry : 0
review entries with no GOA row: 9   (all action: NEW)
```

The stub did **not** collapse anything on this gene — it seeded 24 entries for 24
rows with per-partner WITH/FROM intact. The script asserts all three invariants
(no uncovered GOA row; every extra entry is `NEW`; 24 + 9 = 33) and fails loudly
rather than printing a number.

## 9. Term hygiene

`check_terms.py` resolves all 22 terms this review either reviews or proposes
against QuickGO `/complete`. **None obsolete.** `secondaryIds` recorded where
present (`GO:0003676` ← GO:0000496; `GO:0003723` ← GO:0000498, GO:0044822;
`GO:0007155` ← GO:0098602; `GO:0048018` ← GO:0071884).

---

## 10. The two MODIFY targets, defended by GO's own usage

A definition that *permits* something and a community that never *does* it are
different situations, so `term_choice_checks.py` tests both MODIFY calls against
usage rather than against the definition alone.

**`GO:0019955 cytokine binding` for AGGF1–TNFSF12.** The obvious objection is
that cytokine binding is a receptor's term and AGGF1 is a secreted non-receptor.
Asking each holder's own GO record whether it carries `GO:0038023 signaling
receptor activity` (not guessing from the gene symbol — a suffix heuristic put
ACVRL1, BMPR1A and IFNAR1 in the wrong column) gives **83 receptors and 9
non-receptors** among the 92 human holders read:

```
P21810  BGN     Biglycan
P08246  ELANE   Neutrophil elastase
P78536  ADAM17  Disintegrin and metalloproteinase domain-containing protein 17
P29466  CASP1   Caspase-1
P32455  GBP1    Guanylate-binding protein 1
Q96PD4  IL17F   Interleukin-17F
D2IYK3 / D5K9Q3 / D5K9R3  POU5F1
```

**BGN** is the directly analogous precedent: a secreted extracellular proteoglycan
that binds secreted cytokines. The term is not receptor-restricted in use.

**`GO:0017151 DEAD/H-box RNA helicase binding` for AGGF1–DHX15.** DHX15 is a
DEA**H**-box helicase, so is a more specific term available, and is this one used
that narrowly? Neither. The ontology search for *DEAH* returns **zero** terms, and
`GO:0017151` has no comment, no synonyms and no children — it is the only term GO
offers for binding a helicase of this superfamily. Its ten human annotations name
four partners: **DDX5** (DEAD-box) and, via POT1, **BLM** and **WRN** — which are
RecQ **DNA** helicases, not DEAD/H-box at all. So GO already applies this term well
outside a strict DEAD-box reading; using it for DHX15 is inside existing usage and
considerably more precise than those rows.

## 11. The proposed term is not a duplicate — enumerated, not searched

`proposed_term_check.py` lists **every child** of the three parents under which a
TNFSF12-binding term could plausibly already sit — `GO:0019955` cytokine binding,
`GO:0043120` tumor necrosis factor binding (where `GO:0038057 TNFSF11 binding`
lives), and `GO:0005102` signaling receptor binding — and prints all **90** of
them. None names or defines TNFSF12 or TWEAK.

This is deliberately an enumeration rather than a search: ontology search is
token-based, so a query for "TNFSF12 binding" cannot match a term named
*tumor necrosis factor ligand superfamily member 12 binding*, and a failed search
would have looked like absence. The script exits non-zero if any child ever does
match, so the proposal cannot silently become a duplicate.

## 12. Almost all of this literature is one laboratory

`lab_independence.py` reads the senior (last) author out of each cached record
rather than taking "independent replication" on impression. Its paper set is
**derived** — GOA references + affinage citations + the review's own references,
minus the high-throughput screens and the corrections/commentary — because the
first version used a hand-written list that had silently omitted PMID:29885663
and therefore reported an independent-group count that described its own list
rather than the literature. The correct counts are the ones in the table below,
and `audit_claims.py` now derives them from `lab_independence.measure()` rather
than blacklisting spellings of the wrong ones.
A list you curate is a list you can under-curate, and the conclusion then
describes the list rather than the literature.

Over the resulting **27 cached AGGF1 primary studies**:

```
  Wang   Q    : 18 paper(s)
  Tian   XL   :  2 paper(s)
  Qi J / Xu Y / Zhou B / Zhang JH / Lu Q / Liao S / Chen L : 1 each
```

`Wang Q` and `Wang QK` are merged as initial variants of one name; the merge only
fires when one initial string is a prefix of the other. Lineage is then computed,
not judged — a senior author who also appears in the author list of a
dominant-group paper is a trainee or collaborator, not an independent
investigator:

| | count | |
|---|---|---|
| dominant group | **18** | Wang Q / Wang QK |
| lineage | **5** | Tian XL ×2, Xu Y, Zhou B, Lu Q — each an author on a Wang-group paper |
| senior author on **no** Wang-group paper | **4** | Qi J (17884784), **Zhang JH (29885663)**, Liao S (33168501), **Chen L (39905000)** |

Three of those four are used by the review: **PMID:39905000** for the TNFSF12
interaction and the extracellular pool, **PMID:29885663** on the PI3K/AKT row, and
**PMID:33168501** on the `GO:0005634` nucleus row, where it supplies independent
human-cell corroboration (AGGF1 co-localising with γH2AX in HCT116) for what was
otherwise a Wang-group-and-lineage proposal.

An earlier version of this section applied a significance filter that left
PMID:33168501 out. That was a **judgement layered on top of a measurement** — the
count is derived end to end, then a hand-applied significance filter dropped a
paper bearing directly on the review's largest proposal. Same failure as the
hand-written paper list this script was rewritten to remove, one level up.

This is also why an earlier draft's hedge — anchoring the nucleus proposal on
PMID:33069768 because PMID:35608889 was "from the discovery lab" — was withdrawn:
both papers have the same senior author. The paraspeckle and splicing results
remain entirely single-group.

One caveat the script reports rather than hides: **Xu C appears on PMID:39905000
and on 14 of the dominant group's 18 papers.** A shared surname-plus-initial is not
proof of the same person, the senior author differs and the affiliations are a
different institution, so the paper is still counted as independent — but this
paper's independence is load-bearing here, so the overlap is printed.

`audit_claims.py` imports `lab_independence.measure()` and checks the prose
against it, rather than blacklisting spellings of wrong counts. Three consecutive
review rounds each found a wording the previous round's literal did not cover, so
enumerating spellings does not converge. The derived check instead rejects **any**
counted independent-group claim that disagrees with the measurement, and **any**
significance-ranking of the independent set — and it found two further instances
the literals had missed the moment it was switched on.

(The retracted wordings are described rather than quoted here, for the same
reason they are paraphrased in the notes: a guard that has to tell a retraction
apart from a report of one will eventually let the claim back in. Writing this
paragraph with the examples spelled out tripped the guard immediately, which is
the behaviour you want.)

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
