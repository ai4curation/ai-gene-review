# TAS1R1 (9AVES, A0A7L3NBT4) curation notes

## Identity

- UniProt A0A7L3NBT4, gene `Tas1r1`, ORF `OREMEL_R04111`, organism
  *Oreotrochilus melanogaster* (black-breasted hillstar hummingbird; family
  Trochilidae; NCBI taxon 689266). Unreviewed TrEMBL entry, "Flags: Fragment"
  (572 aa, `NON_TER` at both position 1 and 572), from the Bird 10,000
  Genomes (B10K) project preliminary WGS assembly
  ["Bird 10,000 Genomes (B10K) Project - Family phase." — genes/9AVES/TAS1R1/TAS1R1-uniprot.txt].
- The original `taxon`/`gene_symbol` fields seeded by `just fetch-gene` were
  wrong/placeholder (`NCBITaxon:8782` = Aves class, and `gene_symbol:
  A0A7L3NBT4`). Corrected to `NCBITaxon:689266` / `Oreotrochilus
  melanogaster` (matches `OX NCBI_TaxID=689266` in the cached UniProt
  record) and `gene_symbol: TAS1R1`.
- Domain architecture (ANF_lig-bd_rcpt/IPR001828, GPCR_3/IPR000337,
  GPCR_3_9-Cys_dom/IPR011500, GPCR_3_C/IPR017978; PANTHER PTHR24061 "CALCIUM
  SENSING RECEPTOR-RELATED", subfamily PTHR24061:SF3 "TASTE RECEPTOR TYPE 1
  MEMBER 1") is fully consistent with class C GPCR / TAS1R1 identity.

## Key background biology (used for description/core_functions)

Baldwin et al. 2014 Science, "Evolution of sweet taste perception in
hummingbirds by transformation of the ancestral umami receptor"
[PMID:25146290, full text cached, PMC4302410]:

- Most vertebrate T1R1-T1R3 heterodimers (including chicken and the
  insectivorous chimney swift, the closest living relative of hummingbirds)
  detect amino acids (umami): ["cells expressing chicken or swift T1R1-T1R3
  failed to detect carbohydrates at any concentration tested and instead
  recognized alanine and serine" PMID:25146290].
- Birds generally lack TAS1R2 ["We observed the widespread absence in birds
  of an essential subunit (T1R2) of the only known vertebrate sweet
  receptor" PMID:25146290].
- In hummingbirds, the ancestral T1R1-T1R3 umami receptor was repurposed to
  detect carbohydrates instead: ["Receptor expression studies revealed that
  the ancestral umami receptor (the T1R1-T1R3 heterodimer) was repurposed
  in hummingbirds to function as a carbohydrate receptor" PMID:25146290].
- The receptor is an obligate heterodimer — neither subunit alone responds:
  ["Responses were not observed when T1R1 or T1R3 alone was used,
  suggesting that hummingbird T1R1-T1R3 functions as an obligate
  heterodimer" PMID:25146290]. T1R1 itself also carries sites under
  putative positive selection and contributes to sugar responsiveness (a
  chicken-T1R1 + hummingbird-T1R3 chimera prefers amino acids), so T1R1 is
  not just a passive bystander to T1R3's changes.
- Some residual amino-acid sensitivity is retained even in hummingbirds
  ["Low-affinity responses were observed to some amino acids"
  PMID:25146290], so the functional shift to sweet is not necessarily a
  100%-complete loss of umami sensitivity — it is a change in *primary*
  ligand preference/receptor role.
- Behavioral confirmation: captive ruby-throated hummingbirds and wild
  Anna's/black-chinned hummingbirds show taste preferences that track
  T1R1-T1R3 agonist activity (erythritol, sorbitol) versus receptor-inactive
  human sweeteners (aspartame, cyclamate, acesulfame K) ["We propose that
  changing taste receptor function enabled hummingbirds to perceive and use
  nectar, facilitating the massive radiation of hummingbird species"
  PMID:25146290].

**Important species caveat**: Baldwin et al. cloned and assayed T1R1/T1R3
from *Calypte anna* (Anna's hummingbird), not from *Oreotrochilus
melanogaster*. There is no UniProt entry and (per the falcon deep-research
search) no publication testing *O. melanogaster*, `A0A7L3NBT4`,
`OREMEL_R04111`, or `NXU76429.1` specifically
[genes/9AVES/TAS1R1/TAS1R1-deep-research-falcon.md: "no retrieved study
mentions A0A7L3NBT4, OREMEL_R04111, NXU76429.1, or experimentally tests *O.
melanogaster* Tas1r1"]. The sweet-taste-repurposing claim for this exact
gene/species is therefore a strong, well-supported lineage-level inference
(hummingbirds broadly; ancestral-state reconstruction across multiple major
hummingbird clades in later comparative work — Cockburn 2022, not
independently verified/cached here, only summarized secondhand in the
falcon deep-research report), not a direct experimental result for this
accession.

## Annotation review summary

GOA seeded 6 rows, all IEA (InterPro/ARBA/TreeGrafter pipelines; no
gene-specific PMIDs were found by `fetch-gene-pmids`):

- GO:0004930 (GPCR activity), GO:0005886 (plasma membrane), GO:0007186
  (GPCR signaling pathway) — **ACCEPT**. GO:0016020 (membrane) —
  **MARK_AS_OVER_ANNOTATED** (redundant given the specific plasma-membrane
  annotation). GO:0050909 (sensory perception of taste) —
  **KEEP_AS_NON_CORE** (redundant given the specific taste-modality terms
  below). These generic-term calls are standardized across all five
  taste-receptor genes in this PR (human TAS2R38/TAS2R16, chimp TAS2R38,
  9AVES TAS1R1/TAS1R3): GO:0016020 → MARK_AS_OVER_ANNOTATED, GO:0050909 →
  KEEP_AS_NON_CORE, GO:0004930/GO:0007186 → ACCEPT, wherever a more specific
  sibling term is independently held. They hold regardless of whether the
  receptor's actual ligand is an amino acid or a sugar, so they don't depend
  on resolving the umami-vs-sweet question.
- GO:0050917 (sensory perception of umami taste), from TreeGrafter/PANTHER
  node PANTHER:PTN009077744 — **KEEP_AS_NON_CORE** (revised from an earlier
  MODIFY, per PR review — see "Revisions after PR review" below).
  GO:0050917 is defined specifically as perception of glutamate-rich/savory
  taste; that's the *ancestral* TAS1R1 function, retained in chicken/swift,
  and the Baldwin 2014 data show low-affinity amino-acid responses persist
  even in the hummingbird lineage. Since TAS1R1 and TAS1R3 form an obligate
  heterodimer with one shared ligand spectrum, this row is kept identical to
  the equivalent GO:0050917 call on TAS1R3 (`genes/9AVES/TAS1R3`), which
  already used KEEP_AS_NON_CORE rather than MODIFY.
- Also added a **NEW** proposed annotation for GO:0050916 (sensory
  perception of sweet taste), mirroring the annotation TreeGrafter *did*
  already assign to the partner subunit TAS1R3 in this same genome
  (`genes/9AVES/TAS1R3/TAS1R3-ai-review.yaml`, which carries both GO:0050916
  and GO:0033041 "sweet taste receptor activity" from PANTHER node
  PTN009078551 — TAS1R1 and TAS1R3 were evidently placed in different
  PANTHER/TreeGrafter nodes with different levels of annotation
  granularity/currency). Encoded as `ISS` with no `GO_REF`, since this is a
  curator-proposed cross-species inference, not a genuine TreeGrafter row for
  this record (see "Revisions after PR review" below).

## Revisions after PR review

The `ai4c-reviewer` bot's CHANGES_REQUESTED review on PR #3050 (2026-09-16)
flagged three issues in the original version of this file, all fixed:

1. The GO:0050916 `NEW` row carried `evidence_type: IEA` and
   `original_reference_id: GO_REF:0000118`, provenance it does not actually
   have (it is absent from `TAS1R1-goa.tsv`). Fixed to `evidence_type: ISS`
   with no `original_reference_id`, matching the repo's `NEW`-row pattern
   (e.g. `genes/human/NADK2`).
2. GO:0050916 was proposed twice — once via `proposed_replacement_terms` on
   the GO:0050917 `MODIFY`, once as the standalone `NEW` row. Resolved by
   dropping the `MODIFY`/`proposed_replacement_terms` mechanism (see #3) and
   keeping only the standalone `NEW` row.
3. TAS1R1 and TAS1R3 — obligate partners in the same heterodimer — had
   opposite calls on the identical TreeGrafter GO:0050917 row (TAS1R1
   MODIFY vs TAS1R3 KEEP_AS_NON_CORE). Since the two subunits share one
   ligand spectrum, they cannot carry different retained-function
   judgments; TAS1R1 was changed to KEEP_AS_NON_CORE to match TAS1R3, whose
   reasoning (residual low-affinity amino-acid responses per PMID:25146290)
   is the better-supported reading.

core_functions models TAS1R1 as contributing (not independently enabling)
sweet taste receptor activity (GO:0033041), since T1R1 is an obligate
heterodimer partner rather than a standalone functional receptor; its own
independent activity is modeled as the general GO:0004930 (G
protein-coupled receptor activity).

## Open items / caveats carried into suggested_questions & suggested_experiments

- No direct evidence (sequence-complete transcript, tissue expression,
  ligand assay) exists for *O. melanogaster* TAS1R1 itself; the fragment's
  N- and C-terminal boundaries are unresolved (`NON_TER` at both ends), so
  even basic completeness of the coding sequence is unconfirmed.
- High-Andean hummingbirds (Oreotrochilus, "hillstars") have unusual
  thermal/dietary ecology (torpor, high-altitude nectar) that could
  plausibly further tune receptor pharmacology relative to the lowland
  *Calypte anna* data — an open, testable question rather than an assumed
  fact.

## Validation

`just validate 9AVES TAS1R1` passes cleanly (0 errors, 0 warnings) after
adding a `file:9AVES/TAS1R1/TAS1R1-deep-research-falcon.md` citation into
the GO:0050917 review (validator otherwise warns that no annotation cites
the available deep-research file).
