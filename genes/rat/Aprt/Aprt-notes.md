# Aprt (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 4 new rows, no retired rows.

- GO:0003999 adenine phosphoribosyltransferase activity, ISO from human APRT (UniProtKB:P07741): donor-split of the mouse-donor ISO row; ACCEPT.
- GO:0005829 cytosol, ISO from human APRT (P07741): donor-split; KEEP_AS_NON_CORE as for the mouse-donor sibling.
- GO:0044209 AMP salvage, ISO from mouse Aprt (MGI:88061) with qualifier involved_in (the older sibling row carries acts_upstream_of_or_within): ACCEPT; APRT catalyses the single step of AMP salvage from adenine.
- GO:0007625 grooming behavior, NOT|acts_upstream_of_or_within, ISO from mouse Aprt: genuinely new negated row. Mouse Aprt carries both a positive IGI (with Hprt, PMID:8485579) and a NOT IGI (with Hprt, PMID:8894695) for this term. KEEP_AS_NON_CORE: the negative statement is consistent with APRT being a purine-salvage enzyme with no direct behavioral role. The validator warns about "inconsistent actions" against the positive row (MARK_AS_OVER_ANNOTATED); the warning does not take negation into account and is left as is.

Action changes: none. Existing REMOVE actions on GMP salvage and IMP salvage (ISO from mouse) were re-audited and kept, with propagation comments now naming the actual mouse source evidence:
- GMP salvage: mouse MGI IDA from PMID:718989 (abstract-only), a neuroblastoma purine-metabolism study whose abstract states [PMID:718989 "adenine or guanine were principally sources for adenine (greater than 85%) or guanine (greater than 90%)"]. The mouse IDA itself is not adjudicated; the rat ISO is removed on enzymological grounds (APRT forms AMP).
- IMP salvage: mouse MGI IMP from PMID:9776749 (fetched; abstract-only), an Aprt-knockout loss-of-heterozygosity paper whose abstract does not describe IMP measurements.

Quote hygiene: all 23 UniProtKB quotes were stale (old "FUNCTION: ... energetically less costly" paraphrase; current UniProt text reads "energically"). Replaced with verbatim current FUNCTION, CATALYTIC ACTIVITY, PATHWAY or SUBCELLULAR LOCATION text according to the row.

Description rewritten to remove curation commentary.

Open questions: GO:0006168 "adenine salvage" is defined as a process that *generates* adenine, whereas APRT consumes adenine; nevertheless PAINT (IBA) and InterPro2GO assign it to APRT across species. It is left as accepted (convention), but the definition/usage mismatch could be raised with GO.
