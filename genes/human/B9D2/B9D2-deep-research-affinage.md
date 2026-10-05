---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/B9D2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9BPU9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 13
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for B9D2 (human)

## Current model (mechanistic narrative)

B9D2 is a conserved ciliary transition zone protein that, together with MKS1 and B9D1, forms the B9 protein complex governing the assembly and gating function of the ciliary base [PMID:21763481, PMID:18337471, PMID:32726168]. The complex is organized as MKS1–B9D2–B9D1, with B9D2 and MKS1 localizing to the transition zone interdependently through the B9 domain of MKS1, and intact complex formation is essential for establishing a diffusion barrier that restricts the lateral movement of ciliary membrane proteins [PMID:32726168, PMID:33193692]. B9D2 anchors TMEM67 to the transition zone membrane, and disruption of this B9–TMEM67 module deregulates tubulin-modifying enzymes and reduces post-translational modifications (acetylation, glutamylation) of axonemal microtubules; B9 proteins also localize to centrioles before ciliogenesis to facilitate its initiation [PMID:41165761]. B9D2 contributes to selective ciliary cargo transport by binding IFT particle components (IFT88) and supporting ciliary localization of Inversin and the cargo Opsin [PMID:21602787], and it operates within an interconnected transition zone network that genetically and functionally interacts with the nephrocystin (NPHP) module and other MKS components such as TMEM216 [PMID:18337471, PMID:22152675, PMID:33234550, PMID:21546380]. Beyond cilia, B9D2 localizes to tight junctions prior to ciliogenesis and is required for epithelial barrier integrity and biliary lumen formation [PMID:39455645]. B9D2 variants cause ciliopathies: Joubert syndrome–associated variants primarily impair axonemal microtubule modifications while preserving ciliogenesis initiation, whereas a Meckel syndrome–associated variant disrupts both, and a disease mutation (p.Ser101Arg) abrogates the B9D2–MKS1 interaction [PMID:21763481, PMID:41165761].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005929 cilium, GO:0005815 microtubule organizing center, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance, R-HSA-1643685 Disease
- **partners:** MKS1, B9D1, TMEM67, IFT88, TMEM216, TMEM237, INVERSIN
- **complexes:** B9 protein complex (MKS1–B9D2–B9D1), ciliary transition zone

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | B9D2 physically interacts with MKS1 and B9D1 to form a B9 protein complex; a disease-causing missense mutation (p.Ser101Arg) in B9D2 abrogates its interaction with MKS1, as demonstrated by co-immunoprecipitation and mass spectrometry. Loss of B9d2 in mice compromises ciliogenesis and ciliary protein localization, and the p.Ser101Arg mutant mRNA fails to rescue zebrafish b9d2 morphant phenotypes. | PMID:21763481 | American journal of human genetics |
| 2008 | High | The C. elegans B9D2 ortholog TZA-1 forms a complex with the other two B9 proteins (XBX-7/MKS1 and TZA-2/B9D1) that localizes to the base of cilia (transition zone). Single B9 gene mutations do not overtly affect ciliogenesis, but combinatorial loss with nph-1 or nph-4 causes defects in cilia formation and maintenance in sensory neurons, indicating functional redundancy between the B9 complex and nephrocystins. | PMID:18337471 | Molecular biology of the cell |
| 2009 | High | C. elegans MKSR-2 (B9D2 ortholog) localizes to transition zones/basal bodies of sensory cilia in a manner that is largely co-dependent with MKS-1 and MKSR-1. Disruption of human MKSR2 causes ciliogenesis defects. Genetic interactions among all double mks/mksr mutant combinations in C. elegans manifest as increased lifespan via aberrant insulin-IGF-I signaling. | PMID:19208769 | Journal of cell science |
| 2011 | High | B9d2 binds IFT particle components (Fleer/IFT88) and contributes to the ciliary localization of Inversin (Nephrocystin 2) in zebrafish. B9d2, Inversin, and Nephrocystin 5 collectively support transport of the cargo Opsin but not Peripherin into photoreceptor cilia. | PMID:21602787 | The EMBO journal |
| 2011 | Medium | C. elegans MKSR-2/B9D2 genetically interacts with MKS-2/TMEM216, MKSR-1/B9D1, and JBTS-14/TMEM237 at the transition zone, collectively controlling basal body–transition zone anchoring to the membrane and ciliogenesis. | PMID:22152675 | American journal of human genetics |
| 2012 | Medium | C. elegans mksr-2 genetically interacts with nphp-2 (inversin ortholog) in a sensilla-dependent manner to control cilia formation and placement, but mksr-2 is not required for correct localization of NPHP/MKS transition zone proteins or for intraflagellar transport. | PMID:22393243 | Journal of cell science |
| 2020 | High | The B9D protein complex is organized as MKS1–B9D2–B9D1. B9D2 and MKS1 localize to the ciliary transition zone in an interdependent manner. Knockout of B9D2 compromises ciliogenesis, and rescue experiments show that formation of the intact B9D protein complex is essential for creating a diffusion barrier for ciliary membrane proteins. | PMID:32726168 | Molecular biology of the cell |
| 2021 | Medium | The B9 domain of MKS1 is required for interaction with B9D2; a frameshift mutation (c.1058delG) disrupting the B9 domain of MKS1 attenuates the MKS1–B9D2 interaction and impairs MKS1 ciliary localization at the transition zone. | PMID:33193692 | Frontiers in genetics |
| 2022 | Medium | MKS1 mutations (c.350C>A and c.1408-14A>G) disrupting the B9-C2 domain attenuate the interaction of MKS1 with B9D2, confirming that B9D2 is an essential binding partner of MKS1 at the ciliary transition zone. | PMID:35360848 | Frontiers in genetics |
| 2021 | High | Two B9D2 missense variants associated with Joubert syndrome (P74S and G155S) are pathogenic in C. elegans: both disrupt cilium/transition zone structure and sensory function; G155S more severely disrupts endogenous MKSR-2 organization at the TZ. Compound heterozygous worms (P74S/G155S) phenocopy P74S homozygotes. Both alleles reveal a close functional association between the B9 complex and MKS-2/TMEM216. | PMID:33234550 | Disease models & mechanisms |
| 2024 | Medium | Before ciliogenesis occurs, B9D2 localizes to tight junctions and is required for the maturation and maintenance of tight junctions, ensuring epithelial barrier tightness and appropriate biliary lumen formation. This non-ciliary function of B9D2 is proposed to underlie biliary dysgenesis in Meckel-Gruber and Joubert syndromes. | PMID:39455645 | Scientific reports |
| 2025 | High | The B9D1–B9D2–MKS1 complex interacts with and anchors TMEM67 to the transition zone membrane; disruption of this B9–TMEM67 complex reduces posttranslational modifications (e.g., acetylation, glutamylation) of axonemal microtubules by deregulating tubulin-modifying enzymes within cilia. Additionally, B9 proteins localize to centrioles prior to ciliogenesis and facilitate the initiation of ciliogenesis. Joubert syndrome-associated B9D2 variants primarily impair axonemal microtubule modifications without disrupting ciliogenesis initiation, whereas the Meckel syndrome-associated B9D2 variant disrupts both. | PMID:41165761 | The Journal of clinical investigation |
| 2011 | Medium | NPHP4 missense mutations modify the severity of phenotypes caused by disruption of mksr-2 (B9D2 ortholog) in C. elegans, confirming genetic interaction between the NPHP and MKS/B9 modules at the ciliary transition zone. | PMID:21546380 | Human molecular genetics |

## Citations

- PMID:18337471
- PMID:19208769
- PMID:21546380
- PMID:21602787
- PMID:21763481
- PMID:22152675
- PMID:22393243
- PMID:32726168
- PMID:33193692
- PMID:33234550
- PMID:35360848
- PMID:39455645
- PMID:41165761
