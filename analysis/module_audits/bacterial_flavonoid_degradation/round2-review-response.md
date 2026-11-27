# PR #6140 round-2 annotation consultation

Reviewed head: `ed4fa345048677c168a8fe4beb8a6b9c53c7edf6`. The full [review comment](https://github.com/ai4curation/ai-gene-review/pull/6140#issuecomment-6699748861), current annotation-reviewer/aigr-pr-review skills, schema and repository guidance were read. The bioinformatics-analyzer workflow was used when the catalytic-residue premise required an independent check. Earlier round1 records remain historical; this document records the new judgments.

## 1. Withdrawal semantics

The nine already retired GO:0046275 proposals now use **REMOVE + retired:true**. Their reasons explicitly identify these as earlier curator-authored NEW proposals, not current GOA assertions. REMOVE withdraws the unsupported proposal; it does not assert biological incapacity or an upstream GOA disappearance. This follows the concrete `genes/PSEPK/cysI` precedent while preserving all original row payloads, evidence and positions.

The schema defines retirement as an annotation being retired or replaced, and source-refresh documentation distinguishes retirement from a biological REMOVE judgment. The explicit curator-withdrawal wording is essential here. No additional rows are retired, deleted or introduced. `round2-withdrawals.yaml` lists all nine actions by source-order index. The seven previously retained NEW annotations remain active.

## 2. Broad FdeB molecular function, with an independently checked caveat

Hsero_1004, PP_3195 and bll6428 now each have a **GO:0016787 hydrolase activity** core entry. This is a positive, broad inference from FrsA-like family membership, alpha/beta-hydrolase architecture and conserved candidate catalytic chemistry. It does not choose between ester and C-C hydrolysis, assign a substrate, or assert native flavonoid-catabolic participation. No NEW annotation rows were added. bll6428's existing IBA hydrolase row remains ACCEPT; its PAINT support is not treated as another gene's functional evidence.

Live official QuickGO confirms that GO:0016787 includes hydrolysis of multiple bond classes and is an ancestor of both GO:0052689 and GO:0016822. The prior decision to omit this informative broad inference from the core synthesis was too restrictive. Its inclusion does not revive the withdrawn biological-process proposals or either specific reaction hypothesis.

The reviewer's stronger premise of an established intact target catalytic triad is **not accepted without qualification**. Independent checks found:

| Query/site set | PP_3195 | Hsero_1004 | bll6428 |
|---|---|---|---|
| Actual PP_3195 positions corresponding to the provider's proposed triad | S268 / D359 / H405 | S233 / D324 / H370 | S237 / D328 / Q374 |
| Characterized Q93NG6 S217 / D300 / H329 mapped by sequence alignment | S268 / D359 / H394 | S233 / D324 / H359 | S237 / D328 / H363 |

The provider report calls the acidic residue Asp358, but the frozen PP_3195 sequence has Lys358 and Asp359. Its H405 candidate is not conserved as histidine in bll6428. However, the independently characterized-family alignment identifies a different conserved histidine candidate in all three proteins. Therefore the H405/Q374 difference does **not** establish loss of catalysis in bll6428. Both mappings are sequence-based candidates; the distant Q93NG6 alignment is approximately 30–34% identical over aligned positions and does not prove target geometry. No experimental target catalytic residue assignment or negative activity result is claimed.

The current official Q89GB7 sequence matches the frozen Q374-containing bll6428 sequence. The raw/provider artifacts remain unchanged. The generic, parameterized script, two query runs, input hashes, dependency version, direct outputs and analysis checklist are documented in `genes/PSEPK/PP_3195/PP_3195-bioinformatics/fdeb-round2/RESULTS.md`. These observations support broad functional inference while preventing an unjustified activity-loss claim.

## 3–5. Boundary, speculative term requests and review prose

PP_3195's stale boundary now says the fold, family and candidate catalytic residues support broad hydrolysis but do not resolve bond class or substrate/product. It no longer contradicts the UNDECIDED ester-specific row.

The PP_3195 delta-lactone and PP_3206 oxaloacetate-releasing reaction proposals were removed from `proposed_new_terms`, because the reactions and enzymes have not been demonstrated. Their names and definitions remain as conditional `suggested_questions`; exact original proposal objects, including their supporting text, are archived in `round2-relocated-proposals.yaml`. They are no longer active GO-term requests. No core function depended on either proposal.

The shared FdeB reasons now state findings rather than instructions to a curator. The peptide/proteolysis judgments remain MARK_AS_OVER_ANNOTATED, and the ester-specific judgments remain UNDECIDED. These distinctions are unchanged by the broad hydrolase core inference.

## 6. Shared tracker typography

The two `PR6140` separator glitches were referred to the coordinator, who owns shared tracker edits. This consultation does not modify project or inventory files.

## 7. Direct primary evidence for the C-C hydrolase comparator

The C-C hydrolysis argument now cites **PMID:16321959 directly**, rather than quoting that claim only through the authored round1 audit. **PMID:17275835** supplies the comparator's structural/mutational context. Both were fetched through `just fetch-pmid` and are explicitly marked abstract-only; their abstracts were inspected, and no inaccessible full-text details are claimed. The official reviewed **UniProt Q93NG6** snapshot is also directly referenced as the record linking the characterized enzyme, experimental catalytic-site evidence and IPR050261 membership.

Q93NG6 is a family-breadth comparator, not a donor for nicotine specificity or proof that any FdeB protein cleaves a C-C bond. The original round1 audit and its source records remain unchanged, including the historical quotation.

## Verification boundary

Ten gene histories were generated. Focused gene validation/rendering, module semantic/reference validation and the existing coverage checker are recorded in `round2-validation.yaml`. The executable `round2-preservation.py` records source payload/order, unchanged source artifacts, action/NEW/retirement accounting and added source hashes. The module, family assessments, reaction roles and coverage checker biology are unchanged: modeled FdeB carrier coverage still must not be exported as evidence of ester activity or native flux. Full validation, integration and publication remain coordinator-owned.

All focused checks pass. Two advisory warnings note the new broad core functions without matching existing annotation rows; this uses the requested core-only route without adding NEW rows. Twenty module advisories retain the existing uncertain reaction-role and family-scope boundaries. The preserved panel contains 46 rows (the review comment reports 45), with nine retired proposals and seven active NEW rows.
