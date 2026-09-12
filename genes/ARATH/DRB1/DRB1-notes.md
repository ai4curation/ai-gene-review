# DRB1/HYL1 re-review

## 2026-09-12 annotation and evidence audit

Reviewed all 37 original annotation rows and all 26 original reference entries, including the negated Cajal-body annotation. Preserved every source field and both alternative-product records. Added one NEW transcription-regulation annotation from a subsequently checked primary paper. Generated research paraphrases were removed from `supporting_text`; supporting passages were selected from the actual cached publications. Electronic annotations retain mapping-specific rationale and independent corroboration without a universal snippet requirement.

### RNA binding, enzyme activation and catalytic over-transfer

DRB1/HYL1 binds structured RNA and helps DCL1 process it. The existing miRNA-binding annotation cites association with primary transcripts: [PMID:17369351 "The HYL1 protein coimmunoprecipitates with miR171a and miR159a precursors"]. QuickGO defines GO:0035198 as binding the mature 21–23-nucleotide miRNA. The replacement is now GO:0070878, primary miRNA binding, rather than the less informative generic dsRNA-binding replacement. No argument about an AGO-like function is needed.

OLS and QuickGO were used to check GO:0070878, GO:0070883, GO:0170054 and GO:0004525. The specific ribonuclease activator term GO:0170054 means binding to and increasing activity of a ribonuclease. Primary genetic/interaction evidence (PMID:16428603) and purified-protein assays (PMID:18632569) support this function: [PMID:18632569 "Both HYL1 and SE stimulate DCL1 activity on both pri- and pre-miRNA substrates and markedly increase the fidelity of cleavage."]. This replaces the generic DCL1 interaction annotation and distinguishes the activator from the catalytic RNase.

The RNase III IBA removal is retained. The cached PAINT table `interpro/panther/PTHR11207/PTHR11207-paint.tsv` explicitly records GO:0004525 IBD at PTN000129453. UniProt annotates the two DRBM domains at residues 15–84 and 101–170, without an RNase III domain; biochemical studies assign RNA cleavage to DCL1. This is a target-domain-architecture objection, not an objection to donor count. Removed unverified claims about the plant clade's precise pruning and evolutionary history; source tracing is limited to what the local PAINT data establish. No pseudoenzyme ancestry is asserted.

### Interaction review under the revised rule

Generic protein binding no longer uses MARK_AS_OVER_ANNOTATED. PMID:15821876 and PMID:20462493 directly establish dsRNA-binding function and are MODIFY; PMID:16428603 supports ribonuclease activator activity and is MODIFY. CPL1 regulation (PMID:23141542), PP4-SMEK1 regulation (PMID:28586645), HOS5/RS40/RS41 association (PMID:26227967), and SERRATE association (PMID:16889646) are REMOVE as uninformative generic annotations. The reported interactions remain valid evidence; these removals do not assert that the interactions are false, or that HYL1 is a phosphatase.

PMID:21798944, PMID:32612234 and PMID:29769717 are UNDECIDED: an assay-level HYL1 interaction could not be recovered from the accessed paper/supplementary context. The CHR2 paper's abstract concerns direct CHR2–SE interaction and subsequent DCL1/HYL1 processing; this neither verifies nor refutes a separate HYL1 interaction experiment. Publisher/browser lookup and publication refresh were attempted. The interactome abstracts alone do not identify the relevant HYL1 partner.

HYL1 self-association is retained as non-core mechanistic context. The structural study reports [PMID:20462493 "The dimerization of HYL1 was further confirmed by in vitro pull-down, coimmunoprecipitation, and analytical gel filtration assays."]. The same study separates the canonical dsRBD1 RNA-binding surface from the noncanonical dsRBD2 dimerization-associated surface.

### Localization and developmental outputs

Dicing bodies are distinguished from Cajal bodies using Atcoilin exclusion (PMID:17369351); the original NOT flag remains intact. Nuclear speckle annotation has its own HOS5/RS-protein interaction evidence in PMID:26227967 and is not treated as synonymous with dicing bodies. Live imaging supports both dicing bodies and diffuse nucleoplasmic distribution (PMID:17442570).

Hormone and leaf-patterning annotations retain experimentally supported non-core outcomes. PMID:11148283 explicitly reports reduced auxin/cytokinin sensitivity and ABA hypersensitivity; PMID:22623415 reports leaf shape and venation phenotypes. The target-destabilization row is independently corroborated by [PMID:14972688 "reduced miRNA accumulation in hyl1 correlates with an increased accumulation of uncleaved target mRNAs"]. This supports the downstream process without assigning target-cleavage catalysis to HYL1.

The female germline IGI annotation was checked in the [publisher full text of PMID:37606225](https://nph.onlinelibrary.wiley.com/doi/full/10.1111/nph.19217), Results and Fig. 8. The double-mutant ovule experiments support restriction of megaspore mother-cell identity; this is not merely an upstream transcriptional correlation. The cached publication remains abstract-only, so this notes file preserves the short exact publisher excerpt used by the annotation:

> ER and HYL1 genetically interact at the second checkpoint in MMC development and restrict a single MMC formation in each ovule.

### Newly checked primary research

Europe PMC identifier lookup verified PMID:18632569, PMID:37040378 and PMID:38918606 before adding them to the review. Cached full texts were read. PMID:37040378 separates MIR-transcription effects from precursor-processing defects using reporters/genetics and establishes HYL1 association with Pol II. A NEW GO:0006357 annotation captures the supported process without inventing DNA-binding transcription-factor activity. PMID:38918606 shows substrate-dependent requirements for HYL1/SE rather than a universal requirement at every precursor. Core functions now separate RNA-substrate recognition from DCL1 activation and avoid duplicated dsRNA-function entries.

### Retrieval and validation outcome

The required Falcon refresh completed successfully in 356.6 seconds (2026-09-12T08:49:23–08:55:19 UTC in provider metadata); fallback was not needed. The new report was reviewed as context and agrees with the noncatalytic RNA-binding/processing role. Concurrent publication caching succeeded for all 18 original PMIDs. Pipeline refreshes upgraded PMID:16428603, PMID:17337628, PMID:17442570 and PMID:21798944 to full text. Only caches previously marked `full_text_available: false` were force-refreshed; pre-existing full-text caches were not touched. PMID:18632569, PMID:37040378 and PMID:38918606 were fetched through the normal pipeline with full text. Some old references remain abstract-only, and unresolved interaction evidence is explicitly UNDECIDED.

`just validate ARATH DRB1` passes with one advisory warning that annotation rows do not cite the generated research report. Primary publications support the decisions; no generated snippet was added solely to silence this warning. An explicit source-field comparison confirmed exact preservation of all 37 original rows, including `negated: true`, before addition of the single NEW annotation.


## 2026-09-12 — Completed OpenScientist hypothesis integration

Reviewed `DRB1-hypotheses/function-hypothesis-go-0004525/openscientist.md` (three iterations; 2026-09-12T09:58:40–10:23:28; 1488.34 seconds) using annotation-reviewer and openscientist-hypothesis skills. No new research job or cache refresh was launched; generated report/artifacts remain unchanged. The report agrees with the existing REMOVE decision for GO:0004525 and with retained dsRNA binding/ribonuclease activation. This is corroboration, not a changed biological verdict.

Independently re-read PMID:18632569 full Results. DCL1 cleaves without added HYL1; adding HYL1 increases rate and fidelity [PMID:18632569, “HYL1 increased the accuracy from 11% to 22%, whereas SE increased the accuracy to 41%.”]. This directly supports a stimulatory cofactor. Neither the accessible Results nor the report identifies an explicit HYL1-alone negative nuclease control, so the review does not present such an assay as observed. Domain architecture and positive division of biochemical labor together support rejecting intrinsic RNase III activity.

Local UniProt O04492 and PTHR11207-entries.csv verify HYL1 in SF1 and P0A7Y0/Q9NRR4 in SF0. The actual PAINT table records GO:0004525 IBD at PTN000129453, with IRD exclusions at PTN001025433 and PTN001025446. SF membership alone does not establish the exact topology, ancestral placement rationale, or an unrestricted family-wide transfer. The report's SF0-to-SF1 mechanism and “architecturally impossible” wording are therefore not imported as demonstrated findings. Its own limitation states that domain calls used database records rather than de novo HMMER/InterProScan; no independent computational scan artifacts were supplied. No report claim about unverified paralogs, isoforms or other literature was added, and its suggested BP contributes_to semantics were not imported.

Added report provenance and primary Results support to YAML; retained all 38 annotation identities and actions.
