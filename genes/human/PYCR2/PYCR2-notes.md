# PYCR2 (human) — gene review notes

UniProt: Q96C36 (P5CR2_HUMAN). HGNC:30262. Gene at 1q42.13. 320 aa, EC 1.5.1.2.
Source of authoritative facts below: `file:human/PYCR2/PYCR2-uniprot.txt` unless a PMID is given.

## Identity and core function

PYCR2 is **pyrroline-5-carboxylate reductase 2**, one of three human P5C reductase isozymes
(PYCR1, PYCR2, PYCRL). It catalyzes the **final step of proline biosynthesis**: NAD(P)H-dependent
reduction of (S)-1-pyrroline-5-carboxylate (P5C) to L-proline.

- UniProt FUNCTION: "Oxidoreductase that catalyzes the last step in proline biosynthesis, which
  corresponds to the reduction of pyrroline-5-carboxylate to L-proline using NAD(P)H"
  [file:human/PYCR2/PYCR2-uniprot.txt]. At physiologic concentrations it "has higher specific
  activity in the presence of NADH" [file:human/PYCR2/PYCR2-uniprot.txt].
- EC 1.5.1.2, RHEA:14105 (NAD+) and RHEA:14109 (NADP+); PhysiologicalDirection is right-to-left
  (i.e. P5C -> proline) [file:human/PYCR2/PYCR2-uniprot.txt].
- PATHWAY: "Amino-acid biosynthesis; L-proline biosynthesis; L-proline from L-glutamate
  5-semialdehyde: step 1/1" [file:human/PYCR2/PYCR2-uniprot.txt].
- SIMILARITY: "Belongs to the pyrroline-5-carboxylate reductase family"
  [file:human/PYCR2/PYCR2-uniprot.txt].
- Structure solved (PDB 6LHM); homodecamer of 5 homodimers inferred; NADP(H) and L-proline binding
  residues annotated by similarity to PYCR1 (P32322) [file:human/PYCR2/PYCR2-uniprot.txt].

## Enzymology / cofactor use

- Historic erythrocyte enzyme (the "PYCR" purified by Merrill/Yeh/Phang) has HIGHER affinity for
  NADPH than NADH and is competitively inhibited by NADP+; not inhibited by proline in those studies
  [PMID:2722838 "The affinity for NADPH is 15-fold higher than that for NADH"], [PMID:2722838
  "Erythrocyte pyrroline-5-carboxylate reductase is competitively inhibited by NADP+"].
  These authors proposed that in erythrocytes the enzyme's physiologic role may be to **generate
  NADP+** rather than proline [PMID:6894153 "the function of the enzyme in human erythrocytes may
  be to generate oxidizing potential in the form of NADP+"].
- The isozyme-resolved study (De Ingeniis 2012) purified recombinant PYCR2 and measured kinetics.
  UniProt records, from this paper, that at physiologic conditions PYCR2 has higher specific
  activity with NADH; kcat 149 s-1 (NADH) vs 85 s-1 (NADPH) for P5C reduction
  [file:human/PYCR2/PYCR2-uniprot.txt]. This paper also reported proline inhibition of PYCR2
  (UniProt ACTIVITY REGULATION notes the discrepancy between older and newer studies).

## Subcellular location

- **Mitochondrion** is the location supported by isozyme-resolved cell-fractionation and disease
  work. De Ingeniis 2012: "PYCR1 and PYCR2 are strictly associated with mitochondria, but PYCRL
  is found only in the cytoplasm" [PMID:23024808]; "PYCR1 and PYCR2, which are localized in the
  mitochondria, are primarily involved in conversion of glutamate to proline" [PMID:23024808].
- Nakayama 2015 confirmed mitochondrial localization of WT and mutant PYCR2 in HEK293FT
  [PMID:25865492 "both variant proteins retained normal mitochondrial localization"].
- UniProt SUBCELLULAR LOCATION lists both Cytoplasm (from the 1989 erythrocyte prep, PMID:2722838)
  and Mitochondrion (PMID:23024808, PMID:25865492) [file:human/PYCR2/PYCR2-uniprot.txt]. The
  cytoplasm/cytosol annotations largely derive from the erythrocyte enzyme (erythrocytes lack
  mitochondria) and from Reactome; the isozyme-resolved and disease evidence places PYCR2 in
  mitochondria. I therefore treat mitochondrion as the core location and keep the cytosol/cytoplasm
  annotations as non-core/over-annotated rather than removing experimental ones.

## Biological process: proline biosynthesis (glutamate route)

- De Ingeniis 2012 dissected the three isozymes: "silencing of PYCR2 increased the isotopic
  enrichment ratio (pro/orn), confirming that this enzyme is predominantly involved in the
  glutamate pathway" [PMID:23024808]; "PYCR1 and PYCR2 are located in the mitochondria, and both
  have access to the pool of P5C generated from glutamate by P5CS" [PMID:23024808]. So PYCR2 acts
  chiefly in the glutamate -> P5C -> proline (mitochondrial) route. This is the direct experimental
  basis for GO:0055129 IDA.

## Oxidative stress / redox

- Nakayama 2015: a CRISPR PYCR2-KO HEK293FT line "showed that PYCR2 loss of function led to
  decreased mitochondrial membrane potential and increased susceptibility to apoptosis under
  oxidative stress" [PMID:25865492]. This is the IMP basis for GO:0034599 (cellular response to
  oxidative stress). It is a downstream/secondary role tied to redox and mitochondrial function,
  consistent with the redox interpretation of the NADP+/NADPH couple; kept as non-core.
- UniProt FUNCTION: "Involved in cellular response to oxidative stress (PubMed:25865492)"
  [file:human/PYCR2/PYCR2-uniprot.txt].

## Protein interaction (ORAOV1/LTO1)

- PYCR2 co-purified with the ORAOV1/LTO1 protein (UniProtKB:Q8WV07) in an ESCC study; PYCR
  knockdown reversed the ORAOV1-driven stress resistance [PMID:24930674 "ORAOV1 bound to
  pyrroline-5-carboxylate reductase (PYCR), which is associated with proline metabolism and
  reactive oxygen species (ROS) production"]. UniProt: "Interacts with LTO1 (PubMed:24930674)"
  [file:human/PYCR2/PYCR2-uniprot.txt]. Note the paper writes "PYCR" generically and its focus is
  ORAOV1; the interaction is a single IPI ("protein binding"). Kept as non-core; the specific
  binding partner is captured but "protein binding" is uninformative as a core MF.

## Disease

- **Hypomyelinating leukodystrophy 10 (HLD10)** [MIM:616420], autosomal recessive: postnatal
  microcephaly, severely delayed psychomotor development, hypomyelination, reduced cerebral
  white-matter volume [file:human/PYCR2/PYCR2-uniprot.txt]. Caused by biallelic PYCR2 variants;
  HLD10 variants R119C and R251C decrease protein amount/stability without abolishing mitochondrial
  localization [PMID:25865492]. Zebrafish ortholog knockdown recapitulates microcephaly, rescued by
  WT (not mutant) human PYCR2 mRNA [PMID:25865492]. Distinct from PYCR1 cutis laxa (no lax skin),
  indicating a "unique and indispensable role for PYCR2 in the human CNS during development"
  [PMID:25865492].

## Annotation-review decisions (summary)

Core molecular function: **GO:0004735 pyrroline-5-carboxylate reductase activity** (verified
molecular_function branch; go.db label matches).
Core biological process: **GO:0055129 L-proline biosynthetic process** (verified BP branch).
Core location: **GO:0005739 mitochondrion** (verified CC branch).

- GO:0004735 P5C reductase activity — ACCEPT the IDA (PMID:23024808) and both EXP (PMID:2722838,
  PMID:6894153) and IBA as core MF. Redundant IEA kept as non-core.
- GO:0055129 L-proline biosynthetic process — ACCEPT IDA (PMID:23024808) as core BP; IBA/IEA
  redundant, non-core.
- GO:0005739 mitochondrion — ACCEPT the two IDA (PMID:23024808, PMID:25865492) as core location;
  HTP (PMID:34800366) and IEA kept as non-core corroboration.
- GO:0034599 cellular response to oxidative stress — KEEP_AS_NON_CORE (IMP PMID:25865492); the IEA
  ARBA duplicate also non-core. Real but secondary/downstream.
- Cytoplasm/cytosol (GO:0005737 EXP+IEA, GO:0005829 TAS Reactome) — MARK_AS_OVER_ANNOTATED /
  non-core. Derives from the mitochondria-free erythrocyte prep and Reactome; isozyme-resolved and
  disease data localize PYCR2 to mitochondria. Not removing experimental EXP annotation per policy.
- GO:0005515 protein binding (IPI PMID:24930674, LTO1/ORAOV1) — MARK_AS_OVER_ANNOTATED (uninformative
  MF; do not REMOVE an IPI). Interaction is real but not a core function.
