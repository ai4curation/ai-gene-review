# daf-28 notes

Deep research: falcon failed and the perplexity-lite fallback was unavailable (2026-10-08). No deep-research file was created. Q9NEK7 is an unreviewed TrEMBL entry, and it is the accession the module uses.

## Key findings
- daf-28 encodes an insulin-like protein expressed in ASI and ASJ. Its expression is down-regulated under dauer-inducing conditions [PMID:12654727]. sa191 is a dominant-negative processing-site allele [PMID:12654727 "This DAF-28 mutant is likely to be poisonous to wild-type DAF-28 and other insulins."].
- daf-28 plays the primary role in inhibiting dauer entry [PMID:21343369 "daf-28 plays a more primary role in inhibiting dauer entry"]. Neuronal ILPs inhibit intestinal DAF-16 [PMID:24671950].
- DAF-28 co-localizes with SNB-1 at ASJ synaptic regions [PMID:25048458].

## Decisions
- The 8 dauer larval development rows were changed (MODIFY) to negative regulation of dauer entry (GO:1905910).
- protein import into nucleus (IMP, acts upstream): MARK_AS_OVER_ANNOTATED, because it is indirect and already captured by GO:1900181.
