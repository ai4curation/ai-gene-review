# sqz (squeeze, CG5557, Q9VDZ3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: sqz was reviewed because it is the closest experimentally characterised paralog of
dati (Q9V4C9). This review treats sqz in its own right. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon DROME sqz --fallback perplexity-lite` failed: falcon (Edison)
returned `403 Forbidden` on authentication and the perplexity-lite fallback returned
`401 insufficient_quota`. No deep-research file exists. The review is based on the UniProt
record, the PANTHER/PAINT files in `interpro/panther/PTHR16515/`, and the cached
publications listed below (all abstract-only except PMID:30995488 and PMID:25291190).

### Gene product

- 535 aa Krueppel-like C2H2 zinc-finger protein with five C2H2 fingers (aa 158-297) and
  long disordered, Gln-rich N- and C-terminal regions (UniProt FT; MobiDB-lite).
- PANTHER PTHR16515 (PR domain zinc finger protein), subfamily SF66. SF66 is a large,
  heterogeneous catch-all ("C2H2-TYPE DOMAIN-CONTAINING PROTEIN") that also holds Kr,
  su(Hw), yeast MSN2/MSN4, PRDM16 and MECOM (`PTHR16515-entries.csv`). SF66 membership
  therefore does not by itself support transfer of any subfamily-specific function.
- Closest relatives: rotund (rn) and dati. PMID:25291190 groups dati with Rotund/Squeeze and
  vertebrate ZNF384 [PMID:25291190 "dati encodes a zinc finger transcription factor closely
  related to rotund (rn) and squeeze (sqz) with homologs in several species, including humans"].

### PAINT/IBA

- MF GO:0000981 / GO:0000978 and BP GO:0006357 come from PTN004619861 (taxon:2759,
  Eukaryota), a deep node placed over a large set of C2H2 DNA-binding TFs with experimental
  annotations (human, mouse, yeast, worm, fly). sqz sits inside this clade and retains the
  five C2H2 fingers; there is no evidence for loss of DNA-binding. The IBA is a sound
  family-level statement. Note sqz-specific DNA binding (motif, SELEX/PBM, footprint) has not
  been found in the cached literature.
- CC GO:0005634 from PTN009066117.

### Experimental literature (Drosophila)

- PMID:12679036 (Allan 2003): sqz acts in Tv neurons for axon pathfinding and, with ap and
  retrograde BMP (Gbb/Wit), activates FMRFa; ap+sqz misexpression with BMP activation induces
  ectopic FMRFa ["This signal acts together with apterous and squeeze to activate FMRFamide
  expression."]. Genetic evidence of transcriptional control of a target gene.
- PMID:14568107 (McGovern 2003): pan-neural misexpression of sqz perturbs CNS axon pathways
  (gain-of-function screen).
- PMID:15748845 (Allan 2005): ap, sqz, dimm and BMP interact "genetically and biochemically"
  in subtype-specific combinatorial codes; UniProt records an interaction with Ap.
- PMID:17428824 (Terriente Felix 2007): Nab binds Sqz directly (pull-down) via its conserved
  C-terminal domain; Nab is a co-activator of Sqz; Nab and Sqz limit ap-neuron number and
  specify Tv fate. FlyBase annotates nab to GO:0003712 transcription coregulator activity
  IPI with this paper (QuickGO query, 2026-10-21), consistent with Sqz being the DNA-bound
  partner. Source of the sqz GO:0048666 neuron development IMP.
- PMID:17442544 (Herrero 2007): Sqz is expressed in all leucokinergic neurons; required for
  Lk expression in LHLK and SELK cells, sufficient to induce ectopic ABLK-like cells.
- PMID:17276922 (Komiyama & Luo 2007): sqz required for olfactory projection-neuron dendritic
  targeting (MARCM). Source of GO:0070983 dendrite guidance IMP.
- PMID:18948419 (Tsuji 2008): NB3-3 lineage; neuroblast entry into quiescence regulated by
  Hox and temporal factors plus Nab. Abstract does not name sqz; source of GO:0014019
  neuroblast development IMP (curator read full text; not overruled).
- PMID:19945380 (Baumgardt 2009) and PMID:20485487 (Karlsson 2010): NB5-6T lineage; castor
  temporal window subdivided by feed-forward loops. In the full text (not cached) sqz/nab form
  one of the castor-triggered subtemporal loops; abstracts do not name sqz, so this is not
  quoted as support.
- PMID:27848019 (Percival-Smith 2017): Sqz misexpression induces ectopic T1 beard; a
  non-specific gain-of-function effect.
- PMID:30995488 (Shokri 2019): Y2H TF-TF screen; source of the Sqz-Rel protein binding IPI.
- Disruption phenotype: larval lethal with "squeezing" body-wall overcontraction (UniProt CC).

### Decisions

- IBA MF/BP/CC rows: ACCEPT (family-level, consistent with sqz biology).
- GO:0005515 Rel (Y2H): REMOVE under the protein-binding policy (interaction not disputed).
- IMP neuron development: ACCEPT (core organismal role: neuron subtype identity).
- IMP neuroblast development and dendrite guidance: KEEP_AS_NON_CORE.
- ARBA IEA rows (anatomical structure morphogenesis, cell differentiation, system
  development, animal gross anatomical part developmental process): TOO_GENERAL; each is an
  ancestor of the accepted IMP terms (checked with `runoak ancestors -p i,p`).
- No NEW terms. `neuron fate specification` (GO:0048665) was considered: comparator check
  (QuickGO, taxon 7227) shows the co-acting Ap-cluster regulators (ap, nab, dimm) do not carry
  it from these papers; FlyBase used neuron development instead. Left as a question.

### What is experimentally established for sqz vs inferred (for transfer to dati)

- Established in D. melanogaster: nuclear-acting regulator of neuron subtype identity
  (FMRFa in Tv, Lk in leucokinergic neurons, ap-cluster cell number); physical interaction
  with the co-activator Nab; genetic/biochemical interaction with Ap; PN dendritic targeting;
  larval lethality.
- Inferred only (family/PAINT): sequence-specific DNA binding and RNA Pol II-specific
  DNA-binding TF activity; nuclear localization (UniProt ECO:0000305).
