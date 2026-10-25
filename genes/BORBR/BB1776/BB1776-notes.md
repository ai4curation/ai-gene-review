# BB1776: nicotinate entry-system audit

## Identity and scope

Accession A0A0H3LTT1; Bordetella bronchiseptica RB50. All 3 pre-existing rows reviewed; original non-review fields preserved. Nicotinate entry chemistry is distinct from nicotine oxidoreductases with similar gene names.

## Manual primary-source assessment

PMID:29485696 full publisher article read at https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.13943. Table 1 maps this RB50 locus to the proposed NicB component. Assignment is architectural inference in a study principally about pathway regulation/physiology, not purified target turnover. The cache contains only the abstract, so full-text findings are paraphrased here rather than represented as cached quotations.

BB1783/A0A0H3LKL9 is 774 aa; BB1776/A0A0H3LTT1 is 946 aa. The latter includes MCD-enzyme-related regions and three cytochrome domains. This is more complex than a simple two-way cut of KT2440 NicB. No new nicotinate-process annotation, membrane topology, catalytic stoichiometry or direct native-complex assay is asserted. Broad oxidoreductase function is supported by domain architecture; submitter aldehyde/cytochrome names are not functional proof.

## Research provenance

Normal fetch-gene seeded the accession-specific review. Default Falcon and fallback Perplexity-lite requests failed; manual primary-source and domain analysis substituted, with logs /tmp/nicotinate-BB1776-deep.log. No provider report was invented. FEBA lacks a BORBR mapping and no local or remote dataset was reachable. No cached GO-CAM was identified.

## Verified family membership

- DR   PANTHER; PTHR35008:SF8; ALCOHOL DEHYDROGENASE CYTOCHROME C SUBUNIT; 1.
- DR   PANTHER; PTHR35008; BLL4482 PROTEIN-RELATED; 1.

Official labels were checked against interpro/panther/panther.obo. These broad family assignments do not alone establish nicotinate substrate specificity; no PTN ancestry was guessed.

## Annotation ledger

- GO:0009055 (IEA, GO_REF:0000002): ACCEPT. Independent PROSITE domain matches support the redox-carrier activity. The proposed NicB1 role in PMID29485696 is consistent, but the physiological acceptor and target-specific enzyme turnover remain unassayed here.
- GO:0016491 (IEA, GO_REF:0000002): ACCEPT. Molybdopterin-binding domains support the broad assertion. PMID29485696 proposes this locus as NicB1, an electron-transfer component with cytochrome and MCD-related regions of the nicotinate system, but does not establish purified target-specific reaction kinetics. Keep the warranted broad function rather than infer aldehyde substrate specificity from an automated name.
- GO:0020037 (IEA, GO_REF:0000002): ACCEPT. Three independently detected cytochrome domains provide computational support for heme binding; this is not a claim of directly measured heme stoichiometry.
