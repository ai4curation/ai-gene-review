# Cxcr3 (mouse, O88410) review notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is the first review of mouse Cxcr3. It was written without opening any ProtNLM2
prediction file. Mouse Cxcr3 is meant to serve as the experimentally characterised
reference for transfers to human CXCR3 (P49682), so these notes keep apart what was shown
**in mouse** and what reached the mouse entry by orthology transfer.

### Deep research

`just deep-research-falcon mouse Cxcr3 --fallback perplexity-lite` failed. Falcon
returned `Exception: Failed to authenticate` (Edison client JWT), and the perplexity-lite
fallback returned HTTP 401 `insufficient_quota`. There is no deep-research file. The
review is based on the UniProt record, the cached GOA references, and 13 primary papers
found by PubMed search and cached with `just fetch-pmid`.

### Evolutionary grounding

- PANTHER: O88410 belongs to PTHR10489:SF671 "C-X-C CHEMOKINE RECEPTOR TYPE 3", together
  with human P49682 and rat Q9JII9 (`interpro/panther/PTHR10489/PTHR10489-entries.csv`).
  It is the 1:1 mammalian ortholog. Canonical mouse and human proteins share 86.4%
  identity (`Cxcr3-bioinformatics/RESULTS.md`; the cloning paper also gives 86%
  [PMID:9790904 "exhibits 86 % identity with the human IP-10 receptor"]).
- The IBA rows come from PANTHER:PTN001628461, a deep node that covers both CC and CXC
  chemokine receptors (the donor list includes CCR1/2/5 etc.). For the CC-ligand terms
  (C-C chemokine receptor activity and C-C chemokine binding), CXCR3 inherits from a node
  placed for CC receptors. In human CXCR3 the human ortholog review REMOVEs these IBAs.
  In mouse, however, there is direct evidence that CCL21/6Ckine activates the receptor (see below),
  so for this species the activity is real, even though it is not the core function.

### CXCR3-B does not exist in mouse (new analysis)

Many human annotations were made on the CXCR3-B splice isoform (P49682-2) [PMID:12782716
"overexpression of CXCR3-B dramatically reduced DNA synthesis and up-regulated apoptotic
HMEC-1 death through activation of distinct signal transduction pathways"]. Those
annotations reach mouse through GO_REF:0000119 ISO transfer. Examples are negative
regulation of endothelial cell proliferation, adenylate cyclase-activating GPCR signalling,
positive regulation of execution phase of apoptosis, and positive regulation of
transcription by RNA polymerase II.

`Cxcr3-bioinformatics/cxcr3b_exon_search.py` six-frame searches the mouse Cxcr3 locus (gene ±5 kb) for
the 51-residue CXCR3-B extension. The human positive control is found at 51/51 identity
(z=48). Mouse has no match: the best hit is 10 residues, z=-1.2, and the reading frame
reaches a stop codon after 20 codons. Ensembl annotates one mouse transcript, and UniProt
lists no isoforms. **The mouse locus cannot encode a CXCR3-B-like protein**, so
isoform-B-specific human findings should not be transferred to mouse by gene-level
orthology.

The B-specific cAMP response is pertussis-toxin insensitive and absent from CXCR3-A
[PMID:12782716 "the same chemokines did not induce any significant increase of cAMP levels
in either mock cells nor CXCR3-A transfectants"]. CXCR3-A is the form that mouse retains.

### What is established experimentally in mouse

- **CXCL10 receptor, calcium mobilisation**. The receptor was cloned from CTLL2 cells
  [PMID:9790904 "It mediates Ca2+ mobilization in response to IP-10, but does not recognize
  other rodent chemokines, including GRO, RANTES, monocyte chemoattractant protein-1
  (MCP-1), and macrophage inflammatory protein-1alpha"]. Abstract only.
- **Sole functional receptor for CXCL9/CXCL10 on T cells; chemotaxis**. Cxcr3-/- T cell blasts
  [PMID:11085753 "failed to respond in chemotaxis assays to IP-10"; "indicating that CXCR3
  is the sole functional receptor for these chemokines"]. Full text.
- **CCL21/6Ckine is a mouse-specific CC ligand**. Mouse 6Ckine causes calcium flux in
  mouse CXCR3 transfectants [PMID:9653165 "identified a new ligand for this receptor, the
  recently reported CC chemokine 6Ckine"]. Human 6Ckine does not
  [PMID:10201891 "human CC chemokine 6Ckine is not a ligand for the human or mouse CXC
  chemokine receptor CXCR3"]. In Cxcr3-/- microglia, CCL21 triggers neither a Cl- current nor
  chemotaxis [PMID:11907075]. CCL21-induced calcium transients in astrocytes are
  CXCR3-dependent at low concentrations [PMID:19401230]. The species difference rests
  on the ligand (mouse versus human CCL21), not only on the receptor. All of these are
  abstract-only in the cache.
- **In vivo recruitment of effector T cells**. Allograft rejection [PMID:11085753],
  CD8 T cell entry into the brain in cerebral malaria [PMID:18347328 "CXCR3-deficient CD8(+)
  T cells were 7-fold less efficient at migrating into the infected brains"], T cell
  accumulation in fat [PMID:24812325], and intranodal positioning that optimises Th1
  differentiation [PMID:23123063]. Positioning of CD8 T cells in the spleen affects the
  balance between effector and memory cells [PMID:21788406, PMID:21518913]. These are
  phenotypes that follow from the receptor's chemotactic function. I did not propose them
  as process annotations (T-helper 1 differentiation, memory T cell differentiation),
  because CXCR3 positions the cell; it does not do the work of differentiation.
- **Cell-surface location**. Flow cytometry on mouse T cells [PMID:19008373,
  PMID:23620790].
- **Angiostasis (uncertain)**. Laser-induced choroidal neovascularisation is larger in
  Cxcr3-/- mice, and CXCR3 is detected on CNV endothelium [PMID:22408007]. Macrophage
  infiltration and CCL2 also rise, so this phenotype does not establish a direct
  endothelial anti-angiogenic signal. Without CXCR3-B, the mouse mechanism is unknown.
  Negative regulation of angiogenesis is set to UNDECIDED.
- **Astrocyte proliferation**. CXCL10-induced proliferation of primary astrocytes is absent
  in Cxcr3-/- astrocytes [PMID:19401230]. This supports positive regulation of cell
  population proliferation as a non-core role.

### Decisions summary

- Core: C-X-C chemokine receptor activity, chemokine-mediated signalling, T cell
  chemotaxis, calcium mobilisation, plasma membrane / external side of plasma membrane.
- Non-core but kept, mouse-specific: C-C chemokine receptor activity and C-C chemokine
  binding (CCL21). The IBA rows are kept because mouse experiments support them, not
  because the deep PTN node justifies them for the CXCR3 clade.
- REMOVE (CXCR3-B-specific human data, isoform absent in mouse): adenylate
  cyclase-activating GPCR signalling, positive regulation of execution phase of apoptosis,
  positive regulation of transcription by RNA polymerase II.
- MARK_AS_OVER_ANNOTATED: negative regulation of endothelial cell proliferation
  (B-specific source), positive regulation of angiogenesis (source is CXCR3-A in human
  HMEC-1/mesangial transfectants; the mouse knockout phenotype points the other way),
  and negative regulation of execution phase of apoptosis (a survival readout in human
  transfectants).
- General terms are refined to C-X-C chemokine receptor activity, chemokine-mediated
  signalling pathway, T cell chemotaxis and plasma membrane.
