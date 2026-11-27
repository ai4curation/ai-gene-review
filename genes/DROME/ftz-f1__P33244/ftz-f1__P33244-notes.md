# ftz-f1 (P33244) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder for the reviewed Swiss-Prot canonical entry P33244 (FBgn0001078). The sibling
folder `genes/DROME/ftz-f1/` is keyed to M9NFK2, which is identical to isoform P33244-2.
No ProtNLM2 files or prediction-evidence folders were opened for this review.

### Setup
- `just fetch-gene DROME P33244 --alias ftz-f1__P33244` (41 GOA rows) and
  `just fetch-gene-pmids DROME ftz-f1__P33244`. Also cached PMID:9020363, 9020364,
  1448096, 1709303.
- Deep research: `just deep-research-falcon DROME P33244 --alias ftz-f1__P33244 --fallback perplexity-lite`
  failed twice. Falcon returned "Edison API request failed: Failed to authenticate" (403),
  and the perplexity-lite fallback also failed. The review is therefore based on primary
  literature read directly from `publications/`, plus the UniProt record.

### Isoforms
- P33244-1 (isoform B, 1027 aa, displayed) is the embryonic alphaFTZ-F1 form
  (PMID:1709303). P33244-2 (isoform A, 803 aa) is the metamorphic betaFTZ-F1 form
  (PMID:8096644). Both share the C-terminal 629 aa, which contains the DBD, the FTZ-F1 box
  and the LBD (see the sibling folder's `ftz-f1-bioinformatics/RESULTS-rereview.md`).
- The paralog Hr39 (Q05192, UniProt name "Nuclear hormone receptor FTZ-F1 beta") is a
  different gene in PANTHER SF25. It is not the beta isoform.

### Evolutionary grounding (ftz-f1__P33244-bioinformatics/RESULTS.md)
- P33244 is in PTHR24086:SF15 together with Bombyx FTZ-F1 and C. elegans nhr-25. SF-1
  (SF24) and LRH-1 (SF18) are in different subfamilies.
- All IBA rows come from PTN000639680, a bilaterian (taxon:33213) NR5A node carrying
  only generic terms: GO:0000978, GO:0006357, GO:0090575, GO:0009755 and GO:0009888.
  PAINT did not place steroidogenesis, sex determination, phospholipid binding or
  bile-acid terms at this node, and I read that as a deliberate decision. No vertebrate
  ligand or metabolic function is transferred.

### What is experimentally established in Drosophila (usable as transfer reference)
- Monomeric sequence-specific DNA binding to YCAAGGYCR via the DBD plus the FTZ-F1 box
  [PMID:1448096 "the FTZ-F1 box governs the recognition of the first three bases, while
  the zinc finger region recognizes the remaining part of the binding sequence"].
- Transcription activation through the F1RE [PMID:8164672]. betaFTZ-F1 also represses
  its own gene [PMID:7954827].
- Ftz cofactor activity: AF-2/LXXLL interaction [PMID:11157757, PMID:11592991], a
  complex in embryos and cooperative DNA binding [PMID:9020364], an obligatory
  maternal cofactor [PMID:9020363]. Pair-rule phenotype in embryos lacking maternal
  FTZ-F1 [PMID:9020364]. Added NEW GO:0007366 on participation grounds: FTZ-F1 is the
  DNA-bound co-activator at Ftz target enhancers [PMID:19679121].
- Ecdysone competence factor at the prepupal-pupal transition [PMID:7954827,
  PMID:11060234, PMID:21145504, PMID:12710964]. Also mushroom body gamma-neuron pruning
  via EcR-B1 [PMID:21131955], pupation timing via shade [PMID:27226323] and prothoracic
  gland steroidogenesis via scavenger receptors [PMID:23637637].
- S2 cells: bound at E75A enhancers (ChIP), interacts with MET and GCE, and is required
  for JH activation of E75A [PMID:21832074].
- No ligand: FTZ-F1 does not bind phospholipids [PMID:23737522], and mammalian NR5A
  proteins rescue fly mutants [PMID:23340581]. On this basis I changed both
  `nuclear receptor activity` rows (GO:0004879, which is defined as ligand-regulated) to
  MODIFY with GO:0001228 as the replacement.

### Decisions worth flagging
- Cytoplasm (NAS, PMID:12655640): UNDECIDED. The germline review abstract does not
  mention FTZ-F1.
- Dendrite morphogenesis (PMID:23977298): ftz-f1 is not in the cached main text; kept as
  non-core and deferred to the curator.
- Protein binding with Ftz: MODIFY to GO:0061629. GO:0001223 was rejected because its
  definition excludes coactivators that bind DNA.
