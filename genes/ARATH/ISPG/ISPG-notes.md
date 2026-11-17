# ISPG (At5g60600; HDS / GCPE / CLB4 / CSB3) review notes

## Sources checked

The GOA rows cite PMID:11943178, PMID:12938931, PMID:15650872, PMID:16167903,
PMID:16207701, PMID:18431481, PMID:18633119, PMID:20061580, PMID:25293756 and
PMID:28887381; all are cached. The UniProt function and localization comments also
cite PMID:15133149, PMID:16480720 and PMID:18236010; these were fetched into the
cache for this review. PMID:11943178, PMID:15650872, PMID:16167903, PMID:16480720,
PMID:15133149 and PMID:18236010 are abstract-only in the cache, so the review relies
on their abstracts and does not claim details only present in the full text.

## Enzyme activity and electron donor

- Plant GcpE carries a [4Fe-4S] cluster and makes HMBPP from MEcPP
  [PMID:15650872 "It corresponds to a [4Fe-4S] cluster, suggesting that both plant and bacterial enzymes catalyze the reduction of 2-C-methyl-D-erythritol 2,4-cyclodiphosphate into (E)-4-hydroxy-3-methylbut-2-enyl diphosphate via two consecutive one-electron transfers"].
- The plant enzyme cannot use the bacterial flavodoxin shuttle
  [PMID:15650872 "the plant enzyme could not use this reduction system"]; activity in
  that paper was detected only with a 5-deazaflavin radical, so the ferredoxin-specific
  part of GO:0046429 does not come from this paper.
- Ferredoxin coupling comes from PMID:16480720: illuminated spinach thylakoids alone
  reduce the Arabidopsis enzyme, and in the dark ferredoxin, FNR and NADPH are needed
  [PMID:16480720 "In the dark, the plant GcpE catalysis requires in addition of ferredoxin NADP(+)/ferredoxin oxido-reductase and NADPH as electron shuttle."].
  The abstract says the light reaction acts "most probably via ferredoxin", so the
  direct ferredoxin requirement rests on the dark-reaction reconstitution.
- In vivo function: the mature Arabidopsis protein complements an E. coli gcpE mutant
  [PMID:11943178 "the Arabidopsis mature GCPE was able to complement a gcpE-defective E. coli strain"].

## Localization

- N-terminal transit peptide targets the protein to chloroplasts in vivo
  [PMID:11943178 "We demonstrate that the N-terminal region targets the Arabidopsis protein to chloroplasts in vivo"].
- GFP fusions place the MEP pathway enzymes in chloroplasts [PMID:18236010].
- Stromal proteomics (PMID:16207701, PMID:18431481, PMID:20061580) identify it in
  purified stroma; AT_CHLORO (PMID:20061580) specifically assigned subplastidial
  location by spectral-count partitioning between stroma, thylakoid and envelope.
- The chloroplast envelope HDA row (PMID:12938931) comes from "mixed" envelope
  preparations; a soluble stromal enzyme in such a list is most likely a stromal
  contaminant. Kept as over-annotation rather than removed.
- The nucleus row is an AtSubP prediction (ISM); nothing supports nuclear location.

## Mutant phenotypes (pleiotropic)

- clb4 null: albino, early arrest of chloroplast differentiation
  [PMID:15133149 "Molecular characterization of the noncell autonomous clb4 mutant established that the CLB4 gene encodes for hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase (HDS)"].
  This reflects loss of plastid isoprenoids (carotenoids, chlorophyll phytol,
  plastoquinone), not a direct role in chloroplast organization; no NEW row was added.
- csb3 (G696D, clb4-3) hypomorph: enhanced SA-dependent resistance to biotrophs,
  reversed by fosmidomycin [PMID:16167903]. The defense phenotype is a metabolic
  consequence; GO rows (response to bacterium, SAR SA pathway; acts_upstream_of_or_within)
  kept as non-core. The signalling metabolite linking HDS to SA (MEcPP accumulation
  is the leading candidate in later literature) was not checked against cached papers
  here, so it is only raised as a question.

## Phylogeny

PAINT places GO:0046429 at PTN000765215 and chloroplast at PTN000765210, with At5g60600
itself among the experimental seeds (expected, not circular). Plant HDS belongs to the
long "plant-type" IspG (IPR017178, PIRSF037336) with an extra central domain
[PMID:11943178 "contains two structural domains that are absent in the E. coli protein: an N-terminal extension and a central domain of 30 kDa"].
