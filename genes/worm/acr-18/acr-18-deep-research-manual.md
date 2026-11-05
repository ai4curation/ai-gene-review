# acr-18 (C. elegans) - manual literature research

No deep-research provider API was available for this review, so the literature
search below was done by hand (PubMed searches and the cached publications in
`publications/`). This is not an automatically generated deep-research report.

## Identity

- UniProtKB G5EG72 (unreviewed TrEMBL), WormBase F28F8.1 / WBGene00000057,
  NCBI GeneID 191604, chromosome V. 510 aa.
- Protein named only as "AcetylCholine Receptor" in the record (submitter name).
- Family: Cys-loop ligand-gated ion channel; "Belongs to the ligand-gated ion
  channel (TC 1.A.9) family" (UniProt RuleBase RU000687). Pfam Neur_chan_LBD
  (PF02931, residues 32-237) and Neur_chan_memb (PF02932, 244-489); four
  predicted transmembrane helices (239-261, 273-291, 307-326, 473-492) and a
  predicted signal peptide (1-21). PANTHER PTHR18945.

## Sequence features (own inspection of the UniProt sequence)

- Cys-loop disulfide pair at C155 and C169 (13 intervening residues), the
  defining motif of the Cys-loop receptor superfamily.
- A vicinal cysteine pair, C219-C220 (`...KIYQKIYDCCPHPF...`), in the position of
  loop C of the agonist-binding site. In nAChRs this pair defines an alpha-type
  (principal face) subunit, so ACR-18 is expected to be an alpha subunit that can
  contribute the principal side of an agonist-binding site.

## Family classification

- The C. elegans nAChR-like gene family is the largest known; Jones and
  Sattelle grouped the subunits into groups (UNC-38, UNC-29, ACR-16, ACR-8,
  DEG-3) [PMID:14696039, abstract only in cache: "Analysis of the Caenorhabditis
  elegans genome has revealed one of the most-extensive and diverse nAChR gene
  families known, consisting of at least 27 subunits."]. Nomenclature update
  [PMID:17503100].
- ACR-18 is a DEG-3-group subunit [PMID:23577128: "We observed that acr-18,
  which encodes a DEG-3 type acetylcholine receptor, is also expressed in AVA"].
  The DEG-3 group is nematode-specific. Some characterised DEG-3-group channels
  are gated by ligands other than acetylcholine (e.g. choline for DEG-3/DES-2,
  betaine for ACR-23, from general knowledge of the literature, not verified in
  cached papers for this review). The agonist of ACR-18-containing receptors has
  not been determined by heterologous expression; no paper reporting ACR-18
  electrophysiology was found.

## Experimental work on acr-18

Only one primary paper was found by PubMed searches ("acr-18 elegans",
"ACR-18 OR acr-18 OR F28F8.1 AND nicotinic/acetylcholine/nematode"): Sherlekar
et al. 2013 [PMID:23577128, full text cached].

Key findings:
- Expression: "In both sexes, acr-18 expression is apparent in a number of
  sex-shared head and ventral nerve cord neurons and, in the male, in a subset
  of ray and pre-anal ganglion neurons" and in the backward command interneuron
  AVA [PMID:23577128].
- Function: in males, optogenetic activation of the male-specific interneurons
  PVY and PVX induces reversal. "In acr-18 null mutants, only 28% of males
  reverse in response to PVY+PVX activation" [PMID:23577128].
- Site of action: expression of acr-18(+) from the nmr-1 promoter (AVA, AVD,
  AVE, AVG, RIM, PVC) rescues: "These data suggest that PVY+PVX-induced reversal
  depends on an ACR-18-containing cholinergic receptor that functions in
  nmr-1-expressing cells, most likely the backward command cells as these are
  direct targets of cholinergic PVY and PVX." [PMID:23577128]
- Redundancy: "PVY+PVX-induced reversal depends on cholinergic transmission in
  AVA that is mediated by partially redundant AChRs that contain acr-18-,
  unc-29- and acr-16-encoded subunits." Triple mutants: "only 4% of unc-29;
  acr-16 acr-18 triple mutant males reversed" [PMID:23577128].
- acr-18 single mutants are superficially wild type for backward locomotion
  during natural mating; speed is affected in unc-29; acr-16 but not acr-18
  mutants [PMID:23577128].

What the paper does not show: the subunit partners of ACR-18 (whether it
co-assembles with UNC-29 or ACR-16, or forms a separate receptor), the agonist
of the ACR-18 channel, its ion selectivity or calcium permeability, or the
subcellular location of the protein (expression was by transcriptional
reporters).

## Open questions

1. What ligand gates ACR-18-containing receptors (acetylcholine, choline, or
   another DEG-3-group ligand)?
2. Which subunits co-assemble with ACR-18? Does it form homomers?
3. Is the channel calcium-permeable?
4. Is ACR-18 protein localised at PVY/PVX-AVA synapses?
