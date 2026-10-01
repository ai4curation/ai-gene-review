# CMC2 curation notes

## 2026-10-01 current-GOA and IBA re-review

Reviewed *Saccharomyces cerevisiae* **CMC2/YBL059C-A** after a current GOA/UniProt
refresh. Cmc2 is a small twin Cx9C protein imported into the mitochondrial
intermembrane space by the MIA40/ERV1 disulfide relay; it is peripherally
associated with the inner membrane and is required for cytochrome c oxidase
biogenesis. The key target-specific paper remains Horn et al. 2010, which reports
that Cmc2 localizes to the mitochondrial inner membrane facing the IMS and that
COX activity and cellular respiration are undetectable in `cmc2` mutants
[PMID:20220131 "In the absence of Cmc2, cytochrome c oxidase activity measured
spectrophotometrically and cellular respiration measured polarographically are
undetectable"].

### Source refresh

- The old review already covered all **12** live GOA rows; no new rows were seeded
  and no historical rows needed `retired: true`.
- `just fetch-gene yeast CMC2 --force` backfilled exact `supporting_entities` on
  the live PAINT mitochondrial row and the two UniProt-SubCell rows.
- The review had no `PENDING` rows, no `GO:0005515 protein binding` rows, and no
  unsupported proposed replacements. The direct edits were setting the status to
  `COMPLETE`, adding a structured `propagation_review` for the IBA row, and
  removing the old C-terminal GFP nuclear/cytoplasmic calls as likely
  import-disrupted IMS-fusion artifacts.

### IBA / PAINT review

The sole IBA row is `is_active_in GO:0005739 mitochondrion`, propagated from
`PANTHER:PTN001884832`. Because UniProt no longer exposes a PANTHER cross-reference
for Q3E7A4 even though the live IBA row names a PTN node, I fetched the hidden
family from InterPro:

- `PTHR22977` = COX ASSEMBLY MITOCHONDRIAL PROTEIN.
- Q3E7A4/yeast Cmc2 and Q9NRP2/human CMC2 are in subfamily `PTHR22977:SF1`.
- P36064/yeast Cmc1 and Q7Z7K0/human CMC1 are in sister subfamily
  `PTHR22977:SF5`.
- `PTHR22977-paint.tsv` contains one positive IBD row:
  `PTN001884832 -> GO:0005739`, seeded by yeast Cmc1, yeast Cmc2, human CMC1 and
  human CMC2.

That PAINT placement is sound. The term is generic relative to the direct
intermembrane-space and inner-membrane evidence, so the action remains
`KEEP_AS_NON_CORE` with `root_cause: NO_FAILURE_NON_CORE`; no target-specific loss
or paralog-transfer issue was found.

### Literature checked

Cached publications were sufficient for all existing rows:

- PMID:19703468: systematic twin Cx9C survey that named Cmc2 and established
  Mia40-dependent import and a respiratory-chain phenotype.
- PMID:20220131: focused Cmc2 study showing inner-membrane/IMS localization,
  Cmc1 interaction, non-redundancy with Cmc1, loss of COX activity/respiration in
  `cmc2` mutants, and modulation of mitochondrial Sod1 activity.
- PMID:22984289: Bax-release IMS proteomics validating Cmc2 as an intermembrane
  space protein and explicitly warning that C-terminal GFP fusions can mistarget
  IMS proteins into cytosol/nucleus because the IMS import route lacks a strong
  ATP- and membrane-potential-driven unfolding force.
- PMIDs 14562095 and 24769239: high-throughput localization/proteomics rows.

A 2024-2026 literature search found broader COX-assembly and yeast respiratory-chain
papers but no new CMC2-specific evidence that supersedes the cached primary work.
PMID:38612624 is a useful 2024 yeast/COX-deficiency review, but it does not change
the CMC2 calls here.

### Remaining uncertainty

The molecular activity of Cmc2 is still unknown. Horn et al. proposed that Cmc1/Cmc2
may regulate copper distribution between cytochrome c oxidase and mitochondrial Sod1,
but the same paper explicitly states that it remains unclear whether the proteins
participate in copper homeostasis, redox homeostasis, both, or another COX-biogenesis
mechanism. Keeping the `GO:0003674 molecular_function` ND row is therefore preferable
to fabricating a copper-binding or metallochaperone activity.
