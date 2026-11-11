# srp-2 (C05E4.1, O17365) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: srp-2 is reviewed as the closest experimentally characterised relative (paralog) of the
ProtNLM2 benchmark gene worm/C28G1.2. No ProtNLM2 output was opened or used.

### Deep research
- `just deep-research-falcon worm srp-2 --fallback perplexity-lite` failed. Falcon gave
  `403 Forbidden` at Edison auth, and the perplexity-lite fallback also failed. No deep-research
  file exists. The review was built from primary literature found with a Europe PMC search for
  ("srp-2" OR C05E4.1) AND elegans and cached with `just fetch-pmid`.

### Evolutionary placement
- PANTHER PTHR11461 (serpin). srp-2 is in subfamily SF352; C28G1.2 is in SF332 (uniprot.txt; task brief).
- `interpro/panther/PTHR11461/PTHR11461-paint.tsv`: the IBD for GO:0004867 at node PTN002479231
  is seeded only by WB:WBGene00005643 (srp-2). There is no IBD for GO:0004869
  (cysteine-type inhibitor), so PAINT did not propagate the cross-class activity, and we treat
  that as a deliberate decision. The root node PTN000156123 carries the GO:0005576 extracellular
  region IBD. Vertebrate clade B node PTN002606963 has a NOT for GO:0005576. No equivalent NOT
  exists for the nematode intracellular serpins.
- Silverman et al. 2015 used NJ phylogeny and similarity analysis: SRP-2 is not a neuroserpin
  ortholog. Its closest human relative by similarity is SERPINB7, and in their tree it forms its
  own branch [PMID:25786854 "We concluded that SRP-2 is neither an ortholog nor a functional homolog of neuroserpin."].

### Experimentally established in C. elegans SRP-2 (species-specific, on this protein)
- Cross-class inhibition of granzyme B (serine) and cathepsins K/L/S/V (cysteine), shown with
  recombinant protein [PMID:14739286 "Biochemical analysis of recombinant SRP-2 protein revealed SRP-2 to be a dual cross-class inhibitor of the apoptosis-related serine proteinase, granzyme B, and the lysosomal cysteine proteinases, cathepsins K, L, S, and V."]. Only the abstract is cached (JBC returned 403).
- Cytosolic, not ER, not secreted (GFP fusions; ER marker) [PMID:25786854 "Using confocal imaging and an ER colocalization marker, we confirmed that GFP-tagged wild-type SRP-2 localized to the cytosol and not the ER."].
- Expressed in embryo, intestine and hypodermis. Overexpression causes larval arrest. This is a
  gain-of-function phenotype only, so no process term was added [PMID:14739286].

### Inferred, not established
- The physiological target peptidase in the worm is unknown.
- A role in lysosomal-injury protection (as for SRP-6) has not been tested for SRP-2.

### Decisions
- GO:0004867 IDA and IEA: ACCEPT. GO:0004869 IDA: ACCEPT. For transfer, the cysteine-type
  activity is specific to SRP-2 and should not be propagated to C28G1.2.
- GO:0005576 IBA and IEA: REMOVE. SRP-2 is contradicted by direct evidence: no signal peptide,
  cytosolic, and not secreted.
- NEW GO:0005829 cytosol (IDA, PMID:25786854).
- PMID:23335331 (Schipanski 2013), which claimed SRP-2 aggregates in the ER lumen, is marked
  DISPUTED.
