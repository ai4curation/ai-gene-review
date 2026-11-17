---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SUCLA2
affinage_run_date: 2026-06-10T10:51:54
uniprot_accession: Q9P2R7
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

# Affinage mechanistic annotation for SUCLA2 (human)

## Current model (mechanistic narrative)

SUCLA2 encodes the ADP-forming β subunit of mitochondrial succinyl-CoA synthetase, the TCA-cycle enzyme whose control over local succinyl-CoA availability makes it a central regulator of protein lysine succinylation across cellular compartments [PMID:33230181]. Loss of SUCLA2 function causes succinyl-CoA accumulation and global protein hyper-succinylation (nearly 1,000 sites on hundreds of proteins), many of which are SIRT5 substrates; SIRT5 gain-of-function reverses this and improves survival in sucla2-deficient zebrafish [PMID:33230181]. This succinylation-buffering role lets SUCLA2 act as a direct regulator of partner enzymes: it physically associates with glutaminase (GLS) to suppress GLS K311 succinylation, and p38 MAPK phosphorylation at S79 dissociates the complex to license GLS succinylation, oligomerization and glutaminolysis under oxidative stress [PMID:33991485]; ERK2 phosphorylation at S124, coupled to PIN1 isomerization, redirects SUCLA2 to OXCT1, where locally generated succinyl-CoA succinylates and activates OXCT1 to drive ketolysis [PMID:39862868]. SUCLA2 also binds ALAS2 through the ALAS2 C-terminus, an interaction required for normal heme-biosynthetic ALAS2 activity in vivo [PMID:22740690]. SUCLA2 activity is itself gated by post-translational control: SIRT5 desuccinylates SUCLA2 at K118 and AMPK-dependent phosphorylation tunes its output, with loss of these controls inhibiting the enzyme and propagating TCA-cycle and mitochondrial dysfunction [PMID:39643219, PMID:39966410]. The protein's catalytic loss produces tissue-specific disease, reflecting its expression pattern: in human cerebral cortex SUCLA2 is restricted to neurons and absent from glia, with SUCLG2 instead serving vascular cells [PMID:24085565, PMID:25370487]. Muscle-specific knockout produces a mitochondrial myopathy preferentially affecting oxidative slow-twitch fibers [PMID:39482887], and NAD+ depletion driven by bulk succinylation underlies respiratory and locomotor deficits that NAD+ precursor supplementation rescues in a SIRT5-dependent manner [PMID:41574612].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0016740 transferase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-392499 Metabolism of proteins
- **partners:** GLS, OXCT1, ALAS2, SIRT5
- **complexes:** succinyl-CoA synthetase (SCS)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | SUCLA2 physically associates with kidney-type glutaminase (GLS) and suppresses GLS K311 succinylation. Upon oxidative stress, p38 MAPK phosphorylates SUCLA2 at S79, causing SUCLA2 to dissociate from GLS. Dissociation allows enhanced GLS K311 succinylation, GLS oligomerization, and increased GLS activity, boosting glutaminolysis and NADPH/glutathione production to counteract oxidative stress. | PMID:33991485 | Molecular cell |
| 2025 | High | Upon IGF1 stimulation, ERK2 phosphorylates SUCLA2 at S124, and PIN1-mediated cis-trans isomerization of SUCLA2 facilitates its interaction with OXCT1 (a rate-limiting ketolysis enzyme). SUCLA2-associated with OXCT1 generates succinyl-CoA that directly succinylates OXCT1 at K421, activating OXCT1 and enhancing ketolysis in HCC cells. | PMID:39862868 | Molecular cell |
| 2020 | High | Loss-of-function mutations in SUCLA2 cause accumulation of succinyl-CoA, leading to global protein hyper-succinylation across cellular compartments. Nearly 1,000 succinylation sites on 366 proteins were quantified in patient-derived cells. Many hyper-succinylated targets are known substrates of the desuccinylase SIRT5; SIRT5 gain-of-function in a zebrafish sucla2-deficient model reduced global succinylation and improved survival. | PMID:33230181 | Nature communications |
| 2011 | Medium | In SUCLA2-deficient patient fibroblasts, mtDNA content and NDPK activity are normal; however, shRNA knockdown of the GDP-dependent isoform SUCLG2 in both patient and control fibroblasts caused significant mtDNA depletion, decreased NDPK and cytochrome c oxidase activities, and marked growth impairment, indicating that SUCLG2 (not SUCLA2) is the primary driver of mtDNA maintenance, and that mitochondrial NDPK links succinyl-CoA synthetase activity to mtDNA maintenance. | PMID:21295139 | Biochimica et biophysica acta |
| 2012 | Medium | ALAS2 (erythroid aminolevulinic acid synthase) binds to SUCLA2 via its carboxyl-terminal region. XLSA mutations in the ALAS2 C-terminus (p.Met567Val, p.Ser568Gly, p.Phe557Ter) abolish binding to a SUCLA2 affinity column despite normal ALAS2 enzymatic activity, indicating that the ALAS2–SUCLA2 interaction is required for normal in vivo ALAS2 activity in heme biosynthesis. | PMID:22740690 | The Journal of biological chemistry |
| 2024 | Medium | SIRT5 desuccinylates SUCLA2 at K118; SIRT5 downregulation leads to SUCLA2 K118 hyper-succinylation, which inhibits succinyl-CoA synthetase activity, causing succinyl-CoA accumulation and a feed-forward cycle of further SUCLA2 succinylation. This dysregulation propagates TCA cycle dysfunction and contributes to mitochondrial damage via hypersuccinylation of CYC1 (complex III subunit) and activation of the cGAS-STING pathway in acute pancreatitis. | PMID:39643219 | Biochimica et biophysica acta. Molecular basis of disease |
| 2025 | Medium | In adipose tissue macrophages, ATP generated from glutaminolysis suppresses AMPK, which decreases phosphorylation of SUCLA2. Reduced SUCLA2 phosphorylation activates succinyl-CoA synthetase, causing overproduction of succinate and IL-1β. siRNA-mediated SUCLA2 knockdown in mice reduced HFD-induced obesity, demonstrating that the glutaminolysis/AMPK/SUCLA2/IL-1β axis controls macrophage-driven inflammatory obesity. | PMID:39966410 | Nature communications |
| 2013 | Medium | In human cerebral cortex, SUCLA2 protein (A-SUCL-β) is expressed exclusively in neurons and colocalizes >99% with the mitochondrial F0-F1 ATP synthase d subunit; it is absent in GFAP- and S100-positive astroglia. SUCLA2 mRNA was also detected only in neurons, not glial cells, by in situ hybridization. | PMID:24085565 | Brain structure & function |
| 2014 | Medium | In human cerebral cortex, SUCLG2 (GTP-forming β subunit) is absent in neurons, astrocytes, microglia, and oligodendrocytes but localizes to cerebrovascular structures, confirming that succinyl-CoA ligase substrate-level phosphorylation is restricted to neurons (SUCLA2) and vascular cells (SUCLG2) in the human brain. | PMID:25370487 | Journal of bioenergetics and biomembranes |
| 2024 | Medium | Muscle-specific conditional knockout of Sucla2 (using HSA-Cre with CRISPR-generated floxed allele) in mice produces mitochondrial myopathy with reduced body weight, grip strength, and exercise tolerance. The soleus (slow-twitch, oxidative) muscle was more severely affected than the EDL (fast-twitch), showing 40% reduced specific tetanic force, slower contraction/relaxation, ~3-fold increase in mitochondria, and nearly doubled proportion of Type 1 myosin heavy chain fibers. | PMID:39482887 | Journal of cachexia, sarcopenia and muscle |
| 2026 | Medium | In sucla2-/- zebrafish, excess succinyl-CoA drives bulk protein succinylation that consumes NAD+, impairing mitochondrial respiratory function and causing locomotor deficits. NAD+ precursor supplementation (nicotinamide, nicotinamide riboside) restores NAD+ levels and improves locomotion and survival; this effect requires the NAD+-dependent desuccinylase Sirt5, which enhances oxidative metabolism and urea cycle nitrogen elimination. | PMID:41574612 | JCI insight |
| 2016 | Low | Knockdown of Sucla2 in mouse spermatocyte GC2 cells decreased mitochondrial membrane potential, reduced ATP production, increased ROS, decreased Bcl2 expression, and induced apoptosis, demonstrating that SUCLA2 mitochondrial function is required for spermatocyte viability. | PMID:27766610 | Folia histochemica et cytobiologica |
| 2025 | Low | SUCLA2 overexpression reduced succinyl-CoA levels and inhibited lysine succinylation of SHMT2, suppressing ferroptosis and renal interstitial fibrosis in Ang II-treated cells and mice. SIRT5-mediated desuccinylation of SHMT2 also inhibited ferroptosis, and the anti-ferroptotic effect of SUCLA2 overexpression was abolished by SHMT2 silencing, placing SUCLA2 upstream of SHMT2 succinylation in the ferroptosis pathway. | PMID:41359112 | FASEB journal |

## Citations

- PMID:21295139
- PMID:22740690
- PMID:24085565
- PMID:25370487
- PMID:27766610
- PMID:33230181
- PMID:33991485
- PMID:39482887
- PMID:39643219
- PMID:39862868
- PMID:39966410
- PMID:41359112
- PMID:41574612
