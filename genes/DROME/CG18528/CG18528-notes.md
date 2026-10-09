# CG18528 (Q9VC87) review notes

## Identity
- CG18528 is the Drosophila ortholog of human GTPBP3 / yeast MSS1 / bacterial MnmE (TrmE)
  [file:DROME/CG18528/CG18528-uniprot.txt "tRNA modification GTPase GTPBP3, mitochondrial"].
- Family: [file:DROME/CG18528/CG18528-uniprot.txt "TrmE GTPase family"]; InterPro
  IPR004520 GTPase_MnmE, IPR018948 TrmE N-terminal domain, MnmE helical domain;
  PANTHER PTHR42714:SF2 "TRNA MODIFICATION GTPASE GTPBP3, MITOCHONDRIAL".
- Predicted location: [file:DROME/CG18528/CG18528-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"].

## Literature
- No Drosophila experimental study of CG18528 is in GOA; every annotation is IEA, IBA or
  ISS from human GTPBP3 (Q969Y2), yeast MSS1 and E. coli MnmE.
- In bacteria MnmE (GTPase, binds methylene-THF) and MnmG (FAD) form the MnmEG complex that
  installs the C5 aminomethyl group on wobble U34 (cmnm5U/nm5U); in mammalian mitochondria
  GTPBP3 and MTO1 use taurine to make taum5U34 in mt-tRNAs (Leu UUR, Trp, Gln, Lys, Glu).
  This is background knowledge from the orthologs, not from fly experiments.
- Deep research (falcon) was launched; see deep-research file if present.

## Decisions
- Accept GTPase activity, mitochondrion, mitochondrial tRNA wobble uridine modification,
  and GTPBP3-MTO1 complex (partner CG4610 = MTO1 ortholog).
- tRNA methylation (IBA, from E. coli MnmE): the MnmEG reaction is an aminomethylation
  (methylene transfer from CH2-THF plus amine/taurine) rather than an SAM-type methylation;
  marked as over-annotation.
- Cytoplasm IBA (inherited from a node that includes cytoplasmic bacterial MnmE): kept as
  non-core; the eukaryotic protein is mitochondrial.
- Open question: whether fly mt-tRNAs carry taum5U (taurine) or another C5 substituent;
  the GO MF term on the partner is "tRNA 5-taurinomethyluridine synthase activity".
