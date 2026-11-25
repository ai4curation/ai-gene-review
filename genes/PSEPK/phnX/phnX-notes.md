# phnX curation notes

- Q88KT1 is a reviewed PhnX-family phosphonoacetaldehyde hydrolase with EC
  3.11.1.1 and RHEA:18905. The assigned reaction is phosphonoacetaldehyde plus
  water to acetaldehyde plus phosphate [UniProtKB:Q88KT1,
  "Reaction=phosphonoacetaldehyde + H2O = acetaldehyde + phosphate + H(+);"]
- The specific family evidence is concordant across HAMAP MF_01375, InterPro
  IPR006323, NCBIfam TIGR01422, and PANTHER PTHR43434:SF19
  [UniProtKB:Q88KT1, "DR   InterPro; IPR006323; Phosphonoacetald_hydro."].
- The TreeGrafter phosphoglycolate-phosphatase and DNA-repair annotations are
  inconsistent with the exact PhnX subfamily and reaction and are removed.
- Direct 2-aminoethylphosphonate:pyruvate aminotransferase and phosphonatase
  activities were measured in *P. putida* NG2 and were induced by substrate
  independently of phosphate status [PMID:9841125,
  "phosphonoacetaldehyde hydrolase (phosphonatase) activities which were inducible"].
  No direct biochemical assay of Q88KT1 from KT2440 was found, so its assignment
  remains a strong family- and pathway-context inference rather than
  strain-specific experimental evidence.

## 2026-10-25: PhnWX cross-species module audit

Rechecked all seven existing annotations. The defining activity and phosphonate
catabolism remain ACCEPT, supported by curated HAMAP MF_01375 and the exact PhnX
family. Independent chemistry is established in **Bacillus cereus and Salmonella**
(PMID:9649311), and magnesium coordination in **B. cereus** (PMID:10956028).
Neither experiment tested KT2440 Q88KT1. NG2 pathway activity (PMID:9841125) and
BIRD-1 regulation (PMID:35229442) likewise remain explicitly strain-scoped.

Changed cytosol from KEEP_AS_NON_CORE to UNDECIDED: its only cited support was its
own UniProt electronic GO line. Intracellular catabolic context makes the location
plausible, but no independent localization evidence for Q88KT1 was retrieved.
The absence of such evidence does not establish a different localization.

Retained removal of phosphoglycolate phosphatase and DNA-repair annotations. The
HAD superfamily includes multiple substrate specializations; Q88KT1 has the
PhnX-specific signature and catalytic mechanism. Corrected the earlier rationale:
a free phosphoglycolate phosphatase annotation is not evidence for hydrolyzing
3'-phosphoglycolate directly on damaged DNA. No claim about a particular ancestral
TreeGrafter node is made without inspecting that node.

Replaced the AI-report citation in core support with PMID:9649311, added explicit
reference assessments, and annotated UniProt quote sections using the helper.
No new GO assertion was added.

`just fetch-fitness PSEPK phnX` failed because neither a local FEBA database nor
the remote source was reachable; no artifact was written. This is a data-access
limitation, not a negative fitness result.

## 2026-11-02

Cytosol row changed from UNDECIDED to KEEP_AS_NON_CORE: phosphonates are imported before catabolism (PMID:37836707, "the import of phosphonates implies the involvement of transporters"), PhnX is a soluble signal-less HAD enzyme, and the PTHR43434 family review rates the cytosol IBD at PTN001291474 SOUND. No native-cell localization assay was found; the location stays non-core. Status promoted to COMPLETE; the openscientist deep-research file is now cited as a cross-checked source.
