# UAP1 (Q16222) review notes

Human **UAP1** = *UDP-N-acetylglucosamine pyrophosphorylase 1*, historically **AGX** /
**AgX** / **SPAG2** (sperm-associated antigen 2). UniProt recommended name is
**UDP-N-acetylhexosamine pyrophosphorylase** (Q16222), reflecting that the enzyme acts on
both GlcNAc-1-P and GalNAc-1-P.

## Core enzymatic function (verified)

UAP1 catalyzes the **last step of the hexosamine biosynthetic pathway (HBP)**: condensation
of **N-acetyl-α-D-glucosamine 1-phosphate (GlcNAc-1-P) with UTP to give UDP-GlcNAc + diphosphate**
(EC 2.7.7.23), and analogously **GalNAc-1-P + UTP → UDP-GalNAc** (EC 2.7.7.83).

- UniProt FUNCTION: "Catalyzes the last step in biosynthesis of uridine diphosphate-N-acetylglucosamine (UDP-GlcNAc) by converting UTP and glucosamine 1-phosphate (GlcNAc-1-P) to the sugar nucleotide ... Also converts UTP and galactosamine 1-phosphate (GalNAc-1-P) into uridine diphosphate-N-acetylgalactosamine (UDP-GalNAc)" [file:human/UAP1/UAP1-uniprot.txt].
- UniProt PATHWAY: "Nucleotide-sugar biosynthesis; UDP-N-acetyl-alpha-D-glucosamine biosynthesis; UDP-N-acetyl-alpha-D-glucosamine from N-acetyl-alpha-D-glucosamine 1-phosphate: step 1/1." [file:human/UAP1/UAP1-uniprot.txt].
- CATALYTIC ACTIVITY blocks give EC=2.7.7.23 (Rhea:RHEA:13509) and EC=2.7.7.83 (Rhea:RHEA:34363) [file:human/UAP1/UAP1-uniprot.txt].

The product **UDP-GlcNAc** is the universal amino-sugar donor for N- and O-glycosylation,
O-GlcNAcylation, GPI anchor and proteoglycan synthesis, and (via GNE) sialic acid — so UAP1
sits at a metabolic hub, but its own molecular function is the pyrophosphorylase (nucleotidyl-transfer)
step.

### Cloning / catalytic mechanism
- Mio et al. 1998 (PMID:9603950) cloned the human, *C. albicans*, and *S. cerevisiae* UAP1 genes;
  human UAP1 cDNA "was identical to previously reported AGX1"; all recombinant proteins "possessed
  UDP-N-acetylglucosamine pyrophosphorylase activities in vitro"; ScUAP1 null is lethal and is rescued
  by human UAP1; phosphomutase reaction precedes uridyltransfer [PMID:9603950 abstract]. Basis of the
  TAS GO:0003977 and GO:0006048 annotations.
- Wang-Gillam, Pastuszak & Elbein 1998 (PMID:9765219): the pig-liver UDP-HexNAc pyrophosphorylase makes
  both UDP-GlcNAc and UDP-GalNAc; peptides matched AGX1; the **17-aa insert (isoform AGX2)** shifts
  specificity — AGX1 "was 2-3 times more active with GalNAc-1-P than with GlcNAc-1-P" whereas AGX2
  "had 8-fold better activity with GlcNAc-1-P than with GalNAc-1-P" [PMID:9765219 abstract]. Basis of the
  EXP GO:0003977 and GO:0052630 annotations, and of the isoform substrate-preference note.

### Structure / oligomeric state
- Peneff et al. 2001 (PMID:11707391, not cached; cited in UniProt): X-ray structures (PDB 1JV1/1JV3/1JVD/1JVG)
  of the two human isoforms with UDP-GlcNAc/UDP-GalNAc; the alternatively spliced insert affects oligomeric
  assembly and active-site architecture. UniProt SUBUNIT: "Monomer and homodimer" [file:human/UAP1/UAP1-uniprot.txt].
- Reactome R-HSA-446204: "Cytosolic UAP1 catalyzes the reaction of N-acetyl-D-glucosamine 1-phosphate
  (GlcNAc1P) and UTP to UDP-N-acetyl-D-glucosamine and pyrophosphate. Structural studies indicate that the
  active form of the enzyme is a dimer" [reactome:R-HSA-446204].

## Moonlighting / secondary function: IRF3 pyrophosphorylation (innate immunity)
- Yang et al. 2023 (PMID:36603579, Mol Cell): identifies UAP1 as a **protein serine pyrophosphorylase**
  that pyrophosphorylates IRF3 at Ser-386 (after TBK1 phosphorylation), promoting IRF3 dimerization/activation
  and type I IFN responses; "Uap1 deficiency significantly impairs the activation of both DNA- and RNA-viruse-induced
  type I IFN pathways, and the Uap1-deficient mice are highly susceptible to lethal viral infection" [PMID:36603579 abstract].
  Basis of the IDA GO:0141090 (protein serine pyrophosphorylase activity), GO:0032481 (positive regulation of type I
  interferon production) and GO:0140374 (antiviral innate immune response) annotations. UniProt adds EC 2.7.4.- and a
  third CATALYTIC ACTIVITY (5-InsP7 + phospho-Ser-protein → diphospho-Ser-protein + InsP6) [file:human/UAP1/UAP1-uniprot.txt].
  Mutagenesis: 115-122 (RLGVAYPK→ALGVAYPA) and K407A abolish both pyrophosphorylase and protein-pyrophosphorylation
  activities; R453A decreases IRF3 interaction/pyrophosphorylation [file:human/UAP1/UAP1-uniprot.txt] — i.e. the same
  active site does both jobs. This is a genuine but non-canonical (moonlighting) role, distinct from the metabolic core.

## Localization
- Cytosol. UniProt SUBCELLULAR LOCATION: "Cytoplasm, cytosol" [file:human/UAP1/UAP1-uniprot.txt].
- Original AGX cloning (PMID:8025165): AgX localized by immunofluorescence to the principal piece of the sperm tail;
  widely expressed, low in placenta/muscle/liver; AGX-1 (testis) vs AGX-2 (somatic) isoform abundance [PMID:8025165 abstract].
  Basis of the IDA GO:0005829 (cytosol) annotation. HPA also supports cytosol (IDA, GO_REF:0000052).

## Interaction
- Rolland et al. 2014 (PMID:25416956), the CCSB binary-interactome map, is the IntAct source for the
  GO:0042802 "identical protein binding" (self-interaction / homodimer) IPI. The cached paper is a
  proteome-scale Y2H map with no UAP1-specific text; the self-interaction is consistent with the
  well-established UAP1 homodimer (UniProt SUBUNIT; Peneff 2001; Reactome). Bare identical-protein-binding
  is uninformative as a standalone MF, so it is retained but marked over-annotated (per policy, an IPI is
  not removed).

## Isoforms
- AGX2 (Q16222-1, displayed) and AGX1 (Q16222-2) differ by a **17-aa insert** (residues 454-470, VSP_004483)
  near the C-terminus that switches substrate preference (GlcNAc-1-P for AGX2 vs GalNAc-1-P for AGX1); isoform 3
  (Q16222-3) lacks a single residue (VSP_014523) [file:human/UAP1/UAP1-uniprot.txt; PMID:9765219; PMID:8025165].

## Curation summary
- **Core**: UDP-N-acetylglucosamine diphosphorylase activity (GO:0003977, MF) and UDP-N-acetylglucosamine
  biosynthetic process (GO:0006048, BP), acting in the cytosol (GO:0005829, CC).
- **Secondary/experimentally supported, non-core**: UDP-GalNAc diphosphorylase activity (GO:0052630);
  protein serine pyrophosphorylase activity (GO:0141090) and the associated innate-immunity BP terms.
- **Over-annotations (too general or uninformative)**: GO:0016772 (transferase, transferring P-groups),
  GO:0070569 (uridylyltransferase activity), GO:0042802 (identical protein binding).
</content>
</invoke>
