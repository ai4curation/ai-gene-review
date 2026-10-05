---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKS3
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q6ZW76
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKS3 (human)

## Current model (mechanistic narrative)

ANKS3 is a ciliary ankyrin-repeat and SAM-domain scaffold protein that nucleates and tunes macromolecular assemblies governing left-right axis determination and renal homeostasis [PMID:29290488, PMID:27417436]. Through its SAM domain it self-polymerizes and binds the SAM domain of ANKS6, which docks onto one end of the ANKS3-SAM polymer; the disease-associated R823W mutation in ANKS6 abolishes this interaction [PMID:24998259]. ANKS3 bridges ANKS6 to Bicc1, and together the three proteins cooperatively build giant SAM-dependent assemblies that neither ANKS3 nor ANKS6 forms alone [PMID:29290488]. Within these assemblies ANKS3 acts as a conformational switch over Bicc1-dependent mRNA regulation: a C-terminal coiled-coil of ANKS3 binds Bicc1 and inhibits target mRNA binding, while ANKS6 relieves this inhibition, and ANKS3 disperses Bicc1 condensates to release client transcripts whereas ANKS6 co-recruitment reinstates condensation and ribonucleoparticle phase transitioning [PMID:37733651, PMID:37275520]. This regulation controls symmetric versus asymmetric decay of Dand5 mRNA, the basis of ANKS3's role in laterality, and a homozygous loss-of-function ANKS3 variant causes human laterality defects [PMID:27417436, PMID:37733651]. ANKS3 also interacts with multiple nephronophthisis proteins, localizes to cilia, and retains the kinase Nek7 in the cytoplasm via its N-terminal ankyrin repeats, with NPHP1 limiting ANKS3 polymerization [PMID:25671767, PMID:26188091]. In the kidney ANKS3 acts as a cytosolic regulator of polycystin-dependent cilia signaling, functioning downstream of polycystins but upstream of Glis2; its inactivation suppresses cyst progression in Pkd1 mouse models [PMID:bio_10.1101_2025.04.22.649832].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005929 cilium, GO:0005829 cytosol
- **pathway (Reactome):** *(none)*
- **partners:** ANKS6, BICC1, NEK7, NPHP1, HIF1AN
- **complexes:** ANKS3-ANKS6-Bicc1 giant macromolecular complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | The SAM domain of ANKS3 directly binds the SAM domain of ANKS6; ANKS3-SAM polymerizes and ANKS6-SAM binds to one end of the polymer. Crystal structures of the ANKS3-SAM polymer and ANKS3-SAM/ANKS6-SAM complex were determined, revealing molecular details of their association. The disease-associated R823W mutation in ANKS6-SAM dramatically destabilizes the SAM domain, causing loss of interaction with ANKS3-SAM. | PMID:24998259 | BMC structural biology |
| 2015 | Medium | Anks3 interacts with multiple nephronophthisis proteins (NPHPs) as well as Bicc1 and HIF1AN. GFP-tagged Anks3 localizes to the cilium in multi-ciliated epidermal cells. In the absence of NPHP1, Anks3 forms large aggregates, indicating that NPHP1 curtails Anks3 polymerization. Knockdown of anks3 in zebrafish causes ciliary abnormalities, cyst formation, and laterality defects. | PMID:25671767 | Kidney international |
| 2015 | Medium | ANKS3 interacts with the NIMA-related kinase Nek7 through its N-terminal ankyrin repeats, and this interaction results in an ~20 kDa molecular weight modification of Anks3 (not attributable to Nek7-dependent phosphorylation, as a kinase-dead Nek7 mutant also causes the modification). ANKS3 retains Nek7 in the cytoplasm, preventing Nek7 nuclear localization. | PMID:26188091 | Biochemical and biophysical research communications |
| 2015 | Medium | ANKS3 and ANKS6 interact through their SAM domains (confirmed by yeast two-hybrid and co-immunoprecipitation), and both proteins co-localize in mouse renal cilia in vivo. Downregulation of Anks3 in vivo in mice altered transcription of vasopressin-induced genes, genes encoding cilium structural proteins, and apoptosis/proliferation genes. | PMID:26327442 | PloS one |
| 2017 | High | ANKS3 recruits ANKS6 to Bicc1, and together the three proteins cooperatively generate giant macromolecular complexes in vivo. Neither ANKS3 nor ANKS6 alone formed macroscopic homopolymers in vivo. The giant assemblies are shaped by SAM domains, flanking sequences, and SAM-independent protein-protein and protein-mRNA interactions. | PMID:29290488 | Structure |
| 2016 | Medium | A homozygous loss-of-function variant in ANKS3 causes laterality defects in humans. Mutant ANKS3 RNA failed to rescue laterality defects in zebrafish anks3 morphants (unlike wild-type RNA), and a new CRISPR/mutant anks3 zebrafish line displays laterality defects in the homozygous state, confirming ANKS3's role in right-left axis determination. | PMID:27417436 | Human genetics |
| 2023 | Medium | ANKS3 has a C-terminal coiled-coil domain that interacts with Bicc1 and inhibits binding of target mRNAs to Bicc1. ANKS6 regulates the conformation of ANKS3, relieving this inhibition. A CRISPR-engineered truncation of ANKS3 leads to symmetric mRNA decay of Dand5 (mediated by Bicc1), demonstrating that ANKS3 conformation controls laterality specification via Bicc1 mRNA binding. | PMID:37733651 | PLoS biology |
| 2023 | Medium | ANKS3 disperses Bicc1 cytoplasmic granules and concomitantly releases bound mRNAs; co-recruitment of ANKS6 by ANKS3 reinstates Bicc1 condensation and ribonucleoparticle assembly. Bicc1 head-to-tail SAM polymers are interconnected by KH domains to mediate liquid-to-gel phase transitioning of client transcripts, with dual and opposing regulation by ANKS3 and ANKS6. | PMID:37275520 | iScience |
| 2025 | Medium | Anks3 acts as a cytosolic regulator of polycystin-dependent cilia signaling: it regulates polycystin-dependent Glis2 expression in vitro and in vivo, undergoes polycystin-dependent changes in phosphorylation state, and functions downstream of cilia and polycystins but upstream of Glis2. Inactivation of Anks3 in Pkd1 mouse models suppresses cyst progression. | PMID:bio_10.1101_2025.04.22.649832 | bioRxiv |

## Citations

- PMID:24998259
- PMID:25671767
- PMID:26188091
- PMID:26327442
- PMID:27417436
- PMID:29290488
- PMID:37275520
- PMID:37733651
- PMID:bio_10.1101_2025.04.22.649832
