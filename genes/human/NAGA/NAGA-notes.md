# NAGA (alpha-N-acetylgalactosaminidase, UniProtKB:P17050) - review notes

Literature work for this review was done manually from the cached publications
and the UniProt record (no provider deep-research file was available when the
review was written).

## Biology

- NAGA encodes lysosomal alpha-N-acetylgalactosaminidase (alpha-NAGAL, EC 3.2.1.49),
  a glycoside hydrolase family 27 exoglycosidase that removes terminal
  alpha-linked N-acetylgalactosamine from glycopeptides and glycolipids
  [PMID:19683538 "alpha-N-acetylgalactosaminidase (alpha-NAGAL; E.C. 3.2.1.49) is a lysosomal
  exoglycosidase that cleaves terminal alpha-N-acetylgalactosamine residues from
  glycopeptides and glycolipids"].
- The enzyme was purified from human lung and its cDNA expressed with activity in COS-1
  cells [PMID:2174888 "the lysosomal glycohydrolase that cleaves alpha-N-acetylgalactosaminyl
  moieties from glycoconjugates"].
- It is a homodimer [PMID:19683538 "Human α-NAGAL is a homodimer with each monomer containing
  394 residues"].
- NAGA is paralogous to GLA (alpha-galactosidase A); the two proteins share a fold but
  differ in substrate specificity. NAGA has a weak, promiscuous alpha-galactosidase
  activity on synthetic substrates (KM for pNP-alpha-Gal ~20-fold higher than for
  pNP-alpha-GalNAc) [PMID:19683538 "The pNP-α-GalNAc substrate had a markedly lower KM (0.70 mM)
  compared to pNP-α-Gal (15.2 mM)."]. This is a side activity, not the physiological role.
- Physiological substrates include blood group A glycolipids: NAGA-deficient fibroblasts
  cannot degrade blood group A glycolipid A-6-2 [PMID:9741689 "Skin fibroblasts from patients
  with alpha-N-acetylgalactosaminidase deficiency (Schindler disease) cannot degrade the
  major blood group A glycolipid."], and O-linked/mucin-type glycopeptides (UniProt
  catalytic activity on blood group A and AB mucin glycoproteins).
- Location: lysosome (UniProt; PMID:9741689).

## Disease

Biallelic NAGA variants cause NAGA deficiency: Schindler disease type I (infantile
neuroaxonal dystrophy), Kanzaki disease (type II, adult angiokeratoma) and the
intermediate type III, with urinary excretion of glycopeptides and oligosaccharides
bearing alpha-GalNAc (UniProt DISEASE comments).

## Curation decisions

- Core MF: GO:0008456 alpha-N-acetylgalactosaminidase activity (IDA PMID:19683538).
- Core BPs: GO:0006516 glycoprotein catabolic process (glycopeptide/O-glycan substrates)
  and GO:0019377 glycolipid catabolic process (IMP PMID:9741689).
- Location: lysosomal lumen (soluble acid hydrolase).
- GO:0004557 alpha-galactosidase activity (IBA): side activity only -> non-core.
- GO:0005737 cytoplasm (IBA): uninformative for a soluble luminal hydrolase -> modify to
  lysosomal lumen.
