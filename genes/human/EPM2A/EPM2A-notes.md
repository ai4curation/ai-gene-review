# EPM2A review notes

The review covers all 81 imported O95278 annotations: 31 ACCEPT, 17 KEEP_AS_NON_CORE, 19 MODIFY, 11 UNDECIDED, two MARK_AS_OVER_ANNOTATED and one REMOVE. All original annotation fields and eight product objects are preserved. The separate B3EWF7 source record is not merged into these rows. No NEW annotation or publication quotation was added.

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

The acquisition pipeline retrieved 83 GOA records and retained 81 distinct seed contexts after two deterministic duplicate-context collapses. The accepted 42 publication caches and eight later donor/metadata additions remain unchanged. Falcon returned HTTP403 and the perplexity-lite fallback returned HTTP401/quota; neither produced a research result, and no provider-named research file was fabricated. Manual original reading is documented in [the source guide](EPM2A-source-guide.md), with public identifiers, operative sections, species/construct boundaries and access limits. Reference access flags describe actual reviewer access, independently of cache availability.

The review retains source-specific uncertainty, and its workflow status is calculated separately by validation. The source guide links the inspected originals and distinguishes original access from publication-cache availability.


## Follow-up adjudication, 2026-10-24

The PTG/malin core and two corresponding binding refinements now use the more specific GO:1990756 ubiquitin-like ligase-substrate adaptor activity. The current definition includes ubiquitin ligases such as malin. Its present official label is broader than the historical ubiquitin-only synonym, but the documented EPM2A activity remains PTG recruitment to malin; no UFM1 activity is inferred. PMID:18070875 Figure 3C distinguishes coordinating substrate recruitment from malin's ubiquitin-transfer chemistry. The PMID:22961547 PRDM8-containing complex also supports the specific ubiquitin-protein-ligase-binding term for its malin component, while preserving the PRDM8 association context.

The model-protein and physiological-process claims are separated. PMID:11001928 measures a real protein-phosphate-removal reaction after eight hours; the protein-phosphatase molecular capacities remain non-core. The protein-dephosphorylation and peptidyl-tyrosine process assignments supported by that model assay are judged likely over-annotations of the established physiological role, in light of the glucan evidence and negative tested protein candidates in PMID:16901901. This is a bounded biological judgment, not a claim that the GO definitions prohibit in-vitro evidence or that all protein substrates are excluded. The distinct HIRIP5 paper remains unavailable and its positive abstract is not refuted by experiments on other substrates; its process row is UNDECIDED. PMID:11739371's pNPP/glycogen work remains source context, not positive support for a peptidyl-tyrosine reaction.

The suggested questions now identify the unresolved noncatalytic rescue mechanism and possible physiological protein substrates. No new annotation, product equivalence or publication quotation is introduced. The campaign explicitly requires reference-only support; direct original links and assay locators remain in [the source guide](EPM2A-source-guide.md).

## Database feedback clarification, 2026-10-24

The broad phosphate-metabolism annotation is retained as non-core, supported by glucan phosphate release. QuickGO's `usage: None` for GO:0016311 is an annotation restriction, not an annotation count; the official term display maps it to a restriction on direct annotation. The term is still non-obsolete and OLS records it as an obsoletion candidate. It is therefore not authored as a replacement. See the [official QuickGO display template](https://www.ebi.ac.uk/QuickGO/term/term.html) and [GO decision26424](https://github.com/geneontology/go-ontology/issues/26424).

The negative-phosphate-regulation and exact ER-membrane-face assertions remain undecided. Verified rule matching establishes provenance; the inspected evidence neither establishes these exact claims nor identifies a sufficiently demonstrated erroneous transfer to remove them. Full-text availability does not itself settle biological scope. The broad cytoplasm row is accepted consistently across experimental and electronic evidence, with separately supported cytosol annotations preserved.
