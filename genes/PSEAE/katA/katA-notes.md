# katA (PA4236) review notes

## Literature search (2026-11-05)

No existing katA folder was present in genes/PSEAE, so this is a new review. No
deep-research provider was available, and the PubMed MCP and Europe PMC search
endpoints failed during this session. Sources read: PMID:10368148 (full text,
Ma et al. 1999) and PMID:24663218 (full text, Su et al. 2014), both cited by
UniProt and fetched with the repository tooling.

## Findings

- KatA purified to homogeneity (FRD2 katB background, and as a His-tagged
  recombinant protein); apparent Km for H2O2 44.7 mM; katA complements a
  catalase-deficient E. coli [PMID:10368148 "the P. aeruginosa katA gene
  complemented a catalase-deficient strain of Escherichia coli"].
- katA mutants: no detectable catalase activity; hypersusceptible to H2O2
  [PMID:10368148 "Isogenic katA and bfrA mutants were hypersusceptible to H2O2"].
- BfrA is needed for full KatA activity, probably as a heme-iron source
  [PMID:10368148].
- Ferric heme binds NO directly (Kd about 6 microM); katA mutants are more
  sensitive to anaerobic NO [PMID:24663218 "KatA has a 5-coordinate high spin
  ferric heme that binds NO without prior reduction of the heme iron"]. Added as
  NEW GO:0070026 nitric oxide binding (IDA).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000157250 | GO:0004096 catalase activity | 25 | 283 (109 taxa) | GO:0004096, IDA, PMID:10368148 (PseudoCAP) | 24 others, including human CAT P04040, yeast CTA1 and CTT1, Drosophila Cat, Arabidopsis AT4G35090, MGI:88271, RGD:2279 | Yes | SOUND | Purified-enzyme kinetics, complementation and loss of activity in the mutant. Node term fits the monofunctional heme catalase clade. |

No GO_CENTRAL defect.
