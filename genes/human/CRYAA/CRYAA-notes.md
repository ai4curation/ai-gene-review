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

**Added.** Three `suggested_experiments` from the run's discriminating tests, the most useful being a reconstituted refolding assay read out as *enzymatic activity* (not CD) with and without an Hsp70/Hsp40/ATP system — that is the experiment that would settle the IBA-versus-NOT standoff in GOA.

## 2026-07-25 (later) - review follow-up: GO:0140309 relabel is NOT a redefinition

PR review caught a real error in my first pass. I saw that GO:0140309 had been relabelled from "unfolded protein carrier activity" to **"unfolded protein holdase activity"**, updated the six `label:` fields, and argued the new label made the term a *better* fit for CRYAA. That inverted this repo's own adjudication.

**A relabel is not a redefinition.** Verified live on QuickGO (2026-07-25) that the definition is *unchanged* and still carrier-specific:

> "A protein carrier activity that binds to a protein in an unfolded state and **escorts it to an acceptor molecule or to a specific location**. The unfolded protein carrier prevents aggregation of the target protein **while its being delivers to its final destination**."

It is still a child of GO:0140597 "protein carrier chaperone", and GO:0044183's own comment now contrasts it as the term that "keeps it unfolded **to deliver it to its final destination**". CRYAA is an **in-situ** holdase — it does not escort clients between compartments — so it does not satisfy this definition. `projects/UNFOLDED_PROTEIN_BINDING.md:285` already recorded exactly this: `CRYAA ... retain GO:0051082; in-situ holdase, not carrier`. Sibling reviews DROME/Hsp23, DROME/Hsp27 and yeast/HSP26 all encode the same objection.

All six sites now use `id: NTR` / `holdase chaperone activity (NTR needed; GO:0140309 does not fit -- carrier-specific)`, matching the yeast/HSP26 pattern, and `core_functions.molecular_function` is back to GO:0051082 as an interim, matching all three siblings.

**One detail of the project page has drifted:** it says `holdase` is a **BROAD** synonym on GO:0140309. QuickGO now reports all three synonyms (`holdase`, `unfolded protein carrier activity`, `holdase-carrier chaperone`) as **exact**, and `holdase` was promoted to the primary label. That weakens one of the page's supporting arguments but not its conclusion, which rests on the definition and the parentage — both unchanged.

### The bigger finding: the obsoletion went through and the NTR was never created

The project page (`:134`) says *"Until this NTR is created, GO:0051082 obsoletion should be blocked"* for the 8 holdase genes. Checked today:

- **GO:0051082 IS obsolete** — `isObsolete: true`, name `obsolete unfolded protein binding`. The block was not honoured.
- **No general holdase term exists.** Searching GO for "holdase chaperone activity" returns only GO:0140309 and GO:0044183. The NTR was never created.
- GO:0051082's obsoletion comment offers only those same two terms as replacements — neither fits an in-situ holdase.

So CRYAA, CRYAB, HSPB6, CLU, SCG5, DNAJB6, DNAJB8 and HSPH1 are now **stranded on a formally obsolete term with no correct replacement**. Updated `projects/UNFOLDED_PROTEIN_BINDING.md` to record this; it needs escalating upstream rather than resolving per-gene.

### IBA provenance corrected

I had repeated the OpenScientist report's framing that PMID:8093612 / PMID:1438232 are "the primary evidence underpinning the positive IBA". They are not. The WITH/FROM column on the IBA row is six FlyBase sHSPs + the PANTHER node, resolved via mygene.info: FBgn0001224 **Hsp23**, FBgn0001225 **Hsp26**, FBgn0001226 **Hsp27**, FBgn0011296 **l(2)efl**, FBgn0031037 **CG14207**, FBgn0035817 **CG7409**.

Notably the three seeds we review locally (DROME/Hsp23, Hsp26, Hsp27) each **retain** GO:0042026 on IDA-level cellular refolding evidence (PMID:26705243, PMID:16572729). So the source genuinely supports the term — this is a **transfer failure**, not a bad source, which is a cleaner argument for REMOVE than the one I originally wrote. All six seeds are now itemized in `propagation_review.source_entities`. Jakob/Horwitz are reclassified as family-level literature context, and both are marked `full_text_unavailable` since only abstracts are cached.
