# IL10 curation notes

## 2026-09-04 — Finishing pass (PAINT no-IBA project)

Completed the quality pass over `IL10-ai-review.yaml` (previously DRAFT, now COMPLETE;
validates with zero warnings). All 124 `existing_annotations` entries were checked against
the 132 GOA rows — coverage is complete (multi-partner IPI rows sharing term/evidence/
reference collapse into one entry). Machine-backfilled GOA qualifiers from today's
fetch-gene run were retained.

### Material finding 1: four ISS annotations are sourced from mouse TNF, not IL-10

The eight `GO_REF:0000024` ISS rows split cleanly by WITH/FROM accession:

- `UniProtKB:P18893` = **IL10_MOUSE** (verified via UniProt REST) → GO:0034115,
  GO:1904706, GO:0008285, GO:1903034. Legitimate orthologue transfers.
- `UniProtKB:P06804` = **TNFA_MOUSE**, mouse tumor necrosis factor (verified via UniProt
  REST) → GO:0034116, GO:0045930, GO:0072577, GO:1904707.

The draft review had described P06804 as "FasL/TNFSF6", which is wrong; the accession is
mouse TNF. The corrected identification actually *strengthens* the REMOVE calls, and adds
a diagnostic pattern the earlier draft missed: in two cases the P06804-derived term is the
exact opposite of the P18893-derived term in the same batch —

| P18893 (mouse IL-10) | P06804 (mouse TNF) |
|---|---|
| GO:0034115 negative regulation of heterotypic cell-cell adhesion | GO:0034116 **positive** regulation of heterotypic cell-cell adhesion |
| GO:1904706 negative regulation of VSMC proliferation | GO:1904707 **positive** regulation of VSMC proliferation |

All four P06804 terms are canonical TNF activities (upregulating endothelial adhesion
molecules, endothelial apoptosis, VSMC proliferation). ISS requires a sequence-similarity
basis, and the TNF-superfamily beta-sandwich fold has no homology to the class-II
four-helix-bundle IL-10 fold, so no transfer is possible in principle. This looks like a
wrong-accession data entry in the GO_REF:0000024 batch. All four kept as REMOVE, with the
reasons rewritten to name mouse TNF and to argue from fold non-homology plus the
opposite-direction pattern rather than from a misremembered FasL identity.

### Material finding 2: GO:0043032 resolved from UNDECIDED

The IEA `positive regulation of macrophage activation` row (ortholog transfer from rat
Il10, `UniProtKB:P29456`) had been left UNDECIDED as "seemingly contradictory". The rat
source annotation was traced in QuickGO to an **IDA supported by PMID:25837415** (fetched
into the publications cache), which shows IL-10 on nanofibre scaffolds implanted around
rat sciatic nerve driving M2 polarization: [PMID:25837415 "IL-10 conjugated nanofibres
successfully induced macrophage polarisation towards the M2 activated state within the
scaffold material as well as the adjacent tissue surrounding the nerve."] and
[PMID:25837415 "Interleukin 10 (IL-10) is a cytokine that promotes macrophages toward an
anti-inflammatory/wound healing state (M2 phenotype)."].

GO:0042116 (macrophage activation) is defined broadly ("A change in morphology and
behavior of a macrophage resulting from exposure to a cytokine, chemokine, cellular
ligand, or soluble factor"), which covers alternative (M2) activation, so the transfer is
sound and not contradictory. There is no GO term for alternative macrophage activation
(checked via QuickGO search), so no MODIFY target exists. Changed to **KEEP_AS_NON_CORE**:
real, but a downstream myeloid consequence of IL-10/IL-10R/STAT3 signalling, and easy to
misread without the M2 qualifier given that IL-10 potently suppresses classical activation
[PMID:1940799].

### Other changes

- **HuRI REMOVE (PMID:32296183)** — all six recorded partners were verified against
  UniProt: GLRX3 (cytosolic), NOTCH2NLC, YY1 (nuclear TF), and KRTAP10-8 / KRTAP1-3 /
  KRTAP4-1. The draft called them all "keratins"; corrected to the actual identities. All
  six are intracellular/nuclear or hair-shaft proteins with no compartment overlap with a
  secreted cytokine. Supporting quote swapped from the paper title to the authors' own
  caveat [PMID:32296183 "we expect HuRI to be depleted for PPIs that depend on
  post-translational processing of human proteins that the yeast cell is unable to
  catalyze or that require additional partners to stabilize the interaction"]. REMOVE
  retained.
- **Receptor-binding MODIFY entries** (PMID:11485736, PMID:15837194, PMID:16982608) had
  hedging summaries ("likely describes…"). Replaced with what the papers actually report,
  read from the cached abstracts: the 2.9 A IL-10/sIL-10R1 crystal structure; the EBV
  vIL-10/sIL-10R1 structure with its ~1000-fold affinity difference; and the SPR mapping
  of the IL-10R2 site to helix A adjacent to the IL-10R1 surface. All remain MODIFY →
  GO:0005141.
- **core_functions supporting_by** carried three placeholder "quotes" that were reviewer
  prose flagged `full_text_unavailable: true` (e.g. "Seminal paper cloning human IL-10
  cDNA…"), plus one PMID:1940799 quote that had been silently spliced. Replaced all with
  verbatim abstract text, and dropped PMID:10443688 from the cytokine-activity support
  (that paper is about dexamethasone sensitivity of monocytes, a weak choice for the core
  claim) in favour of PMID:1847510 and PMID:1940799.
- Added findings to the `file:human/IL10/IL10-deep-research-falcon.md` reference and cited
  it in core_functions where the synthesis genuinely grounds the receptor architecture and
  the anti-inflammatory core role. This also cleared the deep-research validation warning.
- The 11 duplicate Reactome TAS `extracellular region` entries and the block of IEA
  "response to X" ortholog transfers (xenobiotic, activity, inactivity, CO, estradiol,
  insulin, liver regeneration, sprouting angiogenesis, synapse organization) were reviewed
  and left as-is: ACCEPT for the duplicates, MARK_AS_OVER_ANNOTATED for the peripheral
  rodent-expression-derived responses. These are consistent across duplicate terms.

Final action counts: ACCEPT 60, KEEP_AS_NON_CORE 38, MARK_AS_OVER_ANNOTATED 15, MODIFY 6,
REMOVE 5, UNDECIDED 0.
