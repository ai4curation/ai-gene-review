# HexR manual literature research — 2026-11-08

This is a manually authored research record, not output from a deep-research provider.
The review concerns UniProt Q88P32, PP_1021, Pseudomonas putida KT2440
(NCBITaxon:160488). Targets are keyed to the reference metadata; this is not a
fresh sequence alignment between historical experimental constructs and the current assembly.

## Search and access record

Searches covered `19506074 HexR full text KT2440 edd zwf gap1`, `HexR regulation
glucose metabolism sugar isomerase domain`, `HexR acetate putida regulation 2025
2026`, `GSE275525 HexR`, and the exact title of the 2026 regulatory-landscape paper.
The new paper was confirmed through the primary publisher abstract, PubMed and
Europe PMC bibliographic search, rather than inferred from a secondary review.

- [PMID:18245293](https://pmc.ncbi.nlm.nih.gov/articles/PMC2293218/): cached abstract
  and indexed primary full-text Methods, Results, Table 3 and Table 6 inspected.
  Those sections identify KT2440 and isogenic mutants, citrate/glucose culture
  conditions, microarrays and promoter fusions. Local cache remains abstract-only.
- [PMID:19506074](https://pmc.ncbi.nlm.nih.gov/articles/PMC2755860/): cached abstract
  and indexed primary full-text cloning, EMSA, DNase I footprinting, DNA-ITC,
  modeling and discussion sections inspected. The cloning template is explicitly
  KT2440 DNA, with recombinant protein produced in E. coli BL21(DE3). Direct PMC
  page opening encountered a browser challenge; Europe PMC XML retrieval failed.
  These access limits do not erase the indexed assay sections that were available.
- [PMID:41260329](https://doi.org/10.1016/j.ymben.2025.11.014): primary abstract and
  bibliographic metadata inspected; the repository fetcher cached the abstract.
  Published online 2025-11-17 and in Metabolic Engineering 94 (March 2026), 77–89.
  Publisher full-text request returned HTTP 403, and no PMC article was available.
  Full text, target tables and assay-specific assignments remain unverified.
- The 2021 G6PDH isozyme paper (DOI:10.1128/msystems.00014-21) was checked as a
  nomenclature and later-regulation lead, but no new target is asserted from it.
- The 2017 RccR/HexR work in P. fluorescens SBW25 is another-species evidence and
  was not used to manufacture KT2440 targets.

## Established mechanism and target set

The 2008 KT2440 mutant study separates local transcriptional effects from pathway
execution. Removing hexR increases expression of gap-1/PP_1009 and members of the
edd and zwf transcription units. Pedd and Pzwf transcriptional fusions establish
repression under noninducing conditions, with induction upon glucose exposure.
The 2009 purified-protein experiments supply direct promoter binding and mapped
operator footprints at Pedd, Pzwf and Pgap-1. Together these justify three
promoter-level direct repressive relationships. The locus mappings are PP_1010
(edd), PP_1022 (zwfA/zwf/zwf-1), and PP_1009 (gapA, historical gap-1).

The exported relationships preserve promoter scope: shared operon membership does
not mean every downstream coding sequence has its own independently bound promoter.
PP_4488 changed expression in the 2008 hexR mutant, but its proposed binding motif
was not experimentally verified there; it is not added as a direct target.
The same study did not observe HexR autoregulation under its tested conditions.
The gene's membership in the HexR iModulon does not overturn that result or prove
autoregulation.

KDPG causes purified HexR to leave operator DNA. The primary paper's ITC
experiments characterize **DNA** binding, specifically Pzwf oligonucleotides;
they do not locate a KDPG pocket or measure ligand binding to every promoter.
The SIS-domain recognition-site and residue assignment comes from homology
modeling and remains qualified. Likewise, blockage of RNA polymerase progression
is a mechanistic proposal based on operator position, not a directly established
step in an in-vitro transcription assay.

The 2026 study reports a substantially broader carbon-source-dependent regulon,
including positive effects on acetate-associated metabolic programs. This makes
an exclusive, all-context repressor-only account inappropriate. Its abstract does
not identify the gene-level positive targets or resolve their individual assays;
therefore no direct activating edges or activator MF annotation are added from
that abstract. The established negative promoter relationships remain valid.

## GO decisions

- Preserve all nine source annotation identities/evidence/reference fields.
- Refine correct broad DNA binding, TF activity and transcription-regulation terms
  to the already-present supported specific terms; broadness is not over-annotation.
- Accept KDPG/carbohydrate-derivative binding as integral effector sensing, without
  asserting a precise experimental SIS pocket or inventing a narrower GO term.
- Remove the electronic carbohydrate-derivative metabolic-process participation
  claim. HexR performs regulation, not the underlying catabolic reactions.
- Add GO:0010906 regulation of glucose metabolic process from the gene-specific
  mutant/promoter experiments and direct binding mechanism. The justification is
  HexR's regulatory activity, not a claim that curators overlooked a term because
  the pathway enzymes carry it. No flux magnitude or catalytic activity is inferred.
- Retain one integrated core repressor function; cis-regulatory DNA binding is the
  mechanism of that function, not a second independent core activity.

QuickGO live checks verified GO:0000976, GO:0001217, GO:0097367 and GO:0010906,
including labels/definitions and non-obsolete status. No fitting narrower
phosphosugar-binding GO term was established. The GO-CAM index had no Q88P32 match.
`just paint-losses PSEPK hexR` reported Q88P32 absent from the available PTHR30514
tree, so lineage losses could not actually be checked; this gene has no IBA rows.
The tool's trailing no-loss message must not be read as a completed lineage audit.

## Required source jobs

`just deep-research-falcon PSEPK hexR --fallback perplexity-lite` was attempted.
Falcon authentication failed (HTTP 403); the fallback failed for insufficient
Perplexity quota (HTTP 401). No provider output was fabricated. Publication caching
succeeded for the existing two PMIDs and for newly fetched PMID:41260329.
`just mod-description-deep-research PSEPK hexR` skipped PSEPK because no MOD provider
is configured. `just fetch-fitness PSEPK hexR` could reach neither a local FEBA
database nor the remote source, and wrote no fitness artifact. These unavailable
services are not treated as negative biological evidence.

## Comparator and ontology checks for the proposed pathway-regulation term

QuickGO annotation queries for GO:0010906 on the same-system regulatory proteins
PtxS/Q88HH7 and GnuR/Q88HE5 each returned zero hits on 2026-11-08. This provides no
support for a pathway-completeness or presumed-curator-oversight argument; no such
argument is used. The proposed HexR annotation instead rests on its directly
established regulatory step and the verified term definition (modulation of glucose
metabolism), and is explicitly a regulatory process rather than metabolic execution.
The is_a/part_of ancestor checks show that GO:0010906 and GO:0045892 are not ancestors
or descendants of each other. The established GOA molecular-function and
transcription-regulation terms do not encode this pathway specificity.

Validation: `just validate PSEPK hexR` passed. Its sole warning is that no annotation
cites this manual research record; the annotations intentionally cite the primary
papers or the curated UniProt record rather than treating these notes as independent
evidence. History validation and whitespace checks also passed.

## Cross-batch specificity refinement — 2026-11-08

A final specificity check identified that the experimentally mapped footprints
and shared operator-recognition sequence justify GO:0000987 cis-regulatory
region sequence-specific DNA binding. The two seeded binding rows are now both
refined to that term, without editing their source IDs. QuickGO verified the
replacement label, definition and non-obsolete status. This is a refinement of
an established binding claim, not a new target assertion.
