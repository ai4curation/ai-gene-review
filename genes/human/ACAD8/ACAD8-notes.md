# ACAD8 (Isobutyryl-CoA dehydrogenase, mitochondrial) — review notes

UniProt: Q9UKU7 (ACAD8_HUMAN). HGNC:87. Gene synonyms ARC42, IBD. EC 1.3.8.5.

## Core biology (from UniProt Q9UKU7 and cited primary literature)

ACAD8 is the mitochondrial **isobutyryl-CoA dehydrogenase (IBD/IBDH)**, an FAD-dependent
member of the acyl-CoA dehydrogenase (ACAD) family. It catalyzes the third step of
**valine catabolism**: the FAD-dependent alpha,beta-dehydrogenation of isobutyryl-CoA
(2-methylpropanoyl-CoA) to methacrylyl-CoA ((2E)-2-methylpropenoyl-CoA), with electrons
passed to the electron-transfer flavoprotein (ETF).

- Function/pathway: "Isobutyryl-CoA dehydrogenase which catalyzes the conversion of
  2-methylpropanoyl-CoA to (2E)-2-methylpropenoyl-CoA in the valine catabolic pathway"
  [file:human/ACAD8/ACAD8-uniprot.txt]. PATHWAY: "Amino-acid degradation; L-valine
  degradation." [file:human/ACAD8/ACAD8-uniprot.txt].
- Catalytic activity (Rhea RHEA:44180, EC=1.3.8.5): 2-methylpropanoyl-CoA + oxidized ETF
  + H+ = 2-methylpropenoyl-CoA + reduced ETF [file:human/ACAD8/ACAD8-uniprot.txt].
- Substrate specificity: purified recombinant enzyme kcat/Km 0.8, 0.23, 0.04 uM^-1 s^-1
  with isobutyryl-CoA, (S)-2-methylbutyryl-CoA, and n-propionyl-CoA respectively
  [PMID:12359132 "Purified recombinant enzyme had a k(cat)/K(m) of 0.8, 0.23, and 0.04
  (microM(-1)s(-1)) with isobutyryl-CoA, (S) 2-methylbutyryl-CoA, and n-propionyl-CoA,
  respectively, as substrates. Thus, this enzyme is an isobutyryl-CoA dehydrogenase."].
  So isobutyryl-CoA is the strongly preferred (physiological) substrate; 2-methylbutyryl-CoA
  (isoleucine pathway) and propionyl-CoA are much weaker in-vitro side activities.
- Cofactor: FAD [file:human/ACAD8/ACAD8-uniprot.txt: "Name=FAD; Xref=ChEBI:CHEBI:57692;
  Evidence={ECO:0000269|PubMed:14752098}"]. Crystal structure 1RX0 (1.77 A) solved with
  FAD and substrate analog (PubMed:14752098).
- Subunit: "Homotetramer, formed by a dimer of dimers" [file:human/ACAD8/ACAD8-uniprot.txt].
- Location: "Mitochondrion" [file:human/ACAD8/ACAD8-uniprot.txt]; residues 1-22 are a
  cleaved mitochondrial transit peptide. Reactome and GOA place the mature enzyme in the
  mitochondrial matrix (GO:0005759), consistent with soluble matrix ACADs.

## Identity/discovery

- cDNA cloned as a "novel member of the acyl-CoA dehydrogenase gene family", maps to 11q25,
  415-aa precursor [PMID:10524212 "A gene encoding the precursor for a novel member of the
  human acyl-CoA dehydrogenase (ACD) gene family has been isolated which maps to human
  chromosome 11q25."]. At that time function was unknown; the paper only established family
  membership by sequence similarity ("shares considerable sequence similarity with other
  members of the ACD family").
- ACAD8 identified as an isobutyryl-CoA dehydrogenase and a mitochondrial valine-pathway
  enzyme, distinct from the isoleucine-pathway SBCAD [PMID:11013134 "showed that ACAD-8 is
  an isobutyryl-CoA dehydrogenase and that both wild-type proteins are imported into
  mitochondria and form tetramers"; "indicate that ACAD-8 is a mitochondrial enzyme that
  functions in valine catabolism"].

## Disease — Isobutyryl-CoA dehydrogenase deficiency (IBDD; MIM:611283)

- Autosomal recessive; plasma carnitine deficiency and elevated C4-acylcarnitine; often
  detected on newborn screening; frequently benign/asymptomatic [file:human/ACAD8/ACAD8-uniprot.txt
  DISEASE block]. First patient homozygous Arg302Gln, stable but enzymatically inactive
  [PMID:12359132 "This encodes an Arg302Gln substitution ... The mutant enzyme was stable
  but inactive when expressed in E. coli."]. Additional variants from newborn screening for
  elevated C4-carnitine [PMID:16857760]. This is a disease-association/phenotype, not part
  of the normal molecular function — track as non-core if annotated.

## Transcription "moonlighting" — ARC42 (do NOT propagate as core)

- ACAD8 was co-purified as the 42-kDa component (ARC42) of the ARC/DRIP transcriptional
  co-activator complex [file:human/ACAD8/ACAD8-uniprot.txt SUBUNIT "May be part of the large
  multiprotein complex ARC/DRIP (PubMed:10235267)"; RN[7] PMID:10235267]. This is the origin
  of the UniProt "Activator/Transcription/Transcription regulation" keywords and the
  GO:0006351 DNA-templated transcription keyword annotation. There is no molecular evidence
  that ACAD8/IBDH itself acts as a transcription factor; the identification is a proteomic
  co-purification. The straightforward, well-supported biology is the mitochondrial
  valine-catabolism enzyme. The DNA-templated transcription IEA (from UniProtKB-KW) is an
  over-annotation for the enzyme's function.

## Interactions / proteomics annotations

- GO:0005515 protein binding IPI with UniProtKB:Q8TAG5 (VSTM2A) from BioPlex AP-MS
  [PMID:33961781]. Bare "protein binding"; per policy keep but mark as over-annotated (not
  informative of function; single high-throughput AP-MS hit).
- GO:0005739 mitochondrion HTP from the MitoCoP high-confidence mitochondrial proteome
  [PMID:34800366] — consistent with matrix localization.

## GO term notes

- GO:0003853 "short-chain 2-methyl fatty acyl-CoA dehydrogenase activity" is the GO term
  for EC 1.3.8.5 (the isobutyryl-CoA dehydrogenase reaction: a short-chain 2-methyl acyl-CoA
  -> 2-methyl-2-enoyl-CoA). This is the correct, most specific MF for ACAD8 and has three
  EXP annotations (PMID:11013134, 12359132, 16857760). Use as core MF.
- GO:0003995 "acyl-CoA dehydrogenase activity" is the parent/general MF; TAS from the
  discovery paper (PMID:10524212, when only family membership was known) and an IEA. Correct
  but less specific than GO:0003853 -> MODIFY to GO:0003853.
- GO:0016937 "short-chain fatty acyl-CoA dehydrogenase activity" (straight-chain 2,3-saturated
  substrates) via RHEA:31287 corresponds to the weak in-vitro propionyl-CoA side activity;
  keep as non-core (real but minor/non-physiological).
- GO:0016627 "oxidoreductase activity, acting on the CH-CH group of donors" — correct grandparent
  MF, InterPro IEA; keep as non-core (redundant with specific term).
- GO:0006629 "lipid metabolic process" (TAS PMID:10524212 + InterPro IEA): overly generic and
  slightly misleading — ACAD8 is a BCAA/valine catabolic enzyme, not a straight-chain fatty-acid
  beta-oxidation enzyme. Acyl-CoA metabolism is broadly "lipid", so not strictly wrong, but a
  clear over-annotation relative to L-valine catabolic process. MARK_AS_OVER_ANNOTATED.
- GO:0006574 "L-valine catabolic process" (IEA UniPathway) is the correct core BP.
</content>
