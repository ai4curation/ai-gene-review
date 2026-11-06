# Manual gene evidence notes

## 2026-11-05 comparative module audit

Reviewed the complete gene rather than only a module placement: all seeded GO
rows, original reference fields, exact raw UniProt record and relevant primary
literature were checked. The 2016 polyamine synthesis review (PMID:27268252)
and 2018 function review (PMID:30254075) were read as background; neither
substitutes for a target-specific assay. The broad family names encompass
substrate-divergent proteins and do not determine native substrate preference.

The normal command `just deep-research BACTN BT_0674 --provider falcon` failed
with HTTP 403 authentication. No Falcon-branded text was authored. The raw
UniProt/GOA files were retained without refresh or edits. Manual curation uses
these notes and the genuine primary sources; no source cache was hand-edited.

QuickGO searches for carboxyaminopropylagmatine and the specific carboxypolyamine
decarboxylases found no corresponding specific activity term. GO:0102143 is
active and its definition explicitly covers both PUT/DAP reactions; obsolete
GO:0102144 is not used. NTRs describe missing activities rather than guessing IDs.
Exact PANTHER labels were checked against panther.obo and the record's DR lines.

The accessible primary Figure 1 identifies CASDC as BT_0674 on the
carboxyspermidine-to-spermidine step. This resolves the gene identity independently
of an automatic protein name. The genuine publisher image is retained in
BT_0674-source-analysis/PMID27118128-figure1.gif; provenance records the URL.

The normal `just fetch-pmid 27118128 --force` refresh still yielded abstract-only
content (no PMC record); the publisher explicitly exposes subscription preview
content. Its publicly accessible supplementary Table S1 lists BLAST query
proteins, not the target assays, and is not used as target evidence. The abstract
explicitly reports that deleting casdc depleted spermidine and decarboxylase
activity and that complementation restored both [PMID:27118128, "The
complemented Δcasdc strain restored the spermidine biosynthetic ability,
decarboxylase activity, and growth."]. No unreported purified-enzyme rates,
substrate specificity exclusions, or microscopy localization are inferred.

Actions: broad catalytic rows MODIFY to the supported shared carboxypolyamine
decarboxylase NTR; native product/pathway row MODIFY from norspermidine to
spermidine, avoiding a redundant NEW row. The two LysA IBA claims are REMOVE
because PTHR43727:SF1 is outside their supported SF2 scope, consistent with
the existing family review's PTN000159906 pruning assessment. The target's
polyamine activity supports that distinction; no target-specific negative
meso-diaminopimelate assay is claimed. `just paint-losses BACTN BT_0674` found
no IRD or IKR on this lineage. The IBD is evaluated by branch scope, not number
of donor proteins.
