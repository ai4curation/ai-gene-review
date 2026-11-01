# GPI16 (YHR188C, P38875) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised fungal ortholog of the
fission-yeast benchmark gene SCHPO/gpi16 (O94380). Both proteins are in PANTHER
subfamily PTHR12959:SF11 (GPI TRANSAMIDASE COMPONENT PIG-T) per their UniProt
cross-references, and SGD:S000001231 (this gene) is one of the experimental
donors at PAINT node PTN000311103 (Eukaryota) that supplies the IBA rows for
both genes. No ProtNLM2 files or prediction-evidence folders were opened.

### Deep research

`just deep-research-falcon yeast GPI16 --fallback perplexity-lite` failed:
falcon raised `Exception: Failed to authenticate`, and the perplexity-lite
fallback returned HTTP 401 (`insufficient_quota`). No deep-research file was
produced. The review is based on the cached publications listed below and the
UniProt record.

### What is experimentally established in S. cerevisiae

- **Complex membership (IDA, affinity purification).** Gpi8 complexes of
  430-650 kDa purified from digitonin extracts consist of Gaa1, Gpi8 and Gpi16
  [PMID:11598210 "These complexes can be affinity purified and are shown to
  consist of Gaa1p, Gpi8p, and Gpi16p (YHR188c)"]. Endogenous 3xFLAG-Gpi16
  purifications later recovered the five-subunit complex
  [PMID:28374821 "GPIT was separately purified from each of four different S. cerevisiae (S. cerevisiae) strains containing 3xFLAG-Gpi8, 3xFLAG-Gaa1, 3xFLAG-Gpi16, or 3xFLAG-Gpi17"].
- **Topology and localisation (IDA).** Essential N-glycosylated type I
  membrane glycoprotein; bulk lumenal, single C-terminal TM, short cytosolic
  tail with an ER retrieval motif [PMID:11598210 "Its bulk resides on the
  lumenal side of the ER, and it has a single C-terminal transmembrane domain"].
  An HTP SWAp-Tag screen also places it in the ER (PMID:26928762).
- **Required for GPI transfer to protein (IMP, depletion).** Depletion
  accumulates the complete GPI lipid CP2 and unprocessed GPI-protein precursors
  [PMID:11598210 "Depletion of Gpi16p results in the accumulation of the
  complete GPI lipid CP2 and of unprocessed GPI precursor proteins"]. This places
  Gpi16 at the attachment step, downstream of GPI lipid assembly, and not in
  synthesis of the GPI glycolipid itself.
- **Mutual stabilisation with Gpi8.** [PMID:11598210 "Gpi8p and Gpi16p are
  unstable if either of them is removed by depletion"; "Overexpression of
  Gpi8p cannot compensate for the lack of Gpi16p"]. Gpi8 becomes unstable when
  any other subunit is depleted [PMID:15939668].
- **No Gpi8-Gpi16 disulfide in yeast.** UniProt annotates an interchain
  disulfide Cys202-Gpi8 Cys85 only "by similarity" (ECO:0000250) to the human
  PIGT-PIGK bond. Yi et al. tested this directly: the purified lumenal domains
  do not interact and the native yeast complex shows no disulfide-linked
  Gpi8-Gpi16 species on non-reducing gels [PMID:28374821 "our data show that
  the luminal domains of S. cerevisiae Gpi8 and S. cerevisiae Gpi16 do not
  interact directly"]. So the disulfide is a mammalian/trypanosome feature that
  should NOT be transferred to fungal orthologs. This is a likely upstream
  UniProt feature defect (not a GO annotation, so recorded here and as a
  suggested question).

### What is inferred, not shown, in yeast

- **Catalysis** belongs to Gpi8 (the caspase-like subunit). In the human
  structure PIGK is the catalytic component [PMID:35165458 "The PIGK subunit
  functions as the catalytic component"]. No activity has been demonstrated for
  Gpi16 itself; it is an essential non-catalytic subunit. The proposed role of
  the PIG-T beta-propeller lumenal domain in substrate access is a hypothesis
  (PMID:28374821 introduction), not tested in yeast.
- **PAINT decision.** PTN000311103 propagates only GO:0042765 (complex) and
  GO:0016255 (attachment of GPI anchor to protein). No MF was propagated, and
  human PIGT also lacks a contributes_to GPI-anchor transamidase activity row, so
  no MF is proposed here (ND row retained).
- PMID:11483512 (mouse F9 knockouts of PIG-T/PIG-S) is the reference for a
  UniProt IMP row to GO:0016255. Its abstract reports only mouse experiments and
  names Gpi16 as the PIG-T orthologue. The function is independently established
  for yeast by PMID:11598210, so the row is accepted, deferring to the curator on
  the full text.

### Annotation decisions (summary)

- Complex, ER membrane, attachment of GPI anchor to protein: ACCEPT (core).
- ER (HDA): ACCEPT (correct, broader localisation from a screen).
- GO:0006506 GPI anchor biosynthetic process (UniPathway IEA): MODIFY to
  GO:0016255. Verified via OLS that GO:0016255 is not a descendant of
  GO:0006506 (it is under GO:0180046 GPI anchored protein biosynthesis); the
  depletion phenotype shows the lipid is still made.
- GO:0031505 fungal-type cell wall organization (ComplexPortal NAS):
  MARK_AS_OVER_ANNOTATED. Downstream consequence of failing to anchor cell-wall
  GPI proteins, not a step Gpi16 performs.
- All eleven GO:0005515 rows: REMOVE per the protein-binding policy; the
  interactions (Gaa1, Gpi8, Gpi17) are real and captured by complex membership.
