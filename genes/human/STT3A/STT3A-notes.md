# STT3A (human) — gene review notes

UniProt: P46977 (STT3A_HUMAN). HGNC:6172. Gene on chr 11q24. 705 aa, multi-pass ER membrane protein.
EC 2.4.99.18. CAZy GT66 (glycosyltransferase family 66). PANTHER PTHR13872:SF43.

## Core identity and function

STT3A is the **catalytic subunit of the STT3A/OST-A oligosaccharyltransferase (OST) complex**, an
ER-membrane multi-subunit enzyme that carries out the central step of protein N-linked glycosylation:
en-bloc transfer of the preassembled Glc3Man9GlcNAc2 glycan from dolichyl-diphosphate (Dol-PP) onto
asparagine residues in N-X-S/T sequons of nascent proteins.

- UniProt FUNCTION: "Catalytic subunit of the oligosaccharyl transferase (OST) complex that catalyzes
  the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier
  dolichol-pyrophosphate to an asparagine residue within an Asn-X-Ser/Thr consensus motif in nascent
  polypeptide chains, the first step in protein N-glycosylation" [file:human/STT3A/STT3A-uniprot.txt].
  "This subunit contains the active site and the acceptor peptide and donor lipid-linked oligosaccharide
  (LLO) binding pockets" [file:human/STT3A/STT3A-uniprot.txt].
- Reaction (EC 2.4.99.18, RHEA:22980): di-trans,poly-cis-dolichyl diphosphooligosaccharide +
  L-asparaginyl-[protein] = N(4)-(oligosaccharide...)-L-asparaginyl-[protein] + dolichyl diphosphate + H+
  [file:human/STT3A/STT3A-uniprot.txt]. Cofactor Mg2+ (and Mn2+ by similarity)
  [file:human/STT3A/STT3A-uniprot.txt].
- STT3A is the ACTIVE-SITE subunit of the eukaryotic OST: "STT3 proteins are the active site subunits of
  the eukaryotic OST" [PMID:19167329]. Direct enzymatic IMP/IDA evidence via isoform-specific siRNA
  knockdown and CRISPR knockout: [PMID:19167329], [PMID:31296534], and structure-guided mutagenesis
  [PMID:38670073], [PMID:39509507].

## Co-translational vs post-translational division of labor (STT3A vs STT3B)

Vertebrates express two paralogous catalytic subunits, STT3A and STT3B, in two distinct OST complexes.
The STT3A complex is the co-translational enzyme, physically associated with the SEC61 translocon, and
scans sequons as the nascent chain enters the ER lumen. STT3B is not translocon-associated and handles
skipped/post-translocational sites.

- "The STT3A isoform is primarily responsible for cotranslational glycosylation of the nascent
  polypeptide as it enters the lumen of the endoplasmic reticulum" [PMID:19167329 abstract].
- "The STT3A complex interacts directly with the protein translocation channel to mediate cotranslational
  glycosylation, while the STT3B complex can catalyze posttranslocational glycosylation" [PMID:31296534].
- Loss of STT3A reduces glycosylation of more sites than loss of STT3B: "Roughly 70% of the quantified
  sites showed reduced recovery in STT3A null cells" [PMID:31296534]. STT3A-dependent classes include
  suboptimal sequons and cysteine-rich domains.
- STT3A also *prevents hyperglycosylation*: in STT3A-null cells the chaperone GRP94 is hyperglycosylated
  ("the lumenal ER chaperone GRP94 was hyperglycosylated in STT3A-deficient cells" [PMID:31296534]).
  This "quality-control" role of OST-A is elaborated in [PMID:39509507]: during HSP90B1 (GRP94)
  translocation, an N-terminal peptide "templates the assembly of a translocon complex containing CCDC134
  and OST-A that protects HSP90B1 during folding, preventing its hyperglycosylation and degradation."

## Complex membership and location

- Component of the OST complex; two complexes OST-A (STT3A) and OST-B (STT3B). Common core subunits
  RPN1, RPN2, OST48, OST4, DAD1, TMEM258; OST-A specific accessory subunits DC2/OSTC and KRTCAP2/KCP2
  [file:human/STT3A/STT3A-uniprot.txt]. ComplexPortal CPX-5621 = "Oligosaccharyltransferase complex A".
- GO complex term for the STT3A complex: GO:0160226 "oligosaccharyltransferase complex A" (child of the
  generic GO:0008250 "oligosaccharyltransferase complex"). IDA evidence: cryo-EM structures
  [PMID:31831667] (OST-A/OST-B structures), [PMID:36697828] (OST-A within the ribosome–SEC61–TRAP
  translocon: "the oligosaccharyltransferase complex A (OSTA)"), and CRISPR/cryo-EM [PMID:38670073]
  ("STT3A, the catalytic subunit of OST-A").
- Location: ER membrane, multi-pass (13 predicted TM helices) [file:human/STT3A/STT3A-uniprot.txt].
  EXP subcellular location [PMID:12887896].

## Disease

STT3A deficiency causes congenital disorder of glycosylation type Iw:
- CDG1WAR (autosomal recessive, MIM:615596): V626A reduces STT3A stable expression / activity
  [PMID:23842455] [file:human/STT3A/STT3A-uniprot.txt].
- CDG1WAD (autosomal dominant, MIM:619714): active-site variants (e.g. H46R, R160Q, R405C/H, Y530S)
  cause partial loss of function [PMID:34653363] [file:human/STT3A/STT3A-uniprot.txt].

## Pharmacology / regulation

- STT3A (not STT3B) is specifically inhibited by NGI-1/NGI-235: "STT3A, but not STT3B, is specifically
  inhibited by the N-glycosylation inhibitor NGI-235, which prevents productive binding pose of the glycan
  donor in the active site of STT3A" [file:human/STT3A/STT3A-uniprot.txt]. NGI-1 binds the catalytic site
  and traps the donor substrate [PMID:38670073]. OST-A is required for TLR4 N-glycosylation and
  cell-surface localization, hence inflammatory NF-κB signaling [PMID:38670073].

## Annotation review summary

- Core MF: GO:0004579 dolichyl-diphosphooligosaccharide-protein glycotransferase activity (well supported
  by IDA/IMP: 19167329, 31296534, 38670073, 39509507). ACCEPT the experimental ones; ACCEPT redundant
  IEA/IBA/ISS/TAS supporting the same correct function.
- Core BP: GO:0006487 protein N-linked glycosylation; GO:0180058 protein co-translational transfer of
  dolichol-linked oligosaccharide (IDA PMID:31296534) — the more specific, STT3A-defining BP.
- Core CC: GO:0005789 endoplasmic reticulum membrane; complex GO:0160226 (OST-A) via in_complex.
- GO:0004576 "oligosaccharyl transferase activity" (IEA InterPro) is a less-informative parent of
  GO:0004579 → MODIFY to GO:0004579.
- GO:0043687 post-translational protein modification (IBA) — STT3A is the CO-translational enzyme; this
  IBA is a generic/imprecise BP and arguably better fits the STT3B paralog. MARK_AS_OVER_ANNOTATED (do
  not remove; it is not strictly wrong at the family level but is not STT3A's core biology).
- GO:0009101 glycoprotein biosynthetic process (IEA InterPro) — correct but generic parent of N-linked
  glycosylation. KEEP_AS_NON_CORE.
- GO:0016020 membrane (IEA InterPro; HDA PMID:19946888) — uninformative parent of ER membrane.
  KEEP_AS_NON_CORE.
- GO:0005783 endoplasmic reticulum (IEA/EXP) — correct but less specific than ER membrane.
  KEEP_AS_NON_CORE (EXP) / ACCEPT is defensible; keep non-core since ER membrane is the precise term.
- GO:0005515 protein binding (IPI, 7 annotations from large-scale interaction/proteomics screens:
  21903422 innate-immunity, 30021884 histone crosslinking-MS, 32707033 kinase interactome, 32814053
  neurodegeneration interactome, 33845483 SARS-CoV-2 proteomics, 35271311 OpenCell, 36217030 SARS-CoV-2
  interactome). Bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED per policy (never REMOVE
  an IPI). Interactors include RPN1 (a genuine OST subunit) and various screen hits.
