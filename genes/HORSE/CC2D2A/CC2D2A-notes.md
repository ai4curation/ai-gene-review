# CC2D2A: paired human–horse review notes

## Biological evidence

Mouse loss-of-function, rescue and microscopy connect CC2D2A to mother-centriole appendages, ciliary assembly and transition-zone elaboration. Loss disrupts cilia-dependent Shh signaling and embryonic laterality/neural development. These developmental roles arise through ciliary organization.

- [PMID:24947469: Ciliopathy-associated gene Cc2d2a promotes assembly of subdistal appendages on the mother centriole during cilia biogenesis.](https://pubmed.ncbi.nlm.nih.gov/24947469/) — full text cached.
- [PMID:22179047: A ciliopathy complex at the transition zone protects the cilia as a privileged membrane domain.](https://pubmed.ncbi.nlm.nih.gov/22179047/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

Horse N-terminal deletions align within the human predicted disordered1–241region, while the long coiled-coil/C2 architecture is retained. This supports broad ciliary/developmental transfer. Renal tubule ciliation defects alone do not resolve the more specific kidney-development claim, which remains UNC.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/CC2D2A/CC2D2A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Confirm the horse transcript model and distinguish renal morphogenesis from renal cilia/homeostasis. A calcium-binding molecular activity should not be invented solely from the C2 domain label.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research (`just deep-research-falcon HORSE CC2D2A --fallback perplexity-lite`) failed: falcon "Failed to authenticate" and perplexity returned HTTP 401 insufficient quota. The review uses cached primary literature instead (PMID:24947469, PMID:21725307 and PMID:21422230 with full text; PMID:22179047 abstract only).

### Identity of A0A5F5PJ44

- The horse gene ENSECAG00000025115 (VGNC:16103) has seven unreviewed TrEMBL models: A0A5F5PUW7 (1643 aa), F6Q4K5 (1638), F6Q4I1 (1633), A0A5F5PJA7 (1584), A0A5F5PL46 (1514), A0A5F5PS28 (1503) and A0A5F5PJ44 (1480). There is no reviewed horse entry.
- New analysis `CC2D2A-bioinformatics/compare_sequences_rereview.py` → `RESULTS-rereview.md` / `results-rereview.json` aligns all of them, plus mouse Q8CFW7, to human Q9P2K1 (1620 aa). The existing RESULTS.md was not modified.
- A0A5F5PJ44 is an **alternative splice model** of this gene, not a fragment. It starts at the Met equivalent to human Met50 (the start used by human isoform 2) and lacks human 147-239. Both gaps lie in the human predicted disordered region 1-241. The coiled coils (439-493, 532-582), the C2 domain (1025-1203, 179/179 paired) and the C-terminal region 1258-1620 (363/363) are all fully present. The benchmark lacks about 140 N-terminal residues of the canonical product but keeps every known domain.
- The gene-centric canonical model is **A0A5F5PUW7**. It pairs with 1619/1620 human residues and is the only horse model with GOA annotations (QuickGO: IBA rows for GO:0035869, GO:1904491 and GO:1905515 from PTN000464650, plus IEA rows). A0A5F5PJ44 has no GOA rows. That is why the review's `existing_annotations` are all NEW.

### Evolutionary grounding

- PANTHER PTHR20837:SF7 holds horse A0A5F5PJ44, human Q9P2K1 and mouse Q8CFW7. The paralog CC2D2B is in SF2. `interpro/panther/PTHR20837/PTHR20837-review.yaml` lists A0A5F5PJ44 as an SF7 representative, which agrees with this review.
- In `PTHR20837-paint.tsv`, node PTN000464650 (taxon 2759) carries ciliary transition zone, protein localization to ciliary transition zone and non-motile cilium assembly. Horse is inside that clade, so these three are added as NEW with IBA, mirroring the horse canonical model.
- PAINT left out MKS complex (mouse IDA, PMID:21725307 and PMID:22179047) and smoothened signaling at that eukaryote-wide node. MKS complex is added only as an ISS transfer from the mouse SF7 ortholog, where the complex was directly purified. Smoothened signalling, laterality, neural tube and kidney phenotypes are downstream consequences of losing cilia and are not annotated.
- Cilium assembly (GO:0060271) was replaced in core_functions by its descendant non-motile cilium assembly (GO:1905515), the term PAINT placed. Using both would be redundant.
- Subdistal appendage localization (mouse immuno-EM, PMID:24947469) is recorded as a suggested question, not an annotation, because it comes from a single study.

### Changes vs previous version

Rewrote the description, which now covers the domain architecture, MKS-module role and gene-model identity. Added four NEW rows. Changed core_function process from cilium assembly to non-motile cilium assembly. Added references PMID:21725307, PMID:22179047, PMID:21422230, the PAINT tsv, the horse UniProt record and RESULTS-rereview.md. All existing references were kept.

### Relative to review next

A0A5F5PUW7, the gene-centric canonical horse CC2D2A model (same gene). No review exists in the repo. Its folder would be `genes/HORSE/CC2D2A__A0A5F5PUW7`. The human ortholog Q9P2K1 already has a complete review (genes/human/CC2D2A, every annotation actioned).
