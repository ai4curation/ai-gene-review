# HP_1507 manual annotation review notes

## 2026-11-05

Applied annotation-reviewer and core-function-synthesizer guidance. Original annotation payloads are preserved; only review blocks were changed on seeded rows. No raw UniProt/GOA file was refreshed.

Default Falcon was attempted through `just deep-research-falcon HELPY HP_1507` and failed with HTTP 403 authentication error. The complete failure log is `HP_1507-falcon-attempt.log`; this file is manual research, not a provider report.

Sources read: PMID22025614 (full text), PMID20534592 (full text after a normal force-fetch retry), PMID36283333 (abstract only; publisher access failed), PMID37878710 (full text), PMID19196710 (full text), the frozen UniProt record and PTHR43727 family review. QuickGO on 2026-11-05 confirms GO:0102143 includes carboxyspermidine chemistry; GO:0102144 is obsolete. Specific CASDC name searches returned no active term; reaction-specific NTRs avoid using broad carboxy-lyase as a falsely specific activity.

The 2011 native experiments used C. jejuni 81116, not NCTC 11168. The loci are C8J_0166 (CASDH candidate) and C8J_1418 (CASDC). [PMID:22025614, "All strains were derived from the sequenced C. jejuni strain 81116 (NCTC 11828)"] The CASDH deletion increased spermidine and grew normally; the CASDC deletion abolished spermidine and complementation restored it. The paper contains an inconsistent methods sentence naming 11168 and a C8J_0715 CASDC deletion, whereas its experimental overview, results, and figures identify 81116/C8J_1418; do not turn that sentence into direct evidence on NCTC 11168.

PMID20534592 directly assays the 81116 CASDC on synthetic carboxyspermidine and carboxynorspermidine. Its clone had an accidental E184K mutation that was repaired before the reported assays. RCSB 3N29 maps to A8FNH9, not Q0P8A4; the C-terminal 382 residues of the deposited tagged sequence match 374/382 residues of Q0P8A4 by direct position comparison. Thus Cj1515c receives close-homolog inference, not IDA. [PMID:20534592, "The gene for Cj CANSDC was cloned from C. jejuni 81116"]

RCSB 8H52 maps to O26037 by SIFTS, but its primary source is NCTC11637_00022, strain NCTC11637/ATCC43504, taxon102618. Its tagged construct is 405 residues; the C-terminal 385 residues match 380/385 residues of frozen O26037 by direct position comparison. O26037 starts later than the construct and differs at several positions; therefore PMID36283333 is not a direct 26695 assay. The abstract establishes NADP-associated structure and describes CASDH chemistry, but does not provide native competition against agmatine.

Neither CASDH is adjacent to the NspC gene in these reference genomes; no adjacency or operon inference is made. PMID28648602 on inactive H. pylori SpeE is not used to establish the alternative route. Family membership, in-vitro substrate acceptance, native metabolite output and genetic necessity are kept separate. PMID37878710 demonstrates CAPA diversification, preventing blanket putrescine specificity transfer. No biofilm/growth-process or generic binding annotation is proposed.


Identity metadata was fetched verbatim from https://data.rcsb.org/rest/v1/core/polymer_entity/8H52/1 into `8H52-polymer-entity-1.json`. The simple comparison takes `entity_poly.pdbx_seq_one_letter_code_can[-len(reference_sequence):]` and counts identical characters at corresponding positions against the frozen UniProt sequence. This is an identity/construct audit, not a kinetic or phylogenetic inference.

NEW process checks: HP1507 is proposed as the catalyst that condenses the amine substrate with aspartate semialdehyde, not a consumed precursor. On 2026-11-05 QuickGO returned no GO:0008295 rows for the same-role dehydrogenases Q9KRL3 (Vibrio), Q88IS1 (Pseudomonas) and A9CG66 (Agrobacterium). Q9KRL3 had only one MF row and A9CG66 had no GO rows at all, so these are sparse annotation records, not evidence that a substrate-role convention excludes dehydrogenase catalysts. This proposal rests on the cited reaction and H. pylori pathway evidence, not on claiming curators overlooked a gap. GO:0008295 defines reactions resulting in spermidine; precursor synthesis is a catalytic step. No matching accession was found in gocams/index.tsv.

## 2026-11-05 structural re-review superseding the initial ISS proposals

The initial two NEW ISS rows and core were withdrawn after explicit contact analysis. The absent native residues 1–14 include five residues within 4 Å of NADP in 8H52. The coordinate header resolves the actual construct to A0A2X5A3P4 (399 residues), with six additional tag residues. High identity across the retained region therefore does not justify assuming cofactor competence of the shorter O26037 sequence. This is a reason to withhold transfer, not proof of inactivity. The original seeded annotation list was empty and remains empty. See HP_1507-bioinformatics/RESULTS.md for reproducible data, control and limits.

## 2026-11-06 — PR6089 structured gene-model follow-up

Added `gene_model_issues` with `WRONG_START_SITE`, `SUSPECTED`, and `ORTHOLOG_COMPARISON`, following the schema and the ECOLI/ybbO example. The 14-residue N-terminal difference is relative to the NCTC 11637 structural homolog, not a demonstrated missing segment in the native 26695 product. The first aligned residue differs (O26037 M versus construct V); true strain divergence and a shortened functional product remain alternatives. The five NADP-proximal residues establish functional relevance of the difference, not an independent demonstration of an annotation error. No genomic sequence evidence, translated upstream extension, corrected initiation codon, or proven loss of activity is claimed. Existing annotations and core functions remain empty; the biological knowledge gap remains appropriate alongside this structured suspected model issue. Raw files and all source artifacts were left untouched.
