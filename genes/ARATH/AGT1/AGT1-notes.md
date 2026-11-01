# AGT1 / SGAT (At2g13360, Q56YA5) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes are a
literature summary built only from cached publications (`publications/PMID_*.md`) and the UniProt
record (`AGT1-uniprot.txt`). No `*-deep-research-*.md` file exists for this gene.

## Identity and family

- AGT1 (alanine:glyoxylate aminotransferase 1; serine:glyoxylate aminotransferase, SGAT) is a class
  V PLP-dependent aminotransferase, homolog of animal AGT1/AGXT, encoded by a single gene with a
  C-terminal PTS1 [PMID:11309139 "Southern blot analysis confirmed that Arabidopsis AGT1 is encoded by
  a single gene."]. PANTHER PTHR21152:SF24; Pfam PF00266 (Aminotran_5).
- Crystal structure: homodimer, PLP bound non-covalently; residues Tyr35'/Arg36' from the partner
  subunit bind L-serine, unlike human/Anabaena AGT1 that prefer alanine [PMID:31681359 "In comparison,
  AGT1 from humans and AGT1 from Anabaena lack these two residues and instead position a tyrosine ring
  into the binding site, which accounts for their preference for l-alanine instead of l-serine."].

## Activities (substrate breadth)

- Recombinant AGT1 catalyses Ala:glyoxylate, Ser:glyoxylate and Ser:pyruvate transamination, with
  Ser:glyoxylate preferred [PMID:11309139 "AGT1 had the highest specific activity with the serine :
  glyoxylate transamination, and apparent Km measurements indicate that this is the preferred in vivo
  reaction."].
- Native leaf SGAT: Ala:glyoxylate about 55% of Ser:glyoxylate rate; kinetic constants suggest Ala and
  Ser could be used similarly as amino donors [PMID:18235971 "suggested that, during photorespiration,
  Ala and Ser are used by Arabidopsis SGAT with equal efficiency as amino group donors for
  glyoxylate."].
- Asparagine is an efficient donor (Vmax 5-20x higher than Ser/Ala); Asn induces AGT1 transcripts in
  roots [PMID:23098902 "These results suggest that AGT1 is involved in Asn metabolism in
  Arabidopsis."].

Judgement: L-serine:glyoxylate transaminase (GO:0050281) is the core photorespiratory activity, the
one whose loss in the sat mutants is lethal in air. Ala:glyoxylate (GO:0008453), Ser:pyruvate
(GO:0004760) and Asn:oxo-acid (GO:0047297) activities are real but non-core.

## Localization

- Peroxisome by in vitro import and fractionation [PMID:11309139 "In vitro import experiments and
  subcellular fractionations localized AGT1 to peroxisomes."]; BiFC with RabGAP22 in peroxisomes
  [PMID:24505423 "A clear fluorescence signal was detected in the peroxisomes, demonstrating interaction
  of the two proteins (Figure 2D)."]; abundant in leaf peroxisome proteome (PMID:17951448).
- Proteomic hits in chloroplast/stroma, mitochondrion, plasma membrane, apoplast and crude cytosol
  are treated as contamination.

## Physiological role

- sat mutants lack SGAT activity, are inviable in air but normal at high CO2, and accumulate Ser and Gly
  [PMID:16592821 "Three mutants of the crucifer Arabidopsis thaliana (Linnaeus) Heynhold were isolated
  that are completely lacking in activity catalyzed by serine-glyoxylate aminotransferase (EC 2.6.1.45),
  a peroxisomal enzyme involved in photorespiratory carbon metabolism."].
- The sat lesion is a P251L substitution in AGT1 that abolishes activity [PMID:11309139 "Sequence
  analysis of the photorespiratory sat mutants revealed a single nucleotide substitution in the AGT1
  gene from these plants."].
- Role in the cycle: the SGAT step supplies the second amino group for glycine formation
  [PMID:22303256 "The amino group is used for the concomitant amination of glyoxylate to glycine."].
- Non-photorespiratory roles: Asn catabolism (PMID:23098902); root development and salt tolerance in
  overexpressors (PMID:31161264, not cached; mentioned in UniProt only).

## Annotation-specific notes

- Peroxisome EXP from PMID:24505423 (RabGAP22 paper): BiFC signal of the RabGAP22-AGT1 pair in
  peroxisomes of N. benthamiana. Supports peroxisomal localization; accepted.
- L-alanine:oxo-acid transaminase (GO:0047635, Rhea IEA) is the parent of GO:0008453; the Rhea reaction
  mapped (Asn + pyruvate = 2-oxosuccinamate + Ala) is a reversible transamination involving alanine.
  Non-core, like GO:0008453.

## Module comparison (modules/photorespiration_c2_cycle.yaml, sgat_step)

Module asserts GO:0050281 / GO:0009853 / GO:0005777 for AGT1. This review agrees on all three.
