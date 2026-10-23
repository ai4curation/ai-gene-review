# Klk9 review notes

## Evidence summary
- [PMID:1900513] The fetched GOA file uses this publication for positive regulation of vasoconstriction.
- [UniProtKB:P07647] UniProt describes Klk9 as a glandular kallikrein that cleaves kininogen to release Lys-bradykinin and has vasoconstrictor activity.

## Curation decisions
- Core function: submandibular glandular kallikrein-9 (serine-type endopeptidase activity, GO:0004252).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-04

**GOA changes.** One new row: GO:0005576 extracellular region (IBA, GO_REF:0000033, is_active_in; kallikrein PAINT node PTN008611740). No retired rows; the other 7 rows are unchanged.

**PENDING resolved.** GO:0005576 extracellular region -> ACCEPT. KLK9/SEV has a signal peptide (FT SIGNAL 1..18) and propeptide, was purified from submandibular gland, and acts on extracellular targets [PMID:1900513 "At pH 6.5, it released angiotensin II when incubated with sheep angiotensinogen"; "It directly contracts vascular smooth muscle, acting via a mechanism that requires intact enzymatic activity."].

**Row audit.** No other action changed. The zymogen activation IBA stays KEEP_AS_NON_CORE; its reason now says that no zymogen substrate of rat KLK9 is known and that KLK9's own zymogen processing is not what the term asserts, but there is no target-specific divergence evidence to challenge the PAINT node.

**Stale quotes fixed.** The refreshed UniProt record has no `DR GO` lines, so six quotes like "GO; GO:0004252; F:serine-type endopeptidase activity; IBA:GO_Central." were replaced with UniProt SIMILARITY text and verbatim abstract quotes from PMID:1900513 (abstract-only cache): serine-protease inhibitor sensitivity for the endopeptidase rows; direct smooth-muscle contraction for the vasoconstriction IDA and blood-pressure IBA rows; submandibular-gland purification for secretory granule.

**Description.** Rewritten as standalone biology (removed "The review accepts..."), now including the angiotensin II-releasing and thrombin-like substrate data from PMID:1900513. `status` set to COMPLETE.

**Open question.** SEV's vasoconstriction was insensitive to the AT1 antagonist DUP753 despite angiotensin II release in vitro, so the physiologically relevant substrate on vascular smooth muscle is unknown (protease-activated receptor?).
