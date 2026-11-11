# ATG3 (horse, A0A3Q2L0A4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior folder). Created with `just fetch-gene HORSE A0A3Q2L0A4 --alias ATG3`;
stub id confirmed as A0A3Q2L0A4. ProtNLM2 predictions were not opened or used.

### Deep research

`just deep-research-falcon HORSE ATG3 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" and the perplexity fallback returned
HTTP 401 insufficient quota. No deep-research file exists. The review uses the cached
publications on human/mouse ATG3 and the reviewed human UniProt record instead.

### Identity of the benchmark accession

- A0A3Q2L0A4 is unreviewed (PE 3), 342 aa, RefSeq XP_005602052.1 / Ensembl ENSECAT00000058152.
- Human ATG3 Q9NT62 is 314 aa. Global alignment (file:HORSE/ATG3/ATG3-bioinformatics/RESULTS.md):
  98.41% identity over all 314 human residues; one 28-aa horse insertion
  (VVADITKPCWTDFFLPPLLGVNFPPNNP) after human residue 222, in the catalytic core between a
  beta strand (212-220) and a helix (229-232).
- Catalytic Cys-264 -> horse Cys-292; N-terminal amphipathic helix, LIR (DGGW..V) and LETD
  caspase motif conserved.
- Other horse ATG3 entries (A0A3Q2HYB0, F6T6K3, A0A3Q2H2Q9, L7MRX2) lack the insertion;
  none is a full-length 314-aa equivalent; L7MRX2 (transcript evidence fragment) lacks it.
- Conclusion: the benchmark accession is an alternative gene model / possible isoform of horse
  ATG3 with an unverified internal insertion; it is not a fragment and all known catalytic
  and interaction residues are present. There is no reviewed horse ATG3 entry.
- The donkey benchmark A0A9L0IHI0 (genes/EQUAS/ATG3) has the identical insertion.

### Evolutionary placement

- PANTHER PTHR12866:SF2 (UBIQUITIN-LIKE-CONJUGATING ENZYME ATG3), same subfamily as human
  Q9NT62, mouse Q9CPX6 and yeast P40344 (interpro/panther/PTHR12866 entries file). No
  subfamily disagreement; the other subfamily in the reviewed set (SF5) is ATG10.
- IBA rows come from PTN000305307 (autophagosome assembly, PAS, nucleophagy, glycophagy)
  and PTN000305308 (cytosol, mitophagy, Atg8-family conjugating enzyme activity).
- PAINT did not propagate Atg12 transferase, cilium, apoptosis-related mitochondrial
  fragmentation, plasma membrane or E3-complex membership; those arrive only via Ensembl
  Compara projection of human/mouse annotations. Treated the omission as deliberate.

### Key literature

- Tanida 2002 [PMID:11825910 "Site-directed mutagenesis revealed that Cys(264) of hApg3p is
  an authentic active-site cysteine residue"]: human ATG3 is the E2 for LC3/GABARAP/GATE-16.
- Qiu 2013 [PMID:24186333 "Atg3 likely cycles back and forth between binding to Atg7 for
  loading with the UBL LC3 and binding to E3 to promote LC3 lipidation"]: E3 contact is
  transient and competitive with E1, which argues against stable membership in the
  ATG12-ATG5-ATG16L1 complex.
- Radoshevich 2010 [PMID:20723759 "ATG12-ATG3 complex formation requires ATG7 as the E1
  enzyme and ATG3 autocatalytic activity as the E2"]: ATG3 auto-conjugates ATG12; loss of
  the conjugate causes mitochondrial expansion/fragmentation and resistance to
  mitochondrial cell death, a downstream phenotype rather than ATG3 executing fragmentation.
- Farnung 2023 [PMID:37252361]: noncanonical LIR required for ATG3~LC3 thioester formation.

### Decisions summary

Core: GO:0141046 (MF), GO:0000045 (BP), cytosol/PAS (CC). "Atg8-family ligase activity"
(E3 class) -> MODIFY to GO:0141046. "protein ubiquitination" -> MODIFY to GO:0061739
protein lipidation involved in autophagosome assembly (ATG3 transfers ubiquitin-like
proteins, not ubiquitin). Selective autophagy IBAs kept non-core. Plasma membrane,
E3-complex part_of, mitochondrial fragmentation in apoptosis and regulation of cilium
assembly marked over-annotated.

### Relative

Human ATG3 Q9NT62 (same PANTHER subfamily SF2, PAINT donor) has no review in the repo
(only worm atg-3 and donkey ATG3 exist). Needs review.
