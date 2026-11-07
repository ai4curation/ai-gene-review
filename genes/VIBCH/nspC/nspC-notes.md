# nspC (VC_1623, Q9KRL4) curation notes

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

Fetched with `just fetch-gene VIBCH Q9KRL4 --alias nspC`.

Deep research: no gene-level provider deep-research file was generated in this
session. The module-level OpenScientist report was used for retrieval only;
claims were checked against cached papers (PMID:19196710 full text; the others
abstract-only).

Key evidence:

- Genetics in V. cholerae: [PMID:19196710 "Deletion of VC1623 resulted in the
  disappearance of norspermidine and the novel accumulation of
  carboxynorspermidine"]; both sym-norspermidine and spermidine are lost.
- Substrate specificity of the orthologue (V. vulnificus CANSDC, assayed in the
  same paper): carboxynorspermidine preferred 20-fold over carboxyspermidine,
  with [PMID:19196710 "no activity with l -arginine, l -lysine, and meso
  -diaminopimelate"]. This contradicts the IBA diaminopimelate decarboxylase
  activity transferred from PTN000159906.
- Orthologue genetics outside Vibrio: C. jejuni [PMID:22025614] and
  B. thetaiotaomicron [PMID:27118128] show the CASDC orthologue makes spermidine.
- Structure of the C. jejuni/V. cholerae CANSDC: group IV PLP decarboxylase fold,
  obligate dimer with active sites at the subunit interface [PMID:20534592].

Decisions:

- GO:0008836 IBA and GO:0009085 IBA: REMOVE. Over-propagation from the
  family-root PAINT node PTN000159906 into the NspC subfamily PTHR43727:SF1; the
  PTHR43727 family review records the node as NEEDS_PRUNING for SF1.
- GO:0003824 IEA: TOO_GENERAL (entailed by the accepted carboxy-lyase activity);
  the KT2440 NspC review uses the same action.
- GO:0016831 (IEA, ISS): ACCEPT; the most specific existing GO MF. A specific
  EC 4.1.1.96 term is proposed, as in the KT2440 review.
- GO:0045312 nor-spermidine biosynthesis (IEA, ISS): ACCEPT as core, because
  norspermidine is the major V. cholerae product. In KT2440 the same term is
  KEEP_AS_NON_CORE because no diaminopropane supply is established there; the
  biology differs between organisms, not the reading of the term.
- GO:0008295 ISS: ACCEPT (core).
- GO:0030170 ISS: ACCEPT (PLP cofactor; Lys51 Schiff base by similarity).
- GO:0042803 ISS: KEEP_AS_NON_CORE (structural dimer, not the function).
- GO:0044010 IDA: KEEP_AS_NON_CORE. The biofilm defect is downstream of
  norspermidine signalling and is rescued by exogenous norspermidine; the enzyme
  performs no biofilm step itself.
