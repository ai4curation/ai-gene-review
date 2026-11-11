---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACBD6
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q9BR61
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACBD6 (human)

## Current model (mechanistic narrative)

ACBD6 is a dual-function acyl-CoA-binding protein that couples acyl-CoA sequestration to the regulation of protein N-myristoylation and membrane lipid remodeling [PMID:26621918, PMID:36551154]. Its ankyrin-repeat (ANK) domain is necessary and sufficient for direct interaction with N-myristoyltransferases NMT1 and NMT2, stimulating their catalytic activity and protecting them from competitive inhibition by abundant acyl-CoAs such as palmitoyl-CoA; the acyl-CoA-binding (ACB) domain is dispensable for this protection but acts as a positive allosteric effector when loaded with acyl-CoA, and grafting the ANK module onto ACBD1 confers NMT-stimulatory activity to the chimera [PMID:26621918, PMID:32108178]. Phosphorylation of two serine residues in the ACB domain enhances ligand binding and further potentiates NMT stimulation [PMID:30642881]. In parallel, the ACB domain binds acyl-CoAs of 6–20 carbons and transfers them to lysophospholipid acyltransferases (e.g. LPCAT1), making it rate-limiting for conversion of lysophosphatidylcholine into phosphatidylcholine [PMID:26290611]. Consistent with these two activities, ACBD6 knockout reduces protein N-myristoylation—without affecting palmitoylation or acyl-CoA synthesis—and diminishes lipid acylation and lipid droplet content [PMID:36551154]. Bi-allelic loss-of-function ACBD6 variants cause a human neurodevelopmental syndrome with movement disorders, with broad impairment of co- and post-translational N-myristoylation in patient fibroblasts and acbd6-deficient zebrafish and Xenopus models [PMID:32108178, PMID:37951597].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008289 lipid binding, GO:0140313 molecular sequestering activity
- **localization:** GO:0005811 lipid droplet, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1430728 Metabolism
- **partners:** NMT1, NMT2, LPCAT1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | Medium | ACBD6 binds acyl-CoAs of chain length 6–20 carbons with non-1:1 stoichiometry; saturation by C16:0-CoA requires higher concentration than less abundant acyl-CoAs; unlike ACBD1 and ACBD3, ligand binding does not cause ACBD6 dimerization. ACBD6 negatively affects phosphatidylcholine (PC) and phosphatidylethanolamine formation in red blood cell membranes, and the acylation rate of lysophosphatidylcholine into PC by LPCAT1 is limited by transfer of acyl-CoA substrate from ACBD6 to the acyltransferase. | PMID:26290611 | Journal of lipid research |
| 2015 | High | ACBD6 stimulates the N-myristoyltransferase (NMT2) reaction; this stimulation requires direct protein–protein interaction between ACBD6 and NMT2 and is enhanced by ACBD6 binding to C18:2-CoA. ACBD6 also prevents competition of the NMT reaction by the abundant palmitoyl-CoA (C16:0-CoA). ACBD6 mutants deficient in either ligand binding (N-terminal ACBD domain) or NMT2 interaction fail to stimulate NMT2 or protect it from C16:0-CoA competition. ACBD6 also interacts with NMT1. | PMID:26621918 | Journal of lipid research |
| 2015 | Medium | During Chlamydia trachomatis infection, human ACBD6 is recruited to cytosolic lipid droplets (LDs) and translocated into the bacterial inclusion. ACBD6 modulates the activity of bacterial acyltransferase CT775 in an acyl-CoA-dependent fashion, buffering acyl-CoA concentrations to sustain CT775 activity for remodeling of host phosphatidylcholine into bacterial lipids. | PMID:25604091 | MicrobiologyOpen |
| 2019 | Medium | ACBD6 supports N-myristoyltransferase (NMT) activity in mammalian cells and in the intracellular parasite Plasmodium. Phosphorylation of two serine residues within the acyl-CoA binding domain of human ACBD6 improves ligand binding capacity, prevents competition by unbound acyl-CoAs, and further enhances NMT activity. A Plasmodium ACBD6 homologue similarly regulates Plasmodium NMT enzymes and protects them from lauryl-CoA competition. | PMID:30642881 | Journal of lipid research |
| 2020 | High | The ankyrin-repeat (ANK) domain of ACBD6 is necessary and sufficient for interaction with NMT2 and for protection of NMT2 from competitive acyl-CoAs; the acyl-CoA binding domain (ACB) is dispensable for protection but acts as a positive allosteric effector when loaded with acyl-CoA. Fusion of the ANK module onto ACBD1 was sufficient to confer NMT-stimulatory properties to the chimera. Fibroblasts from two individuals with homozygous loss-of-function ACBD6 mutations showed deficient protein N-myristoylation and increased sensitivity to NMT substrate analogue competitors. | PMID:32108178 | PloS one |
| 2022 | High | In ACBD6 knockout cells, myristoylation of proteins is significantly reduced and cells show increased sensitivity to NMT competitor substrate analogs, while palmitoylation is not altered, confirming the specific requirement of the ACBD6/NMT complex for myristoyltransferase activity. Additionally, lipid acylation (PC formation from LPC by LPCAT enzymes) is significantly reduced in ACBD6 KO cells, resulting in reduced lipid droplet content, while acyl-CoA formation itself is unaffected. ACBD6 does not show peroxisomal localization (unlike ACBD5). | PMID:36551154 | Biomolecules |
| 2024 | High | Bi-allelic loss-of-function ACBD6 variants in humans cause a neurodevelopmental syndrome with movement disorders. In patient-derived fibroblasts, significant differences in N-myristoylation were observed for 68 co- and 18 post-translationally N-myristoylated proteins by chemical proteomics (YnMyr labeling). N-myristoylation was similarly impaired in acbd6-deficient zebrafish and Xenopus tropicalis CRISPR/Cas9 knockout models, affecting proteins including Fus, Marcks, and Chchd-related proteins implicated in neurological diseases. ACBD6 does not localize to peroxisomes and ACBD6 deficiency does not alter peroxisomal parameters in patient fibroblasts. | PMID:37951597 | Brain : a journal of neurology |

## Citations

- PMID:25604091
- PMID:26290611
- PMID:26621918
- PMID:30642881
- PMID:32108178
- PMID:36551154
- PMID:37951597
