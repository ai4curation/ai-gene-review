# BenR review and published iModulon membership

The source-checked PRECISE321 BenR module (ID 27) has **10 published members**.
Its threshold is 0.12821891758582343; membership comes from the published gene table,
with measured weights checked independently against the named matrix column.

| Locus | Gene | Measured weight |
|---|---|---:|
| PP_3161 | benA | 0.2257799459062349 |
| PP_3162 | benB | 0.2592000505258936 |
| PP_3163 | benC | 0.2422193912594311 |
| PP_3164 | benD | 0.2286050183364702 |
| PP_3165 | benK | 0.170872666802498 |
| PP_3166 | catA-II | 0.2307625819879666 |
| PP_3167 | benE-II | 0.1445424017249806 |
| PP_3713 | catA-I | 0.1459729536267839 |
| PP_3714 | catC | 0.1572874230465502 |
| PP_3715 | catB | 0.1389278906473728 |

PP_3765 (mvaT), PP_3168 (nicP-I) and PP_3792 are **not members**. The previous
13-gene table used an arbitrary 0.05 cutoff; its membership-based conclusions and
proposed targets are withdrawn. The previous version remains in Git history.

Membership records coexpression, not direct regulation. The ben and cat genes can
co-vary across conditions without all being direct BenR targets. Neither module
membership nor a putative benF/nicP equivalence supplies a promoter-binding assay.
The current [regulatory evidence](BenR-regulatory-evidence.yaml) retains one benA
promoter assertion with physical directness unresolved and explicit strain limits.

The source-reported precision/recall values compare against the authors' reference
regulon; they are not validation metrics for this gene review. BenR's own membership
in a module is also separate from its assignment as a module regulator.

See the [reproducible source summary](../../../projects/P_PUTIDA/tf_census/imodulon/reports/Q88I42.md)
and [calibration assessment](../../../projects/P_PUTIDA/tf_census/calibration-review.md).
Source revision: `01af982cb604eef842df4209abe39b033d9067d5`;
publication: https://doi.org/10.1016/j.ymben.2022.04.004.
