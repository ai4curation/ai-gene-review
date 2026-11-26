# GGAT1 (At1g23310, Q9LR30) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes are a
literature summary built only from cached publications (`publications/PMID_*.md`) and the UniProt
record (`GGAT1-uniprot.txt`). No `*-deep-research-*.md` file exists for this gene.

## Identity and family

- GGAT1 (synonyms AOAT1, GGT1, AlaAT3-like) is one of four alanine aminotransferase (AlaAT)-like
  class I PLP-dependent aminotransferases in Arabidopsis; GGAT1 and GGAT2 (At1g70580) carry a C-terminal
  PTS1 [PMID:12529529 "GGT1 and GGT2 are Ala aminotransferase (AlaAT) homologs from Arabidopsis that
  represent another type of glyoxylate aminotransferase. These proteins are class I aminotransferases,
  each containing a putative PTS1."].
- UniProt: "Belongs to the class-I pyridoxal-phosphate-dependent aminotransferase family. Alanine
  aminotransferase subfamily." PANTHER PTHR11751:SF472.

## Activities (substrate breadth)

- Recombinant GGAT1 and GGAT2 catalyse four transaminations [PMID:12529529 "Four aminotransferase
  activities were specifically associated with GGT1 and GGT2, using the substrate pairs glutamate
  (Glu):glyoxylate, Ala:glyoxylate, Glu:pyruvate, and Ala:2-oxoglutarate."].
- No serine:glyoxylate or aspartate aminotransferase activity [PMID:12529529 "AGT activity was also
  detectable, but GGT1 did not catalyze SGT or AspAT reactions (data not shown)."].
- Kinetics (UniProt, from PMID:12529529): Km 0.27 mM glyoxylate, 3 mM glutamate, 7.16 mM alanine,
  0.27 mM 2-oxoglutarate, 0.33 mM pyruvate.
- The AGT (Ala:glyoxylate) reaction was detected but not characterized kinetically, and its
  physiological significance is disputed [PMID:12529529 "but the physiological significance of the AGT
  reaction for photorespiration has been disputed"].

Judgement: the glutamate:glyoxylate reaction (GO:0047958, glycine:2-oxoglutarate transaminase,
written in the reverse direction) is the core photorespiratory activity. Ala:2-oxoglutarate (GO:0004021)
and Ala:glyoxylate (GO:0008453) are genuine but non-core.

## Localization

- Peroxisome: GFP fusion in BY-2 cells depends on PTS1 [PMID:12631323 "When AOAT1 fused to green
  fluorescent protein (GFP) was expressed in BY-2 cells, it was found to be localized to peroxisomes
  depending on PTS1."]; sucrose-gradient fractionation [PMID:12529529 "GGT activity was localized
  exclusively to Arabidopsis peroxisomes"]; leaf peroxisome proteomics [PMID:17951448 "GGT1 (At1g23310;
  SKM>) and pMDH2 (At5g09660; RIx 5 HL) dominated over the second isoform"].
- Proteomic hits in vacuole, chloroplast, apoplast, nucleus/membrane fractions and crude cytosol are
  best explained as contamination by an abundant peroxisomal matrix enzyme.

## Physiological role

- The aoat1-1 (ggat1) knockout has drastically reduced leaf GGAT activity and a conditional,
  high-CO2-rescued growth phenotype [PMID:12631323 "The activity of GGAT and alanine:glyoxylate
  aminotransferase (AGAT) in the above-ground tissues of aoat1-1 was reduced drastically"; "These
  phenotypes resembled those of photorespiration-deficient mutants."].
- Phenotype is weak because GGAT2 provides residual activity [PMID:22303256 "Ggat 1 knock-outs show a weak
  photorespiratory phenotype and survive in air at moderate light intensities. Residual GGAT activity can be
  detected in mutant leaf extracts"].
- Overexpression raises Ser, Gly and citrulline in light, repressed by high CO2 [PMID:16950862 "The levels
  of free serine, glycine, and citrulline increased markedly in GGAT1 overexpression lines compared with
  levels in the wild type"].
- Expression in roots suggests non-photorespiratory roles [PMID:16950862 "In GGAT1 - GUS seedlings, GUS
  signals were also strongly detected in roots ( Fig. 1A ), suggesting that the role of GGAT1 is not
  restricted to photorespiration."].
- ggt1 mutants were recovered in an ABA/RD29A:LUC screen; altered H2O2, ABA and proline
  [PMID:17318317 "A light-dependent increase in H2O2 accumulation was observed in ggt1-1 consistent with
  the previously characterized role of GGT1 in photorespiration."]. Treated as an indirect consequence
  of photorespiratory impairment.

## Annotation-specific notes

- Hypoxia IEP (PMID:17319845, abstract only): the paper is about AlaAT1/AlaAT2; UniProt cites it for slight
  low-oxygen induction of GGAT1 in shoots. Kept as non-core expression response.
- L-alanine catabolic process (UniPathway IEA): the hypoxia alanine breakdown role belongs to AlaAT1
  [PMID:17319845 "suggesting that AlaAT1 is the major AlaAT isozyme in Arabidopsis"]; no evidence that
  peroxisomal GGAT1 catabolizes alanine in vivo, so marked over-annotated.
- mRNA binding: GGAT was a hit in a leaf RNA interactome capture screen (PMID:32344669) with no follow-up;
  a peroxisomal matrix enzyme, so marked over-annotated.

## Module comparison (modules/photorespiration_c2_cycle.yaml, ggat_step)

Module asserts GO:0047958 / GO:0009853 / GO:0005777 for GGAT1. This review agrees on all three.
