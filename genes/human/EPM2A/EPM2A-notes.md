# EPM2A review notes

The review covers all 81 imported O95278 annotations: 31 ACCEPT, 20 KEEP_AS_NON_CORE, 19 MODIFY, 10 UNDECIDED and one REMOVE. All original annotation fields and eight product objects are preserved. The separate B3EWF7 source record is not merged into these rows. No NEW annotation or publication quotation was added.

Two core activities are supported: carbohydrate phosphatase activity in glycogen metabolism, and an adaptor contribution to malin-dependent PTG ubiquitination. Direct human glycogen phosphate release is established in [PMID:25544560](https://doi.org/10.1016/j.molcel.2014.11.020). The original main cloning describes residues 1–328 with N-terminal His6, while a separate DXMS preparation describes a C-terminal tag. [PMID:26231210](https://doi.org/10.1074/jbc.M115.658203) compares C3 and C6 phosphate release from selectively labeled Arabidopsis starch; it does not directly measure C2-specific catalysis or establish exclusive C3 specificity on glycogen. [PMID:18070875](https://doi.org/10.1074/jbc.M708712200), Methods and Figure 3C, reconstitutes laforin-dependent PTG ubiquitination by malin. Malin is the ligase; laforin supplies an adaptor contribution.

The direct human protein-substrate assay in [PMID:11001928](https://doi.org/10.1093/oxfordjournals.hmg.a018916) supports secondary protein phosphatase capacity. Synthetic OMFP/pNPP hydrolysis is kept separate from assays using radiolabeled myelin basic protein. [PMID:28536304](https://doi.org/10.15252/emmm.201707608) distinguishes persistent glycogen hyperphosphorylation from malin-dependent rescue of abnormal glycogen chains and Lafora bodies by phosphatase-inactive transgenes. Thus direct phosphate hydrolysis is established without making every disease-related or structural outcome depend on that activity.

The single REMOVE concerns glucose-transfer enzyme activity traced to glycogen-synthase measurements in Epm2a-null extracts in [PMID:18852261](https://doi.org/10.1074/jbc.M807428200). The source also supports a separate phosphorylation-term query. Exact donor records and operative Methods/Figure 6 scope are recorded in the YAML source_defects; these are unreported curator queries, not remote edits. There are no generated aggregate defect reports.

Localization is treated by experimental context. Human glycogen binding/fractionation and microscopy support cytoplasmic and cytosolic pools; conditional nuclear entry and HPA nucleoplasm observations are retained. Polysome-associated signal and near-ER signal do not by themselves demonstrate membrane attachment. Distinct inaccessible ER/plasma-membrane and HIRIP5 sources remain unresolved rather than being rejected from their titles or abstracts.

## Natural products

| Imported product | Source-described length |
|---|---:|
| O95278-1 | 331 aa |
| O95278-2 | 317 aa |
| O95278-4 | 152 aa |
| O95278-5 | 224 aa |
| O95278-6 | 88 aa |
| O95278-7 | 177 aa |
| O95278-8 | 193 aa |
| B3EWF7-1, external POCR record | 344 aa |

These are distinct source products, not inferred functional equivalents. The [O95278 record](https://www.uniprot.org/uniprotkb/O95278/entry) and separate [B3EWF7 record](https://www.uniprot.org/uniprotkb/B3EWF7/entry) provide the product definitions. The original splice-product studies remain incompletely accessible, so the human 331-residue biochemical results are not automatically assigned to every shorter or external product. External autophagy/STBD1 assertions were considered as product-provenance context, without adding them as O95278 annotations.

## Acquisition and access

The genuine normal pipeline acquired 83 GOA records and retained 81 distinct seed contexts after two deterministic duplicate-context collapses. The accepted 42 publication caches and eight later genuine donor/metadata additions remain unchanged. Falcon returned HTTP403 and the perplexity-lite fallback returned HTTP401/quota; neither produced a research result, and no provider-named research file was fabricated. Manual original reading is documented in [the source guide](EPM2A-source-guide.md), with public identifiers, operative sections, species/construct boundaries and access limits. Reference access flags describe actual reviewer access, independently of cache availability.

Normal validation, strict ontology-term validation, computed status and rendering passed. The computed status is DRAFT, with four advisories: one supported generic-binding row retained under campaign policy and three deliberate source-context differences for nucleus, cytoplasm and ER membrane. Those distinctions are explained in the annotation reasons. History creation and canonical publication are performed by the campaign publisher.
