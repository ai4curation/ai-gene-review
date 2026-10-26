# ORYLA ara: comparative annotation review

## Provenance and scope

Normal `just fetch-gene` seeded every annotation; machine-sourced fields are preserved. Falcon deep research failed with HTTP 403 and its perplexity-lite fallback failed with HTTP 401. This is manual literature research, not a provider-generated report. Source caches were obtained through normal fetch commands and were not edited. Primary publications and curated UniProt statements were read; abstract-only evidence is not treated as proof of a wrong gene. No new biological-process annotations were proposed.

## Identity and native scope

PMID:19819965 and PMID:36918573 Methods map ara to AB252233/chromosome 10 and arb to AB252679/chromosome 14; these identify D1MV72 and D1MV73 respectively. Do not substitute similarly named records. PMID:26507457 compares cloned medaka paralogs in reporter/localization assays. PMID:36918573 provides native knockout and immunostaining evidence. Its double knockouts retain functional sperm and differ from mammalian AR-null testicular phenotypes; reproductive necessity must not be transferred wholesale. Ara localization in native anal fin is cytoplasmic despite constitutive nuclear localization in some transfected-cell experiments.

## Unresolved propagated claims

Estrogen-response-element binding requires PAINT/sequence-specific evidence beyond androgen response elements. Cortisol activation is not demonstrated for medaka by the zebrafish biochemical study. Basolateral localization is not established. No absence claim is inferred solely from the lack of a reported assay.


## Selected source passages

[PMID:26507457] “ARα showed a unique intracellular localization with a higher transactivation response than that of ARβ”

[file:ORYLA/ara/ara-uniprot.txt] “DR PROSITE; PS51030; NUCLEAR_REC_DBD_2; 1.”


## PR5554 member follow-up — 2026-10-26

Replaced generic 2015 abstract support with native 2023 knock-in localization and WT/mutant ARE reporter evidence (36918573). Ara is nuclear in POA/medulla cells but cytoplasmic in anal fin. Zinc binding is a sequence-domain inference. The OUP 2015 full-text route returned HTTP 403; no inaccessible figure was treated as inspected. No NEW annotation was manufactured for a module advisory.

All original annotation payloads were compared before/after and preserved; only reviewer assessments, source evidence, and the specified core-function location were changed.
