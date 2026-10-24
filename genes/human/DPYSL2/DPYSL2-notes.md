# DPYSL2 review notes


## 2026-09-20 full-gene IBA re-review

All 46 annotations assessed: positive/negative catalytic and BP assertions, cytoskeletal and membrane localizations, all interaction sources, Reactome cytosol rows, endocytosis, signal transduction and nervous-system development.

Existing OpenScientist report: DPYSL2-hypotheses/function-hypothesis-go-0016812/openscientist.md. It identifies the lost metal-binding/carboxylated-lysine apparatus. PMID:28044206 directly describes the human CRMP2 active-site loss; PMID:23373749 is a CRMP5 negative assay, not direct DPYSL2 assay. These primary references and report findings are now incorporated. Specific cyclic-amide and mapped ancestral hydrolase rejections remain, without universal claims about every CRMP.

PMID:23373749 directly compares CRMP1/2 oligomerization and describes CRMP signaling/transport. Supported self-association is core ACCEPT; it is not equivalent to generic protein binding. Signal transduction is core ACCEPT. PMID:20801876 supports an endocytic motor-linkage role; endocytosis restored to core ACCEPT. PMID:16260607 demonstrates kinesin-Sra1/WAVE1 linkage, so that generic interaction now MODIFY to molecular adaptor activity.

Legacy GO:0006139 TAS PMID:8973361 is UNDECIDED. The accessible abstract reports cloning, homology and expression; it does not establish absence of any assays throughout the unavailable full text. Loss of cyclic-amide catalysis does not exclude every metabolic process. Existing OpenScientist coverage is incorporated with that limit; no duplicate adjudication requested. Primary-full-text/curator question: what specific nucleobase/nucleotide/nucleic-acid metabolic step was intended for DRP/CRMP2, and does it involve a noncatalytic contribution? Status reviewed with follow-up.

Verified the proximate IBA PANTHER nodes from cached WITH/FROM fields and revised structured propagation metadata to match final decisions; no relationship-field reasoning, donor-count argument, or invented topology reconstruction was used.

The DPYSL2 OpenScientist report addresses cyclic-amide activity; the CRMP1 OpenScientist report explicitly extends legacy metabolic-removal recommendations to CRMP2. Added the latter as a comparative reference with its stated abstract-only provenance; this does not settle the shared PMID:8973361 full-text question.
