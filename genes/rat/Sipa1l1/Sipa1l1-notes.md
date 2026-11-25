# Sipa1l1 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Sipa1l1` (second attempt; first timed out on UniProt) gave O35412,
  52 GOA rows. All 9 GOA PMIDs cached; added PMID:18094260 (EphA4-SPAR, full text) and
  PMID:35121636 (mouse KO, abstract only).
- No deep-research keys; literature synthesis is in `Sipa1l1-deep-research-manual.md`.
- Full text read: PMID:18723513, PMID:19900557, PMID:21382555, PMID:18094260.
  Abstract only: PMID:11502259, PMID:12059963, PMID:15703396, PMID:15823548, PMID:16522626,
  PMID:18498738, PMID:35121636.

## Key decisions

- MF: GTPase activator activity (GO:0005096) accepted on all three rows; GO:0046582 Rap GTPase
  activator activity is obsolete, so no more specific MF exists.
- GO:0090630 "activation of GTPase activity" is defined as initiating activity "through the
  replacement of GDP by GTP" (GEF mechanism) [OLS GO:0090630 definition]; SPAR is a GAP, so
  this row is MODIFIED to GO:0043547 positive regulation of GTPase activity. The two
  "regulation of GTPase activity" rows are refined to the same term.
- InterPro2GO "regulation of small GTPase mediated signal transduction" refined to the
  negative-regulation child GO:0051058 (a Rap GAP inactivates Rap) [PMID:18094260].
- Kinase binding (Plk2, CDK5), ubiquitin ligase binding (beta-TRCP) and protein-containing
  complex binding (SCF-Plk2): real interactions in which SPAR is the substrate. Kept as
  non-core.
- Bare protein binding rows removed under the protein-binding policy (interactions with
  DLG4, LZTS3, PDLIM5, PDLIM7 are real; term is uninformative).
- PSD location kept non-core: the 2022 mouse SRM study [PMID:35121636] reports SIPA1L1 not in
  the PSD. Dendritic spine accepted.
- PMID:15823548 protein-containing complex: abstract names SPA-1, cannot verify Sipa1l1;
  UNDECIDED (not REMOVE, per the curator-deference rule).
- No NEW terms proposed. Homeostatic synaptic plasticity evidence (degradation of SPAR by
  Plk2) shows SPAR is the regulated target; did not propose a homeostatic-plasticity process
  term.
