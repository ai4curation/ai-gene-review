# AKAP12 (gravin / SSeCKS / AKAP250) — review notes

UniProt `Q02952`, 1782 aa, `PE 1: Evidence at protein level`. PANTHER `PTHR23209:SF4`,
InterPro family `IPR028540`.

## Reconciliation: 38 GOA rows, 38 reviewed rows, 4 NEW

`AKAP12-goa.tsv` has 39 lines (38 data rows). The `fetch-gene` stub seeded **38**
`existing_annotations` entries, and a programmatic 1:1 match on
`(term, evidence, reference, with/from)` came back with **zero** rows missing and zero
extra. This is the first gene in this batch where the stub did **not** collapse
`GO:0005515` rows: all nine partner rows survived as separate entries, including the three
that share `PMID:35271311`. The check is worth running anyway — it is what later caught my
own dropped `supporting_entities` (below).

Final: 42 `existing_annotations` = 38 GOA rows + 4 `NEW` proposals.

## The decisive paper the provider missed: PMID:9000000

The affinage record (`gates_passed: True`, 44 citations, all numeric PMIDs) is rich and
mostly accurate, but its citation list starts at 1997 with `PMID:9187136` and **never
includes `PMID:9000000`** — Nauert, Klauck, Langeberg & Scott, *Curr Biol* 1997, "Gravin,
an autoantigen recognized by serum from myasthenia gravis patients, is a kinase scaffold
protein."

That paper is the single most important publication on this gene. On the **human** protein
it maps both anchoring determinants in one experiment:

> residues 1526-1780 of gravin bind the regulatory subunit (RII) of protein kinase A with
> high affinity, and residues 265-556 bind protein kinase C

and isolates a PKA–gravin complex from human erythroleukemia cells. It is also the source
of UniProt's `REGION 266..557 /note="Involved in PKC-binding"`.

It was found in the UniProt `RN` reference list, not by any AKAP12-keyed search — the title
names an autoimmune disease, not a function. This is the campaign's established recall
pattern (ADAMTSL1, ACTG2, AHSP): *the decisive paper for a gene is often titled for
something else.* Recording it here because that is the only way the provider's recall gets
measured.

(The round-numbered PMID is a genuine PubMed identifier, not a placeholder — verified
against the PubMed record.)

## Retraction: PMID:27683220 is retracted for data fabrication

Affinage lists the AKAP12/ATR/nucleotide-excision-repair paper as a **High** confidence
finding with no flag, and it is the sole source of that record's DNA-repair claims and of
its `R-HSA-73894 DNA Repair` Reactome grounding.

It was retracted in 2020 (`PMID:33091128`):

> The authors are requesting retraction of the above article pursuant to an internal
> investigation by a team of scientists at the University of Kentucky that recently
> determined it contains fabricated and/or falsified data.

Set `is_invalid: true`; no annotation in this review rests on it and no NER/ATR term was
proposed.

A systematic check of all 61 candidate PMIDs via `CommentsCorrections/RefType` on each
article's own PubMed record (not a publication-type search, which misses Publisher
Corrections) found three flags in total:

| PMID | flag |
|---|---|
| `PMID:27683220` | **Retracted** → `PMID:33091128` |
| `PMID:22584896` | Erratum → `PMID:37934326` (Correction, scope not stated in the notice) |
| `PMID:9187136` | ErratumIn (no PMID given in the record) |

Nothing in the review rests on the latter two.

## The sign inversion: RGD's GO:0043116 contradicts its own source paper

The highest-value finding after PMID:9000000. `GO:0043116 negative regulation of vascular
permeability` reaches human AKAP12 by Ensembl Compara from rat `Q5QD51`, where RGD holds it
as **IMP from `PMID:20454828`**. That paper reports the opposite sign:

> Depletion of endogenous SSeCKS in RPMVEC significantly attenuated cytokine-induced
> decrease in TER and increase in P (d), but not to the basal levels.

TER is transendothelial electrical resistance: cytokines lower it (leakier barrier),
and *removing SSeCKS blunted that*, i.e. the protein **promotes** permeability here. The
authors' own CONCLUSIONS sentence says so outright:

> SSeCKS is involved in the endothelial hyperpermeability induced by IL-1β and TNF-α in
> inflammatory process.

On its own evidence the rat annotation should be `GO:0043117 positive regulation of
vascular permeability`.

**But the term survives on the human row**, because a *different* body of evidence supports
it: mouse-specific siRNA against Akap12 in MyEnd endothelial cells impairs barrier function
(`PMID:25188285`), and Akap12-knockout mice have leakier vessels. So the action is
`KEEP_AS_NON_CORE` with `propagation_review: root_cause: SOURCE_BAD`,
`failure_modes: [REGULATORY_SIGN_INVERSION]` — the term is right, the provenance is not,
and both facts are recorded rather than one silently inheriting the other.

The two results are probably reconcilable: barrier-protective basally, permeability-promoting
under inflammatory cytokine stimulation. That is the `suggested_experiments` entry with
matched stimulation arms.

Assessed from the abstract only (full text unavailable), so the note to RGD is phrased as a
re-examination request, not a verdict.

## Sequence analysis done for this review: the PKC motifs *are* the CaM motifs

`PMID:21903576` (Gelman lab) publishes a PKC-binding consensus for rodent SSeCKS,
`EG(I/V)(T/S)XWXSFK(K/R)(M/L)VTP(K/R)K(K/R)X(K/R)XXXEXXXE(E/D)`, at aa 592-620 and 741-769.
Those coordinates are rodent, so they cannot simply be read onto human AKAP12.

Rather than transfer the numbers, the consensus was run as a regex against the human Q02952
sequence parsed from `AKAP12-uniprot.txt` (script:
`scratchpad/akap12_motifs.py`; length asserted == 1782 before use). Exactly two matches:

```
605-633  EGVTPWASFKKMVTPKKRVRRPSESDKED
754-782  EGVSTWESFKRLVTPRKKSKSKLEEKSED
```

UniProt annotates AKAP CaM-binding (WSK) motifs at **607-627**, **756-776** and **801-821**.
So matches 1 and 2 coincide with CaM motifs 1 and 2; the shared `W.S.K` cores are `WASFK`
and `WESFK`. The third CaM motif (`WVSIK`, 801-821) does **not** match the PKC consensus.

Two consequences:

1. The human protein carries both published PKC determinants at conserved positions, which
   is what makes `GO:0005080` defensible with the human `PMID:9000000` evidence as primary
   and the rodent mapping as corroboration.
2. It gives a mechanism for `PMID:11820772`'s observation that PKC phosphorylation
   *antagonises* CaM binding — the two ligands compete for one element. That is the
   `suggested_experiments` ITC competition experiment.

Note what this is **not**: it is not evidence that UniProt's `REGION 266..557` PKC-binding
annotation is misplaced. That region comes from `PMID:9000000`'s human fragment mapping and
is a genuinely separate determinant. AKAP12 has two mapped PKC-binding regions from two
labs; UniProt records one of them. Filed as an additive UniProt suggestion, not a correction.

## Per-partner judgement on the nine GO:0005515 rows

IntAct `findInteractions/Q02952` returns 128 records over 105 distinct partners, expanded
and counted by **distinct publication + detection method**, never by `NbExp`.

| partner | rows | independent evidence | verdict |
|---|---|---|---|
| PRKAR2A `P13861` | 2 | `filter binding` (PMID:16642035, direct in vitro) + `anti tag coip` (OpenCell) + human region mapping (PMID:9000000) | **MODIFY → `GO:0034237`** |
| CTNNB1 `P35222` | 2 | `display technology` (mRNA display) + `anti tag coip` (OpenCell) — two orthogonal methods, two groups | **MODIFY → `GO:0008013`** |
| FHL1 `Q13642` | 3 | Y2H ×2 (different libraries/labs) + OpenCell coIP | `KEEP_AS_NON_CORE` |
| EGFR `P00533` | 2 | **both** `ub reconstruction` (split-ubiquitin MYTH), overlapping authors (Curak, Stagljar) | **`MARK_AS_OVER_ANNOTATED`** ×2 |

All four partners resolve to **reviewed canonical Swiss-Prot entries with the expected
lengths** — no TrEMBL/ORFeome substitutions of the kind found on ACRV1. Reporting that as a
negative result of a check that was run.

The EGFR call is the `NbExp` lesson in a new guise: two *publications* but one assay
platform and an overlapping author group, so they are not independent replication. Neither
paper names AKAP12 anywhere in its cached text.

## Projection / reference-scale checks

Queried QuickGO **by reference** for every high-throughput source:

- `PMID:21423176` → `GO:0005925` on **285 annotations**, all HDA, all UniProt-assigned.
  The set includes `P05388` RPLP0, `P05386` RPLP1 and `P05387` RPLP2 — three cytoplasmic
  large-ribosomal-subunit P proteins, which is what co-purifying abundance looks like in an
  isolated-adhesion prep. Kept as non-core rather than removed, because AKAP12 has
  independent adhesion cell biology (vinculin plaques, FAK phosphorylation).
- `PMID:35271311` (OpenCell) → **2872** `GO:0005515` annotations. Endogenous tagging makes
  each edge better than a Y2H hit, but genome-scale means no edge is individually
  validated; used only as the orthogonal confirmation for PRKAR2A and CTNNB1.

Both queries were paginated; `numberOfHits` was compared against `len(results)` and the
truncation was reported rather than a page total being read as a whole.

## Compara donor evidence: all eleven rows traced to their rat source

Every `GO_REF:0000107` row was traced through QuickGO on `UniProtKB:Q5QD51` (reviewed rat
Akap12, 1687 aa, same `PTHR23209:SF4` subfamily — a true 1:1 orthologue, not a paralog
transfer).

| human row | rat evidence | verdict |
|---|---|---|
| `GO:0032496` response to LPS | IEP `PMID:23912647` (+ independent `PMID:17873284`) | KEEP_AS_NON_CORE |
| `GO:0032760` +reg TNF production | **IMP ×2** (`PMID:17873284`, `PMID:19937403`) | KEEP_AS_NON_CORE |
| `GO:0035733` hepatic stellate cell activation | IEP `PMID:23925424` | **MARK_AS_OVER_ANNOTATED** |
| `GO:0043025` neuronal cell body | IDA `PMID:11814414` | KEEP_AS_NON_CORE |
| `GO:0043116` −reg vascular permeability | IMP `PMID:20454828` (**sign-inverted**) | KEEP_AS_NON_CORE + `SOURCE_BAD` |
| `GO:0051602` response to electrical stimulus | IEP `PMID:23912647` | **MARK_AS_OVER_ANNOTATED** |
| `GO:0061870` +reg HSC migration | IMP `PMID:23925424` (**no migration assay in the abstract**) | **MARK_AS_OVER_ANNOTATED** |
| `GO:0070374` +reg ERK1/2 | IMP `PMID:19937403` | KEEP_AS_NON_CORE |
| `GO:0071347` cell. response to IL-1 | IEP `PMID:20454828` | KEEP_AS_NON_CORE |
| `GO:0071356` cell. response to TNF | IEP `PMID:20454828` | KEEP_AS_NON_CORE |
| `GO:1900143` +reg oligodendrocyte apoptosis | IMP `PMID:20155814` | KEEP_AS_NON_CORE |

Three discriminations worth keeping:

- **IEP is not uniformly weak.** `GO:0071347`/`GO:0071356` come from cytokine applied
  *directly to the cells assayed* — the canonical use of IEP for a cellular-response term.
  `GO:0051602` comes from an electrode on the **vagus nerve of a whole rat**, with Akap12
  measured in lung tissue three causal steps downstream. Same evidence code, opposite
  quality.
- **Two rows from one paper, read two ways.** `PMID:23925424` supplied both `GO:0035733`
  (IEP) and `GO:0061870` (**IMP**), yet its abstract describes only expression measurement —
  no knockdown, no over-expression, no migration readout. The internal inconsistency in how
  the same reference was read is the discriminator. Full text was not accessible, so both
  are `MARK_AS_OVER_ANNOTATED` and the question is passed to a curator rather than settled.
- **`GO:0070374` is directionally contested, not wrong.** The rat astrocyte siRNA is real,
  but SSeCKS *suppresses* serum-induced Raf/MEK/ERK activation in rat MAT-LyLu prostate
  carcinoma cells, in a way that requires its PKC-binding domain (`PMID:20018890`).
  Recorded as context-dependent rather than resolved.

  An error worth recording: the first draft wrote "in fibroblasts" here, a detail that
  appears in neither the paper nor the provider summary — I supplied it. Caught by going
  back to the abstract to verify a claim I had carried over from the affinage narrative.
  The provider's sentence was accurate; the embellishment was mine. Two further
  provider-sourced claims were verified the same way and both held
  (`PMID:16547152` RhoA/Cdc42 >5-fold; `PMID:33260683` ZO-1/claudin-5), with one refinement:
  the ZO-1/claudin-5 result is from siRNA in cultured cells, not from the knockout mice, so
  the two halves of that sentence were separated in the `GO:0061028` reason.

## The granularity check on GO:0007165 came back NEGATIVE — reporting it anyway

`GO:0007165 signal transduction` by IBA looks like a textbook `GRANULARITY_MISMATCH`. It is
not, because that classification requires the donors to **agree**.

WITH/FROM is `PANTHER:PTN002755149 | UniProtKB:Q02952 | ZFIN:ZDB-GENE-030131-9753`:

- `PTN002755149` — a tree node, not a protein.
- `Q02952` — **self-referential** (this is AKAP12). Valid: it records a PAINT curator
  judging the term applicable at the node, not a circular inference.
- `ZDB-GENE-030131-9753` — zebrafish **akap12b**. Both UniProt entries (`F2Z4T4`,
  `A0A0R4IC31`) are **unreviewed (TrEMBL)**; reporting that because an unreviewed source is
  weaker and hiding it is the same failure as silent degradation.

Querying akap12b's own GO record: it carries `GO:0005737` by **IDA twice**
(`PMID:17575056`, `PMID:18725198`) — so the cytoplasm IBA rests on measurement. And its
experimental BP annotations are `GO:0035024` negative regulation of Rho signalling,
`GO:0032060` bleb assembly, `GO:0060028` convergent extension — a **cytoskeletal/Rho** axis,
whereas the human protein's measured signalling is **cAMP/PKA and PKC**. The donors
genuinely disagree, so `signal transduction` is the honest LCA. `ACCEPT`.

The reciprocal half *is* a finding: akap12b's `GO:0035024` IMP stops at the zebrafish gene,
while mammalian work independently reports AKAP12 restraining RhoA/Cdc42 (`PMID:16547152`)
and the Rho kinase pathway (`PMID:33260683`). That is a PAINT coverage gap, filed in
`suggested_questions`.

## Hazard check: AKAP12 vs AKAP10 (concurrent review) — no relationship

Verified rather than assumed:

| gene | PANTHER | length |
|---|---|---|
| AKAP12 `Q02952` | `PTHR23209` / `:SF4` | 1782 |
| AKAP10 `O43572` | `PTHR13155` / `:SF1` | 662 |
| AKAP5 `P24588` | `PTHR15182` / `:SF0` | 427 |

Three disjoint families. "AKAP" is a functional class defined by an amphipathic RII-binding
helix, not a homology family, so there is no family-level inference path between them. No
WITH/FROM token on AKAP12 names AKAP10 or any other AKAP. Nothing was imported across.

`PTHR23209` is unusual and worth noting: **1185 proteins, one subfamily, and the only three
reviewed members are human, rat and mouse AKAP12.** It is a single-gene orthogroup. That is
why `IPR028540`-derived IEAs (`GO:0051018`, `GO:0090036`, `GO:0141156`) are treated as well
founded rather than fold-level guesses — and why the "the general term is the LCA of a
heterogeneous clade" defence would *not* have been available if the donors had agreed.

## The ontology gap: GO can name the enzyme that makes cAMP but not the one that destroys it

`GO:0019899 enzyme binding` has 28 direct children — including `GO:0008179 adenylate
cyclase binding`, `GO:0019902 phosphatase binding`, `GO:0035473 lipase binding`,
`GO:0043274 phospholipase binding` — and **none** for a phosphodiesterase.

Checked by enumerating the parent's children, not only by keyword search, because ontology
search is token-based and a failed query is not evidence of absence (the AHSP lesson).
Keyword searches for "phosphodiesterase binding" and "cyclic nucleotide phosphodiesterase
binding" return only `GO:0004112`, `GO:0170005` and `GO:0051344` — catalysis and regulation,
no binding term.

The cost is immediate: the best human experiment on AKAP12 (`PMID:16642035`) shows a gravin
complex containing **PKA and PDE4D**, and GOA can record the PKA half and not the PDE4D
half. Filed as `proposed_new_terms`. GO already models the analogous regulatory relation
(`GO:0170005` cyclic nucleotide phosphodiesterase activator activity), so a binding term
completes a pattern rather than inventing one.

## Hazards from the brief, handled explicitly

**"Tumour suppressor" is not an MF or a BP.** AKAP12/SSeCKS is described as a tumour and
metastasis suppressor throughout the literature, and affinage's narrative leads with it.
**No tumour-suppression, growth-arrest, senescence or metastasis term was proposed.** The
underlying experiments are ectopic over-expression in transformed rodent lines
(`PMID:9187136`, `PMID:9744295`, `PMID:10982843` — the G1 arrest is a tetracycline-induced
over-expression phenotype) or downregulation-in-cancer expression correlations. Neither
establishes a normal physiological process for the wild-type protein. This is noted in the
individual `reference_review.review_notes` for those papers.

**Scaffolds accumulate their clients' functions.** Deliberately avoided: PKA's kinase
activity, PDE4D's hydrolase activity and the cyclases' lyase activity are **not** AKAP12's.
The MF chosen for the bridging role is `GO:0035591 signaling adaptor activity`, whose
definition explicitly covers tethering and localising signalling components without
catalysis — the same shape as the AFF1/AFF4 pair's `GO:0030674`, narrowed one level because
all of AKAP12's clients are in one signalling pathway. No `contributes_to_molecular_function`
was used, because AKAP12 is not a subunit of a catalytic complex; it is an external tether.

**Species discipline.** Checked per row. Notably `PMID:25188285`'s abstract says the study
analysed "human and mouse microvascular endothelial cells as well as isolated rat mesenteric
microvessels", which invites an IMP — but the methods state the knockdown used
**mouse-specific siRNA** in **MyEnd mouse** cells, so `GO:0061028` is `ISS` with
`UniProtKB:Q9WTQ5` (mouse Akap12) as the supporting entity. Which *reagent* was human is the
question, not which materials appear in the paper.

## Terms considered and NOT proposed

Recording the negatives, since an omission with a reason is more useful than a silent gap.

- **`GO:0051015 actin filament binding`** — `PMID:12083796` reports bacterially expressed
  unphosphorylated SSeCKS co-sedimenting with F-actin, which would license it. But
  `PMID:9885289`, from the **same laboratory**, reports SSeCKS along "a cytoskeletal network
  distinct from F-actin". The evidence is self-opposed; filed as a question rather than a
  term.
- **`GO:0140313 molecular sequestering activity`** — the cyclin D1 story is well supported
  (`PMID:10982843` CY-motif binding with K→S ablation; `PMID:22249313` in rat PECs) but
  entirely rodent, and whether the CY motifs are functional in human AKAP12 is untested.
- **`GO:0004860 protein kinase inhibitor activity`** — PKC binding lowers PKC-α activity
  (`PMID:21903576`), but the mechanism is sequestration, not classical inhibition, and
  `GO:0090036 regulation of protein kinase C signaling` (already annotated) captures it at
  the right level.
- **Any DNA-repair / ATR term** — the only source is the retracted `PMID:27683220`.
- **`GO:0002031 G protein-coupled receptor internalization`** — `PMID:10858453` reports that
  gravin deficiency inhibited agonist-induced sequestration, but the cell system is not named
  in the abstract, full text is not cached, and no species claim could be anchored.

## Own-audit findings (process)

`scratchpad/akap12_audit.py` asserts: strict duplicate-key YAML load; raw-vs-parsed
`reference_id` counts (50 = 50, anchored to `^\s*- reference_id:` so
`original_reference_id:` cannot match); GOA row coverage by `(term, evidence, reference,
with/from)`; `source_entities` derived from the GOA WITH/FROM field with a count assertion;
`root_cause`/`failure_modes`/`action` agreement; no undeclared references; and species
discipline on NEW rows.

It caught **a real defect in my own draft**: the `GO:0016020` row had lost its
`supporting_entities: [UniProtKB-SubCell:SL-0162]`, which no other gate would have seen —
the repo validator reported `✓ Valid` with it missing. The by-eye check had passed.

It also produced a **false positive** that was worth fixing properly: the first version of
the species check was a keyword *blacklist* ("does the reason mention rodent?"), and it
fired on `GO:0005080`, whose primary evidence is human (`PMID:9000000`) and whose rodent
mention is corroboration. A blacklist cannot tell those apart. Replaced with the **positive**
invariant — an experimental code must state the species the experiment was done in — which
is the claim actually being made.

`scratchpad/akap12_audit_selftest.py` breaks the document six ways (four mutations that must
trip a guard, two controls that must not), asserting each anchor string is present before
replacing it so a drifted mutation cannot "pass" by changing nothing, and confirming the file
is restored byte-identically afterwards. All six behaved as intended.

`checkquotes.py` from the shared scratchpad was run after confirming it resolved the correct
repo root (it prints it; it derived this worktree, not another agent's). 77 quotes, 0
problems, and 0 `file:` quotes — none were used, because CI does not validate them.

## Why the `validate` warning about the deep-research file is left standing

`just validate` warns that no annotation references `AKAP12-deep-research-affinage.md`. That
is deliberate. The campaign rule is that a provider sentence is a *lead*, never a
`supporting_text` for a mechanistic claim, and quoting `file:` paths is the one fabrication
surface CI does not check. Every claim in this review is anchored to a PMID quote instead.
The affinage record's contributions are real and are credited above — it supplied the
PMID set that led to `PMID:21903576`, `PMID:25188285` and `PMID:19055733` — and its two
defects (missing `PMID:9000000`, citing a retracted paper unflagged) are recorded rather
than papered over.
