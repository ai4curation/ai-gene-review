# Q8P365 (btuE, XCC4213) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

The benchmark accession Q8P365 is the full-length product of XCC4213: 181 aa, a single
GSHPx domain spanning the protein, with the complete catalytic tetrad. It is not an
isoform, fragment or alternative gene model. It is an unreviewed TrEMBL entry (PE 3) and
there is no reviewed canonical entry for this locus.

Evolutionary grounding (PANTHER 19 tree; see Q8P365-bioinformatics/RESULTS-rereview.md):
- Q8P365 sits in PTHR11592:SF40 (THIOREDOXIN_GLUTATHIONE PEROXIDASE BTUE), under
  PTN000173904 (Gammaproteobacteria). That node also holds E. coli BtuE P06610, which
  has been characterized experimentally.
- PAINT IBD at PTN000173904: GO:0008379 thioredoxin peroxidase activity (seed P06610).
  PAINT IBD at the root PTN002480721: GO:0004602 glutathione peroxidase activity and
  GO:0034599 cellular response to oxidative stress. The current GOA file has only the
  GO:0034599 IBA for Q8P365, with a WITH list that lacks the newer FB donor, so the GOA
  snapshot predates the 2026-07 PAINT updates.
- A Xanthomonas in-paralog, Q8PAI2 (XCC1501), comes from a lineage-specific duplication,
  PTN008521337. It has a signal-peptide-like N-terminus and is probably the periplasmic copy.
- Pairwise alignment to P06610 gives 49% identity. Cp C37 and Cr C83 are conserved, as
  are Q71, W143 and N144.

E. coli BtuE literature [PMID:20621065 "Purified BtuE decomposes in vitro hydrogen
peroxide in a glutathione-dependent manner"; "BtuE uses preferentially thioredoxins A or
C as reducing agents irrespective of the peroxide substrate"]. Substrates include H2O2
and cumene, tert-butyl and linoleic acid hydroperoxides. btuE is induced by oxidative
stress elicitors. The protein named BtuE is not involved in B12 transport, despite the
btuCED operon name.

Decisions:
- GO:0004601 peroxidase activity (IEA) → MODIFY to GO:0140824 thioredoxin-dependent
  peroxiredoxin activity (primary, the clade-level reductant preference), with GO:0004602 also listed
  (PAINT root IBD; secondary in vitro GSH activity in E. coli).
  The earlier review chose GO:0004602 alone. That contradicts the BtuE-clade evidence,
  which shows thioredoxin is the preferred reductant.
- GO:0034599 IBA: ACCEPT (root PAINT node, the target descends from it, and BtuE expression is stress-induced).
- GO:0006979 IEA: this is an ancestor of the accepted GO:0034599. Changed from KEEP_AS_NON_CORE to
  TOO_GENERAL (the claim is true but entailed by the more specific accepted term).
- GO:0098869 IEA (GO_REF:0000108): ACCEPT.
- Core function changed to GO:0140824.
- Fitness: `just fetch-fitness XANCP Q8P365` failed (no FEBA data for XANCP).
- No Xanthomonas-specific experimental literature found (falcon deep research returned no grounded contexts).
