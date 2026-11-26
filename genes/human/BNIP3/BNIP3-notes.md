# BNIP3 notes

Deep research was not run: falcon times out in this environment and perplexity-lite is not installed. These notes are based on the cached publications and the UniProt record.

## Core biology
- An LC3-binding autophagy receptor for mitochondria and ER [PMID:22505714 "Our data indicate that Bnip3 regulates the apoptotic balance as an autophagy receptor that induces removal of both mitochondria and ER."]
- The LIR is needed for mitophagy and ER-phagy but not for pro-death activity [PMID:22505714 "Although ablation of the Bnip3-LC3 interaction by mutating the LC3 binding site did not impair the prodeath activity of Bnip3, it significantly reduced both mitophagy and ERphagy."]
- Homodimerizes through its TM domain, which is required for autophagy [PMID:22505714].
- With BNIP3L, required for hypoxia-induced autophagy [PMID:19273585 "the combined silencing of these two HIF targets suppresses hypoxia-mediated autophagy"].
- Cell death is necrosis-like and goes through the PT pore [PMID:10891486 "We propose that BNIP3 is a gene that mediates a necrosis-like cell death through PT pore opening and mitochondrial dysfunction."]

## Curation decisions
- Cell-death terms were kept as non-core.
- Positive regulation of mitochondrial fission (PMID:20436456) was marked as over-annotated, because the paper attributes fragmentation to inhibition of OPA1-mediated fusion.
- Two annotations were left UNDECIDED. Defence response to virus (PMID:9973195, a BNIP3alpha/BNIP3L paper, abstract only) shows only binding by viral anti-apoptotic proteins. For cellular response to mechanical stimulus (PMID:19593445, a BAD paper), BNIP3 is not mentioned in the cached text.
- GO:0061753 is labelled obsolete by GOA, and the IEA row was removed.
- All 84 protein binding rows were removed.
