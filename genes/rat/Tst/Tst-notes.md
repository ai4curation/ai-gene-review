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
- GO:0016226 iron-sulfur cluster assembly (NAS, PMID:2018478): resolved in the 2026-10-17
  review follow-up (see below). Changed ACCEPT -> MARK_AS_OVER_ANNOTATED and removed from
  core_functions: the support is an NAS 1991 introduction statement plus in vitro Fe-S
  reconstitution, UniProt dropped the Fe-S wording, and in vitro sulfur donation does not
  establish participation in the cellular ISC assembly pathway (NFS1/ISCU machinery).
- The 5S rRNA import role (GO:0008097, GO:0035928) is By-similarity from human TST only.

## Review follow-up 2026-10-17

Addressed PR #4615 reviewer suggestion on GO:0016226 iron-sulfur cluster assembly. Changed
ACCEPT -> MARK_AS_OVER_ANNOTATED and removed it from the GO:0004792 core-function
directly_involved_in list. Rationale: support is NAS (a 1991 cDNA-characterization
introduction statement, PMID:2018478) plus in vitro Fe-S reconstitution, UniProt has dropped
the Fe-S wording from FUNCTION, and in vitro sulfane-sulfur donation / sulfur extraction does
not establish that Tst performs a step of the cellular ISC assembly pathway (carried out by
NFS1/ISCU and associated factors) - the participation test is not met. Also removed blank
lines inside quoted YAML scalars (4). Revalidated and re-rendered.

Update (2026-10-17, re-review follow-up 2): (1) The PMID:2018478 reference finding that
asserted the paper "supports direct annotations to iron-sulfur cluster assembly" was
rewritten to describe the literal (NAS introduction) statement and tagged with
finding_review (finding_status: DISPUTED) explaining that the GO:0016226 row was demoted
to MARK_AS_OVER_ANNOTATED, so the reference finding and the annotation row no longer
contradict. (2) Both remaining "iron-sulfur cluster homeostasis" phrasings (top-level
description and the core_functions description) now carry a clause distinguishing
homeostasis (sulfane-sulfur exchange with Fe-S centers) from the dedicated cellular Fe-S
cluster assembly pathway (ISC machinery) that Tst does not carry out.
