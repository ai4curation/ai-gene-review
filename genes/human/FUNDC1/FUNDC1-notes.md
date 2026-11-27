# FUNDC1 notes

Deep research was not run: falcon times out in this environment and perplexity-lite is not installed. These notes are based on the cached publications and the UniProt record.

## Core biology
- An integral mitochondrial outer-membrane receptor for hypoxia-induced mitophagy [PMID:22267086 "Here we report that FUNDC1, an integral mitochondrial outer-membrane protein, is a receptor for hypoxia-induced mitophagy."]
- Binds LC3 through an N-terminal LIR, which is required for mitophagy [PMID:22267086 "FUNDC1 interacted with LC3 through its typical LC3-binding motif Y(18)xxL(21), and mutation of the LC3-interaction region impaired its interaction with LC3 and the subsequent induction of mitophagy."]
- Regulated by phosphorylation: ULK1 phosphorylates Ser17 [PMID:24671035 "The translocated ULK1 interacts with its substrate FUNDC1 and phosphorylates FUNDC1 at Ser-17."]
- Acts as a DRP1 adaptor at MAMs [PMID:27145933 "FUNDC1 is not only a novel MAM protein that acts as an adaptor for DRP1 during the mitochondrial fission process, but also involved in hypoxia‐induced mitophagy."], and is stabilized there by USP19 [PMID:33978709].

## Curation decisions
- Protein binding rows with LC3 partners from PMID:22267086 were changed (MODIFY) to GO:0140580. All other protein binding rows were removed.
- The mitochondrial fusion IGI (PMID:37931419, abstract only) was left UNDECIDED, because the abstract describes Drp1-dependent fission.
- Three NEW annotations: GO:0090141 positive regulation of mitochondrial fission, GO:0044233 MAM contact site, and GO:0043495 protein-membrane adaptor activity, all from PMID:27145933 and PMID:33978709.
