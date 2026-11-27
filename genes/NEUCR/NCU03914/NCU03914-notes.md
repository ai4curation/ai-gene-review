# NEUCR NCU03914 review notes

## 2026-10-24

- Seeded the review with
  `UV_PROJECT_ENVIRONMENT=/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros-yeast/.venv UV_FROZEN=1 just fetch-gene NEUCR NCU03914`.
- `projects/FUNGAL_PAINT_FAMILIES.md` had listed `NEUCR/NCU09652` as the
  Neurospora candidate for `PTHR31297`. Fetching that locus showed that it is a
  `PTHR42812` GH43 beta-xylosidase, not a PTHR31297 GH5 glucanase. InterPro's
  API instead identifies `Q1K5Z7`/`NCU03914` as the Neurospora crassa
  `PTHR31297:SF34` member.
- `UV_PROJECT_ENVIRONMENT=/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros-yeast/.venv UV_FROZEN=1 just fetch-gene-pmids NEUCR NCU03914`
  found no GOA PMIDs because all five seeded rows are GO_REF-only electronic
  annotations.
- `UV_PROJECT_ENVIRONMENT=/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros-yeast/.venv UV_FROZEN=1 just deep-research-falcon NEUCR NCU03914 --fallback perplexity-lite`
  failed because no deep-research provider credentials or agentapi endpoint are
  configured.
- Manual live searches for `NCU03914`, `Q1K5Z7`, and Neurospora
  glucan 1,3-beta-glucosidase found no primary paper that directly assayed
  NCU03914 catalytic activity or localization. The useful hits were Pei et al.
  2015, which screened the FGSC 16594 NCU03914 deletion strain on Avicel and
  found no gross lignocellulase-secretion deficit, Liu et al. 2022, a newer
  HSAF/cell-wall stress transcriptomics study whose cached full text does not
  mention NCU03914, and Galagan et al. 2003, the Neurospora genome paper cited
  by UniProt for the Q1K5Z7 genomic sequence.

PTHR31297 PAINT notes:

- The NCU03914 UniProt record places Q1K5Z7 in `PTHR31297:SF34`, PANTHER's
  `GLUCAN 1,3-BETA-GLUCOSIDASE 2` subfamily, and records a predicted internal
  transmembrane helix followed by a C-terminal GH5 domain.
- The only PTHR31297 IBA inherited by NCU03914 is `PANTHER:PTN001262628` for
  `GO:0009251 glucan catabolic process`. That IBD sits at the broad PTHR31297
  root and is seeded by Aspergillus nidulans ExgD/Q5AVZ7 from SF34 and
  ExgB/Q5B6Q3 from SF39, so it is consistent with a broad exgD-like fungal GH5
  beta-glucanase assertion.
- The exact `GO:0004338 glucan exo-1,3-beta-glucosidase activity` IBD is a
  separate `PANTHER:PTN001262687` Saccharomycetes node seeded by Candida XOG1 and
  budding-yeast EXG1/EXG2/SPR1 members. NCU03914 is outside that SF1 node. The
  current GOA file presents the exact beta-1,3-exoglucosidase row as an
  ARBA/EC-derived IEA. The Q1K5Z7 UniProt flat file still displays the same term
  as a GO_Central IBA, which appears stale against the current PAINT placement.
- The sibling `SCHPO/exg2` review is also an SF34 case and is intentionally
  cautious: S. pombe Exg2 is a membrane GH5 protein with a wall phenotype, but
  direct assays did not detect the narrower beta-1,6-glucanase activity
  transferred from Exg1-like paralogs.
