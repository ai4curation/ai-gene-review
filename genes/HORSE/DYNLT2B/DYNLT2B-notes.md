# DYNLT2B: exact horse protein model

**Finding:** the conserved region supports DYNLT2B-family identity, but this accession is not a straightforward full-length counterpart of the human light chain. All ten functional/localization predictions remain unresolved for the exact protein model.

The [reproducible comparison](DYNLT2B-bioinformatics/RESULTS.md) aligns 128 residues at 91.41% identity, covering 90.14% of human Q8WW35 and 52.24% of horse A0A9L0SWY1. A large N-terminal extension accompanies loss of human residues 129–142. The missing region includes most of the terminal beta-strand observed in the human DYNLT1–DYNLT2B heterodimer, PDB8RGI. [PMID:38454149](https://pubmed.ncbi.nlm.nih.gov/38454149/)

> Structure and tethering mechanism of dynein-2 intermediate chains in intraflagellar transport.

The observed human structure makes this more than an arbitrary percentage-identity concern. However, no folding, stability or binding experiment has established the effect of this exact horse alteration. A gene-model or translation discrepancy is plausible; an evolved horse-specific loss of function is not demonstrated. The sequence submitted to ProtNLM at prediction time is also unknown.

Human knockout and interaction studies strongly support the ordinary DYNLT2B role in retrograde IFT. The horse uncertainty should not be read as evidence against that conserved gene-family function. Human ciliary-base and MTOC localization, tagged-protein axonemal signal, and mouse sperm axonemal biology are separate observations with different transfer limits. [PMID:25830415](https://pubmed.ncbi.nlm.nih.gov/25830415/), [PMID:29742051](https://pubmed.ncbi.nlm.nih.gov/29742051/), [PMID:39827215](https://pubmed.ncbi.nlm.nih.gov/39827215/)

The human evidence synthesis and source-specific limits are recorded in the human notes and Falcon report. No horse-specific functional paper or reviewed horse record was identified for this accession, so the paired human research and protein-model analysis were used instead of an additional horse Edison request.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon HORSE DYNLT2B --fallback perplexity-lite` failed (falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient quota). No deep-research file was written; the review relies on the cached full-text papers (PMID:29742051, PMID:25830415, PMID:38454149, PMID:39827215), the human Swiss-Prot record and the human DYNLT2B review.

GOA has no annotations for A0A9L0SWY1 (header-only goa.tsv), so there were no existing rows to adjudicate.

### Identity of the benchmark accession (alternative gene model)

New analysis: `DYNLT2B-bioinformatics/compare_gene_models_rereview.py` -> `RESULTS-rereview.md`, `models-rereview.json` (existing RESULTS.md untouched). The equine gene ENSECAG00000015913 (chr 19) has ten UniProt/Ensembl protein models, all PTHR21255:SF7:

- Ensembl canonical transcript ENSECAT00000082191 = A0A9L0S150 (259 aa): same N-terminal extension as the benchmark, full human C-terminus, 100% human coverage, all five human strands paired.
- UniProt reference-proteome gene-centric entry = A0A9L0S9P8 (145 aa): full human C-terminus but divergent N-terminus with no initiator Met (GESSHSWLLTLIDLK...), i.e. it lacks the first human strand (SIGVSFSV) by identity even though the global alignment pairs positions there.
- A0A9L0TLH8 (148 aa) is the model closest to human Q8WW35 over its whole length (MAAPRDASFSAGVSF... ending ...DSLFCVVAAFGCFYY).
- A0A9L0SWY1 (benchmark, 245 aa): ~117-residue disordered N-terminal extension (MobiDB-lite disorder 23-83) plus a C-terminus that stops at ...VFMNK, i.e. lacks human residues 128-142 (final Tctex beta-strand). It is therefore an alternative gene model (alternative 3' exon / splice) of the same gene, neither the Ensembl canonical nor the UniProt gene-centric entry. Its Tctex core (human 1-127 equivalent) is 91% identical to human.

### Evolutionary grounding

PANTHER: horse and human DYNLT2B are both in PTHR21255:SF7 (DYNLT2B-specific subfamily); the family review interpro/panther/PTHR21255 agrees (it lists A0A9L0SWY1 and Q8WW35 as SF7 representatives), no placement disagreement. PAINT node PTN000478852 carries GO:0045505 dynein intermediate chain binding, GO:0005868 cytoplasmic dynein complex, GO:0007018 microtubule-based movement and GO:0005737 cytoplasm (seen as IBA on human Q8WW35). Retrograde IFT (GO:0035721) and cilium assembly rows on human are IMP-only and were not propagated by PAINT; I did not transfer them as annotations. Mouse sperm-flagellum phenotypes (PMID:39827215) are organismal and not annotated.

### Changes

- Description rewritten as a project-independent summary, with the gene-model caveat.
- Added two NEW ISO rows (GO:0045505, GO:0005868) grounded in SF7 orthology + PAINT family-node placement + human experiments; added core_function (MF GO:0045505, complex GO:0005868), deliberately no directly_involved_in process.
- Added reference to RESULTS-rereview.md; replaced the Ensembl-name quote on the UniProt reference with the Ensembl cross-reference line. All earlier references retained.
- Status set to COMPLETE.

Next relative: canonical product of the same gene, UniProt gene-centric A0A9L0S9P8 (folder would be genes/HORSE/DYNLT2B__A0A9L0S9P8). Caveat: S9P8 itself has a divergent, Met-less N-terminus; A0A9L0TLH8 is the human-like full-length model and A0A9L0S150 the Ensembl canonical. Whichever is chosen, the experimentally characterised orthologue is human Q8WW35, already reviewed (genes/human/DYNLT2B).

## 2026-10-21 — NEW rows withdrawn from the alternative gene model (PR #5303 review)

The re-review had proposed NEW rows (GO:0045505, GO:0005868) on this benchmark accession because GOA propagates the
gene's annotations, including PAINT IBA rows, to one representative product per gene and not to
alternative transcript models. Neither horse DYNLT2B product has GOA rows; the same two terms are
proposed as NEW on the canonical product (DYNLT2B__A0A9L0S9P8, reviewed in
`genes/HORSE/DYNLT2B__A0A9L0S9P8/`). A gene-level proposal belongs on one representative product, so
the duplicate rows on this alternative model were withdrawn for consistency across the cohort. The gene-level function is unchanged and is recorded on the
canonical product's review; this file's description and core functions still describe it.
