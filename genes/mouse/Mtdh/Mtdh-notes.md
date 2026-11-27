# Mtdh (mouse, Q80WJ7) review notes

## 2026-11-26: review started from literature-scan issue 7142

The trigger paper is PMID:42997994 (Metadherin impairs PPARalpha-mediated fatty acid oxidation in diabetic kidney disease). Only the abstract is available.

Deep research did not run: falcon returned 403 and the perplexity-lite fallback was out of quota. I searched PubMed by hand with the queries 'AEG-1 lipid homeostasis RXR' and 'LYRIC tight junction', which found PMID:26070567 (the Mtdh/AEG-1 KO mouse) and PMID:15383321 (LYRIC at tight junctions).

### What the trigger paper adds

MTDH knockdown in diabetic mouse kidney enhances PPARalpha-dependent fatty acid oxidation, and MTDH overexpression aggravates lipotoxicity in a PPARalpha-agonist-reversible way. The Mtdh-PPARalpha axis had already been published in 2015 (PMID:26070567), but GOA did not capture it. I added a NEW row, GO:0035359 negative regulation of PPAR signaling pathway (IMP), with PMID:26070567 as the primary evidence and the trigger paper as corroboration.

### Unverified rows

Fifteen rows on eight terms (8 ISO and 7 IEA, all transferred from human MTDH) were not traced to accessible evidence. They are left UNDECIDED: dsRNA binding (x2), mRNA catabolism, autophagy, LPS signalling, angiogenesis, PI3K signalling, nuclear body and intercellular canaliculus.

## 2026-11-27: changes after the PR #7151 review

- The RXR-coregulator rows (GO:0003712, GO:0000122, GO:0006357, GO:0061629) are now ACCEPT, and the core function's MF is GO:0003712 transcription coregulator activity. GO:0003714 corepressor activity is the more literal term, but the direct RXR-binding and coactivator-blocking assay is in the earlier Srivastava et al. paper, which is not cached here. GO:0003714 should be revisited once that paper is fetched.
- The Rrs1 and Snd1 protein-binding rows now have separate reasons.
- The nucleolus and ER membrane IDA rows now quote their own reference, PMID:19433866.
- Open: the LXR half of the mechanism has no annotation. No GO term for negative regulation of LXR signalling was checked.
