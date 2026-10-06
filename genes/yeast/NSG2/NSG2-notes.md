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

## 2026-10-01 current GOA refresh

- Refreshed NSG2 against live GOA and UniProt. GOA now carries 11 rows: the 7
  still-live historical assertions plus new rows for `GO:0006457` protein
  folding, `GO:0031965` nuclear membrane, an exact `GO:0044183` protein
  folding chaperone row that replaces the former `GO:0051082` assertion from
  PMID:16270032, and a second `GO:0071561` NVJ row from PMID:42227952.
- Preserved every exact historical assertion. The old `GO:0051082` row from
  PMID:16270032 is no longer present in the live source and is now retained
  with `retired: true`; the live SGD replacement is `GO:0044183`.
- Fetched the current `PTHR15301` PAINT node slice. The two live NSG2 IBA rows
  are both supported by `PANTHER:PTN000393022`; current IBD data propagate
  `GO:0005783` and `GO:0016126` at that node, matching the accepted yeast
  ER/sterol-pathway biology. The row-level `propagation_review.source_entities`
  now name that PTN node only; the extant `WITH/FROM` descendants remain as
  deterministic `supporting_entities`.
- Searched PubMed/Web for newer yeast NSG2/Nsg2 literature. The newest direct
  paper found was Fujimoto and Tamura 2026, PMID:42227952; its full text was
  gated at JCB/Rockefeller University Press, but the PubMed/JCB abstract
  directly supports glucose-starvation recruitment of Nsg1/Nsg2/Hmg1/Hmg2 to
  the NVJ and Nsg2 stabilization to suppress Hmg1.
- Accepted the new SGD `GO:0044183` row and marked the new logical `GO:0006457`
  row as over-annotated, because the current chaperone term is the best
  available molecular-function parent but the inferred broad protein-folding
  process still overstates Nsg2's direct SSD-client stabilization activity.
  Kept the new 2026 nuclear-membrane and NVJ rows as non-core localizations
  because they capture conditional starvation remodeling rather than replacing
  the core Hmg2 sterol-sensing-domain chaperone role.

## 2026-10-01 PR #3774 follow-up

- Harmonized the proposed SSD-client chaperone NTR with the NSG1 wording and
  made the gap rationale explicit: `GO:1904293` and `GO:0050821` capture
  downstream process/outcome terms rather than the molecular activity of
  binding a sterol-sensing domain client.
- Added HMG2 as the direct substrate for the curated core activity and trimmed
  the core-function description so the conditional NVJ/Hmg1 outcome is not
  elevated into the primary molecular activity.
- Changed the logical `GO:0006457 protein folding` row from `ACCEPT` to
  `MARK_AS_OVER_ANNOTATED` to reflect the overbroad process inherited from the
  interim `GO:0044183` mapping.
- Expanded both NSG2 IBA comments to state that `PANTHER:PTN000393022` is an
  Opisthokonta placement, while mammalian cholesterol-process control is placed
  separately in PAINT below a Eumetazoa node.
