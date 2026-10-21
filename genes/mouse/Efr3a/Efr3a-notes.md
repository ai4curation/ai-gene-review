# Efr3a (mouse, Q8BG67) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised ortholog of human EFR3A (Q14156). No ProtNLM2 output was used.

### Deep research
`just deep-research-falcon mouse Efr3a --fallback perplexity-lite` failed: falcon returned "Failed to authenticate" and the
perplexity fallback returned HTTP 401 (quota exceeded). No deep-research file exists; the review is based on cached
publications read directly and a PubMed search for "Efr3a" (33 hits; mouse-relevant papers cached).

### Evolutionary grounding
- Mouse Efr3a and human EFR3A are both PANTHER PTHR12444:SF1, about 97% identical (Efr3a-bioinformatics/RESULTS.md).
  Mouse Efr3b is PTHR12444:SF4. PAINT node PTN000278197 covers the EFR3A/EFR3B clade and propagates plasma membrane and
  protein localization to plasma membrane only, not synaptic terms.
- The Nakatsu 2012 (PMID:23229899) EFR3A constructs are **mouse** Efr3a: "Mouse EFR3A (GenBank accession no. BC007482)";
  BC007482 is a cross-reference of Q8BG67. So palmitoylation of Cys6-Cys9 and its requirement for plasma-membrane
  localization are established on the mouse protein. Wu 2014 (PMID:24360784) basic-patch mutant was in "murine EFR3A-GFP".
- The TTC7B/FAM126A-binding C terminus and PI4KA recruitment assays (PMID:39705356, and the HeLa siRNA work in
  PMID:23229899) are human EFR3A/EFR3B; transferred to mouse by orthology.

### Experimentally established in mouse versus inferred
- Established in mouse protein: plasma-membrane localization (PMID:15363888, PMID:23229899, PMID:24360784);
  palmitoylation-dependent and basic-patch-dependent membrane anchoring.
- Inferred from human ortholog: binding of TTC7-FAM126, recruitment of PI4KA (protein localization to plasma membrane),
  hence protein-membrane adaptor activity (added as NEW with ISS).
- Mouse in vivo phenotypes (not annotated): brain-specific knockout increases adult hippocampal neurogenesis and BDNF-TrkB
  signaling (PMID:28193719); Efr3a dosage modifies Abeta-induced mGluR5/PIP2 loss of release probability (PMID:30867420);
  Rbms1 stabilizes Efr3a mRNA and Efr3a overexpression rescues Rbms1-knockdown migration (PMID:35754370).

### Decisions
- SynGO rows from PMID:30867420 (synaptic vesicle priming IDA/IMP, glutamatergic synapse IDA/IMP) and the derived presynapse
  IEA row: MARK_AS_OVER_ANNOTATED. Full text read: Efr3a was a tool to dampen GPCR responsiveness in an AD model; no direct
  priming step or synaptic localization is shown. Not removed because they are experimental curator annotations, but they
  should not be used as transfer sources (the human Compara copies are removed / over-annotated in genes/human/EFR3A).
- Three 2006 MGI ISO rows (cornified envelope, protein homodimerization activity, cell-cell adhesion) have WITH/FROM
  UniProtKB:Q15517, which is human CDSN (corneodesmosin, PTHR23207). No orthology basis: REMOVE.
- Cytosol (IEA/ISO): KEEP_AS_NON_CORE, a minor pool.
