# NSG1 notes

## 2026-09-28 re-review

- Re-reviewed the two IBA rows (`GO:0005783` endoplasmic reticulum and `GO:0016126`
  sterol biosynthetic process). Both trace in `NSG1-goa.tsv` to
  `PANTHER:PTN000393022`; direct yeast evidence for ER localization and Hmg2
  stabilization supports both transfers.
- Checked cached publications relevant to the accepted core function and NVJ
  localization, especially PMID:16270032 and PMID:41132095.
- Searched for newer NSG1/Nsg1 literature and found Fujimoto and Tamura 2026,
  PMID:42227952. The local cache has the PubMed abstract only, but the abstract
  directly reports glucose-starvation-specific NVJ recruitment of Nsg1, Nsg2,
  Hmg1, and Hmg2 and places NSG1/NSG2 in starvation-dependent ergosterol control.
- The 2026 result supports the existing NVJ localization row and improves the
  starvation-context question. It does not require a new GO assertion: the
  existing `GO:0016126` sterol biosynthetic process rows already capture the
  direct pathway role through HMG-CoA reductase control, and the molecular
  activity remains the SSD-client chaperone/regulator activity proposed from
  the Hmg2 work.
- Migrated the three generic `GO:0005515` high-throughput interactome rows from
  legacy `MARK_AS_OVER_ANNOTATED` to `REMOVE`; the interactions are not rejected,
  but generic protein binding is not useful molecular-function curation for NSG1.

## 2026-09-29 PR #3442 follow-up

- Re-read the cached abstract for Fujimoto and Tamura 2026 (PMID:42227952) and
  verified the PMID/DOI against PubMed. The result is functional, not just
  microscopic colocalization: glucose-starvation NVJ remodeling destabilizes
  Nsg1 and activates Hmg1, while stabilizing Nsg2 and suppressing Hmg1; loss of
  both INSIG homologs hyperactivates Hmg1 and accumulates squalene. The
  top-level description now includes this Hmg1 directionality.
- Did not add a new Hmg1 `involved_in` or regulation-of-sterol-biosynthesis
  annotation from the abstract. GO has `GO:0106118 regulation of sterol
  biosynthetic process` and `GO:0106119 negative regulation of sterol
  biosynthetic process`, but the abstract-only cache establishes the genetic
  output and NVJ remodeling state, not a direct Hmg1 binding mechanism for Nsg1
  comparable to the Hmg2 SSD-chaperone mechanism in PMID:16270032. The open
  Hmg1/Hmg2 sign difference is retained as `suggested_questions`.
- Added `reference_review` and a second exact abstract finding for PMID:42227952
  so the cache now records its central Nsg1/Hmg1 result.
- Expanded the two IBA propagation reviews to enumerate the small donor lists:
  SGD:S000001175/NSG1 self-evidence for both rows, human INSIG1/INSIG2 for ER
  localization, and fungal plus metazoan INSIG donors for sterol biosynthesis.
  The self-evidence is direct descendant support for the PAINT node placement,
  not circular evidence.
- Kept the three `GO:0005515` IntAct rows as `REMOVE` but made their reasons
  partner-specific: the two UniProtKB:P12684 rows are Hmg2, the real functional
  client whose interaction is captured by the GO:0044183 replacement and the
  proposed SSD-chaperone term; the UniProtKB:Q8N6L0 row is a human KASH5
  cross-species hit that UniProt marks `Xeno`.
