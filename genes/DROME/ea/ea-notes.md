# ea (easter) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ea is being reviewed in its own right as the best-characterised
Drosophila relative of DROME/CG30288. ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon DROME ea --fallback perplexity-lite` failed: Falcon
(Edison API) returned 403 on authentication, and the perplexity-lite fallback
returned 401 insufficient_quota. No deep-research file was produced. The review
is based on the cached publications (GOA-cited PMIDs plus PMID:20605458 and
PMID:16566925, cited by UniProt) and the UniProt Swiss-Prot record.

### Evolutionary placement

- PANTHER 19.0 classification: ea is the sole Drosophila member of PANTHER subfamily PTHR24256:SF527 ("SERINE PROTEASE EASTER") within PTHR24256 (TRYPTASE-RELATED).
- CG30288, CG30289, CG30414 and SPH158 are in a different subfamily,
  PTHR24256:SF546.
- The IBA rows for ea (GO:0004252, GO:0006508, GO:0005576) come from PAINT node
  PTN001207268. Its seed lists include ea (FBgn0000533) along with mouse/rat
  Prss and human tryptase genes (e.g. P20231, Q15661), so the node is deep:
  it is a trypsin-like extracellular serine protease node, not an
  Easter-specific one. Several descendant nodes carry IKR NOT
  GO:0004252 (loss of catalytic activity) annotations that point back to
  PTN001207268, showing PAINT curators judged catalytic activity per branch.
- Transferable (node level): serine-type endopeptidase activity, proteolysis,
  extracellular region.
- Not transferable (Easter-specific, experimentally established in fly only):
  Toll receptor ligand protein activation cascade, dorsal/ventral axis
  specification, perivitelline-space location, activation by Snake, inhibition
  by Spn27A.

### Experimentally established in D. melanogaster

- Serine endopeptidase activity: recombinant/refolded Easter cleaves
  pro-Spaetzle [PMID:9533958 "An active form of Easter protease cleaves the Spätzle protein"],
  [PMID:23729565 "show that the renatured enzyme performs the activation cleavage of two Spätzle isoforms"].
- Activated by Snake [PMID:11296245 "GD activates Snake, which in turn activates Easter"];
  Snake cleavage of Easter is the first Pipe-dependent step
  [PMID:20605458 "the proteolysis of Easter by Snake is the first Pipe-dependent step"].
- Zymogen distributed in extracellular (perivitelline) space
  [PMID:1425342 "appears to be evenly distributed in the extracellular space"].
- Loss of function dorsalizes, gain of function ventralizes
  [PMID:2492450 "Loss-of-function mutations in easter result in a dorsalization of the embryonic pattern"].
- Product required only after fertilization [PMID:2492450 "the easter product is only required after fertilization"],
  which is why the oocyte-polarity term GO:0007311 was modified to GO:0009950.
- Inhibited covalently by Spn27A [PMID:14667416], [PMID:14654000].
- Not the immune Spaetzle-processing enzyme: SPE fills that role
  [PMID:16399077 "Although in Drosophila the Easter protease processes the pro-Spätzle protein to generate the Toll ligand during development"].

### Decisions

- GO:0004252 (all rows): ACCEPT.
- GO:0006508 proteolysis: ACCEPT (GO:0160032 is not a descendant of
  proteolysis, so no refinement exists in the same branch).
- GO:0005576: MODIFY to GO:0098595 perivitelline space (as done for snk).
- GO:0007370 ventral furrow formation: MARK_AS_OVER_ANNOTATED (downstream of
  dorsalization).
- GO:0009953: MODIFY to GO:0009950; GO:0007311: MODIFY to GO:0009950.
- No NEW terms. Easter is also the substrate of Snake (zymogen activation),
  but being cleaved is not participation, so no zymogen-activation term was added.
