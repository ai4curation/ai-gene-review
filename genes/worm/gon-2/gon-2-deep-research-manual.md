# gon-2 (Q93971, C. elegans) - manual literature review

No deep-research API was available for this gene, so this is a manual literature review. It draws on the
cached publications in `publications/` and on PubMed searches ("gon-2 elegans TRPM", 15 hits). All
quotations are taken from the cached text.

## Identity and family

- GON-2 (T01H8.5; UniProt Q93971, 2032 aa) is a TRPM-subfamily TRP channel. Its closest relatives are
  its nematode paralogs GTL-1 and GTL-2 and the vertebrate TRPM1/3/6/7 proteins. UniProt puts it in the
  "transient receptor (TC 1.A.4) family. LTrpC subfamily". It has an Ion_trans pore domain (PF00520) and
  TRPM N-terminal homology regions (PF25508, TRPM_SLOG). The six predicted TM helices start at residue
  ~1310.
- The cloning paper described the gene as follows: "This mRNA encodes a protein related to the TRP family of cation channels and has a high
  degree of similarity to several vertebrate genes, including melastatin" [PMID:11290424]. Northern
  analysis suggested that "gon-2 expression is not limited to gonadal tissues" [PMID:11290424].
- Lambie et al. 2015 describe gon-2, gtl-1 and gtl-2 as genes that "encode paralogous TRP cation channel
  proteins that are similar in sequence and function to human TRPM6 and TRPM7" [PMID:26606136].

## Channel activity (direct electrophysiology)

- In intestinal cells, GON-2 carries most of the outwardly rectifying current: "GON-2 is responsible for
  a large outwardly rectifying current of intestinal cells, and its activity is tightly regulated by
  intracellular Mg(2+) levels" [PMID:16054081, abstract only].
- Xing et al. 2008 used deletion and severe loss-of-function alleles. They found that "Loss of GTL-l and GON-2
  function inhibits I(ORCa) approximately 70% and approximately 90%, respectively. I(ORCa) is
  undetectable in gon-2;gtl-1 double mutant cells" [PMID:18299395]. Under bi-ionic conditions, "GON-2,
  GTL-1, and the ORCa channels exhibit a >60-fold selectivity for Ca2+ over Na+" [PMID:18299395], and
  "The ORCa, GON-2, and GTL-1 channels clearly have measurable Mg2+ permeabilities under bi-ionic
  conditions" [PMID:18299395]. The authors "favor the hypothesis that the ORCa channel is formed by
  association of GON-2 and GTL-1 subunits" [PMID:18299395]. Heteromerization has not been shown directly.
- Regulation: the channel is inhibited by PI(4,5)P2 (IC50 2.6 uM). PLCgamma hydrolysis of PIP2 activates it.
  "GON-2/GTL-1 functions as the major intestinal cell Ca(2+) influx pathway" [PMID:19923421, abstract
  only]. "the GON-2 channel is inhibited by intracellular Mg2+ levels above 1 mM, whereas GTL-1 is not
  inhibited even at 6 mM intracellular Mg2+" [PMID:26606136, summarizing PMID:16054081]. GON-2 is
  also "more sensitive than GTL-1 to inhibition by Ca2+" [PMID:26606136].

## Physiological roles

### Intestinal Mg2+/cation uptake (electrolyte homeostasis)
- "Both GON-2 and GTL-1 are necessary for intestinal uptake of nickel" [PMID:16054081].
- "GON-2 and GTL-1 are both expressed in the intestine and act semi-redundantly to mediate the uptake of
  Mg2+ from the gut lumen" [PMID:26606136]; "Mg2+ within the gut lumen is taken up by the intestinal
  cells through apically-localized channels composed of GTL-1 and/or GON-2 subunits" [PMID:20221407,
  citing Teramoto 2005].
- Caveat: Xing et al. "suggested that since GON-2 and GTL-1 are approximately an order of magnitude more
  permeable to Ca2+ than Mg2+, they are not likely to mediate significant levels of Mg2+ uptake in vivo"
  [PMID:20221407]. Teramoto et al. 2010 discuss this argument and answer it with a flux calculation.
- Mg2+ supplementation suppresses the growth defect of gon-2; gtl-1 double mutants. It also partially
  suppresses the gonadogenesis defect of gon-2 single mutants [PMID:20221407]. Mutations in the
  excretory-cell paralog gtl-2 cause hypermagnesemia and suppress gon-2(q388) [PMID:20221407].

### Intestinal Ca2+ oscillations and the defecation motor program
- "GON-2 and GTL-1 are both required for maintaining rhythmic pBoc and intestinal Ca2+ oscillations"
  [PMID:18299395]. Epistasis places them in the IP3 signaling pathway together with PLCgamma
  [PMID:18299395; PMID:19923421]. RNAi of gon-2 plus gtl-1 increases the variability of the defecation cycle
  [PMID:18495023].

### Gonadal precursor cell divisions
- In gon-2 mutants, "gonadogenesis is severely impaired; in some animals, none of the gonad progenitors
  undergo any postembryonic divisions". The primary defect is "a delay (sometimes a complete block) in
  the onset and continuation of gonadal divisions" [PMID:9383054, abstract only]. Cell fate specification
  appears normal.
- Suppressors fall into several groups. gem-4 (a copine) loss of function antagonizes GON-2 [PMID:14573470]. gem-1 gain of function
  (an SLC16-family transporter) bypasses even a gon-2 null and is proposed to act "in parallel to the GON-2 channel to promote
  cation uptake within the developing gonad" [PMID:19087963]. CATP-6 (P5B ATPase) acts upstream of GEM-1
  [PMID:24130856]. The current model is that GON-2 supplies Mg2+ (and possibly Ca2+) to the gonadal precursors, which
  the cell cycle needs. GON-2 is not part of the cell-cycle machinery.

### Behaviour
- GON-2 (with GTL-2) is required for rapid learned avoidance of Enterococcus faecalis, which is triggered by
  intestinal distension. Intestine-specific expression rescues this avoidance [PMID:34032213]. This is a downstream
  physiological phenotype.

## Localization
- No GON-2 protein localization has been reported (no antibody staining and no GON-2::GFP fusion in the
  cached literature). Plasma-membrane location rests on (i) its TRP channel topology (6 TM, pore loop)
  and (ii) the whole-cell patch-clamp currents in intestinal cells that depend on gon-2. Apical
  localization in the intestine is stated as a model [PMID:20221407], but no direct evidence was found.
