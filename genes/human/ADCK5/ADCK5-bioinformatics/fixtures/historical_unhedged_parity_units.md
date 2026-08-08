<!-- REGRESSION FIXTURE - DO NOT EDIT.
     Two units exactly as they stood at branch commit c0a6dacb7, before the parity
     retraction: each contrasts ADCK1/ADCK2 SubCell treatment with ADCK5 without noting
     that the paralogs rest on an assay ADCK5 was never in. Frozen rather than referenced
     by SHA. -->

## reference_review.review_notes on GO_REF:0000044

Correctly applied - SL-0162 does map to GO:0016020, confirmed against the UniProt locations endpoint. The weakness is in the pipeline's input, not its operation: ADCK5's SUBCELLULAR LOCATION line is itself an ECO:0000305 inference from a predicted TM helix, whereas ADCK1 and ADCK2 feed the same pipeline SL-0173 and gain GO:0005739.

## existing_annotations[0].review.summary (excerpt)

Correct but weakly grounded, and less informative than the available evidence. This row is the automatic mapping of UniProt SubCell SL-0162 (Membrane) to GO:0016020, and that SubCell assignment traces to a SUBCELLULAR LOCATION line reading "Membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}" - a curator inference drawn from a purely predicted transmembrane helix at residues 50-67 (ECO:0000255). There is no experimental membrane measurement for ADCK5. The statement is nonetheless very likely true: the characterised UbiB relatives COQ8A and ADCK1 are inner-mitochondrial-membrane anchored, and ADCK5 is independently placed in the mitochondrion by the HTP row below. Kept as ACCEPT because a general parent term that is true should not be removed, and because refining it to GO:0031966 mitochondrial membrane would mean joining an experimental mitochondrion call to a predicted membrane call - a composite inference this review declines to make on ADCK5's behalf. The substantive issue is upstream and not fixable in GO: ADCK1 and ADCK2 receive SL-0173 (Mitochondrion) from the same UniProt pipeline while ADCK5 receives only SL-0162, despite all three carrying the identical MitoCoP HTP evidence. Raised as a UniProt correction request in suggested_questions.
