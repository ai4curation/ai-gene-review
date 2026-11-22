---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP6
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O43182
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGAP6 (human)

## Current model (mechanistic narrative)

ARHGAP6 is a RhoA-specific GTPase-activating protein that couples regulation of Rho-family GTPase signaling to actin cytoskeletal remodeling [PMID:10699171]. It carries a rhoGAP domain whose conserved active-site arginine is required to inactivate RhoA and drive loss of actin stress fibers, but a genetically separable N-terminal domain co-localizes with F-actin and recruits it into growing filopodium-like processes independently of GAP catalysis [PMID:10699171]. In cancer cells, ARHGAP6 acts as a tumor suppressor by restraining RhoA/ROCK signaling: it attenuates STAT3 phosphorylation downstream of IL-6 to limit migration, invasion, and expression of MMP9 and VEGF [PMID:30816546], promotes apoptosis while suppressing glycolysis and cisplatin resistance through STAT3 inhibition [PMID:33116826], and promotes ferroptosis by inhibiting a RhoA/ROCK1–p38 MAPK axis [PMID:38287795]. ARHGAP6 physically interacts with Rac3 in cervical carcinoma cells, where its overexpression suppresses proliferation, migration, invasion, and adhesion and induces G0/G1 arrest [PMID:26628301]. Its expression is constrained post-transcriptionally by miR-96-5p and miR-152-5p, which bind its 3′UTR/mRNA [PMID:34338998, PMID:36936709], and transcriptionally by ZBTB6, which binds the ARHGAP6 promoter to repress it and thereby de-represses STAT3 signaling [PMID:40133895].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5357801 Programmed Cell Death
- **partners:** RHOA, RAC3, ROCK1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | Medium | ARHGAP6 encodes a protein with a GTPase-activating (GAP) domain homologous to the rhoGAP family, identified from the MLS critical region at Xp22.3; the gene produces at least two isoforms (601 and 495 amino acids) via alternative splicing, expressed across multiple tissues. | PMID:9417914 | Genomics |
| 2000 | High | ARHGAP6 functions as a GAP with specificity for RhoA: mutation of a conserved arginine in the rhoGAP domain prevents loss of actin stress fibers (a RhoA-dependent structure) without abolishing process outgrowth, establishing two independent functions — RhoA-GAP activity and actin remodeling via an N-terminal domain. | PMID:10699171 | Human molecular genetics |
| 2000 | High | ARHGAP6 co-localizes with actin filaments through its N-terminal domain and recruits F-actin into growing processes (filopodia-like), independent of its RhoA-GAP activity. | PMID:10699171 | Human molecular genetics |
| 2000 | Medium | Loss of Arhgap6 rhoGAP function in mice (gene targeting of the rhoGAP domain in embryonic stem cells) does not produce any detectable phenotypic or behavioral abnormalities, indicating RhoA-GAP activity of Arhgap6 alone is not essential for normal mouse development. | PMID:10699171 | Human molecular genetics |
| 2003 | Low | Recombinant human ARHGAP6 isoform 4 was expressed as a soluble His-tagged fusion protein and purified to near homogeneity, providing a biochemical tool; expression in standard E. coli strains caused cell lysis, resolved by using a strain lacking small heat-shock proteins IbpA/IbpB. | PMID:12673365 | Acta biochimica Polonica |
| 2015 | Medium | ARHGAP6 physically interacts with Rac3 (Ras-related C3 botulinum toxin substrate 3), identifying Rac3 as a target of ARHGAP6 in cervical carcinoma cells, and overexpression of ARHGAP6 inhibits proliferation, migration, invasion, and adhesion while inducing apoptosis and G0/G1 arrest. | PMID:26628301 | Tumour biology |
| 2019 | Medium | ARHGAP6 upregulation in lung cancer cells suppresses IL-6-induced migration, invasion, and expression of MMP9 and VEGF, and reduces phospho-STAT3 levels without affecting total STAT3, placing ARHGAP6 upstream of STAT3 signaling in lung cancer cells. | PMID:30816546 | Oncology reports |
| 2020 | Medium | ARHGAP6 promotes apoptosis and inhibits glycolysis in DDP-resistant lung adenocarcinoma cells through suppression of the STAT3 signaling pathway (elevated p-STAT3 upon ARHGAP6 loss), and restoring ARHGAP6 re-sensitizes cells to cisplatin in vitro and in vivo. | PMID:33116826 | Cancer management and research |
| 2021 | Medium | miR-96-5p directly targets the ARHGAP6 3′UTR to repress its expression, as verified by dual-luciferase reporter assay; restoration of ARHGAP6 reverses the pro-tumorigenic effects of miR-96-5p on LUAD cell proliferation, migration, and invasion. | PMID:34338998 | Journal of applied genetics |
| 2023 | Medium | miR-152-5p directly binds ARHGAP6 mRNA (verified by dual-luciferase reporter assay) and its mimics inhibit ARHGAP6 expression and downstream ROCK2 activation in cardiomyocytes, linking the miR-152-5p/ARHGAP6/ROCK2 axis to apoptosis and fibrosis in the context of myocardial infarction. | PMID:36936709 | Experimental and therapeutic medicine |
| 2023 | Low | ARHGAP6 overexpression in bladder cancer cells decreases viability, migration, and invasion and modulates β-catenin signaling, and influences sensitivity to mitomycin C treatment. | PMID:36715867 | Human cell |
| 2024 | Medium | ARHGAP6 promotes ferroptosis in breast cancer cells by inhibiting RhoA/ROCK1 signaling, which in turn suppresses p38 MAPK signaling; ROCK1 inhibition compromised ARHGAP6's effect on p38 MAPK, and p38 inhibition reversed the ferroptosis effect of ARHGAP6 knockdown, placing ARHGAP6 upstream of RhoA-ROCK1-p38 MAPK in ferroptosis regulation. | PMID:38287795 | Frontiers in bioscience (Landmark edition) |
| 2025 | Medium | The transcription factor ZBTB6 directly binds the ARHGAP6 promoter to repress its transcription, as established by ChIP-qPCR and luciferase reporter assay; ARHGAP6 overexpression counteracts ZBTB6-driven activation of STAT3 signaling in breast cancer cells. | PMID:40133895 | Journal of translational medicine |

## Citations

- PMID:10699171
- PMID:12673365
- PMID:26628301
- PMID:30816546
- PMID:33116826
- PMID:34338998
- PMID:36715867
- PMID:36936709
- PMID:38287795
- PMID:40133895
- PMID:9417914
