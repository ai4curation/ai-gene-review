# GDAP1: selected original evidence

This page records source and construct limits behind the annotation reasons. Original raw contexts, dataset row locators and the qualified source manifest are retained in [the compact archive](GDAP1-context-archive.json); current counts and exact excerpts are in [source evidence](GDAP1-source-evidence.yaml).

## Membrane dynamics

[PMID:16172208](https://doi.org/10.1083/jcb.200507087), selected Results/Methods: mouse constructs and endogenous assays support outer-membrane topology and fission. A human host cell does not change the construct species. [PMID:21753178](https://pubmed.ncbi.nlm.nih.gov/21753178/), Methods, fusion Results and Figure 3 caption: dominant human variants impair fusion; this does not by itself identify normal GDAP1 as performing membrane merger. Neither paper's figure pixels or supplements were inspected.

[PMID:23628762](https://pubmed.ncbi.nlm.nih.gov/23628762/), selected original main text: depletion/rescue and targeting experiments connect GDAP1 to peroxisomal morphology and PEX19 delivery. Mouse neuronal assays are distinguished from transient cell experiments whose construct species is not fully resolved without the supplement. The existing location assertions do not add an import-catalysis annotation to the cargo.

## Construct-dependent biochemical evidence

[PMID:27841286](https://doi.org/10.1038/srep36930), original Results, Methods and Table 1: human Sf21-derived T288X conjugates glutathione to selected model substrates, while T318X does not under the tested conditions. Full-length protein deforms organelle-like liposomes; catalytic coupling was not established. These are engineered proteins, distinct from the two natural products.

[PMID:32274853](https://doi.org/10.1096/fj.202000110R), selected original biochemical and cellular sections: mouse fragments lack detectable glutathione binding by thermal stabilization/calorimetry. Human-protein overexpression in HeLa changes morphology; this is distinct from a native human catalytic assay or an assertion of universal inactivity.

[PMID:42520938](https://doi.org/10.1016/j.jbc.2026.113378), selected original Results and Experimental sections: human soluble protein binds thapsic acid by DSF/MST, with pocket-mutant effects. Pocket closure is modeled, and endogenous ligand identity remains open. Results describe residues 20–316 whereas Methods describe 21–315; the discrepancy is retained. No supplement or figure pixels were inspected for these three papers.

## Interaction evidence and partner classes

[HuRI](https://interactome-atlas.org/data/HuRI.psi), associated with [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), supplies nine pairs, 30 export rows and 29 matching current IntAct rows. Its GDAP1 target is Q8TB36-2, ORF2560, ENST00000434412.2. These literal identifiers do not prove complete clone identity or functional uniqueness; the GOA target stays Q8TB36. The Q96PD2-2 partner/47–789 construct limit is preserved.

[PMID:32814053](https://doi.org/10.1016/j.celrep.2020.108050), supplement mmc3, supplies 32 GDAP1 pairs across NN1.0 and NN1.0ext; these are two network projections, not independent biological replicates. Current IntAct yields 96 matching rows. Gene-level table identity does not settle every product or clone. Independent partner-class records are cited by UniProtKB accession in each annotation. A refined binding class assigns neither the partner's activity nor a physiological consequence to GDAP1. Generic-term removals preserve the positive interactions.

| Raw index | Partner | Original dataset locator | Binding replacement |
|---|---|---|---|
| 0 | TMEM218 / A2RU14 | HuRI lines 65112,111257,140753 | — |
| 1 | ABHD16A / O95870 | HuRI lines 86723,95975,103636 | GO:0035473 |
| 2 | APOD / P05090 | HuRI lines 8692,54503,73125 | — |
| 3 | CLCN7 / P51798 | HuRI lines 63824,120208,168639 | GO:0044325 |
| 4 | PNLIPRP1 / P54315 | HuRI lines 72164,135041,166080 | — |
| 5 | FAM114A1 / Q8IWE2 | HuRI lines 12718,112221,140733 | — |
| 6 | STARD4 / Q96DR4 | HuRI lines 40033,95867,126733 | — |
| 7 | DCBLD2 / Q96PD2-2 | HuRI lines 10940,107174,116189,139967,141300,163294 | — |
| 8 | TMEM14B / Q9NUH8 | HuRI lines 12310,92435,114256 | — |
| 9 | BIRC5 / O15392 | NN1.0 row 3723; NN1.0ext row 8143 | GO:0005519 |
| 10 | MSH5 / O43196-2 | NN1.0 row 3732; NN1.0ext row 8152 | — |
| 11 | SNX2 / O60749 | NN1.0 row 3737; NN1.0ext row 8157 | — |
| 12 | HOXC4 / P09017 | NN1.0 row 3729; NN1.0ext row 8149 | GO:0140297 |
| 13 | PIK3R1 / P27986-2 | NN1.0 row 3734; NN1.0ext row 8154 | GO:0036312 |
| 14 | TAGLN2 / P37802 | NN1.0 row 3738; NN1.0ext row 8158 | GO:0008092 |
| 15 | ATXN3 / P54252 | NN1.0 row 3721; NN1.0ext row 8141 | GO:1990381 |
| 16 | SPACA3 / Q05C28 | NN1.0 row 10189; NN1.0ext row 23055 | — |
| 17 | ZNF638 / Q14966-2 | NN1.0 row 3740; NN1.0ext row 8160 | — |
| 18 | SMN1 (GeneID6606; shared SMN1/SMN2 entry) / Q16637-3 | NN1.0 row 3736; NN1.0ext row 8156 | — |
| 19 | CLPP / Q16740 | NN1.0 row 3726; NN1.0ext row 8146 | GO:0002020 |
| 20 | CEP55 / Q53EZ4 | NN1.0 row 2087; NN1.0ext row 4326 | — |
| 21 | ZNF697 / Q5TEC3 | NN1.0 row 13633; NN1.0ext row 30217 | — |
| 22 | IQSEC1 / Q6DN90-2 | NN1.0 row 3730; NN1.0ext row 8150 | — |
| 23 | FOXR1 / Q6PIV2 | NN1.0 row 3623; NN1.0ext row 7860 | GO:0140297 |
| 24 | SPATA12 / Q7Z6I5 | NN1.0 row 10229; NN1.0ext row 23103 | — |
| 25 | KRTAP8-1 / Q8IUC2 | NN1.0 row 5555; NN1.0ext row 12792 | — |
| 26 | ZDHHC17 / Q8IUH5 | NN1.0 row 3739; NN1.0ext row 8159 | GO:0019899 |
| 27 | IQUB / Q8NA54 | NN1.0 row 4607; NN1.0ext row 10110 | GO:0008092 |
| 28 | VPS37A / Q8NEZ2 | NN1.0 row 12606; NN1.0ext row 28179 | — |
| 29 | MGARP / Q8TDB4 | NN1.0 row 1560; NN1.0ext row 2880 | — |
| 30 | OPTN / Q96CV9-2 | NN1.0 row 3733; NN1.0ext row 8153 | GO:0097110 |
| 31 | MAP3K5 / Q99683 | NN1.0 row 3731; NN1.0ext row 8151 | GO:0019901 |
| 32 | SCAPER / Q9BY12-3 | NN1.0 row 3735; NN1.0ext row 8155 | — |
| 33 | SKIC8 / Q9GZS3 | NN1.0 row 12751; NN1.0ext row 28411 | — |
| 34 | AAMDC / Q9H7C9 | NN1.0 row 3725; NN1.0ext row 8145 | — |
| 35 | DAZ3 / Q9NR90-2 | NN1.0 row 2498; NN1.0ext row 5460 | — |
| 36 | DDX20 / Q9UHI6 | NN1.0 row 3727; NN1.0ext row 8147 | GO:0051117 |
| 37 | EVL / Q9UI08-2 | NN1.0 row 3728; NN1.0ext row 8148 | GO:0005519 |
| 38 | BOK / Q9UMX3 | NN1.0 row 3724; NN1.0ext row 8144 | GO:0044325 |
| 39 | BAIAP2 / Q9UQB8-6 | NN1.0 row 3722; NN1.0ext row 8142 | GO:0005519 |
| 40 | MRFAP1 / Q9Y605 | NN1.0 row 6579; NN1.0ext row 15142 | — |

## Location and donor limits

[MitoCoP, PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/), supplementary Table S2 A row404/B row366, identifies the GDAP1 protein group; assay classifications support mitochondrial occurrence and integral association without unique isoform resolution. HPA metadata supports mitochondria plus cytosol; image pixels were not independently read.

Reactome [9603775](https://reactome.org/content/detail/R-HSA-9603775), [9603784](https://reactome.org/content/detail/R-HSA-9603784) and [9603804](https://reactome.org/content/detail/R-HSA-9603804) were traced through every component/member edge to human Q8TB36 residues 1–358: cytosolic entity9603796 and membrane entity9603788. Additional9603798 remains unverified pending genuine native retrieval.

[PMID:21630459](https://pubmed.ncbi.nlm.nih.gov/21630459/) is an authentic sperm-nucleus proteomics source, but its target-level evidence remains uninspected. The sperm extension is retained. [PMID:25449168](https://pubmed.ncbi.nlm.nih.gov/25449168/) is a genuine rat INS-1 abundance-response source; human regulation and mechanistic participation are not established by that observation.
