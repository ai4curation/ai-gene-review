# IRF2 notes

## Deep research

`just deep-research-falcon human IRF2 --fallback perplexity-lite` could not run in this workspace: the research client exposed only `claude_code`, while both `falcon` and the `perplexity` provider used by the fallback were unavailable. I did not run a Claude Code deep-research job because this lane is limited to the current Codex writer and no extra sub-workers.

## Manual synthesis

IRF2 shares the IRF N-terminal DNA-binding specificity with IRF1 and binds IRF-E/ISRE motifs in RNA polymerase II promoters [PMID:7687740]. It can activate transcription, as in the human histone H4 Site II assay [PMID:9540062], but its characteristic activity is promoter-bound repression of interferon-stimulated genes.

The newer HUSH2 work is especially direct for IRF2's chromatin-repressor function: TASOR2-containing HUSH2 is recruited by IRF2 to repress ISGs [PMID:39013473]. The HCFC2 work also supports IRF2 binding at the Tlr3 promoter and a positive contribution to Tlr3 expression in mouse macrophages [PMID:28970238].

I therefore kept both broad RNA-polymerase-II transcription-regulator terms and the specific activator/repressor molecular-function rows. The HPA cell-junction call is peripheral to the known nuclear/chromatin role, while the cytosol rows are left undecided because the local HPA/Reactome records do not directly show that compartment for IRF2. The many HTP/bare protein-binding rows should be removed under the protein-binding policy unless they name a supported specific molecular function.
