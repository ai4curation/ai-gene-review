# DarB curation notes

## 2026-11-04

Normally fetched O31698/BACSU; no source GOA annotations were returned. Raw files are pinned in the audit baseline. Falcon research was attempted and failed with HTTP 403 authentication; manual primary-source review supplies the evidence. The initial version retained the directly established functions only in core_functions; the PR review follow-up below supersedes that choice.

PMID:33619274 assays Rel synthesis and hydrolysis with apo- and ligand-bound DarB; DarB alone does not synthesize pppGpp. PMID:35714772 establishes the CBS-domain homodimer and ligand binding. PMID:36652515 resolves the DarB-Rel complex and supports direct activation of the Rel synthesis domain, with inhibition of Rel hydrolysis. PMID:35130724 identifies pyruvate carboxylase as a second direct target of apo-DarB; this must not be confused with direct inhibition of Listeria pyruvate carboxylase by the nucleotide.

Core activities are cyclic-di-AMP binding (GO:0180001) and enzyme activator activity (GO:0008047), both verified in QuickGO. No partner catalytic function is assigned to DarB. The receptor activity belongs to the DarB variant of MODULE:bacterial_c_di_amp_signaling; detailed Rel catalysis and central metabolism are outside that module boundary. PANTHER's broad family PTHR43080 bears a mitochondrial plant-protein label; the source-backed bacterial subfamily is PTHR43080:SF30 CYCLIC DI-AMP RECEPTOR B. Do not infer bacterial localization from the parent-family label.

## 2026-11-04 — PR #5997 review follow-up

Direct molecular evidence warrants NEW annotation recommendations even when the GOA seed is empty. Added cyclic-di-AMP binding and enzyme activator activity with IDA evidence; the two terms describe independent binding and regulatory functions. [PMID:35714772 "We also confirm the DarB dimer binds two cyclic dinucleotide molecules or two AMP molecules"] [PMID:35130724 "Both the interaction and the activation of enzyme activity require apo-DarB and are inhibited by c-di-AMP."] No partner catalytic activity or new biological-process assertion is assigned to DarB.
