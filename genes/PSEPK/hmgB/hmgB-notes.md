# hmgB curation notes

Q88E48/PP_4620 is annotated as fumarylacetoacetase (EC 3.7.1.2)
[UniProtKB:Q88E48, "RecName: Full=fumarylacetoacetase"].

The organism-specific pathway paper identifies HmgB as one of three enzymes
that catabolize homogentisate and produce fumarate and acetoacetate
[PMID:15262943, "Homogentisate is then catabolized by a central catabolic
pathway that involves three enzymes, homogentisate dioxygenase (HmgA),
fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC),
finally yielding fumarate and acetoacetate."].

The generic `catalytic activity` and `aromatic amino acid metabolic process`
annotations are therefore replaced by the specific molecular function and
homogentisate-catabolic process rather than retained as redundant core terms.

## 2026-10-23 re-review (homogentisate catabolism module, step 3)

- Replaced UniProt quotes of the DE name/EC number and the PATHWAY comment, which
  are backed only by ARBA rules (`ECO:0000256|ARBA:...`), with family-signature
  evidence: NCBIfam TIGR01266 (fum_ac_acetase), PANTHER PTHR43069:SF2 and
  InterPro IPR005959, plus the PAINT IBD rows for node PTN002453799
  (interpro/panther/PTHR43069/PTHR43069-paint.tsv). Q88E48 receives the
  TreeGrafter terms via graft node PTN002453800, two steps below that IBD node.
- `catalytic activity` and `aromatic amino acid metabolic process` changed from
  MARK_AS_OVER_ANNOTATED to MODIFY (correct-but-general -> GO:0004334, and ->
  GO:0006572 + GO:0006559, respectively), per the refinement rule.
- Core function now lists homogentisate, L-tyrosine and L-phenylalanine
  catabolic processes; consistent with the PTHR43069 family review, which
  assesses all four PAINT terms as SOUND.
