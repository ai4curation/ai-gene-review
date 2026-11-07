# Cj0172c manual annotation review notes

## 2026-11-05

Applied annotation-reviewer and core-function-synthesizer guidance. Original annotation payloads are preserved; only review blocks were changed on seeded rows. No raw UniProt/GOA file was refreshed.

Default Falcon was attempted through `just deep-research-falcon CAMJE Cj0172c` and failed with HTTP 403 authentication error. The complete failure log is `Cj0172c-falcon-attempt.log`; this file is manual research, not a provider report.

Sources read: PMID22025614 (full text), PMID20534592 (full text after a normal force-fetch retry), PMID36283333 (abstract only; publisher access failed), PMID37878710 (full text), PMID19196710 (full text), the frozen UniProt record and PTHR43727 family review. QuickGO on 2026-11-05 confirms GO:0102143 includes carboxyspermidine chemistry; GO:0102144 is obsolete. Specific CASDC name searches returned no active term; reaction-specific NTRs avoid using broad carboxy-lyase as a falsely specific activity.

The 2011 native experiments used C. jejuni 81116, not NCTC 11168. The loci are C8J_0166 (CASDH candidate) and C8J_1418 (CASDC). [PMID:22025614, "All strains were derived from the sequenced C. jejuni strain 81116 (NCTC 11828)"] The CASDH deletion increased spermidine and grew normally; the CASDC deletion abolished spermidine and complementation restored it. The paper contains an inconsistent methods sentence naming 11168 and a C8J_0715 CASDC deletion, whereas its experimental overview, results, and figures identify 81116/C8J_1418; do not turn that sentence into direct evidence on NCTC 11168.

PMID20534592 directly assays the 81116 CASDC on synthetic carboxyspermidine and carboxynorspermidine. Its clone had an accidental E184K mutation that was repaired before the reported assays. RCSB 3N29 maps to A8FNH9, not Q0P8A4; the C-terminal 382 residues of the deposited tagged sequence match 374/382 residues of Q0P8A4 by direct position comparison. Thus Cj1515c receives close-homolog inference, not IDA. [PMID:20534592, "The gene for Cj CANSDC was cloned from C. jejuni 81116"]

RCSB 8H52 maps to O26037 by SIFTS, but its primary source is NCTC11637_00022, strain NCTC11637/ATCC43504, taxon102618. Its tagged construct is 405 residues; the C-terminal 385 residues match 380/385 residues of frozen O26037 by direct position comparison. O26037 starts later than the construct and differs at several positions; therefore PMID36283333 is not a direct 26695 assay. The abstract establishes NADP-associated structure and describes CASDH chemistry, but does not provide native competition against agmatine.

Neither CASDH is adjacent to the NspC gene in these reference genomes; no adjacency or operon inference is made. PMID28648602 on inactive H. pylori SpeE is not used to establish the alternative route. Family membership, in-vitro substrate acceptance, native metabolite output and genetic necessity are kept separate. PMID37878710 demonstrates CAPA diversification, preventing blanket putrescine specificity transfer. No biofilm/growth-process or generic binding annotation is proposed.

The Cj0172c activity remains a candidate inferred from PTHR43796:SF2 and comparative Campylobacter pathway evidence. UniProt searches for the old 81116 locus C8J_0166 returned no current entry, so no unverified accession or exact ortholog mapping is asserted. No spermidine BP annotation was added: the target-specific catalytic and physiological link needs confirmation.

## 2026-11-05 core-function consistency re-review

The provisional MF refinement was previously promoted into a predicted core. This core has been withdrawn: family membership and a counterintuitive phenotype in another strain do not resolve the physiological substrate or exact reaction in Q0PBW7. Like BT_4612, this is a substrate-uncertain candidate with no asserted core. The original seeded row retains its non-review payload and its explicitly provisional MODIFY recommendation; a knowledge gap records what would confirm or change it.
