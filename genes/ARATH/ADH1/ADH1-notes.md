# ADH1 research notes


## 2026-10-25 alcoholic-fermentation member audit

P06525 / At1g77120 is the plant class-P ADH1, distinct from HOT5/GSNOR (At5g43940). PMID:23707506 demonstrates broad primary/secondary alcohol activity, so GO:0004022 remains informative beyond ethanol. PMID:38308388 directly compares purified ADH1 and GSNOR, with distinct ethanol/GSNO specificity and catalytic cavities. PMID:9215914 demonstrates class-P divergence from ancestral class III. The existing interpro/panther/PTHR43880/PTHR43880-review.yaml specifically calls for pruning the SF26 branch of PTN000191653 for GO:0051903 and GO:0046294. REMOVE on those two IBA rows therefore challenges transfer into a documented derived branch, not the number of donors or the validity of ancestral class-III functions. GSNO discrimination is not mislabeled as a direct negative hydroxymethylglutathione assay.

Hypoxia response rows refine to the existing cellular response; PMID:12857811 supports metabolic participation rather than positive regulation of that response. ADH1 overexpression did not improve survival there, whereas null mutants were impaired. Cold, ABA, salt, water, sucrose, caffeine and peroxide induction remain precise contextual non-core responses. PMID:12231733 explicitly reports that ADH activity is not required for the freezing tolerance tested. The estradiol observation in PMID:18441225 uses the engineered XVE/RAP2.12 induction system; it does not establish native estrogen signaling. NOT-Golgi and plasma-membrane rows are UNDECIDED pending target-specific proteomic evidence; the negated flag is preserved. Cytosol is retained with curator evidence and independent curated cytoplasmic localization.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43880; ALCOHOL DEHYDROGENASE; 1.
- DR   PANTHER; PTHR43880:SF26; ALCOHOL DEHYDROGENASE CLASS-P; 1.

PMID:30861072 (PMC6436157), “Conservation of ethanol fermentation and its regulation in land plants”, was force-refetched successfully with full text. It detects ethanol output even in adh1, adh1 adh2 and pdc1 pdc2 seedlings. Conserved native ethanol output therefore does not establish exclusive reliance on these exact paralogs across plants. The tested Marchantia ADH-like candidate did not complement Arabidopsis ADH1 and groups with GSNOR-like proteins; no functionally validated liverwort ADH1 exemplar is added from that candidate.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 52 rows; ACCEPT=13, KEEP_AS_NON_CORE=20, MODIFY=15, REMOVE=2, UNDECIDED=2. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate ARATH ADH1` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
