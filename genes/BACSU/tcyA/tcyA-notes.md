# tcyA (P42199, BACSU) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: TcyA was chosen as the closest experimentally implicated relative of the
ProtNLM2 benchmark protein XENNA/D3VIU4 (same PANTHER subfamily PTHR35936:SF34, same CDD
cd13711). This review covers TcyA on its own terms. No ProtNLM2 output was consulted.

### Setup and provenance

- `just fetch-gene BACSU tcyA` created the uniprot, goa and stub files. GOA has a single
  annotation: plasma membrane, IEA (GO_REF:0000044, SubCell).
- Deep research failed. `just deep-research-falcon BACSU tcyA --fallback perplexity-lite`
  returned 403 "Failed to authenticate" from the Edison/falcon API, and perplexity-lite
  then returned 401 insufficient_quota. No deep-research file exists. Literature came
  from PubMed searches for (tcyA OR yckK OR tcyABC) AND subtilis, and from the reference
  list on the SubtiWiki TcyA page.
- `just fetch-fitness BACSU tcyA` found no FEBA data for B. subtilis.
- Cached or refreshed: PMID:15262924 (re-fetched; PMC full text recovered), PMID:29995990
  (full text), PMID:22138345 (abstract), PMID:7551042 (abstract), PMID:10092453
  (abstract; not used), PMID:39397791 (full text; structural predictions only, not used).

### What is experimentally established in B. subtilis

- L-cystine uptake, genetic evidence
  [PMID:15262924 "This indicates that YckK was involved in the residual l -cystine transport observed in a Δ yhcL Δ ytmJKLMN mutant."].
  Growth on L-cystine was abolished in the triple mutant. A transposon insertion in tcyA
  was isolated as a selenocystine-resistant mutant.
- TcyABC is the low-affinity system
  [PMID:15262924 "several elements strongly suggest that TcyABC is a lower-affinity l -cystine transporter"],
  and tcyA is weakly expressed under all sulfur conditions tested.
- Probable minor role in S-methylcysteine import (multi-mutant growth data, PMID:15262924).
- Diaminopimelate import by the TcyABC system
  [PMID:29995990 "The results suggest that TcyABC and TcyP are the two major DAP uptake systems"].
  This is system-level evidence from suppression of aspB-mutant lysis, and the cached
  text does not say which tcy gene was deleted. It is recorded here and in the
  description, but not as a GO annotation.
- NOT established: direct ligand binding by purified TcyA, the complex composition (the
  complex has not been isolated), and lipidation (the anchor is predicted from the
  PROSITE lipobox).

### Evolutionary grounding (tcyA-bioinformatics/RESULTS.md)

- PANTHER puts TcyA in PTHR35936:SF34 ("ABC TRANSPORTER EXTRACELLULAR-BINDING PROTEIN
  YCKB-RELATED"). SF34 also contains D3VIU4 and the uncharacterized B. subtilis paralog
  YckB (P42400). The SBP of B. subtilis TcyJKLMN, TcyJ, is in SF18. E. coli TcyJ (P0AEM9)
  and N. gonorrhoeae Ngo0372 (Q5F9M1), the cystine SBPs with biochemical data, are in SF35.
- CDD cd13711 (PBP2_Ngo0372_TcyA) groups TcyA with Ngo0372 (54% identity) and D3VIU4
  (50%). The Ngo0372 pocket Tyr that is crucial for L-cystine binding (Tyr59 in the
  paper, Y58 in UniProt numbering) and the pocket Trp are conserved in TcyA as Y55 and
  W94.
- Neither PANTHER nor PAINT places TcyA with the characterised binders, and PTHR35936
  PAINT has no IBD on an SF34 node (GOA gives TcyA no IBA rows). So no binding MF is
  asserted from transfer. L-cystine binding is recorded as an inference in
  core_functions only.

### Decisions

- GO:0005886 plasma membrane (IEA): ACCEPT. Lipoprotein of a monoderm bacterium; the
  anchor is predicted only, so the term is not refined further.
- NEW GO:0015811 L-cystine transport (IMP, PMID:15262924). Passes the participation test:
  TcyA is the substrate-capturing subunit of the transporter that performs the step.
- NEW GO:0015184 L-cystine transmembrane transporter activity, contributes_to (IMP).
- NEW GO:0055052 ABC transporter complex, substrate-binding subunit-containing (IC), from
  the operon and component assignments.
- No diaminopimelate or S-methylcysteine terms: the evidence is system-level or labelled
  "probably".

### Caution for transfer to D3VIU4

The TcyA evidence comes from genetics in B. subtilis. Transfer to SF34 members should be
limited to contributes_to the ABC importer and the transport process, and should treat
L-cystine specificity as a hypothesis. YckB, also in SF34, has no known substrate.
