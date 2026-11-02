# dsbE / ccmG (P0AA86, b2195) notes

## Deep research status
- 2026-10-23: `just deep-research-falcon ECOLI dsbE` was attempted and failed with
  `Exception: Failed to authenticate`; no other provider credentials were available.
  Review based on cached publications and the UniProt record.

## Biology
- Membrane-anchored, periplasmic thioredoxin domain, WCPTC active site (C80/C83)
  [PMID:9537397 "The CcmG protein was shown to be membrane bound, facing the periplasm with its C-terminal, hydrophilic domain."]
- Null mutant lacks all c-type cytochromes; cysteine mutants rescued by thiols
  [PMID:9537397 "A chromosomal, nonpolar in-frame deletion in ccmG resulted in the complete absence of all c-type cytochromes."]
  [PMID:9537397 "which is in agreement with a reducing function for CcmG"]
- Reduced by DsbD (nDsbD) by direct disulfide exchange
  [PMID:16004871 "CcmG, a highly specific disulfide reductase essential for cytochrome c maturation"]
- Acts late, after CcmF/CcmH; not bypassed by dsbA/dsbB mutation or chemical reductant
  [PMID:11256948 "The data support a model proposed by others in which CcmG catalyses one of the last reactions specific to cytochrome c assembly."]
- Weak reductant (E0' ~ -0.175 to -0.186 V)
  [PMID:11350062 "The standard redox potential (E0') for the active thiol/disulfide is -0.175 V"]
  [PMID:11843181 "DsbE can be regarded as a weak reductant in the Escherichia coli periplasm"]
- Ortholog biochemistry (R. capsulatus)
  [PMID:28634234 "CcmG can efficiently reduce the disulfide bond of apocytochrome c and also resolve a mixed disulfide bond formed between apocytochrome c and CcmH"]

## Curation decisions
- protein binding (IPI, DsbD): REMOVE per protein-binding policy.
- GO:0015036 and GO:0016491 rows: MODIFY -> GO:0015035 protein-disulfide reductase activity.
- GO:0017004 rows: MODIFY -> GO:0018063 cytochrome c-heme linkage (descendant of GO:0017004).
- Locations plasma membrane and periplasmic space: ACCEPT.
- Fetched PMIDs 11256948, 11350062, 11843181 (UniProt RX lines).
