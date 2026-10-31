# Mki67 (mouse, UniProtKB:E9PVX6) - manual literature synthesis

No deep-research API was available in this session, so this summary was assembled by
hand from cached publications in `publications/` and the UniProt record. Every claim
carries its source.

## Identity

- Mouse Ki-67 antigen (KI67_MOUSE, E9PVX6), 3177 aa, MGI:106035, GeneID 17345.
- Cloned as TSG126; contains tandem "Ki-67 repeats" (13 in the original clone)
  [PMID:8834799 "The murine Ki-67 cDNA sequence (TSG126) was found to contain 13 tandem repeats, making up more than half of the total protein size."].
- Conserved elements: N-terminal FHA domain, PP1-binding motif, conserved domain (CD),
  Ki-67 repeats, leucine/arginine-rich C-terminus that binds DNA
  [PMID:26949251 "All homologues contain an N-terminal Forkhead-associated (FHA) domain, which can bind both to DNA and to phosphorylated epitopes."].

## Localisation through the cell cycle

- Accumulates from late G1; granules throughout the nucleus, then foci overlapping
  nucleoli and heterochromatin in S/G2; at mitosis relocates to the surface of
  condensed chromosomes [PMID:8834799 "At the onset of mitosis the TSG126 protein undergoes a dramatic redistribution process and becomes associated with the surface of the condensed chromosomes."].
- In mouse meiosis it colocalises with centromeric heterochromatin and nucleoli in
  zygotene/pachytene and with the perichromosomal layer from late diplotene
  [PMID:12355204 "In the zygotene and pachytene stages, most of the pKi-67 colocalized with centromeric (centric and pericentric) heterochromatin and adjacent nucleoli"].
- In early embryos it decorates prophase chromosomes and later nucleolus precursor
  bodies / nucleoli [PMID:15237214 "during mitosis the protein was found covering the chromosome arms as a constituent of the perichromosomal layer"].

## Function

1. **Mitotic chromosome periphery organiser.** In human cells Ki-67 is required to
   assemble the perichromosomal compartment and is a PP1-binding protein
   [PMID:24867636 "we report that the nucleolar protein Ki-67 is required for the assembly of the perichromosomal compartment in human cells"].
2. **Surfactant that keeps mitotic chromosomes individualised.** Ki-67 prevents
   chromosomes collapsing into one mass after nuclear envelope breakdown; shown in HeLa,
   RPE1 and mouse embryonic stem cells
   [PMID:27362226 "We imaged mitosis in HeLa, non-cancer hTERT-RPE1 cells, and mouse embryonic stem cells depleted of Ki-67."]
   [PMID:27362226 "prevents chromosomes from collapsing into a single chromatin mass after nuclear envelope disassembly, thus enabling independent chromosome motility and efficient interactions with the mitotic spindle"].
3. **Chromosome clustering at mitotic exit.** The brushes collapse in anaphase and
   Ki-67 promotes chromosome clustering, excluding cytoplasm (ribosomes) from the
   reforming nucleus (HeLa) [PMID:32879492 "during mitotic exit the brushes collapse and Ki-67 promotes chromosome clustering"].
   In mouse models, PP2A-B55 counteracts Ki-67-dependent individualization
   [PMID:39003739 "In the absence of PP2A-B55 activity, mitotic cells display increased chromosome individualization in the presence of enhanced phosphorylation and perichromosomal loading of Ki-67."].
4. **Heterochromatin organisation in interphase.** Mouse genetic and knockdown work
   [PMID:26949251 "Ki-67 silencing also had wide-ranging effects on chromatin organisation, disrupting heterochromatin compaction and long-range genomic interactions."]
   [PMID:26949251 "overexpression of human or Xenopus Ki-67 induced ectopic heterochromatin formation"].

## Not required for proliferation

- [PMID:26949251 "Altering Ki-67 expression levels did not significantly affect cell proliferation in vivo."]
- [PMID:26949251 "Ki-67 mutant mice developed normally and cells lacking Ki-67 proliferated efficiently."]
- [PMID:26949251 "We find that mutant mice with disrupted Ki-67 expression are viable and fertile."]

## Marker usage (relevant to GOA)

Most MGI rows for Mki67 come from papers that used anti-Ki-67 immunostaining as a
proliferation read-out while studying another gene, e.g. Ezh2
[PMID:19303854 "In the absence of Ezh2, basal epidermal cells were less proliferative, exhibiting reductions in Ki67(+) cells and BrdU labeling (Figures 3D–3F)."].
These establish nuclear localisation of Ki-67 but say nothing about Ki-67 taking part
in proliferation. PMID:20097747 (a rat myocardial-infarction study) likewise uses Ki-67
only as a cycling-cell marker
[PMID:20097747 "Cycling cells were identified with an antibody against nuclear transcription factor Ki-67."]
(its description of Ki-67 as a "transcription factor" is incorrect).
