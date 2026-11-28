---
title: "Where the ARO→GO mapping should live, and how it tracks ARO releases"
---

# Where the ARO→GO mapping should live, and how it tracks ARO releases

A short options note for a call with the CARD team. Part of the
[Antimicrobial Resistance project](../ANTIMICROBIAL_RESISTANCE.md); the mapping itself is
[`aro2go.sssom.yaml`](aro2go.sssom.yaml) and its curator view is [aro2go.html](aro2go.html).

## Where things stand

- The mapping is an SSSOM mapping set: 46 GO rows and 20 recorded GO gaps over CARD 4.0.2. With
  propagation it gives a GO term to 342 of the 595 families in CARD's *AMR Gene Family* category,
  records a GO gap for 23 more, and lists the other 230 with a reason
  ([coverage report](FAMILY_COVERAGE.md)).
- Release sync already works here as a check, not yet as a schedule. `just fetch-aro` downloads a
  CARD release, and `just check-aro-release` fails on label drift, on ids missing from the release,
  and on any AMR gene family that is neither mapped nor triaged. That check is how the two
  relabellings the CARD team pointed out (ARO:3000560, ARO:3000202) would have been caught. It also
  found that 18 ids listed as AMR gene families in `aro_categories.tsv` are absent from the
  `aro.obo` of the same release.
- Applying the mapping to UniProt's 4,182 CARD-cross-referenced entries gives 1,784 candidate GO
  annotations ([annotation-gain report](ANNOTATION_GAIN.md)). Nothing has been sent to GO.

## Question 1: where the curated mapping lives

| Option | For | Against |
|---|---|---|
| **A. In the ARO repository** (an SSSOM file released with ARO) | The subject side changes only when ARO changes, so the people who rename, split and obsolete ARO terms keep the mapping in step in the same release. CARD's curators know the family membership questions (FosA vs FosB, ddl variants under Van ligase) better than anyone. The mapping is versioned and cited with the ARO release. | CARD takes on watching GO for obsoletions and merges, and reviewing GO-side changes it did not ask for. |
| **B. In GO, next to the other external2go mappings** (ec2go, interpro2go, rhea2go, …) | GO already distributes these files and the annotation pipelines know how to read them. GO editors maintain the object side and would make the new terms. | GO editors would have to track ARO releases and family membership, which they do not curate. The external2go format carries no confidence, justification or no-match rows, which this mapping depends on. |
| **C. Stay in ai-gene-review** | Fastest to change; the checks, coverage report and gain report already run here. | Neither community owns it, nothing downstream reads it, and its future depends on this project. |

## Question 2: keeping it in step with ARO (and GO) releases

Whichever repository hosts the file, the same three checks should run there on every ARO release
and on a schedule against GO:

1. **ARO drift**: every subject id is live in the new release and its label matches. This is
   `aro_release.py check` today, comparing against a pinned release (`aro_release.yaml`).
2. **Coverage**: every AMR gene family is mapped, covered by a mapped ancestor, recorded as a GO gap,
   or listed with a reason. New families then show up as a failing check, not as silent gaps.
3. **GO drift**: every object id is live and its label matches, and gap rows are re-tested when GO
   adds terms. This is how the D-Ala-D-Lac gap closed in this round (GO:0160220 now exists).

Each release of the mapping records the ARO release it was checked against
(`subject_source_version`) and the GO release (`object_source_version`).

## Question 3: how propagated annotations would reach GO

| Route | What it involves |
|---|---|
| **I. An IEA pipeline at UniProt-GOA with its own GO_REF**, like InterPro2GO or Rhea2GO | UniProt already cross-references CARD on these entries, so the join is deterministic. GOA would need to agree to run it and to which predicates and confidence levels to use (for example, `enables` rows at ≥0.85 only). |
| **II. Through PAN-GO / PAINT** | The mapping could inform which PANTHER nodes carry AMR activities, but PAINT works from experimental annotations of family members, not from external mappings, so this is evidence for curators, not a pipeline. |
| **III. CARD submits annotations itself** (a GAF from CARD as a contributing group) | Most control for CARD, but makes CARD a GO annotation provider, with GAF production and evidence-code obligations. |

## Recommendation

**Option A with route I.** Keep the canonical SSSOM file in the ARO repository, released with each
ARO release, with the three checks above running in that repository's CI. Ask GO to take the
released file as an external mapping and ask UniProt-GOA to apply it through an IEA pipeline with
its own GO_REF, starting with the `enables` rows at confidence ≥0.85 and leaving `related match`
rows as curator leads. The ARO side changes most often, and route I reuses the machinery GO already
runs for InterPro2GO and Rhea2GO. Until CARD is ready to take the file, ai-gene-review keeps
maintaining it with the same checks, and the handover is moving the file and its check script.

## For the call

- Would CARD host the file in the ARO repository, and who would review GO-side changes?
- Should the mapping cover individual determinants (for example Tet(A)-type MFS pumps to
  `GO:0015520`) or stay at family level?
- The 18 AMR gene family ids absent from `aro.obo`, and CrcB under the MATE family node (ARO
  describes it as a Camphor Resistance Protein family member): are these known?
- ARO:3001298 'TlrA-like 23S rRNA methyltransferase' sits under the G748 N1-methyltransferase node,
  but the published tlrA of *S. fradiae* is ermSF (A2058), and its member EmtA methylates G2470
  (PMID:11580839). Should the node be renamed, and EmtA moved?
- Would CARD co-sign the GO term requests in [GO_TERM_REQUESTS.md](GO_TERM_REQUESTS.md)?
