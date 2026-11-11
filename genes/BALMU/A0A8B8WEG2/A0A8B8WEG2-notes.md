# A0A8B8WEG2 (CDK16, Balaenoptera musculus) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence used: the cached UniProt record, the falcon
deep-research file (no PMIDs; used only as orientation), primary literature on human, mouse and
rat CDK16/PCTAIRE1 cached into `publications/`, QuickGO annotations for human Q00536 (to read the
PAINT node placements), and a new sequence comparison in `A0A8B8WEG2-bioinformatics/`.

### Identity

- Gene: CDK16 (NCBI GeneID 118888515, chromosome X), RefSeq XP_036695538.1. 421 aa, unreviewed
  TrEMBL, PE 3.
- Blue whale has four UniProt products of this gene: A0A8B8WEF1 (496 aa, equivalent to human
  canonical isoform 1 Q00536-1), A0A8C0DX89 (502 aa, equivalent to human isoform 3), A0A8B8WEA8
  (482 aa) and this entry.
- A0A8B8WEG2 starts at the methionine equivalent to human Met76 and is identical to human CDK16
  76-496 at 419/421 positions [file:BALMU/A0A8B8WEG2/A0A8B8WEG2-bioinformatics/RESULTS.md]. It is an
  N-terminally shorter alternative-start isoform, not a fragment.
- It keeps the full kinase domain (catalytic K119 = human K194, HRD D211 = human D286) and every
  CCNY-binding determinant mapped in human CDK16. Mikolcevic et al. showed "the first 105 residues
  of CDK16 were not essential" for CCNY binding and that a recombinant CDK16 "lacking the N-terminal
  106 amino acid residues" was active with CCNY [PMID:22184064]. The isoform therefore has no
  structural reason to lack cyclin Y-dependent kinase activity. It lacks the Ser12 BRSK2 phosphosite
  [PMID:22798068], so that regulatory input cannot apply to this product.

### Phylogenetic placement

- PANTHER PTHR24056:SF174 (CYCLIN-DEPENDENT KINASE 16), the same subfamily as human Q00536, mouse
  Q04735 and rat Q63686 (`interpro/panther/PTHR24056/PTHR24056-entries.csv`). CDD cd07873
  STKc_PCTAIRE1. Function transfer from the mammalian CDK16 orthologs is therefore justified.
- TreeGrafter rows all come from PTN000623744. Reading the human CDK16 IBA rows in QuickGO
  (2026-10-21): GO:0004693 IBA from a deep CDK node (Drosophila and other donors); cytoplasm
  is_active_in IBA from three mouse donors (MGI:101765, MGI:894318, MGI:97516); nucleus is_active_in IBA seeded only by Arabidopsis
  CDKs; exocytosis, neuron projection development and synaptic vesicle IBA at PTN004656776 seeded
  by mouse Cdk16 (MGI:97516). Synaptic vesicle is `colocalizes_with` in the PAINT/human rows but
  arrived on this whale entry as `located_in`.
- Human CDK16 no longer carries the GO:1901987 cell-cycle-phase-transition IBA listed in its
  UniProt flat file; it is absent from QuickGO today.

### Literature (mammalian orthologs)

- Activation by cyclin Y: CCNY binding needs N-terminal extension plus kinase domain; regulated by
  Ser153 phosphorylation; CCNY recruits CDK16 to the plasma membrane [PMID:22184064]. CCNY raises
  activity >100-fold; PCTAIRE-1 prefers Pro at +1 and basic residue at +4 [PMID:22796189]. 14-3-3
  binding to phosphorylated CCNY is part of activation [PMID:26205494]. Structure [PMID:28057719].
- Substrates/roles: NSF Ser569, regulating NSF oligomerization and regulated GH secretion in PC12
  cells [PMID:16461345]; WIPI2B Ser395 in neuronal autophagosome biogenesis [PMID:42774886];
  CCNY Ser336 in vitro [PMID:22184064].
- Neurons: knockdown abolishes dendrite development; CDK5 phosphorylates Ser95 [PMID:21335063].
- Cdk16 knockout male mice are infertile with sperm annulus defects [PMID:22184064]: necessity
  phenotype, not added as process participation.
- The cell-cycle substrate claims in the falcon report (PRC1, Rb, p53, p27) carry no PMIDs and were
  not verified; they were removed from the description.

### Decisions

- GO:0004693 ACCEPT (core). ATP binding ACCEPT.
- Generic MF parents (nucleotide binding, kinase, transferase, protein kinase, protein S/T kinase):
  TOO_GENERAL (previously MARK_AS_OVER_ANNOTATED, which wrongly implied over-annotation of true terms).
- Cytoplasm ACCEPT. Nucleus MARK_AS_OVER_ANNOTATED (plant-seeded deep node; CDK16-GFP exclusively
  cytoplasmic in 293A cells).
- Exocytosis: MODIFY to GO:0017157 regulation of exocytosis (kinase modulates NSF; not core
  machinery).
- Synaptic vesicle: KEEP_AS_NON_CORE, with a WRONG_QUALIFIER source defect (should be
  colocalizes_with).
- Neuron projection development KEEP_AS_NON_CORE.
- Regulation of cell cycle MARK_AS_OVER_ANNOTATED (ontology-link inference from GO:0004693; PAINT
  no longer propagates a cell-cycle term to CDK16).
- NEW: GO:0000307 cyclin-dependent protein kinase holoenzyme complex (CDK16-CCNY).
- Removed unvetted UniProt quotes (the ARBA RecName; keyword lines) as support.

### Next relative

Canonical full-length product of the same whale gene, A0A8B8WEF1 (496 aa), has no review. The
nearest characterised ortholog, human CDK16 Q00536 (same subfamily SF174), also has no review.

## 2026-10-21 — Characterised comparator (PR #5304 review)

The same-gene relative reviewed in this batch now lives in `genes/BALMU/CDK16__A0A8B8WEF1/` (renamed from the
bare-symbol folder so it does not shadow this accession's folder). That relative has no experimental data of its
own, so the experimentally characterised comparator is human CDK16 (PCTAIRE-1), now reviewed in
`genes/human/CDK16/`. It sits in the same PANTHER subfamily (PTHR24056:SF174) as this target. In human, the core
activity, cyclin Y-dependent serine/threonine kinase activity, is shown directly. The secretion, neurite and
spermatogenesis roles rest on rodent data, and the review records them as regulation or as non-core.
