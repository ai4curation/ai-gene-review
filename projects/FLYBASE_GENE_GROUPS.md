---
title: "FlyBase gene groups as review sets"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [DROME]
genes: [Sgs1, Sgs3, Sgs4, Sgs5, Sgs5bis, Sgs7, Sgs8, Eig71Ee]
---

# FlyBase gene groups as review sets

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
