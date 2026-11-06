# nspC (CAMJ8) manual annotation review notes

## 2026-11-05

Applied annotation-reviewer and core-function-synthesizer guidance. Original annotation payloads are preserved; only review blocks were changed on seeded rows. No raw UniProt/GOA file was refreshed.

Default Falcon was attempted through `just deep-research-falcon CAMJ8 nspC` and failed with HTTP 403 authentication error. The complete failure log is `nspC-falcon-attempt.log`; this file is manual research, not a provider report.

Sources read: PMID22025614 (full text), PMID20534592 (full text after a normal force-fetch retry), PMID36283333 (abstract only; publisher access failed), PMID37878710 (full text), PMID19196710 (full text), the frozen UniProt record and PTHR43727 family review. QuickGO on 2026-11-05 confirms GO:0102143 includes carboxyspermidine chemistry; GO:0102144 is obsolete. Specific CASDC name searches returned no active term; reaction-specific NTRs avoid using broad carboxy-lyase as a falsely specific activity.

The 2011 native experiments used C. jejuni 81116, not NCTC 11168. The loci are C8J_0166 (CASDH candidate) and C8J_1418 (CASDC). [PMID:22025614, "All strains were derived from the sequenced C. jejuni strain 81116 (NCTC 11828)"] The CASDH deletion increased spermidine and grew normally; the CASDC deletion abolished spermidine and complementation restored it. The paper contains an inconsistent methods sentence naming 11168 and a C8J_0715 CASDC deletion, whereas its experimental overview, results, and figures identify 81116/C8J_1418; do not turn that sentence into direct evidence on NCTC 11168.

PMID20534592 directly assays the 81116 CASDC on synthetic carboxyspermidine and carboxynorspermidine. Its clone had an accidental E184K mutation that was repaired before the reported assays. RCSB 3N29 maps to A8FNH9, not Q0P8A4; the C-terminal 382 residues of the deposited tagged sequence match 374/382 residues of Q0P8A4 by direct position comparison. Thus Cj1515c receives close-homolog inference, not IDA. [PMID:20534592, "The gene for Cj CANSDC was cloned from C. jejuni 81116"]

RCSB 8H52 maps to O26037 by SIFTS, but its primary source is NCTC11637_00022, strain NCTC11637/ATCC43504, taxon102618. Its tagged construct is 405 residues; the C-terminal 385 residues match 380/385 residues of frozen O26037 by direct position comparison. O26037 starts later than the construct and differs at several positions; therefore PMID36283333 is not a direct 26695 assay. The abstract establishes NADP-associated structure and describes CASDH chemistry, but does not provide native competition against agmatine.

Neither CASDH is adjacent to the NspC gene in these reference genomes; no adjacency or operon inference is made. PMID28648602 on inactive H. pylori SpeE is not used to establish the alternative route. Family membership, in-vitro substrate acceptance, native metabolite output and genetic necessity are kept separate. PMID37878710 demonstrates CAPA diversification, preventing blanket putrescine specificity transfer. No biofilm/growth-process or generic binding annotation is proposed.


This target is the actual 81116 nspC/C8J_1418. It was seeded normally as CAMJ8/nspC on 2026-11-05; the untouched document, eleven original payloads and raw SHA256 hashes are in `.cache/module-audit-logs/carboxyspermidine-20261105/CAMJ8-nspC-baseline.json`. No NEW annotation rows were needed.

Construct discrepancy: the frozen A8FNH9 sequence is 382 residues and has K184. PMID20534592 states that the original clone acquired spontaneous E184K, lost activity, and was repaired to E184 before kinetics and crystallization. The deposited 3N29 sequence has E184. UniProt calls the variation effect unclear, which conflicts with the explicit paper statement. The review records the established gene function while limiting direct biochemical claims to the repaired E184 construct; raw sequence and original annotations are unchanged. The 2011 native deletion/complementation evidence is independent support for the gene role.


## PR #6089 requested revisions — 2026-11-06

Reconciled PMID20534592 kinetics with the dual-substrate decarboxylase NTR throughout replacements, core and proposal (carboxynorspermidine catalytic efficiency about 4.7 times that for carboxyspermidine). Native spermidine versus norspermidine BP decisions are unchanged. Retained structural homodimerization as KEEP_AS_NON_CORE, not a refinement to catalysis. Added a structured UNIPROT source defect for the kinetic note saying the E184/K184 effect is unclear: the primary methods explicitly report an inactive E184K cloning mutant and repaired E184 assays. Independent native 81116 residue verification remains unresolved. Machine annotation payloads, inherited NEW assertions and raw UniProt/GOA files were preserved; no new annotation rows were added. Existing research/provider records were not refreshed.
