# CTDSP2 (horse, A0A9L0T5X1) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Scope.** A0A9L0T5X1 is the 312-aa product of ENSECAT00000107019, the Ensembl canonical transcript of the horse CTDSP2 gene (ENSECAG00000018788, chr6). It is the full-length catalytic counterpart of the truncated benchmark accession F7A4N8 (`genes/HORSE/CTDSP2/`). It gets its own folder (`CTDSP2__A0A9L0T5X1`) because it is a separate UniProt entry. It was fetched with `just fetch-gene HORSE A0A9L0T5X1 --alias CTDSP2__A0A9L0T5X1`. ProtNLM2 files were not opened.

**Deep research.** `just deep-research-falcon HORSE CTDSP2__A0A9L0T5X1 --fallback perplexity-lite` failed. Falcon returned 403 Forbidden on auth/login ("Failed to authenticate"), and the perplexity-lite fallback also failed. No deep-research file exists. The literature used here is the human CTDSP2 set already cached in `publications/` (PMID:12721286, PMID:16724108, PMID:16882717 and PMID:15681389, all abstract-only). The quotes are the same ones used, and validated, in `genes/human/CTDSP2/CTDSP2-ai-review.yaml`. No horse-specific experimental study of CTDSP2 is known, so every function claim here is an orthology inference.

**Evolutionary grounding.**
- PANTHER 19.0 classification (`.cache/panther/panther-members-19.0.tsv`) puts human O14595, cow Q2KJ43 and mouse Q8BX07 CTDSP2 in PTHR12210:SF187. Human and mouse CTDSP1 are in SF139 and human CTDSPL is in SF43.
- Horse is not a PANTHER reference proteome. InterPro assigns A0A9L0T5X1 to PTHR12210 at the family level only.
- `CTDSP2__A0A9L0T5X1-bioinformatics/map_catalytic_residues.py` produces `RESULTS.md`. Over the horse catalytic region (175 aa from residue 138), A0A9L0T5X1 is 100% identical to cow CTDSP2, 99.4% to human and 96.6% to mouse. It is 82.3% identical to CTDSPL and 78.3% to CTDSP1. Over the human FCP1 domain (97-255), 158 of 159 residues are identical. The sibling analysis `genes/HORSE/CTDSP2/CTDSP2-bioinformatics/RESULTS-rereview.md` builds an NJ tree that places A0A9L0T5X1 with the CTDSP2 orthologs. Together with VGNC naming, this fixes the protein as the CTDSP2 ortholog within the SCP clade.
- Catalytic residues are all conserved. Human D107, the phosphoaspartyl nucleophile, is horse D148. Human D109 (proton donor) is D150. The transition-state residues T163 and K201 are T204 and K242, and the Mg2+ ligand N218 is N259. There is no evidence of pseudoenzyme divergence.
- PAINT (`interpro/panther/PTHR12210/PTHR12210-paint.tsv`) has a single IBD at the SCP node, PTN000954535: GO:0008420, seeded by O14595 and Q9GZU7. No location or process terms were propagated from that node. I read this as a deliberate choice, so I did not add NEW annotations for nucleus, protein dephosphorylation or BMP signalling. These appear only in core_functions, flagged as orthology-inferred, which accounts for the four expected validator warnings.

**Gene-model caveat.** The predicted N-terminus does not start with Met. It is a 37-aa stretch with no human counterpart, inside the region UniProt predicts as disordered (MobiDB-lite 1-67). The model also skips the exon encoding human SDLLQCLQYQFYQ (residues 72-84). The alternative model A0A9L0R207 (252 aa) keeps that exon but lacks a different one. Both changes fall outside the FCP1 domain and do not affect the catalytic inference.

**Decisions (5 GOA rows, all electronic or IBA).**
- GO:0004722 (IEA, EC mapping): ACCEPT. The EC/ARBA name is not itself support. The acceptance rests on orthology, conserved active-site residues, and the fact that this term covers Smad1 dephosphorylation.
- GO:0006357 (IEA, inter-ontology): MODIFY to GO:0000122 negative regulation of transcription by RNA polymerase II, as in the human review.
- GO:0008420 (IBA): ACCEPT. The protein is inside the PTN000954535 clade on sequence grounds, and nothing indicates loss.
- GO:0008420 (IEA, GO_REF:0000120): ACCEPT, consistent with the IBA row.
- GO:0016791 (IEA, InterPro): MODIFY to GO:0008420 plus GO:0004722.

**Experimentally established in horse:** nothing. **Inferred by orthology:** CTD Ser5 phosphatase activity, Smad1 C-terminal phosphatase activity, nuclear location, and repression of RNA Pol II transcription.
