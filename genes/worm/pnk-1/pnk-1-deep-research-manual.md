# pnk-1 (C. elegans, H2KYP7) - manual literature research

No deep-research API was available for this session; this file records a manual
literature search (PubMed MCP query `(pnk-1 OR pantothenate kinase) AND
(Caenorhabditis elegans OR C. elegans)`, 6 hits, plus targeted searches on PANK4)
and reading of the cached publications.

## Identity

- Gene pnk-1, ORF C10G11.5, WormBase WBGene00004068, NCBI GeneID 172327.
  UniProt H2KYP7 (TrEMBL, 449 aa, isoform C10G11.5a); other TrEMBL entries for
  other isoforms: Q86NC9 (403 aa), H2KYP8 (392 aa).
- InterPro IPR004567 Type_II_PanK; NCBIfam TIGR00555 panK_eukar; Pfam PF03630
  Fumble; PANTHER PTHR12280:SF20.

## Function: pantothenate kinase, first step of CoA biosynthesis

- PNK-1 was identified as the homolog of human pantothenate kinase in an RNAi
  screen of mmBCFA metabolism genes [PMID:15340492 "PNK-1, human pantothenate
  kinase"]; pnk-1 RNAi lowered C17ISO / C15ISO levels and pnk-1 promoter-GFP was
  readily detectable in the gut, upregulated in elo-5(RNAi) and downregulated in
  lpd-1(RNAi) [PMID:15340492 "pnk-1Prom::GFP expression is upregulated by
  elo-5(RNAi) but downregulated by lpd-1(RNAi)"]. pnk-1 is a direct DAF-16 target
  (cited there to Lee et al. 2003).
- C. elegans has two PanK-family genes: pnk-1 (Fumble domain only) and pnk-4
  (PANK4-like kinase/phosphatase fusion) [PMID:42523442 "organisms with two PANK
  proteins add a PANK4-like kinase/phosphatase fusion (e.g. C. elegans)"].
  pnk-1 knockout is not viable and CoA partially rescues it [PMID:42523442 "It was
  previously described that the pnk-1 KO strain was not viable and CoA
  supplementation partially rescued the detrimental phenotype"], while pnk-4 KO
  worms are viable with unchanged CoA [PMID:42523442 "indicate that, analogous to
  human Pank4, pnk-4 does not function as a pantothenate kinase"]. The preprint
  calls both genes "orthologous to the human Pank4 gene", a family-level
  statement that does not speak to catalytic competence.
- Hypomorphic pnk-1(tm8231) and pnk-1 RNAi improve proteostasis via HLH-30/TFEB;
  CoA supplementation abolishes the benefit, consistent with PNK-1 acting through
  CoA supply [PMID:40304211 "Remarkably, external supplementation with 400 μM CoA
  negated the benefits of the pnk‐1 reduced expression"]. CoA levels were not
  directly measured in that study.
- No direct enzyme assay of recombinant PNK-1 has been published (searched).

## PANK4 pseudo-kinase context

- All active PANKs contain Glu138 and Arg207 (PANK3 numbering); amniote PANK4s
  carry Glu138Val/Arg207Trp and lack kinase activity, whereas plant and fungal
  PANK4s are active [PMID:30927326 "all active, characterized PANKs contain the
  key catalytic residues Glu138 and Arg207 (HsPANK3 numbering)"; "a catalytically
  deficient variant of the catalytically active PANK4 found in plants and
  fungi"].
- Own analysis (file:worm/pnk-1/pnk-1-bioinformatics/RESULTS.md): PNK-1 keeps
  Glu214/Arg281 at these positions and lacks the C-terminal phosphatase region;
  PNK-4 has Ala at the catalytic Glu position.

## Localization

- No experimental localization of PNK-1 protein. Mammalian PanK1beta and PanK3
  are cytosolic; PanK1alpha and human PANK2 have nuclear pools via isoform-specific
  N-terminal extensions [PMID:23152917 "Both human and mouse PanK1α proteins were
  nuclear"].
