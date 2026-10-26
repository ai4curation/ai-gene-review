# BACSU ahpF: complete annotation review

## 2026-10-26 — source-grounded review

Reviewed all 16 seeded annotation rows, preserving every non-review field and both raw source files. No NEW annotation is added. Default Falcon plus perplexity-lite fallback and publication retrieval were actually attempted by the shared acquisition worker; provider attempts failed and no provider report was fabricated. The fitness fetch also failed because no FEBA source was reachable. Manual primary/source assessment supplies the review.

Bacillus subtilis AhpF is a flavoprotein disulfide reductase that regenerates oxidized AhpC for peroxide detoxification. Its C-terminal FAD/pyridine-nucleotide region supplies electrons to an N-terminal thioredoxin-like relay that reduces the AhpC disulfide. B. subtilis AhpF is encoded with AhpC in the stress-responsive ahpCF operon. Its AhpC-directed catalytic assignment is supported by this native context and conserved AhpF domains; target-specific donor kinetics and any peripheral-membrane pool remain unresolved.

### Evidence and scope

PMID:8555198 explicitly compares purified native Salmonella protein with recombinant Salmonella protein expressed in E. coli, finding the same tested activities. Its apparent NADH/NADPH Km difference is from DTNB reduction, not a universal cellular flux ratio. PMID:8555199 assigns peroxide chemistry to AhpC and regeneration to AhpF. PMID:2643600 purified the system from an oxyR1 regulatory mutant; the current database LT2 annotation does not establish that every later experiment used unmodified LT2.

PMID:8932314 and PMID:8932315 provide native operon/induction/perturbation evidence. Exponential-phase cumene hydroperoxide sensitivity and compensatory H2O2 resistance must be distinguished. These accessible abstracts do not establish purified Bacillus partner kinetics. Normal PMC/publisher/EuropePMC retrievals failed to recover full primary text; the 306-byte PMC download-interstitial cache is excluded from supporting evidence. The AhpC catalytic mechanism and AhpF donor assignment combine native locus/physiology with specific domain and curated orthology evidence.

PMID:10828978 full text is normally cached at publications/url_https___citeseerx.ist.psu.edu_document_doi_9595b48acf5bd878f3f207ac05949130853a61be&repid_rep1&type_pdf.md. It uses Salmonella AhpF/pAF1-derived fragments expressed in E. coli, while free Trx/TrxR are E. coli comparators. Standard NADH/DTNB- and insulin-linked Trx assays were ineffective, but slow reduction occurred after 20 h; intact AhpF was even slower than the isolated C-terminal fragment. Therefore the GO:0004791 correction is a supported specificity broadening to GO:0047134, not a universal assertion of zero thioredoxin side activity. The inspected PAINT PTN005133404 node spans canonical TrxR and AhpF, and the existing family review independently recognizes this divergence. No family file is edited here.

The raw UniProt record retains a legacy NADH:ubiquinone/proton-pumping annotation. PMID:8125345 describes a partial bglA-linked ORF labeled through homology; complete BSU40100 carries both AhpF N-terminal domains and TIGR03140. GO:0008137 explicitly includes four-proton translocation, which is not the AhpF disulfide relay. Its electronic activity is corrected to protein-disulfide reduction and its downstream proton-transport propagation is removed. This does not deny possible low-level quinone chemistry. Peripheral membrane localization is UNDECIDED because soluble architecture alone cannot disprove a peripheral pool.

### Review decisions and provenance

The coupled NADH-dependent peroxide-reduction rows are retained as valid component activities. Core functions distinguish direct molecular function from contribution; ordinary relationship qualifiers never determine the action. Homodimeric AhpF does not imply a fixed permanent AhpCF supercomplex. Broad binding terms refine to the independently supported NAD and FAD binding functions. Obsolete GO:0008379 is independently checked against QuickGO before refinement to the existing peroxiredoxin term.

Source access and short mined findings are recorded per reference in the review. Questions about unknown native donor kinetics or localization remain biological questions; failure of a research service is not a biological knowledge gap. Focused checks, record-section backfill, rendering and helper provenance are recorded in the panel handoff.
