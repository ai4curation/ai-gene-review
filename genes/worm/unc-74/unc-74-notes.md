# unc-74 notes

## 2026-11-21

- `just fetch-gene worm unc-74` could not resolve the WormBase symbol because
  UniProt Q9N4L6 lists `ZK973.11`/`CELE_ZK973.11` gene names rather than
  `unc-74`. I fetched the curated directory with the authoritative accession:
  `just fetch-gene worm Q9N4L6 --alias unc-74`.
- `just mod-description-deep-research worm unc-74` returned `no_curated`,
  indicating that WormBase has no cached hand-written description for this
  gene. `just deep-research-falcon worm unc-74 --fallback perplexity-lite`
  failed because neither external provider was available. The review therefore
  used the seeded GOA rows, cached primary papers mentioning UNC-74 or its TMX3
  orthologs, UniProt, PTHR46426 family membership, and the
  levamisole-sensitive AChR module.
- `just fetch-gene-pmids worm unc-74` cached the only GOA PMID source,
  PMID:15623505. `just paint-losses worm unc-74` reported no IRD or IKR loss on
  the Q9N4L6/PTHR46426 lineage.
- UNC-74/Q9N4L6 is a TMX3-family PDI-like protein. The UniProt record predicts
  an N-terminal signal peptide, a luminal thioredoxin domain with redox-active
  Cys55/Cys58, and a C-terminal transmembrane helix. Human TMX3 is the ISS
  source for the WormBase ER-membrane and protein-disulfide reductase rows; it
  localizes to the ER, is membrane associated after alkaline extraction, and
  its recombinant luminal domain has an ER-PDI-like redox potential and oxidase
  activity [PMID:15623505, "TMX3 showed oxidase activity"].
- In the C. elegans levamisole-sensitive AChR reconstitution system, the five
  pore subunits plus RIC-3, UNC-50 and UNC-74 produced robust acetylcholine-
  and levamisole-gated currents in Xenopus oocytes. Removing UNC-74, like
  removing UNC-50, reduced response amplitudes below 10% of the full eight-gene
  cRNA mix [PMID:19020092, "Removal of UNC-50 or UNC-74 reduced response
  amplitudes to <10%"].
- Boulin et al. showed that `unc-50` and `unc-74` were not required for ACR-16
  N-AChR expression in the same oocyte system that expresses C. elegans
  L-AChRs [PMID:19020092, "coinjection of unc-50 and unc-74 cRNAs together with
  ric-3 did not further enhance the N-AChR expression"]. This limits, rather
  than proves, receptor specificity: Jospin et al. found that
  loss-of-function mutations in `unc-50` and `unc-74` suppress
  `acr-2(n2420gf)` convulsions and concluded that both ancillary factors also
  function in ACR-2R assembly and trafficking [PMID:20027209,
  "loss-of-function mutations in unc-50 and unc-74 suppress acr-2(n2420gf)"].
- Three ancillary factors, RIC-3, UNC-50 and TMX3, were also used to express
  Drosophila, honeybee and bumblebee nAChRs in Xenopus oocytes. Drosophila
  DmTMX3/CG5027 is described as an ortholog of the C. elegans UNC-74
  expression cofactor, and adding DmTMX3 to Dalpha1/Dbeta1 yielded robust
  ACh-induced inward currents [PMID:32611810, "This resulted in robust inward
  current responses to 100 µM ACh"].
- D'Alessandro et al. summarized UNC-74 as a predicted thioredoxin homologous
  to TMX-3 that is necessary for L-AChR expression, while emphasizing that its
  detailed function remained unknown [PMID:30407909, "It is necessary for
  L-AChR expression, but its detailed function remains uncharacterized"].
- The H. contortus ortholog was cloned as Hco-unc-74/HQ116821. It has the same
  signal-peptide, thioredoxin-domain, C-terminal-transmembrane architecture,
  and the Hco-RIC-3/Hco-UNC-50/Hco-UNC-74 ancillary set was strictly required
  for functional H. contortus L-AChR expression in Xenopus oocytes
  [PMID:21486278, "never yielded any detectable currents"].
- The `GO:0045454 cell redox homeostasis` UniRule row was marked
  over-annotated. The conserved thioredoxin-domain oxidoreductase role is well
  supported by the TMX3-family evidence, but the nematode evidence links
  UNC-74 to nicotinic acetylcholine receptor folding or expression, not to
  regulation of a cellular redox environment as a broader process.
