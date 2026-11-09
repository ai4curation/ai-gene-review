# GLA notes

## Core function and evidence

- GLA encodes lysosomal alpha-galactosidase A, a glycosyl hydrolase whose core function is hydrolysis of terminal alpha-D-galactose from glycosphingolipids in the lysosomal lumen. UniProt states that GLA "Catalyzes the hydrolysis of glycosphingolipids and participates in their degradation in the lysosome" and lists EC 3.2.1.22 alpha-galactosidase activity with reactions for globoside Gb3Cer hydrolysis [file:human/GLA/GLA-uniprot.txt].
- Reactome models the core lysosomal reaction as GLA hydrolyzing saposin-B-mobilized Gb3Cer and Gal2Cer in the lysosomal lumen: "Alpha-galactosidase A (GLA) ... removes the terminal galactose residue from glycolipids or glycoproteins, mobilized by PSAP(195-273) (Saposin B), resulting in galactose and an alcohol" [Reactome:R-HSA-1605736; Reactome:R-HSA-9841189].
- In a detergent-free liposomal system mimicking lysosomes, degradation of globotriaosylceramide was dependent on both recombinant human alpha-galactosidase and saposin B, and the authors concluded that "only SAP-B is essential for the degradation of GbOse3Cer by alpha-galactosidase" [PMID:8804427].
- Mutant enzyme studies in Fabry variants confirm the same natural-substrate activity context: "the degradation of the natural substrate, globotriaosylceramide, by the alpha-galactosidases was analyzed in a detergent-free-liposomal system, in the presence of sphingolipid activator protein B" [PMID:10838196].
- Purified human alpha-galactosidase A is a homodimeric enzyme: Bishop and Desnick reported that "The purified enzyme was a homodimer with a native molecular weight of 101,000 and a subunit weight of 49,800" [PMID:6256390], and the crystal structure likewise states that "The structure is a homodimer" [PMID:15003450].

## Localization and trafficking

- The physiologically central compartment is the lysosomal lumen. UniProt lists subcellular location as "Lysosome" and Reactome places the Gb3Cer and Gal2Cer hydrolysis reactions in the lysosomal lumen [file:human/GLA/GLA-uniprot.txt; Reactome:R-HSA-1605736; Reactome:R-HSA-9841189].
- GLA enters the secretory/lysosomal trafficking pathway as a precursor and can be secreted under some conditions: normal fibroblasts synthesize a phosphorylated precursor that is processed to a mature form, while NH4Cl and I-cell fibroblasts cause most newly synthesized enzyme to be secreted [PMID:3029062].
- Overexpression in CHO cells caused TGN and lysosomal crystalline aggregates and selective secretion; the authors explicitly proposed that aggregates forming in the acidic TGN are secreted when unable to bind M6P receptors, making Golgi/TGN accumulation an overexpression phenotype rather than the core location [PMID:1332979].
- Recombinant or secreted alpha-Gal A can bind endocytic/sorting receptors for uptake: the CHO overexpression study found that secreted enzyme had mannose-6-phosphate moieties and bound immobilized 215-kD M6PR [PMID:1332979], and podocyte work identified M6PR, megalin, and sortilin as alpha-Gal A binding proteins important for uptake [PMID:21949853].
- Extracellular-region, extracellular-exosome, and azurophil-granule annotations are best treated as non-core localization/trafficking observations; they do not change the core function from lysosomal glycosphingolipid catabolism.
- Cytoplasm annotations are not supported by the accessible GLA evidence reviewed here; the direct localization papers support lysosome/lysosomal lumen, secretory trafficking, extracellular secretion/uptake, and overexpression-associated TGN aggregates instead.

## Annotation cautions

- Generic protein binding is not informative for GLA. Physiologically interpretable binding evidence concerns receptor-mediated uptake by M6PR/sortilin/megalin, while BioPlex, fragmentomics/PDZ, and multimodal cell-map interaction datasets are high-throughput interactome resources that do not establish a core GLA molecular function [PMID:33961781; PMID:36115835; PMID:40205054].
- The ConA-mediated uptake study used concanavalin A to stabilize and deliver purified enzyme to Fabry fibroblasts, so a GO protein-binding annotation to ConA should not be treated as an endogenous GLA function [PMID:6313412].
- Nitric-oxide and nitric-oxide-synthase regulation annotations are downstream Fabry-disease/orthology phenotypes rather than direct activities of the lysosomal hydrolase; they should not be represented as core biological processes for human GLA.

## Falcon deep-research cross-check

- Falcon deep research completed on 2026-05-13 and independently reinforced the existing review model: the target is human UniProt P06280 GLA/alpha-galactosidase A, a lysosomal enzyme whose primary molecular function is alpha-galactosidase activity and whose pathway context is lysosomal glycosphingolipid degradation [file:human/GLA/GLA-deep-research-falcon.md "Primary molecular function.** Lysosomal **α‑galactosidase A** (EC **3.2.1.22**) that removes terminal **α‑galactose** from glycoconjugates"; file:human/GLA/GLA-deep-research-falcon.md "Pathway/process.** Lysosomal glycosphingolipid degradation; defects lead to Fabry disease pathophysiology"].
- The Falcon report adds recent-review support that Fabry disease biochemistry is described in terms of Gb3/GL-3 plus downstream lyso-Gb3 accumulation, but this does not change the core GO curation from lysosomal alpha-galactosidase activity and glycosphingolipid catabolic process [file:human/GLA/GLA-deep-research-falcon.md "deficiency causes accumulation of **Gb3** and **lyso-Gb3** in Fabry disease"].
- Falcon also corroborates treating M6PR/sortilin/megalin receptor evidence as trafficking or therapeutic-enzyme uptake rather than as the core enzyme function [file:human/GLA/GLA-deep-research-falcon.md "Additional uptake routes reported in kidney cells include **sortilin** and **megalin**."].


## 2026-11-06 — current annotation reassessment

All 58 current annotations were individually reviewed with the literal machine contexts retained. The detailed evidence scope is in [GLA-evidence.md](GLA-evidence.md). This entry supersedes earlier judgments without altering the preceding journal.

Correction: the earlier rejection of cytoplasm equated it with cytosol. GO:0005737 includes organelles; the two current cytoplasm assertions are compatible with the biology and are marked too general, while root lysosome annotations remain accepted. The catalytic core now also recognizes directly demonstrated oligosaccharide turnover. Dimerization is retained as observed, without a universal requirement across enzyme preparations.

Generic-binding removals preserve positive associations and do not allege wrong genes or experimental failures. Cargo uptake is not receptor activity. The inherited provider report is unchanged; primary support and its limits are documented separately. The prior 43 review objects, 28 references and 50 quote associations remain recoverable from the original Git commit and blob. Four earlier curation histories remain intact.


Native preparation also preserves the later main-branch cytoplasm correction from commit 66c8c42c and its 2026-11-03 curation history. Five prior GLA histories remain intact. The fresh native seed reproduces all 58 reviewed contexts and all 16 exported fields; the single 429-residue product is unchanged. Source acquisition added only missing records and preserved every existing cache.


## 2026-11-06 — review follow-up

The review feedback is addressed by narrower process specificity, primary quotation anchors where cached text exists, and clearer evidence boundaries. The public archive manifest is removed; its exact bytes and all historical records remain preserved. The original journal prefix is unchanged. Primary sources now support both electronic catalytic rows explicitly; the inherited provider output remains background only. Selected original reading remains essential where indexed cache text is incomplete.

Native follow-up validation retains one advisory warning because the inherited provider report is not cited as annotation/core evidence. The computed status is therefore DRAFT; this does not signify an unreviewed annotation. All biological support remains grounded in primary sources.
