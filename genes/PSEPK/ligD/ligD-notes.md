# ligD curation notes

## 2026-09-01

Applied the annotation-reviewer workflow to all four GOA rows and evaluated
three missing activities/process annotations. No annotation remains PENDING or
UNDECIDED.

- Q88HU3 is an unreviewed KT2440 protein with the complete LigD domain
  architecture: IPR014144 phosphoesterase, IPR014145 polymerase, and IPR014146
  ligase [file:PSEPK/ligD/ligD-uniprot.txt "InterPro; IPR014144;
  LigD_PE_domain."] [file:PSEPK/ligD/ligD-uniprot.txt "InterPro; IPR014145;
  LigD_pol_dom."] [file:PSEPK/ligD/ligD-uniprot.txt "InterPro; IPR014146;
  LigD_ligase_dom."].
- PTHR42705 PAINT places DNA polymerase activity, ATP-dependent DNA ligase
  activity, and NHEJ at PTN001627042
  [file:interpro/panther/PTHR42705/PTHR42705-paint.tsv
  "PTN001627042	GO:0003887"].
- Direct work on Pseudomonas aeruginosa LigD supports polymerase-mediated end
  remodeling [PMID:20018881 "Pseudomonas Ku stimulates POL-catalyzed
  ribonucleotide addition to a plasmid DSB end"].
- The phosphoesterase domain is not modeled as generic exonuclease activity.
  Pseudomonas LigD removes a terminal ribonucleotide and then hydrolyzes the
  resulting 3-prime phosphate on a DNA repair intermediate
  [PMID:15897197 "The 3'-ribonuclease and 3'-phosphatase activities are"]. A
  general RNA exonuclease term is not asserted because the demonstrated
  substrate is ribonucleotide-terminated DNA, and the isolated nuclease domain
  did not behave as an independent processive 3-prime-to-5-prime exonuclease
  [PMID:16023671 "The nuclease domain did not function independently as a
  3'-5' exonuclease."].
- The POL domain prefers ribonucleotides in biochemical assays, but
  GO:0003887 is retained as the PAINT- and UniProt-grounded polymerase term;
  no more specific MF term is asserted without a verified ontology match
  [PMID:16023671 "DNA-dependent RNA primase activity, catalysing the synthesis
  of unprimed oligoribonucleotides"].
- Direct P. putida genetics links LigD and both its PE and POL domains to
  stationary-phase mutation spectra [PMID:25942369 "both phosphoesterase (PE)
  and polymerase (POL) domains"]. The cached paper is abstract-only, so the
  catalytic assignments remain grounded in domain/family biochemistry.
- Target-organism Cas9 work perturbed NHEJ-associated KT2440 enzymes during DSB
  repair [PMID:36475478 "removal or overproduction of NHEJ-associated P. putida
  KT2440 enzymes on"], directly supporting the pathway assignment.

GO:0006310 is modified laterally to GO:0006303 because bacterial NHEJ is a DNA
repair route, not a child of generic DNA recombination. The three distinct LigD
molecular functions are represented separately in the core-functions list.
