# MVD1 / ERG19 (YNR043W) notes

UniProt P32377; diphosphomevalonate decarboxylase, EC 4.1.1.33; homodimer [UniProt:P32377].

## Evidence journal
- Cloned/expressed: [PMID:8626466 "We also cloned and expressed the yeast homolog using the human enzyme's similarity to a previously unidentified and incomplete genomic sequence."]
- Active site: [PMID:15169949 "support assignment of a crucial catalytic role to Asp 302"]; K18M raises Km(ATP).
- Mutants: [PMID:1779710 "Yeast mutant strains auxotrophic for ergosterol and blocked in mevalonate diphosphate decarboxylase (erg19) and farnesyl diphosphate (FPP) synthetase (erg20) were isolated."]
- Essential, overexpression lowers sterols [PMID:9244250 "a high level of expression of the wild-type ERG19 gene led to a lower sterol steady-state accumulation compared to that of a wild-type strain"].

## Decisions
- Vacuole NAS (Hu et al. 2017 review) REMOVE. Carboxy-lyase IEA MODIFY -> GO:0004163. Rest ACCEPT.

## 2026-11-24: vacuole NAS query to UniProt

The is_active_in vacuole NAS row (PMID:28904410, Hu et al. 2017 review) now carries a UniProt WRONG_TERM CHECK source defect (PROBABLE). It is one of the 2022-02-18 batch UniProt made from that review on ERG10, ERG8, MVD1, ERG20 and IDI1; the ERG10 review already queries the batch, and each entry now records it. The cached PMC text of the review does not mention the vacuole, so the claim was not read in context, which is why this is a query and not a deletion request.
