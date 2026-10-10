# SERINC2 curation notes

## 2026-07-25 evidence log

- Ran `just fetch-gene human SERINC2`: nine GOA rows were seeded one-to-one in the review.
- Ran PMID caching: both GOA publications were present locally.
- Attempted Falcon deep research with Perplexity-lite fallback. Falcon failed with HTTP 402 and the fallback failed with HTTP 401; no provider-named failed output was retained. Manual research is recorded in `SERINC2-deep-research-manual.md`.
- Read reviewed UniProtKB Q96SA4, all nine GOA rows, PMID:16120614, PMID:19056867, the full text of PMID:37474505, the full text of PMID:38785977, and the NHLBI urinary-exosome database row linked from PMID:19056867.

## Annotation decisions

- Core MF/location: GO:0017128 phospholipid scramblase activity at GO:0005886 plasma membrane.
- The two generic GO:0016020 membrane rows are MODIFY to plasma membrane.
- Both plasma-membrane rows and the GO:0017128 phospholipid scramblase activity row are ACCEPT.
- GO:0017121 plasma membrane phospholipid scrambling is MARK_AS_OVER_ANNOTATED. Purified SERINC2 flips NBD-PC in proteoliposomes, and UniProt extrapolates broader PS/PE/PC catalytic activities, but the HIV-1 virion studies specifically report no SERINC2-driven PS exposure/asymmetry loss.
- GO:0006658 phosphatidylserine metabolic process is KEEP_AS_NON_CORE. Older family evidence supports a lipid-synthesis consequence, but direct human evidence identifies scrambling as the proximal activity.
- GO:0010698 acetyltransferase activator activity is REMOVE. It is an electronic orthology transfer from rat Serinc2 ultimately tied to PMID:16120614, whose accessible evidence concerns serine-derived lipid synthesis rather than acetyltransferase activation.
- GO:0070062 extracellular exosome is KEEP_AS_NON_CORE. The cached paper says the proteomic data are publicly accessible, and the NHLBI urinary-exosome database row for reference 2 lists SERINC2/NP_849196 with one peptide. This is high-throughput localization evidence, not a core SERINC2 activity.

## Evidence boundary

SERINC2 scrambling is directly demonstrated in purified proteoliposomes, but antiviral restriction and cellular/virion PS-asymmetry disruption are not. The primary study states that "hSERINC2 lacks antiviral activity" [PMID:37474505], while purified SERINC2 retains lipid flipping. The later virion study found robust SERINC2 incorporation but no infectivity effect or PS-asymmetry disruption [PMID:38785977]. Do not propagate the SERINC3/SERINC5 antiviral role to SERINC2.

## 2026-09-19 revision log — two decisions above are superseded

The "Annotation decisions" section above records the 2026-07-25 state. Two calls were
revised during PR review; the entries for GO:0017121 and GO:0010698 above are retained
as a record of the earlier reasoning but no longer describe the review.

- **GO:0017121 plasma membrane phospholipid scrambling: MARK_AS_OVER_ANNOTATED -> ACCEPT (caveated).**
  The earlier call treated the virion data as evidence against the process term. That
  conflated two claims. Purified SERINC2 does flip NBD-PC in reconstituted proteoliposomes
  [PMID:37474505, "hSERINC2 flips at an intermediate rate"], reviewed UniProt curates this
  IDA process annotation at the cell membrane, and the sibling SERINC3/SERINC5 reviews
  ACCEPT the same IDA from the same study. The paper reports the discordance explicitly
  [PMID:37474505, "there is discordance between the preserved lipid flipping activity in
  proteoliposomes containing hSERINC2"], and SERINC2 does not enhance virion PS exposure
  [PMID:37474505, "hSERINC3 and hSERINC5 enhanced PS exposure, while hSERINC2 did not";
  PMID:38785977, "SER5, but not SER2, which lacks antiviral activity, abrogates PS
  asymmetry"]. That boundary is a caveat on the *antiviral* role, not a reason to deny
  that SERINC2 scrambles plasma-membrane phospholipids. The annotation is now ACCEPT and
  is consistent with the GO:0017128 + GO:0005886 core function.

- **GO:0010698 acetyltransferase activator activity: REMOVE -> MODIFY, replacement GO:0008047 enzyme activator activity.**
  The earlier REMOVE rested on the assertion that the rat transfer was "ultimately tied to
  PMID:16120614". That link was inferred, not verified, and has been withdrawn. The GOA
  WITH/FROM field records a GO_REF:0000107 Ensembl Compara transfer from an
  experimentally-derived rat Serinc2 annotation (UniProtKB:Q4FZV1, ECO:0000265), which is
  stronger provenance than a REMOVE can be justified against from incomplete evidence. The
  specific *acetyl*transferase subclass remains unsupported — the relevant family evidence
  concerns phosphatidylserine synthase and serine C-palmitoyltransferase, an acyltransferase
  [PMID:16120614, "A Serinc protein forms an intracellular complex with key enzymes involved
  in serine and sphingolipid biosyntheses"] — so the term is generalized rather than dropped.
  This matches the sibling SERINC1 treatment of the same term.

The `SERINC2-deep-research-manual.md` synthesis still argues the superseded positions in its
"Molecular function and location" and "Lipid-metabolism and transferred annotations"
sections; it needs the same correction and is flagged on the PR.

## Experimental priorities

1. Determine how endogenous SERINC2 activity is regulated without constitutively collapsing plasma-membrane phospholipid asymmetry.
2. Test the cellular consequences of SERINC2 loss and catalysis-defective rescue under matched surface expression.
3. Compare all four UniProt isoforms for topology, localization, lipid specificity, and scrambling kinetics.
