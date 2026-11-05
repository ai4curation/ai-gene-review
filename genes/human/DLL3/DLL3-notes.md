# DLL3 (Q9NYJ7) — curation notes

Deep research providers were unavailable in this environment (`just deep-research-falcon
human DLL3 --fallback perplexity-lite` failed: "agentapi not found in PATH"; perplexity
provider not configured). Research below was done directly from the cached publications,
the UniProt record and PubMed.

## Protein architecture

UniProt Q9NYJ7: signal peptide 1-26, extracellular topological domain 27-492,
transmembrane 493-513, cytoplasmic 514-618 — a single-pass type I membrane protein with a
DSL domain and six EGF-like repeats.
[file:human/DLL3/DLL3-uniprot.txt "SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass type I membrane protein"]
The DSL domain is the Notch-binding module
[file:human/DLL3/DLL3-uniprot.txt "The DSL domain is required for binding to the Notch receptor."]

## Function: a divergent, cis-inhibitory Notch ligand

DLL3 is a DSL-family member that does **not** trans-activate Notch. Chapman et al. showed
it inhibits signalling in the cell that expresses it, by interacting with Notch1 in the
late endocytic compartment and routing newly synthesised Notch1 to lysosomal degradation
before the receptor reaches the surface.
[PMID:21147753 "DLL3 is a divergent member of the DSL family of Notch ligands that does not activate signalling in adjacent cells, but instead inhibits signalling when expressed in the same cell as the Notch receptor."]
[PMID:21147753 "Dll3 targeting newly synthesized Notch1 for lysosomal degradation prior to post-translational processing and cell surface presentation of the receptor."]

Geffers et al. showed DLL1 and DLL3 are not interchangeable in vivo: Dll3 knocked into the
Dll1 locus does not rescue, and DLL1 but not DLL3 activates Notch in Drosophila wing discs.
[PMID:17664336 "Dll3 does not compensate for Dll1; DLL1 activates Notch in Drosophila wing discs, but DLL3 does not."]

## Localization — important for this review

Endogenous DLL3 is an intracellular, Golgi/late-endosomal membrane protein, **not** a
cell-surface ligand under physiological conditions.
[PMID:17664336 "In contrast to endogenous DLL1 located on the surface of presomitic mesoderm cells, we find endogenous DLL3 predominantly in the Golgi apparatus."]
[PMID:21147753 "we report that Dll3 is not presented on the surface of presomitic mesoderm (PSM) cells in vivo, but instead interacts with Notch1 in the late endocytic compartment"]

The exception is pathological overexpression: in SCLC and LCNEC, DLL3 is upregulated and
aberrantly trafficked to the plasma membrane, which is the basis of the DLL3-directed ADC
and T-cell-engager therapeutics (rovalpituzumab tesirine, tarlatamab).
[PMID:26311731 "DLL3 protein was detectable at the surface of SCLC and LCNEC tumor cells"]
[PMID:26311731 "establishing that DLL3 protein can localize to the cell surface and is not necessarily confined to the Golgi"]
[PMID:37355629 "DLL3 expression is low and mainly confined to the Golgi apparatus and cytoplasmic vesicles in normal cells but is upregulated and traffics to the surface of SCLC cells"]

Conclusion for GO: the primary location is Golgi membrane plus late endosome; `cell
surface` is a genuine but condition-specific (tumour) location; `plasma membrane` as the
site where DLL3 is *active* is not supported for the normal protein.

## Disease

Biallelic DLL3 mutations cause autosomal recessive spondylocostal dysostosis (vertebral
segmentation defects), reflecting a requirement in somitogenesis.
[PMID:10742114 "we have cloned and sequenced human DLL3 to evaluate it as a candidate gene for SD and identified mutations in three autosomal recessive SD families"]

## Review decisions

- `plasma membrane` (IBA is_active_in; IEA located_in): MODIFY to Golgi membrane. The
  PAINT node assertion is right for the Delta/Serrate clade but DLL3 has target-specific
  evidence of divergence in trafficking (Geffers, Chapman).
- `Notch signaling pathway` (IBA, IEA): MODIFY to negative regulation of Notch signaling
  pathway — a sign correction, not a refinement.
- `membrane` (IEA, NAS): MODIFY to Golgi membrane.
- `animal gross anatomical part developmental process` (ARBA IEA): TOO_GENERAL; skeletal
  system development, accepted here, entails it.
