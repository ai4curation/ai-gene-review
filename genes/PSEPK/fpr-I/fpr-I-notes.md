# fpr-I curation notes

## First-pass synthesis

- Q88MD5 (PP_1638) is a type-1 FAD-dependent ferredoxin--NADP reductase with
  EC 1.18.1.2 [UniProtKB:Q88MD5, "Belongs to the ferredoxin--NADP reductase type
  1 family"].
- Pseudomonas fprA loss or reduced expression compromises sulfate assimilation,
  while expression of fprA or E. coli cysJI complements the phenotype
  [PMID:23794620, "The Pdt phenotype of finR mutants could be complemented by
  the known target of FinR regulation, fprA"]. The experiments used P. putida
  DSM 3601, so the KT2440 sulfate-assimilation proposal is an orthology transfer
  to Q88MD5 rather than direct mutant-phenotype evidence.
- The exact carrier between Fpr-I and CysI remains unresolved. The gene review
  accepts the enzyme-specific FNR activity, uses ISO for the transferred
  sulfate-assimilation role, and leaves unsupported TreeGrafter process claims
  undecided.

## Boundary decision

Fpr-I is modeled as the electron-supply role in the Pseudomonad CysI variant,
not as an additional sulfate-to-sulfide chemical transformation.


## Comparative sulfate-assimilation audit — 2026-10-26

Re-reviewed all five rows. Added primary [PMID:19122206] Fd/Fld assays: FprA prefers Fld but retains measured Fd-reductase capability; preference is not absence of activity. Added native KT2440 oxidative/osmotic stress evidence[PMID:16360643], supporting non-core oxidative defense. Heme-catabolic transfer remains unresolved because the cited direct heme-oxygenase pairing is P. aeruginosa. The existing NEW sulfate-assimilation proposal is retained with DSM3601-versus-KT2440 and immediate-carrier caveats. ARBA-only UniProt reaction text is not used as independent functional evidence.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.

## 2026-10-26 PR #5560 evidence follow-up

Consolidated the PMC URL twin into canonical PMID:23794620 after normal full-text recovery. Source findings now describe each study rather than recycle a core-function sentence. Core description states electron-transfer function; the unresolved physiological carrier is separately recorded as a literature-grounded knowledge gap with an experimental resolution.

All original annotation payloads and row order are preserved. Focused validation and automatic record-section backfill pass; generated pages and append-only history record this follow-up.
