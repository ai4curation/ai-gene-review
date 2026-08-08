# PGM3 (human, O95394 / AGM1_HUMAN) review notes

## Identity and biochemistry

- HGNC:8907; gene symbol PGM3, synonym AGM1. Protein = Phosphoacetylglucosamine mutase (PAGM),
  a.k.a. N-acetylglucosamine-phosphate mutase, a.k.a. Phosphoglucomutase-3. 542 aa, isoform 1
  (O95394-1) is displayed; two additional splice isoforms (O95394-3, O95394-4).
- EC 5.4.2.3. Catalyzes the reversible interconversion GlcNAc-6-P <-> GlcNAc-1-P.
  [file:human/PGM3/PGM3-uniprot.txt "Catalyzes the conversion of GlcNAc-6-P into GlcNAc-1-P during"]
  [file:human/PGM3/PGM3-uniprot.txt Rhea:RHEA:23804; "N-acetyl-alpha-D-glucosamine 1-phosphate = N-acetyl-D-glucosamine 6-phosphate ... EC=5.4.2.3"]
- Mg2+-dependent; "Binds 1 Mg(2+) ion per subunit." [file:human/PGM3/PGM3-uniprot.txt]
  Mg2+-coordinating residues curated at 64 (via phosphate), 276, 278, 280; substrate-binding at
  370-372, 496-500, 505.
- Mechanism: alpha-D-phosphohexomutase superfamily; active site Ser64 forms a phospho-serine
  intermediate. Mio et al. showed Ser64Ala, His65Ala, Asp278Ala/Glu, Arg281Ala/Lys abolish
  activity; Arg496Ala raises Km for GlcNAc-6-P (substrate-binding role).
  [PMID:11004509 "demonstrating that Arg(496) serves as a binding" (site for N-acetylglucosamine-6-phosphate)]
- Belongs to the phosphohexose mutase family. [file:human/PGM3/PGM3-uniprot.txt "Belongs to the phosphohexose mutase family."]
- PATHWAY (UniProt): Nucleotide-sugar biosynthesis; UDP-N-acetyl-alpha-D-glucosamine biosynthesis;
  GlcNAc-1-P from alpha-D-glucosamine 6-phosphate (route I): step 2/2. (UniPathway UPA00113/UER00530.)
  So PGM3 is the second of two steps in "route I" and the penultimate step overall before UAP1 makes UDP-GlcNAc.

## Pathway context (hexosamine biosynthetic pathway, HBP)

Fru-6-P -> (GFPT1/2, GFAT) GlcN-6-P -> (GNPNAT1) GlcNAc-6-P -> (PGM3/AGM1) GlcNAc-1-P ->
(UAP1) UDP-GlcNAc. UDP-GlcNAc is the donor for N-/O-glycosylation, proteoglycans, GPI anchors,
glycolipids, and nucleocytoplasmic O-GlcNAcylation.
[PMID:24589341 "PGM3 is a member of the hexose phosphate mutase family and catalyzes the reversible conversion of GlcNAc-6-phosphate (GlcNAc-6-P) to GlcNAc-1-P"]
[PMID:24589341 "This is a key step in the synthesis of UDP-GlcNAc, which is critical for multiple glycosylation pathways including N- and O-linked"]

## Experimental support for function

- IDA (PMID:11004509): human AGM1 cloned, GST-fusion in E. coli displayed
  phosphoacetylglucosamine mutase activity; rescued yeast agm1-delta null.
  [PMID:11004509 "both HsAgm1 and CaAgm1 proteins displayed" (phosphoacetylglucosamine mutase activities)]
- IMP (PMID:24589341, full text): novel enzymatic assay of GlcNAc1-P formation from GlcNAc6-P;
  patient fibroblasts "All patients had substantially decreased PGM3 activity compared to control cells";
  "PGM3-deficient cells showed significant reduction of UDP-GlcNAc"; GlcNAc supplementation restored it.
  Downstream: "decreased O- and N-linked protein glycosylation in patients' cells" (abstract);
  full text quote fragment "along with decreased O- and N-linked protein".
- EXP (PMID:24698316, full text): "the catalytic activity is reduced in mutant PGM3" (20-30% residual,
  retained specificity). Cites mouse: "Pgm3-mediated UDP- GlcNAc synthesis is essential for hematopoiesis and development".
- EXP (PMID:24931394, abstract only): variants expressed in E. coli, "reduced PGM3 activity for all mutants tested".

## Localization

- Cytosol. Reactome R-HSA-446185: "Cytosolic PGM3 catalyzes the isomerization of N-acetyl-D-glucosamine 6-phosphate"
  (GlcNAc6P) to GlcNAc1P. Consistent with soluble cytosolic metabolic enzyme.

## Disease

- Immunodeficiency 23 (IMD23) / PGM3-CDG, MIM:615816, Orphanet 443811. Autosomal recessive, hypomorphic.
  [file:human/PGM3/PGM3-uniprot.txt DISEASE] Features: severe atopy, elevated IgE, recurrent bacterial/viral
  infections, T-/B-cell lymphopenia, autoimmunity, skeletal dysplasia (Desbuquois-like in some),
  neurocognitive impairment with hypomyelination. Complete Pgm3 loss embryonic-lethal in mice; hypomorphs viable.
  Curated IMD23 variants: L83S, D239H, N246S, D297E, E340del, Q451R, E501Q, D502Y (all decreased mutase activity).

## Curation decisions (summary)

- Core MF: phosphoacetylglucosamine mutase activity (GO:0004610). Verified via EBI OLS4 (not obsolete).
- Core MF (secondary): magnesium ion binding (GO:0000287) — cofactor, curated Mg2+ site.
- Core BP: UDP-N-acetylglucosamine biosynthetic process (GO:0006048). Location: cytosol (GO:0005829).
- ACCEPT: all GO:0004610 activity annotations (IBA/IEA/TAS/EXP/EXP/IMP/IDA), GO:0006048 (IBA/TAS/IEA/IMP),
  GO:0000287 (IEA), GO:0005829 (TAS).
- KEEP_AS_NON_CORE: GO:0030097 hemopoiesis (pleiotropic developmental process, indirect via UDP-GlcNAc);
  GO:0006487 N-linked and GO:0006493 O-linked glycosylation (downstream of precursor supply, not a direct
  activity of PGM3 on proteins).
- MARK_AS_OVER_ANNOTATED: GO:0005975 carbohydrate metabolic process (too general vs GO:0006048);
  GO:0016868 intramolecular phosphotransferase activity (parent of GO:0004610);
  GO:0006041 D-glucosamine metabolic process (broad NAS parent vs specific GO:0006048).
- No REMOVE actions used. No experimental annotation removed. No bare "protein binding" annotations present.

## Term id verification

Verified via EBI OLS4 API (2026-07): all of GO:0004610, GO:0000287, GO:0006048, GO:0005829, GO:0006041,
GO:0016868, GO:0005975, GO:0006487, GO:0006493, GO:0030097 resolve to the labels used and are not obsolete.
