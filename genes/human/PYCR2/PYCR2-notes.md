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

## 2026-10-18 — ORGANELLES pilot: mitochondrial sub-compartment (outcome: unresolved, stay at root)

Question: is PYCR2 in the mitochondrial matrix (GO:0005759), at the inner membrane, or only
supportable at the organelle level (GO:0005739)? Applied `projects/ORGANELLES.md` Policy.

Evidence examined:
- De Ingeniis 2012 used a two-way fractionation only: "This was accomplished with Western blotting
  using standard approaches to fractionate Lu1205 cells into mitochondrial and cytosolic fractions"
  [PMID:23024808]. Mitochondrion vs cytosol; no submitochondrial assay. Its argument from cofactor
  use ("PYCR1 and PYCR2 have higher specific activity in the presence of NADH, consistent with
  their localization in the mitochondria" [PMID:23024808]) is a functional hint toward the inside
  of the organelle, not a localization result.
- Nakayama 2015 (abstract only cached): "both variant proteins retained normal mitochondrial
  localization" [PMID:25865492]. Whole-organelle.
- MitoCoP (HTP): "we combined subtractive proteomics, spatial proteomics, mitochondria-specific
  importomics, and literature/database curation by stringent criteria" [PMID:34800366]. It also
  mapped "membrane association and integration of MitoCoP proteins by sonication and treatment at
  alkaline pH" [PMID:34800366], but the per-protein table (Table S3) is not in the cached text, so
  it gives no usable PYCR2 sidedness.
- No transit peptide: UniProt has the N-terminus directly sequenced, "PROTEIN SEQUENCE OF 2-17,
  CLEAVAGE OF INITIATOR METHIONINE, ACETYLATION AT" Ser-2 [file:human/PYCR2/PYCR2-uniprot.txt].
  So the mature protein retains its N-terminus; no MPP-cleaved presequence. This does not exclude
  matrix import via internal signals, but removes the usual sequence line for matrix.
- UniProt also lists "Cytoplasm {ECO:0000269|PubMed:2722838}" [file:human/PYCR2/PYCR2-uniprot.txt]
  (erythrocyte enzyme), consistent with a dual or loosely associated pool.
- PubMed search (2026-10-18; queries on PYCR1/PYCR2 with matrix / inner membrane / outer membrane /
  submitochondrial / APEX / proteinase K / digitonin) found no PYCR1 or PYCR2 submitochondrial
  assay. Liu et al. 2024 (PMID:38719025, Virus Res, not cached; DOI 10.1016/j.virusres.2024.199387,
  read via PubMed/PMC) calls PYCR2 "the mitochondrial matrix protein PYCR2", but this is a cited
  background statement, and their own assay is a mitochondria/cytosol kit fractionation. Kindlin-2
  papers (PMID:30783087, PMID:33761308) report kindlin-2 translocating to mitochondria to bind
  PYCR1; no sidedness for PYCR2.
- PYCR1 comparator: its GO:0005759 matrix annotation is Reactome TAS (R-HSA-70664), whose summary
  cites only fractionation and co-localization ("Subcellular fractionation (De Ingeniis et al.
  2012) and co-localization studies (Reversade et al. 2009) indicate that PYCR1 is mitochondrial"
  [Reactome:R-HSA-70664]). So the paralog's matrix term is not independent evidence either.

Decision (policy rule 4): only one line (function: NADH use, access to P5CS-derived P5C) favours
an inside location, and it does not distinguish matrix from the matrix face of the inner
membrane; the sequence line (no cleaved MTS) and the reported cytoplasmic pool do not agree with a
simple matrix assignment. Lines disagree / only one positive line, so stay at the root. No NEW
sub-compartment row; core_functions location stays GO:0005739. Filled reasons on the four
mitochondrion rows (IEA GO_REF:0000120, HTP PMID:34800366, IDA PMID:23024808, IDA PMID:25865492),
all remaining ACCEPT. A protease-protection / alkaline-carbonate / APEX-matrix experiment would
settle this.
