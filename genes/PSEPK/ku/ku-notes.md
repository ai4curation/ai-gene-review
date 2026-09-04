# ku curation notes

## 2026-09-01

Applied the annotation-reviewer workflow to all five GOA rows. No annotation
remains PENDING or UNDECIDED.

- Q88HU8 is an unreviewed KT2440 protein, so the Ku mechanism is treated as a
  family-supported inference, not as direct experimentation on this protein.
- The target UniProt record supports double-stranded-DNA-end binding and LigD
  recruitment [file:PSEPK/ku/ku-uniprot.txt "Binds linear dsDNA with 5'- and
  3'- overhangs"] [file:PSEPK/ku/ku-uniprot.txt "Recruits and stimulates the
  ligase activity of LigD."].
- PTHR41251 PAINT places double-stranded DNA binding at PTN002222140 using
  P9WKD9 and the Pseudomonas aeruginosa Ku Q9I1W5 as experimental seeds
  [file:interpro/panther/PTHR41251/PTHR41251-paint.tsv
  "PTN002222140	GO:0003690"].
- Pseudomonas aeruginosa Ku protects both DNA ends and works with LigD
  [PMID:20018881 "Ku afforded virtually complete protection from both
  exonucleases"] [PMID:20018881 "PaeKu stimulated ribonucleotide addition to
  DSB ends by PaePOL and DSB end sealing by LigD."].
- Direct P. putida genetics shows that Ku loss changes the mutation spectrum
  under carbon starvation [PMID:25942369 "Both the absence of LigD or Ku
  resulted in"]. The cached paper is abstract-only, so it supports the
  physiological phenotype but is not treated as a direct biochemical assay.
- A second target-organism study perturbed NHEJ-associated enzymes during
  Cas9-induced DSB repair [PMID:36475478 "removal or overproduction of
  NHEJ-associated P. putida KT2440 enzymes on"]. This directly anchors the NHEJ
  process assignment while leaving detailed Ku chemistry to family evidence.

The broad DNA-binding annotation is modified to GO:0003690. Broad DNA repair
and DNA-damage-response terms are retained as non-core context; GO:0003690 and
GO:0006303 define the core function and process.
