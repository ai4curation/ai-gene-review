# nuoH (E. coli K-12, P0AFD4) notes

## 2026-10-23 review session

- Deep-research providers are unavailable in this environment (no API keys), so
  no `-deep-research-*.md` file exists. Literature was reviewed manually from
  cached publications and the UniProt record.
- NuoH (ND1/Nqo8) is the most conserved membrane subunit; links peripheral and
  membrane arms [PMID:34308841 "Membrane-embedded NuoH mediates interaction with the peripheral arm and also contains five-helix structural repeat found in antiporter-like subunits"].
- Quinone-site cavity: [PMID:34308841 "A large hydrophilic cavity stretches from the Q-site towards the center of subunit NuoH and ends next to the invariant HGlu157"].
- Proton path: [PMID:23417064 "Thus, the first half-channel formed by Nqo8 is linked to the second half-channel in Nqo10/11"].
- Genetics (full text read): nuoH::Km is complex I-deficient with aerobic growth
  and acetate-use defects; insertion is polar
  [PMID:9495756 "a mutation in any one of the nuo genes tested causes a complex I deficiency"].
- Decisions: GO:0003954 (IBA, IDA) and GO:0016655 MODIFIED to GO:0008137
  (IBA row given a propagation_review: granularity, node sound); membrane rows
  MODIFIED to plasma membrane; NADH dehydrogenase complex MODIFIED to complex I;
  aerobic respiration (IBA, IMP) ACCEPTED.
- Open question: does NuoH bind quinone directly (UniProt "This subunit may bind ubiquinone")?
