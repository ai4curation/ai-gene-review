# Comparative choline-to-glycine-betaine audit

## Search and access, 2026-11-06

Searched primary databases and publisher articles for bacterial choline/betaine
biosynthesis reviews, Bacillus GbsAB/OpuB mechanisms, Arthrobacter CodA and the
reported Acinetobacter BetA dual-substrate activity. Useful comparative reviews:

- PMID:12007642, *Bacterial osmoadaptation: the role of osmolytes in bacterial
  stress and virulence*. Its comparative treatment distinguishes transport and
  synthesis across Gram-positive and Gram-negative bacteria. Cached abstract
  is available; publisher full text was also inspected for the GbsB/GbsA section:
  https://academic.oup.com/femsre/article/26/1/49/631898
- PMID:23354714, *Homeostasis and catabolism of choline and glycine betaine:
  lessons from Pseudomonas aeruginosa*. The cached abstract identifies betaine
  as a branch point between retention and catabolism. Therefore the module ends
  at formation and does not promise osmoprotection in every organism.
- PMID:33613867, *Stressed out: Bacterial response to high salinity using
  compatible solute biosynthesis and uptake systems, lessons from Vibrionaceae*.
  Cached full text reports lineage-dependent betIBA distribution, including
  the surveyed Cholerae-clade exception, and differing importer organization.
  A Bacteria taxon envelope is not a universal-presence claim. This is a
  literature distribution finding, not a newly executed genome scan.
- PMID:32951822, *Choline oxidases*. Cached abstract supports the two-step
  oxygen-dependent CodA mechanism. Primary enzyme characterization and sequence
  mapping provide the concrete Arthrobacter exemplar; the review alone does
  not establish its native importer.

`just module-deep-research-falcon` was attempted normally and failed with HTTP403
(API authentication/access failure). The log is retained in the audit cache.
These are manual notes; no provider report was authored or fabricated.

## Changes required by the evidence

The previous module treated BetT-BetA-BetB as the uptake-and-synthesis model and
excluded other transporters by its boundary note. The revised boundary still
begins with extracellular choline and ends with glycine betaine, but it needs
alternative transport and oxidation implementations.

PMID:10216873 provides native OpuB/OpuC uptake evidence. OpuB's four distinct
subunit types supply a new reviewed ABC exemplar. Its subunits contribute to
the assembled activity; a family match or one ATPase does not independently
import choline. The OpuC panel is being curated in a separate choline-sulfate
PR, so no duplicate edits to those genes are introduced here.

PMID:8752328 supports GbsB/GbsA conversion in Bacillus. GbsB is a type III
alcohol-dehydrogenase-family implementation, not a GMC BetA. GO:0008812 is
acceptor-unspecified and can describe the choline oxidation without silently
transferring flavin or membrane chemistry. The family classification and
inferred NAD annotation do not replace purified cofactor-specific kinetics.
PMID:9297465 supplies direct GbsA enzyme data; substrate exclusions must be
limited to compounds actually tested.

PMID:39510372 examines purified E. coli BetA and challenges the older
crude-membrane claim of dual-substrate turnover. PMID:34431198 reports a
partially purified Acinetobacter preparation: PMS is the artificial acceptor,
and its reoxidation consumes oxygen; without PMS, oxygen consumption was not
observed. That is not direct oxidase activity and does not demonstrate native
BetB dispensability. The exact old 571-residue assayed sequence must be mapped
before adding a current Acinetobacter exemplar; a current 552-residue record
cannot be assumed identical merely from its strain label.

PMID:14678796 characterizes Arthrobacter CodA. The exact ATCC8010 sequence
AAP68832.1 matches Q7X2H8. It supports two catalytic steps. Current GO:0033713
covers choline-to-betaine-aldehyde oxidation only; substrate-qualified
GO:0004031 covers the independently demonstrated aldehyde-to-betaine oxidation.
The module must require both activities, even though one protein provides them.
Neither the first GO term nor a GMC-family match establishes the whole segment.

## Integration boundaries

The six original reviews were frozen before editing: 55 historical rows, twelve
raw UniProt/GOA files and four provider artifacts. Planned additions are Bacillus
OpuBA/OpuBB/OpuBC/OpuBD/GbsA/GbsB, Arthrobacter CodA and, only after sequence
resolution, the assayed Acinetobacter BetA. All machine annotation payloads and
raw sources remain immutable. Missing importer identity is recorded as an
unresolved role, not a false assertion of pathway absence. Capacity checks must
separate component coverage, native inventory coverage and hypothetical mixed
panels; cross-species assembly is never inferred from a Boolean combination.
