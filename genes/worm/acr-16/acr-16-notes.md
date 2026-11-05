# acr-16 review notes

- Fetched P48180 (ACH1_CAEEL), matches WormBase WBGene00000055 / GeneID 179235; 23 GOA rows.
- Key papers: PMID:19020092 (full text; IDA source, ACR-16+RIC-3 oocyte reconstitution),
  PMID:23577128 (full text; AVA role in male mating reversal), PMID:15944127 and PMID:15917232
  (abstract only; acr-16 null lacks fast/levamisole-insensitive NMJ current), PMID:8627624 (homomer, Ce21).
- Decisions: MF refined to GO:0022848 (homomer, so `enables` is correct, unlike UNC-29); generic
  transport rows refined to GO:0098655; membrane potential rows refined to GO:0060079; ARBA
  chemical synaptic transmission refined to GO:0007271.
- Calcium ion transport (IBA): plausible for an alpha7-like subunit but Ca2+ permeability of ACR-16
  has not been measured [PMID:19020092 "The calcium permeability of N-AChRs has not been measured."]; kept non-core.
- Cell projection IDA rows: abstract-only; PMID:17719547 abstract does not mention ACR-16 (likely used
  as a muscle postsynaptic marker). Kept as non-core, deferring to WormBase curators.
- NEW: GO:0007274 neuromuscular synaptic transmission (IMP; ACR-16 is the postsynaptic channel that
  carries the fast NMJ current, so it does the work; comparator UNC-29 carries this term).
