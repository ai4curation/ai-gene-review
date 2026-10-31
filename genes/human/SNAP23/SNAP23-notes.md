# SNAP23 (human, O00161) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference for the horse
ortholog (HORSE A0A3Q2HTF1). No ProtNLM2 files were opened or used.

### Deep research

`just deep-research-falcon human SNAP23 --fallback perplexity-lite` failed:
falcon returned "Exception: Failed to authenticate" and the perplexity-lite
fallback returned HTTP 401 "insufficient_quota". No deep-research file exists.
The review is built from the cached GOA-cited papers plus UniProt-cited primary
papers fetched with `just fetch-pmid` (8663154, 9070898, 10036234, 11354632,
12130530, 12556468, 21044946, 24910990, 28882895).

### Evolutionary grounding

- UniProt: `PANTHER; PTHR19305:SF4; SYNAPTOSOMAL-ASSOCIATED PROTEIN 23` and
  "Belongs to the SNAP-25 family". Two t-SNARE (Qb and Qc) coiled-coil homology
  domains (14-76, 146-208) linked by a cysteine-rich, palmitoylated linker
  (Cys79/80/83/85/87, Cys112 S-palmitoyl by acyl-RAC, PMID:21044946).
- PAINT nodes behind the IBAs: PTN000447753 (fusogenic activity, exocytosis,
  syntaxin binding, SNARE complex; human O00161 is itself a donor) and
  PTN000447752 (plasma membrane). PTN000447754 carries synaptic vesicle priming
  and synaptic vesicle fusion to the presynaptic active zone, seeded only by
  Drosophila Snap25 (FB:FBgn0011288); human SNAP23 is not a donor there.

### Experimentally established in human (human proteins / human cells)

- Binds multiple syntaxins and VAMPs; identified from human B cells
  [PMID:8663154 "we have identified a 23-kDa protein from human B lymphocytes (termed SNAP-23) that binds tightly to multiple syntaxins and synaptobrevins/VAMPs in vitro"].
- Complex with STX11 in native human B cells [PMID:10036234 "exists in a complex with SNAP-23 in transfected HeLa cells and in native human B lymphocytes"]; STX11 binds SNAP23 in human NK cells [PMID:24910990].
- N-terminal SNARE motif forms a heterotetramer with SNAP-23C, STX4 and VAMP3 (structure, PMID:12556468).
- Mast-cell histamine release requires SNAP-23 (human intestinal mast cells, PMID:18253931), with VAMP7/VAMP8 and STX4 partners.
- Neutrophil/eosinophil: SNAP-23 interacts with STX4 (PMID:16677249).
- IL-6/TNF release from SW982 cells needs SNAP-23 and VAMP-3 (PMID:24373201).
- STX11-SNAP23-VAMP8 cell-cell fusion assay and CTL cytotoxicity (PMID:28265073; abstract only in cache).
- Isoform SNAP-23b lacks residues 90-142, removing the palmitoylation region (PMID:9070898, PMID:11354632).

### Established in mouse cells only (ortholog evidence, attached to human in GOA)

- TLR4 recycling to the plasma membrane in J774 macrophages (PMID:30811271, a
  mouse cell line). The GOA IDA rows to human O00161 rest on mouse-cell data.

### Weak / localisation-screen evidence

- Mitochondrion: light-microscopy colocalisation in human muscle, r = 0.50 (PMID:26733245).
- Adherens junction: BioID proximity to E-cadherin (PMID:25468996).
- Focal adhesion, extracellular exosome: HDA proteomics.
- Immunological synapse (PMID:26771955): the cached full text does not mention
  SNAP23 beyond the generic word SNAP, so the IDA could not be verified.

### Decisions

- Synaptic vesicle priming / SV fusion at presynaptic active zone (IBA from
  PTN000447754) and derived presynapse IEA: marked as over-annotated. SNAP23 is
  the ubiquitous non-neuronal paralog; the synaptic terms reflect SNAP25 biology.
- GO:0099638 is obsolete, replaced by GO:0032456 endocytic recycling (QuickGO comment); MODIFY.
- GO:0140522 fusogenic activity is the parent of GO:0005484; TOO_GENERAL.
- Protein-binding IPIs: MODIFY to syntaxin binding (STX11, STX3) or SNARE binding (VAMP3);
  REMOVE for NAPA, NAPB, SCGN, ZDHHC17, STXBP2.
