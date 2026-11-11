# GLO2 (At3g14415; UniProt Q9LRS0) - curation notes

**Deep research could not be run for this gene** (no deep-research provider API keys in this
environment). These notes were built only from cached publications (`publications/PMID_*.md`),
the UniProt record (`GLO2-uniprot.txt`) and papers cached with `ai-gene-review fetch-pmid`.
No `-deep-research-*.md` file exists for this gene.

## Nomenclature warning (GOX1 vs GOX2)

- UniProt: `GN Name=GLO2; Synonyms=GOX1; OrderedLocusNames=At3g14415`, `Short=GOX2` (from
  PMID:25416784) and `DR TAIR; AT3G14415; GOX2`. In this folder GLO2 = GOX2 = At3g14415 (TAIR
  naming); the UniProt synonym GOX1 reflects crossed usage in part of the literature.
- TAIR-consistent papers: Hackenberg et al. 2011 [PMID:21828292 "Among them, isoform 2, GOX2
  (At3g14415), is thought to play a major role in the photorespiratory glycolate oxidation
  step"]; Dellero et al. 2015 [PMID:25416784 "Kinetic parameters of purified recombinant GOX1
  (At3g14420) and GOX2 (At3g14415) from A. thaliana (the two GOX genes highly expressed in
  leaves)"]; Kerchev et al. 2016 (full text, checked via web: GOX2 = At3g14415).
- Crossed naming: Reumann et al. 2007 [PMID:17951448 "both isoforms of glycolate oxidase (GOX),
  GOX1 (At3g14415; PRL>) and GOX2 (At3g14420; ARL>), were specifically identified"]. Here "GOX1"
  = our GLO2.

## Molecular function

- Glycolate oxidase (EC 1.1.3.15; GO:0003973 (S)-2-hydroxy-acid oxidase activity, which replaced
  obsolete GO:0008891 glycolate oxidase activity; checked in OLS4).
- Recombinant At-GOX2 is an O2-dependent oxidase, not a dehydrogenase [PMID:21828292 "enzymes
  catalyzed oxidase reactions, consuming O 2 and producing H 2 O 2 as byproduct, but neither
  showed any dehydrogenase activity with NAD + or NADP + ."].
- Substrate preference [PMID:21828292 "whereas the plant At-GOX2 was ~10-fold more active with
  glycolate than l -lactate."], [PMID:21828292 "By contrast, At-GOX2 exhibited a 40 times higher
  V max for glycolate than for l -lactate."]. UniProt kinetics: Km 1.906 mM glycolate and 0.356 mM
  L-lactate (PMID:21828292); Km 0.3 mM glycolate, kcat 30.10 s-1 (PMID:25416784). Minor activity
  with hydroxypyruvate and glycerate in vitro.
- In vivo complementation: [PMID:21828292 "The expression of At-GOX2 or No-LOX complemented this
  HCR phenotype"] (Synechocystis glcD1/glcD2 double mutant).
- Mechanism: hydride transfer [PMID:25416784 "Calculations of commitment factors from observed
  kinetic isotope effect values support a hydride transfer mechanism."].
- FMN cofactor (by similarity to spinach GOX P05414); FMN-dependent alpha-hydroxy acid
  dehydrogenase family (PANTHER PTHR10578:SF110).

## Localization

- Peroxisome; identified in purified leaf peroxisomes with PTS1 PRL> (PMID:17951448, where it is
  called GOX1). Other proteomic detections (vacuole, nucleus, chloroplast, stroma, apoplast,
  cytosol, stress granule) are most likely carry-over of this abundant matrix enzyme; handled per
  projects/ARATH/organelle-audit.md.

## Biological process

- Photorespiration (C2 cycle), co-regulated with GLO1 and other photorespiratory genes
  [PMID:22303256 "Two of these genes (At3g14415 and At3g14420) are transcriptionally co-regulated
  with other photorespiratory genes"].
- Redundancy with GLO1 [PMID:26896850 "We show that two Arabidopsis genes, GOX1 and GOX2, share a
  redundant photorespiratory role."]; combined knock-down is severe [PMID:26896850 "Air-grown
  amiRgox1/2 plants with a residual 5% GOX activity exhibited a severe growth phenotype."].
- GOX2 versus GOX1 [PMID:27225899 "knocking out the nearly identical GOX2 in the cat2-2 background
  did not affect the photorespiratory phenotype, indicating that GOX1 and GOX2 play distinct
  metabolic roles."]; both single mutants are affected by high light [PMID:27225899 "High light
  negatively affected the photosynthetic performance and growth of both gox1-1 and gox2-1
  mutants"].
- Defence: GOX-derived H2O2 in nonhost resistance (PMID:22286136, abstract only; Kerchev et al.
  2016 full text attributes gox1-1 and gox2-1 to this paper).
- Ozone sensitivity of a T-DNA line at the GOX1/GOX2 locus with ~60% GOX activity (PMID:28339978).

## Module comparison (modules/photorespiration_c2_cycle.yaml)

- Module: GO:0003973 MF, GO:0009853 photorespiration, GO:0005777 peroxisome. Review agrees on MF
  and location; the existing (accepted) process annotation is the more specific GO:0009854
  oxidative photosynthetic carbon pathway (part_of GO:0009853).
