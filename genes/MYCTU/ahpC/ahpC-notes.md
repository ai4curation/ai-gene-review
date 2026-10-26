# ahpC research notes

## 2026-10-26: source-based AhpC-regeneration audit

The review and annotation-reviewer skills were applied. The seeded annotation payloads, including ordinary qualifiers and NOT flags, are preserved. Actual Falcon and perplexity-lite attempts failed; no provider report was fabricated. Publication caching ran in parallel. FEBA retrieval was attempted but MYCTU has no configured organism mapping and no reachable source; this supplies no phenotype evidence. Logs are in `.cache/module-audit-logs/alkyl-myc-fetch/`.

The module boundary is AhpC peroxide reduction plus specifically supported regeneration chains, not all thioredoxin clients or all oxidative-stress physiology. Reconstituted activity does not establish an exclusive physiological donor or growth requirement.

AhpC is the peroxide-attacking enzyme, distinct from its reducing partners. PMID:10766746 directly assays purified M. tuberculosis AhpC with heterologous Salmonella AhpF or DTT; that early paper does not identify the native donor. PMID:11799204 proposes the Lpd–DlaT–AhpD relay, while PMID:14871480 independently establishes a TrxR–TrxC route. Native pathway predominance remains a separate question.

The full 2017 Scientific Reports paper DOI:10.1038/s41598-017-05354-5 was recovered normally and inspected. It uses M. bovis BCG AhpC, explicitly identical in amino-acid sequence to Mtb AhpC, with M. bovis TrxC/TrxB2. Its NMR interaction and coupled peroxide turnover corroborate the mechanism but are not native H37Rv experiments. Reduced protein forms a dodecamer under the measured conditions; oxidized protein is dimeric. These results and the earlier decamer report (PMID:11171096) preclude an unconditional oligomeric stoichiometry.

Live QuickGO confirms GO:0008379 is obsolete and redundant with GO:0140824. The original annotation remains intact; any replacement is recorded only in review metadata.
