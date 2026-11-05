# Ucp2 (rat, P56500) - manual literature synthesis

No deep-research provider API was available; this synthesis was compiled manually from the
cached publications in `publications/`, the UniProt record (`Ucp2-uniprot.txt`) and the
existing human UCP2 review (`genes/human/UCP2`).

## Identity and family

- Rat uncoupling protein 2 (Ucp2, SLC25A8), 309 aa, UniProt P56500. Member of the mitochondrial
  carrier family, six transmembrane helices in three Mito_carr repeats (Pfam PF00153; PANTHER
  PTHR45618) [file:rat/Ucp2/Ucp2-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."].
- Location: inner mitochondrial membrane [file:rat/Ucp2/Ucp2-uniprot.txt "Mitochondrion inner membrane"].

## Molecular function

- Biochemistry established with the human orthologue: reconstituted UCP2 is a C4-metabolite/phosphate
  antiporter [PMID:24395786 "UCP2 reconstituted in lipid vesicles catalyzed the exchange of malate,
  oxaloacetate, and aspartate for phosphate plus a proton from opposite sides of the membrane."], which
  limits glucose oxidation and favours glutaminolysis [PMID:24395786 "by exporting C4 compounds out of
  mitochondria, UCP2 limits the oxidation of acetyl-CoA-producing substrates such as glucose and enhances
  glutaminolysis"].
- Proton conductance: in rat kidney mitochondria superoxide activated a nucleotide-sensitive proton
  conductance attributed to UCP2 [PMID:12372827 "superoxide activates UCP2 in rat kidney mitochondria from
  the matrix side of the mitochondrial inner membrane"]; this model was later disputed (UniProt CAUTION).
  In rat INS-1E cells UCP2 contributes to proton leak [PMID:21172424 "we show that UCP2 contributes to
  proton leak and attenuates glucose-induced rises in both respiratory activity and the coupling efficiency
  of oxidative phosphorylation."].

## Rat-specific cell biology (INS-1E beta cells)

- UCP2 is of low abundance; levels hundreds-fold below UCP1 in BAT [PMID:18692019 "These mitochondrial
  concentrations are hundreds of times lower than UCP1 in brown adipose tissue"].
- Translational control by glutamine [PMID:18692019 "Omission of glutamine from the medium resulted in
  decreases in UCP2 in cells and mitochondria (Fig. 2A and B) without affecting Ucp2 mRNA levels (Fig. 2C)."]
  and induction by high glucose [PMID:18692019 "doubling glucose concentration to 20 mM increased protein
  levels 2-fold over control (Fig. 2D)"].
- Rapid turnover [PMID:18692019 "UCP2 was found to have a short half-life of approximately 1 h (Fig. 4A, B)"].
- Insulin secretion: UCP2 knockdown improves GSIS, an effect abolished by antioxidant
  [PMID:21172424 "We conclude that UCP2 plays both regulatory and protective roles in β cells by acutely
  lowering GSIS and chronically preventing oxidative stress."].

## Physiology and expression studies in rat

- Hypothalamus: antisense knockdown worsens TNF-alpha-induced damage [PMID:18703058 "The inhibition of UCP2
  expression by an antisense oligonucleotide enhanced the damaging effects of TNF-alpha."].
- Expression changes (IEP-level evidence only): adipocytes, glucose/fatty acids/insulin/T3 [PMID:18079609];
  heart, hypoxia [PMID:17704287]; regenerating liver [PMID:19104935]; placenta, dexamethasone [PMID:20393169];
  hippocampus/PC12, lead [PMID:33576715].
- Cold adaptation (mouse): UCP2 favours fatty-acid use in BAT [PMID:28130074 "We conclude that UCP2 regulates
  BAT thermogenesis by favouring the utilization of NEFA, a process required for the adaptation to cold."].
