# Nepl15 (CG4721, Q9VCU1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Nepl15 is the nearest experimentally studied paralog of the ProtNLM2 benchmark gene Nepl19. No
ProtNLM2 output was opened or used.

### Setup
- `just fetch-gene DROME Nepl15` first resolved the symbol to Q95U74, which is the TrEMBL cDNA entry
  GH01974p. Q95U74 differs from the reference-proteome entry Q9VCU1 at one residue (673 R/M; see
  `Nepl15-bioinformatics/RESULTS.md`). The review was re-seeded with `--force --uniprot-id Q9VCU1`, and
  the stale Q95U74 GOA rows were removed from the stub. Those rows were InterPro2GO metalloendopeptidase
  and metallopeptidase activity, which GOA does not carry for Q9VCU1.
- Deep research (`just deep-research-falcon DROME Nepl15 --fallback perplexity-lite`) failed. Falcon/Edison
  returned 403 Forbidden on authentication, and the perplexity-lite fallback timed out after 600 s.
  No deep-research file exists. The review is based on the three full-text papers and the preprint
  abstract below.

### Literature
- PMID:33483521 (Banerjee et al. 2021, full text) is the primary study. Experimental findings: the
  knockout (ends-out recombination) is viable and fertile; knockout males have less TAG and glycogen;
  knockout males and females both die sooner under starvation; larval development is slower; and
  overexpression with arm-, Cg- or mex1-Gal4 increases storage. Transcripts are enriched in the fat body
  [PMID:33483521 "Knock-out mutations in Nepl15 result in reduced levels of triglycerides and glycogen in
  adult males but not in females."]. Secretion and catalytic inactivity are predictions from SignalP,
  topology and homology models [PMID:33483521 "Nepl15 is likely to be a secreted protein, rather than a
  transmembrane protein."]. Peptide sequestration is a hypothesis from modelling.
- PMID:22952997 (Nfonsam et al. 2012, full text): an RNAi screen downstream of Ey+N, in which CG4721
  knockdown disrupts eye development (Ato, R8 selection, furrow). One UAS-RNAi line was used, and there is
  no rescue. The knockout paper does not report eye defects.
- PMID:34189422 (fly Nep/Nepl survey, full text): Nepl15 is in the motif-deficient Nepl class and in a
  94C4 tandem cluster with Nepl13 and Nepl14.
- PMID:42523199 (bioRxiv preprint 2026, abstract only): knockout females live longer, and both sexes show
  improved age-related physiology. These organismal phenotypes are not annotated.

### Evolutionary grounding
- PANTHER PTHR11733:SF238 (insect-specific, FI07649P-RELATED). The 94C4 tandem neighbours Nepl13 and
  Nepl14 are in SF240, a different subfamily, even though they are physically adjacent.
- The Nepl19 re-review NJ tree (`genes/DROME/Nepl19/Nepl19-bioinformatics/RESULTS-rereview.md`) places
  Nepl15 next to the 98F1 Nepl17-21 cluster, with Nep4 (the active SF238 peptidase) outside the Nepl
  clade. No function from Nep4 is transferred.
- Own alignment (`Nepl15-bioinformatics/RESULTS.md`): MME H584 aligns to R521, E585 to Q522, H588 to
  H525, E647 to R582 and D651 to D586. This matches the paper's description. Nep4 and Nep2 keep every
  site.

### Decisions
- plasma membrane (IBA from PTN000199753, and IEA SubCell from ARBA): MODIFY to extracellular region.
  The protein has a signal peptide and no anchor, so this is a target-specific loss. Not core, because it
  is a prediction.
- proteolysis (IEA InterPro2GO): REMOVE, because the protein is a pseudoenzyme and the row would
  contradict the accepted NOT peptidase activity rows.
- NOT peptidase activity (IKR GO_REF:0000047 and PMID:34189422): ACCEPT both.
- compound eye morphogenesis (IMP PMID:22952997): KEEP_AS_NON_CORE. It is RNAi-only, the knockout has
  not confirmed it, and the role is likely indirect.
- No NEW rows. The storage phenotypes come from bidirectional genetics (knockout and overexpression), but
  the mechanism is unknown, and the slower larval development of mutants could explain the knockout
  phenotype indirectly. Nepl15 has not been shown to do any step of lipid storage (participation test), so
  `GO:0019915` lipid storage and `GO:0010883` regulation of lipid storage are raised as a suggested
  question and not asserted. GOA carries no annotation from PMID:33483521.

### For transfer to relatives (e.g. Nepl19)
- Established experimentally in Nepl15: genetic requirement for normal TAG and glycogen storage, the
  overexpression effect, fat-body-enriched expression, and an RNAi eye phenotype.
- Inferred only: secretion, catalytic inactivity, and peptide sequestration (hypothesis).
- The HExxH loss in Nepl19 arose independently on the tree, so none of the Nepl15 phenotypes should be
  transferred.
