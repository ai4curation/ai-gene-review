# ARV1 review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:40378954 (full text, 2025): ARV1 is a GPI-GnT component that binds PIGQ.
  - PMID:20663892 (abstract): ER resident; knockdown retains ER cholesterol.
  - PMID:39952408 (full text): the ARV1 homology domain binds cholesterol and phospholipids.
  - PMID:32165008 and PMID:34296759: GPI deficiency in patients.
- Reactome R-HSA-5250531 calls ARV1 only "a likely candidate" for ER-to-plasma-membrane cholesterol transport.
- Mouse Arv1 (Q9D0U9) donor rows: IMP for cholesterol biosynthesis and sterol transfer (PMID:20663892, PMID:26479315). These are phenotype-based.

## Decisions
- ACCEPT: ER and ER membrane (IBA, IEA, IDA, TAS); GPI anchor biosynthetic process (IBA).
- MODIFY: sterol transfer activity (IEA, TAS) → cholesterol binding. Binding is shown; transfer is not.
- MARK_AS_OVER_ANNOTATED: cholesterol biosynthetic process (IEA, TAS), an indirect SREBP effect.
- KEEP_AS_NON_CORE: intracellular sterol transport, cholesterol transport, regulation of intracellular cholesterol transport, regulation of cholesterol metabolic process.
- REMOVE: 14 generic protein-binding rows.
- NEW: GPI-GnT complex (IDA, PMID:40378954).
