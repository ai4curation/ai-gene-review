# putA (PA0782, Q9I5F6) review notes

No deep-research API was available. These notes come from manual literature
research on 2026-11-05: the cached publications, a Europe PMC title search for
"putA AND Pseudomonas" (PubMed MCP and NCBI E-utilities returned server errors
that day), and the UniProt record.

## Biology

- PutA of P. aeruginosa PAO1 is a bifunctional proline dehydrogenase (PRODH) /
  1-pyrroline-5-carboxylate dehydrogenase (P5CDH). The native enzyme was purified
  from PAO1 and oxidises L-proline to glutamate in two steps [PMID:6819140
  "Pro/P5C dehydrogenase oxidized L-proline in an FAD-dependent reaction to
  L-delta 1-pyrroline-5-carboxylic acid and converted this intermediate with NAD
  or NADP as cosubstrates to L-glutamic acid"].
- Kinetics: Km 45 mM for L-proline, 0.03 mM for NAD and 0.17 mM for NADP, so NAD+
  is the preferred cosubstrate [PMID:6819140 "Its apparent Km values were 45 mM
  for L-proline, 0.03 mM for NAD and 0.17 mM for NADP"]. Single 119 kDa subunit,
  native dimer/tetramer.
- Domain architecture: P. aeruginosa PutA (1060 aa) has the PRODH and P5CDH
  domains but lacks the N-terminal ribbon-helix-helix (RHH) DNA-binding domain of
  the E. coli/Salmonella PutA [PMID:29632523 "In P. aeruginosa, PutA is 1,060
  amino acid residue long and contains only two domains, PRODH domain and P5CDH
  domain."]. The authors conclude [PMID:29632523 "It is unlikely that PutA
  functions as a transcriptional repressor to regulate the expression of Put
  system in P. aeruginosa."]. My check of the N-terminal sequence (MFKASHVLQG...)
  agrees: no RHH motif precedes the Pfam PF14850 domain at residues 74-187.
- putA is activated by the AraC/XylS regulator PruR, which binds the putA
  promoter; glutamate releases PruR [PMID:29632523 "An AraC/XylS family protein,
  PruR, directly bound to the upstream of -35 box in the putA promoter and
  activated putA expression."]. PutA is required for virulence in a mouse acute
  pneumonia model and for oxidative-stress tolerance (same paper).
- Consequences for the IEA rows: GO:0003700 DNA-binding transcription factor
  activity and GO:0006355 regulation of DNA-templated transcription (InterPro2GO
  from IPR025703, the whole bifunctional-PutA family) are over-propagated from
  RHH-containing enterobacterial PutAs. GO:0055129 L-proline biosynthetic process
  (from IPR005933) is the reverse of this enzyme's physiological direction.
- Membrane location: E. coli PutA associates with the inner membrane when
  proline is high; PRODH reduces membrane quinone (EC 1.5.5.2). No direct
  localization data exist for P. aeruginosa PutA, so the IBA/IEA
  "cytoplasmic side of plasma membrane" rows are plausible but unverified.

## PseudoCAP IBA-seed assessment

Other seeds read from .cache/paint/IBD.gaf (column 8) on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000193023 | GO:0003842 L-glutamate gamma-semialdehyde dehydrogenase (NAD+) activity | 5 | 62 (52 taxa) | GO:0003842, IDA, PMID:6819140 (PseudoCAP) | SOUND | Native PutA purified to >98% from PAO1 converts P5C to glutamate with NAD (Km 0.03 mM) or NADP; abstract states this outright. | E. coli PutA P09546, S. typhimurium PutA P10503, Q2FV67 (S. aureus RocA), yeast PUT2 SGD:S000001079 | Yes |

The node term (P5C/GSA dehydrogenase, NAD+) is shared by bifunctional PutAs and
monofunctional P5CDHs (RocA, Put2), so it suits the clade. No PSEUDOCAP or
GO_CENTRAL defect.

Observation outside this seed: the same node carries a GO:0009898 cytoplasmic
side of plasma membrane IBD seeded only by E. coli PutA (P09546), although yeast
PUT2 (a mitochondrial matrix enzyme) is a seed of sibling IBDs on this node.
Whether eukaryotic leaves inherit 9898 depends on NOT annotations lower in the
tree, which I did not check; flagged as a question, not a defect.

## Action summary

ACCEPT: GO:0003842 (IDA, IBA, IEA), GO:0004657 (IDA, IEA), GO:0006562 (IBA, IEA).
KEEP_AS_NON_CORE: GO:0009898 (IBA, IEA). TOO_GENERAL: GO:0016491.
REMOVE: GO:0003700, GO:0006355, GO:0055129 (all IEA).
GO:0010133 (proline catabolic process to glutamate) is obsolete, so GO:0006562 is
the most specific BP available.
