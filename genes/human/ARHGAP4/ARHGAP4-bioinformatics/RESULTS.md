# ARHGAP4 bioinformatics — results

Five rerunnable analyses supporting `genes/human/ARHGAP4/ARHGAP4-ai-review.yaml`. Each
derives the repo root rather than hardcoding a worktree path, and each takes
`--self-test`, which breaks its input or its anchor on purpose and requires every guard
to fire, with negative controls that must stay silent.

```bash
uv run --with biopython --with requests python arginine_finger.py    # -> arginine_finger.json
uv run --with requests python check_gap_terms.py                     # -> gap_terms.json
uv run --with requests python reference_coverage.py                  # -> reference_coverage.json
uv run --with requests python resolve_entities.py                    # -> entities.json
uv run --with requests python comparator_terms.py                    # -> comparator_terms.json
```

All five query live services (UniProt, RCSB, QuickGO, OLS4, the GO API, the Alliance),
so their JSON outputs are committed as the record of what those services returned on the
run that produced the numbers quoted below.

---

## 1. `reference_coverage.py` — the defect is coverage, not over-annotation

The headline result. QuickGO was queried **by reference** rather than by gene, for 19
primary papers about ARHGAP4. The query is deliberately species-blind, because two of the
three mechanistic papers used the rat protein and the human `GO_REF:0000107` rows are
Ensembl-Compara projections from rat.

**16 of 19 primary papers produced no GO annotation on ARHGAP4 in any species.**

| PMID | rows on ARHGAP4 (any species) |
|---|---|
| 8570618 Tribioli 1996 | human: `GO:0005096`, `GO:0007010`, `GO:0007266`, `GO:0005737`, all TAS |
| 12414125 Foletta 2002 | **rat**: `GO:0005096` **IDA**, `GO:0007399` IEP, `GO:0035023` NAS, `GO:0005874` IDA |
| 17804252 Vogt 2007 | **rat**: `GO:0010764` IMP, `GO:0030517` IMP, `GO:0030426` IDA |
| 16417406 Weiner 2006 (screen) | human: `GO:0005515` IPI |
| the other 16 | none |

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

---

## What none of these can check

None of these scripts validates a quote **against the claim it is attached to**. They
confirm that a term is merged, that a residue is an arginine, that a reference produced
*n* annotations — all mechanical. Whether a `supporting_text` actually supports the
sentence above it was checked by re-reading each `summary` next to its quote, and that
remains the weakest link. Nor can they resolve the two substantive unknowns: which
Rho-family GTPase ARHGAP4 acts on in a cell, and why losing the gene costs neither mouse
nor human anything measurable.
