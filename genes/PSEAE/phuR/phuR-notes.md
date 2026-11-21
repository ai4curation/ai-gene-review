# phuR (PA4710, Q9HV88) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group hasR/phuR)

Fetched with `just fetch-gene PSEAE phuR`. No deep-research provider file was generated.

The strongest row on the entry is the GO:0015232 IMP, because it comes with the control that makes
a phenotype attributable: [PMID:10658665 "Mutant strains with deletions in phuR and phuSTUV showed
greatly reduced growth with either haem or haemoglobin as the only iron source: the defects were
complemented by plasmids harbouring the phuR or the phuSTUV genes, respectively."] Localisation is
direct too: [PMID:10658665 "Both the PhuR and HasR proteins were detected in the outer-membrane
fraction of P. aeruginosa grown in low-iron media."] And the iron-response row is backed by
[PMID:10658665 "Expression of phuR and phuSTUVW from mapped transcriptional-start sites occurred
under iron-restricted growth conditions and was directly controlled by the Fur protein."]

### Same siderophore finding as hasR

phuR carries the identical three siderophore rows from the same node, PTN004738955, and phuR sits
in SF29, "Heme_hemoglobin uptake outer membrane receptor". The tree analysis is written up once in
the hasR notes and the GO_CENTRAL defect is recorded once on the hasR review; this review
cross-references it so the upstream report is filed once rather than twice.

### Annotation decisions

- ACCEPT: GO:0015232 (IEA, IMP), GO:0015886 (IEA, IMP), GO:0009279 (IBA, IEA), GO:0071281 (EXP).
- MODIFY: both GO:0019867 rows to GO:0009279.
- TOO_GENERAL: GO:0022857. KEEP_AS_NON_CORE: GO:0055085, for the ancestry reason in the hasR notes.
- REMOVE: GO:0015344, GO:0044718, GO:0033214.
