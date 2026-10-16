# unc-47 (P34579) — vesicular GABA transporter — curation notes

## Identity

- UniProt P34579 (UNC47_CAEEL, reviewed), WormBase T20G5.6, 486 aa, ten predicted
  transmembrane domains; amino acid/polyamine transporter 2 family. Orthologue of mammalian
  VGAT/VIAAT (SLC32A1).

## Literature

### McIntire et al. 1997 (PMID:9349821, abstract only)

- unc-47 was the founding VGAT gene: "Studies in the nematode Caenorhabditis elegans have
  implicated the gene unc-47 in the release of GABA" [PMID:9349821].
- "Here we show that the sequence of unc-47 predicts a protein with ten transmembrane
  domains, that the gene is expressed by GABA neurons, and that the protein colocalizes with
  synaptic vesicles" [PMID:9349821] — basis of the IDA synaptic vesicle annotation.
- The transport assay was done on the rat homologue: "a rat homologue of unc-47 is expressed
  by central GABA neurons and confers vesicular GABA transport in transfected cells with
  kinetics and substrate specificity similar to those previously reported for synaptic
  vesicles from the brain" [PMID:9349821].
- Bioenergetics differ from VMAT: "Comparison of this vesicular GABA transporter (VGAT) with
  a vesicular transporter for monoamines shows that there are differences in the
  bioenergetic dependence of transport" [PMID:9349821].
- UniProt summarises the worm function as "Involved in the uptake of GABA into the synaptic
  vesicles" with ECO:0000269|PubMed:9349821.

## Assessment

- Core: GABA loading into synaptic vesicles at the synaptic vesicle membrane of GABAergic
  neurons. The GOA set has the process terms (GO:0015812 GABA transport, GO:0098700
  neurotransmitter loading into synaptic vesicle) and the location terms, but no GABA
  molecular-function term; the only MF row is GO:0015187 glycine transmembrane transporter
  activity (IBA). Mammalian VGAT carries GO:0015185 (GABA transmembrane transporter
  activity, IMP/ISS/IEA in QuickGO for SLC32A1 and rat Slc32a1), so the missing GABA MF is a
  gap rather than a convention.
- Glycine: mammalian VGAT loads glycine as well as GABA, and the IBA node is seeded from
  mouse/rat VGAT where glycine transport is experimentally demonstrated (rat Slc32a1
  GO:0015187 IMP PMID:19843525). C. elegans has no glycinergic transmission, and no worm
  data address glycine; these rows are retained but not treated as core for the worm.
- Dendrite terminus (IBA from mouse VGAT) has no worm support and does not match the
  presynaptic site of action; kept as non-core.

## Deep research

- `unc-47-deep-research-falcon.md` supports the review, including the glycine caveat: GABA is
  the physiological substrate, "Thus, UNC-47 acts at the vesicle membrane upstream of
  transmitter release", and while VGAT/VIAAT-family proteins can transport glycine,
  UNC-47-dependent glycinergic signalling in C. elegans is unestablished.
