# trxA research notes

## 2026-10-26: source-based AhpC-regeneration audit

The review and annotation-reviewer skills were applied. The seeded annotation payloads, including ordinary qualifiers and NOT flags, are preserved. Actual Falcon and perplexity-lite attempts failed; no provider report was fabricated. Publication caching ran in parallel. FEBA retrieval was attempted but MYCTU has no configured organism mapping and no reachable source; this supplies no phenotype evidence. Logs are in `.cache/module-audit-logs/alkyl-myc-fetch/`.

The module boundary is AhpC peroxide reduction plus specifically supported regeneration chains, not all thioredoxin clients or all oxidative-stress physiology. Reconstituted activity does not establish an exclusive physiological donor or growth requirement.

The official symbol trxA (Rv3914, P9WG67) maps to the protein called TrxC in the functional literature; it is not the separate Rv1470 protein also called TrxA in papers. PMID:18723612 distinguishes all three constructs. PMID:14871480 assigns AhpC reduction to TrxC rather than indiscriminately to every thioredoxin.

Full PMID:19737561 was recovered from the author's UBC PDF and read, including Methods, Tables 1–4 and controls. Rv3914 and Rv3913 were cloned from H37Rv; the TrxC Cys40Ser mutation abolishes product formation. GSSG and MSSM reduction require TrxR plus TrxC and NADPH in the assay, with HPLC product confirmation. This supports genuine substrate breadth, without making host-compound detoxification a demonstrated infection phenotype.

Final source synthesis: PMID:7591163 independently identifies culture-filtrate MPT46 as the active thioredoxin, resolving the broad extracellular claim despite missing exact PMID:17443846 supplemental evidence. Retained as non-core, without an inferred secretion mechanism.


## 2026-10-27 — PR #5595 reference and wording follow-up

Resolved article identities using canonical PMID-to-full-text mappings in `modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/reference-identities.yaml.txt`; URL sources remain intact for quotations not present in cached abstracts. Added canonical article titles alongside immutable extraction metadata and removed source-ID/workflow boilerplate from reasons. Annotation payloads and actions remain unchanged.
