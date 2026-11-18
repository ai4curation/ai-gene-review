# MVD (Candida albicans) review notes

## 2026-11-18 manual review

UniProt A0A1D8PC43 (MVD1_CANAL), CGD standard name MVD (CGD:CAL0000181620), ordered locus
CAALFM_C100070WA, ORF orf19.6105. PANTHER PTHR10977:SF3. No deep-research provider keys are
configured in this environment, so no provider deep-research file was generated; this review is
built from the UniProt record, the cached publications and the searches below.

### Literature searches (Europe PMC, 2026-11-18)

- `"Candida albicans" AND ERG19` (41 hits) and `"Candida albicans" AND "mevalonate diphosphate
  decarboxylase"` (29 hits): the only primary paper on the Candida gene is Dassanayake et al. 2002
  (PMID:12073030). The rest are reviews, transcriptomics and metabolic-engineering papers.
- `"Candida albicans" AND ("orf19.6105" OR "C1_00070W")`: no functional paper on this locus.
- A 2025 review of fungal lipid synthesis as an antifungal target (PMID:40221522) summarises
  the conditional shut-off data of Becker et al. 2010 (PMID:21135205) for this step. The
  Becker abstract does not name MVD1 and its full text and supplement were not available here
  (PMC returns metadata only), so the essentiality statement rests on the review's summary.
- Closest characterised fungal orthologs: S. cerevisiae ERG19/MVD1 (PMID:9244250,
  PMID:15169949) and A. oryzae AoErg19 (PMID:31156588).

### Evidence on the Candida gene

- Cloning, expression and complementation [PMID:12073030 "We have cloned the gene encoding MVD
  from Candida albicans, and report the first characterization of such a gene from an
  opportunistic fungal pathogen."]. The 362-residue ORF has a 51-bp intron and is single copy on
  chromosome 1. Expression depends on carbon source, growth phase and yeast versus hyphal form
  [PMID:12073030 "the level of MVD expression is affected by (1) the carbon source in the growth
  medium, (2) the growth phase, and (3) the growth form of the fungus (yeast-like or hyphal)"].
- Function was shown by complementing the S. cerevisiae erg19 temperature-sensitive allele
  [PMID:12073030 "A single copy of the C. albicans MVD gene, under the control of the NOP1
  promoter, was able fully to complement the erg19(ts) phenotype"]. The erg19(ts) strain is the
  Bergès lab allele (a Leu-to-Pro change) in an essential gene whose defect blocks mevalonate
  diphosphate decarboxylase and sterol synthesis [PMID:9244250 "the ERG19 gene, which was shown to
  be an essential gene for yeast, was disrupted"]. This is the basis of CGD's three IGI rows
  (GO:0004163, GO:0016126, GO:0019287, with SGD:S000005326). The cached record is abstract-only;
  the abstract does not report an in vitro enzyme assay of the Candida protein, although UniProt
  cites the paper (ECO:0000269) for the EC 4.1.1.33 reaction. The genetic rescue of an
  MVD-deficient yeast strain is direct evidence that the Candida protein supplies MVD activity.
- In vivo essentiality: the 2025 review states that MVD1, with ERG12, ERG8 and ERG20, is required
  for growth in a mouse infection model, from tetracycline-repressible conditional strains
  (PMID:40221522, citing PMID:21135205).
- Expression responds to antifungals: amphotericin B up-regulates MVD1 (ERG19) [PMID:15917516
  "These included the up-regulation of MVD1 ( ERG19 ) and the down-regulation of the ergosterol
  biosynthesis genes"]. UniProt also lists biofilm repression (PMID:19527170, PMID:22265407), not
  re-read here.
- Localization: no C. albicans data. UniProt's FUNCTION text says "The second module is carried
  out in the vacuole", a sentence shared with the S. cerevisiae and A. fumigatus entries. Neither
  cited Candida paper reports a localization (the 12073030 abstract shows only that the
  epitope-tagged protein is detectable by Western blot). In S. cerevisiae the GFP-tagged Mvd1 is
  scored cytoplasmic in the genome-wide collection (PMID:14562095, used by the yeast MVD1 review),
  and the PAINT cytosol seeds are mammalian MVD, which is cytosolic by fractionation and
  microscopy [PMID:14972328 "We found a cytosolic localization for both endogenous human mevalonate
  pyrophosphate decarboxylase"]. The only fungal report of a vacuolar MVD is the overexpressed
  DsRed fusion of A. oryzae AoErg19 [PMID:31156588 "Subcellular localization analysis showed that
  AoErg19 was located in the vacuole."]. The vacuole clause in UniProt is recorded as a suspected
  source defect (CHECK), as in the yeast MVD1 review.

### PANTHER / PAINT

- PTN000104601 carries GO:0004163, GO:0019287 and GO:0005829. In the PTHR10977 tree it spans 132
  of 138 leaves: every eukaryotic member (PTN000104602) plus Sulfolobus SSO2989. Outside it sit the
  bacterial MDDs, Chloroflexus and Halobacterium dmd. Candida MVD (leaf PTN002590612) descends
  through PTN000104602 > PTN000861730 > PTN000104603 > ... > PTN000861755 with S. cerevisiae MVD1.
- CGD:CAL0000181620 is itself a seed of the GO:0004163 and GO:0019287 IBDs; this is the expected
  sign that the target has its own experimental annotation, not circularity.
- `just paint-losses CANAL MVD`: no IRD or IKR on the lineage.

### Decisions

- Accept all GO:0004163, GO:0019287, GO:0016126, GO:0006696 and cytosol rows.
- GO:0008299 (InterPro IPR005935) accepted as a true pathway-level process.
- GO:0016831 carboxy-lyase activity (InterPro IPR005935) marked TOO_GENERAL: IPR005935 is the
  combined diphosphomevalonate/phosphomevalonate decarboxylase family, so this row's own evidence
  does not reach GO:0004163, but the specific activity is accepted on four other rows.
