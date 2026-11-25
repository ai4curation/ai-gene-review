# pfeS (PA2687, Q04804) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q04804 --alias pfeS`; accession matches the worklist.
No deep-research provider was used. PubMed esearch was unavailable (NCBI SOLR errors); a Europe
PMC query (`PfeS AND aeruginosa`) returned reviews and PfeE/enterobactin papers but no direct
biochemical study of PfeS. The seed paper PMID:8808923 is abstract-only here: the PMC record
(PMC178352) is a scanned PDF (checked with WebFetch) and the PubMed MCP returned no full text.

### Literature

- PMID:8808923 (Dean, Neshat and Poole 1996): [PMID:8808923 "PfeR (Regulator) and PfeS (Sensor),
  members of the superfamily of so-called two-component regulatory protein pairs, are required
  for the enterobactin-inducible production of the ferric enterobactin receptor (PfeA) in
  Pseudomonas aeruginosa."] The experiments described are on PfeR (knockout, bandshift with the
  pfeA promoter, pfeR-lacZ) and pfeA; no PfeS assay is described in the abstract.
- UniProt Q04804: two TM helices, periplasmic sensor domain (PDB 3KYZ, residues 28-149), HAMP,
  HisKA with His244 autophosphorylation site (ECO:0000255 PROSITE-ProRule), HATPase. No HPt or
  receiver domain.

### Annotation decisions

- GO:0000155 (IBA, IEA), GO:0000160 (IBA, IDA seed, IEA), GO:0005886 (IBA, IEA): ACCEPT.
- GO:0004673, GO:0007165, GO:0016020, GO:0016772 (IEA): TOO_GENERAL.
- GO:0009927 histidine phosphotransfer kinase activity (IBA): REMOVE; PfeS has no HPt domain.
  GO_CENTRAL WRONG_TERM defect on the PTN002463889 IBD (sole seed AT2G17820), PROBABLE.
- PSEUDOCAP WRONG_EVIDENCE_CODE defect (CHECK, SUSPECTED) on the IDA GO:0000160 row.
- Action counts: ACCEPT 7, TOO_GENERAL 4, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002463889 | GO:0000160 phosphorelay signal transduction system | 3 | 200 (59 taxa) | GO:0000160, IDA, PMID:8808923 (PseudoCAP) | UNVERIFIABLE | Abstract only; it shows PfeS is required (probably genetic) and reports direct assays only for PfeR. The term is true of PfeS by architecture, but whether a PfeS IDA experiment exists could not be checked. | E. coli RcsC P0DMC5, M. tuberculosis PrrB P9WGK7 | Yes; the term suits a sensor-kinase clade |

Other IBD at the node, not seeded by pfeS: GO:0009927 histidine phosphotransfer kinase activity,
sole seed AT2G17820 (Arabidopsis AHK1); does not suit the bacterial classical-kinase members,
GO_CENTRAL defect recorded here. pfeS shares no PTN node with the already reviewed parS or
PA5484 (no PTN002463889 in their files).

## PANTHER tree check (2026-11-05)

The node's family was not resolvable from its IBD seeds, so it was looked up by hand.
This gene's UniProt record cross-references `PTHR45436:SF15 / PTHR45436`, but
PTN002463889 is **not** in PTHR45436. The IBD's seed, Arabidopsis AHK1 (AT2G17820,
UniProt Q9SXL4), cross-references PTHR43711, and the node is in that family, holding both
AHK1 and PfeS (Q04804, PTHR43711:SF1). This is the UniProt-vs-PANTHER family
disagreement CLAUDE.md warns about; PAINT propagates on PANTHER's own tree, so PTHR43711
is the relevant one and the node is correctly placed. No family id in the review was
changed.

PTN002463889: SPECIATION, LUCA, 200 leaves, ten subfamilies (SF1:80, SF31:43, SF26:42,
SF28:19, SF32:4, SF15:3, SF29:3, SF13:2, SF18:2, SF30:2).

| Child node | Event / taxon | Leaves | Subfamilies | Verdict |
|---|---|---|---|---|
| PTN001976854 | SPECIATION, Archaea-Eukaryota | 65 | SF1:60, SF15:3, SF18:2 | Holds the AHK1 seed (16 nodes deeper); the only clade the IBD could defensibly cover |
| PTN002463899 | DUPLICATION, bacteria | 135 | SF1:20, SF26:42, SF31:43, SF28:19, SF32:4, SF13:2, SF29:3, SF30:2 | Classical HisKA sensor kinases (PfeS, BaeS, RcsC, PrrB); no HPt domains |

Paths confirmed with the tree: Q9SXL4 (AHK1) runs through PTN001976854, while Q04804
(PfeS) runs PTN002463899 -> PTN008117710 (24) -> PTN008117711 (9) -> PTN008684377 (7) ->
PTN002536215 (3). P. aeruginosa contributes four leaves in all (Q04804 pfeS, Q9I528
PA0930, Q9HZ34 PA3206, Q9I0V9 PA2524), none with an HPt domain. PfeS's own architecture
is HK_sensor-HAMP-HisKA-HATPase_c (PF16750, PF00672, PF00512, PF02518) with no Hpt
(PF01627) and no receiver domain, so GO:0009927 histidine phosphotransfer kinase activity
is wrong for it. The earlier concern is confirmed and the diagnosis sharpened: one plant
hybrid-kinase seed at a LUCA node propagates across 135 bacterial leaves. Confidence
raised PROBABLE -> CONFIRMED; the requested change stays "withdraw", with PTN001976854 as
the minimum containment if the IBD is kept. The GO:0009927 row in this review remains
REMOVE/over-annotated as previously decided.
