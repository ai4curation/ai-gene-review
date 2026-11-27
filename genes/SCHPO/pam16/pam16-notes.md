# pam16 review notes

## 2026-11-25 GO-CAM 69729a3800007453

Reviewed pam16 for the `69729a3800007453` S. pombe protein-import model.
Falcon and the Perplexity fallback were unavailable, so the review uses cached
UniProt, GOA, PTHR12388 PAINT, Matsuyama et al. S. pombe localization evidence
(PMID:16823372), Hutu et al. budding-yeast PAM/J-complex evidence
(PMID:18400944), and the cached human PAM16 orthology literature
(PMID:19564938, PMID:20053669, PMID:23263864).

The gene-level review agrees with the model that pam16 is a PAM-complex
component involved in `GO:0030150` protein import into the mitochondrial matrix,
but disagrees with the model activity `gomodel:69729a3800007453/6994852c00000361`
on two points to carry into the final GO-CAM consistency PR:

- `GO:0140388` protein translocation chaperone activity describes ATP-dependent
  vectorial pulling by the Hsp70 motor and fits Ssc1 rather than the J-like
  Pam18 regulator Pam16.
- The GO-CAM ISO `enabled_by` evidence cites malformed `SGD:SS000005758`; the
  corresponding valid SGD identifier, `SGD:S000005758`, resolves to MGE1/YOR232W,
  while S. cerevisiae PAM16 is `SGD:S000003640`.
