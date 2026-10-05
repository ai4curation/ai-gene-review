# ARFGEF3 (BIG3) — review notes

UniProt `Q5TH69`, 2177 aa, HGNC:21213. Synonyms BIG3, C6orf92, KIAA1244.
Pharos class **Tdark**; `PE 1: Evidence at protein level` (detected by MS in
several proteomes, and by western/IHC in breast cancer tissue).

## Headline: the name asserts an activity the protein cannot perform

The gene symbol, the UniProt recommended name ("Brefeldin A-inhibited guanine
nucleotide-exchange protein 3", itself `ECO:0000305` — a curator inference from
similarity, not a measurement) and both `GO:0005085` rows all assert ARF-GEF
activity. Nothing has ever measured it on this protein, and the residue that
performs the chemistry is absent.

Sec7-domain ARF-GEFs act through one invariant glutamate, the "glutamic finger",
which inserts into the ARF nucleotide pocket to destabilise bound GDP. Chen *et
al.* showed BIG3 lacks it:

> [PMID:24997568 "they showed that BIG3 lacked the conserved motif and critically, the essential glutamate residue"]

> [PMID:24997568 "This region is conserved among the BIG3 orthologues, all of which lack the functional motif."]

and the divergence is not marginal:

> [PMID:24997568 "BIG3 showed only 21% identities to BIG1 and BIG2, with ~30% identity in DUF1981 and no significant similarity (i.e., a BLAST e-value of > 10) found in the Sec7 domain."]

The group that named the protein says the same thing in their own papers:

> [PMID:24711543 "It is worth noting that the single known functional domain in BIG3 by sequence analysis, the Sec7 domain, has a non-functional catalytic motif"]

> [PMID:27696409 "we recently identified BIG3 as a novel ARF GEF protein with a non-functional catalytic motif in the SEC7 domain"]

### Verified independently — `ARFGEF3-bioinformatics/`

I did not take this on the papers' word. Re-derived from live UniProt + MAFFT,
with the comparison panel built **from the GOA WITH/FROM field** rather than by
hand (`sec7_catalytic_check.py`, full write-up in
`ARFGEF3-bioinformatics/RESULTS.md`):

| class | n | residue at the derived glutamic-finger column |
|---|---|---|
| catalytically-verified WITH/FROM donors | 17 | **E in 17/17** |
| known-dead comparator (`ARFGEF1 E793A`) | 1 | A — scored absent |
| human ARFGEF3 | 1 | **N692** (`LLSLSNVEEVD`, zero motif matches) |
| mouse Arfgef3 | 1 | **S688** (`LLALSSVEEVD`) |

The column is *derived* from the known-active donors, not hardcoded, and
cross-checked against the alignment-free `[FY]-x-[LIVM]-P-G-E` motif. Controls run
in both directions and the `--self-test` exits 0: leave-one-out over all 17 donors,
a verified-active positive control, and a Glu→Ala mutant of that control which must
score negative (a detector that cannot report a negative proves nothing). The
mutation target is asserted present before it is mutated, so the control cannot
silently no-op.

**The asymmetry matters and I have kept to it.** Losing the catalytic residue is
strong evidence *against* the activity; retaining it would *not* have been evidence
*for* it. Only the negative direction is claimed.

**Reproduction defect found.** Chen *et al.*'s Methods give GEP100 as
`Swiss-Prot:Q6ND90`, which is a *Rhodopseudomonas palustris* succinate dehydrogenase
cytochrome b556 subunit (TrEMBL, no Sec7 domain). Human GEP100/BRAG2/IQSEC1 is
**Q6DN90** — two transposed characters. The script reports what each published
accession really resolves to and applies the correction explicitly.

### A caveat I could not close

Chen *et al.* write that their prediction is

> [PMID:24997568 "consistent with a previous demonstration by the GST-GAT pull-down assay"]

and the `<xref rid>` in the PMC XML resolves that citation to **PMID:24711543**
(Li *et al.* 2014). I could not locate a GST-GAT pull-down in the accessible text
of that paper — it is neither in the cached full text nor in any of its five named
supplementary figures, and PMC restricts its XML. So the *direct experimental*
demonstration that BIG3 fails to load ARF with GTP is asserted in the literature
but I could not verify it. **The review therefore rests on the residue analysis and
the authors' repeated sequence-level statements, not on that pull-down.** Recorded
as a question for the authors rather than quoted as evidence.

## What BIG3 actually does

Two well-supported activities, neither of them catalytic, and **neither in GOA**.

### 1. Sequestering PHB2 in the cytoplasm

The founding human paper:

> [PMID:19496786 "BIG3 trapped PHB2/REA in the cytoplasm and inhibited its nuclear translocation, and caused enhancement of ERα transcriptional activity"]

The mechanism is occlusion of PHB2's import receptors, not a generic tether:

> [PMID:26052702 "These data indicated that BIG3 may block the KPNAs (KPNA1, KPNA5, and KPNA6) binding region(s) of PHB2, thereby leading to inhibition of KPNAs-mediated PHB2 nuclear translocation in the presence of E2 in breast cancer cells."]

This is `GO:0140311 protein sequestering activity` almost verbatim — GO defines it
as "Binding to a protein to prevent it from interacting with other partners or to
inhibit its localization to the area of the cell or complex where it is active."
Both clauses are separately demonstrated here: the localisation clause by knockdown
and re-expression, the partner-occlusion clause by the karyopherin work.

**Parent vs child, weighed rather than defaulted.** `GO:0140311` is an `is_a` child
of `GO:0140313 molecular sequestering activity`, carrying the identical definition
with "a specific molecule" narrowed to "a protein". PHB2 is a protein, so the child
adds no claim that the ligand's identity does not already fix, and the child is
correct. This is the opposite situation to the PKA row, where `GO:0034237 protein
kinase A regulatory subunit binding` **would** add an unproven claim — the
interaction was measured but the RII-subunit specificity was only predicted in
silico — so that row deliberately stays at the parent `GO:0051018`. The test is not
"prefer the child" or "prefer the parent" but **whether the child asserts anything
the evidence has not already fixed.**

The same test applies to the phosphatase row: `GO:0004865 protein serine/threonine
phosphatase inhibitor activity` over its parent `GO:0004864`, because PPP1CA is
`EC 3.1.3.16`, a serine/threonine phosphatase by definition.

The downstream process is `GO:0042308 negative regulation of protein import into
nucleus`.

Interface mapped to a single predicted helix and confirmed by mutagenesis:
Q165/D169/Q173, within the experimentally-delimited PHB2-binding region 86–434
(PMID:24997568; the peptide built from it is ERAP, PMID:24051437). Note that
`BIG3` acting *on* ERα directly was tested and failed:

> [PMID:19496786 "we investigated the possibility of a direct interaction between BIG3 and ERα, but failed to indicate their interaction (data not shown)"]

so ERα-pathway terms would be a `ROLE_CONFLATION`: BIG3's substrate is PHB2, and ERα
activity is two steps downstream.

### 2. Scaffolding PKA and PP1Cα (AKAP function)

> [PMID:28555617 "We detected an endogenous interaction between BIG3 and PP1Cα in the ERα-positive breast cancer cell lines MCF-7 and KPL-3C, which highly express both proteins"]

> [PMID:28555617 "This showed that the introduction of WT-BIG3 inhibited endogenous PP1Cα activity in a dose-dependent manner, while ΔPP1Cα-BIG3 did not"]

Binding is via a canonical PP1C docking motif (RVxF, `1,228-KAVSF-1,232`) and the
`ΔPP1Cα` deletion abolishes it. E2-driven PKA phosphorylation of BIG3-S305/S1208
then relieves the inhibition, so PP1Cα dephosphorylates PHB2-S39. So BIG3 is a
genuine `GO:0008157 protein phosphatase 1 binding` + `GO:0004865 protein serine/threonine phosphatase
inhibitor activity` + `GO:0051018 protein kinase A binding` protein. **All three are
human, endogenous-protein experiments, and none is in GOA.**

This is also where the family connection survives: BIG1 and BIG2 carry AKAP
sequences too (PMID:28555617 intro). So what BIG3 inherited from the family is the
*scaffolding*, not the catalysis.

## Secretory-granule biology — real, but mouse

The strongest functional data are from mouse and must be encoded as ISS/ISO, not
IMP/IDA (the experiments were not done in human).

> [PMID:24711543 "BIG3 is predominantly localized to insulin- and clathrin-positive trans-Golgi network (TGN) compartments."]

> [PMID:24711543 "Furthermore, BIG3 predominantly localized to insulin granules of islet β-cells, as revealed by immuno-EM"]

> [PMID:24711543 "these results demonstrate that BIG3 negatively modulates insulin granule biogenesis and insulin secretion and participates in the regulation of systemic glucose homeostasis"]

Same sign in alpha cells:

> [PMID:25737957 "BIG3 is highly expressed in pancreatic alpha-cells in addition to beta-cells, but is absent in delta-cells."]

> [PMID:25737957 "Depletion of BIG3 in alpha-cells leads to elevated glucagon production and secretion."]

The authors' own model is explicitly that the *dead* Sec7 domain is the point:

> [PMID:24711543 "one of our hypotheses is that BIG3 acts as a competitive non-functional Arf-GEF, thereby negatively modulating granule production"]

That is a hypothesis, not a result, and I have not annotated it. But it does mean
the right reading of ARFGEF3 is not "a GEF that GO over-called" — it is "a
catalytically dead family member that regulates the pathway its active relatives
catalyse".

UniProt already carries the granule localisation as `ECO:0000250|UniProtKB:Q3UGY8`
(from mouse), which is where the `GO:0030133` / `GO:0030658` IEA rows come from.
Those SubCell terms say *transport vesicle*; the mouse data say *secretory granule*
and *trans-Golgi network*, which are different things — a genuine, fixable
mismatch (see the review's `GO:0030133` and `GO:0030658` rows).

## Localisation is context-dependent — three compartments, three cell types

| compartment | cell type | evidence |
|---|---|---|
| cytoplasm (diffuse) | human breast cancer | IHC/ICC, endogenous, PMID:19496786 |
| TGN / immature secretory granules | mouse islet β- and α-cells | PMID:24711543, PMID:25737957 |
| lysosome | mouse hippocampal neurons | PMID:27696409 |
| mitochondrion | human osteosarcoma lines | PMID:34363714 |

> [PMID:27696409 "In hippocampal neurons, BIG3 is mainly localized in lysosomes, and its depletion selectively impairs inhibitory synaptic transmission."]

> [PMID:34363714 "BIG3-PHB2 complexes were localized mainly in mitochondria in OS cells, unlike in estrogen-dependent breast cancer cells."]

The osteosarcoma paper explicitly contrasts its own result with the breast-cancer
localisation, so this is not a contradiction being papered over — it is a
cell-type-dependent distribution. `GO:0005737 cytoplasm` (the one EXP row) is the
only one of these four that is human *and* in GOA; the other three are coverage gaps
and are all non-human or non-canonical enough that I have kept them out of
`core_functions` and raised them as questions instead.

## affinage record: gates passed, and two citations are a different gene

`ARFGEF3-deep-research-affinage.md`, `faith_pct: 100.0`, 14 citations, trust gates
clear. The gates are a **precision** gate; there is no recall gate, and both
failure directions showed up here.

**Precision failure the gates do not cover.** Two of its 14 citations —
PMID:14657013 and PMID:15707593 — are not about this gene at all. They concern
"BIG-3 = **BMP-2-induced gene 3 kb**", a **34-kDa, seven-WD-40-repeat** protein
(PMID:11551928), i.e. a pure name collision with ARFGEF3/BIG3 (2177 aa, 240 kDa,
Sec7 + ARM, no WD40). The affinage narrative presents their chondrocyte- and
osteoblast-differentiation results as ARFGEF3 findings. Both are marked
`relevance: NONE`, `correctness: MISCITED` in the review, and nothing rests on them.
Note the gates still passed: the PMIDs are real and the quotes faithful — the join
to *this gene* is what is wrong, which is precisely the class of error no mechanical
gate sees.

**Recall failures.** An independent PubMed sweep over `ARFGEF3 OR BIG3 OR BIG-3 OR
KIAA1244` (129 hits, mostly "Brain Injury Guidelines" noise) found four real
ARFGEF3 papers the provider never returned:

- **PMID:27696409** — lysosomal localisation and GABAergic transmission in
  hippocampal neurons. An entire tissue context and a fourth compartment, missing.
- PMID:28500289 — stapled ERAP peptide.
- PMID:25483453 — xanthohumol as a BIG3–PHB2 interaction inhibitor.
- PMID:42478137 — BIG3 overexpression in extramammary Paget's disease.

So: 2/14 provider citations were the wrong gene, and the single most
compartment-informative paper was absent. Consistent with the campaign measurement
that the gates certify only what was returned.

## Propagation analysis (`ARFGEF3-bioinformatics/`)

All 32 distinct WITH/FROM tokens across the 7 rows that carry one resolve; zero
unresolved. `WB:WBGene00007703` resolved only by free-text fallback (WormBase *gene*
ids are absent from UniProt's `xref:wormbase` index, which holds protein ids) and is
reported as such. Four MOD ids map to >1 UniProt entry and are reported with their
hit counts rather than collapsed.

**ARFGEF3 does not appear in either of its own WITH/FROM lists**, so there is no
self-referential donor and no experimental grounding on the target anywhere in
either chain.

### `GO:0005085` — the node is sound, the target is the exception

18 protein donors. **18/18 carry their own experimental evidence** for the term, and
**15/18 carry their own IDA** (direct exchange assay). The tempting dismissal
("these donors only carry the same family-level inference") is factually false here,
in every single case. So `SOURCE_WEAK_OR_INFERRED` would be contradicted by my own
analysis; the correct classification is `PROPAGATION_BAD` +
`PSEUDO_OR_SUBACTIVITY_LOSS`: PAINT placed the activity correctly at an ancestral
node, and ARFGEF3 is the descendant that lost it.

Reciprocal observation worth sending to PAINT, **checked rather than conjectured**
(`reciprocal_donor_check.py`): **MON2** (`SGD:S000005241`) is the only donor with
**no annotated SEC7 domain** and no `IPR000904`, and is also one of the three
without an IDA (IGI/IPI/ISS only). MON2 and ARFGEF3 share `IPR015403`
(Mon2/Sec7/BIG1-like HDS).

The script selects suspects *by measurement* — a protein donor of the term lacking
the term's own InterPro signature — so MON2 is its output, not its input, and
exactly one donor qualifies. MON2 **receives** `GO:0005085` by IBA from
`PANTHER:PTN008950430`, the same node ARFGEF3's row comes from, and its entire
non-IBA support is one reference, `PMID:12052896`, with no IDA. That paper is itself
careful — its title calls Ysl2p/Mon2 "homologous to Sec7 domain guanine nucleotide
exchange factors" and it claims only a "potential function as an Arf guanine
nucleotide exchange factor".

So the same node **is** donating GEF activity to a *second* member that has never
been shown to perform it — the mis-placed-member pattern, with the donor and the
victim being the same kind of protein. (The WITH/FROM-set identity the script also
reports is largely *entailed* by the shared node, since PAINT emits one
descendant-evidence list per IBD; it is a consistency check on the lookup rather
than a second independent finding.)

### `GO:0016192` — the broad term is the correct LCA

17/18 donors carry their own experimental evidence, but they do **not** agree on a
process: between them they hold `GO:0006887`, `GO:0006888`, `GO:0006890`,
`GO:0006891`, `GO:0006892`, `GO:0006893`, `GO:0006895`, `GO:0016197`, `GO:0032509`,
`GO:0042147`, `GO:0043001`, `GO:0048193` and `GO:0048205` — anterograde, retrograde,
intra-Golgi, endosomal and exocytic. `GO:0016192` is the genuine LCA of a
heterogeneous donor set. `GRANULARITY_MISMATCH` requires the donors to agree; they
do not, so no specificity upgrade is proposed on that row and it is ACCEPTed.

## A second, systematic defect: SL-0244 maps into the wrong GO branch

Found while checking the two `GO_REF:0000044` vesicle rows rather than accepting
them. `subcell_mapping_check.py` resolves each SubCell id in the WITH/FROM column
and asks how the mapped GO term relates to the term the literature supports —
querying QuickGO's `is_a`/`part_of` closure, not reading it off the labels.

| SubCell | UniProt's name | maps to | literature supports | relation |
|---|---|---|---|---|
| `SL-0086` | Cytoplasm | `GO:0005737` | — | EXACT |
| `SL-0244` | **Secretory vesicle** | `GO:0030133` transport vesicle | `GO:0030141` secretory granule | **DISJOINT** |
| `SL-0245` | **Secretory vesicle membrane** | `GO:0030658` | `GO:0030667` | **DISJOINT** |

`GO:0030141` and `GO:0030133` are sibling branches under `GO:0031410`; neither is
an ancestor of the other. GO defines `GO:0030133` as the **constitutive** secretory
pathway, while insulin and glucagon granules are **regulated** secretory granules.
And the mismatch starts inside UniProt: SL-0244's own definition is
regulated-pathway language ("cargo - e.g. hormones or neurotransmitters ... docks
and fuses to release its content").

So the two rows needed MODIFY (a replacement) rather than a specificity
refinement. `SL-0244` is applied to **130,685** UniProtKB entries and `SL-0245` to
**90,419** (read from the `x-total-results` header). That is the number the rule is
*applied to*, **not** a claim that all of them are mis-annotated — SL-0244 is broad
and some members may genuinely be constitutive.

## Two gates I had to fix before they were worth anything

Recording these because both initially reported success while being blind.

1. **My quote checker was structurally blind to 27 of 65 quotes.** It collected
   only dicts carrying *both* `reference_id` and `supporting_text`, so every
   `references[].findings[]` quote — where the reference is implicit in the
   position — was skipped, and it reported "0 problems" over the 38 it could see.
   The raw-vs-parsed reconciliation (65 raw keys vs 38 parsed) is what exposed it.
   I derived the expected number independently (27 findings + 32 annotation
   `supported_by` + 6 `core_functions` = 65) rather than finding a story that made
   the gap acceptable, which confirmed the *document* was intact and the *checker*
   was at fault. Fixed, then mutation-tested on a findings-level quote specifically.

2. **The `file:` quote checker's mutation test passed by crashing.** Exit 1 came
   from a `RuntimeError` in root derivation, not from detection. A check that kills
   the harness is worse than none, because it still prints as though it ran. Fixed
   with a CWD fallback and re-tested: the mutant now produces a `PROBLEM` line and
   the clean file exits 0.

All five `file:` quotes were then verified as literal substrings of `RESULTS.md`.
CI does **not** check these (`file` is in `skip_prefixes`), so they are the one
fabrication surface here, and each is a computed table row chosen so an exact match
is meaningful.

## The pre-write hook validates against the SHARED checkout, not your worktree

Worth knowing for anyone running agents in isolated worktrees, because it produces
confident false failures.

`.claude/hooks/validate_ai_review_pretool_hook.py` computes
`project_root = Path(__file__).parent.parent.parent` and runs the validator with
`cwd=project_root`. `__file__` is the **shared checkout's** hook, so validation uses
the shared checkout's schema and its `genes/` tree — not the worktree the edit is
actually being made in. Two consequences hit this gene:

- The shared checkout sits on `paint/ABHD8` (tip `0e4e91ae55`), which **predates**
  `4697a4e0c7` "Add FamilyReview schema with machine-checkable residue claims"
  (#2757). So the hook rejected `residue_claims` as an unknown property even though
  the slot has been in `PropagationReview` on `main` for some time.
- `reference_base_dir: genes` resolved against the shared checkout, where
  `genes/human/ARFGEF3/ARFGEF3-bioinformatics/RESULTS.md` does not exist, so all
  five `file:` references were reported as pointing at a non-existent file.

**Diagnostic that settles it: run the hook's own procedure on a file you know is
good.** Copying the *unmodified, committed* review to a temp directory and running
`uv run ai-gene-review validate --no-goa` on it returns `✓ Valid`. So does
`just validate human ARFGEF3` in the worktree. Only the hook disagrees, and the
branch-ancestry check (`git merge-base --is-ancestor 4697a4e0c7 0e4e91ae55` → 1)
names the reason.

Same shape as the shared-`checkquotes.py`-with-a-hardcoded-root incident: when a
shared tool suddenly reports failures on work you believe is clean, **suspect the
tool and check what root it resolved** before changing anything. "Fixing" these
would have meant deleting two correct `residue_claims` blocks and five correct
citations. CI is unaffected — it validates against `main`'s schema on real paths.

## The pre-write hook's failures were mostly collateral — verify before "fixing"

The first write attempt was blocked with a long error list including six
"Text part not found as substring" failures and several missing-`file:`-reference
errors. **Those were not real.** The genuine errors were four type errors
(`experts` must be strings, `substrates` must be `Term` objects,
`reference_section_type` is not a `Reference`-level slot, `gap_kind` is
multivalued); because the generated JSON Schema matches the root with `anyOf`,
one type failure makes the validator report errors from a mismatched alternative.
Fixing only the four type errors turned the file `✓ Valid` with every quote
untouched. Had I "corrected" the six quotes, I would have corrupted correct work —
the shared-tool lesson in a new guise.

## Paralogue cross-check

`paint/ARFGEF1` and `paint/ARFGEF2` branches exist but are still at the branch point
with nothing pushed, so I could not compare resolutions. Flagging the divergence in
advance, because all three genes carry the **same** `GO:0005085` IBA from the same
node and it should be resolved **differently**:

| gene | glutamic finger | expected verdict |
|---|---|---|
| ARFGEF1 (BIG1, Q9Y6D6) | **E793** present | ACCEPT — also has its own IDA |
| ARFGEF2 (BIG2, Q9Y6D5) | **E738** present | ACCEPT — also has its own IDA |
| ARFGEF3 (BIG3, Q5TH69) | **N692** — absent | MARK_AS_OVER_ANNOTATED |

Both paralogue positions were verified against the live UniProt sequences, so this
is a checkable claim rather than an assumption about how those reviews will land.

## Retraction / erratum check

Checked each PMID relied on against its PubMed record. No retraction, erratum,
expression of concern or publisher correction found on any of them. Recording the
negative so the next reviewer knows the check ran.

## Things I deliberately did not do

- **No `GO:0005794 Golgi apparatus` row.** UniProt's `DR GO` block lists it
  (`IEA:UniProtKB-ARBA`) but it is **not in the GOA TSV**, so it is not an existing
  annotation to review. Noted, not annotated.
- **No ERα-signalling BP term.** BIG3 acts on PHB2; the ERα effect is downstream and
  BIG3–ERα binding was tested and not detected (PMID:19496786).
- **No `GO:0005739 mitochondrion` / `GO:0005764 lysosome` in `core_functions`.** Each
  rests on a single paper in one cell type (osteosarcoma lines; mouse neurons). They
  are raised as questions.
- **No proposed new GO term.** Every function I needed already exists:
  `GO:0140311`, `GO:0042308`, `GO:0008157`, `GO:0004865`, `GO:0051018`,
  `GO:1904410`. All eight candidate ids were checked against QuickGO
  `/complete` for `isObsolete` and `secondaryIds` before use; none is obsolete or
  merged.

## Row/stub reconciliation

GOA TSV: 8 data rows. `fetch-gene` stub: 8 `existing_annotations` entries. **They
match** — no collapsed `GO:0005515` partner rows and no collapsed same-term rows on
this gene, so the under-seeding defect seen elsewhere in this campaign is absent
here. Checked explicitly rather than assumed.

Final review: **14 entries = 8 GOA rows + 6 `NEW` proposals.** Verified
programmatically, not by eye, by `arfgef3_check_entities.py`, which also asserts
that every row's `supporting_entities` reproduces the GOA WITH/FROM field exactly
and that every `propagation_review` names only sources drawn from it. Hand-built
source lists have drifted on every gene in this campaign that tried it.

## One validation warning left standing, deliberately

`just validate` reports `✓ Valid (with 1 warnings)`: *"No annotations reference
available deep research files"*. Satisfying it would mean putting
`file:...ARFGEF3-deep-research-affinage.md` into a `supported_by` — i.e. quoting a
provider sentence as evidence, which is the practice this campaign specifically
forbids, and on a record that turned out to cite two papers about a different gene.
The provider's contribution is assessed at length above instead. Left standing
rather than silenced.
