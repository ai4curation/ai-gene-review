# pgl-1 review notes

## 2026-09-20 full-gene rereview

All existing annotations, authored NEW rows, description, core functions and references
were assessed. Source fields were preserved. Exact source-row identities and individual
outcomes are recorded in
`projects/IBA_REVIEW/rereview-2026-09-20/germ-granule-rna-regulation.yaml`.

The repository provider reports and the global OpenScientist cache were checked by
exact gene/accession. No target-specific OpenScientist adjudication was found; the
one incidental PGL/MEX name match is a WAGO-1 report, not an adjudication of these genes.
No duplicate provider request was launched by this reviewer.

Actual PTHR47958 topology is positive for all four IBAs. PTN002774495/PTN002773962
helicase-loss nodes are not ancestors of PGL-1. The exact leaf is among DDX39-like
helicases, which creates a concrete conflict with the experimentally characterized
PGL scaffold and novel alpha-helical RNase domain (PMID:26787882). The solved domain
is only part of the protein; it does not itself exclude all helicase mechanisms.
Helicase, spliceosomal splicing and mRNA export are UNDECIDED pending the parent-run
focused OpenScientist request (gated launcher session 15417; no completion claimed).
Splicing/export are assessed independently from catalysis and not rejected merely
because granules are cytoplasmic/perinuclear. mRNA binding remains supported.

Broad nuclease/endonuclease, differentiation, reproductive-process and experimental
protein-binding rows are accepted; breadth and repeated GO IDs are not biological
refutations. The IFE-1 interaction is direct and functional. HT Y2H and NMAD-1 IP-MS
source observations are retained with their supplementary-table/extraction limits;
no unverified partner mechanism is assigned. LAF-1/ELLI studies support PGL marker
location without transferring the perturbed protein's mechanism to PGL-1.

Hydrolase remains valid at the curated overall reaction scope: UniProt explicitly
consumes H2O and yields a 3′-phosphate product. A cyclizing intermediate/lyase EC class
can coexist with hydrolysis; missing GO is_a ancestry alone would not refute it.
The primary paper establishes G-specific cleavage but leaves the novel mechanism
and native RNA targets unresolved. The cached full_text_available flag is broader
than its actual coverage: it contains Abstract/Discussion, not the Results section.
RNase catalysis is not established as the cause of granule assembly or fertility.

Four old authored proposals were withdrawn: spermatogenesis and P-granule assembly
are descendants of existing gamete-generation/organization terms; native RNA
catabolism is not established by the in vitro RNase assay; protein sequestration
was inferred without demonstrating a PGL/SIR-2.1 inhibitory binding mechanism.
Evidence is retained in references/questions. The apoptosis NEW is retained:
PMID:26598553 and full-text PMID:27650246 show gain/loss effects and PGL-dependent
CED-4 protein regulation without matching RNA change. This establishes regulatory
work beyond necessity; direct ced-4 binding or SIR-2.1 sequestration is not asserted.
QuickGO ancestry for this proposal has no overlap with existing process ancestors.

The Falcon report explicitly could not retrieve the RNase primary study; that
limitation is not a refutation. The older OpenAI report provides useful scaffold and
interaction context but overstates native RNA cleavage and SIR-2.1 sequestration and
contains incorrect GO IDs. Its treatment of PGL as autophagy cargo does not establish
participation in executing autophagy. Those claims were not imported into the review.

## 2026-09-21 focused OpenScientist incorporation

The previously pending `pgl-fold-and-inherited-helicase-rna-processing` report is
now complete and critically incorporated together with both HTML/PDF artifacts.
No duplicate report was requested. All 28 annotation objects and actions remain:
24 ACCEPT, three UNDECIDED, and the one previously justified apoptosis NEW. All
27 original source rows and the retained authored proposal preserve their metadata.

The three inherited terms remain unresolved after the report, rather than awaiting
another automatic adjudication. The report correctly emphasizes PGL-specific
RNase/scaffold architecture but does not supply a direct negative helicase test.
The exact positive PAINT descent is unchanged. Its proposed GLH partner-confusion
mechanism is unverified. Independent motif scripts find that two report patterns
miss the GLH-1 control itself; expanded patterns recover the actual control motifs
while remaining absent from PGL-1. The live GAR1 match covers only the RGG-rich
629–728 tail, not the full protein. Raw inputs, hashes, script/output and method
limits are in `pgl-1-bioinformatics/`.

The full 2016 OSTI article supplies the previously missing Results and Methods,
with a hashed copy in `pgl-1-primary-evidence/`. Its duplex-protected cleavage assay
has no added ATP and does not measure unwinding. RNase-defective Q342A animals
remain fertile in the tested conditions, which does not show universal in vivo
dispensability. Full 2021 PMID:33579952 adds an N-terminal assembly interface and
PGL-1-tethered reporter repression requiring WAGO-1 for its full effect. The
1.5-Angstrom structure is C. japonica; the paper also performs C. elegans biochemical
and genetic tests. Reporter turnover is not assigned to PGL-1 RNase chemistry.
The description and existing core functions now reflect this direct regulatory
scaffold work, without adding a new BP or restoring redundant prior proposals.

Full PMID:22991439 supports PGL-1-dependent FBF-2 localization/mRNA binding and
places granules in the export environment. PMID:20223759 remains abstract-only
in the cache and supplies granule-level RNA transit context. The report's claim
that cytoplasmic-side localization excludes export is withdrawn; these observations
also do not independently establish PGL-1 as the export factor. Spliceosomal work
is assessed separately from both export and helicase catalysis.

`pgl-1-report-assessment.md` records the substantive report findings, errors, primary
scope, and exact remaining curator/experimental questions. The original full-gene
audit now marks review complete with this focused follow-up recorded. Source-row
identity and quotation validation are checked again with the new history record.
