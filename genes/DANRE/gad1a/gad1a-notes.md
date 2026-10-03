# gad1a notes (Danio rerio, glutamate decarboxylase 1a; UniProt A0A8M1RDR2)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not
attempted, per instructions. Literature searched by hand in Europe PMC (`gad1a AND zebrafish`,
`"gad1b" AND zebrafish AND (mutant OR knockout OR morphant OR crispr)`,
`TITLE:"glutamate decarboxylase" AND (zebrafish OR teleost OR fish)`, author searches for
VanLeuven/Lauderdale and Filippi) and by following ZFIN expression publications.
Pair material: `gad1a-bioinformatics/RESULTS.md` (protein, expression, synteny, probe identity);
paralog notes in `../gad1b/gad1b-notes.md`.

Accession A0A8M1RDR2 (TrEMBL, RefSeq XP_002663350, 591 aa), ZFIN:ZDB-GENE-070912-472, Ensembl
ENSDARG00000093411, chr9. 8 GOA rows, all IBA or IEA; no experimental annotation.

### Origin
- PANTHER TGD_tree (Neopterygii|Teleostei), 1:1, one gar co-ortholog; Ensembl Compara duplication
  node Clupeocephala; one gar GAD1 ortholog for both copies.
- Chromosomes: [PMID:30200754 "In zebrafish, gad1a is located on chromosome 9, gad1b on chromosome 6, and gad2 on chromosome 24 (VanLeuven,"]
- Other fish also have two gad1 genes: [PMID:30200754 "Other fish species have two gad1 genes, designated as gad1a and gad1b, and a single gad2 gene."]
- My synteny check: tlk1a/tlk1b and dync1i2a/dync1i2b flank both copies (RESULTS.md).
- Medaka: Ensembl lists a one-to-one medaka ortholog only for gad1a; PANTHER lists two medaka
  co-orthologs. Unresolved.

### Protein (RESULTS.md)
- 86.3% identical to gad1b; 80.0% to human GAD1 (gad1b 82.7%).
- PLP lysine (human K405), GABA-binding residues and C-terminus kept. Human phospho-S78 is T in
  gad1a. Relative rate vs gar not significant (37 vs 23 unique changes).
- Mammalian GAD1 background: [PMID:17384644 "GAD67 is constitutively active and is responsible for basal GABA production."]
  [PMID:1549570 "Both cDNAs direct the synthesis of enzymatically active GADs in bacterial expression systems."]
  [PMID:27461130 "While both GADs synthesize GABA and are co-expressed in most vertebrate GABAergic neurons, GAD1 synthesizes cytoplasmic GABA that is used for extrasynaptic and metabolic purposes and GAD2 regulates the vesicular pool for release"]
- No enzyme assay, antibody or tagged-protein data for Gad1a:
  [PMID:30200754 "Nevetheless, this cannot be directly tested at this time, because an antibody specific to Gad1a has yet to be identified."]

### Expression
- Public data (RESULTS.md): E-ERAD-475 whole embryo 0.4-4 TPM from segmentation to day 5 vs gad1b
  up to 84 TPM; Bgee: brain, liver, early embryo, blastula, gastrula, larva, head, bone (RNA-seq only).
- Single-cell RNA-seq of lateral-line efferent neurons:
  [PMID:41950195 "Efferent neurons showed robust expression of gad2 and gad1b (but not gad1a [Fig 4B]), encoding for enzymes required for the synthesis of GABA [35,36]."]
- Lueffe et al. compared both paralogs by in situ:
  [PMID:34650032 "Since the expression pattern of both GAD1 paralogs, gad1a and gad1b, are highly similar (Supplementary Fig. 3A–L), we decided for gad1a as GABAergic marker due to technical reasons."]
  Their probe: [PMID:35769333 "For two-color RNA ISH, a gad1a (previously gad67a) containing plasmid (Martin et al., 1998) was linearized"]
  **Caveat:** the sequenced Martin et al. GAD67 cDNA (AF017266) is gad1b by sequence (99.6% vs 90.9%
  protein identity; probe_identity.py). Another lab calls the old gad67a/gad67b probes gad1b:
  [PMID:26896392 "A mixture of two probes to gad1b (previously called gad67, probes used to be called gad67a and gad67b) and one probe to gad2 (previously called gad65) was used to label GABAergic cells [61, 62]."]
  So the "gad1a" in situ data of Lueffe et al., and ZFIN's curation of gad1a brain expression from
  them, may be gad1b signal. Not resolvable without the probe sequence.
- Other statements of similarity are secondary: [PMID:41097006 "Zebrafish possess two paralogs of Gad1, gad1a and gad1b, which exhibit similar expression patterns [31]."];
  [PMID:42466317 "Immunohistochemistry studies in several species have shown largely overlapping expression of gad1a and gad1b in the developing brain, including studies of the zebrafish brain at 4 dpf (Filippi et al., 2014)."]
  The cited Filippi et al. 2014 (PMID:24374659) used gad1b and gad2 probes, not gad1a, so the second
  statement is not supported by its source.
- Differential regulation (qPCR, which uses paralog-specific primers):
  [PMID:35769333 "In grm8a–/– animals a significant reduction of gad1a transcript level was detected, whereas gad1b and gad2 were unchanged (Supplementary Figure 5A)."]
  [PMID:34650032 "Motivated by our qPCR results, showing a significant reduction in the amount of gad1b transcript in foxp2+/− and a tendency to higher gad1a and gad2 transcript levels in foxp2+/− and foxp2−/− (Fig."]

### Function
- No gad1a mutant, morphant or assay. A gad1b translation-blocking MO has 19/25 matches to gad1a:
  [PMID:30200754 "MO used in our study has only 8 consecutive bases complementary to gad1a, so it seems unlikely that the gad1b translation blocking MO used here would also block translation of gad1a."]
  The authors predict that double nulls would show the craniofacial MO phenotype:
  [PMID:30200754 "If this is the case, we hypothesize that zebrafish embryos null for gad1a and gad1b will exhibit the craniofacially defective phenotype."]

### Annotation decisions
- MF rows (GAD activity IBA/IEA, carboxy-lyase, C-C lyase, PLP binding): ACCEPT; catalytic residues kept.
- GABA biosynthetic process (IBA): ACCEPT (the enzyme performs the step).
- Cytoplasm (IBA): ACCEPT. Presynaptic active zone (IBA): KEEP_AS_NON_CORE (rodent Gad1 donors; no
  Gad1a localization data).
- No NEW annotations: nothing gad1a-specific has been measured.
