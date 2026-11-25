# PA5384 (Q9HTI0) notes

No deep-research provider was available. Literature: PMID:23524670 (abstract only; the PubMed MCP
returned no PMC body for PMC3648032).

## Biology

- Last gene of the carnitine operon; not needed for carnitine catabolism [PMID:23524670 "the last gene
  in the operon, PA5384, was not required for carnitine catabolism"].
- Short-chain acylcarnitine hydrolase [PMID:23524670 "we have characterized PA5384 as an
  l-enantiomer-specific short-chain acylcarnitine hydrolase that is required for growth and hydrolysis
  of acetyl- and butyrylcarnitine to carnitine and the respective short-chain fatty acid"].
- Family: GDXG lipolytic enzyme / AB_hydrolase_3 (PF07859); unreviewed UniProt entry (PE 3).
- Operon regulator: CdhR (PA5389), reviewed in genes/PSEAE/cdhR.
- No GO term for acylcarnitine catabolism; carnitine catabolism terms would be wrong (PA5384 acts
  upstream of carnitine).

### Annotation decisions

- GO:0047619 (IDA, PseudoCAP): ACCEPT, core MF.
- GO:0034338 (IBA, PTN000546472): ACCEPT (reaction falls within the definition; not is_a related).
- GO:0016787 (IEA): TOO_GENERAL.
- Action counts: ACCEPT 2, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009058710 | GO:0016787 hydrolase activity | 16 | 193 (48 taxa) | GO:0047619, IDA, PMID:23524670 (PseudoCAP) | SOUND | Abstract states PA5384 was characterised as an enantiomer-specific acylcarnitine hydrolase; the seed supports the very general node term. | 15 others: human AADAC P22760, E. coli Aes P23872, M. tuberculosis LipN/LipI/NlhH, soybean HIDH, Arabidopsis, mouse, rat and yeast GDXG hydrolases | Yes; 15 independent characterised hydrolases, and the root-level term suits a 193-leaf GDXG clade |

No GO_CENTRAL or PSEUDOCAP defect. PA5384's own IBA comes from the descendant node PTN000546472
(GO:0034338), which PA5384 does not seed.
