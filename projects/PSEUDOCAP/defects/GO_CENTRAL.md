# Source-record defects for GO_CENTRAL

117 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I596 involved_in GO:0042759 long-chain fatty acid biosynthetic process (IDA, PMID:9603946)
- **Field:** GO_ID
- **Change:** check GO:0042759 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0845/PA0845-ai-review.yaml`

The PTN004377481 ceramidase clade carries an IBD for GO:0042759 long-chain fatty acid biosynthetic process, seeded only by PA0845 (Q9I596) and M. tuberculosis neutral ceramidase (O06769). A ceramidase releases a free fatty acid by hydrolysing the ceramide N-acyl bond; it does not synthesise the fatty acid. The underlying IDA (PMID:9603946) shows hydrolysis (and reverse ceramide synthesis), not fatty-acid biosynthesis. The node term misdescribes the family. Suggested change: remove GO:0042759 from the node and the seeds, keeping GO:0046514 ceramide catabolic process. PROBABLE: the M. tuberculosis seed's basis was not read in full.

> Interestingly, the 70-kDa protein catalyzed a reversible reaction in which the N-acyl linkage of ceramide was either cleaved or synthesized.
> — PMID:9603946

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002162750
- **Subject:** UniProtKB:Q9I537
- **Change:** check GO:0055091 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0920/PA0920-ai-review.yaml`

The IBD of GO:0055091 phospholipid homeostasis at PTN002162750 rests on one seed, the PseudoCAP IDA of P. aeruginosa PA0920 (Q9I537) to PMID:26261323, a crystal-structure and in vitro substrate-recognition study of the A-PGS catalytic domain whose abstract describes no homeostasis assay (full text not read). PA0920's own process is A-PG biosynthesis. The node's leaves (about 26 in QuickGO, 2026-10-28) also include fungal ergosteryl-3beta-O-glycine synthases (ErgS; A. fumigatus Q4WB70, Y. lipolytica Q6C7J3), which aminoacylate a sterol rather than a phospholipid. Please withdraw the IBD, or replace it with a biosynthetic term on a node confined to aminoacyl-phosphatidylglycerol synthases.

> Both proteins reveal a continuous tunnel that allows the hydrophobic lipid substrate PG and the polar aminoacyl-tRNA substrate to access the catalytic site from opposite directions.
> — PMID:26261323

## 3. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000511949
- **Subject:** UniProtKB:Q9I4S0
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1054/PA1054-ai-review.yaml`

PTN000511949 (PTHR43373 root, MrpA family, 16 leaf IBAs in 15 taxa) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Its seeds are PseudoCAP IMP on P. aeruginosa PA1054 (PMID:16030218) and IMP on B. subtilis MrpA (PMID:20509166). Both are sound evidence that MrpA is needed for Mrp antiport, but no Mrp antiporter shows activity with MrpA alone, and antiport requires the hetero-oligomeric complex (PMID:20624916). contributes_to GO:0015385 is the right assertion for the family. Please also check the Sulfolobus SSO1021 leaf (named formate hydrogenlyase subunit HycC).

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 4. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002160376
- **Subject:** UniProtKB:Q9I4R9
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

PTN002160376 (PTHR34583 root, Mrp/Mnh/Pha subunit C family, 24 leaf IBAs in 19 taxa) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Its sole seed is a PseudoCAP IMP row on P. aeruginosa PA1055 (ShaC) from PMID:16030218. Its abstract reports a disruption of PA1054 (shaA) only and shows antiport for the whole six-gene cluster. Mrp antiport needs the hetero-oligomeric complex of all subunits (PMID:20624916), so the subunit-C family contributes to the activity: contributes_to GO:0015385 is the right assertion. Please also check whether the IBD should reach the MBH/MBX hydrogenase subunits TK2086 and TK1221, whose complexes are not stand-alone Na+/H+ antiporters. Possible experimental seeds are B. pseudofirmus MrpC site mutants (PMID:20624916), but that species is not a tree leaf.

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 5. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001865541
- **Subject:** UniProtKB:Q9I4R8
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

PTN001865541 (PTHR42703 Eubacteria node, MrpD clade, 16 leaf IBAs in 13 taxa) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Seeds: IMP on B. subtilis MrpD (PMID:20509166) and a PseudoCAP IMP on P. aeruginosa PA1056 (PMID:16030218), the latter resting on a PA1054 disruption and whole-cluster complementation, with no PA1056 mutant in the paper (full text checked). No Mrp antiporter shows activity with MrpD alone, and antiport requires the hetero-oligomeric complex, so contributes_to GO:0015385 is the right assertion for the clade.

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 6. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002160407
- **Subject:** UniProtKB:Q9I4R7
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

PTN002160407 (PTHR34584 root, Mrp/Mnh/Pha subunit E family, 20 leaf IBAs in 17 taxa) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Its sole seed is a PseudoCAP IMP row on P. aeruginosa PA1057 (ShaE) from PMID:16030218. Its abstract reports a disruption of PA1054 (shaA) only and shows antiport for the whole six-gene cluster. MrpE is an accessory subunit required for complex formation (PMID:20624916) and is reported dispensable for transport in B. subtilis, so contributes_to GO:0015385 is the right assertion for the family. Please also check whether the IBD should reach the MBH/MBX hydrogenase subunits TK2080 and TK1226.

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

> However, in B. subtilis, it was reported that MrpE is dispensable for ion transport activity
> — PMID:29218041

## 7. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002162906
- **Subject:** UniProtKB:Q9I4R6
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

PTN002162906 (PTHR34702 root, Mrp/Mnh/Pha subunit F family, 19 GO_Central leaf IBAs in 16 taxa, plus TreeGrafter propagations) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Its sole seed is a PseudoCAP IMP row on P. aeruginosa PA1058 (ShaF) from PMID:16030218. Its abstract reports a disruption of PA1054 (shaA) only and shows antiport for the whole six-gene cluster. Mrp antiport requires the hetero-oligomeric complex (PMID:20624916), so contributes_to GO:0015385 is the right assertion for the family. Please also check whether the IBD should reach the MBH/MBX hydrogenase subunits TK2081 and TK1225, whose complexes are not stand-alone Na+/H+ antiporters.

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 8. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002162936
- **Subject:** UniProtKB:Q9I4R5
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

PTN002162936 (PTHR34703 root, Mrp/Mnh/Pha subunit G family, 19 GO_Central leaf IBAs in 16 taxa, plus TreeGrafter propagations) carries an IBD of GO:0015385 sodium:proton antiporter activity with qualifier enables. Its sole seed is a PseudoCAP IMP row on P. aeruginosa PA1059 (ShaG) from PMID:16030218. Its abstract reports a disruption of PA1054 (shaA) only and shows antiport for the whole six-gene cluster. Mrp antiport requires the hetero-oligomeric complex (PMID:20624916), so contributes_to GO:0015385 is the right assertion for the family. Please also check whether the IBD should reach the MBH/MBX hydrogenase subunits TK2082 and TK1224, whose complexes are not stand-alone Na+/H+ antiporters.

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 9. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000770175
- **Subject:** UniProtKB:Q9I487
- **Change:** check GO:0015184 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA1257/PA1257-ai-review.yaml`

The IBDs for GO:0015184 L-cystine transmembrane transporter activity and GO:0015811 L-cystine transport at PTN000770175 rest on E. coli TcyL alone and propagate to P. aeruginosa PA1257 (Q9I487). PA1257 is the permease of the PA1256-PA1257-PA1260 ABC system, which Johnson et al. 2008 (PMID:18833300) found necessary for growth on hydroxy-L-proline and induced by it. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05 and confirms that the node spans permeases of different specificity. PTN000770175 is a SPECIATION node (Proteobacteria) with 18 leaves, all PTHR30614:SF0. Its children are three single-organism leaves (H. pylori HP_0939, N. meningitidis NMB0788, G. sulfurreducens GSU0799), a Bradyrhizobium DUPLICATION (PTN002826367, 2 leaves) and a Gammaproteobacteria SPECIATION clade (PTN000770168, 13 leaves). That clade is itself heterogeneous: two HORIZ_TRANSFER subtrees (PTN008625440, 4 leaves, carrying B. subtilis TcyB and B. cereus BC_0873 cystine permeases plus H. influenzae HI_1079; PTN008625441, 2 leaves, B. subtilis YxeN and V. cholerae VC_0009), a Pseudomonas-specific DUPLICATION (PTN002413080, 3 leaves: PA1257, PA1258 and PA0313, the latter annotated as the YecS L-cysteine system permease), and an Enterobacteriaceae SPECIATION clade (PTN002024099, 4 leaves). Every cystine/YecS-named enterobacterial member - the seed TcyL (P0AFT2), Salmonella YecS (Q7CQB5) and STM1636 (Q8ZPA0), Yersinia YecS (A0A380PDF6) - falls inside PTN002024099: `--contains P0AFT2,Q7CQB5,A0A380PDF6,Q8ZPA0` returns exactly that node. The cystine-specific support therefore stops at PTN002024099, while PA1257 sits two duplication events away in a clade whose members include the hydroxyproline permeases. Please move both cystine IBDs down to PTN002024099 and, if a term is wanted at PTN000770175, use the broader GO:0015424 ABC-type amino acid transporter activity (with GO:0006865 amino acid transport for the process), which the mixed composition of the node does support. This defect covers the GO:0015811 row as well.

> Knockouts in these genes affected growth on hydroxy-L-proline as a carbon source, and expression of all three genes was induced by hydroxy-L-proline (Table 2 and 3).
> — PMID:18833300

## 10. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000764525
- **Subject:** UniProtKB:Q9I404
- **Change:** check GO:0006868 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA1340/PA1340-ai-review.yaml`

The IBD of GO:0006868 L-glutamine transport at PTN000764525 has one seed, the PseudoCAP IMP of P. aeruginosa PA1340 to PMID:18310026. That paper characterises the P. putida KT2440 AatJMQP system using mutants of the binding protein (aatJ) and ATPase (aatP); it reports high-affinity Glu/Asp binding and uptake and only weak Gln binding, and its abstract reports no test of PA1340 or of any GltK-type permease (full text not read). The node is a GltK-type permease clade (E. coli, Salmonella and Yersinia GltK, Bradyrhizobium bll7598/blr3098, PA1340) of glutamate/aspartate importers, and the sister GltJ node PTN004745596 carries GO:0051938 L-glutamate import. Please replace the glutamine IBD by L-glutamate import (or rely on the GO:0006865 IBD at PTN000770157). About 6 leaf IBAs are affected.

> We describe an ATP-binding cassette (ABC) transporter in Pseudomonas putida KT2440 that mediates the uptake of glutamate and aspartate.
> — PMID:18310026

## 11. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001976860
- **Subject:** UniProtKB:Q9I3B1
- **Change:** delete the record asserting GO:0009927
- **Recorded in:** `genes/PSEAE/PA1611/PA1611-ai-review.yaml`

The GO:0009927 histidine phosphotransfer kinase activity IBD at PTN001976860 (seeds RcsD P39838 and SLN1 S000001409) propagates to hybrid sensor kinases that lack an Hpt domain, including PA1611 and PA3271. GO:0009927 describes the phospho-His intermediate (Hpt) between a hybrid kinase and a response regulator. PA1611 domain content (UniProt/InterPro, checked 2026-11-05) is HAMP, HisKA, HATPase_c and REC with no HPt (IPR008207) match, and it phosphorylates the separate Hpt protein HptB. Please remove the IBD from this node or restrict it to the RcsD-like subclade that carries an HPt domain. The node MF GO:0000155 and BP GO:0000160 are unaffected.

> PF00512; HisKA
> — file:PSEAE/PA1611/PA1611-uniprot.txt

> PF00072; Response_reg
> — file:PSEAE/PA1611/PA1611-uniprot.txt

> between the cytosolic part of PA1611 (a.a. 202–652) and HptB has been confirmed with
> — PMID:32939285

## 12. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002826263
- **Subject:** UniProtKB:Q9I238
- **Change:** check GO:0031408 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA2077/PA2077-ai-review.yaml`

The IBD of GO:0031408 oxylipin biosynthetic process at PTN002826263 has two seeds, P. aeruginosa PA2077 (10S-dioxygenase) and PA2078 (7,10-diol synthase), both PseudoCAP IMP from PMID:24980978 and both sound. The node term does not suit the clade: the seven leaves also include P. aeruginosa PA0007 (Q9I7B9) and PA1941 (Q9I2G3), Bradyrhizobium diazoefficiens blr7738 (Q89CQ8) and bll0021 (Q89YD3), and Rhodopirellula baltica RB5128 (Q7UGM5), none with any evidence of fatty acid oxygenation. The discoverers describe PA2077 and PA2078 as in-paralogs from a recent duplication with very low homology outside Pseudomonas orthologues (PMID:26154497), and the closest characterized relative, RoxA, is a rubber oxygenase. Please move the IBD to a node restricted to the PA2077/PA2078 clade, or remove it. Leaves were checked in the PAINT leaf file (2026-11-05); the paper's tree was not compared node by node with the PANTHER tree.

> PA2077 and PA2078 display very low homology to other proteins in the databases, except for those corresponding to their orthologues in other P.
> — PMID:26154497

## 13. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000764275
- **Subject:** UniProtKB:Q9I1Y8
- **Change:** check GO:0071453 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2127/PA2127-ai-review.yaml`

PTN000764275 (PTHR30083, 12 leaf IBAs in 5 taxa) carries an IBD of GO:0071453 cellular response to oxygen levels whose only two seeds are P. aeruginosa CgrA (PA2127, Q9I1Y8) and CgrC (PA2126, Q9I1Y9), both by PseudoCAP IEP to PMID:17890313 and PMID:20553552 (checked in .cache/paint/IBD.gaf and the GOA files). The IEP rows record that the cgr genes are induced by anaerobiosis through Anr, an expression response wired into one species' regulon, not a property inherited from the ancestor. Nothing shows that orthologs outside P. aeruginosa are oxygen-regulated or act in an oxygen response. Please withdraw the IBD, or reseed the node with an inheritable function (for example positive regulation of transcription, if supported for other members). The PA2126 review cross-references this defect.

> positively controlled by Anr and anaerobiosis
> — PMID:17890313

## 14. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN008682975
- **Subject:** UniProtKB:Q9I1J5
- **Change:** check PMID:22304305 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2280/PA2280-ai-review.yaml`

The IBD of GO:0016655 at PTN008682975 rests on one seed, the PseudoCAP IDA of PA2280 (Q9I1J5) to PMID:22304305, which characterises Synechocystis sp. PCC 6803 ArsH, not the P. aeruginosa protein. The term is nonetheless supported for PA2280 by PMID:26621870 (recombinant P. aeruginosa ArsH shows NAD(P)H quinone oxidoreductase activity). Please confirm the seed once PseudoCAP re-cites it; the IBD content need not change.

> Here we have expressed and purified Synechocystis ArsH and conducted an intensive biochemical study.
> — PMID:22304305

## 15. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002422332
- **Subject:** UniProtKB:Q9HXU3
- **Change:** delete the record asserting GO:0080164
- **Recorded in:** `genes/PSEAE/PA3697/PA3697-ai-review.yaml`

The GO:0080164 regulation of nitric oxide metabolic process IBD at PTN002422332 (MATCAP/DUF1704, QEGLA-motif proteins) has one seed, the PseudoCAP IMP on P. aeruginosa PA3697 to PMID:18043907. That paper reports only that PA3697 mutants lose nitrate- and nitrite-induced activity of the flavohemoglobin (fhp) promoter; NO metabolism was not measured and the mechanism is unknown. A reporter phenotype tied to the P. aeruginosa Fhp/FhpR system is not a family function. It is currently propagated to about 175 proteins, including many Legionella, planctomycete and myxobacterial proteins. Please withdraw the IBD.

> Both PA0779 and PA3697 were found to be essential for NO3(-) and NO2(-) induced Pfhp activity under aerobic and low-oxygen conditions
> — PMID:18043907

## 16. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000532509
- **Subject:** UniProtKB:Q9HXN5
- **Change:** check GO:0015764 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA3760/PA3760-ai-review.yaml`

The IBD of GO:0015764 N-acetylglucosamine transport at PTN000532509 has one seed, the PseudoCAP IMP on P. aeruginosa PA3760, and that seed is sound: PA3760 is the fused EIIA-HPr-EI of the PA3760/PA3761 GlcNAc PTS. The term does not hold across the clade, and three checks on the leaves show why, none of them resting on a protein name. (i) The sister leaf UniProtKB:Q9HY55 (P. aeruginosa PA3562, PTHR46244:SF6, the same subfamily as PA3760) is experimentally a fructose PTS protein, in the same organism and from the same paper that seeds this IBD: the PA3562 knockout fails to grow on D-fructose and the gene is fructose-induced (PMID:18833300). It nonetheless carries the GlcNAc IBA. (ii) Leaf UniProtKB:P08839 (E. coli PtsI), itself a seed of this node's GO:0008965 IBD, has GO:0008965 with evidence code EXP and a curated FUNCTION statement with ECO:0000269 experimental evidence that it is the general, non-sugar-specific component of the PTS; a protein experimentally shown not to be sugar-specific cannot inherit a sugar-specific process term. (iii) Domain content, not nomenclature, separates the fused leaves by sugar module: PA3760 carries a type-1 PTS EIIA domain (Pfam PF00358, PROSITE PS51093), whereas the four fused multiphosphoryl leaves (P77439, P32670, P45597, Q9HY55) all carry a type-2, fructose-class EIIA (Pfam PF00359, PROSITE PS51094, InterPro IPR004715 PTS_IIA_fruc), and P08839 and P37177 carry neither an EIIA nor an HPr domain. UniProtKB:P37177 further carries a GAF domain (Pfam PF01590) that PtsI lacks and has IDA annotations for GO:0008965 and GO:0006468, i.e. it is the nitrogen-PTS EI-Ntr rather than a sugar PTS enzyme. Please withdraw the IBD, or move it to a node confined to type-1-EIIA fused EIIA-HPr-EI proteins if the tree has one. This affects about 43 leaf IBAs. The "FruB"/"PtsA"/"FruI" sugar assignments implied by the leaf names are curated or, for Q9HY55, ARBA-predicted names and are not used as evidence here; the EIIA domain subtype and the PA3562 growth phenotype are.

> Knockouts in either PA3760 or PA3761 were defective in growth on N-acetylglucosamine as a sole carbon source, based on both Biolog and growth data
> — PMID:18833300

> Knockouts in either PA3560 or PA3562 were defective in growth on D-fructose as a sole carbon source, based on both Biolog and growth data
> — PMID:18833300

> The second cluster of PTS genes encodes a putative fused enzyme I/HPr/enzyme IIA and a putative enzyme IIBC. These two genes are located at the end of a putative operon encoding glucosamine utilization genes, suggesting N-acetylglucosamine as a potential substrate for the PTS transporter.
> — PMID:18833300

## 17. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001953445
- **Subject:** UniProtKB:Q9HXC2
- **Field:** With/From
- **Change:** check PANTHER:PTN001953445 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

The IBD for GO:0005886 plasma membrane at PTN001953445 (PTHR43117, about 31 leaf IBAs in 24 taxa) has one seed, P. aeruginosa PA3891 (Q9HXC2), through a PseudoCAP IDA to GO:0043190 citing PMID:17660277. That paper only shows that a PAO1 genomic clone carrying PA3891 complements an osmoprotection defect of a P. syringae opuCA mutant. It does not localise PA3891 or show the complex. The node term is biologically reasonable for ABC importer NBDs, but please re-seed it with an experimental localisation from a clade member, or record that it rests on family-level inference.

## 18. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001953060
- **Subject:** UniProtKB:Q9HXC2
- **Field:** With/From
- **Change:** check PANTHER:PTN001953060 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

The IBD for GO:0031459 ABC-type glycine betaine transporter activity at PTN001953060 (PTHR43117, about 23 leaf IBAs in 18 taxa) has one seed, P. aeruginosa PA3891 (Q9HXC2), through a PseudoCAP IDA citing PMID:17660277. In that paper PA3891 was only identified as a PAO1 genomic clone that restored growth of a P. syringae opuCA mutant on 0.5 M NaCl with betaine or choline. Uptake and specificity assays were done on the P. syringae DC3000 OpuC transporter (ATPase Q87WH5, PSPTO_4575). The node term is plausible for the clade. Please re-seed the IBD with Q87WH5 if it lies within PTN001953060, or with another experimentally characterised OpuC-type ATPase, so that the node does not rest on complementation evidence alone.

## 19. WRONG_STATEMENT (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000241400
- **Subject:** UniProtKB:Q9HWU0
- **Change:** revise "GO:0042286" (see explanation)
- **Recorded in:** `genes/PSEAE/PA4088/PA4088-ai-review.yaml`

The PAINT IBD of GO:0042286 at PTN000241400 is seeded by E. coli HemL and PA4088. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN000241400 is a SPECIATION node (Proteobacteria) with 15 leaves, all PTHR43713:SF3, 13 of them named hemL. Its children are three hemL leaves (H. pylori, N. meningitidis, G. sulfurreducens), a Bradyrhizobium DUPLICATION (PTN000241402, 2 leaves: blr6632, blr3552) and a Gammaproteobacteria SPECIATION clade (PTN000241405, 10 leaves). The earlier reading, that PA4088, PA5523, blr6632 and blr3552 form one divergent lineage, is not supported by the tree: PA4088 and PA5523 sit inside a Pseudomonas-specific DUPLICATION (PTN002463962, 3 leaves) whose third member is PAO1 HemL (P48247), and the smallest clade holding PA4088 and E. coli HemL is PTN000241405. There is therefore no HemL-only subclade to move the IBD to, and the node itself is the right home for the GSAM term. What the tree does show is a recent lineage-specific duplication in which one copy kept the hemL name and annotation while PA4088 and PA5523 diverged to about 27% identity and are named only "probable aminotransferase". Please record that divergence on the paralog branches instead: a NOT or loss at PTN002463963 (PA4088) and PTN002463964 (PA5523). PROBABLE rather than CONFIRMED because the topology settles where a correction belongs, not whether PA4088 has lost GSAM activity; the full text of PMID:29684343 (see the PSEUDOCAP defect on the EXP row) could still report an assay.

> | E. coli HemL vs PA4088 | 26.9 |
> — file:PSEAE/PA4088/PA4088-bioinformatics/RESULTS.md

> | E. coli HemL P23893 vs PAO1 HemL P48247 | 65.7 |
> — file:PSEAE/PA4088/PA4088-bioinformatics/RESULTS.md

## 20. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001297884
- **Subject:** UniProtKB:Q9HWK3
- **Change:** check GO:0006744 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4178/PA4178-ai-review.yaml`

PA4178 (Q9HWK3, EftM) receives the UbiE/COQ5 IBDs of PTN001297884 (GO:0006744 ubiquinone biosynthetic process, GO:0008425 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity). EftM is a characterised EF-Tu lysine 5 trimethyltransferase (full text of PMID:26677219 read). Either PA4178 is misplaced under the UbiE clade, or a NOT/loss annotation is needed on its branch. PROBABLE because the tree itself was not inspected.

> EftM is a thermolabile, SAM-dependent methyltransferase that directly trimethylates lysine 5 of EF-Tu in P. aeruginosa.
> — PMID:26677219

## 21. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000765601
- **Subject:** UniProtKB:Q9HVR8
- **Change:** check GO:0071916 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA4503/PA4503-ai-review.yaml`

The IBD of GO:0071916 dipeptide transmembrane transporter activity at PTN000765601 has one seed, the PseudoCAP row for PA4503 (DppB). The node's 25 leaves include E. coli NikB, whose experimental annotation is nickel transmembrane transporter activity, and E. coli SapB, whose experimental annotation is putrescine transmembrane transporter activity, plus nine Bradyrhizobium japonicum paralogs with unknown substrates. In binding protein-dependent OppBC permeases the substrate is set by the partner binding protein. Please move the dipeptide IBD to a node confined to DppB orthologs (if the tree has one) or rely on the GO:0022857 IBD at the parent PTN002455499. About 25 leaf IBAs are affected.

> The substrate specificity of ABC transporters is determined by its associated substrate-binding proteins (SBPs).
> — PMID:25338022

## 22. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766696
- **Subject:** UniProtKB:Q9HVR7
- **Change:** check GO:0071916 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA4504/PA4504-ai-review.yaml`

The IBD of GO:0071916 dipeptide transmembrane transporter activity at PTN000766696 has one seed, the PseudoCAP row for PA4504 (DppC). The node's 12 leaves include E. coli NikC, whose experimental annotation is nickel transmembrane transporter activity, and E. coli GsiD, whose experimental annotation is glutathione transmembrane transporter activity (glutathione is a tripeptide, not a dipeptide), plus the Salmonella GsiD ortholog. In binding protein-dependent OppBC permeases the substrate is set by the partner binding protein. Please move the dipeptide IBD to a node confined to DppC/DdpC orthologs (if the tree has one) or rely on the GO:0022857 IBD at the parent PTN000765620. About 12 leaf IBAs are affected.

> The substrate specificity of ABC transporters is determined by its associated substrate-binding proteins (SBPs).
> — PMID:25338022

## 23. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** PANTHER:PTN002214697
- **Subject:** UniProtKB:G3XD69
- **Field:** GO_ID
- **Change:** check GO:0046677 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4521/PA4521-ai-review.yaml`

The IBD of GO:0046677 response to antibiotic at PTN002214697 (PTHR38684 AmpE; 7 leaf IBAs in 7 taxa) has a single seed, a PseudoCAP IMP on P. aeruginosa PA4521 citing Langaee et al. 1998 (PMID:9835532), whose abstract reports cloning of ampDE and complementation by ampD only. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05 and does not support a clade-breadth objection, so that part of the earlier concern is withdrawn. PTN002214697 is a SPECIATION node of 7 leaves, all in subfamily PTHR38684:SF1 and all AmpE orthologs, one per organism, with a single internal speciation (PTN002214702, Enterobacteriaceae, 3 leaves) and no duplication anywhere below it; the node is exactly the gammaproteobacterial AmpE orthology group and both the PA4521 leaf (PTN002446049) and the E. coli AmpE leaf (PTN002214704) hang directly from it. The doubt is therefore entirely about the assertion, not its scope: whether AmpE is needed for beta-lactamase induction is contested (PMID:2607970 versus PMID:2691840), P. aeruginosa data suggest only an indirect role (PMID:16251318), and the E. coli leaf has no AmpR, so a broad phenotype term propagated from one unverified seed may be wrong for every leaf rather than for some of them. Reading the full text of PMID:9835532 to see whether an ampE mutant was assayed is what would settle this; topology cannot. Please check the seed and consider withdrawing this phenotype-level IBD; the plasma membrane IBD at the node is sound.

> The ampD product transcomplemented Escherichia coli ampD mutants to wild-type beta-lactamase expression.
> — PMID:9835532

## 24. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001279639
- **Subject:** UniProtKB:Q9HU50
- **Field:** GO_ID
- **Change:** check GO:0007165 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5134/PA5134-ai-review.yaml`

The PAINT IBD for signal transduction on PTN001279639 rests on three seeds. The PA5134 seed cites PMID:24928312, a Staphylococcus aureus CtpA paper (CONFIRMED wrong reference), so UniProtKB:Q9HU50 should be dropped from the WITH/FROM - not because a gene in its own WITH/FROM is circular, which it is not, but because that seed annotation is itself defective. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05 and confirms the scoping problem. PTN001279639 is a DUPLICATION node with 58 leaves spanning three subfamilies (PTHR32060:SF22 9, SF29 2, SF30 47) and exactly two children: PTN004918760 (SPECIATION, Eubacteria, 9 leaves, all SF22 - the Prc/tail-specific protease branch, holding P. aeruginosa Prc Q9HYY3 and, in PTN002078873, E. coli Prc/Tsp P23865) and PTN008644010 (SPECIATION, Eubacteria, 49 leaves, SF29+SF30 - the CtpA branch). The two sound seeds straddle that duplication: `--contains Q9HYY3,P23865` returns PTN000786025 (Gammaproteobacteria Prc, 8 leaves, SF22), while B. subtilis CtpB (O35002) is SF29 in the 2-leaf Bacillus clade PTN002078920 inside PTN008644010. PA5134 is SF30, in the Gammaproteobacteria clade PTN002078922 (6 leaves). The term is therefore asserted at the family root to cover two seeds in different subfamilies, and propagates to all 58 leaves, including the entire SF30 CtpA clade and E. coli Prc/Tsp, for which no signalling role is on record. Please move the term to the clades that support it: PTN000786025 (or PTN004918760) for the Prc lineage and PTN002078920 for CtpB, and remove it from PTN001279639.

## 25. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002194937
- **Subject:** UniProtKB:Q9HTY2
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5208/PA5208-ai-review.yaml`

The IBD of GO:0071978 bacterial-type flagellum-dependent swarming motility at PTN002194937 (PTHR36536, UPF0111/TIGR00153 PhoU-like proteins; 5 leaves, all confirmed in the PANTHER tree and all in PTHR36536:SF3) has a single seed, a PseudoCAP IMP on P. aeruginosa PA5208 from a transposon swarming screen (PMID:17158671) in which the mutant also grows more slowly. Two separate points, of which only the second is load-bearing. (1) The family's function is predicted, not known, so we do not assert what it does. All five leaves match Pfam PF01865 PhoU_div, NCBIfam TIGR00153 and InterPro IPR018445, whose own name is "putative phosphate transport regulator"; the leaf names that state a phosphate role are unvetted - "Pit accessory protein" on UniProtKB:Q83FC5 is a submitter SubName (ECO:0000313|EMBL) and "Phosphate transport regulator" on UniProtKB:Q9KPD1 is a ProtNLM machine-generated name (ECO:0008006), as is "TIGR00153 family protein" on PA5208 itself. What the domain content does establish is that no leaf carries a flagellar component or motor domain. None of the five leaves has any experimental annotation: GO:0071978 is the only GO process term any of them carries, in each case by IBA from this node. (2) The load-bearing claim is a taxon fact, and it holds. A UniProt proteome query (rest.uniprot.org, checked 2026-11-06) for the six core flagellar structural and motor genes fliF, flgB, flgE, flhA, fliC and motA returns zero hits in Haemophilus influenzae Rd KW20 (taxon 71421, 1704 entries) and zero in Coxiella burnetii RSA 493 (taxon 227377, 1812 entries), while returning all six in P. aeruginosa PAO1 (taxon 208964) and all six in Shewanella oneidensis MR-1 (taxon 211586), the flagellated leaves of the same node; both H. influenzae and C. burnetii are non-motile. A flagellum-dependent process term therefore cannot hold for leaves UniProtKB:P44271 (HI_1603) and UniProtKB:Q83FC5 (CBU_0015), and the node spans both flagellated and non-flagellated Gammaproteobacteria. Please withdraw this IBD.

> and a PA5208 mutant that had a slight growth defect
> — PMID:17158671

> InterPro; IPR018445; Put_Phosphate_transp_reg.
> — file:PSEAE/PA5208/PA5208-uniprot.txt

## 26. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002217427
- **Subject:** UniProtKB:Q9HTJ9
- **Change:** check GO:0043448 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5359/PA5359-ai-review.yaml`

PTN002217427 is the root of PTHR39335 (7 reference leaves in 5 organisms) and carries an IBD of GO:0043448 alkane catabolic process whose single seed is the PseudoCAP IMP row on P. aeruginosa PA5359 (UniProtKB:Q9HTJ9, PMID:14574114). The family consists of small signal-peptide-bearing lipoprotein-repeat proteins (Pfam PF03640, PIRSF029720): Streptomyces coelicolor SCO0930 and SCO7673, Gloeobacter violaceus glr0303, Bradyrhizobium diazoefficiens bll4220 and bll5559, Solanum lycopersicum Solyc00g055940.1, and PA5359. Alkane catabolism requires an alkane hydroxylase together with rubredoxin and rubredoxin reductase; no member of this family contributes such a component, and a tomato protein cannot inherit a bacterial alkane degradation role. 764 GOA rows now carry the term from this node, 757 of them by TreeGrafter. Please re-examine the IBD; the seed it rests on is also queried with PseudoCAP (see the IMP row of this review).

> Alkane catabolism needs an alkane hydroxylase, rubredoxin and rubredoxin reductase; nothing in this family supplies any of them
> — file:PSEAE/PA5359/PA5359-bioinformatics/RESULTS.md

## 27. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002466744
- **Subject:** UniProtKB:Q9HTI8
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

The IBD for GO:0005275 amine transmembrane transporter activity at PTN002466744 (PTHR43869, ProV/ChoV-type ABC ATPases, 14 leaf IBAs) is seeded by P. aeruginosa PA5376/CbcV (Q9HTI8, PseudoCAP IDA, PMID:19919675) and E. coli ProV (P14175, EcoCyc IDA, PMID:23249124). Both transport quaternary ammonium compounds (choline, glycine betaine, carnitine, proline betaine), which GO classifies under GO:0015651 and GO:0015418, not under amine transmembrane transporter activity. The IBD is therefore unsound on either seed. Please repoint it to GO:0015418 (or GO:0015651); because the node members are ATPase subunits, consider contributes_to. The parallel permease node PTN000766131 (PA5377/ProW) carries the same error.

## 28. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

The IBD for GO:0005275 amine transmembrane transporter activity at PTN000766131 (PTHR47737, ProW/ChoW-type permeases, about 13 leaf IBAs) is seeded by P. aeruginosa PA5377/CbcW (Q9HTI7, PseudoCAP IDA, PMID:19919675) and E. coli ProW (P14176). Both transport quaternary ammonium compounds (choline, glycine betaine, carnitine, proline betaine), which GO classifies under GO:0015651 and GO:0015418, not under amine transmembrane transporter activity. Please repoint the IBD to GO:0015418 (or GO:0015651). Because the node members are permease subunits, consider contributes_to.

## 29. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** check GO:0015226 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

The IBD for GO:0015226 carnitine transmembrane transporter activity at PTN000766131 (PTHR47737, about 13 leaf IBAs) rests only on P. aeruginosa PA5377/CbcW (Q9HTI7). In PMID:19919675, carnitine transport by CbcWV requires the separately encoded SBP CaiX (PA5388). The 98-100% identical P. syringae DC3000 Cbc core does not transport carnitine because DC3000 lacks caiX, and E. coli ProW, a co-seed of other IBDs at this node, is not a carnitine transporter. Substrate specificity is therefore not a property of the permease clade. Please remove this IBD, or replace it with GO:0015418 ABC-type quaternary ammonium compound transporting activity (contributes_to).

## 30. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** check GO:1902603 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

The IBD for GO:1902603 carnitine transmembrane transport at PTN000766131 (PTHR47737, about 13 leaf IBAs) rests only on P. aeruginosa PA5377/CbcW (Q9HTI7, PseudoCAP IDA, PMID:21478341). Carnitine uptake by Cbc requires the separately encoded SBP CaiX (PMID:19919675). The 98-100% identical P. syringae DC3000 Cbc core does not transport carnitine, and E. coli ProW, in the same node, is a glycine betaine/proline betaine permease. Carnitine transport is therefore not a clade-wide property of these permeases. Please consider removing the IBD (keeping GO:0031460 and GO:0015871 if desired).

## 31. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002288302
- **Subject:** UniProtKB:Q9HTB5
- **Field:** With/From
- **Change:** check PANTHER:PTN002288302 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5455/PA5455-ai-review.yaml`

The PAINT IBD of GO:0016757 glycosyltransferase activity on PTN002288302 (57 leaf IBAs, 43 taxa) has exactly two seeds, UniProtKB:Q9HTB5 (PA5455) and UniProtKB:Q9HTB4 (PA5456). Both seeds are PseudoCAP IDA rows from PMID:23341552, whose full text contains no glycosyltransferase assay: the genes were called putative glycosyltransferases from sequence and studied only by deletion, complementation and overexpression. The IBD therefore has no experimental basis. The term is very probably true for the clade (GT4 Glyco_trans_1_4 domain in both seeds), so the requested check is to re-seed the node from an experimentally characterised member, or to withdraw the IBD and leave the activity to domain-based IEA. Recorded once here; PA5456 cross-references it.

> Gene sequence analysis indicated that pa5455 and pa5456 encode putative glycosyltransferases.
> — PMID:23341552

## 32. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000546715
- **Subject:** UniProtKB:Q9HTB2
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0000271
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5458/PA5458-ai-review.yaml`

The PAINT IBD of GO:0000271 polysaccharide biosynthetic process at PTN000546715 (PTHR23028, acyltransferase-3) has a single seed, the PseudoCAP rows for P. aeruginosa PA5458 (Q9HTB2; GO:0009103 IMP and GO:0009243 IDA, PMID:23341552). They record that a deletion alters the structure of the CPA O antigen, which is still made: a modification of an existing polymer, not its synthesis. The node propagates 113 leaf IBAs, 109 of them to eukaryotic proteins (97 nematode, 9 oomycete, plus fungus, diatom and plant proteins). Nothing is known of a polysaccharide role for these proteins, and a plant subclade already carries a NOT IRD (PTN004595801). Please consider withdrawing this IBD. The node's GO:0016020 membrane IBD (seeded by WB:WBGene00044617) is unaffected.

> So 109 of the 113 leaf IBAs are in eukaryotes, 97 of them nematode proteins.
> — file:PSEAE/PA5458/PA5458-bioinformatics/RESULTS.md

> Mutation of the putative acetyltransferase-encoding gene pa5458 did not abrogate polysaccharide production
> — PMID:23341552

## 33. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000546841
- **Subject:** UniProtKB:Q9HTB2
- **Field:** GO_ID
- **Change:** check GO:0009103 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5458/PA5458-ai-review.yaml`

The PAINT IBD of GO:0009103 lipopolysaccharide biosynthetic process at PTN000546841 (PTHR23028, acyltransferase-3; 31 leaf IBAs in 16 taxa) has a single seed, the PseudoCAP IMP row for P. aeruginosa PA5458 (Q9HTB2, PMID:23341552). In that study a deletion mutant made a structurally altered CPA O antigen. The clade also contains peptidoglycan O-acetyltransferases of Gram-positive bacteria, S. aureus OatA (Q2FV54, PMID:15661003) and L. monocytogenes OatA (Q8Y7I6), together with S. pneumoniae spr1868, B. subtilis YrhL, B. cereus, five M. tuberculosis and four S. coelicolor proteins: 15 of 31 leaves are in organisms that make no LPS. Please either withdraw the IBD or move it to a Gram-negative O-antigen subclade (PA5458, Salmonella OafA Q8ZNJ3), if one exists. A process term covering cell-surface glycan modification would suit the whole node better.

> So 15 of the 31 leaves are in organisms that make no LPS.
> — file:PSEAE/PA5458/PA5458-bioinformatics/RESULTS.md

> the muramic acid of the oatA mutant lacked this modification
> — PMID:15661003

## 34. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002019107
- **Subject:** UniProtKB:Q9HTB8
- **Change:** check GO:0015920 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTB8/Q9HTB8-ai-review.yaml`

The IBD of GO:0015920 lipopolysaccharide transport at PTN002019107 (PTHR30413, inner membrane transport permease) rests on one seed, P. aeruginosa Wzm (Q9HTB8). Its PseudoCAP IMP (PMID:9244257) is sound: wzm mutants accumulate A-band polysaccharide in the cytoplasm. But the node's 24 leaves include Bacillus subtilis TagG (P42953, a wall teichoic acid exporter), Staphylococcus aureus SAOUHSC_00642, Listeria lmo1074, two Streptomyces permeases, the capsule exporters CtrC (P32015) and Synechocystis KpsM (P73974), and the archaeal permeases MA_1176 (Methanosarcina) and SSO1143 (Sulfolobus). Gram-positive bacteria and archaea make no lipopolysaccharide. The substrate-neutral parent GO:0015774 polysaccharide transport fits the clade. Otherwise, GO:0015920 should be restricted to a node confined to Gram-negative O-antigen Wzm permeases.

## 35. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000530809
- **Subject:** UniProtKB:Q52463
- **Change:** check GO:0050501 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/alg8/alg8-ai-review.yaml`

The PAINT IBDs for GO:0050501 hyaluronan synthase activity and GO:0030213 hyaluronan biosynthetic process sit on PTN000530809, whose seeds are all vertebrate HAS proteins. The node's leaves (PAINT leaf GAF, 2026-11-05) also include bacterial and archaeal glycosyltransferases of other specificities, among them P. aeruginosa Alg8 (Q52463, a GDP-mannuronate polymerase), rhizobial NodC (P26024), Streptomyces SCO5051 and Sulfolobus proteins, as well as fungal and Entamoeba leaves. The hyaluronan terms do not suit a clade of this breadth; please move both IBDs down to the vertebrate HAS subclade, or add a NOT at the Alg8 subclade. The broad GO:0000271 IBD at this node is sound. This defect covers the GO:0030213 row as well.

> all of the predicted active site residues in the widely spaced D, DxD, D, LxxRW motif were required for polymerization activity in vivo
> — PMID:18524915

> O67594 alg, Q9FBM8 SCO5051, Q52463 alg8, Q97YM4 nodC-like, P26024 nodC
> — file:PSEAE/alg8/alg8-notes.md

## 36. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002019137
- **Subject:** UniProtKB:G3XCW9
- **Field:** GO_ID
- **Change:** check GO:0009276 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampD/ampD-ai-review.yaml`

The IBD of GO:0009276 Gram-negative-bacterium-type cell wall on PTN002019137 (seeds G3XCW9 ampD, Q9HT86 ampDh2, Q9I5D1 ampDh3, all PseudoCAP) propagates to cytoplasmic AmpD orthologues, including E. coli AmpD P13016, whose UniProt location is cytoplasm, and P. aeruginosa AmpD itself, identified by biochemistry as the cytoplasmic recycling enzyme. The ampD seed is a wrong PseudoCAP row (heterologous complementation of beta-lactamase expression, which does not localize the protein). The two sound seeds are periplasmic paralogues. Requested change - move the IBD to the subclade containing AmpDh2, AmpDh3 and AmiD, or add NOT annotations for the AmpD subclade, or drop the IBD. PROBABLE because the tree topology below the node was not inspected.

> SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:19309146}.
> — file:PSEAE/ampD/ampD-bioinformatics/P13016.txt

> This analysis identifies AmpD of P. aeruginosa as the cytoplasmic protease for commitment to the cell-wall recycling events and for the reversal of the activation of the antibiotic-resistance pathway.
> — PMID:23510438

## 37. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN005338738
- **Subject:** UniProtKB:P13981
- **Change:** check GO:0016990 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcA/arcA-ai-review.yaml`

The GO:0016990 arginine deiminase activity IBD at PTN005338738 (23 leaf IBAs, sole seed P. aeruginosa ArcA P13981) is soundly seeded, but the node spans the whole PTHR47271 family and its event is a SPECIATION placed at LUCA, so the IBD asserts arginine deiminase activity as ancestral to all life. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05 and narrows the concern considerably. The node has two children, PTN005338739 (Archaea-Eukaryota, 10 leaves, SF2) and PTN008715727 (DUPLICATION, 13 leaves), the latter splitting into the SF3 clade PTN008715728 (3 leaves, holding the seed P13981 with Bradyrhizobium and Streptomyces ArcA) and the SF2 bacterial clade PTN000978201 (10 leaves). Of the four leaves flagged earlier, three do not survive the check. Methanosarcina acetivorans Q8TSK4 and Halobacterium salinarum F2Z681 are a Euryarchaeota pair (PTN005338745) and both are named arginine deiminase in UniProt, as is Saccharolobus solfataricus Q97TX4, so the "not annotated as ADIs" ground does not apply to them and length alone is weak evidence. B. subtilis YkgA (O34497) is the duplication-free sister of B. cereus ArcA (Q81II1) within the Bacillus node PTN002933241, inside a Bacillales clade (PTN001763879) whose other members are the S. aureus and L. monocytogenes ArcA enzymes; the topology therefore argues that YkgA is an orthologous ADI whose Swiss-Prot name merely lags, not an over-propagation, even though B. subtilis 168 itself uses arginase. What remains is the Korarchaeum cryptofilum duplication pair PTN008230056 (2 leaves), whose members are named N-dimethylarginine dimethylaminohydrolase (B1L3J0) and amidinotransferase (B1L477) and are the only leaves of the node whose names point to a different pentein activity. Please check whether PTN008230056 needs a NOT for GO:0016990, and whether a LUCA-level node is the right place for a substrate-specific pentein activity at all. The Trichomonas vaginalis triplet PTN009208904, named only "amidinotransferase family protein", is not flagged here, since trichomonads do run an arginine dihydrolase pathway. Not verified by sequence or assay in this review.

> The structure exhibits similarity to other arginine-modifying or substituted arginine-modifying enzymes such as dimethylarginine dimethylaminohydrolase (DDAH)
> — PMID:14701825

## 38. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000150424
- **Subject:** UniProtKB:P08308
- **Change:** add the content described in the explanation to GO:0006526
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/arcB/arcB-ai-review.yaml`

The PTN000150424 IBDs of GO:0006526 L-arginine biosynthetic process and GO:0019240 citrulline biosynthetic process (seeded by anabolic OTCs) propagate to P. aeruginosa ArcB (P08308), the catabolic OTC of the arginine deiminase pathway. UniProt's curated function, citing PMID:2118516, states that this enzyme does not carry out the biosynthetic reaction; it phosphorolyses citrulline to ornithine and carbamoyl phosphate for ATP generation, and P. aeruginosa has a separate anabolic OTC (ArgF). Please add a NOT (loss) annotation for both biosynthetic terms at the node of the catabolic ArcB-type OTC subclade, or move the IBDs below the split between anabolic and catabolic OTCs. PROBABLE because the primary kinetics paper was used through the curated UniProt statement rather than read directly.

> This catabolic OTCase does not carry out the biosynthetic reaction because of a poor affinity and a marked cooperativity for carbamoyl phosphate
> — file:PSEAE/arcB/arcB-uniprot.txt

## 39. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000764469
- **Subject:** UniProtKB:P13982
- **Change:** delete the record asserting GO:0000256
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/arcC/arcC-ai-review.yaml`

The PTN000764469 IBD of GO:0000256 allantoin catabolic process rests on a single seed, E. coli AllK (P37306, IDA PMID:36384810), and propagates to the arginine deiminase pathway carbamate kinases in the same clade, including P. aeruginosa ArcC (P13982), whose curated UniProt pathway is L-arginine degradation via the ADI pathway and whose mutants are blocked in anaerobic arginine catabolism (PMID:6438064). The pathway a carbamate kinase serves follows its operon context (arcDABC for ArcC), not the shared fold, so the process term does not suit the node. Please move the IBD down to the AllK subclade, or replace it with a NOT (loss) on the ADI-pathway members. PROBABLE because the seed papers were read as abstracts and the tree topology below the node was not inspected.

> PATHWAY: Amino-acid degradation; L-arginine degradation via ADI pathway.
> — file:PSEAE/arcC/arcC-uniprot.txt

## 40. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000208945
- **Subject:** UniProtKB:P18275
- **Change:** check UniProtKB:O84379 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

The GO:0043858 arginine:ornithine antiporter activity IBD at PTN000208945 (sole seed P. aeruginosa ArcD P18275, 16 leaf IBAs) is soundly seeded, but it propagates to Chlamydia trachomatis AaxC (O84379, CT_374). The C. pneumoniae ortholog AaxC was shown to exchange L-arginine for agmatine in a decarboxylase-coupled system and to be resistant to L-ornithine. Chlamydiae lack the ADI pathway. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05 and sharpens the request. PTN000208945 is a SPECIATION node at the Eubacteria level with 16 leaves in two subfamilies (SF4 13, SF14 3) and three children: PTN001718796 (Firmicutes, 7 leaves, Clostridium/Staphylococcus/Bacillus arginine-ornithine antiporters and the B. subtilis YvsH group), the single leaf PTN000926691 (C. trachomatis AaxC) and PTN000208950 (Proteobacteria, 8 leaves, holding ArcD at PTN002449614 with its PAO1 paralog PA1194 at PTN002449613, plus Vibrio and the Enterobacteriaceae YdgI clade PTN001718809). There is no chlamydial subclade: C. trachomatis is the only chlamydial representative in the tree and its leaf attaches directly to the annotated node, so the correction must be made at the leaf PTN000926691, either as NOT GO:0043858 or by annotating GO:0043862 arginine:agmatine antiporter activity there. The IBD cannot be relocated instead, because the bacterial arginine-ornithine antiporters it covers sit in both of the other children, whose smallest common clade is PTN000208945 itself. What topology cannot settle is the biology: the C. trachomatis protein itself was not assayed for ornithine exchange, and the call rests on the C. pneumoniae ortholog.

> The chlamydial AaxC transporter was resistant to cadaverine, L-lysine and L-ornithine, which inhibit the E. coli AdiC antiporter.
> — PMID:18790867

## 41. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN004744913
- **Subject:** UniProtKB:P22567
- **Field:** GO_ID
- **Change:** GO:0004358 → GO:0004042 (L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/argA/argA-ai-review.yaml`

The PAINT IBD on PTN004744913 asserts GO:0004358 (acetyl-L-ornithine donor, the ArgJ reaction) for the ArgA-type NAGS clade. Its only two seeds, P. aeruginosa ArgA (PseudoCAP) and E. coli ArgA (EcoCyc), are acetyl-CoA-dependent NAGS enzymes. The full text of PMID:22447897 uses acetyl-CoA plus glutamate, and the UniProt records of both proteins give the acetyl-CoA reaction (RHEA:24292). The IBD is unsound without correction of both seeds; it should be repointed to GO:0004042. The likely cause is a synonym collision: N-acetylglutamate synthase activity and L-glutamate N-acetyltransferase activity are exact or related synonyms of both terms.

> producing N -acetyl- l -glutamate (NAG) from glutamate and acetyl coenzyme A (acetyl-CoA) and being feedback inhibited by arginine
> — PMID:22447897

> Reaction=L-glutamate + acetyl-CoA = N-acetyl-L-glutamate + CoA + H(+)
> — file:PSEAE/argA/argA-uniprot.txt

## 42. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000241318
- **Subject:** UniProtKB:O30508
- **Change:** check UniProtKB:Q9RW75 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/aruC/aruC-ai-review.yaml`

PTN000241318 (PTHR11986) is a SPECIATION node at the Eubacteria level holding 37 leaves in four subfamilies (SF79 22, SF113 10, SF122 3, SF112 2); topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. It carries an IBD of GO:0006526 L-arginine biosynthetic process whose only seed is P. aeruginosa AruC (O30508). The tree withdraws the "move the IBD" option: biosynthetic acetylornithine aminotransferases sit in every child clade (PTN007555578 Terrabacteria 9 leaves; the Thermotoga, Leptospira, Bacteroides, Rhodopirellula, Aquifex and Dictyoglomus singletons; PTN002279535 Cyanobacteria 3 leaves; PTN002279539 Proteobacteria 17 leaves), so arginine biosynthesis is the plesiomorphic state of the node and no ArgD-only subnode exists. The derived, non-biosynthetic activities are scattered single leaves, which is where any NOT has to go: PTN000241310 (Q9RW75, Deinococcus radiodurans LysJ) and PTN002633799 (A9WB46, Chloroflexus aurantiacus LysJ) lie in different child clades, their smallest common clade being PTN000241318 itself, and PTN000241321 (Q93S10, Streptomyces coelicolor diaminobutyrate-pyruvate aminotransferase) sits in a Streptomyces duplication, PTN002279532, whose third member (Q9L1A4) is a genuine ArgD. A NOT at PTN001736429 (Enterobacteriaceae, 2 leaves) already covers the PatA putrescine aminotransferases. The catabolic AstC leaves do form a clean clade, PTN001736444 (Enterobacteriaceae, 3 leaves), but they should not be negated: AruC itself is the same dual-specificity succinylornithine/acetylornithine aminotransferase and serves both pathways, so an AstC negation would risk the mirror-image error. Please check instead whether NOT GO:0006526 (and NOT GO:0003992) belong at the three leaves PTN000241310, PTN002633799 and PTN000241321. This does not affect AruC.

> this explains the enzyme's dual role in arginine biosynthesis and catabolism
> — PMID:16593724

## 43. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000764516
- **Subject:** UniProtKB:P80357
- **Field:** GO_ID
- **Change:** check GO:0009015 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/astA/astA-ai-review.yaml`

The PTN000764516 IBD for GO:0009015 N-succinylarginine dihydrolase activity (sole seed E. coli AstB P76216) sits at the root of PTHR30420, which also contains the AstA/AruG arginine N-succinyltransferase subfamily (SF1). The leaf GAF shows the dihydrolase IBA on seven succinyltransferase leaves (P0AE37 E. coli AstA, P80357 AruF, P80358 AruG, Q8EJ55, Q8ZPV1, Q9KNW3, Q9ZC67). These are GNAT-like acyltransferases (Pfam AstA) catalysing step 1 of the AST pathway, not step 2. Suggested change: move the GO:0009015 IBD to the AstB (SF2) node, and add GO:0008791 L-arginine N-succinyltransferase activity on the SF1 node if desired. GO:0006527 at PTN000764516 is fine. CONFIRMED: the node coverage and the leaf IBAs were checked in the PAINT and leaf GAF files, and the enzyme identities are stated in the cited abstracts and domain records.

> the aruF and aruG genes encode the subunits (AruAI and AruAII) of arginine and ornithine N2-succinyltransferases
> — PMID:9393691

## 44. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002212868
- **Subject:** UniProtKB:P00282
- **Change:** check GO:0005886 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/azu/azu-ai-review.yaml`

The IBD of GO:0005886 plasma membrane at PTN002212868 rests on a single seed, Chloroflexus aurantiacus auracyanin A (P27197, UniProt IDA PMID:1313011), a membrane-associated cupredoxin of a monoderm bacterium. The 11 leaves include soluble periplasmic azurins (P. aeruginosa azu P00282, Shewanella azu Q8CVD5, Xanthomonas az1 Q8P5R2), P. aeruginosa CopI (Q9I036) and Neisseria Laz (P57026), an outer-membrane lipoprotein. P. aeruginosa azurin has a cleaved Sec signal peptide, no lipobox or transmembrane segment, and UniProt places it in the periplasm. Please restrict the IBD to the auracyanin clade or remove it. Leaves checked in the PAINT leaf file and P27197 annotations in QuickGO (2026-11-05).

## 45. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001247822
- **Subject:** UniProtKB:Q9I3N5
- **Change:** remove GO:0004096
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

The IBD of GO:0004096 catalase activity at PTN001247822 (CcmC/heme exporter protein C family, PTHR30071) has one seed, the PseudoCAP IMP annotation of P. aeruginosa PA1477 (ccmC). That annotation records a mutant phenotype: catalase activity is undetectable in the ccmC mutant because heme does not reach the heme catalases. It is not evidence that CcmC is a catalase. CcmC has no catalase domain and handles heme for cytochrome c maturation. Please remove the catalase activity IBD from this node; this withdraws about 143 leaf IBAs. The node's plasma membrane and cytochrome c biosynthetic process IBDs are unaffected.

> The ccmC mutant was also found to accumulate porphyrins, and catalase production was undetectable, consistent with the increased sensitivity to hydrogen peroxide.
> — PMID:18174132

## 46. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002435498
- **Subject:** UniProtKB:Q9I3G5
- **Change:** GO:0004129 → GO:0009055 (electron transfer activity)
- **Recorded in:** `genes/PSEAE/ccoP1/ccoP1-ai-review.yaml`

PTN002435498 carries an IBD of GO:0004129 cytochrome-c oxidase activity whose only seeds are the PseudoCAP IMP rows on P. aeruginosa ccoP1 (Q9I3G5) and ccoP2 (Q9I3G2), both to PMID:14763990. That paper compares the two cbb3 isoforms at the operon level, and PseudoCAP put the same IMP on all eight cbb3 subunits; CcoP is the diheme cytochrome c electron-entry subunit, not the catalytic one. The node's 32 leaf IBAs (cached PAINT leaf GAF, checked 2026-11-05) include soluble cytochromes c4 (P. aeruginosa cc4 P00106, Vibrio VC_0112, Neisseria NMB1805, Shewanella SO_0714/SO_0717/SO_4048/CytcB, Xanthomonas CycA), cytochromes c552/c554 (Xanthomonas CycM, Vibrio VC_A0766), the bc1-complex cytochrome c subunit QcrC of M. tuberculosis (P9WP35) and S. coelicolor (Q9X808), and P. aeruginosa PvcD. Cytochrome c oxidase activity is wrong for these. The function common to the clade is electron transfer by c-type heme; please replace the node term by GO:0009055 electron transfer activity, or place a contributes_to GO:0004129 IBD on a CcoP-only subclade.

> Pfam; PF13442; Cytochrome_CBB3; 2.
> — file:PSEAE/ccoP1/ccoP1-uniprot.txt

## 47. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001273712
- **Subject:** UniProtKB:Q9HTH9
- **Field:** GO ID
- **Change:** GO:0047617 → GO:0016289
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cdhB/cdhB-ai-review.yaml`

PAINT places fatty acyl-CoA hydrolase activity at PTN001273712, a node that includes the betainyl-CoA thioesterase subfamily SF2; the fatty-acyl substrate should be restricted to the FadM branch, or the node term generalized to acyl-CoA hydrolase activity.

## 48. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001252526
- **Subject:** UniProtKB:Q9I1Y5
- **Change:** check GO:0007155 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cupA3/cupA3-ai-review.yaml`

The IBD of GO:0007155 cell adhesion at PTN001252526 (fimbrial usher clade, 36 leaf IBAs in 5 taxa) rests on two seeds, both mutant attachment phenotypes of an usher: P. aeruginosa CupA3 (PseudoCAP IMP, PMID:11381121 and PMID:15090530) and E. coli HtrE (EcoCyc IMP, qualified acts_upstream_of_or_within). Ushers are outer-membrane assembly pores for fimbrial subunits; the adhesion is performed by the assembled fimbria. The IBD converts an upstream role into involved_in for every usher in the clade. Please withdraw the cell adhesion IBD; the node's own role is already captured by GO:0015473 fimbrial usher porin activity, and GO:0009297 pilus assembly would be the appropriate process.

> called usher, that forms a channel into the outer membrane through which the pilin subunits are sequentially assembled
> — PMID:11381121

## 49. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002824317
- **Subject:** UniProtKB:G3XCU6
- **Change:** check GO:0019344 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cysB/cysB-ai-review.yaml`

The IBD of GO:0019344 L-cysteine biosynthetic process at PTN002824317 rests on one seed, the PseudoCAP IMP of P. aeruginosa CysB (G3XCU6, PA1754) to PMID:9218775, which reports that a cysB mutant is a cysteine auxotroph. CysB is a LysR-type transcriptional activator of the cys regulon and performs no step of cysteine synthesis, so the auxotrophy establishes necessity, not participation. That argument stands on its own and does not need the leaf list, but the leaf evidence agrees with it. All 10 leaves have the two-domain LysR architecture and nothing else (Pfam PF00126 HTH_1 plus PF03466 LysR_substrate), all 10 match the CysB-type NCBIfam profiles NF009327 PRK12684 or NF009325 PRK12680, and none carries a cysteine-biosynthetic enzyme domain, neither CysE serine acetyltransferase nor CysK O-acetylserine sulfhydrylase (UniProt records checked 2026-11-06). The two leaves with experimental annotation are both regulators: E. coli CysB (P0A9F3) has GO:0003677 DNA binding (IDA) and GO:0005829 cytosol (IDA) and no experimental GO:0019344, and E. coli Cbl (Q47083, protein level) has GO:0045883 positive regulation of sulfur utilization (IDA). The other eight have no experimental annotation, and five carry SubName names with ECO:0000313 whose "cys regulon transcriptional activator" wording is a prediction and not evidence; it is the domain architecture, not the names, that shows they are regulators. Please withdraw the IBD; the regulatory role is already covered by GO:0006355 at PTN001248394.

> which shares a high degree of sequence identity (63%) with CysB from Escherichia coli and from Salmonella typhimurium, a transcriptional factor of the LysR superfamily
> — PMID:9218775

## 50. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002169725
- **Subject:** UniProtKB:Q9HU17
- **Change:** check GO:0015740 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/dctQ/dctQ-ai-review.yaml`

The IBD of GO:0015740 C4-dicarboxylate transport at PTN002169725 has one seed, the PseudoCAP IMP of P. aeruginosa DctQ (PA5168). The PseudoCAP row is sound for DctQ. The node, however, is a YiaM-type TRAP small-permease clade that also carries an E. coli YiaM-seeded GO:0022857 IBD. Its 24 leaves include E. coli and Salmonella YiaM, whose experimentally characterised YiaMNO system transports 2,3-diketo-L-gulonate (EcoCyc IDA, PMID:16385129), plus Haemophilus, Bradyrhizobium, Geobacter, Dictyoglomus and Yersinia permeases of unknown substrate. TRAP substrate specificity is set by the periplasmic binding protein, not by the small permease. Please withdraw the C4-dicarboxylate IBD or move it to a node confined to DctQ orthologs; GO:0022857 at this node is adequate.

> the DctPQM transporter belonging to the tripartite ATP-independent periplasmic (TRAP) family of carriers
> — PMID:21725012

## 51. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000229983
- **Subject:** UniProtKB:Q9HTG5
- **Change:** check GO:0016491 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/dgcB/dgcB-ai-review.yaml`

PTN000229983 carries an IBD of GO:0016491 oxidoreductase activity that is seeded only by two PseudoCAP rows on P. aeruginosa PA5399 (dgcB), GO:0047865 dimethylglycine dehydrogenase activity and GO:0047866 dimethylglycine oxidase activity, both coded IDA and both citing PMID:17951379. That paper is a genetic study: its evidence for dgcAB is loss of growth on dimethylglycine by transposon mutants plus 13C NMR accumulation of dimethylglycine, and its full text states that characterising the biochemical activities of the dgcA and dgcB products remains a subject for future research. The two seeded terms also specify mutually exclusive chemistries (electron-transfer-flavoprotein dependent dehydrogenase versus O2-dependent oxidase), so at most one could be correct. The generalisation to the root oxidoreductase term was the right response and the node term is independently supported by domain content (PA5399 has two 4Fe-4S ferredoxin domains and two CCG domains, in a family of Fe-S electron-transfer subunits), so this is raised as a query, not a request to remove: the 33 leaf IBAs rest on an inference about a protein whose activity has never been measured, and it would be worth recording that the IBD's grounding is domain-based rather than experimental, or re-seeding it if a better characterised family member exists.

> genes that encode other enzymes with demethylase activity, are required for the
> — PMID:17951379

> The evidence for the DMG → sarcosine step is a **transposon-mutant growth phenotype plus 13C NMR metabolite accumulation**, not an enzyme assay.
> — file:PSEAE/dgcB/dgcB-notes.md

## 52. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN005219546
- **Subject:** UniProtKB:O33407
- **Field:** GO_ID
- **Change:** check GO:0008610 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

The PAINT IBD of GO:0008610 lipid biosynthetic process at PTN005219546 (PTHR45642) has a single seed, P. aeruginosa EstA (UniProtKB:O33407), whose supporting rows (UniProt IMP GO:0008610 and PseudoCAP IMP GO:0009247, PMID:17631636) record that an estA deletion strain produces little rhamnolipid. EstA is a cell-surface outer-membrane carboxylesterase with negligible activity on acyl-CoA and triacylglycerol; the biosynthetic steps are catalysed by RhlA/RhlB/RhlC, so for EstA itself the evidence shows necessity rather than participation. The node, however, is placed at LUCA (topology checked with projects/PSEUDOCAP/panther_tree.py, 2026-11-06): of its 960 leaves only 8 are bacterial (PTN005220548), and 940 are plant GDSL esterase/lipase proteins under PTN005219553, for example Arabidopsis APG (Q9LU14), At5g03810 (Q9FFN0) and At2g40250 (Q9SIZ6). Those plant leaves have no experimental function annotation at all, so the term is unsupported for the great majority of the clade. It is not unsupported everywhere. Within the bacterial clade, the three SF141 leaves form PTN005220549 (Salmonella SseJ Q9FD10, Vibrio cholerae VC_A0218 Q9KMV0, Xanthomonas campestris EstA Q8P634), separate from the SF139 autotransporter carboxylesterases that hold both seeds (EstA O33407, ChoE Q9HUP2, Salmonella ApeE H9L479). SseJ is a glycerophospholipid:cholesterol acyltransferase: purified SseJ with RhoA-GTP converts phosphatidylcholine and cholesterol to lysophosphatidylcholine and cholesteryl ester (PMID:19887681), and infection raises cholesteryl ester and lipid droplets (PMID:18333886). A cholesteryl ester is a lipid and SseJ performs the acyl transfer itself, so GO:0008610 is defensible for SseJ by participation (see genes/SALTY/sseJ). On the plant side, OSP1/AT2G04570 (Q9SJB4, SF32) is also characterised: TAIR curates fatty acyl-[ACP] hydrolase activity by IDA, and PMID:32542680 reports reduced leaf wax in the mutant plus thioesterase activity on C22:0, placing it upstream of CER3. That is a lipid-metabolic role, but an angiosperm-specific wax one unrelated to the bacterial glycolipid phenotype that seeded the node, and the smallest clade holding OSP1 together with the other plant leaves reviewed here is PTN008693276, 892 leaves at the base of the plant radiation, so it does not support the term at this node either. The request is therefore to re-scope rather than simply withdraw: please remove the IBD from PTN005219546, where neither the seed's evidence nor the clade as a whole supports it, and consider instead an IBD on the SF141 node PTN005220549 seeded by SseJ's own IDA rows. Whether the other two SF141 leaves share the acyltransferase activity is open: VC_A0218 is a characterised phospholipase (PMID:9234762, PMID:19717600) with no acyltransferase assay, and that test is suggested in genes/VIBCH/VC_A0218. A narrow plant-clade IBD seeded from OSP1 could also be considered, but that would first need a BP annotation on Q9SJB4, which GOA does not currently carry. The carboxylic ester hydrolase IBD at the same node (GO:0052689, seeds Q9HUP2 and O33407) is sound and unaffected.

> This report is focused on the influence of the outer membrane-bound esterase EstA of P. aeruginosa PAO1 on rhamnolipid production.
> — PMID:17631636

## 53. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000344128
- **Subject:** UniProtKB:G3XD64
- **Field:** With/From
- **Change:** check PANTHER:PTN000344128 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fleN/fleN-ai-review.yaml`

The IBD for GO:0005524 ATP binding at PTN000344128 (PTHR43384, MinD/ParA/FlhG clade; about 149 leaf IBAs in 75 taxa) has a single seed, the PseudoCAP IDA row for P. aeruginosa FleN (G3XD64) citing PMID:10629180. The abstract of that paper reports a putative ATP-binding motif found by sequence analysis, and the same authors still called FleN a putative ATP/GTP binding protein in 2001 (PMID:11673434), so no nucleotide-binding assay appears to underlie the seed; the full text was not available here (rechecked 2026-10-29). The conclusion that the clade binds ATP is correct, but the node rests on a non-experimental seed. Please re-seed the IBD with genuine experimental evidence, e.g. FleN ATP-analog co-crystal structures (PMID:28065505, PDB 5J1J) or experimental ATP binding of E. coli MinD (P0AEZ3), so that the propagation survives correction of the PseudoCAP row.

> Flagellar number in Pseudomonas aeruginosa is controlled by FleN, a putative ATP/GTP binding protein
> — PMID:11673434

> Crystal structures of FleN in the apo form (1.66 Å) and in complex with β,γ-imidoadenosine 5'-triphosphate (1.55 Å) reveal that it undergoes drastic conformational changes on ATP binding to attain a structure capable of dimerization.
> — PMID:28065505

## 54. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002500048
- **Subject:** UniProtKB:Q9HYK7
- **Change:** check GO:0042167 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fpr/fpr-ai-review.yaml`

The IBD of GO:0042167 heme catabolic process at PTN002500048 rests on one seed, the PseudoCAP IDA of P. aeruginosa FPR (Q9HYK7) to PMID:17915950, which shows by in vitro reconstitution that FPR is the electron donor of P. aeruginosa heme oxygenase. That is a partner-specific role of one FNR, not a property of the clade. The node's 13 leaves (QuickGO, 2026-10-28) include E. coli Fpr (P28861) and Salmonella Fpr (Q8ZKP5), from organisms without a canonical heme oxygenase (E. coli Fpr is a flavodoxin/ferredoxin reductase of the oxidative-stress response), and a Nematostella genome entry (A7TBA2). Please withdraw the IBD; the reductase activity (GO:0004324) is the appropriate family-level assertion.

> Hence, findings reported herein extend the range of redox partners recognized by the fold of pa-FPR to include a heme oxygenase (pa-HO).
> — PMID:17915950

## 55. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002112386
- **Subject:** UniProtKB:Q03456
- **Change:** check GO:1900376 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

The IBD of GO:1900376 regulation of secondary metabolite biosynthetic process at PTN002112386 is seeded by the PseudoCAP IMP of P. aeruginosa Fur (Q03456) to negative regulation of siderophore biosynthesis (PMID:8885270) and the PseudoCAP IMP of P. aeruginosa Zur/np20 (Q9HT74). The seeds are reasonable for those genes, but the node is the whole Fur superfamily: its 71 leaves (33 taxa) include Zur zinc regulators, PerR peroxide regulators, Irr heme-responsive regulators, Nur/Mur and archaeal paralogs, most of which have no known role in secondary-metabolite biosynthesis. Please move the IBD to a node restricted to Fur orthologs of siderophore-producing lineages, or withdraw it.

> The A2 and A4 mutants expressed higher levels of siderophores in iron-deficient media and in iron-replete media.
> — PMID:8885270

## 56. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002112483
- **Subject:** UniProtKB:Q03456
- **Change:** check GO:1900705 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN002112483 is a SPECIATION node (Proteobacteria) in PTHR33202 with 12 leaves, all subfamily PTHR33202:SF2 and all bona fide Fur orthologues, and four children: the single leaves PTN002848967 (Helicobacter pylori O25671), PTN002848968 (Neisseria meningitidis P0A0S8) and PTN002112491 (Geobacter sulfurreducens Q74DD7), and PTN002112492 (SPECIATION, Gammaproteobacteria; 9 leaves, containing Coxiella Q83C33, Haemophilus P44561, Shewanella Q8EFN3, Vibrio P0C6C8, Xanthomonas Q8PAL3, P. aeruginosa Q03456 and the Enterobacteriaceae clade PTN002112501 with Salmonella, Yersinia and E. coli). So the IBD of GO:1900705 negative regulation of siderophore biosynthetic process, whose sole seed is the PseudoCAP IMP of P. aeruginosa Fur (Q03456, PMID:8885270) and which is sound for P. aeruginosa, is not a family-heterogeneity problem: the family is homogeneous, and the term instead depends on a trait of the organism, whether it makes a siderophore at all. The tree shows that trait does not follow the topology. The non-producers are not a clade (H. pylori, N. meningitidis and G. sulfurreducens are three separate basal children, while Coxiella and Haemophilus sit inside the gammaproteobacterial clade), and the smallest clade holding the producers P0A9A9, P33086, P0C6C8, Q8EFN3, Q8PAL3 and Q03456 is PTN002112492, which still carries Coxiella and Haemophilus. There is therefore no child node this IBD can be moved to. Please retype the node-level IBD to something true of every Fur orthologue, such as negative regulation of DNA-templated transcription or a regulation-of-iron-import term, and keep GO:1900705 as leaf-level annotations on the siderophore producers that have their own evidence. What the tree settles, and what this request rests on, is the structural point: the trait the term depends on does not partition the clade, so no child node carries the producers alone and relocation is not available. Which of the leaves make a siderophore is not settled here; that reading of H. pylori, N. meningitidis, Coxiella and Haemophilus as non-producers is standard background rather than something checked for this entry, and a curator should confirm it before acting. If any of them turns out to produce one, the remedy changes from retyping to relocating, but the current node placement is wrong either way.

> The A2 and A4 mutants expressed higher levels of siderophores in iron-deficient media and in iron-replete media.
> — PMID:8885270

## 57. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000501197
- **Subject:** UniProtKB:Q9I291
- **Change:** check GO:0009244 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/galU/galU-ai-review.yaml`

PTN000501197 carries an IBD of GO:0009244 lipopolysaccharide core region biosynthetic process seeded by E. coli GalU (P0AEP3, EcoCyc IMP acts_upstream_of_or_within) and P. aeruginosa GalU (Q9I291, PseudoCAP IMP PMID:12044687). Both seeds are sound for their own organisms, but the node's 33 leaf IBAs (cached PAINT leaf GAF, checked 2026-11-05) include Gram-positive and wall-less bacteria that have no lipopolysaccharide, among them B. subtilis GtaB (Q05852) and YngB (O31822), S. aureus GtaB (Q2G1T6), Listeria lmo1078, Streptococcus Q8DN58, Clostridium GtaB, Mycoplasma P47691, Streptomyces GtaB and M. tuberculosis GalU (O05576). Please move the IBD to a Gram-negative subclade, or drop it and rely on the UDP-glucose activity IBD, which suits the whole clade.

> indicating the involvement of GalU in P. aeruginosa LPS core synthesis
> — PMID:12044687

## 58. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN004253691
- **Subject:** UniProtKB:Q9I3S3
- **Change:** check UniProtKB:Q9I6K2 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/gbuA/gbuA-ai-review.yaml`

PTN004253691 (PTHR11358) is a HORIZ_TRANSFER node holding 34 leaves, all in subfamily SF26 (topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05): P. aeruginosa GpuA (Q9I6K2, leaf PTN002260450) as sister to everything else, P. aeruginosa GbuA (Q9I3S3, leaf PTN002260452) nested inside the animal clade through a second HORIZ_TRANSFER node PTN004253692, and 32 animal AGMAT guanidino acid hydrolases (Deuterostomia clade PTN000144490, 30 leaves, plus the Nematostella duplication PTN000888144, 2 leaves). The IBD of GO:0006527 L-arginine catabolic process at this node has GbuA as its only seed, where it is correct. The tree shows the two Pseudomonas enzymes are not sisters, so there is no bacterial guanidinobutyrase subnode to move the IBD to: the smallest clade containing GbuA alone is its own leaf. GpuA is a guanidinopropionase with no activity on arginine, serving 3-guanidinopropionate utilisation, and the vertebrate AGMAT orthologs (e.g. human Q9BSE5) are characterised as guanidino acid hydrolases whose physiological substrates (taurocyamine, 4-guanidinobutyrate, agmatine) are not intermediates of an arginine catabolic pathway in those organisms; arginine itself is turned over only inefficiently. Please either withdraw the clade-level IBD and keep GO:0006527 as a leaf annotation on PTN002260452, or add NOT GO:0006527 at the three nodes that cover the other 33 leaves without touching GbuA: PTN002260450 (GpuA), PTN000144490 (Deuterostomia, 30) and PTN000888144 (Nematostella, 2).

> We demonstrate here that the enzyme efficiently hydrolyzed linear guanidino acids such as TC and GBA, whereas GPA and arginine were turned over less efficiently
> — PMID:36543883

## 59. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN004253691
- **Subject:** UniProtKB:Q9I3S3
- **Change:** add NOT GO:0047972 (NOT guanidinopropionase activity on GbuA (PA1421)) to UniProtKB:Q9I3S3
- **Recorded in:** `genes/PSEAE/gbuA/gbuA-ai-review.yaml`

PTN004253691 (PTHR11358) is a HORIZ_TRANSFER node holding 34 leaves, all in subfamily SF26: two P. aeruginosa enzymes and 32 animal AGMAT guanidino acid hydrolases (topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05). It carries a GO:0047972 guanidinopropionase activity IBD seeded by human AGMAT (Q9BSE5) and P. aeruginosa GpuA (Q9I6K2). The two seeds sit on opposite sides of the tree: GpuA is leaf PTN002260450, the sister of all 33 other leaves, while human AGMAT lies inside the Deuterostomia clade PTN000144490 (30 leaves), so their smallest common clade is PTN004253691 itself. The IBD therefore cannot be relocated to any node that excludes P. aeruginosa GbuA (Q9I3S3), which is leaf PTN002260452, nested between the GpuA branch and the deuterostome clade through a second HORIZ_TRANSFER node, PTN004253692 (31 leaves). A leaf-level NOT is the only available fix, and the activity is excluded by direct assay of the purified enzyme (no activity with 3-guanidinopropionate, PMID:12029055; also stated in the UniProt entry, citing PMID:21600989). Please add NOT GO:0047972 at PTN002260452.

> No enzyme activity was detected with other guanidino compounds, including arginine, agmatine, 3-guanidinopropionate, and guanidinoacetate.
> — PMID:12029055

## 60. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q51366 involved_in GO:0042351 'de novo' GDP-L-fucose biosynthetic process (IBA, GO_REF:0000033)
- **Field:** GO_ID
- **Change:** check GO:0042351 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gmd/gmd-ai-review.yaml`

The IBA assigns P. aeruginosa Gmd (Q51366) to GO:0042351 'de novo' GDP-L-fucose biosynthetic process. The PTN008684430 node seeds for this term are fucose-producing organisms (Arabidopsis AT3G51160, human GMDS O60547, fly, Trypanosoma Q387W4, Dictyostelium); Q51366 is not among them, so it receives the IBA. GMD is the first, shared step; the pathway's identity (fucose vs rhamnose) is set by the second enzyme. P. aeruginosa has no GDP-L-fucose synthase (fcl) and makes GDP-D-rhamnose via Rmd, not GDP-L-fucose. The GDP-L-fucose process term is therefore wrong for this gene. This is a received IBA, not a defect in the node seeds; flagged so the GDP-L-fucose process term is not propagated to non-fucose lineages. PROBABLE pending a check of fcl absence across Pseudomonas.

> P. aeruginosa GMD is bifunctional, and can catalyze both GDP-d-mannose 4,6-dehydration and the subsequent reduction reaction to produce GDP-D-rhamnose.
> — PMID:19459932

## 61. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN004738955
- **Subject:** UniProtKB:Q9HYJ7
- **Field:** GO_ID
- **Change:** check GO:0015344 (alternatives in the explanation)
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/hasR/hasR-ai-review.yaml`

PTN004738955 is the LUCA root of PTHR30069, spanning 149 leaves across 18 subfamilies, and it carries IBDs for the substrate-specific siderophore terms GO:0015344 siderophore uptake transmembrane transporter activity and GO:0044718 siderophore transmembrane transport. Its five seeds are all siderophore or colicin receptors in five different subfamilies: Q9HVC0 (SF42) and Q9HWM5 (SF37), both characterised ferric-siderophore receptors whose own seed rows this project reviewed and found sound, Q9I527 ferric enterobactin receptor PirA (SF8), Q05098 ferric enterobactin receptor (SF51) and P17315 colicin I receptor (SF53). The terms therefore reach the haem-receptor subfamilies, whose PANTHER names state what they are: SF41 "Heme uptake outer membrane receptor HasR", which is this gene, and SF29 "Heme_hemoglobin uptake outer membrane receptor", which is phuR. Both have their own experimental evidence for haem rather than siderophore uptake. The seeds are not the problem; the depth is. What the node supports is the shared mechanism, TonB-dependent transport across the outer membrane, not the substrate. Relocating the IBDs will not fix it: the smallest clade containing all five seeds is PTN002824128 (145 leaves), which contains SF29 and SF41 as well, so no child node holds the siderophore receptors alone. Suggested change: generalise the node terms to substrate-neutral ones, or prune/block the siderophore terms in the haem subfamilies SF29 and SF41. CONFIRMED: the node composition, the subfamily of every seed and target, and the minimal-clade test were checked directly in the PANTHER tree with projects/PSEUDOCAP/panther_tree.py on 2026-11-13. The same request covers the identical rows on phuR, which cross-references this entry.

> A deltahasR mutant also exhibited decreased utilization of haem and haemoglobin, and a deltaphuR deltahasR double mutant was virtually unable to take up either compound.
> — PMID:10658665

## 62. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000138516
- **Subject:** UniProtKB:Q9HU77
- **Change:** check UniProtKB:Q9HU77 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutF/hutF-ai-review.yaml`

Tree topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN000138516 is the LUCA SPECIATION root of PTHR11271:SF48 and has exactly two children: PTN000884852 (SPECIATION, Rhabditida-Chromadorea; 3 nematode cpin-1 leaves, C. elegans Q20166, C. briggsae A8Y0T4, Pristionchus A0A2A6BT36) and PTN000138520 (SPECIATION, Eubacteria; 5 leaves, including Q9HU77). The bacterial leaves carry the HutF-type amidohydrolase signatures (InterPro IPR010252, NCBIfam TIGR02022, HutF_N); the three nematode leaves do not, and no histidine-degradation route is known for them. Asserting GO:0006548 L-histidine catabolic process and GO:0050416 formimidoylglutamate deiminase activity at the LUCA node therefore propagates both terms into a whole clade with no support for either. Please move the two IBDs down to PTN000138520 (Eubacteria, 5 leaves). Within that clade only Q9HU77 is a characterised formimidoylglutamate deiminase (the other four leaves are annotated chlorohydrolase or hydrolase: Q9KZ77, Q89GV1, Q8PAA5, Q9ZC76), so if the family evidence does not extend beyond the gammaproteobacteria the narrower anchors are PTN001681702 (Gammaproteobacteria, 3 leaves) or the Q9HU77 leaf PTN002462020. Separately, the sole seed of the GO:0006548 IBD is the PseudoCAP IMP to PMID:4290562, whose full text contains no hutF mutant; please re-anchor that IBD on PMID:16475788.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

> The protein Pa3175 is dislocated from the hut operon and was shown to catalyze the hydrolysis of N-formimino-L-glutamate to formamide and L-glutamate.
> — PMID:16475788

## 63. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002233700
- **Subject:** UniProtKB:Q9HU85
- **Change:** add NOT GO:0004397 (NOT histidine ammonia-lyase activity (and NOT L-histidine catabolic process) on PA5093) to UniProtKB:Q9HU90
- **Recorded in:** `genes/PSEAE/hutH/hutH-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py (--family PTHR10362, no seed of this node has a PANTHER cross-reference) on 2026-11-05. PTN000796665 (SPECIATION, Eubacteria; 21 leaves) is the node carrying the IBDs of GO:0004397 histidine ammonia-lyase activity and GO:0006548 L-histidine catabolic process, seeded by P. aeruginosa PA5098 (hutH, Q9HU85). The path from it to the PA5093 leaf runs PTN000796665 -> PTN000796672 (SPECIATION, Proteobacteria; 11 leaves) -> PTN001621799 (SPECIATION, Gammaproteobacteria; 10 leaves) -> PTN002233699, which is a DUPLICATION node with exactly two leaves, both P. aeruginosa and both PTHR10362:SF7: PTN002233700 (Q9HU90 PA5093, "probable histidine/phenylalanine ammonia-lyase") and PTN002233701 (Q9HU85 hutH, "histidine ammonia-lyase"). The IBAs on PA5093 therefore come from a terminal in-paralog duplication of the seeded gene itself, and PA5093 has no MIO-forming Ala-Ser-Gly tripeptide (the aligned residues are gapped), is only about 40% identical to PA5098, and corresponds to the HutH1 paralog of P. fluorescens SBW25, which lacks the active-site residues and cannot complement a histidase mutant (PMID:17717196). Because the duplication is P. aeruginosa-specific there is no HutH1-type clade in this tree to annotate: please add the NOT annotations for both terms at the PA5093 leaf PTN002233700.

> Analysis of the deduced amino acid sequences of hutH 1 and hutH 2 showed that HutH 1 lacks the conserved Ala–Ser–Gly active site residues
> — PMID:17717196

> deletion of hutH 1 had no effect; however, deletion of hutH 2 resulted in a strain unable to grow on histidine.
> — PMID:17717196

> PA5093 (Q9HU90), the second HutH-like gene in the PAO1 hut locus, has no Ala-Ser-Gly tripeptide anywhere
> — file:PSEAE/hutH/hutH-bioinformatics/RESULTS.md

## 64. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000505272
- **Subject:** UniProtKB:Q9HU91
- **Change:** check UniProtKB:Q9HU91 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutI/hutI-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN000505272 is the LUCA SPECIATION root of PTHR42752 with two children, PTN000505273 (SPECIATION, Archaea-Eukaryota; 36 leaves) and PTN000505310 (SPECIATION, Eubacteria; 16 leaves). All 52 leaves are subfamily PTHR42752:SF1 and all are named imidazolonepropionase or probable imidazolonepropionase (bacterial HutI plus eukaryotic AMDHD1). So the node breadth and the node terms GO:0050480 imidazolonepropionase activity and GO:0006548 L-histidine catabolic process are sound, and this request is about the IBD's evidence anchor only, not its placement or its terms. Its one seed is the PseudoCAP IMP of P. aeruginosa PA5092 (hutI) to PMID:4290562, whose full text (read 2026-11-05) assays steps I, II and IV in crude extracts, never step III, and describes no hutI mutant; it therefore supports neither term for PA5092 nor, through it, the 52 leaf IBAs. Please re-anchor the IBD on an experimentally characterised descendant already in the clade, for example B. subtilis HutI P42084 (structure and activity, PMID:16990261) or human AMDHD1 Q96NU7. No change to the node terms is requested.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 65. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002217335
- **Subject:** UniProtKB:P33883
- **Change:** GO:0007165 → GO:0009372 (quorum sensing)
- **Recorded in:** `genes/PSEAE/lasI/lasI-ai-review.yaml`

The GO:0007165 signal transduction IBD at PTN002217335 (LuxI-family AHL synthases; leaves P. aeruginosa LasI and RhlI, Yersinia YspI and YpeI, Bradyrhizobium BjaI) has one seed, the PseudoCAP IDA on LasI to PMID:8493556. These enzymes synthesise the diffusible autoinducer; GO:0007165 is restricted to events at and within the receiving cell, starting with signal reception (LuxR-type receptors). Please re-term the IBD to GO:0009372 quorum sensing, whose definition includes producing the signal molecule and which other autoinducer synthases carry experimentally (ainS G3FB25, luxS P45578). The node MF GO:0061579 is correct.

> The lasl gene is involved in the synthesis of a diffusible molecule termed Pseudomonas autoinducer (PAI).
> — PMID:8493556

## 66. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002433936
- **Subject:** UniProtKB:Q9I489
- **Change:** GO:0047580 → GO:0050346 (trans-L-3-hydroxyproline dehydratase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/lhpL/lhpL-ai-review.yaml`

PTN002433936 (PTHR33442, 9 reference leaves in 7 organisms; 35 GOA rows in with/from) carries an IBD of GO:0047580 4-hydroxyproline epimerase activity whose single seed is the PseudoCAP IMP row on P. aeruginosa lhpL (UniProtKB:Q9I489, PMID:27145750). Swiss-Prot records for that same protein, with experimental evidence (ECO:0000269|PubMed:17849014), that it displays neither t4LHyp epimerase nor proline racemase activity, and assigns it instead the trans-3-hydroxy-L-proline reactions (EC 4.2.1.77 and a 2-epimerization to cis-3-hydroxy-D-proline, ECO:0000269|PubMed:27929065). PAO1's genuine 4-hydroxyproline 2-epimerase is the separate gene PA1268 (UniProtKB:Q9I476). Two leaves under the node are already named trans-3-hydroxy-L-proline dehydratases, so the clade looks right and only the term needs re-pointing to GO:0050346. The absence of the 4-hydroxy reaction was checked in the full text of PMID:17849014, whose Table 1 lists Q9I489 as the Ser-Cys variant and whose Figure 1 shows it has neither activity.

> P. aeruginosa (SC) and B. cenocepacia (CT) recombinant proteins whose sequences lack one of the two Cys catalytic residues do not display any PRAC or HyPRE activities.
> — PMID:17849014

> We herein demonstrated that PaLhpL gene (PA1255; Fig. 1d) in the L-hydroxyproline gene cluster encodes a bifunctional dehydratase and 2-epimerase toward trans-3-hydroxy-L-proline as the leading candidate
> — PMID:27929065

## 67. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001627042
- **Subject:** UniProtKB:Q9I1X7
- **Field:** GO_ID
- **Change:** check GO:0006269 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ligD/ligD-ai-review.yaml`

The IBD for GO:0006269 DNA replication, synthesis of primer at PTN001627042 (LigD clade, 15 leaf IBAs) rests on M. tuberculosis LigD (P9WNV3, MTBBASE IDA, PMID:16023671). LigD polymerase/primase activity has been shown in vitro, but LigD functions in Ku-dependent NHEJ repair of double-strand breaks, not in chromosomal replication. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN001627042 is a SPECIATION node (LUCA) with 15 leaves in two subfamilies (PTHR42705:SF2 12, SF3 3) and two children: PTN005127089 (SPECIATION, Eukaryota, 2 leaves: Monosiga MONBRDRAFT_36321 "DNA ligase D" and Gossypium LOC107941224) and PTN000048875 (SPECIATION, Eubacteria, 13 leaves), which holds the Terrabacteria clade PTN008085115 (7 leaves, including Mtb LigD P9WNV3 and B. subtilis LigD O34398, plus the Streptomyces SF2/SF3 duplication PTN000048869) and the Proteobacteria clade PTN005127091 (6 leaves, with P. aeruginosa LigD Q9I1X7 reached through the HORIZ_TRANSFER node PTN005127093). Every leaf is a LigD-type or ATP-dependent DNA ligase; the two with full names are both bifunctional NHEJ proteins, and no leaf is a replicative primase or a DnaG-type enzyme. The clade is thus homogeneous, which means the term cannot be rescued by moving it to a subclade: the mismatch is between the term and the whole family. Please remove this IBD (the activity is already covered by the GO:0003887 IBD at the same node and the role by GO:0006303 non-recombinational repair). PROBABLE rather than CONFIRMED because the topology settles that relocation is not the fix, while the Mtb seed paper PMID:16023671 was still not read and could report a replication-linked assay.

## 68. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001733227
- **Subject:** UniProtKB:Q9I298
- **Change:** check GO:0004490 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuC/liuC-ai-review.yaml`

The IBD of GO:0004490 methylglutaconyl-CoA hydratase activity at PTN001733227 has one seed, the PseudoCAP IMP of P. aeruginosa LiuC (Q9I298) to PMID:16517656, a mutant-based inference with no reported enzyme assay. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN001733227 is a SPECIATION node placed at LUCA, with 13 leaves all in PTHR42964:SF1, splitting into the Monosiga brevicollis leaf PTN000941888 and the Eubacteria clade PTN000234935 (12 leaves), which divides into Terrabacteria PTN008092237 (4 leaves; B. subtilis PksH, Chloroflexus, Actinomycetales) and Proteobacteria PTN000234939 (8 leaves). Placing a substrate-specific crotonase activity at a LUCA node is not supportable, and the tree shows the support stops at the leaf; LiuC's own sister is P. aeruginosa AtuE (Q9HZV7, leaf PTN002452382, duplication node PTN002452381), which hydrates isohexenylglutaconyl-CoA instead, and B. subtilis PksH (P40805) is recorded by UniProt (ECO:0000269) as dehydrating an HMG group tethered to the carrier protein PksL in bacillaene biosynthesis, not HMG-CoA. Even the smallest clade holding the three methylglutaconyl-CoA hydratases of the family (Q9I298, Shewanella Q8EFS1, Coxiella Q83CX5) is PTN001733230 (SPECIATION, Gammaproteobacteria, 7 leaves), which also contains AtuE, Coxiella PksH and the two Xanthomonas enzymes (one a p-hydroxycinnamoyl-CoA hydratase/lyase). There is therefore no node confined to LiuC orthologs above the LiuC leaf PTN002452383. Please put a generic enoyl-CoA hydratase/hydro-lyase term at PTN001733227 and keep GO:0004490 as a leaf-level annotation on the characterised LiuC leaves.

## 69. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001733227
- **Subject:** UniProtKB:Q9I298
- **Change:** delete the record asserting GO:0046247
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuC/liuC-ai-review.yaml`

The IBD of GO:0046247 terpene catabolic process at PTN001733227 rests on one seed, the PseudoCAP IMP of P. aeruginosa LiuC (Q9I298) to PMID:16820476. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN001733227 is a SPECIATION node placed at LUCA, with 13 leaves all in PTHR42964:SF1, splitting into the Monosiga brevicollis leaf PTN000941888 and the Eubacteria clade PTN000234935 (12 leaves; Terrabacteria PTN008092237, 4, and Proteobacteria PTN000234939, 8). An IBD at a LUCA node asserts that acyclic terpenoid utilisation is ancestral to all life, which it is not; LiuC is a 3-methylglutaconyl-CoA hydratase of leucine catabolism and takes part in terpenoid catabolism in P. aeruginosa only because the Atu pathway feeds methylcrotonyl-CoA into the Liu pathway. That context is not inherited by the clade, whose other leaves are in organisms with no Atu pathway (M. tuberculosis EchA7, B. subtilis PksH, Coxiella, Xanthomonas, Streptomyces, Chloroflexus, Monosiga); even P. putida, which has a Liu pathway, cannot grow on acyclic terpenes. Please withdraw the IBD. The one subnode for which a terpenoid-catabolic assertion would hold is PTN002452381, the P. aeruginosa DUPLICATION pair (2 leaves) of LiuC (PTN002452383) and AtuE (PTN002452382), both of which act in acyclic terpene utilisation in PAO1. (For PAO1 the more accurate term would be GO:0016100 monoterpenoid catabolic process.)

> P. fluorescens, but not P. putida, could grow on acyclic terpenes (citronellol and citronellate), while both species were able to utilize leucine and isovalerate
> — PMID:16820476

## 70. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000031222
- **Subject:** UniProtKB:Q9I2A0
- **Field:** GO_ID
- **Change:** check GO:0046951 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuE/liuE-ai-review.yaml`

The GO:0046951 ketone body biosynthetic process IBD on PANTHER node PTN000031222 is seeded only by animal HMG-CoA lyases (UniProtKB:P35914, UniProtKB:P35915, UniProtKB:Q8TB92, RGD:620554, FB:FBgn0031877), but the node spans bacterial, fungal and plant members and propagates the term to them as IBAs - including P. aeruginosa LiuE (Q9I2A0), where HMG-CoA cleavage is the terminal step of L-leucine, isovalerate and acyclic terpene catabolism and the acetoacetate produced is a catabolic intermediate, not a ketone body made as a circulating fuel. Requested change - move this IBD to the animal (or vertebrate) clade in which ketogenesis exists, leaving the family-level GO:0004419 and the catabolic process IBDs at the broader node. Filed as PROBABLE because the seed list and the chemistry are checkable, while the exact node at which to place the restriction is a judgement for the PAINT curator.

> The LiuE protein was purified as a His-tagged recombinant protein and in addition to show HMG-CoA lyase activity
> — PMID:19597963

## 71. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000227060
- **Subject:** UniProtKB:Q9I544
- **Field:** With/From
- **Change:** check PANTHER:PTN000227060 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/mgtE/mgtE-ai-review.yaml`

The IBD of GO:0000287 magnesium ion binding at PTN000227060 (PTHR43773 family root, 25 leaf IBAs in 21 taxa) has a single seed, the PseudoCAP IMP row for P. aeruginosa MgtE (Q9I544, PMID:24722909). A mutant phenotype (site-directed mutants of Mg2+ sites predicted from a homology model) is not evidence of ion binding. The conclusion is probably right: T. thermophilus MgtE (Q5SMG8) binds Mg2+ in crystal structures (IDA, PMID:17700703) and the ligands are largely conserved. But Q5SMG8 is not a leaf of the reference tree, so as it stands the node rests on a non-binding seed. Please consider whether the IBD should be kept without an experimental seed, or anchored on a leaf with direct binding evidence if one becomes available.

> showed that magnesium-binding sites in the connecting helix region of MgtE are vital in coupling these two functions
> — PMID:24722909

## 72. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000227060
- **Subject:** UniProtKB:Q9I544
- **Change:** add NOT GO:0015693 (NOT magnesium ion transport at PTN005181931 (SCO5154, Rv1232c) and at the leaves CBO0203, TM_0892, NEMVEDRAFT_v1g223975 and VC_0300) to PANTHER:PTN000227060
- **Recorded in:** `genes/PSEAE/mgtE/mgtE-ai-review.yaml`

PTN000227060 (PTHR43773 family root, 25 leaves) carries an IBD of GO:0015693 magnesium ion transport seeded by P. aeruginosa MgtE (PA0913). Six reference leaves lack the MgtE transmembrane domain (Pfam PF01769), and five of them have no predicted transmembrane segment: Streptomyces SCO5154 (Q9FBK4) and M. tuberculosis Rv1232c (O86315), which together form PTN005181931, Clostridium CBO0203 (A5HY96), Thermotoga TM_0892 (Q9WZZ4), Nematostella A7T8Y4 and Vibrio VC_0300 (Q9KV57). They are MgtE_N/CBS-domain proteins and cannot transport Mg2+ on their own, yet each inherits the transport IBA. Please consider NOT annotations at these leaves (or at PTN005181931). The seed itself is sound.

> Of the 22 leaves resolved in UniProt, 16 carry Pfam PF01769 (MgtE transmembrane domain) and 6 do not
> — file:PSEAE/mgtE/mgtE-bioinformatics/RESULTS.md

## 73. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001251133
- **Subject:** UniProtKB:Q9HUL2
- **Field:** GO_ID
- **Change:** GO:0071978 → GO:0071973
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motB/motB-ai-review.yaml`

The IBD of GO:0071978 bacterial-type flagellum-dependent swarming motility at PTN001251133 (PTHR30329 MotB clade, 9 leaf IBAs in 7 taxa) has a single seed, PseudoCAP IMP rows on P. aeruginosa MotB (PA4953; PMID:15629949, PMID:25349157). In both papers the motAB single mutant swarms like wild type or better; only the motAB motCD double mutant fails to swarm. Swarming is a surface lifestyle that most leaves (Thermodesulfovibrio, Bradyrhizobium PomB, Xanthomonas, Yersinia LafU) have not been shown to display. The stator role the clade shares is flagellar rotation; please consider replacing the node term with GO:0071973 bacterial-type flagellum-dependent cell motility, alongside the existing stator complex IBD.

> The Δ motAB mutant is able to swarm as well as the WT in agar concentrations up to 0.7%.
> — PMID:15629949

> Mutation of both genes encoding the MotA homologs or MotB homologs was sufficient to abolish motility.
> — PMID:15375113

## 74. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001252377
- **Subject:** UniProtKB:G3XD73
- **Field:** GO_ID
- **Change:** GO:0071978 → GO:0071973 (bacterial-type flagellum-dependent cell motility)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motC/motC-ai-review.yaml`

The IBD of GO:0071978 bacterial-type flagellum-dependent swarming motility at PTN001252377 (PTHR30433 MotA clade, 29 leaf IBAs in 19 taxa) has two seeds, both PseudoCAP IMP rows on P. aeruginosa stator A subunits, MotC (PA1460; PMID:15629949) and MotA (PA4954; PMID:15629949, PMID:25349157). The MotC seed is sound for P. aeruginosa, and the MotA seed is weak (the motAB single mutant swarms like wild type, or better). The objection is to the term, not to the seeds. GO:0071978 is_a GO:0071973 and adds a lifestyle context to it: its definition requires "the smooth movement of a group of cells along a solid surface" and notes that "Swarming motility is observed in groups of bacteria". What a MotA-family protein contributes is the stator half of the flagellar motor, an ion channel that generates torque, and that is what the clade's one experimentally characterised leaf shows: E. coli MotA (UniProtKB:P09348), the seed of this node's own stator-complex IBD, carries GO:0071973 by IMP, GO:0015252 proton channel activity, and GO:0120101 bacterial-type flagellum stator complex by IPI, and has no experimental swarming annotation. Whether an organism swarms over a surface turns on surfactant production, cell density and growth conditions rather than on which stator it encodes, so the context-bearing child term should not be inherited by descent while its parent is the property the clade actually shares. We make no claim about whether the other leaves do or do not swarm; we checked only the annotation state, and in QuickGO (checked 2026-11-06) every GO:0071978 row on the 24 non-PAO1 leaves is IBA or IEA, so no leaf besides the two P. aeruginosa seeds carries experimental support for the specific term. Please consider replacing the node term with GO:0071973 bacterial-type flagellum-dependent cell motility, alongside the existing stator complex IBD (seeded by E. coli MotA, P09348). A parallel defect was filed for the MotB node PTN001251133 (genes/PSEAE/motB).

> The Δ motAB mutant is able to swarm as well as the WT in agar concentrations up to 0.7%.
> — PMID:15629949

> Mutation of both genes encoding the MotA homologs or MotB homologs was sufficient to abolish motility.
> — PMID:15375113

## 75. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** PANTHER:PTN002215378
- **Subject:** UniProtKB:P38108
- **Change:** check GO:0032885 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/mucB/mucB-ai-review.yaml`

The GO:0032885 regulation of polysaccharide biosynthetic process IBD at PTN002215378 (7 leaf IBAs) rests only on P. aeruginosa MucB (P38108, PseudoCAP IMP PMID:9171421). The phenotype is alginate overproduction caused by derepression of the ECF sigma factor AlgU, whose regulon in Pseudomonas includes the algD operon. The clade itself is homogeneous and we do not dispute its coherence: all seven leaves are 310-321 aa and match Pfam PF03888 MucB_RseB plus PF17188 MucB_RseB_C, and six also match NCBIfam NF006990 rseB (UniProt records checked 2026-11-06). Our objection is to the term, not the clade. Only one other leaf has experimental annotation: E. coli RseB (P0AFX9, reviewed, protein level) has GO:0045152 antisigma factor binding (IDA), GO:0050821 protein stabilization (IDA), GO:0042597 periplasmic space (EXP) and GO:1903865 sigma factor antagonist complex (IPI), and no polysaccharide-related annotation of any kind; the other five (H9L461, A0A2U2GWS2, P44792, Q8EH85, Q9KPA8) have no experimental annotation at all. The route by which the seed's phenotype arises is lineage-restricted, since the alginate algD biosynthetic operon is confined to Pseudomonas and Azotobacter, so the alginate output cannot propagate. We flag a counter-consideration we cannot settle: E. coli RseB binds lipopolysaccharide (curated ECO:0000269 statements in P0AFX9) and the sigmaE regulon includes LPS biogenesis genes, so a term as broad as regulation of polysaccharide biosynthetic process might be defensible for the enterobacterial leaves by a different mechanism. We therefore ask only that the IBD be checked, and that it be placed on a Pseudomonas-only node if the broad claim is not intended. The node's antisigma factor binding and periplasm IBDs (seeded by E. coli RseB) are the conserved, experimentally grounded claims.

> RseB (a MucB homolog), which is a protein that inhibits DegS cleavage of RseA
> — PMID:19298369

## 76. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000132400
- **Subject:** UniProtKB:G3XD10
- **Change:** check GO:0006783 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nirJ/nirJ-ai-review.yaml`

The IBD of GO:0006783 heme biosynthetic process at PTN000132400 rests on one seed, the PseudoCAP IMP of P. aeruginosa NirJ (G3XD10) to PMID:8982003, which concerns heme d1, not protoheme. The other 14 leaves (QuickGO, 2026-10-28) are archaeal SPASM-domain radical SAM proteins (Korarchaeum B1L4Z0, B1L5P2, B1L7M3; Methanosarcina Q8THT9, Q8TIJ8, Q8TL56, Q8TR79, Q8TU98; Pyrobaculum Q8ZYW8; Sulfolobus Q97WC3, Q97XA7, Q97XS7; Halobacterium Q9HQF7) classified by InterPro/NCBIfam as generic SPASM, PTO1314-family or pseudo-SAM proteins, or as an aldehyde ferredoxin oxidoreductase cofactor-modifying protein; only Q8TLK1 (TIGR04546, 12,18-didecarboxysiroheme deacetylase AhbC) is a heme-pathway enzyme. Please withdraw the IBD or move it to a node confined to NirJ (TIGR04051) and, separately, AhbC.

> Thus, NirJ and AhbC use the same substrate.
> — PMID:40318205

## 77. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001284536
- **Subject:** UniProtKB:Q9HWH9
- **Change:** check GO:0018580 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nmoA/nmoA-ai-review.yaml`

The IBD of GO:0018580 nitronate monooxygenase activity at PTN001284536 rests on one seed, P. aeruginosa NmoA (Q9HWH9), which is sound. But the node also has P. aeruginosa PA0660 (Q9I5R1) among its 23 leaves, and purified PA0660 shows no nitronate monooxygenase activity; it is an NAD(P)H:quinone reductase that the authors propose as the paradigm of a separate class defined by six conserved motifs across more than 1000 open reading frames currently annotated as hypothetical NMOs. Please consider a NOT at the PA0660 branch, or moving the IBD down to a node confined to class I NMOs (the four-motif group defined in PMID:25002579).

> Despite its annotation, PA0660 did not exhibit nitronate monooxygenase activity.
> — PMID:31075192

## 78. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000171476
- **Subject:** UniProtKB:Q9HT76
- **Change:** add GO:0008998 (ribonucleoside-triphosphate reductase (thioredoxin) activity) to GO:0004748
- **Recorded in:** `genes/PSEAE/nrdJa/nrdJa-ai-review.yaml`

PTN000171476 (PTHR43371, class II / vitamin B12-dependent ribonucleotide reductases) carries an IBD of GO:0004748 ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor, seeded solely by the PseudoCAP IDA row on P. aeruginosa PA5497 (nrdJa), and propagates it as 39 IBAs across 33 taxa. Biochemical characterisation of the seed organism's own enzyme (purified NrdJa plus NrdJb, PMID:26225432) shows that ribonucleoside triphosphates are the preferred substrate by more than 60-fold over the diphosphate, and PTHR43371 contains both NDP-specific and NTP-specific members (several are annotated as adenosylcobalamin-dependent ribonucleoside-triphosphate reductases, rtpR). Please consider adding GO:0008998 at this node, or moving the IBD to a term that does not commit to the phosphorylation state of the substrate; the current single term asserts a substrate specificity that is wrong for the seed and not uniform across the clade. The thioredoxin-acceptor clause is likewise untested in the purified-enzyme study, which used DTT or TCEP as reductant (only the abstract of PMID:15722359 was read).

> The results revealed that CTP is the preferred substrate with a >60-fold higher activity compared to CDP
> — PMID:26225432

> 50 mM Tris-HCl buffer at pH 7.5, 30 mM DTT, 10 mM MgCl2, 100 μM AdoCbl, 1 mM ATP, 1 mM CTP, and 2 μM of NrdJa and NrdJb
> — PMID:26225432

## 79. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001607041
- **Subject:** UniProtKB:Q9HUK1
- **Change:** delete the record asserting GO:0005524
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/parC/parC-ai-review.yaml`

PAINT IBD GO:0005524 ATP binding at PTN001607041, the type IIA topoisomerase A-subunit (GyrA/ParC) node, seeded by M. tuberculosis GyrA P9WG47 and P. falciparum Q8I0X3. In gyrase and topoisomerase IV the ATP-binding GHKL domain is in the B subunit (GyrB/ParE); the A subunit cleaves and rejoins DNA. The IBD propagates ATP binding to every GyrA and ParC leaf of the node. Requested change: withdraw the IBD (or check whether the seed rows reflect holoenzyme assays, or a lineage-specific activity that should sit on a lower node). PROBABLE: the seed papers were not read.

> GyrA is responsible for the DNA strand binding, cleavage, and rejoining, and GyrB is responsible for ATPase activity.
> — PMID:10049263

## 80. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002211012
- **Subject:** UniProtKB:Q51507
- **Change:** check GO:0009697 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pchB/pchB-ai-review.yaml`

The IBD of GO:0009697 salicylic acid biosynthetic process at PTN002211012 rests on one seed, the PseudoCAP IDA of P. aeruginosa PchB (Q51507, isochorismate pyruvate lyase) to PMID:7500944. The seed is correct for PchB, but the node is the AroQ chorismate-mutase family root, the same node that carries the chorismate mutase IBD. Its other 16 leaves (QuickGO, 2026-10-28) are chorismate mutases, e.g. M. jannaschii AroQ Q57696, M. tuberculosis Rv1885c P9WIB9 and Rv0948c P9WIC1, P. aeruginosa AroQ Q9HU05, Yersinia PheA2 Q7CHH5 and fungal secreted CMs A7F9N9 and E3LB91, with no isochorismate pyruvate lyase activity; mycobacteria and Yersinia make salicylate with salicylate synthases instead. Please withdraw the IBD or move it to a node confined to PchB-type IPLs.

> PchB also produces prephenate from chorismate, most likely due to structural homology to the Escherchia coli chorismate mutase.
> — PMID:19432488

## 81. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002441861
- **Subject:** UniProtKB:Q9HZE4
- **Change:** check GO:0019213 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/pelA/pelA-ai-review.yaml`

The GO:0019213 deacetylase activity IBD at PTN002441861 (3 leaf IBAs) rests only on P. aeruginosa PelA (Q9HZE4, PseudoCAP IDA PMID:23504011). The activity belongs to PelA's C-terminal CE21 deacetylase domain (residues 520-804). The other leaves, Dictyoglomus turgidum B8DZ50 (518 aa; GH114 TIM barrel plus CARDB) and Deinococcus radiodurans Q9RWG2 (252 aa; TIM barrel only), are too short to contain that domain, by their UniProt domain features. Please move the IBD to a node containing only deacetylase-domain PelA orthologs, or add NOT for these leaves. The seed itself is sound. Domain content was read from UniProt/InterPro features, not from an alignment.

> The deacetylase domain of PaPelA (residues 520–804) has previously been predicted to have structural similarity to CE4 enzymes (18, 33).
> — PMID:40120681

## 82. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000763909
- **Subject:** UniProtKB:Q05098
- **Change:** check GO:0042912 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/pfeA/pfeA-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN000763909 is a SPECIATION node (Gammaproteobacteria) in PTHR30069 with 3 leaves, all subfamily PTHR30069:SF51, and exactly two children: the P. aeruginosa leaf PTN002409317 (Q05098 PfeA) and PTN002012591 (SPECIATION, Enterobacteriaceae; 2 leaves, E. coli FepA P05825 and S. typhimurium FepA Q8ZR40). The GO:0042912 colicin transmembrane transporter activity IBD is seeded by E. coli FepA, and colicin B/D uptake is a documented property of enterobacterial FepA only; no evidence shows PfeA admits colicins, and colicins B and D are not known to act on P. aeruginosa. Because the colicin-receptor leaves form one clean child clade, moving this IBD from PTN000763909 to PTN002012591 keeps both FepA IBAs and removes the only unsupported leaf IBA (PfeA). The sibling GO:0042930 enterobactin transport IBD is correct at PTN000763909 and should stay there.

## 83. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002463889
- **Subject:** UniProtKB:Q04804
- **Change:** delete the record asserting GO:0009927
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pfeS/pfeS-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. The node could not be resolved from its seeds automatically; it is in PTHR43711 (not PTHR45436, which is the PANTHER family UniProt cross-references for Q04804 - the two sources disagree, and PANTHER's own tree is what PAINT propagates on). PTN002463889 is the family's LUCA SPECIATION node: 200 leaves spread over ten subfamilies (SF1:80, SF26:42, SF31:43, SF28:19, SF32:4, SF15:3, SF29:3, SF13:2, SF18:2, SF30:2), with two children, PTN001976854 (SPECIATION, Archaea-Eukaryota; 65 leaves, SF1:60, SF15:3, SF18:2) and PTN002463899 (DUPLICATION; 135 leaves, all bacterial). The GO:0009927 histidine phosphotransfer kinase activity IBD is seeded only by Arabidopsis AT2G17820 (AHK1, Q9SXL4), which sits sixteen nodes deep inside the eukaryotic child PTN001976854, while P. aeruginosa PfeS (Q04804) is in the bacterial child, at PTN002463899 -> PTN008117710 -> PTN008117711 -> PTN008684377 -> PTN002536215. So a single plant hybrid-kinase seed is propagated across the whole bacterial half of the family, which includes E. coli BaeS (P30847), E. coli RcsC (P0DMC5) and M. tuberculosis PrrB (P9WGK7) as well as PfeS. PfeS has no HPt domain and no receiver domain: its architecture is HK_sensor-HAMP-HisKA-HATPase_c (Pfam PF16750, PF00672, PF00512, PF02518), so it cannot carry an HPt shuttle activity. Requested change: withdraw the IBD; if it is retained it must be moved at least to PTN001976854, which excludes every bacterial leaf, and better to a node restricted to HPt-domain-containing members. No such clade exists on the bacterial side of this tree.

> PF00512; HisKA
> — file:PSEAE/pfeS/pfeS-uniprot.txt

## 84. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000230115
- **Subject:** UniProtKB:P09786
- **Change:** delete the record asserting GO:0002047
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

PTN000230115 (PTHR43418:SF2, 7 reference leaves, 267 GOA rows in with/from of which 260 are TreeGrafter) carries an IBD of GO:0002047 phenazine biosynthetic process whose single seed is the PseudoCAP IMP row on P. aeruginosa phnB (UniProtKB:P09786, PMID:2153661). The other six leaves are trpG of Haemophilus influenzae, Shewanella oneidensis, Vibrio cholerae and Yersinia pestis and the bifunctional TrpGD of Escherichia coli and Salmonella Typhimurium - none of these organisms makes phenazines. The seed itself is an indirect phenotype: PhnAB is an anthranilate synthase, anthranilate is the precursor of the quinolone signal PQS, and PQS induces the phenazine operons, while the phenazine core is made from chorismate by PhzE through 2-amino-2-deoxyisochorismate without an anthranilate intermediate. Please consider removing this IBD; the clade's defensible assertions (anthranilate synthase activity and tryptophan biosynthesis) are already made at the ancestral node PTN000230074.

> Based on its organization in an operon and quinolone-dependent regulation, PhnAB has probably evolved to generate anthranilate for quinolone biosynthesis
> — PMID:23449919

## 85. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000230115
- **Subject:** UniProtKB:P09786
- **Change:** check GO:0004048 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

PTN000230115 (PTHR43418:SF2) carries an IBD of GO:0004048 anthranilate phosphoribosyltransferase activity whose single seed is E. coli P00904, the 531-residue bifunctional TrpGD. In that protein the activity comes from the fused TrpD region. Four of the node's seven leaves, including P. aeruginosa phnB (200 aa, a single glutamine amidotransferase domain at residues 2-195), are standalone TrpG subunits with no TrpD region, so they cannot have this activity. The IBD appears to be placed at the wrong node: it belongs on the TrpGD fusion clade (the Enterobacteriaceae node PTN001729070) rather than on the Gammaproteobacteria node that also contains standalone TrpG. 267 GOA rows currently descend from it.

> FT CHAIN 1..200
> — file:PSEAE/phnB/phnB-uniprot.txt

## 86. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000481936
- **Subject:** UniProtKB:Q7DC82
- **Change:** check GO:0002047 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phzC1/phzC1-ai-review.yaml`

PTN000481936 (PTHR21337, Proteobacteria, 5 leaves, all in PTHR21337:SF0) carries an IBD of GO:0002047 phenazine biosynthetic process whose single seed is the PseudoCAP IDA row on P. aeruginosa phzC1 (UniProtKB:Q7DC82, PMID:11591691). The seed is sound - that protein is the DAH7PS encoded within the phz operons - but the node is a generic type II DAHP synthase clade, and the decisive leaf is P. aeruginosa PA2843 (UniProtKB:Q9I000). That is not an inference from its name: Sterritt et al. (PMID:30242059) identify both P. aeruginosa type II DAH7PSs by locus tag, note that the seeded enzyme is the one inside the cluster ("PaeDAH7PSPA1901, found as a part of the phzA-G PCA biosynthetic cluster") and that PA2843 "is not found within the phzA-G PCA biosynthetic cluster", and conclude from the two solved structures that the type II enzymes "diverged to deliver type II enzymes that function within either primary or secondary metabolism". PA2843 retains the inserted alpha2a and alpha2b helices and the tetrameric, aromatic amino acid-inhibited assembly of MtuDAH7PS (PDB 5UXM, reported separately and cited as ref 33 there), whereas the phz enzyme lacks that sequence, is dimeric and is insensitive to aromatic amino acids. The sequence lengths confirm the identification independently: Q7DC82 is 405 aa and Q9I000 448 aa, exactly the 43-residue difference the paper reports between PaeDAH7PSPA1901 and PaeDAH7PSPA2843 - and Q7DC82 is the merged entry for both PA1901 and PA4212, so the characterised PaeDAH7PSPA1901 is the seed protein itself. The three remaining leaves (O24947 HP_0134, Q8PC31 dhs1, Q89NQ6 blr3778) carry no experimental annotation of any kind and their RecNames and EC numbers come only from UniRule RuleBase RU363071, so no claim is made from those names; at 449, 478 and 462 aa they fall in the longer, full-length type II group with PA2843 rather than with the 405-aa phz enzyme, and a UniProt gene query (2026-11-06) finds no phzB/D/E/F/G/M/S gene in Helicobacter pylori 26695, Xanthomonas campestris pv. campestris ATCC 33913 or Bradyrhizobium diazoefficiens USDA 110, against six such genes in PAO1 (a gene-name query, so suggestive rather than proof of cluster absence). All five leaves now carry the phenazine term by IBA. Please consider moving the IBD down to a node containing only the phz-cluster DAH7PS proteins, or retiring it; the clade's shared and correct assertion, GO:0003849 DAHP synthase activity, is already made at the family root PTN000481914.

> PaeDAH7PSPA1901, found as a part of the phzA–G PCA biosynthetic cluster, is 43 amino acids shorter in sequence length relative to PaeDAH7PSPA2843, which is not found within the phzA–G PCA biosynthetic cluster.
> — PMID:30242059

> The type II DAH7PSs are encoded by the ORFs PA1901 (and duplicated as PA4212) and PA2843 (PaeDAH7PSPA1901 and PaeDAH7PSPA2843 respectively). The structure and properties of PaeDAH7PSPA2843 have recently been reported
> — PMID:30242059

> evolutionary trajectory for the type II DAH7PSs may have diverged to deliver type II enzymes that function within either primary or secondary metabolism
> — PMID:30242059

## 87. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001286216
- **Subject:** UniProtKB:G3XD28
- **Change:** check GO:0043107 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/pilM/pilM-ai-review.yaml`

The IBD of GO:0043107 type IV pilus-dependent motility at PTN001286216 has one seed, P. aeruginosa PilM (G3XD28; PseudoCAP IMP, PMID:7565110 and PMID:19857645), which is sound for PilM. No other leaf of the 23 carries an experimental GO annotation of any kind (UniProt records for all 23 accessions checked 2026-11-06), so the node term rests entirely on this one gene. Domain content splits the clade. Fifteen leaves, the seed among them, match InterPro IPR005883 PilM with Pfam PF11104 PilM_2, and ten of those also match NCBIfam TIGR01175 pilM. Four others match none of the three PilM signatures and instead match InterPro IPR013366 EutJ with Pfam PF14450 FtsA at 274-279 aa: E. coli K-12 P77277 (b2454), Salmonella LT2 P0A206 (STM2462), Fusobacterium nucleatum Q8RI50 and Listeria monocytogenes Q8Y7V8 (lmo1161). The remaining four (Q8F3N4, Q7URQ4, Q74C92, Q9X104) match neither signature. For three of the four EutJ-signature leaves the non-pilus assignment does not rest on the protein name. Salmonella P0A206 carries curated experimental FUNCTION and DISRUPTION PHENOTYPE statements from eutJ deletion and eutJ/eutS overexpression (ECO:0000269 PubMed:10464203, PubMed:16585748, PubMed:27063436) that place it in the 17-gene eut operon and its bacterial microcompartment; E. coli b2454 lies in that operon's E. coli counterpart; and Listeria lmo1161 sits between lmo1160 phosphate propanoyltransferase and lmo1164 corrinoid adenosyltransferase in the cobalamin-dependent catabolic microcompartment locus. For Fusobacterium Q8RI50 the EutJ name is a SubName with ECO:0000313 (imported unchecked from the submitter) and is not evidence; its IPR013366 match and its lack of any PilM signature are. The tree offers no PilM-only node to move the IBD to: the smallest clade containing the seed together with other PilM-signature leaves is PTN001596234, which already holds P77277 and P0A206, and the Enterobacteriaceae clade below it (PTN002089606) is itself mixed, since Yersinia A0A0H2W2G1 carries the PilM signature. Please restrict the IBD with NOT/IKR on the four EutJ-signature leaves rather than by moving it. This affects about 23 leaf IBAs.

> PilM has shared sequence motifs with the cell division protein FtsA from Bacillus subtilis and Escherichia coli, as well as the rod-shape-determining protein MreB
> — PMID:7565110

## 88. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001286216
- **Subject:** UniProtKB:G3XD28
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilM/pilM-ai-review.yaml`

The IBD of GO:0044096 type IV pilus (is_active_in) at PTN001286216 rests only on a PseudoCAP IMP of P. aeruginosa PilM (G3XD28, PMID:7565110), which records that pilM mutants lack fimbriae, a mutant phenotype rather than a location. PilM is a cytoplasmic actin-like protein that associates with the inner membrane through PilN; it is part of the assembly machine, not of the surface fibre that GO:0044096 defines, and G3XD28's own experimental location annotation is GO:0005737 cytoplasm (EXP:UniProtKB). The node is also not uniformly a pilus clade: four of its 23 leaves (E. coli P77277, Salmonella P0A206, Fusobacterium Q8RI50, Listeria Q8Y7V8) lack the PilM signatures that the seed carries (IPR005883, PF11104, TIGR01175) and match InterPro IPR013366 EutJ instead, and no leaf other than the seed has any experimental annotation. Please withdraw the IBD; about 23 leaf IBAs are affected.

> all four proteins, including the nominally cytoplasmic PilM, colocalized to the inner membrane
> — PMID:19857645

## 89. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002220336
- **Subject:** UniProtKB:G3XD30
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilN/pilN-ai-review.yaml`

The IBD of GO:0044096 type IV pilus at PTN002220336 (dated 2026-06-17) rests only on the PseudoCAP IMP of P. aeruginosa PilN (G3XD30, PMID:7565110), which records that pilM-P mutants lack fimbriae, a phenotype rather than a location. PilN is a bitopic inner-membrane alignment-subcomplex protein; the plasma membrane IBD on the same node is the correct location. Please withdraw the type IV pilus IBD (7 leaf IBAs in 6 taxa). The motility and assembly IBDs on this node are sound.

> all four proteins, including the nominally cytoplasmic PilM, colocalized to the inner membrane
> — PMID:19857645

## 90. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000766390
- **Subject:** UniProtKB:G3XCX3
- **Change:** GO:0016888 → GO:0016887 (ATP hydrolysis activity)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/pilU/pilU-ai-review.yaml`

The IBD of GO:0016888 "DNA endonuclease activity, producing 5'-phosphomonoesters" at PTN000766390 (PilU clade of PTHR30486) has a single seed, the PseudoCAP IDA on P. aeruginosa PilU (G3XCX3, PA0396) citing Chiang et al. 2008 (PMID:18174131). That paper measures ATPase activity of purified PilB, PilT and PilU; its abstract reports no nuclease activity, and PilU is a PilT-like retraction ATPase with no nuclease domain. The seed is a keying error for the adjacent id GO:0016887 ATP hydrolysis activity. Please remove the DNA endonuclease IBD from this node (withdrawing about 13 leaf IBAs); if an MF is wanted at this node, ATP hydrolysis activity is the term the seed paper supports. The node's type IV pilus-dependent motility IBD is unaffected.

> Assay of purified 6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all three proteins have ATPase activities in vitro.
> — PMID:18174131

## 91. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002147059
- **Subject:** UniProtKB:Q9I4X1
- **Change:** check GO:0044550 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pqsC/pqsC-ai-review.yaml`

The IBD of GO:0044550 secondary metabolite biosynthetic process at PTN002147059 (PTHR34069) has a single seed, P. aeruginosa PqsC (Q9I4X1), whose PseudoCAP IMP (PMID:12426334, pqsC transposon mutant lacking PQS) is sound for PqsC. But the node sits above canonical type II fatty acid synthase FabH (KAS III) enzymes, and the PAINT leaf file propagates the term to them: Haemophilus influenzae FabH (P43711), Bacillus subtilis FabHB (O07600), P. aeruginosa FabH (Q9HYR2) and PA3286 (Q9HYV7), Plasmodium falciparum FabH (Q7KWI9), Chlamydia FabH (O84242) and others, 30 leaves in all. These initiate primary fatty acid synthesis and do not make secondary metabolites. Please move the IBD down to the node that holds only PqsC orthologues, or drop it.

## 92. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002463206
- **Subject:** UniProtKB:Q9I1N6
- **Change:** delete the record asserting GO:0044010
- **Recorded in:** `genes/PSEAE/pslC/pslC-ai-review.yaml`

The GO:0044010 single-species biofilm formation IBD at PTN002463206 (7 leaf IBAs) rests only on P. aeruginosa PslC (Q9I1N6, PseudoCAP IDA PMID:19659934). That evidence is a deletion-mutant phenotype (loss of Psl and surface attachment), and biofilm formation is a downstream outcome of Psl synthesis. None of the other six leaves carries an experimental GO annotation (UniProt records checked 2026-11-06), and only one is characterised at all: Salmonella RfbN (P26403) is a reviewed entry at protein level whose rhamnosyltransferase activity on the galactosyl-undecaprenyl-diphosphate intermediate is curated from experiment (ECO:0000269 PubMed:7684736). Its product is the LPS O-antigen, not a biofilm matrix polysaccharide, and it is PslC's closest relative here, the only other leaf in PTHR43685:SF13. The remaining five are uncharacterised, and their stated specificities are predicted names rather than evidence: Bradyrhizobium Q89D69 "exoU, UDP-hexose transferase", P. aeruginosa Q9I4N8 "FgtA" and Q9I3V4 "probable glycosyl transferase", Geobacter Q74CL7 and Xanthomonas Q8P4N7 all carry SubName or Pfam-derived names (ECO:0000313 or ECO:0000259) at protein existence "Predicted". What is checkable about them is domain content, and it does not support a shared function either: four share only the GT-2 catalytic domain with PslC (Pfam PF00535, 231-344 aa), while Q9I4N8 does not even do that, being a 1694-aa TagF-like protein (Pfam PF04464, InterPro IPR007554) with no GT-2 match. Nothing at this node outside the P. aeruginosa psl locus is known to make a biofilm matrix polymer, so the term is a gene-specific outcome rather than a family-level claim; please remove the IBD.

> Enzymes in the GT-2 family transfer a wide variety of nucleotide activated sugars (including glucose, rhamnose, and mannose), so it is difficult to speculate which of these substrates PslC specifically recognizes.
> — PMID:21991261

## 93. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002215317
- **Subject:** UniProtKB:G3XDA6
- **Field:** GO_ID
- **Change:** delete the record asserting GO:1900378
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ptrB/ptrB-ai-review.yaml`

The IBD of GO:1900378 positive regulation of secondary metabolite biosynthetic process at PTN002215317 (PTHR38777, DksA/TraR C4 zinc-finger proteins; 8 leaf IBAs in 5 taxa) has a single seed, a PseudoCAP IMP on P. aeruginosa PtrB (PA0612) citing Wu and Jin 2005 (PMID:16109947). That paper shows PtrB represses the type III secretion system and reports no secondary-metabolite phenotype; pyocin genes are activated by PrtN, not PtrB, and pyocins are protein bacteriocins. The leaves are phage- and plasmid-borne DksA/TraR-like proteins. Please withdraw this IBD.

> Therefore, PtrB is a new TTSS repressor that coordinates TTSS repression and pyocin synthesis under the stress of DNA damage.
> — PMID:16109947

## 94. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001083175
- **Subject:** UniProtKB:Q9I524
- **Change:** check GO:0008893 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/relA/relA-ai-review.yaml`

The IBD of GO:0008893 guanosine-3',5'-bis(diphosphate) 3'-diphosphatase activity at PTN001083175 (seed E. coli SpoT P0AG24) propagates to the RelA leaves of the node (e.g. E. coli P0AG20, P. aeruginosa Q9I524, Vibrio, Salmonella, Haemophilus RelA). Proteobacterial RelA lost hydrolase activity after the Rel duplication (Atkinson et al. 2011). Please move the IBD to the SpoT subclade (and Rel leaves), or add a NOT/loss at the RelA subclade node.

> while RelA is clearly more divergent, consistent with its loss of hydrolase activity
> — PMID:21858139

## 95. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002105365
- **Subject:** UniProtKB:Q9HX69
- **Change:** check GO:0005886 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/rocR/rocR-ai-review.yaml`

The IBD of GO:0005886 plasma membrane (is_active_in) at PTN002105365 is seeded by membrane-anchored E. coli EAL proteins, but the 162-leaf clade also contains soluble EAL proteins, including P. aeruginosa RocR (Q9HX69, REC-EAL, tetramer in solution, no TM segment) and PA2133 (Q9I1Y2, a 285-aa lone EAL domain, no TM segment). Please move the PM IBD to the membrane-anchored sub-clades or add NOT annotations at the soluble branches. This defect covers the shared node for bifA, PA2133, PA2200, nbdA and rocR.

> a finding consistent with the observation that RocR forms tetramers in solution
> — PMID:22753070

## 96. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002105365
- **Subject:** UniProtKB:Q9HX69
- **Change:** check GO:0071111 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/rocR/rocR-ai-review.yaml`

The GO:0071111 IBD at PTN002105365 is sound for the clade as a whole and does not depend on any single P. aeruginosa seed. However, the leaf GAF (queried 2026-11-05) shows the IBA reaching proteins with degenerate EAL domains that are not c-di-GMP PDEs, with no NOT annotation, including E. coli CsrD (P13518), E. coli YdiV (P76204), Salmonella YdiV (Q8ZPS6) and E. coli BluF (P75990). CsrD was shown not to hydrolyse c-di-GMP. Please add NOT/loss annotations at these branches. This defect covers the shared node for bifA, PA2133, PA2200, nbdA and rocR.

> These results suggested that the EAL domain of CsrD activity does not hydrolyze c-di-GMP.
> — PMID:16980588

## 97. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000779307
- **Subject:** UniProtKB:P45684
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0003899
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/rpoS/rpoS-ai-review.yaml`

The PAINT IBD of GO:0003899 DNA-directed RNA polymerase activity (enables) at PTN000779307 (PTHR30603, sigma-70 family) is seeded only by Arabidopsis SIG3 (AT3G53920; TAIR IMP PMID:17175536, ISS PMID:9280303) and propagates to 419 leaves in 77 taxa, including bacterial RpoD, RpoS and SigA. Sigma subunits have no catalytic site; the polymerase activity belongs to the core enzyme, and the sigma activity is GO:0016987 sigma factor activity, which the same node already carries. Please withdraw this IBD (or, if the seed is kept, use contributes_to rather than enables). PROBABLE because the TAIR seed papers were not read.

> Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released.
> — file:PSEAE/rpoS/rpoS-uniprot.txt

## 98. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000561806
- **Subject:** UniProtKB:Q9X4P2
- **Change:** check GO:0000290 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/rppH/rppH-ai-review.yaml`

The PTN000561806 IBD of GO:0000290 deadenylation-dependent decapping of nuclear-transcribed mRNA (eukaryotic seeds only) reaches the bacterial RppH leaf Q9X4P2. Please either move the IBD below the split from the bacterial RppH clade or add a NOT on the bacterial RppH subclade (PTN001500664). This node is not seeded by PseudoCAP; recorded because the propagation is a taxon mismatch.

## 99. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000159726
- **Subject:** UniProtKB:Q9HVQ3
- **Change:** add the content described in the explanation to GO:0004586
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/speC/speC-ai-review.yaml`

The PTN000159726 IBD of GO:0004586 ornithine decarboxylase activity propagates to the antizyme inhibitor 1 subclade, e.g. human AZIN1 (O14977) and chicken AZIN1 (A0A1D5PIE4), which are enzymatically inactive ODC paralogs (UniProt curated function). The AZIN2 branch already carries a NOT at PTN000159772, but the AZIN1 branch has none (live QuickGO query, 2026-11-05). Please add a NOT for GO:0004586 at the AZIN1 subclade node. The IBD itself is sound for the ODC members, including P. aeruginosa SpeC.

> AZI is an enzymatically inactive ODC homolog that counteracts the negative effect of ODC antizymes
> — file:PSEAE/speC/speC-notes.md

## 100. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000168372
- **Subject:** UniProtKB:Q9HV34
- **Field:** With/From
- **Change:** remove GO:0010487 from With/From
- **Recorded in:** `genes/PSEAE/speE2/speE2-ai-review.yaml`

The thermospermine synthase activity (GO:0010487) IBD at PTN000168372 is seeded by the multifunctional S. solfataricus SpeE (Q9UXE4) and the plant thermospermine synthase ACL5 (AT5G19530), but the node also contains dedicated putrescine aminopropyltransferases (spermidine synthases) such as P. aeruginosa SpeE2 (Q9HV34, HAMAP MF_00198, EC 2.5.1.16). The thermospermine-synthase MF should sit on the thermospermine-synthase sub-clade rather than the whole family node, so that spermidine synthases receive spermidine synthase activity (GO:0004766) instead. Full enzymatic characterisation of SpeE2 would settle whether it has any thermospermine side activity.

> Catalyzes the irreversible transfer of a propylamine group
> — file:PSEAE/speE2/speE2-uniprot.txt

## 101. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN008624361
- **Subject:** UniProtKB:Q9I6J0
- **Change:** add the content described in the explanation to GO:0015847
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/spuE/spuE-ai-review.yaml`

The PTN008624361 IBD of GO:0015847 putrescine transport (seeds E. coli PotF and PotD) propagates to P. aeruginosa SpuE (Q9I6J0), whose curated function says it does not bind putrescine (PMID:22300763). Please add a NOT for GO:0015847 on the SpuE leaf or its subclade. PROBABLE rather than CONFIRMED because SpuE works in the SpuDEFGH transporter alongside the putrescine-binding SpuD, and the full text was not read.

> Binds spermidine with high affinity (KD=14.3 nM). Does not bind putrescine, cadaverine or spermine.
> — file:PSEAE/spuE/spuE-uniprot.txt

## 102. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN008624361
- **Subject:** UniProtKB:Q9I6J0
- **Change:** add the content described in the explanation to GO:0019810
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/spuE/spuE-ai-review.yaml`

The PTN008624361 IBD of GO:0019810 putrescine binding (seeds SpuD, E. coli PotF and PotD) propagates to P. aeruginosa SpuE (Q9I6J0). The abstract of PMID:22300763 states that SpuE binds spermidine exclusively, and UniProt's curated function records no putrescine binding. Please add a NOT for GO:0019810 on the SpuE leaf or its subclade. The IBD itself is sound for the seeds.

> we found that SpuD is a putrescine-preferential binding protein, while SpuE binds to spermidine exclusively.
> — PMID:22300763

## 103. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002126683
- **Subject:** UniProtKB:Q9HZX3
- **Change:** check GO:0003810 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/tgpA/tgpA-ai-review.yaml`

The IBD of GO:0003810 protein-glutamine gamma-glutamyltransferase activity at PTN002126683 rests on one seed, P. aeruginosa TgpA (Q9HZX3), and propagates to 17 leaves in 15 taxa, none of which is functionally characterised. Two reasons to reconsider the term. First, the seed evidence is a colorimetric kit assay on the isolated periplasmic domain with a blocked dipeptide acyl donor and biotin-cadaverine as amine donor; GO:0003810 is defined as the protein-to-protein isopeptide cross-linking reaction, which was not assayed and for which no TgpA substrate is known. Second, the transglutaminase-like domain (PF01841) is a papain-like fold that supports several chemistries, and the nearest characterised relative cited by the same authors, Bordetella bronchiseptica WbmE, is a periplasmic deamidase of LPS O-antigen uronamides rather than a cross-linking transglutaminase. A more general node term, for example GO:0016755 aminoacyltransferase activity, or restricting the IBD to Pseudomonas TgpA orthologues, would fit the evidence better.

> In the periplasm of B. bronchiseptica, WbmE protein catalyzes the deamidation of uronamide-rich O chains of lipopolysaccharide (LPS)
> — PMID:23209712

## 104. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001804941
- **Subject:** UniProtKB:Q9HU66
- **Change:** remove GO:0052837
- **Recorded in:** `genes/PSEAE/thiI/thiI-ai-review.yaml`

The IBD of GO:0052837 thiazole biosynthetic process at PTN001804941, the root of the ThiI family PTHR43209, has a single seed: the PseudoCAP IDA on P. aeruginosa PA5118 citing PMID:9209060, which its abstract states is a Salmonella typhimurium gene characterisation, with no P. aeruginosa work described. The root node also covers short ThiI proteins (most Firmicutes and archaea) that lack the C-terminal rhodanese domain; in B. subtilis (PMID:22773787) and Methanococcus maripaludis (PMID:22904325) ThiI is needed for 4-thiouridine but not for thiamine, and Salmonella work shows the rhodanese domain is what thiazole synthesis requires (PMID:21724998). Please remove the thiazole IBD from the family root; if wanted, place it at the rhodanese-domain (proteobacterial) subclade, seeded by experimental annotations of E. coli or Salmonella ThiI.

> proteins annotated as ThiI based on containing only the AANH and THUMP domains are unlikely to be involved in thiazole synthesis and would be better annotated as 4-thiouridine sulfurtransferases
> — PMID:21724998

## 105. MISSING_NEGATION (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001464661
- **Subject:** UniProtKB:P29364
- **Change:** check UniProtKB:O34640 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thrB/thrB-ai-review.yaml`

Topology checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05. PTN001464661 is a SPECIATION node (Eubacteria) in PTHR21064 with 10 leaves, all subfamily PTHR21064:SF6, and five children: PTN007684856 (SPECIATION, Terrabacteria; 3 leaves: Chloroflexus A9WJ27 and the Bacillus clade PTN001843206 with B. subtilis AmiN O34640 and B. cereus Q81HY9), the single leaves PTN001843208 (Deinococcus Q9RXC1, uncharacterised), PTN002326065 (Synechocystis P73341, uncharacterised) and PTN001843209 (Fusobacterium Q8RF07, named homoserine kinase), and PTN002326066 (SPECIATION, Proteobacteria; 4 leaves: P. aeruginosa ThrB P29364, Neisseria Q4W557, Bradyrhizobium Q89UU4, Xanthomonas Q8PCP9). Every leaf with evidence of homoserine kinase function sits in PTN002326066, the smallest clade holding P29364, Q4W557 and Q89UU4; the one leaf with its own experimental activity, AmiN, phosphorylates amicoumacin A and sits in a separate child clade in an organism that has an unrelated GHMP-family ThrB. Please move the GO:0004413 homoserine kinase activity and GO:0009088 L-threonine biosynthetic process IBDs from PTN001464661 to PTN002326066, which drops the Terrabacteria clade (including O34640, where a NOT annotation would otherwise be needed) and the two uncharacterised leaves. The smallest clade holding both P29364 and the Fusobacterium leaf is PTN001464661 itself, so if FN0922 is a genuine type II homoserine kinase it needs its own IBD at PTN001843209 rather than retention of the Eubacteria-level node.

> B. subtilis 168 has an amiN homolog (yerI) that also phosphorylates Ami, mediating natural B. subtilis resistance to the drug.
> — PMID:30181282

## 106. OUTDATED_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002454730
- **Subject:** UniProtKB:P57668
- **Change:** GO:0008379 → GO:0140824 (thioredoxin-dependent peroxiredoxin activity)
- **Recorded in:** `genes/PSEAE/tpx/tpx-ai-review.yaml`

The IBD at PTN002454730 (thiol peroxidase clade, 32 leaf IBAs in 30 taxa) uses GO:0008379, which the current GOA file labels 'obsolete thioredoxin peroxidase activity'. Both seeds, E. coli Tpx and P. aeruginosa Tpx, reduce organic hydroperoxides as well as H2O2 with thioredoxin, so the IBD should be moved to GO:0140824 thioredoxin-dependent peroxiredoxin activity. The IBD is otherwise sound.

> The enzyme catalyzes thioredoxin-dependent peroxidation and can utilize organic hydroperoxides and H(2)O(2) as substrates.
> — PMID:22609922

## 107. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001575314
- **Subject:** UniProtKB:Q9HUF5
- **Change:** check GO:0008713 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaC/waaC-ai-review.yaml`

The IBD of GO:0008713 (heptosyl-Kdo2-lipid A + ADP-heptose, the heptosyltransferase II reaction) at PTN001575314 rests on one seed, E. coli WaaF P37692. The same node's GO:0009244 IBD is seeded by WaaC (E. coli P24173, Salmonella P26469, PAO1 Q9HUF5), WaaF (P37692, P37421, PAO1 G3XD35) and WaaQ (P25742), so the node spans heptosyltransferases I, II and III. WaaC proteins therefore receive the Hep II reaction, including E. coli WaaC P24173, whose experimental term is GO:0008920 (IDA, PMID:9446588). Please move the GO:0008713 IBD to the WaaF subclade, or replace it at this node with GO:0008920 lipopolysaccharide heptosyltransferase activity.

> Catalyzes the addition of the first heptose unit to one 3-deoxy-D-manno-octulosonic acid (Kdo) residue of the Kdo2-lipid A module
> — file:PSEAE/waaC/waaC-uniprot.txt

## 108. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000531351
- **Subject:** UniProtKB:Q9HUG5
- **Change:** remove GO:0009244
- **Recorded in:** `genes/PSEAE/wapR/wapR-ai-review.yaml`

The IBD of GO:0009244 lipopolysaccharide core region biosynthetic process at PTN000531351 has two seeds, both P. aeruginosa core rhamnosyltransferases (WapR, MigA; PseudoCAP IMP/IDA). The seeds are sound, but the node term does not suit the clade: the 18 leaf IBAs (10 taxa) include Salmonella RfbV (P26401), an O-antigen abequosyltransferase (IDA GO:0009243, GO:0047600; PMID:7541787), E. coli WcaA (P77414), a colanic acid glycosyltransferase (IDA GO:0009242; PMID:30821147), Yersinia WbyL, five Geobacter paralogues and GT2 proteins of Haemophilus, Helicobacter and Coxiella. Leaf IBAs and the experimental annotations of RfbV and WcaA were checked in the PAINT leaf file and live in QuickGO (2026-11-05). Please remove the IBD from this node, or move it to a descendant node restricted to the Pseudomonas core rhamnosyltransferases (MigA, WapR, PA1014) if one exists. The glycosyltransferase IBD at the parent PTN000531320 is sound and covers these proteins.

> These results provide evidence that WapR is the alpha-1,3-rhamnosyltransferase, while MigA is the alpha-1,6-rhamnosyltransferase.
> — PMID:18178733

## 109. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN001292385
- **Subject:** UniProtKB:G3XD01
- **Field:** GO_ID
- **Change:** GO:0006065 → GO:0009226 (nucleotide-sugar biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpD/wbpD-ai-review.yaml`

The IBD for GO:0006065 UDP-glucuronate biosynthetic process at PTN001292385 (PTHR43300; 8 leaf IBAs in 8 taxa) rests solely on the PseudoCAP EXP row for P. aeruginosa WbpD (G3XD01, PMID:16102001). WbpD is the UDP-GlcNAc3NA 3-N-acetyltransferase of the UDP-ManNAc3NAcA pathway and does not participate in UDP-glucuronate formation. Please re-annotate the node to GO:0009226 nucleotide-sugar biosynthetic process (and/or GO:0009243 O antigen biosynthetic process), seeded from the direct biochemistry in PMID:19348502 or PMID:19282284.

> we confirm that WbpD catalyzes the acetylation of UDP-GlcNAc(3NH(2))A to give UDP-GlcNAc(3NAc)A
> — PMID:19348502

## 110. MISSING_NEGATION (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001056041
- **Subject:** UniProtKB:G3XD61
- **Change:** add NOT GO:0008761 to UniProtKB:G3XD61
- **Recorded in:** `genes/PSEAE/wbpI/wbpI-ai-review.yaml`

PTN001056041 propagates GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity, seeded by E. coli WecB (sound) and P. aeruginosa WbpI (G3XD61). Purified WbpI does not use UDP-GlcNAc; it 2-epimerizes UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucuronate (EC 5.1.3.23, PMID:17346239). Once the two WbpI seed rows are corrected (PseudoCAP IMP PMID:10930727; UniProt IDA PMID:17346239), WbpI remains a leaf below a WecB-seeded IBD. Please add a NOT for GO:0008761 at WbpI, or at a WbpI/WlbD subclade if the tree has one. The IBD itself stands on WecB.

> Neither enzyme utilized UDP-alpha-D-GlcNAc, UDP-alpha-D-GlcNAcA (UDP-2-acetamido-2,3-dideoxy-alpha-D-glucuronic acid) or UDP-alpha-D-GlcNAc3NAc (UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucose) as substrates.
> — PMID:17346239

## 111. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN005302544
- **Subject:** UniProtKB:Q9HTB9
- **Field:** With/From
- **Change:** check PANTHER:PTN005302544 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpY/wbpY-ai-review.yaml`

The IBD for GO:0016757 glycosyltransferase activity at PTN005302544 (PTHR46401, GT4; 60 leaf IBAs in 22 taxa) is seeded only by PseudoCAP IMP rows for P. aeruginosa WbpY (Q9HTB9) and WbpX (G3XCU3) citing PMID:9680202, whose abstract reports mutant LPS phenotypes and hedged (probable/predicted) transferase assignments; full text not read. The conclusion is correct, but please re-seed with the direct in vitro D-rhamnosyltransferase evidence for both enzymes in PMID:35166992 so the node does not depend on a phenotype-based MF annotation.

> We demonstrated that these GTs are indeed D-RhaTs and catalyze the transfer of D-Rha from GDP-D-Rha to the reaction product of WbpZ.
> — PMID:35166992

## 112. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002895351
- **Subject:** UniProtKB:Q9HXT9
- **Change:** check GO:0005886 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wspR/wspR-ai-review.yaml`

The IBD of GO:0005886 plasma membrane at PTN002895351 rests on six E. coli transmembrane DGCs (P46139, P76330, P76236, P76147, P75801, P76237), all IDA from PMID:15919996. The node also covers soluble DGCs with no TM segment in UniProt and no hydrophobic window in a Kyte-Doolittle scan, for example P. aeruginosa WspR (Q9HXT9, a receiver-GGDEF response regulator), PA3177 (Q9HZ57), DgcP (Q9HT84) and PA4843/GcbA (Q9HUW7, receiver-receiver-GGDEF). Please move the IBD to subclades of membrane-anchored DGCs, or withdraw it.

> Kyte-Doolittle, 19-residue window, mean above 1.6: no window found in WspR (347 aa).
> — file:PSEAE/wspR/wspR-notes.md

## 113. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN002895351
- **Subject:** UniProtKB:Q9HXT9
- **Change:** check GO:0043709 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wspR/wspR-ai-review.yaml`

The IBD of GO:0043709 cell adhesion involved in single-species biofilm formation (involved_in) at PTN002895351 rests on one seed, E. coli DgcZ (P31129), whose own annotation is IMP with qualifier acts_upstream_of_or_within (EcoCyc, PMID:19460094; QuickGO 2026-11-05). The IBD upgrades that to involved_in and propagates it to diguanylate cyclases, which regulate adhesion through c-di-GMP rather than perform it. For one leaf, P. aeruginosa PA3177, loss of the gene has no effect on attachment (PMID:30082282). Please withdraw the IBD, or replace it with GO:1900189 positive regulation of cell adhesion involved in single-species biofilm formation on the subclades where that is shown.

> While PA3177 contributed to biofilm drug tolerance, inactivation of PA3177 had no effect on attachment and biofilm formation.
> — PMID:30082282

## 114. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN000794252
- **Subject:** UniProtKB:G3XCY2
- **Change:** check GO:0004713 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wzz/wzz-ai-review.yaml`

The IBD of GO:0004713 protein tyrosine kinase activity at PTN000794252 is seeded by the E. coli BY-kinases Wzc (P76387) and Etk (P38134). The same node's plasma-membrane IBD lists Wzz1 (PAO1 PA3160, G3XCY2), Wzz2 (PA0938, Q9I520) and E. coli FepE (P26266) among its seeds, which are PCP-1 chain-length regulators. Their sequences end shortly after the second TM helix (Wzz1 is 348 aa with TM2 at 319-343) and lack the cytoplasmic Walker A/B tyrosine-autokinase domain, so they cannot have this activity. Please move the kinase IBD to the Wzc/Etk (PCP-2a) subclade or add NOT for the PCP-1 branch.

## 115. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002446181
- **Subject:** UniProtKB:Q00516
- **Change:** check GO:0015627 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

The IBD of GO:0015627 type II protein secretion system complex at PTN002446181 (PTHR38779) has one seed, the PseudoCAP IDA of P. aeruginosa XcpV (Q00516, PMID:8331069). The term is right for XcpV, but of the 49 leaves receiving the IBA in current QuickGO only 14 are named as T2SS proteins (GspI and relatives), while 14 are named type IV pilus PilV, MSHA MshD or pilin, including Neisseria gonorrhoeae PilV (Q5F9E5, NGO_0453), and 21 carry only a generic prepilin-type domain name. The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05, and it reframes the problem. PTN002446181 is the root of PTHR38779: a SPECIATION node (Eubacteria) with 12 reference-proteome leaves, all PTHR38779:SF2, and three children - two deep single leaves that are not T2SS proteins (PTN002446182, Aquifex aeolicus ppdD3 "Pilin"; PTN002409471, Thermodesulfovibrio yellowstonii THEYE_A0597, a bare prepilin-type cleavage/methylation domain) and PTN002215342 (SPECIATION, Proteobacteria, 10 leaves), which contains every T2SS-named leaf in the tree: Geobacter GspI, Shewanella GspI, Vibrio EpsI, the Xanthomonas duplication PTN002215341 (XpsI, XcsI, XcsJ), the Pseudomonas duplication PTN002446183 (XcpV Q00516 and PA0680), and the Enterobacteriaceae pair PTN002215349 (E. coli GspI, Yersinia YPO0811). So the earlier reading, that the node spans a GspI/PilV split, is not what the tree shows: there is no PilV or MshD leaf in the reference tree, and the PilV/MshD proteins that carry the IBA are non-reference members grafted into the family by sequence (TreeGrafter), which the tree cannot place. The node-level problem that remains is real and narrower: the IBD sits at the family root, one node above the clade that supports it, so it covers the two deep generic prepilin branches as well as the GspI clade. Please move both this IBD and the GO:0015628 IBD down to PTN002215342, which is confined to T2SS minor pseudopilins; the grafted PilV/MshD members, being divergent, should then attach outside the annotated clade. If any of them still receive the term after the move, their PTHR38779:SF2 assignment is the next thing to check, not the node placement.

> The real fault is narrower: the IBD sits one node above PTN002215342 (Proteobacteria, 10 leaves), which holds every T2SS-named leaf including XcpV, while the root also covers two deep generic prepilins.
> — file:PSEAE/xcpV/xcpV-bioinformatics/RESULTS.md

## 116. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002446181
- **Subject:** UniProtKB:Q00516
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

The IBD of GO:0015628 protein secretion by the type II secretion system at PTN002446181 (PTHR38779) has one seed, the PseudoCAP IDA of XcpV (Q00516) citing the review PMID:9818381. The term is right for XcpV, but 14 of the 49 proteins receiving the IBA are named type IV pilus PilV, MSHA MshD or pilin (including Neisseria gonorrhoeae PilV Q5F9E5/NGO_0453). The topology was checked with projects/PSEUDOCAP/panther_tree.py on 2026-11-05: PTN002446181 is the root of PTHR38779, a SPECIATION node (Eubacteria) of 12 reference leaves, all SF2, whose two deepest branches are generic prepilins (Aquifex ppdD3, Thermodesulfovibrio THEYE_A0597) and whose third child PTN002215342 (SPECIATION, Proteobacteria, 10 leaves) contains every T2SS-named leaf, XcpV among them. No PilV or MshD protein is a leaf of the tree; those are non-reference members grafted into the family by sequence. Please move the IBD down to PTN002215342 together with the GO:0015627 IBD, and re-seed it with a primary reference (PMID:30346996, IMP). Detail and the leaf table are in the defect recorded on the GO:0015627 IBA row.

> The real fault is narrower: the IBD sits one node above PTN002215342 (Proteobacteria, 10 leaves), which holds every T2SS-named leaf including XcpV, while the root also covers two deep generic prepilins.
> — file:PSEAE/xcpV/xcpV-bioinformatics/RESULTS.md

## 117. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN001952271
- **Subject:** UniProtKB:Q9HT73
- **Change:** GO:0010043 → GO:0071578 (zinc ion import across plasma membrane)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

PTN001952271 (PTHR42734:SF9, 7 reference leaves, 1455 GOA rows in with/from of which 1448 are TreeGrafter) carries an IBD of GO:0010043 response to zinc ion whose single seed is the PseudoCAP IMP row on P. aeruginosa znuC (UniProtKB:Q9HT73, PMID:24086521). The leaves are the ZnuC ATPase subunits of the ZnuABC high-affinity zinc importer, so the clade is coherent, but the process they take part in is zinc import, not a response to a zinc stimulus: in the seeding paper the zinc-sensing component is Zur (Np20, PA5499), which represses the zur-znuC-znuB operon, and ZnuC is its regulatory target. Please consider re-pointing the IBD to GO:0071578 zinc ion import across plasma membrane (or GO:0071577 if the plasma-membrane restriction is thought too strong for some leaves).

> ZurPA is zinc responsive and represses transcription of both znuA and the zur-znuC-znuB operon in a zinc dependent manner.
> — PMID:24086521
