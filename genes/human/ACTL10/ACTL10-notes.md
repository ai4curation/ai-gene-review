# ACTL10 (human, Q5JWF8) — review notes

Journal for the PAINT + affinage review. Provenance is inline; every quote below was
checked as a verbatim substring of the cited file before being used.

## 1. Where this gene starts from: a genuinely dark gene, and how dark

ACTL10 has **three GOA rows** — two IBA and one IEA derived from one of them. There is no
experimental annotation of any kind, in any aspect.

UniProt's record is almost empty of function. The only `CC` line in the whole entry is

> `CC   -!- SIMILARITY: Belongs to the actin family. {ECO:0000305}.`
> [file:human/ACTL10/ACTL10-uniprot.txt]

`ECO:0000305` is curator inference, not even similarity to a named entry. There is **no
FUNCTION line, no SUBCELLULAR LOCATION line and no SUBUNIT line**. This is worth
contrasting with the reviewed sibling ACTL8, which at least carries a
`Cytoplasm, cytoskeleton {ECO:0000250}` location — ACTL10 has nothing to place it anywhere.
The only `FT` feature is `FT   CHAIN           1..245`: no nucleotide-binding site, no
active site, no modified residue.

Corroborating how dark it is:

- `DR   Pharos; Q5JWF8; Tdark.` — Pharos' own "dark protein" classification.
- `DR   PAN-GO; Q5JWF8; 2 GO annotations based on evolutionary models.` — i.e. GO's
  curated set for this gene is two phylogenetic inferences and nothing else.
- All three UniProt `RN` references are large-scale sequencing submissions (the chromosome
  20 paper, the Celera submission, the MGC cDNA collection). **Not one functional paper.**

But it is not undetected: `PE   1: Evidence at protein level;` with
`KW   Proteomics identification; Reference proteome.` So the correct statement is that
there is no *functional or biochemical* characterisation — not that there is no data at
all. It is expressed and detected: `DR   HPA; ENSG00000288649; Tissue enriched (testis).`
[all four from file:human/ACTL10/ACTL10-uniprot.txt]

## 2. The affinage record is empty — and that is not evidence

`ACTL10-deep-research-affinage.md` came back with `gates_passed: True`, `n_discoveries: 0`,
`citation_count: 0`, and the body "No mechanistic discoveries found in literature."

Per the campaign rule (burned on ACP7), an empty provider record is **not** evidence that
literature is absent. Searching Europe PMC independently found 43 hits for `ACTL10` and 31
for the old symbol `C20orf134`, and among them **one paper carries ACTL10 in its title**,
which affinage missed entirely:

- **PMID:32742462** *Prognostic role of ACTL10 in Cytogenetic Normal Acute Myeloid
  Leukemia* (J Cancer 2020, full text cached). This is a TCGA correlative study of RNA
  expression and DNA methylation against survival — **no functional experiment,
  no localisation, no biochemistry**. Its own framing confirms the darkness rather than
  relieving it: [PMID:32742462 "Actin-like 10 (ACTL10) is a member of the actin family;
  however, to the best of our knowledge, there are very few studies on the ACTL10 gene."]
  and it closes by saying [PMID:32742462 "future research should focus on investigating the
  molecular mechanisms"]. It supports **no GO annotation**: a survival correlation is not a
  function.
- **PMID:35180326** *The Wnt1-Cre2 transgene is active in the male germline* (Genesis 2022).
  Mouse `Actl10` appears only because it sits near the transgene insertion site. Reading the
  whole paragraph (not just the sentence naming the gene) is what makes it usable: it gives
  expression, and explicitly withholds function —
  [PMID:35180326 "Actl10 and 1700003F12Rik were both enriched in testis at the tissue
  level"], [PMID:35180326 "Necab3 and Actl10 were moderately expressed"] in spermatids, and
  [PMID:35180326 "Actl10 and 1700003F12Rik mutant mice have not been linked to germline
  biology"]. That last is the authors' own statement about the state of knowledge, which is
  a legitimate thing to cite; it is *not* me inferring an absence.
- PMID:36160324 (a computational study of actin variation) turned out to contain **no
  ACTL10 mention at all** and is not cited.

Retraction check (the ACTL8 trap): PubMed `pubtype` for 32742462, 35180326, 36160324,
11780052 and 15489334 is plain `Journal Article` / `Comparative Study` — **no retraction or
erratum** on anything relied on here.

Everything else in those search results is ACTL10 appearing as a row in a methylation-array
or RNA-seq table. There is no functional literature.

## 3. The central finding: Q5JWF8 begins in the middle of the actin fold

This started as a suspicion from a single number and ended as the main result of the review.
Full reproducible detail in `ACTL10-bioinformatics/RESULTS.md`.

Human ACTL10 is **245 aa**; mouse Actl10 is **346 aa** and several other mammals are 366–368.
Two things then fell out.

**(a) The length variation does not follow the phylogeny.** Across 87 mammalian entries whose
gene name is exactly ACTL10, lengths run 169–487 aa, and in **4 of 4** sister-taxon pairs
tested the two members of one family disagree — *Sapajus apella* 368 aa vs *Cebus imitator*
245 aa (sister genera in Cebidae), *Marmota* 346 vs *Sciurus* 245, *Urocitellus* 346 vs
*Ictidomys* 245. Sister genera cannot differ by 120 residues for phylogenetic reasons. That
points at the annotation pipeline, but on its own it does not say which class is wrong.

**(b) The human genome encodes the missing region, in frame.** The MANE transcript
`ENST00000677665` is a **single exon** with 555 nt of annotated 5′ leader contiguous with the
CDS. Translating that leader in the CDS reading frame — with the frame *proven* by first
asserting the CDS translates to the Swiss-Prot sequence — gives 185 codons containing exactly
one in-frame stop, after which there are **167 uninterrupted codons** running straight into
the annotated initiator. Their translation is unmistakably actin, including
`IAVVVDQGSGFTKAGFAGEN`, which is actin's **phosphate-binding loop 1** (`DNGSGMCK` in
β-actin — the motif that grips the nucleotide β-phosphate).

The extended 412-aa ORF is not a spurious read-through:

| compared with | %id vs 245 aa | score | %id vs extended | score |
|---|---|---|---|---|
| *Sapajus apella* ACTL10 (368 aa) | 96.3 | 1117 | 96.5 | **1835** |
| *Callithrix jacchus* ACTL10 (368 aa) | 93.5 | 1082 | 93.2 | **1772** |
| mouse Actl10 (346 aa) | 78.0 | 868 | 80.6 | **1383** |
| human β-actin | 33.9 | 244 | 34.7 | **553** |

A 123-codon stretch cannot be 96% identical to a sister primate's annotated protein by
accident. **And the ancestral initiator is identifiable:** the Met1 of both *Sapajus* and
*Callithrix* ACTL10 aligns to position 45 of the extended human ORF, where the human genomic
codon is **CTG** (chr20:33667129), not ATG. The human locus has lost the initiator its
orthologues use; the next in-frame ATG lies ~120 codons downstream, and that is exactly where
Swiss-Prot, RefSeq and MANE all begin the protein.

**Scoping this correctly matters.** What is established: the sequence in Q5JWF8 is not the
whole of ACTL10's actin homology, so any residue tally computed from Q5JWF8 measures the
annotation boundary as much as the protein. What is **not** established: which product the
human cell makes. A lost initiator with a conserved downstream reading frame is compatible
both with a genuinely shortened human protein and with initiation at a non-AUG codon or an
unannotated upstream exon. Settling it needs N-terminal proteomics, not sequence analysis.
I have deliberately not asserted a length for the human protein.

## 4. Consequence: ACTL8's committed panel mis-scores ACTL10, and the correction flips the sign

The reviewed sibling ACTL8 built a residue panel (PDB 2BTF nucleotide site, PDB 6DJO filament
protomer interface) that **already included ACTL10**, and ranked it **last of fourteen** — 5 of
38 chemically compatible interface positions, below even Arp3. That reads as the most degraded
actin-like protein in the family.

My script recomputes the same contacts with the same structures and cutoffs, and **asserts that
it reproduces ACTL8's committed numbers** before going further; it reproduces all three shared
rows exactly (ACTB 37/1/0/0, ACTL8 8/3/24/3, ACTL10 3/2/13/20). I then split the single `gap`
column by cause — *outside span* (the query never reaches the position) versus *internal gap*
(a real deletion). The result:

| ACTL10 sequence used | interface: id/cons/non-cons/int-gap/**outside** | positions present | compatible |
|---|---|---|---|
| Q5JWF8, 245 aa as annotated | 3/2/13/0/**20** | 18 | **5/18** |
| extended ORF, 412 aa | 7/4/23/4/**0** | 38 | **11/38** |

**20 of ACTL10's 38 "interface" positions were not substitutions at all — they were positions the
annotated sequence does not reach.** Repaired, ACTL10 scores **11/38, exactly ACTL8's own
11/38**, and *Sapajus* ACTL10 independently gives 11/38 too. ACTL10 is an ordinary member of the
divergent-actin band, not an outlier below Arp3.

The nucleotide site moves the same way, and this is the sharpest version of the point. The five
positions Q5JWF8 fails to reach are **13, 14, 15, 16, 18 — precisely phosphate-binding loop 1**.
In the extended ORF they read G/S/G/F(conservative)/K: **four identical and one conservative, an
intact P-loop 1**. Overall the extended ORF scores **15/19 compatible**, which is *better* than
ACTL8 (14/19) and ACTL7A (14/19). The extended human ORF and *Sapajus* ACTL10 give **identical
calls at all 19 positions**, which is independent corroboration that the extended sequence is
the real one.

So the mirror error the brief warns about (ABHD8) was live here and the measurement refuses it:
**ACTL10 is not a fold that has lost actin's residues.** The one feature that looked lost is
present. This is why nothing in this review is a REMOVE on structural grounds, and why no
nucleotide-binding term is proposed either — residues being present is a *possibility*, not a
measurement, exactly as ACTL8 concluded for its own ATP site ("untested, not refuted").

## 5. Sibling cross-check: all three rows are byte-identical to already-merged reviews

Every one of ACTL10's three rows has a byte-identical WITH/FROM counterpart in a merged sibling
review, so the AADACL trio hazard (same row, three different verdicts) is live. Checked
programmatically, not by eye:

| ACTL10 row | identical row in | that review's verdict |
|---|---|---|
| `GO:0015629` IBA, node PTN002631484, 25 tokens | **ACTL8** | KEEP_AS_NON_CORE |
| `GO:0005200` IBA, node PTN000940351, 11 tokens | **ACTR10** | ACCEPT (core) |
| `GO:0007010` IEA from `GO:0005200` | ACTL7A / ACTL7B / **ACTR10** | MODIFY→GO:0030036 / REMOVE / KEEP_AS_NON_CORE |

The siblings disagree with each other, so I cannot simply copy one. The disagreements are
principled once the grounds are read rather than the verdicts:

- **ACTR10 ACCEPTed `GO:0005200` on gene-specific experimental grounds** — it is a bona fide
  dynactin subunit and "ACTR10's own contribution to dynactin's structural integrity is exactly
  what this MF expresses". ACTL10 has no complex, no localisation, no phenotype, no biochemistry.
  So ACTR10's ACCEPT does not transfer.
- **ACTL7A and ACTL7B REMOVEd `GO:0005200`** on two grounds that are both *absent* for ACTL10:
  their row was **TAS** citing a paper containing no functional data (ACTL10's is a live IBA from
  ten experimentally-annotated donors), and PAINT had **explicitly IRD-negated** the term at their
  node PTN008986528 (PAINT has *not* negated it on ACTL10's branch). So their REMOVE does not
  transfer either.
- **ACTL8's KEEP_AS_NON_CORE on `GO:0015629`** rests on the donating node being the correct LCA
  of a heterogeneous clade — which is a property of the node, and ACTL10 sits on the *same* node
  with the *same* 25 tokens. That one does transfer, and I follow it.

## 6. WITH/FROM resolution, and what it rules out

Built from the GOA field programmatically with the count asserted, never by hand (this drifted on
3 of 6 rows on ACTR10 and on 2 of 2 genes that tried it by hand).

- `GO:0015629`: 25 tokens, 24 protein → **24/24 resolved, 24/24 carry their own
  experimental-code annotation** for the term or a descendant, across 12 organisms. Two resolve
  only to unreviewed (TrEMBL) entries — reported rather than hidden; both still carry their own
  IDA, so evidence provenance and name provenance are separate numbers here.
- `GO:0005200`: 11 tokens, 10 protein → **10/10 resolved, 10/10 carry their own experimental
  evidence** (mouse/rat Actg1 IDA, yeast ACT1 IDA, yeast ARP1 IDA, yeast ARP10 IPI×3, human ACTB
  EXP+IDA+IMP, human ACTR2 IDA, human ACTR3 IDA, Dicty act1/act10 IDA).
- Resolver gotcha fixed: WormBase tokens need bare `xref:WBGene…`; the documented
  `xref:wormbase-…` form returns **zero hits**, which reads as "no such source" rather than
  "wrong query". Four *C. elegans* actins were briefly and wrongly logged as unresolvable.

**Consequence for classification:** because every protein donor on both rows carries its own
experimental evidence, `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` would be *contradicted
by my own analysis*. The correct value is `PROPAGATION_BAD` — sound source annotations that should
not transfer to this target.

## 7. PAINT has already ruled against `GO:0005200` for divergent actins — eight times

From the repo's cached `interpro/panther/PTHR11937/PTHR11937-paint.tsv`. `GO:0005200` is asserted
by **IBD at one node, PTN000940351**, from 10 experimentally-annotated seeds. It is then **negated
by IRD (`negated: true`) at eight nodes descending from it** — dated 2025-08-05 to 2026-04-16, so
current, not stale:

| node | clade (identified from that node's other IBD rows) |
|---|---|
| PTN000233596 | Arp2 (seeds include P61160, plus `GO:0005885` Arp2/3 complex) |
| PTN000233796 | Arp3 (seeds include P61158) |
| PTN000233752 | Arp5 / INO80 (`GO:0031011`, seed Q9H9F9) |
| PTN000233887 | Arp6 (`GO:0000812` Swr1 complex, seed Q9GZN1) |
| PTN000234048 | Arp8 (`GO:0031011`, seed Q9H981) |
| PTN001732543 | ACTL6A/B (`GO:0035267` NuA4, `GO:0016514` SWI/SNF) |
| PTN007551901 | ACTR1A/B (`GO:0106006`) |
| PTN008986528 | ACTL7A/7B (also given parent `GO:0005198` by IBA instead) |

So GO's own phylogenetic pipeline has decided, repeatedly, that "structural constituent of
cytoskeleton" does **not** transfer to divergent actin relatives — and where it wanted to keep
something, it dropped to the parent `GO:0005198` rather than keeping `GO:0005200`.

**Which genes are left holding it?** QuickGO: 43 human `GO:0005200` IBA annotations, of which
exactly **10 come from PTN000940351**: the four conventional muscle actins **ACTA1, ACTA2, ACTC1,
ACTG2** — where it is plainly right — plus six divergent proteins **ACTL9, ACTL10, ACTR10,
ACTRT1, ACTRT2, ACTRT3**. ACTL10 is in the residual set purely because PAINT has not yet visited
its branch. Of those six, only ACTR10 has independent evidence for the term (dynactin).

That is a single, node-level fix that would correct five genes at once, and it belongs in
`suggested_questions` stated **once with all affected genes named** — not repeated per gene.

**Independent convergence, found after rebasing onto a main that had moved.** ACTR5 and ACTR8
merged while this review was in progress. ACTR8's review reaches the *identical* tally from the
same cached file — "PTHR11937 carries 9 GO:0005200 rows in total: 8 IRD negatives at divergent
nodes and 1 IBD positive at the actin node" — and already asks whether "the IRD discipline
applied here be extended to the divergent actin-like nodes that currently lack it". Two agents
arriving at the same 8-plus-1 count from the same file is good corroboration. It also means my
PAINT question must not be a near-duplicate: what ACTR8's question lacks is the **target list**,
so mine now supplies the enumeration (which ten genes still receive the term, which five would be
fixed, and that ACTR10 must be spared because it has its own dynactin evidence) and explicitly
credits ACTR8's for the proposal. Neither ACTR5 nor ACTR8 has a GO:0005200 GOA row at all, which
is exactly what the IRD negations at their nodes PTN000233752 and PTN000234048 predict — a small
confirmation that the mechanism I am describing does what I say it does.

ACTR8 adds one fact worth recording because it validates the *form* of the recommendation: the
ARP8 IRD block is "exactly right - the human crystal structure shows loop insertions that explain
ARP8's inability to polymerise". So IRD is the established, evidence-backed device for exactly
this situation, which is why extending it is the right ask rather than deleting annotations
gene-by-gene.

**A separate tension worth reporting, not asserting.** Arp2 (P61160) and Arp3 (P61158) are among
the ten seeds of the ancestral `GO:0005200` IBD at PTN000940351, and QuickGO confirms each holds
its own IDA for the term — yet PAINT negates the term by IRD at Arp2's and Arp3's own clade nodes.
IRD blocks propagation rather than deleting the direct annotation, so this is not strictly
contradictory; but the ancestral state is being supported by proteins whose own clades have been
excluded from it, and it is worth asking PAINT whether that is intended.

## 7b. Three late checks, run rather than inherited

Added after the coordinator relayed three lessons from reviews that merged during this work. The
instruction was to verify rather than inherit, including the ACTL8 leads — a coordinator summary
carries more apparent authority than the review behind it.

**(i) Count how many entities each supporting reference annotates.** ACTL10's GOA has **no
PMID-backed rows at all**, so the "one paper projected across N entities" pattern has nothing to
bite on in its literal form. The node-level analogue does apply, and both IBA rows are guilty of
it: they **share the same reference, `GO_REF:0000033`**, and each is a single projection —
`GO:0015629` from PTN002631484 to **18** human genes, `GO:0005200` from PTN000940351 to **10**,
each with identical evidence. Neither is an independent statement about ACTL10.

The two rows are not independent of *each other* either. Of the 10 protein donors on the
`GO:0005200` row, **6 also appear on the `GO:0015629` row** (`MGI:MGI:87906`, `RGD:1304556`,
`SGD:S000001855`, `UniProtKB:P60709`, `dictyBase:DDB_G0269234`, `dictyBase:DDB_G0289811`). The **4
that are unique** to the `GO:0005200` row — and therefore the only ones making it more specific
than a generic actin-cytoskeleton call — are yeast **Arp1** (`SGD:S000001171`), yeast **Arp10**
(`SGD:S000002513`), human **Arp3** (`P61158`) and human **Arp2** (`P61160`). Arp2 and Arp3 are
seeds *at* PTN000233596 and PTN000233796, which are two of the eight nodes carrying the
`GO:0005200` IRD negation; yeast Arp1 is a dynactin filament subunit and the centractin clade node
PTN007551901 also carries an IRD. So the specificity of this row rests largely on donors from
clades GO's own pipeline has excluded from the very term they donate. That is a substantive
strengthening of `PROPAGATION_BAD`, found only by asking what each donor contributes rather than
counting donors.

**(ii) Publisher Corrections are invisible to a publication-type query.** Checked
`CommentsCorrections/RefType` on the efetch XML for both load-bearing PMIDs: **PMID:32742462 and
PMID:35180326 have no `CommentsCorrections` element at all** — no correction, erratum or
retraction. Separately, ACTL8's affinage record cites the **retracted** `PMID:32125225`; ACTL10's
affinage record has `citation_count: 0` and cites nothing whatsoever, so there is no shared
reference and nothing in this review can rest on it. Verified by grep, not assumed.

**(iii) The ACTL8 census, re-derived from QuickGO.** The brief asked whether ACTL8's mis-placement
applies to ACTL10. Queried directly for all eight divergent human actin-like / actin-related-T
proteins:

| gene | IBA rows | under PTN002631586 / PTN007551913? |
|---|---|---|
| ACTL7A | 3 | no |
| ACTL7B | 3 | no |
| **ACTL8** | **11** | **yes, both** |
| ACTL9 | 2 | no |
| **ACTL10** | **2** | **no** |
| ACTRT1 | 5 | no |
| ACTRT2 | 2 | no |
| ACTRT3 | 2 | no |

ACTL8's finding is **confirmed** (it alone is under either narrow node; 11 rows against a median
of 2 for the other seven), and it **does not extend to ACTL10**, which sits at the family median
of 2 and under neither narrow node. I also re-derived the 18-gene membership of PTN002631484 and
it matches ACTL8's claim exactly. So the answer to the brief's first lead is a clean negative:
**ACTL10 is correctly placed in the tree; its problem is not mis-placement but a mis-annotated
protein sequence.** A negative result from a check is still a finding, which is why it is recorded
here and in the review rather than dropped.

## 7c. Review round: three non-blocking suggestions, all accepted

PR #2298 was APPROVED with three suggestions. All three were real and all three are addressed.

**(i) Scope the P-loop-1 claims.** The reviewer's sharpest point: "ACTL10 conserves
phosphate-binding loop 1" is true of the extended reading frame and **false of Q5JWF8 as
annotated**, which is ABSENT at all five of those positions per my own RESULTS.md. Three sites in
the review stated it unscoped — the `description`, the `GO:0015629` summary, and the `GO:0005200`
reason — plus one in these notes. All four now name the sequence.

Because this is one claim asserted at a dozen sites, the invariant is now **mechanical rather than
hand-checked**: `ACTL10-bioinformatics/check_claim_scoping.py` requires every P-loop-1 mention in
the review and the notes to sit within 300 characters of a phrase naming which sequence is meant.
It fails loudly if it finds zero claims, since a lint that inspects nothing passes vacuously. The
count is deliberately not quoted here: an earlier draft of this paragraph said "12" and the
reviewer counted 13, because a number in prose that has to track a script's output drifts the
moment the text changes. Run the lint for the current figure.

Two bugs in that lint, both found by running it rather than reading it, and both worth recording:

1. **My first draft was defeated by YAML line-wrapping.** Folded scalars store "does not reach" as
   `does not\n      reach`, so literal matching flagged three *correctly scoped* sites as
   violations. I nearly widened the regex to make them pass — which would have been rationalising
   a discrepancy instead of investigating it. The real fix is to whitespace-normalise before
   matching. Had I "fixed" it the other way I would have shipped a lint that reports false
   positives, which trains a reader to ignore it.
2. **The self-test's own mutations reproduced the same bug.** My mutation asserted on *normalised*
   text and substituted on *raw* text, so the phrases it meant to strip did not match and the
   mutation silently did nothing. The self-test honestly reported FAILURE rather than passing, but
   the fault was in the mutation, not the lint. Fixed by mutating normalised text and asserting
   `detected == changed` — the detector/mutator scope invariant. Also worth noting: my first two
   mutations deleted *one* scoping phrase from passages containing *two*, so the claims stayed
   scoped and the lint was right to keep passing. A mutation must remove **all** scope from a
   claim's window, or add a claim that has none.

**(ii) The `is_active_in` qualifier went undiscussed.** Fair, and it is a genuine
over-assertion: `is_active_in` states that ACTL10 *carries out its molecular function* in the
actin cytoskeleton, and no molecular function has been measured for it at all, so the qualifier
presupposes exactly what is unknown. `located_in` would say what the inference supports. This is a
transfer artefact of the same kind as the term's breadth — the qualifier is correct for the
conventional-actin donors — not a curator error, so the action stays `KEEP_AS_NON_CORE` and the
term is unchanged; a qualifier swap is a GOA-side change. It is now discussed in the row and
raised for PAINT alongside the node recommendation.

**(iii) Assert page-size saturation.** The orthologue query used `size=500` and read the count
from `len(results)`. It now takes the authoritative total from the **`x-total-results` header**,
aborts if a full page comes back, and asserts parsed count equals declared count. Break-tested by
setting `page_size = 10`, which correctly aborts with "returned a full page (10) ... (87
declared)". A fresh run reproduces `RESULTS.md` and `results.json` byte-for-byte, so the guard
changed no number.

## 7d. ACTRT3 merged mid-review with the same row and a different action

Found by re-running the terms.csv gate against a `origin/main` that had moved again: ACTRT3 (#2296)
landed titled *"a GO:0005200 that PAINT has already rejected next door"*. It carries the **same**
`GO:0005200` IBA row from the same node and resolved it **MODIFY → `GO:0005198` structural molecule
activity**, where this review has `MARK_AS_OVER_ANNOTATED`. Two independently reviewed members of
the same six-gene residual set, one row, two actions — precisely the AADACL trio hazard, so it had
to be reconciled rather than left to a reader to notice.

The two agree where it matters and the divergence is principled. Both give
`root_cause: PROPAGATION_BAD`; both cite `FUNCTIONAL_DIVERGENCE`; I have added
`GRANULARITY_MISMATCH` to match ACTRT3's diagnosis, because the term being more specific than what
transfers is a property of the row, not of the remedy chosen for it. So the *diagnosis* is now
identical and only the action differs.

The action differs because ACTRT3's reason is explicit that its generalisation rests on
**gene-specific positive evidence**: "GO:0005198 is supported for ACTRT3 — it is a component of the
perinuclear theca's protein scaffold and contributes to its structural integrity". Generalising
therefore moves ACTRT3's row from an unsupported specific claim onto a supported general one.
ACTL10 has no counterpart: no complex, no assembly, no location, no phenotype, no partner. Since
`GO:0005198` is defined by contribution to the structural integrity of a complex or assembly,
substituting it here would exchange one unsupported assertion for a slightly less specific
unsupported assertion — and, because neither gene already carries `GO:0005198`, it would *newly
add* a molecular function to a gene that has none. That is the wrong direction for a Tdark protein.

Worth noting that ACTRT3 performs the same discrimination in the other direction, distinguishing
its MODIFY from ACTR10's ACCEPT on the ground that ACTR10 "has an ortholog-strength donor in the
seed set and ACTRT3 has none". So this row now has **three** actions across four merged reviews —
ACCEPT (ACTR10), MODIFY (ACTRT3), MARK_AS_OVER_ANNOTATED (ACTL10), REMOVE (ACTL7A/7B on a
different evidence code) — and unlike the AADACL trio, each is pinned to a stated, checkable
gene-specific fact rather than to a differing judgement about the same evidence. That is the
outcome the trio rule is asking for: not uniformity, but a reason per gene.

## 7e. The reconciliation covered one of the *two* rows shared with ACTRT3

The ACTRT3 reconciliation above fixed `GO:0005200` and left the derived `GO:0007010` row alone,
which the reviewer caught. ACTRT3 carries that row byte-identically too, and merged with a **fourth**
verdict on it — `KEEP_AS_NON_CORE`. Having just spent a paragraph arguing that a reader should not
have to notice a divergence themselves, stopping at one row was an oversight rather than a decision.

**Why ACTL10 does not follow ACTRT3 there.** ACTRT3's reason holds that the term "is true at this
level of generality and should not be removed", because ACTRT3 is a perinuclear-theca scaffold
component required for acrosome assembly. Truth *at that level of generality* is exactly what is
unestablished for ACTL10, which has no demonstrated involvement in organising anything. So for
ACTR10 and ACTRT3 the row is true-but-uninformative; for ACTL10 it is unsupported — a difference
`MARK_AS_OVER_ANNOTATED` records and `KEEP_AS_NON_CORE` would hide.

**The substantive half: my coded diagnosis said the opposite of my own prose.** The row was coded
`root_cause: PROPAGATION_BAD`, `failure_modes: [SOURCE_EVIDENCE_WEAK]`,
`source_status: SUPPORTS_SOURCE_BUT_NOT_TARGET`. Checking the schema rather than taking the
reviewer's word: `SUPPORTS_SOURCE_BUT_NOT_TARGET` is *"Source evidence supports the source
annotation…"* — which presupposes source evidence, while the comment on that very entity says the
source is a GO term carrying none. And `SOURCE_EVIDENCE_WEAK` (*"Source evidence is inferred,
statement-level, stale…"*) contradicts **this review's own finding one row above**, that every
donor carries its own experimental annotation. I had criticised exactly that inconsistency in the
`GO:0005200` row and then committed it here.

The schema has precise values for a transfer-from-a-transfer, and the merged siblings already use
them. Verified independently:

| review | action | root_cause | modes | source_status |
|---|---|---|---|---|
| ACTR10 | KEEP_AS_NON_CORE | NO_FAILURE_NON_CORE | – | `CIRCULAR_OR_REDUNDANT` |
| ACTRT3 | KEEP_AS_NON_CORE | `EVIDENCE_CIRCULAR_OR_REDUNDANT` | `CIRCULAR_PROPAGATION` | `CIRCULAR_OR_REDUNDANT` |
| ACTL7A | MODIFY | TERM_SCOPING_PROBLEM | GRANULARITY_MISMATCH, SOURCE_EVIDENCE_WEAK | SOURCE_WEAK_OR_INFERRED |
| ACTL7B | REMOVE | SOURCE_WEAK_OR_INFERRED | SOURCE_EVIDENCE_WEAK, FUNCTIONAL_DIVERGENCE | SOURCE_WEAK_OR_INFERRED |

ACTL10 was the only one of the four using `SUPPORTS_SOURCE_BUT_NOT_TARGET`, and the worst fit. Now
`EVIDENCE_CIRCULAR_OR_REDUNDANT` / `CIRCULAR_PROPAGATION` / `CIRCULAR_OR_REDUNDANT`, matching ACTRT3
exactly. ACTL7A/7B's weak-source values are right *for them*, because their source row is a 1999 TAS
with genuinely weak evidence — the distinction is real, not a house style.

**Generalisable:** the action was correct throughout and only the machine-readable fields were
wrong, so nothing in the prose flagged it. These fields are the output the failure-mode taxonomy
exists to produce, and prose agreeing with itself is no evidence that the codes agree with the
prose. Worth diffing coded metadata against sibling reviews on identical rows as a matter of course,
not just actions.

Also fixed: a sentence saying substituting `GO:0005198` "would newly place a molecular function on a
gene that currently has none" — literally false, since `GO:0005200` *is* an MF row on ACTL10. It now
says "for which none is supported". The one sentence in that paragraph a curator could check against
the GOA file and find wrong.

## 7f. Gate defect worth carrying forward: diff terms.csv against the MERGE BASE, not the tip

`git diff origin/main HEAD -- cache/go/terms.csv | grep '^-GO:'` reported a deletion twice on this
branch — `GO:0031011` and later `GO:0070005` — and **neither was a deletion**. Both were rows *added
to `main`* by sibling PRs (ACTR5/ACTR8, then ACTMAP #2295) after this branch's base. Diffing against
a moving tip attributes another branch's addition to your branch as a removal.

The form that does not misfire:

```
MB=$(git merge-base origin/main HEAD)
git diff $MB HEAD -- cache/go/terms.csv | grep '^-GO:'     # this branch's own deletions
git show origin/main:cache/go/terms.csv | cut -d, -f1 | sort | uniq -d   # duplicates in the merged result
```

The first answers "did I delete anything", the second "will the merge carry a duplicate". The tip
diff answers neither cleanly while siblings are in flight, and three were. This branch changes
`cache/go/terms.csv` not at all, so both are trivially satisfied — but the first pass spent a cycle
"fixing" a deletion that never happened, and `git checkout origin/main -- cache/go/terms.csv` at
that moment would have silently pulled another branch's row into this PR.

## 8. Negative results, recorded because a null from a check is still a finding

- **IntAct**: `findInteractions/Q5JWF8` returns `totalElements: 0`. No interaction data at all, so
  the ACRV1-derived "is `NbExp=3` really one screen" and "resolve the partner accessions" checks
  have nothing to run on. Consistent with ACTL10 having no `GO:0005515` row.
- **GO-CAM**: no entry for ACTL10 or Q5JWF8 in `gocams/index.tsv`.
- **Downward-MODIFY check** (from ACRV1): asked whether either IBA lands *above* its donors' own
  terms. It does not — the donors' experimental annotations are to `GO:0015629` and `GO:0005200`
  themselves, the same terms propagated. No downward MODIFY is warranted on either row.
- **CRISPR screens**: `DR   BioGRID-ORCS; 170487; 21 hits in 1141 CRISPR screens.`
  [file:human/ACTL10/ACTL10-uniprot.txt] — 21/1141 is unremarkable and I draw nothing from it.

## 9. Verdicts and why

- **`GO:0015629` actin cytoskeleton (IBA) → KEEP_AS_NON_CORE.** Same node, same 25 tokens, same
  reasoning as merged ACTL8: PTN002631484 spans conventional actins, the POTE genes and the
  divergent actin-likes, so the generic compartment term is the true **LCA** of a heterogeneous
  donor set and there is no granularity defect to fix. Non-core because no experiment has placed
  ACTL10 in any compartment — and unlike ACTL8, UniProt does not even offer a by-similarity
  location. Kept because ACTL10 *is* a real divergent actin (34.7% to β-actin over the extended
  ORF, with P-loop 1 intact on that extended frame though absent from the annotated 245-residue
  sequence), so the term asserts nothing the sequence contradicts.
- **`GO:0005200` structural constituent of cytoskeleton (IBA) → MARK_AS_OVER_ANNOTATED.** The
  route by which real actins earn this term is filament formation, and ACTL10's protomer interface
  — measured on the *repaired* sequence, so the argument does not rest on the annotation artefact
  — is 11/38 compatible against β-actin 38/38 and Arp53D 33/38 (a divergent actin that *does*
  polymerise). PAINT has negated this exact term at eight sibling divergent nodes and dropped to
  the parent where it wanted to keep anything. But **REMOVE is not earned**, and the control that
  refuses it is one I computed myself: **Arp3 scores 8/38, below ACTL10, and Arp3 genuinely does
  make actin-like protomer contacts** at an Arp2/3 branch. So the interface metric bounds
  *canonical two-stranded filament incorporation*, not all protomer contact — the caveat ACTL8's
  analysis raised against itself, which applies with equal force here. `MARK_AS_OVER_ANNOTATED`
  needs no positive argument; `REMOVE` does, and mine is unavailable.
- **`GO:0007010` cytoskeleton organization (IEA) → MARK_AS_OVER_ANNOTATED.** Its literal WITH/FROM
  is the GO term `GO:0005200`, so it is exactly as strong as the row above and no stronger. It is
  marked at the same level rather than removed (ACTL7B's route) because its basis is being marked,
  not removed; and it cannot follow ACTL7A's MODIFY to `GO:0030036`, because that was earned by a
  knock-out phenotype and ACTL10 has none —
  [PMID:35180326 "Actl10 and 1700003F12Rik mutant mice have not been linked to germline biology"].

**`core_functions` is left empty.** Per the brief, that claim had to be *tested* rather than
asserted, and section 4 is the test: the nucleotide site is well enough preserved that no
loss-of-function call is available, and the interface is degraded enough that no polymerisation
call is available either. Neither supports authoring a molecular function, and inventing one to
silence the validator's "No core functions defined" warning would be exactly the wrong move.
