# GDAP1: selected original evidence

This page records source and construct limits behind the annotation reasons. Original raw contexts, dataset row locators and the qualified source manifest are retained in [the compact archive](GDAP1-context-archive.json); current counts and exact excerpts are in [source evidence](GDAP1-source-evidence.yaml). The [source guide](GDAP1-source-guide.md) records access scope and the PANTHER sources.

## Membrane dynamics

[PMID:16172208](https://doi.org/10.1083/jcb.200507087), selected Results/Methods: mouse constructs and endogenous assays support outer-membrane topology and fission. A human host cell does not change the construct species. [PMID:21753178](https://pubmed.ncbi.nlm.nih.gov/21753178/), Methods, fusion Results and Figure 3 caption: dominant human variants impair fusion; this does not by itself identify normal GDAP1 as performing membrane merger. Neither paper's figure pixels or supplements were inspected.

[PMID:23628762](https://pubmed.ncbi.nlm.nih.gov/23628762/), selected main Results/Methods and Figure 3/4 captions: GDAP1 depletion elongates peroxisomes; re-expression rescues, with HD1 integrity and Drp1/Mff dependence. These results support participation in peroxisomal fission, beyond necessity alone. Mouse N1E115 and transient-cell experiments remain distinct; the wild-type rescue construct's species is unresolved in the inspected text. This cellular evidence is unaffected by the separate liposome translation-mixture limitation. No autonomous GDAP1 scission activity is required for participation.

## Construct-dependent biochemical evidence

[PMID:27841286](https://doi.org/10.1038/srep36930), original Results, Methods and Table 1: human Sf21-derived T288X conjugates glutathione to selected model substrates, while T318X does not under the tested conditions. Reticulocyte-translated full-length protein deforms mitochondrial/peroxisomal lipid-mixture liposomes, unlike pure phosphatidylcholine, with HD1scr, T288X and untreated controls. This is translation mixture, not purified full-length reagent, and deformation is not completed scission. Exact wild-type reagent species/sequence and catalytic coupling remain unresolved. These are engineered proteins, distinct from the two natural products.

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

## Locally checkable partner-class excerpts

The following short source excerpts establish partner class; the interaction sources remain HuRI (two refined pairs) and Haenig (15 refined pairs). They do not establish native colocalization or a physiological consequence. UniProt excerpts come from curated FUNCTION, SIMILARITY or CATALYTIC ACTIVITY text, never DR GO lines. Source hashes and exact local offsets are recorded in [source evidence](GDAP1-source-evidence.yaml). The retained official response SHA256 is `8cf7d5b6c1682abb64c51c4ced8b36cc0d53df77e32fa514ba7bbbcb88de4b21`. UniProt pointers below are relative to each linked accession record; the ledger also retains the original query pointers and exact evidence arrays. Experimental attribution describes UniProt curation, not a new reading of every cited assay. Isoform and clone limits in the interaction table remain unchanged.

| Native index | Source | Selected source location | Exact short excerpt | Evidence attribution |
|---|---|---|---|---|
| 3 | ABHD16A / [O95870](https://rest.uniprot.org/uniprotkb/O95870.json) | FUNCTION; `/comments/0/texts/0/value` | “Also has monoacylglycerol lipase activity” | ECO:0000269 / PMID:25290914; mixed paragraph |
| 5 | CLCN7 / [P51798](https://rest.uniprot.org/uniprotkb/P51798.json) | FUNCTION; `/comments/0/texts/0/value` | “exchange of chloride ions against protons” | ECO:0000269 / PMID:18449189,21527911; mixed paragraph |
| 11 | BIRC5 / [O15392](https://rest.uniprot.org/uniprotkb/O15392.json) | FUNCTION; `/comments/0/texts/0/value` | “participates in the organization of the center spindle” | ECO:0000269 / PMID:20826784 |
| 14 | HOXC4 / [P09017](https://rest.uniprot.org/uniprotkb/P09017.json) | FUNCTION; `/comments/0/texts/0/value` | “Sequence-specific transcription factor” | Curated text; no per-field ECO supplied |
| 15 | PIK3R1 / [P27986](https://rest.uniprot.org/uniprotkb/P27986.json) | SIMILARITY; `/comments/17/texts/0/value` | “Belongs to the PI3K p85 subunit family” | ECO:0000305; curated family membership |
| 16 | TAGLN2 / [PMID:25869671](https://pmc.ncbi.nlm.nih.gov/articles/PMC4395477/) | Results, TAGLN2 actin-association subsection; XML paragraph 13 | “TAGLN2 associates with F-actin” | Selected original Results/Methods; ECO not applicable |
| 17 | ATXN3 / [P54252](https://rest.uniprot.org/uniprotkb/P54252.json) | FUNCTION; `/comments/0/texts/0/value` | “Deubiquitinating enzyme involved in protein homeostasis maintenance” | ECO:0000269; publication-backed paragraph |
| 21 | CLPP / [Q16740](https://rest.uniprot.org/uniprotkb/Q16740.json) | FUNCTION; `/comments/0/texts/0/value` | “Protease component of the ClpXP complex that cleaves peptides” | ECO:0000269; publication-backed paragraph |
| 25 | FOXR1 / [Q6PIV2](https://rest.uniprot.org/uniprotkb/Q6PIV2.json) | FUNCTION; `/comments/0/texts/0/value` | “Transcription factor which acts as both an activator and a repressor” | ECO:0000269 / PMID:34723967; mixed paragraph |
| 28 | ZDHHC17 / [Q8IUH5](https://rest.uniprot.org/uniprotkb/Q8IUH5.json) | FUNCTION; `/comments/0/texts/0/value` | “Palmitoyltransferase that catalyzes the addition of palmitate” | ECO:0000269; publication-backed selected claim |
| 29 | IQUB / [Q8NA54](https://rest.uniprot.org/uniprotkb/Q8NA54.json) | FUNCTION; `/comments/0/texts/0/value` | “Adapter protein that anchors the radial spoke 1 (RS1) complex” | ECO:0000269 / PMID:36355624; mixed paragraph |
| 32 | OPTN / [Q96CV9](https://rest.uniprot.org/uniprotkb/Q96CV9.json) | FUNCTION; `/comments/0/texts/0/value` | “Mechanistically, recruits TBK1 at the Golgi apparatus” | ECO:0000269 / PMID:27538435 |
| 33 | MAP3K5 / [Q99683](https://rest.uniprot.org/uniprotkb/Q99683.json) | FUNCTION; `/comments/0/texts/0/value` | “Serine/threonine kinase which acts as an essential component” | ECO:0000269; publication-backed paragraph |
| 38 | DDX20 / [Q9UHI6](https://rest.uniprot.org/uniprotkb/Q9UHI6.json) | CATALYTIC ACTIVITY; `/comments/1/reaction/name` | “ATP + H2O = ADP + phosphate + H(+)” | ECO:0000269 / PMID:10383418,20510246 |
| 39 | EVL / [Q9UI08](https://rest.uniprot.org/uniprotkb/Q9UI08.json) | FUNCTION; `/comments/0/texts/0/value` | “EVL enhances actin nucleation and polymerization” | Curated text; no per-field ECO supplied |
| 40 | BOK / [PMID:26949185](https://pmc.ncbi.nlm.nih.gov/articles/PMC5018360/) | Results paragraph P29 | “BOK is a pore-forming protein” | Selected original Results/Methods; ECO not applicable |
| 41 | BAIAP2 / [Q9UQB8](https://rest.uniprot.org/uniprotkb/Q9UQB8.json) | FUNCTION; `/comments/0/texts/0/value` | “Necessary for CDC42-mediated reorganization of the actin cytoskeleton” | ECO:0000269; publication-backed paragraph |

[PMID:25869671](https://doi.org/10.1083/jcb.201407130), selected Results and cloning/cosedimentation Methods: human full-length TAGLN2 constructs associate with actin structures, and recombinant His-tagged protein cosediments with F-actin. Mouse endogenous localization is a separate observation. Neither establishes GDAP1 actin activity. Original XML SHA256: `446c2d28c8e7ea1734de802b5e46dec1a31c3354fa94699654bdde3db03c2935`.

[PMID:26949185](https://doi.org/10.1016/j.cell.2016.02.026), Results P28–29 and Methods P40–41: recombinant BOKΔC-8xHIS permeabilizes Ni-coupled large unilamellar vesicles, with lipid-only and total-release controls. Exact recombinant species/sequence is unresolved in the inspected main Methods; human HCT116 loss experiments are separate cellular evidence. No natural full-length human channel preparation or GDAP1 pore activity is inferred. Original HTML SHA256: `9d417a345ec885b2a9d882ce5c48ca8fdd8ef02af059a55e1b9b0a97b760d845`. Neither paper's figure pixels or supplements were inspected.

CLPP's mature matrix location is separated from GDAP1's usual cytosol-facing domain; its assay interaction does not resolve native access. HOXC4's nuclear location similarly leaves native encounter unresolved. FOXR1 has curated cytoplasmic as well as nuclear localization; IQUB's axonemal association is not a demonstrated membrane-separated lumen. No relocalization mechanism is assumed for any pair.

## Location and donor limits

[MitoCoP, PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/), supplementary Table S2 A row404/B row366, identifies the GDAP1 protein group; assay classifications support mitochondrial occurrence and integral association without unique isoform resolution. HPA metadata supports mitochondria plus cytosol; image pixels were not independently read.

Reactome [9603775](https://reactome.org/content/detail/R-HSA-9603775), [9603784](https://reactome.org/content/detail/R-HSA-9603784) and [9603804](https://reactome.org/content/detail/R-HSA-9603804) were traced through every component/member edge to human Q8TB36 residues 1–358: cytosolic entity9603796 and membrane entity9603788. The genuine cached [9603798](https://reactome.org/content/detail/R-HSA-9603798) model summary was also read during native reconciliation; its model-level support is distinct from a new primary experiment.

[PMID:21630459](https://pubmed.ncbi.nlm.nih.gov/21630459/) is an authentic sperm-nucleus proteomics source, but its target-level evidence remains uninspected. The sperm extension is retained. [PMID:25449168](https://pubmed.ncbi.nlm.nih.gov/25449168/) is a genuine rat INS-1 abundance-response source; human regulation and mechanistic participation are not established by that observation.

## Scope of a possible membrane-bending annotation

GO:0180020 is molecular-function membrane bending activity; GO:0097753 is a biological process. The translation-mixture and wild-type reagent limits concern the autonomous membrane-bending assignment from PMID:27841286; they do not weaken the separate cellular peroxisomal-fission evidence. Human OPA1/CHMP2A/CHMP3 show that the MF is used for physical deformation. No GDAP1 GO-CAM entry was found in the inspected index.

## Peroxisomal role and annotation provenance

Peroxisomal fission is supported biologically. PEX11B carries experimental and ancestral GO:0016559 annotations, so there is no inferred GO convention excluding a membrane-remodeling participant. The deferred decision concerns provenance for a new human annotation, not weak or negative biology.

Mitochondrial fission already has a human IDA curator assertion and an inspected PAINT IBD, retained with independent perturbation corroboration. PMID:15772096's abstract does not itself expose the fission assay; it is not presented as direct human evidence independently read here. Retaining that existing assertion is different from creating an experimental assertion. Assigning a new human IMP from the unresolved rescue construct would overstate its inspected provenance. A conserved-role inference would require an explicit inference/source judgment rather than silently relabeling the assay. No NEW is added in this bounded amendment; the positive peroxisomal role remains explicit in the biological description and source assessment.
