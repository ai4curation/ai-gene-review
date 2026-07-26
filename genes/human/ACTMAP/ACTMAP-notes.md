# ACTMAP (C19orf54) — review notes

UniProt `Q5BKX5` (`ACTMP_HUMAN`), HGNC:24758, 351 aa (canonical isoform 1, MANE-Select
`ENST00000378313.7`), chromosome 19. `PE 1: Evidence at protein level`. Formerly `C19orf54`;
renamed `ACTMAP` after the 2022 identification of its activity.

Reviewed 2026-07-26 (PAINT + affinage campaign). Sources used: `ACTMAP-uniprot.txt`,
`ACTMAP-goa.tsv`, `ACTMAP-deep-research-affinage.md` (`gates_passed: True`, faith 100%),
three primary/secondary PMIDs, QuickGO, IntAct, PANTHER PTHR28631, and the computed audit in
`ACTMAP-bioinformatics/RESULTS.md`.

## 1. What the protein does

ACTMAP is the protease that performs the **noncanonical, post-translational** step of actin
N-terminal maturation. The initiator methionine of cytoplasmic actin is *not* removed
co-translationally by methionine aminopeptidase; it is Nt-acetylated and then excised, as a whole
Nα-acetyl-methionine, by ACTMAP:

- [PMID:36173861 "Protein synthesis generally starts with a methionine that is removed during translation. However, cytoplasmic actin defies this rule because its synthesis involves noncanonical excision of the acetylated methionine by an unidentified enzyme after translation."]
- [PMID:36173861 "Here, we identified C19orf54, named ACTMAP (actin maturation protease), as this enzyme."]
- [PMID:42159598 "ACTMAP is a ∼45 kDa cytosolic protein identified in a haploid genetic screen to function as a protease that post-translationally cleaves the N-terminally acetylated methionine from β- and γ-actin, which are then reacetylated by N-acetyltransferase NAA80 to generate mature actins."]
  (The "∼45 kDa" is an apparent mass; UniProt computes **37,779 Da** for the 351-residue canonical
  form, so the review quotes this sentence only from "protein identified in a haploid genetic
  screen…" onward and does not import the mass figure.)

So the pathway order is: translation → Nt-acetylation of Met1 → **ACTMAP cleaves acetyl-Met1** →
NAA80 re-acetylates the newly exposed Asp2/Glu2 → mature actin. For muscle α-actins the initiator
Met *is* removed canonically and ACTMAP then removes the acetylated Cys.

UniProt records four Rhea reactions for this, all of which release a **substituted** amino acid,
not a free one:

- [file:human/ACTMAP/ACTMAP-uniprot.txt "Reaction=N-terminal N(alpha)-acetyl-L-methionyl-L-aspartyl-[protein] +"] → `N-acetyl-L-methionine` (Rhea:74571)
- plus the Glu2 variant (Rhea:74575), and the acetyl-Cys/Asp and acetyl-Cys/Glu variants (Rhea:74579, 74583) for muscle α-actins.

UniProt's own EC assignment is deliberately unspecific:
[file:human/ACTMAP/ACTMAP-uniprot.txt "EC=3.4.11.- {ECO:0000269|PubMed:36173861}"] — i.e. **not**
EC 3.4.11.18.

## 2. The activity claim rests on a tested catalytic residue, not on a domain name

- UniProt annotates a `REGION 124..244` [file:human/ACTMAP/ACTMAP-uniprot.txt "/note=\"Peptidase C39-like\""] and `ACT_SITE 132`.
- The residue was tested: [file:human/ACTMAP/ACTMAP-uniprot.txt "C->A: Catalytically inactive, disrupts N-terminal"] cleavage of immature actin (`ECO:0000269|PubMed:36173861`).
- Independently re-tested four years later with covalent chemistry:
  [PMID:42159598 "AlphaFold predictions revealed that ACTMAP has structural similarity to bacterial cysteine proteases with C132 representing the catalytic nucleophile."]
  [PMID:42159598 "we confirmed the stereoselective reactivity of WX-02-570 with recombinant WT-ACTMAP, but not a C132A mutant, both in HEK293T cells and in cell lysates by gel-ABPP"]
  with the specificity control that other cysteines are not the reactive site:
  [PMID:42159598 "Other representative cysteine mutants of ACTMAP (C119A and C271A) retained reactivity with WX-02-570"]
  and an orthogonal thermal-stability readout:
  [PMID:42159598 "in the thermal stability of WT-, but not C132A-ACTMAP (Figure S6D,E), further supporting that tryptoline butynamides react with the cysteine nucleophile of ACTMAP."]
- Chemical inhibition reproduces the genetic phenotype in human cells:
  [PMID:42159598 "which produced a concentration-dependent increase in immature β-actin"] after
  [PMID:42159598 "genetic disruption of ACTMAP by CRISPR/Cas9 gene editing resulted in substantial accumulation of immature actin"].

Conclusion: the protease call is **not** domain-name-derived. It is a mutated-residue call
supported twice by independent labs and methods. `GO:0070005 cysteine-type aminopeptidase
activity` is therefore well earned on the *mechanism* axis.

## 3. Headline curation finding — `GO:0004239` is the wrong term, and it is a term-scoping problem, not a curator error

`GO:0004239 initiator methionyl aminopeptidase activity` is annotated to ACTMAP twice (IDA by
UniProt from PMID:36173861; IEA by Ensembl ortholog projection). Three computed observations, all
in `ACTMAP-bioinformatics/RESULTS.md`:

1. **The term means canonical MetAP.** Its definition is "Catalysis of the release of N-terminal
   initiator methionine from peptides" and its **only** EC xref is `3.4.11.18` — the
   co-translational, metal-dependent methionine aminopeptidase reaction. ACTMAP releases
   `N-acetyl-L-methionine`, and UniProt gives it `EC 3.4.11.-`, explicitly not `3.4.11.18`. The
   2022 paper's entire point is that actin "defies this rule".
2. **The branch requires a free N-terminus that ACTMAP's substrate does not have.** Both
   `GO:0004239` and `GO:0070005` are descendants of `GO:0008238 exopeptidase activity`, whose
   definition ends "...in a reaction that **requires a free N-terminal amino group**, C-terminal
   carboxyl group or both". ACTMAP's substrate is Nα-acetylated. `GO:0008242 omega peptidase
   activity` (EC `3.4.19.-`, `3.4.19.1` acylaminoacyl-peptidase) is *not* under exopeptidase and
   is defined for "releasing substituted amino acids".
   **GO already models the exact analogue correctly**: `GO:0016920 pyroglutamyl-peptidase
   activity` releases a single N-terminal residue whose α-amino group is blocked, and it sits under
   `GO:0008242` + `GO:0008234` (cysteine-type peptidase) and **not** under `GO:0004177`
   aminopeptidase activity. Computed: `under omega peptidase: True`, `under cysteine type
   peptidase: True`, `under aminopeptidase: False`.
3. **The term now conflates two mechanistically distinct enzyme families.** Censused over five
   model organisms (`9606,10090,7227,7955,559292`): 86 annotations on 74 gene products, of which
   **4 are ACTMAP-family** (PANTHER PTHR28631: human `Q5BKX5`, mouse `J3QPC3`, zebrafish `B0V3H4`,
   *Drosophila* `Q9VCE8`) and **70 are not** — `METAP1`, `METAP1D`, `METAP2`, yeast `MAP1`/`MAP2`,
   `RNPEPL1`, fly `MAP1A`/`MAP1B`/`und`. So one term is being used both for the cobalt/manganese
   MetAP family that removes the *unmodified* initiator Met co-translationally, and for the
   cysteine-nucleophile ACTMAP family that removes the *Nα-acetylated* initiator residue
   post-translationally.

**Correction to my own first pass (see §13):** the five-taxon census **understates** the family,
because bovine and *Xenopus* sit outside those taxa. Querying each reviewed PTHR28631 member
directly gives **6 of 6 carrying `GO:0004239`** — `A6QQD2` (bovine, ISS), `B0BM95` (*Xenopus*,
ISS), `B0V3H4` (zebrafish, ISS), `J3QPC3` (mouse, IDA+ISS+ISO+IEA), `Q5BKX5` (human, IDA+IEA),
`Q9VCE8` (*Drosophila*, ISS). Every non-human one is an ISS/ISO/IEA descendant of the human
annotation.

The right fix is a **new term** (a cysteine-type omega peptidase for Nα-acetylamino-acid release
from actin), which would correct **6 gene products in 6 species** in one edit. Note the term's own
history: `GO:0004239` was obsoleted in 2015 and **reinstated on 2023-03-14** with the narrow
"initiator methionine" definition (QuickGO `comment: This term was reinstated from obsolete`);
UniProt's ACTMAP IDA is dated 2023-03-31, 17 days later. So the term choice was a deliberate,
recent curator decision made when nothing better existed — this is a gap in the ontology, not
sloppy curation, and it should be raised as a term request rather than pinned on the curator.

## 4. The two Ensembl IEA rows are reciprocally circular

`GO:0004239` and `GO:0016485` each appear twice: once IDA from PMID:36173861, once IEA
(`GO_REF:0000107`, Ensembl Compara) with `WITH/FROM = UniProtKB:J3QPC3 | ensembl:ENSMUSP00000137189`.

Resolved: `J3QPC3` → `ACTMP_MOUSE`, mouse Actmap, 361 aa, Swiss-Prot reviewed, requested accession
returns itself (so not a dead/merged entry). The donor **does** carry its own experimental
annotation — but from **the same publication**:

| row term | mouse donor's own evidence | donor WITH/FROM points back at Q5BKX5? |
|---|---|---|
| GO:0004239 | IDA (PMID:36173861), ISS (GO_REF:0000024), ISO (GO_REF:0000119), IEA (GO_REF:0000107) | yes — GO_REF:0000024, :0000107, :0000119 |
| GO:0016485 | IDA (PMID:36173861), ISO (GO_REF:0000119), IEA (GO_REF:0000107) | yes — GO_REF:0000107, :0000119 |

Haahr et al. assayed both the human protein and a mouse knockout, so mouse and human each hold an
independent IDA *from the same paper*; and three of the mouse donor's four annotations to the term
are themselves projections **from human Q5BKX5**. The human IEA row therefore adds no evidence
independent of the human IDA it sits beside. It is not wrong — the donor is the true 1:1 ortholog —
so it is kept, but it must not be counted as a second line of support.

## 5. The anticipated actin-role conflation did **not** happen (negative result, reported)

ACTMAP acts *on* actin, so the obvious risk was that actin's own cell-biology terms would leak onto
it (the `ROLE_CONFLATION` shape that hit ACTL8, where 10 of 11 IBA rows were transfers of β-actin's
specific biology). Checked and refuted: ACTMAP's entire GOA record is 6 rows — cytoplasm, two
protease MF terms, and protein processing. There is **no** actin-binding, actin-cytoskeleton,
actin-filament, sarcomere or cell-motility term, and no `GO:0005515`. The conflation that *did*
occur is at the term level (the MetAP-family term above), not the substrate level.

Also checked, and also negative:
- **No IBA rows at all.** `DR PAN-GO; Q5BKX5; 0 GO annotations based on evolutionary models` — PAN-GO
  has not annotated ACTMAP despite PTHR28631 being a clean single-subfamily family (1109 proteins,
  845 proteomes, 2999 taxa, subfamily `PTHR28631:SF1` "ACTIN MATURATION PROTEASE") whose human
  member has IDA-grade evidence. That is a PAINT gap, not a PAINT error.
- **No paralog problem.** PTHR28631 has one subfamily and six reviewed members, one per species
  (bovine, *Xenopus*, zebrafish, mouse, human, *Drosophila* CG33108) — there is no paralog to
  mis-transfer from.
- **The renaming did not split the literature.** PubMed returns 3 records for `C19orf54` and 5 for
  `ACTMAP`; the 3 are a subset of the 5, and the 2 extra are one unrelated paper (a GPS
  "ActMAP framework" in *Health & Place*) plus the JACS study. The old name persists only in
  resource metadata (PANTHER family name "UPF0692 PROTEIN C19ORF54", `BioMuta; C19orf54`), not in
  the primary literature.

## 6. Interaction data: the partner list belongs to a catalytically dead isoform

UniProt's `CC INTERACTION` block lists 66 partners, and **every one is recorded against isoform
`Q5BKX5-3`**. Isoform 3 carries `VSP_039884`, which replaces residues 1..216 with a 35-residue
alternative N-terminus — deleting `ACT_SITE 132` and most of the `Peptidase C39-like` region
(124..244). Isoforms 2 and 3 therefore **cannot be catalytically active**.

IntAct directly (`/intact/ws/interaction/findInteractions/Q5BKX5`, 220 records): 212 of the 216
ACTMAP-side records are against `Q5BKX5-3`; 197 records have *S. cerevisiae* as host organism and
are logged as `two hybrid array` (70) + `two hybrid prey pooling approach` (70) + `validated two
hybrid` (67) — i.e. the ACRV1 pattern, three sub-methods of one Y2H screen, so a UniProt
`NbExp=3` here is one experiment counted three ways. Only 4 records are `anti tag coip` in human
cells. Profilin appears nowhere in the IntAct set.

GO has imported none of this, which is the right call. The **profilin** interaction, by contrast, is
from the primary paper and is well supported:
[file:human/ACTMAP/ACTMAP-uniprot.txt "Interacts (via N-terminus) with PFN2 isoforms IIa and IIb; the"]
… [file:human/ACTMAP/ACTMAP-uniprot.txt "interactions may facilitate efficient cleavage of the acetylated N-"]terminus of
immature actin, and [file:human/ACTMAP/ACTMAP-uniprot.txt "Interacts with PFN1"]; the binding
surface is mapped to [file:human/ACTMAP/ACTMAP-uniprot.txt "The N-terminal proline-rich disordered region contributes to"]
the interaction with PFN2. Corroborated independently:
[PMID:42159598 "These IP-MS experiments also revealed stereoselective reductions in the enrichment of established ACTMAP-interacting proteins, such as profilin 1 and 2 (PFN1/2)"].
`GO:0005522 profilin binding` exists and is informative, and GOA has no interaction annotation at
all — so this is a concrete, fillable gap. Note the caveat: the "may facilitate efficient cleavage"
mechanism is UniProt's hypothesis, so annotate the *binding*, not a substrate-delivery function.

## 7. Mouse phenotype, and the MGI gap

[PMID:36173861 "Its ablation resulted in viable mice in which the cytoskeleton was composed of immature actin molecules across all tissues."]
[PMID:36173861 "However, in skeletal muscle, the lengths of sarcomeric actin filaments were shorter, muscle function was decreased, and centralized nuclei, a common hallmark of myopathies, progressively accumulated."]
[PMID:36173861 "Thus, ACTMAP encodes the missing factor required for the synthesis of mature actin and regulates specific actin-dependent traits in vivo."]

Despite that knockout being in the same paper, MGI still carries root `ND` (no data) annotations for
mouse Actmap in all three aspects (`GO:0003674`, `GO:0008150`, `GO:0005575`, `GO_REF:0000015`). The
sarcomere/muscle-function phenotype is therefore uncurated. It is deliberately **not** proposed as a
human annotation here: the phenotype is mouse-only and the human evidence is biochemical.

## 8. Reference hygiene

- No retractions or corrections. Checked `CommentsCorrections` via E-utilities for all three PMIDs:
  `36173861` has none; `42159598` is `UpdateOf 41757055` and `41757055` is `UpdateIn 42159598`.
- **The affinage record cites the same study twice.** Its 2026 finding is attributed to
  "PMID:42159598, PMID:41757055", but those are the JACS paper and its own bioRxiv preprint. Cited
  as two sources this reads as independent corroboration; it is one study. The review cites the
  peer-reviewed JACS version (`42159598`) and records `41757055` as `LOW` relevance / the preprint.
- No `PMID:bio_*` pseudo-PMIDs in the citation list; all three ids are numeric and resolve.
- Affinage's own mechanism grounding (`GO:0140096`, `GO:0016787`, `GO:0005829`) was not imported, per
  the standing rule; its narrative was used only as a lead and every claim above is anchored to a
  PMID or to UniProt.

## 9. Row-by-row disposition

| # | term | evidence | action | why |
|---|---|---|---|---|
| 1 | GO:0005737 cytoplasm | IEA (SubCell) | ACCEPT | faithful mapping of UniProt's own `Cytoplasm` call; both papers describe ACTMAP as cytosolic, so `GO:0005829` is plausible but I could not verify a fractionation/imaging experiment (Science full text unavailable) — raised as a question instead |
| 2 | GO:0004239 initiator methionyl aminopeptidase | IEA (Ensembl) | MODIFY | same term problem as row 5, plus reciprocally circular (§4) |
| 3 | GO:0016485 protein processing | IEA (Ensembl) | ACCEPT | term correct; redundant/circular with row 6, recorded but not a defect in the term |
| 4 | GO:0070005 cysteine-type aminopeptidase | IDA (FlyBase) | ACCEPT | best available MF; mechanism twice-tested (§2); `has_input` ACTB/ACTG1 added. Verified about the odd assigner: FlyBase holds `GO:0070005` and `GO:0016485` ISS on fly `Q9VCE8` with WITH/FROM `UniProtKB:Q5BKX5`; that the human IDA was created as the ISS source is inference. It is the *only* row in GOA capturing the cysteine mechanism, since UniProt annotated only `GO:0004239` |
| 5 | GO:0004239 initiator methionyl aminopeptidase | IDA (UniProt) | MODIFY | wrong released product and wrong EC, plus family conflation (§3); the branch argument does not discriminate the replacement and motivates the term request instead |
| 6 | GO:0016485 protein processing | IDA (UniProt) | ACCEPT | core biological process; `has_input` ACTB/ACTG1 added, which is what records the substrate (§10) |
| 7 | GO:0005522 profilin binding | IPI (proposed) | NEW | §6 |

## 10. The substrate is absent from the GO record, and the fix is an extension, not a process term

*(Journal order: the case for a process term is recorded first, then the objections that killed it.
The conclusion is the "What replaced it" paragraph — no `GO:0030047` annotation is proposed.)*

Nothing in ACTMAP's GOA record says the protein it processes is actin. `GO:0030047 actin
modification` ("Covalent modification of an actin molecule") says it exactly, and the precedent is
already set one step downstream: **NAA80 carries `GO:0030047` by IDA from three separate papers**
(`PMID:29581253`, `PMID:29581307`, `PMID:30028079`; verified via QuickGO for `Q93015`), alongside
`GO:0017190` and `GO:0018002` for the N-terminal Asp/Glu acetylation it performs. Human evidence for
ACTMAP is loss-of-function and directly quotable, hence **IMP**:
[PMID:42159598 "genetic disruption of ACTMAP by CRISPR/Cas9 gene editing resulted in substantial accumulation of immature actin as measured by Western blotting with an antibody recognizing the N-terminus of β-actin"]
and [PMID:42159598 "which produced a concentration-dependent increase in immature β-actin"] on
covalent Cys132 engagement.

**Withdrawn after review (see §14).** Two objections, and the second is decisive:

1. `GO:0030047`'s ancestors include `GO:0030036 actin cytoskeleton organization` and
   `GO:0030029 actin filament-based process`, so the term hands a substrate-directed enzyme
   cytoskeletal-organisation ancestry on the strength of a modification result — the §5
   role-conflation risk re-entering through the ontology's `is_a` structure rather than through the
   annotations. This applies to NAA80 identically, so on its own it is an argument for a question to
   GO editors, not against the annotation.
2. **GO keeps proteolysis and protein modification in disjoint branches.** Computed:
   `GO:0016485 protein processing` is under `GO:0006508 proteolysis` and **not** under
   `GO:0036211 protein modification process`; `GO:0030047 actin modification` is under `GO:0036211`
   and **not** under `GO:0006508`. So a proteolytic event has no place in the modification branch at
   all, and the NAA80 precedent is an acetyl *transfer* — an additive modification — which does not
   extend to peptide-bond hydrolysis. (The term's only child, `GO:0007014 actin ubiquitination`, is
   additive too.) Same shape as the ABR lesson that GO keeps the Rac and Rho *regulation* branches
   disjoint: the structure, not the label, decides.

**What replaced it.** The substrate is recorded with `RO:0002233` has_input extensions to ACTB
(`UniProtKB:P60709`) and ACTG1 (`UniProtKB:P63261`) on **both** the accepted `GO:0070005` MF row and
the accepted `GO:0016485` BP row. That states the same fact with no branch violation and no unwanted
ancestry. The definitional question — whether GO intends "covalent modification" to include
hydrolytic removal — is now the primary `suggested_questions` item, with the placement question
secondary to it.

## 11. Sibling and repo-wide cross-checks

- `ACTR5` and `ACTR8` merged into `main` while this review was in progress (PRs #2290, #2291, #2293),
  and `ACTRT3` during round 2 (#2296). Re-checked each time: none mentions ACTMAP, actin maturation,
  N-terminal processing or NAA80, so there is no sibling inconsistency to reconcile.
- Grepped every `*-ai-review.yaml` in the repo for `GO:0004239` and `GO:0030047`: **ACTMAP is the
  only gene review that touches either term**, so no other merged review has already resolved these
  rows a different way.
- `ACTB`, `ACTL7A`, `ACTL7B`, `ACTL8`, `ACTR1A`, `ACTR1B`, `ACTR10` were checked for statements about
  actin maturation or N-terminal processing. None makes any; `ACTL7A`'s N-terminal-extension material
  is about a LIM-domain ligand, unrelated.

## 12. Gates

- `checkquotes.py`: all `supported_by`/`provenance`/`findings` quotes in the review verified verbatim,
  0 problems; the bracketed quotes in these notes verified by the same normalisation, 0 problems.
  (Counts are printed by the runs rather than restated here, since round 2 changed them.)
- Extra check beyond the shared script: every `file:` quote was additionally required to be an
  **exact** (not whitespace-normalised) substring, which is what catches a UniProt quote that
  silently crosses a `CC       ` continuation line. Clean on every run; the figure is deliberately
  not restated here, for the same reason as the bullet above - and because a stale copy of it is
  exactly what masked the duplicate-key bug described in §15.
- `just validate human ACTMAP`: `✓ Valid`, one warning left standing deliberately - "No annotations
  reference available deep research files". The affinage record's substantive content is entirely
  traceable to PMIDs which are cited directly, and the campaign rule forbids quoting a provider
  sentence as `supporting_text` for a mechanistic claim, so citing it would be decorative.
- `cache/go/terms.csv`: 0 deletions versus `origin/main`; exactly 1 addition (`GO:0070005`) appended
  at EOF without re-sorting - `GO:0030047` was removed again when that annotation was withdrawn. Note that `just validate` **de-duplicated**
  `GO:0001675` and `GO:0009566`, main's two known pre-existing duplicates; that unrelated change was
  reverted by restoring main's file and re-appending only the two new rows, so the duplicates remain
  as `main` has them.
- The bioinformatics report was re-generated from scratch and byte-compared against the committed
  copy: `RESULTS.md` reproduces exactly and `results.json` is identical.

## 13. A claim of mine that was wrong, and how it was caught

My first pass wrote "would correct 4 gene products in 4 species", taken from the taxon-restricted
census. That census covers `9606,10090,7227,7955,559292`, so it **cannot see** the bovine (`A6QQD2`)
and *Xenopus* (`B0BM95`) members of PTHR28631, both of which carry `GO:0004239` by ISS. The true
figure is **6 of 6 reviewed family members**. The number was not wrong as scoped, but the sentence
built on it understated the scope of the fix, which is the load-bearing part of the argument.

Caught by asking each PANTHER-reviewed accession directly rather than reading the census total — the
same "the denominator is set by my query, not by the biology" mistake the campaign has hit before.
The fix is now computed by `family_wide_usage()` in the script and printed as its own table, so the
two numbers (taxon-restricted census, family-wide count) are visibly different quantities instead of
one being mistaken for the other. All four assertion sites were corrected together
(`review.reason`, `review.knowledge_gaps[0].resolution`, `suggested_questions[0].question`, and these
notes) using a script that asserts each anchor is present before replacing, re-greps afterwards, and
checks that exactly the intended leaf values changed and no structure did. The PR body was the fifth
site and was patched too.

## 14. Round 2: the reviewer was right, and the decisive fact was not the one it used

`ai4c-reviewer` requested changes on one item: `GO:0030047 actin modification` is a
covalent-modification term proposed for a proteolytic event, the NAA80 precedent is *acetylation* and
does not transfer, and this very file already demonstrated the side-effect-free alternative —
`RO:0002233` has_input extensions.

Checked before conceding, and the check went **against** me and beyond the reviewer's own argument:
`GO:0016485 protein processing` is under `GO:0006508 proteolysis` and **not** under
`GO:0036211 protein modification process`, while `GO:0030047` is under `GO:0036211` and **not** under
`GO:0006508`. The branches are **disjoint**, so this is not a matter of how loosely "covalent
modification" reads — GO's structure already says a proteolytic process does not live there. The
annotation was withdrawn and the substrate moved onto has_input extensions on the two accepted rows.
Both facts are now computed by `process_branch_audit()` in the script, so the ancestry and NAA80-IDA
claims are no longer the only uncomputed ones.

Four non-blocking suggestions, all taken:

- **The exopeptidase argument does not discriminate the two terms.** Correct: `GO:0004239` and
  `GO:0070005` are both under `GO:0008238`, so ground 2 cannot motivate replacing one with the other.
  The row now says so explicitly and attributes ground 2 to the *term request*, leaving grounds 1
  (wrong EC / wrong released product) and 3 (family conflation) to carry the MODIFY.
- **Row 4's FlyBase-assigner explanation was unsourced.** Split into the verified part — FlyBase holds
  `GO:0070005` and `GO:0016485` ISS annotations on fly `Q9VCE8` with WITH/FROM `UniProtKB:Q5BKX5`, now
  printed by the script — and the causal step ("the human IDA was created to serve as the ISS
  source"), which is labelled a plausible inference rather than a fact.
- **`core_functions.substrates` listed ACTA1 where the extensions listed only ACTB/ACTG1.** ACTA1
  removed; the knowledge gap now records that its omission is deliberate and why.
- **The description stated the alpha-actin activity flatly.** Hedged in both the top-level
  `description` and the core-function description: established for mouse, inferred for human by
  similarity (`ECO:0000250|UniProtKB:J3QPC3`).

## 15. Round 3: a duplicate YAML key, and a number I explained away

The reviewer found a genuine bug in the round-2 edit. Adding provenance to the accepted
`GO:0016485` row produced **two `supported_by:` keys in the same mapping**. PyYAML keeps the *last*
value for a repeated key, so the two `RESULTS.md` entries were deleted before any consumer saw them -
the validator, the renderer, the exporters, `checkquotes.py`, and my own invariant harness alike.
Merged into a single four-entry list; verified by counting `supported_by` entries on that row (2 → 4)
and by loading the whole file through a duplicate-key-rejecting loader.

**The part worth recording is how it hid.** The file holds **27** `reference_id: file:` lines while
the parsed exact-substring check reported **25**, and the notes still carried the round-1 figure of
**26**. I had written "the count moved from 26 to 25 when the GO:0030047 annotation was withdrawn" -
which is arithmetically true (that row carried one `file:` quote) and *wrong as an explanation*,
because the same round also added two entries that should have taken it to 27. The coincidence made a
rationalisation look like a reconciliation. This is the campaign's own "do not rationalise a numeric
discrepancy - investigate it" rule, failed on the very number I had just edited.

It is also the "detector and mutator must agree on scope" failure in a new guise: **every quote gate
in this repo walks the parsed document, so none of them can see a quote that parsing removed.** The
gate reporting clean was not weak, it was blind.

Two guards added so the class cannot recur silently here:

1. `audit_actmap_claims.py` now loads the review through a `_StrictLoader` that **raises** on a
   duplicate mapping key, rather than relying on any downstream consumer to notice.
2. It also cross-checks **raw against parsed** - the number of `reference_id: file:` lines in the text
   versus the number that survive `safe_load` - so a discarded entry is reported as an arithmetic
   mismatch even if the strict loader were bypassed. A seventh self-test case reintroduces the exact
   duplicate key and confirms both fire.

Whether a duplicate-key-rejecting loader belongs in the **shared** validator is a good question and
deliberately not answered here: `src/ai_gene_review/validation/` is shared infrastructure and out of
scope for a gene PR. Nothing in the repo would flag this today, so it is worth raising separately.

Two further reviewer suggestions, both taken:

- **The disjointness sentence in `render()` had its boolean interpolated but its explanatory clause
  hardcoded**, so a future ontology change could have printed `False` next to prose asserting the
  `True` case. The clause is now generated from the per-term flags, with an explicit warning appended
  if the test ever fails.
- **`census()` and `family_wide_usage()` read `numberOfHits` for a total but derived their breakdowns
  from a capped `results` page.** Nothing was truncated at 86 and 6 hits, but the script's contract is
  to fail loudly, so `assert_complete_page()` refuses any response where
  `len(results) != numberOfHits` and names the fix. Verified by feeding it a synthetic truncated
  response. Fitting, since the error this review corrected on itself was also a denominator set by a
  query rather than by the biology. **Round 4 widened it to all six `/annotation/search` call sites**
  (`source_evidence()`, the NAA80 probe, the fly-ortholog query and `curation_state()` were still
  bare), which matters most for `source_evidence()` because that is what backs the
  `CIRCULAR_PROPAGATION` disposition. The one deliberately unguarded call is the `limit=1` probe that
  exists only to read `numberOfHits`, where the guard would correctly abort; it is commented as such.

## 16. Round 4: three non-blocking items from the approving review

Approved in round 3, with three suggestions. Two were accuracy defects in committed files rather than
polish, so they were fixed rather than deferred.

1. **The truncation guard covered 2 of 6 call sites while §15 described it in general terms.** That is
   an overclaim in a committed file, and the uncovered `source_evidence()` is precisely what the
   `CIRCULAR_PROPAGATION` disposition rests on. All six `/annotation/search` calls now go through
   `assert_complete_page()`; §15 states the coverage and names the single deliberate exception.
2. **The raw-vs-parsed cross-check counted parsed entries only when `supporting_text` was truthy,
   while the raw side counted every `reference_id: file:` line.** All 27 currently carry a quote, but
   `supporting_text` is optional in the schema, so a future bare `file:` provenance entry would have
   been reported as a discarded entry when nothing was discarded — a false positive in a guard, which
   is worse than no guard because it trains you to ignore it. The count is now keyed on
   `reference_id` alone. **Round 5 made that verification reproducible from the repo** rather than
   asserting it in prose: see §17.
3. **The PR description's Gates section still carried the round-1 figures** (41 quotes, 26 `file:`
   quotes) where round 3 reports 40 and 27. Description-only; patched.

## 17. Round 5: the guard that its own self-test could not reach, and a count that conflated two keys

The approving review added two observations about the raw-vs-parsed cross-check. Both were right, and
between them they were the last places where this gene's tooling claimed more than it demonstrated.

**The self-test could not reach it.** Case 7 reintroduces the duplicate `supported_by` key, but
`_StrictLoader` raises on it and `check_structural()` returns *before* the arithmetic below runs — so
the one check whose whole purpose is to survive a bypass of the loader had no case that fired it, in a
file whose stated standard is "prove every check can actually fire". Worse, §16 recorded a
verification "on a synthetic document" that existed only in a throwaway command, i.e. not reproducible
from the repo — the same defect as the §15 coverage sentence fixed one round earlier. Fixed by
factoring the comparison into `_cross_check(raw, doc)` and adding a **case 8** that calls it directly
on a synthetic (raw, parsed) pair: silent on a matched pair, reporting on a lossy one. Eight cases now,
all firing, clean baseline silent.

**The arithmetic covered only `file:` references.** Restricting to `file:` left the PMID and GO_REF
reference_ids outside it, so a duplicate key discarding a PMID-only `supported_by` list would have been
invisible to the arithmetic — and the arithmetic exists to *back up* the loader, not to duplicate a
subset of its coverage. Now counts every `reference_id` on both sides.

**A measurement correction, found by making the check work.** The review cites "46 `reference_id`
lines"; a bare `grep -c reference_id:` does report 46, and my own grep had agreed. But **7 of those are
`original_reference_id:`** — a different key, naming the annotation's own GOA reference, carrying no
supporting_text and belonging to no list. The honest total is **39**, and raw 39 now equals parsed 39.
Two real bugs surfaced from insisting the numbers reconcile rather than adopting the quoted figure:
the first regex omitted the `- ` list marker and matched **nothing** (reporting a spurious 39-entry
loss), and the same omission made the synthetic self-test assertion fail. Both were visible only
because the check was made to run on real input instead of being reasoned about.

Stopping here. The curation content has been settled since round 2 and the remaining rounds have all
been about the tooling that guards it; the working tree is clean and nothing is outstanding.
