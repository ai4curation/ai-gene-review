---
title: "RHEA → GO in promiscuous enzyme families: CYP450, carboxylesterases, haloalkane dehalogenases"
species: [human]
genes: [CYP1B1, CYP2E1, CYP2J2, CYP4F2, CYP4F22, CYP11B2, CES1, CES2]
---

# RHEA → GO in promiscuous enzyme families

**Parent project:** [RHEA.md](../RHEA.md) · **Background:**
[RHEA-EC-SPECIFICITY.md](RHEA-EC-SPECIFICITY.md) ·
[RHEA-GAP-CASES.md](RHEA-GAP-CASES.md)

**Bottom line:** the project's specificity-collapse finding (G5) was measured
globally, one GO term absorbing many reactions. This page measures the *other*
half of the same problem in three families chosen for substrate promiscuity —
where one protein carries many reactions — and finds the dominant failure is not
collapse but **drop-out**: **201 of 297 (68%)** distinct reactions annotated to
reviewed human cytochrome P450s have no `rhea2go` target at all, and **192 of
those 201 carry no EC number either**, so neither `rhea2go` nor `ec2go` can route
them. The reverse gap found in the earlier pilot does not appear here: with
`is_a` closure applied, **zero** of the 98 entries across the three families is
missing a GO term that a mapped reaction would give it. The pipeline propagates
what it maps; the problem is what it never maps. 18 new SSSOM rows follow from
these families, worth **46 reviewed-entry annotations**.

## Why these three families

RHEA records a reaction per substrate, GO records an activity per protein. That
mismatch is worst where one enzyme turns over many substrates, so these families
are the stress test:

- **Human cytochrome P450s** — the extreme case: 60 reviewed entries, 556
  catalytic-activity lines, 528 of them experimental (`ECO:0000269`).
- **Human carboxylesterases (CES1–CES5A)** — the drug/lipid ester hydrolases,
  where one protein hydrolyses ester classes with unrelated biology.
- **Haloalkane dehalogenases (EC 3.8.1.5, all organisms)** — the microbial
  contrast: broad substrate range in the *chemistry*, but GO represents it with a
  single term whose definition is itself generic.

Computed live by [`rhea_family_explorer.py`](rhea_family_explorer.py) against
UniProtKB, `rhea2go`, `ec2go` and QuickGO; per-family TSVs in
[`families/`](families/). Nothing below is hardcoded.

## Results

| | Haloalkane dehalogenases | Human CES1–5 | Human CYP450s |
|---|---:|---:|---:|
| Reviewed entries | 33 | 5 | 60 |
| Catalytic-activity lines (RHEA) | 37 | 15 | 556 |
| …of them experimental (`ECO:0000269`) | 3 | 13 | 528 |
| Distinct reactions | 3 | 8 | **297** |
| …with a `rhea2go` target | 2 | 5 | 96 |
| …**with no target** | 1 | 3 | **201 (68%)** |
| …unmapped *and* with no EC number | 1 | 2 | **192** |
| Distinct GO terms those targets collapse onto | 1 | 4 | 59 |
| GOA MF rows on these entries | 93 | 72 | 1,302 |
| …contributed by `GO_REF:0000116` | 0 | 2 | 90 |
| Entries with a closure-filtered reverse gap | **0** | **0** | **0** |

Three things stand out.

**Drop-out, not collapse, is the dominant failure.** The global analysis found
GO terms absorbing up to 67 reactions each. Here the ratio is mild — 96 mapped
CYP reactions onto 59 GO terms, 1.6:1, the same as `rhea2go` overall — because
the reactions that *would* collapse are mostly not mapped in the first place.
Two thirds of the reaction space is simply invisible to GO.

**The unmapped reactions are the substrate-specific ones, and they lack an EC.**
192 of the 201 unmapped CYP reactions have no EC number, which is the structural
reason the EC bridge cannot rescue them: EC classifies at the level of
"unspecific monooxygenase" (1.14.14.1), while RHEA records
`(4Z,7Z,10Z,13Z,16Z,19Z)-docosahexaenoate → 19,20-epoxy-…`. These are exactly
the instance-level reactions the `rhea2go` curators have no GO term to point at.
The mapped 96 are the ones where a named activity already exists (steroid
11-beta-monooxygenase, sterol 14-demethylase, arachidonate 14,15-epoxygenase).

**The reverse gap is zero once closure is applied.** The pilot in
[RHEA.md](../RHEA.md) measured exact-term match and reported up to ~99% missing.
Applying the `is_a` closure this page uses, every entry in all three families
carries the mapped term or a descendant of it — 0 gaps out of 98 entries. This
is the concrete confirmation of the project's own closure caveat: the earlier
40–99% figures were altitude difference, not missing annotation. It also means
**the reverse direction is not where the remaining value is** in well-curated
families; the value is in the reactions that never enter the mapping.

### Per-entry: promiscuity concentrates the loss

| Gene | UniProt | Reactions | Mapped | Unmapped | Distinct mapped GO terms |
|------|---------|----------:|-------:|---------:|------------------------:|
| CYP4F3 | Q08477 | 46 | 11 | **35** | 9 |
| CYP3A4 | P08684 | 43 | 14 | **29** | 10 |
| CYP1A1 | P04798 | 30 | 12 | 18 | 8 |
| CYP4F2 | P78329 | 29 | 8 | 21 | 7 |
| CYP2C9 | P11712 | 28 | 15 | 13 | 9 |
| CYP27A1 | Q02318 | 15 | 1 | **14** | 1 |
| CYP4F8 | P98187 | 14 | 1 | **13** | 1 |
| CYP4F12 | Q9HCS2 | 10 | 1 | 9 | 1 |

CYP4F3 and CYP3A4 are the promiscuity extreme and lose the most reactions in
absolute terms. CYP27A1, CYP4F8 and CYP4F12 are the more interesting shape: a
dozen-plus curated reactions collapsing to a *single* mapped GO term, so the
protein's GO molecular function is one term standing in for its whole
characterised substrate range. Full table: [`families/cyp-entries.tsv`](families/cyp-entries.tsv).

### The haloalkane family: a term that is generic by design

The microbial contrast behaves differently. All 33 entries share
**RHEA:19081** (`1-haloalkane + H2O = a halide anion + a primary alcohol + H+`),
which maps to **GO:0018786 haloalkane dehalogenase activity** — and the GO
definition *is* that reaction, RHEA:19081 being its own definitional xref. The
generality is deliberate, not a collapse artifact: GO once had the
substrate-specific term GO:0018777 for LinB's tetrachlorocyclohexadiene
reaction, and **obsoleted it explicitly as "a specific substrate of"
GO:0018786**, with `replaced_by: GO:0018786`.

That obsoletion is the single most useful datum on this page, because it is GO
stating the convention that the CYP450 gap runs into: **GO does not create a
term per substrate.** It is also why the unmapped LinB reaction RHEA:11944 gets
a `broadMatch` below rather than a new-term proposal — GO has already ruled on
this exact reaction.

Note also that these 33 entries receive **zero** GOA rows from `GO_REF:0000116`,
despite all carrying a mapped reaction: they get GO:0018786 from other routes
(IBA, EC2GO). The masking result at its purest.

## New mappings (SSSOM batch 7)

18 rows added to [`rhea2go.sssom.yaml`](rhea2go.sssom.yaml), each backed by a
reviewed enzyme with an `ECO:0000269` catalytic-activity line. Scored with
[`rhea_annotation_gain.py`](rhea_annotation_gain.py): **46 new Swiss-Prot
(reviewed) annotations**, 958 across all of UniProtKB.

### Subsumed instance reactions (`skos:broadMatch`, 10 rows)

These map a substrate-specific reaction to a GO class term **whose definition
already covers it**. They request no new term — following the GO:0018777
precedent, a per-substrate child would be obsoleted again.

| RHEA | Reaction | → GO term | Reviewed enzyme | SP gain |
|------|----------|-----------|-----------------|--------:|
| RHEA:39791 | EPA (C20) ω-hydroxylation | GO:0102033 long-chain fatty acid omega-hydroxylase | CYP4F2 (P78329) | 0 |
| RHEA:40155 | DHA (C22) 22-hydroxylation | GO:0102033 | CYP4F2 (P78329) | 0 |
| RHEA:50164 | C20:3 20-hydroxylation | GO:0102033 | CYP4F2 (P78329) | 0 |
| RHEA:39787 | EPA 19-hydroxylation | GO:0120319 long-chain fatty acid omega-1 hydroxylase | CYP2E1 (P05181) | **13** |
| RHEA:50076 | C20:3 19-hydroxylation | GO:0120319 | CYP2E1 (P05181) | **11** |
| RHEA:50088 | DHA 21-hydroxylation | GO:0120319 | CYP2E1 (P05181) | 5 |
| RHEA:50096 | C14 13-hydroxylation | GO:0120319 | CYP2E1 (P05181) | 5 |
| RHEA:63376 | ULCFA ω-hydroxylation | GO:0140692 very long-chain fatty acid omega-hydroxylase | CYP4F22 (Q6NT55) | 1 |
| RHEA:50336 | C30 ω-hydroxylation | GO:0140692 | CYP4F22 (Q6NT55) | 1 |
| RHEA:11944 | tetrachlorocyclohexadiene hydrolysis | GO:0018786 haloalkane dehalogenase | LinB (D4Z2G1) | 0 |

The ω-1 rows are the ones that pay: **34 reviewed annotations**, reaching CYP2E1
and CYP1A1 orthologs across cow, pig, rabbit, macaque and sheep, plus mouse
Cyp4a12a/Cyp4a12b. The ω rows score 0 because those reactions' carriers already
have GO:0102033 — correctly-masked rows, kept because they are still true
`rhea2go` entries.

**CYP4F22 (Q6NT55) is the clean single-entry gap.** It carries two experimental
ULCFA ω-hydroxylation reactions, neither mapped; EC 1.14.14.177 has no `ec2go`
line; and its GOA molecular function is only generic P450 boilerplate
(`monooxygenase activity`, the `oxidoreductase activity, acting on paired
donors...` parent, `iron ion binding`, `heme binding`) plus `protein binding`. Nothing in GO says what this enzyme does, in an autosomal
recessive congenital ichthyosis gene whose ω-hydroxylation step is the
mechanism. GO:0140692 is defined for >22 carbons, so it covers the
ultra-long-chain case without a new term.

### New-term candidates (`sssom:NoTermFound`, 5 rows)

Reactions where QuickGO has no covering term, verified by comparing the
definitions of the nearest siblings.

| RHEA | Reaction | Proposed term | Sibling that exists | Enzyme |
|------|----------|---------------|---------------------|--------|
| RHEA:47280 | 17β-estradiol → 4-hydroxyestradiol | estrogen 4-hydroxylase activity | GO:0101021 estrogen **2**-hydroxylase | CYP1B1 (Q16678) |
| RHEA:47292 | estrone → 4-hydroxyestrone | *(same term)* | GO:0101020 estrogen 16-α-hydroxylase | CYP1B1 (Q16678) |
| RHEA:39779 | EPA 17,18-epoxidation | eicosapentaenoate epoxygenase activity | GO:0008392 **arachidonate** epoxygenase | CYP2J2 (P51589) |
| RHEA:52120 | DHA 19,20-epoxidation | docosahexaenoate epoxygenase activity | GO:0071614 **linoleate** epoxygenase | CYP2J2 (P51589) |
| RHEA:50792 | 18-hydroxycorticosterone → aldosterone | 18-hydroxycorticosterone 18-oxidase activity | GO:0047783 corticosterone 18-monooxygenase | CYP11B2 (P19099) |

Three notes on why these are gaps rather than subsumed instances:

- **Estrogen 4-hydroxylation** is the case where the substrate-generality
  argument does not apply, because GO has *already* split this activity by
  position: 2- and 16-α- terms exist, 4- does not. The 4-hydroxy catechol
  estrogens are the genotoxic branch and CYP1B1's signature reaction; the
  asymmetry looks like an omission, not a convention.
- **The epoxygenase terms** are the same shape one level up: GO splits
  epoxygenase activity by *substrate fatty acid* (arachidonate, with four
  regio-specific children; linoleate), so EPA and DHA epoxygenation are missing
  members of an existing pattern, not new per-substrate children. Seven CYPs
  carry the EPA reaction and seven the DHA reaction.
- **Aldosterone synthase.** CYP11B2's defining final step has no GO term at all.
  GO:0047783 is defined strictly as the *preceding* step (corticosterone →
  18-hydroxycorticosterone), and no aldosterone-synthase term exists in QuickGO.
  This is a named clinical enzyme — corticosterone methyloxidase deficiency —
  whose terminal reaction GO cannot express.

### Substrate-class gaps in CES (`skos:broadMatch` + new term requested, 3 rows)

| RHEA | Reaction | Current best | Proposed term | SP gain |
|------|----------|--------------|---------------|--------:|
| RHEA:27506 | cocaine → ecgonine methyl ester + benzoate | GO:0106435 carboxylesterase | cocaine esterase activity | 1 |
| RHEA:48296 | PGE2 1-glyceryl ester hydrolysis | GO:0106435 | prostaglandin glyceryl ester hydrolase activity | 6 |
| RHEA:48300 | PGF2α 1-glyceryl ester hydrolysis | GO:0106435 | *(same term)* | 3 |

Unlike the CYP fatty-acid rows, these are not "one more substrate in a class the
term already names" — they are chemically distinct hydrolyses with their own
biology (the prostaglandin glyceryl esters are the COX-2 products of
2-arachidonoylglycerol, so their hydrolysis sits in endocannabinoid signalling),
and EC 3.1.1.84 has neither an `ec2go` line nor a GO term. The gain reaches
MGLL, LYPLA2 and their rodent orthologs, plus the bacterial cocaine esterase
CocE.

## Follow-up

The CYP450 half of this page is taken further, family-wide, in the
[CYTOCHROME_P450](../CYTOCHROME_P450.md) project: tier classification of all 60
reviewed human CYPs, the evidence behind their activity terms, and the
**cascade-step** gap class this page did not separate out — intermediate steps of
multi-step P450 transformations that GO holds for one substrate and not for
another on the same protein (SSSOM batch 8).

## What this adds to the project's conclusions

1. **Revise the emphasis on the reverse direction.** [RHEA.md](../RHEA.md)
   currently calls the reverse gap "the high-value half". In these three
   families it is empty: 0 closure-filtered gaps across 98 entries. The value
   is in gap class **G4** (no `rhea2go` line), which this page measures at 68%
   of the reaction space for human CYPs — far above the 36% global figure.
2. **The EC bridge fails exactly where promiscuity is highest.** 192 of 201
   unmapped CYP reactions have no EC, because EC stops at "unspecific
   monooxygenase" where RHEA continues to the substrate. So for this family EC
   is not the masking competitor of the global analysis — it is absent.
3. **Distinguish subsumed instances from real term gaps before proposing.** The
   GO:0018777 obsoletion gives a citable rule: a reaction differing from an
   existing term only by substrate identity, within the class that term names,
   gets a mapping and not a new term. Applying it here turned what looked like
   201 new-term candidates into 10 subsumable rows, 5 genuine proposals, and a
   large residue that is neither — instance reactions awaiting a class term that
   may never be worth creating.
4. **Single-entry gaps are still worth finding.** CYP4F22 scores 1 on
   propagation gain and is nonetheless the most consequential row here: a
   disease gene whose characterised activity GO does not state.

## Reproduce

```bash
cd projects/RHEA
uv run python rhea_family_explorer.py --out families             # all three families
uv run python rhea_family_explorer.py --family cyp --out families # one family
just validate-rhea-mappings                                       # validate the SSSOM set
```

Outputs per family: `<family>-summary.json`, `-entries.tsv` (per protein),
`-reactions.tsv` (per reaction, with the `rhea2go`/`ec2go` comparison),
`-entry-reactions.tsv` (the raw protein × reaction join), `-closure-gaps.tsv`
(empty for all three).
