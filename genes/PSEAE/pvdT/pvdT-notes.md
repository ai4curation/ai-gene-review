# pvdT (PA2390, Q9I190) review notes

No deep-research provider was available; notes compiled from UniProt, the cached full text of PMID:19906986, and cached abstracts.

- PvdRT-OpmQ is a tripartite MacB-type ABC exporter [PMID:19906986 "PvdRT-OpmQ displays the typical architecture of Gram-negative tripartite ABC-type exporters, consisting of an IM component with both ATPase and permease domains, a periplasmic membrane fusion protein, and a TolC-like OM protein"].
- Periplasmic accumulation in mutants [PMID:19906986 "nearly all intracellular PVD was associated with the periplasmic fraction of pvdR , pvdT , and opmQ mutants"].
- Secretion of new PVD [PMID:21035449 "Bacteria lacking this efflux pump accumulated PVD, or a fluorescent precursor, in the periplasm, due to their inability to efficiently secrete into the media newly synthesized PVD"]; recycling [PMID:23766114]; metal-complex export [PMID:22187978 "the PvdRT-OpmQ efflux pump exports unwanted metals complexed with PVD from the bacterium"].
- PMID:12686626 (pyoverdine biosynthesis row): mutant screen scored by pyoverdine production [PMID:12686626 "The candidate genes were mutated and the effects of the mutations on pyoverdine production were determined"]. Abstract only.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN001254814 | GO:0022857 transmembrane transporter activity | 2 | 118 (36 taxa) | GO:0015562, IDA/IMP, PMID:19906986, PMID:21035449, PMID:22187978, PMID:23766114 (PseudoCAP) | E. coli MacB P75831 | Yes (MacB is an experimentally characterized ABC exporter) | SOUND | Mutants of any pump component trap pyoverdine in the periplasm; PvdT is the energizing IM component. Generic node term suits a MacB-like clade exporting different substrates. |

Shared nodes: pvdR (membrane fusion protein) and opmQ (outer membrane factor) belong to other PANTHER families and do not share PTN001254814, so no node-level defect is shared.

Defects: PSEUDOCAP WRONG_TERM on GO:0002049 pyoverdine biosynthetic process (PROBABLE; indirect phenotype, row does not seed a worklist IBD). No GO_CENTRAL defect.
