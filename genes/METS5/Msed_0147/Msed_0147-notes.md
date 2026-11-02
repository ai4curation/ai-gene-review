# Msed_0147 (A4YD22) notes: biotin carboxylase (alpha) subunit of acetyl-CoA/propionyl-CoA carboxylase

Automated deep research was unavailable for this gene (no `-deep-research-*.md` file). These notes
come from my own literature search (Europe PMC, cached papers in `publications/`) and the UniProt
record. Session date 2026-11-01.

## Identity

- UniProt A4YD22 (TrEMBL, unreviewed), 510 aa, "Biotin carboxylase", EC 6.3.4.14, locus Msed_0147.
- Domains: biotin carboxylation domain (PS50979, 3-451), ATP-grasp (PS50975, 122-320); Pfam
  Biotin_carb_N, CPSase_L_D2, Biotin_carb_C. PANTHER PTHR45007:SF1. [file:METS5/Msed_0147/Msed_0147-uniprot.txt]
- Gene neighbour: Msed_0148 (BCCP, beta subunit); the two genes appear translationally coupled
  [PMID:23530213 "The M. sedula RBS for E1β was retained, as the two genes (E1α and E1β) appear to be translationally coupled."].
  The carboxyltransferase (gamma) subunit is encoded elsewhere, Msed_1375.

## The enzyme

- The carboxylase of the 3HP/4HB cycle was purified from M. sedula. It is one enzyme that acts on both
  acetyl-CoA and propionyl-CoA, a ~560 kDa complex of a 57 kDa biotin carboxylase (alpha), a 57 kDa
  carboxyltransferase (gamma) and an 18.6 kDa biotin carrier (beta), probably (alpha beta gamma)4
  [PMID:12581213 "These reactions were studied in the thermophilic and acidophilic Metallosphaera sedula and are shown to be catalyzed by one single large enzyme, which acts equally well on acetyl-CoA and propionyl-CoA."]
  [PMID:12581213 "The enzyme consists of two large subunits of 57 kDa each representing biotin carboxylase (alpha) and carboxytransferase (gamma), respectively, and a small 18.6 kDa biotin carrier protein (beta)."]
  Km 0.06 mM acetyl-CoA, 0.07 mM propionyl-CoA, 0.04 mM ATP, 0.3 mM bicarbonate (abstract).
- Earlier: biotin-dependent ACC and PCC activities in autotrophic M. sedula extracts, and a small
  biotin-carrying protein [PMID:9973333 "cells contained the biotin-dependent acetyl-CoA carboxylase and propionyl-CoA carboxylase as well as phosphoenolpyruvate carboxylase."].
- Acidianus brierleyi ortholog: alpha4beta4gamma4, bifunctional; ATP-binding residues are in the BC
  subunit [PMID:12533469 "The ATP-binding residues were found in the biotin carboxylase subunit, whereas the conserved biotin-binding site was located on the biotin carboxyl carrier protein."].
- Pathway role: key carboxylating enzyme of the cycle [PMID:18079405 "Metallosphaera sedula, fixed CO2 with acetyl-coenzyme A (acetyl-CoA)/propionyl-CoA carboxylase as the key carboxylating enzyme."];
  promiscuous [PMID:19684143 "This enzyme is the second promiscuous enzyme in this cycle; the other is acetyl-CoA/propionyl-CoA carboxylase"].
- Gene assignment and induction: [PMID:24532060 "especially the genes encoding acetyl-CoA/propionyl-CoA carboxylase (ACCαβγ) (Msed_0147, Msed_0148, Msed_1375; 7- to 30-fold)"].
- Heterologous function: Msed_0147-0148 + Msed_1375 (E1) expressed in Pyrococcus furiosus gave ACC
  activity (phosphate release from acetyl-CoA, ATP, bicarbonate) and, with E2/E3, 3-HP from CO2
  [PMID:23530213 "E1 (acetyl/propionyl-CoA carboxylase, encoded by Msed_0147, Msed_0148, and Msed_1375)"].
- ACC is a high flux-control step and is inhibited by malonyl-CoA, succinyl-CoA, ADP and CoA
  [PMID:27771364 "ACC is known to be post-translationally regulated through inhibition by malonyl-CoA, succinyl-CoA, ADP, and CoA (Hugler et al., 2003)."].
- Archaea have no fatty acids, so this ACC does not feed fatty-acid synthesis [PMID:9973333 "Acetyl-CoA carboxylase activity is unexpected in archaea since they do not contain fatty acids in their membranes."].

- Subunit expression: recombinant alpha and gamma subunits made in E. coli were insoluble and inactive;
  active recombinant holoenzyme was obtained only in P. furiosus with the M. sedula biotin protein ligase
  [PMID:27315782 "In both cases, the recombinant ACC α and γ subunits were recovered only in the insoluble fraction, and furthermore lacked catalytic activity."].

## Subunit-level function

The BC subunit performs the first half-reaction: ATP-dependent carboxylation of the biotin on BCCP
(GO:0004075 biotin carboxylase activity, EC 6.3.4.14). The overall acyl-CoA carboxylase activities
(GO:0003989, GO:0004658) belong to the alpha-beta-gamma complex, so the BC subunit `contributes_to`
them. No individual-subunit assay has been published for the M. sedula enzyme; the half-reaction
assignment rests on the BC domain architecture and on the A. brierleyi homology analysis.

## GO annotation decisions

- GO:0004075 biotin carboxylase activity (IEA EC) - ACCEPT, core.
- GO:0005524 ATP binding - KEEP_AS_NON_CORE (substrate binding, part of BC activity).
- GO:0000166 nucleotide binding - MODIFY to ATP binding.
- GO:0046872 metal ion binding - KEEP_AS_NON_CORE (ATP-grasp Mg2+; the ARBA Co2+ cofactor line is unsupported).
- NEW: contributes_to GO:0003989 and GO:0004658; involved_in GO:0015977 carbon fixation.
- CC: GO has no propionyl-CoA carboxylase complex term, and GO:0009317 acetyl-CoA carboxylase complex
  is defined as catalysing "the first step in long-chain fatty acid biosynthesis", which does not fit an
  archaeal enzyme in a CO2-fixation cycle. No CC term is added, and no complex is set in core_functions
  (the generic GO:1902494 catalytic complex would add little). Raised as a suggested question.

## Open points

- NCBI esummary was down on 2026-11-01. The uncached PMIDs (12581213, 9973333, 12533469, 27315782)
  were cached with the repo's normal fetch pipeline, using metadata taken from efetch XML.
