# PDI1 review notes

## Update 2026-09-02

Audited `PDI1-ai-review.yaml` for factual accuracy. The top-level `description`
field asserted "Orthologous to human PDIA3." This is incorrect and has been
corrected: the closest human counterpart of yeast Pdi1p is PDIA1/P4HB.

Evidence that *does not* discriminate (recorded so it is not reused as an
argument):

- Recommended name and EC are shared across the whole catalytic PDI family and
  cannot separate P4HB from PDIA3. Yeast PDI1 (`PDI1-uniprot.txt`) is
  `DE   RecName: Full=Protein disulfide-isomerase;` / `DE            EC=5.3.4.1;`,
  human P4HB (P07237) is the same, and human PDIA3 (P30101) also carries
  `EC=5.3.4.1 {ECO:0000269|PubMed:27897272, ECO:0000269|PubMed:7487104}`
  (checked against the UniProt REST record for P30101 on 2026-09-04). An
  earlier draft of these notes claimed PDIA3 had "no independent EC entry of
  its own in the same catalytic sense"; that was wrong and has been deleted.
- eggNOG KOGs are family-level groups. Yeast PDI1 and human P4HB both
  cross-reference `eggNOG; KOG0190; Eukaryota.`, but so does human PDIA3
  (P30101). Shared KOG0190 membership is therefore *consistent with* the
  assignment but is not confirmation of orthology, and the earlier
  "confirming direct orthology" wording has been removed.

Evidence that does discriminate:

- Shared domain architecture in the same arrangement. Yeast Pdi1p has
  `FT   DOMAIN          29..141` "Thioredoxin 1" and
  `FT   DOMAIN          356..485` "Thioredoxin 2"; human P4HB has
  `FT   DOMAIN          18..134` "Thioredoxin 1" and
  `FT   DOMAIN          349..475` "Thioredoxin 2" — the a-b-b'-a' catalytic
  layout of the canonical PDI, with the two active-site thioredoxin folds at
  matching relative positions.
- Equivalent position in the Ero1-driven oxidative-folding relay. Pdi1p
  activates Ero1p, which reoxidizes it; human P4HB likewise
  `Interacts with ERO1B (PubMed:11707400)` (`P4HB-uniprot.txt`). PDIA3 is not
  the principal Ero1 relay partner.
- General versus glycan-restricted substrate scope. Yeast Pdi1p is
  "required for formation of disulfide bonds in secretory and cell-surface
  proteins and which unscrambles non-native disulfide bonds", partnering EPS1,
  KAR2 and MNL1 (`PDI1-uniprot.txt`). PDIA3 is instead specialized on
  N-glycosylated clients through the lectin chaperones — it
  `Interacts with ERP27 and CANX` and is a "Core component of the major
  histocompatibility complex class I (MHC I) peptide loading complex"
  with CALR (P30101). Yeast has no such calnexin/calreticulin-partnered PDI
  specialization for Pdi1p.
- Caveat on framing: the PDI family expanded independently in the fungal and
  metazoan lineages, so this is best stated as "closest human counterpart"
  rather than a clean 1:1 orthology relationship.
- The gene's own `PDI1-deep-research-falcon.md` file frames the mammalian
  comparison around PDIA1, not PDIA3: "Although much of this work is framed
  around mammalian PDIA1, the mechanistic concepts apply to canonical yeast
  PDI architecture and redox cycling."

No GO term annotations were affected by this fix (the `existing_annotations`
list does not reference cross-species orthology); only the standalone
biological `description` field was corrected. Per CLAUDE.md the `description`
is a standalone biological summary, so the supporting identifiers (eggNOG KOG,
EC numbers) and the explicit "not PDIA3" negation are kept here rather than in
that field.
