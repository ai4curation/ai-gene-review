---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:36:14.540039'
end_time: '2026-10-26T03:46:21.046596'
duration_seconds: 606.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: PTPRN2
  gene_symbol: PTPRN2
  uniprot_accession: A0A9L0T4W6
  protein_description: 'RecName: Full=Protein-tyrosine-phosphatase {ECO:0000256|PROSITE-ProRule:PRU10044};
    EC=3.1.3.48 {ECO:0000256|PROSITE-ProRule:PRU10044};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: IA-2/IA-2_beta. (IPR033522); Prot-tyrosine_phosphatase-like. (IPR029021);
    PTP_cat. (IPR000242); Receptor_IA-2_dom. (IPR021613); Receptor_IA-2_ectodomain_sf.
    (IPR038112)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 90
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0T4W6
- **Protein Description:** RecName: Full=Protein-tyrosine-phosphatase {ECO:0000256|PROSITE-ProRule:PRU10044}; EC=3.1.3.48 {ECO:0000256|PROSITE-ProRule:PRU10044};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** IA-2/IA-2_beta. (IPR033522); Prot-tyrosine_phosphatase-like. (IPR029021); PTP_cat. (IPR000242); Receptor_IA-2_dom. (IPR021613); Receptor_IA-2_ectodomain_sf. (IPR038112)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PTPRN2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PTPRN2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PTPRN2** (gene ID: PTPRN2, UniProt: A0A9L0T4W6) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PTPRN2 (IA-2β / phogrin) in the horse, *Equus caballus* (UniProt A0A9L0T4W6): a research review for functional annotation

## 1. Introduction and summary

The horse protein A0A9L0T4W6 is an unreviewed, computationally annotated TrEMBL entry described only as a "protein-tyrosine-phosphatase" (EC 3.1.3.48). Its EC number and catalytic-activity line come from a generic PROSITE rule, and its subcellular location (secretory vesicle membrane, synapse) comes from automatic ARBA rules [uniprot-A0A9L0T4W6-entry]. The entry gives no gene name. However, it comes from Ensembl gene ENSECAG00000012762 on horse chromosome 4, which Ensembl names *PTPRN2*, "protein tyrosine phosphatase receptor type N2 [HGNC:9677]" [ensembl-ENSECAG00000012762-lookup]. The record also carries the IA-2/IA-2β family signature (IPR033522), the IA-2 receptor ectodomain (IPR021613/IPR038112, including a RESP18 homology domain) and the PANTHER subfamily PTHR46106:SF5, "receptor-type tyrosine-protein phosphatase N2" [uniprot-A0A9L0T4W6-entry]. In our own pairwise alignment, the horse sequence is 66% identical to human PTPRN2/IA-2β (Q92932) over the human length and nearly identical across the cytoplasmic domain, but only 43% identical to its paralogue PTPRN/IA-2 (SEQUENCE_ANALYSIS.md). The gene symbol PTPRN2 is therefore correct and unambiguous, and the protein is the horse orthologue of IA-2β, also called phogrin ("phosphatase on the granule of insulinoma cells"). We found no horse-specific experimental literature, so everything about its function below is inferred from orthologues: mainly rat, mouse and human phogrin/IA-2β.

In brief, PTPRN2 is a single-pass type I transmembrane glycoprotein of the receptor protein tyrosine phosphatase (RPTP) family. It sits on the membrane of dense-core secretory granules (DCVs) in neuroendocrine cells, and in neurons also on synaptic-vesicle-rich fractions. Its single PTP-like domain faces the cytosol [wasmeier-1996-phogrin-cloning][nishimura-2009-neurotransmitter-secretion]. Despite the UniProt EC 3.1.3.48 label, phogrin is classed as a pseudophosphatase. Substitutions at three catalytic-region positions leave it essentially inactive against conventional phosphotyrosine substrates [drake-2003-ia2-phogrin-inhibitors][barr-2009-ptpome-structures][stojilkovic-2025-ptprn-ptprn2-review]. Its best-supported enzymatic activity is instead a low-to-moderate phosphoinositide phosphatase activity toward PI(3)P and PI(4,5)P2, but not PI(3,4,5)P3. This activity depends on the catalytic cysteine and lowers plasma-membrane PI(4,5)P2 [caromile-2010-phogrin-pi-phosphatase][sengelaub-2016-ptprn2-plcb1-metastasis]. Physiologically, PTPRN2 helps maintain DCV number and stimulus-coupled secretion of insulin, other peptide hormones and monoamine neurotransmitters [kubosaki-2004-ia2beta-knockout][cai-2011-dense-core-vesicles][nishimura-2009-neurotransmitter-secretion]. In β-cells it also acts as a scaffold that binds the insulin receptor, keeping autocrine insulin signalling going through effects on PTP1B redox state and IRS2 stability [torii-2009-phogrin-silencing][torii-2018-pseudophosphatase-phogrin]. In humans it is also a major autoantigen in type 1 diabetes: it is the "37-kDa antigen" [lu-1996-ia2beta-autoantigen][hawkes-1996-37kda-antigen].

## 2. Gene identity, domain architecture and the horse gene model

Phogrin was first cloned from a rat insulinoma expression library as a 1004-residue transmembrane glycoprotein. It is about 80% identical to the diabetes autoantigen ICA512/IA-2 within its 260-residue PTP domain and 42% identical overall [wasmeier-1996-phogrin-cloning]. In parallel, a mouse brain cDNA, IA-2β, was isolated whose intracellular domain is 74% identical to IA-2 while its extracellular region is only 26% identical [lu-1996-ia2beta-autoantigen]. The human orthologue is a 1015-residue polypeptide that is more than 90% identical to the rat and mouse proteins [kawasaki-1996-human-phogrin]. The human and mouse genes have 23 exons and span about 1 Mb and 800 kb respectively [kubosaki-2004-ia2beta-knockout]. The horse gene (ENSECAG00000012762) spans about 950 kb of chromosome 4 [ensembl-ENSECAG00000012762-lookup]. That is consistent with the large mammalian locus and with the horse genome's extensive conserved synteny with human chromosomes [wade-2009-horse-genome].

The predicted horse protein is 976 residues long. It has a signal peptide (1–20), a luminal ectodomain, one transmembrane helix (568–592), a juxtamembrane region, and a PTP-like domain (697–923) with the predicted active-site cysteine at Cys897 [uniprot-A0A9L0T4W6-entry]. Our alignment with human PTPRN2 showed two departures from the human protein (SEQUENCE_ANALYSIS.md). First, about 32 residues of the N-terminal propeptide region are missing. Second, the last 43 residues (934–976) have no counterpart in the human protein and replace the conserved C-terminal segment of the PTP fold. Comparison with the four NCBI RefSeq models of horse PTPRN2 (isoforms X1–X4, 905–1005 residues) resolves both [ncbi-refseq-horse-ptprn2-isoforms-sequences]. All four RefSeq isoforms end with the canonical C-terminus, identical to human (…AKEIDIAATLEHLRDQRPGMVQTKEQFEFALTAVAEEVNAILKALPQ), so the divergent C-terminus of A0A9L0T4W6 is an Ensembl gene-model artefact. The missing N-terminal segment, by contrast, is present in isoform X1 and absent from isoform X3, which shows it is an alternatively included exon. The 1005-residue isoform X1 is therefore the best current representation of full-length horse PTPRN2 (924/1005 identical to A0A9L0T4W6 and 742/1015 identical to human PTPRN2 in our alignments). The rest of the cytoplasmic domain is highly conserved, including the juxtamembrane tyrosine-based sorting motif (horse "AYQELCRQRMA", corresponding to the rodent Y654QELCRQRMA motif [wasmeier-2005-tyrosine-motif-endocytosis]). The luminal portion holds the RESP18 homology domain/pro-region and a mature ectodomain (ME). For human phogrin the ME has been solved by X-ray crystallography at 1.95–2.01 Å. It adopts a ferredoxin-like fold, four antiparallel β-strands packed against two α-helices, and unlike the IA-2 ME it is monomeric [noguera-2015-phogrin-ectodomain-structure]. AlphaFold-based surveys of RPTP extracellular regions place this compact ectodomain in the broader structural landscape of the family [el-badaoui-2024-rptp-alphafold].

## 3. Catalytic activity: a pseudo-PTP with phosphoinositide phosphatase activity

The UniProt EC 3.1.3.48 annotation (protein-tyrosine-phosphate phosphohydrolase) is a generic rule-based call [uniprot-A0A9L0T4W6-entry], and the primary literature does not support it as written. IA-2 and phogrin are "characterized by a lack of activity against conventional PTP substrates". Drake and colleagues made them catalytically competent by "back-mutating" just three non-consensus residues to the PTP1B consensus, at the positions equivalent to PTP1B Tyr46, Asp181 and Ala217. Their kinetic analyses also showed that the overall fold is that of a classical PTP [drake-2003-ia2-phogrin-inhibitors]. The Structural Genomics Consortium solved the human IA-2β PTP domain (PDB 2QEP) as part of the classical phosphatome. It grouped IA2 and IA2β as R8 pseudophosphatases, in which the gateway and second-site loops are open and the phosphate-binding loop carries a substitution (alanine/serine in IA-2, aspartate in IA-2β) typical of inactive pseudophosphatases. The isolated domain was monomeric in solution [barr-2009-ptpome-structures]. A 2025 review likewise states that PTPRN and PTPRN2 lack protein tyrosine phosphatase activity because of residue substitutions in the catalytic domain, while noting that this does not rule out activity toward other substrates [stojilkovic-2025-ptprn-ptprn2-review].

The horse sequence keeps every one of these hallmarks (SEQUENCE_ANALYSIS.md). The P-loop reads HCSDGAGRSG, with Asp in place of PTP1B Ala217. The WPD-loop equivalent reads WYD, with Tyr in place of the catalytic-loop Pro. At the pTyr-recognition loop, where PTP1B has Tyr46 and human PTPRN2 has Ser, the horse protein has Cys, a substitution shared by all four RefSeq horse isoforms and so a real feature of the horse genome assembly [ncbi-refseq-horse-ptprn2-isoforms-sequences]. The horse protein should therefore be considered a pseudo-PTP just like its orthologues.

A specific non-protein activity has been shown, though. Caromile et al. found that phogrin dephosphorylates phosphatidylinositol 3-phosphate and PI(4,5)P2, but not PI(3,4,5)P3. The isolated catalytic-domain fusion was only weakly active. The full-length transmembrane protein, purified and assayed in vitro, had a specific activity of 142 mol/min/mol, 75-fold higher than the fusion and comparable to other phosphoinositide phosphatases. Overexpressed phogrin lowered plasma-membrane PI(4,5)P2 in a dose-dependent way. Activity required the catalytic-site cysteine and tracked with effects on glucose-stimulated insulin secretion [caromile-2010-phogrin-pi-phosphatase]. Sengelaub et al. independently confirmed the lipid-phosphatase function in breast cancer cells. PTPRN2 reduced plasma-membrane PI(4,5)P2 and released cofilin from its inactive membrane-bound state, enhancing actin turnover, migration and metastatic colonisation. A catalytic-cysteine-to-alanine mutant (C945A) failed to reproduce these effects, whereas Cys-to-Ser mutation is known to abrogate PI(4,5)P2 dephosphorylation [sengelaub-2016-ptprn2-plcb1-metastasis]. The horse active-site Cys897 aligns exactly with human Cys945 (SEQUENCE_ANALYSIS.md). On current evidence the most defensible molecular-function annotation is phosphatidylinositol phosphate phosphatase activity, specifically phosphatidylinositol-4,5-bisphosphate and phosphatidylinositol-3-phosphate phosphatase activity. Protein-tyrosine phosphatase activity should be treated as unsupported or minimal.

## 4. Subcellular localisation and membrane trafficking

Phogrin is one of the best-characterised integral membrane proteins of neuroendocrine dense-core granules. In β-cells it localises to insulin secretory granule membranes with the PTP domain on the cytosolic face. It is made as a precursor and cleaved about 30 minutes after synthesis to mature 60–64 kDa forms, a timing that indicates processing in a late secretory compartment [wasmeier-1996-phogrin-cloning]. Phogrin–EGFP chimaeras reached dense-core granules with up to 95% efficiency in INS-1 β-cells and PC12 cells. This made phogrin a standard granule marker for imaging glucose-stimulated granule movement and fusion, after which the chimaera diffuses into the plasma membrane [pouli-1998-phogrin-gfp]. Immunochemistry in mouse tissue detected several proteolytic isoforms of 60–71 kDa in brain, with alternative N-termini beginning at Ser414, Ala464 and Glu489, but only the 60-kDa form in pancreas and MIN6 cells. This points to tissue-specific processing [kawakami-2007-ia2beta-cleavage]. Subcellular fractionation of mouse brain showed that IA-2β, unlike IA-2, also co-purifies with synaptic-vesicle-rich fractions [nishimura-2009-neurotransmitter-secretion], which supports the UniProt "synapse" location [uniprot-A0A9L0T4W6-entry].

Several sorting signals act together to target phogrin to granules. The luminal domain, both pro-region and mature ectodomain, can by itself route a soluble protein into the regulated pathway [wasmeier-2002-lumenal-domain-targeting]. Its pro-domain binds the cargo-sorting enzyme carboxypeptidase E at mildly acidic pH, and each protein helps the other reach granules [saito-2011-phogrin-cpe]. On the cytosolic side, a leucine-based [EExxxIL] motif binds the AP-1 and AP-2 clathrin adaptors and controls steady-state granule localisation [torii-2005-cytoplasmic-transport-signal]. An extended juxtamembrane tyrosine motif (Y654QELCRQRMA) binds the AP-2 μ subunit and drives endocytosis and re-targeting to DCVs [wasmeier-2005-tyrosine-motif-endocytosis]. After stimulated exocytosis, phogrin is exposed on the cell surface and then internalised. More than 35% of the internalised protein returns through a syntaxin-6-positive compartment to insulin-positive granules, largely bypassing the main TGN, and can be re-exocytosed [vo-2004-phogrin-recycling][wasmeier-2005-tyrosine-motif-endocytosis]. Live-cell retention-using-selective-hooks (RUSH) assays in INS-1 and PC12 cells added a further step. Unlike soluble granule cargoes such as NPY and secretogranin II, most newly synthesised phogrin leaves the TGN in non-regulated vesicles and joins secretory granules only later. This suggests that transmembrane granule proteins reach the granule partly through post-Golgi, endosome-like routes [hummer-2020-tgn-sorting]. Phogrin therefore cycles between the granule membrane and the plasma membrane. This explains how a granule protein can act on plasma-membrane PI(4,5)P2 [caromile-2010-phogrin-pi-phosphatase] and engage the insulin receptor at the cell surface [torii-2009-phogrin-silencing]. Because these sorting motifs are conserved in the horse sequence (Section 2), the same itinerary is expected for the horse protein.

## 5. Role in regulated secretion and dense-core vesicle homeostasis

The clearest physiological function of PTPRN2 comes from mouse genetics. *Ptprn2*-null mice have mild glucose intolerance and impaired glucose-stimulated insulin secretion (GSIS) [kubosaki-2004-ia2beta-knockout]. Islets from *Ptprn2* single knockouts and *Ptprn*/*Ptprn2* double knockouts (DKO) have lower insulin content and secretion, fewer DCVs, and shorter DCV half-life, consistent with DCV loss through increased lysosomal turnover [cai-2011-dense-core-vesicles]. A β-cell-specific phogrin knockout showed an age-dependent fall in insulin granule density and changes in carbohydrate-positive lysosomal regions. This implicates phogrin in insulin granule homeostasis and crinophagy [yasui-2024-phogrin-crinosome].

The secretory role reaches well beyond the β-cell. DKO brains have reduced noradrenaline, dopamine and serotonin. Their synaptosomes release less dopamine, GABA and glutamate and contain fewer synaptic vesicles. The animals show anxiety-like behaviour, impaired conditioned learning, seizures and shortened lifespan [nishimura-2009-neurotransmitter-secretion]. In the pituitary, DKO females lack the pre-ovulatory LH surge and are essentially infertile [kubosaki-2006-female-infertility]. Later work placed the main defect upstream of the gonadotroph. DKO mice of both sexes have lower hypothalamic *Gnrh1* and *Kiss1* expression and sparser GnRH and kisspeptin fibres in the arcuate nucleus, and females also show delayed puberty. Yet GnRH-induced Ca²⁺ signalling and LH release by gonadotrophs remain intact, which points to a role for these granule proteins in kisspeptin–GnRH neurosecretory output [sokanovic-2023-ptprn-reproduction]. DKO mice also show increased *Pomc* expression, higher release of ACTH, β-endorphin and α-MSH, and hyperplasia of the intermediate lobe [constantin-2024-ptprn-melanotroph]. These and other phenotypes are reviewed by Stojilkovic and colleagues, who stress that the mechanism behind them is still unclear [stojilkovic-2025-ptprn-ptprn2-review].

Overexpression results are more mixed. Ghrelin induces IA-2β (but not IA-2) in islets and brain. Overexpressed IA-2β inhibits GSIS in MIN6 cells, and IA-2β knockdown relieves ghrelin's inhibition of secretion [doi-2006-ia2beta-ghrelin]. Phogrin also interacts with the small GTPase Rab35, which modulates phogrin abundance and distribution and insulin secretion in β-TC-6 cells [lu-2022-rab35-phogrin]. Secretagogues regulate phogrin itself. Glucose and depolarisation trigger Ca²⁺-dependent phosphorylation that parallels insulin release [wasmeier-1999-secretagogue-phosphorylation]. This phosphorylation is carried out by PKA at juxtamembrane Ser680 and Thr699 (rat numbering) [wasmeier-2001-pka-phosphorylation]. One likely unifying model is that phogrin's PI(4,5)P2/PI(3)P phosphatase activity shapes the phosphoinositide microenvironment of granules and the plasma membrane during priming and exocytosis [caromile-2010-phogrin-pi-phosphatase], together with structural roles in DCV biogenesis and stability [cai-2011-dense-core-vesicles].

## 6. Signalling functions: insulin-receptor scaffolding, RPTP heterodimerisation and miR-153

Phogrin also acts as a non-catalytic signalling scaffold. In β-cells, phogrin knockdown abolished glucose-induced proliferation and lowered IRS2 protein without changing insulin secretion. Phogrin formed a glucose-promoted complex with the insulin receptor at the plasma membrane [torii-2009-phogrin-silencing]. Mechanistically, phogrin binds the insulin receptor directly. It suppresses insulin-induced local H₂O₂ production and thereby protects PTP1B from oxidative inactivation, which lets insulin-receptor dephosphorylation proceed and prevents feedback-driven proteasomal degradation of IRS2. *Ptprn2*-knockout islets had 44% less IRS2 [torii-2018-pseudophosphatase-phogrin]. *In vivo*, β-cell-specific phogrin deletion blunted compensatory β-cell mass expansion on a high-fat diet. Phogrin–insulin receptor complexes were detected only in proliferating conditions, whereas under confluent conditions phogrin was engaged in trans phogrin–phogrin binding instead [kubota-2024-phogrin-hfd]. These results place PTPRN2 in the autocrine insulin/IR–IRS2 signalling pathway, as a positive modulator of signal duration.

The PTP-like domain also takes part in oligomerisation. IA-2 and IA-2β homo- and heterodimerise through their juxtamembrane and PTP-like segments. They can also heterodimerise with active RPTPs, notably RPTPα and RPTPε, and inhibit RPTPα catalytic activity [gross-2002-multimerization-rptp]. This "decoy" or regulatory mode is typical of pseudophosphatases and may complement the lipid-phosphatase activity.

Finally, the *PTPRN2* locus has a regulatory output of its own. The microRNA miR-153-2 lies in intron 19 of *Ptprn2* and is co-regulated with its host gene, including induction by glucose [mandemakers-2013-mir153-host-gene]. miR-153 represses *Cacna1c* and so lowers insulin and dopamine secretion, an effect opposite to that of the IA-2β protein [xu-2015-mir153-cacna1c]. Whether miR-153-2 is conserved in the horse *PTPRN2* intron has not been examined.

## 7. Autoimmunity and comparative context

In human type 1 diabetes, IA-2β/phogrin is the precursor of the 37-kDa tryptic islet autoantigen [lu-1996-ia2beta-autoantigen][hawkes-1996-37kda-antigen]. Autoantibodies against its cytoplasmic domain are found in roughly half to 60% of new-onset patients [kawasaki-1996-human-phogrin]. However, Ptprn2 deletion does not prevent cyclophosphamide-induced diabetes in NOD mice [kubosaki-2004-ia2beta-knockout]. We found no report of PTPRN2 autoimmunity or disease association in horses. The high conservation of the cytoplasmic domain across vertebrates [kawasaki-1996-human-phogrin], together with the ferredoxin-like ectodomain fold conserved even in invertebrate homologues [noguera-2015-phogrin-ectodomain-structure], supports transferring the rodent and human findings to the horse protein. A reasonable annotation for horse A0A9L0T4W6 would include the following. Molecular function: phosphatidylinositol-4,5-bisphosphate phosphatase and phosphatidylinositol-3-phosphate phosphatase activity, inferred from orthologues [caromile-2010-phogrin-pi-phosphatase]; insulin receptor binding [torii-2018-pseudophosphatase-phogrin]; and protein heterodimerisation with RPTPs [gross-2002-multimerization-rptp]. Cellular component: dense-core/secretory granule membrane, synaptic vesicle and plasma membrane (transiently) [wasmeier-1996-phogrin-cloning][nishimura-2009-neurotransmitter-secretion][vo-2004-phogrin-recycling]. Biological process: regulation of insulin secretion, dense-core granule maintenance, regulation of neurotransmitter and peptide-hormone secretion, and positive regulation of insulin receptor signalling / β-cell proliferation [cai-2011-dense-core-vesicles][torii-2009-phogrin-silencing]. The rule-based EC 3.1.3.48 assignment should be treated with caution.

## 8. Open Questions

The horse gene model is the first thing to fix. RefSeq models show that the C-terminus of A0A9L0T4W6 (residues 934–976) is an artefact and that the protein lacks an alternatively spliced N-terminal exon [ncbi-refseq-horse-ptprn2-isoforms-sequences]. The UniProt entry should be revised, or replaced by the 1005-residue isoform X1, which has the canonical C-terminus. Horse tissue RNA-seq (pancreas, pituitary, brain) would show which isoforms are actually expressed. All horse models carry a Cys where human has Ser in the pTyr-recognition loop. Because that residue is one of the three that, when back-mutated, restore PTP activity [drake-2003-ia2-phogrin-inhibitors], it would be worth testing whether it alters the residual catalytic chemistry or redox sensitivity of the horse protein.

The physiological substrate of phogrin's phosphatase activity also remains open. The PI(4,5)P2/PI(3)P activity was measured *in vitro* and on overexpression [caromile-2010-phogrin-pi-phosphatase][sengelaub-2016-ptprn2-plcb1-metastasis]. It is unclear whether endogenous phogrin on granule membranes changes local phosphoinositide pools during priming and fusion, and how its low catalytic-domain activity squares with its classification as a pseudophosphatase [drake-2003-ia2-phogrin-inhibitors][barr-2009-ptpome-structures]. Lipid imaging in knockout β-cells and neurons, and knock-in catalytic-dead alleles, would separate enzymatic from scaffolding roles.

The function of the luminal ectodomain is unknown. Its ferredoxin-like fold, its interaction with carboxypeptidase E [saito-2011-phogrin-cpe], and trans phogrin–phogrin binding at the cell surface [kubota-2024-phogrin-hfd] all hint at luminal or extracellular partners or ligands. It is also unknown whether, as reported for IA-2, the cytoplasmic domain of IA-2β is released by calpain cleavage and signals to the nucleus [stojilkovic-2025-ptprn-ptprn2-review]. Finally, no data exist on PTPRN2 expression, polymorphisms or disease associations in horses. Given the importance of equine metabolic syndrome and insulin dysregulation, studying PTPRN2 in equine islets and the hypothalamic–pituitary axis (including pituitary pars intermedia dysfunction, where POMC-derived peptide secretion is disturbed, compare [constantin-2024-ptprn-melanotroph]) would be a natural follow-up.

## 9. References

- [uniprot-A0A9L0T4W6-entry] UniProtKB/TrEMBL entry A0A9L0T4W6_HORSE, "Protein-tyrosine-phosphatase", *Equus caballus*, entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0T4W6.txt
- [ensembl-ENSECAG00000012762-lookup] Ensembl gene ENSECAG00000012762 (PTPRN2), EquCab3.0, chromosome 4. https://rest.ensembl.org/lookup/id/ENSECAG00000012762
- [ncbi-refseq-horse-ptprn2-isoforms-sequences] NCBI RefSeq protein models of horse PTPRN2: XP_023495958.2 (isoform X1), XP_070122225.1 (X2), XP_070122226.1 (X3), XP_070122227.1 (X4). https://www.ncbi.nlm.nih.gov/protein/XP_023495958.2
- [wade-2009-horse-genome] Wade CM, et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 326:865-867. PMID:19892987; PMCID:PMC3785132; DOI:10.1126/science.1178158
- [wasmeier-1996-phogrin-cloning] Wasmeier C, Hutton JC. (1996). Molecular cloning of phogrin, a protein-tyrosine phosphatase homologue localized to insulin secretory granule membranes. J Biol Chem 271:18161-18170. PMID:8663434; DOI:10.1074/jbc.271.30.18161
- [lu-1996-ia2beta-autoantigen] Lu J, et al. (1996). Identification of a second transmembrane protein tyrosine phosphatase, IA-2beta, as an autoantigen in insulin-dependent diabetes mellitus: precursor of the 37-kDa tryptic fragment. PNAS 93:2307-2311. PMID:8637868; PMCID:PMC39791; DOI:10.1073/pnas.93.6.2307
- [kawasaki-1996-human-phogrin] Kawasaki E, Hutton JC, Eisenbarth GS. (1996). Molecular cloning and characterization of the human transmembrane protein tyrosine phosphatase homologue, phogrin, an autoantigen of type 1 diabetes. Biochem Biophys Res Commun 227:440-447. PMID:8878534; DOI:10.1006/bbrc.1996.1526
- [hawkes-1996-37kda-antigen] Hawkes CJ, Wasmeier C, Christie MR, Hutton JC. (1996). Identification of the 37-kDa antigen in IDDM as a tyrosine phosphatase-like protein (phogrin) related to IA-2. Diabetes 45:1187-1192. PMID:8772720; DOI:10.2337/diab.45.9.1187
- [caromile-2010-phogrin-pi-phosphatase] Caromile LA, Oganesian A, Coats SA, Seifert RA, Bowen-Pope DF. (2010). The neurosecretory vesicle protein phogrin functions as a phosphatidylinositol phosphatase to regulate insulin secretion. J Biol Chem 285:10487-10496. PMID:20097759; DOI:10.1074/jbc.m109.066563
- [sengelaub-2016-ptprn2-plcb1-metastasis] Sengelaub CA, Navrazhina K, Ross JB, Halberg N, Tavazoie SF. (2016). PTPRN2 and PLCβ1 promote metastatic breast cancer cell migration through PI(4,5)P2-dependent actin remodeling. EMBO J 35:62-76. PMID:26620550; PMCID:PMC4717998; DOI:10.15252/embj.201591973
- [drake-2003-ia2-phogrin-inhibitors] Drake PG, Peters GH, Andersen HS, Hendriks W, Møller NP. (2003). A novel strategy for the development of selective active-site inhibitors of the protein tyrosine phosphatase-like proteins islet-cell antigen 512 (IA-2) and phogrin (IA-2beta). Biochem J 373:393-401. PMID:12697028; PMCID:PMC1223505; DOI:10.1042/bj20021851
- [barr-2009-ptpome-structures] Barr AJ, et al. (2009). Large-scale structural analysis of the classical human protein tyrosine phosphatome. Cell 136:352-363. PMID:19167335; PMCID:PMC2638020; DOI:10.1016/j.cell.2008.11.038
- [stojilkovic-2025-ptprn-ptprn2-review] Stojilkovic SS, Sokanovic SJ, Constantin S. (2025). What is known and unknown about the role of neuroendocrine genes Ptprn and Ptprn2. Front Endocrinol 16:1531723. PMID:39926347; PMCID:PMC11802530; DOI:10.3389/fendo.2025.1531723
- [noguera-2015-phogrin-ectodomain-structure] Noguera ME, Primo ME, Jakoncic J, Poskus E, Solimena M, Ermácora MR. (2015). X-ray structure of the mature ectodomain of phogrin. J Struct Funct Genomics 16:1-9. PMID:25421040; DOI:10.1007/s10969-014-9191-0
- [el-badaoui-2024-rptp-alphafold] El Badaoui L, Barr AJ. (2024). Analysis of Receptor-Type Protein Tyrosine Phosphatase Extracellular Regions with Insights from AlphaFold. Int J Mol Sci 25:820. PMID:38255894; PMCID:PMC10815196; DOI:10.3390/ijms25020820
- [pouli-1998-phogrin-gfp] Pouli AE, Emmanouilidou E, Zhao C, Wasmeier C, Hutton JC, Rutter GA. (1998). Secretory-granule dynamics visualized in vivo with a phogrin-green fluorescent protein chimaera. Biochem J 333:193-199. PMID:9639579; PMCID:PMC1219572; DOI:10.1042/bj3330193
- [kawakami-2007-ia2beta-cleavage] Kawakami T, et al. (2007). Detection of proteolytic cleavages of diabetes-associated protein IA-2 beta in the pancreas and the brain using novel anti-IA-2 beta monoclonal antibodies. Int J Mol Med 20:177-185. PMID:17611635; DOI:10.3892/ijmm.20.2.177
- [nishimura-2009-neurotransmitter-secretion] Nishimura T, Kubosaki A, Ito Y, Notkins AL. (2009). Disturbances in the secretion of neurotransmitters in IA-2/IA-2beta null mice: changes in behavior, learning and lifespan. Neuroscience 159:427-437. PMID:19361477; PMCID:PMC2672562; DOI:10.1016/j.neuroscience.2009.01.022
- [wasmeier-2002-lumenal-domain-targeting] Wasmeier C, Bright NA, Hutton JC. (2002). The lumenal domain of the integral membrane protein phogrin mediates targeting to secretory granules. Traffic 3:654-665. PMID:12191017; DOI:10.1034/j.1600-0854.2002.30907.x
- [saito-2011-phogrin-cpe] Saito N, Takeuchi T, Kawano A, Hosaka M, Hou N, Torii S. (2011). Luminal interaction of phogrin with carboxypeptidase E for effective targeting to secretory granules. Traffic 12:499-506. PMID:21210912; DOI:10.1111/j.1600-0854.2011.01159.x
- [torii-2005-cytoplasmic-transport-signal] Torii S, et al. (2005). Cytoplasmic transport signal is involved in phogrin targeting and localization to secretory granules. Traffic 6:1213-1224. PMID:16262730; DOI:10.1111/j.1600-0854.2005.00353.x
- [wasmeier-2005-tyrosine-motif-endocytosis] Wasmeier C, Burgos PV, Trudeau T, Davidson HW, Hutton JC. (2005). An extended tyrosine-targeting motif for endocytosis and recycling of the dense-core vesicle membrane protein phogrin. Traffic 6:474-487. PMID:15882444; DOI:10.1111/j.1600-0854.2005.00292.x
- [vo-2004-phogrin-recycling] Vo YP, Hutton JC, Angleson JK. (2004). Recycling of the dense-core vesicle membrane protein phogrin in Min6 beta-cells. Biochem Biophys Res Commun 324:1004-1010. PMID:15485654; DOI:10.1016/j.bbrc.2004.09.147
- [kubosaki-2004-ia2beta-knockout] Kubosaki A, et al. (2004). Targeted disruption of the IA-2beta gene causes glucose intolerance and impairs insulin secretion but does not prevent the development of diabetes in NOD mice. Diabetes 53:1684-1691. PMID:15220191; DOI:10.2337/diabetes.53.7.1684
- [cai-2011-dense-core-vesicles] Cai T, et al. (2011). Deletion of Ia-2 and/or Ia-2β in mice decreases insulin secretion by reducing the number of dense core vesicles. Diabetologia 54:2347-2357. PMID:21732083; PMCID:PMC3168514; DOI:10.1007/s00125-011-2221-6
- [yasui-2024-phogrin-crinosome] Yasui T, et al. (2024). Insulin granule morphology and crinosome formation in mice lacking the pancreatic β cell-specific phogrin (PTPRN2) gene. Histochem Cell Biol 161:223-238. PMID:38150052; DOI:10.1007/s00418-023-02256-8
- [kubosaki-2006-female-infertility] Kubosaki A, Nakamura S, Clark A, Morris JF, Notkins AL. (2006). Disruption of the transmembrane dense core vesicle proteins IA-2 and IA-2beta causes female infertility. Endocrinology 147:811-815. PMID:16269463; DOI:10.1210/en.2005-0638
- [constantin-2024-ptprn-melanotroph] Constantin S, et al. (2024). Protein Tyrosine Phosphatase Receptors N and N2 Control Pituitary Melanotroph Development and POMC Expression. Endocrinology 165:bqae076. PMID:38923438; PMCID:PMC11242453; DOI:10.1210/endocr/bqae076
- [doi-2006-ia2beta-ghrelin] Doi A, et al. (2006). IA-2beta, but not IA-2, is induced by ghrelin and inhibits glucose-stimulated insulin secretion. PNAS 103:885-890. PMID:16418280; DOI:10.1073/pnas.0502470102
- [lu-2022-rab35-phogrin] Lu C, et al. (2022). Rab35 regulates insulin secretion via phogrin in pancreatic β cells. Clin Exp Pharmacol Physiol 49:104-112. PMID:34448213; DOI:10.1111/1440-1681.13581
- [wasmeier-1999-secretagogue-phosphorylation] Wasmeier C, Hutton JC. (1999). Secretagogue-dependent phosphorylation of phogrin, an insulin granule membrane protein tyrosine phosphatase homologue. Biochem J 341:563-569. PMID:10417318; PMCID:PMC1220392; DOI:10.1042/bj3410563
- [wasmeier-2001-pka-phosphorylation] Wasmeier C, Hutton JC. (2001). Secretagogue-dependent phosphorylation of the insulin granule membrane protein phogrin is mediated by cAMP-dependent protein kinase. J Biol Chem 276:31919-31928. PMID:11353772; DOI:10.1074/jbc.m102580200
- [torii-2009-phogrin-silencing] Torii S, et al. (2009). Gene silencing of phogrin unveils its essential role in glucose-responsive pancreatic beta-cell growth. Diabetes 58:682-692. PMID:19073770; PMCID:PMC2646067; DOI:10.2337/db08-0970
- [torii-2018-pseudophosphatase-phogrin] Torii S, et al. (2018). The pseudophosphatase phogrin enables glucose-stimulated insulin signaling in pancreatic β cells. J Biol Chem 293:5920-5933. PMID:29483197; PMCID:PMC5912479; DOI:10.1074/jbc.ra117.000301
- [kubota-2024-phogrin-hfd] Kubota C, Torii R, Hosaka M, Takeuchi T, Gomi H, Torii S. (2024). Phogrin Regulates High-Fat Diet-Induced Compensatory Pancreatic β-Cell Growth by Switching Binding Partners. Nutrients 16:169. PMID:38201998; PMCID:PMC10780347; DOI:10.3390/nu16010169
- [gross-2002-multimerization-rptp] Gross S, et al. (2002). Multimerization of the protein-tyrosine phosphatase (PTP)-like insulin-dependent diabetes mellitus autoantigens IA-2 and IA-2beta with receptor PTPs (RPTPs). Inhibition of RPTPalpha enzymatic activity. J Biol Chem 277:48139-48145. PMID:12364328; DOI:10.1074/jbc.m208228200
- [mandemakers-2013-mir153-host-gene] Mandemakers W, et al. (2013). Co-regulation of intragenic microRNA miR-153 and its host gene Ia-2β: identification of miR-153 target genes with functions related to IA-2β in pancreas and brain. Diabetologia 56:1547-1556. PMID:23595248; PMCID:PMC3671108; DOI:10.1007/s00125-013-2901-5
- [xu-2015-mir153-cacna1c] Xu H, et al. (2015). The Ia-2β intronic miRNA, miR-153, is a negative regulator of insulin and dopamine secretion through its effect on the Cacna1c gene in mice. Diabetologia 58:2298-2306. PMID:26141787; PMCID:PMC6754265; DOI:10.1007/s00125-015-3683-8
- [sokanovic-2023-ptprn-reproduction] Sokanovic SJ, Constantin S, et al. (2023). Common and female-specific roles of protein tyrosine phosphatase receptors N and N2 in mice reproduction. Sci Rep 13:355. PMID:36611058; PMCID:PMC9825377; DOI:10.1038/s41598-023-27497-4
- [hummer-2020-tgn-sorting] Hummer BH, Maslar D, Soltero-Gutierrez M, de Leeuw NF, Asensio CS. (2020). Differential sorting behavior for soluble and transmembrane cargoes at the trans-Golgi network in endocrine cells. Mol Biol Cell 31:157-166. PMID:31825717; PMCID:PMC7001476; DOI:10.1091/mbc.e19-10-0561


## Citations

1. barr-2009-ptpome-structures-abstract.md
2. barr-2009-ptpome-structures-fulltext.txt
3. barr-2009-ptpome-structures-summary.md
4. cai-2011-dense-core-vesicles-abstract.md
5. cai-2011-dense-core-vesicles-summary.md
6. caromile-2010-phogrin-pi-phosphatase-abstract.md
7. caromile-2010-phogrin-pi-phosphatase-summary.md
8. constantin-2024-ptprn-melanotroph-abstract.md
9. constantin-2024-ptprn-melanotroph-summary.md
10. doi-2006-ia2beta-ghrelin-abstract.md
11. doi-2006-ia2beta-ghrelin-summary.md
12. drake-2003-ia2-phogrin-inhibitors-abstract.md
13. drake-2003-ia2-phogrin-inhibitors-summary.md
14. el-badaoui-2024-rptp-alphafold-abstract.md
15. el-badaoui-2024-rptp-alphafold-fulltext.txt
16. el-badaoui-2024-rptp-alphafold-summary.md
17. ensembl-ENSECAG00000012762-lookup.json
18. gross-2002-multimerization-rptp-abstract.md
19. gross-2002-multimerization-rptp-summary.md
20. hawkes-1996-37kda-antigen-abstract.md
21. hawkes-1996-37kda-antigen-summary.md
22. hummer-2020-tgn-sorting-abstract.md
23. hummer-2020-tgn-sorting-fulltext.txt
24. hummer-2020-tgn-sorting-summary.md
25. kawakami-2007-ia2beta-cleavage-abstract.md
26. kawakami-2007-ia2beta-cleavage-summary.md
27. kawasaki-1996-human-phogrin-abstract.md
28. kawasaki-1996-human-phogrin-summary.md
29. kubosaki-2004-ia2beta-knockout-abstract.md
30. kubosaki-2004-ia2beta-knockout-summary.md
31. kubosaki-2006-female-infertility-abstract.md
32. kubosaki-2006-female-infertility-summary.md
33. kubota-2024-phogrin-hfd-abstract.md
34. kubota-2024-phogrin-hfd-fulltext.txt
35. kubota-2024-phogrin-hfd-summary.md
36. lu-1996-ia2beta-autoantigen-abstract.md
37. lu-1996-ia2beta-autoantigen-summary.md
38. lu-2022-rab35-phogrin-abstract.md
39. lu-2022-rab35-phogrin-summary.md
40. mandemakers-2013-mir153-host-gene-abstract.md
41. mandemakers-2013-mir153-host-gene-fulltext.txt
42. mandemakers-2013-mir153-host-gene-summary.md
43. ncbi-refseq-horse-ptprn2-isoforms-sequences.fasta
44. nishimura-2009-neurotransmitter-secretion-abstract.md
45. nishimura-2009-neurotransmitter-secretion-summary.md
46. noguera-2015-phogrin-ectodomain-structure-abstract.md
47. noguera-2015-phogrin-ectodomain-structure-summary.md
48. pouli-1998-phogrin-gfp-abstract.md
49. pouli-1998-phogrin-gfp-summary.md
50. saito-2011-phogrin-cpe-abstract.md
51. saito-2011-phogrin-cpe-summary.md
52. saxena-2026-ap3-dcv-sorting-abstract.md
53. saxena-2026-ap3-dcv-sorting-fulltext.txt
54. saxena-2026-ap3-dcv-sorting-summary.md
55. sengelaub-2016-ptprn2-plcb1-metastasis-abstract.md
56. sengelaub-2016-ptprn2-plcb1-metastasis-fulltext.txt
57. sengelaub-2016-ptprn2-plcb1-metastasis-summary.md
58. sokanovic-2023-ptprn-reproduction-abstract.md
59. sokanovic-2023-ptprn-reproduction-fulltext.txt
60. sokanovic-2023-ptprn-reproduction-summary.md
61. stojilkovic-2025-ptprn-ptprn2-review-abstract.md
62. stojilkovic-2025-ptprn-ptprn2-review-fulltext.txt
63. stojilkovic-2025-ptprn-ptprn2-review-summary.md
64. torii-2005-cytoplasmic-transport-signal-abstract.md
65. torii-2005-cytoplasmic-transport-signal-summary.md
66. torii-2009-phogrin-silencing-abstract.md
67. torii-2009-phogrin-silencing-fulltext.txt
68. torii-2009-phogrin-silencing-summary.md
69. torii-2018-pseudophosphatase-phogrin-abstract.md
70. torii-2018-pseudophosphatase-phogrin-summary.md
71. uniprot-A0A9L0T4W6-entry.txt
72. uniprot-A0A9L0T4W6-summary.md
73. vo-2004-phogrin-recycling-abstract.md
74. vo-2004-phogrin-recycling-summary.md
75. wade-2009-horse-genome-abstract.md
76. wade-2009-horse-genome-summary.md
77. wasmeier-1996-phogrin-cloning-abstract.md
78. wasmeier-1996-phogrin-cloning-summary.md
79. wasmeier-1999-secretagogue-phosphorylation-abstract.md
80. wasmeier-1999-secretagogue-phosphorylation-summary.md
81. wasmeier-2001-pka-phosphorylation-abstract.md
82. wasmeier-2001-pka-phosphorylation-summary.md
83. wasmeier-2002-lumenal-domain-targeting-abstract.md
84. wasmeier-2002-lumenal-domain-targeting-summary.md
85. wasmeier-2005-tyrosine-motif-endocytosis-abstract.md
86. wasmeier-2005-tyrosine-motif-endocytosis-summary.md
87. xu-2015-mir153-cacna1c-abstract.md
88. xu-2015-mir153-cacna1c-summary.md
89. yasui-2024-phogrin-crinosome-abstract.md
90. yasui-2024-phogrin-crinosome-summary.md