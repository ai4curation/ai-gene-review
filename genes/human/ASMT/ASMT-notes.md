# ASMT (Acetylserotonin O-methyltransferase / HIOMT) — review notes

UniProt: P46597 (ASMT_HUMAN). HGNC:750. Gene on the pseudoautosomal region 1
(PAR1) of the X and Y chromosomes. EC 2.1.1.4.

## Core biology

ASMT (historically hydroxyindole O-methyltransferase, HIOMT) is a cytosolic,
S-adenosyl-L-methionine (SAM)-dependent O-methyltransferase that catalyzes the
**last step of melatonin biosynthesis**: O-methylation of N-acetylserotonin to
melatonin.

- Catalytic activity (authoritative, UniProt): "Reaction=N-acetylserotonin +
  S-adenosyl-L-methionine = melatonin + S-adenosyl-L-homocysteine + H(+)" with
  "EC=2.1.1.4" and "Evidence={ECO:0000269|PubMed:22775292}"
  [file:human/ASMT/ASMT-uniprot.txt].
- Function (isoform 1): "Catalyzes the transfer of a methyl group onto N-
  acetylserotonin, producing melatonin (N-acetyl-5-methoxytryptamine)"
  [file:human/ASMT/ASMT-uniprot.txt, ECO:0000269|PubMed:22775292].
- Pathway: "Aromatic compound metabolism; melatonin biosynthesis; melatonin from
  serotonin: step 1/2" [file:human/ASMT/ASMT-uniprot.txt]. In the overall
  pathway Trp -> 5-HTP -> serotonin -> N-acetylserotonin -> melatonin, ASMT is
  the last and rate-influencing enzyme.
- Confirmed by primary literature: HIOMT "catalyzes the last step in the
  synthesis of the pineal hormone melatonin" [PMID:8397829 abstract]; and the
  X-ray structure paper describes "human N-acetyl serotonin methyltransferase
  (ASMT), the last enzyme of the melatonin biosynthesis pathway"
  [PMID:22775292 abstract].

## Structure / mechanism

- SAM-dependent, class I-like methyltransferase. UniProt: "Belongs to the class
  I-like SAM-binding methyltransferase superfamily. Cation-independent O-
  methyltransferase family" [file:human/ASMT/ASMT-uniprot.txt].
- Crystal structure (PDB 4A6D, 4A6E) solved with SAM and N-acetylserotonin
  bound. Botros et al.: "we present the X-ray crystal structure of human N-acetyl
  serotonin methyltransferase (ASMT)" and "The polypeptide chain of ASMT consists
  of a C-terminal domain, which is typical of other SAM-dependent
  O-methyltransferases, and an N-terminal domain, which intertwines several
  helices with another monomer to form the physiologically active dimer"
  [PMID:22775292 abstract].
- SUBUNIT (UniProt): "Homodimer" [file:human/ASMT/ASMT-uniprot.txt,
  ECO:0000269|PubMed:22775292]. INTERACTION table records the P46597–P46597
  self-interaction (NbExp=3), the basis for the two IntAct/UniProt homodimer
  annotations (GO:0042802 identical protein binding; GO:0042803 protein
  homodimerization activity). The N-terminal domain mediates the dimer
  interface. These correspond to a real, structurally validated homodimer, but
  the "identical/homodimerization" MF terms are supporting/structural, not the
  gene's core catalytic function.
- Active site: ACT_SITE 255 "Proton donor/acceptor". SAM-binding residues 147,
  164, 210, 235-237, 252; substrate-binding residues 256, 302, 306
  [file:human/ASMT/ASMT-uniprot.txt].

## Isoforms

Three isoforms. Only isoform 1 is catalytically active. UniProt: "[Isoform 2]:
Does not show Acetylserotonin O-methyltransferase activity" and "[Isoform 3]:
Does not show Acetylserotonin O-methyltransferase activity"
[file:human/ASMT/ASMT-uniprot.txt, ECO:0000269|PubMed:22775292]. Isoform 3
includes part of a LINE-1 element — this is the historically-cloned pineal cDNA
[PMID:8397829]. Note: the experimental GO annotations (IDA from PMID:22775292)
were made without an isoform tag in GOA; the enzyme activity is a property of
isoform 1.

## Localization / expression

- Cytosolic (Reactome places the reaction in cytosol; GO:0005829 TAS Reactome).
  No transit peptide or membrane anchor in UniProt; class I O-MTases are soluble
  cytosolic enzymes.
- TISSUE SPECIFICITY (UniProt): "Expressed in the pineal gland (at protein
  level). In the retina, very low expression is found at the mRNA level
  (PubMed:7989373), and not at the protein level (PubMed:8574683)"
  [file:human/ASMT/ASMT-uniprot.txt]. Pineal gland is the principal site.
- HPA: tissue-enriched in choroid.

## Disease associations

ASMT variants have been repeatedly screened in neuropsychiatric / neurodevelopmental
disorders (autism spectrum disorder, ADHD, bipolar disorder, intellectual
disability). Many nonsynonymous variants reduce or abolish enzyme activity.
Botros et al.: "the majority of these mutations reduced or abolished ASMT activity
including one relatively frequent polymorphism in the Han Chinese population (N17K,
rs17149149)" and this "provides a structural basis for understanding melatonin
deficiency in humans" [PMID:22775292 abstract]. (UniProt VARIANT records: N17K,
V171M, D210G, R291Q, L298F etc. nearly abolish activity.) These are disease-context
findings, not a distinct core molecular function.

## Annotation review decisions (summary)

Core MF: acetylserotonin O-methyltransferase activity (GO:0017096) — strong,
multi-source, including experimental IDA (PMID:22775292).
Core BP: melatonin biosynthetic process (GO:0030187) — IDA + IBA + IEA.
Core CC: cytosol (GO:0005829) — TAS Reactome.

Over-annotations / non-core:
- GO:0008172 S-methyltransferase activity (TAS Reactome): WRONG BRANCH. ASMT is
  an O-methyltransferase (methyl transferred to an oxygen), not an
  S-methyltransferase (methyl to sulfur). This is a Reactome->GO mapping artifact.
  MARK_AS_OVER_ANNOTATED (non-experimental; not the enzyme's chemistry).
- GO:0008168 methyltransferase activity (IEA) and GO:0008171 O-methyltransferase
  activity (IEA/TAS): correct but general parents of the specific MF; keep as
  non-core / accept-but-general.
- GO:0046983 protein dimerization activity (IEA InterPro): generic; the specific,
  evidence-backed term is GO:0042803 homodimerization. MARK_AS_OVER_ANNOTATED /
  keep non-core.
- GO:0042802 identical protein binding (IPI) and GO:0042803 protein
  homodimerization activity (IPI): real homodimer, but structural, not core
  catalytic. KEEP_AS_NON_CORE.
- GO:0046219 indolalkylamine biosynthetic process (TAS Reactome): correct but a
  broad parent of melatonin biosynthesis; KEEP_AS_NON_CORE.
- GO:0032259 methylation (IBA): high-level BP parent; KEEP_AS_NON_CORE.
- GO:0006412 translation (TAS PMID:8397829): almost certainly a legacy PINC/ProtInc
  mis-annotation — the 1993 paper is about cloning HIOMT cDNA (which discusses a
  LINE-1 fragment and mRNA), NOT about ASMT participating in protein translation.
  The abstract does not support any role in translation. Non-experimental TAS,
  clearly wrong -> MARK_AS_OVER_ANNOTATED (policy: do not REMOVE; use
  MARK_AS_OVER_ANNOTATED for non-IEA wrong annotations). Provenance: abstract
  discusses "three species of HIOMT mRNA" and a "LINE-1 fragment," i.e. gene
  structure/mRNA, not the protein's role in translation [PMID:8397829].

Note on GO:0006629 lipid metabolic process (IEA UniProtKB-KW, from the "Lipid
metabolism" keyword) appears in the UniProt DR GO block but is NOT in the seeded
GOA TSV, so it is not among the 17 annotations to review.
