# YAR1 annotation re-review notes

## Scope and reconciliation

Dedicated re-review completed 2026-08-28 against `YAR1-goa.tsv`, UniProt
P46683, the Falcon synthesis, all five cached PMID records, the focused
OpenScientist hypothesis report, and the current PTHR24198 PAINT table. The GOA
has 19 physical rows and 19 qualifier-aware signatures; all are represented
one-for-one. All rows are positive, with no NOT or isoform-specific annotations.

## PAINT provenance

All four IBA rows trace to `PANTHER:PTN000917496` in the very broad ankyrin-
repeat family PTHR24198. UniProt and PANTHER place Yar1 in PTHR24198:SF165,
officially `ANKYRIN REPEAT-CONTAINING PROTEIN-RELATED`; the local membership
table shows this subfamily also contains highly diverse ankyrin proteins.

The exact pinned GOA traces are:

- GO:0001228: `PANTHER:PTN000917496|PomBase:SPAC22F3.09c|SGD:S000000913|SGD:S000002214`
- GO:0045944: `CGD:CAL0000174900|CGD:CAL0000183437|CGD:CAL0000186541|PANTHER:PTN000917496|PomBase:SPAC22F3.09c|PomBase:SPBC336.12c|PomBase:SPBC725.16|SGD:S000000913|SGD:S000002214|SGD:S000004172|UniProtKB:Q5B8H6`
- GO:0030907: `PANTHER:PTN000917496|PomBase:SPAC22F3.09c|PomBase:SPBC336.12c|PomBase:SPBC725.16|SGD:S000002214|SGD:S000004172`
- GO:0033309: `PANTHER:PTN000917496|SGD:S000000913|SGD:S000004172`

The current PAINT table still places GO:0001228, GO:0045944, and GO:0030907 at
PTN000917496 with the same experimentally grounded transcription-factor source
sets. Those sources support their own transcription biology but not transfer to
Yar1. The APSES-domain argument applies specifically to GO:0001228. For MBF,
SBF, and broader transcription regulation, the donor sets also contain
Swi6/Cdc10-like ankyrin proteins that genuinely lack APSES domains; Yar1 is not
their co-ortholog but a much smaller 200-residue protein with only two ankyrin
repeats, and no Yar1 study reports cell-cycle or promoter-association evidence.
These are `PROPAGATION_BAD` calls, not weak-source or donor-count arguments. The
SBF-complex term GO:0033309 is absent from current PAINT, so its pinned 2018 row
is additionally `SOURCE_STALE_OR_MISSING`. PTN labels are kept as bare
`PANTHER:PTN000917496`.

The current node also has positive IBD assertions for GO:0000978
`RNA polymerase II cis-regulatory region sequence-specific DNA binding` and
GO:0000082 `G1/S transition of mitotic cell cycle`, both dated 2026-02-24. These
are absent from the pinned YAR1 GOA snapshot but can propagate on refresh, so the
review raises the broad node placement itself for PAINT-curator reconsideration.

## Experimental biology

Yar1 is a dedicated chaperone for Rps3. The initial study established the
specific physical and genetic context: [PMID:15611164, "We provide genetic and
biochemical evidence that Yar1, a small ankyrin-repeat protein, physically
interacts with RpS3, a component of the 40S subunit, and with Ltv1, a protein
recently identified as a substoichiometric component of a 43S preribosomal
particle."] RPS3 dosage suppresses both major yar1 phenotypes: [PMID:15611164,
"Overexpression of RPS3 suppresses both the stress sensitivity and the ribosome
biogenesis defect of Deltayar1 mutants"].

Focused work directly establishes the carrier/holdase-like mechanism:
[PMID:22570489, "We further show that Yar1 protects Rps3 from aggregation in
vitro and increases its solubility in vivo."] The same abstract supports the
delivery route: [PMID:22570489, "Here, we report that the ankyrin repeat protein
Yar1 directly interacts with the small ribosomal subunit protein Rps3 and
accompanies newly synthesized Rps3 from the cytoplasm into the nucleus where
Rps3 is assembled into pre-ribosomal subunits."]

Full-text PMID:26112308 independently demonstrates co-translational specificity:
[PMID:26112308, "Affinity purification of four chaperones (Rrb1, Syo1, Sqt1 and
Yar1) selectively enriched the mRNAs encoding their specific ribosomal protein
clients (Rpl3, Rpl5, Rpl10 and Rps3)."] The paper describes Yar1 as a holding
chaperone protecting Rps3 from illicit interactions and aggregation rather than
a general folding enzyme.

## Curation decisions and limitations

The four transcription-related IBAs are removed because target-specific
biochemistry and domain architecture contradict transcription-factor or MBF/SBF
complex roles. This conclusion is independently consistent with the focused
OpenScientist report, but the report's incorrect PTHR43828/SF10 family identifier
is not used; the repository's PTHR24198:SF165 membership and current PAINT table
are authoritative for provenance.

GO:0051082 `unfolded protein binding` is obsolete in current GO, whose obsoletion
comment recommends replacement by an activity term. Both rows are modified to
the more specific GO:0140597 `protein carrier chaperone`. This is not a generic
holdase inference:
Yar1 binds nascent Rps3, prevents aggregation, maintains solubility, and
accompanies the client toward its assembly site. The protein-binding rows remain
marked over-annotated because the specific Rps3 carrier-chaperone term is more
informative.

The PMID:14562095 cytoplasm HDA is accepted with explicit evidence restraint.
The cache is abstract-only and lacks the gene-specific localization table, but
cytoplasmic Yar1 is independently established by direct Rps3-accompaniment work;
the HDA is therefore biologically concordant rather than removed or treated as
the sole evidence. PMID:15611164 and PMID:22570489 are also abstract-only in the
cache, whereas PMID:26112308 and PMID:37968396 have full text. The individual
Yar1-Rps3 row from the 2023 interactome is in the dataset rather than the cached
prose, so that reference is recorded as UNVERIFIED for the exact row.

Osmotic- and oxidative-stress response annotations are kept as non-core mutant
phenotypes. Ribosomal small-subunit biogenesis, Rps3 localization regulation,
cytoplasm-to-nucleus distribution, and the downstream 40S export phenotype are
retained. The core synthesis is the Rps3-specific carrier-chaperone role in 40S
biogenesis.

## Final action profile

The 19 physical rows have 9 ACCEPT, 4 REMOVE, 2 MODIFY, 2
MARK_AS_OVER_ANNOTATED, and 2 KEEP_AS_NON_CORE decisions. There are no PENDING,
UNDECIDED, or NEW rows, and COMPLETE status remains justified.
