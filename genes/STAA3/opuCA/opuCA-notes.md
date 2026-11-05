# opuCA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

Gene source uses opuCa; the literature uses opuCA. The direct transport data resolve carnitine versus glycine-betaine/choline claims in the tested USA300 strain. The whole transporter MF is recorded only as a complex contribution. c-di-AMP-sensitive ATPase coupling is an experimental question, not a demonstrated mechanism.

Falcon deep research was attempted using `just deep-research-falcon STAA3 opuCA` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:27531650](https://pubmed.ncbi.nlm.nih.gov/27531650/): Cyclic di-AMP binds the paired CBS region of OpuCA. "c-di-AMP binds specifically to the C-terminal CBS domains of the S. aureus OpuCA protein"
- [PMID:27531650](https://pubmed.ncbi.nlm.nih.gov/27531650/): OpuCA is required for carnitine uptake in the tested USA300 strain. "accumulation of radiolabelled carnitine was only observed in the WT and opuCA complementation strains but not in the ΔopuCA strain"
- [PMID:27531650](https://pubmed.ncbi.nlm.nih.gov/27531650/): Glycine-betaine uptake was unaffected by OpuCA deletion under the tested conditions. "radiolabelled glycine betaine was taken up at a similar rate by the WT, ΔopuCA, and opuCA complementation strains"
- [PMID:27531650](https://pubmed.ncbi.nlm.nih.gov/27531650/): Purified OpuCA displayed weak ATPase activity insensitive to c-di-AMP. "the protein had very weak ATPase activity, which was not sensitive to the concentration of c-di-AMP."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

## 2026-11-04 — PR #5997 review follow-up

Rechecked the binding recommendation: the existing nucleotide-binding MODIFY already proposes GO:0180001, so an additional NEW row would be redundant. Corrected the authored HTTP status formatting. The carnitine-uptake result and absence of a demonstrated direct ATPase response remain unchanged.
