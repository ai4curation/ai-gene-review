# CSAD (Cysteine sulfinic acid decarboxylase) — review notes

UniProt: Q9Y600 (CSAD_HUMAN). Gene HGNC:18966 (synonym CSD). Chromosome 12.
493 aa; MW ~55 kDa. PE 1 (evidence at protein level). PDB 2JIS (1.6 Å).

## Identity and family
- Name: Cysteine sulfinic acid decarboxylase; AltNames: Cysteine-sulfinate
  decarboxylase, Sulfinoalanine decarboxylase; also annotated Aspartate
  1-decarboxylase (secondary activity) [file:human/CSAD/CSAD-uniprot.txt
  "RecName: Full=Cysteine sulfinic acid decarboxylase"].
- Belongs to the group II decarboxylase family (glutamate-decarboxylase-like /
  DOPA decarboxylase-like fold; Type I PLP-dependent aspartate
  aminotransferase-like major domain) [file:human/CSAD/CSAD-uniprot.txt
  "Belongs to the group II decarboxylase family."]. InterPro IPR002129
  (PyrdxlP-dep_de-COase); Pfam PF00282 (Pyridoxal_deC); PANTHER
  PTHR45677:SF8 CYSTEINE SULFINIC ACID DECARBOXYLASE.

## Molecular function / catalysis
- PLP (pyridoxal 5'-phosphate)-dependent decarboxylase. Cofactor:
  pyridoxal 5'-phosphate, established from the crystal structure in complex
  with PLP (Ref.6, SGC) [file:human/CSAD/CSAD-uniprot.txt
  "Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;"]. PLP is bound via a
  Schiff base to Lys305 (MOD_RES 305 "N6-(pyridoxal phosphate)lysine").
- Catalyzes the decarboxylation of L-aspartate, 3-sulfino-L-alanine (cysteine
  sulfinic acid / L-cysteinesulfinate) and L-cysteate to beta-alanine,
  hypotaurine and taurine respectively; the preferred substrate is
  3-sulfino-L-alanine; does not decarboxylate glutamate
  [file:human/CSAD/CSAD-uniprot.txt "sulfino-L-alanine. Does not exhibit any
  decarboxylation activity toward"].
- Principal committed reaction (EC 4.1.1.29): 3-sulfino-L-alanine + H+ ->
  hypotaurine + CO2 [file:human/CSAD/CSAD-uniprot.txt
  "Reaction=3-sulfino-L-alanine + H(+) = hypotaurine + CO2;"]. Can also convert
  L-cysteate -> taurine + CO2 [file:human/CSAD/CSAD-uniprot.txt
  "Reaction=L-cysteate + H(+) = taurine + CO2;"].
- Secondary/promiscuous aspartate 1-decarboxylase activity (EC 4.1.1.11):
  L-aspartate + H+ -> beta-alanine + CO2, inferred by similarity to mouse
  Csad (Q9DBE0). This is a minor side activity, not the physiological core role.

## Pathway / biological process
- Committed step of taurine/hypotaurine biosynthesis: "Organosulfur
  biosynthesis; taurine biosynthesis; hypotaurine from L-cysteine: step 2/2"
  [file:human/CSAD/CSAD-uniprot.txt "PATHWAY: Organosulfur biosynthesis; taurine
  biosynthesis; hypotaurine"]. Hypotaurine is subsequently oxidized to taurine.
- CSAD is the principal route of endogenous taurine synthesis in mammals
  (highest in liver). GO BP terms in GOA: taurine biosynthetic process
  (GO:0042412), L-cysteine catabolic process (GO:0019448). NB the more specific
  GO:0019449 (L-cysteine catabolic process to hypotaurine) and GO:0019452
  (taurine biosynthetic process from L-cysteine) are now OBSOLETE in GO — these
  appear only in the UniProt DR block, not in the GOA TSV.

## Localization
- Cytosolic/cytoplasmic (ISS from rat Q64611; IBA is_active_in cytoplasm)
  [file:human/CSAD/CSAD-uniprot.txt cytoplasm ISS:UniProtKB DR line]. No
  membrane/signal features.

## Subunit / structure
- Homodimer [file:human/CSAD/CSAD-uniprot.txt "SUBUNIT: Homodimer."]. Crystal
  structure PDB 2JIS at 1.6 Å solved by the Structural Genomics Consortium in
  complex with PLP (Ref.6).

## Tissue expression
- Expressed in liver and brain; expressed in both astrocytes and neurons, with
  lower levels in astrocytes [file:human/CSAD/CSAD-uniprot.txt "Expressed in
  liver and brain. Also expressed in"], per PMID:26327310 (Winge et al. 2015,
  Neurochem Int; abstract-only, NOT cached locally). This paper also compares
  CSAD and its paralog GADL1, showing they have distinct biochemical properties
  and brain-expression patterns.

## Isoforms
- 3 isoforms (alternative splicing): isoform 1 (Long, canonical Q9Y600-1),
  isoform 2 (Short, Q9Y600-2; missing residues 43-189), isoform 3 (Q9Y600-3;
  N-terminal extension VSP_039002). None assigned an isoform-specific function
  in UniProt.

## Cited references (cache status)
- PMID:15489334 (MGC cDNA project) — CACHED, abstract only; sequence-report
  only, no functional evidence for CSAD.
- PMID:14702039 (Ota et al., full-length cDNAs) — sequence report, not cached;
  not functional evidence.
- PMID:26327310 (Winge et al. 2015) — tissue specificity + CSAD/GADL1
  comparison; NOT cached (abstract-only per UniProt). Used only via UniProt
  ECO:0000269 attribution; not quoted directly.
- Ref.6 (SGC, PDB 2JIS) — crystal structure with PLP; source of cofactor and
  homodimer evidence.

## Annotation review summary (actions)
- Core MF: sulfinoalanine decarboxylase activity (GO:0004782); cofactor
  pyridoxal phosphate binding (GO:0030170).
- Core BP: taurine biosynthetic process (GO:0042412).
- Core CC: cytoplasm (GO:0005737).
- Non-core: aspartate 1-decarboxylase activity (GO:0004068, secondary
  promiscuous activity); L-cysteine catabolic process (GO:0019448).
- Over-annotation: carbon-carbon lyase activity (GO:0016830) — over-general
  parent of the specific decarboxylase MF.
