# ADH8a3 review

## 2026-10-25

Normal fetch seeded the original GOA assertions; all source fields are retained. Reviewed the full primary Carassius study [PMID:28801642](https://pubmed.ncbi.nlm.nih.gov/28801642/) and the source record. The record-to-publication sequence linkage was checked against the ENA accessions KF960826 (E1alpha3), KF960828 (E1beta2, partial CDS) or JX975104 (ADH8a3). Source files were not edited.

The muscle pathway has strong physiological support, while the individual paralog enzyme assignment uses expression, sequence, localization and structural modeling. No purified alpha3/beta2 reconstitution or ADH8a3 substrate panel is claimed. Conserved PDH-domain membership does not settle coupling to E2 after beta2 interface divergence. The retained conventional-PDH claims therefore remain UNDECIDED rather than being removed. ADH8a comparisons use [PMID:15231826](https://pubmed.ncbi.nlm.nih.gov/15231826/) as homolog evidence, not as a direct carp assay. No new process rows were proposed.

Falcon and fallback provider attempts failed; manual primary research was used and no provider report was fabricated. GOA contains only GO_REF sources, so publication caching from GOA yielded no target paper; relevant primaries were fetched separately. No matching cached GO-CAM activity was found for the three accessions. Exact family labels are reported separately for module integration; no unverified PTN origin is asserted.

Independent annotation-reviewer follow-up: distinguish E1alpha antibody localization from alpha3-specific evidence and general cytosolic ADH background from target localization. Zebrafish ADH8A had no detectable HMGSH activity in the published assay, not low measured activity; target carp specificity remains unresolved.


## 2026-10-25 PR #5545 review follow-up

The suggestion to retain GO:0004022 as the most precise support was evaluated against live QuickGO definitions. GO:0004022 is “Catalysis of the reaction: an alcohol + NAD+ = an aldehyde or ketone + NADH + H+.” Its descendant GO:0120542 is “Catalysis of the reaction: ethanol + NAD+ = acetaldehyde + NADH + H+.” Neither definition makes an exclusivity or substrate-preference claim. Checked https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120542 and the corresponding GO:0004022 endpoint on 2026-10-25.

Retain the two MODIFY decisions and the qualified core function. The evidence is an explicitly inferred reaction capacity, integrating native Carassius muscle physiology, ADH8a3 transcript predominance, branch identity and direct zebrafish ADH8A biochemistry (PMIDs:28801642,15231826). Expression alone does not prove activity, nor do comparator kinetics establish target kinetic constants. However, possible wider substrate activity does not contradict the specific reaction term; absence of a complete carp substrate panel is not evidence against inferred ethanol/acetaldehyde turnover. The modelled Pro122His substrate-channel substitution remains functionally untested. Reasons now make these limits and the nonexclusive GO meaning explicit. No annotation actions, source fields or row counts changed; no NEW was added.
