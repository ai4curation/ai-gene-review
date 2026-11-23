# ONCVO Q25634 / GluClX notes

- 2026-11-22: fetched `ONCVO` `Q25634` from exact UniProt accession `Q25634`
  into an accession-named `genes/ONCVO/Q25634/` folder. The live UniProtKB
  record resolved to `Q25634_ONCVO`, gene `GluClX`, protein
  `Glutamate-gated chloride channel`, EMBL `U59745` / `AAB03404.1`, and
  PANTHER `PTHR18945`.
- `just fetch-gene-pmids ONCVO Q25634` found no GOA PMID references; the
  seeded rows were all automated InterPro, UniProt-SubCell, or combined
  automated mappings.
- The UniProt record itself cites PMID:9051935 for `U59745`, so
  `just fetch-pmid 9051935` cached the abstract-only Parasitology review.
- `just paint-losses ONCVO Q25634` reported that Q25634 is in PANTHER
  PTHR18945 but is not a leaf of the cached PAINT tree, so no IRD or IKR loss
  could be checked on this lineage.
- `just deep-research-falcon ONCVO Q25634 --fallback perplexity-lite` failed
  because `agentapi` was not on `PATH`; the wrapper reported only
  `claude_code` available and both configured providers failed before writing
  a deep-research report.

## Curation Notes

`Q25634` is a partial O. volvulus GluClX sequence, not a full experimentally
reconstituted parasite receptor. UniProt flags the record as `Fragment` and the
feature table has `NON_TER` at residue 351. The record predicts the signal
peptide plus M1 and M3, and direct sequence inspection places the `PAR`
anion-selectivity motif and complete M2 pore helix in the intervening
`VPARVSLGVT TLLTMTTQAS` sequence; the fragment lacks the M3-M4 intracellular
loop and M4 helix. The CDD cross-references are GluCl-specific for the
extracellular domain and anion-selective for the transmembrane region, and the
EMBL `U59745` accession is tied to Cully et al.'s invertebrate
glutamate-gated chloride-channel review.

The review therefore keeps the generic InterPro2GO receptor and channel rows
and adds inferred `contributes_to` `GO:0008068` plus `GO:1902476` only with a
fragment caveat. The generic `GO:0005216` channel row is marked `TOO_GENERAL`
against the inferred GluCl/chloride assignments on the same "which ion?"
reading as the generic transport rows. The review does not assert a homomeric
channel, exact Onchocerca subunit composition, ivermectin sensitivity, or a
module association: those need a full-length sequence and direct
reconstitution.
