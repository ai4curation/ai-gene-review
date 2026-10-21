# PPP4R4 notes


## 2026-09-08 paired review

Selected accession A0A9L0S961; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/PPP4R4/PPP4R4-notes.md). [Sequence comparison](PPP4R4-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

The primary affinity-purification study identifies PP4R4 as a stable PP4c-specific partner and distinguishes it from PP2A/PP6 interactions and other PP4 regulatory complexes. PP4R4-associated activity toward fluorogenic substrate and gammaH2AX is lower than free PP4c and different from PP4R2/3-associated activity. This supports a regulatory subunit and an inhibitory effect in the tested assays, but does not establish that it inhibits all physiological PP4 substrates. It also does not establish blastocyst hatching. The selected horse sequence is nearly full-length and highly conserved, allowing stronger transfer of complex membership than a particular developmental phenotype.

Sources: [PMID:18715871](https://pubmed.ncbi.nlm.nih.gov/18715871/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not use ProtNLM2 output or any prediction-review file.

**Deep research.** `just deep-research-falcon HORSE PPP4R4 --fallback perplexity-lite` failed. Falcon gave
"Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (quota exceeded). No
deep-research file was written. The literature below was read directly from Europe PMC and the publication
cache.

**Identity of the benchmark accession.** The full analysis is in
[RESULTS-rereview.md](PPP4R4-bioinformatics/RESULTS-rereview.md) and `compare_horse_models_rereview.py`.
- UniProt has ten horse PTHR21467 entries. All are translations of one Ensembl gene,
  ENSECAG00000019485 (PPP4R4, chromosome 24).
- The UniProt gene-centric canonical product is A0A9L0S938 (869 aa). The Ensembl canonical transcript
  encodes A0A9L0RAK5 (908 aa, N-terminally extended).
- A0A9L0S961 (865 aa) is an alternative product. It is identical to A0A9L0S938 over residues 1-861. Its
  C-terminus `...ATFLNI` replaces the conserved `...ATLKSRKSNP` found in the canonical horse and human
  (873 aa) proteins. The change falls in the disordered C-terminal tail.
- A0A9L0S961 keeps both HEAT repeats and the ARM-like body. It also keeps the PP4c-interface residues
  R501 and V618, whose mutation abolishes PP4c binding in human (UniProt Q6NUP7 MUTAGEN, PMID:18715871).
- It is an alternative C-terminal isoform, not a fragment, and nothing needed for function is missing.

**Evolutionary grounding.** A0A9L0S961 is in PTHR21467:SF0, the only subfamily, together with human
Q6NUP7. PAINT node PTN001087371 propagates GO:0019888, GO:0005829 and GO:0008287 from Q6NUP7. QuickGO
shows those IBA rows on the horse canonical A0A9L0S938 but not on A0A9L0S961. Ensembl Compara
projections are on A0A9L0RAK5. The missing IBAs on this accession are therefore an artefact of which
entry the pipeline treats as canonical. PAINT did not propagate the human IDA inhibitor terms
(GO:0004864/GO:0004865), and I treat that omission as deliberate.

**Literature.**
- PMID:18715871 (abstract only) is still the only functional study. It shows that PP4R4 is PP4c-specific,
  forms a stable cytosolic heterodimer, and is independent of the PP4R1, PP4R2/R3 and alpha4 complexes.
  PP4c-PP4R4 is less active than free PP4c toward the tested substrates.
- PMID:34845248 (full text) measures PP4c-PP4R4 directly as one of the PP4 holoenzymes. PP4R4 binding is
  largely insensitive to loss of LCMT1 methylation.
- PMID:37605615 (full text) states "The function of PP4R4 in cells has not been reported".
- No horse-specific functional data exist.

**Changes from the 2026-09-08 review.**
- GO:0005737 cytoplasm (IEA): changed from ACCEPT to MODIFY, with GO:0005829 cytosol as the replacement.
  The general term is correct, but cytosol is supported and is the core-function location.
- NEW GO:0019888 protein phosphatase regulator activity (IBA, PTN001087371). The same gene's canonical
  entry already carries it.
- NEW GO:0030289 protein phosphatase 4 complex (ISS). Its only parent is GO:0008287. The other PP4
  subunits (PPP4R1, PPP4R2, PPP4R3A, PPP4C) carry GO:0030289 in human GOA, so the specific term is the
  convention. I did not also add GO:0008287 because it is the parent.
- gene_symbol set to PPP4R4, the Ensembl gene name. The TrEMBL record has no GN line.
- The description was rewritten as a standalone summary. It now includes the identity of the isoform.
- in_complex was added to core_functions.

**Relative.** The benchmark is an alternative isoform. The canonical product of the same gene, A0A9L0S938,
has no review in the repo, so it is the next relative to review. Its folder would be
genes/HORSE/PPP4R4__A0A9L0S938. The closest characterised ortholog is human PPP4R4 (Q6NUP7), which has a
COMPLETE review. That review leaves its five GO:0005515 IPI rows as UNDECIDED instead of applying the
protein-binding policy.

**Family/modules.** interpro/panther/PTHR21467 lists A0A9L0S961 and Q6NUP7 as SF0 representatives. Its
subfamily placement agrees with this review. No module in modules/ mentions PPP4R4, Q6NUP7 or PTHR21467.
