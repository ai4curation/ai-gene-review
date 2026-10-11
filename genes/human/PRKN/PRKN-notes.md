# PRKN notes

Deep research was not run: falcon times out in this environment and perplexity-lite is not installed. These notes are based on the 96 cached publications and the UniProt record.

## Core biology
- A RING-type (RBR) E3 that binds UbcH7/UbcH8 [PMID:10973942 "Here, we show that Parkin is a RING-type E3 ubiquitin-protein ligase which binds to E2 ubiquitin-conjugating enzymes, including UbcH7 and UbcH8, through its RING-IBR-RING motif."]
- C431 is the catalytic cysteine and is needed for mitophagy [PMID:23770887].
- Activated by PINK1 through phospho-Ser65 ubiquitin [PMID:24660806, PMID:24751536] and phosphorylation of Ser65 in its Ubl [PMID:23754282].
- Recruited to depolarized mitochondria, where it drives mitophagy [PMID:19029340 "Here, we show that Parkin is selectively recruited to dysfunctional mitochondria with low membrane potential in mammalian cells."]
- Builds K6, K11 and K63 chains on mitochondria, which USP30 opposes [PMID:25621951].
- Many non-mitochondrial substrates: Pael-R [PMID:11439185], PARIS [PMID:21376232], Fbw7beta [PMID:23858059], RIPK3 [PMID:31358971], NEMO via LUBAC [PMID:23453807]. These were kept as non-core.

## Curation decisions
- Neuronal and synaptic IEA locations and neuroprotection processes were kept as non-core. Stress-response IEAs transferred from rodent studies were marked as over-annotated.
- Protein deubiquitination (Reactome TAS) was removed, because Parkin is a substrate of DUBs and does not carry out deubiquitination.
- The midnolin paper (PMID:24187134) reports only an overexpression effect on insulin secretion and glucokinase, so these annotations were marked as over-annotated.
- Host-mediated suppression of viral genome replication (PMID:25244949, abstract only) was left UNDECIDED. The abstract implies Parkin supports HCV propagation.
- All 77 protein binding rows were removed.
