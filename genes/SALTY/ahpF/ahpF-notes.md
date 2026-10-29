# SALTY ahpF: complete annotation review

## 2026-10-26 — source-grounded review

Reviewed all 11 seeded annotation rows, preserving every non-review field and both raw source files. No NEW annotation is added. Default Falcon plus perplexity-lite fallback and publication retrieval were actually attempted by the shared acquisition worker; provider attempts failed and no provider report was fabricated. The fitness fetch also failed because no FEBA source was reachable. Manual primary/source assessment supplies the review.

Salmonella typhimurium AhpF is a flavoprotein disulfide reductase that regenerates oxidized AhpC for peroxide detoxification. Its C-terminal FAD/pyridine-nucleotide region supplies electrons to an N-terminal thioredoxin-like relay that reduces the AhpC disulfide. The characterized Salmonella enzyme is homodimeric and accepts NADH and NADPH, with NADH preferred in the tested DTNB reductase assays. Free thioredoxin reduction is negligible on standard assay timescales compared with canonical thioredoxin reductase, although very slow side activity is detectable.

### Evidence and scope

PMID:8555198 explicitly compares purified native Salmonella protein with recombinant Salmonella protein expressed in E. coli, finding the same tested activities. Its apparent NADH/NADPH Km difference is from DTNB reduction, not a universal cellular flux ratio. PMID:8555199 assigns peroxide chemistry to AhpC and regeneration to AhpF. PMID:2643600 purified the system from an oxyR1 regulatory mutant; the current database LT2 annotation does not establish that every later experiment used unmodified LT2.

PMID:10828978 full text is normally cached at publications/url_https___citeseerx.ist.psu.edu_document_doi_9595b48acf5bd878f3f207ac05949130853a61be&repid_rep1&type_pdf.md. It uses Salmonella AhpF/pAF1-derived fragments expressed in E. coli, while free Trx/TrxR are E. coli comparators. Standard NADH/DTNB- and insulin-linked Trx assays were ineffective, but slow reduction occurred after 20 h; intact AhpF was even slower than the isolated C-terminal fragment. Therefore the GO:0004791 correction is a supported specificity broadening to GO:0047134, not a universal assertion of zero thioredoxin side activity. The inspected PAINT PTN005133404 node spans canonical TrxR and AhpF, and the existing family review independently recognizes this divergence. No family file is edited here.

### Review decisions and provenance

The coupled NADH-dependent peroxide-reduction rows are retained as valid component activities. Core functions distinguish direct molecular function from contribution; ordinary relationship qualifiers never determine the action. Homodimeric AhpF does not imply a fixed permanent AhpCF supercomplex. Broad binding terms refine to the independently supported NAD and FAD binding functions. Obsolete GO:0008379 is independently checked against QuickGO before refinement to the existing peroxiredoxin term.

Source access and short mined findings are recorded per reference in the review. Questions about unknown native donor kinetics or localization remain biological questions; failure of a research service is not a biological knowledge gap. Focused checks, record-section backfill, rendering and helper provenance are recorded in the panel handoff.


## 2026-10-27 — PR #5595 reference and wording follow-up

Resolved article identities using canonical PMID-to-full-text mappings in `modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/reference-identities.yaml.txt`; URL sources remain intact for quotations not present in cached abstracts. Added canonical article titles alongside immutable extraction metadata and removed source-ID/workflow boilerplate from reasons. Annotation payloads and actions remain unchanged.
