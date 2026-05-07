# TAX1BP1 manual deep research

Generated on 2026-04-24 as a manual fallback after provider-based deep research did not produce a usable report in this worktree.

Update on 2026-04-25: a provider-generated focused OpenAI report was subsequently created at
`TAX1BP1-deep-research-openai.md`. This manual memo is retained as a fallback synthesis and
local provenance record for the earlier provider failures.

## Provenance

- Attempted `just deep-research-falcon human TAX1BP1`; the Edison/Falcon job remained active for several minutes without producing an output file.
- Attempted `just deep-research-openai human TAX1BP1`; the OpenAI deep-research job likewise remained long-running without producing an output file in a usable window.
- Attempted `just deep-research-perplexity-lite human TAX1BP1`; this failed immediately with `401 insufficient_quota`.
- This fallback memo synthesizes the locally cached publications already used for the PN-focused review.

## PN-focused conclusion

TAX1BP1 is best supported as a ubiquitin-binding selective-autophagy cargo adaptor/receptor rather than as a general signaling adaptor or a dedicated mitophagy/fusion factor.

- Xenophagy/selective-autophagy receptor function is directly supported by Salmonella and structural/autophagy-receptor studies [PMID:26451915 "Here, we demonstrate that myosin VI and TAX1BP1 are recruited to ubiquitylated Salmonella and play a key role in xenophagy."] [PMID:29940186 "TAX1BP1 may not only function as an autophagy receptor to recruit ubiquitylated substrates for autophagic degradation, but also serve as a Myosin VI cargo adaptor protein for mediating the maturation of autophagosome."] [PMID:30459273 "NDP52 and TAX1BP1, two SKIP carboxyl homology (SKICH) domain-containing autophagy receptors, play crucial roles in selective autophagy."].
- Cargo-coupled macroautophagy initiation is supported by FIP200 recruitment around ubiquitin-positive cargo [PMID:33226137 "TAX1BP1's ability to cluster FIP200 around NBR1 cargo and induce local autophagosome formation enforces cargo specificity and replaces the requirement for lipidated LC3."] [PMID:34471133 "TAX1BP1 is the main driver of FIP200 recruitment and thus the autophagic degradation of p62-ubiquitin condensates."].
- Innate immune pathway effects are real but are best interpreted as contextual consequences of selective autophagic cargo handling in the PN frame [PMID:28898289 "TRIM32-mediated as well as poly(I:C)- and LPS-induced degradation of TRIF is inhibited by deficiency of TAX1BP1, a receptor for selective autophagy."] [PMID:28898289 "TRIM32 negatively regulates TLR3/4-mediated immune responses by targeting TRIF to TAX1BP1-mediated selective autophagic degradation."].
- Older A20/NF-kappaB pathway papers support a broader adaptor role, but not one that should displace the autophagy-centered core call [PMID:17703191 "Thus, TAX1BP1 is pivotal for the termination of NF-kappaB and JNK signaling by functioning as an essential regulator of A20."] [PMID:18239685 "Mechanistically, TAX1BP1 acts in NF-kappaB signalling as an essential adaptor between A20 and its targets."].

## Conservative boundaries

- Mitophagy should remain non-core here. The local evidence shows mitochondrial localization in a MAVS setting [PMID:27736772 "Virus infection promotes the mitochondrial localization of TAX1BP1 and concomitant interaction with the mitochondrial adaptor MAVS."], but this does not by itself justify a standalone core mitophagy annotation.
- Autophagosome-lysosome fusion should also remain below the threshold for direct promotion. PMID:26451915 supports a Myosin VI-linked maturation connection [PMID:26451915 "TAX1BP1 may not only function as an autophagy receptor to recruit ubiquitylated substrates for autophagic degradation, but also serve as a Myosin VI cargo adaptor protein for mediating the maturation of autophagosome."], but the available TAX1BP1-specific evidence is still indirect for a direct fusion term.
- Broad signaling-adaptor annotations are acceptable as contextual/non-core descriptions, but the GO-facing core remains better captured by `autophagy cargo adaptor activity` plus the selective-autophagy process calls.

## Impact on the local review

The current PN-focused YAML remains appropriately conservative. This manual fallback does not justify promoting additional core terms beyond:

- `autophagy cargo adaptor activity`
- `macroautophagy`
- `xenophagy`

It also does not justify promoting standalone core annotations for:

- `mitophagy`
- `autophagosome-lysosome fusion`
- broad inflammatory-signaling adaptor terms
