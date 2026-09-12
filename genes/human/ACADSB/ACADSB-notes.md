# ACADSB (P45954) — curation notes

Human short/branched-chain specific acyl-CoA dehydrogenase, mitochondrial (SBCAD;
2-methylbutyryl-CoA dehydrogenase; ACADSB). HGNC:91, gene ID 36, chromosome 10.
UniProt reviewed entry P45954; 432 aa precursor with an N-terminal mitochondrial
transit peptide (residues 1..33) cleaved to give the mature matrix enzyme.

## Identity and family

- Member of the acyl-CoA dehydrogenase (ACAD) family: "Belongs to the acyl-CoA
  dehydrogenase family." [file:human/ACADSB/ACADSB-uniprot.txt "Belongs to the acyl-CoA dehydrogenase family."].
- FAD-dependent flavoprotein oxidoreductase; EC 1.3.8.1 (short-chain acyl-CoA:ETF
  oxidoreductase) and EC 1.3.8.5 (2-methylbutanoyl-CoA:ETF oxidoreductase). Recombinant
  human SBCAD was originally isolated as "a novel member (gene symbol ACADSB) of the ACD
  gene family" with "significant sequence similarity to other members of the acyl-CoA
  dehydrogenase family, with the greatest homology (38%) to the short chain acyl-CoA
  dehydrogenase" [PMID:7698750 "with the greatest homology (38%) to the short"].

## Molecular function (core)

- Catalyzes the FAD-dependent, ETF-coupled alpha,beta-dehydrogenation of acyl-CoA
  thioesters. UniProt: "catalyzes the proR-proR stereospecific alpha,beta-dehydrogenation
  of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their
  physiologic electron acceptor" [file:human/ACADSB/ACADSB-uniprot.txt "physiologic electron acceptor"].
- Substrate specificity: short and branched chain acyl-CoAs. Recombinant human protein has
  "activity toward the short branched chain acyl-CoA derivatives ((S)-2-methylbutyryl-CoA,
  isobutyryl-CoA, and 2-methylhexanoyl-CoA), as well as toward the short straight chain
  acyl-CoAs (butyryl-CoA and hexanoyl-CoA)" [PMID:7698750 "((S)-2-methylbutyryl-CoA, isobutyryl-CoA, and 2-methylhexanoyl-CoA)"].
- The physiologically important reaction is dehydrogenation of (S)-2-methylbutyryl-CoA to
  tiglyl-CoA in isoleucine catabolism. Reactome: "Mitochondrial 2-methyl branched-chain
  acyl-CoA dehydrogenase (ACADSB) catalyzes the reaction of alpha-methylbutyryl-CoA and FAD
  to form 'tiglyl-CoA and FADH2" [file:reactome/R-HSA-70800.md].
- FAD cofactor: UniProt COFACTOR "Name=FAD" with multiple FAD-binding site features
  (BINDING 174..183, 207..209, 319, 330, 387..391, 416..418) established by the 2JIF crystal
  structure. FAD binding is a core molecular function (GO:0050660), consistent with the
  flavoprotein family assignment.
- Homotetramer: "Homotetramer." [file:human/ACADSB/ACADSB-uniprot.txt "Homotetramer."], confirmed
  by the crystal structure (2JIF; SGC) and by PMID:11013134 ("both wild-type proteins are
  imported into mitochondria and form tetramers"). This is the basis of the GO:0042802
  identical protein binding IDA annotation (self-association into the homotetramer).

## Substrate breadth / promiscuity

- SBCAD is catalytically promiscuous within the short/branched class: 2-methylbutanoyl-CoA
  (the physiological substrate), 2-methylpropanoyl-CoA (isobutyryl-CoA), 2-methylhexanoyl-CoA,
  butanoyl-CoA, hexanoyl-CoA, and the xenobiotic valproyl-CoA. Kinetics (UniProt): KM 2.7 uM
  for (2S)-2-methylbutanoyl-CoA vs 36 uM for hexanoyl-CoA vs 130 uM for 2-methylpropanoyl-CoA,
  i.e. the branched-chain isoleucine substrate is strongly preferred.
- Hexanoyl-CoA (C6) is a straight-chain substrate at the boundary between short and medium
  chain; GOA carries a RHEA-derived GO:0070991 "medium-chain fatty acyl-CoA dehydrogenase
  activity" IEA from the hexanoyl-CoA reaction (RHEA:43464). This is a real in vitro activity
  but not the biological role of the enzyme (over-annotation of substrate breadth).
- Valproyl-CoA: SBCAD is "the most probable candidate for the first dehydrogenation step of
  VPA beta-oxidation" and is competitively inhibited by valproyl-CoA [PMID:21430231 "the first
  dehydrogenation step of VPA"; "did inhibit SBCAD activity by a purely competitive mechanism"].
  Xenobiotic/drug metabolism, not a distinct GO function beyond the dehydrogenase activity.

## Biological process (core)

- L-isoleucine catabolism. UniProt PATHWAY "Amino-acid degradation; L-isoleucine degradation"
  and FUNCTION: "Plays an important role in the metabolism of L-isoleucine by catalyzing the
  dehydrogenation of 2-methylbutyryl-CoA, one of the steps of the L-isoleucine catabolic
  pathway" [file:human/ACADSB/ACADSB-uniprot.txt "one of the steps of the L-isoleucine catabolic"].
- Genetic evidence for the isoleucine-specific role: a patient with isolated
  2-methylbutyrylglycinuria had a homozygous SBCAD exon-10-skipping mutation, and study showed
  "it results in an isolated defect in isoleucine catabolism" [PMID:11013134 "an isolated defect
  in isoleucine catabolism"]. This paper also distinguishes SBCAD (isoleucine) from ACAD8/IBD
  (valine): "indicate that ACAD-8 is a mitochondrial enzyme that functions in valine metabolism".
- Fatty acid metabolic process: SBCAD also acts on short straight-chain acyl-CoAs (butyryl-CoA,
  hexanoyl-CoA); UniProt also lists PATHWAY "Lipid metabolism; mitochondrial fatty acid
  beta-oxidation" [file:human/ACADSB/ACADSB-uniprot.txt "mitochondrial fatty acid beta-oxidation"].
  This is a genuine but secondary/non-core contribution relative to isoleucine catabolism.

## Cellular location (core)

- Mitochondrial matrix. UniProt SUBCELLULAR LOCATION "Mitochondrion matrix"
  [file:human/ACADSB/ACADSB-uniprot.txt "Mitochondrion matrix"]. Consistent with the cleaved
  N-terminal transit peptide (1..33) and with IDA mitochondrial localization (PMID:11013134),
  HPA IDA (GO_REF:0000052), and mitochondrial proteome MS (PMID:34800366). Reactome TAS
  annotations place it in the mitochondrial matrix (GO:0005759).

## Disease

- Short/branched-chain acyl-CoA dehydrogenase deficiency (SBCADD; 2-methylbutyryl-CoA
  dehydrogenase deficiency), MIM:610006, autosomal recessive. UniProt DISEASE: "a defect in
  catabolism of L-isoleucine which is characterized by an increase of 2-methylbutyrylglycine
  and 2-methylbutyrylcarnitine in blood and urine" [file:human/ACADSB/ACADSB-uniprot.txt
  "2-methylbutyrylglycine and 2-methylbutyrylcarnitine in"]. First case: PMID:10832746
  (L222F variant; "absence of enzyme activity for the 2-MBCDase protein expressed in
  Escherichia coli"). Molecular basis / first gene mutation: PMID:11013134. Detected on
  newborn screening as elevated C5 (2-methylbutyryl) acylcarnitine; frequently benign and
  notably common in Hmong populations (background, not in cached publications).

## Notes on the annotation set (GOA)

- Multiple redundant MF annotations to GO:0003853 (short-chain 2-methyl fatty acyl-CoA
  dehydrogenase activity) from EXP/IDA (PMID:7698750, 10832746, 11013134, 21430231) — this is
  the correctly specific term for the isoleucine step and is the primary core MF. IEA to the
  same term (GO_REF:0000120, Rhea/EC 1.3.8.5) corroborates.
- GO:0016937 (short-chain fatty acyl-CoA dehydrogenase activity) IDA (PMID:7698750) captures
  the straight-chain butyryl/hexanoyl activity — a genuine secondary MF.
- GO:0003995 (acyl-CoA dehydrogenase activity) IBA/IEA is the correct general parent; keep as
  non-core because more specific children are annotated.
- GO:0016627 (oxidoreductase, CH-CH group of donors) IEA is a very general grandparent —
  over-annotation.
- GO:0070991 (medium-chain fatty acyl-CoA dehydrogenase activity) IEA from the hexanoyl-CoA
  Rhea reaction — over-annotation of substrate breadth (C6 boundary), not the biological role.
- GO:0006631 (fatty acid metabolic process) IDA (PMID:7698750) / IEA and GO:0046395
  (carboxylic acid catabolic process) IEA are correct but non-core relative to isoleucine
  catabolism.
- Reactome TAS to GO:0005759 via R-HSA-9838081 / R-HSA-9838093 are "LONP1 degrades/binds
  mitochondrial matrix proteins" — these place ACADSB in the matrix only as a LONP1 substrate;
  the location call is correct but the process context is protein turnover, not SBCAD function.
</content>
</invoke>
