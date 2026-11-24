
## 2026-11-07 canonical E. coli review

Reviewed all 17 seeded annotations, preserving ordered source payloads and qualifiers. No NEW annotations were added. The default Falcon attempt failed with HTTP403 authentication; the actual log is in ecoli-canonical-consultation/validation/falcon-metE.log. This is a manual literature review, not a fabricated provider report. Normal PAINT-loss checking reported no IRD/IKR on the target lineage. Target self-donors were not treated as circular.

MetE requires polyglutamyl folate. Both GO0008705 rows are refined to GO0003871 because current GO8705 specifies monoglutamate, not because it requires B12 (it does not). Full PMID16618097 uses K-12 GW2531/pJG816 wild-type MetE and synthetic triglutamate; the monoglutamate restriction is an explicit literature statement citing earlier studies. See durable16618097-substrate-scope.md and provenance. PMID8823155 establishes catalytic zinc; PMID15502870 establishes reversible Cys645 glutathionylation, which is not inflated into a new stress-response role. Recorded P03018 partner is UvrD, not MetR.

## PR6196 evidence follow-up, 2026-11-07

- Classify directly measured catalytic zinc binding as core.
- Repair malformed PMID references in authored prose; source payloads, quotations and fetched titles remain unchanged.

Source adjudication and additive receipt: analysis/module_audits/bacterial_methionine_cycle/review-followup/. Original rows, qualifiers and prior audit artifacts are preserved.
