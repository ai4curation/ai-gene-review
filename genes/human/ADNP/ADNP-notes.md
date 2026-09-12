# ADNP (human, Q9H2P0) — review notes

Working journal for the PAINT + affinage review. Provenance is inline as
`[PMID:xxxx "verbatim quote"]`.

## 1. What the gene actually is

ADNP is a 1102-residue nuclear protein with nine C2H2 zinc fingers (UniProt ZN_FING
74..97, 107..129, 165..188, 221..244, 447..469, 489..510, 512..535, 622..647, 662..686),
a homeodomain (DNA_BIND 754..814, PROSITE PS50071), and a single C-terminal PxVxL motif.
Its defining activity is as the sequence-specific DNA-binding and assembling subunit of
the **ChAHP** complex:

[PMID:29795351 "ADNP interacts with the chromatin remodeller CHD4 and the chromatin
architectural protein HP1 to form a stable complex, which we refer to as ChAHP."]

[PMID:29795351 "Besides mediating complex assembly, ADNP recognizes DNA motifs that
specify binding of ChAHP to euchromatin."]

Repression by ChAHP is **not** classical HP1 heterochromatin silencing:

[PMID:29795351 "ChAHP-mediated repression, however, acts in a locally restricted manner
by establishing inaccessible chromatin around its DNA-binding sites and does not depend
on H3K9me3-modified nucleosomes."]

Three later papers extend and sharpen this:

- [PMID:31491387 "we demonstrate that the ChAHP complex (CHD4, ADNP, HP1) competes with
  CTCF for a common set of binding motifs"] — so ADNP occupancy also shapes local loop
  boundaries, and ChAHP sites sit mostly in SINE B2 elements.
- [PMID:42413491 "Our findings support a model in which ADNP recruits chromatin-remodeling
  activity in a sequence-specific manner, enabling transcriptional control and local
  modulation of chromatin architecture."] and, importantly for how much weight HP1
  deserves: [PMID:42413491 "we demonstrate in mouse embryonic stem cells that the CHD4
  subunit is essential for antagonizing CTCF and silencing the transcription of
  transposons, whereas HP1 proteins are dispensable"].
- [PMID:42413492 "Instead, we identify the ChAHP complex as a key repressor of SINE B2
  elements. ChAHP directly inhibits POL III transcription by blocking TFIIIB recruitment
  without affecting TFIIIC binding."] — mechanism resolved, and it is *not* heterochromatin:
  [PMID:42413492 "Although DNA methylation and heterochromatin formation have been
  implicated in their repression, we find that these pathways play only a minor role in
  mouse embryonic stem cells."]

The paralogue ADNP2 forms ChAHP2 and covers a different transposon class
[PMID:38960717 "Genetic ablation of ADNP2 alleviates ERV and LINE1 repression, which is
synthetically exacerbated by additional depletion of ADNP."].

## 2. The headline finding: an eight-residue peptide's pharmacology became the protein's GO record

**26 of ADNP's 53 GOA rows are Ensembl Compara projections (`GO_REF:0000107`).** Nineteen
come from rat `Adnp` (Q9JKL8) and seven from mouse `Adnp` (Q9Z103). Resolving each donor's
own primary reference — the campaign's highest-yield check — shows that **13 of the rat-derived
rows trace to experiments on the synthetic ADNP-derived octapeptide NAPVSIPQ ("NAP",
davunetide), applied exogenously, with the ADNP protein never perturbed or measured.**

The classification is computed, not hand-assigned: `ADNP-bioinformatics/analyze_compara_donors.py`
resolves every Compara row to its donor annotation and primary reference, pulls the title and
abstract from PubMed, and reports which peptide markers and which ADNP-scoped protein markers
fired. Output is committed as `results.json` / `RESULTS.md`.

The worst cases, in ascending order of how obviously wrong they are:

| human GO row | rat donor reference | what was actually assayed |
|---|---|---|
| `GO:0005507` copper ion binding, `GO:0042277` peptide binding | PMID:14706557 | NAP peptide vs beta-amyloid aggregation; the only binding reported is biotin-NAP binding Abeta |
| `GO:0046068` cGMP metabolic, `GO:0080164` reg. NO metabolic | PMID:11438390 | VIP / SNV / NAP dosed onto cortical cultures |
| `GO:0033484` intracellular NO homeostasis, `GO:0043524` neg. reg. neuron apoptosis | PMID:16938277 | i.p. ADNF-9 + NAP peptides in neonatal rats |
| `GO:0007614` short-term memory | PMID:12212775 | inhaled NAP in normal rats, water maze |
| `GO:0048487` beta-tubulin binding | PMID:16893427 | NAP peptide on an affinity column |
| `GO:0010976`, `GO:0051965` | PMID:15800376 | femtomolar ADNF-9 + NAP in culture |
| `GO:0045773` pos. reg. axon extension | PMID:19047645 | NAP peptide; the only siRNA is against *Fyn* |
| `GO:0010629` neg. reg. gene expression | PMID:15314252 | NAP; new datum is p53 as a NAP target |
| `GO:0050805` neg. reg. synaptic transmission | PMID:15963648 | **D-NAPVSIPQ**, the all-D enantiomer |

**The decisive single case is `GO:0050805`.** The molecule is an all-D-amino-acid octapeptide,
which no gene can encode [PMID:15963648 "Ethanol also inhibits L1-mediated cell adhesion in a
manner that is prevented by an octapeptide, D-NAPVSIPQ (D-NAP), as well as long chain alcohols
such as 1-octanol."], and the paper's own control says it did nothing on its own
[PMID:15963648 "Application of D-NAP alone had no effect on LTP induction or expression."].
The suppression required co-application with 50 mM ethanol. The donor evidence code is IMP,
which normally implies a perturbation of the gene; there was none.

**Second decisive case: `GO:0046068` / `GO:0080164`.** The paper is titled for vasoactive
intestinal peptide, and ADNP is not manipulated anywhere in it
[PMID:11438390 "In rat cerebral cortical cultures, 10(-16)-10(-7) M NAP increased intracellular
cyclic guanosine monophosphate (cGMP) (2.5-4-fold) and 10(-10) M NAP increased extracellular
nitric oxide (NO) by 60%."]. The authors themselves decouple the doses
[PMID:11438390 "However, the concentrations of NAP, SNV and VIP affecting NO production did not
match the neuro-protective doses."].

**`GO:0042277` peptide binding — the argument I first gave was wrong; the verdict is not.**
The binding measured is [PMID:14706557 "Further assays showed biotin-NAP binding to Abeta."],
so the entity that binds is the synthetic eight-residue NAP peptide. REMOVE rests on **entity
identity alone**: no experiment shows that sequence is released from ADNP, so nothing measured
here is a molecular function of the gene product. `PMID:14706557` annotates exactly one entity
in all of GOA, so no cross-reference is involved.

**Retracted from an earlier draft** (kept here because process history belongs in the notes,
not in a row summary). I originally argued the annotation was *directionally inverted* and that
RGD's own records made the inversion "explicit and checkable", citing the `GO:0042277` rows on
rat Tubb3 (Q4QRB4) and Tubb4b (Q6P9T8) that carry `WITH/FROM RGD:71030`. Both halves were
wrong. Abeta **is** a peptide, so for the fragment the direction is correct, not inverted. And
those tubulin rows come from **PMID:16893427**, the donor for `GO:0048487` beta-tubulin
binding, **not** for `GO:0042277` — `RESULTS.md` puts the two references on different rows.
There is no internal contradiction in RGD's records of the kind I described, and the claim
would have misled exactly the RGD/GO curators `suggested_questions[0]` is addressed to. The
tubulin cross-check is real and is deployed where it belongs, on the `GO:0048487` row.
**Generalisable lesson: check `original_reference_id` per row before reasoning across rows.**
Guarded by `audit_adnp_review.py` check **J**, which selects on the stable tokens
(`16893427`, `RGD:71030`, `Tubb3`, `Tubb4b`, `invert`) rather than on the conclusion's wording,
fires on the exact version that shipped (`12f374d14`), and is clean on the current file. Its
stated limitation: a paraphrase avoiding all five tokens would pass, so the prose still needs
human re-reading.

**Two of the peptides are not even ADNP fragments.** ADNF-9 is the active site of a different
protein [PMID:15800376 "The active site for ADNF function is localized to a 9-amino-acid stretch
(SALLRSIPA; ADNF-9)."], yet PMID:16938277 (ADNF-9 + NAP, i.p.) supplies two human IEA rows.

**`GO:0043524` reaches human twice and both chains end in peptide.** The rat donor is
PMID:16938277; the mouse donor is the 1999 cloning paper
[PMID:10037502 "In mixed neuron-astrocyte cultures, NAPVSIPQ provided neuroprotection at
subfemtomolar concentrations against toxicity associated with tetrodotoxin (electrical
blockade), the beta-amyloid peptide (the Alzheimer's disease neurotoxin), N-methyl-D-aspartate
(excitotoxicity), and the human immunodeficiency virus envelope protein."]. Checking the
*other* rodent source is what turned a suspicion into a verdict.

### The scoping bug in my own classifier

First pass called `GO:0045773` MIXED, because PMID:19047645's abstract contains an siRNA. Reading
it: the siRNA is against **Fyn kinase**, not ADNP
[PMID:19047645 "Pharmacological inhibition of Fyn kinase or expression of a Fyn kinase siRNA
abolished NAP-mediated axon outgrowth."]. Fixed by scoping protein-perturbation markers to
sentences that name ADNP. That changed the call on three references (PMID:15800376,
PMID:15963648, PMID:19047645) and is recorded in `RESULTS.md`. The self-test that encodes this
shape then caught a *second* defect in my own patterns: a bare `\bdisrupt` matched the title
"…by disrupting ADNP signaling", where what is disrupted is downstream NAP signalling, not the
gene product. Narrowed to require ADNP to be named as the thing lost.

### What did NOT confirm

- **Reference-projection test: negative.** Every rat donor reference annotates exactly one
  entity except PMID:16893427 (3 — Adnp plus two tubulins) and PMID:17222401 (2). No
  complex-to-subunit projection of the ACTR8 kind. Recorded so the next reader knows it was run.
- **Logical-opposite cross-product: negative.** Scanning the GOA TSV for `positive regulation of
  X` / `negative regulation of X` pairs found **no opposed pair at all**, so no shared-reference
  defect. The Wnt-direction disagreement in the literature (below) is real but is not encoded as
  an annotation contradiction.
- **Retraction / erratum: negative.** All **33** PMIDs in this review's reference list were
  checked via `CommentsCorrections` on their own PubMed records; none carries `RetractionIn`,
  `ErratumIn`, `ExpressionOfConcernIn` or a republication link. The sweep is performed by the
  committed `analyze_compara_donors.py` and its result written into `results.json` /
  `RESULTS.md`, so the claim is reproducible rather than a one-off shell command. Known hole,
  stated in `RESULTS.md`: a correction whose own PubMed id is null is invisible to this route
  and would need a Crossref `relation`/`update-to` lookup.
- **Four rat rows survive the check.** `GO:0030424` axon, `GO:0030425` dendrite, `GO:0043025`
  neuronal cell body and `GO:0005576` extracellular region rest on genuine immunodetection of the
  ADNP protein [PMID:19130308 "The dentate gyrus (DG) of the normal rat brain contains
  activity-dependent neuroprotective protein (ADNP) which is widely distributed in the cytoplasm
  of neurons and astrocytes."]. Not everything in the block is an artefact, and saying so is part
  of the finding.

## 3. `GO:0044849` estrous cycle — decided from the definition, not the label

`GO:0044849`'s definition is "A type of ovulation cycle, which occurs in most mammalian therian
females, where the **endometrium is resorbed** if pregnancy does not occur." Humans and other
catarrhines menstruate — the endometrium is shed. The formal taxon constraint is
`only_in_taxon Theria`, which humans satisfy, **so the constraint does not block the annotation
but the differentia in the definition does.** The rat annotation is separately weak: an IEP
recording mRNA oscillation [PMID:16023261 "Significant increases in the expression of the VIP
receptor type 2 (VPAC2) mRNA and parallel increases in a novel VIP responsive gene,
activity-dependent neuroprotective protein (ADNP) mRNA were detected in the rat vagina during
the estrus phase."]. REMOVE for human; the rat row is fine for rat, which is why
`source_status` is `SUPPORTS_SOURCE_BUT_NOT_TARGET` rather than `SOURCE_BAD`.

## 4. `GO:0009743` response to carbohydrate — an honest non-determination

The rat IEP cites PMID:19130308, whose abstract describes L-NAME, 7-nitroindazole, ODQ and
kainic acid — no carbohydrate [PMID:19130308 "Treatment with nitric oxide (NO) synthase (NOS)
inhibitor N(G)-nitro-L: -arginine methyl ester (L: -NAME) caused a decrease in ADNP expression
in granule cells which persisted 3 days post-treatment."]. The cached record has
`full_text_available: false`. **I am not asserting the rat annotation is wrong** — the supporting
experiment may be in the full text. I am declining to propagate an IEP across species, which is
a claim about the human row only. MARK_AS_OVER_ANNOTATED, `root_cause: SOURCE_WEAK_OR_INFERRED`.

## 5. `GO:0005576` extracellular region — a real measurement that still should not travel

Unlike the rest of the rat block this is a genuine protein measurement
[PMID:16845437 "In addition, ADNP-like immunoreactivity in the extracellular milieu of astrocytes
increased by approximately 1.4 fold after incubation of the astrocytes with VIP."]. Three things
hold it back: human ADNP has **no SIGNAL feature** (the FT table runs `CHAIN 1..1102` with no
cleaved leader) and no non-classical secretion route has been proposed; UniProt lists only
Nucleus and Chromosome; and the antibody was raised against the NAP epitope
[PMID:16845437 "Here, we investigate the subcellular localization of ADNP through cell
fractionation, gel electrophoresis, immunoblotting and immunocytochemistry using alpha-CNAP, an
antibody directed to the neuroprotective NAP fragment that constitutes part of an N-terminal
epitope of ADNP."], so it cannot distinguish full-length ADNP from a NAP-containing fragment in
conditioned medium. MARK_AS_OVER_ANNOTATED, not REMOVE.

Housekeeping: this row is the successor of `GO:0005615 extracellular space`, obsoleted
2026-03-06 and replaced by `GO:0005576`. The UniProt `DR GO;` list still shows the old id while
the GOA TSV has migrated — a harmless lag, noted so nobody reads it as a discrepancy.

## 6. The homeobox lead did NOT confirm — ADNP really is sequence-specific

The campaign's standing lead is "a homeobox does not establish sequence-specific DNA binding".
For ADNP it fails, and that is worth as much as a finding. The ISS/IEA route to `GO:0000977` and
`GO:0000981` runs through mouse PMID:17222401, a ChIP at promoters
[PMID:17222401 "The pluripotent P19 cells were used for ADNP-chromatin-immunoprecipitation,
showing direct interactions with multiple relevant gene promoters including members of the
up-regulated as well as the down-regulated gene clusters."] — and ChIP occupancy alone genuinely
would not distinguish direct recognition from tethering. Note **MGI read that same paper more
conservatively as `GO:0003682` chromatin binding while ARUK-UCL read it as `GO:0000977` +
`GO:0000981`**. The later ChAHP work vindicates the stronger reading independently of the paper
in question (section 1). ACCEPT, and the directional child `GO:0001227` is proposed additively
rather than as a replacement.

## 7. The `GO:0005515` block — 14 rows, one per partner

The `fetch-gene` stub had **47** entries against **53** distinct GOA rows. The whole gap is
`GO:0005515`: 14 GOA rows collapsed to 8 stub entries, one per PMID, dropping the partner
distinction. Restored to one row per (reference, partner). No distinct GO term was missing.

Partners resolve to four reviewed canonical Swiss-Prot entries — CBX5 (P45973, 191 aa), CBX1
(P83916, 185 aa), CBX3 (Q13185, 183 aa), CHD4 (Q14839, 1912 aa). No TrEMBL clones, no ORFeome
fragments. HP1 binding is recovered by **seven independent studies**, including OpenCell at
*endogenous* expression (PMID:35271311) and IP-MS in human induced neurons (PMID:36950384), so
it is not screen noise. Per the brief I did **not** use UniProt's `NbExp` (5/7/3) as an evidence
proxy; the reference-level count is the meaningful one.

MODIFY targets:
- HP1 rows → `GO:0070087 chromo shadow domain binding`. Proteins engage HP1 through PxVxL
  docking on the chromo shadow domain [PMID:20562864 "Proteins generally interact with HP1
  through a PxVxL (where x is any amino-acid residue) motif"], and ADNP's is conserved
  [PMID:38960717 "the C-terminal HP1 interaction motif (PxVxL) (Thiru et al. 2004; Mosch et al.
  2011) is well conserved"]. The scan is committed (`analyze_compara_donors.py`, `pxvxl_scan`,
  which also asserts Q9H2P0 is still 1102 aa before trusting any position): the single
  `P.V.[LMIV]` match is **PGVLL at 820–824**, immediately C-terminal to the homeobox — **but the
  same function reports 0.76 matches expected by chance** under the protein's own residue
  composition, so one match is what chance predicts and **its uniqueness is not evidence**. An
  earlier draft leaned on "exactly one match in 1102 residues" as though it were enrichment; it
  is not. The weight rests on the ADNP↔ADNP2 conservation and on all three HP1 paralogues
  binding. Caveat recorded as a knowledge gap: no ADNP PxVxL point mutant has been shown to lose
  HP1 binding, so this is motif + paralogue-wide binding, not a mapped surface.
- CHD4 row → `GO:0140463 chromatin-protein adaptor activity`, whose definition ("brings together
  a protein and a region of the chromatin … to establish or maintain the chromatin localization
  of the protein, or the complex to which it belongs") is exactly what the experiments assign to
  ADNP.

## 8. Reactome TAS — checked, benign

`GO:0005654` TAS from `Reactome:R-HSA-9940477` ("Formation of ChAHP complex"). Reference-projection
test: **4 entities (ADNP, CBX1, CBX3, CHD4), 1 term**. Complex-membership localisation spreading
to exactly the complex's members, with **no functional or phenotype term spreading alongside** —
the benign shape, not the ACTR8 shape. ACCEPT.

## 9. affinage: gate passed, recall missed, and one mechanistic error

`gates_passed: True`, 28 citations, `faith_pct: 100.0`. It is still not the literature search:

- **PMID:29795351 (Ostapcuk 2018, the ChAHP-defining Nature paper) is absent from its citation
  list**, as is PMID:31491387 (Kaaij 2019) and both 2026 *Mol Cell* papers. These are the papers
  GOA itself cites for ADNP's only human IDA. A passing gate is a floor on precision and carries
  no recall guarantee.
- **It states the complex composition wrongly**: its own grounding block reads
  `complexes: ChAHP complex (ADNP-CHD4-BRG1)`. ChAHP is ADNP–CHD4–**HP1**; BRG1/SMARCA4 belongs
  to a separate reported SWI/SNF association. Textbook case of why a provider sentence is a lead,
  not a source, for a mechanistic claim. Complex composition in this review is taken from the
  primary papers. The affinage file is cited once, in the `GO:0090575` row, quoting that exact
  line — as evidence *about the record*, not about biology.

The papers it did surface that mattered: PMID:32533114 (Wnt), PMID:25178163 (EB1/EB3 SxIP),
PMID:38479840 (SINE B2 / CTCF in blastocysts), PMID:41174994 (methyltransferase claim).

**Where the affinage record is cited.** In `references` only, with a `reference_review` marking
it `MISCITED` and recording both defects. It is deliberately **not** in any `supported_by`:
`supported_by` should carry evidence *for* an annotation, and quoting a statement this review
rejects would misuse the slot. The cost is that the repo's non-blocking
"no annotations reference available deep research files" warning now stands — correctly, since
no annotation here rests on the provider record.

## 10. Unresolved and recorded, not adjudicated

- **Wnt direction.** PMID:32533114 has ADNP stabilising beta-catenin
  [PMID:32533114 "Mechanistically, ADNP functions to stabilize β-Catenin through binding to its
  armadillo domain which prevents its association with key components of the degradation complex:
  Axin and APC."]; PMID:27903678 has ADNP repressing WNT in colorectal cancer. Both marked
  `DISPUTED`; GOA carries only the positive term.
- **Neurite direction.** NAP promotes neurite outgrowth in culture, but Adnp knockdown in cortical
  pyramidal neurons *increases* basal dendrite number and axon length (PMID:36631597). Feeds the
  MARK_AS_OVER_ANNOTATED on `GO:0010976`/`GO:0045773`.
- **Methyltransferase.** [PMID:41174994 "Immunoprecipitated fractions containing wild-type ADNP
  exhibited methyltransferase activity, which was reduced by nonsense variants."] Overexpression
  plus immunoprecipitate — a co-purifying enzyme is not excluded. No GO term proposed; reference
  flagged `LOW_QUALITY` for this claim specifically.
- **ADNP2 has no review in this repo** (`genes/human/ADNP2/` absent from main), so the
  sibling-consistency check on the shared `PTN000405125` IBA rows could not be run. Recorded as a
  CURATION knowledge gap. Q6IQ32 is on the same worklist line as ADNP.

## 11. Process log

- Worklist line `human,Q9H2P0,ADNP` verified against UniProt: `Q9H2P0 / ADNP_HUMAN / 1102 aa`.
- **The "no-IBA" worklist is wrong here too**: QuickGO returns **2 IBA rows** for Q9H2P0
  (`GO:0005634`, `GO:0010468`). Both adjudicated. `GO:0005634`'s WITH/FROM cites `UniProtKB:Q9H2P0`
  itself — the valid self-referential PAINT pattern, not circularity.
- Row reconciliation: TSV 53 data lines, 53 distinct, stub 47, gap = 6 collapsed `GO:0005515`
  rows. Reconciled before reviewing.
- `cache/go/terms.csv`, in two acts. **Act 1:** `just validate` added `GO:0070087` on a cache
  miss and, as documented, silently collapsed main's two then-existing duplicate curies
  (`GO:0001675`, `GO:0009566`, 2→1 each). Caught by a **multiset** `Counter` comparison; a set
  comparison would have sailed straight through, because the whole failure is two copies
  becoming one. **Act 2, and the more useful finding:** merging `origin/main` forward showed
  that main has since landed `src/ai_gene_review/tools/cache_lint.py` and
  `tests/test_cache_sorted.py`, which require every `cache/**/*.csv` to be **sorted by CURIE and
  deduplicated**. That **supersedes the append-at-the-end convention** this campaign has been
  following. The two orderings mis-aligned under git's line-based merge and silently duplicated
  **24** curies. Correct resolution is now: reset the file to main's version, let validate
  re-insert your row in sorted position, and verify with
  `uv run python -m ai_gene_review.tools.cache_lint`. Asserted afterwards four ways — nothing
  from main dropped, exactly one curie added, nothing invented, no duplicate anywhere.
- Quote surfaces: `checkquotes.py` checks 138; the committed `audit_adnp_review.py` checks 145.
  The 7-quote difference is exactly the `knowledge_gaps[].provenance` entries that
  `checkquotes.py` does not walk — derived independently from the parsed document rather than
  rationalised after the fact.
- Both committed scripts break-test their own guards: `analyze_compara_donors.py --self-test`
  (7 classifier directions, including the false-friend and other-gene-perturbation cases) and
  `audit_adnp_review.py --self-test` (baseline + 9 mutations + the SafeLoader dedup baseline).

## 12. Verdict tally

Generated from the review file, not hand-counted. `audit_adnp_review.py` check **I** asserts
this table equals the computed counts and fails if they drift.

<!-- verdict-counts:begin -->

| action | rows |
|---|---|
| ACCEPT | 14 |
| KEEP_AS_NON_CORE | 9 |
| MARK_AS_OVER_ANNOTATED | 8 |
| MODIFY | 15 |
| NEW | 2 |
| REMOVE | 7 |
| **total** | **55** |

<!-- verdict-counts:end -->

The first version of this PR's body stated a hand-counted tally that was **wrong on three of
six actions** (MODIFY, KEEP_AS_NON_CORE and ACCEPT). REMOVE and MARK_AS_OVER_ANNOTATED, the two
that carry the argument, happened to be right — which is exactly why the error survived a
read-through. Check I exists because of it: anything countable should be counted, and then
compared against what was written.
