---
title: "FlyBase gene groups as review sets"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [DROME]
genes: [Sgs1, Sgs3, Sgs4, Sgs5, Sgs5bis, Sgs7, Sgs8, Eig71Ee]
---

# FlyBase gene groups as review sets

**Modules (update):** every FlyBase group, including the 182 metabolic and
signaling *pathway* groups, has now been triaged. 174 new fly modules
(`modules/dmel_*.yaml`) model the groups that are complexes, pathways or
functional systems; 68 existing modules already cover others; the remaining
groups are sequence families or activity classes, which are not modules. See
[Modules from gene groups](#modules-from-gene-groups).

**Bottom line:** FlyBase curates 1,836 gene groups (release FB2026_03). They
cover 8,607 *D. melanogaster* genes, and most terminal groups are small (median
4 members). That makes them ready-made, expert-bounded batches for fly reviews.
Our 199 DROME reviews touch 128 groups but cover only 10 completely, because
genes were picked one at a time rather than by group. As a pilot we looked at
the 8-member GLUE group (`FBgg0001189`, salivary glue proteins). Its GO
annotations are sparse and almost all rest on a single 1976 paper. The group and
GO agree on membership. The open questions are about the evidence, not about
who belongs.

## Why gene groups

FlyBase gene groups ([FlyBase gene groups](https://flybase.org/lists/FBgg/)) are
built by FlyBase curators from the literature and from HGNC-style family
classifications. Each group is either a family (for example *S1A serine
proteases*), a complex (for example *GATOR1 complex*), or a functional set (for
example *glue proteins*). Groups are arranged in a hierarchy, and genes are
attached only to the terminal (leaf) groups.

This differs from the PANTHER families we use in modules. A FlyBase group
records a curator's decision about which genes form one unit, including
functional sets that share no common ancestor. The GLUE group is an example: its
members are "apparently unrelated proteins" by sequence
[PMID:30696414 "The glue is a mixture of apparently unrelated proteins"].

## Landscape (computed)

All numbers below come from
[`fb_gene_groups.py`](FLYBASE_GENE_GROUPS/fb_gene_groups.py). The full output is in
[`fb_gene_groups_summary.yaml`](FLYBASE_GENE_GROUPS/fb_gene_groups_summary.yaml).

| Measure | Value |
|---|---|
| Groups (all levels) | 1,836 |
| Terminal groups with members | 1,413 |
| Member genes | 8,607 |
| Terminal groups with ≤10 members | 1,166 |
| Groups named "... COMPLEX" | 315 |
| Groups named "UNCLASSIFIED ..." | 88 |
| DROME reviews in the repo | 199 |
| ... of which in some group | 143 |
| Groups with at least one review | 128 |
| Groups fully reviewed | 10 |

The largest top-level branches are enzymes (510 terminal groups), transmembrane
transporters (133), tRNAs (45), transmembrane receptors (36) and transcription
factors (34).

The groups we already cover completely are mostly complexes and very small
families: GATOR1 (Iml1, Nprl2, Nprl3), the apoptosome (Dark, Dronc), the
mitochondrial trifunctional protein (Mtpalpha, Mtpbeta), the cGAS-like
receptors, and the IAP ubiquitin ligases. Several partly covered groups could be
finished cheaply:

- RHG proteins: 4 of 6 reviewed.
- ACAD acyl-CoA dehydrogenases: 5 of 8 reviewed.
- NF-κB: 2 of 3 reviewed.
- CSL-Notch-Mastermind complex: 2 of 3 reviewed.

## Pilot: GLUE proteins (FBgg0001189)

At the end of the third larval instar, the salivary glands make a glycoprotein
glue. The larva expectorates it at pupariation, and it fixes the puparium to the
substrate [PMID:825230 "These glands synthesize and secrete massive amounts of a
glue which attaches the pupae to the substrate during metamorphosis."]. The glue
is not essential in the laboratory, but it is strong. One study measured a mean
pull-off force of 217 mN, about 15,500 times the weight of the pupa
[PMID:32165432]. The glue genes are among the most highly expressed genes in the
salivary gland [PMID:34788814].

### Members and their GO annotations (QuickGO, computed)

| Gene | UniProt | MF `GO:0140073` bioadhesive activity | BP `GO:0007594` puparial adhesion | Other |
|---|---|---|---|---|
| Sgs1 | Q9VR49 (TrEMBL) | EXP, PMID:825230 | IEP, PMID:825230 and PMID:10511555 | — |
| Sgs3 | P02840 | EXP, PMID:825230 | IEP, PMID:825230 | — |
| Sgs4 | Q00725 | EXP, PMID:825230 | IEP, PMID:825230 | — |
| Sgs5 | P07701 | EXP, PMID:825230 | IEP, PMID:825230 | — |
| Sgs5bis | Q9VEI6 (TrEMBL) | ISS from Sgs5 | ISS, PMID:30696414 | — |
| Sgs7 | P02841 | EXP, PMID:825230 | IEP, PMID:825230 | — |
| Sgs8 | P02842 | EXP, PMID:825230 | IEP, PMID:825230 | — |
| Eig71Ee (gp150, I71-7) | Q9VUS8 (TrEMBL) | **none** | IEP, PMID:15544943; ISS from Sgs4 | hemolymph coagulation (IDA, IMP); chitin-based ECM (IDA) |

Every Sgs gene also has an extracellular-region annotation (IDA, PMID:825230).

### Observations

1. **The GO footprint matches the group exactly.** Every fly gene with
   `GO:0140073` is in the group. The only gene outside the group with
   `GO:0007594` is Swip-1, and its annotation is `acts_upstream_of` (IMP,
   PMID:36727484). That paper shows Swip-1 promotes exocytosis of glue
   granules, so Swip-1 is needed to secrete the glue but is not part of it. Under the participation rule in `CLAUDE.md`, Swip-1 should not be
   added to the group or given the MF term.

2. **Nearly all of the experimental support is one 1976 paper.** Six of the
   seven MF annotations cite Beckendorf & Kafatos (1976). That paper identified
   the glue proteins by SDS-PAGE and followed when they appear during
   development [PMID:825230 "We find six major proteins in this glue."]. It
   shows that these proteins are in the glue. It does not test whether any one
   of them is adhesive. Gene-level adhesion tests now exist: the Courtier-Orgogozo
   lab's pull-off assay [PMID:32165432; PMID:39370426] and natural variation
   across strains [PMID:34788814 "We observe a three-fold difference in glue
   adhesion between the least and the most adhesive D. melanogaster strain"].
   These are the right kind of evidence to confirm the `EXP` rows, or to replace
   them with a more specific code. Following `CLAUDE.md`, we would not remove
   these rows on the abstract alone. They are good candidates for `UNDECIDED` or
   `ACCEPT` with a note.

3. **Eig71Ee is in the group but lacks the MF term.** The gp150 mucin is a
   known glue component [PMID:15544943 "we identified gp150 as the previously
   described I71-7, an ecdysone-induced salivary glue protein"]. It also works
   in hemolymph clotting. It is the one group member without `GO:0140073`. Before
   proposing it as `NEW`, run the comparator check: is the MF withheld because
   Eig71Ee's adhesive role was never tested, or because FlyBase deliberately
   reserves `GO:0140073` for the Sgs proteins?

4. **Sgs5 and Sgs5bis may not be adhesive.** Sgs5 and Sgs5bis lack the long
   glycosylated repeats of Sgs1, Sgs3 and Sgs4 [PMID:30696414]. Population data
   show local adaptation at Sgs3, Sgs5 and Sgs5bis [PMID:34788814]. Whether
   these small proteins provide adhesion, or do something else in the glue
   such as cross-linking or setting, is a real knowledge gap. It is a good
   question for experts.

5. **Possible missing members: new-glue genes ng1–ng3.** ng1 (P23938), ng2
   (P40139) and ng3 (P40140) are named "new glue". They have only an
   extracellular-region annotation and are not in any FlyBase group. Whether
   they are true glue components is an open question, not an established gap.

## Modules from gene groups

FlyBase publishes three kinds of group in release FB2026_03: 1,836 gene groups,
109 metabolic pathway groups and 73 signaling pathway groups (2,016 groups,
counting the two that appear in two files once). We triaged all of them and
built a module wherever a group describes something that works as a unit.

### Triage

A group is a module candidate when its members act together: a protein complex,
a pathway, or a functional system such as the salivary glue. A group is not a
module when its members are only related by sequence (for example peptidase
family S1) or share a broad activity class (enzymes, transporters, receptors,
transcription factors). The curated rules are in
[`triage_rules.yaml`](FLYBASE_GENE_GROUPS/triage_rules.yaml);
[`triage_groups.py`](FLYBASE_GENE_GROUPS/triage_groups.py) applies them to every
group, letting subgroups inherit from their parents, and writes
[`group_triage.yaml`](FLYBASE_GENE_GROUPS/group_triage.yaml).

| Decision | Groups | Meaning |
|---|---|---|
| NEW_MODULE | 291 | realized by one of 174 new `dmel_` modules |
| SUBSUMED | 231 | subgroup folded into its parent's module (subunits, variants, stages) |
| EXISTING_MODULE | 110 | already covered by one of 68 existing modules (OXPHOS complexes, TCA cycle, glycolysis, GPI anchor, ...) |
| REGULATOR_SET | 34 | "positive/negative regulators of" a signaling pathway: context, not parts |
| UMBRELLA | 26 | category grouping several complexes or pathways |
| NOT_A_MODULE | 1,324 | 1,067 activity classes, 182 sequence families, 68 tRNA classes, 4 gene clusters, 3 single genes |

Several FlyBase groups often go into one module. For example the Polycomb module
covers PRC1, PRC2, PhoRC, PR-DUB, dRAF, the variant PRC1 complexes and the PcG
recruiters, and the iron-sulfur cluster module joins the FESCA metabolic pathway
group with the four Fe-S assembly complex groups.

### How the modules were built

Each module is written as a short spec in
[`module_specs/`](FLYBASE_GENE_GROUPS/module_specs/) that names participants only
by FlyBase gene or group symbol.
[`generate_modules.py`](FLYBASE_GENE_GROUPS/generate_modules.py) expands a spec
into a ModuleReview file. It maps each gene to UniProtKB from
[`group_index.yaml`](FLYBASE_GENE_GROUPS/group_index.yaml) (built by
[`build_group_index.py`](FLYBASE_GENE_GROUPS/build_group_index.py) from UniProt
and FlyBase's own mapping), and it adds the FlyBase groups as evidence. No
accession was typed by hand. Genes without a protein product (snRNAs, 7SK, roX,
RNase P and MRP RNAs, mitochondrial rRNAs) and the three Y-linked dynein heavy
chains, which lack a UniProt entry, are grounded to FlyBase gene ids.

FlyBase subgroups shape each module: subcomplexes become parts, and paralog or
testis-specific versions become variant sets (for example the testis
proteasome, ribosome and TOM complex variants). Signaling pathways model only
the core components and ligand production, in order. Every GO id was checked
against QuickGO when the spec was written, and the module validator checks the
labels again.

### Checks

- All 174 modules pass the LinkML schema and `module_validator` with no errors.
  The one routine warning is that the NCBITaxon label could not be checked
  offline.
- [`check_modules.py`](FLYBASE_GENE_GROUPS/check_modules.py) confirms that every
  member of every realized and subsumed group appears in its module, and that
  each module splits into at least two parts or variants
  ([`module_coverage.yaml`](FLYBASE_GENE_GROUPS/module_coverage.yaml)).
- A few non-member genes were added where a module could not be built without
  them. Each one is stated in the module notes: Cdc6 and dup (Cdt1) in origin
  licensing, sd in Hippo, Rheb in TORC1 nutrient sensing, y in cuticle tanning,
  Diap1 in RHG apoptosis, and ptc, which FlyBase lists only among Hedgehog
  regulators. The axonemal light chains ODA-Dnal1 and Dnali1 were moved from the
  shared dynein light-chain group into the axonemal dynein module.

### Caveats

- Status is DRAFT. No member gene has a gene review yet, so
  molecular-function assertions rest on conserved, well-established activities
  and are marked as unreviewed by the validator.
- Most modules cite no PMIDs. Their evidence is the FlyBase group and the GO
  terms. The histamine and cardiolipin modules cite checked PMIDs, and the glue
  module cites PMID:825230.
- Some FlyBase data quirks are kept as FlyBase has them and noted in the modules
  concerned. In the SMN complex, the Gem4c variant group does not list Gem4c, and
  it was placed there from the group name. In the mitochondrial ribosome,
  mRpS30 is listed in both subunits. In the RHG group, whether Prx4 acts as an
  IAP antagonist is unverified.
- Some GO gaps forced broader terms: there is no specific CC term for KPC,
  LKB1-STRAD-MO25, the HIF heterodimer, ELBA or Nxf1-Nxt1. A citrate-malate
  shuttle BP term (GO:7770108) exists in QuickGO but not yet in the validator's
  ontology snapshot.

### Reproduce

```bash
uv run python projects/FLYBASE_GENE_GROUPS/build_group_index.py -o projects/FLYBASE_GENE_GROUPS/group_index.yaml
uv run python projects/FLYBASE_GENE_GROUPS/triage_groups.py
uv run python projects/FLYBASE_GENE_GROUPS/generate_modules.py
uv run python projects/FLYBASE_GENE_GROUPS/check_modules.py
uv run python -m ai_gene_review.validation.module_validator modules/dmel_*.yaml
```

## Proposed workflow

1. Pick groups by completeness gain: partly reviewed groups first (RHG, ACAD,
   NF-κB, CNM), then small functional sets like GLUE.
2. For each group, run `fb_gene_groups.py --detail <SYMBOL>` to get the member
   list, accessions, and GO footprint before running `just fetch-gene`.
3. Review the members together, so that annotation decisions are consistent
   across the group (for example, one decision on the `EXP` bioadhesive rows
   for all six Sgs proteins).
4. Feed back to FlyBase where group membership and GO disagree (for example,
   Eig71Ee and the MF term; the status of ng1–ng3).

## Next steps

- [ ] Review the GLUE group (8 genes). This needs `just fetch-gene DROME Sgs3`
      and so on. Sgs1, Sgs5bis and Eig71Ee have TrEMBL accessions only.
- [ ] Finish the nearly complete groups. Missing members: RHG (HtrA2, Prx4),
      ACAD (Ivd, CG3902, CG9547), NF-κB (Rel), CNM (Su(H)).
- [ ] Ask FlyBase about the evidence code on the `GO:0140073` rows from
      PMID:825230.
- [ ] Decide whether FlyBase group membership should be recorded in reviews
      (for example as a `references` entry `FB:FBgg0001189`).

## Reproduce

```bash
uv run python projects/FLYBASE_GENE_GROUPS/fb_gene_groups.py \
    --release fb_2026_03 --detail GLUE \
    -o projects/FLYBASE_GENE_GROUPS/fb_gene_groups_summary.yaml
```

The FlyBase file is cached in the git-ignored `.cache/flybase/`.
