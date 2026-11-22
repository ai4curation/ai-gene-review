# ENTR1 (donkey, A0A8C4MKL2) notes

## Sequence and record

- Unreviewed TrEMBL entry, 356 aa, "Endosome-associated-trafficking regulator 1"; PANTHER
  PTHR31259:SF3; Pfam ENTR1 coiled-coil region (PF29363) at 178..347
  [file:EQUAS/ENTR1/ENTR1-uniprot.txt "Belongs to the ENTR1 family."].
- No literature on donkey ENTR1. All 8 GOA rows are TreeGrafter IEA (GO_REF:0000118) from
  PTN009117290.
- Pairwise comparison to human Q96C92 (435 aa): 81.41% identity over 355 paired residues; the
  donkey sequence covers only 81.61% of human
  [file:EQUAS/ENTR1/ENTR1-bioinformatics/RESULTS.md "Paired coverage is 81.61% of the human sequence and 99.72% of the donkey sequence."].
  Inspection of `alignment.txt`: RESULTS.md lists human residues 9-85 as unpaired;
  donkey residue 9 onward aligns from human residue ~86. The donkey sequence also begins with Gln
  ("QPPVHAAP..."), not Met, so this entry is most likely an N-terminally incomplete gene model
  (UniProt does not flag it as a fragment). Seven donkey ENTR1 entries exist in UniProt
  (351-476 aa; UniProt REST query 2026-10-14), so longer models of the same gene exist.
- Consequence: the human N-terminal region (aa 1-100) is the one shown to be necessary and
  sufficient for basal-body localization, ciliogenesis rescue and IFT88 binding
  [PMID:27767179 "Amino acids 1-100 of SDCCAG3 are necessary and sufficient for basal body localization"].
  Human UniProt also maps GIT1 binding to the N-terminus
  [file:EQUAS/ENTR1/ENTR1-bioinformatics/human_Q96C92-uniprot.txt "Interacts (via N-terminus) with GIT1"].
  The conserved C-terminal coiled-coil region is intact.

## Human ortholog biology

- Endosomal protein (early and recycling endosomes) with roles in receptor sorting, cytokinesis
  and ciliogenesis [file:EQUAS/ENTR1/ENTR1-bioinformatics/human_Q96C92-uniprot.txt
  "Endosome-associated protein that plays a role in membrane receptor sorting, cytokinesis and ciliogenesis"].
- SNX27-retromer cargo recycling: VPS35 interactome identified SDCCAG3; depletion caused
  trafficking defects of retromer cargo [PMID:25278552 "Depletion of these proteins resulted in trafficking defects of retromer-dependent cargo"].
  Human GOA (QuickGO 2026-10-14) has GO:0032456 endocytic recycling (IMP, PMID:25278552) and
  GO:0030904 retromer complex only as `colocalizes_with` (IDA, PMID:25278552).
- Cilia: basal body localization, IFT88 interaction, PKD2 ciliary localization
  [PMID:27767179 "we demonstrate that SDCCAG3 is important for ciliary localization of the membrane protein Polycystin-2"].
- Cytokinesis/midbody (PMID:23108400, not cached; cited via human UniProt text).

## Decisions

- Endosome localizations (early, recycling): ACCEPT, core.
- Cytokinesis, midbody, centrosome: KEEP_AS_NON_CORE.
- Cilium-related terms: KEEP_AS_NON_CORE for the gene, with the caveat that this entry lacks the
  N-terminal region that mediates these roles in human.
- NEW: GO:0032456 endocytic recycling (ISS from human IMP), as the core process.

## ProtNLM2 (donkey40 snapshot)

- GO:0032456 endocytic recycling -> COR (not in donkey GOA; supported by human IMP).
- GO:0030904 retromer complex -> UNC (human evidence is colocalization/interaction, not
  subunit membership).
- Non-GO: subcellular_location "Membrane" (not scored).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 8 GOA rows, the previously proposed NEW row, description and
core_functions. ProtNLM2 outputs were not opened or used.

### Deep research

- `just deep-research-falcon EQUAS ENTR1 --fallback perplexity-lite` failed on 2026-10-21:
  falcon returned "Edison API request failed: Failed to authenticate" (403) and the
  perplexity-lite fallback returned HTTP 401 insufficient_quota. No deep-research file was
  written; the review relies on the cached literature (PMID:23108400 abstract, PMID:24980502,
  PMID:25278552 and PMID:27767179 full text) and the human UniProt record.

### Identity of the benchmark accession

- A0A8C4MKL2 (356 aa, starts "QPPVHAAP", no Met) vs canonical human Q96C92 (435 aa): lacks the
  region aligned to human residues 9-85, i.e. most of the N-terminal 1-100 segment that is
  necessary and sufficient for basal-body localization and IFT88 binding
  [PMID:27767179 "Amino acids 1-100 of SDCCAG3 are necessary and sufficient for basal body localization"].
  Coiled-coil Pfam PF29363 region intact. Conclusion unchanged: an N-terminally incomplete
  Ensembl gene model (ENSEASP00005027020.2) of the single donkey ENTR1 gene; six other donkey
  ENTR1 models exist (351-476 aa, e.g. A0A9L0K3Z4 476 aa, A0A8C4MT65 433 aa), all in SF3. No
  reviewed donkey ENTR1 entry exists, so there is no separate canonical donkey product to review.

### Evolutionary placement (new analysis)

- `ENTR1-bioinformatics/panther_subfamily_rereview.py` -> `RESULTS-rereview.md`
  (UniProt REST, 2026-10-21). PTHR31259 has 4 subfamilies: SF3 (1520 entries, ~900 organisms,
  vertebrates to Dictyostelium; includes donkey, horse, mouse A2AIW0, rat, bovine) and three
  great-ape-only splits: SF4 (4), SF5 (3), SF6 (19; Homo, Pan, Gorilla, Pongo).
- Human canonical ENTR1 Q96C92 is in SF6, but a human ENTR1 fragment (A0A0A0MRP9, 223 aa) scores
  into SF3 [file:EQUAS/ENTR1/ENTR1-bioinformatics/RESULTS-rereview.md "| A0A0A0MRP9 | Homo sapiens (Human) | 223 | unreviewed | PTHR31259;PTHR31259:SF3; |"].
  ENTR1 is single-copy in mammals, so SF6 vs SF3 is an HMM partition inside one orthologous
  lineage, not a paralog split. Transfer of human experimental functions is acceptable at the
  ortholog level; reported as a subfamily-placement discrepancy.
- Human IBAs (QuickGO 2026-10-21): early endosome, recycling endosome, midbody, centrosome,
  regulation of cytokinesis from PTN002039065 (2019-04-10); ciliary basal body, positive
  regulation of cilium assembly, positive regulation of protein localization to cilium from
  PTN004793274 (2024-02-29). The single donor is human Q96C92. The 8 donkey TreeGrafter rows
  (PTN009117290) are exactly this set.
- The human IMP to GO:0032456 endocytic recycling (PMID:25278552) dates from 2014-11-25, so it
  was available at both PAINT passes and was not propagated; nor was colocalizes_with retromer
  complex. Mouse carries GO:0032456 only via Ensembl Compara (GO_REF:0000107) and ISO.

### Changes made

- WITHDREW the previously proposed NEW GO:0032456 endocytic recycling (ISS) and removed it from
  core_functions.directly_involved_in. Reasons: (1) PAINT curators twice declined to propagate
  this human term while propagating all others, which the campaign treats as deliberate; (2)
  the human evidence is RNAi necessity data and cargo-selective
  [PMID:25278552 "Suppression of SDCCAG3 led to a decrease in GLUT1 surface expression and a reduction in whole-cell levels, but this did not correlate with an obvious accumulation of GLUT1 in lysosomes"]
  [PMID:25278552 "For RME-8 and SDCCAG3, RNAi-mediated suppression produced minor effects on CD97 surface levels"];
  (3) ENTR1 associates with retromer indirectly, via WASH
  [PMID:24980502 "for SDCCAG3 this is necessary for targeting to retromer-labeled endosomes"].
  The recycling role is kept in prose (description, core function text) and raised as a
  suggested question.
- Added PMID:23108400 (now cached, abstract-only) as direct support for endosome, midbody and
  cytokinesis rows, and PMID:24980502 for the WASH-dependent retromer association.
- Actions on the 8 GOA rows unchanged (2 ACCEPT: early and recycling endosome; 6
  KEEP_AS_NON_CORE: centrosome, midbody, regulation of cytokinesis, ciliary basal body, two
  cilium regulation terms); reasons now cite the PAINT nodes and the SF3/SF6 placement.
- Modules: no module in modules/ includes ENTR1 (grep for ENTR1/SDCCAG3/Q96C92); the only
  retromer module is the Drosophila `dmel_retromer.yaml`, which does not include ENTR1. ENTR1 is
  not in gocams/index.tsv.
- Relative for next review: human ENTR1 Q96C92 (ortholog; sole experimental donor for the PAINT
  nodes behind every donkey row). No genes/human/ENTR1 review exists. Mouse Entr1 A2AIW0 shares
  SF3 with donkey but has only one experimental row (cytoplasm, EXP, PMID:16332174).
