# TF batch 2: signaling, sigma-factor and RNA regulation

Date: 2026-11-16. Full GO re-review completed for GacA, FleQ, RpoS and Hfq.
The batch separates transcription-factor signaling, sigma-factor promoter recognition
and post-transcriptional RNA control while retaining supported targets and pathway context.

| Gene | GO review | Target evidence | Main outcome |
| --- | --- | --- | --- |
| GacA / Q88FJ6 | [review](../../../genes/PSEPK/gacA/gacA-ai-review.yaml) | [3 relationships](../../../genes/PSEPK/gacA/gacA-regulatory-evidence.yaml) | Primary evidence replaces paraphrased notes; core binding remains core. lapA/lapF and K1-T6SS are explicitly system-level inferences with unresolved physical directness. |
| FleQ / Q88ET0 | [review](../../../genes/PSEPK/fleQ/fleQ-ai-review.yaml) | [5 relationships](../../../genes/PSEPK/fleQ/fleQ-regulatory-evidence.yaml) | Both activation and repression are represented; adds the experimentally supported repressor MF. Records lapA, bcs, lapE, cyaA and the FleQ–FleN K1 structural-promoter relationship. |
| RpoS / Q88ME8 | [review](../../../genes/PSEPK/rpoS/rpoS-ai-review.yaml) | [1 relationship](../../../genes/PSEPK/rpoS/rpoS-regulatory-evidence.yaml) | Refines DNA binding to core-promoter recognition, grounds starvation response in primary evidence, withdraws redundant stress and biofilm-execution proposals. PwspA binding-site mutation supports direct activation. |
| Hfq / Q88DD3 | [review](../../../genes/PSEPK/hfq/hfq-ai-review.yaml) | [1 relationship](../../../genes/PSEPK/hfq/hfq-regulatory-evidence.yaml) | Separates RNA recognition, translational repression and CrcZ stabilization. Retains explicit ortholog provenance of existing ISS proposals; decoy RNAs are not described as mRNA-pairing guides. |

These ten relationships are a supported subset, not complete regulons. Six have
binding plus functional regulation evidence; three GacA relationships and Hfq/CrcZ
retain unresolved physical directness. Two Gac-system adhesin relationships also
retain unknown sign rather than assigning a sign from an abstract or iModulon.

## Interpretation and source limits

GacA's KT2440 biofilm mutant evidence is conditioned on multicopy rup4959 in the
cfcT-5 screen (PMID:27489550). The K1 promoter study (PMID:36748579) tests gacS,
not gacA; the sidecar makes that inference explicit. No direct KT2440 RsmX/Y/Z
promoter contacts are manufactured from the conserved Gac/Rsm model.

FleQ target signs are promoter- and condition-dependent. The primary K1 study
(PMID:35178858) reports increased FleQ–FleN binding at high c-di-GMP; a conflicting
low-c-di-GMP summary in PMID:36748579 is recorded in notes. Existing downloaded
texts are unchanged. Structural details established mainly in P. aeruginosa are
not presented as KT2440 measurements. Flagellar work in KT2442 retains that
strain provenance.

RpoS recognizes the major wsp promoter. The −10 motif mutation affects both
binding and reporter activity (PMID:39589111). The edge does not establish seven
separate DNA contacts or reconstituted holoenzyme transcription. Downstream WspR
and biofilm machinery execute c-di-GMP synthesis and biofilm production; those
processes are preserved as regulated context rather than RpoS execution claims.

Hfq-dependent CrcZ stabilization is measured by a rifampicin-chase Northern assay
(PMID:27777366). It is not activation of the crcZ promoter, and the protection
complex remains proposed in that experiment. The primary transcript contains
62 extra nucleotides; processed CrcZ is undetectable in the hfq deletion, so its
half-life is not inferred. No CrcY stabilization edge is extrapolated.

The [LinkML sidecar schema](../tf_census/regulatory-evidence.schema.yaml) adds an
explicit regulatory level and RNA target types. Older records retain their
transcription interpretation. Semantic validation rejects promoter stabilization,
translation of ncRNA and RNA targets lacking an explicit level. Reusable LinkML
classes still permit standalone snippet validation.

## Validation and provenance

- All four `just validate PSEPK GENE` runs passed, including companion records.
  GacA and RpoS retain an advisory to cite research summaries; their annotations
  deliberately cite the inspected primary evidence directly.
- All 129 quotations in the four reviews and four sidecars were verified against
  readable sources, with zero blocking failures, baseline exemptions or unchecked sources.
- The 68-test census/importer/sidecar suite and repository Ruff check passed.
  Six new history records validated. The whole-repository quote gate reported
  20,328 verified quotations, zero blocking failures, 222 existing baselined
  failures and 324 unchecked sources elsewhere; 23 stale local-quote baseline
  entries for these re-reviews were pruned.
- Existing Falcon/provider artifacts, UniProt/GOA records and publication caches
  were preserved. All needed primary caches already existed; normal PMID fetching
  reused them. No research was regenerated.
- FEBA retrieval failed for all four genes because neither the local database nor
  a remote source was reachable. No fitness evidence was invented. PSEPK has no
  applicable MOD-description provider.
- Two annotation-reviewer consultations supplied independent, read-only biological
  assessments. One writer made the changes in an Orca-managed checkout using the
  retained runtime; the lockfile and runtime were not synchronized.
- Gene, project and schema history records accompany the batch. The manifest
  records changed artifacts and preserved provider/source hashes.

## Queue

- [x] GacA
- [x] FleQ
- [x] RpoS
- [x] Hfq
- [ ] Next: Ada, LexA2, TurB/MvaT and RsmE/csrA, preserving the DNA-repair,
  nucleoid-associated and RNA-regulatory distinctions identified by calibration.
- [ ] Then the remaining eight calibration cases, including sigma/anti-sigma,
  chemotaxis and identity-negative controls, followed by system/family batches.

Eight of the twenty calibration cases now have full re-reviews in this TF campaign;
twelve retain their original scoped-assessment status. Existing files elsewhere
are not counted as newly validated campaign work.
