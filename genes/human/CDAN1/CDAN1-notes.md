# CDAN1 evidence and annotation review — 2026-10-09

The reviewed human Codanin-1 source contains 17 GO assertions and three alternative-product records. All source fields, qualifiers and partners are preserved. The five original references are retained and three primary papers are added. The annotation-reviewer and core-function-synthesizer skills were applied.

## ASF1 sequestration and chromatin regulation

The 2012 study directly tested binding to ASF1A and ASF1B, reciprocal cellular interactions, knockdown, overexpression and rescue. These experiments support regulation of ASF1 availability rather than intrinsic histone deposition by Codanin-1 [PMID:22407294]. The two generic binding rows are therefore refined to protein sequestering activity (GO:0140311).

A short primary anchor identifies the directly tested partners: “full-length Codanin-1 bound to both recombinant Asf1a and Asf1b” [PMID:22407294].

Two 2025 studies provide structural, biochemical and cellular support. Interaction elements occupy ASF1 surfaces used by histones and downstream partners, and mutation of these elements changes binding or cytoplasmic retention [PMID:40038274; PMID:40091041]. The paralogs differ in their dependence on individual binding elements. Neither histone mimicry nor association with ASF1 warrants assigning Codanin-1 histone-chaperone activity. A historical histone-containing complex and later histone-excluding preparations should not be compressed into one universal endogenous composition or stoichiometry.

Chromatin organization is refined to its regulation where the mechanistic evidence supports that distinction. The original positive-effect qualifier on the 2012 source row remains unchanged as provenance; it does not establish that Codanin-1 itself promotes nucleosome assembly. The import annotation is refined to negative regulation of protein import into nucleus, consistent with ASF1 retention and rescue. No new biological-process assertion is proposed, and no matching CDAN1 activity was found in the available GO-CAM index.

## Localization and erythroblast context

Cytosol is the principal established functional location. The 2012 fractionation and the 2025 endogenous-tagging, fractionation and live-imaging experiments support this assignment [PMID:22407294; PMID:40091041]. Nuclear `located_in` observations remain non-core because they are reported in erythroblasts and in a less abundant complex. The separate IBA `is_active_in` nucleus assertion is UNDECIDED: nuclear presence does not establish nuclear molecular activity, and the 2012 discussion presents inhibition after nuclear entry as a possibility rather than an assayed nuclear mechanism. Predominantly cytosolic localization in one experimental cell line does not demonstrate universal nuclear exclusion. A specificity problem reported for one CDIN1 antibody is not attributed to every Codanin-1 antibody.

The 2011 normal cache contains an abstract. Selected primary Results and the Figure 4 legend were additionally accessible through the publisher's indexed text, but the complete body and original supplemental images were not retrieved. These passages describe nuclear/cytoplasmic staining, ER/Golgi marker costaining and SEC23B colocalization. They support retaining the existing broad endomembrane localization, without inventing a more precise organelle or a direct COPII-complex role. The source also reports abnormal HP1alpha distribution in patient intermediate erythroblasts; that contextual phenotype is retained rather than replaced with an ASF1-specific claim [PMID:21364188].

The current [Human Protein Atlas CDAN1 page](https://www.proteinatlas.org/ENSG00000140326-CDAN1/subcellular) reports enhanced cytosol and supported additional plasma-membrane localization. Its antibody/cell-line table was inspected; raw immunofluorescence images were not independently scored. The membrane annotations remain non-core and do not establish integral or multipass membrane topology.

## CDIN1 exonuclease activation

A 2026 primary study demonstrates that a Codanin-1 C-terminal fragment increases CDIN1-mediated RNA cleavage; Codanin-1 alone is inactive. The assay used Codanin-1 residues 866–1227 and a stabilized CDIN1 W237R/C223S/V18M background. Catalytic CDIN1 mutations abolish cleavage. This supports the proposed exoribonuclease activator activity, with the construct limits retained explicitly. The modeled C-terminal complex is not an experimentally solved structure, and no physiological RNA-processing pathway is asserted [PMID:42393042].

## Access and provenance

All five PMID identities and titles were checked against official Europe PMC records. The 2012 full Results/Methods, selected full 2025 experiments, and the 2026 activity Results/protein-expression Methods were inspected. The 2011 cache remains unchanged and abstract-only. Existing source objects and all three products—Q8IWY9-2, Q8IWY9-1 and Q8IWY9-3—remain intact; construct numbering is not treated as an isoform-specific annotation.

A genuine isolated Falcon attempt with an explicit Perplexity-lite fallback failed while fetching a dependency from PyPI and produced no research report. These are manual notes. The YAML uses two short exact quotations, totaling 13 words from PMID:40038274 and 20 words from PMID:42393042. These notes add one nine-word anchor from PMID:22407294, with no repeated quotation.
