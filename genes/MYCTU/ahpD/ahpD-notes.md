# ahpD research notes

## 2026-10-26: source-based AhpC-regeneration audit

The review and annotation-reviewer skills were applied. The seeded annotation payloads, including ordinary qualifiers and NOT flags, are preserved. Actual Falcon and perplexity-lite attempts failed; no provider report was fabricated. Publication caching ran in parallel. FEBA retrieval was attempted but MYCTU has no configured organism mapping and no reachable source; this supplies no phenotype evidence. Logs are in `.cache/module-audit-logs/alkyl-myc-fetch/`.

The module boundary is AhpC peroxide reduction plus specifically supported regeneration chains, not all thioredoxin clients or all oxidative-stress physiology. Reconstituted activity does not establish an exclusive physiological donor or growth requirement.

PMID:10766746 directly reports weak alkylhydroperoxidase activity of purified AhpD, so its better-established electron-relay role does not negate all peroxide turnover. PMID:15178486 shows catalytic mixed-disulfide formation between AhpC Cys61 and AhpD Cys133, with explicit bovine dihydrolipoamide dehydrogenase/free-lipoamide assay context. This is direct evidence of AhpC–AhpD chemistry, not purified native Lpd–DlaT pairing. PMID:11799204 and the later native metabolic studies ground the latter relay.

### Final independent review refinement

The broad molecular-function replacement now lists both supported activities, preserving the existing secondary-activity assay limits and non-core assessment. Original annotation payloads and actions remain unchanged.


## 2026-10-27 — PR #5595 reference and wording follow-up

Resolved article identities using canonical PMID-to-full-text mappings in `modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/reference-identities.yaml.txt`; URL sources remain intact for quotations not present in cached abstracts. Added canonical article titles alongside immutable extraction metadata and removed source-ID/workflow boilerplate from reasons. Annotation payloads and actions remain unchanged.
Verified current GO:0051920 reaction chemistry against PMID:11914371 and PMID:12761216: the peroxide reaction oxidizes the AhpD catalytic cysteines to their own disulfide. Its distinct fold is not grounds to discard the supported activity or allege an InterPro mapping defect; the assay remains non-core and does not prove native predominance.
