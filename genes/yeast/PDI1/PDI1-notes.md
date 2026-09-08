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
- Shared a-b-b'-a' domain architecture. Yeast Pdi1p has
  `FT   DOMAIN          29..141` "Thioredoxin 1" and
  `FT   DOMAIN          356..485` "Thioredoxin 2"; human P4HB has
  `FT   DOMAIN          18..134` "Thioredoxin 1" and
  `FT   DOMAIN          349..475` "Thioredoxin 2" (FT lines verbatim from the
  respective `-uniprot.txt` files). An earlier draft listed this as a
  *discriminating* argument; that was wrong, because the same layout is shared
  with PDIA3 [PMID:17507649 "In PDI, these domains have an a-b-b′-a′
  organization. PDIp, ERp57, and PDILT share the same domain structure with
  PDI"] — ERp57 *is* PDIA3. What the matched FT lines do establish is that
  Pdi1p is a canonical **two-active-site** PDI, which rules out the b-type-only
  and single-a-domain family members (ERp27, ERp29 and similar) but says
  nothing about P4HB versus PDIA3.

Evidence that does discriminate:

- Equivalent position in the Ero1-driven oxidative-folding relay. Pdi1p
  activates Ero1p, which reoxidizes it; human P4HB likewise
  `Interacts with ERO1B (PubMed:11707400)` (`P4HB-uniprot.txt`). The
  discriminating weight of this bullet is carried by that verified positive
  P4HB–ERO1B interaction; the corresponding negative — whether PDIA3 acts as a
  comparable Ero1 relay partner — is **not checked** against data cached here
  (P30101 is uncached; see below) and is therefore not relied on.
- General versus glycan-restricted substrate scope. Yeast Pdi1p is
  "required for formation of disulfide bonds in secretory and cell-surface
  proteins and which unscrambles non-native disulfide bonds", partnering EPS1,
  KAR2 and MNL1 (`PDI1-uniprot.txt`). PDIA3 is instead specialized on
  N-glycosylated clients through the lectin chaperones — it
  `Interacts with ERP27 and CANX` and is a "Core component of the major
  histocompatibility complex class I (MHC I) peptide loading complex"
  with CALR (P30101; these P30101 lines are quoted from the same UniProt REST
  record fetched on 2026-09-04 that the EC check above used). Yeast has no such
  calnexin/calreticulin-partnered PDI specialization for Pdi1p. This split is independently corroborated in the
  literature [PMID:17507649 "ERp57 interacts with a specific set of
  glycosylated proteins that are recruited via its interaction with the lectins
  calnexin/calreticulin ( Oliver et al. , 1997 ; Jessop et al. , 2007 ) and is
  a component of the major histocompatibility complex (MHC) class I loading
  complex"], against PDI itself catalyzing "in vitro redox reactions in a wide
  variety of substrates". This is the decisive argument in this audit.
- Caveat on framing: the PDI family expanded independently in the fungal and
  metazoan lineages, so this is best stated as "closest human counterpart"
  rather than a clean 1:1 orthology relationship.
- The gene's own `PDI1-deep-research-falcon.md` file frames the mammalian
  comparison around PDIA1, not PDIA3: "Although much of this work is framed
  around mammalian PDIA1, the mechanistic concepts apply to canonical yeast
  PDI architecture and redox cycling."

Repo-local data pointing the *other* way (recorded so this audit is not silent
about the datapoints that disagree with its conclusion):

- **PANTHER places yeast PDI1 in the same subfamily as PDIA3, not as P4HB.**
  `PDI1-uniprot.txt:238` reads
  `DR   PANTHER; PTHR18929:SF132; PROTEIN DISULFIDE-ISOMERASE A3; 1.`, and
  `interpro/panther/PTHR18929/PTHR18929-entries.csv` assigns P30101 (PDIA3) to
  `PTHR18929:SF132` as well, whereas P07237 (P4HB) sits in `PTHR18929:SF101`
  (`P4HB-uniprot.txt:716`). This is the strongest contrary datapoint, and it is
  on the same UniProt file quoted elsewhere in these notes.
- **OrthoDB splits Pdi1p from P4HB.** `PDI1-uniprot.txt:206` is
  `DR   OrthoDB; 427280at2759; -.` while `P4HB-uniprot.txt:627` is
  `DR   OrthoDB; 72053at2759; -.` — different eukaryotic orthologous groups.

Neither datapoint overturns the "closest human counterpart is PDIA1/P4HB"
conclusion, but the reasons should be stated rather than assumed. The PANTHER
call is an automated HMM subfamily assignment, not a curated orthology
statement; given the lineage-independent expansion of the PDI family noted
above, there is no metazoan subfamily that the single fungal canonical PDI fits
cleanly, so a best-scoring-model assignment is weak evidence of orthology
either way. The functional arguments — Ero1 relay partner and, decisively,
general versus glycan/lectin-restricted substrate scope — run the other way and
are what the conclusion rests on. The `description` wording ("closest human
counterpart", not "ortholog of") is deliberately chosen to remain compatible
with this unresolved family-level ambiguity.

Possibly discriminating, **not yet checked**: Pdi1p and P4HB share an identical
OMA group fingerprint — `DR   OMA; FFGMKKD; -.` at `PDI1-uniprot.txt:205` and
`P4HB-uniprot.txt:626`. Unlike the family-level KOG0190 above, an OMA group is
a real orthologous-group call, so this would be genuine evidence *if* P30101's
fingerprint differs. P30101 is not cached in this repo (there is no
`genes/human/PDIA3/`), so that comparison has not been run; recorded as a lead
only, not as evidence.

No GO term annotations were affected by this fix (the `existing_annotations`
list does not reference cross-species orthology); only the standalone
biological `description` field was corrected. Per CLAUDE.md the `description`
is a standalone biological summary, so the supporting identifiers (eggNOG KOG,
EC numbers) and the explicit "not PDIA3" negation are kept here rather than in
that field.
