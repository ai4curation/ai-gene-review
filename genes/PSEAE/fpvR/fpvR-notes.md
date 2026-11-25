# fpvR (PA2388, Q9I192) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I192 --alias fpvR`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used; literature from the cached seed paper,
PubMed MCP and a web search ("FpvR cytoplasmic domain binds PvdS FpvI anti-sigma"). Read with
the cognate sigma reviews fpvI and pvdS for consistency.

### Literature

- Seed paper PMID:12492864 (Beare et al. 2003), abstract only (no PMC copy). [PMID:12492864
  "FpvR negatively regulates the activity of a second ECF sigma factor, FpvI, which is required
  for the synthesis of FpvA"]; FpvR also controls PvdS, which drives pyoverdine production.
- PMID:25433393 (Edgar et al. 2014, full text cached): [PMID:25433393 "The cytoplasmic region of
  FpvR bound to and inhibited both FpvI and PvdS when the proteins were co-expressed in
  Escherichia coli."]; tandem affinity purification showed FpvR-PvdS binding in P. aeruginosa;
  FpvI binding involves sigma region 4. [PMID:25433393 "the anti-sigma factor FpvR that spans
  the cytoplasmic membrane"].
- UniProt Q9I192: FecR_N (PF16220), FecR (PF04773), PIRSF018266, one Phobius TM helix (93-114).

### Annotation decisions

- GO:0016989 sigma factor antagonist activity (IMP): ACCEPT, core MF.
- GO:0045892 (IEA, GO_REF:0000108): MODIFY to GO:2000143 negative regulation of DNA-templated
  transcription initiation (matches the GO:2000142 accepted on the cognate sigma reviews).
- GO:1900705 negative regulation of siderophore biosynthetic process (IMP): KEEP_AS_NON_CORE
  (via PvdS).
- NEW GO:0005886 plasma membrane (IC): TM helix plus published description.
- Action counts: ACCEPT 1, MODIFY 1, KEEP_AS_NON_CORE 1, NEW 1.
- GOA has no IBA rows on fpvR, although the PAINT leaf file assigns it the PTN001250434 IBA.

## PseudoCAP IBA-seed assessment

Node-level assessment recorded here once (fpvR has the most direct evidence: binding and
inhibition assays); PA0471 and foxR cross-reference it.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001250434 | GO:0016989 sigma factor antagonist activity | 4 | 53 (7 taxa) | GO:0016989, IMP, PMID:12492864 | SOUND | The abstract states FpvR negatively regulates FpvI activity; direct binding and inhibition of FpvI and PvdS shown later (PMID:25433393). | VreR (G3XCU5, now merged into O69006), PA0471/FiuR and foxR (IMP, PMID:16484199, derepression in mutants) | Yes |

### Node PTN001250434

The four seeds are all P. aeruginosa FecR-family anti-sigma factors (PseudoCAP). G3XCU5 is
inactive in UniProt, merged into O69006 (vreR, PA0676). Leaf IBAs (`.cache/paint/leaf.gaf.gz`):
13 P. aeruginosa FecR-family proteins (including PA0150, PA1301, PA1364, PA2051, PA2094,
PA3409, PA3900, PA4895, femR, vreR, fiuR, foxR, fpvR), 26 Bacteroides thetaiotaomicron, 8
Rhodopirellula baltica, 3 Leptospira, 1 Xanthomonas, E. coli FecR (P23485) and one Ricinus
communis protein (B9TEC7, probably a bacterial contaminant sequence in the plant genome
assembly). The clade is the FecR anti-sigma family, whose members (FecR itself, the
Bacteroides PUL-associated anti-sigma factors) hold cognate ECF sigma factors inactive, so
the term suits the clade. FpvR's seed is supported by direct binding data; the FiuR and FoxR
seeds are sound derepression phenotypes. The IBD stands without any one seed. No GO_CENTRAL
defect. The dual pro-sigma role of the cytoplasmic fragments is not in conflict with the
term. No PSEUDOCAP defects.
