# DUT (human) — curation notes

UniProt: P33316 (DUT_HUMAN). HGNC:3078. EC 3.6.1.23. Deoxyuridine 5'-triphosphate
nucleotidohydrolase (dUTPase / dUTP pyrophosphatase). NCBI taxon 9606.

Deep research provider note: falcon deep research was NOT run for this gene (falcon
API is out of credits / HTTP 402). No `-deep-research-falcon.md` file exists. This
review is grounded in the cached UniProt record (`DUT-uniprot.txt`), the seeded GOA
(`DUT-goa.tsv`), the cached `publications/PMID_*.md` entries, and the cached Reactome
entry `reactome/R-HSA-73666.md`.

## Core biology

dUTPase hydrolyses dUTP to dUMP + inorganic diphosphate (Mg2+-dependent). It has a
dual role:
1. Keeps the cellular dUTP:dTTP ratio low, preventing uracil misincorporation into
   DNA and the resulting futile base-excision-repair cycles / DNA strand breaks
   ("thymine-less" DNA damage).
2. Produces dUMP, the substrate that thymidylate synthase (TYMS) methylates to dTMP
   in de novo thymidylate biosynthesis.

Reaction (UniProt/RHEA:10248): dUTP + H2O = dUMP + diphosphate + H(+); EC 3.6.1.23.
Cofactor Mg2+ (PubMed:8805593). Enzyme is a homotrimer; active sites are formed at
subunit interfaces, with residues from all three subunits contributing to catalysis
(PubMed:8805593, PubMed:17880943).

- [PMID:8805593 "dUTPase hydrolyzes dUTP to dUMP and pyrophosphate, simultaneously
  reducing dUTP levels and providing the dUMP for dTTP biosynthesis. A high cellular
  dTTP: dUTP ratio is essential to avoid uracil incorporation into DNA, which would
  lead to strand breaks and cell death."]
- [PMID:8805593 "the first detailed atomic-resolution structure of a eukaryotic
  dUTPase, human dUTPase" — X-ray structure, Mg2+, homotrimer, uracil recognition]
- [PMID:17880943 "Human dUTPase, essential for DNA integrity, is an important survival
  factor for cancer cells. We determined the crystal structure of the
  enzyme:alpha,beta-imino-dUTP:Mg complex" — catalytic mechanism, C-terminus role]
- Reactome R-HSA-73666: "Deoxyuridine triphosphatase (DUT) catalyzes the hydrolysis
  of dUTP to form dUMP and pyrophosphate ... this reaction depletes the supply of
  dUTP, preventing its incorporation into DNA, while generating dUMP, the immediate
  precursor of thymidine nucleotides."

## Isoforms and localization

Two isoforms from alternative splicing of the N-terminus (UniProt):
- Isoform 2 (DUT-N, P33316-2): nuclear; major isoform; cell-cycle regulated (onset of
  DNA replication); phosphorylated on Ser-11 by CDK.
- Isoform 3 (DUT-M, P33316-3, displayed sequence): mitochondrial (N-terminal transit
  peptide 1-69); constitutively expressed.
- [PMID:8631816 "the lower molecular weight form of dUTPase (DUT-N) is associated
  with the nucleus, while the higher molecular weight species (DUT-M) fractionates
  with the mitochondria."] Both forms have identical dUTP binding (KM ~2.5 uM).
- [PMID:9070952] — DUT gene assigned to 15q15-q21.1; abstract-only cache, but UniProt
  cites it for subcellular location (nucleus + mitochondrion) of the two isoforms.

Note: the GOA/UniProt record for P33316 is annotated on the mitochondrial precursor
(isoform 3) as the canonical/displayed sequence, but the protein product is the same
enzyme; nuclear + mitochondrial localization is well established for the two isoforms.

## dTMP-biosynthesis / TYMS-inhibitor context (dUMP supply + uracil-avoidance)

- [PMID:10952785 "dUTPase catalyses the hydrolysis of dUTP to dUMP, thereby
  maintaining low intracellular dUTP." Relates dUTPase expression to sensitivity to
  the TS inhibitor ZD9331 in human lung tumour cell lines.] (acts_upstream_of_or_within
  / involved_in dTMP biosynthetic process — dUTPase is upstream of TYMS by supplying
  dUMP and by preventing uracil misincorporation when dTTP is low.)
- [PMID:15322254 "dUTPase, which eliminates dUTP from the DNA biosynthetic pathway,
  opposes uracil misincorporation" — siRNA knockdown of dUTPase sensitizes cancer
  cells to the TS inhibitor FUdR (IMP).]

## Non-core / moonlighting / high-throughput annotations

- RNA binding (GO:0003723, HDA, PMID:22658674): dUTPase captured in a HeLa mRNA
  interactome ("interactome capture") screen. Not a characterized function; treat as
  non-core moonlighting.
- protein binding (GO:0005515, IPI x2, PMID:16189514 + PMID:19060904, both IntAct,
  with NUDT18/Q6ZVK8): high-throughput Y2H interactome maps. Uninformative "protein
  binding"; mark over-annotated (per policy: do not REMOVE experimental IPIs).
- extracellular exosome (GO:0070062, HDA, PMID:20458337): B-cell exosome proteome MS
  survey; dUTPase not a functional exosome component. Non-core.
- PPAR-related Ensembl-projected terms (GO:0030547 signaling receptor inhibitor
  activity; GO:0042975 PPAR binding; GO:0043254 regulation of protein-containing
  complex assembly; GO:0001889 liver development; GO:0032556 pyrimidine
  deoxyribonucleotide binding; GO:0042802 identical protein binding): all GO_REF:0000107
  IEA transferred from rat ortholog P70583. UniProt records a "By similarity" PPAR
  inhibition moonlighting function ("Inhibits peroxisome proliferator-activated receptor
  (PPAR) activity by binding of its N-terminal to PPAR"). These are peripheral /
  ortholog-projected; not the core enzymatic function. identical protein binding is a
  correct correlate of homotrimer formation but uninformative.

## Disease

Biallelic DUT variants cause bone marrow failure and diabetes mellitus syndrome
(BMFDMS; MIM 620044) — variants Y142C, R173W, Y227C (UniProt; PubMed:28073829,
35931051, 35611808). Consistent with dUTPase being essential for genome integrity /
nucleotide metabolism.

## Core function summary

MF: GO:0004170 dUTP diphosphatase activity (with GO:0000287 magnesium ion binding).
BP: dUTP catabolism (GO:0046081) coupled to dUMP biosynthesis (GO:0006226), feeding
    de novo dTMP biosynthesis (GO:0006231) and preventing uracil misincorporation.
CC: cytosol (GO:0005829) / nucleus (GO:0005634) and mitochondrion (GO:0005739).
