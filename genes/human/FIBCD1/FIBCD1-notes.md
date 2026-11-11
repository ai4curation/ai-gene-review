# FIBCD1 (human, Q8N539) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: FIBCD1 was reviewed because it is the closest experimentally characterised relative of the fly
ProtNLM2 benchmark gene CG10359 (B7Z0B2) and the donor of CG10359's ISS chitin-binding and membrane
rows. No ProtNLM2 output was opened or used. This is a first review; no previous review file existed.

### Deep research

`just deep-research-falcon human FIBCD1 --fallback perplexity-lite` failed. Falcon gave a 403 on Edison
auth ("Failed to authenticate"), and the perplexity-lite fallback timed out after 600 s. No deep-research file
was written. Instead, the review rests on primary literature found by a PubMed "FIBCD1" search (27 hits)
and cached with `just fetch-pmid`.

### Evolutionary placement

- PANTHER: PTHR19143:SF45 "FIBRINOGEN C DOMAIN-CONTAINING PROTEIN 1". Per `PTHR19143-entries.csv` the members
  are vertebrates only (human, macaque, mouse, Xenopus). CG10359 is in SF327 (insect/nematode) and ficolins are in SF377/SF454.
- PAINT (`interpro/panther/PTHR19143/PTHR19143-paint.tsv`): the only IBD reaching FIBCD1 is the family-root
  ECM node PTN000441162 (GO:0031012). No PAINT node carries chitin binding, endocytosis or GAG binding. FIBCD1's
  IDA chitin binding was **not** propagated, which I treat as a deliberate decision: chitin binding is
  established for FIBCD1/SF45, not family-wide.
- PMID:35916241 calls CG10359 a "potential orthologue" ["First, we identified the D. melanogaster gene
  CG10359 as a potential orthologue of FIBCD1."]. The basis is InterPro domain and AlphaFold fold similarity,
  not a phylogeny, and PANTHER separates the two.

### What is experimentally established for human FIBCD1

- Type II TM, homotetramer, chitin/acetyl binding, endocytosis [PMID:19710473 "Screening for ligands revealed
  that the FIBCD1 is a high-affinity receptor for chitin and chitin fragments."].
- S1 site mutagenesis [PMID:19892701 "mutations of central residues (A432V and H415G) in the hydrophobic funnel
  (S1) abolish the binding of FIBCD1 to acetylated bovine serum albumin and chitin"].
- Structures: ManNAc in S1, sulfate sites [PMID:24293368]; preference for long chitooligosaccharides, K381L
  [PMID:38072065].
- CS-4S binding and endocytosis to lysosomes by human FIBCD1 in HEK293T [PMID:35916241 "cells expressing hFIBCD1
  showed increased FITC+ cells relative to unstained controls"; uptake "abrogated by compounds that inhibit
  endocytosis, Dynole and PitStop"].
- Surface expression on lung epithelium; immunomodulation (IL-8, mucin suppression) [PMID:30279687]. Mouse
  transgenic: control of gut fungi and colitis [PMID:31601676]. These are phenotype-level and mechanism is unknown,
  so no process terms were proposed.
- Mouse/fly organismal phenotypes (KO learning deficits, fly NMJ RNAi, IPA, mucositis, CRC, myokine) are not
  used for GO process terms.

### Annotation decisions

- GO:0005515 protein binding (IPI x2, MAL, HT Y2H): REMOVE (protein-binding policy).
- GO:0008061 chitin binding (IDA): ACCEPT, core.
- GO:0016020 membrane (IDA, IEA): MODIFY -> GO:0005886 plasma membrane. Apical PM not proposed because
  polarity varies by tissue [PMID:29220632].
- GO:0031012 extracellular matrix (IBA, PTN000441162): MARK_AS_OVER_ANNOTATED with propagation_review
  (TERM_SCOPING_PROBLEM; compartment mismatch). FIBCD1 is a TM receptor that acts on ECM glycans.
- NEW: GO:0035374 chondroitin sulfate binding, GO:0038024 cargo receptor activity and GO:0006898 receptor-mediated
  endocytosis, all from human-protein experiments in PMID:35916241. Endocytosis passes the participation
  test (FIBCD1 is the receptor). Comparator: LRP2, STAB1 and MRC1 carry GO:0006898.

### Implications for transfer to CG10359

Only the FReD fold is shared. The type II TM anchor, which underlies plasma membrane location, cargo receptor
activity and endocytosis, is absent from CG10359, so those functions should not be transferred. Chitin binding
is SF45-level experimental evidence and was not propagated by PAINT, so transferring it across subfamilies
needs target-specific evidence.
