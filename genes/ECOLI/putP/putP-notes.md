# putP (Escherichia coli K-12, UniProtKB P07117) review notes

## Provenance of these notes

No deep-research provider keys were available in this environment, so no
provider deep-research file (`putP-deep-research-*.md`) was generated. These
notes were assembled manually from the cached PubMed records in `publications/`
(all abstract-only; `full_text_available: false`), the UniProt record
(`putP-uniprot.txt`), and one read of the PMC full text of PMID:17088549
(PMC1859954) to check what was actually shown for propionate (not quotable from
the cache; used for judgment only).

PMIDs consulted: 1567896, 3512540, 9693004, 3007935, 3902503, 9756872,
15919996, 17309111, 17088549, 17088459 (mis-keyed, see below), 16079137,
3053649, 3053687, 8119910, 3302614, 1400239, 28712849.

## Function: Na+-coupled high-affinity L-proline uptake

- Reconstituted PutP accumulates proline driven by a Na+ electrochemical
  gradient, not by proton motive force alone; ~1:1 Na+:proline
  [PMID:3512540 "More than a 10-fold accumulation was seen with a sodium
  electrochemical gradient while no accumulation was found with proton motive
  force alone"; "The stoichiometry of the co-transport system was approximately
  one Na+ for one proline"].
- Purified His-tagged PutP reconstituted inside-out accumulates proline with
  Na+ or Li+ gradients; pH gradient does not drive transport
  [PMID:9693004 "Reconstituted PutP is able to accumulate proline against a
  concentration gradient in the presence of an inwardly directed
  electrochemical Na+ or Li+ gradient, while a pH gradient does not affect
  transport"].
- Na+ binds the carrier even in the absence of proline; Cys-344 (TM VIII)
  implicated in high-affinity Na+/proline binding
  [PMID:1567896 "Na+ alone, even in the absence of proline, partially protected
  it from the NEM-inactivation"].
- Cys residues are not essential for transport [PMID:3053687 "these cysteine
  residues are not essential for proline transport"]; R257C alters cation
  dependence of proline binding [PMID:3053649]; R376K abolishes activity
  [PMID:8119910].
- Genetic: putP mutants lack high-affinity proline transport
  [PMID:3007935 "They had no high affinity proline transport activity"]; putP
  lies in the put cluster with putA (PutA is the autogenous repressor and
  proline dehydrogenase) [PMID:28712849 "the Na+-proline transporter PutP"].

## Location: cytoplasmic (inner) membrane, 13 TM

- 35 kDa (anomalous mobility) cytoplasmic membrane protein
  [PMID:3902503 "was identified as a 35 kDa cytoplasmic membrane protein"].
- Topology: 13 TMs, N-terminus periplasmic, C-terminus cytoplasmic
  [PMID:9756872 "the protein consists of 13 TMs with the N terminus on the
  outside and the C terminus facing the cytoplasm"].
- Global topology (C-terminal PhoA/GFP tagging) [PMID:15919996] and inner
  membrane proteomics [PMID:17309111] corroborate.
- Homodimer in inner membrane preparations [PMID:16079137 per UniProt].

## Propionate (short-chain fatty acid) transport

- GOA rows GO:0015912 (IMP, IEP; EcoCyc) cite PMID:17088459, which is a
  Circulation paper on heart failure. The intended paper is PMID:17088549
  (Reed et al. 2006 PNAS, "Systems approach to refining genome annotation"),
  which UniProt cites for the propionate function: a transposition of two
  digits (459 vs 549). Recorded as a source defect (WRONG_REFERENCE, EcoCyc).
- PMID:17088549 assigns putP a transport function [PMID:17088549 "leading to the
  functional assignment of eight ORFs (yjjLMN, yeaTU, dctA, idnT, and putP)"].
  Full text (PMC) shows the evidence is a growth-rate defect of the deletion on
  propionate, increased putP expression on propionate, and homology to MctP; no
  uptake assay. So propionate transport by PutP is plausible but indirect; kept
  as non-core at the curators' precision (acts_upstream_of_or_within).

## Judgments

- Core MF: GO:0005298 proline:sodium symporter activity; BP GO:0035524 proline
  transmembrane transport; CC GO:0005886 plasma membrane.
- General terms (transport, membrane, transmembrane transporter, carboxylic acid
  transmembrane transport, sodium ion transport, proline transport) MODIFY,
  consistent with genes/PSEPK/putP.
- GO:0031402 sodium ion binding: PSEPK marked over-annotated (IEA only); in
  E. coli there is direct biochemical evidence that Na+ binds the carrier
  independently of proline, so kept as non-core here.
