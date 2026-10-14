# akt-1 (Q17941) review notes

Deep research: falcon run failed (timeout/connection reset; perplexity fallback unavailable). Review based on cached publications, UniProt and PubMed.

## Key findings
- Indispensable for DAF-2 signalling, antagonises DAF-16 [PMID:9716402 "A loss-of-function mutation in the Fork head transcription factor DAF-16 relieves the requirement for Akt/PKB signaling, which indicates that AKT-1 and AKT-2 function primarily to antagonize DAF-16."]
- Kinase complex and DAF-16 phosphorylation [PMID:15068796 "All three kinases of this complex are able to directly phosphorylate DAF-16/FKHRL1, yet have different functions in DAF-2 signaling."]
- SKN-1 phosphorylation [PMID:18358814 "The IIS kinases AKT-1, -2, and SGK-1 phosphorylate SKN-1, and reduced IIS leads to constitutive SKN-1 nuclear accumulation in the intestine and SKN-1 target gene activation."]
- PIP3 binding / membrane recruitment [PMID:25383666 "suggesting that AKT-1-PH::GFP translocated to the plasma membrane through binding to PIP3 (Fig."]
- Anti-apoptotic, cep-1-dependent [PMID:17276923 "The antiapoptotic activity of akt-1 is independent of its target gene daf-16 but dependent on cep-1/p53."]

## Curation decisions
- Protein binding rows: substrates (DAF-16, MDF-1) REMOVE; kinase partners (SGK-1, AKT-2) -> protein kinase binding; PPTR-1 -> protein phosphatase 2A binding.
- p53-class DNA-damage apoptosis IMP -> negative regulation (GO:1902166).
- IBA positive regulation of blood vessel endothelial cell migration REMOVE (no vasculature in nematodes).
