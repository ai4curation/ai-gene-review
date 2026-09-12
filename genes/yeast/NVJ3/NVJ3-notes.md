# NVJ3 (YDR179W-A / Q03983) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* NVJ3
("Nucleus-Vacuole Junction 3"). Understudied / dark gene. Provenance is recorded inline as
`[PMID:xxxx "verbatim quote"]`.

## Identity

- SGD standard name **NVJ3**; systematic name **YDR179W-A**; UniProt **Q03983** (YD179_YEAST),
  463 aa. Confirmed via SGD locus API: `systematic: YDR179W-A | standard: NVJ3`, and via UniProt
  cross-references (`SGD; S000002587; YDR179W-A`).
- SGD one-line description: "Protein involved in lipid metabolism; localizes to endoplasmic
  reticulum-vacuole membrane contact sites at the nucleus-vacuole junction in an Mdm1p-dependent
  manner; contains a lipid-binding PXA domain."
- `just fetch-gene yeast NVJ3` failed because UniProt does not carry `NVJ3` as a gene name
  (gene name = ORF `YDR179W-A`); fetched with `--uniprot-id Q03983`.

## Domain architecture / bioinformatics (done inline)

- InterPro/Pfam for Q03983 returns ONLY the **PXA domain** (Pfam PF02194 / IPR003114
  "Phox-associated domain"). No PX (PF00787) domain, no annotated transmembrane region.
  (Queried InterPro API `entry/all/protein/uniprot/Q03983`.)
- UniProt feature table lists only `CHAIN 1..463` — no TRANSMEM, no SIGNAL. Consistent with a
  soluble, peripherally-recruited protein rather than an integral membrane protein.
- Inline Kyte–Doolittle hydropathy scan (window 19) of the full sequence: max mean hydropathy
  = **1.14** (pos ~422), below the ~1.6 threshold typically indicative of a candidate TM helix.
  Supports the "predicted soluble" characterization (no strong TM segment).
- This matters for the annotations: **the only domain Nvj3 shares with its paralog Mdm1 is the
  PXA domain.** The PI3P-binding activity that anchors Mdm1 to the vacuole is a property of
  Mdm1's separate **PX** domain, which Nvj3 does NOT possess.
  [PMID:26283797 "In yeast, the PXA domain is the only domain shared between Mdm1 and Nvj3 and is unique to these proteins"]
  [PMID:26283797 "its C-terminal PX domain, which binds PI3P with high affinity"]

## What is KNOWN

### Localization (well supported, experimental)
- Nvj3 was discovered as a novel paralog of Mdm1 and named in PMID:26283797.
  [PMID:26283797 "We also characterize a novel Mdm1 paralogue Ydr179w-a, which we name Nvj3, and show that both it and Mdm1 localize specifically to NVJs in an Nvj1-independent manner."]
- GFP-tagged Nvj3 localizes to the nucleus–vacuole junction (NVJ) / ER–vacuole membrane contact
  site (basis of GO:0071561 IDA and GO:0098853 IDA).
  [PMID:26283797 "To determine its localization, we GFP tagged the YDR179W-A locus and observed that Ydr179w-a–GFP also localized to NVJs"]
  [PMID:26283797 "A tBFP2-tagged Ydr179w-a colocalized with Mdm1-GFP, confirming its NVJ localization, and thus we name it Nvj3"]
- NVJ / ER–vacuole localization is **independent of the canonical tether Nvj1**.
  [PMID:26283797 "Remarkably, both Mdm1 and Nvj3 retained ER–vacuole MCS localizations in nvj1Δ yeast but were no longer restricted to NVJ patches."]
  [PMID:26283797 "In some cells, Nvj3 was clearly enriched at the tips of ER tubules making contact with the vacuole, confirming ER–vacuole tethering does not require Nvj1"]

### Recruitment by Mdm1 (well supported)
- Nvj3 is predicted soluble and requires Mdm1 for NVJ localization; in mdm1Δ it goes cytosolic.
  [PMID:26283797 "Because Nvj3 is predicted to be soluble, we hypothesized that it required Mdm1 for its NVJ localization."]
  [PMID:26283797 "Consistent with this, Nvj3-GFP redistributed into the cytoplasm in mdm1Δ cells, suggesting Nvj3 interacts directly with Mdm1 at NVJs"]
- Mdm1 co-purifies with Nvj3.
  [PMID:29146766 "we show that Mdm1 co‐purifies with Faa1 and Fas1/2 in addition to Mdm1 paralog Nvj3"]
- SGD interaction data: physical partners include MDM1 (paralog/recruiter) and SEC61 (ER
  translocon); other partners are high-throughput (NAM7, MPT5, DHH1, CCR4, PUP1, HSC82).

### Lipid / neutral-lipid metabolism (biological process; experimental IMP)
- Deleting MDM1, NVJ3, or both causes lipid-droplet accumulation and ~2-fold TAG increase;
  suppressed by Faa1 loss (basis of GO:0006629 IMP, PMID:29146766).
  [PMID:29146766 "deleting MDM1, NVJ3, or both causes accumulation of LDs in yeast, and a ~2‐fold increase in TAG, implying a functional role for Mdm1 and Nvj3 in NVJ‐associated LD dynamics"]
  [PMID:29146766 "Deletion of Faa1 in addition to Mdm1 and Nvj3 suppresses the increase in TAG we see in the mdm1 Δ nvj3 Δ double knockout"]
  [PMID:29146766 "our results are consistent with a role for Mdm1/Nvj3 in LD production following fatty acyl‐CoA activation"]
- Nvj3 is NOT required for piecemeal microautophagy of the nucleus (PMN).
  [PMID:26283797 "Nvj1-mCherry–positive PMN vesicles formed even in the absence of Mdm1 and Nvj3, suggesting they are not required for yeast PMN"]

### Newer (preprint, NOT peer-reviewed — treat cautiously)
- PMID:41542480 (bioRxiv 2026): "Nvj3 regulates Dga1-mediated triacylglycerol synthesis and lipid
  droplet formation at ER contact sites." Abstract: Nvj3 induced by glucose depletion; recruited
  to LD-associated ER domains; required to couple Dga1-dependent TAG synthesis to LD formation;
  nvj3Δ → TAG accumulates but is inefficiently packaged into LDs, with altered phospholipid
  remodeling and DAG mislocalization. This corroborates the lipid role and adds a DAG/Dga1 axis,
  but assigns no direct biochemical (molecular-function) activity to Nvj3. Preprint → do not use
  as sole basis for a positive core molecular-function claim; used only to frame knowledge gaps.

## What is NOT known (the primary deliverable — knowledge gaps)

1. **Molecular function is undetermined (MF-dark).** No direct biochemical activity has been
   demonstrated for Nvj3. It carries only a PXA domain (function of the PXA domain itself is
   uncharacterized: [PMID:26283797 "All Mdm1 homologues encode an uncharacterized PXA domain."]).
   Whether Nvj3 transfers lipids, binds/senses a specific lipid, or acts purely as a
   scaffold/adaptor recruited by Mdm1 is unknown.
2. **The PI3P-binding (GO:0032266) annotation is ISS, transferred from Mdm1** (with/from
   SGD:S000004572 = MDM1). But the PI3P-binding activity in Mdm1 resides in its **PX** domain,
   which Nvj3 lacks; Nvj3 shares only the PXA domain. So the sequence basis for transferring
   PI3P binding to Nvj3 is weak. This is flagged as a likely over-annotation / MODIFY-to-gap.
3. **Is Nvj3 itself a tether, or a passenger?** Nvj3 is recruited to ER–vacuole MCSs by Mdm1
   and is predicted soluble; independent tethering activity of Nvj3 alone has not been shown.
4. **Loss-of-function phenotype is subtle.** Single nvj3Δ has mild neutral-lipid phenotypes;
   there is no reported growth phenotype and 0 hits in 10 CRISPR screens (UniProt DR BioGRID-ORCS),
   consistent with redundancy with Mdm1 and a modulatory role.

## Annotation-by-annotation plan

| GO term | Evidence | Ref | Action | Rationale |
|---|---|---|---|---|
| GO:0071561 nucleus-vacuole junction (CC) | IDA | PMID:26283797 | ACCEPT | GFP colocalization at NVJ; core localization |
| GO:0098853 ER-vacuole membrane contact site (CC) | IDA | PMID:26283797 | ACCEPT | direct imaging; ER-vacuole MCS |
| GO:0006629 lipid metabolic process (BP) | IMP | PMID:29146766 | ACCEPT (core, but consider specificity) | nvj3Δ neutral-lipid/TAG phenotype |
| GO:0032266 PI3P binding (MF) | ISS | PMID:26283797 (from MDM1) | MARK_AS_OVER_ANNOTATED | activity is Mdm1-PX-domain-specific; Nvj3 lacks PX; only PXA is shared |

## core_functions plan
- CC/localization: NVJ / ER-vacuole MCS resident, Mdm1-recruited (supported).
- BP: participates in neutral-lipid (TAG/LD) metabolism at ER-vacuole contacts (IMP-supported).
- MF: NO confident positive MF term (dark). Do not assert PI3P binding or lipid transfer.

## Deep research
- falcon deep-research launched via `just deep-research-falcon yeast NVJ3 --fallback perplexity-lite`.
- Independently grounded review in UniProt + GOA + cached primary literature (PMID:26283797,
  PMID:29146766) + PubMed metadata for the 2026 preprint (PMID:41542480). No fabrication.
