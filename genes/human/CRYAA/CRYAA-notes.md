# CRYAA Gene Review Notes

## 2026-05-30 - PROTEOSTASIS PN small-HSP positive-control pass

Full review is present and marked complete. The local review supports CRYAA/HSPB4 as a small heat-shock-protein holdase and lens structural protein. It explicitly treats the chaperone activity as ATP-independent aggregation suppression rather than active refolding: the existing `GO:0051082 unfolded protein binding` annotation is marked `MODIFY` to `GO:0140309 unfolded protein carrier activity`, and `GO:0042026 protein refolding` is rejected. [file:human/CRYAA/CRYAA-ai-review.yaml; PMID:8943244; PMID:18407550]

PN curation conclusion: the PN placement under `Cytonuclear proteostasis > Chaperone > small HSP system > small HSP` is a good positive control. Propagation to a broad chaperone term such as `GO:0044183 protein folding chaperone` is biologically reasonable as a bridge from PN small-HSP membership, but curator-facing displays should keep the local holdase distinction visible so this is not interpreted as evidence for foldase/refolding activity.

## 2026-07-25 - OpenScientist function-hypothesis run on GO:0042026

Ran a blinded OpenScientist `function_hypothesis` job on the seed "CRYAA has protein refolding (GO:0042026)" (IBA, GO_REF:0000033). Report at `file:human/CRYAA/CRYAA-hypotheses/function-hypothesis-go-0042026/openscientist.md`.

**Verdict of the run:** "partially supported / weakly supported" — retain the IBA as non-core, and ADD GO:0051082 as the "missing" MF term.

**What was adopted.** The run's *mechanism* is sound and agrees with the existing review, so it was wired in as corroboration for keeping `action: REMOVE`:

- P02489 has "no nucleotide-binding site and no ATPase domain" — a single alpha-crystallin domain protein cannot be an autonomous foldase.
- The productive refolding step belongs to downstream ATP-dependent Hsp70/Hsp100 [PMID:34055885 "Formation of these assemblies facilitates subsequent Hsp70 and Hsp100 chaperone-dependent disaggregation and substrate refolding into native species"; PMID:35281256 "HSPBs act as ATP-independent holdases, avoiding misfolded substrates aggregation"].
- Usefully, the run identified the primary evidence *behind* the positive IBA, and it is paralog-derived: PMID:8093612 (Jakob 1993) assayed "murine Hsp25, human Hsp27, and bovine alpha-B-crystallin" — **alphaA was not tested**; PMID:1438232 (Horwitz 1992) used unfractionated alpha-crystallin (alphaA+alphaB) with a CD readout. Both are now recorded in the review as explicit counter-evidence to the REMOVE, with the reason they do not establish autonomous alphaA foldase activity.

**What was rejected, and why.** The run's two headline claims about the annotation set are factually wrong, checked against `CRYAA-goa.tsv` and OLS:

1. It read the GO:0042026 ISS (GO_REF:0000024) as *positive supporting evidence*. It is actually `NOT|involved_in`, transferred from bovine UniProtKB:P02470. That negated assertion is the single most decisive datum for this hypothesis and the run missed it entirely.
2. Its "highest-value curation action" — add the missing GO:0051082 — is a no-op. GOA already carries **three** GO:0051082 annotations for P02489 (IBA GO_REF:0000033; IPI PMID:8943244 with UniProtKB:P07320; IMP PMID:18407550). It is also stale advice: GO:0051082 is now a **formally obsolete** term ("obsolete unfolded protein binding"), and the GO obsoletion note directs replacement to GO:0044183 or GO:0140309 — which is exactly the MODIFY the review already had.

So the run did not overturn the prior review; it confirmed it, while the review's pre-existing MODIFY to GO:0140309 is now independently vindicated by the formal obsoletion. The report is recorded with `correctness: LOW_QUALITY` and the specific errors documented in its `review_notes`.

**Incidental fix.** OLS shows GO:0140309 has been **relabelled** from "unfolded protein carrier activity" to **"unfolded protein holdase activity"** (the old string is retained as a synonym, which is why local term validation still passed). All six `label:` fields and the prose mentions in the review were updated. The new label is a better fit anyway — "holdase" is precisely the distinction this whole review turns on.

**Added.** Three `suggested_experiments` from the run's discriminating tests, the most useful being a reconstituted refolding assay read out as *enzymatic activity* (not CD) with and without an Hsp70/Hsp40/ATP system — that is the experiment that would settle the IBA-versus-NOT standoff in GOA.
