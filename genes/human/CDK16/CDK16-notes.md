# CDK16 (PCTAIRE-1, PCTK1) — human, UniProt Q00536

## Session log

### 2026-10-21 — initial review

- `just fetch-gene human CDK16` created the UniProt, GOA (65 rows) and stub files.
- `just deep-research human CDK16 --provider falcon` FAILED: the Edison/falcon client
  exited with `Exception: Failed to authenticate` ("All providers failed"). No
  deep-research file was produced; this review is built from the cached publications
  listed below, the UniProt record and PANTHER/PAINT data.
- `just fetch-gene-pmids human CDK16` cached all 16 GOA-cited PMIDs. A further set of
  CDK16 papers was already cached in `publications/` and was read here.
- Context: this review is the experimentally characterised comparator for the blue/minke
  whale CDK16 model `genes/BALMU/A0A8B8WEG2`, which is placed in the same PANTHER
  subfamily (PTHR24056:SF174, CYCLIN-DEPENDENT KINASE 16).

## What is experimentally established, and in which species

### Human protein (direct evidence)

- Ser/Thr protein kinase activity of recombinant and endogenous human PCTAIRE-1; optimal
  motif needs Pro at +1 and a basic residue at +4; cyclin Y binding increases activity
  >100-fold [PMID:22796189 "Here we demonstrate that binding of PCTAIRE-1 to cyclin Y
  increases (> 100-fold) PCTAIRE-1 activity towards PCTAIRE-tide."].
- Cyclin Y recruits CDK16 to the plasma membrane in human cells; S153 phosphorylation
  (PKA site) blocks CCNY binding [PMID:22184064 "a fraction of CDK16-GFP was recruited to
  the plasma membrane"].
- Activation requires cyclin Y phosphorylated at S100/S326 bound to 14-3-3
  [PMID:26205494 "activation of PCTAIRE-1, which is mediated through interaction with the
  phosphorylated form of cyclin Y in complex with 14-3-3"]; the cryo-EM structure shows
  CDK16 contacting the CCNY cyclin box and 14-3-3 [PMID:41857027 "CDK16 interacts with
  the cyclin box of CCNY, while 14-3-3 provides additional contacts, including with the
  activation segment of CDK16."].
- Crystal structures of the isolated kinase domain with inhibitors [PMID:28057719].
- Substrates in human cells: p27 Ser10 [PMID:25205104 "In vitro kinase assays showed
  PCTAIRE1 phosphorylates p27 at Ser10."], PRC1 Thr481 [PMID:30992425 "we identified
  PRC1 as the first substrate of the CDK16/CCNY complex"], CCNY Ser336 [PMID:26205494].
- AMPK phosphorylates CCNY S326 to promote CCNY-CDK16 activation; CCNY/CDK16 is
  sufficient to promote autophagy in cells [PMID:32098961 "When expressed in cells,
  Cyclin Y/CDK16 is sufficient to promote autophagy."].
- Cytoplasmic localisation [PMID:10511311 "Indirect immunofluorescence indicated that
  PCTAIRE-1 exhibits cytoplasmic distribution throughout the cell cycle."].
- Direct interaction with the COPII subunit SEC23A; depletion or kinase-dead expression
  impairs ER-to-Golgi cargo transport [PMID:16091426].
- Proliferation/mitosis role is cancer-cell specific [PMID:25205104 "PCTAIRE1 was not
  similarly involved in proliferation of nontransformed cells"].
- Candidate X-linked intellectual disability gene, not confirmed [PMID:25644381 "more
  evidence is required to accept CDK16 as a novel XLID gene"]; patient variants are
  inactive and cannot bind CCNY [PMID:26205494].

### Mouse / rat (ortholog evidence; source of the ISS/IEA/IBA rows)

- Cdk16 knockout male mice are infertile with sperm annulus, head and residual-cytoplasm
  defects; development otherwise normal [PMID:22184064].
- CCNYL1 (not CCNY) is the partner required in testis; mutual stabilisation
  [PMID:26305884].
- Pctaire1 phosphorylates NSF Ser569 and restrains NSF oligomerisation; kinase-dead
  Pctaire1 *increases* stimulated growth hormone (reporter) release from PC12 cells
  [PMID:16461345]. The "growth hormone secretion" and "exocytosis" annotations derive
  from this regulatory, reporter-based evidence.
- Cdk5/p35 phosphorylates Pctaire1 Ser95 and activates it [PMID:12084709]; knockdown in
  hippocampal neurons abolishes dendrite development [PMID:21335063]. Neurite phenotypes
  in Neuro-2A [PMID:12154078]; MRTF/Srf regulates Pctaire1 expression in brain
  development [PMID:20534669].
- Brain substrates from a chemical-genetic screen: AAK1, dynamin 1, synaptojanin 1
  [PMID:30880224] (abstract only).
- In MIN6 β-cells, BRSK2 phosphorylates PCTAIRE1 Ser12; overexpressed active PCTAIRE1
  inhibits glucose-stimulated insulin secretion in a kinase-dependent manner
  [PMID:22798068].
- Mouse neurons / C. elegans: CDK16 phosphorylates WIPI2B S395, antagonised by PP2A, in
  neuronal autophagosome biogenesis [PMID:42774886] (2026; not yet in GOA).

## Phylogenetic grounding

- PANTHER PTHR24056:SF174 (CYCLIN-DEPENDENT KINASE 16).
- PAINT PTN002373304 (taxon Eukaryota, a broad CDK node) carries GO:0004693, GO:0000307
  and GO:0005737; CDK16 (Q00536) is itself one of the IBD seeds for GO:0000307 and
  GO:0005737.
- PAINT PTN004656776 (taxon Euteleostomi, the vertebrate PCTAIRE node) carries GO:0006887
  exocytosis, GO:0031175 neuron projection development and GO:0008021 synaptic vesicle;
  it is seeded only by mouse Cdk16 (MGI:97516), i.e. the rodent NSF/neurite work.
- PAINT PTN000623091 (broad CMGC node) gives GO:0005634 nucleus; there is no CDK16-
  specific evidence for nuclear activity and the endogenous protein is cytoplasmic.

## Curation decisions in brief

- Kinase MF terms: the specific supported term is GO:0004693 (cyclin-dependent protein
  serine/threonine kinase activity); general kinase terms are refined to it.
- Process terms from rodent overexpression/reporter assays are recast as regulation
  (regulation of exocytosis; regulation of neuron projection development) rather than
  participation.
- Protein-binding rows: CCNY/CCNYL1 → cyclin binding; 14-3-3 → 14-3-3 protein binding;
  others removed as uninformative.
- No NEW terms were added. WIPI2B / autophagosome biogenesis evidence is recent, partly
  worm-based, and recorded here and as a suggested question.
