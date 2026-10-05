# SMIM14 review notes

## Identity

SMIM14 (previous symbol C4orf34; UniProt Q96QK8, SIM14_HUMAN) is a 99-residue (10.7 kDa)
protein. UniProt topology (ECO:0000255): residues 1-49 lumenal, TM helix 50-70, 71-99
cytoplasmic; 78-99 disordered and proline-rich. Pfam PF11027 (DUF2615), PANTHER PTHR31019.
UniProt subcellular location "Endoplasmic reticulum membrane; Single-pass membrane protein"
is experimental (ECO:0000269, PMID:24499674). PE level 1.

## Literature search (2026-10-03)

PubMed `SMIM14[tiab] OR C4orf34[tiab]`: 4 hits. Only PMID:24499674 studies the protein.
The other three mention SMIM14 in gene lists (a hypertension/LV-remodelling expression
meta-analysis, an acral melanoma WGS study, a bovine papillomavirus E5 transcriptome);
none tests function. The task brief anticipated possible lipid/obesity or developmental
studies; none were found in PubMed under either symbol.

## PMID:24499674 (Jun et al. 2014, BMB Rep; full text cached)

- Expression: mouse orthologue transcript in all tissues tested: [PMID:24499674 "The mouse
  C4orf34 (mC4orf34) gene was ubiquitously expressed in mouse tissues including the heart,
  thymus and hippocampus (Fig. 1B)."]
- ER localisation of tagged human protein in HeLa/HEK293T: [PMID:24499674 "hC4orf34-EGFP
  was co-localized with endogenous calnexin (Fig. 2B), suggesting ER targeting of
  hC4orf34-EGFP."] and Sec61 co-localisation [PMID:24499674 "Human hC4orf34-3xFLAG was
  co-localized with Sec61-EGFP (Fig. 2B), further confirming the ER localization of
  hC4orf34-3xFLAG."]
- ER retention mapped to the TM domain (no canonical KKXX/RR motif): [PMID:24499674 "our
  results suggest that TMD of hC4orf34 might have an ER retention signal."]
- Topology by engineered glycosylation sites: N terminus lumenal: [PMID:24499674 "These
  results suggested that the N-terminus of hC4orf34 might be localized at the luminal side
  of the ER"]. Note: SMIM14 has no cleavable signal peptide, so an N-lumenal/C-cytosolic
  orientation from an internal anchor is what is sometimes called type III; the paper uses
  "type I". Either way, lumenal N terminus and cytosolic proline-rich C terminus.
- Function: only speculation (Ca2+ homeostasis, ER stress) in the abstract. The one
  functional test was negative: [PMID:24499674 "This result indicates that gene expression
  of hC4orf34 is not changed by ER stress (Fig. 4)."] No Ca2+ experiment was done.
- Caveat: the abstract says "highly conserved from invertebrate to mammalian cells", but
  the alignment for C4orf34 shows human, mouse, zebrafish and Xenopus only (the Aplysia
  sequence in Fig. 1A belongs to C4orf52). Vertebrate conservation is supported;
  invertebrate conservation is not shown for SMIM14.
- All localisation used overexpressed tagged constructs; no endogenous protein staining.

## Expression (HPA ENSG00000163683, JSON inspected 2026-10-03)

RNA tissue enhanced in liver; single-cell enhanced in hepatocytes, goblet cells and
oesophageal apical cells. No HPA immunofluorescence data.

## Interactions (all binary Y2H)

FATE1 (two screens: PMID:21516116 and HuRI PMID:32296183), SGTA, SLPI, TMEM42 (HuRI), SPRED1
(PMID:32814053). SGTA is a cytosolic chaperone for hydrophobic membrane-protein segments, a
classic pairing for a TM protein in Y2H; SLPI is secreted and topologically incompatible.
FATE1 is an ER/mitochondria-contact protein, which is compartment-compatible, and is the
only reproduced pair, but no functional study exists.

## Decisions

- 6 x protein binding: REMOVE.
- ER (IDA): ACCEPT. ER (IBA): ACCEPT. ER membrane (IEA): ACCEPT (most specific; core location).
- No MF/BP; no NEW.
