---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:22:49.298158'
end_time: '2026-10-26T03:40:32.215138'
duration_seconds: 1062.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: SIRT5
  gene_symbol: SIRT5
  uniprot_accession: F6S899
  protein_description: 'SubName: Full=Sirtuin 5 {ECO:0000313|Ensembl:ENSECAP00000022781.3};'
  gene_info: Name=SIRT5 {ECO:0000313|VGNC:VGNC:22990};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: DHS-like_NAD/FAD-binding_dom. (IPR029035); NAD-dep_sirtuin_deacylases.
    (IPR050134); Sirtuin. (IPR003000); Ssirtuin_cat_dom. (IPR026590); SIR2 (PF02146)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 73
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** F6S899
- **Protein Description:** SubName: Full=Sirtuin 5 {ECO:0000313|Ensembl:ENSECAP00000022781.3};
- **Gene Information:** Name=SIRT5 {ECO:0000313|VGNC:VGNC:22990};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DHS-like_NAD/FAD-binding_dom. (IPR029035); NAD-dep_sirtuin_deacylases. (IPR050134); Sirtuin. (IPR003000); Ssirtuin_cat_dom. (IPR026590); SIR2 (PF02146)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SIRT5" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SIRT5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SIRT5** (gene ID: SIRT5, UniProt: F6S899) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SIRT5 in the Horse (*Equus caballus*; UniProt F6S899): an NAD⁺-dependent Lysine Deacylase for Negatively Charged Acyl Groups

## 1. Introduction and Summary

SIRT5 is one of the seven mammalian sirtuins, which are NAD⁺-dependent class III lysine deacylases. The horse gene (VGNC:22990, chromosome 20) is represented in UniProtKB by the unreviewed entry F6S899, which was derived from an Ensembl gene model built on the Thoroughbred reference genome [uniprot-F6S899-record; wade-2009-horse-genome-abstract]. The protein has a sirtuin catalytic domain (PROSITE PS50305, Pfam PF02146 SIR2, InterPro IPR003000/IPR026590) and is placed in the PANTHER subfamily "NAD-dependent protein deacylase sirtuin-5, mitochondrial" (PTHR11085:SF10) [uniprot-F6S899-record]. This confirms that the gene symbol and the domain architecture agree. No study has characterised the horse SIRT5 protein biochemically. The horse-specific literature consists of transcript-level observations in chondrocytes, endurance-exercise blood transcriptomes and reproductive tissues [zabek-2022-equine-chondrocytes-fulltext; mach-2021-horse-exercise-fulltext; pollard-2024-mare-fertility-fulltext]. The function of the horse protein must therefore be inferred from its close orthologs in human and mouse, which have been studied in depth.

That inference is strong. In mammals, SIRT5 is a weak deacetylase but an efficient NAD⁺-dependent demalonylase, desuccinylase and deglutarylase. It removes negatively charged dicarboxylic acyl groups from the ε-amino group of lysine, releasing nicotinamide and 2''-O-acyl-ADP-ribose [du-2011-desuccinylase-fulltext; tan-2014-glutarylation-fulltext; roessler-2014-acyl-specificity-abstract; uniprot-Q9NXA8-record]. The selectivity for acidic acyl groups comes from Tyr102 and Arg105 in the acyl-binding pocket [du-2011-desuccinylase-fulltext], and both residues are conserved in horse SIRT5 (this report, Section 2). SIRT5 resides mainly in the mitochondrial matrix, with additional pools in the intermembrane space, cytosol, nucleus and peroxisomes [nakagawa-2009-cps1-fulltext; schlicker-2008-substrates-abstract; park-2013-succinylome-fulltext; nishida-2015-malonylation-fulltext; chen-2018-acox1-abstract]. Its substrates are concentrated in metabolism: the urea cycle (CPS1), fatty acid β-oxidation and ketogenesis (ECHA/HADHA, HMGCS2), glycolysis (GAPDH, PKM2), the TCA cycle and respiration (PDC, SDH), and NADPH/antioxidant systems (IDH2, G6PD, SOD1) [nakagawa-2009-cps1-fulltext; rardin-2013-succinylome-fulltext; sadhukhan-2016-cardiac-abstract; nishida-2015-malonylation-fulltext; park-2013-succinylome-fulltext; zhou-2016-idh2-g6pd-abstract; lin-2013-sod1-abstract; xiangyun-2017-pkm2-fulltext].

One caveat bears directly on annotating this accession. The current sequence of F6S899 (version 3, 282 aa) corresponds to the Ensembl transcript SIRT5-206. This transcript skips a 124-nt coding exon, which shifts the reading frame at codon 207 [ensembl-SIRT5-gene-model-summary]. It matches the canonical 310-aa horse SIRT5 exactly up to residue 206 and then diverges, so it loses the second pair of zinc-binding cysteines and the C-terminal NAD⁺-binding segments (Section 2; notes/identity_analysis.md). UniProt flags this with a CAUTION that the entry "lacks conserved residue(s) required for the propagation of feature annotation" [uniprot-F6S899-record]. Function annotations for the SIRT5 gene apply to the canonical horse protein (for example A0A9L0T9B1, which is identical to F6S899 sequence version 2). If the 282-aa product is translated at all, it is predicted to be catalytically compromised.

## 2. Gene and Protein Identity: Orthology, Conservation and an Aberrant Isoform Model

The UniProt record F6S899 names the gene SIRT5 (VGNC:22990) in *Equus caballus*. It cites the horse genome paper as the source of the sequence and Ensembl ENSECAP00000022781.3 as the protein model [uniprot-F6S899-record; wade-2009-horse-genome-abstract]. UniProt also holds a separate, HAMAP-annotated horse entry, A0A9L0T9B1 (310 aa), named "NAD-dependent protein deacylase sirtuin-5, mitochondrial" (EC 2.3.1.-) and assigned to the cytosol, mitochondrion and nucleus by the HAMAP rule MF_03160 [uniprot-A0A9L0T9B1-record]. The UniParc archive shows that the 310-aa sequence (UPI00071AAB30) was F6S899 sequence version 2. The current version 3 is a distinct 282-aa sequence (UPI0023FEADFC) (notes/identity_analysis.md). So the accession changed from the canonical protein to an alternative transcript model when Ensembl revised the gene annotation.

I aligned the horse sequences to reviewed human SIRT5 (Q9NXA8) with a global BLOSUM62 alignment (notes/identity_analysis.md). Canonical horse SIRT5 shares 273 of 310 residues (88%) with human SIRT5 over its full length, as expected for one-to-one mammalian orthologs. F6S899 version 3 is identical to the canonical horse protein for residues 1–206, which include the predicted N-terminal mitochondrial presequence and most of the Rossmann-fold NAD⁺-binding and zinc-binding small domains. Over this region it is 85% identical to human SIRT5. Several residues that are mechanistically important in human SIRT5 are retained: Tyr102 and Arg105 (substrate acyl-carboxylate binding), Gln140, the catalytic proton acceptor His158, and Cys166/Cys169, the first half of the structural zinc site [uniprot-Q9NXA8-record; du-2011-desuccinylase-fulltext]. The divergence begins exactly at Cys207, one of the four zinc ligands. In the variant, Cys207 and Cys212 are replaced by tryptophans, and the downstream segments corresponding to human NAD⁺-binding residues 249–251 and 275–277 are missing [uniprot-Q9NXA8-record]. The 76 residues after the divergence show no recognisable similarity to the sirtuin fold. This explains the UniProt caution [uniprot-F6S899-record].

The human gene also produces several C-terminal isoforms. Matsushita and colleagues showed that human SIRT5 iso1 and iso2 differ only at their C-termini. Both carry cleavable N-terminal mitochondrial targeting signals, but iso1 distributes to mitochondria and cytoplasm, whereas iso2 has a hydrophobic C-terminal mitochondrial membrane-insertion signal and is primate-specific [matsushita-2011-isoforms-abstract]. The horse 282-aa model is not equivalent to either human isoform: it truncates the catalytic core itself rather than altering a short C-terminal tail. The Ensembl gene model explains how the horse variant arises. The horse SIRT5 locus (ENSECAG00000026898, chr20:13,723,059–13,759,730 on EquCab3.0) has six annotated protein-coding transcripts, of 79 to 318 aa. The Ensembl canonical transcript, SIRT5-205, encodes 318 aa and differs from the 310-aa SIRT5-201 only at its 5' exons [ensembl-SIRT5-gene-model-summary; ensembl-ENSECAG00000026898-lookup]. F6S899 corresponds to transcript SIRT5-206 (ENSECAT00000028843). Unlike SIRT5-201 and SIRT5-205, it skips a 124-nt exon at chr20:13,742,662–13,742,785. Comparing the coding sequences shows that SIRT5-201 and SIRT5-206 diverge at nucleotide 621, which is codon 207, and that the downstream SIRT5-206 sequence is the SIRT5-201 sequence offset by exactly those 124 nucleotides [ensembl-ENSECAT00000146678-cds; ensembl-ENSECAT00000028843-cds; notes/identity_analysis.md]. Because 124 is not a multiple of three, the exon skip shifts the reading frame from codon 207 onward. That produces the non-sirtuin C-terminal tail and removes the second zinc-ligand pair and the C-terminal NAD⁺-binding motifs. SIRT5-206 also ends in two terminal exon pieces separated by a 3-nt gap, which looks like a computational model rather than a curated cDNA [ensembl-ENSECAG00000026898-lookup]. No experimental evidence (RT-PCR, cDNA, proteomics) specific to this isoform was found. If the exon-skipped mRNA exists, it would likely be a nonsense-mediated decay substrate or a minor splice product, not a functional enzyme. This remains to be tested.

## 3. Catalytic Function: NAD⁺-Dependent Removal of Malonyl, Succinyl and Glutaryl Groups

The first report on SIRT5 enzymology described it as a mitochondrial NAD⁺-dependent deacetylase. Nakagawa et al. showed that SIRT5 binds and activates carbamoyl phosphate synthetase 1 (CPS1) [nakagawa-2009-cps1-fulltext]. Its deacetylase activity, however, was always weak. A survey of all seven human sirtuins found robust peptide deacetylation activity mainly for SIRT1 [michishita-2005-localization-abstract]. Schlicker et al. found that Sirt5 deacetylated none of the mitochondrial matrix proteins they tested, though it did deacetylate cytochrome c [schlicker-2008-substrates-abstract]. Du et al. resolved this in 2011. They found that the catalytic efficiency (kcat/Km) of SIRT5 for deacetylation was about 500-fold lower than that of SIRT1, but that SIRT5 efficiently removes malonyl and succinyl groups from lysine. Across three peptide sequences, the catalytic efficiencies for demalonylation and desuccinylation were 29- to more than 1000-fold higher than for deacetylation [du-2011-desuccinylase-fulltext]. The reaction follows the sirtuin mechanism: NAD⁺ is consumed, nicotinamide is released and the acyl group is transferred to ADP-ribose, producing O-malonyl- or O-succinyl-ADP-ribose [du-2011-desuccinylase-fulltext]. UniProt's curated record for human SIRT5 encodes this as the Rhea reactions N6-malonyl/succinyl/glutaryl-L-lysyl-[protein] + NAD⁺ + H₂O → 2''-O-acyl-ADP-D-ribose + nicotinamide + L-lysyl-[protein] [uniprot-Q9NXA8-record].

The structural basis of this specificity is well defined. Crystal structures of human SIRT5 with ADP-ribose and with the inhibitor suramin showed the canonical sirtuin architecture, a large Rossmann-fold NAD⁺-binding domain and a small zinc-binding domain, with substrate and NAD⁺ binding in the cleft between them [schuetz-2007-structure-abstract]. In the SIRT5 structures, buffer sulfonate groups sat in the acyl pocket and contacted Arg105 and Tyr102. In a SIRT5 structure with a succinylated peptide, the succinyl carboxylate interacts with these same two residues. The mutations R105M and Y102F raise the Km for desuccinylation substantially [du-2011-desuccinylase-fulltext]. Tan et al. extended the substrate range to glutaryl-lysine, a modification derived from glutaryl-CoA, and showed that among the HDACs tested SIRT5 was the only one with significant deglutarylase activity in vitro [tan-2014-glutarylation-fulltext]. Roessler et al. systematically varied the acyl chain on a CPS1-derived peptide and defined the acyl selectivity of SIRT5 with crystallographic support: it prefers short, negatively charged dicarboxylic acyl groups [roessler-2014-acyl-specificity-abstract]. Because Tyr102, Arg105 and the catalytic His158 are conserved in the horse protein (Section 2), the horse enzyme can be predicted with high confidence to share this acidic-acyl-lysine specificity. Suitable GO molecular-function terms are protein-malonyllysine demalonylase activity (GO:0036054), protein-succinyllysine desuccinylase activity (GO:0036055), protein-glutaryllysine deglutarylase activity (GO:0061697), NAD⁺ binding (GO:0070403) and zinc ion binding (GO:0008270). These apply to the canonical full-length protein but not to the truncated F6S899 version 3 model, which lacks two zinc ligands.

## 4. Subcellular Localization

SIRT5 was first placed in mitochondria with SIRT3 and SIRT4 in a systematic localization survey of human SIRT1–7 [michishita-2005-localization-abstract]. Nakagawa et al. localized it to the mitochondrial matrix, where it meets CPS1 [nakagawa-2009-cps1-fulltext]. Import assays showed that Sirt5 can also enter the intermembrane space, consistent with its activity on cytochrome c [schlicker-2008-substrates-abstract]. A substantial share of SIRT5 is extramitochondrial, however. Park et al. reported that "a substantial fraction of SIRT5 is extra-mitochondrial" and that succinylation also decorates cytosolic and nuclear proteins [park-2013-succinylome-fulltext]. Nishida et al. found that malonylated proteins are more abundant in the cytosolic than in the mitochondrial fraction of liver, and that SIRT5 controls malonylation in both compartments [nishida-2015-malonylation-fulltext]. SIRT5 has also been detected in peroxisomes, where it regulates ACOX1 [chen-2018-acox1-abstract]. The human isoform study suggests how a single gene achieves this spread: N-terminal presequences give mitochondrial import, while C-terminal sequences tune retention, membrane insertion and cytosolic stability [matsushita-2011-isoforms-abstract]. SIRT5 is broadly expressed in mammals, with the highest levels in brain, heart, liver, kidney, muscle and testis. Its expression rises with PGC-1α and food withdrawal and falls with AMPK activation, linking SIRT5 abundance to nutritional state [kumar-2018-review-fulltext]. The reviewed human entry summarises the localization as mitochondrial matrix (main), intermembrane space, cytosol and nucleus [uniprot-Q9NXA8-record]. The HAMAP-derived horse annotation lists cytosol, mitochondrion and nucleus [uniprot-A0A9L0T9B1-record]. The horse protein keeps a conserved N-terminal presequence region (30 of the first 40 residues are identical to human SIRT5; Section 2), so mitochondrial matrix localization (GO:0005759) with a cytosolic pool (GO:0005829) is the best-supported inference. This has not been tested experimentally in horse cells.

## 5. Metabolic Pathways Regulated by SIRT5

### 5.1 Nitrogen metabolism and the urea cycle

The best-established physiological role of SIRT5 is in ammonia detoxification. In mouse liver, mitochondrial NAD⁺ rises during fasting and SIRT5 activates CPS1, the rate-limiting first enzyme of the urea cycle. SIRT5-knockout mice fail to increase CPS1 activity and develop elevated blood ammonia during fasting. SIRT5 is also activated by a prolonged high-protein diet [nakagawa-2009-cps1-fulltext]. Later work showed that the relevant modifications on CPS1 are acidic acylations, not acetylation. Succinylation of CPS1 at Lys1291 rises sharply in Sirt5-knockout liver, and CPS1 activity is lower [du-2011-desuccinylase-fulltext]. CPS1 is also glutarylated, which inhibits it, and SIRT5 reverses this. In a glutaric aciduria type I model with excess glutaryl-CoA, CPS1 glutarylation increases and its activity falls [tan-2014-glutarylation-fulltext]. SIRT5 targets also include cytosolic urea-cycle enzymes (argininosuccinate synthase, argininosuccinate lyase, arginase) through demalonylation [nishida-2015-malonylation-fulltext]. Outside the liver, SIRT5 limits glutaminase-dependent ammonia production from glutamine and thereby modulates ammonia-induced autophagy and mitophagy [polletta-2015-ammonia-fulltext].

### 5.2 Fatty acid oxidation and ketogenesis

Quantitative succinylome analysis of liver mitochondria from wild-type and Sirt5-knockout mice placed SIRT5 targets mainly in β-oxidation, branched-chain amino acid catabolism, the TCA cycle, ATP synthesis, ketone-body synthesis and propionyl-CoA catabolism. All four ketogenic enzymes are targeted. The rate-limiting enzyme HMGCS2 carries the most SIRT5-regulated sites, and succinylation-mimetic mutations at K83 and K310 strongly inhibit it [rardin-2013-succinylome-fulltext]. In heart, succinyl-CoA is the most abundant acyl-CoA. Succinylation accumulates mainly in the heart of Sirt5-knockout mice, where SIRT5 regulates ECHA (HADHA), the trifunctional β-oxidation enzyme. Knockout hearts show reduced ECHA activity, accumulation of long-chain acyl-CoAs, reduced ATP under fasting and hypertrophic cardiomyopathy [sadhukhan-2016-cardiac-abstract]. In peroxisomes, by contrast, SIRT5 desuccinylation inhibits ACOX1 by suppressing formation of the active dimer, which limits H₂O₂ production [chen-2018-acox1-abstract]. SIRT5 therefore does not act as a uniform activator. Its effect depends on the target and compartment.

### 5.3 Glycolysis, the TCA cycle and respiration

In the cytosol, glycolysis is the pathway most strongly regulated by SIRT5-dependent demalonylation. Six of ten glycolytic enzymes carry SIRT5-regulated malonyl-lysines, GAPDH malonylation (most strongly at K184) suppresses its activity, and wild-type SIRT5 reverses this but the catalytically inactive H158Y mutant does not. Primary hepatocytes lacking Sirt5 have reduced glycolytic flux [nishida-2015-malonylation-fulltext]. SIRT5 also desuccinylates PKM2 at K498 and thereby inhibits it. Reactive oxygen species increase SIRT5–PKM2 binding, which diverts glucose carbon towards NADPH production [xiangyun-2017-pkm2-fulltext]. In mitochondria, SIRT5 suppresses the biochemical activity of the pyruvate dehydrogenase complex and succinate dehydrogenase and the respiration that depends on them [park-2013-succinylome-fulltext]. A later study reached the opposite conclusion for the respiratory chain. It reported that SIRT5 binds cardiolipin, desuccinylates subunits of all four electron-transport complexes and of ATP synthase, and supports Complex II-driven respiration. Kumar and Lombard attribute the discrepancy partly to differences in cell type and experimental context [kumar-2018-review-fulltext]. Beyond energy metabolism, SIRT5 desuccinylates and activates mitochondrial serine hydroxymethyltransferase 2 (SHMT2) at Lys280, which links it to one-carbon metabolism [kumar-2018-review-fulltext].

### 5.4 Redox homeostasis and NADPH

Several SIRT5 targets are linked to antioxidant defence. SIRT5 desuccinylates and activates Cu/Zn superoxide dismutase (SOD1), which lowers ROS [lin-2013-sod1-abstract]. It desuccinylates mitochondrial IDH2 and deglutarylates cytosolic G6PD, activating both NADPH-producing enzymes and increasing resistance to oxidative stress [zhou-2016-idh2-g6pd-abstract]. Together with the PKM2 and ACOX1 mechanisms above, these findings place SIRT5 as a regulator that coordinates carbon flux and redox balance. Bringman-Rodenbarger et al. and Kumar and Lombard review this integrated role, covering glycolysis, the TCA cycle, fatty acid oxidation, nitrogen metabolism, the pentose phosphate pathway, antioxidant defence and apoptosis [bringman-2018-review-abstract; kumar-2018-review-fulltext].

Whole-animal genetics puts these molecular findings in proportion. Germline Sirt5-knockout mice show global protein hypersuccinylation in liver and skeletal muscle and higher serum ammonia after fasting, but no overt metabolic abnormality on chow or high-fat diets [yu-2013-sirt5-ko-fulltext]. Their main phenotypes emerge under stress, such as the fasting-induced cardiac energy deficit and hypertrophic cardiomyopathy reported by Sadhukhan et al. [sadhukhan-2016-cardiac-abstract]. SIRT5 therefore looks less like a pathway switch and more like a buffer that protects many enzymes from accumulating inhibitory acylation when acyl-CoA loads rise.

The common logic is that SIRT5 reverses non-enzymatic or semi-enzymatic acylation by reactive acyl-CoAs: succinyl-CoA, malonyl-CoA and glutaryl-CoA. These modifications convert a lysine's positive charge to a negative one and usually inhibit the modified enzyme. SIRT5 consumes NAD⁺ to restore the native lysine, coupling the cell's NAD⁺ status and acyl-CoA load to enzyme activity [du-2011-desuccinylase-fulltext; nishida-2015-malonylation-fulltext; sadhukhan-2016-cardiac-abstract].

## 6. Evidence from the Horse

Direct evidence on SIRT5 in horses is sparse and entirely at the transcript level. In ex vivo expanded equine articular chondrocytes, the HDAC inhibitor trichostatin A unexpectedly increased SIRT5 transcripts, together with HDAC3 and SIRT2. The authors note that sirtuins are generally insensitive to TSA, so the induction is probably an indirect transcriptional response rather than feedback on SIRT5 enzyme activity [zabek-2022-equine-chondrocytes-fulltext]. In endurance horses studied during long-distance exercise, SIRT5 appeared among the fatty acid metabolism genes in a blood transcriptome signature enriched for mitochondrial transport, β-oxidation (CPT1B, ACADVL, ACOX1) and mitochondrial dynamics. This is consistent with the conserved role of SIRT5 in fatty acid oxidation, but the evidence is only an association [mach-2021-horse-exercise-fulltext]. A review of NAD⁺ and sirtuins in mare fertility summarises equine expression studies reporting Sirt5 upregulation in the inner cell mass and trophectoderm of equine embryos, and a decline in endometrial Sirt5 expression from mid- to late gestation. The same review stresses that sirtuin proteins have not been directly measured in equine reproductive tissues [pollard-2024-mare-fertility-fulltext]. UniProt reports PeptideAtlas evidence of the horse protein ("Evidence at protein level"), and Bgee records expression in muscle tissue and 23 other cell types or tissues [uniprot-F6S899-record]. The proteomic evidence presumably maps to the shared N-terminal region and cannot distinguish the 282-aa model from the canonical protein.

Horses are elite aerobic athletes with very high skeletal muscle mitochondrial density, and they depend heavily on fatty acid oxidation during prolonged exercise. The SIRT5 targets characterised in rodents (ECHA, HMGCS2, SDH, PDC and the NADPH-generating enzymes) are central to this kind of metabolism [rardin-2013-succinylome-fulltext; sadhukhan-2016-cardiac-abstract; park-2013-succinylome-fulltext]. It is plausible that SIRT5 helps keep β-oxidation and TCA enzymes free of inhibitory acylation in equine muscle and heart, but this has not been tested.

## 7. Synthesis for Functional Annotation

The evidence supports annotating horse SIRT5, the gene product encoded at VGNC:22990, as follows. It is an NAD⁺-dependent protein lysine deacylase with strong preference for malonyl, succinyl and glutaryl groups and only weak deacetylase activity. This rests on experimental work on human and mouse orthologs [du-2011-desuccinylase-fulltext; tan-2014-glutarylation-fulltext; roessler-2014-acyl-specificity-abstract] and on conservation in the horse sequence of the Tyr102/Arg105 acyl pocket and the His158 catalytic base. It localizes predominantly to the mitochondrial matrix, with cytosolic, nuclear, intermembrane-space and peroxisomal pools [nakagawa-2009-cps1-fulltext; park-2013-succinylome-fulltext; nishida-2015-malonylation-fulltext; schlicker-2008-substrates-abstract; chen-2018-acox1-abstract]. It acts in the urea cycle and ammonia homeostasis through CPS1, in fatty acid β-oxidation and ketogenesis, in glycolysis, and in NADPH/antioxidant metabolism [nakagawa-2009-cps1-fulltext; rardin-2013-succinylome-fulltext; nishida-2015-malonylation-fulltext; zhou-2016-idh2-g6pd-abstract]. All of these are inferences by orthology (ISO/IBA-type evidence); none rests on direct experiments in horse. For the specific accession F6S899 in its current 282-aa form, curators should note that the sequence is the product of a frameshifting exon skip [ensembl-SIRT5-gene-model-summary] and lacks Cys207/Cys212 and the C-terminal NAD⁺-binding segments. Domain-based or orthology-based propagation of catalytic activity and zinc binding to this isoform should be treated with caution, consistent with the UniProt CAUTION [uniprot-F6S899-record].

## 8. Open Questions

The most immediate open question for annotation is whether the 282-aa F6S899 transcript (Ensembl SIRT5-206) exists in vivo. Ensembl shows that it arises from skipping a 124-nt exon, which shifts the reading frame at codon 207 [ensembl-SIRT5-gene-model-summary]. Counting RNA-seq reads that span the junction joining the flanking exons, or long-read sequencing of horse tissues, could test whether this junction is real and how abundant it is. Ribosome profiling or targeted proteomics of the frameshifted C-terminal peptide would show whether it is translated. UniProt might consider linking the SIRT5 functional annotation to the canonical 310/318-aa entries (A0A9L0T9B1/A0A9L0T6A9) rather than to F6S899. If it is real, the next questions are whether the truncated protein is stable, and whether it is inactive or acts as a dominant-negative competitor for substrates or NAD⁺. Comparing it with the primate-specific human iso2 and the stability-conferring iso1 C-terminus [matsushita-2011-isoforms-abstract] would show whether C-terminal isoform diversity at SIRT5 is a recurring evolutionary theme.

Second, the enzyme activity of recombinant horse SIRT5 has never been measured. A simple study comparing kcat/Km for acetyl, malonyl, succinyl and glutaryl peptides, modelled on Du et al. and Roessler et al. [du-2011-desuccinylase-fulltext; roessler-2014-acyl-specificity-abstract], would convert the orthology-based inference into direct evidence. Third, given the exceptional oxidative capacity of equine muscle and heart, quantitative succinylome and malonylome profiles of horse skeletal muscle at rest and after endurance exercise would be valuable, especially for ECHA, SDH, PDC and HMGCS2 as candidate SIRT5 targets [rardin-2013-succinylome-fulltext; sadhukhan-2016-cardiac-abstract; park-2013-succinylome-fulltext]. Equine metabolic disorders could also be informative, for example equine metabolic syndrome, or myopathies affecting lipid or energy metabolism. It is also unknown whether horses have an extramitochondrial SIRT5 pool like rodents. Finally, the transcript-level reports in chondrocytes, embryos and endometrium [zabek-2022-equine-chondrocytes-fulltext; pollard-2024-mare-fertility-fulltext] need protein-level confirmation before they can be read as functional statements.

## 9. References

- **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science*. 2009;326(5954):865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158.
- **zabek-2022-equine-chondrocytes**: Ząbek T, Witarski W, Szmatoła T, Sawicki S, Mrozowicz J, Samiec M. Trichostatin A-Mediated Epigenetic Modulation Predominantly Triggers Transcriptomic Alterations in the Ex Vivo Expanded Equine Chondrocytes. *Int J Mol Sci*. 2022;23(21):13168. PMID: 36361948; PMCID: PMC9655705; DOI: 10.3390/ijms232113168.
- **pollard-2024-mare-fertility**: Pollard CL. Can Nicotinamide Adenine Dinucleotide (NAD+) and Sirtuins Be Harnessed to Improve Mare Fertility? *Animals (Basel)*. 2024;14(2):193. PMID: 38254361; PMCID: PMC10812544; DOI: 10.3390/ani14020193.
- **mach-2021-horse-exercise**: Mach N, Moroldo M, Rau A, Lecardonnel J, Le Moyec L, Robert C, Barrey E. Understanding the Holobiont: Crosstalk Between Gut Microbiota and Mitochondria During Long Exercise in Horse. *Front Mol Biosci*. 2021;8:656204. PMID: 33898524; PMCID: PMC8063112; DOI: 10.3389/fmolb.2021.656204.
- **nakagawa-2009-cps1**: Nakagawa T, Lomb DJ, Haigis MC, Guarente L. SIRT5 Deacetylates carbamoyl phosphate synthetase 1 and regulates the urea cycle. *Cell*. 2009;137(3):560-570. PMID: 19410549; PMCID: PMC2698666; DOI: 10.1016/j.cell.2009.02.026.
- **du-2011-desuccinylase**: Du J, Zhou Y, Su X, et al. Sirt5 is a NAD-dependent protein lysine demalonylase and desuccinylase. *Science*. 2011;334(6057):806-809. PMID: 22076378; PMCID: PMC3217313; DOI: 10.1126/science.1207861.
- **park-2013-succinylome**: Park J, Chen Y, Tishkoff DX, et al. SIRT5-mediated lysine desuccinylation impacts diverse metabolic pathways. *Mol Cell*. 2013;50(6):919-930. PMID: 23806337; PMCID: PMC3769971; DOI: 10.1016/j.molcel.2013.06.001.
- **rardin-2013-succinylome**: Rardin MJ, He W, Nishida Y, et al. SIRT5 regulates the mitochondrial lysine succinylome and metabolic networks. *Cell Metab*. 2013;18(6):920-933. PMID: 24315375; PMCID: PMC4105152; DOI: 10.1016/j.cmet.2013.11.013.
- **tan-2014-glutarylation**: Tan M, Peng C, Anderson KA, et al. Lysine glutarylation is a protein posttranslational modification regulated by SIRT5. *Cell Metab*. 2014;19(4):605-617. PMID: 24703693; PMCID: PMC4108075; DOI: 10.1016/j.cmet.2014.03.014.
- **nishida-2015-malonylation**: Nishida Y, Rardin MJ, Carrico C, et al. SIRT5 Regulates both Cytosolic and Mitochondrial Protein Malonylation with Glycolysis as a Major Target. *Mol Cell*. 2015;59(2):321-332. PMID: 26073543; PMCID: PMC4571487; DOI: 10.1016/j.molcel.2015.05.022.
- **lin-2013-sod1**: Lin ZF, Xu HB, Wang JY, et al. SIRT5 desuccinylates and activates SOD1 to eliminate ROS. *Biochem Biophys Res Commun*. 2013;441(1):191-195. PMID: 24140062; DOI: 10.1016/j.bbrc.2013.10.033.
- **michishita-2005-localization**: Michishita E, Park JY, Burneskis JM, Barrett JC, Horikawa I. Evolutionarily conserved and nonconserved cellular localizations and functions of human SIRT proteins. *Mol Biol Cell*. 2005;16(10):4623-4635. PMID: 16079181; PMCID: PMC1237069; DOI: 10.1091/mbc.e05-01-0033.
- **schuetz-2007-structure**: Schuetz A, Min J, Antoshenko T, et al. Structural basis of inhibition of the human NAD+-dependent deacetylase SIRT5 by suramin. *Structure*. 2007;15(3):377-389. PMID: 17355872; DOI: 10.1016/j.str.2007.02.002.
- **sadhukhan-2016-cardiac**: Sadhukhan S, Liu X, Ryu D, et al. Metabolomics-assisted proteomics identifies succinylation and SIRT5 as important regulators of cardiac function. *Proc Natl Acad Sci U S A*. 2016;113(16):4320-4325. PMID: 27051063; PMCID: PMC4843474; DOI: 10.1073/pnas.1519858113.
- **zhou-2016-idh2-g6pd**: Zhou L, Wang F, Sun R, et al. SIRT5 promotes IDH2 desuccinylation and G6PD deglutarylation to enhance cellular antioxidant defense. *EMBO Rep*. 2016;17(6):811-822. PMID: 27113762; PMCID: PMC5278614; DOI: 10.15252/embr.201541643.
- **chen-2018-acox1**: Chen XF, Tian MX, Sun RQ, et al. SIRT5 inhibits peroxisomal ACOX1 to prevent oxidative damage and is downregulated in liver cancer. *EMBO Rep*. 2018;19(5):e45124. PMID: 29491006; PMCID: PMC5934778; DOI: 10.15252/embr.201745124.
- **polletta-2015-ammonia**: Polletta L, Vernucci E, Carnevale I, et al. SIRT5 regulation of ammonia-induced autophagy and mitophagy. *Autophagy*. 2015;11(2):253-270. PMID: 25700560; PMCID: PMC4502726; DOI: 10.1080/15548627.2015.1009778.
- **xiangyun-2017-pkm2**: Xiangyun Y, Xiaomin N, Linping G, et al. Desuccinylation of pyruvate kinase M2 by SIRT5 contributes to antioxidant response and tumor growth. *Oncotarget*. 2017;8(4):6984-6993. PMID: 28036303; PMCID: PMC5351684; DOI: 10.18632/oncotarget.14346.
- **roessler-2014-acyl-specificity**: Roessler C, Nowak T, Pannek M, et al. Chemical probing of the human sirtuin 5 active site reveals its substrate acyl specificity and peptide-based inhibitors. *Angew Chem Int Ed Engl*. 2014;53(40):10728-10732. PMID: 25111069; DOI: 10.1002/anie.201402679.
- **schlicker-2008-substrates**: Schlicker C, Gertz M, Papatheodorou P, Kachholz B, Becker CF, Steegborn C. Substrates and regulation mechanisms for the human mitochondrial sirtuins Sirt3 and Sirt5. *J Mol Biol*. 2008;382(3):790-801. PMID: 18680753; DOI: 10.1016/j.jmb.2008.07.048.
- **bringman-2018-review**: Bringman-Rodenbarger LR, Guo AH, Lyssiotis CA, Lombard DB. Emerging Roles for SIRT5 in Metabolism and Cancer. *Antioxid Redox Signal*. 2018;28(8):677-690. PMID: 28707979; PMCID: PMC5824490; DOI: 10.1089/ars.2017.7264.
- **matsushita-2011-isoforms**: Matsushita N, Yonashiro R, Ogata Y, et al. Distinct regulation of mitochondrial localization and stability of two human Sirt5 isoforms. *Genes Cells*. 2011;16(2):190-202. PMID: 21143562; DOI: 10.1111/j.1365-2443.2010.01475.x.
- **yu-2013-sirt5-ko**: Yu J, Sadhukhan S, Noriega LG, Moullan N, He B, Weiss RS, Lin H, Schoonjans K, Auwerx J. Metabolic characterization of a Sirt5 deficient mouse model. *Sci Rep*. 2013;3:2806. PMID: 24076663; PMCID: PMC3786297; DOI: 10.1038/srep02806.
- **kumar-2018-review**: Kumar S, Lombard DB. Functions of the sirtuin deacylase SIRT5 in normal physiology and pathobiology. *Crit Rev Biochem Mol Biol*. 2018;53(3):311-334. PMID: 29637793; PMCID: PMC6233320; DOI: 10.1080/10409238.2018.1458071.
- **ensembl-SIRT5-gene-model** (files ensembl-ENSECAG00000026898-lookup, ensembl-ENSECAT00000146678-cds, ensembl-ENSECAT00000028843-cds): Ensembl REST API, gene ENSECAG00000026898 (horse SIRT5, EquCab3.0) and transcripts ENSECAT00000146678 and ENSECAT00000028843. https://rest.ensembl.org/lookup/id/ENSECAG00000026898?expand=1
- **uniprot-F6S899**: UniProtKB/TrEMBL entry F6S899 (SIRT5, *Equus caballus*), entry version 90, sequence version 3. https://rest.uniprot.org/uniprotkb/F6S899.txt
- **uniprot-A0A9L0T9B1**: UniProtKB/TrEMBL entry A0A9L0T9B1 (NAD-dependent protein deacylase sirtuin-5, mitochondrial, *Equus caballus*). https://rest.uniprot.org/uniprotkb/A0A9L0T9B1.txt
- **uniprot-Q9NXA8**: UniProtKB/Swiss-Prot entry Q9NXA8 (SIR5_HUMAN). https://rest.uniprot.org/uniprotkb/Q9NXA8.txt


## Citations

1. _metadata.json
2. bringman-2018-review-abstract.md
3. bringman-2018-review-summary.md
4. chen-2018-acox1-abstract.md
5. chen-2018-acox1-summary.md
6. du-2011-desuccinylase-abstract.md
7. du-2011-desuccinylase-fulltext.txt
8. du-2011-desuccinylase-summary.md
9. ensembl-ENSECAG00000026898-lookup.json
10. ensembl-ENSECAT00000028843-cds.fasta
11. ensembl-ENSECAT00000146678-cds.fasta
12. ensembl-SIRT5-gene-model-summary.md
13. kumar-2018-review-abstract.md
14. kumar-2018-review-fulltext.txt
15. kumar-2018-review-summary.md
16. lin-2013-sod1-abstract.md
17. lin-2013-sod1-summary.md
18. mach-2021-horse-exercise-abstract.md
19. mach-2021-horse-exercise-fulltext.txt
20. mach-2021-horse-exercise-summary.md
21. matsushita-2011-isoforms-abstract.md
22. matsushita-2011-isoforms-summary.md
23. michishita-2005-localization-abstract.md
24. michishita-2005-localization-summary.md
25. nakagawa-2009-cps1-abstract.md
26. nakagawa-2009-cps1-fulltext.txt
27. nakagawa-2009-cps1-summary.md
28. nishida-2015-malonylation-abstract.md
29. nishida-2015-malonylation-fulltext.txt
30. nishida-2015-malonylation-summary.md
31. park-2013-succinylome-abstract.md
32. park-2013-succinylome-fulltext.txt
33. park-2013-succinylome-summary.md
34. pollard-2024-mare-fertility-abstract.md
35. pollard-2024-mare-fertility-fulltext.txt
36. pollard-2024-mare-fertility-summary.md
37. polletta-2015-ammonia-abstract.md
38. polletta-2015-ammonia-fulltext.txt
39. polletta-2015-ammonia-summary.md
40. rardin-2013-succinylome-abstract.md
41. rardin-2013-succinylome-fulltext.txt
42. rardin-2013-succinylome-summary.md
43. roessler-2014-acyl-specificity-abstract.md
44. roessler-2014-acyl-specificity-summary.md
45. sadhukhan-2016-cardiac-abstract.md
46. sadhukhan-2016-cardiac-summary.md
47. schlicker-2008-substrates-abstract.md
48. schlicker-2008-substrates-summary.md
49. schuetz-2007-structure-abstract.md
50. schuetz-2007-structure-summary.md
51. tan-2014-glutarylation-abstract.md
52. tan-2014-glutarylation-fulltext.txt
53. tan-2014-glutarylation-summary.md
54. uniprot-A0A9L0T9B1-record.txt
55. uniprot-A0A9L0T9B1-summary.md
56. uniprot-F6S899-record.txt
57. uniprot-F6S899-summary.md
58. uniprot-Q9NXA8-record.txt
59. uniprot-Q9NXA8-summary.md
60. wade-2009-horse-genome-abstract.md
61. wade-2009-horse-genome-fulltext.txt
62. wade-2009-horse-genome-summary.md
63. xiangyun-2017-pkm2-abstract.md
64. xiangyun-2017-pkm2-fulltext.txt
65. xiangyun-2017-pkm2-summary.md
66. yu-2013-sirt5-ko-abstract.md
67. yu-2013-sirt5-ko-fulltext.txt
68. yu-2013-sirt5-ko-summary.md
69. zabek-2022-equine-chondrocytes-abstract.md
70. zabek-2022-equine-chondrocytes-fulltext.txt
71. zabek-2022-equine-chondrocytes-summary.md
72. zhou-2016-idh2-g6pd-abstract.md
73. zhou-2016-idh2-g6pd-summary.md