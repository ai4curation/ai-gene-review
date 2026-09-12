# Arc42 (Drosophila melanogaster) research notes

UniProt: Q9VDT1 (Q9VDT1_DROME, TrEMBL/unreviewed). Gene: Arc42; synonym dARC42; ORF CG4703;
FlyBase FBgn0038742; GeneID 42364; chromosome 3R. 405 aa, MW 43654.

## Identity / naming

- The name "Arc42" / "Activator-recruited cofactor subunit 42" is a historical FlyBase gene
  name and is a misnomer with respect to molecular function: the protein is in fact a
  mitochondrial short-chain acyl-CoA dehydrogenase (SCAD family), not a transcriptional
  Mediator/ARC subunit. The paper below explicitly lists the "Fly name" for Arc42 as
  "Activator-recruited cofactor subunit 42" while its "Closest human symbol" is ACADS
  [PMID:40519079 Table 1 "Arc42 / Activator-recruited cofactor subunit 42"; Table 4 "Arc42 /
  ACADS"].
- UniProt names it "Short-chain specific acyl-CoA dehydrogenase, mitochondrial" (RecName,
  ARBA), AltName "Butyryl-CoA dehydrogenase", EC 1.3.8.1
  [Arc42-uniprot.txt "RecName: Full=Short-chain specific acyl-CoA dehydrogenase, mitochondrial";
  "EC=1.3.8.1"; "AltName: Full=Butyryl-CoA dehydrogenase"].

## Human ortholog

- Human ortholog is ACADS (P16219; SCAD; short-chain specific acyl-CoA dehydrogenase; EC 1.3.8.1),
  a mitochondrial matrix flavoenzyme that catalyzes the first, FAD-dependent step of short-chain
  (C4-C6, optimum butyryl-CoA C4) fatty acid beta-oxidation, passing electrons to ETF (see
  genes/human/ACADS/ACADS-ai-review.yaml for full grounding).
- Drosophila has TWO predicted ACADS orthologs: Arc42 (CG4703) and CG4860. DIOPT predicts both;
  Arc42 has the higher score, and only Arc42 loss of function reproduces the SCAD-deficiency
  metabolite signature [PMID:40519079 "Two different fly genes were predicted by DIOPT to be
  orthologs of human ACADS: Arc42 and CG4860"; "Arc42 received a higher score, but both are
  annotated on FlyBase as orthologous to ACADS"].

## Domain architecture (UniProt / InterPro)

- Three acyl-CoA dehydrogenase family domains: N-terminal (Pfam PF02771, res 28-140),
  middle (PF02770, 144-239), C-terminal (PF00441, 253-399)
  [Arc42-uniprot.txt "DOMAIN 28..140 ... Acyl-CoA dehydrogenase/oxidase N-terminal"].
- CDD cd01158 SCAD_SBCAD (short-chain / short-branched-chain acyl-CoA dehydrogenase subfamily)
  [Arc42-uniprot.txt "CDD; cd01158; SCAD_SBCAD; 1."].
- FAD cofactor (flavoprotein) [Arc42-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692"].
- Belongs to the acyl-CoA dehydrogenase family [Arc42-uniprot.txt "Belongs to the acyl-CoA
  dehydrogenase family."].
- PE 1: Evidence at protein level (PeptideAtlas proteomics detection) [Arc42-uniprot.txt
  "PE   1: Evidence at protein level"].

## UniProt-curated (ARBA) function and catalytic activity

- FUNCTION: short-chain specific acyl-CoA dehydrogenase catalyzes the first step of mitochondrial
  fatty acid beta-oxidation, removing one hydrogen from C-2 and C-3 of straight-chain fatty
  acyl-CoA to form trans-2-enoyl-CoA; acts specifically on C4-C6 acyl-CoAs
  [Arc42-uniprot.txt "short-chain specific acyl-CoA dehydrogenase acts specifically on acyl-CoAs
  with saturated 4 to 6 carbons long primary chains"].
- Catalytic activities (Rhea): butanoyl-CoA (C4, RHEA:24004), pentanoyl-CoA (C5, RHEA:43456),
  hexanoyl-CoA (C6, RHEA:43464) + oxidized ETF -> (2E)-enoyl-CoA + reduced ETF; EC 1.3.8.1
  [Arc42-uniprot.txt "butanoyl-CoA + oxidized [electron-transfer flavoprotein] + H(+) =
  (2E)-butenoyl-CoA + reduced [electron-transfer flavoprotein]"].
- PATHWAY: Lipid metabolism; mitochondrial fatty acid beta-oxidation
  [Arc42-uniprot.txt "Lipid metabolism; mitochondrial fatty acid beta-oxidation."].

## Experimental evidence (primary literature)

PMID:40519079 (Geronazzo et al. 2025, G3 Bethesda; "Characterizing fatty acid oxidation genes in
Drosophila"; full text available):

- CRISPR-Cas9 frameshift knockout of Arc42 (8 bp deletion, exon 2, predicted loss of function)
  [PMID:40519079 Table 4 "Arc42 / ACADS / 8 bp deletion, predicted frameshift / Elevated C4
  acylcarnitine"].
- Homozygous Arc42 mutants show elevated C4 (butyrylcarnitine), the SCAD-deficiency signature,
  exacerbated by starvation [PMID:40519079 "C4 was elevated in the homozygous Arc42 mutant flies,
  and this elevation was exacerbated in the starved condition, as expected"].
- Interpreted as functional conservation of the ACADS/SCAD role
  [PMID:40519079 "Arc42 knockout flies exhibited the C4 elevation characteristic of humans and
  mice lacking functional SCAD, while CG4860 knockout flies did not"].
- Summary statement [PMID:40519079 "only Arc42 loss of function mirrors the acylcarnitine profile
  of ACADS loss of function"].
- This IMP evidence supports involvement in mitochondrial fatty acid beta-oxidation (the
  FlyBase IMP annotation GO:0033539 cites this PMID). C4 (butyryl/butanoyl) is the C4 short-chain
  substrate, so this in-vivo data specifically supports short-chain / butyrate-level FAO.

Note: the paper does NOT provide a direct in-vitro enzyme assay of purified Arc42 protein, nor a
direct localization experiment; the enzyme-activity and mitochondrial-matrix assignments for the
fly protein rest on ARBA/InterPro (IEA), phylogeny (IBA), and ISS transfer from the human/pig
ortholog (UniProtKB:P15651 = pig ACADS). The in-vivo metabolite phenotype (elevated C4) is fully
consistent with short-chain acyl-CoA dehydrogenase function.

## GOA annotations to review (Arc42-goa.tsv)

1. GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity — IBA (GO_REF:0000033) — enables
2. GO:0005739 mitochondrion — IBA — is_active_in
3. GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — IBA — involved_in
4. GO:0046359 butyrate catabolic process — IBA — involved_in
5. GO:0003995 acyl-CoA dehydrogenase activity — IEA (ARBA/InterPro, GO_REF:0000120) — enables
6. GO:0016627 oxidoreductase activity, acting on the CH-CH group of donors — IEA (InterPro) — enables
7. GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity — IEA (EC 1.3.8.1, GO_REF:0000003) — enables
8. GO:0050660 flavin adenine dinucleotide binding — IEA (InterPro) — enables
9. GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — IMP (PMID:40519079, FlyBase) — involved_in
10. GO:0003995 acyl-CoA dehydrogenase activity — ISS (UniProtKB:P15651 pig ACADS, GO_REF:0000024) — enables
11. GO:0005759 mitochondrial matrix — ISS (P15651) — located_in
12. GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — ISS (P15651) — involved_in

P15651 = pig (Sus scrofa) short-chain acyl-CoA dehydrogenase (SCAD), a well-characterized SCAD;
appropriate ISS source.

## Review reasoning summary

- Core MF: GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity (ACCEPT the IBA; the
  EC-based IEA duplicate ACCEPT; the parent GO:0003995 and intermediate GO:0016627 KEEP_AS_NON_CORE).
- Core BP: GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase (ACCEPT; strongest
  is the IMP from PMID:40519079, plus IBA + ISS). GO:0046359 butyrate catabolic process
  KEEP_AS_NON_CORE (substrate-specific restatement; C4/butyryl-CoA is the optimal short-chain
  substrate, consistent with the elevated-C4 phenotype).
- Core CC: GO:0005759 mitochondrial matrix (ACCEPT ISS). GO:0005739 mitochondrion IBA ACCEPT
  (parent, less specific).
- GO:0050660 FAD binding: ACCEPT (genuine flavoprotein cofactor).
- No bare "protein binding" annotations present in the fly GOA.
</content>
</invoke>
