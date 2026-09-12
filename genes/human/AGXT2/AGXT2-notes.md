# AGXT2 (human) — Gene Review Notes

UniProt: Q9BYV1 (AGT2_HUMAN). HGNC:14412. Gene ID 64902. 514 aa precursor;
41-aa N-terminal mitochondrial transit peptide (mature chain 42–514).

## Summary of function

AGXT2 = alanine--glyoxylate aminotransferase 2, mitochondrial. A **class-III
pyridoxal-5'-phosphate (PLP)-dependent aminotransferase** (Pfam PF00202
Aminotran_3; InterPro IPR005814), functioning as a **homotetramer**
[file:human/AGXT2/AGXT2-uniprot.txt "Homotetramer"]. It is a **multifunctional
aminotransferase with a broad substrate specificity**
[file:human/AGXT2/AGXT2-uniprot.txt "Multifunctional aminotransferase with a
broad substrate specificity"].

### Core reactions / MF
- **Alanine:glyoxylate transaminase, EC 2.6.1.44** — glyoxylate + L-alanine =
  glycine + pyruvate (RHEA:24248). This is the exact GOA MF term:
  **GO:0008453 L-alanine:glyoxylate transaminase activity**. IDA in humans
  (PMID:20018850, PMID:24586340), plus IBA/IEA/ISS. This is the enzyme's
  namesake activity and the anchor MF.
- **(R)-3-amino-2-methylpropanoate:pyruvate transaminase, EC 2.6.1.40**
  (GO:0047305) — D-β-aminoisobutyrate (D-BAIB) + pyruvate = 2-methyl-3-
  oxopropanoate + L-alanine. IDA PMID:24586340. AGXT2 is identical to
  "D-3-aminoisobutyrate-pyruvate aminotransferase"; BAIB is a pyrimidine
  catabolism end-product and a prototypic AGXT2 substrate. Metabolizes the D-
  (not L-) isomer.
- **β-alanine:pyruvate transaminase, EC 2.6.1.18** (GO:0016223) — by similarity
  to rat Q64565 (ISS/IEA).
- **Methylarginine transamination**: metabolizes NMMA, ADMA and SDMA (with
  pyruvate/glyoxylate as amino acceptor) to (dimethylguanidino)valerate isomers.
  This is the physiologically important "alternative pathway" for ADMA/SDMA
  clearance besides DDAH. PMID:20018850, PMID:23023372 (23023372 not cached).

### Cofactor
- **PLP** (pyridoxal 5'-phosphate); Schiff-base lysine at K350
  [file:human/AGXT2/AGXT2-uniprot.txt "N6-(pyridoxal phosphate)lysine"].
  GO:0030170 pyridoxal phosphate binding (IEA InterPro). Secondary/enabling
  cofactor-binding MF.

### BP
- **Glyoxylate catabolic process** GO:0009436 (IDA PMID:20018850) — glyoxylate
  detoxification via transamination to glycine.
- **Glycine biosynthetic process** GO:0006545 (IDA PMID:20018850) — the product
  side of the same reaction (UniProt DR uses the more specific
  GO:0019265 "glycine biosynthetic process, by transamination of glyoxylate").
- **L-alanine catabolic process** GO:0042853 (IDA PMID:20018850, IBA) — alanine
  is consumed as amino donor.
- **Positive regulation of nitric oxide biosynthetic process** GO:0045429 (IDA
  PMID:20018850) — by lowering ADMA (an endogenous NOS inhibitor), AGXT2
  overexpression protects endothelial NO production. This is a downstream/
  physiological effect of methylarginine metabolism, not a canonical signaling
  role; keep but not as the enzymatic core.

### CC
- **Mitochondrion** GO:0005739 / **mitochondrial matrix** GO:0005759. N-terminal
  41-aa transit peptide cleaved; mitochondrial localization shown by confocal/
  IF (PMID:20018850, PMID:24586340, PMID:31818439) and HTP mito proteome
  (PMID:34800366). Reactome places the reaction in mito matrix.

### Tissue / disease
- Expressed mainly in **kidney (proximal/convoluted tubule) and liver
  hepatocytes** at protein level (PMID:31818439).
- Common coding SNP rs37369 (p.Val140Ile) reduces activity and raises urinary
  BAIB (hyper-β-aminoisobutyric aciduria, MIM:210100, a benign trait) and plasma
  SDMA (PMID:24586340). AGXT2 variants are cardiovascular/renal MODIFIERS
  (blood pressure via ADMA/NO), NOT a classic monogenic hyperoxaluria gene.

## Curation notes / caveats
- Reactome R-HSA-904864 summary notes that most glyoxylate→glycine conversion
  in vivo occurs in the peroxisome (AGXT, EC 2.6.1.44 too), and "the
  physiological role of the AGXT2 reaction is unclear." So the glyoxylate/
  glycine BP terms are correct for the reaction AGXT2 catalyzes, but AGXT2's
  dominant physiological role is arguably methylarginine + BAIB metabolism.
  Still, the alanine:glyoxylate transaminase activity IS the defining,
  experimentally-measured MF.
- PMID:23023372 (Caplin et al., ATVB 2012 — methylarginines/NO/blood pressure)
  is NOT in the local publications cache; it is cited in UniProt as ECO:0000269.
  Not used as a supporting_text source here (no cached text to quote).
- All MF/CC/BP annotations are consistent with UniProt and each other; no
  contradictions. No REMOVEs warranted — the IEA/ISS terms (β-alanine:pyruvate,
  D-BAIB:pyruvate, amino acid transaminase, alanine:oxo-acid transaminase) are
  all legitimate members of AGXT2's documented broad substrate range.

## GOA MF term used for core_functions
**GO:0008453 — L-alanine:glyoxylate transaminase activity** (exactly as it
appears in the GOA TSV; EC 2.6.1.44).
