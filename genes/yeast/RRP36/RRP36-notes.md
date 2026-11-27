# RRP36 (YOR287C, Q12481) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: yeast RRP36 is the experimental donor (SGD:S000005813) for PAINT node
PTN000497661 (PANTHER PTHR21738:SF0, the only subfamily of the family), from which
the S. pombe rrp36 IBA rows were propagated. No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon yeast RRP36 --fallback perplexity-lite`
failed (falcon: "Failed to authenticate"; perplexity: HTTP 401 insufficient quota).
The review is based on literature read directly from the publication cache.
PMID:20038530 was re-fetched with force=True and now has full text (PMC2820894).

### Experimentally established in S. cerevisiae
- Nucleolar, with a low nucleoplasmic pool [PMID:20038530 "We conclude that Rrp36p accumulates predominantly in yeast cell nucleoli."; "Rrp36p-3HA is present at low levels in the nucleoplasmic area"].
- 90S preribosome component; co-IP of 35S, 33S/32S pre-rRNA and U3; weaker pre-40S association [PMID:20038530 "These interactions suggest that Rrp36p is a component of the 90S preribosomal particles"; "Rrp36p seems also to interact to a lesser extent with pre-40S particles containing the 23S and 20S intermediates"].
- Preferential UTP-C association [PMID:20038530 "suggesting that Rrp36p may be preferentially associated with the UTP-C module"].
- Recruitment requires UTP-A and UTP-B, not Rrp5 [PMID:20038530 "Together, these data suggest that Rrp36p recruitment to nascent preribosomes requires prior loading of the UTP-A and UTP-B subcomplexes."].
- Depletion blocks A0/A1/A2, 18S-specific [PMID:20038530 "We conclude that Rrp36p is specifically required for early cleavages of the 35S pre-rRNA at sites A 0 , A 1 , and A 2 in the processing pathway leading to the mature 18S rRNA and the production of the 40S ribosomal subunit."].
- Direct contacts with Rrp9 and Rrp5 (GST pull-down); unmapped in cryo-EM [PMID:31996908 "As shown by GST pull-down assays, interactions of Rrp36 (A) and the C-terminal domain of Sgd1 (B) with Rrp9 are direct interactions."; "some SSU-processome proteins remain unmapped, including Rrp36 and Sgd1 for which no 3D structures are established"].

### Inferred / conserved
- Human RRP36 (C6orf153) is nucleolar and required for 18S production in HeLa cells [PMID:20038530 "Altogether, our results show that the function of RRP36 in the production of the mature 18S rRNA has been conserved from yeast to human cells"]. Same PANTHER subfamily (PTHR21738:SF0), so the IBA node placement is sound.
- No molecular function is established; no catalytic motif [PMID:20038530 "These conserved blocks do not correspond to any recognizable protein motif"]. Rrp36 should not receive endonucleolytic-cleavage terms: it is required for the cleavages but there is no evidence it catalyses them; PAINT propagated GO:0000462 only.

### Decisions
- GO:0000462 (IBA, IMP), nucleolus (IBA/IDA/IEA), 90S preribosome (IBA/IDA), GO:0042274 IMP: ACCEPT.
- GO:0006364 rRNA processing IMP: MODIFY -> GO:0000462 (60S rRNAs unaffected).
- GO:0005654 nucleoplasm (Reactome TAS): KEEP_AS_NON_CORE.
- GO:0003674 ND: ACCEPT (no activity known).
- 20 x GO:0005515 IPI: REMOVE per protein-binding policy; content captured by 90S preribosome.
- Considered but not added: GO:0030688 pre-40S (association only ~1% of 20S co-IP; weak) and GO:0032040 small-subunit processome (redundant in practice with the accepted 90S preribosome term).
