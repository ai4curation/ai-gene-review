# Manual gene evidence notes

## 2026-11-05 comparative module audit

Reviewed the complete gene rather than only a module placement: all seeded GO
rows, original reference fields, exact raw UniProt record and relevant primary
literature were checked. The 2016 polyamine synthesis review (PMID:27268252)
and 2018 function review (PMID:30254075) were read as background; neither
substitutes for a target-specific assay. The broad family names encompass
substrate-divergent proteins and do not determine native substrate preference.

The normal command `just deep-research 9FIRM CLOLEP_01503 --provider falcon` failed
with HTTP 403 authentication. No Falcon-branded text was authored. The raw
UniProt/GOA files were retained without refresh or edits. Manual curation uses
these notes and the genuine primary sources; no source cache was hand-edited.

QuickGO searches for carboxyaminopropylagmatine and the specific carboxypolyamine
decarboxylases found no corresponding specific activity term. GO:0102143 is
active and its definition explicitly covers both PUT/DAP reactions; obsolete
GO:0102144 is not used. NTRs describe missing activities rather than guessing IDs.
Exact PANTHER labels were checked against panther.obo and the record's DR lines.

The raw entry A7VSG2 cross-references EDO61992.1, the exact sequence crystallized
in PMID:39887002 and identified as CAPADC in PMID:40074085 Table S1. The crystal
structure is direct target evidence for the PLP Schiff base [PMID:39887002,
"PLP forms a Schiff base with Lys43 in both chains"]. It contains a homodimer
with interfacial active sites. The structure paper does not provide a measured
substrate-specific kinetic panel; a historical CASDC name does not settle
preference against CAPA.

The 2025 exact-pair reconstruction supports agmatine-to-aminopropylagmatine
chemistry toward spermidine. Native flux and isolated CAPADC specificity remain
open. Clostridium APT, a separate protein, produces spermine; no spermine
synthesis function is assigned to this CAPADC from the APT result.

Actions: broad catalytic rows MODIFY to a CAPADC NTR; the TreeGrafter LysA
IEA is REMOVE because the target is an SF1 carboxypolyamine enzyme, not SF2
LysA. Original node PTN001691016 is preserved and kept distinct from the
family PAINT IBD PTN000159906; no new ancestral placement is invented. The
family-derived norspermidine process is MARK_AS_OVER_ANNOTATED because no
endogenous norspermidine pathway is established. NEW IDA PLP binding is
justified by direct target crystallography, not an ARBA cofactor keyword.
No separate generic homodimerization row is proposed: assembly supports the
catalytic mechanism without requiring another core function.
