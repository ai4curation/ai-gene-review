# Ddo review notes

## Evidence summary
- [PMID:25747990] Rat Ddo/DASPO is experimentally characterized for D-aspartate oxidase activity and D-aspartate catabolism.
- [PMID:29292239] The rat enzyme is described as D-aspartate oxidase with FAD-dependent activity.
- [UniProtKB:D3ZDM7] UniProt records D-aspartate oxidase activity with experimental evidence from PubMed:25747990, PubMed:29292239, and PubMed:32376478.

## Curation decisions
- Core function: D-aspartate oxidase (D-aspartate oxidase activity, GO:0008445).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 14 new rows, all ISO donor-splits of existing reviewed terms; 1 row retired.

- New donors: RGD:14215375, human DDO (UniProtKB:Q99489) and human isoform-qualified donors (Q99489-1, Q99489-3). Resolved consistently with the existing rows for each term:
  - GO:0005777 peroxisome x3: KEEP_AS_NON_CORE.
  - GO:0008445 D-aspartate oxidase activity x4: ACCEPT.
  - GO:0019478 D-amino acid catabolic process x3: ACCEPT.
  - GO:0047821 D-glutamate oxidase activity x2: KEEP_AS_NON_CORE (weak secondary substrate).
  - GO:0071949 FAD binding (human donor): KEEP_AS_NON_CORE.
  - GO:0050877 nervous system process (human donor): MARK_AS_OVER_ANNOTATED, with propagation_review naming the human IMP source (PMID:28560262).
- Retired: GO:0046416 D-amino acid metabolic process (IEA, InterPro). Review kept; reason notes GOA no longer carries it.

Action changes:
- GO:0006533 L-aspartate catabolic process (ISO from human DDO Q99489/Q99489-1): MARK_AS_OVER_ANNOTATED -> REMOVE. DDO is stereospecific for the D-enantiomer [PMID:29292239 "d-Aspartate oxidase (DDO) is a degradative enzyme that is stereospecific for the acidic amino acid d-aspartate"], so an L-aspartate catabolism claim is contradicted, not just broad. The source could not be traced on the canonical human record in QuickGO (source_status changed from SOURCE_BAD to SOURCE_STALE_OR_MISSING).

Quote hygiene: 36 UniProtKB quotes cited DR GO lines (6 no longer present in the refreshed D3ZDM7 entry) and 3 quoted an old FUNCTION sentence ("strict substrate specificity ... no activity on L-amino acids or D-alanine") that UniProt has replaced. All were replaced with verbatim current CC text (FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBCELLULAR LOCATION). Experimental rows (EXP/IDA from PMID:12209855, 1991137, 25747990, 29292239, 32376478) now also cite their own abstracts, e.g. [PMID:1991137 "By means of subcellular fractionation D-aspartate oxidase was shown to be localized in peroxisomes in rat and human liver."].

Description rewritten to remove curation commentary.

Open question: RGD:14215375 donor identity was not resolved (left unnamed rather than guessed).
