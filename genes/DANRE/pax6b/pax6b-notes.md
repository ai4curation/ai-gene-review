# pax6b notes (DANRE, A0A0R4IQL7)

## 2026-09-27 session log

- Deep research FAILED for this gene (Edison: 402 Payment Required; OpenAI key invalid). Not retried.
  Literature research done manually (Europe PMC REST); see pax6a-notes.md for the searches and new PMIDs.

## Key facts with provenance

- Naming: pax6b = old pax6.2 (Nornes 1998 "Pax6.2")
  [PMID:18282108 "Overlapping divergent expression patterns have been reported for pax6a and pax6b (previously named pax6.1 and pax6.2 respectively) [43,49]."]
- sunrise = pax6b L244P homeodomain missense; homozygous viable
  [PMID:18282108 "Sequencing of sri homozygotes and heterozygotes identified a leucine to proline missense mutation in a highly conserved residue of the pax6b homeodomain (Figures 1B, S1B, and S1C)."]
- Null allele sa0086 (Y109*): [PMID:20177065 "This pax6b mutant allele ( sa0086 ) harbors a C to A substitution changing codon 109 (Tyr) to a premature stop codon."]
- Pancreas: only pax6b expressed [PMID:18282108 "only pax6b is expressed in the pancreas isolated from 6 month old wild type and sri/sri fish, while eyes from the same individuals express both pax6a and pax6b"]
- Endocrine phenotype: [PMID:20177065 "Pax6b-depleted embryos have almost no beta cells, a strongly reduced number of delta cells, and a significant increase of epsilon cells."]
- Homeodomain needed for lens, not pancreas: [PMID:20177065 "we show that deletion of the Pax6b homeodomain in zebrafish embryos does not disturb pancreas development, whereas lens formation is strongly affected."]
- Enteroendocrine: [PMID:32867764 "Finally, we show that the homeodomain of Pax6b is dispensable for its action in both EECs and PECs."]
- Cornea: [PMID:25692557 "Lack of pax6b function leads to severe disturbance of the corneal gene regulatory programme."]
- Habenula NOT pax6b: [PMID:27387288 "Homozygous pax6bsa86 mutant embryos display cxcr4b and brn3a expression in the habenulae largely indistinguishable from that of wild type siblings (Fig 2A, 2B, 2E and 2F)."]
- Regeneration: [PMID:20152834 "Loss of Pax6b expression did not affect Müller glial cell division, but blocked the subsequent first cell division of the neuronal progenitors."]

## Decisions

- All 59 GOA rows reviewed; the experimental IMP/IGI/IDA rows are accepted (non-core for A/P patterning,
  hindbrain, epithalamus, regulation of gene expression, neural crest migration, cell differentiation).
- Epithalamus IGI kept as non-core: evidence is double knockdown; later work shows the habenula role is pax6a's.
- MODIFY IEA GO:0006351 DNA-templated transcription -> GO:0006357.
- NEW GO:2000179 (IMP PMID:20152834), mirroring the (modified) pax6a annotation from the same paper.
