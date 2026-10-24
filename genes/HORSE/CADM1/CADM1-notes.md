# CADM1 (horse, Equus caballus; UniProt A0A5F5PGJ5) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No earlier review existed for this accession; the folder was created with
`just fetch-gene HORSE A0A5F5PGJ5 --alias CADM1` (stub id confirmed as A0A5F5PGJ5). ProtNLM2
outputs were not consulted.

### Deep research

`just deep-research HORSE CADM1 --provider falcon --fallback perplexity-lite` failed: falcon
raised "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). No deep-research file was produced. The review relies on cached publications
(PMID:12050160, PMID:12202822, PMID:12234973, PMID:15781451, PMID:15811952, PMID:22438059) and the
human UniProt record Q9BY67 (`CADM1-bioinformatics/human-CADM1-Q9BY67-uniprot.txt`).

### Identity of the benchmark accession

- Horse A0A5F5PGJ5, 417 aa, unreviewed (Ensembl ENSECAP00000047575.1, VGNC:15999), PE 3.
- [RESULTS.md "The horse CADM1 protein matches human CADM1 at 99.03% identity over 414 paired residues."]
- The only length difference that matters is a 28-residue gap at human 332..359 in the stalk, the
  segment UniProt marks as missing from human isoform 5 (VAR_SEQ 333..360). Horse therefore
  corresponds to the human isoform 5 / SP4 splice form (exons 7/8/11), not the displayed human
  isoform 1 (SP1). SP4 is the main isoform in human mast cells [PMID:22438059 "Differentiated HLMCs
  and LAD2 cells expressed the functional isoform SP4 containing exons 7/8/11 (~80% of clones)"].
- It is a complete product, not a fragment: signal peptide, three Ig-like domains, TM helix and
  the full cytoplasmic tail ending EYFI (PDZ-binding) are present. Unlike the donkey partner entry
  (A0A9L0IX39, divergent tail), the horse tail is identical to human.

### Evolutionary grounding

- UniProt places horse A0A5F5PGJ5 in PANTHER PTHR45889:SF2 (CELL ADHESION MOLECULE 1), the same
  subfamily as human Q9BY67, mouse Q8R5M8 and rat Q6AYP5 (`interpro/panther/PTHR45889/PTHR45889-entries.csv`).
- IBA rows come from PTN002913382 (CADM1 node; donors human, mouse, rat) and, for homophilic
  cell-cell adhesion, from the deeper PTN001910345 (donors include mouse Cadm1 and another MGI CADM
  member). No PANTHER family review YAML exists for PTHR45889, so there is no subfamily disagreement
  to report.
- No module under `modules/` mentions CADM1 or Q9BY67.

### Function (orthologs)

- Homophilic adhesion [PMID:12050160 "TSLC1 mediates intracellular adhesion through homophilic interactions in a Ca(2+)/Mg(2+)-independent manner"].
- Synapse [PMID:12202822 "functions as a homophilic cell adhesion molecule at the synapse"].
- CRTAM ligand [PMID:15811952 "natural killer (NK) cells and CD8+ T cells recognize Necl-2 through a receptor known as class I-restricted T-cell-associated molecule (CRTAM)"].
- Actin link via 4.1 [PMID:12234973 "TSLC1 directly associates with DAL-1"].

### Decisions

- ACCEPT: signaling receptor binding (CRTAM ligand), plasma membrane (IBA + IEA), homophilic
  cell-cell adhesion (core), susceptibility to NK cell mediated cytotoxicity, synapse (IBA + IEA;
  tail intact in horse).
- KEEP_AS_NON_CORE: cell recognition (broad), neuron projection (broad location).
- MARK_AS_OVER_ANNOTATED: detection of stimulus (CADM1 is the detected ligand; the CRTAM-bearing
  lymphocyte detects). Recorded as SOURCE_BAD / ROLE_CONFLATION at PTN002913382.
- No NEW annotations. Core MF given as GO:0098632 cell-cell adhesion mediator activity in
  core_functions only (validator warns that it is not in existing_annotations).

### Relative for next review

Human CADM1 (Q9BY67), ortholog in the same PANTHER subfamily and a donor of the PTN002913382 IBD;
no review exists in the repo for human CADM1 or mouse Cadm1.
