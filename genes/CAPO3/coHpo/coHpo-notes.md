# coHpo (CAOG_01932) notes — Capsaspora owczarzaki Hippo/MST kinase

**Automated deep research was unavailable** for this gene (no deep-research provider
keys in this environment). These notes were compiled manually from cached full-text
publications in `publications/`; every claim carries inline provenance. No
`*-deep-research-*.md` file was created.

## Identity and choice of UniProt entry

- The gene targeted in the knockout study is CAOG_01932
  [PMID:38517944 "target the coHpo gene (CAOG_01932)"]. UniProt records the ORF as
  `CAOG_001932` (EMBL KE346361 / KJE90658.1 for the chosen entry).
- UniProt has three TrEMBL entries for this locus, all with ORF name CAOG_001932 on
  contig KE346361 (checked via UniProt REST, 2026-10-01):
  - **A0A0D2WLF3** — 430 aa; protein kinase domain (IPR000719) **plus** SARAH domain
    (IPR011524, IPR024205 Mst1/2 SARAH) and the p53-like tetramerisation superfamily
    (IPR036674) match that the SARAH helix hits. **Chosen entry.**
  - A0A0D2VKT0 — 466 aa; kinase domain only (no SARAH match).
  - A0A0D2X1E3 — 367 aa; kinase domain only (no SARAH match).
- These are alternative gene models / predicted isoforms. The primary paper says only
  one encodes the SARAH domain and used that one for the rescue transgene
  [PMID:38517944 "There are three predicted isoforms of the coHpo sequence, but only one of these encodes the SARAH domain, which is important for Hippo kinase activity in Hippo pathway signaling"].
  The paper does not give a UniProt/protein accession, so the mapping of "the SARAH
  isoform" to A0A0D2WLF3 is by domain content (the only one of the three with SARAH),
  not by an accession stated in the paper. Which models are actually expressed (RNA-seq
  support for each splice form) is unresolved.
- UniProt: "Belongs to the protein kinase superfamily. STE Ser/Thr protein kinase
  family. STE20 subfamily"; CDD cd06612 STKc_MST1_2 and cd21884 SARAH_MST_Hpo;
  PANTHER PTHR48012:SF2. Protein existence level 3 (inferred from homology).
- Hpo homologues are defined by a Ste20-like kinase domain plus a SARAH domain
  [PMID:22832104 "Our searches further identified homologues of Hpo, defined by the presence of a Ste20-like kinase domain and a SARAH domain"].

## Function in Capsaspora (PMID:38517944, Phillips & Pan 2024 eLife — primary)

- Knockout: both alleles had the kinase domain replaced by selectable markers
  [PMID:38517944 "homologous recombination was used to replace the kinase domain of both WT alleles with selectable markers"].
- coYki localization: in WT, mScarlet-coYki is mainly cytoplasmic; in mutants it is
  nuclear [PMID:38517944 "In contrast, the majority of coHpo-/- and coWts-/- cells showed nuclear levels of mScarlet-coYki greater than or equal to that seen in the cytoplasm"].
  coWts-/- has a stronger effect than coHpo-/-
  [PMID:38517944 "Interestingly, we found that coWts-/- cells were significantly more likely to show nuclear mScarlet-coYki localization than coHpo-/- cells"].
  Authors conclude [PMID:38517944 "Together, these results show that the Capsaspora Hippo kinase cascade regulates coYki by cytoplasmic sequestration, indicating a premetazoan origin of this regulatory activity of the Hippo pathway."]
- No proliferation phenotype [PMID:38517944 "In adherent growth conditions, coWts-/- and coHpo-/- cells proliferated at similar rates as WT cells"];
  also no EdU difference in aggregates.
- Cell shape / contractile behaviour: elongated, spindle-shaped cells that contract;
  rescued by transgene [PMID:38517944 "The presence of elongated cells was rescued by transgenic expression of coHpo or coWts in the respective mutant"].
  Blebbistatin increases elongated cells in both WT and coHpo-/- (myosin-dependent
  contraction).
- Aggregates: size and circularity normal in coHpo-/-
  [PMID:38517944 "coHpo -/- aggregates showed similar size and circularity as WT aggregates"],
  but cell packing density is increased
  [PMID:38517944 "These results indicate that loss of the Hippo pathway kinases increases cell density within Capsaspora aggregates."];
  packing is actomyosin-dependent (blebbistatin, LatB decrease it in WT and mutant).
- Epistasis by phenocopy: coYki 4SA (non-phosphorylatable) phenocopies, and requires
  the TEAD-binding residue F123
  [PMID:38517944 "These results suggest that the phenotypes observed in coHpo and coWts mutants are due to coYki activation resulting from a loss of upstream kinase signaling."].
  True double-mutant epistasis was not possible
  [PMID:38517944 "Since techniques are currently unavailable to create double mutants in Capsaspora, we could not test this possibility through classic genetic epistasis."].
- RNA-seq: 1032 genes differentially expressed in coHpo-/-; 107-gene "core Hippo"
  overlap with coWts and coYki enriched for membrane proteins and laminin G domains.
- Not done: no in vitro kinase assay, no kinase-dead allele, no localization of coHpo
  protein, no demonstration that coHpo phosphorylates coWts in Capsaspora.

## Heterologous function in Drosophila (PMID:22832104, Sebé-Pedrós et al. 2012)

- Capsaspora Hpo cDNA was tested
  [PMID:22832104 "Capsaspora Hpo, Yki and Sd cDNAs were amplified by PCR and inserted into pUAST vector"].
- In S2R+ cells: [PMID:22832104 "expression of Co-Hpo induced phosphorylation of Co-Yki in S2R+ cells, and this phosphorylation was further enhanced by co-expression of Dm-Wts"];
  [PMID:22832104 "Interestingly, Co-Hpo also stimulated the phosphorylation of Dm-Wts and Dm-Yki, as revealed by phospho-specific antibodies against P-Dm-Wts-T1077 and P-Dm-Yki-S168, respectively"].
  Co-Hpo also suppressed Co-Sd/Co-Yki reporter activity.
- In vivo: [PMID:22832104 "Overexpression of Co-Hpo by the GMR-Gal4 driver (GMR>Co-Hpo) resulted in a small eye phenotype"];
  [PMID:22832104 "Thus, Co-Hpo not only possesses growth-suppressing activity but also functionally activates a signaling cascade leading to the phosphorylation of endogenous Yki in Drosophila."]
- This is overexpression in a heterologous system: it shows the protein *can* activate
  the animal cascade (consistent with an active Ser/Thr kinase targeting Wts T1077), not
  that it restricts growth in Capsaspora — indeed in Capsaspora it does not restrict
  proliferation (PMID:38517944). The phosphorylation readouts are cell-based; the
  kinase was not purified and assayed directly.

## SARAH domain and the tetramerization IEA

- GO:0051262 protein tetramerization comes from InterPro2GO on IPR036674 "p53-like
  tetramerisation domain superfamily" (a Gene3D/SUPERFAMILY fold class, Gene3D
  4.10.170.10), which the helical SARAH segment matches structurally. The SARAH-specific
  entries map differently (IPR011524 -> signal transduction; IPR024205 -> protein
  Ser/Thr kinase activity), checked via the InterPro API.
- MST1 SARAH forms an antiparallel homodimer and 1:1 heterodimers with RASSF/SAV
  SARAH domains [PMID:17517604 "The Mst1 SARAH structure forms a homodimer containing two helices per monomer."];
  [PMID:17517604 "identified an elongated, tight-binding interface with the Rassf5 SARAH domain and a 1:1 heterodimer formation."].
  Free Rassf5 SARAH forms tetramers but is converted to dimers by MST1 SARAH
  [PMID:17517604 "In cross-linking experiments, the major population of the free Rassf5 SARAH domain formed tetramers in solution. However, when the Mst1 SARAH domain was added, dimers were formed"].
  MST2 SARAH also homodimerizes (PMID:25004971).
- So the Hpo/MST SARAH domain mediates dimerization, not tetramerization; the IEA is a
  fold-level mapping artefact. No oligomerization data exist for coHpo itself.
- SARAH is retained in Capsaspora (and amoebozoans) but lost in most fungi
  [PMID:38729842 "the Hippo-like kinases in most fungal lineages do not contain a SARAH domain, which is known to mediate critical protein-protein interactions in animal Hippo signaling"].

## Track C (propagation audit) observations

- All 6 GOA rows are IEA (InterPro2GO, UniRule, TreeGrafter, combined). None carries an
  animal-specific multicellular process term; the only process terms are generic
  `signal transduction` (SARAH InterPro2GO) and the structural-fold-derived `protein
  tetramerization`. So for this protein the problem is under-specification and one
  fold artefact, not TAXON_CONSTRAINT_VIOLATION.
- GO:0035329 hippo signaling has no taxon constraint (QuickGO, 2026-10-01) and its
  definition (Hpo -> LATS -> YAP cytoplasmic retention) matches what was shown in
  Capsaspora. coHpo is the initiating kinase of that cascade, so it does the work of the
  process (participation test passes; comparators: Drosophila hpo, human STK3/STK4 carry
  the term).
- Downstream phenotypes (cell elongation/contraction, aggregate packing) are mediated by
  coYki transcriptional output; they are not proposed as coHpo process terms.
