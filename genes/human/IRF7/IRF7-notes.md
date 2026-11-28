# IRF7 notes

## Deep research

`just deep-research-falcon human IRF7 --fallback perplexity-lite` could not run in this workspace: the research client exposed only `claude_code`, while both `falcon` and the `perplexity` provider used by the fallback were unavailable. I did not run a Claude Code deep-research job because this lane is limited to the current Codex writer and no extra sub-workers.

## Manual synthesis

IRF7 is the signal-activated IRF transcription factor that amplifies type I interferon transcription. After viral or TLR stimulation, phosphorylation of latent cytoplasmic IRF7 promotes dimerization, nuclear accumulation, promoter binding, and IFNA/IFNB transcriptional activation; acetylation of Lys-92 in the DNA-binding domain impairs DNA binding and illustrates direct regulatory control of its core activity [PMID:12374802, "Mutation of lysine 92 resulted in complete abolition of DNA binding ability"].

Human and Reactome evidence both place activated IRF7 at IFN-alpha/beta promoters and in nuclear VAF/CBP/p300 transcriptional complexes [PMID:16127453; PMID:17404045; Reactome:R-HSA-1028819; Reactome:R-HSA-933531]. The numerous cytosol Reactome annotations represent the pre-activation and adapter-recruited state of the same protein, not the final site of transcriptional activity.

I kept core sequence-specific DNA-binding transcription-factor and type I IFN-production annotations, kept broader antiviral/innate-immune terms where they summarize that pathway role, and removed uninformative viral or HTP bare protein-binding rows unless the row supported a more specific function.
