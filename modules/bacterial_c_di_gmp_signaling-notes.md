# Bacterial c-di-GMP module audit

## 2026-11-05: boundary, comparative literature and evidence

This audit follows the synthesis → turnover → protein-recognition motif across 17 reference proteins in Pseudomonadota, Bacillota and Spirochaetota. It preserves 116 original GOA-derived annotation payloads and 34 raw UniProt/GOA files. The basal inventory and file hashes are in [seed-baseline.yaml](../analysis/module_audits/bacterial_c_di_gmp_signaling/seed-baseline.yaml). Individual gene notes distinguish reference sequences from experimentally assayed strains.

The broad bacterial scope is appropriate for the motif, but neither universal presence nor a complete copy in every sampled species follows. The selected E. coli K-12, B. subtilis 168 and B. burgdorferi B31 reference panels cover all three required roles. The other representatives illustrate particular mechanisms. Reference-protein role coverage is not evidence that every edge was experimentally demonstrated in each reference strain. BdcA-associated DdpA is an optional Bordetella context, not a required universal cyclase subunit.

### Comparative sources and mined conclusions

- [PMID:37251514](https://pubmed.ncbi.nlm.nih.gov/37251514/) reviews local and global c-di-GMP signalling and gives experimental criteria for local signalling: pathway-specific phenotypes, messenger measurements and direct protein interactions. Its E. coli/Pseudomonas comparisons justify qualifying all pool-level edges. Synthesis and degradation need not feed one homogeneous pool or impose one receptor-affinity hierarchy.
- [PMID:23893111](https://pubmed.ncbi.nlm.nih.gov/23893111/) directly characterizes Bacillus DgcK/DgcP/DgcW, PdeH and DgrA. Elevated c-di-GMP inhibits swarming without changing the tested biofilm phenotype. The motif therefore does not universally encode a motility-to-biofilm switch.
- [PMID:32156823](https://pubmed.ncbi.nlm.nih.gov/32156823/) shows DgcK–YdaK and DgcK/DgcP–DgrA interactions, supporting local input pathways while PdeH provides a global turnover influence. YdaK uses an inactive GGDEF I-site; LapD instead binds through inactive EAL.
- [PMID:24822172](https://pubmed.ncbi.nlm.nih.gov/24822172/) provides the Borrelia comparison: a compact Rrp1–PdeA/PdeB–PlzA system with tick/host-dependent outputs. Primary Rrp1, PdeA, PdeB and PlzA papers anchor each role rather than transferring those outputs to other bacteria. The B31-centred inventory is not asserted for all Borrelia strains.
- [PMID:41452322](https://pubmed.ncbi.nlm.nih.gov/41452322/) compares classical Bordetella species and motivates the conditional BdcA/DdpA relationship. [PMID:31209073](https://pubmed.ncbi.nlm.nih.gov/31209073/) supplies the primary evidence: 9.73 phenotypes, RB50 sequence predictions, unstable/undetectable GGAAF mutant and no demonstrated direct DdpA binding. DdpA also has a separate histidine-kinase region, which must not be dismissed because its GGDEF/EAL motifs are degenerate.
- [PMID:42429561](https://pubmed.ncbi.nlm.nih.gov/42429561/) reviews metal-dependent c-di-GMP chemistry. Metal binding, catalytic cofactor use and physiological metal sensing are different claims. DgcZ's experimentally characterized CZB zinc-sensing domain is not a generic property of GGDEF enzymes.

The module now has 24 curated reference records with claim-specific findings. Every annoton and connection carries evidence. Full-text availability and construct/strain limitations remain in member reviews rather than being hidden by a COMPLETE status.

### Turnover chemistry and family constraints

EAL and HD-GYP enzymes are alternative turnover implementations, not universally co-occurring enzymes. [PMID:24066157](https://pubmed.ncbi.nlm.nih.gov/24066157/) resolves pGpG as a PA4781 intermediate and slow onward GMP production. Its apparent Km for pGpG is lower than for c-di-GMP; this is not a measured equilibrium Kd. [PMID:21670168](https://pubmed.ncbi.nlm.nih.gov/21670168/) measures PdeB conversion to GMP, so ring opening is an inference within the demonstrated overall reaction. The module's GO:0071111 reaction names only the shared ring-opening step; GMP is not incorrectly listed as a co-product of that single reaction. The retracted RpfG paper is not used to establish chemistry.

PANTHER assignments were resolved through UniProt and exact labels checked against the committed PANTHER ontology. The EAL and HD-GYP groupings span multiple verified families. Membership is intersected with molecular activity; an official family name containing “phosphodiesterase” does not make LapD, YdaK or DdpA catalytic. PilZ remains an explicitly described functional family grouping with domain and binding constraints because no PANTHER id was established for the selected members. [PMID:20030712](https://pubmed.ncbi.nlm.nih.gov/20030712/) explicitly cautions that PilZ-domain presence alone does not confer ligand binding.

QuickGO still defines GO:0061939 as information transfer from one cell to another (checked 2026-11-05). The module therefore uses the messenger concept without inheriting that intercellular definition. This is an unresolved ontology issue, not a reason to deny the intracellular biology.

### Individual reviews and uncertainty

Eight NEW annotations supply demonstrated or explicitly inferred molecular activities absent from the seeded annotation rows: PleD allosteric ligand binding, LapD ligand binding, MotI motor regulation, YdaK ligand binding, PdeB ring opening and three PlzA activities. Strain transfers use ISS with verified full-length sequence identity where documented; PdeB's unobserved intermediate uses IC. PdeL transcriptional activation and LapD protease inhibition are refinements of existing rows rather than duplicate NEW claims. No NEW biological-process annotation was added solely from necessity or infection phenotypes.

Five DdpA kinase/relay/transferase claims and one PA4781 phosphorelay claim remain UNDECIDED. DdpA has no invented core molecular function: its established genetic requirement does not yet establish an adaptor mechanism, direct binding or kinase catalysis. PA4781 acetyl-phosphate activation does not identify its native kinase. Other corrections distinguish soluble cyclases from membrane enzymes and reject inappropriate transfers of adhesion, kinase or cell-wall roles. PAINT checks and their unavailable-lineage limitations are recorded in gene notes.

Falcon research was attempted for the module and every member and failed authentication (HTTP 403). This file and the member notes document manual research; no provider report was fabricated. An independent read-only QA of the four root-authored reviews supported the uncertainty decisions and prompted the apparent-Km precision correction above.

### Reproducible audit

Run `uv run python modules/bacterial_c_di_gmp_signaling-source-analysis/check_audit.py` from the repository root. It checks the 116 original payloads and 34 raw hashes, complete reviews, module/member identity, all six family/evidence-bearing annotons, core-function consistency, exact PANTHER labels and member assignments, publication closure, 24 cases through the production module compiler: seven reference-strain panels, nine required-role-removal cases, alternative PDE/receptor retention, empty/optional-only inputs, mixed-species rejection and separation of PleD feedback binding from dedicated reception. The generated reports are in `analysis/module_audits/bacterial_c_di_gmp_signaling/`.

The family membership refresh, module schema/biological validators, all 17 focused gene validations, history validation, rendering, Ruff and repository-wide `just validate-all` are recorded separately in the audit checks. The project completion state will be updated only after the module-specific PR actually merges.

The full-corpus reference check reports 19 existing quote-matching failures in 17 yeast reviews, all outside this module. Both affected publication caches (PMID:18701704 and PMID:18719252), every affected review and the schema/configuration/wrapper/lockfile exactly match the audit base commit. A focused replay on those unchanged files reproduces exit 1. The file/blob evidence is in `analysis/module_audits/bacterial_c_di_gmp_signaling/preexisting-reference-failures.yaml`; these unrelated reviews are not changed here. This limitation must not be reported as a passing full-corpus run.

Final whole-corpus run: schema and ontology checks passed, best-practices validation completed on 10,550 reviews with zero errors and 28,000 advisory warnings, and all 54 pathway files containing PMID references passed. The overall command exited 1 solely because of the 19 documented pre-existing reference failures. All 17 scoped reviews, module schema/biological checks, 24 production-compiler cases, 19 history records, rendering and Ruff passed.


## PR #6062 review follow-up — 2026-11-06

Updated seven representative protein labels from the frozen UniProt RecName fields, retaining readable gene/strain names in preferred_term. Corrected the BdcA finding and step evidence to distinguish increased c-di-GMP on overexpression from the motility-only deletion result, and retained the catalytic-mutant stability limitation.


## PR #6062 second follow-up — 2026-11-06

Normalized the three remaining gene/strain-style representative labels to frozen UniProt RecNames, retaining readable preferred_term values. Added a biological knowledge gap for PlzA endogenous nucleic-acid targets and physiological output; no receptor-class-wide output is inferred.
