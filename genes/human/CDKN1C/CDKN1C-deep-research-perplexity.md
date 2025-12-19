---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:05:40.132726'
end_time: '2025-12-12T07:08:57.613648'
duration_seconds: 197.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CDKN1C
  gene_symbol: CDKN1C
  uniprot_accession: P49918
  protein_description: 'RecName: Full=Cyclin-dependent kinase inhibitor 1C; AltName:
    Full=Cyclin-dependent kinase inhibitor p57; AltName: Full=p57Kip2;'
  gene_info: Name=CDKN1C; Synonyms=KIP2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the CDI family. .
  protein_domains: CDI_dom. (IPR003175); CDI_dom_sf. (IPR044898); CDI (PF02234)
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
- **UniProt Accession:** P49918
- **Protein Description:** RecName: Full=Cyclin-dependent kinase inhibitor 1C; AltName: Full=Cyclin-dependent kinase inhibitor p57; AltName: Full=p57Kip2;
- **Gene Information:** Name=CDKN1C; Synonyms=KIP2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the CDI family. .
- **Key Domains:** CDI_dom. (IPR003175); CDI_dom_sf. (IPR044898); CDI (PF02234)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDKN1C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDKN1C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDKN1C** (gene ID: CDKN1C, UniProt: P49918) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me review the user's query and the search results to verify I'm researching the correct gene and provide a comprehensive research report.

**Verification of Gene Identity:**
- Gene Symbol: CDKN1C
- UniProt Accession: P49918
- Organism: Homo sapiens (Human)
- Full Description: Cyclin-dependent kinase inhibitor 1C (p57, Kip2)
- Gene synonyms: KIP2
- Protein Family: CDI (Cyclin-Dependent Kinase Inhibitor) family
- Key Domains: CDI_dom

**Verification against search results:**
Looking at the search results, I can confirm:
- [1] Wikipedia: "Cyclin-dependent kinase inhibitor 1C (p57, Kip2), also known as CDKN1C, is a protein which in humans is encoded by the CDKN1C imprinted gene."
- [2] NCBI: "CDKN1C cyclin dependent kinase inhibitor 1C [ (human)]"
- Multiple sources consistently refer to this as the human CDKN1C gene encoding p57Kip2

This matches perfectly with the UniProt information provided. I can proceed with the research.

**Key Information from Search Results:**

Primary Function:
- Cell cycle regulation (inhibits CDK complexes, particularly G1 cyclin/CDK complexes)
- Tumor suppressor
- Involved in cell differentiation
- Stress response regulation

Specific Functions:
- Binds to and inhibits G1 cyclin/CDK complexes [1][2][3]
- Arrests cell cycle in G1 phase [1]
- Tumor suppressor candidate [1]
- Leads to cancer cell dormancy [1]
- Regulates stress-activated pathways [29]
- Involved in cell differentiation during development [4][19][57]


- Promotes cancer cell dormancy through CDK inhibition

**Structural Architecture:**
The protein contains several functionally distinct regions: a CDK inhibitory domain at the N-terminus, a PAPA domain unique to p57 (distinguishing it from related inhibitors p21 and p27), a QT box enriched in glutamine and threonine residues, a nuclear localization signal, and a PCNA-binding domain at the C-terminus, along with proline-rich and acidic repeat regions. When active, the protein localizes to the nucleus where it exerts its CDK inhibitory effects.

**Subcellular Dynamics:**
The protein exhibits dynamic localization patterns—it shuttles between cytoplasm and nucleus depending on cellular state, remaining cytoplasmic during active proliferation but translocating to the nucleus during differentiation processes.

**Functional Roles:**
Beyond direct CDK/cyclin inhibition and Rb phosphorylation control, the protein regulates E2F transcription factors and participates in multiple signaling pathways including JNK/SAPK inhibition independent of CDK effects, MAPK signaling, and DNA damage responses. It maintains stem cell quiescence, promotes myogenic differentiation, and modulates apoptosis through both pro- and anti-apoptotic mechanisms depending on cellular context, with involvement in mitochondrial pathways.

**Developmental and Metabolic Functions:**
The protein plays roles in placental development and pancreatic beta cell regulation.

**Genomic Features:**
Positioned on chromosome 11p15.5, this imprinted gene is expressed exclusively from the maternal allele and contains four exons separated by three introns, with its imprinting control region (KvDMR1) embedded within its structure.

**Disease Associations:**
Loss-of-function mutations cause Beckwith-Wiedemann Syndrome and IMAGe syndrome, while mutations appear in sporadic cancers. The gene is silenced in 30-55% of acute hematologic malignancies and its dysfunction associates with childhood tumor development.
</think>

# Cyclin-Dependent Kinase Inhibitor 1C (CDKN1C): A Comprehensive Functional and Molecular Analysis

CDKN1C, encoding the p57Kip2 protein, is a critical cell cycle regulator and tumor suppressor gene located on chromosome 11p15.5 that functions primarily through the inhibition of cyclin-dependent kinase complexes to control cellular proliferation, differentiation, and stress responses. This extensively studied protein belongs to the CIP/Kip family of CDK inhibitors and plays essential roles across multiple biological contexts including embryonic development, tissue differentiation, stem cell maintenance, and cancer prevention, with mutations in CDKN1C associated with overgrowth disorders and increased pediatric tumor formation. The gene is uniquely subject to genomic imprinting, expressed exclusively from the maternal allele, and its cellular function is tightly regulated through multiple mechanisms including epigenetic control, subcellular localization, protein degradation pathways, and dynamic interactions with transcriptional and signaling machinery, making it a paradigmatic example of multifunctional tumor suppressor proteins that operate through both canonical cell cycle mechanisms and context-dependent signaling pathways.

## Molecular Identity and Structural Organization

### Gene and Protein Architecture

The CDKN1C gene, located at human chromosome 11p15.5, encodes a 316-amino acid protein known as p57Kip2 (cyclin-dependent kinase inhibitor p57, Kip2), representing the third member of the CIP/Kip family of CDK inhibitors alongside p21Cip1/WAF1 and p27Kip1[1][14]. The gene spans multiple exons with alternative splicing generating three mature mRNA variants that share identical open reading frames but differ in their untranslated regions[43]. The protein exhibits a complex modular architecture comprising several structurally and functionally distinct domains that confer its multiple biological activities.

The most critical functional domain is the N-terminal cyclin-dependent kinase inhibitory domain (KID), which is conserved across all CIP/Kip family members[14][43]. This KID domain contains three short motifs essential for CDK inhibition: a cyclin-binding domain that recognizes cyclin partner proteins, a CDK-binding site that directly interfaces with kinase catalytic machinery, and a distinctive 3₁₀ helix characterized by a specific pair of amino acids (phenylalanine-tyrosine) that functionally mimics the adenine component of ATP[43]. This molecular mimicry allows p57Kip2 to insert into the ATP-binding pocket of CDK enzymes, thereby blocking substrate access and preventing catalytic activity. Through this conserved N-terminal domain, p57Kip2 inhibits the kinase activity of multiple cyclin/CDK complexes in vitro, including cyclin E/CDK2, cyclin A/CDK2, and cyclin D1,2/CDK4 complexes[43].

Distinguishing p57Kip2 from other CIP/Kip members is the presence of a unique proline-alanine rich domain termed the PAPA region, positioned between the N-terminal and C-terminal regions of the protein[14][43]. This PAPA domain is peculiar to human p57Kip2, being largely absent or substantially divergent in mouse and rat homologs where a proline-rich region followed by acidic repeats serves a potentially analogous function[14]. The PAPA region creates a striking discrepancy between the sequence-derived molecular weight of approximately 29 kDa and the apparent molecular weight on sodium dodecyl sulfate-polyacrylamide gel electrophoresis of approximately 38-40 kDa, indicating structural features that alter protein migration patterns[44]. While the precise functional significance of the PAPA domain remains incompletely understood, evidence suggests it may confer distinct functional capabilities and protein interactions that differentiate p57Kip2 from p21 and p27[14].

The carboxy-terminal region of p57Kip2 contains a QT box domain rich in glutamine and threonine residues that shows homology to the corresponding QT domain in p27Kip1 and mediates interactions with regulatory proteins beyond simple CDK inhibition[14][43]. Within this QT box region, a consensus sequence for a putative nuclear localization signal (NLS) has been identified[14][43]. Further towards the C-terminus, p57Kip2 presents a domain homologous to that found in p21Cip1/WAF1 that permits binding to proliferating cell nuclear antigen (PCNA), a cofactor of DNA polymerase delta[14][43]. This PCNA-binding capability allows p57Kip2 to inhibit PCNA, although with substantially lower affinity than p21Cip1/WAF1, suggesting a secondary regulatory role in DNA replication processes.

Recent structural studies have identified that p57Kip2 contains a classical bipartite nuclear localization sequence characterized by two clusters of positively charged amino acids (lysine and arginine residues) separated by a proline-rich linker region[44]. The first NLS cluster spans approximately amino acid positions 278-281, while a second NLS sequence is located at the C-terminal region spanning residues 312-316, with the RKRLR sequence at the C-terminus (residues 312-316) being absolutely required for nuclear entry[44][45]. Indeed, the removal of the C-terminal RKRLR sequence by tryptophan substitution at R316 or truncation results in cytosolic accumulation of the protein, demonstrating the critical importance of this sequence for nuclear localization signals[45].

### Genomic Imprinting and Epigenetic Regulation

CDKN1C occupies a unique genomic position as an imprinted gene subject to parent-of-origin-dependent expression[1][4][34]. The gene is expressed exclusively from the maternal allele, while the paternal allele remains transcriptionally silent through a process of genomic imprinting coordinated by epigenetic mechanisms[1][4][43]. This imprinting is established through actions of the imprinting control region KvDMR1 (also designated KCNQ1OT1:TSS-DMR), which acquires DNA methylation in the maternal germline during female gametogenesis[43]. The KvDMR1 region, which spans the promoter of the paternally expressed long non-coding RNA KCNQ1OT1 (also called Kcnq1ot1), acts as a transcriptional regulator that maintains continuous domain-wide imprinting at the 11p15.5 locus[34][43].

This imprinting mechanism has profound developmental consequences. During early development, failure of proper methylation of CDKN1C or acquisition of mutations in this imprinted gene results in loss of cell cycle suppression and consequent pediatric tumor growth, as the paternal allele cannot compensate for loss of the maternal allele[1]. Complete hydatidiform moles, which consist exclusively of paternal DNA, provide a clinical example of this principle—cells in these lesions lack p57 expression because the gene is paternally imprinted (silenced), and immunohistochemical stains for p57 have proven diagnostically useful in distinguishing complete hydatidiform moles from other pregnancy-related pathologies[1].

The CDKN1C promoter and gene body are subject to direct methylation on the paternal allele post-fertilization after allelic silencing has been established[43]. Additionally, the CDKN1C promoter is strongly regulated by methylation at numerous CpG islands located upstream and downstream of the transcription start site, playing a critical role in mediating p57 silencing in cancers[19]. This epigenetic silencing through DNA methylation represents a frequent mechanism of CDKN1C inactivation in human malignancies, suggesting that pharmacological approaches targeting DNA methylation patterns could potentially reactivate p57 expression and restore tumor suppressive functions in cancer cells.

## Primary Biochemical Function: Cyclin-Dependent Kinase Inhibition

### Molecular Mechanism of CDK Inhibition

The primary and most thoroughly characterized biochemical function of CDKN1C-encoded p57Kip2 is that of a tight-binding, strong inhibitor of cyclin/cyclin-dependent kinase complexes, particularly those involved in G1 phase progression[1][2][11]. The inhibitory mechanism operates through direct protein-protein interactions between the N-terminal KID domain of p57Kip2 and the active site architecture of CDK enzymes. The CDK inhibitory domain binds to CDK catalytic subunits through a multi-step interaction process where the domain first engages the cyclin-binding surface, then inserts a small helix into the ATP-binding cleft of the kinase[8].

This insertion into the ATP-binding pocket serves a critical function: it partially triggers conformational rotation of the CDK, causing the cyclin to release the T loop (an inhibitory element in the kinase structure) and detach from the CDK[8]. The CDK inhibitor then initiates the small helix insertion into the active site cleft, blocking it and preventing ATP access to the active site. Subsequently, the inhibitor releases existing ATP from the aperture of the CDK, thereby deactivating the kinase through two complementary mechanisms: direct steric blockade of the active site and depletion of the ATP cofactor required for catalysis[8].

Importantly, p57Kip2 exhibits specificity in its inhibitory profile. The protein functions as a strong inhibitor of CDK2 complexes with cyclin E (cyclin E/CDK2), cyclin A (cyclin A/CDK2), and CDK4 complexes with D-type cyclins (cyclin D1/CDK4, cyclin D2/CDK4)[28][51]. This inhibitory spectrum contrasts with the INK4 family of CDK inhibitors (p16INK4A, p15INK4B, p18INK4C, p19INK4D), which preferentially inhibit CDK4 and CDK6, whereas the KIP/CIP inhibitors including p57Kip2 inhibit activity of CDK2-containing complexes and can serve as assembly factors for cyclin D-CDK4/6 complexes[28]. This dual character—as both an inhibitor of certain complexes and an assembly factor for others—adds considerable complexity to understanding p57Kip2 function in cell cycle regulation.

The binding of p57Kip2 to cyclin/CDK complexes results in formation of inactive trimeric complexes composed of cyclin, CDK, and the inhibitor protein[25]. Studies employing fluorescence recovery after photobleaching (FRAP) have demonstrated that the presence of p57Kip2 or related CIP/KIP proteins results in dramatic stabilization of cyclin binding to the cognate CDK for all trimeric complexes examined, with no recovery of cyclins observed during 15-minute time courses[25]. This stabilization reflects dramatically increased binding affinity between cyclin and CDK in the presence of p57Kip2, suggesting that the inhibitor protein not only blocks catalytic activity but fundamentally alters the biophysical properties of the complex.

### Cell Cycle Arrest and G1 Phase Regulation

The fundamental biological consequence of p57Kip2-mediated CDK inhibition is arrest of the cell cycle in the G1 phase, preventing progression from G1 into S phase[1][8]. Expression of p57Kip2 leads to accumulation of cells in G1 phase, as demonstrated by inducible expression systems in multiple cell types including astrocytoma cells[3]. Within three days after induction of p57Kip2 in astrocytoma cell lines (U343C9, U87C2, U373C3), cells were rapidly growth arrested and accumulated in G1 phase[3]. This accumulation reflects the role of cyclin E/CDK2 complexes in phosphorylating retinoblastoma (Rb) protein and related pocket proteins, with p57Kip2 inhibition of cyclin E/CDK2 preventing this critical phosphorylation event.

The p57Kip2-induced proliferative block is accompanied by substantial alterations in the expression and phosphorylation status of downstream cell cycle regulatory factors[3]. Upon p57Kip2 induction, expression levels of the retinoblastoma protein and p107 (an Rb family member) are sharply reduced by three days after p57Kip2 induction, whereas p130 expression remains unchanged[3]. Notably, the Rb protein is shifted to a faster-migrating, hypophosphorylated form characteristic of the inactive, growth-suppressive state[3]. Simultaneously, E2F transcription factor family members are downregulated—specifically E2F-1 expression is repressed while E2F-4 levels remain unchanged[3]. These coordinated changes in cell cycle regulatory proteins constitute a coherent molecular program ensuring stable cell cycle arrest rather than transient growth inhibition.

## Cellular Localization and Regulation of Subcellular Trafficking

### Dynamic Subcellular Localization During Cell Cycle and Differentiation

A critical discovery in understanding p57Kip2 function has been the demonstration that its biological activity is extensively regulated by dynamic subcellular localization, with the protein shifting between cytoplasmic and nuclear compartments depending on cellular state and developmental context[7][20]. This regulated trafficking represents an elegant mechanism through which cells can maintain p57Kip2 protein expression while temporally controlling its CDK-inhibitory function, allowing cells to remain proliferative when needed despite p57Kip2 protein presence.

During muscle satellite cell (MuSC) activation and early proliferation phases, p57Kip2 is predominantly restricted to the cytoplasm despite being expressed at substantial levels[7][20]. This cytoplasmic localization is compatible with cell proliferation and does not trigger growth arrest[7][20][36]. Specifically, when myoblasts are cultured in proliferating conditions, p57Kip2 remains predominantly cytoplasmic at 72 hours of culture, at which point most cells are PAX7+ (satellite cell marker expressing MYOD+, indicating early differentiation)[20]. As differentiation proceeds and myoblasts express progressively higher levels of MYOGENIN (a late myogenic marker), p57Kip2 demonstrates increasingly strong nuclear localization[7][20]. Around 25% of MYOD+ differentiation-stage myoblasts show nuclear p57Kip2, whereas approximately 55% of MYOGENIN+ late-differentiation myoblasts display nuclear localization of the protein[7][20].

Experimental manipulation of p57Kip2 subcellular localization directly confirms that this localization is functionally determinative. Overexpression of full-length p57Kip2 in myofiber cultures results in strong nuclear localization of the protein and a marked decrease in cycling myoblasts[7][20]. In striking contrast, forced expression of a p57Kip2 construct lacking the nuclear localization signal (Cdkn1c-NLS) results in restriction of the protein to the cytoplasm and fails to induce cell cycle exit despite protein expression at similar or higher levels than the full-length construct[7][20]. These experiments definitively establish that nuclear translocation is an obligatory requirement for p57Kip2 growth-arrest activity and that cytoplasmic sequestration represents a mechanism through which cells maintain p57Kip2 protein expression while permitting continued proliferation[7][20][36].

This principle generalizes across multiple developmental contexts. In the developing muscle tissue, p57Kip2 is not expressed in quiescent muscle satellite cells but is induced upon activation and maintained in differentiating myogenic cells[7][20][36]. Similarly, in neural stem cells (NSCs), p57Kip2 is abundantly expressed in quiescent NSCs but its expression decreases when NSCs become committed and proliferative[14][24]. The common principle appears to be that p57Kip2 expression marks cells committed to exit from the cell cycle and enter terminal differentiation, with subcellular trafficking to the nucleus representing the final regulatory step that commits these cells to growth arrest and differentiation programs.

### Mechanisms of Subcellular Trafficking

The nuclear localization of p57Kip2 depends critically on the bipartite nuclear localization signals identified in the C-terminal domain, particularly the RKRLR sequence at residues 312-316[44][45]. These signals are recognized by classical nuclear import machinery involving importin-α/β heterodimer transport receptors that mediate active transport through nuclear pore complexes. Experimental deletion or mutation of the C-terminal NLS region results in cytoplasmic accumulation and loss of nuclear function, confirming the necessity of this sequence for efficient nuclear entry[45].

The mechanisms regulating dynamic trafficking between cytoplasm and nucleus remain incompletely characterized but likely involve regulated recognition of NLS sequences by nuclear transport machinery in response to cellular signaling and differentiation cues. During myogenesis, progressive nuclear translocation correlates with myogenic transcription factor expression and likely involves signaling cascades that activate nuclear import mechanisms. The fact that p57Kip2 initially localizes to the cytoplasm upon myoblast activation despite containing functional NLS sequences suggests that active nuclear export or sequestration mechanisms may operate during proliferation phases, with these mechanisms being relieved during differentiation.

## Tissue-Specific Expression Patterns and Developmental Regulation

### Embryonic Expression and Developmental Roles

Unlike other CIP/Kip family members p21 and p27, p57Kip2 exhibits a highly tissue-specific expression pattern with marked variations across embryonic and postnatal development[19]. During embryogenesis, p57Kip2 is strongly expressed from embryonic day 9.5 to birth, with peak expression occurring at critical stages of differentiation in each developing organ[19]. The protein is present in all three embryonic germ layers (endoderm, mesoderm, and ectoderm) and is found in the majority of developing organs including cartilage, skeletal muscle, heart, nervous system, and parenchymal organs such as intestine, pancreas, lungs, adrenals, thymus, gonads, and kidney[19]. Additionally, high p57Kip2 expression occurs in extra-embryonic tissues, consistent with roles in trophoblast differentiation and placental development[19][40].

After embryonic day 13.5, p57Kip2 expression strongly decreases in most tissues but persists selectively in specific locations including skeletal muscle, kidney, intestine, palate, and lens[19][22]. This selective persistence of expression in specific tissues at later developmental stages suggests tissue-specific roles in differentiation and tissue-specific stem cell maintenance. During embryonic development, p57Kip2 expression is especially high in embryonic tissues entering mitotic arrest or differentiating, reflecting its fundamental role as a critical terminal effector of signal transduction pathways controlling cell cycle exit and differentiation.

### Skeletal Muscle and Myogenic Differentiation

The role of p57Kip2 in skeletal muscle development and adult myogenesis represents one of the best-characterized tissue-specific functions of this protein. During development, genetic studies using conditional knockout mice have demonstrated that p57Kip2 is absolutely required for correct cell cycle regulation and differentiation during postnatal myogenesis[7][20][36]. In the absence of p57Kip2, skeletal muscle repair after injury is severely impaired, with mutant animals displaying impaired muscle regeneration and reduced differentiation of myogenic cells[7][20][36].

Mechanistically, p57Kip2 drives muscle differentiation through a positive feedback loop involving myogenic regulatory factors (MRFs), particularly MYOD[23]. In developing muscle, MRF activation and cell cycle exit are two key, interdependent steps in terminal myoblast differentiation[23]. MyoD can drive cell cycle exit through multiple pathways, one of which involves activation of the cyclin-dependent kinase inhibitor p21Cip1[23]. Additionally, studies in zebrafish development have demonstrated that p57Kip2 promotes MyoD accumulation in adaxial cells and stabilizes MyoD protein through inhibition of CDK2 activity, and may enhance MyoD DNA binding through direct protein-protein interaction[23]. This MyoD-mediated stabilization of p57Kip2 expression creates a positive feedback loop whereby MRF activity induces p57Kip2 expression, which then enhances MRF protein activity and stability, thereby driving terminal differentiation[23].

Furthermore, knockdown of p57Kip2 in developmental contexts where MRF activity is altered shows that p57Kip2 activity is sufficient to rescue myogenesis even in the absence of critical developmental signals. Specifically, in zebrafish development, p57Kip2 activity appears capable of rescue adaxial myogenesis in the absence of hedgehog (Hh) signaling, presumably by promoting MRF activity[23]. This demonstrates that p57Kip2 represents a downstream convergence point through which multiple developmental signals ultimately coordinate cell cycle exit and myogenic differentiation.

### Placental Development and Trophoblast Function

In the placenta, p57Kip2 plays multiple specialized roles related to trophoblast function and placental development[40]. The protein is involved in endoreduplication (DNA replication without mitotic cell division) that is essential for trophoblast giant cell formation and differentiation[40]. Placental trophoblast cells undergo endoreduplication as part of their normal developmental program, particularly in the formation of trophoblast giant cells that invade the maternal endometrium[40]. p57Kip2 participates in endoreduplication through cell cycle arrest mechanisms that allow trophoblasts to replicate their DNA without completing mitosis, thereby achieving polyploidy. Additionally, p57Kip2 regulates trophoblast invasion and expansion of placental cell layers, demonstrating that the protein functions as both a cell cycle regulator and a modulator of cell migration and invasive capacity in this developmental context[40].

The expression of p57Kip2 levels oscillate during endoreplication, with the protein decreasing before S phase entry and accumulating after S phase completion and during G1[19]. This oscillatory pattern reflects the dynamic nature of p57Kip2 function in coordinating the unusual cell cycle program of endoreplication, where cells must execute DNA synthesis while suppressing mitotic entry. Recent CRISPR screening in human trophoblast stem cells (hTSCs) has identified CDKN1C as one of eight growth-restricting genes required for normal placental development[37]. This finding confirms the critical importance of p57Kip2 in placental development and trophoblast cell cycle regulation.

### Hematopoietic Stem Cell and Neural Stem Cell Maintenance

p57Kip2 plays critical roles in maintaining quiescence and regulating function of adult stem cell populations, particularly hematopoietic stem cells (HSCs) and neural stem cells (NSCs)[14][24][33]. High p57Kip2 mRNA and protein expression are reported in the HSC side population, especially in c-kit+/Sca-1+/Lineage+ side population cells[14][24]. In these cells, p57Kip2 has been designated as responsible for cell cycle blockage, and its downregulation is required for S phase entry and HSC activation[14][24].

In NSCs, p57Kip2 is abundantly expressed and its expression decreases when these cells become committed and proliferative[14][24]. Conditional deletion of p57Kip2 in NSCs results initially in transient recruitment of NSCs into the cell cycle, thus activating neurogenesis in both young and aged mouse brains, but later leads to excessive depletion of the quiescent NSC population and impairment of hippocampal neurogenesis[14][24]. This biphasic effect reflects the complexity of p57Kip2 function in stem cells: while acute loss of p57Kip2 activates otherwise quiescent NSCs to enter neurogenic programs, chronic loss depletes the NSC pool through exhaustion, as the NSCs lack a crucial brake on proliferation.

The role of p57Kip2 in maintaining HSC quiescence and stress response provides insights into how this protein functions as a rheostat for tissue regeneration. In studies using conditional p57Kip2-deficient mice, it was found that p57-null HSCs are qualitatively superior to wild-type HSCs in serial transplantation assays, a standard measure of HSC self-renewal capacity[33]. However, mice with p57-null hematopoiesis are less sensitive to myelotoxic stress induced by chemotherapeutics (5-fluorouracil and cytarabine) and recover more briskly following such treatment[33]. This indicates that p57Kip2 normally serves a critical function in restraining HSC self-renewal during periods of hematopoietic stress, with loss of p57Kip2 providing a competitive advantage during regenerative demands but potentially compromising long-term HSC maintenance under steady-state conditions.

## Clinical Associations and Disease Pathology

### Beckwith-Wiedemann Syndrome and Overgrowth Disorders

Beckwith-Wiedemann syndrome (BWS) represents the most clinically significant disease associated with CDKN1C mutations, being characterized as an imprinting disorder that associates macroglossia (enlarged tongue), abdominal wall defects, visceromegaly (enlarged internal organs), and a high risk of childhood tumor formation[1][9][49][52]. Molecular anomalies underlying BWS are mostly epigenetic; however, mutations of CDKN1C are implicated in approximately 8% of BWS cases, including both sporadic and familial forms[9][49].

Comprehensive analysis of CDKN1C mutations in BWS patients has identified 37 distinct mutations across 38 different pedigrees affecting 50 patients and seven fetuses[9][49]. Analysis of parental samples when available showed that all mutations tested but one were inherited from the mother, consistent with the maternal-only expression of CDKN1C[9][49]. The phenotypic presentation of CDKN1C-associated BWS shows interesting genotype-phenotype correlations: the four missense mutations identified led to a less severe phenotype with lower frequency of exomphalos (abdominal wall defect) than the other 33 mutations[9][49]. This suggests that subtle reductions in p57Kip2 function (from missense mutations potentially retaining partial activity) produce less severe phenotypes than complete loss-of-function mutations resulting from nonsense, frameshift, or splice site alterations[9][49].

The cancer predisposition in CDKN1C-associated BWS is substantial. Among the BWS patients with CDKN1C mutations identified in one comprehensive study, four tumors occurred: one neuroblastoma, one ganglioneuroblastoma, one melanoma, and one acute lymphoid leukemia[9][49]. This diversity of tumor types reflects the broad tumor suppressive role of p57Kip2 across multiple tissue lineages. Loss-of-function mutations in CDKN1C are also associated with IMAGe syndrome (Intrauterine growth restriction, Metaphyseal dysplasia, Adrenal hypoplasia congenita, and Genital anomalies), indicating that p57Kip2 functions extend beyond simple overgrowth regulation to encompass multiple aspects of developmental and endocrine function[1].

Notably, CDKN1C sequencing should be performed for BWS patients presenting with specific features including abdominal wall defects, cleft palate, features occurring without 11p15 methylation defects or body asymmetry, or in familial cases of BWS where multiple family members are affected[9][49]. This clinical recommendation reflects the molecular heterogeneity of BWS, where different molecular mechanisms (epigenetic alterations versus genetic mutations) are associated with different clinical presentations and inheritance patterns.

### Cancer Associations and Silencing in Malignancies

Beyond Beckwith-Wiedemann syndrome, mutations of CDKN1C are implicated in sporadic cancers, establishing the gene as a legitimate tumor suppressor candidate[1]. Comprehensive examination of hematologic malignancies has revealed that p57Kip2 expression is silenced in 30 to 55% of acute lymphoblastic leukemia (ALL), acute myelogenous leukemia (AML), and B-cell lymphoma patients[33]. This frequent silencing in hematologic malignancies, contrasted with normal expression of other CDK inhibitors in most of these same malignancies, strongly suggests a specialized role for p57Kip2 as a suppressor of hematopoietic cell transformation.

The silencing of p57Kip2 in cancer typically occurs through epigenetic mechanisms involving DNA methylation at the CDKN1C promoter region[19]. The CDKN1C promoter contains numerous CpG islands both upstream and downstream of the transcription start site that are subject to methylation-dependent transcriptional silencing[19]. This epigenetic silencing of CDKN1C plays a critical role in mediating p57 silencing in human cancers and represents a reversible mechanism that could potentially be therapeutically targeted through DNA methyltransferase inhibitors or targeted demethylation approaches.

Recent technological advances in epigenetic editing have demonstrated that targeted demethylation at the CDKN1C/p57 locus using a transcription activator-like effector (TALE) protein fused to the catalytic domain of TET1 (ICR2-TET1) can reduce p57 expression levels and increase cellular proliferation in human fibroblasts[21]. Notably, this approach identified therapeutic potential in inducing beta cell proliferation by demethylating the ICR2 at the CDKN1C locus, causing increased proliferation in human pancreatic beta cells while reducing CDKN1C expression[21]. These studies establish proof-of-concept that epigenetic editing strategies targeting CDKN1C regulatory regions represent a promising therapeutic avenue for conditions requiring increased cell proliferation, such as diabetes mellitus where insufficient beta cell mass contributes to disease pathology.

## Protein Interactions and Signaling Functions Beyond Cell Cycle Regulation

### E2F Transcription Factor Regulation and RNA Polymerase II Control

Beyond its canonical role in CDK inhibition, p57Kip2 functions in transcriptional regulation through direct interactions with transcription factors, particularly the E2F family[27]. CDKN1C binds directly to E2F1 transcription factor, and this CDKN1C-E2F1 complex negatively regulates transcription by inhibiting phosphorylation of the RNA polymerase II C-terminal domain (CTD)[27]. The CTD of RNA polymerase II contains heptapeptide repeats (consensus sequence YSPTSPS) that are subject to phosphorylation at serine residues 2 and 5, with this phosphorylation being essential for transcriptional initiation and productive elongation[27]. p57Kip2 expression leads to dramatic reduction in phosphorylation of both Ser-2 and Ser-5 of the RNA polymerase II CTD[27].

The mechanism through which p57Kip2 achieves this transcriptional repression involves direct interactions with CDK7 and CDK9, putative RNA polymerase II CTD kinases[27]. p57Kip2 can block the ability of CDK7 and CDK9 to phosphorylate glutathione S-transferase-CTD fusion protein substrates in vitro, suggesting direct inhibition of these kinases as the molecular mechanism[27]. Importantly, the CDKN1C-E2F1 interaction is mediated by two distinct E2F1 domains: a central E2F1 domain that interacts directly with CDKN1C, and a C-terminal E2F1 domain that interacts with CDKN1C via interaction with the retinoblastoma (Rb) protein[27]. This multiplicity of interaction surfaces provides multiple layers through which p57Kip2 can be recruited to E2F1-regulated promoters.

Functionally, p57Kip2-mediated repression of E2F1-driven transcription appears to constitute a negative feedback loop: E2F1 activates transcription of CDKN1C (as well as CDKN1B/p27), and the resulting p57Kip2 protein then feeds back to inhibit E2F1 transcriptional activity[27]. This negative feedback circuit likely serves to limit excessive E2F1 activity that would otherwise drive unwanted apoptosis, representing a homeostatic mechanism through which cells prevent dysregulated E2F1 transcription.

### JNK/SAPK Pathway Inhibition and Stress Response Regulation

A critical non-cell-cycle function of p57Kip2 involves direct inhibition of the c-Jun NH2-terminal kinase/stress-activated protein kinase (JNK/SAPK) pathway, a function that operates independently of CDK inhibition[26][29]. p57Kip2 physically interacts with and inhibits JNK/SAPK through a mechanism involving its QT box domain[26][29]. Specifically, p57Kip2 interacts with JNK1 via its QT-BOX domain, and this interaction precludes the interaction between JNK1 and c-Jun, thereby inhibiting JNK kinase activity[26][29]. This interaction mechanism is mechanistically distinct from the CDK inhibition pathway, as the QT box domain is entirely separate from the CDK-inhibitory domain at the N-terminus.

JNK/SAPK pathway activation is implicated in regulation of multiple cellular activities ranging from cell growth to cell death, and stress conditions that activate JNK often promote apoptotic pathways. The ability of p57Kip2 to suppress JNK signaling thus represents an important antiapoptotic mechanism in certain contexts. However, this JNK-inhibitory function can show context-dependent effects: p57Kip2-mediated JNK inhibition is associated with antiapoptotic activity and is observed in physiological contexts including embryogenesis, yet in other settings such as cancer cell responses to certain drugs, p57Kip2 overexpression can promote apoptosis through distinct mechanisms[26]. This demonstrates that cellular context profoundly determines whether p57Kip2 functions in an antiapoptotic or proapoptotic capacity.

### Myogenic Regulatory Factor Interactions

p57Kip2 interacts with myogenic regulatory factors including MyoD and MYOGENIN, with these interactions playing critical roles in skeletal muscle development and differentiation[1][14][19][23][56]. In differentiating muscle cells, MyoD regulates p57Kip2 transcription through interaction with a long-distance regulatory element located within the imprinting control region KvDMR1[56]. The induction of p57Kip2 expression during myogenic differentiation requires MyoD binding to this distant cis-element and the consequent release of a chromatin loop involving the p57Kip2 promoter[56].

In undifferentiated and unresponsive myoblasts, the p57Kip2 promoter shows epigenetic features such as DNA hypermethylation similar to those associated with imprinting, restricting accessibility to MyoD-dependent regulation[56]. Upon myogenic differentiation, MyoD is recruited to the F3 sub-region of KvDMR1, and this recruitment represents a limiting factor for p57Kip2 de-repression[56]. The three-dimensional chromatin architecture is remodeled, resulting in disruption of a chromatin loop between KvDMR1 and the p57Kip2 promoter that had been maintaining promoter repression in undifferentiated cells[56]. This release of the chromatin loop allows MyoD-dependent trans-activation of the p57Kip2 promoter through upregulation of intermediate transcription factors including p73, Sp1, and Egr1[56].

The interaction of p57Kip2 with MyoD operates bidirectionally: MyoD binding to KvDMR1 activates p57Kip2 transcription, while p57Kip2 protein, once synthesized, stabilizes MyoD protein through CDK2 inhibition and potentially enhances MyoD DNA binding through direct protein-protein interaction[23][56]. This creates an autoamplifying positive feedback loop that coordinates myogenic gene expression with cell cycle exit during terminal differentiation.

## Degradation Pathways and Post-Translational Regulation

### SCF-Skp2 and SCF-FBL12 Mediated Ubiquitination and Proteasomal Degradation

The cellular levels of p57Kip2 are tightly regulated through targeted proteolysis mediated by the proteasome, with the primary degradation pathway involving the Skp1/Cullin/F-box (SCF)-type E3 ubiquitin ligase complex SCFSkp2[19][50][53]. The degradation of p57Kip2 is mediated by phosphorylation of threonine 310 (Thr310) by cyclin E/CDK2 complexes, which creates a binding site for the F-box protein Skp2[19][50]. The SCFSkp2 complex then recognizes the phosphorylated p57Kip2 and directs it to ubiquitination through polyubiquitin chain conjugation, resulting in targeting to proteasomal degradation[19][50]. This degradation occurs in a cell cycle-dependent manner from late G1 to early M phase, with the Skp2-SCF complex activity being frequently deregulated in human cancers, contributing to loss of p57Kip2 expression in malignancies[19].

A second F-box protein, FBL12, has been identified as involved in p57Kip2 degradation through interaction with Thr310-phosphorylated p57Kip2 and mediating proteasomal degradation independently of Skp2[19][50]. The FBL12-mediated degradation pathway has been particularly characterized in osteoblasts, where transforming growth factor-beta 1 (TGFβ1) stimulates FBL12 expression that interacts with phosphorylated p57Kip2 and causes its proteasomal degradation[19]. This suggests that tissue-specific and pathway-specific signals can determine which ubiquitin ligase machinery predominates in p57Kip2 degradation in different cellular contexts.

Like other CIP/Kip family proteins, p57Kip2 is capable of promoting assembly of cyclin D1-CDK4/6 complexes in addition to its inhibitory functions on other CDK complexes, and this function is regulated by phosphorylation. The CDK inhibitory activity of p57Kip2 is regulated by phosphorylation on specific tyrosine residues that relax the inhibitory conformation of the CDK inhibitor, allowing partial CDK activation and permitting continued cell cycle progression even in the presence of p57Kip2[19]. This represents an elegant mechanism through which cells can modulate the strength of cell cycle inhibition exerted by p57Kip2 through post-translational modification.

### PCNA Interactions and DNA Replication Checkpoint Control

Beyond its roles in CDK inhibition, p57Kip2 binds to and inhibits proliferating cell nuclear antigen (PCNA), a critical cofactor of DNA polymerase delta[14][17][43]. Mutations in the PCNA-binding site of CDKN1C significantly increase p57Kip2 protein stability and prevent cell cycle progression into the S phase, demonstrating that PCNA interaction represents a functionally important domain of the protein[17]. The PCNA-binding domain allows p57Kip2 to participate in DNA replication checkpoint control, potentially preventing entry into S phase when DNA damage or replication stress is detected.

## Regulation of Expression and Signaling Inputs

### Transcriptional and Epigenetic Regulation

p57Kip2 expression is subject to regulation by multiple signaling pathways that converge on transcriptional control of the CDKN1C gene[14][19][24][57]. The transforming growth factor-beta/Smad (TGFβ/Smad) signaling pathway stimulates p57Kip2 expression in hematopoietic stem cells, mediating maintenance of HSC quiescence through this CDK inhibitor[19][24][57]. Conversely, the TGFβ pathway has been reported to induce p57Kip2 degradation in osteoblasts, indicating context- and tissue-dependent effects of the same signaling pathway on p57Kip2 expression[19].

The Wnt/β-catenin and Notch/Hes pathways are reported to reduce p57Kip2 expression in several cell types[14][19][57]. In midbrain dopaminergic neurons, Wnt1 downregulates p57Kip2 expression[19]. In lens epithelium and pancreas, Notch effector proteins suppress p57Kip2 expression, with studies in highly myopic eyes demonstrating that NOTCH2 inhibition relieves transcriptional repression of p57Kip2 (and other genes like MAF), thereby promoting lens fiber cell differentiation[39]. However, the general regulatory picture is complex and difficult to understand due to cross-talk and overlapping of different signal pathways, with sometimes contradictory effects of the same signaling pathway in different cellular contexts or developmental stages.

The DNA methyltransferase (DNMT) family of enzymes plays a critical role in regulating p57Kip2 expression through methylation of CpG islands in the CDKN1C promoter region[14][19][57]. Both DNMT1, which maintains methylation patterns during DNA replication, and DNMT3a, which is involved in de novo methylation, have been implicated in controlling CDKN1C methylation status and consequently its expression level[19][57]. The complex interplay between maintaining versus establishing DNA methylation patterns at CDKN1C represents an important mechanism through which developmental signals and cellular stress can modulate p57Kip2 expression through epigenetic mechanisms.

### Glucocorticoid Receptor-Mediated Regulation

Recent studies have identified that p57Kip2-mediated cancer cell dormancy is regulated through the activity of glucocorticoid receptors (GRs), with GR-dependent control of p57Kip2 expression occurring through chromatin remodeling mediated by SWI/SNF complexes[1]. This represents an additional layer of transcriptional regulation through which systemic hormonal signals can influence p57Kip2 expression and consequently control cell cycle progression in specific cell populations. This hormonal regulation of p57Kip2 may have therapeutic implications, as glucocorticoids have been used clinically in various contexts, and understanding their effects on p57Kip2 expression could inform clinical decision-making regarding glucocorticoid use.

## Specialized Functions in Pancreatic Beta Cell Development and Proliferation

### Role in Beta Cell Mass Regulation

p57Kip2 has emerged as a critical regulator of pancreatic beta cell proliferation and mass, with particularly important roles at the intersection of development and metabolic disease[6][21][44]. Interestingly, promoting p57Kip2 function has proven remarkably effective at targeting human beta cell proliferation, with targeted demethylation at the CDKN1C locus inducing human beta cell proliferation in both cultured pancreatic islets and in isolation[6][21]. The newly replicated beta cells retain properties of mature beta cells, including expression of beta cell markers such as insulin, PDX1, and NKX6.1[6].

The therapeutic potential of modulating p57Kip2 lies in addressing a fundamental limitation of diabetes treatment: the proliferative capacity of human beta cells declines dramatically after early childhood, correlating with age-related accumulation of the senescence effector p16 that induces cell cycle arrest in beta cells[21]. This loss of proliferative capacity limits the potential for beta cell regeneration in response to metabolic demands or beta cell loss from autoimmune destruction. The observation that CDKN1C-associated overgrowth disorder Beckwith-Wiedemann syndrome is characterized by an expansion of beta cell mass in addition to other tissue types that is associated with decreased protein levels of p57Kip2 provides a clinical example of how p57Kip2 downregulation drives beta cell expansion[21].

### Domain-Specific Requirements for Beta Cell Function

Structure-function analysis of p57Kip2 in human pancreatic beta cells has revealed that the protein contains a classical bipartite nuclear localization sequence characterized by two clusters of positively charged amino acids (lysine and arginine) separated by a proline-rich linker region[44]. Variants in the sequences encoding these two NLS sequences account for functional p57Kip2 loss and beta cell expansion seen in human disease[44]. This structure-function relationship has been dissected through adenoviral expression of mutant p57Kip2 constructs lacking individual functional domains (the PAPA domain, the CDK inhibitory domain, the PCNA domain, or the NLS) in isolated human pancreatic islets[44].

These studies have identified that the CDKI domain, PCNA domain, and both NLS sequences contribute to the ability of p57Kip2 to suppress beta cell proliferation[44]. Removal of any of these domains substantially diminishes or abolishes the beta cell growth-suppressive function of p57Kip2, indicating that all contribute to its full biological activity in this context[44]. The requirement for both NLS sequences suggests that the bipartite NLS structure provides robust nuclear import necessary for efficient beta cell growth suppression, perhaps reflecting the high transcriptional activity and proliferative capacity of these cells.

## Subcellular Localization and Signaling Specificity

### Mitochondrial Localization and Apoptosis Regulation

In addition to its canonical nuclear localization where it functions as a CDK inhibitor, p57Kip2 can relocate to mitochondrial membranes under specific stress conditions, particularly in response to apoptotic stimuli[26]. Upon treatment with staurosporine (a protein kinase inhibitor that triggers apoptosis), p57Kip2 rapidly translocates to mitochondrial membranes within minutes and promotes Bax activation and decrease of mitochondrial membrane potential, resulting in cytochrome c release into the cytosol and consequent activation of the intrinsic apoptotic pathway through caspases 9 and 3[26]. This mitochondrial pathway specificity was confirmed experimentally, as p57Kip2 expression proved ineffective in promoting death receptor-mediated apoptosis stimulated with agonistic anti-FAS antibodies[26].

The mechanism by which p57Kip2 triggers the mitochondrial intrinsic apoptotic pathway has been linked to its ability to stabilize the actin cytoskeleton through direct interaction with LIM domain kinase-1 (LIMK-1)[26]. p57Kip2 interacts directly with LIMK-1, resulting in increased LIMK-1 kinase activity[26]. LIMK-1 is known to inactivate the cytoskeleton remodeling factor cofilin, which is involved in disassembling actin filaments, so increased LIMK-1 activity stabilizes the actin cytoskeleton[26]. It has been hypothesized that stabilization of the actin cytoskeleton can promote apoptotic cell death through mechanisms that may involve facilitating communication between the cytoskeleton and apoptotic machinery at mitochondrial membranes[26].

### Context-Dependent Apoptotic Functions

The proapoptotic effects of p57Kip2 are observed particularly in cancer cells after p57Kip2 overexpression or reinduction, and can contrast sharply with its antiapoptotic activity observed during physiological regulation of JNK/SAPK pathway activity and during embryogenesis[26]. This context-dependency emphasizes an important principle about p57Kip2 function: the same protein can exert dramatically different biological effects depending on cellular context, expression level, subcellular localization, and interaction with various regulatory proteins and signaling cascades. In cancer cells facing metabolic stress or drug-induced damage, p57Kip2 can promote apoptosis, whereas in normal developing tissues, p57Kip2 often promotes differentiation without triggering cell death[26].

## Conclusion and Future Perspectives

CDKN1C encoding p57Kip2 has emerged as a paradigmatic multifunctional tumor suppressor protein that operates through both canonical cell cycle regulatory mechanisms and context-dependent signaling pathways to control cellular proliferation, differentiation, stress responses, and apoptosis. The protein's function depends critically on sophisticated regulation of subcellular localization, protein degradation, post-translational modification, and dynamic interactions with transcription factors and signaling machinery. The tissue-specific expression patterns and developmental regulation of p57Kip2 reflect its essential roles in orchestrating cell cycle exit during differentiation in multiple tissue lineages, from skeletal muscle and neural tissue to placental trophoblasts and pancreatic beta cells.

The substantial gaps in understanding p57Kip2 biology that remain—including the precise mechanisms controlling its subcellular trafficking between cytoplasm and nucleus, the functional significance of the unique PAPA domain found only in human p57Kip2, and the full spectrum of protein-protein interactions through which p57Kip2 exerts its diverse biological functions—represent important areas for continued investigation. Recent technological advances in epigenetic editing, structural biology, and systems-level analysis of protein interactions offer unprecedented opportunities to illuminate these remaining questions and to develop novel therapeutic approaches targeting p57Kip2 function for treatment of both overgrowth disorders and cancer.

## Citations

1. https://en.wikipedia.org/wiki/Cyclin-dependent_kinase_inhibitor_1C
2. https://www.ncbi.nlm.nih.gov/gene/1028
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC1885689/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC1891291/
5. https://www.orpha.net/en/disease/gene/CDKN1C
6. https://www.jci.org/articles/32031
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC6172026/
8. https://en.wikipedia.org/wiki/Cyclin-dependent_kinase_inhibitor_protein
9. https://pubmed.ncbi.nlm.nih.gov/26077438/
10. https://elifesciences.org/articles/33337/peer-reviews
11. https://www.nature.com/articles/s41439-025-00316-0
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC2643088/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5979523/
14. https://www.nature.com/articles/1200851
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4389716/
16. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2020.584590/full
17. https://elifesciences.org/articles/33337
18. https://www.jci.org/articles/view/99170
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC2967216/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC3044464/
21. https://www.nature.com/articles/s41467-021-23612-z
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC4600511/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC2843230/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC9048628/
25. https://pubmed.ncbi.nlm.nih.gov/12963725/
26. https://www.embopress.org/doi/10.15252/embj.2019103421
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC7863277/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC5538190/
29. https://ashpublications.org/blood/article/116/21/3162/66079/CDKN1C-Modulates-the-Stress-Reponse-of
30. https://www.nature.com/articles/pr2007130
31. https://www.cambridge.org/core/journals/fetal-and-maternal-medicine-review/article/insulinlike-growth-factors-and-placental-function/50A26263DCA7347715D274AA393510F8
32. https://www.pnas.org/doi/10.1073/pnas.2311372120
33. https://www.nature.com/articles/cdd200972
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC10392066/
35. https://pubmed.ncbi.nlm.nih.gov/26988311/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC3616292/
37. https://stemcellsjournals.onlinelibrary.wiley.com/doi/10.1002/stem.602
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC11491829/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC8305445/
40. https://genesdev.cshlp.org/content/9/6/650.full.pdf
41. https://www.pnas.org/doi/abs/10.1073/pnas.1831009100
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8348313/
43. https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.63777
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC193544/
45. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.693104/full
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC10542123/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC3458561/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC1283108/
49. https://pubmed.ncbi.nlm.nih.gov/30352048/