# Zpr1 (Drosophila melanogaster, Q9W379, CG9060, FBgn0030096) - manual literature review

No deep-research provider was run for this gene (no API keys in this environment).
This file records the literature work done by hand from the cached publications in
`publications/` and PubMed searches ("Zpr1 AND Drosophila" returns a single paper,
PMID:23029159; "Zpr1 AND (eEF1A OR chaperone)" returns the ortholog literature below).

## Identity and family

- Q9W379 is a 457-aa protein encoded by Zpr1/CG9060 on the X chromosome. UniProt places it
  in the ZPR1 family, with two C4-type zinc fingers (residues 43-75 and 261-293) annotated
  by similarity to human ZPR1 (O75312), two ZPR1 A/B (jr) domains (Pfam PF22794) and two
  Zn_ribbon_ZPR1 domains (PF03367, NCBIfam TIGR00310), and PANTHER PTHR10876:SF0
  (ZINC FINGER PROTEIN ZPR1). Protein existence is at transcript level only (PE 2); no
  biochemical work has been done on the fly protein.
- ZPR1 genes are found across eukaryotes and archaea and are essential
  [PMID:36630955 "ZPR1 genes are found in organisms spanning the eukaryotic and archaeal domains of life where they perform an essential but poorly-defined role."].

## Drosophila experimental evidence (single paper)

Ruiz, Nikolova & Metzstein 2012 (PMID:23029159, full text cached):

- Allele 31ZZ, from a MARCM X-chromosome mosaic screen, is a nonsense mutation in exon 1
  [PMID:23029159 "This mutation results in a premature termination codon at amino acid position 58."].
  It is lethal and rescued by a genomic transgene and by terminal-cell UAS-cDNA expression.
- Phenotype in larval tracheal terminal cells: no gas-filled lumen (fully penetrant) and
  loss of tertiary and quaternary branches (variable)
  [PMID:23029159 "we find that 31ZZ mutants are able to generate a central branch and secondary branches, but fail to undergo tertiary and quaternary branching"].
- Lumen is initiated but does not mature; the lumen lacks cuticle and is occluded
  [PMID:23029159 "the conclusion from both our staining and EM analysis is that Zpr1-mutant terminal cells initiate lumen formation, but that progression to a mature, gas-filled lumen is blocked."].
- EGFR loss in terminal cells gives the same lumen defect at ~15% penetrance; EGFR
  overexpression gives extra lumens, and Zpr1 loss is epistatic to it
  [PMID:23029159 "We found that Zpr1 mutant cells that overexpress either the wild-type or the activated form of the EGFR lack gas-filled lumens, and appear essentially identical to Zpr1 mutant cells"].
- Zpr1 loss is likewise epistatic to activated FGFR (lambda-btl) overexpression
  [PMID:23029159 "indicating that Zpr1 is epistatic to FGFR overexpression in terminal cell lumen formation."].
  The authors did not test a Zpr1-Btl physical interaction
  [PMID:23029159 "interaction with the FGFR has not been directly tested."].
- Smn RNAi in trachea phenocopies the lumen defect (but not the branching defect).
- The authors themselves raise eEF1A as one possible mechanism
  [PMID:23029159 "Alternatively, Zpr1 is also known to interact with the eukaryotic translation elongation factor 1α (EF1α)"].

Interpretation: the fly data are tissue-level loss-of-function and epistasis. They show that
Zpr1 is required in terminal cells for lumen maturation and for fine branching. They do not
measure EGFR or FGFR pathway output (no dpERK or target-gene readout), do not show
physical binding to any receptor in the fly, and the Zpr1 phenotype is stronger and more
penetrant than that of EGFR loss. Because Zpr1 is a conserved essential chaperone for
eEF1A (below), a permissive (cell-capacity) requirement explains the epistasis equally
well as a dedicated signal-transduction role.

## Ortholog evidence for the molecular function

- Yeast Zpr1 is a dedicated ATP-independent chaperone for eEF1A
  [PMID:36630955 "Our work uncovers the long-sought-after function of Zpr1 as a bespoke chaperone tailored to the biogenesis of one of the most abundant proteins in the cell."];
  without it newly made eEF1A misfolds
  [PMID:36630955 "Zpr1 depletion causes acute proteotoxicity driven by biosynthesis of misfolded eukaryotic translation elongation factor 1A (eEF1A)."].
- The folding cycle uses client GTP hydrolysis and a co-chaperone, Aim29
  [PMID:37597513 "folding of eEF1A by Zpr1 requires GTP hydrolysis"].
- Mammalian and yeast ZPR1 bind eEF1A
  [PMID:9852145 "We report that ZPR1 binds to eukaryotic translation elongation factor-1α (eEF-1α)."].
- Mammalian ZPR1 binds the EGFR kinase domain via its zinc fingers and is released on
  receptor activation [PMID:8650580 "ZPR1 is a zinc finger protein that binds to the cytoplasmic tyrosine kinase domain of the epidermal growth factor receptor (EGFR)."].
- Mammalian ZPR1 is cytoplasmic in quiescent cells and moves to the nucleus/nucleolus
  with mitogens [PMID:9763455 "Here we demonstrate that ZPR1 accumulates in the nucleolus of proliferating cells."];
  it binds SMN and co-localises in gems and Cajal bodies
  [PMID:11283611 "Here we report that the SMN protein interacts with the zinc-finger protein ZPR1 and that these proteins colocalize in small subnuclear structures, including gems and Cajal bodies."].

## Annotation-relevant observations

- The fly ISS row "translation initiation factor binding" (GO:0031369) is transferred from
  the human IPI row (PMID:9852145, with P68104). P68104 is EEF1A1, a translation
  *elongation* factor, and PMID:9852145 is about eEF-1alpha; the term is wrong at source
  and should be GO:0061770 translation elongation factor binding.
- The fly ISS row "pre-mRNA catabolic process" (GO:1990261) is transferred from a human IMP
  row on PMID:11283611, whose abstract describes SMN localisation to nuclear bodies, not
  pre-mRNA degradation.
- The fly ISS row "cellular response to epidermal growth factor stimulus" rests on the
  mammalian EGF-induced nuclear redistribution of ZPR1; nothing comparable has been
  examined in Drosophila.
