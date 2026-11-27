# IRF1 notes

## Deep research

`just deep-research-falcon human IRF1 --fallback perplexity-lite` could not run in this workspace: the research client exposed only `claude_code`, while both `falcon` and the `perplexity` provider used by the fallback were unavailable. I did not run a Claude Code deep-research job because this lane is limited to the current Codex writer and no extra sub-workers.

## Manual synthesis

IRF1 is a nuclear IRF-family sequence-specific transcription factor for ISRE/IRF elements. The shared biochemical DNA-binding evidence for IRF1 and IRF2 identifies nearly indistinguishable IRF recognition sequences in type I interferon and interferon-inducible promoters [PMID:7687740, "sequences selected by this method and the affinities for each sequence were virtually indistinguishable between IRF-1 and IRF-2"].

Its direct cellular role is transcriptional regulation, with both activating and repressive outputs. Human IRF1 was assayed as a positive regulator on IFN-beta response genes, p53-dependent transcription, PUMA, POLH, and other targets [PMID:15509808; PMID:17516545; PMID:19851330; PMID:22367195]. ZBED2 antagonizes IRF1 at co-occupied promoter elements in pancreatic cancer cells, further supporting IRF1 as a promoter-bound activator of interferon-stimulated genes [PMID:32385160, "antagonism of IFN regulatory factor 1 (IRF1)-mediated transcriptional activation at cooccupied promoter elements"].

Several immune and cell-growth annotations describe consequences of that transcriptional program rather than separate molecular functions. I kept broad innate/adaptive immune and antiviral terms where they summarize curated IRF1 target-gene biology, kept cell-cycle/apoptosis rows as non-core transcriptional outputs, and treated generic DNA-binding/transcription terms as too broad only when the row's own evidence was generic and a specific accepted descendant was already present.
