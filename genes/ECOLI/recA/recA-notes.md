# recA (Escherichia coli K-12, UniProtKB:P0A7G6) - review notes

Author: Claude (AI-assisted), 2026-11-09.

## Provenance and method

Deep research was NOT run for this gene: no deep-research provider was available
in this session (no API keys). These notes summarise the cached publications in
`publications/` (most are abstract-only; full text was available for PMID:17391508,
PMID:19606142, PMID:19820696, PMID:21912525, PMID:25811184, PMID:27378775,
PMID:36598938 and PMID:37212693) and the reviewed UniProt entry. PMIDs 9230304,
16483938, 7608206 and 1731253 were fetched for this review (abstract only).

## Biology summary

- RecA is the E. coli homologous recombinase. UniProt (curated, ECO:0000269):
  "Catalyzes ATP-driven homologous pairing and strand exchange of DNA molecules
  necessary for DNA recombinational repair" and "Polymerizes non-specifically on
  ssDNA to form filaments; filament formation requires ATP or ATP-gamma-S."
- ssDNA and dsDNA binding: [PMID:7021553 "The recA protein of Escherichia coli binds
  both single- (SS) and double-stranded (DS) DNA"]; "SS DNA binds to recA protein in
  the absence of a nucleoside triphosphate".
- DNA-dependent ATPase: [PMID:7021552 "Both single- and double-stranded DNA stimulate
  the hydrolysis of ATP catalyzed by the recA protein of Escherichia coli."]
  ATP is an allosteric effector: [PMID:1731253 "ATP-bound recA protein has a high
  affinity for DNA, whereas the ADP-bound form has a low affinity."]
- Presynaptic filament loading: by RecBCD at chi on DSB ends [PMID:9230304 "the
  translocating RecBCD enzyme, which has been activated by chi, coordinates the
  preferential loading of the homologous pairing protein, RecA, onto the resultant
  single-stranded DNA downstream of chi"], via the RecB nuclease domain
  [PMID:16483938 "the C-terminal nuclease domain of the RecB subunit (RecBnuc) forms
  stable complexes with RecA"]; and by RecFOR at postreplication gaps [PMID:37212693
  "The formation of a RecA filament in the gap, a step often referred to as
  presynapsis, occurs with the aid of the RecF, RecO, and RecR proteins"]. SSB
  must be displaced [PMID:19820696 "Diffusional migration of SSB helps in the local
  displacement of SSB by an elongating RecA filament."]
- Recombinational repair pathways [PMID:10585965 "daughter-strand gaps are closed by
  the RecF pathway, while disintegrated replication forks are reestablished by the
  RecBCD pathway."]
- SOS co-protease (RecA*): [PMID:21764927 "In SOS induction, the RecA filament
  functions as a coprotease, enabling the autodigestion of the LexA repressor."]
  Structures: [PMID:36598938 "The RecA filaments stimulate the autocleavage of LexA,
  the repressor of more than 50 SOS genes, and activate the SOS response."] and
  "During the late phase of SOS response, the RecA filaments stimulate the
  autocleavage of UmuD and λ repressor CI". LexA binds only the activated filament
  [PMID:2554312 "Purified LexA protein bound tightly to these activated RecA columns,
  whereas the LexA protein bound poorly to RecA-agarose alone."]. Separation of
  function mutants [PMID:21912525 "Mutation analysis at these sites disrupted either
  recombination or LexA cleavage."].
- Pol V mutasome subunit: [PMID:19606142 "RecA* transfers a single RecA-ATP
  stoichiometrically from its DNA 3'-end to free pol V (UmuD'(2)C) to form an active
  mutasome (pol V Mut) with the composition UmuD'(2)C-RecA-ATP."]; the UmuC contact
  surface is residues 112-117 [PMID:25811184].
- Other partners (non-core): MutL inhibits RecA ATPase [PMID:22001225]; RecA binds
  AlkB and stimulates its repair [PMID:27378775]; DinI stabilises filaments
  [PMID:36598938].
- Non-SOS role in swarming [PMID:17391508 "the RecA effect on swarming does not
  require induction of the SOS response"].
- IR resistance alleles [PMID:24596148]; recA is itself LexA-regulated and
  damage-induced [PMID:10760155, PMID:11967071].

## Annotation decisions (summary)

- Core MF: GO:0000150 DNA strand exchange activity (IBA, PTN000534381, SOUND per
  PTHR45900 family review), GO:0003697 ssDNA binding, GO:0008094 ATP-dependent activity
  acting on DNA, GO:0140664 ATP-dependent DNA damage sensor activity, GO:0005524 ATP binding.
- GO:0004520 DNA endonuclease activity IBA: REMOVE. PTN000534381 IBD seeded by
  M. tuberculosis P9WHJ3, whose activity belongs to the PI-MtuI intein; E. coli RecA
  carries no intein. Family review assesses this node WRONG_NODE. Source defect to
  GO_CENTRAL recorded.
- GO:0009355 DNA polymerase V complex: ACCEPT both rows. The family review judges the
  root placement TOO_DEEP for the family, but E. coli RecA is the seed and is a genuine
  Pol V Mut subunit.
- Differences from the PSEPK (P. putida) review: for E. coli the gene already carries
  the specific GO:0000725 recombinational repair and GO:0035825 homologous recombination
  terms with literature support, so the general GO:0006281 DNA repair and GO:0006310
  DNA recombination rows are refined (MODIFY) rather than ACCEPTed as in PSEPK, where
  the specific terms were absent. Other shared terms (DNA binding -> ssDNA binding,
  damaged DNA binding KEEP_AS_NON_CORE, cytoplasm -> cytosol, DNA damage response ->
  SOS response, damage sensor ACCEPT) are handled as in PSEPK.
- Bare protein binding rows: LexA/UmuD row MODIFY to GO:0016504 peptidase activator
  activity (RecA* stimulates LexA and UmuD autocleavage); others REMOVE per policy.
