# GLO1 (At3g14420; UniProt Q9LRR9) - curation notes

**Deep research could not be run for this gene** (no deep-research provider API keys in this
environment). These notes were built only from cached publications (`publications/PMID_*.md`),
the UniProt record (`GLO1-uniprot.txt`) and papers cached with `ai-gene-review fetch-pmid`.
No `-deep-research-*.md` file exists for this gene.

## Nomenclature warning (GOX1 vs GOX2)

- UniProt: `GN Name=GLO1; OrderedLocusNames=At3g14420`, with `Short=GOX1` (from PMID:25416784)
  and `DR TAIR; AT3G14420; GOX1`. So in this folder GLO1 = GOX1 = At3g14420.
- The two leaf genes are adjacent on chromosome 3 (At3g14415 and At3g14420) and the
  GOX1/GOX2 names are crossed in part of the literature:
  - Dellero et al. 2015 uses TAIR naming: [PMID:25416784 "Kinetic parameters of purified
    recombinant GOX1 (At3g14420) and GOX2 (At3g14415) from A. thaliana (the two GOX genes
    highly expressed in leaves)"].
  - Reumann et al. 2007 (leaf peroxisome proteome) uses the crossed naming:
    [PMID:17951448 "both isoforms of glycolate oxidase (GOX), GOX1 (At3g14415; PRL>) and GOX2
    (At3g14420; ARL>), were specifically identified"]. Here "GOX2" = our GLO1.
  - UniProt Q9LRS0 (GLO2, At3g14415) lists `Synonyms=GOX1`, reflecting the crossed usage.
  - Kerchev et al. 2016 (PMID:27225899) uses TAIR naming in its full text (GOX1 = At3g14420,
    GOX2 = At3g14415; checked on the PMC full text via WebFetch, not in the cached abstract).
- Always check the AGI locus, not the GOX number.

## Molecular function

- Glycolate oxidase (EC 1.1.3.15), an FMN-dependent (S)-2-hydroxy-acid oxidase:
  [file:ARATH/GLO1/GLO1-uniprot.txt "Catalyzes the oxidation of glycolate to glyoxylate, with a
  reduction of O2 to H2O2"]; kinetics from recombinant enzyme: Km 0.22 mM glycolate, kcat
  29.86 s-1 (UniProt, from PMID:25416784).
- Recombinant His-tagged AtGOX1 and AtGOX2 were purified and assayed with glycolate
  [PMID:25416784 "For each GOX tested, their catalytic activities were measured over a range of
  glycolate concentrations (0.1–10 m m ) at around 0.2 m m O 2 ."]; the study supports a hydride
  transfer mechanism [PMID:25416784 "Calculations of commitment factors from observed kinetic
  isotope effect values support a hydride transfer mechanism."].
- GO term: GO:0008891 glycolate oxidase activity is obsolete and replaced by GO:0003973
  (S)-2-hydroxy-acid oxidase activity (verified in OLS4, `term_replaced_by: GO_0003973`).
- Family: FMN-dependent alpha-hydroxy acid dehydrogenase family (PROSITE PS51349, Pfam
  PF01070, PANTHER PTHR10578:SF107); FMN binding residues by similarity to spinach GOX P05414.
- Class description [PMID:22303256 "Glycolate oxidase (GO, EC 1.1.3.15) belongs to the class of
  flavindependent 2-hydroxy acid oxidases and catalyzes the oxidation of glycolate to
  glyoxylate. Molecular oxygen is used as a co-substrate and, thus, H 2 O 2 is produced by the
  enzyme."].
- No experimental data found for GLO1 activity on L-lactate (that data, PMID:21828292, is for
  GOX2/At3g14415 only).

## Localization

- Peroxisome (UniProt by similarity); C-terminal PTS1 tripeptide ARL> per Reumann 2007, and the
  protein was detected in purified leaf peroxisomes [PMID:17951448].
- Detections in chloroplast, stroma, nucleus, plasmodesma, apoplast, cytosolic ribosome and
  cytosol proteomes are most likely carry-over of this very abundant leaf peroxisomal protein;
  the Arabidopsis cytosolic proteome (PMID:21166475) gave a NOT cytosol (RCA) annotation.

## Biological process

- Photorespiration (C2 cycle), glycolate -> glyoxylate step in the leaf peroxisome.
  [PMID:22303256 "Two of these genes (At3g14415 and At3g14420) are transcriptionally co-regulated
  with other photorespiratory genes"], and redundancy explained the lack of mutants in
  classical screens [PMID:22303256 "Probably because of this genetic redundancy, no mutants were
  identified in the classical Arabidopsis and barley screens"].
- GOX1 and GOX2 are redundant for photorespiration under normal conditions:
  [PMID:26896850 "We show that two Arabidopsis genes, GOX1 and GOX2, share a redundant
  photorespiratory role. Air-grown single gox1 and gox2 mutants grew normally"]; double
  knock-down [PMID:26896850 "Air-grown amiRgox1/2 plants with a residual 5% GOX activity exhibited
  a severe growth phenotype."].
- GOX1 is the more important isoform under high photorespiratory flux and in the cat2 background:
  [PMID:27225899 "we isolated a second-site loss-of-function mutation in GLYCOLATE OXIDASE1
  (GOX1) that attenuated the photorespiratory phenotype of cat2-2"] and [PMID:27225899 "the
  negative consequences of severe photorespiration were more pronounced in the absence of GOX1,
  which was accompanied with lesser ability to process glycolate."]
- Post-translational regulation: GOX1 S-nitrosylation at Cys-343 in cat2 [PMID:39777728 "We found
  that GOX1 is S-nitrosylated at Cys-343 during consecutive oxidative stress in the cat2 mutant."]
  (abstract only; locus mapping for "GOX1" not verified from the cached abstract).
- Ozone/photo-oxidative stress: a T-DNA line at the GOX1/GOX2 locus with ~60% GOX activity is
  ozone sensitive [PMID:28339978].
- Defence / H2O2 production: GOX-derived H2O2 contributes to nonhost resistance
  [PMID:22286136 "Arabidopsis gox mutants have lower H(2)O(2) accumulation, reduced callose
  deposition, and reduced electrolyte leakage upon inoculation with hypersensitive
  response-causing nonhost pathogens."]. Cached text is abstract-only; Kerchev 2016 full text
  states that gox1-1 and gox2-1 were described in Rojas et al. 2012, consistent with the GOA IMP
  rows on both genes. This is a secondary, non-core role of the H2O2 product.

## RNA binding

- Leaf RNA interactome capture lists "(S)-2-HYDROXY-ACID OXIDASE" among moonlighting enzymes
  [PMID:32344669 "Additional moonlighting enzymes were identified in the leaf RBPome, such as
  COBALAMIN-INDEPENDENT METHIONINE SYNTHASE, (S)-2-HYDROXY-ACID OXIDASE, GLYCINE DEHYDROGENASE
  and GLUTAMATE-GLYOXYLATE AMINOTRANSFERASE"]; no functional follow-up.

## Module comparison (modules/photorespiration_c2_cycle.yaml)

- Module: GO:0003973 MF, GO:0009853 photorespiration, GO:0005777 peroxisome. Review agrees on MF
  and location; for process the existing annotation is the more specific GO:0009854 oxidative
  photosynthetic carbon pathway (part_of GO:0009853), which is accepted here.
