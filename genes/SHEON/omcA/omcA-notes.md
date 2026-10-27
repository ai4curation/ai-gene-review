# OmcA (SO_1779, UniProtKB:Q8EG33) — review notes

Research done by hand (no deep-research provider is configured in this environment; no
`-deep-research-<provider>.md` file was created). Provenance is given inline.

## Identity

- TrEMBL entry Q8EG33_SHEON, name from EMBL AAN54832.1, gene `omcA`, locus `SO_1779`,
  735 aa, "Evidence at protein level", PDB 4LMH.
- The submitted protein name contains a typo, "Extracelllular" (three l's). It is a
  cosmetic defect in a submitter-derived `DE` line rather than a wrong claim, so it was
  not recorded as a `source_defect` on an annotation; noting it here in case someone
  wants to report it to UniProt.
- Features used: lipobox LIPID 27 (N-palmitoyl / S-diacylglycerol cysteine), CHAIN
  27..735, ten heme c BINDING sites and Ca(2+) sites from 4LMH.
- `omcA` is immediately adjacent to `mtrC`/`omcB` (SO_1778) on the genome, but the two
  are not in the same operon.

## What the evidence supports

- Decaheme structure [PMID:24747425 "The X-ray crystal structure of Shewanella
  oneidensis OmcA, an extracellular decaheme cytochrome involved in mineral reduction,
  was solved to a resolution of 2.7 Å."], with the electron-egress heme at the
  mineral-binding face [PMID:24747425 "forming a hydroxylated surface that would bring
  a heme 10 electron egress site to ∼10 Å of a mineral surface"].
- Direct mineral reduction [PMID:17061851 "The purified outer membrane bacterial
  protein OmcA binds densely to the surface of hematite (Fe2O3), permitting direct
  electron transfer to this solid mineral to reduce Fe (III)"].
- Cr(VI) kinetics, faster than MtrC [PMID:21498755 "purified MtrC and OmcA reduced
  Cr(VI) with apparent k(cat) values of 1.2 ± 0.2 (mean ± standard deviation) and
  10.2 ± 1 s(-1)"], and a whole-cell deletion effect [PMID:21498755 "the deletion of
  omcA or both mtrC and omcA lowered the rate by 53.4% and 68.9%, respectively"].
- MnO2 [PMID:11133454 "OMCA1 and OMCB1 were 45 and 75% slower than MR-1, respectively,
  at reducing MnO(2)"] with a clean specificity control [PMID:11133454 "The omcA mutant
  (OMCA1) resembled MR-1 in its growth on trimethylamine N-oxide (TMAO), dimethyl
  sulfoxide, nitrate, fumarate, thiosulfate, and tetrathionate"].
- U(VI) [PMID:16875436 "deletions of mtrC and/or omcA significantly affected the in vivo
  U(VI) reduction rate relative to wild-type MR-1"].
- Surface exposure [PMID:12904229 "Immunofluorescence confirmed a prominent cell surface
  exposure of OmcA and a partial exposure of OmcB and the noncytochrome OM protein
  MtrB."], lipoprotein status [PMID:15482439 "Both OmcA and OmcB are lipoproteins, and
  OmcA is cell surface exposed."], T2SS dependence [PMID:18502849].
- Partnership with MtrC [PMID:16788180 "the OmcA-MtrC complex was observed to have
  enhanced Fe(III)-NTA reductase specific activity relative to either protein alone"].
  Note that OmcA is *not* a stoichiometric subunit of MtrCAB — that complex is
  MtrC:MtrA:MtrB 1:1:1 [PMID:17675441] — so OmcA was not given a complex-subunit or
  `contributes_to` treatment.

## Annotation decisions

GOA has exactly one row: `GO:0071281 cellular response to iron ion`, EXP
(ECO:0001808, RT-PCR evidence used in manual assertion), assigned by CollecTF, citing
the Fur modulon paper PMID:15576789.

- Action `MARK_AS_OVER_ANNOTATED`, not `REMOVE`. The paper is cached in full and was
  read: it compares a *fur* deletion mutant with wild type under fixed aerobic and
  anaerobic conditions and predicts a Fur-binding motif upstream of `omcA`
  computationally. No iron stimulus was applied, and the authors say the motifs still
  need verification [PMID:15576789 "Future research will focus on experimentally
  verifying the functionality of predicted Fur-binding regulatory motifs"]. The
  underlying claim (omcA is in the Fur modulon, and OmcA respires Fe(III)) is not
  false, so the row is kept and flagged rather than deleted.
- A `source_defects` entry of type `WRONG_TERM` with `requested_change: CHECK` and
  `confidence: SUSPECTED` records this for the assigning group. Confidence is
  deliberately low: the GAF row does not show the full curation rationale, and the
  repository rule against overruling curators from incomplete evidence applies.
  `resource` is `OTHER` because `CollecTF` is not in `SourceResourceEnum`; the
  assigning group is named in the explanation.
- Five NEW rows from direct evidence on this protein: GO:0020037 heme binding,
  GO:0016722 oxidoreductase activity acting on metal ions, GO:0009055 electron transfer
  activity, GO:0031240 external side of cell outer membrane, GO:0019645 anaerobic
  electron transport chain. Before adding GO:0019645, the participation test was
  applied: OmcA itself performs the terminal electron transfer (purified-protein
  assays), so the mutant phenotypes are read as corroboration of participation rather
  than as the sole argument.

## Relation to the CMMMech records

CMMMech cites UniProtKB:Q8EG33 in `data/records/{uranium,uraninite,chromium,vanadium,
silver,rhodochrosite,nontronite,montmorillonite,chlorite}.yaml` as "Outer-membrane
surface decaheme c-type cytochrome OmcA (SO_1779) partnering with MtrC in extracellular
metal/mineral reduction".

- The chromium and uraninite/uranium records (`supports: support`) are backed by
  OmcA-specific data: purified-protein Cr(VI) kinetics and an omcA deletion phenotype
  (PMID:21498755), and an omcA-dependent U(VI) reduction rate with colocalization of
  UO2 nanoparticles (PMID:16875436).
- The silver, vanadium, rhodochrosite, nontronite, montmorillonite and chlorite records
  mark `supports: partial` and state that individual cytochrome genes were not mutated
  in the cited studies. That is the correct level: this review found no OmcA-specific
  assay for Ag(I), V(V), or for the specific clay/carbonate minerals, only the general
  Mtr-pathway role. Anyone tightening those records should not upgrade them to
  `support` on the strength of this review.
- OmcA does not appear in the selenium record, which is consistent with the literature:
  selenite reduction in MR-1 is attributed mainly to the periplasmic FccA route.
- Nothing here supports an industrial-performance claim; all rates above are laboratory
  measurements on purified protein or washed cell suspensions.

## Not done

- `just fetch-fitness SHEON omcA` fails here (no local FEBA database, fit.genomics.lbl.gov
  unreachable), so no RB-TnSeq evidence was used.
- No GO-CAM model in `gocams/index.tsv` covers this protein.
