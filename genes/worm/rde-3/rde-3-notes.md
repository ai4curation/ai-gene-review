# rde-3 / mut-2 (O44768) review notes

## Provenance / process
- Fetched with `just fetch-gene worm O44768 --alias rde-3`. This is TrEMBL O44768, 441 aa, WormBase K04F10.6, the same accession as the module. Note that Preston et al. found UG-addition activity only for isoform MUT-2a [PMID:30988468 "Only CeMUT-2a exhibited UG-addition activity"].
- Deep research FAILED (falcon timeout; perplexity fallback not configured). No deep-research file was written.

## Key findings
- Poly(UG) polymerase: [PMID:30988468 "a poly(UG) polymerase, Caenorhabditis elegans MUT-2, that adds alternating uridine and guanosine nucleotides to form poly(UG) tails"].
- In vivo: [PMID:32499657 "Here we show that, in its natural context in C. elegans, RDE-3 adds pUG tails to targets of RNA interference, as well as to transposon RNAs."] and [PMID:32499657 "pUG tails promote gene silencing by recruiting RNA-dependent RNA polymerases, which use pUG-tailed RNAs (pUG RNAs) as templates to synthesize small interfering RNAs (siRNAs)."].
- Genetics: [PMID:15723801 "rde-3 is required for siRNA accumulation and for efficient RNAi in all tissues, and it is essential for fertility and viability at high temperatures"].
- Antiviral: RDE-3 pUGylates Orsay virus RNAs [PMID:41165327].

## Curation decisions
- No GO term exists for poly(UG) polymerase activity. A new term was proposed (parent GO:0098680), and the core function uses `proposed_molecular_function`. The IBA for RNA uridylyltransferase activity was accepted as correct but incomplete.
- The IBA for polyuridylation-dependent mRNA catabolic process was marked as over-annotated. pUG tails make silencing templates, which is functional divergence from the Cid1/TUT4/7-type decay function.
