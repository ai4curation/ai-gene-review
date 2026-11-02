# Pnlip notes

## 2026-09-20 IBA full-gene re-review

All 33 annotation rows were reassessed. Broad lipase, carboxylic ester hydrolase and lipid metabolism terms were restored, and extracellular localization is recognized as a core property of a secreted digestive enzyme. Description was rewritten as standalone biology, removing workflow commentary. Retinyl ester core support now quotes the actual rat/mouse enzyme separation study PMID:10769148 rather than a generic UniProt triglyceride sentence.

The six IBA assertions trace to PTN000906454 in PTHR11610. PMID:8656075 explicitly describes phospholipids as "a substrate poorly hydrolyzed by PL"; that positive comparator evidence contradicts the old rationale that only PLRP2 can hydrolyze them. Exact sn-1 chemistry remains unresolved because the accessible source is abstract-only. Lipoprotein-lipase GO:0004465 really does require lipoprotein-bound TG (live QuickGO), but primary intestinal secretion alone does not prove that Pnlip cannot use that substrate. HDL remodeling requires its own pathway evidence. The live fatty-acid biosynthesis definition concerns formation of fatty acid, so excluding hydrolytic release requires checking the GO process convention, not assuming de novo synthase scope. These three IBA disputes and exact PLA1 capacity are pending focused adjudication. Cholesterol homeostasis remains non-core; it is not equated with cholesterol ester hydrolysis.

The positive lipase-regulation ISO was traced from rat GOA to human PNLIP UniProtKB:P16233, then live QuickGO to CACAO IDA PMID:9631512. The abstract reports colipase dependence and interfacial activation; without its full context, REMOVE would overrule an experimental donor on incomplete evidence. It is now UNDECIDED. Root received the source as an explicitly post-launch lead. Human source follow-up is recorded without expanding this bounded batch to its folder. Experimental post-embryonic-development interpretations also remain unresolved because full text was inaccessible. In contrast PMID:15181189 and PMID:17010228 report actual activity/secretion changes with dietary lipid and leptin, supporting non-core response annotations. No pre-existing OpenScientist query/body match was found; report request is coordinated by root.

## 2026-10-10 focused OpenScientist follow-up

The `secondary-lipolysis-and-fatty-acid-pathway-scope` focused report resolved
the five pending PAINT/ISO secondary-lipase calls.

- GO:0004465 lipoprotein lipase activity, GO:0034375 HDL remodeling and
  GO:0006633 fatty-acid biosynthesis all trace through PTN000906454 to
  resolved vascular-lipase donors (rat Lipc `RGD:3009`, rat Lpl `RGD:3017`,
  mouse Lpl `MGI:96820`, human LPL/LIPC/LIPG, and bovine LPL as applicable)
  or the same intravascular substrate context, not to intestinal
  pancreatic-lipase evidence for Pnlip.
- GO:0008970 glycerophospholipid phospholipase A1 activity belongs chiefly to
  PLRP2/vascular-lipase paralog chemistry. PMID:8656075 still matters because
  it reports poor phospholipid hydrolysis by conventional rat PL rather than
  zero activity, so this is over-annotation rather than a complete biochemical
  impossibility.
- GO:0061365 positive regulation of triglyceride lipase activity traces to
  human PNLIP self-characterization in PMID:9631512. Its bile-salt inhibition,
  colipase requirement and interfacial activation support the core lipase
  activity of PNLIP/Pnlip rather than a process in which Pnlip regulates a
  separate triglyceride lipase. PMID:9631512 remains abstract-only, however,
  so the ISO row is marked as over-annotated rather than removed outright.

## Re-review 2026-10-10

GOA changes: four new rows: ISO from human PNLIP (UniProtKB:P16233) for GO:0004806 triacylglycerol lipase activity (a donor-split of the mouse-donor ISO row); GO:0005576 extracellular region by IBA (PTN008325466) and by IEA (SubCell SL-0243); and GO:0120516 diacylglycerol lipase activity (IEA, RHEA:38455). Two rows retired and kept with a note: GO:0005576 extracellular region (IEA GO_REF:0000120) and GO:0061365 positive regulation of triglyceride lipase activity (ISO). 37 rows total.

- PENDING resolved: all four ACCEPT. Diacylglycerol hydrolysis is the second step of sn-1/3 lipolysis [UniProtKB:P27657 "producing mainly 2-monoacylglycerol and free fatty acids"].
- GO:0034375 high-density lipoprotein particle remodeling (IBA): UNDECIDED -> MARK_AS_OVER_ANNOTATED. In QuickGO, the only experimental grounding for this term in the family is IMP on LIPC and LIPG, which are plasma-acting lipases. Pnlip is secreted into the gut lumen (CONTEXT_OR_TISSUE_MISMATCH).
- GO:0006633 fatty acid biosynthetic process (IBA): UNDECIDED -> KEEP_AS_NON_CORE. A comparator check shows curators annotate lipolytic fatty acid release to this term (human LPL and LIPC IDA PMID:182536; mouse LPL IDA PMID:18635818); Pnlip does the same chemistry.
- GO:0009791 post-embryonic development (IDA PMID:15181189; IEP PMID:8203536): UNDECIDED -> MARK_AS_OVER_ANNOTATED. Both abstracts state that the measurements were lipase activity and mRNA across postnatal ages [PMID:8203536 "In contrast, the PL mRNA is low at birth and rises rapidly during the suckling-weanling transition."]. This shows that Pnlip expression is developmentally regulated, not that Pnlip takes part in development.
- Lipase activity IDA rows now cite their own papers (PMID:15181189, PMID:8203536) rather than PMID:10769148. The retinoid rows now cite the retinyl ester hydrolase evidence [PMID:10769148 "these studies clearly show that PTL is the major pancreatic REH activity in mice, as well as in rats."] instead of the generic FUNCTION line. The extracellular rows cite "SUBCELLULAR LOCATION: Secreted".
- The intestinal cholesterol absorption ISO row was kept non-core, with the mouse donor traced to IMP PMID:12915407 (QuickGO).
- Status COMPLETE.

Still UNDECIDED (for a human to adjudicate): GO:0008970 glycerophospholipid phospholipase A1 activity (IBA; rat PL reported to hydrolyze phospholipid "poorly", PMID:8656075, so it is unclear whether the activity was lost or is only low); GO:0004465 lipoprotein lipase activity (IBA; no assay of Pnlip on lipoprotein-bound triglyceride); GO:0061365 (retired ISO).

## Merge with main 2026-10-17

Main's 2026-10-10 OpenScientist follow-up (PR #4647) and this re-review edited the same rows. Resolution: GO:0006633 keeps this re-review's KEEP_AS_NON_CORE, because the comparator check (LPL/LIPC/mouse Lpl IDA to the same term) shows curators apply the term to lipolytic fatty-acid release, which argues against main's SOURCE_BAD/REMOVE. GO:0034375 keeps MARK_AS_OVER_ANNOTATED (main had REMOVE) but takes main's exact WITH/FROM donor entities and OpenScientist support. GO:0008970 (MARK_AS_OVER_ANNOTATED), GO:0004465 (REMOVE) and the retired GO:0061365 ISO (MARK_AS_OVER_ANNOTATED) take main's decided calls, which replace this re-review's UNDECIDED; main's added support (PMID:9805004, PMID:32034094) is kept.

Review follow-up 2026-10-17 (PR #4617 reviewer findings): (1) The family/gene cross-check CI failure is fixed. PTHR11610's family review scopes GO:0006633 as NOT_APPLICABLE and calls PTN000906454 WRONG_NODE, and human LPL's review marks its own GO:0006633 IDA/IC/ISS rows as over-annotations, so the comparator argument for KEEP_AS_NON_CORE no longer holds. The row is now REMOVE, matching main, which supersedes the GO:0006633 call in the merge note above. (2) Broad parents now follow the batch policy: GO:0016298 lipase activity (IEA, ISO, and the PMID:8203536 IDA, whose assay is triolein hydrolysis) goes to GO:0004806, GO:0052689 goes to GO:0004806 + GO:0050253, and GO:0006629 (IEA, ISO) goes to GO:0019433 + GO:0042572. The PMID:15181189 lipase IDA is ACCEPTed at the curator's breadth because the abstract does not name the substrate, so validation's mixed-action warning for GO:0016298 is deliberate. (3) GO:0004465 is no longer UNDECIDED; it takes main's REMOVE. CC convention for this batch: a location row is ACCEPTed only when that location is part of a core_functions entry (Pnlip extracellular region for luminal digestion, Arsb lysosome for GAG degradation); otherwise location rows are KEEP_AS_NON_CORE. Batch policy for broad parents (applied to all eight genes in PR #4617): an uninformative broad parent of a specific activity or process the gene already carries is MODIFIED to that specific term; experimental rows stay at the curator's breadth unless the cited assay itself identifies the specific substrate.
