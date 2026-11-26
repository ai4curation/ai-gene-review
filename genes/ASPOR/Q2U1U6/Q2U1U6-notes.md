# Q2U1U6 notes

## Re-review 2026-10-01 (GOA refresh)

- Current GOA snapshot has no rows for Q2U1U6; nothing to review or retire.
- Audit of core_functions: removed the `locations: GO:0005576 extracellular region`
  assertion, which had no supporting evidence (the review's own knowledge gap states
  secretion is unknown and no signal peptide is annotated). Added a knowledge gap and a
  description caveat that the 134-aa protein may be a truncated gene model / non-catalytic
  fragment (OpenScientist hypothesis report in `Q2U1U6-hypotheses/`: only fold-level
  SSF48230 match over residues 6-97; paralogs Q2TXR4, Q2USR3, Q2UB60 are 395-453 aa).
  The predicted polysaccharide lyase MF is retained as a hedged, domain-based prediction.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used. GOA still has no rows for Q2U1U6, so
the review has no existing annotations to act on; the re-review covers identity, the
description, references and core functions.

### Identity: truncated gene model (new finding)

- New reproducible analysis: `Q2U1U6-bioinformatics/gene_model_check.py`, output in
  `gene_model_check_output.txt`, summary in `RESULTS.md`.
- Q2U1U6 residues 6-134 = residues 280-408 of the 408-aa *A. flavus* NRRL 3357 protein
  A0A7U2MCM8 (128/129 identical); same for *A. minisclerotigenes* A0A5N6JAE3 (408 aa).
  *A. fumigatus* Q4WKU8 (399 aa) aligns over 272-398 (97/127). Q2U1U6 is the C-terminal
  third only.
- The missing N-terminal 279 residues are encoded in RIB40 (AP007170.1 ~186173-187010,
  frame +1), joined to the annotated exon by a 65-nt GT...AG intron (187011-187075). The
  annotated start ATG (187060) lies inside that intron. So AO090138000091 omits exon 1;
  the true product should be ~408 aa. RefSeq XP_001825602.3 is identical to the 134-aa
  model, so the error is shared by DDBJ, RefSeq and UniProt.
- The InterPro toroid domain spans ~62-371 in the full-length ortholog; Q2U1U6 contains
  only 280-371 of it, explaining the weak SSF48230 match (residues 6-97, E 4e-06).
- No other UniProt entry exists for this RIB40 locus, so there is no canonical product of
  the same gene to review. A0ABQ6LHX9 (*A. oryzae* var. *brunneus*, 745 aa) contains
  Q2U1U6 at 612-745 fused to a beta-lactamase-related domain (likely a merged model in a
  different strain), not a canonical product of this RIB40 locus.

### Evolutionary grounding

- No PANTHER family/subfamily for Q2U1U6 or the full-length orthologs (the 745-aa fusion
  has PTHR43283 only over its beta-lactamase part). No Pfam family, no CAZy family in the
  UniProt records; the only signature is fold-level IPR008929/SSF48230/Gene3D 1.50.10.100.
  No PANTHER family review under interpro/panther/ applies.
- UniProt has no reviewed fungal IPR008929 proteins (query: reviewed, taxonomy Fungi).
  Characterized members of this fold are bacterial/viral PLs and animal dermatan sulfate
  epimerases, related only at superfamily level, so no subfamily-specific function
  (substrate, secretion) can be transferred. The "Alginate lyase domain-containing
  protein" names on the fungal orthologs are ProtNLM-generated and were not used.
- Relative: no experimentally characterized relative can be placed phylogenetically; the
  nearest informative relative is the full-length *A. flavus* ortholog A0A7U2MCM8 (also
  uncharacterized). No modules in modules/ cover this protein.

### Changes to the review

- Description rewritten: removed the GAG-substrate analogy and the CAZyme-repertoire
  framing; now states the truncated gene model and fold-level-only evidence.
- Core function: kept GO:0016837 as a hedged fold-level prediction applying to the
  full-length product; removed `directly_involved_in GO:0000272 polysaccharide catabolic
  process` (a process inferred from the fold alone, with no substrate or pathway
  evidence). Knowledge gaps rewritten (activity/substrate; expression/secretion); the
  "may be a truncated gene model" gap is now resolved by analysis and moved to identity.
- Not added as `NEW`: a fold-level prediction on an unverified gene model does not meet
  the bar for a new annotation.
- References: kept all; added reference_review to each; replaced the genome-paper
  quote (which was only the title) with a methods quote; added the new RESULTS.md.
