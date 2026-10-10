# Pgp review notes

## Evidence summary
- [PMID:26755581] The abstract reports identification of a mammalian Gro3P phosphatase that directly hydrolyzes Gro3P to glycerol and regulates glycolysis, glucose oxidation, gluconeogenesis, glycerolipid synthesis, fatty acid oxidation, redox state, and ATP production.
- [UniProtKB:D3ZDK7] UniProt summarizes rat Pgp/G3PP as a glycerol-3-phosphate phosphatase hydrolyzing glycerol-3-phosphate into glycerol.

## Curation decisions
- Core function: glycerol-3-phosphate phosphatase (sn-glycerol 3-phosphatase activity, GO:0043136).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-10

GOA refresh changes:
- 8 new rows seeded: GO:0000121 sn-glycerol 1-phosphatase activity IEA (GO_REF:0000120, RHEA:46084); GO:0005737 cytoplasm IBA (PTN002711682); and six ISO rows with human PGP (UniProtKB:A6NDG6) as donor that duplicate existing mouse-sourced ISO rows (GO:0000121, GO:0006114, GO:0006650, GO:0008967, GO:0043136, GO:0110052).
- 1 row retired: GO:0000121 IEA GO_REF:0000116 (superseded by the GO_REF:0000120 row).

Decisions:
- Donor-split A6NDG6 rows reviewed consistently with their mouse-sourced siblings; cytoplasm IBA KEEP_AS_NON_CORE (no target-specific divergence; substrates are cytosolic).
- GO:0008967 phosphoglycolate phosphatase activity (IEA, ISS, ISO x2) and GO:0110052 toxic metabolite repair (ISS, ISO x2): KEEP_AS_NON_CORE -> ACCEPT. Mammalian PGP is a conserved metabolite-repair enzyme [PMID:27294321 "We discovered that a single, widely conserved enzyme, known as phosphoglycolate phosphatase (PGP) in mammals, dephosphorylates both 4-phosphoerythronate and 2-phospho-L-lactate, thereby preventing a block in the pentose phosphate pathway and glycolysis."], and the refreshed UniProt FUNCTION now leads with this role ["Acts as a metabolite repair enzyme which eliminates toxic glycolytic side products (By similarity)."]. The earlier Km argument (2-PG below Km in hepatocytes) limits the physiological weight of 2-PG in those cells but does not refute the activity. Added a second core_functions entry for metabolite repair.
- Experimental rows from PMID:26755581 now quote the paper [PMID:26755581 "We identified that mammalian phosphoglycolate phosphatase, with an uncertain function, acts in fact as a G3PP."].
- All UniProt quotes were GO cross-reference lines (circular) or a stale FUNCTION text; replaced with CATALYTIC ACTIVITY, COFACTOR or FUNCTION fragments from the current entry.
- The proposed_new_terms entry for GO:0061179 (an existing GO term, not a new-term request) was converted into a suggested_questions entry: the insulin-secretion effect is mediated by Gro3P levels and needs curator judgment on whether it counts as regulation by Pgp.
- Description rewritten without review commentary and to include metabolite repair.

Open questions:
- GO:0140401 4-phosphoerythronate phosphatase activity is not yet annotated to rat Pgp; recorded as a suggested question.
