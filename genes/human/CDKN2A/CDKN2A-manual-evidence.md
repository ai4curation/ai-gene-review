# CDKN2A primary-source access and product evidence

Manually prepared on 2026-10-10 from authentic primary sources and database responses. This is an evidence locator and bounded interpretation, not a generated provider report or replacement publication cache. The original annotation objects and product records are unchanged. Source PDFs remain in local provenance; no complete copyrighted paper is republished here.

## Distinct protein products

The fetched UniProt P42771 record describes the 156-residue p16 protein and explicitly lists external Q8N726-1/p14ARF and Q8N726-2/smARF products. Alternative first exons join shared genomic sequence in different reading frames. The [literal product/donor extract](CDKN2A-product-evidence.json) preserves the current human and mouse annotation records, protein identifiers and Ensembl mapping. The current mouse p16 accession is P51480; mouse ARF is Q64364. The separate historical Ensembl GO assertion was not recovered, although its protein identity was checked.

### PMID:11278317 — ARF/spinophilin

*The human tumor suppressor arf interacts with spinophilin/neurabin II, a type 1 protein-phosphatase-binding protein.* [DOI](https://doi.org/10.1074/jbc.M006845200); [author manuscript](https://www.iris.unina.it/retrieve/e268a72d-bf41-4c8f-e053-1705fe0a812c/J.%20Biol.%20Chem.-2001-Vivo-jbc.M006845200.pdf).

SHA256 `efd80aff9d50790e52caa3e3d402fb21a252240e3900aae53a40fe14203fe10d`. Selected Methods PDF pp.5–10, Results pp.12–15 and Figure2/3 legends pp.28–29 were read. The Methods describe a “fragment encoding the entire ARF (132 amino acids)”. Purified MBP–ARF/GST–spinophilin binding and ARF co-IP in COS-7 test ARF constructs, not p16. This supports removal of the exact P42771 assignment while preserving valid ARF biology; no source isoform is invented.

### PMID:20381282 — product-selective apoptosis experiment

*p19(ARF) deficiency reduces macrophage and vascular smooth muscle cell apoptosis and aggravates atherosclerosis.* [DOI](https://doi.org/10.1016/j.jacc.2010.01.026); [author manuscript](https://digital.csic.es/bitstream/10261/24423/1/JACC120409-5696D-revision%202.pdf); [supplement](https://digital.csic.es/bitstream/10261/24423/2/Online%20supplement-JACC120409-5696D.pdf).

Main SHA256 `c8951f310ddeda1be7092c28eb4e5d7fc8010366594fb49daf9930a2cb03c2ef`; supplement `ab661f8ebd685bec20ebf2900bd3c85e559c7fa81e46b68eff839fc715140621`. Main Methods pp.6–10, Results pp.12–13, Figure4/5 and supplement genotyping/qPCR pp.2–3/FigureS2 p.5 distinguish ARF deficiency from retained p16. Aortic p16 expression increases in the ARF-deficient background; cultured smooth-muscle p16 levels do not differ significantly. The phenotype is not a deletion of all Cdkn2a products. Both current mouse apoptosis GO records attach that experiment to P51480, explaining the source-specific error in the human p16 transfers.

### Human ARF mechanism — PMID:9724636 and PMID:35944929

[PMID:9724636 full publisher article](https://link.springer.com/article/10.1093/emboj/17.17.5001) establishes human ARF/MDM2-dependent p53 regulation. The ternary co-IP requires MDM2; it does not prove direct ARF–p53 binding. [PMID:35944929](https://pmc.ncbi.nlm.nih.gov/articles/PMC9366199/) was read in its genuine full normal cache: selected Figures3–5 and construct/purification/pull-down/lysine-discharge Methods. Engineered N32 ARF/GFP/MDM2 fusion constructs support E3 inhibition, not an untagged full-length physiological assay. GO:1990948 is consequently recorded only in the explicitly mapped Q8N726-1 functional-product class, never as an unqualified P42771 core or an added source assertion.

## p16 activity and non-core contexts

### PMID:8259215 — own inhibitor activity

*A new regulatory motif in cell-cycle control causing specific inhibition of cyclin D/CDK4.* [Publisher PDF](https://www.nature.com/articles/366704a0.pdf), SHA256 `288d5bf5089a048132479ac4d74bfa25d59c64899ded16e03945e03972a8e0b8`.

Selected Results/Figures1–3 and Methods distinguish the historical 148-residue human p16 clone, native human p16/CDK4 complexes, and purified His-p16 inhibition of CDK4/cyclinD2-mediated GST-RB phosphorylation. The insect expression host is not the protein species. The adjacent p21 article on the first printed page is excluded. No activity is transferred to every present-day splice product. The supporting quotation appears once in the review YAML, not repeated here.

### PMID:10208428 — cell counts versus individual-cell growth

*Comparison of the effectiveness of adenovirus vectors expressing cyclin kinase inhibitors p16INK4A, p18INK4C, p19INK4D, p21(WAF1/CIP1) and p27KIP1 in inducing cell cycle arrest, apoptosis and inhibition of tumorigenicity.* [Publisher PDF](https://www.nature.com/articles/1202466.pdf), SHA256 `1428b87c36aca09df063992b54f3eee157ce16ecce513b9b4b83ccf54fec6a2f`.

Selected Figure2, Results and Methods on PDF pp.2–3/11–12 identify human p16 constructs, human A549 and separate mouse MT1A2 experiments. Daily viable-cell counts, thymidine incorporation, colonies and DNA-content profiles support population-proliferation regulation. Early cytostasis is distinguished from later cell death. GO:0016049 concerns individual-cell size/material accumulation, so the existing cell-growth regulation row is refined to GO:0008285 rather than denying the observed effect.

### PMID:10205165 — adhesion assay distinctions

*The p16(INK4a) tumour suppressor protein inhibits alphavbeta3 integrin-mediated cell spreading on vitronectin by blocking PKC-dependent localization of alphavbeta3 to focal contacts.* [Full publisher article](https://link.springer.com/article/10.1093/emboj/18.8.2106), retrieved HTML SHA256 `1a6f9d882fdcbb6b17004e945151345b1a01000e3aede90b0075056a1686bb5d`.

Selected full Results/Figure10 and Methods show full-length p16 in human VUP15 melanoma reducing spreading and 12-hour attachment on vitronectin, reversed by CDK6 co-expression. Separate acute CKI-peptide assays preserve attachment while affecting spreading/focal contacts. No peptide result is represented as a full-length human-domain assay, and p16 is not assigned integrin or PKC activity.

### PMID:16243918 — compartment and phenotype scope

*Contribution of p16INK4a and p21CIP1 pathways to induction of premature senescence of human endothelial cells: permissive role of p53.* DOI `10.1152/ajpheart.00364.2005`. [Author-uploaded full manuscript](https://www.researchgate.net/publication/7522539_Contribution_of_p16INK4a_and_p21CIP1_pathways_to_induction_of_premature_senescence_of_human_endothelial_cells_Permissive_role_of_p53).

The browser-indexed full Results state that “p16 fusion protein was localized in both nuclei and cytoplasm”, explicitly as data not shown. Selected Figure2/4–7 descriptions establish cell-cycle and senescence effects in HUVECs. The source is a p16–EGFP experiment, not an endogenous-only localization image. Direct HTTP retrieval failed, but selected indexed full-text reading succeeded and its genuine tool response was preserved; the repository abstract remains unchanged.

### PMID:10353611 and PMID:9054499

[10353611 publisher PDF](https://www.nature.com/articles/1202617.pdf), SHA256 `d53ae562733c9df47d9a0dc57e15bd6bfc869a67c54de2621e7ed037d0419543`: selected Figures1–4 show human p16/RELA co-IP, recombinant overlay and NF-kappaB reporter suppression. The short supporting quotation appears once in YAML. [9054499 primary PDF](https://elearning.unimib.it/pluginfile.php/1491488/mod_resource/content/0/Serrano_1997_Oncogene-induced%20senescence.pdf), SHA256 `55984f837e3fd6519f5c5cc312172332352787c8950f797f865b8e551516848d`: selected Results/Figures2–6 distinguish Ras-induced CKI accumulation from a demonstrated Ras relay. Human IMR90, rat REF52 and broader E1A perturbations are not collapsed into a selective human p16 knockout.

## RNA-capture boundary

The primary study associated with [PMID:22681889](https://pubmed.ncbi.nlm.nih.gov/22681889/) is reproduced in the [author's institutional thesis](https://refubium.fu-berlin.de/bitstream/handle/fub188/9034/Dissertation_Baltz.pdf?sequence=1), SHA256 `9294306a7120ef640de2e435840f94dd1b98eb7e4056032eafa36aec3cef16e8`. TableS1 PDF p.147 was visually checked; class criteria and longest-isoform reduction are described on printed p.70. Literal numeric fields are:

| Gene | Class | L1 log2 FC | H1 log2 FC, label swap | L2 log2 FC | Reported mean log2 FC | log10 iBAQ |
|---|---|---:|---:|---|---:|---:|
| CDKN2A | III | -3.31 | 1.39 | NA | 2.35 | 6.40 |

ClassIII passed the threefold threshold in one of three captures. The sign convention is preserved; negative L1 is not treated as depletion. This is positive CDKN2A gene-level capture. The inspected table lacks accession/unique-peptide evidence resolving P42771 p16 versus Q8N726 ARF; no target-specific CLIP validation or absence of RNA binding is inferred.

## Interaction records and unresolved location

[Exact IntAct records](CDKN2A-interaction-evidence.json) preserve accession pairs, PMIDs, methods, protein/host taxa, mutations, negative flags and resolvable record URLs. [Additional original/curated screen records](CDKN2A-screen-evidence.json) preserve OpenCell p16 metadata, human CDK4/CDK6 associations and the human ORFeome CDKN2A/GMNN Y2H pair. Gene-level ORF and protein-group limits are explicit in the review; shared source records are not independent replication.

The normal PMID:16901784 cache and recovered original records remain abstract-only after bounded full-text attempts. Its positive p16 proliferation/transcription findings do not establish the separate located_in assertion for a senescence-associated heterochromatin focus. That IDA row remains UNDECIDED, without alleging that the curator saw no additional evidence.

Reactome [R-HSA-182594](https://reactome.org/content/detail/R-HSA-182594) was inspected through its authentic machine API: INK4 and CDK4/CDK6 inputs and their output complex are assigned to cytosol. Raw response SHA256 `de45b5fd8ec389929c287483e99d6166a5a6bd2b5f844c8ff93ae45a547300b7`. This supports the cytosolic regulatory context separately from staining alone.
