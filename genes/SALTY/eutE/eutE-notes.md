# eutE (P41793, Salmonella enterica serovar Typhimurium LT2) — curation notes

Reviewer: Claude (AI-assisted). Date: 2026-11-04.

## Provenance of this review

No `eutE-deep-research-*.md` file exists and deep-research providers were unavailable in
this session (no API keys), so **no deep research file was generated** and none is cited.
Sources used:

- `eutE-uniprot.txt` (UniProtKB P41793, reviewed) — CC FUNCTION, CATALYTIC ACTIVITY,
  BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT, SUBCELLULAR LOCATION, INDUCTION,
  DOMAIN, DISRUPTION PHENOTYPE, SIMILARITY, plus the DR family lines (PIRSF036410
  EutE_PduP, NCBIfam NF011927, InterPro IPR012408, PANTHER PTHR11699).
- Cached publications for the GOA PMIDs (3045078, 21803884, 27450681) and for the
  UniProt-cited eut literature fetched with `just fetch-pmids-from-file`: 7868611,
  2656649, 10464203, 16585748, 16272400, 23585538.
- `interpro/panther/PTHR11699/` (family review, `PTHR11699-paint.tsv`,
  `PTHR11699-entries.csv`) and `.cache/panther/panther-members-19.0.tsv` plus
  `.cache/panther/PTHR19.0_salmonella`, which both place P41793 in PTHR11699:SF68
  "ACETALDEHYDE DEHYDROGENASE (ACETYLATING) EUTE". UniProt's own DR line stops at the
  family (PTHR11699) with no subfamily.
- `just paint-losses SALTY eutE`: no IRD or IKR on this gene's lineage.

Literature search note: GOA's PMID set plus UniProt's citation list was the search
frontier; no online literature search tool was available, so nothing outside those cached
papers is asserted.

## Biology

EutE is the acetylating acetaldehyde dehydrogenase of the 17-gene *eut* operon, which lets
*Salmonella* use ethanolamine as a carbon, nitrogen and energy source when cobalamin is
available [PMID:3045078, "Ethanolamine can serve as the sole source of carbon and nitrogen
for Salmonella typhimurium if vitamin B12 is present to serve as a cofactor."]. The pathway
runs ethanolamine → acetaldehyde (EutBC, B12-dependent ethanolamine ammonia-lyase) →
acetyl-CoA (EutE), and the acetyl-CoA enters the glyoxylate bypass and TCA cycle
[PMID:16272400, "This report shows that Salmonella enterica catabolizes ethanolamine to
acetyl-CoA (Ac-CoA), which enters the glyoxylate bypass and tricarboxylic acid cycle for
the generation of energy and central metabolites."].

The key point for GO is that EutE is **CoA-acylating**: its product is acetyl-CoA, not
acetate. Purified SeEutE has both acetaldehyde dehydrogenase (68.07 ± 1.63 µmol/min/mg) and
the reverse acetyl-CoA reductase activity (49.23 ± 2.88 µmol/min/mg) [PMID:21803884], and
UniProt records the reaction as acetaldehyde + NAD+ + CoA = acetyl-CoA + NADH + H+ (EC
1.2.1.10, RHEA:23288) with a strong preference for NAD+ over NADP+ in both directions. This
is a different reaction from the non-acylating ALDH chemistry (aldehyde + NAD+ + H2O =
carboxylate) that the rest of PTHR11699 performs.

Genetics: *eutE* mutants cannot use ethanolamine as a carbon source and are impaired for
its use as a nitrogen source [PMID:7868611; PMID:2656649], and the gene product was
identified as the second enzyme of the pathway from the original genetic map
[PMID:3045078]. A non-polar *eutE* deletion releases increased acetaldehyde.

Localisation: EutE is inside the Eut bacterial microcompartment. Its first ~19-21 residues
are a signal sequence that targets cargo to the BMC interior through a hydrophobic
interaction with a helix of the shell protein EutS [PMID:27450681], and genetic analysis
places EutE, EutD and EutG in the lumen using private pools of CoA and NAD, with EutBC
outside injecting acetaldehyde in [PMID:23585538].

## Judgement calls recorded in the review

- **GO:0004029 (non-acylating ALDH activity), IBA from PTN000192666 → MODIFY to GO:0008774.**
  The node is sound for the family's classical branches but its reaction is not EutE's: EutE
  produces acetyl-CoA, and the PTHR11699 family review already states that the family holds
  "CoA-acylating EutE-type enzymes whose chemistry the term does not describe". This is a
  lateral correction, so the replacement (GO:0008774) is not a descendant of GO:0004029;
  GO:0008774 is already carried by this gene on EXP and IEA evidence, which is the term the
  row should have been.
- **GO:0006091 generation of precursor metabolites and energy, TAS → MODIFY to GO:0046336.**
  True (ethanolamine catabolism feeds acetyl-CoA into central metabolism) but uninformative,
  and not entailed by any more specific term in the review, so MODIFY rather than
  TOO_GENERAL. The replacement is the term the gene already carries by UniPathway mapping.
- **GO:0016491 oxidoreductase activity, IEA → TOO_GENERAL**, entailed by the accepted
  GO:0008774.
- **No `NEW` acetyl-CoA biosynthesis row.** EutE does catalyse acetyl-CoA formation, but the
  acylating-activity term already carries that chemistry and the pathway context is covered
  by ethanolamine catabolism; adding a biosynthesis process term would be redundant coverage
  rather than new information.

## PR #5970 review round (2026-11-04)

- Both GO:0031469 bacterial microcompartment rows (EXP PMID:27450681, IEA GO_REF:0000044)
  changed from ACCEPT to MODIFY → GO:0031471 ethanolamine degradation polyhedral organelle
  (is_a child of GO:0031469, checked in OLS), and core_functions.locations updated to match.
  This aligns with the E. coli EutB/EutC reviews in the same PR; EutE has the strongest
  direct evidence (EutE1-21 binding to the EutS shell protein). The lumen-versus-shell
  distinction stays as the existing suggested_question about a BMC lumen term.
