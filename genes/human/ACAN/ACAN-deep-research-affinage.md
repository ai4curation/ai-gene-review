---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACAN
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: P16112
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 16
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACAN (human)

## Current model (mechanistic narrative)

ACAN encodes aggrecan, a large extracellular matrix proteoglycan that anchors into cartilage matrix and into CNS perineuronal nets (PNNs) through its N-terminal G1 region, whose immunoglobulin domain and tandem Link modules form a single structural unit that clamps a hyaluronan decasaccharide within a continuous binding groove; mutation of this glycosaminoglycan-binding site abolishes hyaluronan binding yet only partially reduces PNN incorporation, showing that hyaluronan binding contributes to but is not strictly required for PNN integration. At the C-terminus, integrity of the G3 domain C-type lectin repeat is required for efficient aggrecan secretion and for binding to cartilage matrix ligands, and missense variants there reduce both [PMID:35338222]. ACAN transcription in chondrocytes is driven by SOX9 cooperating with the SOX trio, a step gated upstream by TET1-mediated 5hmC deposition at chondrocyte-specific SOX9 sites that licenses SOX9 occupancy [PMID:33134768] and by SIRT1 deacetylation of SOX9, which promotes its importin-β-dependent nuclear entry and binding to a -10 kb ACAN enhancer [PMID:26910618]; SHOX2 contributes by physically partnering with SOX5/SOX6 to transactivate ACAN regulatory elements [PMID:24421874], and the locus carries at least eleven evolutionarily conserved, partly SOX9-independent enhancers [PMID:22820679]. ACAN output is further tuned post-transcriptionally by miR-140 acting through RALA and translationally by the mTOR/4E-BP1/eIF4E axis coupled to Smad signaling [PMID:24063364, PMID:32485037]. Loss-of-function mutations — nonsense/frameshift and aberrant-splicing alleles triggering nonsense-mediated decay, and locus-disrupting rearrangements — produce ACAN haploinsufficiency that causes chondrodysplasia and proportionate short stature [PMID:17952705, PMID:38782218, PMID:29302920]. In the CNS, aggrecan-containing PNNs serve cell-type-specific roles: deletion from CA2 pyramidal neurons impairs social memory and reversal learning while deletion from PV interneurons impairs contextual fear memory, and HDAC2 in PV+ cells sustains Acan expression to gate PNN aggregation and fear-memory extinction [PMID:37131076].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008289 lipid binding
- **localization:** GO:0031012 extracellular matrix, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1474244 Extracellular matrix organization, R-HSA-1266738 Developmental Biology, R-HSA-112316 Neuronal System
- **partners:** HA, SOX5, SOX6, MAPT
- **complexes:** perineuronal net

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | High | The N-terminal G1 region of ACAN (aggrecan) was co-crystallized with a hyaluronan (HA) decasaccharide, revealing that the single immunoglobulin domain and two Link modules form a single structural unit, and that HA is clamped inside a groove spanning the length of the tandem Link domains. Point mutations introduced into the glycosaminoglycan-binding site eliminated HA-binding activity in ACAN but only decreased (not abolished) its integration into perineuronal nets (PNNs), demonstrating that HA-binding is important but not essential for ACAN incorporation into PNNs. | — | bioRxiv |
| 2016 | High | SOX9 acetylation reduces its nuclear entry and its ability to transactivate the ACAN gene. SIRT1 deacetylates SOX9 (co-immunoprecipitated with SOX9 in 3D chondrocyte cultures), promoting SOX9 nuclear translocation via importin β, which then enhances SOX9 binding to a -10 kb ACAN enhancer and increases ACAN mRNA. Inhibition of importin β by importazole kept SOX9 cytoplasmic even after SIRT1 activation, placing importin β downstream of SIRT1-mediated deacetylation in this pathway. | PMID:26910618 | Aging cell |
| 2014 | Medium | SHOX2 activates ACAN transcription not directly but through cooperation with the SOX trio (SOX5, SOX6, SOX9): SHOX2 protein physically interacts with SOX5 and SOX6 (demonstrated by yeast-two-hybrid and co-immunoprecipitation), and this interaction is required for ACAN promoter/enhancer transactivation as shown by luciferase reporter assay. | PMID:24421874 | PloS one |
| 2020 | High | TET1-mediated deposition of 5-hydroxymethylcytosine (5hmC) at chondrocyte-specific class II SOX9-binding sites on the Col2a1 and Acan loci is required for SOX9 occupancy at these loci. Knockdown of Tet1 in ATDC5 chondroprogenitors blocked chondrogenic differentiation, and SOX9 could not bind Acan or Col2a1 regulatory regions despite unchanged SOX9 protein levels, placing TET1-mediated DNA demethylation upstream of SOX9 target-gene activation. | PMID:33134768 | JBMR plus |
| 2020 | Medium | 4E-BP1, a translational repressor, regulates ACAN and collagen type II expression in chondrocytes through two mechanisms: (1) mTOR phosphorylates 4E-BP1 to relieve its inhibition of eIF4E, allowing TGF-β1-induced protein synthesis including ACAN; (2) 4E-BP1 itself controls translation of inhibitory Smads (Smad6/7), which in turn modulate nuclear accumulation of the Smad2/3 complex on the ACAN promoter, thereby affecting ACAN transcription. mTOR silencing suppressed TGF-β1-induced ACAN/Col II via decreased 4E-BP1 phosphorylation; 4E-BP1 knockdown paradoxically reduced ACAN/Col II by increasing inhibitory Smads. | PMID:32485037 | FASEB journal |
| 2013 | Medium | miR-140 promotes ACAN protein expression in chondrocytes post-transcriptionally (translational enhancement): inhibition of miR-140 in differentiating MSCs reduced SOX9 and aggrecan protein without changing their mRNA levels. RALA (a small GTPase) was identified as a direct target of miR-140; RALA knockdown rescued SOX9 protein levels, placing RALA downstream of miR-140 in this regulatory axis controlling ACAN. | PMID:24063364 | Stem cells and development |
| 2012 | Medium | Multiple transcriptional enhancers (at least eleven) distributed from >100 kb upstream of ACAN to within the first intron are independently capable of directing reporter gene expression to cartilage in transgenic zebrafish. Six of these enhancers have clear orthologs at the chicken ACAN locus that are also functional in zebrafish, demonstrating deep evolutionary conservation of this redundant transcriptional regulatory architecture. Several enhancers lack SOX9 consensus binding sites, implicating additional transcription factors beyond the SOX9 pathway in ACAN regulation. | PMID:22820679 | Matrix biology |
| 2007 | High | A 4-bp insertion in exon 11 of ACAN (2266_2267insGGCA) causes bulldog dwarfism (chondrodysplasia) in Dexter cattle. In heterozygous chondrocytes, the mutant ACAN mRNA is subject to nonsense-mediated decay, retaining only ~8% of normal expression, establishing haploinsufficiency as the mechanism underlying the heterozygous short-limbed phenotype. | PMID:17952705 | Mammalian genome |
| 2022 | High | Missense ACAN variants in the C-type lectin repeat of the G3 domain (from families with hereditary osteochondritis dissecans) result in reduced secretion of both recombinant variant proteins and full-length variant aggrecan from heterozygous patient cartilage, and in decreased binding of the variant proteins to known cartilage extracellular matrix ligands, establishing that G3 domain integrity is required for proper aggrecan secretion and matrix interactions. | PMID:35338222 | Scientific reports |
| 2020 | Medium | In a bigenic TauP301L-Acan mouse model, reduced aggrecan protein levels (from heterozygous Acan deletion) were accompanied by increased total tau protein levels and reduced numbers of Tau-1-positive neurons (indicating increased tau phosphorylation) in the brainstem, demonstrating a correlation between aggrecan abundance and tau expression/phosphorylation. However, aggrecan had no significant impact on tau aggregation. | PMID:32737917 | European journal of neuroscience |
| 2022 | Medium | Co-immunoprecipitation in a TauP301L-Acan mouse model revealed a physical interaction between perineuronal net (PN) components (including aggrecan) and tau protein. Additionally, tau modulates protein levels of other PN components such as brevican, and changes in PN composition are accompanied by altered expression of protein phosphatase 2A. | PMID:35454094 | Biomolecules |
| 2023 | High | PV+ cell-specific deletion of Hdac2 reduces Acan expression in prefrontal cortex PV+ cells and decreases perineuronal net aggregation, which correlates with enhanced PV+ cell bouton remodeling and reduced spontaneous fear memory recovery after extinction training. Re-expression of Hdac2 in Hdac2-KO PV+ cells rescued Acan expression. siRNA-mediated knockdown of Acan alone before extinction training was sufficient to reduce spontaneous fear memory recovery in wild-type mice, placing Acan downstream of Hdac2 in this plasticity pathway. | PMID:37131076 | Molecular psychiatry |
| 2024 | High | Conditional deletion of Acan from CA2 pyramidal neurons (Amigo2-Acan KO), but not from PV interneurons (PV-Acan KO), impaired social memory and reversal learning in mice. Amigo2-Acan KO also reduced supramammillary nucleus input to CA2 and eliminated a social novelty-related local field potential response. Conversely, PV-Acan KO impaired contextual fear memory. This establishes cell-type-specific roles for aggrecan-containing PNNs in distinct forms of hippocampal-dependent memory. | — | bioRxiv |
| 2024 | Medium | A non-canonical splicing variant in intron 4 of ACAN (c.630-13G>A) creates a novel splice acceptor site, inserting an 11 bp intronic sequence into the transcript, causing a frameshift and premature termination codon, establishing loss of aggrecan protein function as the mechanism of short stature in the affected pedigree. | PMID:38782218 | Gene |
| 2018 | Medium | A balanced reciprocal translocation t(10;15)(q22.3;q26.1) that disrupts ACAN at intron 1 decreases ACAN transcriptional expression (measured by RT-PCR), establishing that ACAN haploinsufficiency caused by a chromosomal rearrangement leads to autosomal dominant proportionate short stature. | PMID:29302920 | Journal of endocrinological investigation |
| 2023 | Low | Downregulation of ACAN in ATDC5 chondrocyte cells inhibited cell proliferation induced by growth hormone (GH), and bioinformatic analysis showed strong association between ACAN and the GH signaling pathway. ACAN does not affect GH receptor (GHR) levels but regulates the cellular response to GH, placing ACAN downstream of GHR in the GH signaling axis. | PMID:36597844 | Journal of clinical laboratory analysis |

## Citations

- PMID:17952705
- PMID:22820679
- PMID:24063364
- PMID:24421874
- PMID:26910618
- PMID:29302920
- PMID:32485037
- PMID:32737917
- PMID:33134768
- PMID:35338222
- PMID:35454094
- PMID:36597844
- PMID:37131076
- PMID:38782218
