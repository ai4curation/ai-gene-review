# BEH2 (At4g36780; UniProt Q94A43) - manual literature synthesis

No deep-research API was available; this summary was compiled manually from cached
publications (`publications/PMID_*.md`) and PubMed searches ("BEH2 AND Arabidopsis"
returned 5 records, all reviewed here).

## Identity and family

- BEH2 = BES1/BZR1 homolog protein 2, 318 aa, one of six BZR1/BES1 family members
  (BZR1, BES1, BEH1-BEH4). UniProt: "Belongs to the BZR/LAT61 family." Pfam PF05687
  (BES1_N), InterPro IPR008540 (BES1_N) and IPR033264 (BZR); region 16..97 "Required for
  DNA-binding" is assigned by similarity (ECO:0000250) to BES1/BZR1.
- [PMID:37926922 "The BZR1/BES1 family is composed of BZR1, BES1, and four BES1/BZR1 homologs (BEH1-BEH4)."]

## Regulation by GSK3-like kinases (phosphorylation)

- Rozhon et al. 2010 (full text): ASKtheta (group III GSK3) was used as yeast two-hybrid
  bait and BEH2 was recovered [PMID:20128883 "Among the ASKθ-interacting clones, the full-length cDNA of the transcription factor BEH2 was isolated twice."]
- BIN2 also interacts in Y2H [PMID:20128883 "BIN2 interacted with BES1, BZR1 and BEH2."]
- Direct phosphorylation in vitro [PMID:20128883 "GST-ASKθ phosphorylated GST-BZR1, GST-BES1 and GST-BEH2, but not GST alone (Figure 5)."]
  and in protoplasts [PMID:20128883 "When ASKθ was co-expressed with BEH2, phosphorylated BEH2 accumulated in parallel with increasing quantities of ASKθ, whereas unphosphorylated BEH2 disappeared."],
  blocked by the GSK3 inhibitor bikinin.
- UniProt PTM: "Phosphorylated. Phosphorylation increases protein degradation." (ECO:0000269, PubMed:15680330, Yin et al. 2005; abstract-only in cache).
- UniProt MUTAGEN P222L (BEH2m, the bzr1-1D/bes1-D-equivalent proline): "increased stability of the protein and constitutive brassinosteroids response" (no evidence tag on the line; record cites PMID:15680330).
- Otani et al. 2022 (full text): BL shifts BEH2-GFP to the dephosphorylated form and brassinazole to the phosphorylated form (Supplementary Fig. 5).

## Subcellular localization

- CFP-BEH2 in tobacco leaves [PMID:20128883 "The fluorescence signals for the CFP-tagged transcription factors BES1, BZR1 and BEH2 were found in the nucleus."]
- BEH2-GFP in onion cells and Arabidopsis roots, independent of BR status [PMID:35695417 "Together, the results indicate that, unlike BZR1, BEH2 proteins are consistently localized in the nucleus and not modulated by a nuclear-cytoplasmic shuttling mechanism depending on BR levels."]
- Kim et al. 2024 (abstract only) [PMID:37926922 "Notably, BEH1 and BEH2 are predominantly localized in the nucleus, which induces the nuclear accumulation of other BZR1/BES1 family proteins through heterodimerization."]

## Transcriptional function and BR signalling

- Overexpression rescues bri1-5 and produces enhanced BR responses [PMID:37926922 "We found that all BZR1/BES1 family members restored the phenotypic defects of bri1-5 by their overexpression. Unexpectedly, BEH2-overexpressing plants showed the most distinct phenotype with enhanced BR responses."]
- RNA-seq: [PMID:37926922 "RNA-Seq analysis indicated that overexpression of both BZR1 and BEH2 regulates BR-responsive gene expression, but BEH2 has a much greater proportion of BR-independent gene expression than BZR1."]
- Otani 2022: BEH2 overexpression (6x) altered >=1131 genes; ~20-35% BR-regulated; GO enrichment of DEGs pointed to stress response and photosynthesis (overexpression-derived, indirect; not a basis for BP annotation).
- No direct DNA-binding assay (EMSA/ChIP) for BEH2 itself was found in the cached
  literature; DNA binding (BRRE/E-box) is inferred from the conserved BES1_N domain
  and family members BZR1/BES1 (e.g. PMID:15680330 shows BES1 binds E-boxes).

## BEH2 transcription is itself BR-repressed

- [PMID:35695417 "Altogether, these results suggest that BRs downregulate BEH2 transcriptionally, and that this regulation occurs in both shoots and roots."]; BES1 more than BZR1 mediates this.
- Expression: preferentially roots and leaf margins (PMID:35695417); family expression profiles in PMID:32508516.

## Genetics

- The bes1 bzr1 beh1 beh3 beh4 quintuple mutant (qui-1) is male sterile; BEH2 was not
  included because no valid T-DNA allele was found [PMID:31519953 "Genotypic analyses confirmed the true T-DNA insertions for BES1, BZR1, BEH1, BEH3, and BEH4, but not for BEH2."]
  So no loss-of-function phenotype is described for BEH2 in the cached literature.
