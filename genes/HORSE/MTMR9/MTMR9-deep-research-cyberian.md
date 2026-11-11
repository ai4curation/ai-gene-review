---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:10:07.398814'
end_time: '2026-10-26T03:22:34.525629'
duration_seconds: 747.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: MTMR9
  gene_symbol: MTMR9
  uniprot_accession: A0A9L0T3C1
  protein_description: 'RecName: Full=Myotubularin-related protein 9 {ECO:0000256|ARBA:ARBA00072711};
    AltName: Full=Inactive phosphatidylinositol 3-phosphatase 9 {ECO:0000256|ARBA:ARBA00077527};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the protein-tyrosine phosphatase family. Non-
  protein_domains: Myotubularin. (IPR030564); Myotubularin-like_Pase_dom. (IPR010569);
    PH-like_dom_sf. (IPR011993); Prot-tyrosine_phosphatase-like. (IPR029021); Myotub-related
    (PF06602)
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
citation_count: 61
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0T3C1
- **Protein Description:** RecName: Full=Myotubularin-related protein 9 {ECO:0000256|ARBA:ARBA00072711}; AltName: Full=Inactive phosphatidylinositol 3-phosphatase 9 {ECO:0000256|ARBA:ARBA00077527};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the protein-tyrosine phosphatase family. Non-
- **Key Domains:** Myotubularin. (IPR030564); Myotubularin-like_Pase_dom. (IPR010569); PH-like_dom_sf. (IPR011993); Prot-tyrosine_phosphatase-like. (IPR029021); Myotub-related (PF06602)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MTMR9" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MTMR9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MTMR9** (gene ID: MTMR9, UniProt: A0A9L0T3C1) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MTMR9 (Myotubularin-related protein 9) in the Horse, *Equus caballus* (UniProt A0A9L0T3C1): A Review of Function, Localization and Pathways

## 1. Introduction and Summary

UniProt entry A0A9L0T3C1 is an unreviewed (TrEMBL) protein of 507 amino acids. It was predicted from the Thoroughbred horse reference genome [wade-2009-horse-genome-abstract]. Automated annotation calls it "Myotubularin-related protein 9" (alternative name "Inactive phosphatidylinositol 3-phosphatase 9") and places it in the non-receptor class myotubularin subfamily of the protein-tyrosine phosphatase superfamily. Its domains are a PH-GRAM domain, a myotubularin phosphatase-like domain (PF06602) and a C-terminal coiled coil. No experimental work has been published on horse MTMR9. Everything below about its function is inferred from orthology to human and mouse MTMR9, which have been studied biochemically and in cells, and to the nematode ortholog MTM-9. That inference is well supported, for two reasons. First, the horse sequence matches human MTMR9 (Q96QG7) at 97.8% of aligned positions and mouse Mtmr9 (Q9Z2D0) at 94.8% (this report, Section 2). Second, MTMR9 has no paralogs that could cause confusion: it is the only member of its myotubularin subgroup [zou-2012-mtmr9-mtmr8-fulltext]. The gene symbol is therefore not ambiguous. One nomenclature caveat applies. A 2001 report named a 549-residue, phosphatase-dead myotubularin gene on human 8p22-p23 "MTMR8" [appel-2001-mtmr8-abstract]. UniProt now cites that report for human MTMR9, and the name MTMR8 has since been reassigned to a catalytically active paralog [lorenzo-2006-systematic-myotubularins-abstract; zou-2012-mtmr9-mtmr8-fulltext].

MTMR9 is a catalytically dead "pseudophosphatase." It does not dephosphorylate anything itself. Its primary function is to act as a regulatory, adapter subunit for the catalytically active myotubularin phosphoinositide 3-phosphatases of the MTMR6/7/8 subfamily. It forms heterodimers with each of them through its C-terminal coiled-coil domain [mochizuki-2003-mtmr7-mtmr9-fulltext; zou-2009-mtmr9-mtmr6-fulltext; zou-2012-mtmr9-mtmr8-fulltext; lorenzo-2006-systematic-myotubularins-abstract]. Inside these complexes, MTMR9 does three things. It stabilizes its partners: in HeLa cells, MTMR9 extends the half-life of MTMR6 from about 40 min to about 4 h [zou-2009-mtmr9-mtmr6-fulltext]. It raises their catalytic activity and their affinity for anionic membranes [zou-2009-mtmr9-mtmr6-fulltext]. It also changes their substrate preference. With MTMR9 bound, MTMR6 becomes mainly a phosphatidylinositol 3,5-bisphosphate [PtdIns(3,5)P2] 3-phosphatase that produces PtdIns(5)P, while MTMR8 becomes mainly a PtdIns(3)P 3-phosphatase that produces PtdIns [zou-2012-mtmr9-mtmr8-fulltext]. The reactions catalyzed by MTMR9-containing complexes are therefore the hydrolysis of the D-3 phosphate of PtdIns(3)P and PtdIns(3,5)P2. MTMR7–MTMR9 complexes also act on the soluble inositol 1,3-bisphosphate [mochizuki-2003-mtmr7-mtmr9-fulltext].

Mammalian MTMR9 is mostly cytosolic. It concentrates in the perinuclear region, partly overlaps with the endoplasmic reticulum (ER) and is found in the ER-Golgi intermediate compartment and the Golgi [zou-2009-mtmr9-mtmr6-fulltext; doubravska-2020-mtmr9-er-golgi-abstract]. After growth-factor stimulation it moves to plasma-membrane ruffles through its PH-GRAM domain [maekawa-2014-macropinocytosis-fulltext]. Through these complexes MTMR9 takes part in several processes: completion of macropinocytosis [maekawa-2014-macropinocytosis-fulltext], ER-to-Golgi transport and secretion, including WNT3A secretion [doubravska-2020-mtmr9-er-golgi-abstract], suppression of autophagy via MTMR8 [zou-2012-mtmr9-mtmr8-fulltext], suppression of DNA-damage-induced apoptosis via MTMR6 [zou-2009-mtmr9-mtmr6-fulltext], and fine-tuning of PI3K/AKT signaling in T cells [guo-2013-tcell-phosphatases-fulltext]. In *C. elegans*, the MTM-6/MTM-9 complex is needed for fluid-phase endocytosis and for Wntless recycling and Wnt secretion [dang-2004-myotubularins-endocytosis-fulltext; silhankova-2010-mtm6-mtm9-wnt-fulltext]. This shows that the complex's role in endomembrane trafficking is ancient.

## 2. Identity of the Horse Gene Product and Isoform Structure

The horse entry was checked against reviewed mammalian orthologs. A0A9L0T3C1 maps to Ensembl transcript ENSECAT00000122597.1 of the horse gene ENSECAG00000014120 on chromosome 2. Two other horse UniProt entries come from the same gene: A0A5F5PR89 (549 aa, ENSECAT00000074905) and F7CCR9 (553 aa, ENSECAT00000015118). Both carry the gene name MTMR9 (UniProt cross-references, retrieved during this work). Horse chromosome 2 corresponds to the human 8p region that contains MTMR9, which fits the generally conserved synteny between horse and human chromosomes [wade-2009-horse-genome-abstract]. The 549-residue horse isoform A0A5F5PR89 matches human MTMR9 at 538 of 549 positions.

The 507-residue A0A9L0T3C1 sequence was aligned globally (BLOSUM62) against human Q96QG7 and mouse Q9Z2D0. The alignment shows full collinearity with one exception: a single 42-residue internal deletion relative to human MTMR9. The missing segment is human residues 98–139 (ALSTLDSITLMYPFFYRPMFEVIEDGWHSFLPEQEFELYSSA). It lies just after the annotated GRAM domain (human residues 4–99) and in the N-terminal part of the myotubularin phosphatase domain (human 123–498), per the UniProt Q96QG7 features. The rest of the protein, including the full catalytic-domain core and the C-terminal coiled coil, is retained. A0A9L0T3C1 therefore looks like an alternative splice isoform of horse MTMR9 that skips an exon in the PH-GRAM–phosphatase junction. Whether this transcript exists in vivo, and whether its product folds and binds partners, has not been tested. The 42-residue segment lies at the edge of the PH-GRAM module, which in mouse MTMR9 is necessary and sufficient for targeting to membrane ruffles [maekawa-2014-macropinocytosis-fulltext]. Losing it could therefore affect membrane recruitment more than partner binding, but this is speculation (see Open Questions). The human gene also has an annotated alternative isoform, one lacking residues 1–85 (UniProt Q96QG7, VSP_056209), so alternative splicing of MTMR9 is not unique to horse.

## 3. Domain Architecture and the Basis of Catalytic Inactivity

Myotubularins form a large eukaryotic group within the tyrosine/dual-specificity phosphatase superfamily. Both catalytically active and inactive members are conserved from nematodes to humans [laporte-2003-myotubularins-review-abstract]. Active members use the canonical CX5R active-site motif to remove the 3-phosphate from PtdIns3P and PtdIns(3,5)P2, producing PtdIns and PtdIns5P [laporte-2003-myotubularins-review-abstract; zou-2009-mtmr9-mtmr6-fulltext]. MTMR9 was recognized early as one of the inactive members (originally called LIP-STYX), alongside MTMR5, MTMR10–13 and others, because it lacks the cysteine in the PTP motif that catalysis requires [mochizuki-2003-mtmr7-mtmr9-fulltext]. In human MTMR9, the position of the catalytic cysteine (residue 333) holds a glycine, within the sequence ...ILIHG(333)TEGTDS(339)T.... The position of the conserved catalytic arginine (residue 339) holds a serine (sequence from UniProt Q96QG7; analysis in this work). The horse protein has the same ...ILIHGTEGTDST... sequence, at residues 287–298. Horse MTMR9 therefore lacks both invariant catalytic residues and should be catalytically inactive. Reviews of the family stress that nearly half of human myotubularins appear to be catalytically inactive, yet several of these inactive members have essential functions in mammals [robinson-2006-myotubularin-review-abstract]. These pseudophosphatases usually work by dimerizing with active members [liu-2022-pseudophosphatases-review-fulltext]. Current family classifications agree: MTM1, MTMR1–4, MTMR6–8 and MTMR14 are active, while MTMR5, MTMR9–13 and MTMR15 are inactive [saar-2025-mtmr-disordered-cterm-fulltext; mochizuki-2013-mtmr6-rab1b-fulltext].

MTMR9 has three structured parts. The first is an N-terminal PH-GRAM domain, which mediates membrane targeting. In mouse MTMR9, the isolated PH-GRAM domain is sufficient for recruitment to EGF-induced membrane ruffles, and a construct without it is not recruited [maekawa-2014-macropinocytosis-fulltext]. The second is the large phosphatase-like (pseudophosphatase) domain. The third is a C-terminal coiled coil. Saar and colleagues compared MTMR C-terminal regions and found that MTMR9 has the shortest C-terminal tail in the family (49 residues). It also has the longest predicted coiled coil (47 residues) and one of the most negatively charged (net charge about −5). It is the only MTMR whose tail is not predicted to be Ser/Thr-phosphorylated [saar-2025-mtmr-disordered-cterm-fulltext]. Within that short tail they predicted di-arginine ER-retention/localization motifs, tyrosine-based and di-leucine sorting motifs, and an LC3-interacting region (LIR) [saar-2025-mtmr-disordered-cterm-fulltext]. The crystal structure of the active paralog MTMR2 gives the structural framework for reading these domains. It showed that the myotubularin phosphatase domain is structurally unique among PTPs, and that the GRAM motif is part of a larger module with a pleckstrin-homology (PH) fold, now called the PH-GRAM domain. The MTMR2 structure was proposed as a model for the rest of the family, including its inactive members [begley-2003-mtmr2-structure-abstract]. Applied to MTMR9, this framework implies that the pseudophosphatase domain keeps the overall myotubularin fold, and probably the lipid-headgroup-binding surface, but cannot carry out the cysteine-dependent nucleophilic attack. These are computational predictions, but the ER motifs fit the experimentally observed ER enrichment of MTMR9 [saar-2025-mtmr-disordered-cterm-fulltext; zou-2009-mtmr9-mtmr6-fulltext]. AlphaFold3 models of the MTMR7–MTMR9 heterodimer show the two proteins held together by their coiled-coil helices [saar-2025-mtmr-disordered-cterm-fulltext]. This agrees with biochemical data showing that the MTMR9 coiled coil alone is enough to bind MTMR7 [mochizuki-2003-mtmr7-mtmr9-fulltext]. Deleting the MTMR6 coiled coil abolishes MTMR6–MTMR9 binding [mochizuki-2013-mtmr6-rab1b-fulltext].

## 4. Molecular Function: A Regulatory Subunit That Sets the Activity, Stability and Substrate Choice of MTMR6, MTMR7 and MTMR8

### 4.1 Heterodimer formation

The first evidence that MTMR9 has a function came from purifying binding partners. Mochizuki and Majerus immunoprecipitated MTMR7 from mouse N1E-115 neuroblastoma cells and identified MTMR9 as the co-purifying protein by tandem mass spectrometry. They also showed that MTMR6 binds MTMR9 [mochizuki-2003-mtmr7-mtmr9-fulltext]. Human MTMR6 and MTMR9 were then shown to bind each other directly, with purified recombinant proteins (GST pull-down and reciprocal co-IP) and in HeLa cells. Each protein also forms homodimers [zou-2009-mtmr9-mtmr6-fulltext]. When endogenous MTMR6 was immunoprecipitated from HeLa cells, MTMR9 was the major co-purifying protein. Size-exclusion chromatography showed that the soluble MTMR6–MTMR9 complex is a heterodimer of about 134 kDa [mochizuki-2013-mtmr6-rab1b-fulltext]. A systematic yeast two-hybrid and co-IP survey of the human family added MTMR8 as a third active partner [lorenzo-2006-systematic-myotubularins-abstract], and this was later confirmed by co-IP in HeLa cells [zou-2012-mtmr9-mtmr8-fulltext]. MTMR9 therefore sits at the hub of a small network: it is the inactive partner shared by all three active members of the closely related MTMR6/7/8 subfamily [zou-2012-mtmr9-mtmr8-fulltext]. The nematode orthologs MTM-6 and MTM-9 also co-immunoprecipitate and act together genetically [dang-2004-myotubularins-endocytosis-fulltext], so this pairing has been conserved across bilaterians.

### 4.2 Stabilization of partner proteins

The most consistent cellular effect of MTMR9 is to stabilize its partners. In transfected HeLa cells, co-expressing MTMR6 and MTMR9 raised the steady-state levels of both proteins. In cycloheximide chase experiments, MTMR9 extended MTMR6 half-life from about 40 min to about 4 h. In the other direction, MTMR6 stabilized MTMR9 in an inducible HEK293 line. Knocking down both proteins reduced MTMR6 by up to 90%, much more than knocking down MTMR6 alone [zou-2009-mtmr9-mtmr6-fulltext]. MTMR9 stabilizes MTMR8 in the same way [zou-2012-mtmr9-mtmr8-fulltext]. A large part of MTMR9's function may therefore be to control how much of each active phosphatase is present.

### 4.3 Enhancement of lipid binding and catalysis

On PIP-strip overlays, purified MTMR9 alone did not bind any phosphoinositide, phosphatidic acid or phosphatidylserine (PS). MTMR6 bound monophosphorylated phosphoinositides, PtdIns(3,5)P2, phosphatidic acid and PS. Adding MTMR9 increased MTMR6 lipid binding in a concentration-dependent way without changing which lipids it bound [zou-2009-mtmr9-mtmr6-fulltext]. MTMR9 raised the first-order rate constant of MTMR6 toward PtdIns(3)P by 1.7-fold in neutral liposomes and up to 6.4-fold in 50% PS. The combination of MTMR9 and 100% PS raised MTMR6 activity 84-fold over MTMR6 alone in PC/PE vesicles. MTMR9 did not shift the pH optimum (about 7.0) [zou-2009-mtmr9-mtmr6-fulltext]. MTMR9 also increased the Ins(1,3)P2 phosphatase activity of MTMR7 [mochizuki-2003-mtmr7-mtmr9-fulltext]. Mechanistically, then, MTMR9 behaves like a regulatory subunit. It helps the catalytic subunit associate with anionic membranes and raises its turnover. It contributes no catalytic residues of its own.

### 4.4 Determination of substrate specificity

The most informative result for functional annotation is that MTMR9 sets which phosphoinositide pool its partner hydrolyzes. Zou et al. (2012) compared the two complexes directly. MTMR9 increased MTMR6 activity toward PtdIns(3,5)P2 more than 30-fold but toward PtdIns(3)P only about 2-fold. For MTMR8, MTMR9 increased activity 4-fold toward PtdIns(3)P and only 1.4-fold toward PtdIns(3,5)P2 [zou-2012-mtmr9-mtmr8-fulltext]. The cellular lipid changes matched the in vitro results. Co-expressing MTMR6 with MTMR9 raised cellular PtdIns(5)P, the product of PtdIns(3,5)P2 3-dephosphorylation, about threefold. Co-expressing MTMR8 with MTMR9 lowered PtdIns(3)P puncta, and neither MTMR8 alone nor MTMR6/R9 had this effect [zou-2012-mtmr9-mtmr8-fulltext]. Overexpressing MTMR9 alone modestly reduced PtdIns(3)P. The authors attributed this to MTMR9 activating endogenous MTMR8 [zou-2012-mtmr9-mtmr8-fulltext]. In summary, an MTMR9-containing complex catalyzes:

1-phosphatidyl-1D-myo-inositol 3,5-bisphosphate + H2O → 1-phosphatidyl-1D-myo-inositol 5-phosphate + phosphate (dominant for MTMR6–MTMR9), and

1-phosphatidyl-1D-myo-inositol 3-phosphate + H2O → 1-phosphatidyl-1D-myo-inositol + phosphate (dominant for MTMR8–MTMR9),

with MTMR9 serving as the non-catalytic, specificity-determining subunit. For Gene Ontology-style annotation, MTMR9 is best described as a phosphatase activator / phosphatase regulator and protein-stabilizing binding partner, not as a phosphatase.

## 5. Subcellular Localization

Experiments on human and mouse MTMR9 place it in several cytoplasmic locations, depending on context. In HeLa cells, epitope-tagged MTMR9 accumulates in the perinuclear region in a punctate cytosolic pattern and overlaps closely with co-expressed MTMR6. It does not colocalize well with Lamp-1, γ-adaptin or EEA1, but it partly overlaps with the ER marker calnexin [zou-2009-mtmr9-mtmr6-fulltext]. The resting pattern in A431 cells is described differently: MTMR9 is diffusely cytosolic and does not colocalize with calnexin [maekawa-2014-macropinocytosis-fulltext]. This suggests that ER association varies with cell type or expression level. Within five minutes of EGF stimulation, mouse MTMR9 relocates to F-actin-rich plasma-membrane ruffles, and its PH-GRAM domain is necessary and sufficient for this [maekawa-2014-macropinocytosis-fulltext]. Doubravská and colleagues placed human MTMR9 in the ER-Golgi intermediate compartment and the Golgi apparatus. They showed that it recruits its active partners MTMR6 and MTMR8 to these compartments and that MTMR8/MTMR9 colocalize with RAB1A [doubravska-2020-mtmr9-er-golgi-abstract]. MTMR9's partner MTMR6 binds GDP-bound Rab1B through its own GRAM domain and is held in pericentrosomal and peri-Golgi regions in a microtubule-dependent way [mochizuki-2013-mtmr6-rab1b-fulltext]. This suggests that Rab1 GTPases and MTMR9 cooperate to target the complexes to the early secretory pathway. The predicted di-arginine ER-retention motifs in the MTMR9 tail offer a possible sequence basis for its ER/ERGIC enrichment [saar-2025-mtmr-disordered-cterm-fulltext]. The automated subcellular-location annotations on the horse entry (ruffle membrane, cytoplasmic side; perinuclear region; endoplasmic reticulum; cytosol) are consistent with this literature and appear to be propagated from it.

## 6. Pathways and Biological Processes

### 6.1 Macropinocytosis and fluid-phase endocytosis

MTMR9's best-defined role in a membrane pathway is in macropinocytosis. The first evidence came from *C. elegans*. Mutations in mtm-6 (cup-6) and mtm-9 (cup-10) block fluid-phase uptake by scavenger coelomocytes and disrupt PI(3)P distribution. MTM-6 and MTM-9 act as a complex in an ARF-6-dependent endocytic pathway [dang-2004-myotubularins-endocytosis-fulltext]. Genetic analysis showed that nematode myotubularins oppose VPS34-generated PI(3)P but are also, unexpectedly, needed for coelomocyte endocytosis [xue-2003-myotubularins-elegans-abstract]. Maekawa et al. built on these mutants to show that knocking down MTMR6 or MTMR9 in EGF-stimulated A431 cells strongly impairs macropinocytic dextran uptake but leaves clathrin-dependent transferrin uptake intact. In these cells, ruffles still form and move but fail to close into macropinosomes [maekawa-2014-macropinocytosis-fulltext]. The authors proposed a sequential lipid-breakdown cascade in the ruffle: PI(3,4,5)P3 to PI(3,4)P2 to PI(3)P to PI, carried out by SHIP2, INPP4B and the MTMR6/MTMR9 complex. The intermediate lipids would act through specific effectors, among them the PI(3)P-activated Ca2+-activated K+ channel KCa3.1, which is also needed for macropinocytosis [maekawa-2014-macropinocytosis-fulltext]. MTMR6 had earlier been shown to bind KCa3.1 through coiled-coil domains on both proteins and to inhibit the channel by dephosphorylating PI(3)P, which the channel requires. Swapping in the MTMR6 coiled coil was enough to transfer this target specificity to MTM1 [srivastava-2005-mtmr6-kca31-fulltext]. The MTMR6 coiled coil is therefore used both for heterodimerization with MTMR9 [mochizuki-2013-mtmr6-rab1b-fulltext] and for choosing targets such as KCa3.1 [srivastava-2005-mtmr6-kca31-fulltext]. How MTMR9 binding fits together with channel binding has not been studied. In this model, MTMR9 acts at the last step, PI(3)P removal, by recruiting and activating MTMR6 at the ruffle.

### 6.2 Early secretory pathway, Golgi integrity and Wnt secretion

MTMR9 also acts at the ER–Golgi interface. Loss of MTMR9 disrupts Golgi integrity and changes the distribution of RAB1A and of the actin nucleation-promoting factor WHAMM. Both depletion and overexpression of MTMR9 slow protein secretion, including secretion of the physiologically relevant cargo WNT3A [doubravska-2020-mtmr9-er-golgi-abstract]. This mammalian phenotype parallels an earlier nematode finding. There, the MTM-6/MTM-9 complex is required in Wnt-producing cells for retromer-dependent recycling of the Wnt cargo receptor MIG-14/Wntless, and the MTM-6 ortholog has the same role in *Drosophila* Wg secretion [silhankova-2010-mtm6-mtm9-wnt-fulltext]. The exact step differs between the systems: endosome-to-Golgi recycling in worms versus ER-to-Golgi transport in human cells. Even so, the evidence agrees that MTMR9 complexes regulate PI3P-dependent sorting needed for Wnt ligand export.

### 6.3 Autophagy

PtdIns(3)P generated by the class III PI3K–Beclin 1 complex is required for autophagosome biogenesis. Zou et al. showed that the MTMR8–MTMR9 complex inhibits autophagy [zou-2012-mtmr9-mtmr8-fulltext]. Overexpressing both proteins raised levels of p62 and abolished rapamycin-induced WIPI-1 puncta. Knocking down both lowered p62 under bafilomycin A1 and increased WIPI-1 puncta. Knocking down MTMR9 alone had a noticeable effect, but knocking down MTMR6 (with or without MTMR9) did not [zou-2012-mtmr9-mtmr8-fulltext]. The MTMR8–MTMR9 complex dissociated within 2 h of serum starvation. This suggests a regulated release that lets PtdIns(3)P build up when autophagy is induced [zou-2012-mtmr9-mtmr8-fulltext]. MTMR6 and Rab1B are separately needed to form DFCP1-positive omegasomes [mochizuki-2013-mtmr6-rab1b-fulltext]. Predicted LIR motifs in the MTMR9 tail [saar-2025-mtmr-disordered-cterm-fulltext] point to a possible direct link to LC3, but this has not been tested. Rodents lack an MTMR8 gene [mochizuki-2013-mtmr6-rab1b-fulltext], whereas the horse proteome contains MTMR8 entries (for example F6WPK8 and A0A3Q2I6X3; UniProt query, this work). The MTMR8–MTMR9 autophagy axis described in human cells is therefore more likely to apply to horse than to mouse.

### 6.4 Apoptosis

The MTMR6–MTMR9 complex protects cells against apoptosis caused by genotoxic stress. In HeLa cells treated with etoposide, knocking down MTMR9, or MTMR6 together with MTMR9, increased apoptosis on annexin V/FACS and APOPercentage assays, while knocking down MTMR6 alone did not [zou-2009-mtmr9-mtmr6-fulltext]. Co-expressing MTMR6 and MTMR9 lowered etoposide-induced apoptosis. MTMR8/R9 overexpression had no such effect [zou-2009-mtmr9-mtmr6-fulltext; zou-2012-mtmr9-mtmr8-fulltext]. The authors linked this to the MTMR6/R9 complex shifting PtdIns(3,5)P2 into PtdIns(5)P [zou-2012-mtmr9-mtmr8-fulltext]. The downstream mechanism has not been worked out.

### 6.5 PI3K/AKT signaling and T-helper differentiation

An unbiased shRNA screen of the mouse phosphatome in CD4 T cells identified Mtmr9 as one of the strongest regulators of helper T-cell fate [guo-2013-tcell-phosphatases-fulltext]. Silencing Mtmr9 with several independent shRNAs and an siRNA increased Th1 differentiation (T-bet and IFN-γ) and AKT phosphorylation. In bone-marrow chimeras, Mtmr9-silenced progenitors gave rise to more T-bet-expressing CD4 T cells [guo-2013-tcell-phosphatases-fulltext]. The authors proposed that MTMR9-containing complexes fine-tune PI3K/AKT activity [guo-2013-tcell-phosphatases-fulltext]. The biochemical link to AKT is unresolved, because the myotubularins' known substrates (PtdIns3P and PtdIns(3,5)P2) are not the class I PI3K products that activate AKT.

## 7. Physiology, Human Genetics and Relevance to the Horse

Human genetic association studies link MTMR9 to energy balance, but they do not show that the protein's function is involved. In a three-stage Japanese case-control study, the coding-region SNP rs2293855 was associated with obesity (global P = 5 × 10⁻⁷) and with blood pressure. MTMR9 transcript and protein were found in the rodent lateral hypothalamus and arcuate nucleus, alongside orexin, MCH, NPY and POMC. Hypothalamic Mtmr9 mRNA rose with fasting and fell on a high-fat diet [yanagiya-2007-mtmr9-obesity-abstract]. The same SNP was associated with metabolic syndrome in an independent Japanese cohort [hotta-2011-metabolic-syndrome-abstract] and with glucose intolerance, lower insulin secretion and sensitivity, and prediabetes risk in Han Chinese [tang-2014-mtmr9-prediabetes-abstract]. MTMR9 lacks phosphatase activity, so any such effect probably works through its active partners [zou-2012-mtmr9-mtmr8-fulltext]. Weaker, family-based associations with nonsyndromic intellectual disability have also been reported [shi-2020-mtmr9-intellectual-disability-abstract]. Reviews of the family stress that catalytically dead myotubularins regulate their active homologs by heterodimerization and may be key players in the phosphoinositide kinase–phosphatase balance [hnia-2012-myotubularin-review-abstract; raess-2017-myotubularins-review-abstract].

No horse-specific functional, expression or genetic study of MTMR9 was found. The horse genome assembly [wade-2009-horse-genome-abstract] supplies the gene model. Given near-identity with human MTMR9 and an intact partner repertoire in horse (MTMR6, MTMR7 and MTMR8 entries all exist in the horse proteome; UniProt query, this work), horse MTMR9 is expected to work like the human protein, as a cytosolic and endomembrane-associated regulatory subunit of MTMR6/7/8. These equine traits make horse MTMR9 an interesting candidate for future study: equine metabolic syndrome, the shared obesity/insulin-dysregulation phenotypes in ponies, and the horse's highly oxidative skeletal muscle. To date, none of these has been linked to MTMR9.

## 8. Open Questions

Several gaps remain, both for MTMR9 generally and for the horse protein specifically. First, it is unknown whether the 507-residue A0A9L0T3C1 isoform is really expressed in horse tissues, and whether removing the 42-residue segment at the PH-GRAM–phosphatase-domain junction (human 98–139) changes folding, membrane recruitment or partner binding. RNA-seq junction analysis of equine tissues and co-expression tests with horse MTMR6/MTMR8 would answer this directly. Second, there is no experimental structure of MTMR9 or of any MTMR9 heterodimer. The coiled-coil interface is supported mainly by deletion mapping and AlphaFold3 models [mochizuki-2003-mtmr7-mtmr9-fulltext; saar-2025-mtmr-disordered-cterm-fulltext]. A structure would show how a pseudophosphatase changes its partner's substrate preference between PtdIns(3)P and PtdIns(3,5)P2 [zou-2012-mtmr9-mtmr8-fulltext]. Third, the localization data conflict: ER association in HeLa cells versus no calnexin overlap in A431 cells. Together with ERGIC/Golgi localization [zou-2009-mtmr9-mtmr6-fulltext; maekawa-2014-macropinocytosis-fulltext; doubravska-2020-mtmr9-er-golgi-abstract], this calls for endogenous-level imaging with validated antibodies and for testing the predicted ER-retention motifs. Fourth, the signals that assemble and disassemble MTMR9 complexes, such as their dissociation during starvation [zou-2012-mtmr9-mtmr8-fulltext], and the link between MTMR9 and AKT activity [guo-2013-tcell-phosphatases-fulltext] are mechanistically unexplained. Fifth, a knockout mouse was reported to be in preparation in 2012 [zou-2012-mtmr9-mtmr8-fulltext], but no organismal loss-of-function phenotype was found in this survey. Because rodents lack MTMR8 [mochizuki-2013-mtmr6-rab1b-fulltext], species that keep MTMR8, such as the horse, may be better models of the full MTMR9 interaction network. MTMR9 and KCa3.1 both bind the MTMR6 coiled coil [mochizuki-2013-mtmr6-rab1b-fulltext; srivastava-2005-mtmr6-kca31-fulltext]. Whether they compete for it or form a ternary complex in membrane ruffles is an open mechanistic question. Finally, it would be worth testing whether equine MTMR9 variants are associated with metabolic or insulin-dysregulation phenotypes, given the human data [yanagiya-2007-mtmr9-obesity-abstract; tang-2014-mtmr9-prediabetes-abstract].

## 9. References

- **[appel-2001-mtmr8]** Appel S, Reichwald K, Zimmermann W, Reis A, Rosenthal A, Hennies HC. Identification and localization of a new human myotubularin-related protein gene, mtmr8, on 8p22-p23. *Genomics* 2001;75:6-8. PMID: 11472061; DOI: 10.1006/geno.2001.6591.
- **[begley-2003-mtmr2-structure]** Begley MJ, Taylor GS, Kim SA, Veine DM, Dixon JE, Stuckey JA. Crystal structure of a phosphoinositide phosphatase, MTMR2: insights into myotubular myopathy and Charcot-Marie-Tooth syndrome. *Mol Cell* 2003;12:1391-402. PMID: 14690594; DOI: 10.1016/s1097-2765(03)00486-6.
- **[dang-2004-myotubularins-endocytosis]** Dang H, Li Z, Skolnik EY, Fares H. Disease-related myotubularins function in endocytic traffic in *Caenorhabditis elegans*. *Mol Biol Cell* 2004;15:189-96. PMID: 14565969; DOI: 10.1091/mbc.e03-08-0605; PMCID: PMC307539.
- **[doubravska-2020-mtmr9-er-golgi]** Doubravská L, Dostál V, Knop F, Libusová L, Macůrková M. Human myotubularin-related protein 9 regulates ER-to-Golgi trafficking and modulates WNT3A secretion. *Exp Cell Res* 2020;386:111709. PMID: 31704058; DOI: 10.1016/j.yexcr.2019.111709.
- **[guo-2013-tcell-phosphatases]** Guo L, Martens C, Bruno D, Porcella SF, Yamane H, Caucheteux SM, et al. Lipid phosphatases identified by screening a mouse phosphatase shRNA library regulate T-cell differentiation and protein kinase B AKT signaling. *Proc Natl Acad Sci USA* 2013;110:E1849-56. PMID: 23630283; DOI: 10.1073/pnas.1305070110; PMCID: PMC3657794.
- **[hnia-2012-myotubularin-review]** Hnia K, Vaccari I, Bolino A, Laporte J. Myotubularin phosphoinositide phosphatases: cellular functions and disease pathophysiology. *Trends Mol Med* 2012;18:317-27. PMID: 22578719; DOI: 10.1016/j.molmed.2012.04.004.
- **[hotta-2011-metabolic-syndrome]** Hotta K, Kitamoto T, Kitamoto A, Mizusawa S, Matsuo T, Nakata Y, et al. Association of variations in the FTO, SCG3 and MTMR9 genes with metabolic syndrome in a Japanese population. *J Hum Genet* 2011;56:647-51. PMID: 21796137; DOI: 10.1038/jhg.2011.74.
- **[laporte-2003-myotubularins-review]** Laporte J, Bedez F, Bolino A, Mandel JL. Myotubularins, a large disease-associated family of cooperating catalytically active and inactive phosphoinositides phosphatases. *Hum Mol Genet* 2003;12 Spec No 2:R285-92. PMID: 12925573; DOI: 10.1093/hmg/ddg273.
- **[liu-2022-pseudophosphatases-review]** Liu D, Zhang Y, Fang H, Yuan J, Ji L. The progress of research into pseudophosphatases. *Front Public Health* 2022;10:965631. PMID: 36106167; DOI: 10.3389/fpubh.2022.965631; PMCID: PMC9464862.
- **[lorenzo-2006-systematic-myotubularins]** Lorenzo O, Urbé S, Clague MJ. Systematic analysis of myotubularins: heteromeric interactions, subcellular localisation and endosome related functions. *J Cell Sci* 2006;119:2953-9. PMID: 16787938; DOI: 10.1242/jcs.03040.
- **[maekawa-2014-macropinocytosis]** Maekawa M, Terasaka S, Mochizuki Y, Kawai K, Ikeda Y, Araki N, et al. Sequential breakdown of 3-phosphorylated phosphoinositides is essential for the completion of macropinocytosis. *Proc Natl Acad Sci USA* 2014;111:E978-87. PMID: 24591580; DOI: 10.1073/pnas.1311029111; PMCID: PMC3964036.
- **[mochizuki-2003-mtmr7-mtmr9]** Mochizuki Y, Majerus PW. Characterization of myotubularin-related protein 7 and its binding partner, myotubularin-related protein 9. *Proc Natl Acad Sci USA* 2003;100:9768-73. PMID: 12890864; DOI: 10.1073/pnas.1333958100; PMCID: PMC187840.
- **[mochizuki-2013-mtmr6-rab1b]** Mochizuki Y, Ohashi R, Kawamura T, Iwanari H, Kodama T, Naito M, et al. Phosphatidylinositol 3-phosphatase myotubularin-related protein 6 (MTMR6) is regulated by small GTPase Rab1B in the early secretory and autophagic pathways. *J Biol Chem* 2013;288:1009-21. PMID: 23188820; DOI: 10.1074/jbc.M112.395087; PMCID: PMC3542987.
- **[raess-2017-myotubularins-review]** Raess MA, Friant S, Cowling BS, Laporte J. WANTED - Dead or alive: Myotubularins, a large disease-associated protein family. *Adv Biol Regul* 2017;63:49-58. PMID: 27666502; DOI: 10.1016/j.jbior.2016.09.001.
- **[robinson-2006-myotubularin-review]** Robinson FL, Dixon JE. Myotubularin phosphatases: policing 3-phosphoinositides. *Trends Cell Biol* 2006;16:403-12. PMID: 16828287; DOI: 10.1016/j.tcb.2006.06.001.
- **[saar-2025-mtmr-disordered-cterm]** Saar D, Lennartsson CLE, Weidner P, Burgermeister E, Kragelund BB. The Myotubularin Related Proteins and the Untapped Interaction Potential of Their Disordered C-Terminal Regions. *Proteins* 2025;93:831-854. PMID: 39614773; DOI: 10.1002/prot.26774; PMCID: PMC11878207.
- **[shi-2020-mtmr9-intellectual-disability]** Shi Z, Jia X, Tian Y, Liu X, Bai J, Liu Y, et al. Genetic Variants of the MTMR9 Gene Are Associated with Nonspecific Intellectual Disability: A Family-Based Association Study. *Genet Test Mol Biomarkers* 2020;24:625-631. PMID: 32991201; DOI: 10.1089/gtmb.2020.0145.
- **[silhankova-2010-mtm6-mtm9-wnt]** Silhankova M, Port F, Harterink M, Basler K, Korswagen HC. Wnt signalling requires MTM-6 and MTM-9 myotubularin lipid-phosphatase function in Wnt-producing cells. *EMBO J* 2010;29:4094-105. PMID: 21076391; DOI: 10.1038/emboj.2010.278; PMCID: PMC3018790.
- **[srivastava-2005-mtmr6-kca31]** Srivastava S, Li Z, Lin L, Liu G, Ko K, Coetzee WA, Skolnik EY. The phosphatidylinositol 3-phosphate phosphatase myotubularin-related protein 6 (MTMR6) is a negative regulator of the Ca2+-activated K+ channel KCa3.1. *Mol Cell Biol* 2005;25:3630-8. PMID: 15831468; DOI: 10.1128/MCB.25.9.3630-3638.2005; PMCID: PMC1084293.
- **[tang-2014-mtmr9-prediabetes]** Tang L, Tong Y, Cao H, Xie S, Yang Q, Zhang F, et al. The MTMR9 rs2293855 polymorphism is associated with glucose tolerance, insulin secretion, insulin sensitivity and increased risk of prediabetes. *Gene* 2014;546:150-5. PMID: 24937802; DOI: 10.1016/j.gene.2014.06.028.
- **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865-7. PMID: 19892987; DOI: 10.1126/science.1178158; PMCID: PMC3785132.
- **[xue-2003-myotubularins-elegans]** Xue Y, Fares H, Grant B, Li Z, Rose AM, Clark SG, Skolnik EY. Genetic analysis of the myotubularin family of phosphatases in *Caenorhabditis elegans*. *J Biol Chem* 2003;278:34380-6. PMID: 12788949; DOI: 10.1074/jbc.M303259200.
- **[yanagiya-2007-mtmr9-obesity]** Yanagiya T, Tanabe A, Iida A, Saito S, Sekine A, Takahashi A, et al. Association of single-nucleotide polymorphisms in MTMR9 gene with obesity. *Hum Mol Genet* 2007;16:3017-26. PMID: 17855449; DOI: 10.1093/hmg/ddm260.
- **[zou-2009-mtmr9-mtmr6]** Zou J, Chang SC, Marjanovic J, Majerus PW. MTMR9 increases MTMR6 enzyme activity, stability, and role in apoptosis. *J Biol Chem* 2009;284:2064-71. PMID: 19038970; DOI: 10.1074/jbc.M804292200; PMCID: PMC2629094.
- **[zou-2012-mtmr9-mtmr8]** Zou J, Zhang C, Marjanovic J, Kisseleva MV, Majerus PW, Wilson MP. Myotubularin-related protein (MTMR) 9 determines the enzymatic activity, substrate specificity, and role in autophagy of MTMR8. *Proc Natl Acad Sci USA* 2012;109:9539-44. PMID: 22647598; DOI: 10.1073/pnas.1207021109; PMCID: PMC3386095.

Database sources used for sequence and identity analysis: UniProtKB A0A9L0T3C1, A0A5F5PR89, F7CCR9 (horse MTMR9), Q96QG7 (human MTMR9), Q9Z2D0 (mouse Mtmr9); Ensembl gene ENSECAG00000014120 (as cross-referenced in UniProt). Local copies: `horse_MTMR9.fasta`, `horse_MTMR9_A0A5F5PR89.fasta`, `human_MTMR9_Q96QG7.fasta`, `mouse_Mtmr9_Q9Z2D0.fasta`.


## Citations

1. appel-2001-mtmr8-abstract.md
2. appel-2001-mtmr8-summary.md
3. begley-2003-mtmr2-structure-abstract.md
4. begley-2003-mtmr2-structure-summary.md
5. dang-2004-myotubularins-endocytosis-abstract.md
6. dang-2004-myotubularins-endocytosis-fulltext.txt
7. dang-2004-myotubularins-endocytosis-summary.md
8. doubravska-2020-mtmr9-er-golgi-abstract.md
9. doubravska-2020-mtmr9-er-golgi-summary.md
10. guo-2013-tcell-phosphatases-abstract.md
11. guo-2013-tcell-phosphatases-fulltext.txt
12. guo-2013-tcell-phosphatases-summary.md
13. hnia-2012-myotubularin-review-abstract.md
14. hnia-2012-myotubularin-review-summary.md
15. hotta-2011-metabolic-syndrome-abstract.md
16. hotta-2011-metabolic-syndrome-summary.md
17. laporte-2003-myotubularins-review-abstract.md
18. laporte-2003-myotubularins-review-summary.md
19. liu-2022-pseudophosphatases-review-abstract.md
20. liu-2022-pseudophosphatases-review-fulltext.txt
21. liu-2022-pseudophosphatases-review-summary.md
22. lorenzo-2006-systematic-myotubularins-abstract.md
23. lorenzo-2006-systematic-myotubularins-summary.md
24. maekawa-2014-macropinocytosis-abstract.md
25. maekawa-2014-macropinocytosis-fulltext.txt
26. maekawa-2014-macropinocytosis-summary.md
27. mochizuki-2003-mtmr7-mtmr9-abstract.md
28. mochizuki-2003-mtmr7-mtmr9-fulltext.txt
29. mochizuki-2003-mtmr7-mtmr9-summary.md
30. mochizuki-2013-mtmr6-rab1b-abstract.md
31. mochizuki-2013-mtmr6-rab1b-fulltext.txt
32. mochizuki-2013-mtmr6-rab1b-summary.md
33. raess-2017-myotubularins-review-abstract.md
34. raess-2017-myotubularins-review-summary.md
35. robinson-2006-myotubularin-review-abstract.md
36. robinson-2006-myotubularin-review-summary.md
37. saar-2025-mtmr-disordered-cterm-abstract.md
38. saar-2025-mtmr-disordered-cterm-fulltext.txt
39. saar-2025-mtmr-disordered-cterm-summary.md
40. shi-2020-mtmr9-intellectual-disability-abstract.md
41. shi-2020-mtmr9-intellectual-disability-summary.md
42. silhankova-2010-mtm6-mtm9-wnt-abstract.md
43. silhankova-2010-mtm6-mtm9-wnt-fulltext.txt
44. silhankova-2010-mtm6-mtm9-wnt-summary.md
45. srivastava-2005-mtmr6-kca31-abstract.md
46. srivastava-2005-mtmr6-kca31-fulltext.txt
47. srivastava-2005-mtmr6-kca31-summary.md
48. tang-2014-mtmr9-prediabetes-abstract.md
49. tang-2014-mtmr9-prediabetes-summary.md
50. wade-2009-horse-genome-abstract.md
51. wade-2009-horse-genome-summary.md
52. xue-2003-myotubularins-elegans-abstract.md
53. xue-2003-myotubularins-elegans-summary.md
54. yanagiya-2007-mtmr9-obesity-abstract.md
55. yanagiya-2007-mtmr9-obesity-summary.md
56. zou-2009-mtmr9-mtmr6-abstract.md
57. zou-2009-mtmr9-mtmr6-fulltext.txt
58. zou-2009-mtmr9-mtmr6-summary.md
59. zou-2012-mtmr9-mtmr8-abstract.md
60. zou-2012-mtmr9-mtmr8-fulltext.txt
61. zou-2012-mtmr9-mtmr8-summary.md