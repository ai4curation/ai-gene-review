# MDH1 (P40925) review notes

Human cytosolic (NAD-dependent) malate dehydrogenase. UniProt entry MDHC_HUMAN,
334 aa, EC 1.1.1.37. Gene on chromosome 2p15.

## Core biology (from UniProt P40925)

- RecName: "Malate dehydrogenase, cytoplasmic"; EC=1.1.1.37; AltName "Aromatic
  alpha-keto acid reductase (KAR)"; AltName "Cytosolic malate dehydrogenase"
  [file:human/MDH1/MDH1-uniprot.txt].
- Primary catalytic reaction (RHEA:21432, EC 1.1.1.37):
  "Reaction=(S)-malate + NAD(+) = oxaloacetate + NADH + H(+)"
  [file:human/MDH1/MDH1-uniprot.txt]. This is the canonical MF and maps to
  GO:0030060 "L-malate dehydrogenase (NAD+) activity" (OLS: "Catalysis of the
  reaction: (S)-malate + NAD+ = oxaloacetate + NADH + H+").
- FUNCTION line: "Plays essential roles in the malate-aspartate shuttle and the
  tricarboxylic acid cycle, important in mitochondrial NADH supply for oxidative
  phosphorylation" [file:human/MDH1/MDH1-uniprot.txt].
- Also "Catalyzes the reduction of aromatic alpha-keto acids in the presence of
  NADH" — this is the historical "aromatic alpha-keto acid reductase (KAR)"
  activity, shown to be the same protein as cytosolic MDH
  [file:human/MDH1/MDH1-uniprot.txt; PMID:3052244].
- Additional promiscuous activity: "Catalyzes the reduction of 2-oxoglutarate to
  2-hydroxyglutarate, leading to elevated reactive oxygen species (ROS)"
  (PubMed:34012073) [file:human/MDH1/MDH1-uniprot.txt].
- SUBUNIT: "Homodimer" [file:human/MDH1/MDH1-uniprot.txt].
- SUBCELLULAR LOCATION: "Cytoplasm, cytosol" [file:human/MDH1/MDH1-uniprot.txt].
- SIMILARITY: "Belongs to the LDH/MDH superfamily. MDH type 2 family."
  [file:human/MDH1/MDH1-uniprot.txt].
- DISEASE: recessive Developmental and epileptic encephalopathy 88 (DEE88,
  MIM:618959) [file:human/MDH1/MDH1-uniprot.txt; PMID:31538237].

## Evidence for specific annotations

### GO:0030060 L-malate dehydrogenase (NAD+) activity — CORE MF
- EXP (PMID:3052244, Reactome/UniProt), IBA (GO_REF:0000033), IEA (RHEA/EC via
  GO_REF:0000120). All converge on the same catalytic activity.
- PMID:3052244 (abstract only; full_text_available: false) is the biochemical
  identity paper: it establishes human MDH-s = KAR and studies catalytic activity
  and the malate-inhibited reduction of aromatic alpha-keto acids. Abstract:
  "cytoplasmic malate dehydrogenase (MDH-s) from several non-human species
  catalyses the reduction of aromatic alpha-keto acids in the presence of NADH ...
  Here we present evidence that this also occurs in humans" [PMID:3052244]. This
  is the reference UniProt uses for EC=1.1.1.37 (ECO:0000269|PubMed:3052244), so
  the EXP annotation to GO:0030060 is well-founded.

### GO:0043490 malate-aspartate shuttle — CORE BP
- IBA (GO_REF:0000033), TAS (Reactome R-HSA-9856872), IMP (PMID:37647199).
- PMID:37647199 (abstract only): MAS-deficient HEK293 panel; "Among the
  MAS-deficient cells, those lacking malate dehydrogenase 1 (MDH1) show the most
  severe metabolic disruptions" [PMID:37647199] — direct genetic (IMP) support
  that MDH1 functions in the MAS.
- Reactome R-HSA-9856872 "Malate-aspartate shuttle" describes MDH1 reducing OA to
  malate as the cytosolic arm of the shuttle [reactome/R-HSA-9856872.md].
- UniProt FUNCTION: "essential roles in the malate-aspartate shuttle"
  [file:human/MDH1/MDH1-uniprot.txt].

### GO:0006099 tricarboxylic acid cycle — BP (non-core / borderline)
- IBA only. UniProt FUNCTION states MDH1 plays a role in "the tricarboxylic acid
  cycle" [file:human/MDH1/MDH1-uniprot.txt] and lists KW "Tricarboxylic acid
  cycle". However, the canonical TCA-cycle malate->OAA step is catalysed by the
  MITOCHONDRIAL isozyme MDH2; cytosolic MDH1 participates in the cytosolic arm of
  the MAS and gluconeogenesis rather than the mitochondrial TCA cycle proper.
  Keep as non-core (UniProt/IBA support it, so not removed).

### GO:0006108 malate / GO:0006107 oxaloacetate metabolic process — BP (parent terms)
- Broader parent terms of the catalytic activity; consistent but non-core (the
  specific MF + MAS terms capture the biology). Keep as non-core.

### GO:0005829 cytosol / GO:0005737 cytoplasm — CC CORE
- Multiple lines: IDA:HPA (GO_REF:0000052), IDA:ComplexPortal (PMID:34547241,
  cytoplasm), IBA, IEA(SubCell), TAS(Reactome/PMID:8786100).
- UniProt SUBCELLULAR LOCATION "Cytoplasm, cytosol" [file:human/MDH1/MDH1-uniprot.txt].

### GO:0019674 NAD+ / GO:0006739 NADP+ metabolic process — BP (IDA, ComplexPortal)
- PMID:34547241 (abstract only; full_text_available: false): describes a "hydride
  transfer complex (HTC) ... assembled by malate dehydrogenase 1, malic enzyme 1,
  and cytosolic pyruvate carboxylase" that "reprograms NAD metabolism by
  transferring reducing equivalents from NADH to NADP+" [PMID:34547241]. The
  ComplexPortal IDA annotations (GO:0019674 NAD+ met; GO:0006739 NADP+ met;
  GO:0005737 cytoplasm) derive from MDH1's role in this complex. Legitimate but
  represents a specialized cancer/senescence-bypass context; keep as non-core.

### GO:0005515 protein binding (IPI, PMID:21044950)
- PMID:21044950 = genome-wide split-YFP (BiFC) screen for telomere-signaling
  regulators; MDH1 was picked up as associating with a core telomere protein
  (TERF1/P54274; matches UniProt INTERACTION line "P40925; P54274: TERF1")
  [file:human/MDH1/MDH1-uniprot.txt]. Bare "protein binding" is uninformative and
  the biological meaning of an MDH1-TERF1 BiFC hit is unclear. Per policy, an IPI
  protein-binding annotation is NOT removed -> MARK_AS_OVER_ANNOTATED.

### GO:0004470 malic enzyme activity (TAS, PMID:8786100) — MISANNOTATION
- GO:0004470 is "Catalysis of the oxidative decarboxylation of malate with the
  concomitant production of pyruvate" (OLS) — this is malic enzyme (ME1, EC
  1.1.1.40), a DIFFERENT enzyme. MDH1 does not decarboxylate malate to pyruvate;
  it oxidises malate to oxaloacetate (EC 1.1.1.37).
- The cited paper PMID:8786100 (abstract only) is only a cloning/mapping study:
  "We have isolated a human cDNA encoding a protein of 334 amino acids that shows
  96% identity ... to murine cytosolic malate dehydrogenase" [PMID:8786100]; it
  does NOT report malic enzyme activity. TAS (not experimental) -> MODIFY to the
  correct MF GO:0030060.

### GO:0047545 (S)-2-hydroxyglutarate dehydrogenase / GO:0047995
  (2R)-hydroxyphenylpyruvate reductase — promiscuous MF (IEA/EXP)
- These are RHEA/EC-mapping (IEA) and one EXP (PMID:3052244 for the aromatic
  alpha-keto acid / hydroxyphenylpyruvate reductase side activity) annotations for
  documented moonlighting/promiscuous activities of MDH1 (UniProt lists the
  corresponding CATALYTIC ACTIVITY blocks). Real but non-core side reactions; keep
  as non-core (the 2-hydroxyglutarate activity is the alpha-KG reduction reported
  in PubMed:34012073).

### Generic parent MF terms (IEA, InterPro)
- GO:0003824 catalytic activity, GO:0016491 oxidoreductase activity, GO:0016615
  malate dehydrogenase activity, GO:0016616 oxidoreductase acting on CH-OH/NAD(P):
  all correct but generic parents of GO:0030060. MARK_AS_OVER_ANNOTATED (redundant
  with the specific EXP/IBA MF).

### Extracellular localizations (HDA)
- GO:0070062 extracellular exosome (PMID:23533145 prostatic-secretion exosomes;
  PMID:19056867 urinary exosomes), GO:0005576 extracellular region (PMID:22664934
  breast-cancer tear proteome). All high-throughput proteomic detections of a
  cytosolic housekeeping enzyme in body fluids/exosomes; PMID:22664934 explicitly
  mentions "MDH1 in glycolysis and the citric acid cycle" as detected in tears
  [PMID:22664934]. These reflect passive presence of an abundant cytosolic protein
  in secreted vesicles, not a functional extracellular role. HDA (not experimental)
  -> MARK_AS_OVER_ANNOTATED (do not remove; consistent with common exosome/body-fluid
  proteomics for cytosolic enzymes).

## Summary of core functions
- MF: GO:0030060 L-malate dehydrogenase (NAD+) activity (EC 1.1.1.37)
- BP: GO:0043490 malate-aspartate shuttle
- CC: GO:0005829 cytosol
