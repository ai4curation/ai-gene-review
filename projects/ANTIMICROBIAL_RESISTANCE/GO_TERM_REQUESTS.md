---
title: "Draft GO term requests from the ARO→GO mapping"
---

# Draft GO term requests from the ARO→GO mapping

Part of the [Antimicrobial Resistance project](../ANTIMICROBIAL_RESISTANCE.md). Each draft fills the
go-ontology new-term-request template (label, definition with references, parent, synonyms, EC/Rhea
cross-references, example gene products) for an ARO family that [`aro2go.sssom.yaml`](aro2go.sssom.yaml)
records as a GO gap (`sssom:NoTermFound`). **None has been filed**; Chris will file them on go-ontology.
Tracking issue: [ai-gene-review#7188](https://github.com/ai4curation/ai-gene-review/issues/7188).

The CARD team reviewed the first seven gaps and said it would support the requests. Vat is the same kind
of gap and is included, marked as not on CARD's list.

| Proposed GO term | ARO family | EC | CARD reviewed |
|---|---|---|---|
| [tetracycline 11a-monooxygenase activity](go_term_requests/tetracycline-monooxygenase.md) | ARO:3000036 tetracycline inactivation enzyme | EC:1.14.13.231 | yes |
| [23S rRNA (adenine(2503)-C(8))-methyltransferase activity](go_term_requests/rrna-adenine2503-c8-methyltransferase.md) | ARO:3000202 Cfr-like 23S rRNA methyltransferase | EC:2.1.1.224 | yes |
| [lincosamide nucleotidyltransferase activity](go_term_requests/lincosamide-nucleotidyltransferase.md) | ARO:3000221 lincosamide nucleotidyltransferase (LNU) | — | yes |
| [macrolide esterase activity](go_term_requests/erythromycin-esterase.md) | ARO:3000320 macrolide esterase | EC:3.1.1.- | yes |
| [streptogramin B lyase activity](go_term_requests/streptogramin-b-lyase.md) | ARO:3000376 streptogramin vgb lyase | EC:4.2.99.- | yes |
| [rifampicin ADP-ribosyltransferase activity](go_term_requests/rifampicin-adp-ribosyltransferase.md) | ARO:3000390 rifampin ADP-ribosyltransferase (Arr) | — | yes |
| [rifampicin monooxygenase activity](go_term_requests/rifampicin-monooxygenase.md) | ARO:3000445 rifampin monooxygenase | EC:1.14.13.211 | yes |
| [streptogramin A O-acetyltransferase activity](go_term_requests/streptogramin-a-acetyltransferase.md) | ARO:3000453 streptogramin vat acetyltransferase | EC:2.3.1.- | no |

A further 12 gaps are recorded in the mapping file without drafts (streptothricin acetyltransferase,
chloramphenicol phosphotransferase, macrolide glycosyltransferase, rifampicin glycosyltransferase,
rifampicin phosphotransferase, fosfomycin kinase, 5-nitroimidazole reductase, fusidic acid esterase,
capreomycin kinase, edeine acetyltransferase, bacitracin amidohydrolase, and peptidoglycan
D,D-transpeptidase for PBP2a). The A1408 16S rRNA methyltransferases are mapped to the general
`GO:0016433` for now; a site-specific term would be a natural ninth request.
