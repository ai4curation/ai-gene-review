# CDH23 notes

## 2026-06-02

PITA context: CDH23 corresponds to PITA5 / pituitary adenoma 5, multiple types. UniProt notes that PITA5 includes GH-, PRL-, ACTH-, TSH-secreting and plurihormonal tumors and that familial transmission is consistent with autosomal dominant inheritance with reduced penetrance [file:human/CDH23/CDH23-uniprot.txt "PITA5 is consistent with autosomal dominant inheritance with reduced penetrance"].

Deep research status: `just deep-research-falcon human CDH23 --fallback perplexity-lite` timed out on Falcon after 600 seconds, and the fallback failed with a Perplexity quota error. I proceeded using fetched UniProt, GOA, and cached publications.

Functional summary: CDH23 is a cadherin-family adhesion protein whose best-supported normal function is in stereocilia/hair-bundle architecture. UniProt states that "Cadherins are calcium-dependent cell adhesion proteins" and that CDH23 is required for "proper organization of the stereocilia bundle" [file:human/CDH23/CDH23-uniprot.txt "Cadherins are calcium-dependent cell adhesion proteins."; file:human/CDH23/CDH23-uniprot.txt "proper organization of the stereocilia bundle of hair cells"]. Experimental evidence shows cadherin 23 is present in growing stereocilia and binds harmonin [PMID:12485990 "cadherin 23 are both present in the growing stereocilia and that they bind to each other"], and CDH23/PCDH15 maintain normal stereocilia bundle organization [PMID:15537665 "CDH23 and PCDH15 play an essential long-term role in maintaining the normal organization of the stereocilia bundle"].

Annotation decisions: I accepted cadherin adhesion, calcium binding, membrane/stereocilium localization, and sensory phenotypes as supported, with sensory phenotypes kept non-core where they are phenotype-level consequences. I removed the calcium ion transport annotation because the cited PMCA2 paper describes stereociliary calcium entry/export biology rather than CDH23 transporter activity [PMID:17234811 "Ca2+ enters the stereocilia of hair cells through mechanoelectrical transduction channels"; PMID:17234811 "exported back to endolymph by an unusual splicing isoform"].

