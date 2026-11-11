# CG42331 (Q9VC41) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

The previous review file was an uncurated stub (all rows PENDING). This re-review did not use any ProtNLM2 output.

### Identity
- FlyBase CG42331 (FBgn0259233) has 3 transcripts and 2 unique polypeptides. CG42331-PB and CG42331-PD are 1615 aa (UniProt Q9VC42), and CG42331-PC is 1439 aa (UniProt Q9VC41, the benchmark accession).
- Q9VC41 is an exact C-terminal suffix of Q9VC42, starting at Q9VC42 residue 177, so it is an N-terminally truncated alternative isoform. It lacks the 1-22 signal peptide and the 176-residue N-terminal extension, but keeps the whole animal haem peroxidase domain, which starts at the YRTxDGxCNN motif. The analysis is in `CG42331-bioinformatics/RESULTS.md`.
- The UniProt symbol CG13632 and synonym CG6879 are historical. The current FlyBase symbol is CG42331.
- Catalytic residues are all conserved in Q9VC41: Asp85 and Glu217 (covalent heme links), His86 (distal His), Arg214, His318 (proximal His) and the Ca2+ loop. The UniProt CAUTION line does not refer to a core catalytic residue.

### Phylogeny (PANTHER 19.0)
- SF109 contains only the fly protein among the reference proteomes.
- The leaf sits in a polytomy at the fly-specific duplication node PTN008518854, together with cardinal (cd, SF141) and the clade of Pxd and CG4009 (SF86) with CG10211 (SF134).
- Pxt (SF4, chorion hardening/oogenesis) is more distant: it is in the Pxt+Irc clade under PTN007509807. So the reproduction-related ARBA terms are not supported by the subfamily.
- The peroxidase activity IBD is at the deep node PTN000158755. FlyBase shows the IBA on the gene, and in UniProt it appears on Q9VC42.
- There is no vertebrate or worm ortholog. The closest characterised relatives are fly paralogs: Pxd (Q01603, Swiss-Prot, IDA lactoperoxidase-type activity, chorion location) and cardinal (IMP ommochrome biosynthesis). I chose Pxd as the next relative to review, as the best biochemically characterised member of the same polytomy. Neither Pxd nor cd has a review in the repo.

### PANTHER family review
- `interpro/panther/PTHR11475/PTHR11475-review.yaml` places CG42331 in SF109, which agrees with this review. That file's mention of a "predicted Peroxidasin name" comes from an automated name. CG42331 lacks the LRR and Ig domains of peroxidasin (Pxn is in SF58, a different clade), so collagen IV cross-linking should not be transferred.

### Decisions
- Peroxidase activity and heme binding: ACCEPT.
- Oxidoreductase activity: MODIFY to peroxidase activity.
- Extracellular region: UNDECIDED, because the PC isoform lacks a signal peptide while the PB/PD isoform has one.
- Response to oxidative stress and cellular oxidant detoxification: MARK_AS_OVER_ANNOTATED.
- The 3 ARBA developmental/reproductive BP terms: REMOVE.
- The deep research (falcon) found no CG42331-specific functional literature. Hurd et al. 2015 screened CG42331 RNAi, but the positive hit was cysu (CG5873).
- Modules: no module contains CG42331. `modules/dmel_ommochrome_biosynthesis.yaml` (cardinal) and `modules/dmel_eggshell_structural_proteins.yaml` only touch relatives.
