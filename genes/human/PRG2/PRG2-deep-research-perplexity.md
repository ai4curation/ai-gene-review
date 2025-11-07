---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-03T21:51:37.272304'
end_time: '2025-11-03T21:53:54.800515'
duration_seconds: 137.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: P13727
  gene_symbol: PRG2
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
---

## Question

# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene PRG2 (P13727) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
This is a comprehensive request for a research report on the gene PRG2 (P13727), also known as proteoglycan 2 or eosinophil major basic protein (MBP). The user wants a detailed narrative explaining function, biological processes, and localization, with proper citations.

Let me plan this out:

## Planning my approach:

1. **Main Themes to Cover:**
   - Gene and protein identification/nomenclature
   - Molecular structure and organization
   - Cellular localization and compartmentalization
   - Primary biological functions (cytotoxic, antimicrobial, immunomodulatory)
   - Biochemical mechanisms of action
   - Protein-protein interactions
   - Transcriptional regulation
   - Signaling pathways
   - Disease associations
   - Storage and activation mechanisms

2. **Available Evidence in Sources:**
   - Multiple database entries (GeneCards, UniProt, NCBI)
   - Research on structural properties (C-type lectin-like fold)
   - Functional studies on cytotoxicity
   - Interactions with basophils and mast cells (histamine release)
   - Interactions with PAPPA and IGF bioavailability
   - Transcriptional regulation (GATA-1, PU.1, C/EBPε)
   - Storage in crystalline cores
   - Piecemeal degranulation mechanisms
   - Role in allergic diseases
   - Potential tumor suppressor role
   - Effects on epithelial cells
   - Antimicrobial activity
   - Heparan sulfate binding

3. **Sections I should structure:**
   - Title and Introduction with key findings
   - Gene Nomenclature and Identification
   - Protein Structure and Molecular Features
   - Cellular Localization and Compartmentalization
   - Storage and Crystalline Organization
   - Primary Biological Functions:
     * Cytotoxic and antimicrobial properties
     * Immunomodulatory effects
     * Basophil and mast cell activation
   - Molecular Mechanisms and Signaling Pathways
   - Protein-Protein Interactions
   - Transcriptional Regulation and Gene Expression
   - Degranulation and Secretion
   - Physiological and Pathological Roles
   - Conclusion

I'll develop a comprehensive research strategy to explore the multifaceted aspects of PRG2, systematically investigating its molecular characteristics, functional significance, and potential clinical implications. The approach will integrate structural analysis, functional studies, and pathological insights to provide a holistic understanding of this complex protein.

The diverse source references cover critical domains including cytotoxicity, antimicrobial activity, cellular interactions, transcriptional mechanisms, and potential therapeutic applications. I'll focus on synthesizing information across immunological, cellular, and molecular perspectives to construct a nuanced research framework.

Key research priorities include examining protein-protein interactions, exploring transcriptional regulation mechanisms, and understanding the protein's role in allergic responses and potential tumor suppression. The comprehensive source collection enables an in-depth, multidimensional investigation of PRG2's biological significance.
</think>

# Comprehensive Functional Annotation of the PRG2 Gene: Molecular Structure, Cellular Localization, and Biological Functions

The PRG2 gene (protein coding gene located on chromosome 11q12.1) encodes proteoglycan 2, also known as eosinophil major basic protein (MBP), which represents one of the most abundant and potent effector molecules produced by eosinophils[1][7][10]. This 117-amino acid protein serves as the predominant constituent of the crystalline core within eosinophil-specific granules and is subject to precise transcriptional and post-translational regulation to ensure safe storage while maintaining immediate availability for rapid cytotoxic deployment upon immune challenge[1][3][28]. PRG2 functions as a multifaceted molecular weapon in immune defense, exhibiting potent antimicrobial activity against gram-positive and gram-negative bacteria as well as fungi, while simultaneously orchestrating complex immunomodulatory effects through direct interactions with basophils, mast cells, and respiratory epithelial cells[1][7][20][22]. Beyond its classical roles in allergic inflammation and parasitic defense, emerging evidence suggests PRG2 may serve as a biomarker for certain hematologic disorders and possibly exert tumor-suppressive activities in specific disease contexts[3][55]. This comprehensive report synthesizes current molecular, biochemical, and cellular biological knowledge regarding PRG2, with particular emphasis on its structural features, subcellular compartmentalization, primary enzymatic and immunological functions, and integration into broader physiological and pathological processes.

## Molecular Nomenclature, Gene Organization, and Protein Identity

The PRG2 gene has been assigned multiple identifiers across biological databases, including HGNC identifier 9362, NCBI Gene ID 5553, and Ensembl gene ID ENSG00000186652[1][10]. The protein product carries the UniProtKB/Swiss-Prot accession number P13727 and is commonly referred to by several synonyms reflecting its discovery and functional characterization history: bone marrow proteoglycan (BMPG), eosinophil granule major basic protein (EMBP), and natural killer cell activator[1][9]. The gene is located on the long arm of chromosome 11 (11q12.1) and spans approximately 4.9 kilobases of genomic DNA, encompassing six exons that generate the mature 222-amino acid protein following removal of the signal peptide and proteolytic processing of the prosequence[1][38]. The PRG2 gene produces alternatively spliced transcript variants that encode different isoforms, providing molecular diversity that may contribute to tissue-specific functions[1][50]. The predominant form synthesized during eosinophil differentiation is the proform (proMBP or proform of eosinophil major basic protein), consisting of an acidic N-terminal propiece comprising residues 1-106 connected through disulfide bonds to the highly cationic mature MBP domain (residues 107-222)[35][56]. The pro-domain serves a critical protective function during intracellular trafficking and storage, neutralizing the extreme basicity of the mature MBP and preventing accidental cytotoxic activation within the cell[35][56].

The gene exists as part of a small proteoglycan family, with PRG3 (also called eosinophil major basic protein 2 or MBP-2) representing an important paralog that shares approximately 73% amino acid sequence identity with PRG2 and exhibits similar functional properties including cytotoxic and immunomodulatory activities[52][40]. The structural similarity between PRG2 and PRG3 suggests they may have evolved from a common ancestral gene through duplication events, though their distinct tissue distribution and regulatory mechanisms indicate functional specialization[52]. In contrast to PRG3, PRG2 is predominantly expressed in bone marrow and placenta at the highest levels, with lower expression detected in a variety of tissues including kidney, myometrium, endometrium, ovaries, breast, prostate, and colon, suggesting regulated developmental and tissue-specific expression patterns[1][9][41].

## Structural Organization and Molecular Architecture

PRG2/MBP possesses a unique structural fold categorized as a C-type lectin-like domain (CTLD), despite lacking the characteristic calcium-binding and carbohydrate-recognition properties of classical C-type lectins[7][30][56]. The protein architecture consists of two α-helices and seven β-strands organized into three anti-parallel β-sheet arrays, with two disulfide bonds (Cys125-Cys220 and Cys197-Cys212) stabilizing local conformations by connecting the α1 helix to β7 strand and anchoring the β6-Loop6-β7 region[56]. Crystallographic studies of granule-associated MBP-1 (gMBP-1) resolved at high resolution reveal a highly positive molecular surface, consistent with the protein's extreme basicity arising from its exceptionally high content of arginine and lysine residues (approximately 21% of amino acids)[56]. This cationic character is central to MBP's mechanism of action, enabling electrostatic interactions with anionic cellular membranes and enabling rapid membrane disruption following secretion.

Unlike canonical C-type lectins that recognize carbohydrates through a conserved canonical calcium-binding pocket, PRG2 instead recognizes heparan sulfate proteoglycans (HSPGs) through discrete surface-exposed residues that mediate specific protein-ligand interactions[7][56]. The downward-pointing loop configuration characteristic of the CTL fold in MBP is stabilized through aromatic stacking interactions involving tryptophan (Trp185) and proline (Pro190) residues, which engage in hydrophobic interactions with neighboring molecules during crystalline core formation[56]. This architectural feature is remarkably conserved across eosinophil MBP-1 homologues in higher primates, suggesting strong evolutionary pressure to maintain this specific structural arrangement, likely reflecting its functional importance for both storage and activation mechanisms.

The proform of PRG2 (proMBP) adds complexity to the structural organization through three intramolecular disulfide bonds linking the acidic propiece to the cationic MBP domain[35]. These disulfide linkages (Cys51-Cys169, Cys89-Cys128, and Cys104-Cys107) are thermodynamically stable in the oxidizing extracellular environment but are subject to controlled reduction through enzymatic and redox-sensitive mechanisms that regulate transition from the inactive proform to the toxic mature form[25][35]. The propiece itself contributes a high density of negatively charged acidic residues (glutamate and aspartate), providing electrostatic neutralization of the positive charges on the mature MBP domain and rendering proMBP physiologically inert and unsuitable for membrane disruption[25][35]. This elegant structural design ensures that the inherent toxicity of mature MBP is sequestered until appropriate biological signals trigger its liberation through proteolytic cleavage or redox-dependent disulfide reduction.

## Cellular Localization and Intracellular Compartmentalization

PRG2 demonstrates a highly specialized subcellular localization pattern reflecting its unique biology as an eosinophil-specific granule protein. During eosinophil differentiation, PRG2 synthesis occurs on ribosomes associated with the endoplasmic reticulum (ER), where the nascent polypeptide chain is directed to the ER lumen through an N-terminal signal peptide, leading to synthesis of the proform[1][9]. Following removal of the signal peptide by signal peptidase during translocation, proMBP transits from the ER through the Golgi apparatus in vesicular carriers, eventually accumulating within the specialized secretory granules characteristic of mature eosinophils[3][15]. Within these secretory granules, proMBP is packaged into the crystalloid core—an extraordinarily ordered nanocrystalline structure formed through precise intermolecular stacking interactions that occur exclusively following proteolytic removal of the propiece[25][28][56].

The organization into nanocrystalline cores appears to be a fundamental requirement for eosinophil viability, as studies employing targeted ablation of core cationic proteins (either EPX or MBP) result in selective loss of eosinophil lineage-committed progenitors and prevent normal eosinophil differentiation[3][15]. This remarkable observation suggests that the crystalline organization itself is essential for surviving the cytotoxic potential of these proteins and protecting the developing cell from self-inflicted damage. The crystalline arrangement achieves this through subtle conformational locking of the protein monomers that restrains their intrinsic membrane-disrupting potential until appropriate activation signals trigger crystal disassembly.

In placental tissues, proMBP localizes to the X cells of the syncytiotrophoblast septa and anchoring villi, where it exists in circulating levels in pregnancy serum[1][9][35]. The precise physiological function of proMBP in pregnancy remains incompletely understood, though its association with pregnancy-associated plasma protein A (PAPPA) and its regulatory effects on insulin-like growth factor bioavailability suggest roles in placental growth factor physiology and fetal development[3][21][35].

## Storage Mechanisms and Regulated Activation

The storage of PRG2/MBP within eosinophil granules represents one of biology's most elegant solutions to the problem of safely housing a broadly toxic protein until the moment of deployment. The crystalline core packaging mechanism fundamentally alters the conformational state and biological activity of MBP-1, rendering intact nanocrystalline cores completely inert in bacterial killing assays despite the inherent toxicity of the monomeric protein[28]. This inactivation is achieved through specific intermolecular interactions occurring along crystallographic axes that stabilize conformations incompatible with membrane disruption. When crystalline cores are exposed to acidic pH conditions (pH 3.0), which occur during eosinophil granule acidification upon activation, the nanocrystals undergo controlled disassembly, liberating monomeric MBP-1 that rapidly undergoes amyloidogenic aggregation at neutral pH, ultimately generating the toxic oligomeric or fibrillar assemblies responsible for antimicrobial and immunomodulatory activities[28].

This pH-dependent activation mechanism represents a sophisticated two-stage control system ensuring that antimicrobial activity is reserved exclusively for extracellular environments where activated eosinophils encounter pathogens. The granule acidification below pH 4.0 that occurs upon immune stimulation through Fc receptors, chemokine receptors, or complement activation provides the biological trigger for this transformation[3][15][28]. Following granule acidification, eosinophils employ two complementary secretion pathways: classical exocytotic degranulation involving fusion of entire granules with the plasma membrane, and the more refined piecemeal degranulation (PMD) pathway that mobilizes specific granule constituents into small secretory vesicles for targeted delivery[15][18].

The piecemeal degranulation pathway demonstrates remarkable selectivity in transporting individual granule proteins, with MBP-1-containing vesicles trafficked through the cytoplasm in close association with the granule membrane, enabling regulated release of MBP-1 while leaving other granule components intact[15][18][33]. This selective trafficking mechanism depends critically upon receptor-mediated recognition of specific proteins within the granule lumen, with evidence indicating that cytokine-specific secretion is mediated through recognition by their cognate receptors localized to granule and secretory vesicle membranes[18]. The mobilization of MBP-1 into secretory vesicles occurs through budding from membrano-vesicular networks within the granule, producing tubular carriers and pleiomorphic vesicles that traverse the cytoplasm before docking and fusing with the plasma membrane[15][18][33].

## Primary Biological Functions: Cytotoxic and Antimicrobial Properties

PRG2/MBP exerts potent antimicrobial activity through a fundamentally different mechanism from most traditional antimicrobial peptides, operating as a broad-spectrum toxin rather than a sequence-specific pathogen recognition molecule. The protein is directly toxic to a wide spectrum of targets including gram-positive bacteria, gram-negative bacteria, fungi, parasitic helminths, and even mammalian cells in vitro, reflecting its non-specific membrane-disrupting mechanism[1][7][20][22]. The peptide contains specific regions displaying particularly potent antimicrobial activity against gram-positive and gram-negative bacteria as well as fungi, though the molecular basis for any differential selectivity among these organisms remains incompletely characterized[1][20].

The cytotoxic mechanism involves initial formation of ion-selective pores in target cell membranes through insertion of oligomeric MBP-1 assemblies, followed by progression to non-selective membrane fragmentation as amyloid fibrils form on the membrane surface[28][31]. This two-step process bears mechanistic similarity to membrane disruption by amyloid-beta in neurodegeneration, suggesting that amyloidogenic aggregation may represent a general mechanism by which cationic antimicrobial peptides achieve their cytotoxic effects[28][31][34]. The formation of these structures depends upon the protein's extreme basicity, which enables electrostatic interactions with anionic phospholipid head groups and anionic polysaccharides on bacterial cell walls. The initial pore formation steps can be partially blocked by zinc ions, implicating specific histidine residues in the pore-forming mechanism, though the detailed structural basis remains to be fully elucidated[28].

Against parasitic helminths, MBP appears particularly effective, consistent with its evolutionary role in antiparasitic defense during helminth infection[1][36]. The protein acts as both a direct helminthotoxin through membrane disruption and an indirect effector through recruitment and activation of immune cells. The broad-spectrum nature of MBP toxicity reflects its lack of reliance on specific receptors or pathogen-associated molecular patterns, instead exploiting the fundamental biophysical incompatibility between a highly cationic peptide and the anionic lipid bilayers present on all cell membranes. This makes MBP immune to evasion strategies commonly employed against pattern recognition receptors, though it also requires careful containment within the eosinophil to prevent autotoxicity.

## Immunomodulatory Functions and Cross-talk with Mast Cells and Basophils

Beyond direct antimicrobial toxicity, PRG2/MBP serves critical immunomodulatory functions through diverse interactions with resident immune cells, particularly basophils and mast cells. MBP directly triggers non-cytolytic histamine release from purified human basophils through a mechanism that is IgE-independent and fundamentally distinct from classical IgE-mediated degranulation[11][37][40]. This basophil activation occurs with kinetics and potency characteristics similar to activation by other polycations such as poly-L-arginine, though MBP proves somewhat less potent than similarly-sized polycationic molecules[11][37]. The mechanism underlying MBP-induced histamine release involves electrostatic interactions between the highly cationic protein and anionic molecular targets on the basophil surface, likely involving plasma membrane proteoglycans or other anionic molecules, rather than a classical ligand-receptor interaction[11][37][40].

Critically, reduction and alkylation of MBP, treatments that modify cysteine residues within the protein, substantially diminish both the potency and efficacy of histamine release from human basophils, indicating that the native cysteine-containing disulfide structures are essential for optimal basophil activation[11][37]. This surprising dependence of an activity attributed to net charge on the native disulfide bonding pattern suggests more complex molecular interactions than simple electrostatic attraction, possibly involving specific conformational requirements for optimal engagement with basophil surface molecules.

MBP also activates rat peritoneal mast cells to release histamine in a manner characteristic of polycations, though the relative potency differs from basophil activation, and eosinophil cationic protein (ECP) shows distinct activity profiles in these two cell types[40]. This differential response reflects underlying differences in basophil and mast cell receptor expression and signaling mechanisms, suggesting that MBP engages distinct surface molecules on the two cell types or that downstream signaling diverges following initial engagement.

The physiological significance of MBP-induced basophil and mast cell histamine release lies in its role in amplifying allergic inflammation through the bidirectional basophil/mast cell-eosinophil regulatory axis[11][37]. Eosinophil-derived MBP released during eosinophilic inflammation stimulates mast cells and basophils to release histamine, which itself promotes eosinophil recruitment through histamine H4 receptor activation, thereby establishing a positive feedback loop that amplifies allergic responses[8]. This mechanism represents a critical pathogenic pathway in allergic diseases and may explain the often-dramatic worsening of allergic symptoms in conditions characterized by eosinophilic inflammation.

## Activation of Neutrophils and Integration into Innate Immune Signaling

PRG2/MBP functions as a potent stimulus for neutrophil activation, triggering multiple effector functions including superoxide production, degranulation, and interleukin-8 (IL-8) production[19][20]. The molecular mechanism of neutrophil activation by MBP involves a Src kinase-dependent pathway that activates class IA phosphoinositide 3-kinase (PI3K) through tyrosine phosphorylation of the p85 regulatory subunit, leading to recruitment to the neutrophil plasma membrane[19]. PI3K activation generates phosphatidylinositol 3,4,5-trisphosphate (PIP3) at the membrane, which recruits proteins containing pleckstrin homology domains including Akt and the atypical protein kinase C zeta (PKCζ). Akt phosphorylation at both Ser473 and Thr308 confirms that MBP stimulates full activation of this canonical survival kinase through a PI3K-dependent mechanism[19]. Notably, inhibition of PI3K activity blocks MBP-stimulated superoxide production but does not prevent degranulation or IL-8 production, indicating that these latter functions employ distinct signaling pathways not requiring PI3K.

PKCζ activation represents a critical downstream effector of MBP-stimulated superoxide production, as PKCζ phosphorylation at Thr410 occurs with kinetics paralleling PI3K p85 recruitment and Akt activation, and inhibition of PKCζ activity substantially reduces superoxide generation[19]. The phosphorylated PKCζ likely regulates the assembly or activation of the NADPH oxidase complex responsible for generating the respiratory burst in activated neutrophils. This signaling pathway represents a Src-PI3K-Akt-PKCζ cascade, providing a mechanistic explanation for how a cationic peptide engages surface molecules to trigger complex intracellular signaling events leading to coordinated activation of the antimicrobial oxidative burst.

## Protein-Protein Interactions and Regulation of Growth Factor Biology

A major functional role for PRG2 emerges from its interactions with pregnancy-associated plasma protein A (PAPPA), a metzincin superfamily metalloproteinase that mediates insulin-like growth factor (IGF) bioavailability through proteolytic cleavage of IGF-binding protein 4 (IGFBP-4)[3][12][24][35]. The proform of PRG2 (proMBP) forms specific covalent complexes with PAPPA through disulfide bonding involving multiple cysteine residues on both proteins, and these complexes serve as potent inhibitors of PAPPA proteolytic activity[3][12][24][35]. The formation of the PAPPA/proMBP complex involves a complex series of disulfide exchange reactions: the proMBP disulfide bond Cys51-Cys169 undergoes reduction and reformation as the first interchain disulfide (Cys169-Cys652 of PAPPA), followed by disruption of the proMBP disulfide Cys89-Cys128 to form a second interchain disulfide (Cys51-Cys381 of PAPPA)[35]. ProMBP then dimerizes through formation of interchain disulfides (Cys104-Cys104 and Cys107-Cys107) between two Cys104-Cys107 intrachain disulfides, creating a highly ordered complex architecture[35].

The PAPPA/proMBP complex does not bind to heparan sulfate proteoglycans on the cell surface, unlike uncomplexed PAPPA which localizes to the surface through interactions of its complement control protein modules 3 and 4 with heparan sulfate chains[35]. However, the surface-binding capacity can be regained following heparinase treatment of the complex, indicating that the proMBP GAG chain can compete with the PAPPA HSPG receptor for binding following disruption of the covalent complex[35]. The proMBP GAG does not mediate initial recognition of PAPPA; rather, recognition depends on protein-protein interactions involving specific regions of the MBP domain (Loop 2 and the loop between Strand 2 and Helix 2), with Cys169 positioned in the binding interface[35]. Complex formation causes conformational changes that reduce surface binding affinity, providing a mechanism for releasing PAPPA from the cell surface and regulating the spatial availability of IGF-bioavailable IGFBP-4 cleavage products.

This regulatory interaction holds significant physiological implications for placental development and fetal growth, as studies have demonstrated that increased circulating IGFBP-4 in early pregnancy correlates with development of fetal growth restriction, while increased PAPPA levels correlate with normal fetal growth[21][24]. The relative balance between PAPPA and proMBP activities thus influences IGF availability for placental and fetal growth promotion, suggesting that dysregulation of this interaction may contribute to adverse pregnancy outcomes[3][21][24]. The appearance of proMBP in pregnancy serum at high concentrations, complexed with PAPPA and other proteins including angiotensinogen and C3dg, indicates this system is mobilized during reproduction, though the precise maternal physiological benefits of this mobilization remain incompletely understood[1][35][41].

## Transcriptional Regulation and Developmental Gene Expression

The PRG2 gene is subject to precise transcriptional control during eosinophil differentiation through a complex combinatorial network of lineage-specific transcription factors. Studies employing nuclear extracts from eosinophil-committed cell lines and in vitro transcription assays have identified a synergistic activation mechanism involving GATA-1 and PU.1, two transcription factors essential for myeloid and eosinophil development[3][43][46]. The eosinophil-specific P2 promoter of the PRG2 gene contains consensus binding sites for GATA-1, C/EBP family proteins, and PU.1 that all contribute to transcriptional regulation[43][46]. GATA-1 alone produces basal transactivation of the MBP promoter, but low levels of PU.1 in combination with optimal GATA-1 levels generate synergistic transactivation substantially exceeding the additive effects of the individual factors[43][46].

This cooperative GATA-1/PU.1 interaction is critically regulated by the CCAAT enhancer binding protein epsilon (C/EBPε) family of proteins[3][43][46]. Certain isoforms of C/EBPε, particularly the C/EBPε(27) isoform, function as potent repressors of both GATA-1 activity and the GATA-1/PU.1 synergy, thereby establishing a tightly controlled program for MBP expression in developing eosinophils[3][43][46]. In vitro mutational analysis of the MBP-P2 promoter has demonstrated that both the GATA-1/PU.1 synergy and C/EBPε(27) repressor activity are mediated through protein-protein interactions occurring at the C/EBP and/or GATA-binding sites, rather than through direct DNA binding by PU.1 in these regions[43]. Co-immunoprecipitation studies using lysates from eosinophil myelocyte cell lines confirm that C/EBPε isoforms physically interact in vivo with both PU.1 and GATA-1, demonstrating that functional interactions among these factors occur in native eosinophil progenitors[43].

The broader context of eosinophil lineage commitment reveals that GATA-1 is absolutely required for eosinophil development, as mice bearing mutations in the Gata1 promoter that reduce Gata1 expression by approximately 75% lack eosinophils[46]. Furthermore, eosinophil potential is restricted to GATA-1-positive myeloid progenitors, and human hematopoietic progenitors receiving ectopic GATA-1 expression alone are sufficient to undergo eosinophil differentiation[46]. The eosinophil-lineage priming process involves complex interactions between GATA factors, C/EBP family members, and the GATA co-factor FOG-1 (Friend of GATA-1), with FOG-1 normally acting as a repressor of eosinophil potential[46]. PU.1 antagonizes GATA-1 expression in multipotent progenitors but appears less critical than previously believed for later stages of eosinophil commitment, as PU.1-deficient fetal liver cells retain expression of both eosinophil peroxidase and MBP[46].

IRF8 (interferon regulatory factor 8) provides early driving force for eosinophil fate commitment through direct transcriptional activation of Gata1, and IRF8-deficient mice show reductions in both eosinophil progenitors and Gata1 expression in these cells[46]. The precise temporal sequence of transcription factor expression and the specific protein-DNA and protein-protein interactions governing MBP gene transcription remain subjects of ongoing investigation, particularly through emerging techniques enabling analysis of chromatin accessibility and transcription factor occupancy during eosinophil development.

## Interaction with Respiratory Pathogens and Epithelial Cell Dysfunction

PRG2/MBP plays an important pathogenic role in allergic airway disease through its capacity to interact directly with viral pathogens and synergize with viral pathogen-associated molecular patterns to trigger epithelial cell damage. Studies examining respiratory syncytial virus (RSV) infection have demonstrated that MBP synergizes with viral pathogen signals to provoke airway epithelial cell death and release of pro-inflammatory cytokines[3][20][26]. The mechanism underlying this synergy likely involves simultaneous engagement of viral pattern recognition pathways and direct membrane disruption by MBP, resulting in amplified epithelial cell damage beyond that caused by either stimulus alone. This MBP-virus synergy contributes to the immunopathology of RSV bronchiolitis, where eosinophilic infiltration of airways correlates with more severe disease, and elevated MBP levels are detected in respiratory secretions of patients with acute viral bronchiolitis[3][20].

Beyond respiratory pathogens, MBP contributes to local tissue damage and epithelial barrier dysfunction in various conditions characterized by eosinophilic inflammation. In eosinophilic esophagitis, a disorder of increasing prevalence characterized by dense eosinophilic infiltration of the esophageal mucosa, MBP-containing granule products are directly implicated in epithelial cell exfoliation and damage[3][15][20][23]. Similar mechanisms operate in other eosinophil-associated inflammatory conditions including atopic dermatitis (where keratinocyte damage occurs through direct MBP effects), eosinophilic myositis (tissue-infiltrating eosinophil-derived MBP damages muscle fibers), atopic cataracts (lens epithelial cell damage from eosinophil products), and chronic rhinosinusitis (nasal epithelial damage and polyp formation)[3][20][23]. In respiratory epithelia particularly, MBP directly damages epithelial cells through multiple mechanisms including direct membrane disruption, interference with tight junction protein expression, and induction of epithelial cell apoptosis or necroptosis.

The epithelial barrier dysfunction occurring in allergic diseases involves MBP-mediated disruption of tight junction organization, reduced expression of critical tight junction proteins including zonula occludens-1 (ZO-1) and occludin, and physical separation of adjacent epithelial cells[23]. These structural changes increase epithelial permeability, facilitating increased penetration of allergens and pathogens across epithelial barriers, thereby amplifying allergic inflammation in a feedforward manner. MBP also induces histamine release from epithelial mast cells, further promoting barrier dysfunction through histamine-receptor signaling that modulates tight junction integrity.

## Heparan Sulfate Proteoglycan Binding and Signal Modulation

PRG2/MBP recognizes heparan sulfate proteoglycans (HSPGs) through discrete surface-exposed residues that appear to represent an evolutionarily conserved feature of the C-type lectin-like fold[7][30][56]. Unlike classical C-type lectins that employ a canonical carbohydrate-binding pocket requiring coordinated calcium, MBP binding to HSPGs occurs through a distinct structural mechanism involving aromatic amino acid residues positioned in the characteristic downward-pointing loop configuration of the CTL domain[56]. The functional significance of HSPG binding likely involves positioning MBP at cell surfaces where HSPGs are abundant, potentially enhancing local concentrations and enabling more efficient cell targeting. Moreover, HSPG binding may direct MBP toward specific cellular compartments or membrane microdomains containing target proteins or receptors involved in downstream signaling.

The strategic positioning of MBP through HSPG binding in inflammatory tissues suggests its role as an intercellular signal modulator in inflammatory settings[3][20]. Rather than operating solely as a diffusible toxin, membrane-bound MBP pools at HSPG-enriched sites on epithelial cells and infiltrating immune cells may trigger local signaling cascades through proximity effects and enhanced local concentration. This mechanism would allow eosinophils to establish localized zones of MBP-dependent cellular activation while minimizing systemic toxicity through compartmentalization.

## Amyloidogenic Aggregation and Toxicity Mechanisms

Recent structural studies employing X-ray free electron laser (XFEL) radiation on nanocrystalline MBP-1 within intact eosinophil granules have revealed that the storage and activation of MBP involves a remarkable transition from ordered crystalline states to amyloidogenic fibrillar assemblies[25][28][34]. The nanocrystalline cores lock MBP-1 in a non-toxic conformation through specific intermolecular interactions occurring along defined crystallographic axes, particularly the two-fold screw axis along the crystallographic c-axis[28][56]. The packing observed in natural granule cores differs substantially from crystals grown in vitro through re-crystallization from acid-solubilized protein, likely reflecting differences in the chemical microenvironment in vivo including pH, redox conditions, and ionic strength[28].

Upon granule acidification below pH 4.0 during eosinophil activation, the ordered crystalline lattice undergoes controlled disassembly, liberating monomeric MBP-1 that rapidly equilibrates to neutral pH upon secretion[28]. At neutral pH, the released MBP-1 undergoes amyloidogenic aggregation, generating toxic oligomeric and fibrillar assemblies that directly disrupt biological membranes through a two-step mechanism[28][31][34]. The initial step involves formation of ion-selective pores through insertion of oligomeric MBP-1 assemblies into target membranes, recapitulating channel formation detected in earlier electrophysiological studies[28][31]. The second step involves amyloid fibril elongation directly on the membrane surface, causing non-selective physical disruption through a detergent-like mechanism that fragments the lipid bilayer[28][31].

The aggregation-prone segments identified within the MBP-1 sequence, including the 26-30 steric zipper, likely facilitate amyloid formation and may be conserved across eosinophil cationic proteins including eosinophil cationic protein (ECP)[28]. The parallels between MBP amyloidogenic mechanisms and Alzheimer amyloid-beta toxicity suggest that amyloidogenic aggregation represents a conserved mechanism by which cationic antimicrobial peptides achieve biological activity, possibly reflecting evolutionary pressure to employ irreversible, hard-to-reverse mechanisms for antimicrobial defense. The functional evidence that intact MBP-1 nanocrystalline cores fail to elicit significant bacterial killing while cores treated at pH 3.0 rescue toxicity provides compelling evidence that the crystallization process fundamentally alters protein conformation and immunoreactivity in ways that prevent membrane disruption.

## Disease Associations and Potential Tumor Suppressor Functions

PRG2 gene alterations have been associated with several human diseases. The most direct associations include **dermatographia** (a condition characterized by exaggerated skin reactivity and histamine-mediated whealing responses) and **hypereosinophilic syndrome** (a disorder involving sustained overproduction of eosinophils with multi-organ involvement)[1][49]. These disease associations likely reflect dysregulation of normal PRG2 expression or function leading to excessive or inappropriate eosinophil accumulation and MBP release.

Emerging evidence suggests PRG2 may function as a tumor suppressor gene in certain hematologic malignancies, particularly in chronic myeloid leukemia (CML) cells resistant to imatinib tyrosine kinase inhibitor therapy[55]. Studies employing demethylation with 5-azacytidine found that forced PRG2 expression in imatinib-resistant K562 cells is associated with STAT3 inactivation, restoration of imatinib sensitivity, and enhanced apoptosis[55]. The methylation status of the PRG2 gene inversely correlates with expression levels and imatinib sensitivity, indicating that epigenetic silencing of PRG2 through DNA hypermethylation contributes to the resistant phenotype[55]. This tumor suppressor function likely involves PRG2-mediated inhibition of the JAK/STAT3 signaling pathway, as re-expression studies demonstrate STAT3 inactivation accompanying PRG2 upregulation[55]. The molecular basis for PRG2-mediated STAT3 suppression remains to be fully elucidated, though possibilities include direct protein-protein interactions, regulation of STAT3-inhibitory proteins such as SOCS-1 and SOCS-3, or indirect effects through alterations in cellular redox status affecting kinase and phosphatase activities.

## Alternative Splicing and Protein Diversity

The PRG2 gene generates multiple transcript variants through alternative splicing mechanisms that produce isoforms with potentially distinct functions[1][50]. Alternative splicing represents a major mechanism for expanding proteome complexity in eukaryotes, with individual protein-coding genes producing an average of 5.4 different mRNA species through various splicing patterns[50]. Seven basic types of alternative splicing have been characterized, including exon skipping, alternative 5' and 3' splice sites, mutually exclusive exons, intron retention, alternative promoters, and alternative polyadenylation[50]. The regulation of alternative splicing depends on the intrinsic strength of splice sites, the concentration and composition of splicing regulatory factors (including SR proteins and heterogeneous nuclear ribonucleoproteins), chromatin modifications, and RNA secondary structure elements[50].

The availability of multiple PRG2 isoforms suggests tissue-specific specialization, with different isoforms potentially exhibiting distinct subcellular localizations, stability, or functional properties[1]. The splicing pattern is likely regulated by eosinophil-specific factors that differ from those present in other cell types, contributing to the cell-type specificity of eosinophil protein expression. Understanding the functional significance of individual PRG2 splice variants represents an important frontier in eosinophil biology and may reveal novel therapeutic targets for modulating eosinophil-mediated inflammation.

## Conclusion

The PRG2 gene encodes a structurally and functionally sophisticated multi-domain protein that integrates antimicrobial, immunomodulatory, and growth-factor regulatory functions within a single 222-amino acid polypeptide. As the predominant constituent of eosinophil granule crystalline cores, PRG2/MBP represents an evolutionary solution to the challenge of storing an inherently toxic protein in a safe, inert state while maintaining rapid availability for immediate deployment upon immune challenge. The protein's extreme cationic charge density and C-type lectin-like structural fold enable broad-spectrum antimicrobial toxicity through non-specific membrane disruption mechanisms, while simultaneously allowing selective immunomodulatory engagement with basophils, mast cells, and neutrophils through more sophisticated signaling pathways. The subcellular compartmentalization of PRG2 in secretory granules, its protection through encapsulation in nanocrystalline cores, and its regulated mobilization through piecemeal degranulation mechanisms exemplify how the immune system achieves safety and specificity in employing inherently dangerous effector molecules. The emerging tumor suppressor functions and broader physiological roles of PRG2 in placental development through growth factor regulation suggest that this protein likely possesses additional uncharacterized biological activities. Future investigations employing structural biology, cellular biology, and tissue-specific knockout approaches should illuminate the complete repertoire of PRG2 functions and identify precise therapeutic opportunities for modulating eosinophil-mediated inflammation in allergic and other immune-mediated diseases.

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRG2
2. https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.984655/full
3. https://maayanlab.cloud/Harmonizome/gene/PRG2
4. https://www.uniprot.org/uniprotkb/P13727/entry
5. https://www.ncbi.nlm.nih.gov/gene/5553
6. https://febs.onlinelibrary.wiley.com/doi/10.1111/j.1432-1033.1987.tb11172.x
7. https://en.wikipedia.org/wiki/Major_basic_protein
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC1574117/
9. https://www.affbiotech.com/goods-5794-DF6992-PRG2_Antibody.html
10. https://pubmed.ncbi.nlm.nih.gov/6854212/
11. https://thebiogrid.org/interaction/303046/pappa-prg2.html
12. https://www.ncbi.nlm.nih.gov/books/NBK1943/
13. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=5553
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC5783317/
15. https://www.ncbi.nlm.nih.gov/books/NBK579916/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC3427618/
17. https://pubmed.ncbi.nlm.nih.gov/14500673/
18. https://pubmed.ncbi.nlm.nih.gov/22689691/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9030405/
20. https://pubmed.ncbi.nlm.nih.gov/10077652/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC11483036/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC7258638/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3322459/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC4904734/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC137037/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC3443794/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC11394122/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC6332049/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC3709793/
30. https://academic.oup.com/biolreprod/article/84/6/1077/2530375
31. https://pubmed.ncbi.nlm.nih.gov/36890022/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC2187055/
33. https://www.ncbi.nlm.nih.gov/gtr/genes/5553/
34. https://pubmed.ncbi.nlm.nih.gov/30507713/
35. https://pubmed.ncbi.nlm.nih.gov/6206154/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC11855017/
37. https://pubmed.ncbi.nlm.nih.gov/12202480/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC10885618/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC2911633/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC7388079/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC12531897/
42. https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2020.00231/full
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC8951537/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC8530902/
45. https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRG3
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC2613545/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC2581549/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC6103584/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC9595336/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC8355064/