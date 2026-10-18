# NSG2 notes

## 2026-09-28 re-review

- Re-reviewed the two NSG2 IBA rows and traced both in `NSG2-goa.tsv` to the
  same INSIG-family PAINT node, `PANTHER:PTN000393022`. Both transfers are
  supported: ER localization matches the direct Nsg2 membrane-protein record,
  and sterol biosynthetic process is correct when interpreted as HMG-CoA
  reductase regulation rather than direct sterol-enzyme catalysis.
- The `GO:0016126` IBA includes `SGD:S000005100` in `WITH/FROM`; this is Nsg2
  itself and is expected descendant support for the PAINT node placement, not
  circular evidence.
- Read the cached NSG2-relevant publications, especially PMID:16270032 and the
  2025 NVJ full text PMID:41132095. Searched for newer Nsg2 literature and found
  Fujimoto and Tamura 2026, PMID:42227952, which is the published follow-up to
  the bioRxiv work noted in the Falcon report.
- The 2026 paper is cached as an abstract-only PubMed record. It directly
  supports Nsg2 recruitment to the NVJ with Hmg1/Hmg2 during glucose starvation
  and the model that Nsg2 is stabilized during this remodeling to suppress Hmg1.
- Removed the suggested question about whether the PANTHER/IBA annotations are
  reliable across INSIG subfamilies because the node-level re-review supports
  both current IBA rows for yeast Nsg2.

## 2026-09-29 PR #3443 follow-up

- Re-read PMID:42227952 and verified the PubMed record. The direct microscopy
  and the 2026 abstract agree that Nsg1 and Nsg2 are recruited to the NVJ
  during glucose starvation, but the functional consequence is paralog-specific:
  this remodeling destabilizes Nsg1 and activates Hmg1 while stabilizing Nsg2
  and suppressing Hmg1. The `GO:0071561 nucleus-vacuole junction` annotation
  therefore remains `KEEP_AS_NON_CORE` as a conditional site, but the rationale
  no longer treats shared recruitment as evidence against an Nsg2-specific NVJ
  outcome.
- Updated the top-level description and core-function text to include Nsg2
  suppression of Hmg1 during glucose-starvation remodeling, alongside the
  classic Hmg2 ERAD-protection activity.
- Added `reference_review` for PMID:42227952 and expanded the
  `GO:0016126` IBA `source_entities` to list the SGD:S000005100 self-donor,
  the NSG1 paralog, and the fungal/metazoan INSIG donors that appear in
  `NSG2-goa.tsv`.
- Removed the Hmg2 interaction quote from the ER IBA row's `supported_by`
  list; the UniProt subcellular-location sentence is the direct support for the
  ER component assertion.
- Reworded the low-glucose suggested question from a question the 2026 paper
  had already answered into the remaining mechanism: whether stabilized Nsg2
  suppresses Hmg1 directly through SSD binding, through Hmg1 assembly, or
  indirectly through local NVJ lipid composition.
