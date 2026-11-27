---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADM5
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: C9JUS6
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

# Affinage mechanistic annotation for ADM5 (human)

## Current model (mechanistic narrative)

ADM5 (adrenomedullin 5) is an evolutionarily ancient member of the calcitonin gene-related peptide (CGRP)/adrenomedullin peptide family that functions as a secreted regulator of cardiovascular, fluid, and neuroendocrine homeostasis [PMID:17092606, PMID:21436721]. The mature peptide is encoded in the middle of its prohormone and carries signals for intramolecular ring formation and C-terminal amidation characteristic of this peptide family [PMID:18434369]. In non-mammalian vertebrates, AM5 signals through the calcitonin receptor-like receptor complexed with RAMP3 (CLR-RAMP3): this complex generates cAMP in response to AM5 in teleost fish [PMID:16195494] and drives CRE-luciferase reporter activity in amphibian receptor-expressing cells [PMID:33711314]. In mammals, AM5 produces a vasodepressor response and reduced peripheral resistance with increased heart rate, cardiac output, renin activity, and natriuresis when infused peripherally, including in heart failure models, whereas central (intracerebroventricular) administration is vasopressor and activates oxytocin-secreting neurons of the hypothalamic supraoptic and paraventricular nuclei to raise plasma oxytocin [PMID:18434369, PMID:19420012, PMID:21436721, PMID:22087608]. The mammalian receptor for AM5 remains unidentified: no combination of CLR or CTR with RAMP1–3 responds to AM5 in cell-based cAMP assays, and central oxytocin induction is only partially blocked by CGRP and AM receptor antagonists, indicating signaling through an as-yet-undefined receptor [PMID:18434369, PMID:19420012]. AM5 is differentially expressed across tissues including spleen, thymus, liver, and kidney, and its expression in fish is modulated by salinity, consistent with a role in osmoregulation [PMID:18434369, PMID:26605057].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** CALCRL, RAMP3
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | Medium | Comparative genomic analysis revealed that AM5 is an ancestral member of the calcitonin gene-related peptide (CGRP)/adrenomedullin family. In teleost fish, AM5 was located on a proto-chromosome before teleost genome duplication. In mammals, a novel AM5 gene was identified in several mammalian species (primates, carnivores, ungulates) but could not be found in rodents. In primates, nucleotide deletion occurred in the mature AM5 sequence during transition from rhesus monkey to anthropoids (human and chimp). | PMID:17092606 | Peptides |
| 2005 | Medium | In pufferfish (Takifugu), AM5 signals through the calcitonin receptor-like receptor (CLR1) complexed with RAMP3 to generate cAMP in COS7 cells at physiological concentrations, establishing CLR1-RAMP3 as a functional receptor complex for AM5 in teleosts. | PMID:16195494 | American journal of physiology. Regulatory, integrative and comparative physiology |
| 2008 | Medium | Porcine AM5 was cloned; the mature AM5 peptide is localized in the middle of the prohormone with signals for intermolecular ring formation and C-terminal amidation. The AM5 gene is expressed most abundantly in spleen and thymus. Intravenous AM5 in rats caused dose-dependent decreases in arterial pressure (vasodepressor effect, ~half the potency of AM). In contrast, intracerebroventricular AM5 increased arterial pressure and heart rate. Critically, AM5 did not activate any combination of CLR or CTR with RAMPs (1–3) to produce cAMP in cultured cells, indicating it acts on an as-yet-unknown receptor distinct from CLR/CTR+RAMP. | PMID:18434369 | The Journal of endocrinology |
| 2009 | Medium | Central (ICV) administration of AM5 in conscious rats activated oxytocin (OXT)-secreting neurons in the supraoptic nucleus (SON) and paraventricular nucleus (PVN) of the hypothalamus, evidenced by Fos-like immunoreactivity predominantly co-localizing with OXT (not AVP) neurons. Plasma OXT levels rose significantly within 5 min and remained elevated at 15 and 30 min without changes in plasma AVP. c-fos gene induction in SON/PVN was significantly but incompletely reduced by combined pretreatment with CGRP antagonist CGRP-(8-37) and AM receptor antagonist AM-(22-52), suggesting partial mediation through AM/CGRP receptors. | PMID:19420012 | The Journal of endocrinology |
| 2009 | Low | In cyclostomes (hagfish, lamprey) and chondrichthyes (sharks), a hybrid-type AM gene with both AM1 and AM2 characteristics was identified; an AM5-like gene was additionally detected in Squalus acanthias (spiny dogfish), expressed more specifically in the liver, suggesting AM5 emerged as a distinct lineage early in vertebrate evolution. | PMID:19616113 | Comparative biochemistry and physiology. Part B, Biochemistry & molecular biology |
| 2011 | Medium | Intravenous infusion of AM5 in normal conscious sheep produced dose-dependent reductions in mean arterial pressure and total peripheral resistance, and increases in heart rate, cardiac output, plasma renin activity, aldosterone, and cyclic AMP. Urine volume and sodium excretion were unchanged. These cardiovascular and hormonal actions are similar to those of AM and AM2, suggesting AM5 is a regulator of volume and pressure homeostasis. | PMID:21436721 | Journal of cardiovascular pharmacology |
| 2012 | Medium | In sheep with pacing-induced heart failure, IV infusion of AM5 produced dose-dependent increases in left ventricular dP/dt(max) and cardiac output, decreases in total peripheral resistance, mean arterial pressure, and left atrial pressure. AM5 increased plasma renin activity and urine volume, sodium, potassium, and creatinine excretion (natriuretic/diuretic effect), while aldosterone fell post-infusion despite raised renin activity, indicating AM5 has significant haemodynamic, endocrine, and renal actions in heart failure. | PMID:22087608 | Clinical science (London, England : 1979) |
| 2015 | Low | In Japanese medaka (Oryzias latipes), AM5 is expressed in multiple tissues with relatively high levels in liver and kidney. After transfer to seawater, AM5 expression in the brain-eye and kidney decreased, suggesting AM5 promotes hyper-osmoregulation (freshwater adaptation) and/or inhibits hypo-osmoregulation. | PMID:26605057 | Zoological letters |
| 2021 | Medium | In Xenopus tropicalis, AM5 activates the CLR-RAMP3 receptor complex: in HEK293T cells expressing Xenopus clr-ramp3, AM5 (at higher doses than AM2) increased CRE-luciferase reporter activity, establishing CLR-RAMP3 as a receptor for amphibian AM5 and extending the receptor specificity of AM5 beyond teleosts. | PMID:33711314 | General and comparative endocrinology |

## Citations

- PMID:16195494
- PMID:17092606
- PMID:18434369
- PMID:19420012
- PMID:19616113
- PMID:21436721
- PMID:22087608
- PMID:26605057
- PMID:33711314
