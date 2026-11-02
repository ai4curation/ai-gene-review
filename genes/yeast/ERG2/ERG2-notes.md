# S. cerevisiae ERG2 Notes

## 2026-10-11

`just fetch-gene yeast ERG2` seeded 21 GOA rows for the reviewed UniProt
entry `P32352`: C-8 sterol isomerase activity rows from PAINT, the legacy
DOI-only SGD/UniProt biochemical reference, Rhea, and maize-complementation
mutant evidence; two `protein binding` rows for Erg24; multiple ER and
ER-membrane localization rows; three YeastPathways RCA cytosol rows; the
fungal PAINT ergosterol-biosynthesis row; direct and RCA
ergosterol-biosynthesis rows; and a UniPathway sterol-biosynthesis IEA.

Automated deep research was not available in this environment:

```text
just deep-research-falcon yeast ERG2 --fallback perplexity-lite
```

failed because neither `agentapi` nor provider API keys were configured. I
therefore did a manual literature, PAINT, and GO-CAM pass.

### PAINT

`interpro/panther/PTHR10868/PTHR10868-paint.tsv` has one fungal ERG2 ancestor,
`PTN001280219`, carrying `GO:0000247 C-8 sterol isomerase activity` and
`GO:0006696 ergosterol biosynthetic process`. The S. cerevisiae target
`SGD:S000004815` is one of the experimentally grounded descendants that seeded
this node, so the self-entry in GOA `WITH/FROM` is evidence of direct grounding,
not circular propagation.

The ER row comes from the broader `PTN001328958` eukaryotic ERG2/SIGMAR1-family
node seeded by fungal ERG2 and animal SIGMAR1 entries. That node is appropriate
for the shared ER compartment. The animal signaling, postsynaptic, and
neuron-apoptosis rows in PTHR10868 sit on `PTN001593709` and `PTN008312250` and
do not propagate to `P32352`.

Fungal Erg2 is homologous to mammalian SIGMAR1, not to EBP, the mammalian
8,7-sterol isomerase; the shared PTHR10868 placement therefore supports the ER
compartment but not transfer of the catalytic activity to animal SIGMAR1
descendants or the Sigma-receptor signaling terms back to fungal ERG2.

### Cached Publications

- DOI:10.1016/S0031-9422(00)80523-3 is the 1984 Baloch et al.
  tridemorph/fenpropimorph/fenpropidin study. It is not cached locally because
  it is DOI-only in the source GOA, but Crossref resolves the DOI and UniProt
  cites it as direct evidence for the curated C-8 sterol isomerase activity.
- PMID:8988026 is abstract-only locally. Moebius et al. show that
  radioligand binding present in wild-type ERG2 microsomes is absent from erg2
  mutant/disruption strains and is inhibited by sterol isomerase inhibitors;
  they also photoaffinity-labeled and immunoprecipitated the c-myc-tagged ERG2
  product. This supports the direct assignment of the drug-binding sterol
  isomerase activity to Erg2p.
- PMID:18459942 is abstract-only locally. The Zea mays 8,7 sterol isomerase
  study uses a yeast erg2 mutant that lacks 8,7SI activity and shows that the
  maize enzyme restores endogenous ergosterol biosynthesis. This supports loss
  of the endogenous S. cerevisiae C-8 sterol isomerase reaction in the mutant.
- PMID:16300994 is abstract-only locally. The split-ubiquitin sterol-enzyme
  interaction study places Erg2p in an ER sterol-enzyme interaction network and
  reports an Erg2p-Erg24p interaction.
- PMID:37968396 is full text locally. The 2023 yeast interactome re-detected
  Erg2p-Erg24p by affinity purification/mass spectrometry; this corroborates
  the older interaction but remains an interaction annotation rather than a
  separate molecular activity.
- PMID:15716577 is abstract-only locally. The abstract supports the
  proteome-scale S. cerevisiae GFP-localization assay that SGD and UniProt use
  for Erg2p ER-membrane localization.
- PMID:26928762 is full text locally. The SWAp-Tag GFP library is a general
  high-throughput localization resource; SGD uses it for an ER HDA row on ERG2.
- PMID:21946531 is abstract-only locally. The review summarizes fungal
  steroid-transforming enzymes and the ER localization of the ergosterol
  pathway; I treated the NAS ER row as weaker context beside direct localization
  and PAINT evidence.
- PMID:33889823, PMID:38419072, and PMID:38450166 are full text locally. All
  three are chemogenomic stress-tolerance studies that find
  ergosterol-pathway deletions, including erg2, hypersensitive to
  organic-acid or catechol stresses. These are downstream membrane-composition
  phenotypes, not new direct ERG2 process terms.

### GO-CAMs

The curated SGD model `gocams/61f34dd300001044` already models
`SGD:S000004815` as a `GO:0000247` C-8 sterol isomerase activity that occurs in
the ER and is part of `GO:0006696` ergosterol biosynthetic process.

The three `GO_REF:0000123` RCA rows come from imported YeastPathways GO-CAMs
for `ERGOSTEROL-SYN-PWY-1`, `PWY-6075-1`, and `PWY3O-31704`. Those models
connect `SGD:S000004815` to the same `RXN3O-203` reaction and
`GO:0006696`, but use generic `GO:0003674 molecular_function` and
`GO:0005829 cytosol`. The pathway membership is biologically sound, but the
cytosol compartment is a conversion artifact and conflicts with direct ER and
ER-membrane localization.

### Curation Decisions

The core function is ER-membrane C-8 sterol isomerase activity that converts
fecosterol to episterol during ergosterol biosynthesis. The fungal
`PTN001280219` activity and pathway IBAs should be accepted with
`NO_FAILURE_CORE`, as should the broader eukaryotic `PTN001328958`
ER-localization IBA.

The Erg24 `protein binding` rows describe a real interaction between two
ergosterol enzymes but should be removed because bare protein binding is not
an informative Erg2p molecular function. The YeastPathways ergosterol
biosynthesis RCA rows can be accepted for pathway membership, while the three
cytosol RCA rows should be modified to GO:0005789 endoplasmic reticulum
membrane to correct the pathway-conversion compartment error.

No new GO rows are proposed. Organic-acid tolerance, catechol sensitivity,
adipic-acid sensitivity, and plasma-membrane endocytosis phenotypes are
consequences of altered sterol composition in erg2 mutant cells.
