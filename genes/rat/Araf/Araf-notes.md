# Araf (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d) changes:
- No new rows.
- 3 rows retired: positive regulation of peptidyl-serine phosphorylation (ISO), protein phosphorylation (IDA, PMID:10648842), protein phosphorylation (TAS, PMID:9779826). Reviews kept, each with a retirement note.

Action and evidence changes:
- MAP kinase kinase kinase activity (IDA, PMID:10648842): stays ACCEPT, but the legacy reason calling the paper "evidence-mismatched" was withdrawn. The cached record is abstract-only. It reports that Raf/MEKK immunoprecipitation kinase assays did not explain the EGF-sensitive hepatic MEK kinase activity; it does not report that A-Raf lacks MEK kinase activity [PMID:10648842 "Western immunoblotting confirmed that Raf-1, A-Raf, B-Raf, MEKK1 and MEKK2 were present at similar levels in E19 and adult liver."]. The retired IDA protein phosphorylation row was corrected the same way.
- Regulation of TOR signaling (ISS/ISO) and regulation of proteasomal ubiquitin-dependent protein catabolic process (ISS/ISO): traced to the human ARAF IMP annotation from PMID:22609986 (cached, full text). Within that study the effect is ARAF-specific [PMID:22609986 "Knockdown of ARAF, but not BRAF or CRAF, by siRNAs inhibited Gα12QL-mediated upregulation of RFFL expression and polyubiquitination of PRR5L"]. TOR stays KEEP_AS_NON_CORE. Proteasomal catabolism stays MARK_AS_OVER_ANNOTATED, now with a stated reason (ARAF acts upstream via ERK-driven RFFL expression) and a propagation_review (TERM_SCOPING_PROBLEM / ROLE_CONFLATION).
- Location rows (cytoplasm, cytosol, mitochondrion) now cite deep-research text on cytosolic inactive RAF monomers and on A-Raf at mitochondria with MST2, replacing the generic FUNCTION quote. ATP binding cites the UniProt kinase-family SIMILARITY line. Kinase MF rows gained the UniProt CATALYTIC ACTIVITY quote.
- 23 stale UniProt quotes were paraphrases of the FUNCTION line. They were replaced with verbatim text ("...to the nucleus. May also regulate the TOR signaling cascade (By similarity).").
- Description rewritten without curation commentary.

Open questions:
- Human ARAF negative regulation of apoptotic process (IDA, PMID:19667065, a BAD phosphorylation study) is cached abstract-only. The rat ISO row stays KEEP_AS_NON_CORE on the strength of the MST2 mechanism.
