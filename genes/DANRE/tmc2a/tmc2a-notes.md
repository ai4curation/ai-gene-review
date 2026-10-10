# tmc2a notes (Danio rerio, transmembrane channel-like 2a; UniProt E7FFT2)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random TGD_tree sample)

**Deep research:** not available for this gene (Edison/Falcon returns 402 Payment Required; the OpenAI key
is invalid). Not attempted, per instructions. No `-deep-research-*.md` file exists; the literature search was
done by hand (Europe PMC query `(tmc2a OR tmc2b) AND zebrafish`, 49 hits; cached the primary papers listed
below). Shared pair material is also in `../tmc2b/tmc2b-notes.md`.

Accession E7FFT2 (Swiss-Prot TMC2A_DANRE, 916 aa), ZFIN:ZDB-GENE-060526-280, Ensembl ENSDARG00000033104,
chr5:55.22 Mb. Paralog tmc2b (F1QZE9, ZDB-GENE-060526-262) is also on chr5, at 25.62 Mb, 5 kb from tmc1.

### Origin of the pair
- Maeda 2014 named the pair: [PMID:25114259 "There are two zebrafish tmc2 genes in the Ensembl genome database (release 73), and we designated the paralogous gene isolated in the screen as tmc2a , and the gene duplicate as tmc2b ."]
- All three tmc1/2 genes on chr5: [PMID:25114259 "All three genes are located on chromosome 5, with tmc1 and tmc2b directly adjacent to one another ( Fig. S2 )."]
- Zhu 2020 attributes the pair to the TGD (citation, not an analysis): [PMID:33490059 "Tmc2a and tmc2b paralogs are the result of a whole-genome duplication that occurred in teleost fish between 300 and 450 million years ago (Taylor et al., 2001)."]
- My analysis (`tmc2a-bioinformatics/RESULTS.md`): Ensembl Compara places the duplication at Osteoglossocephalai;
  one gar orthologue for both. Both copies sit in segments whose genes map to human 9q21 (the TMC1 region) and
  to gar LG2. The gar TMC2 anchor is on LG2 near the gar orthologues of the tmc2b neighbourhood; the tmc2a
  neighbourhood maps to LG2 but farther from the anchor. Same zebrafish chromosome for both copies is unusual
  for TGD ohnologs; see RESULTS.md.

### Protein
- 68% identity to tmc2b (compare_pair.py); 71.8% to gar TMC2 vs 67.2% for tmc2b (my script): tmc2b has
  diverged slightly more from the outgroup sequence.
- N-terminus binds Pcdh15a cytoplasmic domain (Y2H, co-IP): [PMID:25114259 "Tmc2a interacted with both CD1 and CD3 isoforms of Pcdh15a, demonstrating that binding is not restricted to a particular Pcdh15a isoform."]
- Dominant-negative N-terminal fragment: [PMID:25114259 "Overexpression of the Tmc2a N terminus results in mislocalization of Pcdh15a within hair bundles, together with a significant decrease in mechanosensitive responses, suggesting that a Pcdh15a–Tmc complex is critical for mechanotransduction."]
- A Tmc2a-mEGFP transgene failed to express, so no Tmc2a localization or rescue data exist: [PMID:32371604 "The Tg(myo6b:tmc2a-mEGFP-pA) construct failed to express Tmc2a-mEGFP."]

### Expression
- Inner ear from 1 dpf: [PMID:25114259 "We observed that tmc2a is expressed in the nascent hair cells of the developing ear as early as 1 dpf, and expression in the inner ear continues throughout development ( Fig."]
- Ear-biased: [PMID:25114259 "However, semiquantitative PCR with larval tissues suggests that tmc2a is expressed predominantly in the inner ear, whereas tmc1 and tmc2b appear to be more abundant in lateral-line hair cells."]
- Lateral line: low; [PMID:29269857 "According to RNA in situ hybridization studies of zebrafish larva, tmc2b is robustly expressed in hair cells of the lateral line, but the mRNAs of the paralogs tmc2a and tmc1 are present at much lower levels and cannot be detected by this method."]
- Only in P-to-A hair cells of neuromasts: [PMID:36905930 "Interestingly, Tmc2b and Tmc2a proteins, which constitute the mechanotransduction channels in neuromasts, distribute asymmetrically so that Tmc2a is expressed in hair cells of only one orientation."]
- Striolar/central zones of ear, upper crista layer: [PMID:38035267 "tmc1, tmc2b, and cib3 are largely expressed in peripheral or extrastriolar hair cells, whereas tmc2a and cib2 are enriched in central or striolar hair cells."]
- Ear gene repressed by prdm1a in lateral line: [PMID:40825768 "In the sibling lateral line, tmc2a is only expressed in a few sibling lateral line hair cells, but is expressed in all ear (lateral crista) hair cells (Fig. 2h, o, p, t)73."]
- mRNA stability controlled by Esrp1/2 (tmc2b not): [PMID:40086870 "Meanwhile, our data demonstrated that Esrp1/2 regulates the mRNA stability of tmc1 and tmc2a but not tmc2b ."]

### Function (mutants)
- Alleles: cwr3 (CRISPR, exon 6, 2-bp del, PTC; Chou 2017), cwr6/cwr7 (Chen/Zhu), Ex4 −23bp (TALEN; Smith 2020).
- Lateral line: double tmc2a/tmc2b abolishes MET; residual in tmc2b single depends on tmc2a: [PMID:29269857 "Overall, these findings indicate that the residual activity in the tmc2b −/− mutant is dependent on Tmc2a."]
- Hearing: tmc2a single mutant reduces saccular microphonics: [PMID:32371604 "Interestingly, the tmc2a single mutants ( n = 8) had significantly reduced microphonic signals compared with WT siblings ( n = 7) and were the only single-gene mutants with such a deficit ( p = 0.001; t = 4.34; df = 8.36) ( Fig. 7 A )."]
- [PMID:32371604 "Together, these results demonstrate a Tmc2a > Tmc2b > Tmc1 hierarchy in the detection of sound."]
- Crista upper layer (teardrop cells) needs Tmc2a: [PMID:32371604 "Together, our experiments reveal that, in cristae, hair cells stratify into an upper, Tmc2a-dependent layer of teardrop-shaped cells, and a lower, Tmc1/2b-dependent tier of gourd-shaped cells."]
- Utricle high-frequency sensitivity: [PMID:37952940 "We found that Tmc2a function correlates with the broadest range of frequency sensitivity, whereas Tmc2b mainly contributes to lower-frequency responses."]
- Neuromast asymmetry lost without tmc2a: [PMID:36905930 "Remarkably, loss of Tmc2a does not impact hair cell orientation but abolishes the functional asymmetry as measured by recording extracellular potentials and calcium imaging."]
- No paralog upregulation in tmc1 mutants [PMID:32167554 "Expression of tmc2a mRNA or tmc2b mRNA in the tmc1 mutants did not increase and was similar to controls ( Supplementary Material, Figure S2 )."]; none in tmc2b mutants [PMID:29269857 "These findings indicate that these genes are not upregulated in response to genetic inactivation of tmc2b."]
- Cross-rescue: Tmc2b-mEGFP rescues all end organs of tmc1/2a/2b triple mutants [PMID:32371604 "The results described above (1) confirm the expectation that concurrent disruption of tmc1/2a/2b leads to complete loss of MET activity and (2) reveal that exogenous Tmc2b-mEGFP can rescue auditory/vestibular deficits and restore FM labeling in all mechanosensory end organs."]. No reciprocal Tmc2a transgene exists.

### Annotation decisions (summary)
- Voltage-gated calcium channel IBA: MODIFY to GO:0140135 (mechanically gated), as in the human TMC1 review.
- protein binding IPI (Pcdh15a): MODIFY to cadherin binding (GO:0045296); Pcdh15a is a cadherin-superfamily tip-link protein and the binding is mapped to the Tmc2a N-terminus.
- IEP development terms (lateral line development, inner ear receptor cell development): REMOVE; expression is not
  participation, and hair bundles develop normally in tmc triple mutants.
- GO:0050910 IGI from Chou 2017 (lateral line data only): MODIFY to GO:0050974.
