# gtl-1 (G5ECM4, C. elegans) - manual literature review

No deep-research API was available for this gene, so this is a manual literature review built from
the cached publications in `publications/` and a PubMed search ("gtl-1 AND elegans", 12 hits, all
inspected). Quotations are taken from the cached text.

## Identity and family

- gtl-1 ("gon-2-like 1"; ORF C05C12.3; WBGene00001795; GeneID 178031; UniProt G5ECM4, unreviewed
  TrEMBL, 1694 aa) encodes one of three C. elegans TRPM (melastatin) channels, with GON-2 and GTL-2
  [PMID:17233618]. PANTHER places it in PTHR13800 (TRPM) subfamily SF10 "GTL-1". Pfam/InterPro: TRPM
  SLOG domain (PF18139), two TRPM-like N-terminal homology regions (PF25508), and five to six predicted
  TM helices (Phobius, residues ~1081-1233). The protein has no C-terminal kinase domain (unlike
  TRPM6/7).
- "GON-2 and GTL-1 share ~23% identity with TRPM1, TRPM3, TRPM6, and TRPM7" and "The homologous pore
  domains are nearly identical in GON-2 and GTL-1" [PMID:18299395].
- gtl-1 lies only 13 kb from its paralog gtl-2 [PMID:20221407].

## Channel activity

### In intestinal cells (loss-of-function electrophysiology)
- Xing et al. 2008 recorded whole-cell currents in cultured intestinal cells from wild type, gtl-1(ok375)
  (a deletion that "deletes all of the predicted transmembrane domains of GTL-1 and is almost certainly
  null"), gon-2(q388) and the double mutant [PMID:18299395].
  - "Loss of GTL-l and GON-2 function inhibits I(ORCa) approximately 70% and approximately 90%,
    respectively. I(ORCa) is undetectable in gon-2;gtl-1 double mutant cells" [PMID:18299395].
  - The current remaining in gon-2 mutants is defined as I(GTL-1): "We define the currents observed in
    gon-2 and gtl-1 mutant cells as IGTL-1 and IGON-2, respectively" [PMID:18299395].
  - Selectivity: "GON-2, GTL-1, and the ORCa channels exhibit a >60-fold selectivity for Ca2+ over Na+"
    and "The ORCa, GON-2, and GTL-1 channels clearly have measurable Mg2+ permeabilities under bi-ionic
    conditions" [PMID:18299395].
  - Conclusion: "These results indicate that (a) GON-2 and GTL-1 can function independently as ion
    channels" [PMID:18299395]; the authors "favor the hypothesis that the ORCa channel is formed by
    association of GON-2 and GTL-1 subunits", but heteromerization was not tested directly.
- Teramoto et al. 2005 (abstract only in cache) reported that GON-2 carries most of the outwardly
  rectifying current "while GTL-1 mainly contributes to appropriate Mg(2+) responsiveness of the
  outwardly rectifying current", and that "GTL-1 is continuously active while GON-2 is inactivated at
  higher Mg(2+) levels" [PMID:16054081]. Xing et al. 2008 disagree on the Mg2+ sensitivity point
  ("we found that IORCa, IGON-2, and IGTL-1 exhibit similar sensitivities to intracellular Mg2+").
- Regulation: GON-2/GTL-1 is inhibited by PI(4,5)P2 and activated downstream of PLCgamma; "GON-2/GTL-1
  functions as the major intestinal cell Ca(2+) influx pathway" [PMID:19923421, abstract only].

### In a heterologous system (direct)
- Cohen et al. 2020 expressed GTL-1 cDNA in HEK293 cells: "using excised patches we show that GTL-1 can
  be activated by internal calcium" and "Our results show GTL-1-dependent currents induced by
  activation of a Gαq-coupled Designer Receptor" [PMID:32009965]. "no currents are detected in the
  absence of CNO or in cells not expressing GTL-1" [PMID:32009965]. This shows GTL-1 forms a
  functional, Ca2+-activated channel on its own. Ion selectivity was not measured in HEK cells.

## Physiological roles

### Intestinal Mg2+ uptake and systemic Mg2+ homeostasis (strongest in vivo role)
- "Both GON-2 and GTL-1 are necessary for intestinal uptake of nickel" [PMID:16054081].
- gtl-1 single mutants "contain only approximately 0.4 times as much Mg2+ as wild type" [PMID:20221407,
  citing PMID:16054081]. "In the nematode, C. elegans, intestinal magnesium uptake is dependent on the
  activities of the TRPM channel proteins, GON-2 and GTL-1" [PMID:20221407].
- gtl-1 loss-of-function alleles were isolated as suppressors of gtl-2 (excretory Mg2+ excretion
  defect); "inactivation of gtl-1 suppresses the hypermagnesemic phenotype of gtl-2 mutants"
  [PMID:20221407]. Mg2+ supplementation suppresses the gtl-1(RNAi) growth defect [PMID:20221407].
- In cnnm-1; cnnm-3 Mg2+-efflux mutants, gtl-1 RNAi (described as encoding a "Mg2+-intake channel")
  reverses intestinal Mg2+ overload phenotypes (body size, ROS, lifespan) [PMID:38373693;
  PMID:32148064, abstracts only].
- Caveat: Xing et al. argued that a >10-fold Ca2+:Mg2+ permeability ratio makes significant Mg2+ uptake
  unlikely; Teramoto et al. 2010 rebut this with a flux calculation [PMID:20221407].

### Intestinal Ca2+ oscillations and defecation rhythm
- "GON-2 and GTL-1 are both required for maintaining rhythmic pBoc and intestinal Ca2+ oscillations"
  [PMID:18299395]. gtl-1 single mutants have increased pBoc period and variability; double mutants are
  more severe. Calcium oscillations are arrhythmic in gtl-1 intestines [PMID:18299395].
- PLCgamma(RNAi) in the double mutant does not worsen pBoc, whereas PLCbeta(RNAi) does, placing
  GON-2/GTL-1 with PLCgamma in IP3 receptor regulation [PMID:18299395].
- Combined RNAi of gon-2 and gtl-1 increases defecation cycle variability and interacts genetically with
  itr-1, flr-1 and kqt-3 [PMID:18495023].

### Neuronal roles (PVD nociceptor)
- PVD-specific knockdown shows "GTL-1 may amplify its signals" downstream of primary mechanosensors
  [PMID:22483941]. GTL-1 is required in PVD for behavioural responses to cold and contributes to the
  magnitude of the response to noxious mechanical stimuli [PMID:32009965]. Model: cytosolic Ca2+
  activates GTL-1 to amplify sensory signals.

### Systemic ion homeostasis and network excitability
- In acr-2(gf) convulsion mutants, "The compensatory effects of removing gtl-2 are counterbalanced by
  another TRPM channel, GTL-1" [PMID:21549603]; this is a downstream systemic-ion effect.

## Localization
- No GTL-1 protein localization (antibody or translational fusion) is reported in the cached
  literature. Transcriptional reporters show intestinal expression ("gon-2 and gtl-1 are both expressed
  in the intestine" [PMID:17233618]); PVD expression is inferred from PVD mRNA profiling and
  cell-specific knockdown [PMID:22483941; PMID:32009965]. Plasma-membrane activity follows from
  whole-cell currents in intestinal cells and from excised inside-out patch recordings of
  heterologously expressed GTL-1. Apical intestinal localization is a model, not an observation
  [PMID:20221407].
