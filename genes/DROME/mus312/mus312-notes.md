# mus312 review notes

## Session 1 (2026-10-28)
- `just fetch-gene DROME mus312` resolved Q9VS48 (SLX4_DROME, FlyBase FBgn0002909, GeneID 38809); 21 GOA rows. First two fetch attempts timed out at rest.uniprot.org; succeeded on retry.
- Papers read in full text: PMID:19595722, PMID:19596236, PMID:15944364, PMID:22022278, PMID:25205745. Abstract only: PMID:12504024, PMID:18957704. Extra context cached: PMID:18957705, PMID:21205937.
- Literature synthesis with provenance in `mus312-deep-research-manual.md` (manual; no deep-research provider used).

## Decisions
- Protein binding rows (MEI-9, SLX1 partners) -> MODIFY to GO:0030674 protein-macromolecule adaptor activity [PMID:25205745 "MUS312 is a scaffolding protein that interacts physically and functionally with both MEI-9 (the Drosophila ortholog of Rad1/XPF) and SLX1"], consistent with the human SLX4 review.
- Oocyte fate determination (IMP, PMID:18957704) -> MARK_AS_OVER_ANNOTATED: checkpoint-mediated delay shared by all crossover-defective mutants, suppressed by pch2.
- DNA replication (InterPro2GO) -> MARK_AS_OVER_ANNOTATED.
- DNA metabolic process (ARBA) -> MODIFY to DNA repair + resolution of meiotic recombination intermediates.
- Meiotic chromosome segregation -> KEEP_AS_NON_CORE (downstream of crossover loss).
- Interstrand cross-link repair: supported by HN2 hypersensitivity plus orthology to SLX4/FANCP, but per the strict NEW bar (mutant phenotype only; Drosophila partner nuclease unknown) no NEW row was added; raised as a suggested question.
