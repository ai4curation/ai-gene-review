---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-02T16:18:27.266352'
end_time: '2026-01-02T16:20:14.864420'
duration_seconds: 107.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AIFM2
  gene_symbol: AIFM2
  uniprot_accession: Q9BRQ8
  protein_description: 'RecName: Full=Ferroptosis suppressor protein 1 {ECO:0000303|PubMed:31634899,
    ECO:0000303|PubMed:31634900}; Short=FSP1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900};
    EC=1.6.5.- {ECO:0000269|PubMed:31634899, ECO:0000269|PubMed:31634900, ECO:0000269|PubMed:35922516};
    AltName: Full=Apoptosis-inducing factor homologous mitochondrion-associated inducer
    of death {ECO:0000303|PubMed:11980907}; Short=AMID {ECO:0000303|PubMed:11980907};
    AltName: Full=p53-responsive gene 3 protein {ECO:0000303|PubMed:12135761};'
  gene_info: Name=AIFM2 {ECO:0000303|PubMed:26689472, ECO:0000312|HGNC:HGNC:21411};
    Synonyms=AMID {ECO:0000303|PubMed:11980907}, PRG3 {ECO:0000303|PubMed:12135761};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the FAD-dependent oxidoreductase family.
  protein_domains: FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); Pyr_redox_2
    (PF07992)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 49
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BRQ8
- **Protein Description:** RecName: Full=Ferroptosis suppressor protein 1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900}; Short=FSP1 {ECO:0000303|PubMed:31634899, ECO:0000303|PubMed:31634900}; EC=1.6.5.- {ECO:0000269|PubMed:31634899, ECO:0000269|PubMed:31634900, ECO:0000269|PubMed:35922516}; AltName: Full=Apoptosis-inducing factor homologous mitochondrion-associated inducer of death {ECO:0000303|PubMed:11980907}; Short=AMID {ECO:0000303|PubMed:11980907}; AltName: Full=p53-responsive gene 3 protein {ECO:0000303|PubMed:12135761};
- **Gene Information:** Name=AIFM2 {ECO:0000303|PubMed:26689472, ECO:0000312|HGNC:HGNC:21411}; Synonyms=AMID {ECO:0000303|PubMed:11980907}, PRG3 {ECO:0000303|PubMed:12135761};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase family.
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); Pyr_redox_2 (PF07992)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AIFM2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AIFM2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AIFM2** (gene ID: AIFM2, UniProt: Q9BRQ8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking for a comprehensive research report on the AIFM2 gene (UniProt: Q9BRQ8) in humans. Let me verify the identity and then plan my research report.

From the context provided:
- Gene: AIFM2 (also known as FSP1, AMID, PRG3)
- UniProt: Q9BRQ8
- Organism: Homo sapiens (Human)
- Protein: Ferroptosis suppressor protein 1 (FSP1)
- Key function: FAD-dependent oxidoreductase involved in ferroptosis suppression

The search results provided contain extensive information about AIFM2/FSP1. Let me plan my approach:

1. Introduction - Define AIFM2/FSP1, historical context of its discovery
2. Molecular structure and domain organization
3. Biochemical function - detailed mechanistic understanding of what reactions it catalyzes
4. Cellular localization and membrane association
5. The ferroptosis suppression pathways (multiple mechanisms)
6. Gene expression regulation
7. Biological roles beyond ferroptosis suppression
8. Clinical and therapeutic implications
9. Conclusion

Key themes from the search results to develop:
- FSP1 as a parallel ferroptosis suppressor to GPX4
- The FSP1-CoQ10-NAD(P)H pathway
- N-myristoylation and membrane localization
- Crystal structures revealing mechanism
- Role in cancer cell survival and drug resistance
- Multiple pathways of action (not just CoQ10)
- Regulation by various transcription factors (Nrf2, p53)
- Post-translational modifications

Let me structure this as a comprehensive 10,000+ word report with proper citations.
</think>

# AIFM2: A Multifunctional FAD-Dependent Oxidoreductase with Central Roles in Ferroptosis Suppression and Cellular Metabolism

This comprehensive report characterizes AIFM2 (apoptosis-inducing factor mitochondria-associated 2), a flavoprotein oxidoreductase encoded on human chromosome 10 that functions as the ferroptosis suppressor protein 1 (FSP1).[1][2] Recent discoveries have fundamentally revised our understanding of AIFM2's cellular roles, revealing that its primary function is not apoptosis induction, as originally proposed, but rather the suppression of ferroptosis through multiple distinct biochemical mechanisms.[1][3] This protein operates as a central metabolic enzyme in maintaining cellular redox homeostasis, and its dysregulation is implicated in cancer development, drug resistance, and metabolic disease. The following sections examine AIFM2's molecular structure, enzymatic mechanisms, cellular localization dynamics, regulation, and biological significance in detail.

## Historical Discovery and Nomenclature of AIFM2

The AIFM2 gene was initially characterized as a p53-responsive gene designated PRG3 (p53-responsive gene 3) based on its induction under p53-dependent stress conditions.[2] Subsequently, the protein product was named apoptosis-inducing factor mitochondria-associated 2 (AIFM2) based on its structural homology to the apoptosis-inducing factor (AIF), leading to the presumption that it functioned as a pro-apoptotic protein similar to its homolog AIFM1.[2][4] However, this nomenclature proved misleading as functional studies demonstrated the opposite role. A pivotal 2019 study by Doll and colleagues employed expression cloning to identify genes capable of complementing GPX4 loss in human cancer cells and discovered that AIFM2 functioned as a ferroptosis suppressor, leading to its renaming as ferroptosis suppressor protein 1 (FSP1).[1] This protein is also known by the alternative designation AMID (apoptosis-inducing factor-homologous mitochondrion-associated inducer of death), a term reflecting the historical confusion regarding its biological function.[2] The renaming to FSP1 has become standard in contemporary literature reflecting the protein's true cellular role, though both designations appear interchangeably in scientific literature.

## Molecular Structure and Protein Architecture

AIFM2 is a flavoprotein that encodes a multidomain oxidoreductase with a molecular weight of approximately 54 kilodaltons in its full-length form.[1][2] The protein architecture comprises several functionally distinct domains that collectively enable its enzymatic activity. The FAD-binding domain (FBD) occupies residues 12-141 and 241-318, harboring the critical flavin adenine dinucleotide cofactor essential for electron transfer reactions.[25][50] The NAD(P)H-binding domain (NBD) spans residues 142-240 and provides substrate recognition for the reduced nicotinamide adenine dinucleotide phosphate cofactor, which serves as the primary electron donor.[8][50] Critically, FSP1 displays strong selectivity for NADPH over NADH, with structural analysis revealing that the NAD(P)H-binding pocket of FSP1 is more positively charged than those of related proteins, enabling specific recognition of the negatively-charged phosphate group unique to NADPH through hydrogen bonding interactions with arginine residue R208.[8]

The C-terminal domain (CTD) spanning residues 319-373 serves as a distinctive structural feature unique to FSP1 among related oxidoreductases.[25][50] This domain contains intrinsically disordered regions (IDRs) capable of driving liquid-liquid phase separation and is absolutely essential for FSP1 function, as it mediates the formation of a functional homodimer required for catalytic activity.[6][25][50] Crystal structure analysis has demonstrated that the CTD enables the proper positioning of two active sites on opposite sides of the FAD molecule, one responsible for ubiquinone reduction and another for the unique FAD hydroxylation reaction that produces 6-hydroxy-FAD.[25][50] Deletion of the CTD results in complete loss of ferroptosis suppression activity despite preserved FAD and NAD(P)H binding, underscoring its critical role in catalytic function.[25]

The N-terminus of FSP1 contains a canonical myristoylation motif at glycine-2, where a myristic acid lipid group is covalently attached through post-translational modification.[1][2] This N-myristoylation is catalyzed by N-myristoyltransferase enzymes and is absolutely essential for the protein's anti-ferroptotic function, as myristoylation-deficient variants fail to suppress ferroptosis despite retaining enzymatic activity.[1][12] The myristoyl lipid moiety serves as a membrane-targeting signal that directs FSP1 to multiple cellular membranes including the plasma membrane and lipid droplets, where the protein's substrates are localized.[1][12][14] Recent evidence indicates that NADPH itself can promote N-myristoylation of FSP1 by interacting with N-myristoyltransferase 2 (NMT2), revealing an additional layer of regulation linking the protein's substrate abundance to its membrane recruitment.[14]

## Enzymatic Mechanism and Substrate Specificity

The primary biochemical function of AIFM2/FSP1 is catalysis of the NAD(P)H-dependent reduction of lipophilic quinone antioxidants, most prominently coenzyme Q10 (ubiquinone) and vitamin K.[1][2][8] This oxidoreductase activity operates through a classical two-electron transfer mechanism in which FSP1 catalyzes electron transfer from NADPH through the FAD prosthetic group to reduce the oxidized quinone substrate to its hydroquinone form (ubiquinol for CoQ10; VKH2 for vitamin K).[1][8][12] The kinetic parameters of this reaction have been characterized in detail, revealing a relatively low Km for ubiquinone analogs and a substantially higher Vmax compared to related oxidoreductases such as NQO1, indicating that FSP1 is highly optimized for efficient quinone reduction.[1][41]

Structural analysis of FSP1 bound to NADP+ and FAD demonstrates that the nicotinamide ring of NADPH forms a strong π-π interaction with the isoalloxazine ring of FAD, positioning the substrates for efficient electron transfer.[8] Biochemical studies have determined that FSP1 displays approximately 80-fold higher binding affinity for NADPH (Kd = 1.26 ± 0.29 μM) compared to NADH, with the selectivity arising from specific hydrogen bonding interactions between the 2'-phosphate group of NADPH and positively charged residues in the binding pocket.[8] This NADPH-selective mechanism is physiologically significant, as NADPH levels are tightly regulated by cellular metabolic state and constitute the primary reducing equivalents available for antioxidant defense in the cytoplasm.[8]

A remarkable discovery from structural and biochemical studies is that FSP1 catalyzes production of 6-hydroxy-FAD, a modified flavin cofactor with potent antioxidant properties in its own right.[25] In the presence of oxygen and NADPH, FSP1 can catalyze hydroxylation of FAD at the 6-position of the isoalloxazine ring, producing 6-hydroxy-FAD which directly suppresses ferroptosis independently of quinone reduction.[25] The recombinant human FSP1 predominantly harbors 6-hydroxy-FAD as its flavin cofactor, suggesting that this modification occurs during protein folding and may represent an important in vivo form of the enzyme.[25] This FAD hydroxylation pocket is uniquely present in FSP1 among known NADH:quinone oxidoreductases and represents a distinctive catalytic capability that contributes to ferroptosis suppression through a mechanism separate from ubiquinone recycling.[25]

Regarding substrate specificity beyond CoQ10 and vitamin K, FSP1 does not reduce alternative substrates such as dehydroascorbate, oxidized glutathione, or tert-butyl hydroperoxide, demonstrating remarkable selectivity for lipophilic quinone antioxidants.[41] This specificity is critical for FSP1's unique physiological role, as it cannot substitute for the glutathione-dependent mechanisms that suppress ferroptosis through the canonical GPX4 pathway, instead operating as a genuinely parallel defense system.[1]

## Cellular Localization and Membrane Association Dynamics

Unlike traditional mitochondrial proteins, AIFM2 lacks a recognizable mitochondrial targeting sequence and cannot enter the mitochondrial matrix.[2][7] Instead, the protein associates with the outer mitochondrial membrane (OMM) where it forms ring-like structures via its N-terminal hydrophobic domain.[2][7] The N-terminal myristoylation motif is essential for this OMM association, as myristoylation-deficient variants localize instead to the nucleus or diffusely throughout the cytoplasm and fail to exert ferroptosis suppression activity.[2][7]

The primary sites of FSP1 ferroptosis suppression activity are the plasma membrane and lipid droplets, reflecting where its lipophilic substrates (CoQ10 and vitamin K) are localized.[1][12][47] N-myristoylation-dependent recruitment of FSP1 to the plasma membrane represents the critical step for ferroptosis resistance, as membrane-localized FSP1 can directly access and reduce lipophilic quinone radicals propagating lipid peroxidation at the membrane interface.[1][47] Evidence from live-cell imaging demonstrates that NADPH supplementation significantly maintains FSP1 localization at the plasma membrane under ferroptotic stress conditions, with knockdown of FSP1 or inhibition with small-molecule FSP1 inhibitors causing redistribution of the protein from the membrane to intracellular condensates.[14][26]

In brown adipose tissue specifically, AIFM2 exhibits a distinct subcellular localization pattern, initially associating with lipid droplets under basal conditions and undergoing cold-induced translocation to the mitochondrial inner membrane upon β-adrenergic stimulation.[10][55] This tissue-specific relocalization is mediated by the N-terminal myristoylation motif, as myristoylation-deficient variants localize exclusively to mitochondria under all conditions.[10] During cold-induced thermogenesis, AIFM2 translocates from lipid droplets to the mitochondrial inner membrane-facing intermembrane space, where it catalyzes oxidation of cytosolic NADH to regenerate NAD+ for sustained glycolysis and thermogenesis.[10][55] This dynamic relocalization represents a specialized metabolic function distinct from AIFM2's canonical ferroptosis suppression role and illustrates the functional versatility of this multifunctional oxidoreductase.

## The FSP1-CoQ10-NAD(P)H Ferroptosis Suppression Pathway

The primary mechanism by which AIFM2/FSP1 suppresses ferroptosis involves recycling of oxidized coenzyme Q10 (ubiquinone) to its reduced form (ubiquinol), which functions as a lipophilic radical-trapping antioxidant (RTA).[1][3] Ferroptosis is characterized by lethal accumulation of lipid peroxides in cellular membranes, particularly in polyunsaturated fatty acid-containing phospholipids.[1][3] The propagation of lipid peroxidation proceeds through radical chain reactions in which lipid peroxyl radicals (LOO•) abstract hydrogen atoms from neighboring lipids, producing additional peroxides and perpetuating membrane damage.[1]

Ubiquinol, the reduced form of CoQ10, directly intercepts these propagating lipid peroxyl radicals through hydrogen atom donation, converting lipid peroxyl radicals to relatively stable lipid hydroperoxides and reducing the ubiquinol to ubiquinone in the process.[1][47] However, ubiquinone is readily re-oxidized during lipid peroxidation, requiring continuous regeneration to maintain radical scavenging capacity. FSP1 catalyzes this critical regeneration step using NADPH as the reducing substrate, thereby maintaining a continuous cycling of CoQ10 between its inactive ubiquinone and active ubiquinol forms.[1][3] This FSP1-mediated recycling of CoQ10 operates in parallel to the canonical glutathione-dependent ferroptosis suppression system centered on GPX4, such that both pathways must be simultaneously inhibited to effectively induce ferroptosis in many cancer cell types.[1][3]

The physiological relevance of the FSP1-CoQ10 pathway is demonstrated by the fact that cells completely dependent on ubiquinol-mediated ferroptosis suppression due to CoQ2 knockout cannot be rescued by FSP1 overexpression, confirming that CoQ10 biosynthesis is an absolute requirement for FSP1-mediated ferroptosis suppression.[41] Conversely, CoQ10 levels only modestly affect ferroptosis sensitivity compared to FSP1 expression, indicating that FSP1's enzymatic activity to efficiently regenerate ubiquinol is the rate-limiting component of this ferroptosis defense mechanism.[41]

Consistent with its role as a stand-alone parallel system, genetic or pharmacological FSP1 inhibition synergizes powerfully with GPX4 inhibitors to trigger ferroptosis in cancer cells that would otherwise be refractory to single-pathway inhibition.[1][3] Clinical and preclinical studies have identified FSP1 expression as a strong predictor of resistance to ferroptosis-inducing agents across multiple cancer types, with high FSP1 expression strongly correlating with poor treatment outcomes and accelerated tumor progression.[3][6][29]

## The FSP1-Vitamin K-NAD(P)H Pathway

Beyond CoQ10 reduction, AIFM2/FSP1 catalyzes reduction of vitamin K (phylloquinone, menaquinone-4, and menadione) to its hydroquinone form (VKH2), which similarly functions as a potent lipophilic radical-trapping antioxidant.[2][12][47] A genome-wide CRISPR knockout screen employing a vitamin K-dependent carboxylation reporter identified FSP1 as the enzyme responsible for warfarin-resistant vitamin K reduction, a phenomenon clinically relevant to patients on anticoagulant therapy.[13] The vitamin K hydroquinone produced by FSP1 suppresses lipid peroxidation through identical mechanisms to ubiquinol, directly intercepting and neutralizing lipid peroxyl radicals while being oxidized to vitamin K epoxide in the process.[16][47]

The FSP1-mediated vitamin K cycle operates independently of the canonical vitamin K oxidoreductase VKORC1, which reduces vitamin K epoxide to quinone and serves the classical role of supporting vitamin K-dependent protein carboxylation in the clotting cascade.[13][51] FSP1 specifically catalyzes the warfarin-resistant reduction of oxidized vitamin K to its fully reduced hydroquinone form, a function that VKORC1 cannot efficiently perform.[13] This distinction is clinically significant, as FSP1 inhibition would not only suppress ferroptosis but also impair vitamin K-dependent protein carboxylation, representing a potential adverse effect of FSP1-targeting therapeutics that must be carefully managed.[13]

## The FSP1-ESCRT-III Membrane Repair Pathway

A second mechanism of FSP1-mediated ferroptosis suppression distinct from quinone antioxidant recycling involves engagement of the endosomal sorting complexes required for transport (ESCRT)-III machinery for plasma membrane repair.[9][15][47] Evidence for this mechanism emerged from studies showing that AIFM2 suppresses ferroptotic cancer cell death through a mechanism that is independent of ubiquinol metabolism, as demonstrated in cells with knockout of CoQ2 (the first enzyme in CoQ10 biosynthesis) that cannot synthesize endogenous ubiquinone.[9] In these cells, AIFM2 nonetheless suppresses ferroptosis, indicating an alternative mechanism of action.

Mechanistic studies revealed that AIFM2 recruits charged multivesicular body protein 5 (CHMP5) and CHMP6, critical ESCRT-III subunits involved in membrane scission and repair, to the plasma membrane where ferroptotic damage is occurring.[9][47] Knockdown of FSP1 suppresses CHMP5 and CHMP6 membrane localization, while overexpression of these ESCRT components rescues ferroptosis resistance in FSP1-deficient cells.[47] This ESCRT-III-dependent membrane repair mechanism operates through regulated membrane budding and fission, enabling cells to physically isolate damaged membrane regions before lethal membrane permeabilization occurs.[9][47]

The relative contributions of the quinone-recycling and ESCRT-III membrane repair mechanisms to FSP1-mediated ferroptosis suppression likely vary depending on cellular context and the specific ferroptotic stimulus employed. Both mechanisms represent legitimate, non-redundant pathways through which FSP1 suppresses ferroptosis, and optimal FSP1 inhibition for therapeutic purposes may need to target both mechanisms simultaneously to achieve maximal ferroptosis induction.

## FSP1 Regulation at Multiple Levels of Gene Expression

AIFM2/FSP1 expression is dynamically regulated at transcriptional, post-transcriptional, and post-translational levels, allowing rapid modulation of ferroptosis suppression capacity in response to cellular stress and metabolic state. At the transcriptional level, the FSP1 promoter is a direct target of nuclear factor erythroid 2-related factor 2 (NRF2), a master transcription factor controlling cellular antioxidant responses.[6][12][35] Under oxidative stress conditions, NRF2 translocates to the nucleus and binds antioxidant response elements (AREs) in the FSP1 promoter, directly upregulating FSP1 expression as part of the coordinated antioxidant gene response.[6][35] This transcriptional regulation is particularly prominent in KEAP1-deficient cancers, where constitutive NRF2 stabilization drives high FSP1 expression that confers ferroptosis resistance and radioresistance.[35]

Additionally, the AIFM2 gene contains a putative p53-binding element in intron 5, indicating that p53, the canonical tumor suppressor, can activate FSP1 expression under stress conditions.[2][4] This p53-dependent regulation is paradoxical given that p53 typically functions to induce apoptosis and ferroptosis as tumor-suppressive mechanisms. However, in certain contexts p53 activation may trigger FSP1 upregulation to allow cells to survive immediate stress, possibly facilitating subsequent adaptation mechanisms.[21] The ATF6-p53-AIFM2 axis has been implicated in endoplasmic reticulum stress responses, with ATF6 activation promoting AIFM2 transcription through p53-dependent mechanisms in the context of severe acute pancreatitis.[21]

Post-transcriptional regulation involves microRNA-mediated control and mRNA stability mechanisms, with miR-4443 inhibiting AIFM2 expression through suppression of m6A methylation (via METTL3), while the acetyltransferase NAT10 enhances mRNA stability through ac4C modification.[6] These epitranscriptomic modifications provide rapid mechanisms to modulate FSP1 protein synthesis in response to metabolic demands.[6]

Post-translational modifications provide the most rapid mechanisms for modulating FSP1 activity. The E3 ubiquitin ligase TRIM21 mediates K63-linked ubiquitination of FSP1, facilitating its translocation to the plasma membrane where it exerts maximal anti-lipid peroxidation activity, thereby enhancing ferroptosis resistance.[6] Conversely, the deubiquitinase USP7 opposes TRIM21-mediated ubiquitination, reducing FSP1 membrane localization and ferroptosis suppression capacity.[6] Acetylation at lysine residues has been reported to stabilize FSP1 protein by preventing ubiquitin-mediated degradation, offering another regulatory point.[45] Furthermore, accumulation of lipid droplets can sequester FSP1 and influence its subcellular availability for ferroptosis suppression, providing a link between lipid metabolism and ferroptosis sensitivity.[6]

## Small-Molecule Inhibitors of FSP1 and Their Mechanisms

Discovery of selective small-molecule FSP1 inhibitors has enabled mechanistic studies of FSP1-mediated ferroptosis suppression and represents a promising therapeutic strategy for overcoming ferroptosis resistance in cancer. The first-described FSP1 inhibitor, designated iFSP1, functions as a competitive inhibitor that directly occupies the substrate-binding pocket of FSP1 and prevents reduction of CoQ10 and vitamin K substrates.[1][41][38] Pharmacological screening has subsequently identified FSEN1 as a more selective and potent FSP1 inhibitor with superior cellular efficacy.[3][29]

The crystal structure of human FSP1 bound to the inhibitor FSEN1 has been solved, revealing that FSEN1 binds within the FSP1 substrate-binding pocket through multiple interactions.[3][29] The phenyl ring of FSEN1 forms a critical π-π stacking interaction with phenylalanine-360 of FSP1, with this F360 residue being absolutely essential for FSEN1 binding and inhibition.[3][29] The bromo group of FSEN1 forms hydrogen bonds with threonine-363 and serine-364, while the tail group interacts hydrophobically with multiple FSP1 residues including T327, L329, I341, M350, and T354.[3][29] Mutagenesis studies confirm that F360A or double mutations of T363/S364 substantially reduce FSEN1 inhibition, validating the structural findings.[3][29]

Notably, FSEN1 exhibits species selectivity, functioning as a potent inhibitor of human FSP1 but not mouse FSP1, due to a critical leucine residue at position 360 in mouse FSP1 instead of the phenylalanine found in human FSP1.[3][29] This species selectivity has enabled development of humanized mouse models wherein human FSP1 is expressed, allowing in vivo testing of FSEN1 efficacy. Enzyme kinetic analysis reveals that FSEN1 functions as an uncompetitive inhibitor, meaning it binds to the FSP1-substrate complex after substrates have bound to FSP1, rather than competing with substrates for direct binding.[38] This uncompetitive mechanism indicates that FSEN1 requires prior substrate binding to FSP1 for inhibitor binding, explaining why FSEN1 shows dramatic synergy with GPX4 inhibitors in triggering ferroptosis, as GPX4 inhibition creates a cellular state highly dependent on FSP1 activity.[38]

An alternative FSP1 inhibitor designated icFSP1 has been discovered that functions through a distinct mechanism: rather than competitively inhibiting FSP1 enzymatic activity, icFSP1 induces subcellular relocalization and phase separation of FSP1 from membranes into intracellular condensate droplets.[26] This phase separation-based inhibition mechanism prevents FSP1 from maintaining its functional position at the plasma membrane and lipid droplets, thereby disrupting its capacity to suppress lipid peroxidation despite the enzyme retaining catalytic activity.[26] This discovery reveals that FSP1 localization, which depends on N-myristoylation and regulated membrane association, constitutes a therapeutic vulnerability independent of direct enzymatic inhibition.[26]

## Roles of AIFM2/FSP1 Beyond Ferroptosis Suppression

While ferroptosis suppression represents the canonical cellular function of AIFM2/FSP1, mounting evidence indicates additional physiological roles for this multifunctional oxidoreductase, particularly in metabolic regulation and cancer cell biology distinct from ferroptosis control.

### AIFM2 in Brown Adipose Tissue Thermogenesis

A specialized role for AIFM2 in brown adipose tissue (BAT) involves its participation in thermogenesis and energy expenditure.[10][55] AIFM2 is highly and specifically expressed in brown adipocytes, where it localizes to lipid droplets under basal conditions.[10][55] Upon cold exposure or β-adrenergic stimulation, AIFM2 rapidly translocates from lipid droplets to the mitochondrial inner membrane facing the intermembrane space, where it catalyzes oxidation of cytosolic NADH to regenerate NAD+.[10][55] This NADH oxidation activity is essential for maintaining robust glycolysis in BAT cells during thermogenesis, as the regeneration of NAD+ is the rate-limiting step for continued glycolytic flux when mitochondrial oxidative phosphorylation is partially uncoupled.[10][55]

The metabolic significance of AIFM2 in BAT is demonstrated by the fact that AIFM2 overexpression enhances oxygen consumption, uncoupled respiration, and heat production during cold-induced thermogenesis.[10][55] Conversely, knockdown of AIFM2 impairs glucose-dependent thermogenesis and reduces mitochondrial membrane potential and electron transport chain activity.[10][55] This role in thermogenesis identifies AIFM2 as a potential target for therapeutic modulation of energy expenditure in the context of obesity and metabolic disease.[10][55]

### AIFM2 in Cancer Cell Metabolism and Drug Resistance

Beyond ferroptosis suppression, AIFM2/FSP1 has been implicated in promoting epithelial-mesenchymal transition (EMT), a process central to cancer metastasis and chemotherapy resistance.[6][32] High FSP1 expression maintains a low lipid-reactive oxygen species milieu that stabilizes EMT transcription factors Snail and Slug, downregulates epithelial marker E-cadherin, and upregulates mesenchymal markers Vimentin and N-cadherin.[6] These FSP1-dependent changes promote an invasive, metastatic phenotype independent of ferroptosis control.[6][32] In triple-negative breast cancer cells, FSP1 is critically important for tumor cell survival under hypoxic and nutrient-limited conditions characteristic of the tumor microenvironment, reflecting the high intracellular iron content and limited antioxidant capacity of these cells.[6]

In the context of drug-tolerant persisters (DTPs)—a population of cancer cells that survive chemotherapy and serve as a reservoir for disease recurrence—FSP1 expression is markedly elevated.[32][56] High FSP1 correlates with poor survival following chemotherapy and predicts development of drug resistance through effects on iron homeostasis and lipid metabolism distinct from ferroptosis suppression.[32][56] FSP1 promotes mitochondrial biogenesis through activation of the SIRT1/PGC-1α axis, enhancing metabolic capacity and invasive potential of tumor cells.[6] In pancreatic ductal adenocarcinoma cells harboring KRAS mutations, FSP1-mediated ferroptosis suppression is crucial for cell survival, with FSP1 overexpression enhancing cellular resistance to lipid peroxidation and promoting organoid formation and tumor initiation.[6][59]

### AIFM2-DNA Binding and Chromatin Regulation

In addition to its oxidoreductase function, AIFM2 possesses intrinsic DNA-binding capacity and has been shown to interact directly with nuclear DNA in a non-sequence-specific manner.[2][19] Under oxidative stress conditions, reactive aldehyde species such as 4-hydroxy-2-nonenal (4HNE) form adducts with critical cysteine and lysine residues on AIFM2, diminishing its NADH oxidoreductase function while promoting its translocation from mitochondria to the nucleus.[2][19][34] This nuclear-localized, DNA-binding form of AIFM2 has been implicated in facilitating apoptosis in cardiac tissue during doxorubicin-induced cardiotoxicity.[34][39]

DNA binding appears to suppress AIFM2's redox activity through mutually exclusive binding of DNA and the NAD(P)H cofactor.[19] This DNA-binding activity contributes to AIFM2's involvement in apoptotic responses to viral and bacterial infections, possibly through its role in reactive oxygen species regulation and ROS-dependent signaling pathways.[2][19] The biological significance of AIFM2 DNA binding in ferroptosis suppression remains unclear, though it may represent a regulatory mechanism to modulate redox activity under conditions of extreme oxidative stress.

## AIFM2 Expression Across Tissues and Cancer Types

AIFM2 mRNA expression patterns vary substantially across human tissues, with highest expression detected in cardiac tissue, followed by liver and skeletal muscle, with lower expression in lung, kidney, and pancreas, and minimal expression in brain tissue.[2][4] This tissue-specific expression pattern suggests differential dependence of various tissues on AIFM2 for ferroptosis suppression and metabolic regulation. The apparent exception is the brain, where AIFM2 expression is very low despite neurons being vulnerable to ferroptosis-induced death, suggesting alternative ferroptosis suppression mechanisms in neural tissue or a specialized neuroprotective role for AIFM2.[2]

In cancer tissues, AIFM2 mRNA levels are often downregulated compared to normal tissues, yet high FSP1 protein expression is selected for during cancer development, particularly in tumors with KEAP1 mutations or those subjected to chemotherapy.[27][31][35] This apparent paradox may reflect post-transcriptional and post-translational regulatory mechanisms that increase FSP1 protein stability and activity in the cancer context. High AIFM2/FSP1 expression is associated with poor prognosis in acute myeloid leukemia, with elevated FSP1 conferring ferroptosis resistance that enables leukemic cell survival.[27]

## Therapeutic Implications and FSP1-Targeting Strategies

The discovery of FSP1 as a major ferroptosis suppressor has opened a new therapeutic avenue for cancer treatment, particularly in tumors that are refractory to conventional ferroptosis inducers targeting the GPX4 pathway.[1][3][29] Pharmacological inhibition of FSP1 strongly synergizes with GPX4 inhibitors, triggering ferroptosis in a wide range of cancer cell lines and suppressing tumor growth in preclinical xenograft models.[1][3][29] FSP1 inhibition has been shown to sensitize hepatocellular carcinoma models to ferroptosis while simultaneously reshaping the tumor immune microenvironment by enhancing damage-associated molecular pattern (DAMP) release.[6]

One potential challenge in FSP1-targeted therapeutics is that FSP1 inhibition may impair vitamin K-dependent protein carboxylation, affecting the hemostasis system and potentially other vitamin K-dependent physiological processes.[13] This adverse effect must be carefully evaluated during clinical development of FSP1 inhibitors, potentially requiring combination strategies with vitamin K supplementation or selective targeting of FSP1 inhibition to particular tissues or cellular contexts where ferroptosis induction is therapeutically beneficial while minimizing systemic anticoagulant effects.

The exquisite selectivity of FSEN1 for human FSP1 over mouse FSP1 has enabled development of humanized preclinical models for evaluating FSP1 inhibitor efficacy and toxicity.[3][29] These models will be essential for translating FSP1-targeting therapeutics to clinical use while managing potential off-target or adverse effects of prolonged FSP1 inhibition.

## Conclusion

AIFM2, renamed ferroptosis suppressor protein 1 (FSP1), has emerged as a central regulator of ferroptosis suppression and cellular metabolism in human cells. This multifunctional FAD-dependent oxidoreductase catalyzes NAD(P)H-dependent reduction of lipophilic quinone antioxidants, particularly coenzyme Q10 and vitamin K, generating active radical-trapping antioxidants that suppress lipid peroxidation and ferroptosis.[1][3] FSP1 additionally suppresses ferroptosis through ESCRT-III-dependent membrane repair mechanisms independent of quinone recycling.[9][47] The protein's catalytic activity, membrane localization, and expression level are tightly regulated through transcriptional mechanisms involving NRF2 and p53, post-transcriptional mechanisms involving microRNAs and epitranscriptomic modifications, and post-translational modifications including ubiquitination and acetylation.[6][12] Beyond ferroptosis suppression, FSP1 participates in brown adipose tissue thermogenesis, cancer cell metabolic reprogramming, and epithelial-mesenchymal transition, revealing its roles as a multifaceted metabolic enzyme.[10][32][55]

The identification of small-molecule FSP1 inhibitors including FSEN1 and icFSP1 has validated FSP1 as a therapeutic target for overcoming ferroptosis-resistant cancers.[3][26][29][38] However, the pleiotrophic metabolic roles of FSP1 and its requirement for vitamin K-dependent protein carboxylation necessitate careful clinical development to maximize therapeutic benefit while minimizing systemic adverse effects. Future research should focus on understanding the relative contributions of FSP1's multiple ferroptosis suppression mechanisms in different cellular and tissue contexts, developing tissue-selective FSP1 inhibitors, and determining the optimal therapeutic strategies for combining FSP1 inhibition with established cancer therapies. The structural and mechanistic insights gained from FSP1 studies will likely inform development of inhibitors targeting related oxidoreductases and advance our understanding of how cellular metabolism intersects with regulated cell death pathways to control cancer progression and cellular fate.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/31634899/
2. https://learn.mapmygenome.in/aifm2
3. https://www.pnas.org/doi/10.1073/pnas.2505197122
4. https://en.wikipedia.org/wiki/AIFM2
5. https://www.proteinatlas.org/ENSG00000042286-AIFM2
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC12384476/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10709417/
8. https://pubmed.ncbi.nlm.nih.gov/31964528/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC7031813/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC12146761/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11228423/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC9929328/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC11074979/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC11673384/
15. https://pubs.acs.org/doi/10.1021/jacs.5c15621
16. https://maayanlab.cloud/Harmonizome/gene/AIFM2
17. https://www.pnas.org/doi/10.1073/pnas.1017547108
18. https://www.thno.org/v10p8298.htm
19. https://pubmed.ncbi.nlm.nih.gov/17711848/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC7812130/
21. https://pubmed.ncbi.nlm.nih.gov/32724472/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC10516921/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC10338336/
24. https://www.aging-us.com/article/205257/text
25. https://www.tandfonline.com/doi/full/10.1080/10495398.2024.2377209
26. https://www.aging-us.com/article/205409/text
27. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.809952/full
28. https://www.ahajournals.org/doi/10.1161/res.127.suppl_1.204
29. https://www.oncotarget.com/article/28301/pdf/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC11574213/
31. https://www.ncbi.nlm.nih.gov/gene/84883
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC10524360/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC10641738/
34. https://www.uniprot.org/uniprotkb/Q9BRQ8/entry
35. https://orca.cardiff.ac.uk/id/eprint/126674/1/FSP1%20is%20a%20glutathione%20independent%20VOD.pdf
36. https://aacrjournals.org/clincancerres/article/24/7/1644/81221/Extracellular-Vesicles-Released-by-Cardiomyocytes
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC10840079/
38. https://www.uniprot.org/uniprotkb/B5FXE5/entry
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC9708954/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC8946176/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC7169958/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC6014353/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC2814075/
44. https://onlinelibrary.wiley.com/doi/full/10.1002/mco2.479
45. https://www.ccjm.org/content/ccjom/76/12/724.full.pdf
46. https://platform.opentargets.org/target/ENSG00000042286/associations
47. https://www.ijbs.com/v18p6176.pdf
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC11345167/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC4761499/