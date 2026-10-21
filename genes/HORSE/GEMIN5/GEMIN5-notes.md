# GEMIN5: paired human–horse review notes

## Biological evidence

Primary RNA-bound structures establish cap/snRNA recognition by tandem WD40 propellers. Direct SMN-UTR binding and ribosome experiments establish transcript-dependent translation regulation. Generic physical interactions are not substituted for these specific molecular activities.

- [PMID:27881600: Structural insights into Gemin5-guided selection of pre-snRNAs for snRNP assembly.](https://pubmed.ncbi.nlm.nih.gov/27881600/) — abstract cached; full-text availability must be checked separately.
- [PMID:27881601: Structural basis for snRNA recognition by the double-WD40 repeat domain of Gemin5.](https://pubmed.ncbi.nlm.nih.gov/27881601/) — full text cached.
- [PMID:25911097: Gemin5 Binds to the Survival Motor Neuron mRNA to Regulate SMN Expression.](https://pubmed.ncbi.nlm.nih.gov/25911097/) — full text cached.
- [PMID:27507887: The RNA-binding protein Gemin5 binds directly to the ribosome and regulates global translation.](https://pubmed.ncbi.nlm.nih.gov/27507887/) — full text cached.
- [PMID:11714716: Gemin5, a novel WD repeat protein component of the SMN complex that binds Sm proteins.](https://pubmed.ncbi.nlm.nih.gov/11714716/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The horse model lacks human723–798, spanning the end of the WD40 RNA-recognition module. Nuclear/cytoplasmic localization remains plausible, but specific RNA recognition and assembly require the module integrity to be resolved. Protein ubiquitination has no demonstrated mechanistic role in the retrieved sources; being a ubiquitination substrate would not establish that process.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/GEMIN5/GEMIN5-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Inspect the deletion in the tandem-propeller structure and check horse transcripts. Resolve high-throughput partner rows from supplementary records; do not infer their validity from other known GEMIN5 interactions.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Deep research.** `just deep-research-falcon HORSE GEMIN5 --fallback perplexity-lite` failed. Falcon/Edison returned "Failed to authenticate" (403), and the perplexity-lite fallback also failed. No deep-research file was produced. This review rests on the cached primary literature (PMID:16857593, PMID:11714716, PMID:27881601, PMID:25911097) and on new sequence analysis.

**Identity of the benchmark accession: alternative-transcript isoform.** UniProt has four horse GEMIN5 entries, all from Ensembl gene ENSECAG00000020479.3. Analysis, scripts and raw output are in `GEMIN5-bioinformatics/rereview/` (`RESULTS-rereview.md`).
- F6WDM0 (1517 aa) is full length relative to human Q8TEQ6 (1508 aa), with no missing human segment. It carries the VGNC name and the PAINT IBA rows (PTN005299808) in GOA. This is the canonical horse product.
- A0A9L0R5P7 (benchmark, 1433 aa; ENSECAT00000103662.1) lacks a 76-aa block equivalent to human 723-798. Otherwise it is 89% identical to human.
- A0A3Q2H9B3 (1420 aa) is C-terminally truncated. A0A9L0TIL3 (1471 aa) lacks the block equivalent to human 799-836.

**Correction to the earlier entry.** The earlier notes said the deletion "spans the end of the WD40 RNA-recognition module". In the solved structure the folded tandem WD40 region is residues 3-722 [PMID:27881601 "The 2.0 Å structure shows that the G5N region encompassing residues 3–722 is folded into two seven-bladed WD40 repeat domains."]. The missing block begins at 723, in a region human UniProt annotates as disordered (715-790). That region carries phosphosites (T751, S757, S770, S778) and a SUMO2 acceptor lysine (K754). All 12 RNA-contact residues mutated in PMID:27881601 are conserved in A0A9L0R5P7. The isoform therefore keeps the snRNA/cap-recognition module intact, together with the C-terminal TPR-like and RBS regions.

**Evolutionary grounding.** A0A9L0R5P7, F6WDM0 and human Q8TEQ6 all fall in PTHR46362:SF1. PAINT node PTN005299808 propagates spliceosomal snRNP assembly, SMN complex, nucleus (is_active_in) and mRNA 3'-UTR binding. PAINT did not propagate snRNA binding or cap binding, although human has IDA support for both. I treated that omission as deliberate: snRNA binding is not added as a NEW annotation. I kept it as the molecular function of the core function, because it rests on the human structure plus residue-level conservation in this isoform, not on a PAINT transfer. The question is raised in suggested_questions.

**Changes to the review.**
- GO:0003730 mRNA 3'-UTR binding: UNDECIDED changed to ACCEPT. The deletion is outside the RNA-binding modules, and PAINT places the term at the gene's node.
- Cytoplasm: ACCEPT. Nucleoplasm and gems: KEEP_AS_NON_CORE (minor pool). These actions are unchanged; the reasons were rewritten.
- NEW (ISS from human, matching the PAINT IBA on F6WDM0): GO:0000387 spliceosomal snRNP assembly and GO:0032797 SMN complex. Participation test: GEMIN5 itself selects and delivers the snRNA, so it does part of the work of assembly and is not a substrate of the process.
- No translation-regulation or ribosome-binding process term was added. GO:0006417 appears only in the core-function narrative.
- The description was rewritten to be project-independent, and it now states the isoform status correctly.
- The old `RESULTS.md` is kept. It is now marked DISPUTED in reference_review because of its WD40-boundary wording, and it is no longer cited as support.

**Relative.** The canonical product of the same gene, F6WDM0, has no review in the repo. A future folder would be `genes/HORSE/GEMIN5__F6WDM0`. The human ortholog (genes/human/GEMIN5) is fully reviewed. The PANTHER family review `interpro/panther/PTHR46362/PTHR46362-review.yaml` agrees with the SF1 placement. It lists the benchmark isoform A0A9L0R5P7 as a representative member; F6WDM0 would be the better representative. No module in modules/ references GEMIN5.
