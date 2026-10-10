# Sdsl review notes

## Evidence summary
- [PMID:33079132] The abstract states that rat SDHL was expressed recombinantly and characterized as a multifunctional enzyme with glutamate racemase plus L-serine/L-threonine dehydratase activities.
- [UniProtKB:A0A6N3IN21] UniProt records Rhea reactions for L-serine deamination, L-threonine deamination, and L-glutamate/D-glutamate racemization with PubMed:33079132 evidence.

## Curation decisions
- Core function: serine dehydratase-like / glutamate racemase (L-serine ammonia-lyase activity, GO:0003941).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-04

**GOA changes.** None in substance: the refreshed GOA has the same 11 rows (IEA/ISO/IDA for L-serine ammonia-lyase and threonine deaminase activity; IEA and IDA glutamate racemase activity; IDA pyridoxal phosphate binding; ISO identical protein binding; ND biological_process). No PENDING, no retired rows.

**Stale quotes fixed.** The refreshed UniProt flat file no longer contains `DR GO` lines, so seven `supporting_text` quotes of the form "GO; GO:0003941; F:...; IDA:UniProtKB." were no longer in the source. They now quote the CATALYTIC ACTIVITY / COFACTOR lines (e.g. "Reaction=L-serine = pyruvate + NH4(+)", "Reaction=L-glutamate = D-glutamate", "Name=pyridoxal 5'-phosphate"). The three IDA activity rows also cite the abstract directly [PMID:33079132 "rat SDHL is a multifunctional enzyme with glutamate racemase activity in addition to l-serine/l-threonine dehydratase activity"] (abstract-only cache).

**Action changed.**
- GO:0042802 identical protein binding (ISO from human Q96GA7): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. The human donor rows are two-hybrid interactome self-interactions (QuickGO: IPI PMID:16189514, 25416956, 31515488, 32296183), and the rat-specific evidence says the recombinant rat enzyme is monomeric [UniProtKB:A0A6N3IN21 "SUBUNIT: Monomer (PubMed:33079132). Homodimer (By similarity)."]. Added a `propagation_review` (PROPAGATION_BAD; source Q96GA7 SUPPORTS_SOURCE_BUT_NOT_TARGET). This does not claim rat SDSL cannot dimerize.

**Unchanged.** The two ISO activity rows stay ACCEPT; their reason now names the donor (human SDSL Q96GA7, which carries IDA/EXP evidence for both dehydratase activities, PMID:16580895 and PMID:18342636). PLP binding stays KEEP_AS_NON_CORE; the ND root stays REMOVE.

**Description.** Rewritten as standalone biology (removed "The review keeps...", Falcon-run commentary).

**Open questions.** Rat SDSL is reported monomeric but human SDSL is a crystallographic dimer; is this a real species difference or an assay artefact? Human SDSL carries IBA L-serine catabolic process (GO:0006565) and rat does not. The rat paper shows L-serine/L-threonine decomposition in cells, so a process annotation could be considered by a curator; it was not added here.

**Stale UniProt quotes (2026-10-10):** replaced 3 `UniProtKB:A0A6N3IN21` supporting_text quotes (the FUNCTION text now wraps at "alpha-/ketobutyrate", so the old quote no longer matched the flat file) with verbatim FUNCTION fragments and the L-serine CATALYTIC ACTIVITY reaction from the current `Sdsl-uniprot.txt`.
