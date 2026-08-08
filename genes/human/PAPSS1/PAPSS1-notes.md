# PAPSS1 (Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 1) — review notes

UniProt: O43252 (PAPS1_HUMAN). Gene: PAPSS1 (synonyms ATPSK1, PAPSS). Human, NCBITaxon:9606.

## Summary of function

PAPSS1 is a cytosolic and nuclear **bifunctional enzyme** that synthesizes PAPS (3'-phosphoadenosine
5'-phosphosulfate), the universal activated sulfate donor for all cytosolic and Golgi sulfotransferases.
Two catalytic domains act sequentially in the sulfate-activation pathway:

1. **ATP sulfurylase / sulfate adenylyltransferase (ATP) domain** (C-terminal, residues ~234–624):
   sulfate + ATP + H(+) -> adenosine 5'-phosphosulfate (APS) + diphosphate (EC 2.7.7.4).
2. **APS kinase / adenylyl-sulfate kinase domain** (N-terminal, residues 1–225):
   APS + ATP -> 3'-phosphoadenylyl sulfate (PAPS) + ADP + H(+) (EC 2.7.1.25).

[file:human/PAPSS1/PAPSS1-uniprot.txt "Bifunctional enzyme with both ATP sulfurylase and APS kinase
activity, which mediates two steps in the sulfate activation pathway."]
[file:human/PAPSS1/PAPSS1-uniprot.txt "In mammals, PAPS is the sole source of sulfate; APS appears to be only an intermediate in the sulfate-activation pathway"]

Domain assignment and boundaries from UniProt FT REGION:
- REGION 1..225 "Adenylyl-sulfate kinase"
- REGION 234..624 "Sulfate adenylyltransferase"
[file:human/PAPSS1/PAPSS1-uniprot.txt]

Note the domain order in the primary sequence is unusual for the animal fusion: the **APS kinase**
domain is N-terminal and the **ATP sulfurylase** domain is C-terminal
[PMID:9648242 "The enzyme contains an APS kinase domain in its N-terminal portion and an ATP sulfurylase domain in its C-terminal portion."]
[PMID:9668121 "A 1-268-amino acid fragment expressed APS kinase activity, whereas a 220-623 fragment evinced ATP sulfurylase activity."]

## Catalytic activity (verbatim, UniProt)

- [file:human/PAPSS1/PAPSS1-uniprot.txt "Reaction=sulfate + ATP + H(+) = adenosine 5'-phosphosulfate +"] (EC 2.7.7.4, RHEA:18133)
- [file:human/PAPSS1/PAPSS1-uniprot.txt "Reaction=adenosine 5'-phosphosulfate + ATP = 3'-phosphoadenylyl sulfate"] (EC 2.7.1.25, RHEA:24152)

## Pathway

Sulfur metabolism; sulfate assimilation. UniProt PATHWAY + UniPathway UPA00097.
[file:human/PAPSS1/PAPSS1-uniprot.txt "Sulfur metabolism; sulfate assimilation."]

PAPS is the sole physiological sulfonate donor; it feeds sulfation of glycosaminoglycans/proteoglycans,
sulfomucins, steroids, tyrosine, neurotransmitters, hormones, drugs and xenobiotics.
[PMID:9576487 "suggesting that human PAPS synthetase may be important for sulfation not only of HEV sialomucins, but also of many other molecules, including mucins such as the P-selectin ligand PSGL-1, proteoglycans, hormones, neurotransmitters, drugs, and xenobiotics."]

## Biochemical / structural evidence

- Both activities and PAPS synthesis demonstrated on the recombinant human enzyme
  [PMID:9576487 "Functional expression of the isolated cDNA in Chinese hamster ovary cells results in high levels of PAPS synthesis, which is abolished by treatment of the transfected cells with chlorate."]
- Recombinant full-length and each isolated domain shown to carry their respective activities
  [PMID:9648242 "Recombinant full-length enzyme and its constituent APS kinase and ATP sulfurylase domains were individually expressed, purified, and shown to have their respective enzymatic activities."]
- Full-length enzyme is a homodimer and is catalytically active (25 nmol PAPS/min/mg)
  [PMID:14747722 "The pure protein migrates as a dimer in gel-filtration chromatography. It is moderately active, forming 25 nmol PAPS per minute per milligram."]
  UniProt SUBUNIT: [file:human/PAPSS1/PAPSS1-uniprot.txt "Homodimer."]
- APS kinase domain crystal structures (Michaelis complex with ADP-Mg + PAPS; APS-bound)
  [PMID:17276460 "The former reaction is catalyzed by the ATP-sulfurylase domain and the latter by the APS-kinase domain."]
- APS kinase is uncompetitively substrate-inhibited by APS; N-terminal residues R37/R40 mediate this
  [PMID:17540769 "The substrate APS acts as a strong uncompetitive inhibitor of the APS kinase reaction."]
  UniProt DOMAIN: [file:human/PAPSS1/PAPSS1-uniprot.txt "The N-terminal first 50 residues are required for inhibition by"]
- ATP-sulfurylase HXGH motif (His425/His428) is essential; H425A and H428A abolish activity
  (UniProt MUTAGEN, PMID:9915785).

## Subcellular localization

- Both cytosol and nucleus, experimentally (dynamic shuttling)
  [PMID:22242175 title "Human PAPS synthase isoforms are dynamically regulated enzymes with access to nucleus and cytoplasm."]
- PAPSS1 accumulates in the nucleus; nuclear targeting mediated by the APS kinase domain and an
  N-terminal 21-aa sequence
  [PMID:10657990 "human PAPS synthetase 1 (PAPSS1), a bifunctional ATP sulfurylase/adenosine 5'-phosphosulfate (APS) kinase enzyme sufficient for PAPS synthesis, accumulates in the nucleus of mammalian cells."]
  [PMID:10657990 "Nuclear targeting of the enzyme is mediated by its APS kinase domain and requires a catalytically dispensable 21 amino acid sequence at the amino terminus."]

## Tissue specificity

Wide distribution; testis, pancreas, kidney, thymus, prostate, ovary, intestine, colon, leukocytes,
liver; also HEV cells and cartilage.
[file:human/PAPSS1/PAPSS1-uniprot.txt "Expressed in testis, pancreas, kidney, thymus,"]

## Notes on specific annotations

- **GO:0001501 skeletal system development (TAS, PMID:9771708)** — This reference is about the *paralog*
  PAPSS2 / ATPSK2 (the human SEMD and mouse brachymorphic gene), not PAPSS1. The paper maps SEMD to
  chromosome 10q23-24 and identifies mutations in ATPSK2/Atpsk2.
  [PMID:9771708 "We identified two orthologous genes, ATPSK2 and Atpsk2, encoding novel ATP sulfurylase/APS kinase orthologues in the respective regions of the human and mouse genomes."]
  The skeletal/cartilage phenotype is the PAPSS2 (chondrocyte-restricted) function; PAPSS1 is broadly
  expressed. This is a non-experimental (TAS) annotation attributed to PAPSS1 but the cited paper does
  not concern PAPSS1 — treated as over-annotation / mis-attribution (kept non-core, flagged), not a
  core PAPSS1 function.

- **GO:0005515 protein binding (IPI, PMID:33961781)** — BioPlex 3.0 high-throughput AP-MS interactome;
  the with/from is PAPSS2 (O95340), consistent with UniProt's recorded PAPSS1–PAPSS2 IntAct interaction.
  Uninformative bare "protein binding" — marked over-annotated (per policy, IPI protein binding is not
  removed).

- **GO:0042803 protein homodimerization activity (IPI, PMID:14747722)** — supported by the homodimer
  observed in gel filtration and crystal structures. Real structural property; kept as non-core (the
  homodimer is the biological unit but the catalytic MFs are the core functions).

- **GO:0016779 nucleotidyltransferase activity (ISS)** — a less-specific parent of the ATP sulfurylase
  (sulfate adenylyltransferase) activity GO:0004781; MODIFY -> GO:0004781.

- **Reactome cytosol annotations R-HSA-6802927/32/33/34/35** — these are "Signaling by BRAF and RAF1
  fusions" pathway reactions; the cytosol location is correct for PAPSS1 but the BRAF/RAF-fusion
  pathway context is spurious co-occurrence (PAPSS1 is not a component of RAF signaling). Location kept
  non-core.

## Core functions (for review)

- MF: sulfate adenylyltransferase (ATP) activity — GO:0004781
- MF: adenylylsulfate kinase activity — GO:0004020
- MF: ATP binding — GO:0005524 (both catalytic reactions consume ATP; UniProt BINDING sites for two
  ATP molecules, labels 1 and 2)
- BP: sulfate assimilation — GO:0000103 / 3'-phosphoadenosine 5'-phosphosulfate biosynthetic process — GO:0050428
- CC: cytosol — GO:0005829; nucleus — GO:0005634
</content>
</invoke>
