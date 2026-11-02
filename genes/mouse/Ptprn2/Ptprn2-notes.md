# Ptprn2 (mouse, P80560) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. Deep research could not be generated: `just deep-research-falcon mouse Ptprn2 --fallback perplexity-lite`
failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). The review is based on cached
publications, the UniProt record, QuickGO and a small sequence comparison.

### Evolutionary grounding
- Mouse P80560, rat Q63475 and human Q92932 are all in PANTHER PTHR46106:SF5 (UniProt DR PANTHER lines).
- Mouse vs rat 92.9% identity; rat catalytic Cys934 = mouse Cys931, identical context PIIVHCSDGAGR
  (`Ptprn2-bioinformatics/RESULTS.md`, `compare_orthologs.py`).
- PAINT: PTN000439769 (IA-2 family) carries secretory granule, synapse, regulation of secretion; PTN000439772
  (vertebrate IA-2/IA-2beta) carries insulin secretion in response to glucose. Mouse Ptprn2 (MGI:107418) is a donor.
  No IA-2 family member has an experimental GO annotation for phosphoinositide phosphatase activity (rat Q63475 QuickGO
  2026-10-20), so the absence of PIPase from PAINT is not a curator decision against it.

### Experimentally established in mouse
- Dense-core granule and synaptic vesicle membrane (fractionation, synaptosome biotinylation, synapsin colocalization)
  [PMID:19361477 "IA-2beta, but not IA-2, co-purifies with fractions rich in synaptic vesicles (SV)"].
- Presynaptic axon terminals of PV+ interneurons in mouse hippocampus [PMID:27630542 "immunoelectron microscopy revealed phogrin staining in axon terminals of symmetrical synapses"].
- Single KO: reduced insulin content, GSIS, DCV number and half-life [PMID:21732083 "Islets from single and DKO mice all showed a significant decrease in insulin content, insulin secretion and the number and half-life of DCV"];
  [PMID:15220191 "showed mild glucose intolerance and impaired glucose-stimulated insulin secretion"].
- Overexpression in MIN6 inhibits GSIS [PMID:16418280].
- Homo/heterodimerization with Ptprn and RPTPs [PMID:12364328 "IA-2 and IA-2beta are capable of homo- and heterodimerization"].
- Enzymatically inactive as a PTP [PMID:15220191 "is an enzymatically inactive member of the transmembrane protein tyrosine phosphatase family"].
- DKO-only phenotypes (neurotransmitter content/release, female infertility via LH [PMID:16269463], renin [PMID:19019914])
  are downstream/indirect; not annotated as process participation beyond the existing neurotransmitter secretion IMP (kept non-core).

### Inferred, not shown in mouse
- Phosphatidylinositol phosphate phosphatase activity, from rat phogrin [PMID:20097759 "phogrin is able to dephosphorylate specific inositol phospholipids"]
  — added as NEW with ISS.

### Decisions
- REMOVE IEA protein tyrosine phosphatase activity (catalytically inactive toward phosphoproteins).
- REMOVE ISO negative regulation of GTPase activity: rat donor annotation no longer present in QuickGO; no supporting biology.
- MARK_AS_OVER_ANNOTATED ISO ER lumen (type I TM protein; biosynthetic transit only).
- MODIFY secretory granule / secretory granule membrane rows -> dense core granule membrane (GO:0032127);
  synapse, presynapse, transport vesicle membrane -> synaptic vesicle membrane.
- MODIFY protein binding (IPI with Ptprn) -> protein heterodimerization activity.
- UNDECIDED signaling receptor complex (human IDA source PMID:23382219 does not mention PTPRN2 in cache), consistent with human review.
