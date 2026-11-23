# Idh notes

- 2026-10-09: Initial review of Idh (B7Z0E0; FBgn0001248), NADP+-isocitrate dehydrogenase.
- Single fly gene encodes both compartments: "However, in Drosophila, a cytosolic isoform (IDHc) and
  mitochondrial isoforms (IDHm1 and IDHm2) are expressed from the single gene IDH" [PMID:28827794].
  B7Z0E0 starts MFALRRTAAMM... (mitochondrial presequence-like); UniProt entries Q8IQA7 and Q7KUB0
  lack it. All five UniProt isoforms end ...GALAKNAVAAK (no PTS1), so the peroxisome IBA/ISS rows
  (from human IDH1, which has a PTS1) were removed / marked over-annotated.
- Mutant phenotype: "IDHP flies successfully developed into adults (Fig 1C), but they showed decreased
  IDH mRNA expression, IDH enzyme activity, and NADPH/NADP+ ratio compared to wild type controls
  (Fig 1D–1F)." and "the survival rate of IDHP flies radically declined under rotenone treatments"
  [PMID:28827794].
- TCA cycle IBA (sole donor M. tuberculosis Icd) marked over-annotated: in animals the TCA step is
  NAD-IDH (Idh3 complex).
- NADP+ metabolic process -> NADPH regeneration (GO:0006740); same convention used for G6pd, Pgd,
  Men, Men-b in the cytosolic NADPH regeneration module.
- Mitochondrion rows (IBA/IDA/HDA) -> MODIFY to mitochondrial matrix (already IC) for consistency.
- Williamson 1980 (DOI:10.1016/0305-0491(80)90023-1, "Properties of Drosophila NADP+-isocitrate
  dehydrogenase purified on Procion Brilliant Blue-Sepharose-4B") not cached; accepted on trust.
- Falcon deep research (Idh-deep-research-falcon.md): adds Murari et al. 2022 [PMID:35544578], where Idh
  is called dIDH2/CG7176: "CG7176 (dIDH2) is the sole Drosophila ortholog of both IDH1 and IDH2";
  muscle knockdown raises NADP:NADPH ratio, impairs complex I assembly and triggers ferroptotic
  signals. Added to references and as support for the NADPH regeneration replacement. Also reports
  that ~13.5-16.4% of adult NADP-IDH activity fractionates with mitochondria (Williamson 1980 era data).
