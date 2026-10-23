# DGKE source guide

Normal publication caches and separately recovered original passages retain distinct access states. Abstract-only flags are unchanged. Selected passage reading does not imply exhaustive supplementary-file or figure-pixel inspection.

| Source | Actual evidence read | Scope and limitation |
| --- | --- | --- |
| [8626589](https://pubmed.ncbi.nlm.nih.gov/8626589/) | Original PDF, Methods p.10238 and Results/Figure 3 pp.10239–10240 | Human endothelial cDNA/COS-7 assays; cDNA truncation removes untranslated sequence, not protein sequence. Normal cache abstract-only. |
| [19744926](https://doi.org/10.1074/jbc.M109.050617) | Original PDF, Methods pp.31064–31065, Results pp.31067–31071, Discussion pp.31071–31072 | Human full-length/engineered Δ58 and separate mouse knockout lipidomics; enriched lysates, no sn-position assignment. Normal cache abstract-only. |
| [21477596](https://pmc.ncbi.nlm.nih.gov/articles/PMC3095698/) | Full-cache selected Methods/Results, DGKE constructs, preparation and activity | Human FLAG-DGKE/mutants in COS-7 extracts; PIP5Kalpha is a separate enzyme. |
| [22108654](https://pmc.ncbi.nlm.nih.gov/articles/PMC3237191/) | Full-cache selected Methods/Results, substrate panel/Figure 1/Table 1 discussion | Human His6-DGKE in Sf21 extracts; sn-2 selectivity stronger than sn-1. |
| [18004883](https://doi.org/10.1021/bi701584v) | Author-repository original, Methods/Results pp.14227–14230, Table 1/Figure 5 | Human His6-DGKE in Sf21 extracts with mock/no-enzyme controls; possible substrate-isomer contamination. Normal cache abstract-only. |
| [23542698](https://pmc.ncbi.nlm.nih.gov/articles/PMC3719402/) | Methods/Results including Figure 4b | Endogenous human platelet membrane/cytoplasmic fractionation; rat and human tissue data distinguished; no unique membrane compartment. |
| [23274426](https://pmc.ncbi.nlm.nih.gov/articles/PMC3582208/) | Human constructs, knockdown and M3/TRPC6 Methods/Results | Receptor-driven currents are a DAG-sensitive readout, not direct DAG concentration. |
| [11287665](https://pmc.ncbi.nlm.nih.gov/articles/PMC31904/) | Mouse cloning/knockout, electrophysiology and lipid-signaling Methods/Results | Perforant path–dentate granule synaptic potentiation; no direct protein localization. Normal cache abstract-only. |
| [15544348](https://pubmed.ncbi.nlm.nih.gov/15544348/) | Complete abstract | Explicit epsilon experiment despite alpha-focused title; full Methods unavailable. |
| [23949095](https://pubmed.ncbi.nlm.nih.gov/23949095/) | Complete abstract | Epsilon in ten-isozyme activity comparison; species/construct details unavailable. |
| [19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) | Complete abstract and bibliographic identity | YTS membrane proteomics; target peptide/table evidence unavailable. Broad membrane annotation retained on curator deference and independent human platelet evidence; this particular target-table identification was not verified. |

The [UniProt P52429 record](https://www.uniprot.org/uniprotkb/P52429/entry) and all-isoform sequences identify products of 567 and 177 residues. Sequence features were reconstructed independently. The natural short product is distinct from UTR-deleted cDNA and engineered Δ58 proteins. Retaining or losing a domain is not an experimental activity measurement.

The [HPA subcellular record](https://www.proteinatlas.org/ENSG00000153933-DGKE/subcellular) identifies cytosol/nucleoplasm staining. Only the existing cytosol assertion and its supported broad-term refinements are used. The PAINT reconstruction uses the actual PTHR11255 target lineage and root IBD PTN007499105; literal experimental donor records are distinguished from inferred transfer.

[Reactome R-HSA-426240](https://reactome.org/content/detail/R-HSA-426240) represents DAG phosphorylation. [Catalyst 426239](https://reactome.org/ContentService/data/query/426239) → [set 426070](https://reactome.org/ContentService/data/query/426070) → [DGKE member 426061](https://reactome.org/ContentService/data/query/426061) identifies human P52429 residues 1–567 at plasma membrane. The [platelet pathway R-HSA-76002](https://reactome.org/content/detail/R-HSA-76002) reaches that reaction through [DAG/IP3 signaling 114508](https://reactome.org/ContentService/data/query/R-HSA-114508). This establishes the curated pathway role but not an independently localized native organelle or a selective platelet-activation mechanism.

Short exact publication anchors occur once each across YAML and notes. The four-paper original locators and assay/product limits are described in the [review notes](DGKE-notes.md). There is one catalytic core and no new annotation; general lipid-phosphorylation and DAG-metabolism annotations describe its reaction rather than separate biochemical activities.
