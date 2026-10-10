# Tst notes

- UniProtKB:P24329 states: FUNCTION: Together with MRPL18, acts as a mitochondrial import factor for the cytosolic 5S rRNA and is involved in formation of iron-sulfur complexes, cyanide detoxification, or modification of sulfur-containing enzymes. [UniProtKB:P24329].
- Core interpretation: rhodanese sulfur transfer, cyanide detoxification, and mitochondrial 5S rRNA import.
- Accepted direct GO terms include: 5S rRNA binding, cellular detoxification of nitrogen compound, iron-sulfur cluster assembly, rRNA import into mitochondrion, rRNA transport, sulfurtransferase activity, thiosulfate-cyanide sulfurtransferase activity.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

**GOA changes.** Three new rows: GO:0005739 mitochondrion (IBA, PANTHER:PTN000146244),
GO:0005739 mitochondrion (IEA, ARBA, GO_REF:0000120), GO:0016783 sulfurtransferase
activity (IBA, PANTHER:PTN000146159). One row retired: GO:0005739 mitochondrion (IEA,
GO_REF:0000044); review kept, with a note that GOA no longer carries it.

**Actions.** All three new rows set to KEEP_AS_NON_CORE, matching their existing siblings
(the localization rows and the generic sulfurtransferase parent of GO:0004792). No existing
action changed. The NEW GO:0070813 hydrogen sulfide metabolic process row was re-checked
against the participation test and the comparator check. Tst catalyzes the
persulfide-to-sulfite step itself (Reactome R-RNO-1614611 "Persulfide sulfur is transferred
onto sulfite"). In QuickGO (human/mouse/rat), Ethe1 carries GO:0070813 (ISO), and
SQOR/ETHE1 (IDA) and TSTD1 (TAS) carry GO:0019418 sulfide oxidation. The NEW row is kept.

**UniProt refresh.** The rewritten P24329 FUNCTION no longer contains "is involved in
formation of iron-sulfur complexes, cyanide detoxification, or modification of
sulfur-containing enzymes". It now gives rat-specific experimental evidence (PubMed:7608189)
for the reaction [UniProtKB:P24329 "Catalyzes the transfer of sulfur ion from thiosulfate to
cyanide, although other thiol compounds, besides cyanide, can act as sulfur ion acceptors"].
All 15 stale UniProt quotes were replaced with current FUNCTION, SUBCELLULAR LOCATION or
5S-rRNA FUNCTION sentences that fit each row. The description was rewritten to remove the
curation commentary, and status was set to COMPLETE.

**Open questions.**
- GO:0016226 iron-sulfur cluster assembly (NAS, PMID:2018478) is still ACCEPTed and listed
  in core_functions. UniProt has dropped the Fe-S wording from FUNCTION, and the support is
  a 1991 statement in an introduction plus in vitro Fe-S reconstitution literature. A
  curator could consider whether Tst actually participates in cellular Fe-S cluster
  assembly, or only donates sulfide in vitro.
- The 5S rRNA import role (GO:0008097, GO:0035928) is By-similarity from human TST only.
