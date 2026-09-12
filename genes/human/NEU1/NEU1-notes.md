# NEU1 (Sialidase-1 / lysosomal neuraminidase) — review notes

UniProt: Q99519 (NEUR1_HUMAN). Gene: NEU1 (synonym NANH). HGNC:7758. EC 3.2.1.18.
Taxon: Homo sapiens (NCBITaxon:9606). 415 aa precursor; signal peptide 1-47, mature chain 48-415.

## Core biology (from UniProt Q99519, `file:human/NEU1/NEU1-uniprot.txt`)

- FUNCTION: "Lysosomal exo-alpha-sialidase that catalyzes the removal of sialic acid
  (N-acetylneuraminic acid) moieties from glycoproteins and glycolipids. To be active,
  it is strictly dependent on its presence in the multienzyme complex ... Appears to
  have a preference for alpha 2-3 and alpha 2-6 sialyl linkage."
  [file:human/NEU1/NEU1-uniprot.txt]
- CATALYTIC ACTIVITY (EC 3.2.1.18): "Hydrolysis of alpha-(2->3)-, alpha-(2->6)-,
  alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides,
  glycoproteins, glycolipids, colominic acid and synthetic substrates."
  [file:human/NEU1/NEU1-uniprot.txt]
- SUBUNIT: "Homooligomer. Interacts with cathepsin A/CTSA; activates the exo-alpha-sialidase
  activity. Interacts with cathepsin A/CTSA (protective protein), beta-galactosidase and
  N-acetylgalactosamine-6-sulfate sulfatase in a multienzyme complex."
  [file:human/NEU1/NEU1-uniprot.txt]
- SUBCELLULAR LOCATION: "Lysosome lumen. Lysosome membrane; Peripheral membrane protein;
  Lumenal side. Cell membrane; Peripheral membrane protein. Note=Localized not only on the
  inner side of the lysosomal membrane and in the lysosomal lumen, but also on the plasma
  membrane and in intracellular vesicles." [file:human/NEU1/NEU1-uniprot.txt]
- SIMILARITY: "Belongs to the glycosyl hydrolase 33 family." (GH33; six-bladed
  beta-propeller). [file:human/NEU1/NEU1-uniprot.txt]
- DISEASE: Sialidosis (MIM:256550), a lysosomal storage disease; type 1 (cherry-red
  spot/myoclonus, late-onset) and type 2 (dysmorphic, severe/early-onset). NEU1 loss also
  underlies galactosialidosis phenotypes via CTSA deficiency. [file:human/NEU1/NEU1-uniprot.txt]

## Key experimental references (cached)

### PMID:8985184 (Bonten et al. 1996, Genes Dev) — abstract only (full_text_available: false)
Original cloning/characterization of human lysosomal neuraminidase. Establishes: enzyme
"occurs in complex with beta-galactosidase and protective protein/cathepsin A (PPCA)";
"deficient in ... sialidosis ... and galactosialidosis"; "the enzyme is compartmentalized
in lysosomes and restored neuraminidase activity in a PPCA-dependent manner"; three
sialidosis mutations identified. [PMID:8985184 "the enzyme is compartmentalized in
lysosomes and restored neuraminidase activity in a PPCA-dependent manner"]. GOA uses this
paper for exo-alpha-sialidase activity (IDA), lysosome (IDA), and oligosaccharide catabolic
process (IMP).

### PMID:37205763 (Gorelik et al. 2023, Sci Adv) — full text
Crystal structure of murine NEU1 (86% identity to human); all point/enzymatic assays done
on the human homolog. Confirms: "NEU1 removes terminal sialic acid residues from glycans
on lysosomal degradation products and on cell surface proteins"; six-bladed beta-propeller
GH33 fold; "NEU1 is unique among all known ... sialidases, as it requires an accessory
protein for activity — the protective protein cathepsin A (CTSA; PPCA)"; "NEU1 and CTSA,
along with beta-galactosidase (GLB1), form a megadalton-sized lysosomal multienzyme
complex." Human active-site mutants (Asp103, His220, Asp263) lose activity; CTSA activates
~150-fold. GOA uses this for exo-alpha-sialidase activity (IDA). [PMID:37205763 "NEU1
removes terminal sialic acid residues from glycans on lysosomal degradation products and
on cell surface proteins"]

### PMID:25153125 (Bonardi et al. 2014, PLoS ONE) — full text
Population-variant + functional study. Confirms "Sialidases (EC 3.2.1.18) are a family of
glycohydrolitic enzymes that remove the terminal sialic acid from oligosaccharide chains";
"the lysosomal NEU1"; "The association of NEU1 with PPCA ... is essential for the correct
trafficking to lysosomes, where the sialidase enzyme is processed to its active form."
Two novel variants (V217A, D234N) reduce sialidase activity and alter subcellular
localization. GOA uses this for exo-alpha-sialidase activity (IMP) and lysosome (IMP,
is_active_in). [PMID:25153125 "remove the terminal sialic acid from oligosaccharide chains"]

### PMID:27917893 (Maurice et al. 2016, Sci Rep) — full text
Proposes two putative transmembrane segments (139-159, 316-333) and plasma-membrane NEU1
dimerization. "Neuraminidase 1 (NEU1) is a lysosomal sialidase catalyzing the removal of
terminal sialic acids from sialyloconjugates. A plasma membrane-bound NEU1 modulating a
plethora of receptors by desialylation, has been consistently documented." GOA uses this
for lysosomal membrane (IDA) and plasma membrane (IDA). NOTE: the later crystal structure
(PMID:37205763) argues the mature enzyme is NOT transmembrane ("crystal structure is
therefore incompatible with a transmembrane arrangement of the mature, functional enzyme"),
but plasma-membrane/cell-surface localization of NEU1 is independently well supported.

## Interaction (IPI) annotations — bare "protein binding" (GO:0005515)
- PMID:25910212 (Sahni et al. 2015) — "Widespread macromolecular interaction perturbations
  in human genetic disorders" (Y2H-based disease-variant interactome). One IPI vs CREB3
  (O43889-2).
- PMID:32296183 (Luck et al. 2020) — "A reference map of the human binary protein
  interactome" (HuRI; systematic Y2H). ~18 IPI partners (AQP6, CD79A, CERS3/4, EBP,
  ERGIC3, GOLM1, GPR152, GPX8, HSD17B11, MGST3, MUC1, SLC10A1/6, SLC18A1, SLC39A9,
  TMEM14B, CREB3L1). These are high-throughput binary-interactome hits; almost all
  partners are unrelated ER/Golgi/membrane proteins with no established NEU1 biology,
  and none capture the biologically meaningful CTSA/GLB1 multienzyme-complex interaction.
  Bare "protein binding" is uninformative for MF; policy = MARK_AS_OVER_ANNOTATED (IPI,
  never REMOVE).

## Location annotations — assessment
- Lysosome (GO:0005764) / lysosomal lumen (GO:0043202) / lysosomal membrane (GO:0005765):
  core, well supported (UniProt, Reactome, IDA/IMP). ACCEPT/KEEP.
- Plasma membrane (GO:0005886) / cell membrane: supported (IDA PMID:27917893; UniProt
  Cell membrane). Real but non-core relative to the lysosomal catabolic role. KEEP_AS_NON_CORE.
- Cytoplasm (GO:0005737, IBA): NEU1 is a lysosomal/membrane sialidase, not cytosolic
  (the cytosolic mammalian sialidase is NEU2). IBA "cytoplasm" is a broad/imprecise
  propagation; cytoplasm technically includes the lysosome but is uninformative and
  potentially misleading here. MARK_AS_OVER_ANNOTATED.
- Membrane (GO:0016020, IBA): correct but uninformatively general (better captured by
  lysosomal membrane / plasma membrane). KEEP_AS_NON_CORE.
- Extracellular region (GO:0005576, TAS Reactome; neutrophil degranulation) and specific
  granule lumen (GO:0035580, TAS): reflect NEU1 as cargo of neutrophil specific granules
  released on degranulation. Real but peripheral to core lysosomal function. KEEP_AS_NON_CORE.
- Extracellular exosome (GO:0070062, HDA PMID:23533145, PMID:19199708): high-throughput
  proteomic detection in exosomes/secretions; typical HDA over-detection, not a functional
  site. MARK_AS_OVER_ANNOTATED.
- Cell junction (GO:0030054, IDA HPA / GO_REF:0000052): single HPA immunofluorescence
  localization; not corroborated as a functional NEU1 site. MARK_AS_OVER_ANNOTATED.

## Function annotations — assessment
- exo-alpha-sialidase activity (GO:0004308): CORE MF. Multiple lines: IDA (PMID:8985184,
  PMID:37205763), IMP (PMID:25153125), IBA, TAS Reactome, IEA. ACCEPT the experimental
  ones as core.
- oligosaccharide catabolic process (GO:0009313, IMP PMID:8985184 + IBA): core BP; NEU1
  removes terminal sialic acid from oligosaccharide chains as the committed step of glycan
  catabolism. ACCEPT.
- ganglioside catabolic process (GO:0006689, IBA): NEU1 also desialylates gangliosides
  (Reactome R-HSA-1605724 GM3->LacCer; UniProt "glycolipids"). Real contribution but note
  ganglioside sialidase activity in vivo is predominantly NEU3/NEU4; KEEP_AS_NON_CORE.

## Proposed additions (not in GOA)
- N-acetylneuraminate catabolic process (GO:0019262) and/or glycoprotein catabolic process
  (GO:0006516) — better capture the committed desialylation step; noted in core_functions.
- Cellular role: part of lysosomal multienzyme complex with CTSA + GLB1 (interaction well
  documented; no single "in_complex" GO term is asserted here as a strict core-function id).

## Validation
`just validate human NEU1` — see below in review process.
