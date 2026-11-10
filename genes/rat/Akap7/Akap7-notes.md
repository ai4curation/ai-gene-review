# Akap7 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Akap7` resolved Q6JP77 (AKA7G_RAT; RGD:1303071; GeneID
  361458). 39 GOA rows. No deep-research provider was available, so I wrote the
  literature synthesis myself in `Akap7-deep-research-manual.md`.
- Read PMID:21177871 in full (FMP-API-1 disruptors). It uses AKAP18delta-RIIalpha
  binding as its assay and treats AKAP18delta as the PKA anchor beside PLN
  [PMID:21177871 "FMP-API-1 displaces PKA from AKAP18δ (Fig. 2), which tethers PKA to PLN (22)"].
  No GOA row cites it. It supports the PKA-RII binding rows.
- Isoform scope matters here. Q6JP77 holds only delta and gamma. Several RGD ISO
  rows name human Q9P0M2 (gamma) in With/From, but the human experimental
  annotations behind them (PMID:11299204 IKs/KCNQ1 regulation; PMID:10613906
  apical and lateral membrane) sit on O43687 (alpha/beta). QuickGO for Q9P0M2 (checked
  2026-10-28) carries none of action potential, membrane repolarization,
  K+ transport regulation, cellular response to cAMP, or apical or lateral
  membrane. I recorded WRONG_WITH_FROM defects (RGD, PROBABLE).
- The short alpha isoform (AKAP15) is missing from Q6JP77. The rat sequence exists
  as unreviewed A0ABK0LH41 (81 aa, MGQLCC...; RefSeq XP_038937088.1), and its
  C-terminal 57 aa are identical to Q6JP77's. I recorded this as a functional_isoform with
  MISSING_ISOFORM. Human UniProt instead uses a separate Swiss-Prot entry (O43687),
  so UniProt may prefer to make a separate rat entry rather than add an isoform.
- T-tubule (PMID:14569017) is AKAP15 immunostaining. The 15 kDa protein is the alpha form,
  but PMID:23035250 found only long isoforms in mouse ventricle. The antibody may
  recognise the shared C-terminus, so I kept the row as non-core.
- Protein binding (IPI, PLN): removed under the protein-binding policy. The PLN
  interaction is captured by MODIFYing the "protein domain specific binding" IPI row
  to signaling adaptor activity (GO:0035591). AKAP18delta bridges PKA-RII and PLN
  [PMID:17901878 "We show that AKAP18delta acts as a scaffold that coordinates PKA phosphorylation of PLN and the adrenergic effect on Ca(2+) re-uptake."].
- OAK check: GO:0034237 is_a GO:0051018 is_a GO:0005515. GO:0019901 protein
  kinase binding is NOT an ancestor of GO:0051018, so MODIFYing GO:0019901 to
  GO:0034237 is a lateral correction. The mouse source showed binding to the RI regulatory subunit,
  not to a kinase catalytic subunit. GO:0016529 SR and GO:0005829 cytosol are both under
  GO:0005737 cytoplasm. GO:0016324 is_a GO:0005886.
- No NEW rows. PKC binding (PMID:22670899) could be added, but the species of the
  constructs was not clear from the text I could read; I raised it as a question.
