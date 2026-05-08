---
provider: openai
model: gpt-5.4-mini
cached: false
start_time: '2026-04-25T18:52:42.590618'
end_time: '2026-04-25T18:53:09.196558'
duration_seconds: 26.61
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 10
---

## Question

Research human TAX1BP1 (UniProt Q86VP1) with a narrow proteostasis focus. Determine whether the strongest evidence supports selective-autophagy cargo adaptor activity, macroautophagy, xenophagy, mitophagy, or autophagosome-lysosome fusion. Keep core roles distinct from contextual innate-immune signaling functions and cite each substantive claim.

## Output

## Bottom line

For **human TAX1BP1 (UniProt Q86VP1)**, the **strongest evidence supports it as a selective-autophagy cargo adaptor / autophagy receptor**. Within that broad class, the best-supported proteostasis-related roles are **aggrephagy** and **lysophagy**. It also has well-supported roles in **xenophagy** and **mitophagy**, but these appear more **context-specific** than its core identity as a cargo adaptor. I found **no strong evidence that TAX1BP1’s primary proteostasis function is autophagosome-lysosome fusion itself**; rather, it helps recruit/organize upstream autophagy machinery and cargo. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9809930/?utm_source=openai))

## Classification, from strongest to weakest support

### 1) Selective-autophagy cargo adaptor activity — **strongest support**
TAX1BP1 is consistently described as a **selective autophagy receptor / cargo adaptor** that binds ubiquitinated cargo and LC3/GABARAP-family proteins via its ubiquitin-binding and LIR-containing regions. Reviews and mechanistic studies describe SLRs as adaptor-like proteins that tether cargo to the phagophore, and TAX1BP1 is repeatedly placed in that group. A 2024 mechanistic paper further emphasizes TAX1BP1’s interactions with **RB1CC1/FIP200** and ATG8-family proteins, reinforcing its receptor/adaptor identity rather than a late fusion factor. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9809930/?utm_source=openai))

### 2) Macroautophagy — **supported, but as a broader pathway context**
TAX1BP1 participates in **selective macroautophagy**, especially in cargo-specific autophagic sequestration. Studies show TAX1BP1 can trigger **LC3 lipidation** in reconstituted systems and can recruit the autophagy initiation machinery to cargo, which is macroautophagy-related but still in the selective-autophagy subclass. So “macroautophagy” is true in a broad sense, but it is less precise than “selective-autophagy cargo adaptor.” ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8064641/?utm_source=openai))

### 3) Lysophagy — **strong proteostasis-relevant evidence**
Among specific cargo contexts, TAX1BP1 has strong evidence for **lysophagy**. Quantitative proteomics studies found TAX1BP1 recruited to **damaged lysosomes**, and functional work showed TAX1BP1 is required for efficient lysophagic flux. The mechanism involves TAX1BP1’s **SKICH domain** and interactions with **TBK1** and **RB1CC1/FIP200**, which places it firmly in autophagy initiation around damaged lysosomes. This is one of the cleanest proteostasis phenotypes for TAX1BP1. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/34585663/?utm_source=openai))

### 4) Aggrephagy — **strong and arguably the most proteostasis-specific substrate class**
For misfolded-protein handling, TAX1BP1 has strong support in **aggrephagy**. Reviews summarize that TAX1BP1 contributes to clearance of **protein aggregates**, and 2024 work specifically describes TAX1BP1 as an **autophagy initiator** that advances aggrephagy from cargo collection to sequestration. Another recent study shows TAX1BP1 recruits **FIP200** in p62-aggregate aggrephagy. If your focus is narrow proteostasis, this is likely the most relevant substrate-specific function besides lysophagy. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9809930/?utm_source=openai))

### 5) Xenophagy — **real and well supported, but more context-dependent**
TAX1BP1 was shown to be required for clearance of **Salmonella Typhimurium** by autophagy, i.e. xenophagy, and is recruited to cytosolic bacteria. However, this function is one branch of its selective-autophagy repertoire rather than the dominant proteostasis role. It is meaningful, but not the most convincing “core” function if you are choosing one label for TAX1BP1 overall. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4599966/?utm_source=openai))

### 6) Mitophagy — **supported, but not the strongest overall identity**
TAX1BP1 is repeatedly implicated in **Parkin/PINK1-dependent mitophagy**. Reconstitution experiments used TAX1BP1 as one of the mitophagy cargo receptors capable of driving cargo-induced LC3 lipidation, and proteogenetic analyses of PARK2-dependent mitophagy identified TAX1BP1 as a receptor recruited to ubiquitinated mitochondria. That said, the mitophagy literature generally places TAX1BP1 alongside other receptors such as OPTN and NDP52, rather than uniquely emphasizing TAX1BP1. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8064641/?utm_source=openai))

### 7) Autophagosome-lysosome fusion — **weakest / not primary**
I did not find strong evidence that TAX1BP1 is a **core autophagosome-lysosome fusion factor**. Some papers mention roles in **amphisome formation** or recruitment of motor/adaptor machinery, but that is distinct from directly mediating autophagosome-lysosome fusion. The current evidence supports TAX1BP1 more as an **upstream cargo adaptor and autophagy initiator** than as a fusion executor. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9809930/?utm_source=openai))

## Distinguishing core proteostasis roles from innate-immune signaling
TAX1BP1 is also involved in **innate-immune and inflammatory signaling** pathways, including regulation of NF-κB-, TNF-, TLR-, RIG-I-, and antiviral pathways. Those functions are real, but they are **separable from its core proteostasis role** as an autophagy receptor/cargo adaptor. Reactome and reviews explicitly list TAX1BP1 as participating in inflammatory and antiviral processes **as well as** selective autophagy regulation. ([reactome.org](https://www.reactome.org/content/schema/instance/browser/uniprot%3AQ86VP1?utm_source=openai))

## Overall conclusion
If you need **one best label** for human TAX1BP1 in a proteostasis-focused analysis, choose:

**Selective-autophagy cargo adaptor / autophagy receptor**  
with strongest substrate-context evidence in **aggrephagy** and **lysophagy**, and additional evidence for **xenophagy** and **mitophagy**.  
It is **not best classified primarily as an autophagosome-lysosome fusion factor**. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9809930/?utm_source=openai))

If you want, I can turn this into a **ranked evidence table** with columns for **mechanism, substrate, assay type, and strength of evidence**.