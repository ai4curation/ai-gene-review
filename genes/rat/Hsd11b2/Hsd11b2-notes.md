# Hsd11b2 (rat, UniProt P50233) curation notes

## Re-review 2026-10-04

### What GOA changed

The refreshed `Hsd11b2-goa.tsv` carries 25 rows and no new or retired rows relative
to the reviewed set (no `retired: true` rows, no `action: PENDING` rows were seeded).
The refreshed UniProt record (P50233) is substantially expanded relative to the text
the original review quoted: it now documents the androgen-directed activities
(11beta-hydroxytestosterone to 11-ketotestosterone, 11beta-hydroxyandrostenedione to
11-ketoandrostenedione), the oxysterol activity
[UniProtKB:P50233 "Catalyzes the conversion of 7-beta-hydroxycholesterol into 7-ketocholesterol (7-oxocholesterol), a precursor of 7-keto,27-hydroxycholesterol, which activates smoothened (SMO) and the smoothened signaling pathway"],
the corresponding Rhea reaction (RHEA:68656), a KM of 10 nM for corticosterone, a
microsome/ER subcellular location, the SAME-rat disruption phenotype
[UniProtKB:P50233 "manifesting hypokalaemia by 15 days of age and contributing to salt sensitive hypertension"],
and a CAUTION note
[UniProtKB:P50233 "Rats and mice do not produce appreciable cortisol, because they do not express the 17-alpha hydroxylase (Cyp17a1) enzyme in the adrenals."].

### Actions changed

1. **GO:0045880 positive regulation of smoothened signaling pathway (IEA
   GO_REF:0000107; ISO GO_REF:0000121): REMOVE -> KEEP_AS_NON_CORE.**
   The previous reason asserted that any smoothened effect must be an indirect
   consequence of glucocorticoid inactivation. The donor evidence contradicts this.
   The mouse donor (UniProtKB:P51661 / MGI:MGI:104720) annotation comes from
   PMID:30340023, where HSD11B2 is characterized as an oxysterol synthase acting
   upstream of SMO
   [PMID:30340023 "Either genetic or pharmacologic inhibition of HSD11β2, an oxysterol synthase, attenuates HH signal transduction and the growth of HH pathway-associated medulloblastoma."],
   positioned between PTCH1 and SUFU
   [PMID:30340023 "Like sterol depletion, depleting HSD11β2 attenuated HH signaling in Ptch1−/− MEFs, but not Sufu−/− MEFs, suggesting that HSD11β2 modulates HH signaling downstream of PTCH1 and upstream of SUFU"],
   with rescue by the downstream oxysterols
   [PMID:30340023 "Following genetic or pharmacologic inhibition of HSD11β2, the addition of 7k-C, 7β,27-DHC, and 7k,27-OHC restored HH pathway activity"].
   The glucocorticoid-mediated explanation was tested and excluded in that paper
   [PMID:30340023 "However, deletion of HSD11β2 in the cerebellum did not affect glucocorticoid target gene expression (Figures S5A and S5B), suggesting that HSD11β2 may not be critical for restraining physiological levels of glucocorticoids in the cerebellum."].
   Kept as non-core (not ACCEPT) because the enzyme catalyses a biosynthetic step
   upstream of the SMO ligand rather than acting within the pathway, and because the
   effect is confined to cell types expressing the enzyme in Hedgehog-active domains
   (cerebellar external granule layer, Hedgehog-associated medulloblastoma).
   `propagation_review` on both rows changed from
   `PROPAGATION_BAD`/`ROLE_CONFLATION`/`SUPPORTS_SOURCE_BUT_NOT_TARGET` to
   `NO_FAILURE_NON_CORE`/`SUPPORTS_TRANSFER`.

2. **GO:0047022 7-beta-hydroxysteroid dehydrogenase (NADP+) activity (IEA
   GO_REF:0000120; ISS GO_REF:0000024; ISO GO_REF:0000121):
   MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE.**
   The previous reason called this a family-level SDR transfer. It is not: the
   oxidation is directly demonstrated and isomer-specific
   [PMID:30340023 "HSD11β2 increased 7k-C production in 7β-OHC-treated cells, but not in 7a-OHC-treated cells (Figure 4B)."],
   inhibitor-sensitive in cells and cilia
   [PMID:30340023 "Pharmacologic inhibition of HSD11β2 reduced 7k-C in LLC-PK1 cells and cilia (Figure 4E), further indicating that HSD11β2 generates 7k-C."],
   and the rat UniProt record carries both the conversion and RHEA:68656.
   Retained as non-core with an explicit caveat: the GO term names NADP(+) as
   cofactor, and the cofactor actually used for the 7beta-oxidation by the rat enzyme
   has not been established experimentally (the characterized 11beta-dehydrogenase
   chemistry is NAD(+)-dependent). The ISS row gained a `propagation_review` naming
   the mouse anchor; the ISO row's block changed from
   `PROPAGATION_BAD`/`WRONG_ORTHOLOG_OR_PARALOG`+`FUNCTIONAL_DIVERGENCE` to
   `NO_FAILURE_NON_CORE`/`SUPPORTS_TRANSFER`.

### Other edits (no action changes)

- `description` rewritten as standalone biology. The prior text contained curation
  commentary ("The review accepts ...", "Falcon (Edison Scientific) deep research
  corroborates ...") and asserted Smoothened signalling was an over-extension, which
  is no longer the review's position. The new text adds the KM, the microsome/ER
  location, the AME/salt-sensitive-hypertension consequence of loss, and the two
  secondary activities (11-ketoandrogen production, oxysterol synthesis).
- GO:0005783 endoplasmic reticulum (IEA): kept KEEP_AS_NON_CORE, but the
  `supported_by` quote was the FUNCTION sentence, which says nothing about location;
  replaced with the SUBCELLULAR LOCATION line.
- GO:0007565 female pregnancy (ISO): kept KEEP_AS_NON_CORE, support replaced with the
  UniProt statement that actually bears on pregnancy
  [UniProtKB:P50233 "Plays an important role in maintaining glucocorticoids balance during preimplantation and protects the fetus from excessive maternal corticosterone exposure"],
  and a `propagation_review` added for the mouse donor.
- GO:0034650 cortisol metabolic process (IEA, ISO): MARK_AS_OVER_ANNOTATED retained;
  the UniProt CAUTION note on Cyp17a1 and cortisol in rats and mice was added as
  direct support for the species argument.
- PMID:30340023 added to `references` with four findings and a `reference_review`
  (relevance HIGH, correctness VERIFIED; cached full text read).
- `core_functions` unchanged: NAD(+)-dependent glucocorticoid inactivation remains the
  single core activity, and the two re-rated rows are explicitly secondary.

### Open questions

- Which cofactor does the rat enzyme use for the 7beta-hydroxycholesterol oxidation?
  GO:0047022 specifies NADP(+); the UniProt reaction (RHEA:68656) is written with
  NADP(H), but no rat (or, as far as the cached paper shows, mouse) measurement
  establishes the cofactor for this side reaction. If it is NAD(+)-dependent, the
  correct term would be a 7beta-hydroxysteroid dehydrogenase (NAD+) activity term,
  which does not obviously exist.
- The androgen-directed activities on the UniProt record (11beta-hydroxytestosterone
  to 11-ketotestosterone, 11beta-hydroxyandrostenedione to 11-ketoandrostenedione) are
  "By similarity" and currently have no GO annotation on the rat gene. No NEW term was
  proposed: the evidence is transferred, not rat-specific, and GO:0070523
  (11-beta-hydroxysteroid dehydrogenase (NAD+) activity) already covers the chemistry
  at the general-substrate level.

**Stale UniProt quotes (2026-10-10):** replaced 7 `UniProtKB:P50233` supporting_text quotes (an abridged FUNCTION sentence no longer in the refreshed flat file) with verbatim CATALYTIC ACTIVITY reactions (generic 11beta-hydroxysteroid and corticosterone) and a verbatim FUNCTION sentence on glucocorticoid inactivation from the current `Hsd11b2-uniprot.txt`.
