# TXNDC12 (O95881) review notes

## Identity
- Thioredoxin domain-containing protein 12; aliases ERp18, ERp19, ERp16, hTLP19, TLP19. HGNC:24626. 172 aa precursor (mature 27-172 after signal peptide cleavage).
- Small ER-lumen thioredoxin-superfamily oxidoreductase of the AGR/PDI-related family. Single thioredoxin-like domain (27-156) with an **unusual CGAC active-site motif** and redox-active disulfide C66-C69.
- C-terminal EDEL/ER-retention motif (169-172, "Prevents secretion from ER"). N-terminal signal peptide 1-26. PDB 1SEN (X-ray, 1.20 A), 2K8V (NMR).
- EC 1.8.4.2 (protein-disulfide reductase, glutathione). UniProt FUNCTION: "Protein-disulfide reductase of the endoplasmic reticulum that promotes disulfide bond formation in client proteins through its thiol-disulfide oxidase activity."

## Functional evidence

### PMID:12761212 (Alanen et al. 2003, "Functional characterization of ERp18") — abstract only cached
- "we describe the functional characterization of a new 18-kDa protein (ERp18) related to protein-disulfide isomerase. We show that ERp18 is located in the endoplasmic reticulum and that it contains a single catalytic domain with an unusual CGAC active site motif"
- "in vitro ERp18 possesses significant peptide thiol-disulfide oxidase activity, which is dependent on the presence of both active site cysteine residues."
- "the reduced form of the protein is more stable than the oxidized form, suggesting that it is involved in disulfide bond formation."
- Basis of EC 1.8.4.2 and the MUTAGEN C66S/C69S "Loss of protein-disulfide reductase (glutathione) activity" annotations.

### PMID:18628206 (Jeong et al. 2008, "ERp16 ... role in apoptosis") — full text cached
- Same protein: "a mammalian thioredoxin-like protein, ERp16 (previously designated ERp18, ERp19, or hTLP19)."
- "a thioredoxin-like domain with an active site motif (CGAC), and a COOH-terminal endoplasmic reticulum (ER) retention sequence (EDEL) ... localized in the lumen of the ER."
- "Biochemical experiments with the recombinant mature protein revealed it to be a thioldisulfide oxidoreductase. Its redox potential was about -165 mV; its active site cysteine residue Cys(66) was nucleophilic ... it catalyzed the formation, reduction, and isomerization of disulfide bonds, with the unusual CGAC active site motif being responsible for these activities"
- "The observations that the redox potential of ERp16 (-165 mV) was within the range of that of the ER (-135 to -185 mV) and that ERp16 catalyzed disulfide isomerization of scrambled ribonuclease A suggest a role for ERp16 in protein disulfide isomerization in the ER."
- Apoptosis: "Expression of ERp16 in HeLa cells inhibited the induction of apoptosis by agents that elicit ER stress, including brefeldin A, tunicamycin, and dithiothreitol. In contrast, expression of a catalytically inactive mutant of ERp16 potentiated such apoptosis, as did depletion of ERp16 by RNA interference. Our results suggest that ERp16 mediates disulfide bond formation in the ER and plays an important role in cellular defense against prolonged ER stress."

## GOA assessment
- GO:0005783 ER (IBA) / GO:0005788 ER lumen (IEA/IDA) — ACCEPT; ER lumen is the curated/experimental localization (EDEL retention motif).
- GO:0019153 protein-disulfide reductase (glutathione) activity (IEA + IDA, EC 1.8.4.2) — ACCEPT (core MF; PMID:12761212).
- GO:0015035 protein-disulfide reductase activity (IDA, MGI) — ACCEPT (core MF; broader oxidoreductase).
- GO:1902236 negative regulation of ER stress-induced intrinsic apoptotic signaling (IDA, MGI; PMID:18628206) — ACCEPT/KEEP_AS_NON_CORE; well supported (inhibits ER-stress apoptosis; catalytically dependent) but a downstream/physiological consequence of its redox-folding function rather than the primary biochemical activity.
- GO:0005515 protein binding x3 (IPI; PMID:25416956 proteome-scale interactome, PMID:31515488 variant interactome, PMID:32296183 HuRI) — HT interactome captures, uninformative; KEEP_AS_NON_CORE.

## Core function summary
Core MF = protein-disulfide reductase / thiol-disulfide oxidoreductase activity (CGAC motif, C66/C69); BP = oxidative protein folding in the ER / cell redox homeostasis, with a documented role in negative regulation of ER-stress-induced apoptosis; CC = ER lumen.
