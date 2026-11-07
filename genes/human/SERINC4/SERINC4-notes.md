# SERINC4 curation notes

## 2026-07-25 evidence log

- Ran `just fetch-gene human SERINC4`: two GOA rows were seeded one-to-one in the review.
- The seed contained no PMID references. PMID:16120614 was already cached, and the direct SERINC4 study PMID:33521797 was fetched with full text.
- Attempted Falcon deep research with Perplexity-lite fallback. Falcon failed with HTTP 402 and the fallback failed with HTTP 401; no provider-named failed output was retained. Manual research is recorded in `SERINC4-deep-research-manual.md`.
- Read reviewed UniProtKB A6NH21, both GOA rows, the PMID:16120614 abstract, and the full text of PMID:33521797.

## Annotation decisions

- Both GO:0016020 membrane rows are ACCEPT. SERINC4 is a multipass membrane protein, but the available direct evidence does not justify replacing them with a more specific steady-state location.
- Add a NEW GO:0140374 antiviral innate immune response row supported by PMID:33521797.
- Do not infer phospholipid scramblase activity for SERINC4. Direct purified-protein scrambling has been shown for other human SERINC family members, not SERINC4.
- Do not claim an established endogenous restriction role. Human SERINC4 is normally about 250-fold less abundant than SERINC5 in the tested system; restriction was detected after normalized overexpression or stabilization.

## Evidence boundary

The direct study found that "human SERINC4 strongly restricts HIV-1 replication when it is overexpressed" [PMID:33521797]. This supports a conditional antiviral annotation, while the physiological importance of endogenous SERINC4 remains unresolved.

## Experimental priorities

1. Measure endogenous SERINC4 abundance and antiviral contribution in relevant primary human cells without ectopic overexpression.
2. Determine whether purified human SERINC4 has phospholipid scramblase activity and define its substrate range.
3. Compare the two UniProt isoforms for stability, topology, membrane trafficking, virion incorporation, Nef sensitivity, and restriction.
