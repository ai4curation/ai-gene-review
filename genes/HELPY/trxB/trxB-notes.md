# trxB: Helicobacter pylori 26695

## 2026-10-26 — strain-resolved antioxidant review

Applied the review and annotation-reviewer workflows to every seeded row. Original machine annotation fields, order, qualifiers and flags are preserved. No NEW annotations are proposed. Actual Falcon plus perplexity-lite attempts failed (403/authentication or quota failure); no generated report was fabricated. Publication acquisition ran in parallel and succeeded. The required FEBA fitness attempt failed because no HELPY mapping/local database or reachable source was available; no fitness file was written. Actual logs are retained in `.cache/module-audit-logs/helpy-review/`.

PMID:11222594 was read in full through the normal cached author PDF (`publications/url_https___scb.wfu.edu_Poole-files_Baker_Hpylori.pdf.md`). The Methods distinguish 26695 genomic DNA, TIGR-ATCC genomic clones, recombinant E. coli expression, and native-component reconstitution. Table 2 identifies P21762 explicitly; HP0824 and HP0825 identify Trx1 and TrxR. Figures 2–6 measure the native H. pylori system. In contrast, fine AhpC/peroxide kinetic measurements deliberately replace native TrxR with E. coli TrxR to suppress background NADPH oxidase activity. This distinction is retained in all core descriptions.

Live QuickGO definitions were checked on 2026-10-26. GO:0008379 is obsolete; current GO:0140824 explicitly names thioredoxin-dependent hydroperoxide reduction. GO:0102039 specifically requires NADH. GO:0019430 includes cellular superoxide removal and is not restricted to a direct dismutase reaction. Canonical PMID records and the full author PDF are cited separately so full-text quotations retain recoverable provenance. No GOA file, ARBA-only statement, protein name, keyword or evidence-existence field is used as functional support.

The two NADPH-dependent thioredoxin reductase rows are accepted using the native TrxR assays, including donor substitution and reduction of both Trx1 and Trx2 (PMID:11222594). Broad oxidoreductase activity is refined to the already-present specific reductase term. FAD is an integral enzyme cofactor; native spectral evidence and curated cofactor annotation support its description without a redundant NEW binding annotation.

Cytoplasm is retained at the precision of the curated by-similarity location, not upgraded merely from heterologous solubility. The IPR005982 superoxide-removal row is UNDECIDED. Tested reductase/peroxide-relay chemistry and paraquat-sensitivity phenotypes do not establish a specific superoxide-removal step, but absence of direct SOD chemistry does not disprove multistep participation. The precise unresolved mechanism is recorded rather than an unsupported family-wide negative.


## 2026-10-27 — PR #5595 reference and wording follow-up

Resolved article identities using canonical PMID-to-full-text mappings in `modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/reference-identities.yaml.txt`; URL sources remain intact for quotations not present in cached abstracts. Added canonical article titles alongside immutable extraction metadata and removed source-ID/workflow boilerplate from reasons. Annotation payloads and actions remain unchanged.
