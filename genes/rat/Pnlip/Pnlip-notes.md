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
  vascular-lipase donors (LPL/LIPC/LIPG) or the same intravascular substrate
  context, not to intestinal pancreatic-lipase evidence for Pnlip.
- GO:0008970 glycerophospholipid phospholipase A1 activity belongs chiefly to
  PLRP2/vascular-lipase paralog chemistry. PMID:8656075 still matters because
  it reports poor phospholipid hydrolysis by conventional rat PL rather than
  zero activity, so this is over-annotation rather than a complete biochemical
  impossibility.
- GO:0061365 positive regulation of triglyceride lipase activity traces to
  human PNLIP self-characterization in PMID:9631512. Its bile-salt inhibition,
  colipase requirement and interfacial activation support the core lipase
  activity of PNLIP/Pnlip rather than a process in which Pnlip regulates a
  separate triglyceride lipase.
