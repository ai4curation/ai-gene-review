# SIZ1 (YDR409W, Q04195) review notes

## 2026-10-04 session

### Identity
- S. cerevisiae Siz1/Ull1, PIAS family SP-RING SUMO E3 (PANTHER PTHR10782:SF4), paralog of Siz2/Nfi1.
  Domains: SAP (34-68), PINIT (162-314), SP-RING zinc finger (344-431), C-terminal bud neck region (794-904)
  [file:yeast/SIZ1/SIZ1-uniprot.txt "The SP-RING-type zinc finger mediates interaction with UBC9 and"].
- No yeast reviews yet for SIZ2/NFI1, UBC9, SMT3 or MMS21 in this repo; consistency checked against
  human PIAS1 (GO:0019789 annotations ACCEPTed there; GO:0061665 used as core MF) and ARATH SIZ1 (still pending).

### Core biology (verified against primary sources)
- Septin E3: [PMID:11572779 "Siz1 is required for SUMO attachment to the S. cerevisiae septins in vivo and strongly
  stimulates septin sumoylation in vitro"]; [PMID:11577116 "Ull1 is additionally required as well as E1 (Sua1.Uba2
  complex), E2 (Ubc9), and ATP"]; [PMID:11587849 "In the siz1 mutant septin-sumoylation was completely abolished"].
- Septin substrates Cdc3, Cdc11, Shs1 need the Siz1 C-terminus; PCNA/Prp45 need PINIT; local-concentration model
  [PMID:17077124 "sumoylation of the bud neck-associated septin proteins Cdc3, Cdc11 and Shs1/Sep7 requires the
  C-terminal domain of Siz1"].
- Structure: [PMID:19748360 "the PINIT domain is essential for redirecting SUMO conjugation to the proliferating
  cell nuclear antigen (PCNA) at lysine 164"].
- PCNA K164: [PMID:18701921 "As expected, sumoylation at K164 was abolished in the siz1 mutant"]. Downstream:
  [PMID:15931174 "SUMO-modified PCNA recruits Srs2 in S phase in order to prevent unwanted recombination events of
  replicating chromosomes"].
- dsDNA binding via SAP [PMID:18701921 "Recombinant full-length Siz1 was efficiently retained on a biotinylated
  76-bp fragment of dsDNA"], but not required for PCNA sumoylation in vivo [PMID:18701921 "This indicates that DNA
  binding of Siz1 might not be a prerequisite for efficient modification of PCNA in vivo"] -> KEEP_AS_NON_CORE.
- Localization: nuclear in interphase, bud neck/septin ring in M phase [PMID:17403926 "In M phase, Siz1p is exported
  from the nucleus by the karyopherin Kap142p/Msn5p and subsequently targeted to the septin ring"];
  [PMID:16109721 "modifies both cytoplasmic and nuclear proteins"].
- Top2 / chromosome segregation [PMID:16204216 "Sumoylation of the carboxy-terminus of Top2p, a known SUMO target,
  is mediated by Siz1p and Siz2p both in vivo and in vitro"].
- Cse4 [PMID:26960795 "revealed that Siz1 serves as an E3 for Cse4 sumoylation"].
- Rsp5 crosstalk [PMID:23443663 "SUMOylated Rsp5p has reduced ubiquitin ligase activity"].
- SUMO stress response [PMID:25434491 "the SSR is effected primarily by the Siz1 E3 ligase"].
- DSB relocation: Siz2/Mms21 dominant, Siz1 minor [PMID:27056668 "siz2Δ compromises perinuclear relocation more
  efficiently than siz1Δ alone"].

### Deep research audit
- Most claims verified. The quote "Siz1 and Siz2 redundantly control the abundances of most sumoylated substrates"
  attributed to PMID:23935535 is not present verbatim in the cached full text; not used.
- Note: a guessed PMID (15989971) for the Srs2 paper turned out to be a separase paper; the correct one,
  found by PubMed esearch, is PMID:15931174.

### Decisions
- 27 ACCEPT, 9 KEEP_AS_NON_CORE, no REMOVE/MODIFY/NEW. No protein binding annotations present.
- Non-core: dsDNA binding, zinc ion binding (x2), chromosome segregation (x2), negative regulation of protein
  ubiquitination (x2, Rsp5), DSB attachment to nuclear envelope (x2).
- GO:0019789 SUMO transferase activity ACCEPTed (correct parent; consistent with PIAS1); GO:0061665 SUMO ligase
  activity used in core_functions.
- No NEW terms: candidate process terms (e.g. septin ring organization, DNA repair) would rest on substrate-level
  necessity rather than Siz1 doing the work of the process.
