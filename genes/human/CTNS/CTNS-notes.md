# CTNS (cystinosin, UniProtKB:O60931) - review notes

Literature work was done manually from cached publications, UniProt and Reactome (no
provider deep-research file was available when the review was written).

## Biology

- CTNS encodes cystinosin, a seven-transmembrane PQ-loop family protein of the lysosomal
  membrane [PMID:9537412 "CTNS encodes an integral membrane protein, cystinosin, with features
  of a lysosomal membrane protein"].
- Cystinosin is a proton-coupled cystine exporter: redirected to the plasma membrane it
  takes up L-cystine at acidic pH, and the authors conclude it is "a novel H(+)-driven
  transporter that is responsible for cystine export from lysosomes" [PMID:11689434].
  Electrophysiology shows cystine binding is coupled to protonation of a buried aspartate
  [PMID:22232659 "cystine binding is coupled to protonation of a clinically relevant aspartate
  buried in the membrane"]. Cryo-EM structures capture lumen-open, cytosol-open and
  cystine-bound states [PMID:36113465].
- Lysosomal targeting uses a C-terminal GYDQL tyrosine motif (AP-3 dependent) plus a second
  conformational motif in the third cytosolic loop [PMID:11150305; PMID:25753619]. An
  alternatively spliced isoform, cystinosin-LKG, lacks GYDQL and is also found at the plasma
  membrane [PMID:18337546].
- Cystinosin also localises to melanosomes, and CTNS silencing reduces melanin synthesis
  [PMID:22649030].
- Cystinosin engages the Ragulator-Rag complex in a conformation-dependent manner, linking
  lysosomal amino acid efflux to mTORC1 signalling [PMID:36113465 "show conformation-dependent
  Ragulator-Rag complex engagement"].

## Disease

Biallelic CTNS variants cause cystinosis (nephropathic infantile, juvenile, and ocular
forms) with intralysosomal cystine accumulation; infantile disease generally results from
total loss of transport activity [PMID:15128704 "infantile cystinosis generally resulting from
a total loss of activity"].

## Curation decisions

- Core MF: GO:0015184 L-cystine transmembrane transporter activity plus GO:0015295
  solute:proton symporter activity (cystine/H+ symport).
- Core BP: GO:1904919 L-cystine transmembrane transport from lysosomal lumen to cytosol.
- Patient-cell phenotypes (glutathione redox state, ATP content, non-verbal cognition)
  are downstream consequences of cystine storage, not processes cystinosin performs.
- Reactome "SLC-mediated transport of oligopeptides" (TAS, oligopeptide transmembrane
  transport) does not fit: cystine is a disulfide-linked amino acid dimer, not an
  oligopeptide.
