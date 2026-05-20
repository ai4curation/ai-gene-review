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
