---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:32:48.148378'
end_time: '2026-10-26T00:53:30.982232'
duration_seconds: 1242.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: PIKFYVE
  gene_symbol: PIKFYVE
  uniprot_accession: A0A9L0JQ61
  protein_description: 'SubName: Full=Phosphoinositide kinase, FYVE-type zinc finger
    containing {ECO:0000313|Ensembl:ENSEASP00005055349.1};'
  gene_info: Name=PIKFYVE {ECO:0000313|Ensembl:ENSEASP00005055349.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: DEP_dom. (IPR000591); PIKfyve. (IPR043548); PIKfyve_DEP. (IPR037378);
    WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 93
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JQ61
- **Protein Description:** SubName: Full=Phosphoinositide kinase, FYVE-type zinc finger containing {ECO:0000313|Ensembl:ENSEASP00005055349.1};
- **Gene Information:** Name=PIKFYVE {ECO:0000313|Ensembl:ENSEASP00005055349.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DEP_dom. (IPR000591); PIKfyve. (IPR043548); PIKfyve_DEP. (IPR037378); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIKFYVE" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIKFYVE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIKFYVE** (gene ID: PIKFYVE, UniProt: A0A9L0JQ61) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PIKFYVE (UniProt A0A9L0JQ61) in the donkey, *Equus asinus*: function, localization and pathways

## 1. Introduction and summary

PIKFYVE encodes PIKfyve, the FYVE finger-containing phosphoinositide kinase. It is the mammalian ortholog of yeast Fab1p, and it is the enzyme that makes phosphatidylinositol 3,5-bisphosphate [PtdIns(3,5)P2] by phosphorylating the 5-hydroxyl of phosphatidylinositol 3-phosphate (PtdIns3P) [sbrissa-1999-pikfyve-5-phosphoinositides-abstract]. In the cell, PIKfyve's activity provides essentially all PtdIns(3,5)P2 and, through PtdIns(3,5)P2, nearly all phosphatidylinositol 5-phosphate (PtdIns5P) [zolov-2012-pikfyve-pi5p-precursor-abstract]. The enzyme works as part of a ternary complex with the scaffold VAC14 (ArPIKfyve) and the lipid phosphatase FIG4 (Sac3), which reverses the reaction [sbrissa-2007-pas-complex-abstract; lees-2020-pikfyve-complex-structure-abstract]. It is recruited to endosomal membranes when its N-terminal FYVE finger binds PtdIns3P [sbrissa-2002-pi3p-interacting-domains-abstract]. From there, its lipid products control the identity and dynamics of endosomes and lysosomes. They govern fission versus fusion, retrograde transport to the trans-Golgi network, receptor recycling, lysosome reformation, phagosome maturation, melanosome biogenesis and autophagy. They also gate lysosomal ion channels such as TRPML1 and the two-pore channels [rutherford-2006-pikfyve-retrograde-abstract; choy-2018-lysosome-coalescence-abstract; giridharan-2022-vps34-pikfyve-retriever-abstract; bissig-2017-pikfyve-lysosome-reformation-abstract; dong-2010-pi35p2-trpml1-abstract; wang-2012-tpc-phosphoinositide-channels-abstract; rivero-rios-2022-pikfyve-review-fulltext].

The UniProt entry under study, A0A9L0JQ61, is an unreviewed Ensembl prediction (protein existence level 4) from the donkey reference genome [wang-2020-donkey-genomes-abstract]. The symbol PIKFYVE is not ambiguous here. The entry carries the PIKfyve family signature (IPR043548; PANTHER PTHR46715) and the PIKfyve-specific DEP domain (IPR037378). Its sequence is identical to the corresponding region of full-length donkey PIKfyve and 441 of 460 residues identical to a curated human isoform (notes/sequence_analysis.md). It is not, however, the full-length kinase. Our sequence analysis shows that A0A9L0JQ61 is the donkey counterpart of human PIKfyve **isoform 3** (UniProt Q9Y2I7-3, 462 residues), an alternatively spliced product supported by a human full-length cDNA [gerhard-2004-mgc-full-length-cdna-abstract]. Like that isoform, it replaces most of the FYVE finger with a short alternative segment (NSLQHPQEN), and it ends just after the DEP domain with an alternative "GRR" C-terminus. It therefore lacks the chaperonin-like (CCT) domain, which binds VAC14 and FIG4, and the whole PIPK catalytic domain. The horse genome encodes an identical 460-residue product (notes/alignment_short_isoforms.txt), so this splice form is conserved across equids and primates. There is no experimental literature on PIKfyve in donkeys or horses, and none on the short isoform in any species. Everything about function below is therefore inferred from orthologs, mainly mouse and human, and from the domains this product retains. This report first describes what full-length PIKfyve does and then works out which of those properties the 460-residue product can and cannot have.

## 2. Identity of the target: a conserved short splice isoform of PIKFYVE

The UniProt record lists A0A9L0JQ61 as a 460-aa protein encoded by Ensembl transcript ENSEAST00005054447 (11 exons) of gene ENSEASG00005003072 on donkey chromosome 4. It is annotated with a DEP domain at residues 277–352 and several intrinsically disordered regions, but with no FYVE or kinase domain (notes/uniprot_A0A9L0JQ61.txt). The same gene has five transcripts with 42–44 exons that encode 2,052–2,108-residue proteins (notes/ensembl_gene_ENSEASG00005003072.txt). These match the 2,052-residue mouse protein [shisheva-1999-pikfyve-cloning-abstract] and the 2,098-residue human protein [cabezas-2006-human-pikfyve-cloning-abstract]. The gene also has a second short transcript encoding 449 residues (A0A9L0KIN8). We aligned A0A9L0JQ61 with the canonical full-length donkey product A0A8C4L106 (2,108 aa). The two are identical except for two features. First, the short product lacks a 97-residue segment corresponding to full-length residues ~117–213. Second, after the equivalent of full-length residue 555 it ends with a divergent "GRR" tripeptide (notes/alignment_A0A9L0JQ61_vs_A0A8C4L106.txt). The FYVE zinc finger of A0A8C4L106 lies at residues 168–228, so the internal deletion removes all but its last ~15 residues, including most of the zinc-coordinating cysteines (notes/uniprot_A0A8C4L106_features.txt).

Comparison with curated human isoforms shows this is a conserved splice form and not a donkey-specific gene-model error. UniProt documents four human PIKFYVE isoforms, with the short ones attributed to cDNA evidence from the Mammalian Gene Collection [gerhard-2004-mgc-full-length-cdna-abstract]. In human isoform 3 (Q9Y2I7-3, 462 aa), residues 109–203, which span most of the FYVE finger, are replaced by the nonapeptide NSLQHPQEN. Isoforms 2, 3 and 4 all replace residues 546–548 (EYL) with GRR and lack residues 549–2098 (notes/uniprot_Q9Y2I7_human.txt). The donkey product contains exactly the NSLQHPQEN junction (…VLE**NSLQHPQEN**TGDLRACTYC…) and the same …PADQK**GRR** C-terminus. Its global alignment with human isoform 3 and with the matching human Ensembl transcript ENST00000308862 (462 aa) gives 441 identical residues with the same block structure. The horse Ensembl transcript ENSECAT00000071693 (PIKFYVE-203, 10 exons) encodes a 460-residue protein 100% identical to the donkey product (notes/alignment_short_isoforms.txt). Human and horse also each carry a 449–451-residue variant matching donkey A0A9L0KIN8 (human isoform 2) (notes/ensembl_pikfyve_horse_human_transcripts.txt). Alternative splicing of PIKFYVE has been reported from the start: the original mouse cloning study detected at least two close-in-size splice variants [shisheva-1999-pikfyve-cloning-abstract], and zebrafish pip5k3 has four temporally regulated splice variants [boisset-2008-zebrafish-pip5k3-abstract]. However, the dominant form detected in human cell lines is a single full-length species [cabezas-2006-human-pikfyve-cloning-abstract]. No study has detected a ~50 kDa N-terminal PIKfyve polypeptide or assigned it a function. The conserved transcript structure strongly suggests that A0A9L0JQ61 is a genuine isoform, but its expression level as a protein, its tissue distribution and its function are unknown.

## 3. Domain architecture of PIKfyve and what the short isoform retains

Full-length mammalian PIKfyve is a large multidomain protein. From N to C terminus it has a Zn2+-binding FYVE finger, a DEP domain, a central chaperonin-like (Cpn60_TCP1/CCT) region and a C-terminal phosphoinositide 5-kinase (PIPK) catalytic domain [shisheva-1999-pikfyve-cloning-abstract; cabezas-2006-human-pikfyve-cloning-abstract]. InterPro uses the same architecture to define the PIKfyve-specific DEP domain family (notes/interpro_IPR037378.txt). The FYVE finger is a high-affinity, specific PtdIns3P-binding module whose conserved basic core is required for lipid binding. An intact finger is absolutely required to target PIKfyve to membranes of the late endocytic pathway [sbrissa-2002-pi3p-interacting-domains-abstract]. The N-terminal region binds about 2.2 molar equivalents of Zn2+, and an N-terminal fragment loses its vesicular localization when Zn2+ is chelated or the FYVE finger is truncated [shisheva-1999-pikfyve-cloning-abstract]. The chaperonin-like domain has two interaction roles. It is the main determinant for binding the ArPIKfyve(VAC14)–Sac3(FIG4) subcomplex [ikonomov-2009-core-complex-contacts-abstract], and it is also the binding site for the kinesin adapter JLP, which couples PIKfyve to microtubule-based endosome-to-TGN transport [ikonomov-2009-jlp-pikfyve-furin-abstract]. Cryo-EM placed the CCT module on the PIKfyve density closest to VAC14, with the kinase domain extending away from the complex [lees-2020-pikfyve-complex-structure-fulltext]. The catalytic domain carries both the lipid kinase and the protein kinase activities; truncating it (Δ1812–2052, mouse numbering) or introducing the K1831E substitution abolishes both [sbrissa-2000-pikfyve-protein-kinase-abstract]. Regions outside the catalytic domain are also needed for full enzymatic activity [sbrissa-1999-pikfyve-5-phosphoinositides-abstract].

The DEP domain is named in the human cloning paper [cabezas-2006-human-pikfyve-cloning-abstract], but our PubMed searches found no study that tests its function in PIKfyve or Fab1. The published cryo-EM analysis modelled only the CCT and kinase modules of PIKfyve, and it reported additional density that was not assigned to any domain [lees-2020-pikfyve-complex-structure-fulltext]. In the donkey short isoform, the DEP domain (277–352) is intact and nearly identical to the human sequence. The isoform also keeps the N-terminal stretch that carries several regulatory serines known from human and rodent PIKfyve. Mapped onto donkey numbering (notes/sequence_analysis.md), these are as follows. Ser23 and Ser48 are autophosphorylation sites, and Ser48 is also dephosphorylated by FIG4 [lees-2020-pikfyve-complex-structure-fulltext]. Donkey Ser102 corresponds to human Ser105, which PKB/Akt phosphorylates in vitro [hill-2010-pikfyve-phosphorylation-insulin-abstract]. Donkey Ser219 corresponds to the AMPK site Ser307 [liu-2013-pikfyve-ampk-abstract]. Donkey Ser230 corresponds to Ser318, the insulin-regulated PKB site [berwick-2004-pkb-pikfyve-glut4-abstract; hill-2010-pikfyve-phosphorylation-insulin-abstract]. The isoform thus combines the N-terminal regulatory region and the DEP domain. It lacks the three elements that define PIKfyve's biochemical function: PtdIns3P-dependent membrane targeting (FYVE), assembly with VAC14–FIG4 and JLP (chaperonin-like domain), and catalysis (PIPK domain).

## 4. Catalytic function and substrate specificity of full-length PIKfyve

PIKfyve's defining reaction is ATP-dependent phosphorylation of PtdIns3P at the D-5 position of the inositol ring, which produces PtdIns(3,5)P2 (EC 2.7.1.150). Recombinant and native mouse PIKfyve make PtdIns(3,5)P2 from PtdIns3P in vitro. They also convert PtdIns into PtdIns5P, and in such assays the enzyme strongly prefers PtdIns over other phosphoinositide substrates [sbrissa-1999-pikfyve-5-phosphoinositides-abstract; shisheva-1999-pikfyve-cloning-abstract]. The enzyme is sensitive to nonionic detergents and relatively resistant to wortmannin [sbrissa-1999-pikfyve-5-phosphoinositides-abstract]. Mutating basic residues of the activation loop separates the two products. In mouse PIKfyve, K1999E preferentially loses PtdIns(3,5)P2 synthesis and K2000E preferentially loses PtdIns5P synthesis. Only the PtdIns(3,5)P2-deficient mutant caused the hallmark endomembrane swelling, and microinjected PtdIns(3,5)P2 specifically rescued it. PtdIns(3,5)P2 is therefore the product critical for endomembrane integrity [ikonomov-2001-lipid-protein-kinase-dissection-abstract]. Lys1999 also forms a low-affinity PtdIns3P-binding site within the catalytic domain [sbrissa-2002-pi3p-interacting-domains-abstract].

Where cellular PtdIns5P comes from was debated for some time. Low doses of the selective inhibitor YM201636 preferentially reduced cellular PtdIns5P, which pointed to PIKfyve as its principal source [sbrissa-2012-ym201636-pi5p-abstract]. Genetic work settled the question: in a Pikfyve hypomorph (~10% of normal protein) combined with shRNA, PIKfyve was required for the entire PtdIns(3,5)P2 pool and nearly all of the PtdIns5P pool. PtdIns5P was made from PtdIns(3,5)P2, probably by a 3-phosphatase, rather than by direct 5-phosphorylation of PtdIns [zolov-2012-pikfyve-pi5p-precursor-abstract]. The current consensus is that the PIKfyve–FIG4–VAC14 complex controls both PI(3,5)P2 and PI(5)P, the two least abundant phosphoinositides [rivero-rios-2022-pikfyve-review-abstract]. PIKfyve is also a serine-directed protein kinase. It autophosphorylates and can phosphorylate exogenous proteins, and this activity cannot be separated from the lipid kinase activity: it is absent in kinase-dead (K1831E) and catalytic-domain-truncated mutants. Autophosphorylation lowers lipid product formation by about 70% [sbrissa-2000-pikfyve-protein-kinase-abstract]. The selective inhibitors YM201636 and apilimod both block PIKfyve phosphotransferase activity [jefferies-2008-ym201636-abstract; cai-2013-apilimod-pikfyve-abstract].

A0A9L0JQ61 lacks the whole PIPK domain, so it cannot carry out any of these reactions by itself. The UniProt record nevertheless carries "1-phosphatidylinositol-3-phosphate 5-kinase activity", an electronic annotation transferred from InterPro (notes/uniprot_A0A9L0JQ61.txt). That term is valid for the full-length products of the gene but not for this isoform.

## 5. The PIKfyve–VAC14–FIG4 complex and its phosphoregulation

PIKfyve does not act alone. Human Vac14 (ArPIKfyve) associates with PIKfyve and activates it. Depleting Vac14 lowers PIKfyve activity and the conversion of PtdIns3P to PtdIns(3,5)P2, and reproduces the vacuolation phenotype [sbrissa-2004-arpikfyve-vac14-abstract]. The PtdIns(3,5)P2 5-phosphatase Sac3/FIG4 forms a stable ternary complex with PIKfyve and ArPIKfyve (the "PAS" complex), which physically couples synthesis and turnover of the lipid [sbrissa-2007-pas-complex-abstract]. ArPIKfyve organizes this complex through C-terminal homomeric interactions; a peptide that disrupts them dissociates the complex and lowers PIKfyve activity [sbrissa-2008-arpikfyve-scaffold-abstract]. Within the complex, the chaperonin-like domain of PIKfyve is the main binding surface for ArPIKfyve–Sac3 [ikonomov-2009-core-complex-contacts-abstract]. Work in yeast and mouse showed that Vac14 is a HEAT-repeat scaffold that contacts Fab1/PIKfyve, Fig4 and other regulators. It also showed that Fab1 must associate with the complex for the mouse to survive: the *ingls* Vac14 missense mutation blocks Fab1 binding [jin-2008-vac14-complex-abstract].

Structural biochemistry has clarified both the architecture and the internal regulation. The human complex contains a star-shaped pentamer of VAC14 with one PIKfyve and one FIG4. Within the isolated complex, steric constraints prevent PIKfyve from reaching phosphoinositides embedded in membranes [lees-2020-pikfyve-complex-structure-abstract]. Mass spectrometry identified PIKfyve autophosphorylation sites (S23, S48, S1522, S1669, S1969 and S2053, the last in the activation loop). Autophosphorylation represses lipid kinase activity and stimulates FIG4's lipid phosphatase activity. In turn, FIG4 acts as a protein phosphatase on S48, S1669 and S2053, which stimulates PIKfyve [lees-2020-pikfyve-complex-structure-fulltext]. This reciprocal mechanism explains why catalytically active FIG4 is needed for maximal PtdIns(3,5)P2 production in vivo [lees-2020-pikfyve-complex-structure-abstract]. AlphaFold2- and cryo-EM-based modelling has since shown that VAC14 oligomerization is itself required for Fab1/PIKfyve function, and that VAC14 mutations from pediatric neurodegeneration cluster at the VAC14–VAC14 interfaces [zhang-2025-vac14-oligomerization-abstract].

Signalling kinases outside the complex also regulate PIKfyve. PKB/Akt phosphorylates Ser318 in response to insulin, which stimulates PtdIns3P 5-kinase activity. The S318A mutant enhances insulin-stimulated IRAP/GLUT4 vesicle translocation [berwick-2004-pkb-pikfyve-glut4-abstract]. A later study confirmed that PKB phosphorylates S318 directly and ruled out autophosphorylation. It also found that PKB phosphorylates S105 in vitro but not in cells, and that hyperosmotic stress phosphorylates S318 through a PKB-independent route [hill-2010-pikfyve-phosphorylation-insulin-abstract]. AMPK phosphorylates Ser307, which promotes PIKfyve recruitment to endosomes and contributes to contraction-stimulated glucose uptake in muscle [liu-2013-pikfyve-ampk-abstract]. During glucose starvation, AMPK-activated ULK1 phosphorylates S1548. This raises PtdIns5P synthesis without changing PtdIns(3,5)P2 and drives the formation of PtdIns5P-containing autophagosomes [karabiyik-2021-ulk1-pikfyve-autophagy-abstract]. In the donkey short isoform the N-terminal sites are conserved (S23, S48, S102/S105, S219/S307 and S230/S318), but S1548, S1669, S2053 and the catalytic domain are absent. Any regulatory role for this isoform would therefore have to work in trans on full-length PIKfyve or on partner proteins. That idea is a hypothesis and has not been demonstrated.

## 6. Subcellular localization

Endogenous PIKfyve is distributed between cytosol and membranes. In 3T3-L1 adipocytes, about 76% is cytosolic, about 20% is in a low-density microsomal fraction and about 4% is at the plasma membrane. The membrane-associated pool overlaps trans-Golgi network and multivesicular-body markers rather than GLUT4 or recycling-endosome markers, and insulin recruits cytosolic PIKfyve onto membranes [shisheva-2001-adipocyte-localization-abstract]. When expressed at low levels in HeLa cells, PIKfyve associates mainly with dynamic tubular and vesicular elements of early endosomes [rutherford-2006-pikfyve-retrograde-abstract]. Human PIKfyve localizes to early endosomes that contain EEA1 and Hrs, but within microdomains separate from those proteins [cabezas-2006-human-pikfyve-cloning-abstract]. Endogenous PIKfyve colocalizes with the SNX17, Retriever, WASH and CCC complexes on endosomes [giridharan-2022-vps34-pikfyve-retriever-abstract] and cofractionates with JLP in the perinuclear region [ikonomov-2009-jlp-pikfyve-furin-abstract]. Membrane association depends on PtdIns3P, made mainly by VPS34: wortmannin releases PIKfyve from endosomes, and the FYVE finger is essential for targeting [sbrissa-2002-pi3p-interacting-domains-abstract; giridharan-2022-vps34-pikfyve-retriever-abstract]. PI(3,5)P2 is hard to detect, so its presence on early endosomes, late endosomes and lysosomes is largely inferred from where PIKfyve is found [rivero-rios-2022-pikfyve-review-fulltext]. Functional studies place PIKfyve activity on phagosomes in macrophages and neutrophils and on stage I melanosomes in melanocytes [kim-2014-pikfyve-phagosome-maturation-abstract; dayam-2017-pikfyve-neutrophil-rac-abstract; bissig-2019-pikfyve-melanosome-amyloid-abstract].

The short isoform has almost no FYVE finger. It should therefore be unable to bind PtdIns3P-containing endosomal membranes by the canonical mechanism. An intact finger is absolutely required for late-endocytic targeting, and the catalytic-domain PtdIns3P-binding site, which this isoform also lacks, cannot substitute for it [sbrissa-2002-pi3p-interacting-domains-abstract]. If the isoform is expressed, it is most likely largely cytosolic, as the FYVE-truncated N-terminal mouse fragment was [shisheva-1999-pikfyve-cloning-abstract], unless the DEP domain or other regions mediate a different membrane interaction. The UniProt electronic annotations "cytoplasmic vesicle" and "vesicle membrane" are inherited from the full-length family, and they should be treated cautiously for this gene product.

## 7. Pathways and cellular roles of the PIKfyve lipid products

PIKfyve sits downstream of the class III PI 3-kinase VPS34 in a phosphoinositide cascade on endosomes: VPS34 makes PtdIns3P, which both recruits PIKfyve and serves as its substrate [giridharan-2022-vps34-pikfyve-retriever-abstract]. Loss of PIKfyve activity, whether by dominant-negative mutants, siRNA, or YM201636 and apilimod, most consistently causes dramatic enlargement of endosomes and lysosomes and cytoplasmic vacuolation. *fab1Δ* yeast show the same phenotype [ikonomov-2001-lipid-protein-kinase-dissection-abstract; rutherford-2006-pikfyve-retrograde-abstract; jefferies-2008-ym201636-abstract; shisheva-2008-pikfyve-review-abstract]. The swelling reflects reduced membrane fission and reduced exit of cargo, particularly endosome-to-TGN retrograde traffic. It does not reflect a defect in multivesicular-body biogenesis, endocytic uptake or degradation [rutherford-2006-pikfyve-retrograde-abstract]. For cargo such as furin, retrograde transport depends on microtubules and on the PIKfyve–JLP interaction [ikonomov-2009-jlp-pikfyve-furin-abstract]. On acute inhibition, lysosomes enlarge by coalescence, as fusion outpaces fission, rather than by increased biogenesis, even though TFEB, TFE3 and MITF are activated [choy-2018-lysosome-coalescence-abstract]. PIKfyve activity is also needed for the extensive membrane remodelling that reforms terminal storage lysosomes from endolysosomes [bissig-2017-pikfyve-lysosome-reformation-abstract]. PIKfyve and VPS34 together promote recycling of integrins and other cargo through the SNX17–Retriever–WASH–CCC pathway, and PIKfyve inhibition displaces Retriever and CCC from endosomes [giridharan-2022-vps34-pikfyve-retriever-abstract].

Several downstream effectors of PI(3,5)P2 have been identified at the molecular level. Patch-clamp recordings of endolysosomes show that PI(3,5)P2 binds and activates TRPML Ca2+-release channels with specificity and potency. TRPML1 overexpression suppresses the enlarged-vacuole phenotype of PI(3,5)P2-deficient fibroblasts, and the PI(3,5)P2–TRPML link is conserved in yeast [dong-2010-pi35p2-trpml1-abstract]. The endolysosomal two-pore channels TPC1 and TPC2 are Na+-selective channels activated by PI(3,5)P2, not by NAADP [wang-2012-tpc-phosphoinositide-channels-abstract]. Atomic structures confirm that PI(3,5)P2 binds TRPML1, TPC1 and TPC2 directly. PIKfyve/Fab1 also contributes to lysosomal and vacuolar acidification, in part through the V-ATPase, and TRPML1 partly mediates the fission of enlarged vacuoles [rivero-rios-2022-pikfyve-review-fulltext]. PIKfyve also regulates the lysosomal transcription factor TFEB: it supports mTORC1-dependent phosphorylation of TFEB Ser211 and so keeps TFEB on lysosomes, and inhibition lets PP2A dephosphorylate TFEB, which then enters the nucleus [rivero-rios-2022-pikfyve-review-fulltext].

These membrane functions explain PIKfyve's more specialized roles in particular cell types. In macrophages, PIKfyve inhibition delays removal of PtdIns3P from phagosomes and reduces their acquisition of LAMP1 and cathepsin D and their degradative capacity [kim-2014-pikfyve-phagosome-maturation-abstract]. In neutrophils, PIKfyve is required for phagosome–lysosome fusion, which TRPML1 agonists or Ca2+ ionophores partly rescue, and for chemotaxis, reactive oxygen species production and Rac activation. The proposed model divides the labour: PI(3,5)P2–TRPML1 drives phagosome maturation, and PtdIns5P–Rac drives motility and ROS [dayam-2017-pikfyve-neutrophil-rac-abstract]. In melanocytes, PIKfyve is required for the delivery of melanosomal proteins (PMEL, TYRP1) from endosomes, and melanocyte-specific knockout mice grey [liggins-2018-pikfyve-melanosome-abstract]. PIKfyve activity shapes stage I melanosomes, their PMEL amyloid matrix and their kiss-and-run contacts with lysosomes through endosomal actin branching [bissig-2019-pikfyve-melanosome-amyloid-abstract]. These studies are the experimental basis for the family-level GO terms that UniProt transfers to A0A9L0JQ61: phagosome–lysosome fusion, neutrophil chemotaxis, regulation of reactive oxygen species biosynthesis and melanosome organization. Through PtdIns5P, PIKfyve also mediates insulin-induced disassembly of actin stress fibres [sbrissa-2012-ym201636-pi5p-abstract] and ULK1-driven autophagy under glucose starvation [karabiyik-2021-ulk1-pikfyve-autophagy-abstract]. In metabolic signalling, PIKfyve activity and its phosphorylation by PKB and AMPK are linked to GLUT4 trafficking and to insulin- and contraction-stimulated glucose uptake [berwick-2004-pkb-pikfyve-glut4-abstract; sbrissa-2008-arpikfyve-scaffold-abstract; liu-2013-pikfyve-ampk-abstract]. In innate immune signalling, PIKfyve is required for Toll-like receptor-induced IL-12/IL-23p40 expression [cai-2013-apilimod-pikfyve-abstract]. Its inhibition also blocks retroviral budding [jefferies-2008-ym201636-abstract].

## 8. Physiological and disease relevance

Whole-organism genetics show that PIKfyve is essential. Global *Pikfyve* knockout mouse embryos die before the 32–64-cell stage, and null fibroblasts show markedly reduced DNA synthesis. Heterozygotes are ostensibly normal despite having about 50% less protein [ikonomov-2011-pikfyve-knockout-embryo-abstract]. A hypomorph with ~10% of normal protein shows that PIKfyve is critical in neural tissue, heart, lung, kidney, thymus and spleen [zolov-2012-pikfyve-pi5p-precursor-abstract]. Loss of PIKfyve specifically in melanocytes causes coat hypopigmentation [liggins-2018-pikfyve-melanosome-abstract]. In humans, heterozygous missense, frameshift and truncating PIKFYVE (PIP5K3) mutations cause autosomal-dominant François-Neetens fleck corneal dystrophy [li-2005-pip5k3-fleck-corneal-dystrophy-abstract]. In zebrafish, the orthologous gene is expressed in cornea, lens and retina [boisset-2008-zebrafish-pip5k3-abstract]. Several of the corneal dystrophy mutations (for example R851X, Q988X, E1030X and R1038X) truncate the protein before the catalytic domain [li-2005-pip5k3-fleck-corneal-dystrophy-abstract]. This supports the expectation that PIKfyve products lacking the kinase domain are catalytically null. Mutations in the partners FIG4 and VAC14 that lower PI(3,5)P2 cause neurodegenerative disorders [zolov-2012-pikfyve-pi5p-precursor-abstract; jin-2008-vac14-complex-abstract; rivero-rios-2022-pikfyve-review-abstract]. PIKfyve inhibitors are being tested for neurodegenerative diseases, cancers and SARS-CoV-2 infection [rivero-rios-2022-pikfyve-review-abstract]. The donkey genome study that produced the gene model does not discuss PIKFYVE [wang-2020-donkey-genomes-fulltext], and we found no functional studies of PIKfyve in equids.

## 9. Implications for functional annotation of A0A9L0JQ61

The full-length donkey PIKfyve products, such as A0A8C4L106, can be annotated with confidence by orthology. Their molecular function is 1-phosphatidylinositol-3-phosphate 5-kinase activity (PtdIns3P + ATP → PtdIns(3,5)P2 + ADP), with secondary 1-phosphatidylinositol 5-kinase and autophosphorylating protein serine kinase activities. They act on the cytosolic face of early endosomes, late endosomes, lysosomes, phagosomes and early melanosomes, recruited by PtdIns3P, in complex with VAC14 and FIG4. Their biological roles include endosome-to-TGN retrograde transport, endosomal recycling, lysosome fission and reformation, gating of lysosomal channels, phagosome maturation, melanosome biogenesis and PtdIns5P-dependent signalling and autophagy [sbrissa-1999-pikfyve-5-phosphoinositides-abstract; sbrissa-2000-pikfyve-protein-kinase-abstract; sbrissa-2002-pi3p-interacting-domains-abstract; lees-2020-pikfyve-complex-structure-abstract; dong-2010-pi35p2-trpml1-abstract; bissig-2017-pikfyve-lysosome-reformation-abstract; dayam-2017-pikfyve-neutrophil-rac-abstract; liggins-2018-pikfyve-melanosome-abstract; rivero-rios-2022-pikfyve-review-fulltext].

The evidence for the 460-residue A0A9L0JQ61 supports a narrower conclusion. It is a conserved alternatively spliced isoform of PIKFYVE, orthologous to human isoform 3 and identical to a horse transcript product. It contains the N-terminal regulatory region and the DEP domain, and it lacks the FYVE finger, the chaperonin-like domain and the catalytic domain. It therefore cannot be an active phosphoinositide 5-kinase, and it is unlikely to be targeted to endosomes by the canonical FYVE mechanism. Electronic annotations that transfer catalytic activity, vesicle-membrane localization or downstream biological processes from the family to this entry are not supported for this particular gene product. A defensible annotation would be limited to its membership of the PIKfyve family and the presence of the PIKfyve DEP domain, with any function left unknown. If the isoform has a role, the most plausible kinds are non-catalytic, such as regulatory or dominant-interfering effects through the DEP domain or the N-terminal phosphosites, but none has been tested.

## 10. Open Questions

The most direct open question is whether the short isoform is made as a protein, and where. The conservation of its exon structure, NSLQHPQEN junction and GRR terminus across donkey, horse and human (notes/alignment_short_isoforms.txt) argues that the splice event is real. Quantifying it in equine tissues by RNA-seq junction counts, and detecting junction-spanning peptides by proteomics, would show whether the isoform is a meaningful product or a minor splicing outcome. The temporal regulation of splice variants seen in zebrafish eye development [boisset-2008-zebrafish-pip5k3-abstract] suggests that developmental and corneal tissues would be good places to look. If the protein exists, it would be worth testing whether the DEP-containing N-terminal fragment binds full-length PIKfyve, VAC14, FIG4 or membranes. It would also be worth testing whether its expression changes cellular PtdIns(3,5)P2 or PtdIns5P levels or vacuolation, as was done for the dominant-negative constructs [ikonomov-2001-lipid-protein-kinase-dissection-abstract].

Several questions about PIKfyve in general remain open. The function of the PIKfyve DEP domain is unknown in every species. The unassigned density in the cryo-EM maps [lees-2020-pikfyve-complex-structure-fulltext] and AlphaFold models of the complex [zhang-2025-vac14-oligomerization-abstract] could show whether the DEP domain contacts VAC14 or FIG4 or is free to bind membranes. It is still unclear how PIKfyve within the complex reaches membrane PtdIns3P despite the steric constraints seen in vitro [lees-2020-pikfyve-complex-structure-abstract]. The phosphatase that converts PtdIns(3,5)P2 to PtdIns5P has not been identified [zolov-2012-pikfyve-pi5p-precursor-abstract], and how PI(3,5)P2 mechanistically drives membrane fission is not known [rivero-rios-2022-pikfyve-review-fulltext]. For equids, no study has examined PIKfyve biology. Natural first targets would be corneal stroma (given the human fleck dystrophy), skeletal muscle glucose uptake, coat pigmentation (in view of the melanocyte knockout phenotype and the donkey coat-colour genomics [wang-2020-donkey-genomes-abstract]) and innate immune cells. Such studies would confirm whether the conserved mammalian functions apply in the donkey.

## 11. References

- **[berwick-2004-pkb-pikfyve-glut4]** Berwick DC, Dell GC, Welsh GI, Heesom KJ, Hers I, Fletcher LM, et al. (2004). Protein kinase B phosphorylation of PIKfyve regulates the trafficking of GLUT4 vesicles. *Journal of cell science* 117:5985-93. PMID: 15546921; DOI: 10.1242/jcs.01517. https://pubmed.ncbi.nlm.nih.gov/15546921/
- **[bissig-2017-pikfyve-lysosome-reformation]** Bissig C, Hurbain I, Raposo G, van Niel G (2017). PIKfyve activity regulates reformation of terminal storage lysosomes from endolysosomes. *Traffic (Copenhagen, Denmark)* 18:747-757. PMID: 28857423; DOI: 10.1111/tra.12525. https://pubmed.ncbi.nlm.nih.gov/28857423/
- **[bissig-2019-pikfyve-melanosome-amyloid]** Bissig C, Croisé P, Heiligenstein X, Hurbain I, Lenk GM, Kaufman E, et al. (2019). The PIKfyve complex regulates the early melanosome homeostasis required for physiological amyloid formation. *Journal of cell science* 132. PMID: 30709920; PMCID: PMC6432708; DOI: 10.1242/jcs.229500. https://pubmed.ncbi.nlm.nih.gov/30709920/
- **[boisset-2008-zebrafish-pip5k3]** Boisset G, Polok BK, Schorderet DF (2008). Characterization of pip5k3 fleck corneal dystrophy-linked gene in zebrafish. *Gene expression patterns : GEP* 8:404-410. PMID: 18558518; DOI: 10.1016/j.gep.2008.04.007. https://pubmed.ncbi.nlm.nih.gov/18558518/
- **[cabezas-2006-human-pikfyve-cloning]** Cabezas A, Pattni K, Stenmark H (2006). Cloning and subcellular localization of a human phosphatidylinositol 3-phosphate 5-kinase, PIKfyve/Fab1. *Gene* 371:34-41. PMID: 16448788; DOI: 10.1016/j.gene.2005.11.009. https://pubmed.ncbi.nlm.nih.gov/16448788/
- **[cai-2013-apilimod-pikfyve]** Cai X, Xu Y, Cheung AK, Tomlinson RC, Alcázar-Román A, Murphy L, et al. (2013). PIKfyve, a class III PI kinase, is the target of the small molecular IL-12/IL-23 inhibitor apilimod and a player in Toll-like receptor signaling. *Chemistry & biology* 20:912-21. PMID: 23890009; PMCID: PMC4878021; DOI: 10.1016/j.chembiol.2013.05.010. https://pubmed.ncbi.nlm.nih.gov/23890009/
- **[choy-2018-lysosome-coalescence]** Choy CH, Saffi G, Gray MA, Wallace C, Dayam RM, Ou ZA, et al. (2018). Lysosome enlargement during inhibition of the lipid kinase PIKfyve proceeds through lysosome coalescence. *Journal of cell science* 131. PMID: 29661845; PMCID: PMC6031331; DOI: 10.1242/jcs.213587. https://pubmed.ncbi.nlm.nih.gov/29661845/
- **[dayam-2017-pikfyve-neutrophil-rac]** Dayam RM, Sun CX, Choy CH, Mancuso G, Glogauer M, Botelho RJ (2017). The Lipid Kinase PIKfyve Coordinates the Neutrophil Immune Response through the Activation of the Rac GTPase. *Journal of immunology (Baltimore, Md. : 1950)* 199:2096-2105. PMID: 28779020; DOI: 10.4049/jimmunol.1601466. https://pubmed.ncbi.nlm.nih.gov/28779020/
- **[dong-2010-pi35p2-trpml1]** Dong XP, Shen D, Wang X, Dawson T, Li X, Zhang Q, et al. (2010). PI(3,5)P(2) controls membrane trafficking by direct activation of mucolipin Ca(2+) release channels in the endolysosome. *Nature communications* 1:38. PMID: 20802798; PMCID: PMC2928581; DOI: 10.1038/ncomms1037. https://pubmed.ncbi.nlm.nih.gov/20802798/
- **[gerhard-2004-mgc-full-length-cdna]** Gerhard DS, Wagner L, Feingold EA, Shenmen CM, Grouse LH, Schuler G, et al. (2004). The status, quality, and expansion of the NIH full-length cDNA project: the Mammalian Gene Collection (MGC). *Genome research* 14:2121-7. PMID: 15489334; PMCID: PMC528928; DOI: 10.1101/gr.2596504. https://pubmed.ncbi.nlm.nih.gov/15489334/
- **[giridharan-2022-vps34-pikfyve-retriever]** Giridharan SSP, Luo G, Rivero-Rios P, Steinfeld N, Tronchere H, Singla A, et al. (2022). Lipid kinases VPS34 and PIKfyve coordinate a phosphoinositide cascade to regulate retriever-mediated recycling on endosomes. *eLife* 11. PMID: 35040777; PMCID: PMC8816382; DOI: 10.7554/eLife.69709. https://pubmed.ncbi.nlm.nih.gov/35040777/
- **[hill-2010-pikfyve-phosphorylation-insulin]** Hill EV, Hudson CA, Vertommen D, Rider MH, Tavaré JM (2010). Regulation of PIKfyve phosphorylation by insulin and osmotic stress. *Biochemical and biophysical research communications* 397:650-5. PMID: 20513353; DOI: 10.1016/j.bbrc.2010.05.134. https://pubmed.ncbi.nlm.nih.gov/20513353/
- **[ikonomov-2001-lipid-protein-kinase-dissection]** Ikonomov OC, Sbrissa D, Mlak K, Kanzaki M, Pessin J, Shisheva A (2002). Functional dissection of lipid and protein kinase signals of PIKfyve reveals the role of PtdIns 3,5-P2 production for endomembrane integrity. *The Journal of biological chemistry* 277:9206-11. PMID: 11714711; DOI: 10.1074/jbc.M108750200. https://pubmed.ncbi.nlm.nih.gov/11714711/
- **[ikonomov-2009-core-complex-contacts]** Ikonomov OC, Sbrissa D, Fenner H, Shisheva A (2009). PIKfyve-ArPIKfyve-Sac3 core complex: contact sites and their consequence for Sac3 phosphatase activity and endocytic membrane homeostasis. *The Journal of biological chemistry* 284:35794-806. PMID: 19840946; PMCID: PMC2791009; DOI: 10.1074/jbc.M109.037515. https://pubmed.ncbi.nlm.nih.gov/19840946/
- **[ikonomov-2009-jlp-pikfyve-furin]** Ikonomov OC, Fligger J, Sbrissa D, Dondapati R, Mlak K, Deeb R, et al. (2009). Kinesin adapter JLP links PIKfyve to microtubule-based endosome-to-trans-Golgi network traffic of furin. *The Journal of biological chemistry* 284:3750-61. PMID: 19056739; PMCID: PMC2635046; DOI: 10.1074/jbc.M806539200. https://pubmed.ncbi.nlm.nih.gov/19056739/
- **[ikonomov-2011-pikfyve-knockout-embryo]** Ikonomov OC, Sbrissa D, Delvecchio K, Xie Y, Jin JP, Rappolee D, et al. (2011). The phosphoinositide kinase PIKfyve is vital in early embryonic development: preimplantation lethality of PIKfyve-/- embryos but normality of PIKfyve+/- mice. *The Journal of biological chemistry* 286:13404-13. PMID: 21349843; PMCID: PMC3075686; DOI: 10.1074/jbc.M111.222364. https://pubmed.ncbi.nlm.nih.gov/21349843/
- **[jefferies-2008-ym201636]** Jefferies HB, Cooke FT, Jat P, Boucheron C, Koizumi T, Hayakawa M, et al. (2008). A selective PIKfyve inhibitor blocks PtdIns(3,5)P(2) production and disrupts endomembrane transport and retroviral budding. *EMBO reports* 9:164-70. PMID: 18188180; PMCID: PMC2246419; DOI: 10.1038/sj.embor.7401155. https://pubmed.ncbi.nlm.nih.gov/18188180/
- **[jin-2008-vac14-complex]** Jin N, Chow CY, Liu L, Zolov SN, Bronson R, Davisson M, et al. (2008). VAC14 nucleates a protein complex essential for the acute interconversion of PI3P and PI(3,5)P(2) in yeast and mouse. *The EMBO journal* 27:3221-34. PMID: 19037259; PMCID: PMC2600653; DOI: 10.1038/emboj.2008.248. https://pubmed.ncbi.nlm.nih.gov/19037259/
- **[karabiyik-2021-ulk1-pikfyve-autophagy]** Karabiyik C, Vicinanza M, Son SM, Rubinsztein DC (2021). Glucose starvation induces autophagy via ULK1-mediated activation of PIKfyve in an AMPK-dependent manner. *Developmental cell* 56:1961-1975.e5. PMID: 34107300; DOI: 10.1016/j.devcel.2021.05.010. https://pubmed.ncbi.nlm.nih.gov/34107300/
- **[kim-2014-pikfyve-phagosome-maturation]** Kim GH, Dayam RM, Prashar A, Terebiznik M, Botelho RJ (2014). PIKfyve inhibition interferes with phagosome and endosome maturation in macrophages. *Traffic (Copenhagen, Denmark)* 15:1143-63. PMID: 25041080; DOI: 10.1111/tra.12199. https://pubmed.ncbi.nlm.nih.gov/25041080/
- **[lees-2020-pikfyve-complex-structure]** Lees JA, Li P, Kumar N, Weisman LS, Reinisch KM (2020). Insights into Lysosomal PI(3,5)P2 Homeostasis from a Structural-Biochemical Analysis of the PIKfyve Lipid Kinase Complex. *Molecular cell* 80:736-743.e4. PMID: 33098764; PMCID: PMC7962480; DOI: 10.1016/j.molcel.2020.10.003. https://pubmed.ncbi.nlm.nih.gov/33098764/
- **[li-2005-pip5k3-fleck-corneal-dystrophy]** Li S, Tiab L, Jiao X, Munier FL, Zografos L, Frueh BE, et al. (2005). Mutations in PIP5K3 are associated with François-Neetens mouchetée fleck corneal dystrophy. *American journal of human genetics* 77:54-63. PMID: 15902656; PMCID: PMC1226194; DOI: 10.1086/431346. https://pubmed.ncbi.nlm.nih.gov/15902656/
- **[liggins-2018-pikfyve-melanosome]** Liggins MC, Flesher JL, Jahid S, Vasudeva P, Eby V, Takasuga S, et al. (2018). PIKfyve regulates melanosome biogenesis. *PLoS genetics* 14:e1007290. PMID: 29584722; PMCID: PMC5889185; DOI: 10.1371/journal.pgen.1007290. https://pubmed.ncbi.nlm.nih.gov/29584722/
- **[liu-2013-pikfyve-ampk]** Liu Y, Lai YC, Hill EV, Tyteca D, Carpentier S, Ingvaldsen A, et al. (2013). Phosphatidylinositol 3-phosphate 5-kinase (PIKfyve) is an AMPK target participating in contraction-stimulated glucose uptake in skeletal muscle. *The Biochemical journal* 455:195-206. PMID: 23905686; DOI: 10.1042/BJ20130644. https://pubmed.ncbi.nlm.nih.gov/23905686/
- **[rivero-rios-2022-pikfyve-review]** Rivero-Ríos P, Weisman LS (2022). Roles of PIKfyve in multiple cellular pathways. *Current opinion in cell biology* 76:102086. PMID: 35584589; PMCID: PMC9108489; DOI: 10.1016/j.ceb.2022.102086. https://pubmed.ncbi.nlm.nih.gov/35584589/
- **[rutherford-2006-pikfyve-retrograde]** Rutherford AC, Traer C, Wassmer T, Pattni K, Bujny MV, Carlton JG, et al. (2006). The mammalian phosphatidylinositol 3-phosphate 5-kinase (PIKfyve) regulates endosome-to-TGN retrograde transport. *Journal of cell science* 119:3944-57. PMID: 16954148; PMCID: PMC1904490; DOI: 10.1242/jcs.03153. https://pubmed.ncbi.nlm.nih.gov/16954148/
- **[sbrissa-1999-pikfyve-5-phosphoinositides]** Sbrissa D, Ikonomov OC, Shisheva A (1999). PIKfyve, a mammalian ortholog of yeast Fab1p lipid kinase, synthesizes 5-phosphoinositides. Effect of insulin. *The Journal of biological chemistry* 274:21589-97. PMID: 10419465; DOI: 10.1074/jbc.274.31.21589. https://pubmed.ncbi.nlm.nih.gov/10419465/
- **[sbrissa-2000-pikfyve-protein-kinase]** Sbrissa D, Ikonomov OC, Shisheva A (2000). PIKfyve lipid kinase is a protein kinase: downregulation of 5'-phosphoinositide product formation by autophosphorylation. *Biochemistry* 39:15980-9. PMID: 11123925; DOI: 10.1021/bi001897f. https://pubmed.ncbi.nlm.nih.gov/11123925/
- **[sbrissa-2002-pi3p-interacting-domains]** Sbrissa D, Ikonomov OC, Shisheva A (2002). Phosphatidylinositol 3-phosphate-interacting domains in PIKfyve. Binding specificity and role in PIKfyve. Endomenbrane localization. *The Journal of biological chemistry* 277:6073-9. PMID: 11706043; DOI: 10.1074/jbc.M110194200. https://pubmed.ncbi.nlm.nih.gov/11706043/
- **[sbrissa-2004-arpikfyve-vac14]** Sbrissa D, Ikonomov OC, Strakova J, Dondapati R, Mlak K, Deeb R, et al. (2004). A mammalian ortholog of Saccharomyces cerevisiae Vac14 that associates with and up-regulates PIKfyve phosphoinositide 5-kinase activity. *Molecular and cellular biology* 24:10437-47. PMID: 15542851; PMCID: PMC529046; DOI: 10.1128/MCB.24.23.10437-10447.2004. https://pubmed.ncbi.nlm.nih.gov/15542851/
- **[sbrissa-2007-pas-complex]** Sbrissa D, Ikonomov OC, Fu Z, Ijuin T, Gruenberg J, Takenawa T, et al. (2007). Core protein machinery for mammalian phosphatidylinositol 3,5-bisphosphate synthesis and turnover that regulates the progression of endosomal transport. Novel Sac phosphatase joins the ArPIKfyve-PIKfyve complex. *The Journal of biological chemistry* 282:23878-91. PMID: 17556371; DOI: 10.1074/jbc.M611678200. https://pubmed.ncbi.nlm.nih.gov/17556371/
- **[sbrissa-2008-arpikfyve-scaffold]** Sbrissa D, Ikonomov OC, Fenner H, Shisheva A (2008). ArPIKfyve homomeric and heteromeric interactions scaffold PIKfyve and Sac3 in a complex to promote PIKfyve activity and functionality. *Journal of molecular biology* 384:766-79. PMID: 18950639; PMCID: PMC2756758; DOI: 10.1016/j.jmb.2008.10.009. https://pubmed.ncbi.nlm.nih.gov/18950639/
- **[sbrissa-2012-ym201636-pi5p]** Sbrissa D, Ikonomov OC, Filios C, Delvecchio K, Shisheva A (2012). Functional dissociation between PIKfyve-synthesized PtdIns5P and PtdIns(3,5)P2 by means of the PIKfyve inhibitor YM201636. *American journal of physiology. Cell physiology* 303:C436-46. PMID: 22621786; PMCID: PMC3422984; DOI: 10.1152/ajpcell.00105.2012. https://pubmed.ncbi.nlm.nih.gov/22621786/
- **[shisheva-1999-pikfyve-cloning]** Shisheva A, Sbrissa D, Ikonomov O (1999). Cloning, characterization, and expression of a novel Zn2+-binding FYVE finger-containing phosphoinositide kinase in insulin-sensitive cells. *Molecular and cellular biology* 19:623-34. PMID: 9858586; PMCID: PMC83920; DOI: 10.1128/MCB.19.1.623. https://pubmed.ncbi.nlm.nih.gov/9858586/
- **[shisheva-2001-adipocyte-localization]** Shisheva A, Rusin B, Ikonomov OC, DeMarco C, Sbrissa D (2001). Localization and insulin-regulated relocation of phosphoinositide 5-kinase PIKfyve in 3T3-L1 adipocytes. *The Journal of biological chemistry* 276:11859-69. PMID: 11112776; DOI: 10.1074/jbc.M008437200. https://pubmed.ncbi.nlm.nih.gov/11112776/
- **[shisheva-2008-pikfyve-review]** Shisheva A (2008). PIKfyve: Partners, significance, debates and paradoxes. *Cell biology international* 32:591-604. PMID: 18304842; PMCID: PMC2491398; DOI: 10.1016/j.cellbi.2008.01.006. https://pubmed.ncbi.nlm.nih.gov/18304842/
- **[wang-2012-tpc-phosphoinositide-channels]** Wang X, Zhang X, Dong XP, Samie M, Li X, Cheng X, et al. (2012). TPC proteins are phosphoinositide- activated sodium-selective ion channels in endosomes and lysosomes. *Cell* 151:372-83. PMID: 23063126; PMCID: PMC3475186; DOI: 10.1016/j.cell.2012.08.036. https://pubmed.ncbi.nlm.nih.gov/23063126/
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://pubmed.ncbi.nlm.nih.gov/33293529/
- **[zhang-2025-vac14-oligomerization]** Zhang L, Uygun T, Hahn HJ, Liu Y, Rivero-Ríos P, Li D, et al. (2025). VAC14 oligomerization is essential for the function of the FAB1/PIKfyve-VAC14-FIG4 complex. *Molecular biology of the cell* 36:ar78. PMID: 40305106; PMCID: PMC12260172; DOI: 10.1091/mbc.E24-11-0490. https://pubmed.ncbi.nlm.nih.gov/40305106/
- **[zolov-2012-pikfyve-pi5p-precursor]** Zolov SN, Bridges D, Zhang Y, Lee WW, Riehle E, Verma R, et al. (2012). In vivo, Pikfyve generates PI(3,5)P2, which serves as both a signaling lipid and the major precursor for PI5P. *Proceedings of the National Academy of Sciences of the United States of America* 109:17472-7. PMID: 23047693; PMCID: PMC3491506; DOI: 10.1073/pnas.1203106109. https://pubmed.ncbi.nlm.nih.gov/23047693/


## Citations

1. berwick-2004-pkb-pikfyve-glut4-abstract.md
2. berwick-2004-pkb-pikfyve-glut4-summary.md
3. bissig-2017-pikfyve-lysosome-reformation-abstract.md
4. bissig-2017-pikfyve-lysosome-reformation-summary.md
5. bissig-2019-pikfyve-melanosome-amyloid-abstract.md
6. bissig-2019-pikfyve-melanosome-amyloid-summary.md
7. boisset-2008-zebrafish-pip5k3-abstract.md
8. boisset-2008-zebrafish-pip5k3-summary.md
9. cabezas-2006-human-pikfyve-cloning-abstract.md
10. cabezas-2006-human-pikfyve-cloning-summary.md
11. cai-2013-apilimod-pikfyve-abstract.md
12. cai-2013-apilimod-pikfyve-fulltext.txt
13. cai-2013-apilimod-pikfyve-summary.md
14. choy-2018-lysosome-coalescence-abstract.md
15. choy-2018-lysosome-coalescence-summary.md
16. dayam-2017-pikfyve-neutrophil-rac-abstract.md
17. dayam-2017-pikfyve-neutrophil-rac-summary.md
18. dong-2010-pi35p2-trpml1-abstract.md
19. dong-2010-pi35p2-trpml1-fulltext.txt
20. dong-2010-pi35p2-trpml1-summary.md
21. gerhard-2004-mgc-full-length-cdna-abstract.md
22. gerhard-2004-mgc-full-length-cdna-summary.md
23. giridharan-2022-vps34-pikfyve-retriever-abstract.md
24. giridharan-2022-vps34-pikfyve-retriever-fulltext.txt
25. giridharan-2022-vps34-pikfyve-retriever-summary.md
26. hill-2010-pikfyve-phosphorylation-insulin-abstract.md
27. hill-2010-pikfyve-phosphorylation-insulin-summary.md
28. ikonomov-2001-lipid-protein-kinase-dissection-abstract.md
29. ikonomov-2001-lipid-protein-kinase-dissection-summary.md
30. ikonomov-2009-core-complex-contacts-abstract.md
31. ikonomov-2009-core-complex-contacts-summary.md
32. ikonomov-2009-jlp-pikfyve-furin-abstract.md
33. ikonomov-2009-jlp-pikfyve-furin-summary.md
34. ikonomov-2011-pikfyve-knockout-embryo-abstract.md
35. ikonomov-2011-pikfyve-knockout-embryo-summary.md
36. jefferies-2008-ym201636-abstract.md
37. jefferies-2008-ym201636-fulltext.txt
38. jefferies-2008-ym201636-summary.md
39. jin-2008-vac14-complex-abstract.md
40. jin-2008-vac14-complex-fulltext.txt
41. jin-2008-vac14-complex-summary.md
42. karabiyik-2021-ulk1-pikfyve-autophagy-abstract.md
43. karabiyik-2021-ulk1-pikfyve-autophagy-summary.md
44. kim-2014-pikfyve-phagosome-maturation-abstract.md
45. kim-2014-pikfyve-phagosome-maturation-summary.md
46. lees-2020-pikfyve-complex-structure-abstract.md
47. lees-2020-pikfyve-complex-structure-fulltext.txt
48. lees-2020-pikfyve-complex-structure-summary.md
49. li-2005-pip5k3-fleck-corneal-dystrophy-abstract.md
50. li-2005-pip5k3-fleck-corneal-dystrophy-summary.md
51. liggins-2018-pikfyve-melanosome-abstract.md
52. liggins-2018-pikfyve-melanosome-fulltext.txt
53. liggins-2018-pikfyve-melanosome-summary.md
54. liu-2013-pikfyve-ampk-abstract.md
55. liu-2013-pikfyve-ampk-summary.md
56. rivero-rios-2022-pikfyve-review-abstract.md
57. rivero-rios-2022-pikfyve-review-fulltext.txt
58. rivero-rios-2022-pikfyve-review-summary.md
59. rutherford-2006-pikfyve-retrograde-abstract.md
60. rutherford-2006-pikfyve-retrograde-fulltext.txt
61. rutherford-2006-pikfyve-retrograde-summary.md
62. sbrissa-1999-pikfyve-5-phosphoinositides-abstract.md
63. sbrissa-1999-pikfyve-5-phosphoinositides-summary.md
64. sbrissa-2000-pikfyve-protein-kinase-abstract.md
65. sbrissa-2000-pikfyve-protein-kinase-summary.md
66. sbrissa-2002-pi3p-interacting-domains-abstract.md
67. sbrissa-2002-pi3p-interacting-domains-summary.md
68. sbrissa-2004-arpikfyve-vac14-abstract.md
69. sbrissa-2004-arpikfyve-vac14-summary.md
70. sbrissa-2007-pas-complex-abstract.md
71. sbrissa-2007-pas-complex-summary.md
72. sbrissa-2008-arpikfyve-scaffold-abstract.md
73. sbrissa-2008-arpikfyve-scaffold-fulltext.txt
74. sbrissa-2008-arpikfyve-scaffold-summary.md
75. sbrissa-2012-ym201636-pi5p-abstract.md
76. sbrissa-2012-ym201636-pi5p-summary.md
77. shisheva-1999-pikfyve-cloning-abstract.md
78. shisheva-1999-pikfyve-cloning-summary.md
79. shisheva-2001-adipocyte-localization-abstract.md
80. shisheva-2001-adipocyte-localization-summary.md
81. shisheva-2008-pikfyve-review-abstract.md
82. shisheva-2008-pikfyve-review-summary.md
83. wang-2012-tpc-phosphoinositide-channels-abstract.md
84. wang-2012-tpc-phosphoinositide-channels-fulltext.txt
85. wang-2012-tpc-phosphoinositide-channels-summary.md
86. wang-2020-donkey-genomes-abstract.md
87. wang-2020-donkey-genomes-fulltext.txt
88. wang-2020-donkey-genomes-summary.md
89. zhang-2025-vac14-oligomerization-abstract.md
90. zhang-2025-vac14-oligomerization-fulltext.txt
91. zhang-2025-vac14-oligomerization-summary.md
92. zolov-2012-pikfyve-pi5p-precursor-abstract.md
93. zolov-2012-pikfyve-pi5p-precursor-summary.md