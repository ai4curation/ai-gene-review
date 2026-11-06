# Bacterial cysteine synthesis via O-acetylserine

This audit retains the two-reaction pathway: CysE makes O-acetylserine (OAS) from
serine and acetyl-CoA, and an OAS sulfhydrylase incorporates free sulfide to make
cysteine. The abstract module has an explicit bacterial taxon context; it does not
assert that every bacterium or every member of either protein family has this route.

Eighteen curated references supply 30 findings and evidence on each reaction and
the OAS connection. Comparative reviews (PMID:36148777, PMID:38257399 and
PMID:38931847) are reconciled with primary studies rather than used to erase
substrate and lineage differences. The source-analysis directory records the
comparative findings, exact family placements and member evidence. Sources available
only as abstracts are identified in the reference reviews and gene notes; full-text
claims use independently inspected primary evidence. No acquired full articles or
PDFs are included in this change.

## Species and biochemical boundaries

Sixteen completed gene reviews cover six species: E. coli K-12, P. putida KT2440,
P. aeruginosa PAO1, B. subtilis, C. jejuni NCTC 11168 and M. tuberculosis H37Rv.
Fifteen proteins represent the core pathway. M. tuberculosis CysM is the sixteenth
review, an OPS/CysO-route comparator rather than an OAS-route representative.
KT2440 assignments remain conserved-role inferences: the S-313 sulfur study is not
a direct KT2440 assay.

CysE is grounded in PTHR42811/PTN000602332. PTHR10314 supplies CysK and CysM
alternatives, but family membership or the CysM gene name alone does not establish
substrates. The experimentally OAS-active C. jejuni protein has a separate terminal
alternative with its verified family and no guessed PAINT node. M. tuberculosis CysM
is inside the CysM PAINT node but specializes in OPS and thiocarboxylated CysO; the
review preserves this counterexample to blanket OAS-function propagation. The broad
family-level GO:0004124 assessment is consequently UNRESOLVED. PAINT assertions,
node identifiers, seeds and source snapshots are retained.

Thiosulfate chemistry first makes S-sulfocysteine and requires reduction; it is not
silently modeled as direct cysteine production. The OPS/CysO/Mec+ system likewise
lies outside the two-step boundary. A slow OAS aminoacrylate intermediate does not
prove complete turnover to free cysteine. The published Mtb CysM product assay found
no OAS/sulfide product under its conditions; its calibration range is not a limit of
detection or proof of chemical impossibility.

Regulatory complexes are context, not required pathway components. E. coli supports
the canonical CysE–CysK complex; PAO1 interaction assays have specified negative
results. B. subtilis supports CymR–CysK regulation and negative tested CysE–CysK
association. The newer Mtb complex report describes reduced CysE activity; its
abstract does not establish unreported assembly details. B. subtilis CysK's CBS
annotation is removed only after full primary biochemical evidence, not from an
abstract naming a paralog. MccA's OAS-dependent chemistry is distinguished from the
serine-dependent reaction in GO:0004122.

## Preservation and checks

The frozen baseline contains 158 historical annotation rows: 155 machine-derived
rows and three inherited NEW assertions. All are retained. One supported E. coli
CysK molecular-function proposal (ribonuclease activator activity) brings the total
to 159. This reflects direct toxin activation, not RNase catalysis or a new process
claim. All 32 raw UniProt/GOA files and three provider artifacts are unchanged.
Falcon access failures are documented; no substitute text is labeled as provider
output.

The production module-logic engine passes 59 capacity and preservation cases. Its
independent oracle requires the reviewed core reaction, curated member role, actual
family membership, representative selection and matching strain. This tests the
curated panel's biochemical capability; it does not discover genes, prove genome
completeness or infer native flux or growth. Positive and negative controls include
the Mtb CysM counterexample even when an annotation is artificially accepted.

All 16 targeted gene reviews and their histories passed. Module schema, semantic
validation, rendering, checker lint and three structure/sequence comparisons pass.
The three module advisories transparently reflect unresolved broad PTHR10314
function scope. Final family checks pass with zero conflicts and four unresolved cases, recorded
separately following independent scientific review. Full-corpus validation is terminal: 10,544 reviews, 17 reference errors in 16 unrelated yeast reviews, and zero best-practice errors. All 22 affected inputs are byte-identical to the pinned base; the exact errors, input blobs and log hash are recorded in preexisting-reference-failures.yaml. A dedicated PR, external review/CI and actual merge remain pending. Module status COMPLETE describes the curated artifact, not completion of the project audit.
