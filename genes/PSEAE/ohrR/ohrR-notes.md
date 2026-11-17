# ohrR / PA2849 (Q9HZZ4) review notes

## Summary of the literature

OhrR is a 151-residue MarR/OhrR-family regulator. The UniProtKB entry is unreviewed (SubName
"OhrR") and its only CC line, a cytoplasm location, is ARBA-derived, so it is not usable as
evidence. Usable features: `FT DNA_BIND 61..84` (winged-helix recognition region) and the family
assignment [file:PSEAE/ohrR/ohrR-uniprot.txt "PANTHER; PTHR33164:SF5; ORGANIC HYDROPEROXIDE
RESISTANCE TRANSCRIPTIONAL REGULATOR; 1."].

Primary data, Atichartpongkul et al. 2010 [PMID:20139188], **abstract only** — the PubMed MCP
returns no body text for PMC2849439:

- [PMID:20139188 "ohrR encodes an organic hydroperoxide sensor and a transcriptional repressor
  that regulates organic hydroperoxide-inducible expression of a thiol peroxidase gene, ohr, and
  itself"].
- [PMID:20139188 "OhrR binds directly to the operators and represses transcription of these
  genes"] — direct binding, which is what the CollecTF site records rest on.
- Redox switch: [PMID:20139188 "Exposure to an organic hydroperoxide leads to oxidation of OhrR
  and to subsequent structural changes that result in the loss of the repressor's ability to bind
  to the operators that allow expression of the target genes"].
- Genetics: [PMID:20139188 "ohrR and ohr mutants show increased and decreased resistance to
  organic hydroproxides, respectively, compared to a parental strain"] and [PMID:20139188 "the
  ohrR mutant had a reduced-virulence phenotype in the Pseudomonas aeruginosa-Caenorhabditis
  elegans pathogenicity model"].

The abstract therefore states, outright, every claim annotated from this paper by PseudoCAP and
CollecTF (operator binding, repression, redox release, mutant phenotypes). The partner thiol
peroxidase Ohr is further characterised in [PMID:22609922] (cached), consistent with this picture.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002109389 | GO:0006355 regulation of DNA-templated transcription | 8 | 229 (33 taxa) | GO:0045892, IMP + EXP + IEP, PMID:20139188 (PseudoCAP and CollecTF) | SOUND | Three independent evidence lines on the same gene, and the abstract states both the direct operator binding and the mutant de-repression phenotype. OhrR is a *bona fide* transcriptional repressor; the node term is a correct generalisation. | *B. subtilis* OhrR (O34777, IMP GO:0001227 / IMP+IDA GO:0045892), *E. coli* MarR (P27245, IDA GO:0003677, IMP GO:0045892), SlyA (P0A8W2, IMP GO:0003700, IDA GO:0045893), MprA/EmrR (P0ACR9, IDA GO:0000976/GO:0003677), *S. oneidensis* OhrR (Q8EI70, EXP GO:0045892), *P. aeruginosa* PA0942 (Q9I516, IEP GO:0045892), *B. subtilis* ScoC/Hpr (P11065, IMP GO:0006355) — verified by live QuickGO query 2026-11-05 | Yes, strongly: five other seeds carry experimental transcription-regulation annotations. The node term suits the whole MarR clade. **No GO_CENTRAL defect.** |
| PTN002109389 | GO:0006950 response to stress | 2 | 229 (33 taxa) | not seeded by OhrR | n/a (leaf IBA only) | OhrR receives this IBA but does not seed it. The two seeds are *B. subtilis* OhrR (IMP GO:0042542 response to hydrogen peroxide) and *E. coli* MarR (IMP GO:0071236 response to antibiotic, GO:0009408 response to heat). The node term stops at the root precisely because the clade's stresses differ; that is granularity, not unsoundness. | O34777, P27245 | Yes. No GO_CENTRAL defect; for OhrR the row is MODIFYed to the hydroperoxide-specific child (see below). |

This is a different node from the one shared by the sensor kinases in this batch, so there is no
overlap with `pprA`/`fleS`/`cbrA`, nor with the reviewed `genes/PSEAE/fleQ` (a sigma-54 activator
on an unrelated family).

## Annotation decisions

- GO:0045892 (IMP, EXP, IEP) and GO:1900407 (IMP): ACCEPT. Core function; the seed row is sound.
- GO:0000976, GO:0001217 (IPI and IMP each): ACCEPT — direct operator binding and repression.
- GO:0032993 protein-DNA complex (IPI, IMP): KEEP_AS_NON_CORE, a component restatement of the
  binding (the same call as in `genes/PSEAE/fleQ`).
- GO:0003677, GO:0003700, GO:0006355 (IBA, IEA), GO:0006355 (IEA): TOO_GENERAL — each entailed by
  an accepted specific term. Note GO:0001217 *is_a* GO:0003700, so TOO_GENERAL rather than
  MODIFY is right there.
- GO:0006950 response to stress (IBA): **MODIFY** to GO:0033194 response to hydroperoxide. Note
  that GO:1900407 (regulation of cellular response to oxidative stress) is a regulation class and
  does **not** entail GO:0006950, so TOO_GENERAL would be wrong here; a `propagation_review`
  block records the node reading.
- GO:0006351 DNA-templated transcription (IEA, GO_REF:0000104): **REMOVE**, with a
  `resource: UNIPROT` `WRONG_TERM` defect (PROBABLE). A repressor does not perform transcription;
  the sequence-feature mapping from the MarR HTH should point into the regulation branch. This is
  a UniProt/ARBA rule-based row, not a PseudoCAP row, so the defect is filed against UNIPROT.
- GO:0005737 cytoplasm (IEA GO_REF:0000044): ACCEPT on biological grounds (the only possible
  location for an operator-binding repressor), with the reason noting that the underlying UniProt
  statement is ARBA-derived.

**No PseudoCAP defect** is filed on this gene: the PseudoCAP row (GO:0045892 IMP) and the two
CollecTF rows for the same claim are all correct.
