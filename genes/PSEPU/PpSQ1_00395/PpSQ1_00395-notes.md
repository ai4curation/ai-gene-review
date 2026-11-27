# PpSQ1_00395 (P0DOV9) 3-sulfolactaldehyde dehydrogenase, Pseudomonas putida SQ1 — notes

## Provenance and access

- Deep research with perplexity failed in this environment (2026-11-10; "All providers failed").
  Sources: UniProt P0DOV9, PMID:26195800 (abstract only), PMID:37886098 (Li et al. 2023, R.
  leguminosarum SLA dehydrogenase RlGabD, full text), PMID:41676062 (review, full text).

## Function

- UniProt (ECO:0000269 PubMed:26195800): "Catalyzes the oxidation of (2S)-3-sulfolactaldehyde to
  (2S)-3-sulfolactate, using both NAD(+) and NADP(+) as electron acceptors." RHEA:47932 (NAD+) and
  RHEA:47928 (NADP+), EC 1.2.1.97.
- [PMID:26195800 "3-sulfolactaldehyde (SLA), which is oxidized to SL by an NAD(P)(+)-dependent SLA
  dehydrogenase."]
- Kinetic constants in UniProt are for 4-oxobutanoate (succinate semialdehyde, SSA), not SLA:
  "KM=0.14 mM for 4-oxobutanoate with NAD(+) as cosubstrate"; kcat 11.8 s-1 (NAD+) and 11.4 s-1
  (NADP+). This fits [PMID:37886098 "In all cases accurate kinetic parameters have not been
  reported for any SLA dehydrogenase as SLA was not available in pure form."]: SSA served as a
  surrogate substrate. So P0DOV9 really oxidizes SSA in vitro, but SSA oxidation is not its
  shown biological role.
- RlGabD (ortholog role in Rhizobium sulfo-ED): uses both NAD+ and NADP+, rapid-equilibrium
  ordered mechanism, tetramer [PMID:37886098]. SLA dehydrogenases are "annotated as GabD or SlaB"
  and sit in the PF00171 ALDH superfamily.

## GOA rows

- GO:0004029 (Rhea 47932) and GO:0033721 (Rhea 47928): ACCEPT; exact reaction mapped by rhea2go.
  GO has no SLA-specific term; GO:0004029 is the module's term. GO:0004030 aldehyde
  dehydrogenase [NAD(P)+] activity is their common parent and would describe the dual-cofactor
  enzyme in one term.
- GO:0004777 SSADH (NAD+) (TreeGrafter, graft clade PTN000192659 under PAINT node PTN008681047)
  and GO:0009013 SSADH [NAD(P)+] (InterPro2GO IPR010102): MARK_AS_OVER_ANNOTATED — measured in
  vitro activity on a surrogate substrate, of unknown physiological relevance. Note GO:0004777
  is_a GO:0004029 (OLS hierarchy), so the SSADH row is a substrate-specific child of the accepted
  term, not a different chemistry.
- GO:0009450 GABA catabolic process (combined IEA): MARK_AS_OVER_ANNOTATED — no evidence the
  protein participates in GABA breakdown in SQ1; the gene is in the SQ cluster and SQ-induced.
- GO:0016491 and GO:0016620: MODIFY to GO:0004029 + GO:0033721.
- GO:0005829 cytosol (TreeGrafter; PAINT PTN000192659 seeded by E. coli AldA): KEEP_AS_NON_CORE.

## PAINT lineage

- PTHR43353 tree (175 leaves): PTN000192659 (8 leaves: E. coli GabD and AldA, Salmonella GabD,
  P. aeruginosa DavD, Neisseria GabD, Shewanella PuuC, Vibrio VC_1745, Bradyrhizobium blr0807) is
  inside PTN008681047 (162 leaves, 7 subfamilies), the node carrying the GO:0004777 and
  GO:0009450 IBDs. P0DOV9 (not a tree leaf) is grafted into PTN000192659 per its GOA rows.
