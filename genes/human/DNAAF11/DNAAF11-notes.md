# DNAAF11 review notes

## 2026-10-17

Reviewed human DNAAF11 (LRRC6), Q86X45, using the 53 normalized source annotations and both official products. The review contains 10 ACCEPT, 15 MODIFY, 23 KEEP_AS_NON_CORE, four UNDECIDED and one REMOVE decisions. No new annotation is proposed. Detailed source locators and assay boundaries are in the [source guide](DNAAF11-source-guide.md).

The core is outer and inner dynein-arm assembly in DynAPs. Primary human airway studies establish assembly defects; endogenous human LRRC6/DNAI1 foci provide a more specific core location. The positive ciliary observations and a different airway study's negative axonemal localization are both retained. Foci are not used to infer a separate diffuse cytosolic pool; the imported cytosol assertions retain their curated mouse donor evidence. The one rejected extracellular-region mapping confuses a fluid-movement process with the assembly factor's location.

Partner-specific review preserves the ZMYND10 and SCRIB associations with assay limits. Sequence-resolved HuRI DDX6 and MEOX2 interactions support finer binding classes without transferring helicase or transcriptional activity to LRRC6. Seven other HuRI interactions remain positive non-core associations. The two natural products retain their source identities; the 414-residue product retains the CS domain and is not assumed functionally equivalent to the canonical product.

Four developmental assertions remain unresolved. Mouse meiotic expression, impaired sperm movement and infertility alone do not identify the developmental step performed by LRRC6. The later FOXJ1 study informs this question without establishing a direct import mechanism or a new molecular function.

Normal source caches and their availability flags are preserved. Separately recovered original sections are identified in the source guide, including the human-versus-mouse distinction in PMID:33403504. The ordinary research-provider attempt and configured fallback failed authentication/quota checks; no provider report was fabricated. Manual source review supplies the evidence described here. The three short quotations occur once each in the YAML core and are exact cached substrings.

## Follow-up: location scope and original-source access

This clarification supersedes the earlier DynAP-only replacement of every broad cytoplasm row. Cytosol and DynAPs are distinct compartments in GO. The germ-cell rows now refine to the already supported cytosol assignment; broader target-level rows retain both cytosol and DynAP coverage, with separate source attribution. This synthesis does not exhaust the cytoplasmic locations in every cell examined by the original studies. The cytosol assignment relies on existing MGI donor evidence from mouse O88978, not on interpreting human cytoplasmic foci as soluble fractionation. The one assembly/incorporation core includes both locations and the already accepted protein-localization process. Its DynAP evidence is specifically human airway multiciliated-cell imaging, not a germ-cell condensate demonstration.

The earlier human airway paper [PMID:23527195](https://doi.org/10.1371/journal.pone.0059436), Results on LRRC6 expression and Figure 2, reports “distributed throughout the cytoplasm”. This observation remains valid alongside the later human DynAP study; the two images do not establish mutually exclusive pools.

The source availability flags remain unchanged. The following short passages come from separately recovered original text and are not represented as quotations from the abstract-only normal caches:

- [PMID:33403504, PMC7910352](https://pmc.ncbi.nlm.nih.gov/articles/PMC7910352/), Results, Expression of LRRC6 in various germ cells, and Figure 4: “testis sections from adult mice”. The Immunofluorescence staining Methods also identify 12-week-old C57BL mice. The separate loss-of-function Results and Figure 2c concern patient/control human sperm. These are text/caption distinctions; no new image analysis was performed.
- [PMID:23891471, PMC3738835](https://pmc.ncbi.nlm.nih.gov/articles/PMC3738835/), Results describing the human interaction tests beside Figure 4F/G and Figure S7: “Human ZMYND10 and LRRC6 cDNAs were cloned”; the controlled pull-down “showed specific binding of the GST-ZMYND10 only”. The passage distinguishes the human two-hybrid constructs from in-vitro-translated Myc-LRRC6 and its GST control. Verification is of the recovered relevant sections, not an assertion that the normal cache contains the full article.

The DDX6 and MEOX2 HuRI refinements remain qualitative binding-class claims with exact sequence and assay-record support. They do not imply native ciliary complexes or transfer the partners' activities to LRRC6. The [source guide](DNAAF11-source-guide.md) now links the exact validated records and explains the clone comparison and the different partner-class evidence for TERF1 and SSX7. It is a locator, not primary support.

Motile-cilium assembly is now ACCEPTed and included in the same core: assembling the dynein-arm constituents contributes to assembling functional motile cilia, even when ciliary projections remain after disruption. The term is not a typed ancestor of the two arm-assembly terms in the current ontology. The later FOXJ1 study is addressed in this reason; its mouse organoid and transfected-cell results inform the broader biogenesis context, while the direct connection remains unresolved. The localization-process replacement is explicitly lateral in the current ontology. No new molecular activity or annotation is added merely to fill a core slot.

The resulting review has 11 ACCEPT, 14 MODIFY, 23 KEEP_AS_NON_CORE, four UNDECIDED and one REMOVE decisions. All 53 imported source objects and both product descriptions remain unchanged.
