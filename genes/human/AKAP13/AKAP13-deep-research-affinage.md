---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKAP13
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q12802
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 31
citation_count: 31
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKAP13 (human)

## Current model (mechanistic narrative)

AKAP13 (AKAP-Lbc) is a dual-function scaffold that simultaneously anchors protein kinase A (PKA) and acts as a Gα12-activated, RhoA-selective guanine nucleotide exchange factor (GEF), thereby coupling GPCR signaling to actin cytoskeleton remodeling and transcriptional reprogramming [PMID:11546812, PMID:11696353]. Its DH-PH catalytic module engages RhoA-GDP through an N-terminal 'GEF switch' that undergoes a conformational change upon binding, with the PH domain dispensable for nucleotide exchange [PMID:25186459], and a distinct C-terminal region confers selective coupling to Gα12 over Gα13 [PMID:31051012]. The GEF activity is held in check by an integrated network of negative regulators: anchored-PKA phosphorylation of Ser1565 recruits 14-3-3 [PMID:15229649], C-terminal leucine-zipper homo-oligomerization is required for that inhibition [PMID:15691829], and LC3 binding to the N-terminal regulatory region suppresses RhoA engagement [PMID:19696020]. Beyond its GEF role, AKAP13 nucleates multikinase complexes—coordinating PKCη-dependent PKD activation [PMID:15383279], assembling a PKNα/MLTK/MKK3/p38α module downstream of α1-adrenergic receptors [PMID:21224381], and scaffolding the KSR-1/RAF/MEK/ERK cassette via PKA phosphorylation of KSR-1 [PMID:21102438]. Through these outputs it drives pathological cardiac hypertrophy via PKD-dependent HDAC5 nuclear export and MEF2 transcription [PMID:18951085, PMID:20139090, PMID:24161911], and is essential for embryonic cardiac development [PMID:20139090]. AKAP13 also positions PKA toward diverse effectors to control transcription and cell fate, including ERα Ser305 phosphorylation and tamoxifen resistance [PMID:26272591], CREB1 activation [PMID:36401072], and PKA-mediated phosphorylation of Raptor (Ser791) to inhibit mTORC1 [PMID:34673774]. It additionally contributes to cell migration through polarized leading-edge PKA gradients and integrin/LPA-driven RhoA signaling [PMID:19106088, PMID:22049212]. The AKAP13/Lbc locus also encodes the HA-3 minor histocompatibility antigen [PMID:12663445].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-74160 Gene expression (Transcription), R-HSA-1266738 Developmental Biology
- **partners:** RHOA, GNA12, PRKACA, YWHAZ, MAP1LC3, PRKD1, RPTOR, CD47
- **complexes:** AKAP-Lbc PKA-signaling scaffold, KSR-1/RAF/MEK/ERK module, PKNα/MLTK/MKK3/p38α module

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | AKAP-Lbc (AKAP13) functions as both an A-kinase anchoring protein (AKAP) that binds PKA and a Rho-selective guanine nucleotide exchange factor (GEF). Expression in fibroblasts promotes stress fiber formation in a Rho-dependent manner, and Gα12 selectively couples to and activates AKAP-Lbc to drive RhoA signaling. | PMID:11546812 | The Journal of biological chemistry |
| 2001 | Medium | The Ht31/AKAP13 gene encodes AKAP13 and smaller splice variants (Brx and proto-Lbc); an endogenous ~309 kDa Ht31 protein co-immunoprecipitates RhoA from primary rat renal inner medullary collecting duct cells, confirming in vivo interaction between AKAP and RhoA. | PMID:11696353 | FEBS letters |
| 2004 | High | AKAP-Lbc assembles a protein kinase D (PKD) activation scaffold by recruiting upstream kinase PKCη and coordinating PKA phosphorylation events that release activated PKD, thereby synchronizing PKA and PKC activities to activate a third kinase. | PMID:15383279 | Molecular cell |
| 2004 | High | PKA anchored to AKAP-Lbc phosphorylates AKAP-Lbc on Ser1565, which induces recruitment of 14-3-3, and 14-3-3 binding inhibits the Rho-GEF activity of AKAP-Lbc. Under basal conditions, 14-3-3 maintains AKAP-Lbc in an inactive state; AKAP-Lbc mutants that cannot bind PKA or 14-3-3 show elevated basal Rho-GEF activity. | PMID:15229649 | The EMBO journal |
| 2005 | High | AKAP-Lbc forms homo-oligomers inside cells via two adjacent leucine zipper motifs in its C-terminal region. Disruption of oligomerization drastically increases basal RhoA-GEF activity. Additionally, 14-3-3 can only inhibit AKAP-Lbc Rho-GEF activity when the protein is in an oligomeric state; oligomerization-deficient mutants are resistant to PKA/14-3-3-mediated inhibition. | PMID:15691829 | The Journal of biological chemistry |
| 2007 | High | AKAP-Lbc is critical for α1-adrenergic receptor (α1-AR)-mediated RhoA activation and cardiomyocyte hypertrophy. α1-ARs activate AKAP-Lbc via a Gα12-dependent pathway. shRNA suppression of AKAP-Lbc in neonatal ventricular cardiomyocytes strongly reduces α1-AR-mediated RhoA activation and hypertrophic responses. | PMID:17537920 | Proceedings of the National Academy of Sciences of the United States of America |
| 2008 | High | AKAP-Lbc is upregulated in hypertrophic cardiomyocytes and coordinates PKD activation coupled to phosphorylation-dependent nuclear export of class II histone deacetylase HDAC5, driving MEF2-mediated transcriptional reprogramming leading to pathological cardiac hypertrophy. | PMID:18951085 | Molecular cell |
| 2008 | Medium | AKAP-Lbc is a major contributor to the formation of PKA activity gradients at the leading edge of migrating cells. FRET-based PKA activity reporters show strongest PKA activity at the leading edge (basal surface); disruption of PKA anchoring by Ht31 peptide or AKAP-Lbc knockdown abolishes this polarized gradient. | PMID:19106088 | The Journal of biological chemistry |
| 2009 | High | The ubiquitin-like protein LC3 interacts with AKAP-Lbc via its N-terminal α-helical domain binding to two sites in the N-terminal regulatory region of AKAP-Lbc. LC3 overexpression reduces AKAP-Lbc interaction with RhoA, inhibits its Rho-GEF activity, and impairs actin stress fiber formation. AKAP-Lbc mutants that cannot bind LC3 display higher basal Rho-GEF activity and are refractory to LC3 inhibition. | PMID:19696020 | The Journal of biological chemistry |
| 2010 | High | AKAP13 (Brx-1/AKAP-Lbc) is essential for cardiac development in mice. Akap13-null embryos die at E10.5–11.0 with deficient sarcomere formation and thin-walled hearts. AKAP13 coordinates Gα12 and Rho signaling upstream of MEF2C transcription; Akap13 siRNA reduces Mef2c mRNA and AKAP13 overexpression augments MEF2C-dependent reporter activity. | PMID:20139090 | The Journal of biological chemistry |
| 2010 | High | AKAP-Lbc forms the core of a signaling network with KSR-1 to relay signals from RAF through MEK to ERK1/2. AKAP-Lbc enhances ERK signaling by anchoring RAF near MEK1 and synchronizing PKA-mediated phosphorylation of Ser838 on KSR-1. | PMID:21102438 | Nature cell biology |
| 2011 | High | AKAP-Lbc assembles a novel signaling complex containing PKNα, MLTK, MKK3, and p38α downstream of α1b-adrenergic receptors. This complex integrates α1b-AR signals to promote RhoA-dependent activation of p38α MAPK. Silencing AKAP-Lbc or disrupting the AKAP-Lbc·p38α complex specifically reduces α1-AR-mediated p38α activation without affecting other MAPK pathways. | PMID:21224381 | The Journal of biological chemistry |
| 2011 | Medium | Integrin α6β4 cooperates with LPA to activate RhoA specifically through AKAP-Lbc, and this RhoA activation is required for LPA-dependent chemotaxis and lamellae formation. AKAP-Lbc-mediated RhoA activation in turn facilitates Rac1 activation dependent on de novo β1 integrin ligation. | PMID:22049212 | American journal of physiology. Cell physiology |
| 2012 | Medium | AKAP-Lbc directly anchors PKA to facilitate phosphorylation of Hsp20 on Ser16, which is required for the anti-apoptotic cardioprotective actions of Hsp20. PKA anchoring disruptor peptides block this phosphorylation; gene silencing and rescue experiments confirm AKAP-Lbc is the responsible anchoring protein. | PMID:22731613 | The Biochemical journal |
| 2012 | Medium | Shp2 (tyrosine phosphatase) is a component of the AKAP-Lbc complex; AKAP-Lbc-anchored PKA phosphorylates Shp2, inhibiting its phosphatase activity under pathological hypertrophic conditions in the heart (chronic β-adrenergic stimulation). | PMID:23045525 | The Journal of biological chemistry |
| 2013 | High | The C-terminus of AKAP-Lbc is critical for PKD1 interaction in vivo. AKAP-Lbc-ΔPKD mice (lacking PKD1-binding domain) show reduced PKD1 activation, diminished HDAC5 phosphorylation, and attenuated compensatory cardiac hypertrophy with accelerated progression to cardiac dysfunction under pressure overload or neurohumoral stimulation. | PMID:24161911 | Journal of molecular and cellular cardiology |
| 2013 | Medium | AKAP13 Rho-GEF and PKD-binding domains are not required for normal mouse development or cardiac architecture, but are required for proper cardiac contractility (fractional shortening and ejection fraction) in response to β-adrenergic-induced cardiac hypertrophy. | PMID:23658642 | PloS one |
| 2014 | High | Crystal structure of the RhoA-GDP/AKAP-Lbc DH-PH domain complex was determined at 2.1 Å resolution. The PH domain plays no role in nucleotide exchange (confirmed by GEF assays comparing DH-PH vs. DH alone). The structure reveals a conformational change in the N-terminal 'GEF switch' region upon RhoA binding, and AKAP-Lbc has only micromolar affinity for RhoA (measured by ITC). | PMID:25186459 | The Biochemical journal |
| 2015 | Medium | AKAP13 anchors PKA near estrogen receptor alpha (ERα) and a PKA regulatory subunit; AKAP13 knockdown prevents PKA-mediated phosphorylation of ERα on Ser305 and abrogates PKA-driven tamoxifen resistance in breast cancer cells. | PMID:26272591 | BMC cancer |
| 2015 | Medium | Akap13 haploinsufficient mice display reduced bone mineral density, reduced osteoblast numbers, and diminished Runx2 and alkaline phosphatase expression, indicating AKAP13 is required for early osteogenesis. Akap13 siRNA knockdown in bone marrow stem cells reduces Runx2 and Alp transcripts. | PMID:25892096 | Journal of bone and mineral research |
| 2016 | Medium | A novel Gα12-binding region was identified near the C-terminus of AKAP-Lbc (distinct from the RGS-homology domain interface used by other RhoGEFs). AKAP-Lbc shows high selectivity for Gα12 over Gα13; charge-reversal of conserved residues in this region disrupts Gα12 binding. This binding region is also conserved in p114RhoGEF. | PMID:31051012 | Journal of molecular signaling |
| 2017 | Medium | AKAP-Lbc is required for α1-adrenergic receptor-mediated cardioprotection against doxorubicin-induced apoptosis. AKAP-Lbc mediates this protection through activation of anchored PKD1, which promotes Bcl2 expression and inhibits Bax translocation to mitochondria. | PMID:28923249 | Biochimica et biophysica acta. Molecular cell research |
| 2018 | Medium | AKAP-Lbc-mediated RhoA activation controls aquaporin-2 (AQP2) trafficking in renal collecting duct principal cells. A small-molecule inhibitor (Scaff10-8) that binds RhoA and specifically blocks AKAP-Lbc-mediated (but not other GEF-mediated) RhoA activation promotes redistribution of AQP2 from intracellular vesicles to the plasma membrane. | PMID:29373579 | PloS one |
| 2019 | Medium | AKAP13 physically interacts with progesterone receptor B (PR-B) through its carboxyl terminus (shown by GST-binding assay) and augments ligand-dependent PR-B (but not PR-A) activation. This effect is reduced by ERK inhibition but not p38 MAPK inhibition. | PMID:30239831 | The Journal of clinical endocrinology and metabolism |
| 2021 | Medium | AKAP13 acts as a scaffold for PKA and mTORC1, enabling GPCR/Gαs/cAMP-induced PKA phosphorylation of Raptor on Ser791, thereby inhibiting mTORC1. AKAP13 was identified as an mTORC1 binding protein and mediates mTORC1-dependent cell proliferation, cell size, and colony formation. | PMID:34673774 | PLoS genetics |
| 2021 | Medium | CD47 interacts with AKAP13 and facilitates AKAP13-mediated RhoA activation, promoting T-cell lymphoma metastasis through elevated basal RhoA activity independent of CD47's anti-phagocytic function. | PMID:33406263 | International immunology |
| 2022 | Medium | AKAP13 physically interacts with CREB1 (shown by co-immunoprecipitation) and enhances FSH-induced PKA-dependent CREB1 phosphorylation in granulosa cells. AKAP13 siRNA knockdown reduces FSH-stimulated CREB1 phosphorylation and decreases aromatase and LH receptor transcript levels. | PMID:36401072 | Reproductive sciences |
| 2026 | Medium | AKAP13 drives glioma progression by enhancing YAP expression and nuclear translocation, which upregulates TAM-recruiting chemokines CSF1 and CCL2. FBXW7 was identified as an upstream E3 ligase that promotes ubiquitin-mediated degradation of AKAP13, placing AKAP13 in a FBXW7/AKAP13/YAP/chemokine axis. | PMID:41506544 | Biochemical pharmacology |
| 2026 | Medium | Neutrophil P2Y14 receptor deletion promotes PKA-induced phosphorylation of AKAP13, thereby inhibiting RhoA activation and cytoskeleton rearrangement, resulting in reduced neutrophil-platelet aggregates and NET release. This places AKAP13 in a PKA/AKAP13/RhoA signaling axis downstream of P2Y14R in neutrophils. | PMID:41143464 | European heart journal |
| 2003 | High | The HA-3 minor histocompatibility antigen peptide (VTEPGTAQY) is encoded by the AKAP13/Lbc oncogene. The allelic variant (VMEPGTAQY, HA-3M) is destroyed by proteasome-mediated digestion whereas the HA-3T peptide is not, explaining the differential immunogenicity — the Thr→Met substitution does not affect TAP transport or HLA-A1 binding but leads to proteasomal destruction of the negative allele. | PMID:12663445 | Blood |
| 2007 | Medium | AKAP13 (via its GEF activity) is required for TLR2-mediated NF-κB activation and IL-8/MCP-1 secretion in macrophages and epithelial cells. A GEF-deficient AKAP13 mutant partially inhibits NF-κB activation. AKAP13 is also involved in JNK phosphorylation but not ERK1/2 phosphorylation downstream of TLR2. | PMID:17878165 | The Journal of biological chemistry |

## Citations

- PMID:11546812
- PMID:11696353
- PMID:12663445
- PMID:15229649
- PMID:15383279
- PMID:15691829
- PMID:17537920
- PMID:17878165
- PMID:18951085
- PMID:19106088
- PMID:19696020
- PMID:20139090
- PMID:21102438
- PMID:21224381
- PMID:22049212
- PMID:22731613
- PMID:23045525
- PMID:23658642
- PMID:24161911
- PMID:25186459
- PMID:25892096
- PMID:26272591
- PMID:28923249
- PMID:29373579
- PMID:30239831
- PMID:31051012
- PMID:33406263
- PMID:34673774
- PMID:36401072
- PMID:41143464
- PMID:41506544
