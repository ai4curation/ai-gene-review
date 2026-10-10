# Ces2c review notes

## Evidence summary
- [PMID:12230550] The publication supports Ces2c retinyl ester hydrolase/retinol metabolism annotations.
- [UniProtKB:O70631] UniProt summarizes Ces2c as a hydrolase with high activity toward palmitoylcarnitine and possible retinyl ester hydrolysis.

## Curation decisions
- Core function: acylcarnitine/retinyl ester hydrolase (acylcarnitine hydrolase activity, GO:0047619).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-04

- GOA refresh (commit a3cf70b6d): no new rows and no retired rows; WITH/FROM and qualifiers
  backfilled on the 13 existing rows. 0 PENDING.
- Description rewritten as standalone biology (the previous text described what "the review
  keeps"). New text uses UniProt O70631: acylcarnitine hydrolase (EC 3.1.1.28), retinyl
  hexadecanoate -> all-trans-retinol (RHEA:13933), "Microsome {ECO:0000269|PubMed:12230550}",
  expressed in liver, stomach and kidney, signal peptide 1..26.
- GO:0043231 intracellular membrane-bounded organelle (IDA, PMID:12230550):
  MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0005783 endoplasmic reticulum. The problem is
  generality, not an overreaching claim; the experiment purified the enzyme "from rat liver
  microsomal extracts" [PMID:12230550], and microsomes are ER-derived (GO has no current
  microsome CC term).
- GO:0050253 retinyl-palmitate esterase activity (IDA, PMID:12230550) kept ACCEPT with added
  provenance. The cached abstract (abstract-only) lists AB010635 (the Ces2c EMBL entry) among
  the purified isoenzymes but explicitly names only "D50580 and AY034877 also hydrolyzed retinyl
  palmitate"; the full text is not cached, so the curator/UniProt reading is deferred to.
- Open question: confirm from the full text of PMID:12230550 the retinyl palmitate hydrolase
  rate measured for the AB010635 (Ces2c) protein.

**Stale UniProt quotes (2026-10-10):** replaced 6 `UniProtKB:O70631` supporting_text quotes (legacy `DR GO;` lines with evidence codes no longer present in the refreshed flat file) with verbatim SUBCELLULAR LOCATION, CATALYTIC ACTIVITY (acylcarnitine hydrolysis) and FUNCTION text from the current `Ces2c-uniprot.txt`.
