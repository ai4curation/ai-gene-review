# lacS (P22498, BGAL_SACS2, SSO3019) - Saccharolobus solfataricus P2

## Provenance note

Automated deep-research providers (falcon, openai) were unavailable for this
review (API authentication failures). No `-deep-research-*.md` file exists. The
notes below come from manual literature research (NCBI E-utilities/PubMed
searches, cached abstracts/full texts under `publications/`), QuickGO queries and
the local PANTHER PAINT file `interpro/panther/PTHR10353/PTHR10353-paint.tsv`.
Much of the classic biochemistry was done on the enzyme from strain MT-4. The
UniProt entry P22498 merges the MT-4 sequence (PMID:2121622) and the P2 genome
sequence, so those data apply to this entry.

## Identity and structure

- GH1 (glycoside hydrolase family 1), clan GH-A, (beta/alpha)8 barrel; homotetramer
  [PMID:9299327 "The enzyme is a tetramer with subunit molecular mass at 60 kDa"].
- Cloned from strain MT-4; 489 aa; no homology to E. coli lacZ
  [PMID:2121622 "There appears to be no evident similarity between this and the
  Escherichia coli lacZ sequence, thus suggesting that the two enzymes have
  analogous function, but are not homologous."].
- Active site at centre of barrel top face; a tunnel likely binds oligosaccharides
  [PMID:9299327 "probably acts as the binding site for extended oligosaccharide substrates"].
- Retaining mechanism: Glu387 nucleophile, Glu206 acid/base
  [PMID:9860840 "Glu387, which acts as the nucleophile of the reaction, and Glu206,
  which acts as the general acid/base catalyst"]; [PMID:9010932 "The Glu387-->Gln mutant
  showed no detectable activity"].
- In vivo lysine N-epsilon-methylation affects thermal stability and aggregation (PMID:14660666).

## Activity / specificity (experimental)

- Purified as a thermostable beta-galactosidase [PMID:2105216 "A thermophilic and
  thermostable beta-galactosidase activity was purified to homogeneity from crude
  extracts of the archaebacterium Sulfolobus solfataricus"].
- Same protein is the beta-glucosidase, and beta-glucosides/beta-fucosides are the
  preferred substrates [PMID:16348503 "chromogenic beta-d-galactosides and
  beta-d-glucosides are hydrolyzed at a common active site and that beta-glucosides
  and beta-fucosides represent the preferred substrates"].
- Broad specificity, exo-acting at non-reducing end, hydrolyses beta-linked
  di/oligosaccharides including cello-oligosaccharides
  [PMID:8484908 "has broad specificity for beta-D-gluco-, fuco- and galacto-sides"];
  [PMID:8484908 "cellotetraose > cellotriose > cellobiose"];
  [PMID:8484908 "The cleavage occurred at the non-reducing end of the oligosaccharide"].
- Retaining GH1 enzymes also transglycosylate; LacS from P2 is used to make
  galacto-oligosaccharides from lactose in vitro (PMID:23411285). This is a
  biotechnological side reaction of the hydrolase mechanism, not a physiological
  transferase activity.
- Engineering of specificity (M439C, E432C, W433C) (PMID:11749955).

## Physiological role

- S. solfataricus grows on lactose; a deletion mutant (GthetaW) lacking lacS (and the
  flanking lacTr/SSO3017 putative MFS transporter and xylS) cannot grow on lactose;
  complementation requires both lacS and lacTr [PMID:12813089 "The presence of both
  lacS and lacTr was necessary to sustain growth on the specific sugar and hence to
  complement the mutation"]. LacS performs the hydrolytic step of lactose
  utilisation; lacTr is presumably needed for uptake.
- lacS expression is under a catabolite-repression-like transcriptional control
  together with malA and the alpha-amylase [PMID:10383958 "acts at the level of
  transcription to coordinate synthesis of three physically unlinked glycosyl
  hydrolases implicated in carbohydrate utilization"]; see also PMID:10430566,
  PMID:15342498.
- Intracellular enzyme (purified from crude cell extracts; no signal peptide in UniProt).
  Not used for a NEW CC annotation (no direct localisation experiment found).

## GOA review reasoning

- GO:0004565 beta-galactosidase (IEA EC): correct, ACCEPT.
- GO:0004553 hydrolase, O-glycosyl (IEA InterPro): true but general -> MODIFY to
  beta-glucosidase (GO:0008422), beta-galactosidase (GO:0004565), beta-D-fucosidase
  (GO:0033907; definition "hydrolysis of terminal non-reducing beta-D-fucose residues
  in beta-D-fucosides", verified in OLS).
- GO:0005975 carbohydrate metabolic process (IEA InterPro): MODIFY to GO:0005990
  lactose catabolic process (OLS-verified). Participation test: LacS catalyses the
  glycosidic bond hydrolysis step itself. Comparator: PAINT node PTN002570652
  (mammalian lactase LCT, P09848) carries GO:0005990 IBD - the hydrolase is the
  normal bearer of this term.
- GO:0008378 galactosyltransferase activity (IBA): OLS definition "Catalysis of the
  transfer of a galactosyl group to an acceptor molecule, typically another
  carbohydrate or a lipid." REMOVE.
  - PAINT (PTHR10353-paint.tsv): node PTN008498319 carries an IBD for GO:0008378
    seeded only by AT3G06510 (SFR2), plus a negated IRD for GO:0008422
    beta-glucosidase (i.e. PAINT asserts loss of beta-glucosidase at that node).
  - SFR2 is a plant chloroplast outer-envelope galactolipid:galactolipid
    galactosyltransferase that has lost hydrolase activity [PMID:25100720 "SFR2 has no
    detectable hydrolase activity, although its catalytic site is highly conserved with
    that of family 1 glycosyl hydrolases."]; [PMID:20798281 "SFR2 processively
    transfers galactosyl residues from the abundant monogalactolipid to different
    galactolipid acceptors"].
  - PANTHER HMM scoring places lacS and the other crenarchaeal/Pyrococcus GH1
    beta-galactosidases (P14288 bgaS, P50388 bglY, O52629) in subfamily
    PTHR10353:SF209 "GALACTOLIPID GALACTOSYLTRANSFERASE SFR2, CHLOROPLASTIC"
    (PTHR10353-entries.csv). QuickGO: of 58 GO:0008378 IBA rows citing
    PTN008498319, all are land plants/algae except lacS. Sister archaeal homologs
    bgaS and bglY instead receive GO:0008422 by TreeGrafter (GO_REF:0000118,
    PTN000039748).
  - LacS is a demonstrated hydrolase (beta-glucosidase/galactosidase); target-specific
    evidence contradicts the SFR2-specific neofunctionalisation (loss of hydrolysis,
    gain of transferase). Archaea have no plant galactolipid substrate pool.
  - Note: a negated beta-glucosidase IRD at the same node would, if propagated,
    contradict direct experimental evidence for lacS (PMID:16348503, PMID:8484908).
    No such NOT row currently appears in GOA for P22498.

## Archaea error-pattern candidate

PANTHER subfamily misassignment / IBD node over-reach: archaeal GH1 beta-glycosidases
sit in PTHR10353:SF209 (named after plant SFR2) and lacS inherits the plant SFR2
neofunctionalised galactolipid galactosyltransferase activity by IBA, while PAINT
simultaneously asserts loss of beta-glucosidase at that node.
