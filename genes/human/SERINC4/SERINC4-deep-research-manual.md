# SERINC4 manual deep-research synthesis

## Scope and provenance

This manual synthesis was prepared after the required automated deep-research attempt failed: Falcon returned HTTP 402 (payment required), and the Perplexity-lite fallback returned HTTP 401 (insufficient quota). No failed provider-named output was retained. Evidence was assembled from reviewed human UniProtKB A6NH21, both GOA rows, the abstract of the original Serinc-family study, and the full text of the direct human SERINC4 antiviral study.

## Membrane protein and family-level lipid context

SERINC4 is a multipass membrane member of the SERINC family. Reviewed UniProt records generic membrane localization and cites the original family study for incorporation of serine into membrane-lipid synthesis. That paper described "carrier proteins, termed Serinc1-5" that facilitate phosphatidylserine and sphingolipid synthesis [PMID:16120614]. However, its accessible abstract does not directly assay human SERINC4, and no cached purified-protein experiment establishes SERINC4 phospholipid scrambling. The two existing generic membrane annotations are therefore acceptable, but scramblase activity should not be inferred from SERINC2, SERINC3, or SERINC5.

## Conditional antiviral activity

Human SERINC4 is unusually unstable: "human SERINC4 is subjected to proteasome-mediated turnover, resulting in ~250-fold lower expression than SERINC5" [PMID:33521797]. When expression was experimentally normalized, SERINC4 restricted HIV-1 as effectively as SERINC5 and was antagonized by Nef through a lysosomal route [PMID:33521797, "when expression was normalized, human SERINC4 restricted HIV-1 replication as effectively as SERINC5"]. Stabilized chimeras were incorporated into particles and showed envelope-dependent restriction [PMID:33521797, "SERINC4 is incorporated into HIV-1 virions and restricts Tier 1 HIV-1 more effectively than Tier 3 HIV-1."].

This is direct evidence for a conditional antiviral phenotype and justifies a NEW GO:0140374 antiviral innate immune response annotation. The expression caveat is essential: the experiments overcame very low steady-state abundance by overexpression or N-terminal stabilization, and the paper calls the endogenous physiological role potential rather than established. Plasma-membrane localization is discussed as the presumed route to virions, but the paper's discussion labels this as speculation; the review therefore retains generic membrane rather than authoring a more specific localization.

## Open questions

It is unknown whether endogenous human SERINC4 reaches sufficient abundance in any physiological cell state to restrict retroviruses. Its direct molecular activity is also unknown: neither the older family paper nor the available human antiviral study demonstrates phospholipid scrambling by purified SERINC4. The two UniProt isoforms have not been compared for stability, localization, virion incorporation, or restriction.
