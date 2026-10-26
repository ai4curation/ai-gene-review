# Arabidopsis APR1 review

## 2026-10-26

Identity was seeded by exact UniProt accession P92979 (At4g04610), not an ambiguous symbol search. All 19 original annotation payloads, including the NOT chloroplast-thylakoid row, are preserved; no NEW rows.

Read the full normal caches for PMID:8917600 (Setya et al., 1996) and PMID:9653199 (Bick et al., 1998). APR1 is a direct catalyst of APS reduction, using GSH through its fused glutaredoxin-like domain. The PAPS signal in crude APR1 extracts has a lag and is explained by prior conversion of PAPS to APS; it does not justify the IPR004511-derived PAPS/thioredoxin claim. The full protein does not share every activity measured with the isolated C-terminal domain. [PMID:9653199, Glutaredoxin function for the carboxyl-terminal domain of the plant-type 5′-adenylylsulfate reductase: “The purified recombinant enzyme (APR1p) can use GSH efficiently as a hydrogen donor in vitro”.]

GO:0033741 was verified in current QuickGO as the glutathione-dependent reaction (EC1.8.4.9; RHEA14141). Current QuickGO ancestors include GO:0003824 and GO:0016671 but do not encode GO:0009973 as its ancestor; the latter replacement specifies the donor chemically without asserting a nonexistent ontology edge.

PMID:19259774's abstract explicitly covers APR proteins and a generally stromal distribution, but neither the publisher preview nor author repositories exposed the APR1 assay. https://link.springer.com/article/10.1007/s11103-009-9471-4 and https://wrap.warwick.ac.uk/id/eprint/28021/ were inspected. The specific stroma and NOT-thylakoid rows remain UNDECIDED, not rejected. Chloroplast location rests independently on primary targeting-sequence analysis and curated UniProt location; no invented direct imaging claim.

Falcon deep research failed with HTTP403/JWT authentication; the separate Perplexity-lite fallback failed with HTTP401 insufficient_quota. Logs are in .cache/module-audit-logs/sulfate-APR1-{falcon,perplexity-lite}.log. No provider-labelled report was written manually. Literature evaluation above is the manual fallback.

### Independent annotation-reviewer QA

The module reviewer independently read the APR1 activity evidence and agrees
with the 19-row action set, including retention of the negative thylakoid flag
and the two unresolved suborganellar assertions. No action or original payload
was changed in QA. Refinement reasons now distinguish catalytic activity,
sulfur-group redox class, and donor-unspecified APS reduction instead of reusing
one explanation for all terms.

The local `interpro/panther/PTHR46482/PTHR46482-paint.tsv` records an IBD for
GO:0009973 at PTN008207357 with AT1G62180, AT4G04610 and AT4G21990 as descendant
evidence. Structured propagation metadata therefore records a granularity
refinement with `SUPPORTS_TRANSFER`, not a phylogenetic failure. APR1's own
AT4G04610 evidence is legitimate target grounding, not circularity. GSH-specific
chemistry remains supported by the purified target and is not represented as a
nonexistent ontology parent-child edge.
