# DANRE ar: comparative annotation review

## Provenance and scope

Normal `just fetch-gene` seeded every annotation; machine-sourced fields are preserved. Falcon deep research failed with HTTP 403 and its perplexity-lite fallback failed with HTTP 401. This is manual literature research, not a provider-generated report. Source caches were obtained through normal fetch commands and were not edited. Primary publications and curated UniProt statements were read; abstract-only evidence is not treated as proof of a wrong gene. No new biological-process annotations were proposed.

## Primary evidence

PMID:17942797 identifies the single zebrafish ar locus and androgen-responsive clone; PMID:17698417 and PMID:18469035 directly assay ligand binding and transcriptional activation. PMID:25111804 uses computational docking; its original IDA evidence code is preserved, but direct binding support comes from the independent experimental papers. PMID:29228103, PMID:29272351, PMID:29849943 and PMID:28620015 supply native gonadal and behavioral evidence. Transcript in situ hybridization is not protein-localization evidence.

## Cortisol assay scope

The full primary de Waal paper (PMID:18469035, doi:10.1530/REP-08-0055), Table 1 and Figure 3D, was inspected at https://scispace.com/pdf/functional-characterization-and-expression-analysis-of-the-42uw323frs.pdf . Cortisol Ki is 352 ± 162 nM; reporter EC50 is 1855 ± 702 nM, maximum induction 10.07 ± 2.55-fold. At 100 nM cortisol was inactive. This is real weak receptor activation, not proof that the physiological receptor is a glucocorticoid receptor. The local normal cache contains only the abstract; no table quotation is fabricated in YAML. Literal biochemical cortisol activity and response are retained as non-core, while an in vivo glucocorticoid pathway remains unresolved.


## Selected source passages

[PMID:18469035] “The zebrafish Ar responded well in terms of binding and transactivation to synthetic androgens as well as to testosterone and 11-KT”

[file:DANRE/ar/ar-uniprot.txt] “DR PROSITE; PS51030; NUCLEAR_REC_DBD_2; 1.”


## PR5554 member follow-up — 2026-10-26

Reviewed all 37 rows and replaced the single generic biochemical quote with claim-specific binding, phenotype, and structural-domain evidence. Chromatin association and nucleus are explicitly inferred conserved receptor roles; mRNA in situ is not protein localization. Native binding is directly supported by radioligand assays (17698417), whereas spermatogenic/oocyte/courtship claims cite their native perturbation studies. Full-text publisher/Scispace/ResearchGate routes for 18469035 returned HTTP 403; the previously inspected Table 1 quantitative cortisol evidence remains distinguished from the abstract cache. No direct zebrafish protein-localization or chromatin-occupancy experiment was identified in the inspected primary material.

All original annotation payloads were compared before/after and preserved; only reviewer assessments, source evidence, and the specified core-function location were changed.

## 2026-10-26 final PR evidence follow-up

Restore explicit PMID:18469035 evidence links on the two cortisol rows. The quantitative Table 1 result and high-concentration limitation remain in the reason and notes; no quotation from the abstract-only local cache is fabricated. Actions are unchanged.
