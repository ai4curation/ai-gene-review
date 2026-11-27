# IRF5 notes

## Deep research

`just deep-research-falcon human IRF5 --fallback perplexity-lite` could not run in this workspace: the research client exposed only `claude_code`, while both `falcon` and the `perplexity` provider used by the fallback were unavailable. I did not run a Claude Code deep-research job because this lane is limited to the current Codex writer and no extra sub-workers.

## Manual synthesis

IRF5 is a latent IRF-family transcriptional activator in innate immune cells. Virus and pattern-recognition-receptor pathways induce phosphorylation-dependent nuclear accumulation and target-gene transcription [PMID:12138184, "Mutation of these residues from serine to alanine dramatically decreased phosphorylation and resulted in a substantial loss of IRF-5 transactivation in infected cells"], and IRF5/IRF7 dimerization can change IFNA enhanceosome assembly and IFNA subtype expression [PMID:12600985, "formation of IRF-5/IRF-7 heterodimers occurs through the amino terminus resulting in a masking of the DNA binding domain"].

Multiple papers support IRF5 as the transcriptional effector downstream of innate immune adapters. RIP2/NOD2 activation can drive IRF5-regulated IL12p40, IFNA14, and IFNB reporter transcription [PMID:22412986]. In TLR9-stimulated human plasmacytoid dendritic cells, IRF5 contributes to MyD88/TRAF6-dependent IFN-beta and IL-6 induction [PMID:23616277, "IRF-5 and NF-κB p50 are key co-regulators of IFN-β and IL-6 expression following TLR9-mediated activation of human pDCs"]. IKK-beta phosphorylation drives IRF5 dimerization and nuclear translocation [PMID:25326418, "IKKβ phosphorylated IRF5 at Ser462 in vitro and induced the dimerization of wild-type IRF5"], and TASL licenses IRF5 phosphorylation downstream of endolysosomal TLR7/8/9 signaling [PMID:32433612, "recruitment and activation of IRF5. This finding shows that TASL is an innate immune adaptor for TLR7, TLR8 and TLR9 signalling"].

I treated nuclear DNA-binding transcriptional activation of inflammatory and type I IFN genes as the core function, cytoplasmic/cytosolic rows as the latent pre-activation state, and NOD2/TLR/cytokine-response process annotations as real pathway contexts in which IRF5 performs that core transcriptional work.
