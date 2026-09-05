# sgo1 (Shugoshin-1) — S. pombe — Review Notes

UniProt: Q9P7A0 (SGO1_SCHPO). PomBase: SPBP35G2.03c. 319 aa. Pfam Shugoshin_N + Shugoshin_C; coiled-coil 33-62.

## Summary of function
Sgo1 is the fission-yeast meiosis-specific shugoshin that protects centromeric sister-chromatid cohesion during meiosis I. It localizes to the centromere/pericentromere (kinetochore + pericentric heterochromatin), recruits the PP2A-B56 phosphatase, and thereby keeps the cohesin subunit Rec8 dephosphorylated and protected from separase cleavage at anaphase I, so centromeric cohesion persists until meiosis II. Its paralog Sgo2 acts mainly in mitosis/tension sensing.

## Key evidence
- Identification as protector of centromeric cohesin Rec8 in fission yeast meiosis; Sgo2 paralog required for mitotic segregation; Bub1 required for centromeric localization of Sgo1/Sgo2 [PMID:14730319 "Here we identify Sgo1 (shugoshin), a protector of the centromeric cohesin Rec8 in fission yeast"; "Localization of Sgo1 and Sgo2 at centromeres requires the kinase Bub1"].

- sgo1 and sgo2 are Mei-S332 homologs; sgo1 required for retention of sister centromere cohesion between meiotic divisions; Rec8 retained at centromeres after meiosis I is reduced in Δsgo1 not Δsgo2; Sgo1 regulates Rec8 cleavage by separase; both localize to centromere regions [PMID:14972679 "The amount of meiotic cohesin's Rec8 subunit retained at centromeres after meiosis I is reduced in Deltasgo1, but not in Deltasgo2, cells, and Sgo1 appears to regulate cleavage of Rec8 by separase. Both Sgo1 and Sgo2 proteins localize to centromere regions"].

- Sgo1 recruits PP2A to centromeres; inactivation causes loss of centromeric cohesin at anaphase I; PP2A blocks Rec8 phosphorylation/cleavage [PMID:16541024 "Here we show in both fission and budding yeast that Sgo1 recruits to centromeres a specific form of protein phosphatase 2A (PP2A). Its inactivation causes loss of centromeric cohesin at anaphase I"].

- Meiotic shugoshin of fission yeast associates with PP2A; both collaboratively protect Rec8-containing cohesin at centromeres; mechanism is dephosphorylation of cohesin [PMID:16541025 "Meiotic shugoshin of fission yeast also associates with PP2A, with both proteins collaboratively protecting Rec8-containing cohesin at centromeres"]. The IPI interactor UniProtKB:Q10428 is par1 (PP2A B56 regulatory subunit). PomBase:SPCC188.02 is also par1.

- Sgo1 is a meiosis-specific centromere protein loaded onto the centromere at times similar to the NMS (Ndc80-Mis12-Spc7) group; Sgo1 protects Rec8 at the centromere to maintain cohesion between sister centromeres until meiosis II [PMID:17035632 "another meiosis-specific protein, Sgo1, is loaded at times similar to the NMS group"; "Sgo1 protects Rec8 at the centromere to maintain cohesion between sister centromeres until meiosis II"].

- Heterochromatin protein Swi6 (HP1) binds directly to meiosis-specific Sgo1; Sgo1(V242E) abolishes Swi6 interaction and impairs centromeric localization/function; forced centromeric Sgo1 restores meiotic segregation in swi6 cells [PMID:18716626 "the heterochromatin protein Swi6 associates directly with meiosis-specific shugoshin Sgo1, a protector of cohesin at centromeres. A point mutation of Sgo1 (V242E), which abolishes the interaction with Swi6, impairs the centromeric localization and function of Sgo1"]. swi6 = UniProtKB:P40381. This is the basis for the swi6 IPI.

- Bub1 phosphorylates histone H2A-S121; this mark localizes shugoshin proteins to centromeres; loss phenocopies localization defect; tethering shugoshin restores CIN defects [PMID:19965387 "The h2a-SA mutant... phenocopies the bub1 kinase-dead mutant (bub1-KD) in losing the centromeric localization of shugoshin proteins... Bub1 kinase creates a mark for shugoshin localization and the correct partitioning of chromosomes"]. (Paper covers both Sgo1 and Sgo2; PomBase assigned the sgo1 cohesion-protection, pericentric heterochromatin, and meiotic spindle localization annotations.)

- Survivin/Borealin phosphorylation promotes binding with shugoshin, "a conserved centromeric adaptor of the CPC"; relevant to mitotic bi-orientation [PMID:20739936 "Survivin phosphorylation promotes direct binding with shugoshin, which we now define as a conserved centromeric adaptor of the CPC"]. IPI interactor Q10428 (par1) again. The mitotic sister chromatid biorientation IMP was assigned to sgo1 by PomBase from this paper.
  NOTE/CAUTION: In S. pombe the dominant mitotic CPC/tension-sensing shugoshin is Sgo2; this paper discusses "shugoshin" generically. The IMP mitotic biorientation annotation to sgo1 should be flagged as uncertain (KEEP_AS_NON_CORE / note), not removed — the curator read the full text.

- Meikin (Moa1)-Plo1 recruits Bub1 to kinetochores in meiosis I; meiotic Bub1 ensures robust Sgo1 localization and cohesion protection cooperating with Swi6 which binds/stabilizes Sgo1; Sgo1 localizes to kinetochore [PMID:28497540 "The meiotic Bub1 pool ensures robust Sgo1 (shugoshin) localization and cohesion protection at centromeres by cooperating with heterochromatin protein Swi6, which binds and stabilizes Sgo1"].

- Sgo1 declines/degraded after meiosis I (APC ubiquitination) [PMID:14972679 "The abundance of Sgo1 protein normally declines after the first meiotic division"; UniProt: "Ubiquitinated by the anaphase promoting complex (APC) at the onset of anaphase"].

## Core function synthesis
1. Molecular adaptor/PP2A recruitment: Sgo1 acts as a chromatin-protein adaptor (GO:0140463) that recruits PP2A-B56 (Par1/Par2) to the meiotic centromere and bridges to heterochromatin (Swi6). Avoid bare "protein binding".
2. BP: meiotic centromeric cohesion protection in anaphase I (GO:1990813); meiotic sister chromatid segregation/cohesion; meiotic chromosome segregation.
3. CC: chromosome centromeric region, condensed chromosome centromeric region, inner kinetochore/kinetochore, pericentric heterochromatin, nucleus.

## Annotation-by-annotation considerations
- protein binding (GO:0005515) x several: par1 (Q10428 / SPCC188.02) and swi6 (P40381) interactions. Per curation guidance avoid bare "protein binding" as a core MF — MODIFY toward chromatin-protein adaptor activity (GO:0140463) which captures the informative adaptor function (already present as EXP annotation). Mark these IPIs as non-core / over-general.
- chromatin organization (GO:0006325) IEA from GO:0140463 logical inference — generic; KEEP_AS_NON_CORE.
- meiotic chromosome segregation (GO:0045132) IEA InterPro — broad but correct parent; KEEP_AS_NON_CORE (more specific terms are the core).
- mitotic sister chromatid biorientation (GO:1990758) IMP PMID:20739936 — Sgo2 is the principal mitotic player; defer to curator (full text) but mark non-core/uncertain.
- spindle attachment to meiosis I kinetochore (GO:0051455) IMP PMID:14972679 — mono-orientation in meiosis I; supported (sgo1 mutants affect MI kinetochore orientation). Accept.
- meiotic spindle (GO:0072687) IDA PMID:19965387 — localization; defer/accept.
- nuclear envelope (GO:0005635) HDA PMID:16823372 — high-throughput; keep non-core.

## Reassessment — 2026-09-05

The annotation-reviewer consultation rechecked the primary sources and live
QuickGO records. These corrections supersede the earlier statements where they
conflict:

- Sgo1-associated fission-yeast PP2A is the Paa1–Par1–Ppa2 combination. The
  primary paper distinguishes the severe segregation phenotype of par1 deletion
  from the substantially faithful segregation of par2 deletion; the description,
  core function and proposed imaging experiment should not assert interchangeable
  Par1/Par2 complexes [PMID:16541024, p. 54, full primary paper:
  https://publications.mpi-cbg.de/Riedel_2006_1292.pdf].
- GO:0140463 chromatin-protein adaptor activity is explicitly `part_of`
  GO:0006325 chromatin organization. The latter is broader than chromatin
  remodeling, so this automated process inference is accepted. The earlier
  rejection rested on an incorrectly narrow reading of chromatin organization
  [QuickGO GO:0140463 relationships, checked 2026-09-05].
- The PMID:20739936 IPI record is assigned by IntAct with WITH/FROM
  UniProtKB:Q10428 (Par1). It is not a Survivin interaction record. Independent
  PP2A evidence supports retaining this as a non-core interaction, while the
  original paper-specific assay remains to be traced; the broad abstract does
  not justify a CPC-adaptor claim for this row [QuickGO annotations for
  UniProtKB:Q9P7A0, checked 2026-09-05; PMID:16541024].
- The current record of APC-mediated ubiquitination in UniProt is an inference
  (ECO:0000305). Declining abundance after meiosis I and proven APC causality
  should not be conflated, so the standalone description now states only the
  abundance change [UniProt:Q9P7A0; PMID:14972679].

The mitotic biorientation assertion from PMID:20739936 remains under focused
investigation. Its full main text was not recovered in the evidence audit. The
open supplement contains Sgo2 experiments and human SGO1/SGO2 experiments;
this is not grounds for alleging that PomBase misattributed the Sgo1 annotation.
An OpenScientist request was launched through `just gene-hypothesis-research`
to recover exact species, genotype, expression regime and assay provenance.
No outcome from that request is assumed here.

The nuclear-envelope HDA (PMID:16823372) and meiotic-spindle IDA
(PMID:19965387) are now UNDECIDED because the accessible abstracts do not expose
the gene-specific observations. This does not dispute the experimental records;
absence of a known compartment-specific function is not evidence that observed
localization is wrong. The earlier nuclear-envelope over-annotation claim and
assertion of a secondary spindle pool were unsupported.

The existing UNDECIDED review for GO:0051455 (PMID:14972679) remains appropriate
pending its primary attachment assay. This supersedes the earlier notes entry
saying ACCEPT. The term concerns physical spindle attachment to a meiosis-I
kinetochore; it is not simply synonymous with cohesion protection or with
kinetochore orientation [QuickGO GO:0051455 definition, checked 2026-09-05].
