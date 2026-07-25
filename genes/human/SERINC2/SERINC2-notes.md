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

## Experimental priorities

1. Determine how endogenous SERINC2 activity is regulated without constitutively collapsing plasma-membrane phospholipid asymmetry.
2. Test the cellular consequences of SERINC2 loss and catalysis-defective rescue under matched surface expression.
3. Compare all four UniProt isoforms for topology, localization, lipid specificity, and scrambling kinetics.
