# dlaT research notes

## 2026-10-26: source-based AhpC-regeneration audit

The review and annotation-reviewer skills were applied. The seeded annotation payloads, including ordinary qualifiers and NOT flags, are preserved. Actual Falcon and perplexity-lite attempts failed; no provider report was fabricated. Publication caching ran in parallel. FEBA retrieval was attempted but MYCTU has no configured organism mapping and no reachable source; this supplies no phenotype evidence. Logs are in `.cache/module-audit-logs/alkyl-myc-fetch/`.

The module boundary is AhpC peroxide reduction plus specifically supported regeneration chains, not all thioredoxin clients or all oxidative-stress physiology. Reconstituted activity does not establish an exclusive physiological donor or growth requirement.

DlaT was historically called SucB. PMID:16045627 directly reconstitutes PDH with AceE, DlaT and Lpd; the full Results, inspected through the publisher PDF, distinguish Lpd dehydrogenase activity from DlaT-mediated lipoyl transfer. Native lysates and the candidate recombinant combination did not yield CoA-dependent oxoglutarate-dehydrogenase activity. This supports the existing NOT annotation and limits the inherited succinyltransferase/TCA interpretation.

DlaT carries the redox-active lipoyl arm that transfers reducing equivalents between Lpd and AhpD. Its antioxidant role is not an assertion that its metabolic acetyltransferase reaction itself reduces peroxide. The full PMID:21238944 also shows an alternative lipoylated BkdC protein in a DlaT-deficient background; older claims that DlaT is the sole lipoylated protein need condition limits.


## 2026-10-27 — PR #5595 reference and wording follow-up

Resolved article identities using canonical PMID-to-full-text mappings in `modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/reference-identities.yaml.txt`; URL sources remain intact for quotations not present in cached abstracts. Added canonical article titles alongside immutable extraction metadata and removed source-ID/workflow boilerplate from reasons. Annotation payloads and actions remain unchanged.
