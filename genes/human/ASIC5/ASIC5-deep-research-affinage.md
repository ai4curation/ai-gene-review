---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASIC5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NY37
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASIC5 (human)

## Current model (mechanistic narrative)

ASIC5 (also termed hINaC, BLINaC, and BASIC) is a member of the DEG/ENaC superfamily that functions as an amiloride-sensitive Na+ channel which is inactive at rest and, unlike other ASICs, is not gated by protons [PMID:10767424]. Heterologous expression established its channel identity: wild-type hINaC is electrically silent, but gain-of-function point mutations unmask robust amiloride-sensitive (IC50 ~0.5 µM) Na+ currents, indicating the protein requires an unknown physiological activator [PMID:10767424]. That activator was identified as bile acids, with chenodeoxycholic and hyodeoxycholic acids activating both rat and human channels and motivating the name BASIC (bile acid-sensitive ion channel) [PMID:22735174]. Consistent with this ligand, the channel localizes to cholangiocytes lining bile ducts [PMID:22735174]. In the nervous system, ASIC5 has a highly restricted expression pattern, confined to mGluR1α+ (calretinin-negative) type II unipolar brush cells of the vestibulocerebellum [PMID:24663811]. There it sets intrinsic excitability: global Asic5 knockout mice develop cerebellar ataxia with impaired motor coordination, and loss of the channel slows the maximum depolarization rate, reduces spontaneous firing, and alters delayed hyperpolarizing K+ currents and glutamate-triggered burst firing in type II UBCs [PMID:32034189]. Beyond bile acids, no short-neuropeptide agonist of ASIC5 has been found in systematic screening [PMID:30573735].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005215 transporter activity, GO:0060089 molecular transducer activity, GO:0140299 molecular sensor activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-382551 Transport of small molecules
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | hINaC (human ASIC5) was molecularly cloned from human small intestine and found to be inactive at rest — not activated by lowering external pH. However, gain-of-function point mutations introduced into hINaC revealed robust amiloride-sensitive Na+ channel activity (IC50 ~0.5 µM amiloride) when expressed in Xenopus oocytes, demonstrating the protein is a functional Na+ channel requiring an unknown physiological activator. The hINaC gene was mapped to chromosome 4q31.3-q32. | PMID:10767424 | FEBS letters |
| 2012 | High | BLINaC (rat ortholog of ASIC5/hINaC) protein localizes to cholangiocytes (epithelial cells lining bile ducts). Both rBLINaC and human INaC (ASIC5) are robustly activated by bile acids, particularly chenodeoxycholic acid and hyodeoxycholic acid (EC50 = 2.1 ± 0.05 mM), identifying bile acids as physiological activators of this channel. On this basis the channel was renamed BASIC (bile acid-sensitive ion channel). | PMID:22735174 | FASEB journal |
| 2013 | Medium | BASIC/ASIC5 (previously BLINaC/INaC) is confirmed as a third subgroup within the DEG/ENaC family, sharing ligand-gated activation with ASICs and epithelial localization with ENaC. Pharmacological characterization and identification of bile acids as putative natural activators are reviewed, with species differences noted between rat and human orthologs. | PMID:24365967 | Channels (Austin, Tex.) |
| 2014 | High | Asic5 is restrictively expressed in the brain specifically in unipolar brush cells (UBCs) of the vestibulocerebellum (ventral uvula and nodulus), particularly in the subset of UBCs that express metabotropic glutamate receptor 1α (mGluR1α) but not calretinin. Single-cell RT-PCR and electrophysiological recordings of these cells confirmed Asic5 expression and UBC identity. | PMID:24663811 | PloS one |
| 2018 | Medium | A screen of 109 neuropeptides on five homomeric ASICs including BASIC (ASIC5) revealed no direct agonists of BASIC. None of the tested short neuropeptides directly activated ASIC5/BASIC channels. | PMID:30573735 | Scientific reports |
| 2020 | High | Global knockout of Asic5 in mice causes cerebellar ataxia with impaired motor coordination. Brain slice electrophysiology showed that Asic5 deletion decreased intrinsic excitability of type II UBCs by slowing the maximum depolarization rate and reducing spontaneous action potential firing. Loss of Asic5 also altered delayed hyperpolarizing K+ currents and burst firing properties triggered by glutamate in type II UBCs, demonstrating that Asic5 is required for normal type II UBC activity and vestibular processing. | PMID:32034189 | Scientific reports |
| 2016 | Low | The ASIC/ENaC superfamily including ASIC5 shares a common structural architecture with two transmembrane segments (TM1, TM2) and a large extracellular domain, forming trimeric channels. ASICs can function as homo- or heterotrimers. Comparative structural modeling based on ASIC1 crystal structures in desensitized and open states was used to infer the selectivity filter and conformational changes responsible for channel gating relevant to all ASIC family members including ASIC5. | PMID:27580245 | The FEBS journal |
| 2021 | Low | Whole-genome sequencing of a family with recurrent pregnancy loss identified a novel homozygous exonic variant (c.680G>T, p.R227I) in ASIC5. Molecular docking and interaction analysis predicted that this substitution is highly pathogenic, decreases protein stability, and prevents binding of amiloride (described as an activator to open the ASIC5 channel), suggesting ASIC5 channel function is required for fetal viability. | PMID:34395479 | Frontiers in medicine |

## Citations

- PMID:10767424
- PMID:22735174
- PMID:24365967
- PMID:24663811
- PMID:27580245
- PMID:30573735
- PMID:32034189
- PMID:34395479
