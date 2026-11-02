---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB8
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9H765
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB8 (human)

## Current model (mechanistic narrative)

ASB8 is a cytoplasmic CRL5 substrate-receptor E3 ubiquitin ligase that controls the stability of multiple regulatory proteins by directing their ubiquitination [PMID:12559969, PMID:36731340]. It is built from four ankyrin repeats, which engage substrates, and a C-terminal SOCS box that recruits the Elongin B-C complex to nucleate the Cullin-RING ligase; this SOCS box is required for its pro-growth activity in lung adenocarcinoma cells [PMID:12559969, PMID:12796816]. As a CRL5 substrate receptor, ASB8 promotes K48-linked polyubiquitination and proteasomal degradation of its targets, most strikingly the nuclear export factor XPO1: cryo-EM shows ASB8 binds a cryptic XPO1 surface that is exposed allosterically only after the export protein is conjugated by SINE compounds such as selinexor or by the endogenous metabolite 4-octyl itaconate, thereby triggering degradation [PMID:36731340, PMID:41286136, PMID:39416201]. ASB8 likewise degrades estrogen receptor beta via K48-linked ubiquitination, and its loss stabilizes ERβ and promotes lung adenocarcinoma lymph node metastasis [PMID:40739091]. In antiviral signaling, ASB8 degrades the kinases IKKβ, TBK1, and IKKi through K48-linked ubiquitination to dampen NF-κB and IRF3/IFN-β responses, while conversely catalyzing K63-linked ubiquitination of the PRRSV protein Nsp1α to stabilize it and boost viral replication; this activity is tuned by phosphorylation at Ser17 and Ser31 [PMID:31009856, PMID:32298923].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-168256 Immune System
- **partners:** XPO1, IKBKB, TBK1, IKBKE, LRRC10B, ESR2, ELOB, ELOC
- **complexes:** CRL5 (Cullin5-RING ligase), Elongin B-C

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Medium | ASB8 protein contains four ankyrin repeats and one SOCS box; it localizes to the cytoplasm (EGFP-tagged, in BEL-7402 cells); and it interacts with the Elongin B-C complex in vitro, consistent with a role in Cullin-RING E3 ligase assembly. | PMID:12559969 | Biochemical and biophysical research communications |
| 2003 | Medium | Expression of a SOCS box-deficient ASB8 mutant (ASB-8 SB) suppressed growth of lung adenocarcinoma SPC-A1 cells in vitro and in vivo (nude mouse tumor formation), indicating the SOCS box is required for ASB8's pro-growth function, likely through its E3 ligase activity. | PMID:12796816 | Sheng wu hua xue yu sheng wu wu li xue bao Acta biochimica et biophysica Sinica |
| 2019 | Medium | Porcine ASB8 interacts with PRRSV Nsp1α and promotes K63-linked ubiquitination of Nsp1α, increasing its stability and boosting PRRSV replication. Simultaneously, ASB8 is phosphorylated at N-terminal Ser-31 by host IKKβ, and in turn ASB8 promotes K48-linked ubiquitination and proteasomal degradation of IKKβ, suppressing NF-κB signaling. | PMID:31009856 | Virology |
| 2020 | Medium | ASB8 interacts with TBK1 and IKKi, promotes their K48-linked ubiquitination and proteasomal degradation, thereby reducing IRF3 phosphorylation and IFN-β production. Phosphorylation of ASB8 at Ser17 enhances its ubiquitination activity. A bridge molecule LRRC10B, upregulated after viral infection, participates in the ASB8–TBK1/IKKi complex. | PMID:32298923 | Molecular immunology |
| 2023 | Medium | ASB8 acts as a CRL5 substrate receptor that promotes selinexor-induced proteasomal degradation of XPO1; both ASB8 knockout and overexpression result in selinexor hypersensitivity, indicating ASB8 modulates XPO1 protein stability in the context of SINE drug treatment. | PMID:36731340 | Biomedicine & pharmacotherapy |
| 2025 | High | Cryo-EM structures reveal that ASB8 binds to a cryptic site on XPO1 that becomes exposed only upon SINE (e.g., selinexor) conjugation; this interaction is allosteric—SINEs bind XPO1 without directly contacting ASB8—and leads to CRL5-ASB8-mediated K48-linked ubiquitination and proteasomal degradation of XPO1. The endogenous itaconate derivative 4-octyl itaconate triggers the same ASB8-mediated degradation, suggesting exploitation of a native cellular mechanism. | PMID:41286136, PMID:39416201 | Nature chemical biology |
| 2025 | Medium | ASB8, acting as an E3 ubiquitin ligase, degrades estrogen receptor beta (ERβ) through K48-linked polyubiquitination; low ASB8 expression increases ERβ stability and promotes lung adenocarcinoma lymph node metastasis. | PMID:40739091 | Cell death & disease |
| 2021 | Low | MiR-452 directly targets ASB8 mRNA; overexpression of miR-452 downregulates ASB8 mRNA and protein levels in colorectal cancer cells, as confirmed by luciferase reporter assay. | PMID:33398662 | Genes & genomics |

## Citations

- PMID:12559969
- PMID:12796816
- PMID:31009856
- PMID:32298923
- PMID:33398662
- PMID:36731340
- PMID:39416201
- PMID:40739091
- PMID:41286136
