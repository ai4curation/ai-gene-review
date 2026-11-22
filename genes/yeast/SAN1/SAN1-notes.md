# SAN1 curation notes

## 2026-09-29 IBA propagation re-review and recent-literature check

Rechecked the three SAN1 IBA rows from `GO_REF:0000033`. UniProt places San1 in
PANTHER family `PTHR15710` ("E3 UBIQUITIN-PROTEIN LIGASE PRAJA"), but this
workspace does not have a cached `interpro/panther/PTHR15710/` PAINT export.
The GOA rows still provide the immediate PTN source nodes: `GO:0006511` and
`GO:0061630` trace to `PANTHER:PTN001864905`, while the non-core cytoplasm
annotation traces to `PANTHER:PTN004565028`.

Kept the two core IBA rows (`ubiquitin-dependent protein catabolic process` and
`ubiquitin protein ligase activity`) as `ACCEPT` / `NO_FAILURE_CORE`: San1 has
direct budding-yeast evidence as a nuclear RING E3 that ubiquitinates misfolded
or mutant substrates for proteasomal degradation. Kept the cytoplasm IBA row as
`KEEP_AS_NON_CORE` / `NO_FAILURE_NON_CORE`: San1 is primarily nuclear, but GOA
also carries a direct SGD cytoplasm row from Heck et al. 2010 for
chaperone-dependent handling of cytoplasmic misfolded proteins routed to San1.

Searched PubMed and the web for 2023-2026 SAN1/San1 yeast papers. Cached six
relevant primary papers:

- PMID:38302116: abstract-only Genetics study showing San1-dependent degradation
  of nonnative Nup1 in the nuclear pore complex.
- PMID:39617269: full-text JBC study showing quiescent cells retain
  degradation-mediated PQC that can depend on Ubr1 and San1, although Ubr1 is
  dominant for the tested tGnd1/stGnd1 reporters.
- PMID:39855624: abstract-only BBA Gene Regulatory Mechanisms study extending
  San1/Spt16 work by analyzing San1-dependent FACT interactome changes.
- PMID:41370327: full-text PLoS Genetics study implicating San1 and Das1 in
  Mcd1 degradation when cohesin function is aberrant.
- PMID:41511351: full-text Cells study showing San1-dependent proteasomal
  turnover of soluble Htt103QP is required for efficient IBophagy in a budding
  yeast model.
- PMID:42300961: abstract-only FEBS Journal study using UBR1/SAN1 deletion to
  reveal PQC-sensitive DHFR indel variants.

Skipped the PMID:41341165 bioRxiv preprint because it is superseded by the
PMID:41370327 PLoS Genetics paper, and skipped the 2023 Senataxin/ALS review
because it is not about budding-yeast San1 function.

The newer literature extends the set of San1 substrate contexts but does not
change the core molecular picture: San1's central function is still recognition
and RING E3-mediated ubiquitination of misfolded or aberrant proteins for
proteasomal degradation.

## 2026-10-01 current GOA refresh

Forced a current GOA/UniProt refresh, fetched all 12 SAN1 GOA PMIDs, and fetched
the current PTHR15710 PAINT export. The refresh left 20 live GOA rows and the
review now retains five older source assertions as `retired: true` because they
no longer exactly match live GOA:

- `GO:0006511` / IBA / `GO_REF:0000033`: the current PTHR15710 export no longer
  carries this catabolic-process assertion on `PANTHER:PTN001864905`, although
  San1 still has direct IDA/IMP evidence for ubiquitin-dependent protein
  catabolism.
- `GO:0008270` and `GO:0046872` / IEA / `GO_REF:0000043`: the old keyword rows
  disappeared from live GOA; the curated SGD RCA zinc-binding row from
  PMID:30358795 remains live.
- Two `GO:0031249` / IPI / PMID:21211726 rows: DisProt has replaced these
  denatured-protein-binding rows with a live `GO:0051787` misfolded-protein
  binding row for Cdc68/Spt16.

Rechecked all current IBA rows against `interpro/panther/PTHR15710/PTHR15710-paint.tsv`
and kept `propagation_review.source_entities` to the PAINT PTN nodes rather than
the extant `WITH/FROM` members:

- `PANTHER:PTN001864905` still supports inherited `GO:0061630` ubiquitin protein
  ligase activity.
- `PANTHER:PTN004565028` still supports a defensible non-core cytoplasmic
  localization row.
- `PANTHER:PTN008581526` supports inherited `GO:0051788` response to misfolded
  protein, seeded by SGD SAN1. The same node also propagates Candida-seeded
  `GO:0036503` ERAD quality control pathway to budding-yeast SAN1; changed that
  row to `MODIFY` because San1 is a nuclear/cytosolic misfolded-protein PQC
  ligase, not an ERAD ligase, and `GO:0051788` is the correct inherited process.

The refresh also materialized the previously proposed `GO:0016567` protein
ubiquitination annotation from PMID:15078868, which is now `ACCEPT`, and added
the direct SGD `GO:0061630` row from the same paper. The new DisProt
`GO:0045732` positive regulation of protein catabolic process row from
PMID:21211726 was changed to `MODIFY` toward protein ubiquitination / response
to misfolded protein, because San1 executes substrate ubiquitination rather than
indirectly regulating protein catabolism.

Repeated the PubMed/web search for newer yeast SAN1/San1 papers. PMID:42300961
is the newest cached direct hit; it uses `ubr1`/`san1` deletion to stabilize
DHFR indel variants, but does not change the core San1 curation.

## PR #3789 follow-up

- Dropped `GO:0006511` from the first core function because it is an ancestor of
  `GO:0071630` already listed on the same activity.
- Rewrote the `GO:0005737` cytoplasm IBA to keep the row conservatively on the
  strength of SGD/PAINT localization rather than with quotes that only locate
  cytoplasmic substrates.
- Recast the `GO:0036503` ERAD IBA as a compartment-specific PAINT mismatch
  rather than a parent/child granularity problem.
- Clarified that the `GO:0036503` and `GO:0045732` MODIFY replacements are
  already present as live SAN1 annotations, cross-cited PMID:15078868 on the
  broad `GO:0004842` transferase row, and reframed the proposed sensor term
  against GO's usual has-input modeling pattern.
