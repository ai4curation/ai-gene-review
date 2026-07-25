# GLIPR1L1 review notes

## 2026-07-18 — data retrieval and research boundary

- `just fetch-gene human GLIPR1L1` retrieved UniProt Q6UWM5 and 12 current GOA rows.
- `just fetch-gene-pmids human GLIPR1L1` found no PMID-backed rows in the seeded GOA; all 12 source rows use GO references.
- The configured Falcon/Edison deep-research request failed with HTTP 402, and the `perplexity-lite` fallback failed with HTTP 401 (quota exceeded). No provider-named deep-research file was created. The manual synthesis is recorded in `GLIPR1L1-deep-research-manual.md`.

## Direct human evidence

- The original human study identified two splice isoforms and testis-specific expression. [PMID:16714093 Identification and characterization of RTVP1/GLIPR1-like genes, a novel p53 target gene cluster, "GLIPR1L1 is testis-specific"]
- UniProt Q6UWM5 describes a 242-aa CAP/CRISP-family precursor with a cleaved signal peptide (residues 1–22), a predicted GPI anchor at residue 221, one predicted N-linked glycosylation site, and two splice isoforms. The fertilization function and most subcellular locations are explicitly transferred from mouse Q9DAG6 or bovine Q32LB5 rather than measured in human.
- A recent cross-species expression analysis reports high expression of Glipr1l1/GLIPR1L1 in mouse and human testis and epididymis. [PMID:40572022 Mouse genome engineering uncovers 18 genes dispensable for male reproduction, "Glipr1l1, Glipr1l2, Izumo4, Slc22a16, Spmip2, Tex51, Tmco2, Triml1, and Triml2 are highly expressed in mouse and human testis and epididymis"]

## Ortholog evidence defining the functional model

- In mouse, GLIPR1L1 is testis enriched, glycosylated during spermatogenesis, and localizes to the sperm connecting piece and, after capacitation, anterior sperm head. [PMID:20219979 Glioma pathogenesis-related 1-like 1 is testis enriched, dynamically modified, and redistributed during male germ cell maturation and has a potential role in sperm-oocyte binding, "After sperm capacitation, however, GLIPR1L1 is also localized to the anterior regions of the sperm head."]
- The 2019 mouse study identified GLIPR1L1 in high-molecular-weight oolemma-binding complexes with IZUMO1 and confirmed the interaction by reciprocal immunoprecipitation. [PMID:31672133 GLIPR1L1 is an IZUMO-binding protein required for optimal fertilization in the mouse, "Collectively, these results confirm that IZUMO1 and GLIPR1L1 form a protein complex within male germ cells"]
- GLIPR1L1 and IZUMO1 colocalize with the GM1 raft marker in live capacitated mouse sperm. [PMID:31672133, "Both proteins displayed strong colocalization with GM1 gangliosides in the peri-acrosomal region of the head of capacitated spermatozoa"]
- Mouse Glipr1l1 knockout reduced progesterone-induced acrosome reaction and strongly attenuated IZUMO1 redistribution after the acrosome reaction. [PMID:31672133, "IZUMO1 was relocated throughout the sperm head in 85% of sperm, compared to 21% of acrosome-reacted Glipr1l1−/− sperm"]
- Knockout sperm bound the zona pellucida normally but produced fewer two-cell embryos in vitro, placing the defect after zona binding and near sperm–oocyte fusion. [PMID:31672133, "the loss of Glipr1l1 did not affect the ability of sperm to bind to the zona pellucida, but did significantly reduced their ability to fertilize oocytes"]
- Bovine GLIPR1L1 is a GPI-anchored sperm plasma-membrane and lipid-raft protein; anti-GLIPR1L1 reduced sperm–zona interaction. [PMID:22552861 Bovine sperm raft membrane associated Glioma Pathogenesis-Related 1-like protein 1 (GliPr1L1) is modified during the epididymal transit and is potentially involved in sperm binding to the zona pellucida, "GliPr1L1 is glycosyl phosphatidyl inositol (GPI) anchored to caput and cauda spermatozoa"]
- Bovine GLIPR1L1 is also present in a CD9-positive epididymosome subpopulation, but the acquisition route is species dependent: mouse GLIPR1L1 is acquired during spermatogenesis rather than from epididymosomes. [PMID:23785420 CD9-positive microvesicles mediate the transfer of molecules to Bovine Spermatozoa during epididymal maturation, "P25b, GliPr1L1, and MIF were highly expressed in CD9-positive microvesicles"]

## Important negative/caveat evidence

- The 2019 single-gene knockout did not reduce litter size after natural mating, despite its acrosome-reaction and IVF phenotypes. [PMID:31672133, "Glipr1l1 knockout males sired litters of equivalent size to that of WT control males"]
- A newer 10-kb deletion removing mouse Glipr1l1, Glipr1l2, and Glipr1l3 likewise produced normal litter size, testis/epididymis histology, sperm morphology, and motility. [PMID:40572022, "depletion of all three genes does not significantly affect male fertility"]
- These findings do not refute a modulatory role in acrosome remodeling or optimal in-vitro fertilization because the triple-knockout study did not repeat the acrosome-reaction, IZUMO1-redistribution, or IVF assays. They do show that GLIPR1L1 is not an essential standalone fusogen or an indispensable determinant of male fecundity under standard mouse mating conditions.
- The 2019 paper explicitly states that the precise molecular function remains unresolved; `molecular adaptor activity` is therefore the most defensible current MF term, based on complex membership, direct IZUMO1 interaction, and GLIPR1L1-dependent IZUMO1 redistribution. It should not be upgraded to fusogen activity.

## Annotation-review conclusions

- Accept the two IBA annotations. The broad extracellular localization is consistent with a signal peptide/GPI anchor and direct ortholog data; molecular adaptor activity captures the supported nonenzymatic role without asserting direct fusogenicity.
- Accept the acrosomal vesicle, plasma membrane, membrane raft, and extracellular-region mappings. These are concordant across sequence features, mouse experiments, and bovine experiments.
- Accept the inferred sperm–egg membrane-fusion process and adhesion-complex annotations, but state that the role is optimizing rather than essential.
- Add `GO:0060476 protein localization involved in acrosome reaction` by orthology because the mouse loss-of-function experiment directly establishes defective IZUMO1 redistribution.
- Add `GO:0120212 sperm head-tail coupling apparatus` by orthology because two mouse studies localize GLIPR1L1 to the connecting piece; this is an ancillary location and not a second core molecular activity.
- Do not add sperm–zona binding as a core function: antibody-based mouse/bovine studies suggested it, but the 2019 knockout did not significantly reduce zona binding.
- Do not add epididymosome/extracellular-vesicle location for human: bovine evidence is strong, but the acquisition mechanism is explicitly species variable and has not been shown in human.

