# Psmc4 (rat, Q63570): manual literature research

No deep-research provider API was available for this session, so this summary was
compiled by hand from the cached publications, the UniProt record and PubMed
searches. Every claim carries its source.

## Identity

- Rat Psmc4 (UniProt Q63570, PRS6B_RAT, 418 aa) is the 26S proteasome regulatory
  subunit 6B, also known as TBP7 and, in yeast nomenclature, Rpt3.
  [PMID:8607789 "The protein sequences of rat TBP1, TBP7, MSS1, S4, and SUG1 predicted from the open reading frames consist of 439, 418, 433, 440, and 406 amino acid residues, respectively"]
- It belongs to the AAA ATPase family, with a P-loop/Walker A ATP-binding segment
  at residues 206-213 (UniProt FT BINDING, ECO:0000255), and InterPro AAA core
  (IPR003959), AAA conserved site (IPR003960), AAA lid (IPR041569) and the
  proteasomal ATPase OB-fold domain (IPR032501). PANTHER family PTHR23073
  (26S proteasome regulatory ATPase). [file:rat/Psmc4/Psmc4-uniprot.txt]
- The C-terminus of the rat sequence ends ...HEFYK, which matches the
  hydrophobic-tyrosine-X (HbYX) motif that proteasomal ATPase tails use to dock
  into the 20S alpha ring and open its gate (sequence read from the UniProt
  record; the HbYX mechanism is from PMID:17803938, which tested Rpt2 and Rpt5
  peptides, not Rpt3 directly).
  [PMID:17803938 "These ATPases contain a conserved C-terminal hydrophobic-tyrosine-X motif (HbYX)."]
- The rat cDNA paper noted helicase-like motifs and speculated about RNA/DNA
  unwinding; this was a sequence-based speculation that was not borne out: the
  motifs are the AAA Walker A/B and arginine-finger elements.
  [PMID:8607789 "These findings suggest a common function of the rat proteasomal ATPases in ATP-dependent RNA/DNA unwinding."]

## Function (mostly by orthology to human PSMC4 / yeast Rpt3)

- UniProt (by similarity to human P43686): component of the 26S proteasome; one of
  the six AAA ATPases of the base heterohexamer that unfolds ubiquitinated
  substrates and translocates them into the 20S proteolytic chamber.
  [file:rat/Psmc4/Psmc4-uniprot.txt "PSMC4 belongs to the heterohexameric ring of AAA (ATPases associated with diverse cellular activities) proteins that unfolds ubiquitinated target proteins that are concurrently translocated into a proteolytic chamber and degraded into peptides."]
- Subunit: base of the 19S regulatory particle.
  [file:rat/Psmc4/Psmc4-uniprot.txt "a base containing 6 ATPases including PSMC4 and few additional components"]
- Location: cytoplasm and nucleus (by similarity).

## Rat experimental data

### Rousseau et al. 2009 (PMID:18986984, full text read)

- In rat hippocampal primary neurons (E18 rats), endogenous Rpt3 co-localised with
  mutant huntingtin (Htt73) inclusions, while the 20S alpha7 subunit did not.
  [PMID:18986984 "Rpt4 and Rpt3 co-localize with poly(Q) inclusions."]
  [PMID:18986984 "Primary cultures of rat hippocampal neurons were prepared from E18 rats."]
- Glycerol-gradient work showing Rpts in both 26S proteasome and a free "APIS"
  19S-like complex was done in human 293T cells; Rpt3 was detected in both
  complexes only when Rpt4 was overexpressed.
  [PMID:18986984 "Rpt3 was also detected in both complexes but only when Rpt4 was overexpressed."]
- Overexpression of Rpt3 only modestly enhanced Htt73 aggregation; the effect was
  mainly attributed to Rpt4 and Rpt6.
  [PMID:18986984 "Overexpression of Rpt3 modestly enhanced aggregation of Htt73, in contrast to Rpt2, Rpt1, and Rpt5, which had no significant effect"]
- The GOA annotations from this paper are inclusion body (IDA) and cytosolic
  proteasome complex (IDA). The inclusion body location is a disease-model
  co-localisation, not a normal-physiology location.

### Sun et al. 2023 (PMID:37228199, abstract only; no PMC copy)

- Free 19S particles are abundant near synapses in rat cortical neurons; they bind
  and deubiquitylate K63-ubiquitin; inhibition of the 19S deubiquitylase activity
  changed excitatory transmission and synaptic availability of AMPA receptors in a
  proteasome-independent manner.
  [PMID:37228199 "We discovered an unexpected abundance of free 19S particles near synapses."]
  [PMID:37228199 "Inhibition of the 19S deubiquitylase activity significantly altered excitatory synaptic transmission and reduced the synaptic availability of AMPA receptors at multiple trafficking points in a proteasome-independent manner."]
- The abstract does not mention synaptic vesicles or Psmc4 individually. The
  deubiquitylase activity is not a property of the base ATPases. GOA rows from
  this paper (synaptic vesicle IDA/HTP, regulation of AMPA receptor activity IDA,
  proteasome accessory complex IPI, proteasome complex and proteasomal protein
  catabolic process HTP) cannot be checked against the full text here.

## Mouse genetics (source of the ISO blastocyst row)

- Psmc4-null mice die before implantation with defective blastocyst development.
  [PMID:10945464 "Both Psmc3- and Psmc4-deficient mice died before implantation, displaying defective blastocyst development."]
  This is a necessity phenotype expected for loss of any essential 26S subunit.

## Mechanism of ATPase-driven gate opening (family-level)

- [PMID:17803938 "Upon ATP binding, these C-terminal residues bind to pockets between the 20S's alpha subunits."]
- [PMID:17803938 "C-terminal residues in the 19S ATPases were also shown to be critical for gating and stability of 26S proteasomes."]
